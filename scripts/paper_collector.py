#!/usr/bin/env python3
"""
Scholar Paper Collector & Figure Extractor (v2)
------------------------------------------------
自动化收集目标学者的代表作，提取核心插图、LaTeX 源码与「风格燃料」语料。

支持：
1. --arxiv id1,id2,...   批量下载 PDF 与源码包（自动剥离 vN 版本号，请求间限速 3 秒）。
2. --author "姓名" --max-results N   通过 arXiv API 检索作者近期论文，生成 papers_index.json 并批量下载。
3. 安全解压源码包（防路径穿越；Python 3.12+ 用 filter="data"，低版本手动检查 member 路径），
   并兼容单文件 gzip 与纯 .tex 的非 tar 源码包。
4. 解析全部 .tex 文件，生成 <id>_corpus_report.md（蒸馏分析的核心燃料）：
   - \\definecolor{name}{model}{spec} 全部出现位置（文件:行号 + 完整行）
   - figure/table 环境内的 \\caption{...} 全文（支持跨多行与嵌套花括号，做花括号配平）
   - Abstract 全文（\\begin{abstract}...\\end{abstract}）
   - \\section / \\subsection / \\subsubsection 章节树
   - \\includegraphics 引用的图片文件名清单
5. 可选 PyMuPDF (fitz)：从 PDF 中提取全部位图图片；未安装时打印提示并跳过，不报错退出。

仅用标准库 + 可选 PyMuPDF。
"""

import os
import re
import sys
import json
import gzip
import time
import tarfile
import argparse
import http.client
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

ARXIV_API = "http://export.arxiv.org/api/query"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) scholar-style-distiller/2.0"
REQUEST_INTERVAL = 3.0  # arXiv 官方限速：相邻请求至少间隔 3 秒

_last_request_time = [0.0]  # 上次 HTTP 请求的时间戳（模块级节流器）


# ---------------------------------------------------------------------------
# 网络层：限速 + 下载
# ---------------------------------------------------------------------------

def _throttle():
    """请求限速：保证相邻两次 HTTP 请求间隔不少于 REQUEST_INTERVAL 秒。"""
    elapsed = time.time() - _last_request_time[0]
    if elapsed < REQUEST_INTERVAL:
        wait = REQUEST_INTERVAL - elapsed
        print(f"[*] arXiv 限速，等待 {wait:.1f} 秒...")
        time.sleep(wait)
    _last_request_time[0] = time.time()


def http_get(url: str, retries: int = 2, max_resume: int = 10) -> bytes:
    """带限速与 UA 的 HTTP GET，返回原始字节。

    - arXiv 高频访问下偶发 406/429 等瞬时风控：对 406/429/5xx 做线性退避重试；
    - 大文件偶发被 CDN 中途断流（IncompleteRead）：改用 Range 头从已收字节处
      断点续传，最多续传 max_resume 次，避免单篇超大源码包无限卡死整个批次。
    """
    data = b''
    retries_left = retries
    resume_left = max_resume
    while True:
        _throttle()
        headers = {'User-Agent': USER_AGENT}
        if data:
            headers['Range'] = f'bytes={len(data)}-'
        req = urllib.request.Request(url, headers=headers)
        try:
            resp = urllib.request.urlopen(req, timeout=180)
        except urllib.error.HTTPError as e:
            # 瞬时风控/服务端错误：线性退避后重试（已收到的断点进度保留）
            if e.code in (406, 429, 500, 502, 503) and retries_left > 0:
                retries_left -= 1
                wait = 5 * (retries - retries_left)
                print(f"[!] HTTP {e.code}（arXiv 瞬时风控），{wait} 秒后重试（剩余 {retries_left} 次）...")
                time.sleep(wait)
                continue
            raise
        except Exception as e:
            if retries_left > 0:
                retries_left -= 1
                wait = 5 * (retries - retries_left)
                print(f"[!] 请求失败: {e}，{wait} 秒后重试（剩余 {retries_left} 次）...")
                time.sleep(wait)
                continue
            raise

        status = getattr(resp, 'status', 200)
        try:
            chunk = resp.read()
            complete = True
        except http.client.IncompleteRead as e:
            chunk = e.partial or b''
            complete = False
        finally:
            resp.close()

        if status != 206:
            data = b''  # 服务端忽略 Range 返回全量，丢弃旧进度从头算
        data += chunk
        if complete:
            return data

        # 传输中断：有进展就继续断点续传，否则走普通重试
        if chunk and resume_left > 0:
            resume_left -= 1
            print(f"[!] 传输中断（已收 {len(data) / 1048576:.1f} MB），断点续传（剩余 {resume_left} 次）...")
            continue
        if retries_left > 0:
            retries_left -= 1
            print(f"[!] 传输中断且断点续传次数用尽，{5} 秒后整体重试（剩余 {retries_left} 次）...")
            data = b''
            time.sleep(5)
            continue
        raise http.client.IncompleteRead(data)


def clean_arxiv_id(arxiv_id: str) -> str:
    """剥离 vN 版本号与首尾空白，返回干净的 ArXiv ID。"""
    return re.sub(r'v\d+$', '', arxiv_id.strip())


# ---------------------------------------------------------------------------
# 下载：PDF 与源码包
# ---------------------------------------------------------------------------

def download_arxiv_pdf(clean_id: str, output_dir: str):
    """下载指定 ArXiv 论文的 PDF 文件。

    首选官方模板 https://arxiv.org/pdf/<id>.pdf；该地址会 301 到不带后缀的
    canonical 地址，偶发触发 arXiv 风控返回 406，因此失败时自动回退到不带
    .pdf 后缀的地址再试一次。
    """
    os.makedirs(output_dir, exist_ok=True)
    pdf_path = os.path.join(output_dir, f"{clean_id}.pdf")

    # 断点续采：已存在且非空的 PDF 直接跳过，避免批量重跑时重复下载
    if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
        print(f"[*] PDF 已存在，跳过下载: {pdf_path}")
        return pdf_path

    for url in (f"https://arxiv.org/pdf/{clean_id}.pdf", f"https://arxiv.org/pdf/{clean_id}"):
        print(f"[*] 正在下载 PDF: {url} -> {pdf_path}")
        try:
            data = http_get(url)
            with open(pdf_path, 'wb') as out_f:
                out_f.write(data)
            print(f"[+] PDF 保存至: {pdf_path}（{len(data) / 1024:.0f} KB）")
            return pdf_path
        except Exception as e:
            print(f"[-] PDF 下载失败（{url}）: {e}")
    return None


def download_arxiv_source(clean_id: str, output_dir: str):
    """下载 ArXiv 原始源码包（含 .tex 与矢量图源文件，是学习排版和作图的最佳资料）。

    依次尝试多个端点：/src/（现行 canonical 地址，/e-print 已 301 至此且
    风控更敏感）、旧版 /e-print、export 镜像，任一成功即返回。
    """
    urls = [
        f"https://arxiv.org/src/{clean_id}",
        f"https://arxiv.org/e-print/{clean_id}",
        f"https://export.arxiv.org/src/{clean_id}",
    ]
    os.makedirs(output_dir, exist_ok=True)
    tar_path = os.path.join(output_dir, f"{clean_id}_source.tar.gz")

    # 断点续采：已存在且非空的源码包直接跳过
    if os.path.exists(tar_path) and os.path.getsize(tar_path) > 0:
        print(f"[*] 源码包已存在，跳过下载: {tar_path}")
        return tar_path

    for url in urls:
        print(f"[*] 正在下载 ArXiv 源码包: {url} -> {tar_path}")
        try:
            data = http_get(url)
            with open(tar_path, 'wb') as out_f:
                out_f.write(data)
            print(f"[+] 源码包下载完成（{len(data) / 1024:.0f} KB）")
            return tar_path
        except Exception as e:
            print(f"[-] 源码包下载失败（{url}）: {e}")
    return None


# ---------------------------------------------------------------------------
# 解压：防路径穿越，兼容 tar / 单文件 gzip / 纯 tex
# ---------------------------------------------------------------------------

def _is_safe_member(name: str) -> bool:
    """检查 tar member 路径是否安全：非绝对路径且不含 '..' 段（防路径穿越）。"""
    if os.path.isabs(name) or name.startswith('/'):
        return False
    parts = re.split(r'[/\\]', name)
    return '..' not in parts


def extract_source_safely(tar_path: str, extract_dir: str):
    """
    安全解压源码包，返回解压目录；失败返回 None。
    - Python 3.12+：tarfile.extractall(filter="data")，自动剥离危险路径与特殊文件；
    - 低版本：手动检查每个 member 的路径不含 ".." 且不是绝对路径；
    - 非 tar 源码包（单文件 .gz 或纯 .tex）：优雅降级处理。
    """
    os.makedirs(extract_dir, exist_ok=True)

    # 1) 标准 tar / tar.gz 源码包
    if tarfile.is_tarfile(tar_path):
        try:
            with tarfile.open(tar_path, "r:*") as tar:
                if sys.version_info >= (3, 12):
                    tar.extractall(path=extract_dir, filter="data")
                else:
                    for member in tar.getmembers():
                        if not _is_safe_member(member.name):
                            raise tarfile.TarError(f"检测到可疑路径，已中止解压: {member.name}")
                    tar.extractall(path=extract_dir)
            print(f"[+] 源码已安全解压至: {extract_dir}")
            return extract_dir
        except Exception as e:
            print(f"[-] tar 解压失败: {e}")
            return None

    # 2) 单文件 gzip（常见于只有单个 .tex 的老论文）
    try:
        with gzip.open(tar_path, 'rb') as gz:
            data = gz.read()
        out_path = os.path.join(extract_dir, "main.tex")
        with open(out_path, 'wb') as f:
            f.write(data)
        print(f"[+] 源码包为单文件 gzip，已解压为: {out_path}")
        return extract_dir
    except Exception:
        pass

    # 3) 纯文本 .tex（少数 e-print 直接返回未压缩的 tex）
    try:
        with open(tar_path, 'rb') as f:
            data = f.read()
        data.decode('utf-8')  # 仅校验是否为文本
        out_path = os.path.join(extract_dir, "main.tex")
        with open(out_path, 'wb') as f:
            f.write(data)
        print(f"[+] 源码包为纯 .tex 文本，已保存为: {out_path}")
        return extract_dir
    except Exception:
        pass

    print("[!] 无法识别的源码包格式（非 tar / 非 gzip / 非纯 tex），跳过解压。")
    return None


# ---------------------------------------------------------------------------
# TeX 解析：蒸馏风格燃料
# ---------------------------------------------------------------------------

def _brace_balance(text: str, open_pos: int) -> int:
    """
    从 text[open_pos] == '{' 开始做花括号配平，返回与之匹配的 '}' 的下标；未配平返回 -1。
    正确处理 \\{、\\} 等转义序列（caption 里经常含嵌套花括号与换行，单行正则抓不住）。
    """
    depth = 0
    i = open_pos
    while i < len(text):
        ch = text[i]
        if ch == '\\':
            i += 2  # 跳过整个转义序列（如 \{ \% \\）
            continue
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def _line_no(text: str, pos: int) -> int:
    """返回 text 中字符下标 pos 所在的 1-based 行号。"""
    return text.count('\n', 0, pos) + 1


def find_definecolors(text: str, rel_path: str):
    """提取全部 \\definecolor{name}{model}{spec}，记录 文件:行号 + 完整行。"""
    results = []
    pattern = re.compile(r'\\definecolor\{[^}]*\}\{[^}]*\}\{[^}]*\}')
    for lineno, line in enumerate(text.splitlines(), start=1):
        if pattern.search(line):
            results.append({'file': rel_path, 'line': lineno, 'text': line.strip()})
    return results


def find_captions(text: str, rel_path: str):
    """
    提取 figure/table 环境内的全部 \\caption{...} 全文。
    caption 经常跨多行且含嵌套花括号（如 \\caption{... \\textbf{...} ...}），
    因此先定位 \\begin{figure|table}...\\end{...} 区间，再在区间内做花括号配平提取。
    """
    results = []
    env_re = re.compile(r'\\begin\{((?:figure|table)\*?)\}(.*?)\\end\{\1\}', re.DOTALL)
    for env_m in env_re.finditer(text):
        env_type, body = env_m.group(1), env_m.group(2)
        for cap_m in re.finditer(r'\\caption\b', body):
            # caption 可能带可选参数 \caption[短标题]{长标题}，直接找其后第一个 '{'
            brace_pos = body.find('{', cap_m.end())
            if brace_pos == -1:
                continue
            end = _brace_balance(body, brace_pos)
            if end == -1:
                continue
            content = body[brace_pos + 1:end].strip()
            abs_pos = env_m.start(2) + brace_pos
            results.append({
                'file': rel_path,
                'line': _line_no(text, abs_pos),
                'env': env_type,
                'content': content,
            })
    return results


def find_abstract(text: str):
    """提取 \\begin{abstract}...\\end{abstract} 之间的 Abstract 全文。"""
    m = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', text, re.DOTALL)
    return m.group(1).strip() if m else None


def find_sections(text: str, rel_path: str):
    """提取 \\section / \\subsection / \\subsubsection 标题（含星号变体），用于章节树。"""
    results = []
    sec_re = re.compile(r'\\(section|subsection|subsubsection)\*?\{')
    for m in sec_re.finditer(text):
        brace_pos = m.end() - 1
        end = _brace_balance(text, brace_pos)
        if end == -1:
            continue
        results.append({
            'file': rel_path,
            'line': _line_no(text, m.start()),
            'level': m.group(1),
            'title': text[brace_pos + 1:end].strip(),
        })
    return results


def find_includegraphics(text: str, rel_path: str):
    """提取全部 \\includegraphics 引用的图片文件名清单。"""
    results = []
    img_re = re.compile(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}')
    for m in img_re.finditer(text):
        results.append({
            'file': rel_path,
            'line': _line_no(text, m.start()),
            'image': m.group(1).strip(),
        })
    return results


def _iter_tex_files(extract_dir: str):
    """递归收集解压目录下的全部 .tex 文件（按路径排序）。"""
    tex_files = []
    for root, _, files in os.walk(extract_dir):
        for fn in files:
            if fn.lower().endswith('.tex'):
                tex_files.append(os.path.join(root, fn))
    return sorted(tex_files)


def generate_corpus_report(clean_id: str, extract_dir: str, output_dir: str):
    """
    扫描解压目录下所有 .tex 文件，汇总风格燃料，生成 <id>_corpus_report.md。
    """
    tex_files = _iter_tex_files(extract_dir)
    if not tex_files:
        print(f"[!] {extract_dir} 中未找到 .tex 文件，跳过语料报告。")
        return None

    all_colors, all_captions, all_sections, all_images = [], [], [], []
    abstract = None
    for tex_path in tex_files:
        rel_path = os.path.relpath(tex_path, extract_dir)
        try:
            with open(tex_path, 'r', encoding='utf-8', errors='ignore') as f:
                text = f.read()
        except Exception as e:
            print(f"[-] 读取 {rel_path} 失败: {e}")
            continue
        all_colors.extend(find_definecolors(text, rel_path))
        all_captions.extend(find_captions(text, rel_path))
        all_sections.extend(find_sections(text, rel_path))
        all_images.extend(find_includegraphics(text, rel_path))
        if abstract is None:
            abstract = find_abstract(text)

    # 章节树按层级缩进
    level_indent = {'section': 0, 'subsection': 1, 'subsubsection': 2}
    section_lines = [
        f"{'  ' * level_indent.get(s['level'], 0)}- [{s['level']}] {s['title']}（{s['file']}:{s['line']}）"
        for s in all_sections
    ]

    report = []
    report.append(f"# Corpus Report: arXiv {clean_id}\n")
    report.append(f"- 扫描 .tex 文件数：{len(tex_files)}")
    report.append(f"- \\definecolor 配色定义：{len(all_colors)} 处")
    report.append(f"- figure/table caption：{len(all_captions)} 条")
    report.append(f"- section 节点：{len(all_sections)} 个")
    report.append(f"- \\includegraphics 引用：{len(all_images)} 处\n")

    report.append("## 1. 配色定义（\\definecolor）\n")
    if all_colors:
        for c in all_colors:
            report.append(f"- `{c['file']}:{c['line']}` — `{c['text']}`")
    else:
        report.append("（未找到）")
    report.append("")

    report.append("## 2. 图注/表注（figure/table 环境的 \\caption）\n")
    if all_captions:
        for cap in all_captions:
            content = re.sub(r'\s+', ' ', cap['content'])  # 折叠换行，便于阅读
            report.append(f"### [{cap['env']}] `{cap['file']}:{cap['line']}`\n")
            report.append(f"> {content}\n")
    else:
        report.append("（未找到）\n")

    report.append("## 3. Abstract 全文\n")
    report.append(abstract if abstract else "（未找到）")
    report.append("")

    report.append("## 4. 章节树（\\section）\n")
    report.extend(section_lines if section_lines else ["（未找到）"])
    report.append("")

    report.append("## 5. 图片引用清单（\\includegraphics）\n")
    if all_images:
        for img in all_images:
            report.append(f"- `{img['image']}`（{img['file']}:{img['line']}）")
    else:
        report.append("（未找到）")
    report.append("")

    report_path = os.path.join(output_dir, f"{clean_id}_corpus_report.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    print(f"[+] 语料报告已生成: {report_path}（配色 {len(all_colors)} / caption {len(all_captions)} / section {len(all_sections)} / 图片 {len(all_images)}）")
    return report_path


# ---------------------------------------------------------------------------
# PDF 图片提取（可选 PyMuPDF）
# ---------------------------------------------------------------------------

def extract_figures_from_pdf(pdf_path: str, output_dir: str):
    """使用 PyMuPDF (fitz) 提取 PDF 中的全部插图；未安装时仅提示并跳过。"""
    try:
        import fitz  # PyMuPDF
    except ImportError:
        print("[!] 未检测到 PyMuPDF (fitz)，跳过 PDF 图片提取。建议运行: pip install pymupdf")
        print("    或者直接通过解压 ArXiv 源码包获取所有高清原始图片！")
        return []

    doc = fitz.open(pdf_path)
    extracted_images = []
    stem = os.path.splitext(os.path.basename(pdf_path))[0]
    figures_dir = os.path.join(output_dir, f"{stem}_figures")
    os.makedirs(figures_dir, exist_ok=True)

    for page_idx, page in enumerate(doc):
        image_list = page.get_images(full=True)
        for img_idx, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            img_filename = f"page_{page_idx+1}_img_{img_idx+1}.{image_ext}"
            img_filepath = os.path.join(figures_dir, img_filename)
            with open(img_filepath, "wb") as f:
                f.write(image_bytes)
            extracted_images.append(img_filepath)

    print(f"[+] 从 PDF 成功提取了 {len(extracted_images)} 张图片至 {figures_dir}")
    return extracted_images


# ---------------------------------------------------------------------------
# 作者检索：arXiv API + Atom XML 解析
# ---------------------------------------------------------------------------

def search_author_papers(author: str, max_results: int):
    """
    调用 arXiv API 检索作者近期论文，用标准库 ElementTree 解析 Atom XML。
    返回 [{id, year, title, authors, url}] 列表。
    """
    params = {
        'search_query': f'au:"{author}"',
        'sortBy': 'submittedDate',
        'sortOrder': 'descending',
        'max_results': str(max_results),
    }
    url = ARXIV_API + '?' + urllib.parse.urlencode(params)
    print(f"[*] 正在检索作者论文: {url}")
    data = http_get(url)

    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    root = ET.fromstring(data)
    papers = []
    for entry in root.findall('atom:entry', ns):
        entry_url = (entry.findtext('atom:id', default='', namespaces=ns) or '').strip()
        raw_id = entry_url.rsplit('/', 1)[-1] if entry_url else ''
        arxiv_id = clean_arxiv_id(raw_id)
        title = ' '.join((entry.findtext('atom:title', default='', namespaces=ns) or '').split())
        published = entry.findtext('atom:published', default='', namespaces=ns) or ''
        authors = [
            (a.findtext('atom:name', default='', namespaces=ns) or '').strip()
            for a in entry.findall('atom:author', ns)
        ]
        papers.append({
            'id': arxiv_id,
            'year': published[:4],
            'title': title,
            'authors': authors,
            'url': entry_url,
        })
    return papers


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------

def collect_paper(arxiv_id: str, output_dir: str):
    """对单个 ArXiv ID 执行完整采集：PDF + 源码下载、安全解压、语料报告、PDF 图片提取。"""
    clean_id = clean_arxiv_id(arxiv_id)
    print(f"\n=== 开始处理论文: {clean_id} ===")
    tar_path = download_arxiv_source(clean_id, output_dir)
    pdf_path = download_arxiv_pdf(clean_id, output_dir)
    if tar_path:
        extract_dir = os.path.join(output_dir, f"{clean_id}_extracted")
        if extract_source_safely(tar_path, extract_dir):
            generate_corpus_report(clean_id, extract_dir, output_dir)
    if pdf_path:
        extract_figures_from_pdf(pdf_path, output_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scholar Paper & Figure Collector (v2)")
    parser.add_argument("--arxiv", type=str,
                        help="逗号分隔的 ArXiv ID 列表（兼容 vN 版本号，例如 2111.06377,1502.01852v3）")
    parser.add_argument("--author", type=str,
                        help="学者姓名（例如 \"Kaiming He\"），通过 arXiv API 检索其近期论文并批量下载")
    parser.add_argument("--max-results", type=int, default=5,
                        help="--author 模式下最多检索的论文数（默认 5）")
    parser.add_argument("--output", type=str, default="./scholar_data", help="输出保存路径")
    args = parser.parse_args()

    if args.author:
        print(f"=== 检索作者: {args.author}（最近 {args.max_results} 篇）===")
        try:
            papers = search_author_papers(args.author, args.max_results)
        except Exception as e:
            print(f"[-] 作者检索失败: {e}")
            sys.exit(1)
        if not papers:
            print(f"[!] 未检索到 {args.author} 的论文。")
            sys.exit(0)

        # 打印论文列表并保存索引
        print(f"[+] 检索到 {len(papers)} 篇论文:")
        for i, p in enumerate(papers, start=1):
            print(f"    {i}. [{p['id']}] ({p['year']}) {p['title']}")
            print(f"       作者: {', '.join(p['authors'])}")
        os.makedirs(args.output, exist_ok=True)
        index_path = os.path.join(args.output, "papers_index.json")
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump({'author': args.author, 'papers': papers}, f, ensure_ascii=False, indent=2)
        print(f"[+] 论文索引已保存: {index_path}")

        # 对每篇执行同样的 PDF + 源码下载
        for p in papers:
            collect_paper(p['id'], args.output)

    elif args.arxiv:
        ids = [s.strip() for s in args.arxiv.split(',') if s.strip()]
        print(f"=== 批量处理 {len(ids)} 个 ArXiv ID: {ids} ===")
        for arxiv_id in ids:
            collect_paper(arxiv_id, args.output)

    else:
        print("用法示例:")
        print("  python paper_collector.py --arxiv 2111.06377,1502.01852 --output ./papers/kaiming_he")
        print("  python paper_collector.py --author \"Kaiming He\" --max-results 5 --output ./papers/kaiming_he")

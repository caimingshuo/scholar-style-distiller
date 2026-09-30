#!/usr/bin/env python3
"""
Academic Publication Plot Style Generator
------------------------------------------
提供顶级学者级别的 Matplotlib 绘图配置与示例脚本。
特点：
1. 字体与排版严格匹配出版级标准（Serif / Times）。
2. 配色采用低饱和度、高辨识度的顶会推荐色系（支持多种学者风格）。
3. 隐藏冗余边框（Spines），精细虚线网格，高信息密度。
4. 支持 --from-profile 直接读取蒸馏出的学者档案（profile.md），
   从「调色板」章节提取十六进制色值，形成 蒸馏 -> 绘图 的闭环。

用法示例：
    # 内置色板
    python3 plot_style_template.py --palette morandi --output out.png
    # 由学者档案驱动（优先于 --palette）
    python3 plot_style_template.py --from-profile ../examples/kaiming_he_profile.md --output out.pdf
"""

import argparse
import re
import sys

try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("[!] 运行此绘图脚本需要安装 matplotlib 和 numpy:")
    print("    pip install matplotlib numpy")
    sys.exit(0)

# 常用顶会经典配色字典
PALETTES = {
    "kaiming_blue": {
        "ours": "#1F77B4",        # 科技蓝 (Ours)
        "baseline1": "#FF7F0E",   # 复古橙
        "baseline2": "#2CA02C",   # 沉稳绿
        "gray": "#7F7F7F",        # 中性灰
        "light_gray": "#E0E0E0"
    },
    "nature_teal": {
        "ours": "#2A9D8F",        # 优雅孔雀青
        "baseline1": "#E76F51",   # 陶土红
        "baseline2": "#F4A261",   # 暖沙金
        "gray": "#4A5568",
        "light_gray": "#EDF2F7"
    },
    "morandi": {
        "ours": "#4A6FA5",        # 莫兰迪灰蓝
        "baseline1": "#B85B5B",   # 莫兰迪干枯玫瑰
        "baseline2": "#6C8E74",   # 莫兰迪浅草绿
        "gray": "#7F7F7F",        # 中性灰
        "light_gray": "#E0E0E0"
    }
}

# 从档案中提取的色值按出现顺序依次映射到这些角色
PROFILE_COLOR_ROLES = ["ours", "baseline1", "baseline2", "gray"]

# 匹配十六进制色值，如 #1F77B4
HEX_COLOR_RE = re.compile(r"#[0-9A-Fa-f]{6}\b")
# 匹配 Markdown 标题行
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
# 「调色板」章节的标题/段落特征
PALETTE_SECTION_RE = re.compile(r"调色板|Palette", re.IGNORECASE)


def extract_palette_from_profile(profile_path):
    """
    从学者档案 markdown 中解析调色板：
    1. 定位含「调色板」或「Palette」的标题段落，取该标题到下一个同级（或更高级）标题之间的文本；
       若调色板写在普通段落/列表行中（无独立标题），则取该行所在段落的文本。
    2. 用正则按出现顺序提取所有 #RRGGBB 色值（去重，保持顺序）。
    3. 依次映射为 ours / baseline1 / baseline2 / gray，缺失的角色用 kaiming_blue 色板补足。
    提取不到任何色值时返回 None，由调用方回退。
    """
    try:
        with open(profile_path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
    except OSError as e:
        print(f"[!] 无法读取学者档案 {profile_path}: {e}")
        return None

    # 第一步：定位调色板章节
    section_lines = []
    for i, line in enumerate(lines):
        if not PALETTE_SECTION_RE.search(line):
            continue
        heading = HEADING_RE.match(line)
        if heading:
            # 情况 A：调色板是独立标题 -> 截取到下一个同级或更高级标题
            level = len(heading.group(1))
            for follow in lines[i + 1:]:
                follow_heading = HEADING_RE.match(follow)
                if follow_heading and len(follow_heading.group(1)) <= level:
                    break
                section_lines.append(follow)
        else:
            # 情况 B：调色板写在普通段落/列表行 -> 截取该段（到空行或下一标题为止）
            for follow in lines[i:]:
                if section_lines and (not follow.strip() or HEADING_RE.match(follow)):
                    break
                section_lines.append(follow)
        break  # 只取第一个命中的调色板章节

    # 第二步：按出现顺序提取色值（去重，避免档案中重复引用同一色值污染角色映射）
    hex_colors = []
    for hex_color in HEX_COLOR_RE.findall("\n".join(section_lines)):
        hex_color = hex_color.upper()
        if hex_color not in hex_colors:
            hex_colors.append(hex_color)

    if not hex_colors:
        print(f"[!] 在 {profile_path} 的「调色板」章节中未找到任何 #RRGGBB 色值")
        return None

    # 第三步：按顺序映射角色，缺失项用 kaiming_blue 补足
    colors = dict(PALETTES["kaiming_blue"])
    mapping = {}
    for role, hex_color in zip(PROFILE_COLOR_ROLES, hex_colors):
        colors[role] = hex_color
        mapping[role] = hex_color

    print(f"[+] 已从学者档案解析调色板 ({profile_path}):")
    for role in PROFILE_COLOR_ROLES:
        print(f"    {role:<10} -> {colors[role]}" + ("" if role in mapping else "  (档案未提供，沿用 kaiming_blue 默认)"))
    if len(hex_colors) > len(PROFILE_COLOR_ROLES):
        print(f"    (档案中还有 {len(hex_colors) - len(PROFILE_COLOR_ROLES)} 个色值未映射: {hex_colors[len(PROFILE_COLOR_ROLES):]})")
    return colors


def apply_scholar_style():
    """
    全局配置 Matplotlib 样式为顶会期刊出版级标准
    """
    # 字体与排版设置
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Times New Roman', 'DejaVu Serif', 'Computer Modern Roman'],
        'font.size': 11,
        'axes.labelsize': 12,
        'axes.titlesize': 13,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 10,
        'legend.frameon': True,
        'legend.framealpha': 0.9,
        'legend.edgecolor': 'none',
        'axes.linewidth': 1.0,
        'grid.linestyle': '--',
        'grid.alpha': 0.5,
        'grid.color': '#CBCBCB',
        'savefig.dpi': 300,
        'savefig.bbox': 'tight'
    })


def resolve_palette(palette_name="kaiming_blue", from_profile=None):
    """
    决定本次绘图使用的色板：--from-profile 优先于 --palette；
    档案解析失败时回退到 kaiming_blue 并打印提示。
    """
    if from_profile:
        colors = extract_palette_from_profile(from_profile)
        if colors is not None:
            return colors
        print(f"[!] 学者档案解析失败，回退到内置 kaiming_blue 色板")
    return PALETTES.get(palette_name, PALETTES["kaiming_blue"])


def generate_sample_plot(output_path="scholar_benchmark_plot.pdf",
                         palette_name="kaiming_blue", from_profile=None):
    apply_scholar_style()
    colors = resolve_palette(palette_name, from_profile)

    # 固定随机种子，保证示例图完全可复现
    np.random.seed(42)

    # 模拟一个典型的 Accuracy vs Compute 曲线
    epochs = np.linspace(1, 100, 20)
    baseline_acc = 70 + 15 * (1 - np.exp(-epochs / 25)) + np.random.normal(0, 0.4, 20)
    ours_acc = 74 + 17 * (1 - np.exp(-epochs / 18)) + np.random.normal(0, 0.3, 20)

    fig, ax = plt.subplots(figsize=(6, 4.2))

    # Baseline: 细线、常规标记
    ax.plot(epochs, baseline_acc, label="Standard Baseline", color=colors["gray"],
            linestyle="--", marker="s", markersize=5, linewidth=1.8, alpha=0.8)

    # Ours: 粗线、醒目主色、大标记（用 fontweight 强调，而非 LaTeX \textbf —— 未开启 text.usetex 时会被原样打印）
    ax.plot(epochs, ours_acc, label="Ours",
            color=colors["ours"], marker="o", markersize=6, linewidth=2.6)

    # 美化轴与网格
    ax.set_xlabel("Training Epochs / Pre-training Budget")
    ax.set_ylabel("Top-1 Accuracy (%)")
    ax.set_title("Scaling Efficiency on Target Benchmark", pad=12, fontweight="bold")
    ax.grid(True, linestyle="--", alpha=0.6)

    # 移除顶部与右侧冗余边框（学术极简原则）
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # 图例位于右下
    ax.legend(loc="lower right")

    plt.tight_layout()
    plt.savefig(output_path)  # 按扩展名自动选择 .pdf / .png 等后端格式
    print(f"[+] 示例出版级图表已保存至: {output_path}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="生成出版级学术示例图：内置学者色板，或从蒸馏档案 --from-profile 提取调色板。")
    parser.add_argument("--palette", choices=list(PALETTES.keys()), default="kaiming_blue",
                        help="内置色板名称（默认: kaiming_blue）")
    parser.add_argument("--from-profile", metavar="PATH", default=None,
                        help="学者档案 markdown 路径；提供时优先于 --palette，从「调色板」章节提取色值")
    parser.add_argument("--output", metavar="PATH", default="scholar_benchmark_plot.pdf",
                        help="输出文件路径，支持 .pdf / .png（按扩展名，默认: scholar_benchmark_plot.pdf）")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    generate_sample_plot(output_path=args.output,
                         palette_name=args.palette,
                         from_profile=args.from_profile)

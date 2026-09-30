# Scholar Style Distiller（学者科研风格蒸馏系统）

> Distill a target scholar's research style from their papers into an evidence-anchored, verifiable style profile — covering **figure/table aesthetics, writing rhetoric, research taste, and idea-design patterns** — then use the profile to guide topic selection, idea design, teaser/figure drawing, and paper writing.
>
> 蒸馏指定学者的科研风格，产出**证据锚定、可执行、可验证**的风格档案，再用档案辅助选题评估、Idea 设计、Teaser/图表绘制与论文写作润色。

## 为什么不是又一个"文风模仿"提示词

网上大多数风格模仿方案会把风格压成一份短文档，本质是"摘要式蒸馏"：产出"极简、清晰、低饱和度"这类放之四海皆准的正确废话。本 skill 用三条硬规则对症：

1. **证据锚定**——档案里每条结论必须挂证据（论文 + tex 行号 + 原文引用或图号），无证据的印象禁止入档；
2. **必须看图**——插图结论必须实际打开渲染图观察，配色用渲染图与 `\definecolor` 源码双向验证；
3. **盲测验证（强制）**——留一篇未参与蒸馏的论文，用档案仿写同主题 Abstract 并排对比，不像就回炉修档案。

另附**使用协议**：每次实战前强制重读档案 + 2~3 篇体裁最近的语料原文，校准档案描述不出的"手感"。

## 四个蒸馏维度

| 维度 | 内容 |
| --- | --- |
| 插图与表格 | Teaser 叙事模式、调色板（hex 级）、架构图抽象层级、Caption 三层结构、表格美学 |
| 写作修辞 | Abstract 句序骨架、Introduction 段落功能序列、Related Work 组织法、签名短语库、贡献清单范式、标题与方法命名学 |
| 选题品味 | 创新类型梯队、选题过滤网（他做什么/不做什么）、消融实验哲学、选题时间线 |
| Idea 设计 | Idea 原型分布、问题表述句式、Idea 谱系图（Limitations → 下一篇）、Idea 记分卡 |

## 流水线（7 阶段）

```
阶段 1 语料采集（8~12 篇一作/通讯，脚本批量）
→ 阶段 2 插图与表格蒸馏
→ 阶段 3 写作修辞蒸馏
→ 阶段 4 选题品味蒸馏
→ 阶段 5 Idea 设计蒸馏
→ 阶段 6 建档 + 盲测验证（强制）
→ 阶段 7 使用协议（此后每次实战前执行）
```

## 实战示例：存晓东风格档案

一条完整流水线的真实产物见 [examples/xiaodong_cun/](examples/xiaodong_cun/)：20 篇语料（2019–2026）→ 20 张 tex:行号级证据卡 → 四维风格档案 → 盲测验证通过（SadTalker 留样）→ 可直接套用的**画图/写作/Idea 应用手册**。想最快感受产出形态，直接看 [style_handbook.md](examples/xiaodong_cun/style_handbook.md)。

## 安装与使用

把整个文件夹放进任意支持 Agent Skills 的环境（如 `~/.claude/skills/`、`~/.zcode/skills/`），或在对话中直接粘贴 `SKILL.md` 内容。

```bash
# 按作者批量采集语料（arXiv API，自动生成语料报告：配色/Caption/章节树）
python scripts/paper_collector.py --author "Kaiming He" --max-results 10 --output ./scholar_data/kaiming_he

# 按 ArXiv ID 批量采集
python scripts/paper_collector.py --arxiv 2111.06377,1512.03385 --output ./scholar_data/kaiming_he

# 用蒸馏出的档案渲染同风格示例图
python scripts/plot_style_template.py --from-profile ./scholar_profiles/xxx/profile.md --output demo.png
```

蒸馏产物建议存放：`scholar_profiles/<学者名>/profile.md`（语料与逐篇证据卡放同目录），**不要写进 skill 安装目录**（可能只读）。范例档案见 [examples/kaiming_he_profile.md](examples/kaiming_he_profile.md)。

## 文件结构

```
SKILL.md                     # 主规程（7 阶段 + 全局硬规则）
references/
  figure_style_guide.md      # 插图与表格蒸馏指南
  writing_rhetoric_guide.md  # 写作修辞蒸馏指南
  research_taste_guide.md    # 选题品味蒸馏指南
  idea_design_guide.md       # Idea 设计蒸馏指南
  scholar_profile_template.md# 档案模板
scripts/
  paper_collector.py         # arXiv 批量采集 + 语料报告生成
  plot_style_template.py     # 风格示例图渲染（--from-profile 按角色关键词提取档案色板；内置 matplotlib_classic ≈ 2024+ 主流风格）
examples/
  kaiming_he_profile.md      # 范例档案
  xiaodong_cun/              # 完整实战示例（档案 + 应用手册 + 20 张证据卡 + 盲测记录）
```

## 使用边界

复刻风格 ≠ 冒充本人：档案用于学习风格与思维方式，**禁止**抄袭原文句子进新论文、禁止冒充作者本人、禁止误导读者认为产物出自该学者。

## 相关项目

- [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills)：把一位博导自己的科研经验蒸馏成技能（成品思路来源）
- [writing-dna-skill](https://github.com/larashero3-dotcom/writing-dna-skill)：通用文风蒸馏（"写作前重读原文"设计参考）

## License

MIT

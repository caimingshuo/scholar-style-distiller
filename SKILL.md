---
name: scholar-style-distiller
description: >-
  蒸馏指定学者或实验室的科研风格，产出证据锚定的风格档案，并用档案指导选题评估、Idea 设计、插图绘制与论文写作。覆盖四个维度：论文插图与表格审美、写作修辞、选题品味、Idea 设计模式。Distill a target scholar's or lab's research style from their papers into an evidence-anchored profile covering figure/table aesthetics, writing rhetoric, research taste, and idea-design patterns. Use when the user wants to 蒸馏/模仿/分析某学者或实验室的科研风格, emulate a scholar's paper style, distill research taste, or evaluate new research ideas in a scholar's taste.
---

# Scholar Style Distiller（学者科研风格蒸馏系统）

将指定学者（或实验室）的科研风格逆向解构为**证据锚定、可执行、可验证**的风格档案（Scholar Profile），再用档案辅助四个实战环节：选题评估、Idea 设计、Teaser/图表绘制、论文写作与润色。

## 全局硬规则（任何阶段不得违反）

1. **证据锚定**：写入档案的每一条结论必须附证据（论文 + 位置 + 原文引用或图/表号）。没有证据的印象（"极简""清晰"这类空泛形容词）禁止入档。
2. **必须看图**：插图结论必须来自实际打开渲染图或矢量图观察，禁止仅凭 `.tex` 源码推断视觉效果；配色结论须渲染图与 `\definecolor` 源码双向验证。
3. **作者位置过滤**：只蒸馏目标学者为一作或通讯的论文；挂名中间作者的论文是噪声。
4. **复刻写法，不搬运内容**：档案用于学习风格与思维方式。禁止抄袭原文句子进新论文、禁止冒充作者本人、禁止误导读者认为产物出自该学者。

## 流水线总览

```
阶段 1 语料采集 → 阶段 2 插图与表格蒸馏 → 阶段 3 写作修辞蒸馏
→ 阶段 4 选题品味蒸馏 → 阶段 5 Idea 设计蒸馏
→ 阶段 6 建档与盲测验证 → 阶段 7 使用协议（此后每次实战前执行）
```

## 阶段 1：语料采集（Corpus Harvesting）

规格：**8~12 篇**目标学者为一作/通讯的论文，覆盖不同时期与不同类型（方法类 / 实证类 / Benchmark 类各至少 1 篇）。若该学者有公开 talk、博客、访谈或课程讲义，补充 1~3 份——选题逻辑与 Idea 来源往往只在这些场合被明说。

用脚本批量采集并自动生成语料报告（`\definecolor` 配色、全部 Caption、Abstract、章节树）：

```bash
# 按 ArXiv ID 批量（逗号分隔）
python scripts/paper_collector.py --arxiv 2111.06377,1512.03385 --output ./scholar_data/kaiming_he

# 按作者检索（arXiv API，按时间倒序）
python scripts/paper_collector.py --author "Kaiming He" --max-results 10 --output ./scholar_data/kaiming_he
```

脚本产物：`<id>_extracted/`（.tex 源码 + 矢量图原文件）、`<id>.pdf`、`figures/`、`<id>_corpus_report.md`。

## 阶段 2：插图与表格蒸馏

按 [figure_style_guide.md](references/figure_style_guide.md) 逐篇分析：Teaser (Figure 1) 叙事模式、调色板、架构图抽象层级、排版字体一致性、Caption 三层结构、**表格美学**（线型、最优标注、数字排版）。每张代表性 Figure/Table 必须打开查看，并按指南第六节格式记录证据。

## 阶段 3：写作修辞蒸馏

按 [writing_rhetoric_guide.md](references/writing_rhetoric_guide.md) 逐句解剖至少 3 篇的 Abstract 与 Introduction：Abstract 句序骨架、Introduction 段落功能序列、**Related Work 组织法**、标志性短语库、贡献清单范式、**标题与方法命名学**。每个句式模板必须附 ≥2 条原文例句。

## 阶段 4：选题品味蒸馏

按 [research_taste_guide.md](references/research_taste_guide.md) 分析：创新类型梯队分布、立意重构套路、消融实验哲学、**选题时间线**（主线深挖还是多点开花、相邻论文延续还是跳变、近年口味漂移方向）。产出该学者的「选题过滤网」——他**不做**什么和做什么同等重要。

## 阶段 5：Idea 设计蒸馏

按 [idea_design_guide.md](references/idea_design_guide.md) 分析该学者**如何产生与打磨 Idea**：

1. **Idea 原型分布**：矛盾驱动 / 现象驱动 / 迁移驱动 / 简化驱动 / 尺度驱动 / 基准驱动，各占几篇，附论文佐证；
2. **问题表述句式**：他如何把大方向收敛成一句话研究问题；
3. **Idea 谱系图**：论文按时间排列，标注哪篇的结论或局限催生了哪篇，识别「下一篇论文」的生成逻辑；
4. **Idea 记分卡**：把隐性筛选标准变成可给用户新 Idea 打分的 checklist。

## 阶段 6：建档与盲测验证

1. 按 [scholar_profile_template.md](references/scholar_profile_template.md) 填写档案，存到 `./scholar_profiles/<学者名>/profile.md`（语料放同目录 `corpus/`）。范例见 [kaiming_he_profile.md](examples/kaiming_he_profile.md)。
2. **盲测验证（强制）**：留一篇未参与蒸馏的论文，遮住其 Abstract，用档案仿写同主题 Abstract，并排对比句序骨架、短语习惯、claim 强度；明显不像则回阶段 3 修档案。插图侧同理：用 `scripts/plot_style_template.py --from-profile <profile.md>` 渲染示例图，与学者原图并排检查。
3. 验证未通过而交付的档案视为半成品，必须向用户声明差距点。

## 阶段 7：使用协议（此后每次实战前强制执行）

1. 布置任务后，**先完整重读 profile.md**，再读 2~3 篇与当前任务体裁最接近的语料原文——校准档案描述不出的手感（句子的呼吸感、转折时机、图的留白节奏）。
2. 冲突优先级：用户本次明确指令 > 目标 venue 的格式要求 > 档案中的风格规则。
3. 实战入口：
   - **选题/Idea**：“用该学者的 Idea 记分卡评估我的 idea：……，并按他的原型给出 2 个重构方向。”
   - **Teaser/图表**：“按档案的调色板与构图模式为我的方法设计 Figure 1 草案 + Caption。”绘图用 `plot_style_template.py --from-profile`。
   - **写作**：“用该学者的句序骨架与短语库重写我的 Abstract/Introduction，每处改动对照档案说明依据。”

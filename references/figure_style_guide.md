# 论文插图与视觉审美规范 (Figure & Visual Aesthetics Guide)

顶会审稿（CVPR/ICCV/ECCV/NeurIPS/ICML/ICLR 等）中，**插图（Figures）往往决定了审稿人的第一印象**。优秀的顶尖学者通常在正文第 1 页或第 2 页顶部放置一个极其亮眼的“Figure 1 (Teaser)”，并在方法章节提供一目了然的 Pipeline 图。

---

## 一、Figure 1 (Teaser Figure) 黄金设计法则

### 1. 3秒原则与自解释性 (Self-Contained)
- **审稿人心理**：审稿人快速翻阅论文时，首先看 Title、Abstract、以及 Figure 1。如果 Figure 1 无法在 3~5 秒内传达文章的核心贡献，文章就会被潜意识归为“平庸之作”。
- **要求**：不阅读正文，仅凭“图 + Caption”即可完全理解：
  1. 研究面临的根本瓶颈是什么？
  2. 本文提出的核心 Insight 是什么？
  3. 最终达成的突破性效果是什么？

### 2. 三种经典 Teaser 视觉构图模式

#### 模式 A：范式对比型 (Paradigm Shift: (a) Prior vs. (b) Ours)
*适用场景*：提出新框架、新范式、或挑战传统假设（如 ResNet, MoCo, MAE, NeRF, LoRA）。
*构图*：
- **(a) Conventional / Prior Approach**：用灰暗、略显繁琐或带有明显痛点（红叉、红色警示箭头、虚线瓶颈）的结构展示既有方法的死胡同。
- **(b) Our Proposed Approach**：用清爽、对称、极简的路径（绿色对勾、高亮主色箭头）展示本文机制，形成鲜明反差。

#### 模式 B：现象观察与启示型 (Observation-Driven: Observation -> Hypothesis -> Result)
*适用场景*：实证科学类论文、大模型行为分析、Scaling Law 发现。
*构图*：
- 左侧：一个清晰的实验曲线或散点图，展示传统方法失败或某个惊人的反直觉现象（Surprising Discovery）。
- 右侧：本文由此提炼出的核心假说与验证结果。

#### 模式 C：效果震撼型 (Visual Hero / Teaser Showcase)
*适用场景*：生成模型（Diffusion/Sora/Gaussian Splatting）、3D 重建、具身智能等视觉效果极强的任务。
*构图*：
- 极其清晰的高清定性对比结果，直接将 SOTA 方法的瑕疵与本文方法的完美细节并列（可带局部放大镜 Inset 效果）。

---

## 二、顶级学者配色美学体系 (Color Palette Philosophy)

顶尖学者的论文配色通常遵循**低饱和度、高辨识度、典雅克制**的原则，严禁使用原生彩虹色（如 Matplotlib 默认高亮红绿蓝、Jet colormap 等）。

### 1. 常用经典学术色卡推荐

#### 色卡 1：经典清华/何恺明沉稳风 (Academic Navy & Muted Orange)
- **主色（本文方法 / Ours）**：深海蓝 `#2C5282` 或 科技钴蓝 `#1F77B4`
- **对比色（基线 / Baseline）**：复古砖橙 `#DD6B20` 或 温暖赤红 `#D62728`
- **辅助中性色**：暖灰 `#E2E8F0`、炭黑 `#2D3748`
- *特点*：对比鲜明而不刺眼，蓝橙对比是国际顶级学术出版物（Nature, Science, IEEE）的首选互补色。

#### 色卡 2：DeepMind / Nature 极简薄荷风 (Teal & Slate Gray)
- **主色**：冷青绿 `#2A9D8F`
- **强调色**：姜黄 `#E76F51` / 杏黄 `#F4A261`
- **底色与基线**：岩板灰 `#4A5568`、浅冰灰 `#EDF2F7`
- *特点*：极具现代感与科学理性感，非常适合信息量大的结构图与柱状图。

#### 色卡 3：伯克利 / 斯坦福温润学术风 (Morandi Muted Colors)
- **莫兰迪灰蓝**：`#4A6FA5`
- **莫兰迪干枯玫瑰**：`#B85B5B`
- **莫兰迪浅草绿**：`#6C8E74`
- *特点*：即使多个模块并列，视觉压力也很小，极显高级感。

### 2. 色彩语义规范 (Color Semantics)
- **Ours 永远突出**：Ours 的曲线/模块应当使用最醒目、饱和度适中的主色，线宽加粗（如 `linewidth=2.5`）。
- **Baselines 永远退后**：竞争对手或 baseline 曲线使用灰色系、虚线（dashed/dotted），或半透明度（alpha=0.6~0.8）。
- **模块背景色**：大区域底框（Bounding Box / Sub-network container）必须使用浅度透明色（Alpha 5%~10%），避免喧宾夺主。

---

## 三、排版与字体一致性 (Typography & Consistency)

1. **字体与正文 LaTeX 一致**：
   - 严禁在 LaTeX 论文中使用 Arial/Calibri 混搭。
   - 图中文字应优先匹配正文字体（如 `Computer Modern`, `Times New Roman`, 或 `TeX Gyre Termes`）。
   - 字号不应小于正文的 `\footnotesize`（一般为 8pt~9pt），确保在单栏或双栏打印时清晰可辨。

2. **数学符号一致性**：
   - 图中的变量名必须用 LaTeX 语法书写（如 $x_i$, $f_\theta$, $\mathcal{L}_{\text{total}}$），与正文公式严格对应，避免图文脱节。

3. **微间距与对齐 (Alignment & Spacing)**：
   - 所有连接线横平竖直，严禁歪斜或随意交叉。
   - 模块与文字之间留有充足负空间（Padding），切忌拥挤。

---

## 四、Caption 撰写公式 (The "Figure Caption" Formula)

顶尖学者的图题通常不是一句话草草了事，而是由**三层结构**组成的微型摘要：
1. **Boldface Title (核心结论)**：用粗体提炼出该图最核心的 takeaway（例如：`\textbf{Overall architecture of our framework.}` 或 `\textbf{Scaling behavior on benchmark X.}`）。
2. **Component Explanation (图解描述)**：按逻辑顺序解释输入、核心模块、输出以及箭头/颜色的含义。
3. **Core Conclusion / Takeaway (审稿人启示)**：一句话总结出核心优势（例如："Notice that without any additional bells and whistles, our method achieves..."）。

---

## 五、表格美学规范 (Table Aesthetics)

表格是论文视觉的另一半，蒸馏时逐篇记录目标学者的表格习惯：

1. **线型**：是否严格三线表（`\toprule` / `\midrule` / `\bottomrule`，无竖线）？是否用浅色交替行底（row coloring）区分方法族？
2. **最优/次优标注**：最优加粗、次优下划线还是灰色？Ours 所在行是否底色高亮？
3. **数字排版**：小数位是否对齐、有效数字位数习惯、均值±方差的写法、提升幅度是否用括号标注。
4. **表题句式**：Table caption 置于表上方；句式与 Figure caption 是否一致（是否同样以粗体结论开头）。
5. **信息密度**：一表容纳多少列对比方法？是否用缩写 + 脚注控制宽度？

## 六、蒸馏证据记录格式

每条插图/表格结论按如下格式记录，**无证据不入档**：

| 结论 | 证据（论文 + 图/表号） | 观察方式 |
| --- | --- | --- |
| Ours 主色为 `#1F77B4` | MAE Fig.1/3/5；`\definecolor` 见 main.tex | 渲染图 + 源码双向验证 |
| Teaser 采用三栏范式对比 | MoCo Fig.1：(a) end-to-end (b) memory bank (c) MoCo | 渲染图观察 |

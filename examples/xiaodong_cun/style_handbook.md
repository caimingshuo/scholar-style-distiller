# 论文 Idea + 画图 + 写作风格手册（存晓东风格 · 详细版）

> 给自己的论文直接套用。**每条规则的原始证据**（原文引用 + tex 行号 + 看图记录）见 [profile.md](profile.md) §一/§二 与 [analysis/](analysis/) 逐篇证据卡。
> 用途边界：复刻写法与思维方式，不搬运原文内容、不冒充本人。
>
> **使用前先选年代**：本手册默认按 **2024–26 当前风格**（matplotlib 红实线 + 诚实工程 + 三件套产出）写。2019–20（PPT 高饱和）与 2021–23（draw.io 淡彩为主）的旧习惯只在标注处出现，勿混用——色板混年代是最容易被识破的破绽。

---

# A. 画图风格

## A0. 工具链与全局设定

- **架构图/流程图**：draw.io。淡彩圆角块 + 黑描边 + 白底；无 3D、无渐变、无阴影；衬线字体（与正文 Times 接近）；颜色全在绘图工具端实现，LaTeX 端 `\definecolor` 基本为 0
- **曲线/散点/柱状/曲面**：matplotlib。当前期用默认色系 + 少量自定义；xkcd 手绘风仅用于轻松向工作（二选一，别混）
- matplotlib 全局设定（当前期风格的最小实现）：

```python
import matplotlib.pyplot as plt
plt.rcParams.update({
    "font.family": "serif",          # 与正文字体一致
    "axes.grid": True,
    "grid.linestyle": "--",
    "grid.color": "#cccccc",
    "grid.linewidth": 0.6,
    "axes.spines.top": False, "axes.spines.right": False,
    "legend.frameon": False,
})
C_OURS, C_B1, C_B2, C_B3 = "#d62728", "#1f77b4", "#2ca02c", "#9467bd"
```

## A1. Teaser / Figure 1 —— 五型选一（**效果墙禁止**）

| 论文类型 | 模式 | 具体做法 | 实例 |
| --- | --- | --- | --- |
| 效率/检测/训练类 | **量化曲线前置** | 跨双栏放 2 张子图，子图标题就是卖点词；红色实线 Ours、蓝色虚线基线；图内灰色虚线箭头标注倍数；x 轴用断轴符号「<<」把基线的劣势拉远 | DEIM teaser：两个 subfigure 各占半栏，标题 `\textbf{Faster}: training is more compute-efficient` / `\textbf{Better}: exceeding all real-time detectors`；图内箭头标 "2× faster in convergence"；80→500 epoch 断轴 |
| 恢复/编辑类 | **失效模式主角型** | 大图左 2/3 场景照，黄框=输入检查区、**红框=前人方法瑕疵、绿框=本文修复**；右侧一列放大 patch + 底部一行 patch；标题卖点直接可视化 | 1911 fig1：ghost 瑕疵做主角；caption 两句内嵌结论 "our method successfully removes the shadow and reduces the ghost" |
| 方法/模块类 | **机制自解释型** | 上半=任务数据流（输入→encoder→模块→输出），下半=模块拆解；caption 是微缩 Introduction，末尾指向正文章节 | 1907 fig1：S²AM 两路拆解 + "More detail of each component in S²AM can be found in the Section 3" |
| 训练方法类 | **训练配方图** | Figure 1 画**训练管线**而非网络：两条训练路线并列 + 循环箭头，把「免费标签机」一图讲清 | 2203 fig1：UIP/SAF 双管线，sRGB→反处理→随机光源重照=免费样本 |
| 新任务/新范式类 | **反差柱状图** | 关键对照数字前置：双面板柱状图，柱顶标原始值，**红字标基线失败值、绿字标增益** | VAU-R1 fig1：左 QA 面板橙渐变、右 Grounding 面板蓝渐变，红 "0.00" / 绿 "+5.89" |

> 效率-性能散点图是 A1 的变体（架构类论文用）：PSNR vs GMACs(log) 散点，Ours 红星折线居左上，caption 一句话即可——"PSNR vs. computational cost on the SIDD dataset."（Uformer fig1，信息全在图里）。

## A2. 调色板（当前期全表）

| 用途 | 颜色 | 规则 |
| --- | --- | --- |
| Ours（曲线/柱） | `#d62728` 红 | **实线 + 加粗 + marker**，永远在最上层 |
| 基线 1/2/3 | `#1f77b4` 蓝 / `#2ca02c` 绿 / `#9467bd` 紫 | 一律**虚线/点线/点划线**，marker 区分，视觉退后 |
| 图内增益标注 | 绿字 | "+2.50 / +5.89" 直接写在图上 |
| 图内失败标注 | 红字 | 基线失败值 "0.00" 原样标出 |
| 图内倍数注释 | 灰色虚线箭头 + 灰字 | "2× faster in convergence" |
| 架构图模块 | `#DAE8FC` 蓝 / `#D5E8D4` 绿 / `#FFE6CC` 橙 / `#FFF2CC` 黄 | 淡彩四件套；**核心组件块放大 3 倍**；其余模块小一号 |
| 表格 Ours 行 | `\rowcolor[gray]{0.95}` 浅灰 | 行名加粗 |
| 表格 OOD 行 | `lightyellow RGB(255,255,204)` 浅黄 | caption 明写含义 |
| 表格变差数字 | 红 `#CB0000` / `alizarin` | 变差标红，不藏 |
| 可训练/冻结 | flame 🔥 / snowflake ❄️ 图标 | 架构图统一词汇（DocShadow/DepthTTT/ForgeryTTT 同款） |
| 超链接色 | `citecolor #0071BC`、`linkcolor #ED1C24` | 仅链接用，不进插图 |

⚠️ **禁混年代**：2019-20 的 PPT 高饱和（亮红/紫/橙/khaki 竖条）只存在于他学生时期作品；2021-23 淡彩只用于 draw.io 架构图。2026 投稿正文图 = matplotlib 红实线这套。

## A3. 架构图规范

1. **两级分解**：框架图（整网数据流）和模块图（单个 block 的层顺序）分开两张画；粗细两极并存——teaser 粗粒度示意，模块图可画到算子级（pooling→FC→sigmoid）
2. **张量形状写在图顶部**：`3×H×W → C×H/2×W/2 → … → 16C×H/16×W/16`，与正文公式逐项对应（Uformer overview）
3. **图内变量 = 正文公式变量**：caption 里的 $s^{src}_t$、$c^{edit}_t$ 全部出现在图中（FateZero framework）
4. **真实样例直塞方法图**：用真实照片/示例帧讲机制（DEIM 用真实狗照片讲匹配机制、3D viridis 曲面画损失地形标红星），不用抽象圆圈
5. **图例行**：框架图底部横排图例，逐一定义每个符号（"k Dilated CONV (Dilation=k) / Conv(1×1) / A Attentive Aggregation Node"）
6. **复合图用 (a)(b)(c) 编号**，caption 按 `(a)… (b)… (c)…` 顺序走读

## A4. 定性对比图固定协议

- **列序**：`Input → 各方法（按年份旧→新）→ Ours → Target/GT`，**Ours 紧邻 GT**；或行=方法、Ours 垫底收尾
- 每列/每格下标方法名 + 指标值：`NBNet (34.84 dB)`、`Ours (\textbf{35.05 dB})`——**Ours 加粗**；指标在整图上算，crop 仅为展示（caption 可注明 "The PSNR value under each patch is computed on the corresponding whole image."）
- 输入图上画红/黄框标放大区，右侧配放大 patch 列
- **差分图签名动作**：absolute difference colormap **放大 10×/30×** 拼在结果下方，caption 写 "We enlarge the colormap 10× for better visualization"——用差分图代替肉眼对比
- 多样本图配 `(a) Input, (b) Guo, … (g) Target` 编号清点，caption 逐列指认
- 注意力/中间信号可视化单独立图，用它闭环正文观察句（"gated attention 只亮局部 vs Ours 覆盖整个影子区域"）

## A5. 曲线与散点图

- Ours 红实线加粗在最上/左上；基线全虚线退后；图例 Ours 放末位
- 关键数值直接标在数据点旁（延迟-AP 图沿途标 49.0/52.7/54.7/56.5）
- 需要强调差距时用**断轴「<<」**压缩基线区间（DEIM：80→500 epoch 断轴）
- 训练动力学可入图：Step1 Loss=0.36 → Step3 0.22 递减曲线当 teaser（DepthTTT）
- 超参扫描画成谷形：γ∈{0.01, 0.05, 0.1, 1, 5} 两个数量级，展示「太大太小都变差」

## A6. 表格美学（LaTeX 模板可直接抄）

```latex
% 三线表 + 最优加粗/次优下划线 + 效率列 + Ours 行底色
\begin{table*}[t]
  \centering
  \caption{\textbf{Comparison with real-time methods on COCO val2017.}
    The best results are in \textbf{bold} and second best are \underline{underlined}.
    $^{\star}$ indicates the NMS is tuned with a confidence threshold of 0.01.}
  \label{tab:sota}
  \resizebox{\linewidth}{!}{%
  \begin{tabular}{lcccccc}
    \toprule
    Model & Epochs$\downarrow$ & Params(M)$\downarrow$ & FPS$\uparrow$ & AP$\uparrow$ & AP$_{50}$\uparrow \\
    \midrule
    \rowcolor{f2ecde} \multicolumn{6}{l}{\textit{YOLO-based}} \\
    YOLOv11 & 500 & 37.4 & \underline{430.1} & \underline{56.1} & \underline{72.7} \\
    \rowcolor{f2ecde} \multicolumn{6}{l}{\textit{DETR-based}} \\
    D-FINE-L & 80 & 29.5 & 315.0 & 54.7 & 71.5 \\
    \midrule
    \rowcolor[gray]{0.95}
    \textbf{Ours} & \textbf{24} & 31.2 & 325.0 & \textbf{56.5} & \textbf{73.0} \\
    \bottomrule
  \end{tabular}}
\end{table*}
```

规则清单：

1. 三线表 `\toprule/\midrule/\bottomrule` + `\cmidrule(lr){2-3}` 分组，**无竖线**；整体 `\resizebox{\linewidth}{!}` 控宽
2. **最优加粗 + 次优下划线**，且 caption 明写约定："The best results are bold and the second best are underlined."——这条 caption 声明每篇必写
3. 方法族分组行用底色条：`\rowcolor{f2ecde}`（米色）+ `\multicolumn{6}{l}{\textit{YOLO-based}}`
4. Ours 行：`\rowcolor[gray]{0.95}` 浅灰 + 行名加粗；基线区与 Ours 区用 `\midrule` 物理隔开，基线行可用 `\small{}` 缩一号
5. **效率列与质量指标同权**：Epochs/Params/FPS/GMACs 紧跟模型名；对手 FPS 更高照样给对手加粗（2007 主表 BASNet 90.9 加粗，自己 35.7 不加粗）
6. 指标带方向箭头 `AP$\uparrow$ / FID$\downarrow$`；区间型指标用 `$\rightarrow$`
7. 小数位全表统一（AP 1 位、PSNR/RMSE 2 位、CLIP 3 位）；缺数据如实填 "-"；百分比 0%/50%/100%
8. 特殊处理用脚注符号并在 caption 解释：`$^{\star}$` = 调过 NMS 的基线；`$\dagger$` = 训练集与本文重叠的基线
9. 相对增减用彩字：**蓝=提升、红=下降**（"The blue and red numbers are the relative improvement and decline"）
10. 基线命名带年份下标：`Yang$_{12'}$`、`ST-CGAN$_{18'}$`，caption 解释 "The subscripts represent the years of the compared methods."
11. 公平分组：backbone/训练数据不同的方法用 `\hline` 隔开，不混排冒充 SOTA
12. 中间产物单独立表（合成数据的质量也立表自证）；OOD 测试行浅黄底 + caption 明说 "serving as an out-of-distribution test"

## A7. Caption 三层结构（所有图表通用）

```
\textbf{粗体结论导语.} + 机制/图例展开（颜色含义、(a)(b)(c) 走读、计算口径） + 结论或观图提示（"Best viewed with zoom-in" / "best view with zoom in"）
```

三种成品变体：

- 粗体导语型（默认）：`\textbf{Effectiveness of Reinforcement Fine-Tuning.} We compare QA accuracy ... across different models. This demonstrates that RFT enhances both reasoning and temporal localization.`
- 粗斜体型（结果章小节图）：`\textbf{\textit{Correlation Analysis.}} ...`
- 编号指认型（早期/期刊风）："(d) 的上下两行结果分别来自 ST-CGAN~(ST) 与 DeShadowNet~(DS)。Best view with zoom-in."
- 图内文字染强调色：编辑词在 prompt 里直接染色 `\textcolor{red}{porsche car}`（排版系统实现，不是贴图）

---

# B. 写作风格

## B1. Abstract —— 按任务选骨架（4 选 1）

**骨架 1 · 观察式**（底层视觉/恢复类任务）：

```
① 任务一句话定义（"X aims to separate/do Y from a single image."）
② 失效模式具体命名（"often causes two types of ghosts: A or B (as shown in Figure 1)"）
③ 总纲（"In this paper, we tackle these issues in two ways."）
④ 斜体观察宣言（"we start from an empirical observation: *…*"）
⑤ 方法一（命名模块）＋数据经济学数字对比（"the largest dataset contains 2k+ pairs. However, it has only 0.1k+ unique scenes"）
⑥ 方法二
⑦ 战绩（"outperforms other state-of-the-art methods by a large margin"）＋代码 URL
```

**骨架 2 · 宣言式**（架构/通用框架类）：

```
① 第一句即宣言（"In this paper, we present X, an effective and efficient …"）——背景句写好也删掉
② "there are two core designs. First, we introduce A, which…" ③ "Second, we propose B to…"
④ "Powered by these two designs, X enjoys …"
⑤ 实验范围一句（"extensive experiments on four tasks, including…"）
⑥ "Without bells and whistles, …" ＋代码 URL
```

**骨架 3 · 链式**（训练策略/损失设计类）：

```
① 第一句报方法名（"We introduce X, an innovative and efficient training framework designed to…"）
② 问题→方案同句完成
③ **主动暴露方案副作用**（"While A speeds up convergence, it also introduces numerous low-quality matches"）
④ 方案二接住副作用
⑤ 复现级量化（"53.2% AP in a single day of training on an NVIDIA 4090 GPU"）
⑥ 定位收尾（"We believe X sets a new baseline for …"）＋代码 URL
```

**骨架 4 · 双资产式**（方法+基准一起发）：

```
① 应用场景开头＋挑战（"yet remains challenging due to…"）
② 矛盾一（现有方法缺什么）
③ **矛盾二独立成句**（"This limitation is further compounded by the absence of comprehensive benchmarks…"）
④ "To address both challenges, we introduce \textbf{X-R1}, a data-efficient framework… Besides, we propose \textbf{X-Bench}, the first … benchmark tailored for …"
⑤ 定性+定量结果句（可无具体数字）
⑥ "Together, our method and benchmark establish a strong foundation for …"＋GitHub
```

通用细节：失效模式命名（骨架 1②）和替代理划界（"On the other hand, explicitly using 3D information also suffers problems of stiff expression and incoherent video."）可跨骨架混用；6–9 句为宜。

## B2. Introduction 五段式

- **P1** 任务/场景/自然现象一句切入，落到下游动机（禁宏大叙事；"Shadows are a common phenomenon in nature." / 从 Photoshop 拼图场景开场）
- **P2** 前人路线按时间线各给一句局限（`\citeauthor{...} proposed … \shortcite{...} … however …`）
- **P3** 缺口段枚举，**枚举结构 = 论文结构**：
  - 双因版："we hypothesize that the reasons are two-fold. \ding{182} Sparse supervision \ding{183} Low-quality matches"（两因各接一个组件）
  - 双缺口版："two major drawbacks. First,… In addition,…"
  - 三连版："(i)…(ii)…(iii) evaluation protocols remain underdeveloped."
- **P4** 方案领起二选一：
  - **斜体观察句**（签名动作）："Different from the previous methods, our key observation is: *For X, the model needs to learn the dissimilarity in A and ensure the consistency in B.*"——同一模板跨任务换词复用
  - 断言式："we argue that the accuracy of X is highly related to Y"
  - 附「替代理也堵死」句："On the other hand, explicitly using Z also suffers problems of …"
- **P5** 框架走读（Firstly/Then/Moreover/Finally）+ 贡献清单
- 数据经济学句式（造数据时必用）："It is much easier to collect A than B" / "2k+ pairs, but only 0.1k+ unique scenes"
- 物理第一性切入（可选加分项）：从成像公式推问题——"DOF≈2NCD²/f²，唯一非相机参数的是 D"→"整个领域在用 2D 视角看 3D 现象"

## B3. 签名短语库（场景 × 短语 × 实例）

| 场景 | 短语 | 原文实例 |
| --- | --- | --- |
| 立论 | we argue that… | "we argue that the accuracy of DBD is highly related to scene depth"；"we argue that these issues are mainly because of learning from the coupled 2D motion fields" |
| 双因拆解 | we hypothesize that the reasons are two-fold. \ding{182}…\ding{183}… | DEIM intro |
| 占位 | for the first time / the first X / We make the very first step to… | "We make the very first step to evaluate the general T2V models"（全文三现）；"To the best of our knowledge, this is the first attempt to…" |
| 自我定性 | simple yet effective / novel yet straightforward | "a simple yet effective method for zero-shot video editing"；"a novel yet straightforward approach named Dense O2O" |
| 无 trick 声明 | without bells and whistles | "without bells and whistles, \eg, the multi-stage or multi-scale framework and the advanced loss function" |
| 战绩 | by a large margin / establishes a new SoTA | "outperforms other state-of-the-art methods by a large margin" |
| 效率卖点 | computation-free / data-efficient / with only 16% parameters | "our approach is computation-free"；"with only 16\% parameters of the previous best model" |
| RW 划界 | However, … / Differently, our … / In contrast, we… | "However, these methods are designed for image in-painting task specifically."；"Differently, our pre-training aims to regress the illuminant directly" |
| 问题开放钩子 | However, how to … is still unclear. | "However, how to edit real-world content using this model is still unclear." |
| 组件展开 | Precisely, we present A to… / As for B, we design C via… | SadTalker 组件段 |
| 承上启下 | Powered by these two designs / Based on the above two designs | Uformer abstract/intro |
| 补充限定 | Notice that… / Note that… | "Note that, in order to conduct a fair comparison…" |
| 实验收束 | It is clear that… / Obviously, | "It is clear that our method outperforms other methods to a large extent." |
| 扩展宣言（早期） | make a big step / We expect our work will encourage further research to explore… | 1907 / Uformer 结尾 |
| 借力开场 | built upon the commonly used X | DocShadow/DepthTTT/ForgeryTTT |
| 悖论钩子 | 训 A 却不用 A（问句仅用于悖论场景） | "training high-quality video models without using high-quality videos"；"We raise a question: What makes the inpainting hard…" |

## B4. Related Work

- **分类法组织**：3 个 `\noindent\textbf{}` run-in 段头（按任务/技术路线分派，非时间线；段内可按 GAN→Transformer→Diffusion 代际推进）
- **RW 段头复用 Intro 拆出的矛盾名**（DEIM：Intro 拆 "sparse supervision / low-quality matches" → RW 小节就叫 "Increasing positive samples / Optimizing low-quality matches"）
- 每段收束句式库（轮换用）：
  1. "However, these methods are designed for X specifically."
  2. "Differently, our method leverages…"
  3. "In contrast, we design a general…"
  4. "However, how to … is still unclear."
  5. "To bridge this gap, we propose…"
  6. "…, which further increases the difficulties in X."
- 温度规则：只陈述失效场景（"may fail when the track is lost" / "results in flickering"），无人身化贬词；对并用竞品礼貌性让步（"although our network is not particularly designed for X, it still gets better results"）
- 显式接线自己前作：`\cite{cun2018depth}`——个人研究线在 RW 里可见

## B5. 贡献清单（3 条范式）

**范式 1 · 组件式**（默认）：

```
\begin{itemize}
  \item We present X, a general and superior …（框架，first 宣言）
  \item We propose A, which …；and B, which …（机制，每条带功能从句或立即给结果："Once trained with …, our model achieves state-of-the-art performance on …"）
  \item Extensive experiments show that X establishes new state-of-the-arts on … while using only 16% parameters.（战绩+效率双卖点）
\end{itemize}
```

**范式 2 · 双因对应式**：贡献条目与 P3 的 two-fold 枚举一一对应（quantity/quality 对仗）。

**范式 3 · 发现清单式**（benchmark 论文）：第 3 条就是 Findings 本身——"we also discuss several conclusions and findings, which might also contribute to further innovation"，正文用 `\noindent\textbf{Finding \#1: …}` 加粗小标题驱动，每条=一句论断+"As shown in Table/Fig…"。

## B6. 标题与方法命名

- **冒号结构**（主导）：「缩写: 机制描述+收益词」——"DEIM: DETR with Improved Matching for Fast Convergence"；「方法名: A General X for Y」——"Uformer: A General U-Shaped Transformer for Image Restoration"
- **Towards 式**：把卖点+组件全写进标题——"Towards Ghost-free Shadow Removal via Dual Hierarchical Aggregation Network and Shadow Matting GAN"
- **命名即论点**：经典概念一字改动当标题（Knowledge→**Depth** Distillation）
- 缩写字母来源可在标题里排版标注：`\underline{F}using \underline{A}ttentions for Zero-shot \underline{T}ext-based video \underline{E}diting`
- 系列词缀占位：-Crafter（TaleCrafter/EvalCrafter/VideoCrafter…）、-R1（借 DeepSeek-R1 认知）、任务缩写+GAN/Bench（SMGAN、VAU-Bench）
- 组件命名朴素功能式：Dense O2O、Lightweight Head、Matchability-Aware Loss；**给每个设计决策单独起名**（S²AM→S²ASC→S²AD 各自成名）
- 备选标题保留在源码注释里是正常工作流（从 "An Empirical Study of…" 收敛到 "A General X" 宣言）
- 基准三件套命名：方法 X-R1 + 数据 X-Bench + 协议 X-Eval

## B7. 实验章节写法

1. **公平性声明前置**（实验节第一段）："for training, we do not use any additional samples or synthesized samples… all the results are raw outputs from the network without any post-processing."
2. **镜像对照物**：把 Ours 的核心模块全换常规件重建基线（把 LeWin 全换 ResBlock 造 UNet-T/S/B），证明涨点来自模块而非架构
3. **参数量对齐**："we increase the channels in each level of the original Unet to match the parameters of our model for a fair comparison"
4. **plug-in 通用性**：模块插入 ≥3 个 backbone 全涨；或即插即用跨检测器（+RT-DETRv2 / +D-FINE）
5. **组件增量开关表**：`Base → +A → +A+B → Full` 或 `\checkmark/-` 开关列；**主动做「更简单的替代品」对照**并诚实报结果（SRFB vs 去掉 selective attention 的 RFB：简单版在简单集更好，难的集上才赢——照写）
6. **超参扫两端**：γ∈{0.01, 0.05, 0.1, 1, 5} 两个数量级，报谷形
7. **跨数据集/OOD 必做**：A 训 B 测 zero-shot（"without retraining on their specific training datasets"）；OOD 行浅黄底标出
8. **机制可视化闭环**：attention/激活图验证正文假设，收束句 "This fact perfectly explains our assumption"
9. **中间产物单独立表**：合成质量、匹配数分布等也立表自证
10. **效率叙事**：推理时间精确到 0.012s；"53.2% AP in a single day on a 4090" 级复现声明；对标 "IPT: 32 V100 / Ours: Single GPU"
11. **辩护小节**：预判审稿人替代解释，专设小节正面回答（"Relationship with RNN" / "Comparison with CROP"）
12. 结果列表述收束句："It is clear that our method outperforms … to a large extent."

## B8. 诚实工程与 Limitation（他的加分习惯）

- **主动暴露方案副作用**再引出第二个组件（链式叙事）——不藏弱点，把弱点变成结构
- **Failure Cases 小节** + 真实失败样例图，收束句式："the apply range of our X is limited. However, our main target is Y other than X."
- **Limitation 独立成节**，编号自曝 (i)(ii)(iii)，并给未来工作接口（"the real-world situation is very complicated…" / "we believe better and larger X will be released and we can use them as our metrics"）
- 表格里变差标红、对手更强的数字给对手加粗、消融反超自己照样呈现
- 公平出处声明："all the results and figures are provided by the authors or taken from the original papers."
- 复杂度诚实：承认 "the success rate of composing two characters is not satisfying" 这类不满意结果

---

# C. Idea 设计（像他一样想 Idea）

## C0. 内核一句话

**管线内免费信号 + 极简机制 + 数据经济学 + 效率执念**；双主线之二是「给编辑操作找参数化原型」；**每篇 Limitations 节就是下一篇的选题清单**。

## C1. 选题硬过滤（先过闸门，含一票否决项）

✅ **做**（五类，附证据锚点）：
1. **管线内免费信号**——已被算出来但要被丢弃的量：注意力图、反演 latent、白平衡方程的可逆性。「免费」是第一判据（零额外标注、零额外训练）
2. **参数化原型**——从人类工作流/物理定律借可学习参数：Photoshop 曲线→逐通道染色公式（CurveHarmonization）；填洞→只查询洞内坐标（CoordFill）；重光→光图掩码内注噪（LightCtrl）；剪辑→时间戳三元组（CutClaw）
3. **失效模式可见可命名**——ghost / flickering / inharmonious，要能画进 teaser 做主角
4. **新红利首次适配**——新模型红利出现 6–12 个月内做 "the first X"（Transformer→restoration 2021；扩散→视频编辑 2023；GRPO→视频理解 2025；agentic→长视频 2026）
5. **数据矛盾**——标注贵/数据少/伪造进化快于收集 → 自造数据集当主贡献（DocShadow "10 times larger"）或零标注测试时自适应（TTT 配方：辅助任务+更新策略，复用于 DepthTTT/ForgeryTTT）

❌ **不做**（出现即不像他）：
- 训新基座 / 大规模预训练（只借现成权重：冻结基座 + 轻量 LoRA）
- per-prompt 优化、依赖用户手工标注
- 多流 / 多阶段重型工程
- 无 benchmark 输出的纯方法

## C2. 选题公式（照抄）

> **现成强先验（diffusion / MLLM，冻结）+ 被浪费的免费信号 + 一条没人控过的轴（时间/光照/节拍/规模）**
> → 三件套输出：**training-free 方法 + 自建 benchmark/数据集 + 自造指标**
> → 叙事锚点："the first training-free X" + data-efficient + 单卡可复现

真实套用示例（全是他走过的路）：
- 视频重光 + FreeInit/FreeTraj 噪声操控（现成先验）+ 光照轨迹轴（没人控过）→ LightCtrl：training-free 方法 + 自造指标 PSNR_light
- MLLM + GRPO（借 DeepSeek-R1 红利）+ 四阶段可评测分解 → VAU-R1 + VAU-Bench + VAU-Eval 三件套
- DDIM 反演期注意力（被丢弃的中间信号）+ 视频编辑 → FateZero：零训练零 mask

## C3. Idea 原型库（7 种，对号入座）

| 原型 | 自问一句 | 内核模板 | 他的实例 |
| --- | --- | --- | --- |
| 迁移驱动 | 有没有已验证机制可以搬？ | "把 X 迁入 Y，贡献=解决适配矛盾（two main challenges…First…Second）" | Uformer（window attention×UNet）；Depth Distillation |
| 矛盾驱动 | 失效模式归因到什么根因？ | "失效命名→归因→双因各配一组件" | 1911 双 ghost；DEIM |
| 简化驱动 | 哪个昂贵组件能换掉？ | "替换后战绩不降反升" | 16% 参数；computation-free；training-free |
| 现象驱动 | 管线里有什么被忽略的信号/意外？ | "观察到→重解读→变成控制信号" | FateZero 反演注意力；EasyOmnimatte 朴素 LoRA 失败成方法核心 |
| 基准驱动 | 社区是不是没有战场？ | "没有就自己建，方法与数据互为护城河" | EvalCrafter；VAU-Bench |
| 能力反推 | 模型已经能做什么，说明它感知了什么？ | "能擦除⇒必感知⇒可微调成保留" | EasyOmnimatte |
| 尺度驱动 | 时长/分辨率/规模本身是不是矛盾？ | "把规模当轴" | CutClaw hours-long 超上下文 |

## C4. 问题表述句式（把大方向收敛成一句话）

1. **观察陈述式**（签名模板）：「X 与 Y 共享同一 [语义信息]，[任务] 只需学习 [差异部分]」
   例：*the shadow and shadow-free images share the same semantic information and shadow removal specifically and only needs to learn the shadow*（1911 :120）
2. **断言式**：we argue that… / we find that… / we hypothesize that the reasons are two-fold
3. **任务形式化式**："we decompose VAU into four progressive stages: Perception→Grounding→Reasoning→Conclusion"
4. **合格标准清单式**："An eligible X should meet several essential requirements… First… Second… Third…"——先立合格线，组件逐条认领，实验指标与需求严格闭环
5. **典型收敛链**：应用痛点 → 失效模式命名 → 归因到「被浪费的信号 or 被浪费的计算」→ 一句话设计原则 → 命名模块

## C5. 谱系法（下一篇从哪来）

**规则：Limitations 节 = 选题清单**（每条边都有 tex 证据）：
- FateZero 自述做不了 shape 编辑（swan→pterosaur）→ 等通用视频模型 → VideoCrafter1/2
- EvalCrafter Finding#4 "camera motion 无法用文本控制" → LightCtrl
- TaleCrafter 自曝 LoRA 多人组合失败 → 身份表征解耦（PhotoMaker 一脉）
- cun2018拼接定位 → ForgeryTTT（main.bbl:134 自引）

**操作步骤**（auto research 可直接执行）：
1. 取目标领域近 6–12 个月的 SOTA 论文，抓 Limitations/讨论节
2. 逐条过 §C1 过滤网（有免费信号内核的留下）
3. 套 §C3 原型选一个，用 §C4 句式写成一句话问题
4. 过 §C6 打分卡，触发一票否决即丢弃
5. 按 §C2 三件套规划产出（方法 + benchmark + 指标）

## C6. Idea 打分卡（1–5 分 × 8 维）

| 维度 | 5 分锚点 | 1 分锚点 |
| --- | --- | --- |
| 免费信号 ⛔ | 零标注零训练（von Kries 反转、反演注意力存回） | 需要新标注或从头训练 |
| 极简性 | 一段话+一行公式说清；computation-free | 多流/多阶段/多损失堆叠 |
| 失效模式可见性 | 有可命名视觉缺陷当 teaser 主角 | 只有指标层面的提升 |
| 公平可验证 ⛔ | 单卡复现 + 同预算镜像对照物 | 依赖大规模预训练或闭源模型 |
| 数据杠杆 | 顺带产出可公开数据集/基准 | 纯方法无资产沉淀 |
| 首发占位 | 「该红利下的第一个 X」 | 赛道已有 3+ 同位论文 |
| 谱系延续 | 长在自己（或领域 SOTA）某篇 Limitations 上 | 凭热点硬蹭 |
| 参数化原型 | 从人类工作流/物理定律借到参数 | 全靠端到端黑箱 |

⛔ = **一票否决项**（该维度 1–2 分直接丢弃）。其余维度建议总分 ≥24/40 再立项（此阈值为操作默认值，可按风险偏好调；非源自他本人）。

## C7. 2025/26 加分项（当前红利窗口）

- **training-free 编排**（LightCtrl / CutClaw / Seg-Agent 路线）：创新全在控制轴与编排层，不训模型
- **MLLM/Agent 当系统组件**（GPT-4 当组件从 TaleCrafter 2023 起没断过）
- **新增用户可控时序轴**：光照轨迹、音乐节拍
- **方法+基准+协议三件套** + 自造指标（PSNR_light）
- **极简 reward 美学**（0/1、IoU 分段函数）
- **诚实工程当卖点**而非负担
- 档案外推（推断，非语料内证据）：视频编辑/生成 × 更强推理先验（MLLM/RL）的「免费信号」型工作；「生成+理解」统一基准

---

# D. 反例对照（不要这样）

| ❌ 不要 | ✅ 要 |
| --- | --- |
| Teaser 用效果墙（一堆好看结果） | 五型选一，图本身就是论点 |
| 「Since the pioneering work of deep learning…」宏大开场 | 任务/现象一句切入 |
| 塞壳工程：多流、多阶段、大而全 pipeline | 极简机制替换，"without bells and whistles" |
| 训新基座/大规模预训练叙事 | 冻结基座 + 轻量适配；借现成先验 |
| 只加结果不谈效率 | FPS/Params/GMACs 每表必列 |
| 隐藏失败案例、只报好看的 | Failure Cases 小节 + 变差标红 |
| RW 贬损对手 | 只陈述失效场景，划界句收束 |
| Abstract 写成段落式流水账 | 失效模式命名 + 枚举结构 = 论文结构 |
| per-prompt 训练/用户标注当卖点 | "without per-prompt training or use-specific mask" 当卖点 |
| 色板混年代（淡彩 + 高饱和混用） | 全文统一当前期色板 |
| Idea 凭热点硬蹭、无管线内依据 | 长在某篇 Limitations 上 / 有免费信号内核 |
| 纯方法无论文外资产 | 顺带产出数据集/基准/协议 |

---

# E. 交稿前检查单

**Idea 侧**
- [ ] 过了 §C1 过滤网，无一票否决项
- [ ] 打分卡达标；谱系可追溯（能指出来长在哪篇 Limitations 上）
- [ ] 产出按三件套规划（方法 + benchmark/数据集 + 指标）

**画图侧**
- [ ] Teaser 是五型之一，图本身是论点，不是效果墙
- [ ] 全文色板同年代；Ours 红实线加粗、基线虚线退后
- [ ] 每张表有效率列 + 加粗/下划线约定 caption 声明
- [ ] 每张图 caption 三层结构、粗体导语开头；多样本图有 (a)(b)(c) 指认
- [ ] 定性对比图 Ours 紧邻 GT、指标下标加粗、差分图放大拼接
- [ ] Abstract 有失效模式命名 +（替代理划界）+ 复现级数字或定性收尾（按任务选）
- [ ] Intro 缺口枚举与贡献清单/组件严格同构
- [ ] we argue / the first X 各至少出现一次（自然，不堆砌）
- [ ] RW 每段以划界句收束、无贬损词
- [ ] 有镜像对照物或参数量对齐实验
- [ ] 跨数据集 OOD 实验 + 超参谷形扫描
- [ ] Failure Cases / Limitation 独立成节，诚实自曝
- [ ] 代码 URL 就位；开源数据集写明 "will be released"
- [ ] 伦理/误用段落（涉及生成/编辑真实性时）

---

# F. 文件索引

| 内容 | 路径 |
| --- | --- |
| 完整风格档案（选题/品味/Idea 也在这） | [profile.md](profile.md) |
| 逐篇证据卡 ×20（tex:行号级证据） | [analysis/](analysis/)`<arxiv_id>_evidence.md` |
| Skill 规程 | [../../SKILL.md](../../SKILL.md) |

> 语料（PDF+源码+报告，约 564MB）与盲测留样未随仓库分发，采集命令见本目录 [README.md](README.md)。

# 学者档案：存晓东 Xiaodong Cun / GVC Lab（大湾区大学）(Scholar Style Profile)

> 蒸馏自 10 篇一作/通讯/主导论文（2019–2025），全部结论附证据。语料与逐篇证据卡见本目录 `corpus/` 与 `analysis/`。
> 用途边界：复刻写法与思维方式，不搬运内容、不冒充本人。

## 〇、语料清单 (Corpus Manifest)

| # | 论文 | 年份/会议 | ArXiv ID | 作者位置 | 类型 | 参与蒸馏 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Improving the Harmony of the Composite Image by Spatial-Separated Attention Module (S²AM) | 2019→TIP 2020 | 1907.06406 | 一作 | 方法 | 是 |
| 2 | Towards Ghost-free Shadow Removal via DHAN and Shadow Matting GAN | 2020 AAAI | 1911.08718 | 一作 | 方法+数据 | 是 |
| 3 | Defocus Blur Detection via Depth Distillation | 2020 ECCV | 2007.08113 | 一作 | 方法 | 是 |
| 4 | Uformer: A General U-Shaped Transformer for Image Restoration | 2022 CVPR | 2106.03106 | 二作+通讯 | 架构 | 是 |
| 5 | Learning Enriched Illuminants for Cross and Single Sensor Color Constancy | 2022 期刊 | 2203.11068 | 共同一作 | 方法 | 是 |
| 6 | FateZero: Fusing Attentions for Zero-shot Text-based Video Editing | 2023 ICCV | 2303.09535 | 二作(共同贡献) | 方法 | 是 |
| 7 | TaleCrafter: Interactive Story Visualization with Multiple Characters | 2023 ACM MM | 2305.18247 | 三作 | 系统 | 是 |
| 8 | EvalCrafter: Benchmarking and Evaluating Large Video Generation Models | 2024 CVPR | 2310.11440 | 共同一作 | Benchmark | 是 |
| 9 | DEIM: DETR with Improved Matching for Fast Convergence | 2025 CVPR | 2412.04234 | 三作 | 方法 | 是 |
| 10 | VAU-R1: Advancing Video Anomaly Understanding via Reinforcement Fine-Tuning | 2025 preprint | 2505.23504 | 末位+通讯 | 方法+Benchmark | 是 |
| H | SadTalker (盲测留样) | 2023 CVPR | 2211.12194 | 二作(主导) | 方法 | 否（留作盲测） |

- **时期覆盖**：2019–2026（澳门大学一作期 → 华为/腾讯效率期 → 腾讯生成期 → 大湾区 GVC Lab 建 lab 期）
- **类型覆盖**：方法 7 / Benchmark 2 / 系统 1（主语料 10 篇）
- **扩充语料（已蒸馏，证据卡同在 analysis/）**：DocShadow 2308.14221（ICCV23 末位通讯）、DepthTTT 2403.04258（CVPR24 末位通讯）、ForgeryTTT 2410.04032（末位通讯）、EasyOmnimatte 2512.21865（CVPR26 末位通讯）、FairyGen 2506.21272（末位通讯）、VideoCrafter2 2401.09047（中间作者，品味信号）、CoordFill 2303.08524（二作）、CurveHarmonization 2109.05750（共同一作）、LightCtrl 2603.27083（ICLR26 投稿，末位通讯）、CutClaw 2603.29664（ECCV26 模板，末位双通讯）——共 20 篇参与蒸馏

---

## 一、视觉与表格指纹 (Visual & Table Fingerprint)

### 1. 调色板（三阶段演化，用错时期会被识破）
- **绘图主色板（2026 当前，供 `plot_style_template.py --from-profile` 使用）**：
  - **Ours 主色**：`#d62728`（红实线加粗；证据：DEIM teaser 实看）
  - **Baselines**：`#1f77b4` `#2ca02c` `#9467bd`（一律虚线/点线退后）
  - **Gray 注释**：`#7f7f7f`（图内虚线箭头倍数标注）
  - **架构图淡彩（draw.io 端，非曲线用）**：`#DAE8FC` `#D5E8D4` `#FFE6CC` `#FFF2CC`
- **2019–2020 澳门期**：无精选色卡——`\definecolor` 0 处（1907/1911 corpus report §1），颜色是 PPT/draw.io 默认高饱和：亮红 Encoder、紫 Decoder、橙 Attention、棕褐/khaki 竖条、青色 I/O 盒（证据：1911 fig2–4 实看；1907 fig1.png 实看）。**此期为原生手绘风，图内甚至有拼写错误**（"Aggreataion"，1911 fig2；"ablution study"，1911 :288）。
- **2021–2023 成熟期**：低饱和 draw.io 淡彩系——淡蓝 #DAE8FC 系、淡绿 #D5E8D4 系、淡橙 #FFE6CC 系、淡黄 #FFF2CC 系（证据：TaleCrafter fig/unet.pdf 实看取色；EvalCrafter pipeline.pdf 同系；Uformer overview.pdf 蓝灰主色+橙/绿点缀）。LaTeX 端几乎零配色（TaleCrafter 0 处、EvalCrafter 2 处且为链接色）——**颜色全部在绘图工具端实现，正文 .tex 不定义图色**。
- **2024–2025 GVC 期**：matplotlib 写实路线（DEIM：红 #d62728 Ours 实线、蓝 #1f77b4 基线虚线、灰注释箭头）与 xkcd 手绘卡通路线（VAU-R1 bar_chart.pdf 手绘字体柱状图）并存；新增**表格行底色语义**：`\rowcolor[gray]{0.95}` 标 Ours 行（DEIM 5-experiments.tex:36）、`lightyellow RGB(255,255,204)` 标 OOD 测试行（VAU-R1 arxiv.tex:72+542）。
- **通用规则**：Ours 红/深色实线加粗，基线一律虚线/点线退后（DEIM teaser 实看）；图内直接写关键数字——红字标基线失败 "0.00"、绿字标增益 "+5.89"（VAU-R1 bar_chart 实看）、灰箭头标 "2× faster in convergence"（DEIM coco_epochs_vs_ap.pdf 实看）。
- **跨稿复用视觉词汇**（GVC 期签名）：flame/snowflake 图标标可训练/冻结模块（DocShadow/DepthTTT/ForgeryTTT 三篇同款）；同一 DarkGreen 色定义跨稿件复用；TTT 训练动力学入 teaser（DepthTTT：Step1 Loss=0.36→Step3 0.22 递减曲线）；表格里「变差」的数字标红（DepthTTT/ForgeryTTT）——诚实编码进视觉语言。

### 2. Teaser (Figure 1) 叙事模式——五型轮换，从不用"纯效果墙"
- **机制自解释型**：teaser=微缩 Introduction，"任务 I/O + 为什么需要该模块"一图讲完（1907 fig1.png：encoder→decoder + 两个 S²AM 模块拆解；caption 从 "The basic idea of our method" 讲到指向 Section 3）。
- **失效模式主角型**：标题卖点（ghost-free）直接可视化——黄框标输入、红框=前人 ghost 瑕疵、绿框=本文修复（1911 fig1.png）。
- **效率-性能权衡图**：PSNR vs GMACs(log) 散点，Ours 红星居左上，caption 仅一句（Uformer macs_uformer.pdf）。
- **训练配方图**：Figure 1 画训练管线而非网络（2203 mainpage.pdf：UIP/SAF 双管线；本质是"免费标签机"的一图化）。
- **量化曲线前置**：训练前期就放两张实验曲线，子图标题就是卖点句 `\textbf{Faster}` / `\textbf{Better}`（DEIM teaser.tex:38/45）；反差柱状图 "SFT 0 分 vs RFT 赢分"（VAU-R1 bar_chart.pdf）。
- **Caption 三层结构**（成熟期定型）：粗体结论导语 → 机制/图例展开 → 结论或观图提示。例：`\textbf{Zero-shot text-driven video editing.} We present a zero-shot approach... without any optimization for each target prompt.`（FateZero teaser.tex:44）；`\textbf{Effectiveness of Reinforcement Fine-Tuning.} We compare... This demonstrates that RFT enhances...`（VAU-R1 arxiv.tex:113-124）。

### 3. 架构图 (Pipeline Figure)
- **框架图与模块图两级分解**：框架图管数据流（Uformer overview.pdf (a)），模块图管层结构（(b)(c) 放大 LeWin/Modulator）；粗细两极并存——teaser 粗粒度示意 vs CAM.jpg 画到 pooling→FC→sigmoid 算子级（1907）。
- **张量形状写在图顶部与公式严格对应**（Uformer overview 顶部 3×H×W→…→16C×H/16×W/16）；图内变量（s^src_t、c^edit_t）全部出现在正文公式（FateZero framework.tex:7）。
- **真实例子直塞方法图**：DEIM 用真实狗照片讲 O2M/Dense O2O 匹配、3D 损失地形图（viridis 曲面标红星）；VAU-R1 用奥特曼漫画帧当示例；损失函数画成 3D 地形是少见签名做法。
- **工具链**：draw.io（淡彩圆角块、3 倍放大核心组件）+ matplotlib（曲线/散点/曲面）+ PowerPoint（早期）；核心组件在图中放大 3 倍突出（TaleCrafter pipeline.pdf 的 C-T2I）。
- **定性对比固定协议**：行/列序 Input→(旧→新)各方法→Ours→Target；Ours 紧邻 GT（2007 fig6/7）；每方法下标 PSNR 且 Ours 加粗（Uformer sidd 图；2203 标角度误差 0.10°）；差异用 **absolute difference colormap 放大 10×/30× 拼在结果下方**（1907 figurecoco.tex:57）——用差分图代替肉眼对比，是他的定性签名。

### 4. 表格美学
- **线型演化**：2019–2020 竖线全封闭 `|l|c|c|` + `\hline\hline` 表头（1907/1911）→ 2021 起向三线表过渡（Uformer `\toprule…\hline…\bottomrule` 混竖线分组；FateZero 严格 `\toprule/\midrule/\bottomrule` + `\cmidrule` 无竖线）。
- **最优/次优**：加粗最优 + 下划线次优，caption 明写约定 "The best results are bold and the second best are underlined."（2203 experiment.tex:599）；早期整行加粗/整行下划线（1911 :264-265），后期逐格标注（FateZero）。
- **公平细节**：基线带年份下标 Yang₁₂′ 并在 caption 解释（1911 :249）；不用额外数据/后处理前置声明（2007 exp.tex:3）；对手 FPS 更高照样给对手加粗（2007 主表 FPS 行 BASNet 90.9 加粗，自己 35.7 不加粗）；backbone 不同的方法用 `\hline` 分组不混排冒充 SOTA（1911 :333-336）。
- **数字排版**：小数位统一（RMSE/PSNR 2 位、SSIM 早期 4 位后期 2 位、角度 2 位、FateZero CLIP 3 位）；指标带方向箭头 `PSNR↑ / FID↓`；`-` 表示缺数据。
- **行底色/彩字承担语义**（2024 起签名）：灰底=Ours 行、浅黄底=OOD 行；蓝字=提升、红字=下降（2203 experiment.tex:475）。
- **消融表**：`+D / +D+SRFB / +D+RFB+SA / Full` 增量开关列（2007 exp.tex:75）或 `\checkmark/-` 开关列（Uformer exp.tex:634-640）。

---

## 二、写作修辞指纹 (Writing & Rhetoric Fingerprint)

### 1. Abstract 句序骨架（三段演化）
- **观察式**（2019–2020）：①任务一句话 ②**失效模式具体命名**（"two types of ghosts: color in-consistencies…or artifacts on shadow boundaries"）③总纲 "we tackle these issues in two ways" ④斜体观察宣言 "we start from an empirical observation: …" ⑤方法（命名模块）⑥量化战绩 ⑦代码 URL。证据：1911 :103；1907 main.tex:450-457。
- **双路线对置变体**（盲测补充，SadTalker）：失效命名后不止划现有路线的界，还把「直觉上的替代理」也划掉——"We argue that these issues are mainly because of learning from the coupled 2D motion fields. On the other hand, explicitly using 3D information also suffers problems of stiff expression and incoherent video."（holdout 00_abstract.tex:5）——两条路都堵死，自己的路线成为唯一出口。
- **宣言式**（2021–2022）：**第一句即 "In this paper, we present X"**，背景句写好后被注释删掉（Uformer main.tex 定稿 vs 注释行 890）；First/Second 双设计 + "Powered by these two designs" 收束 + "without bells and whistles"。
- **链式/双资产式**（2024–2025）：方案 A 引出新副作用 → 方案 B（DEIM：Dense O2O → low-quality matches → MAL），主动暴露自己方案的缺点再解；方法名+基准名并列加粗，各配一个矛盾（VAU-R1）。
- 长度：6–9 句；量化句密度随时期上升（DEIM 给到 "53.2% AP in a single day on a 4090" 复现级数字），但**收尾有定性变体**——"We conducted extensive experiments to demonstrate the superiority of our method in terms of motion and video quality."（SadTalker，无数字无代码 URL）——纯定性收尾用于强调感知质量的任务，量化收尾用于效率/检测类任务。
- 组件介绍连接词："Precisely, we present X to learn Y by Z" / "As for the head pose, we design X via Y"（SadTalker）——First/Second 之外的第三种组件展开法。

### 2. 标志性短语库 (Signature Phrases)
| 短语 | 功能 | 原文例句 |
| --- | --- | --- |
| "we argue that…" | 立论动词，几乎每篇必用 | "we argue that training on a limited dataset restricts…"（1911 :103）；"we argue that the accuracy of DBD is highly related to scene depth"（2007 abstract） |
| "for the first time / the first X / We make the first step" | 占坑定位，Abstract/Intro/Conclusion 三现 | "We make the very first step to evaluate the general T2V models"（EvalCrafter 01_intro.tex:18） |
| "simple yet effective" | 方法自我定性 | FateZero 01_intro.tex:40；2007 method.tex:29 |
| "without bells and whistles" | 无 trick SOTA 声明 | Uformer abstract + intro.tex:62 双现 |
| "by a large margin" | 战绩定性 | 1911 :103；2203 abstract 末句 |
| "However, …" 段尾划界 | RW 每段收束 | 1911 :141；FateZero 02_related.tex:30 |
| "Differently, our …" | RW 划界（2022 变体） | 2203 relatedwork.tex 三处 |
| "In contrast, we propose a novel yet straightforward approach" | 先破后立 | DEIM 2-introduction.tex |
| "we hypothesize that the reasons are two-fold. ①…②…" | 双因拆解立论 | DEIM intro（\ding{182}/\ding{183} 带圈编号） |
| "make a big step" | 早期扩展宣言 | 1907 main.tex:455 |
| "It is clear that / Obviously," | 实验段收束 | 1911 :304；2203 fig_canon5d caption |
| "Notice that / Note that" | 补充限定 | 1911 :200, :292 |
| "It is much easier to collect A than B" | 数据经济学论证 | 1911 :123 |
| "data-efficient / computation-free / with only 16% parameters" | 效率卖点句位 | DEIM RW；2203 abstract |
| "built upon the commonly used X" | 谦逊借力开场 | DocShadow/DepthTTT/ForgeryTTT 各一篇 |
| "to the best of our knowledge, (the) first" | 首发・变体 | ForgeryTTT；2007 intro.tex:22 "first attempt" |
| 悖论设问句 | 摘要/引言钩子 | "training high-quality video models without using high-quality videos"（VideoCrafter2 01_intro.tex:15）；"We raise a question: What makes the inpainting hard..."（CoordFill）——设问仅用于悖论场景，常规立论仍用断言式 |

### 3. Introduction 推进逻辑
- P1 不搞宏大叙事，从**任务定义/生活场景/自然现象/应用**一句切入（1907 从 Photoshop 拼图、1911 从 "Shadows are a common phenomenon in nature"）。
- P2 前人路线按时间线各给一句局限（\citeauthor 句式）。
- P3 缺口段双因/三连枚举："two major drawbacks. First,… In addition,…"（1911 :118）→ "(i)…(ii)…(iii)…" 罗马数字（VAU-R1）；**枚举的结构=论文结构**（两个 gap 对应 two ways，两因对应两组件）。
- P4 **斜体观察句/断言句领起方案**："our key observation is: *…share the same semantic information and only needs to learn the shadow*"（1911 :120；1907 intro.tex:83 同模板换词）——同一观察句模板跨任务复用是他的核心签名。
- P5 框架走读 Firstly/Then/Moreover/Finally；贡献清单收尾。
- 物理第一性切入：从成像原理推问题（2007 从 DOF≈2NCD²/f² 推出"整个领域在用 2D 视角看 3D 现象"）。

### 4. Related Work 组织法
- **分类法**（3 个 run-in bold 段头按任务/技术路线分派，非时间线）；段内可再按代际时间线（GAN→transformer→diffusion，TaleCrafter）。
- **每段以划界句收束**：However / Differently / In contrast / "To bridge this gap, we…"；RW 段落标题直接复用 Intro 拆出的矛盾名（DEIM：Increasing positive samples / Optimizing low-quality matches）。
- 对前人温度中性：指失效场景不贬损人格（"may fail when the track is lost"）；有礼貌性让步（"although our network is not particularly designed for shadow detection, it still gets better results"，1911 :315）；引用自己前作显式接线个人研究线（2007 related.tex:9 引 cun2018depth）。

### 5. 标题与命名学
- **冒号结构主导**：「方法名: 机制描述+收益词」（DEIM: DETR with Improved Matching for Fast Convergence）；「Towards+理想态 via 组件 A and 组件 B」（1911，卖点与两大组件全进标题）。
- **命名即论点**：把经典概念一字改动当标题（Knowledge→**Depth** Distillation，2007）；斜体下划线标注缩写字母来源（FateZero: \underline{F}using \underline{A}ttentions…）；**-Crafter 词缀系列**（TaleCrafter/EvalCrafter/VideoCrafter/ScaleCrafter/DepthCrafter/StereoCrafter——系列化占位意识）；R1 后缀借 DeepSeek-R1 认知（VAU-R1）。
- 方法名可读朴素：Uformer、DHAN、SMGAN、DEIM、CoordFill；组件名功能描述式（Dense O2O、Matchability-Aware Loss）；**给每个设计决策单独起名**（S²AM→S²ASC→S²AD 变体各自命名，1907 method.tex:127-129）。
- 基准命名 = 任务缩写+Bench（VAU-Bench）+ 配套评测协议（VAU-Eval）——**方法+基准+协议三件套**。

### 6. 贡献清单范式
- 组件式三条（结构+数据/模块+实验），每条「提出 X + 机制从句/立即给结果」："Once trained using randomly generated labels, our model achieves state-of-the-art performance…"（2203 P5）。
- 首条必是 first 宣言；末条必是战绩+效率双卖点（"halving training costs… establishes a new SoTA"，DEIM）。
- Benchmark 论文把**发现清单当第三贡献**（EvalCrafter Finding #1–#6）。

---

## 三、选题品味 (Research Taste)

### 1. 创新类型梯队分布
| Tier | 占比 | 代表 | 证据 |
| --- | --- | --- | --- |
| Tier 2 极简机制替代复杂工程（主力） | 6/10 | S²AM（hard-coded mask 免费先验替代学习式 attention）、Uformer（window attention+UNet 替代全局 attention）、DEIM（mosaic/mixup 增目标，不加解码器，"computation-free"） | 1907 method.tex:40-43 一行公式；DEIM RW |
| 免费信号/免费标签（方法论内核） | 4/10 | von Kries 方程反转造跨传感器样本（2203）；DDIM 反演期注意力存回生成期（FateZero）；物理成因当软标签（2007 depth distillation） | 2203 introduction.tex:52；FateZero 01_intro.tex:43 |
| 数据经济学/造数据并公开 | 4/10 | S-COCO 43k+S-Adobe5K 36k（1907，"We will public these two synthesized datasets"）；SMGAN 合成管线（1911）；VAU-Bench（2505）；"It is much easier to collect A than B" | 1907 method.tex:185-204；1911 :123 |
| 基准/评测驱动（建 lab 后加重） | 2/10 | EvalCrafter 700 prompts+17 指标+人偏好对齐；VAU-Bench 首个 CoT 视频异常基准 | 2310 00_abstract.tex:3 |

### 2. 选题过滤网
- **他做**：①管线里已被算出来但要被丢弃的中间信号（注意力图、反演 latent、白平衡方程的可逆性）——"免费"是核心判据；②**给编辑操作找参数化原型**：从人类工作流/专业工具里提取可学习参数——Photoshop 曲线→逐通道染色公式（CurveHarmonization intro.tex）、填洞→只查询洞内坐标（CoordFill）、重光→光图掩码内注噪（LightCtrl）、剪辑→时间戳三元组（CutClaw）；③失效模式可见、可命名的底层/编辑任务（ghost、inharmonious、flickering）；④单卡可复现/免训练的效率叙事（"IPT: 32 V100 / Ours: Single GPU"，Uformer intro.tex:94-98 注释稿；2080Ti 24ms（CoordFill）→ 2026 training-free（LightCtrl））；⑤新模型红利出现 6–12 个月内做"首次适配"（Transformer→restoration 2021；扩散→视频编辑 2023；GRPO→视频理解 2025）；⑥**数据矛盾切入**：标注贵/数据少/伪造进化快于收集→自造数据集当主贡献（DocShadow "10 times larger"）或零标注测试时自适应（TTT 双插槽配方：辅助任务+更新策略，复用于 DepthTTT/ForgeryTTT）。
- **他不做**：不训新基座/不做大规模预训练（借力现成权重："leveraging the prior knowledge of large language and T2I models"，TaleCrafter abstract）；不做 per-prompt 优化/用户交互式标注（FateZero 卖点即 "without per-prompt training or use-specific mask"）；不堆多流/多阶段工程（2007 exp.tex 批 multi-stream "heavy and computationally inefficient"）；纯理论/无实验验证的论文语料中为零。

### 3. 消融实验哲学
1. **公平性声明前置**：同预算对照物自造——把 LeWin 全换 ResBlock 造 UNet-T/S/B 镜像（Uformer exp.tex:586-599）；参数量对齐（"increase the channels…to match the parameters"，1907 experiment.tex:185）。
2. **plug-in 通用性**：模块插入 3 个 backbone 全涨（1907 experiment.tex:39）；即插即用跨检测器（DEIM+RT-DETRv2/D-FINE）。
3. **机制可视化闭环回观察句**：attention 热图证明"gated attention 只亮局部 vs Ours 覆盖整个影子"（1911 fig8）；"This fact perfectly explains our assumption"（1907 experiment.tex:262）。
4. **报弱结果不隐瞒**：shifted-window "only slightly better"（Uformer method.tex:117）；消融行比完整模型还好照实加粗（1907 tableevaluation.tex:23）；基线 0.00 失败原样呈现（VAU-R1）。
5. **中间产物单独评测**：合成影子质量立表自证（1911 :380）；正样本数分布直方图（DEIM one_and_many.pdf）。
6. **跨数据集/OOD 必做**：ISTD→SRD/SBU zero-shot（1911 :400）；CrowdHuman（DEIM）；UCF-Crime 行底色标注 OOD（VAU-R1）。
7. **超参扫到两端呈谷形**：γ∈{0.01…5}（2007 exp.tex:105）；attention loss 比例 0.01×–10×（1907 psnr.pdf）。
8. **专设辩护小节**对抗审稿人替代解释："Relationship with RNN"、"Comparison with CROP"（2203 experiment.tex:727-728）。
9. 效率是一等公民：FPS/GMACs/Params 每表必列；推理时间精确到 0.012s（1907 experiment.tex:7）。
10. **受控扰动探针**：同架构同数据造 full/partial 双基座，用参数扰动（PERTB）读出耦合强度——方法是从实验里"读"出来的（VideoCrafter2）；「先分析后设计」，分析发现单列成贡献条目（EasyOmnimatte block-wise 贡献分数曲线 Fig.3）。
11. **诚实升级为视觉语言**：TTT 后变差的数字标红、对手训练集重叠加 † 脚注、JPEG 鲁棒性输给 TruFor 照写（DepthTTT/ForgeryTTT）；消融表中 "w/o Reviewer" 反超自己完整版照样加粗呈现（CutClaw）。

### 4. 选题时间线
| 年份 | 问题 | 方法一句话 | 延续/跳变 |
| --- | --- | --- | --- |
| 2018 | 深度辅助视图合成 | depth 当视图合成先验 | 起点（cun2018depth，2007 related.tex:9 引用） |
| 2019 | 图像调和/拼接取证 | 区域差异共享语义观察 + S²AM | 观察句模板确立 |
| 2020 | 阴影去除 | 同观察句平移 + SMGAN 造数据 | 配方平移 + 数据经济学升级 |
| 2020 | 散焦检测 | 深度当软标签（蒸馏） | 深度主线回收 |
| 2021–22 | 图像恢复通用骨架 | window attention+UNet（Uformer） | 从"借任务先验"到"借架构机制" |
| 2022 | 色彩恒常 | 物理方程当免费标签机 + 16% 参数压缩 | 免费信号+效率双母题合流 |
| 2023 | 视频编辑 | 反演注意力当免费控制信号（FateZero） | 进入扩散时代，方法论不变 |
| 2023 | 故事可视化/评测 | LLM 当系统组件；T2V benchmark | Crafter 系列化 + GPT-4 入管线 |
| 2022 | 图像调和（曲线参数化） | 把 Photoshop 曲线当可学习参数（CurveHarmonization） | 「参数化原型」主线确立，intro 预告 relighting/AR 伏笔 |
| 2023 | 文档阴影去除 | 大规模真实数据集 + 频域方法（DocShadow） | DHAN 谱系回归 + 数据经济学 |
| 2023 | 高分辨率填补 | 只查询洞内坐标（CoordFill） | 参数化原型 + 分辨率第一维 |
| 2024 | 视频生成数据配方 | 无高质量视频训出高质量模型（VideoCrafter2） | 受控探针方法论（PERTB） |
| 2024 | 零样本 VOS/篡改定位 | TTT 配方（辅助任务+更新策略）×2 | 零标注自适应，深度/拼接线索资产回收 |
| 2025 | 视频分层/卡通生成 | 生成先验重做 matting；角色→风格传播（EasyOmnimatte/FairyGen） | 低层视觉问题意识当生成选题罗盘 |
| 2026 | 可控重光/长视频剪辑 | training-free 编排 + 可控时序轴（LightCtrl/CutClaw） | 不训模型，创新在控制轴与编排；尺度驱动（hours-long） |
- **结论**：表面多点开花（low-level→生成→检测→视频理解→agentic 剪辑），内核双线——**「管线内免费信号 + 极简机制 + 数据经济学 + 效率执念」**与**「给编辑操作找参数化原型」**（曲线→坐标→光图→时间戳），随大模型红利换战场；每 2–3 年借一次新范式红利做"首次适配"。近年漂移：从图像到视频到 agentic 工作流、从训练模型到 training-free 编排、从单方法到「方法+基准+协议」组合拳、可控性成为新卖点轴（光照轨迹/音乐节拍）、lab 品牌（GVCLab org）化运营。

---

## 四、Idea 设计模式 (Idea Design Patterns)

### 1. Idea 原型分布
| 原型 | 篇数 | 代表 | 一句话内核 |
| --- | --- | --- | --- |
| 迁移驱动 | 6 | Uformer、2007、VAU-R1、TaleCrafter | 把已验证机制/先验迁入新任务，贡献=解决适配矛盾（"two main challenges…First…Second"，Uformer method.tex:69） |
| 矛盾驱动 | 5 | 1911、DEIM、2203 | 失效模式命名→归因根因→双因各配一组件 |
| 简化驱动 | 5 | 2203（16% 参数）、DEIM（computation-free）、Uformer（单阶段单损失）、LightCtrl（training-free） | 替换掉昂贵组件后战绩不降反升 |
| 现象驱动 | 3 | FateZero、EasyOmnimatte（朴素 LoRA 失败的意外现象成方法核心）、EvalCrafter Findings | 观察到中间信号/反直觉现象，重新解读它 |
| 基准驱动 | 3 | EvalCrafter、VAU-Bench、DocShadow（"10 times larger"） | 社区没有战场→自己建战场，方法与数据互为护城河 |
| **能力反推**（新识别） | 1 | EasyOmnimatte | 「能擦除效果⇒必感知了效果⇒可微调成保留」（sec/intro.tex:38-40）——从模型已有能力反推可控性 |
| 尺度驱动 | 1 | CutClaw（hours-long 超上下文） | 把时长/分辨率/规模本身当矛盾轴 |

### 2. 问题表述句式
- 观察陈述式（无设问）："X 与 Y 共享同一语义信息，任务只需学习差异部分"（1907 intro.tex:83 / 1911 :120 同模板）。
- 断言式："we argue that…"/"we find that…"/"we hypothesize that the reasons are two-fold"。
- 任务形式化式："we decompose VAU into four progressive stages: Perception→Grounding→Reasoning→Conclusion"（VAU-R1）。
- 合格标准清单式："An eligible story visualization should meet several essential requirements… First… Second… Third…"（TaleCrafter 00_intro.tex:25）——先立合格线，组件逐条认领，实验指标与需求严格闭环。
- 典型收敛链：应用/现象痛点 → 失效模式命名 → 归因到「被浪费的信号或被浪费的计算」→ 一句话设计原则 → 命名模块。

### 3. Idea 谱系图
```
cun2018depth(深度先验) ──[深度是可借的先验]──► 2007 Depth Distillation ──[深度一致性当免费自监督]──► DepthTTT(2403)
cun2018image(拼接定位, ECCV-W) ──[伪影取证资产]──► ForgeryTTT(2410, main.bbl:134 自引)
1907 S²AM(区域观察句+attention loss) ──[配方平移]──► 1911 Shadow Removal ──[造数据升级]──► DocShadow(2308)
1911 局限(合成域差距) + Uformer StyleGAN modulator(GAN 背景) ──[生成式转向]──► FateZero ──[自述"等通用视频模型"]──► VideoCrafter1/2
CurveHarmonization intro 伏笔(relighting/AR) ──[参数化原型延续]──► LightCtrl(2603 光图掩码注噪)
VideoCrafter2 外观/运动解耦 ──[解耦演化]──► FairyGen identity/motion 两阶段
TaleCrafter 局限(LoRA 多人组合失败) ──[身份表征解耦]──► (PhotoMaker 一脉方向)
EvalCrafter Finding#4(camera motion 不可控) ──[给自己可控生成出题]──► LightCtrl(2603)
DEIM(训练效率价值观) + DeepSeek-R1 红利 ──[RL 迁移]──► VAU-R1 ──[自述缺因果推理]──► 下一代
```
- 谱系规律：**每篇论文的 Limitations 节是下一篇的选题清单**（FateZero 自述 swan→pterosaur 做不了→等更强视频先验；EvalCrafter 自述 700 prompts 太少+MLLM-as-metric 预告；TaleCrafter 自曝多人组合不满意）。
- **外推**（依据上述规律）：他当下最可能的下一篇 = 视频编辑/生成 × 更强推理先验（MLLM/RL）的"免费信号"型工作，或为 GVC Lab 补「生成+理解」统一基准。

### 4. Idea 记分卡（给新 Idea 打分，1–5）
| 维度 | 问题 | 5 分锚点 |
| --- | --- | --- |
| 免费信号 | 是否利用管线里已被计算/物理定律给定的免费量？ | von Kries 反转、反演注意力——零额外标注零额外训练 |
| 极简性 | 能否一段话+一行公式说清？是否替换而非叠加工程？ | DEIM "computation-free"；拒绝多流/多阶段 |
| 失效模式可见性 | 痛点是否有一个可命名的视觉缺陷可做 teaser？ | ghosts、flickering、inharmonious |
| 公平可验证 | 单卡能否复现？有没有同预算镜像对照物？ | "single day on a 4090"、UNet-T/S/B 镜像 |
| 数据杠杆 | 顺带能否造出可公开的数据集/基准？ | S-COCO、VAU-Bench、DocShadow |
| 参数化原型 | 编辑操作是否找到了从人类工作流/物理定律借来的可学习参数？ | Photoshop 曲线→染色公式；剪辑→时间戳三元组 |
| 首发占位 | 是否是"该红利下的第一个 X"？ | "the first zero-shot video editing" |
| 谱系延续 | 是否长在自己某篇的 Limitations 上？ | FateZero→VideoCrafter |

---

## 五、盲测验证记录 (Validation)

- **留样论文**：SadTalker: Learning Realistic 3D Motion Coefficients for Stylized Audio-Driven Single Image Talking Face Animation（CVPR 2023, 2211.12194，蒸馏期间未读）
- **写作盲测**（2026-09-30）：仅凭档案 + 标题仿写 Abstract 后与原文并排比对。
  - **命中**：①失效模式清单式命名（原文 "unnatural head movement, distorted expression, and identity modification" ↔ 仿写同构三连）；②归因句位完全一致（原文 "We argue that these issues are mainly because of learning from the coupled 2D motion fields" ↔ 仿写 "We argue that..."）；③宣言式提案 "We present SadTalker, which..."；④双组件分别建模（"individually" ↔ 仿写 "separately"）；⑤"extensive experiments" 收尾。
  - **差距（已修入档案 §二.1）**：①原文把「直觉替代理」也划界（"explicitly using 3D information also suffers..."），档案原只有 RW 划界；②原文为定性收尾（无数字无代码 URL），档案原把"战绩+代码 URL"当成通用规则；③连接词 "Precisely, / As for X" 未收录。
  - **污染声明**：仿写中组件名 ExpNet/PoseVAE 来自训练语料先验（SadTalker 为知名工作），不计入命中；结构层命中有效。
  - **判定**：结构层像，细节层两处偏差已回修档案——按 skill 标准记「通过（含回修）」。
- **插图盲测**（2026-09-30）：`plot_style_template.py --from-profile` 渲染 /tmp/blindtest_from_profile.png。**命中**：Ours 实线加粗居上、基线虚线退后、浅灰虚线网格、衬线字体、少墨水。**差距**：脚本从档案抓到 draw.io 淡彩系（#D5E8D4/#FFE6CC/#FFF2CC）作主色，而 2024–25 matplotlib 期 Ours 应为 #D62728 红实线（脚本日志已自曝 2 个未映射色值）——三阶段色板需显式区分，建议给脚本加 `--era {2019,2021,2024}` 参数或在档案中单列「绘图主色板」小节。
- **验证日期与结论**：2026-09-30，**通过（写作含两处回修；绘图构图通过、色板选择待脚本小改）**。

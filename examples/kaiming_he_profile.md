# 学者档案范例：何恺明风格解构 (Scholar Profile: Kaiming He)

> 本档案为**压缩版演示范例**，用于展示模板各字段的填写粒度与证据标注方式。真实蒸馏时证据应更密集（每条结论 2 处以上佐证），并附盲测验证记录。

## 〇、语料清单 (Corpus Manifest)

| # | 论文 | 年份/会议 | 作者位置 | 类型 | 参与蒸馏 |
| --- | --- | --- | --- | --- | --- |
| 1 | Deep Residual Learning for Image Recognition | 2016 CVPR | 一作 | 方法类 | 是 |
| 2 | Feature Pyramid Networks for Object Detection | 2017 CVPR | 一作(共) | 方法类 | 是 |
| 3 | Mask R-CNN | 2017 ICCV | 一作 | 方法类 | 是 |
| 4 | Momentum Contrast (MoCo) | 2020 CVPR | 通讯 | 方法类 | 是 |
| 5 | Masked Autoencoders Are Scalable Vision Learners | 2022 CVPR | 通讯 | 方法类 | 否（盲测留样） |

## 一、视觉与表格指纹

- **调色板**：Ours 主色经典蓝 `#1F77B4`；对比方法灰 `#7F7F7F` 或橙 `#FF7F0E`；无渐变、无阴影、无 3D 特效（证据：ResNet/MoCo/MAE 各主图；`#1F77B4` 为 Matplotlib 默认蓝，推断其图表以 Matplotlib 直出——推断项已标注）。
- **Teaser 模式**：**范式对比型**为主——MoCo Fig.1 三栏对比 (a) end-to-end / (b) memory bank / (c) MoCo；MAE Fig.1 单图三段（原图 → 75% 遮盖 → 重建），靠现象本身制造冲击。
- **Caption**：粗体短语开头（如 `\textbf{Masked Autoencoder (MAE) architecture.}`），正文 ≤3 行，不堆参数公式。
- **架构图**：模块抽象为灰色语义方块，仅保留核心张量流；箭头横平竖直，字号偏大。
- **表格**：严格三线表，最优结果加粗，无竖线（证据：MoCo/MAE 主实验表）。

## 二、写作修辞指纹

- **标志性短语库**（附例句）：
  - *"without bells and whistles"* —— 方法自我定性（MoCo、MAE 摘要/引言多次出现）
  - *"conceptually simple"* / *"simple yet effective"* —— 同上
  - *"driven by a simple question"* —— Introduction 的问题引入
  - *"surprisingly, we find that..."* —— 反直觉结果的呈报
- **Abstract 句序**：背景常识 → 跨领域矛盾（"NLP 成了，CV 为什么没成"）→ 核心洞见（信息密度差异 → 高遮盖率）→ 极简方法 → 量化结果（提速 + 超越监督基线）→ 范式升华。
- **Related Work**：分类法分派别；划线句式温和（"In contrast, ..."），几乎不贬前人，先肯定 "pioneering" 再指出底层假设差异。
- **标题命名**：朴素可读缩写（ResNet 例外为沿用，FPN/MoCo/MAE 均可发音）；标题为陈述发现式，不玩梗。

## 三、选题品味

- **梯队分布**：全部语料均在 Tier 1~2——从不做"提 0.5% mAP"式增量。
- **选题过滤网**：做底层机制问题（梯度流/信息熵/表征本质）；不做复杂工程堆叠、不做单数据集 trick。
- **消融哲学**：大跨度单变量扫描定生死（MAE 将 mask ratio 从 10% 扫到 90%，倒 U 曲线直接立论 75% 最优）；主动做"去掉所有增强的极简 baseline"自证。
- **时间线**：ResNet(2015 梯度流) → FPN(2016 多尺度) → Mask R-CNN(2017 像素对齐) → MoCo(2019 无监督字典) → MAE(2021 掩码建模)。**一条主线（表征学习）上的阶段性深挖，相邻论文多为延续**。

## 四、Idea 设计模式

- **原型分布**：
  | 原型 | 代表论文 | 一句话内核 | 证据 |
  | --- | --- | --- | --- |
  | 矛盾驱动 | ResNet | 加深退化与"恒等映射可无损传导"矛盾，故问题在优化而非容量 | ResNet Intro |
  | 迁移驱动 | MAE | 把 BERT 掩码预训练迁入视觉，关键适配是信息密度 → 75% 高遮盖 | MAE Intro/Abstract |
  | 简化驱动 | MoCo | 用队列把字典大小与 batch size 解耦，替代庞杂的 memory bank | MoCo Fig.1 + Intro |
- **问题表述句式**：朴素设问式——把大方向收敛成一句外行能懂的问题（"what makes deep networks hard to train?" 式的收敛链：领域 → 子矛盾 → 一句话问题）。
- **谱系与外推**：MoCo 证明无监督表征可行 → 其扩展性局限催生 MAE；MAE 证明掩码建模可扩展 → 后续延伸至多模态与视频（延续型演化为主）。若按此规律外推，下一篇大概率仍在"极简机制 × 大规模预训练"主线上。
- **Idea 记分卡（校准后）**：根本矛盾性（是否直指被广泛默认的假设）、一句话可陈述性、极简内核（核心变化能否一行公式说清）、可证伪性（单变量扫描能否定生死）、社区势能（能否成为别人的预训练范式）。

## 五、盲测验证记录

- 留样论文：MAE。**本范例未执行真实盲测**——真实蒸馏时必须补做：用本档案仿写 MAE 主题 Abstract 并与原文并排对比，差距点回写档案。

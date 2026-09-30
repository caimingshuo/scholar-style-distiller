# 论文写作与修辞范式 (Academic Writing & Rhetoric Guide)

顶尖学者的论文之所以能征服严苛的审稿人，并非因为词汇艰涩深奥，反而在于其**清晰度（Clarity）、严谨度（Rigor）与强大的叙事张力（Narrative Arc）**。

---

## 一、Abstract 的“六句闭环法则” (The 6-Sentence Abstract)

高接受率论文的摘要通常严格遵循这六个逻辑步进，字数通常控制在 150~220 词：

1. **Context & Motivation (宏观背景与长期使命)**
   - *目标*：确立研究领域的重要地位，引发审稿人共鸣。
   - *经典句式*：
     > "[Field/Task] has witnessed remarkable progress in recent years, largely driven by..."
     > "Recent breakthroughs in [X] have opened new frontiers for [Y]."

2. **The Fundamental Tension / Dilemma (核心矛盾与不可调和的瓶颈)**
   - *目标*：指出既有工作为什么不够好，揭示深层矛盾（而非表面上的“调参不好”）。
   - *经典句式*：
     > "However, existing methods fundamentally struggle with [Problem], primarily because they rely on [Flawed Assumption]."
     > "Despite their empirical success, these approaches incur heavy computational overhead, or fail to generalize when [Condition]."

3. **Core Insight / The Key Idea (核心洞见与认知跃迁)**
   - *目标*：用一句话说出本文的最核心直觉，让审稿人产生“原来如此”的顿悟感。
   - *经典句式*：
     > "In this paper, we argue that the crux of this problem lies in [Underlying Phenomenon/Principle], rather than [Superficial Factor]."
     > "We observe that [Surprising Property], suggesting that [Simple Mechanism] is sufficient to [Achieve Goal]."

4. **Proposed Approach / Framework (极简方法概述)**
   - *目标*：简述解决方案，强调优雅与极简（Simple yet effective）。
   - *经典句式*：
     > "Motivated by this insight, we propose [Method Name], a conceptually simple yet remarkably effective framework for [Task]."
     > "[Method Name] addresses this challenge by [Core Operation], eliminating the need for [Complex Component]."

5. **Empirical Highlights / Quantitative Proof (关键量化成果)**
   - *目标*：用无可辩驳的数据或 SOTA 指标证明其威力。
   - *经典句式*：
     > "Extensive experiments on [Benchmarks] demonstrate that our approach outperforms prior state-of-the-art by [Metric] while reducing [Cost] by [Ratio]."
     > "Across three diverse benchmarks, [Method] consistently achieves competitive performance with [X%] fewer parameters."

6. **Broader Impact / Theoretical Takeaway (学术启示与价值升华)**
   - *目标*：拔高文章价值，指出本工作对社区的长期意义。
   - *经典句式*：
     > "Our findings challenge the prevailing convention that [Old Belief] is necessary, pointing toward a more streamlined paradigm for [Domain]."
     > "We hope our simple baseline will serve as a solid foundation for future research in [Area]."

---

## 二、Introduction 的“五段论”叙事架构 (The 5-Paragraph Intro)

Introduction 是整篇论文的“立论法庭”，顶级学者通常按以下节奏推进：

```
Para 1: 领域的繁荣与基础假设 (Broad Context & Standard Premise)
   ↓
Para 2: 既有范式的裂痕与隐藏瓶颈 (The Hidden Bottleneck / Counter-intuitive Dilemma)
   ↓
Para 3: 本文的核心观察与顿悟 (Core Insight / Occam's Razor Revelation)
   ↓
Para 4: 方法概览与工作机制 (Framework Walkthrough & Key Design Decisions)
   ↓
Para 5: 实验验证与主导优势 (Empirical Validation & Surprising Findings)
   ↓
Bullet Points: 凝练的贡献清单 (Summary of Contributions: 3 Crisp Bullets)
```

### 贡献清单（Contributions）的撰写禁忌与正道

- ❌ **低分表述（工程打工人视角）**：
  1. We propose a new model called XYZNet.
  2. We add a cross-attention module and a focal loss to improve performance.
  3. We conduct experiments on dataset A and B and achieve good results.
  *(评语：毫无思想，全是流水账工程，极易被拒。)*

- ✅ **高分表述（顶尖学者视角）**：
  1. **Conceptual Discovery / Principle**: We identify and systematically analyze [Phenomenon], revealing that [Fundamental Factor] is the true governing factor of [Outcome].
  2. **Methodological Novelty**: We introduce [Method], a minimalist formulation that achieves [Goal] without resorting to [Heuristic / Complex Mechanism].
  3. **Empirical Breadth & Benchmark**: Through exhaustive evaluations across [Datasets], we demonstrate that our method sets new state-of-the-art performance, while offering [X%] faster inference and strong out-of-domain transferability.

---

## 三、顶尖学者的修辞与行文气质 (Tone & Prose Cadence)

1. **谦逊而自信 (Confident Humility)**：
   - 避免狂妄的宣传式词汇（如 "revolutionary", "flawless", "miraculous"）。
   - 采用严谨客观的学术判断词汇（"conceptually straightforward", "surprisingly effective", "counter to conventional wisdom"）。

2. **主动句与精炼动词 (Active Voice & Strong Verbs)**：
   - 多用主动句：*"We uncover..."*, *"Our analysis reveals..."*, *"Figure 2 illustrates..."*。
   - 减少冗余的被动句与名词堆砌（Avoid nominalizations）。

3. **顺畅的转折与承托 (Seamless Transitions)**：
   - 在提出自身方法前，先给既有工作以公正的评价（*"While these approaches have achieved commendable accuracy, they inevitably inherit..."*）。
   - 让审稿人感觉你的创新是水到渠成、历史必然，而不是为了发论文硬生生发明出来的需求。

4. **坦诚讨论局限性 (Intellectual Honesty)**：
   - 在 Discussion / Limitations 章节，主动且诚恳地指出当前方法的适用边界、极端失败案例（Failure Cases）。
   - **审稿人心理学**：自己主动剖析的弱点是“严谨与深刻”；被审稿人揪出来的弱点是“重大漏洞与拒稿理由”。

---

## 四、Related Work 的组织法 (Related Work Fingerprint)

Related Work 是最能区分学者风格的 section 之一，蒸馏时记录：

1. **分类法 vs 时间线法**：按技术路线分派别（"Existing approaches fall into three camps..."），还是按演化时间线推进？
2. **划线句式**：如何与前人划清界限——"In contrast to ...", "Unlike ..., we ...", "..., however, ..."。收集该学者惯用的 3~5 个。
3. **对对手的温度**：逐篇统计其评价前人的用词（pioneering / elegant / limited / fails to），确定褒贬尺度——有的学者从不贬人，有的学者句句点穴。
4. **段落收束**：是否每段 Related Work 以一句"我们的差异"收尾？

## 五、标题与方法命名学 (Titles & Naming)

1. **标题公式**：陈述发现式（*Deep Residual Learning for Image Recognition*）、设问式（*Is X All You Need?*）、宣言式（*X Are Y*）——该学者偏好哪种？标题平均词数是多少？
2. **方法命名**：朴素缩写（MAE, MoCo, FPN）还是概念词（Transformer, Diffusion）？缩写是否可读（pronounceable）？
3. **冒号结构**：是否用 "X: Simple ..." 式副标题把卖点写进标题。

## 六、蒸馏证据记录格式

每个句式模板、每条短语入档时附 ≥2 条原文例句（标注论文 + 段落位置），**无例句不入档**。

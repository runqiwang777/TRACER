# 相关工作与研究定位

以下工作涉及重新采样、Lean 证明修复和编译诊断。各自使用不同的模型、数据集和预算。

| 工作 | 核心方向 | 与 TRACER 的关系 |
| --- | --- | --- |
| [Li 与 Li (2026)](https://arxiv.org/abs/2610.22698) | 固定失败证明，操纵正确／错误诊断、旧证明呈现与重试指令；在 MiniF2F 上使用 Qwen3.6-27B 和 DeepSeek-Prover-V2-7B | 是 TRACER 反馈对照的重要参考。它区分了两种问题：给定失败证明时，诊断是否帮助修复，以及修复能否胜过从头重试。 |
| [MathForm (2026)](https://arxiv.org/abs/2608.14221) | 知识检索、验证反馈与数学陈述自动形式化 | 输入自然语言并生成形式化陈述；TRACER 固定形式化声明，修复其证明。不能将陈述编译率与完整证明通过率比较。 |
| [APOLLO (2025)](https://arxiv.org/abs/2505.05758) | 模型无关的 Lean 协作修复，定位失败子证明并再次验证 | 更直接的相关工作。编译器引导修复不是本项目首创；可以比较局部修复粒度、预算与失败工件。 |
| [Baldur (2023)](https://arxiv.org/abs/2303.04910) | Isabelle/HOL 整体证明生成，利用失败证明和错误消息训练修复模型 | 说明“上轮候选＋诊断”的价值已有先例；TRACER 当前不训练模型，采用外部 provider。 |
| [LeanDojo / ReProver (2023)](https://arxiv.org/abs/2306.15626) | Lean 环境交互、证明数据提取、基于可用前提的训练式检索 | 是检索与可复现环境的重要基线；我们的词项检索不是学习式 premise selection，也没有其规模。 |
| [LeanAgent (2024/2025)](https://arxiv.org/abs/2410.06209) | 动态知识库、课程与渐进训练下的终身定理证明 | 与训练、知识持续积累有关；错误驱动查询只改变推理上下文，不更新模型权重。 |
| [Lean Copilot (2024)](https://arxiv.org/abs/2404.12534) | Lean 内的 tactic 建议、证明搜索与前提选择 | 侧重交互辅助；TRACER 侧重可重放失败案例与批量实验记录。 |
| [miniF2F (2021/2022)](https://arxiv.org/abs/2109.00110) | 跨证明系统的奥赛级形式数学基准 | 它评测形式化定理的求证，TRACER 的修复试点从已失败的证明出发。 |
| [Zeller & Hildebrandt (2002)](https://pm.st.cs.uni-sb.de/papers/tse2002/?lang=en) | Delta Debugging：在保留失败的条件下缩减输入 | LeanCapsule 的编译验证式精简与此相关；当前只做有限 imports 删除和定理抽取，不声称全局最小切片或完整 ddmin。 |

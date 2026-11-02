# TRACER 当前进度

2026-11-02（面向初次读者）：重写中英首页，新增日语、韩语首页与网站；用等式修复例子解释 Lean、功能、实际观察和待验证贡献。网站新增不调用 API 的三步教学交互。介绍页统一区分已完成、正在做和准备做，内部协议编号留在方法文档。按用户要求，开题报告、PPT、讲稿仅保留在本机，撤下当前仓库中的公开文件和下载入口；实验代码、配置与运行工件均不改动。

2026-11-02（R1 对齐）：中英文 README、项目网站与研究重点统一围绕四个 RQ；明确 E1 冻结 v3、E2 现有诊断分析、E3 新语义干预及 E4 独立路由验证。开题材料已按此重做并保存在本机，不能作为完成的新模型结果。E3／E4 未运行；现有实验配置、预注册和输出未改写。

2026-11-02：更新中英文 README、相关工作与研究重点说明，突出三供应商模型、真实项目修复、诊断表示和可审计证据。Li 与 Li 仅在首页作简短参考引用。此次为文档定位更新；现有 v3 配置、预注册和实验工件未改写，未调用 provider。后续分析顺序见 [研究重点说明](docs/RESEARCH_POSITIONING.md)。

2026-10-29：公开文档、命令、配置路径、协议标识和密钥变量统一使用 v3 命名；冻结实验参数与日期保持原值，本机原始批次未改写。既有批次继续使用其原工作副本与原目录；详见 [公开命名说明](docs/RELEASE_NAMING.md)。

本轮完整 Python 回归共 250 项：248 项通过、2 项平台专属测试跳过。v3 离线审计与 7 份配置/协议的研究参数一致性检查通过；不调用付费 API。

本文件只记录本仓库实际包含的当前代码、协议和发布工件。早期 repair24 付费实验、旧 pilot、FATE-M 中间产物及其完整历史归档不随本次上传。

## 已具备的交付

| 项目 | 当前工件 | 证据边界 |
| --- | --- | --- |
| LeanCapsule | `capsules/`、`leancapsule/`、`capsule_schema/` | 24 个固定案例可审计与回放；不代表任意 Lake 项目都可自动封装。 |
| Capsule feasibility | `scripts/run_capsule_feasibility.py` 与固定输入 | 12 个 core、4 个 challenge 的有限矩阵；不推广为一般最小化能力。 |
| Compiler Feedback v1 | `docs/COMPILER_FEEDBACK_V1.md`、`src/compiler_feedback.py` 和离线夹具 | 保留 raw、normalized、structured 三层及来源诊断片段；不等同于模型采纳研究结论。 |
| SP v2 | `published/security-study-tracer-sp-v2/` | 12 个冻结危险案例在编译前拒绝，8 个正常对照由 Lean 编译；不代表完整沙箱或零风险。 |
| SP Linux isolation | `published/security-isolation-tracer-sp-v1/` | 单次 Linux 容器运行观察 14/14 项冻结控制；Windows Docker Desktop 仍待测。 |
| TRACER-REAL v2 | `benchmarks/real_repairs/tracer_real_v2/` 与对应筛查账本 | 254 道题、五个独立 test 项目；题库已冻结，provider 最终结果包未随本次上传。 |
| v3 causal protocol | `docs/V3_EXPERIMENT_PROTOCOL.md`、`experiments/preregistrations/`、`scripts/run_v3_formal.ps1` | 运行门禁和恢复机制已实现；当前上传内容不含经过全量审计的正式 provider 结果。 |

## 当前实验状态

v3 的原始运行目录与当前可能进行中的批次留在本机。本次上传未包括经全量审计的最终结果包，因此不在仓库中报告该批次的性能或因果结果，也不推断本机运行是否已经完成。后续发布应基于原输出目录审计，保留失败工件、模型配置、完整脱敏轨迹和成功证明。

2026-10-28 本次整理副本的 Python 回归共 248 项：246 项通过、2 项 Linux 专属符号链接检查跳过；不含付费模型调用。

## 验收入口

```text
lake build
python -m unittest discover -s tests -v
python scripts/verify_compiler_feedback_v1.py --verify-only
python src/tracer_real_v2.py audit
python src/security_study.py --check published/security-study-tracer-sp-v2/report.json
python scripts/audit_security_isolation_release.py published/security-isolation-tracer-sp-v1
python -m leancapsule audit capsules
python -m leancapsule verify capsules
```

离线门禁不调用付费模型 API。Capsule 全量回放需准备固定 Mathlib 依赖；软件测试通过不等于研究假设成立。

## 后续优先项

1. 完成 v3 provider 批次并通过轨迹、复编译和发布审计。
2. 完成人工计时与跨环境复验，再把结果与完整脱敏工件一起交付。
3. 扩展 SP 容器隔离至 Windows Docker Desktop，并保留 Linux 单平台证据边界。


# TRACER 当前进度

2026-11-02：重写中英首页，新增日语、韩语首页与网站；用等式修复例子解释 Lean、功能、实际观察和待验证贡献。网站新增不调用 API 的三步教学交互。介绍页统一区分已完成、正在做和准备做，内部协议编号留在方法文档。按用户要求，开题报告、PPT、讲稿仅保留在本机，撤下当前仓库中的公开文件和下载入口；实验代码、配置与运行工件均不改动。

本文件只记录本仓库实际包含的当前代码、协议和发布工件。早期 repair24 付费实验、旧 pilot、FATE-M 中间产物及其完整历史归档未随当前版本发布。

## 已具备的交付

| 项目 | 当前工件 | 证据边界 |
| --- | --- | --- |
| LeanCapsule | `capsules/`、`leancapsule/`、`capsule_schema/` | 24 个固定案例可审计与回放；不代表任意 Lake 项目都可自动封装。 |
| Capsule feasibility | `scripts/run_capsule_feasibility.py` 与固定输入 | 12 个 core、4 个 challenge 的有限矩阵；不推广为一般最小化能力。 |
| Compiler Feedback v1 | `docs/COMPILER_FEEDBACK_V1.md`、`src/compiler_feedback.py` 和离线夹具 | 保留 raw、normalized、structured 三层及来源诊断片段；不等同于模型采纳研究结论。 |
| SP v2 | `published/security-study-tracer-sp-v2/` | 12 个冻结危险案例在编译前拒绝，8 个正常对照由 Lean 编译；不代表完整沙箱或零风险。 |
| SP Linux isolation | `published/security-isolation-tracer-sp-v1/` | 单次 Linux 容器运行观察 14/14 项冻结控制；Windows Docker Desktop 仍待测。 |

## 验收入口

```text
lake build
python -m unittest discover -s tests -v
python scripts/verify_compiler_feedback_v1.py --verify-only
python src/security_study.py --check published/security-study-tracer-sp-v2/report.json
python scripts/audit_security_isolation_release.py published/security-isolation-tracer-sp-v1
python -m leancapsule audit capsules
python -m leancapsule verify capsules
```

离线门禁不调用付费模型 API。Capsule 全量回放需准备固定 Mathlib 依赖；软件测试通过不等于研究假设成立。

## 后续优先项

反馈研究的方法与验证计划见[研究重点](docs/RESEARCH_POSITIONING.md)。

1. 完成人工计时与跨环境复验，再把结果与完整脱敏工件一起交付。
2. 扩展 SP 容器隔离至 Windows Docker Desktop，并保留 Linux 单平台证据边界。

# 项目概览

TRACER（Typed Repair Agent with Compiler-validated Example Retrieval）是 Lean 4 证明修复与失败复现工具。它在推理阶段连接候选生成、真实 Lean 编译、结构化反馈、错误自适应检索、有限重试和可审计保存；不训练模型。

## 当前仓库内容

- `src/`：Agent、provider、编译器、反馈、检索及研究运行器。
- `benchmarks/`、`lean_project/`：冻结修复基准与项目环境。
- `capsules/`、`leancapsule/`：失败案例格式、审计和回放。
- `docs/`、`experiments/`：当前协议、使用说明、预注册与配置。
- `published/security-study-tracer-sp-v2/`：SP-1～SP-12 与正常对照的离线安全结果。
- `published/security-isolation-tracer-sp-v1/`：单次 Linux 容器隔离实测；Windows Docker Desktop 仍待完成。

完整 repair24 六臂运行包、逐轮轨迹、成功证明复核账本和旧项目归档不在本次仓库中。README 中的 repair24 汇总表和图仅用于背景展示，不能从此仓库独立审计。

## 复验入口

在已安装仓库固定 Lean 工具链的环境中，可运行：

```text
lake build
python scripts/verify_compiler_feedback_v1.py --verify-only
python src/tracer_real_v2.py audit
python src/security_study.py --check published/security-study-tracer-sp-v2/report.json
python scripts/audit_security_isolation_release.py published/security-isolation-tracer-sp-v1
python scripts/run_ci_tests.py
python -m leancapsule audit capsules
python -m leancapsule verify capsules
```

这些命令不调用付费模型；Capsule 全量回放需要准备固定 Mathlib 依赖。软件门禁通过不等于研究假设成立。

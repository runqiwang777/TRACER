# TRACER

[English](README.md) | **简体中文**

### Typed Repair Agent with Compiler-validated Example Retrieval

![TRACER 项目概览](https://runqiwang777.github.io/contents/images/tracer.jpg)

TRACER 是 Lean 4 证明修复与失败复现工具。它将模型生成候选接入真实 Lean 编译、结构化编译反馈、检索、有界重试和可审计证明工件；项目不训练或微调模型。

[![CI](https://github.com/runqiwang777/TRACER/actions/workflows/ci.yml/badge.svg)](https://github.com/runqiwang777/TRACER/actions/workflows/ci.yml)
[![Lean](https://img.shields.io/badge/Lean-4.32.0-blue)](lean-toolchain)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## 当前交付内容

- **修复与因果实验基础设施：** 已冻结 TRACER-REAL v2 基准纳入方案和 v3 预注册协议。本次上传未包含完成审计的 provider 最终结果包；不能根据仓库缺少结果文件推断本地运行是否完成。
- **编译反馈：** 原始、规范化和结构化诊断层，保留来源证据，并提供离线失败夹具。
- **LeanCapsule：** 24 个可回放失败案例，覆盖 Std、Mathlib 和 project-local 环境。
- **安全：** SP-1～SP-12 编译前策略案例及 8 个正常对照；一次 Linux 容器运行观察到声明的 14/14 项控制。Windows Docker Desktop 尚待验证。

已发布安全工件：[SP v2 离线策略结果](published/security-study-tracer-sp-v2/) · [Linux 隔离报告](published/security-isolation-tracer-sp-v1/)。

## 快速开始

需要 Python 3.11+、Git 和通过 `elan` 安装的 Lean。仓库在 [lean-toolchain](lean-toolchain) 中固定 Lean 版本。

```bash
git clone https://github.com/runqiwang777/TRACER.git
cd TRACER
python -m pip install -r requirements.txt
lake build
python -m leancapsule audit capsules
```

回放一个冻结失败案例（成功表示预期失败被复现）：

```bash
python -m leancapsule replay capsules/std/unknown-identifier
```

真实模型请求的配置方法见 [API_GUIDE.md](docs/API_GUIDE.md)。请求可能产生费用；不要把凭据写入源码、命令历史或结果工件。

## 研究设计

v3 使用三条确认条件和五条扩展条件。SP-1～SP-12 是独立安全策略，不是实验臂。参见[冻结实验协议](docs/V3_EXPERIMENT_PROTOCOL.md)和[安全策略](docs/security_policy.md)。

冻结的 TRACER-REAL v2 测试集包含来自五个独立上游项目的 254 道修复题。v3 协议冻结了嵌套设计：DeepSeek 和 GLM 运行八个实验臂，MiniMax 运行三条确认臂。本仓库目前不依据 provider 批次提出性能或因果结论。

## 验证

```bash
python -m unittest discover -s tests -v
lake build
python scripts/verify_compiler_feedback_v1.py --verify-only
python src/tracer_real_v2.py audit
python src/security_study.py --check published/security-study-tracer-sp-v2/report.json
python scripts/audit_security_isolation_release.py published/security-isolation-tracer-sp-v1
python -m leancapsule audit capsules
python -m leancapsule verify capsules
```

Capsule 全量验证需要准备固定项目依赖。离线测试和审计不会调用付费模型 API。软件检查通过不等于研究假设成立，也不能证明形成了完整沙箱。

## 文档

- [Provider/API 配置](docs/API_GUIDE.md)
- [编译反馈协议](docs/COMPILER_FEEDBACK_V1.md) · [反馈采纳分析](docs/FEEDBACK_ADOPTION_V1.md)
- [TRACER-REAL v2 题库](docs/TRACER_REAL_V2.md) · [v3 实验](docs/V3_EXPERIMENT_PROTOCOL.md)
- [v3 公开命名与既有运行](docs/RELEASE_NAMING.md)
- [LeanCapsule 格式](docs/CAPSULE_FORMAT.md) · [失败案例库](capsules/index.md)
- [SP 安全策略](docs/security_policy.md) · [隔离协议](docs/SP_ISOLATION_V1.md)
- [相关工作](docs/RELATED_WORK.md) · [进度登记](PROGRESS.md)

## 引用与许可

研究或教学使用时，请引用 [CITATION.cff](CITATION.cff)，并注明仓库版本和实验批次。项目采用 [MIT License](LICENSE)；各 Capsule 保留其来源许可。

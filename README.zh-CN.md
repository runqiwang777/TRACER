# TRACER

[English](README.md) | **简体中文** | [日本語](README.ja.md) | [한국어](README.ko.md)

**让 AI 写的数学证明出错后能修复，每次修改都交给 Lean 检查。**

[Website](https://runqiwang777.github.io/TRACER/zh.html) · [Demo](https://runqiwang777.github.io/TRACER/demo/) · [API 指南](docs/API_GUIDE.md)

![CI](https://github.com/runqiwang777/TRACER/actions/workflows/ci.yml/badge.svg) [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

![TRACER 项目总览图](TRACER.png)

TRACER 把语言模型和 Lean 连接起来。Lean 是检查数学证明的软件：它指出哪一步不成立，TRACER 把报错和相关例子交给模型，再检查修改后的证明。

没接触过 Lean？可以把它理解为数学证明的检查器。我们把命题和证明步骤写成代码，Lean 检查每一步是否符合给定定义和假设。看起来有道理，还不够通过检查。

## 体验 TRACER

### [体验 24 个已保存的修复案例](https://runqiwang777.github.io/TRACER/demo/)

无需安装、无需 API。演示读取已保存案例，不会现场调用模型。

![TRACER repair workflow](site/overview.svg)

## 一个没用上的条件，为什么会导致失败

已知 x = y、y = z，要证明 x = z。如果 AI 只使用第一个等式，证明就少了一步。

```lean
-- x = y, y = z; goal: x = z
-- rejected
by exact hxy
-- accepted
by exact hxy.trans hyz
```

Lean 指出实际得到的结论和目标不一致。TRACER 保留这段原文，把相关信息交给模型。 修改后的证明连接两个等式。这个示例可以通过 Lean 检查。 这是解释流程的教学示例。完整演示中另有 24 个来自实验的已保存失败与修复案例。

## TRACER 已经能做什么

| | |
| --- | --- |
| **检查 AI 的证明** | 在固定命题和依赖的情况下编译候选证明，找到真正的失败原因。 |
| **保留并整理报错** | 保留原文，提取找不到的名称、类型差异和未完成目标，每个字段都能找到原始依据。 |
| **让模型再修一次** | 提供反馈，并按设置检索相关本地例子。限制尝试次数，避免无限重试。 |
| **保存可复查的结果** | 记录每次候选、报错和用量，保存通过的证明，供独立重新编译。 |

## 已经完成的研究，得到了什么结果

24 道不同题目，在两种模型配置和多种设置下重复运行，共形成 864 个任务实例。它们不是 864 道不同定理。

| | Lean 通过数 |
| --- | ---: |
| 第一次尝试 | 735/864 (85.1%) |
| 最多三次尝试 | 811/864 (93.9%) |

**第一次未通过的任务中，另有 76 个任务实例后来通过。** 85.1% 到 93.9% 包含了多次尝试的收益，不能全部算作报错反馈的贡献。

与“不提供报错、直接再试”的设置相比，加入反馈后 Flash 的成功数相同，Pro 少了 2 个；每种设置各 72 个任务实例。目前没有证明反馈能稳定提升成功率。

Lean 通过表示证明在给定环境和假设下形式有效。AI 辅助复核不等于完整的人工数学审查。离线安全测试和一次 Linux 容器运行，也不构成通用沙箱保证。

完整的前期实验包保留在本机归档；当前仓库提供其中 24 个案例的浏览器回放。 [数据与来源说明](docs/INTRODUCTION_EVIDENCE.md).

## 我们真正想弄清的问题

**AI 改对了，是因为看懂了错误提示，还是因为它又试了一次？**

- **让比较从同一个错误出发.** 复制同一份失败证明，只改变下一次能看到的信息，减少起点不同带来的干扰。
- **检查提示里的信息有没有被用上.** 整理报错时保留原始依据，再检查模型是否修改了与错误相关的代码。
- **研究真实项目里的维护问题.** 从不同项目的历史修复中构造测试题，把参考答案与模型生成过程隔离。

**难在哪里:** 找不到名称、类型不对、目标没证完、依赖发生变化，都可能让证明失败。我们需要保留必要上下文、避免答案泄漏、区分 API 故障和证明错误，还要统计每次尝试真实消耗的时间与 token。

## 已完成、正在做、准备做

| | |
| --- | --- |
| **已完成** | 限次修复流程、可追溯报错、例子检索、成功证明保存、24 个可回放失败案例，以及来自 5 个项目的 254 道历史修复测试题。 |
| **正在做** | 使用 DeepSeek、GLM、MiniMax 比较不同反馈的作用。收齐轨迹、审计并独立重新编译后再发布最终结果。这里不是实时运行监控。 |
| **准备做** | 一次只改变错误提示中的一个事实，观察模型是否沿对应方向修改；再用独立材料检验按错误类型选择反馈是否有效。 |

## 在本地体验一个小例子

先安装 Python 3.11+ 和仓库指定的 Lean 工具链，然后运行：

```bash
git clone https://github.com/runqiwang777/TRACER.git
cd TRACER
python -m pip install -r requirements.txt
lake build
python src/agent.py solve --file docs/examples/equality_chain.lean --theorem equality_chain --provider mock --mock-candidate "by exact hxy.trans hyz"
```

这里提供固定候选，用来体验编译、验证和保存，不调用模型，也不衡量模型能力。

要让模型真正生成证明，请看 API 指南。密钥通过终端隐藏输入；付费调用会把必要源码和报错发送给你选定的服务商。

## 进一步了解

- [API 指南](docs/API_GUIDE.md)
- [证明修复与失败回放](docs/CAPSULE_FORMAT.md) · [案例库](capsules/index.md)
- [查看方法与证据边界](docs/INTRODUCTION_EVIDENCE.md) · [进度](PROGRESS.md)
- [受控反馈比较](docs/V3_EXPERIMENT_PROTOCOL.md) · [执行安全](docs/security_policy.md)
- [离线安全证据](published/security-study-tracer-sp-v2/) · [Linux 隔离证据](published/security-isolation-tracer-sp-v1/)
- [参与贡献](CONTRIBUTING.md) · [相关研究](docs/RELATED_WORK.md)

LeanDojo、Baldur 和 APOLLO 为交互、检索和修复流程提供参考；Li 与 Li 是反馈对照的重要参考。TRACER 进一步关注真实项目中的诊断信息、可核查修改和使用反馈的成本。

## 引用与致谢

本项目采用 MIT 许可。引用时请注明软件版本和证据批次。感谢 SJTU AI4Math Summer School 2026 及参与点评的社区成员。 [CITATION.cff](CITATION.cff) · [MIT](LICENSE) · [SJTU AI4Math Summer School 2026](https://sjtu-ai4math.github.io/summer-school/2026/).

<sub>Typed Repair Agent with Compiler-validated Example Retrieval</sub>

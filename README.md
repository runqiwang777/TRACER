# TRACER

**English** | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

**Repair AI-written mathematical proofs. Check every result with Lean.**

[Website](https://runqiwang777.github.io/TRACER/) · [Demo](https://runqiwang777.github.io/TRACER/demo/) · [API guide](docs/API_GUIDE.md)

![CI](https://github.com/runqiwang777/TRACER/actions/workflows/ci.yml/badge.svg) [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

![TRACER project overview](TRACER.png)

TRACER connects a language model to Lean, a tool that checks mathematical proofs. It sends useful error information back to the model, can retrieve related examples, and checks the revised proof again.

New to Lean? A proof is a sequence of justified mathematical steps. Lean checks those steps against a stated theorem and its assumptions. Fluent text alone is not enough to pass.

## Try TRACER

### [Explore 24 saved repairs](https://runqiwang777.github.io/TRACER/demo/)

No installation or API key. The demo replays saved examples, not live model calls.

![TRACER repair workflow](site/overview.svg)

## A missing step, made visible

Suppose x = y and y = z. We want to prove x = z. Using only the first equality leaves a gap.

```lean
-- x = y, y = z; goal: x = z
-- rejected
by exact hxy
-- accepted
by exact hxy.trans hyz
```

Lean identifies the mismatch. TRACER preserves the exact evidence and sends the relevant information back. The revised proof uses both equalities. Lean accepts this example. Small teaching example. The 24-case demo contains saved experimental failures and repairs.

## What TRACER does

| | |
| --- | --- |
| **Check the candidate** | Compile a proposed proof while keeping the theorem and imports fixed. |
| **Explain the failure** | Keep the original message and extract identifiers, types and unfinished goals with their source snippets. |
| **Try a repair** | Give the model feedback and, when enabled, related local examples. Stop at a fixed attempt limit. |
| **Save the evidence** | Save the candidate, diagnostic, usage and accepted proof for independent rechecking. |

## What the completed study shows

24 distinct problems, two model configurations and repeated settings produced 864 task instances. Repeated instances are not 864 different theorems.

| | Lean success |
| --- | ---: |
| First attempt | 735/864 (85.1%) |
| Within three attempts | 811/864 (93.9%) |

**76 additional task instances passed after the first attempt.** The increase from 85.1% to 93.9% includes extra attempts. It does not isolate the benefit of feedback.

In the direct comparison with retrying without feedback, compiler feedback produced the same number of successes on Flash and two fewer on Pro, out of 72 instances per setting. We have not established a stable feedback advantage.

Compiler checks establish formal validity in the chosen environment and assumptions. AI-assisted review is not a full human mathematical review. One Linux container report and offline policy tests do not establish a universal sandbox.

The full earlier study is retained in the local archive; this repository exposes its 24-case replay. [Evidence and source notes](docs/INTRODUCTION_EVIDENCE.md).

## The question behind the toolkit

**Does an error message help because of what it says, or does the model simply benefit from trying again?**

- **Comparable starting point.** Reuse the same failed proof, then change only the information supplied for the next attempt.
- **Checkable information.** Trace each extracted error field to the original message. Check whether edits address that specific problem.
- **Real maintenance tasks.** Evaluate historical proof repairs from independent projects, with reference solutions kept outside generation.

**The hard part:** A proof can fail because of a missing name, a wrong type, an unfinished goal or a changed dependency. We must preserve the right context, avoid leaking answers, separate API failures from proof failures, and account for the actual cost of every attempt.

## Built, under study, and planned

| | |
| --- | --- |
| **Built** | Bounded proof repair, source-linked diagnostics, example retrieval, saved proofs, 24 replayable failure cases, and a frozen test set of 254 historical repairs from five projects. |
| **Under study** | A controlled comparison using DeepSeek, GLM and MiniMax. Complete trace auditing and independent recompilation must precede final results. This page is not a live run monitor. |
| **Planned** | Change one diagnostic fact at a time to test editing behavior. Then test whether choosing feedback by error type helps on independent data. |

## Run a small example locally

After installing Python 3.11+ and the Lean toolchain pinned by this repository:

```bash
git clone https://github.com/runqiwang777/TRACER.git
cd TRACER
python -m pip install -r requirements.txt
lake build
python src/agent.py solve --file docs/examples/equality_chain.lean --theorem equality_chain --provider mock --mock-candidate "by exact hxy.trans hyz"
```

This supplied candidate exercises compilation and saving without a model call. It does not measure model quality.

For real model generation, see the API guide. You enter the key in a hidden terminal prompt. Paid requests can send source code and diagnostics to your provider.

## Documentation

- [API guide](docs/API_GUIDE.md)
- [Proof repair and reproducible failure cases](docs/CAPSULE_FORMAT.md) · [Gallery](capsules/index.md)
- [Read the method and evidence limits](docs/INTRODUCTION_EVIDENCE.md) · [Progress](PROGRESS.md)
- [Controlled feedback study](docs/V3_EXPERIMENT_PROTOCOL.md) · [Execution safety](docs/security_policy.md)
- [Offline safety evidence](published/security-study-tracer-sp-v2/) · [Linux isolation evidence](published/security-isolation-tracer-sp-v1/)
- [Contributing](CONTRIBUTING.md) · [Research context](docs/RELATED_WORK.md)

LeanDojo, Baldur and APOLLO inform the tooling and repair workflow. Li and Li is an important reference for feedback controls. TRACER focuses on real-project diagnostics, observable edits and the cost of using feedback.

## Citation and acknowledgments

MIT license. Cite the software and the exact evidence batch. Thanks to SJTU AI4Math Summer School 2026 and the community reviewers. [CITATION.cff](CITATION.cff) · [MIT](LICENSE) · [SJTU AI4Math Summer School 2026](https://sjtu-ai4math.github.io/summer-school/2026/).

<sub>Typed Repair Agent with Compiler-validated Example Retrieval</sub>

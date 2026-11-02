# TRACER

**English** | [简体中文](README.zh-CN.md) | [Project website](https://runqiwang777.github.io/TRACER/)

### Typed Repair Agent with Compiler-validated Example Retrieval

![TRACER project overview](https://github.com/runqiwang777/TRACER/blob/main/TRACER.png)

TRACER studies **when compiler feedback helps language models repair Lean 4 proofs in real projects**. Its preregistered v3 study covers **DeepSeek-v4-Pro, GLM-4.5, and MiniMax-M3** through three first-party providers. The toolkit connects candidate proofs to real Lean compilation, source-linked diagnostics, retrieval, bounded retries, and auditable proof artifacts. It does not train or fine-tune models.

[![CI](https://github.com/runqiwang777/TRACER/actions/workflows/ci.yml/badge.svg)](https://github.com/runqiwang777/TRACER/actions/workflows/ci.yml)
[![Lean](https://img.shields.io/badge/Lean-4.32.0-blue)](lean-toolchain)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> [!IMPORTANT]
> **[Explore the TRACER website and 24-case demo](https://runqiwang777.github.io/TRACER/)**. The static explorer shows stored Lean failures and repairs without an API key. The full prior repair24 release remains in the local archive; this repository includes the embedded 24-case replay.

[Research proposal (PDF)](docs/proposal/TRACER_Proposal.pdf) · [5-minute talk (PPTX)](docs/proposal/TRACER_5min_Talk.pptx) · [Speaker notes](docs/proposal/TALK.zh-CN.md)

## Current deliverables

- **Repair and causal-study infrastructure:** frozen TRACER-REAL v2 benchmark enrollment and v3 preregistered protocol. This upload does not include an audited final provider result package; local run status is not inferred from the repository contents.
- **Compiler feedback:** raw, normalized, and structured diagnostic layers with retained source evidence and offline failure fixtures.
- **LeanCapsule:** 24 replayable failures across Std, Mathlib, and project-local environments.
- **Security:** SP-1–SP-12 pre-compilation policy cases with 8 benign controls; one Linux container run observed 14/14 declared controls. Windows Docker Desktop remains pending.

Published security artifacts: [SP v2 offline policy results](published/security-study-tracer-sp-v2/) · [Linux isolation report](published/security-isolation-tracer-sp-v1/).

## Quick start

Requirements: Python 3.11+, Git, and Lean via `elan`. The repository pins Lean in [lean-toolchain](lean-toolchain).

```bash
git clone https://github.com/runqiwang777/TRACER.git
cd TRACER
python -m pip install -r requirements.txt
lake build
python -m leancapsule audit capsules
```

Replay a frozen failure (success means the expected failure was reproduced):

```bash
python -m leancapsule replay capsules/std/unknown-identifier
```

For a real model request, configure a supported provider as described in [API_GUIDE.md](docs/API_GUIDE.md). Requests may incur charges; never put credentials in source files, command history, or result artifacts.

## Research focus

TRACER studies the information in diagnostics, observable repair behavior, and the cost of using feedback. Four questions organize the work:

- **RQ1 — Effect:** does correct feedback improve repair over another generation attempt from the same failure?
- **RQ2 — Semantics:** do true, irrelevant, and counterfactual diagnostics lead to different edits and outcomes?
- **RQ3 — Representation:** what do raw, normalized, and structured diagnostics preserve, and at what cost?
- **RQ4 — Error state:** when does feedback help, and can feedback selection be validated on independent data?

The frozen TRACER-REAL v2 test set contains 254 historical repairs from five upstream projects. Within each model, task, and repeat, v3 branches from the same eligible failed first candidate.

| Frozen model | Provider | v3 scope |
| --- | --- | --- |
| `deepseek-v4-pro` | DeepSeek | Eight arms, three repeats |
| `glm-4.5` | Zhipu BigModel | Eight arms, three repeats |
| `MiniMax-M3` | MiniMax China | Three confirmatory arms, three repeats |

All models share `true_structured - content_free_retry` and the `counterfactual` control. DeepSeek and GLM also compare raw and normalized diagnostics, matched irrelevant feedback, retrieval-only, and the frozen adaptive prototype. Three providers extend the scope of validation; model choice alone does not establish a method or performance advantage.

**Roadmap R1:** finish and audit the frozen v3 batch (**E1**), analyze existing diagnostic fidelity, edits, error transitions, and cost (**E2**), then independently preregister targeted semantic interventions (**E3**). New error-aware routing rules require independent validation (**E4**). These follow-ups do not change the running v3 protocol.

[Li and Li (2026)](https://arxiv.org/abs/2610.22698) is an important reference for the feedback controls. TRACER's proposed increment combines real historical repairs with diagnostic information structure and verifiable behavioral evidence; see [related work](docs/RELATED_WORK.md).

**Evidence status:** this repository does not yet contain the fully audited final v3 provider release. Equal generation counts and output caps do not imply equal actual token expenditure. See the [frozen protocol](docs/V3_EXPERIMENT_PROTOCOL.md) and [R1 research priorities](docs/RESEARCH_POSITIONING.md). SP-1–SP-12 remain separate security policies.

## Validation

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

Capsule verification needs the pinned project dependencies. Offline tests and audits do not call paid model APIs. Passing software checks does not establish a research hypothesis or prove a complete sandbox.

## Documentation

- [Provider/API setup](docs/API_GUIDE.md)
- [Compiler feedback protocol](docs/COMPILER_FEEDBACK_V1.md) · [feedback adoption analysis](docs/FEEDBACK_ADOPTION_V1.md)
- [TRACER-REAL v2 benchmark](docs/TRACER_REAL_V2.md) · [v3 experiment](docs/V3_EXPERIMENT_PROTOCOL.md)
- [v3 release naming and existing runs](docs/RELEASE_NAMING.md)
- [LeanCapsule format](docs/CAPSULE_FORMAT.md) · [failure gallery](capsules/index.md)
- [SP security policy](docs/security_policy.md) · [isolation protocol](docs/SP_ISOLATION_V1.md)
- [Research priorities and contribution scope](docs/RESEARCH_POSITIONING.md)
- [Related work](docs/RELATED_WORK.md) · [Progress register](PROGRESS.md)

## Citation and license

For research or teaching use, cite [CITATION.cff](CITATION.cff) and identify the exact version and experiment batch. The project is under the [MIT License](LICENSE); capsules retain their individual source licenses.

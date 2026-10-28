# TRACER

**English** | [简体中文](README.zh-CN.md)

### Typed Repair Agent with Compiler-validated Example Retrieval

TRACER is a Lean 4 proof-repair and failure-reproduction toolkit. It connects model-generated candidates to real Lean compilation, structured compiler feedback, retrieval, bounded retries, and auditable proof artifacts. It does not train or fine-tune models.

[![CI](https://github.com/runqiwang777/TRACER/actions/workflows/ci.yml/badge.svg)](https://github.com/runqiwang777/TRACER/actions/workflows/ci.yml)
[![Lean](https://img.shields.io/badge/Lean-4.32.0-blue)](lean-toolchain)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Current deliverables

- **Repair and causal-study infrastructure:** frozen TRACER-REAL v2 benchmark enrollment and ACL 2027 preregistered protocol. This upload does not include an audited final provider result package; local run status is not inferred from the repository contents.
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

## Research design

ACL 2027 uses three confirmatory conditions and five additional extension conditions. SP-1–SP-12 are separate security policies, not experiment arms. See the [frozen experiment protocol](docs/ACL2027_EXPERIMENT_PROTOCOL.md) and [security policy](docs/security_policy.md).

The frozen TRACER-REAL v2 test set contains 254 repairs from five independent upstream projects. ACL protocol v3 freezes a nested design for DeepSeek and GLM across eight arms and MiniMax across three confirmatory arms. This repository currently makes no performance or causal claim from the provider batch.

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
- [TRACER-REAL v2 benchmark](docs/TRACER_REAL_V2.md) · [ACL 2027 experiment](docs/ACL2027_EXPERIMENT_PROTOCOL.md)
- [LeanCapsule format](docs/CAPSULE_FORMAT.md) · [failure gallery](capsules/index.md)
- [SP security policy](docs/security_policy.md) · [isolation protocol](docs/SP_ISOLATION_V1.md)
- [Related work](docs/RELATED_WORK.md) · [Progress register](PROGRESS.md)

## Citation and license

For research or teaching use, cite [CITATION.cff](CITATION.cff) and identify the exact version and experiment batch. The project is under the [MIT License](LICENSE); capsules retain their individual source licenses.

Thanks to [SJTU AI4Math Summer School 2026](https://sjtu-ai4math.github.io/summer-school/2026/) and to [subfish-zhou](https://github.com/subfish-zhou) and [Fulcrum-Nebula](https://github.com/Fulcrum-Nebula) for feedback that informed the research direction.

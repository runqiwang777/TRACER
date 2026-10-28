"""对 standalone capsule 执行有界、编译验证的 import 删除。"""

from __future__ import annotations

import re
from collections.abc import Callable


def minimize_imports(
    source: str,
    trial: Callable[[str], tuple[bool, str]],
    expected_key: str,
    *,
    max_attempts: int = 20,
) -> tuple[str, dict]:
    """逐个尝试删除 import，只有诊断键保持一致才接受删除。"""

    lines = source.splitlines(keepends=True)
    import_positions = [index for index, line in enumerate(lines) if re.match(r"^\s*import\s+", line)]
    attempts = 0
    accepted = 0
    for index in list(import_positions):
        if attempts >= max_attempts:
            break
        candidate_lines = list(lines)
        candidate_lines[index] = ""
        candidate = "".join(candidate_lines)
        ok, key = trial(candidate)
        attempts += 1
        if ok and key == expected_key:
            lines = candidate_lines
            accepted += 1
    retained = sum(1 for line in lines if re.match(r"^\s*import\s+", line))
    return "".join(lines), {
        "mode": "verified_greedy_imports",
        "original_imports": len(import_positions),
        "retained_imports": retained,
        "removed_imports": accepted,
        "compile_attempts": attempts,
        "budget_exhausted": attempts >= max_attempts and len(import_positions) > attempts,
    }

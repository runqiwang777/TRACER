"""把 capsule manifest 渲染为可人工审核的 issue Markdown。"""

from __future__ import annotations

import json
from pathlib import Path


def render_issue(capsule: Path) -> str:
    manifest = json.loads((capsule / "capsule.json").read_text(encoding="utf-8"))
    expected = manifest["expected"]
    target = manifest["target"]
    return "\n".join(
        [
            f"# Lean 失败案例：{manifest['capsule_id']}",
            "",
            "## 目标",
            "",
            f"- 文件：`{target.get('source_file')}`",
            f"- 定理：`{target.get('theorem', '未指定')}`",
            f"- 选择方式：`{target.get('selection_mode')}`",
            "",
            "## 期望诊断",
            "",
            f"- 类别：`{expected.get('category')}`",
            f"- diagnostic key：`{expected.get('diagnostic_key')}`",
            f"- 摘要：{expected.get('summary', '')}",
            "",
            "## 重放",
            "",
            "```powershell",
            "python -m leancapsule replay .",
            "```",
            "",
            "请在提交前人工确认 toolchain、来源许可和诊断是否仍然合理。",
            "",
        ]
    )

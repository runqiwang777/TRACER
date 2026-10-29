"""校验公开 v3 入口与冻结配置在重命名后仍保持一致。"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from v3 import (  # noqa: E402
    EXTENDED_CONFIG_PATH, MINIMAX_CONFIG_PATH, PROTOCOL_PATH,
    STUDY_PROTOCOL_VERSION, freeze_runtime_records,
)


class V3ReleaseTest(unittest.TestCase):
    def test_existing_runtime_records_match_the_derived_freeze_exactly(self):
        result = freeze_runtime_records()
        self.assertTrue(result["ok"])
        self.assertEqual(result["written"], [])

    def test_protocol_references_and_script_key_names_are_consistent(self):
        protocol = json.loads(PROTOCOL_PATH.read_text(encoding="utf-8"))
        self.assertEqual(protocol["version"], STUDY_PROTOCOL_VERSION)
        for role in protocol["model_roles"]:
            self.assertTrue((ROOT / role["runtime_config"]).is_file())
        for prereg in protocol["runtime_freeze"]["records"]:
            self.assertTrue((ROOT / prereg).is_file())
        scripts = [
            (ROOT / "scripts" / name).read_text(encoding="utf-8-sig")
            for name in ("preflight_v3.ps1", "run_v3_formal.ps1")
        ]
        for config_path in (EXTENDED_CONFIG_PATH, MINIMAX_CONFIG_PATH):
            config = json.loads(config_path.read_text(encoding="utf-8"))
            for model in config["models"]:
                key = model["api_key_env"]
                self.assertTrue(key.startswith("TRACER_V3_"))
                for script in scripts:
                    self.assertIn(key, script)
                    self.assertIn("Remove-Item Env:" + key, script)


if __name__ == "__main__":
    unittest.main()

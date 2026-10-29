import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DocumentationConsistencyTest(unittest.TestCase):
    def test_readmes_are_bilingual_and_link_current_protocols(self):
        en = (ROOT / "README.md").read_text(encoding="utf-8")
        zh = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        self.assertIn("[简体中文](README.zh-CN.md)", en)
        self.assertIn("[English](README.md)", zh)
        for readme in (en, zh):
            self.assertIn("docs/V3_EXPERIMENT_PROTOCOL.md", readme)
            self.assertIn("docs/security_policy.md", readme)
            self.assertNotIn("historical/", readme)
            self.assertNotIn("published/research-six-arm-313f437f", readme)

    def test_published_links_exist_and_are_current_security_artifacts(self):
        for name in ("README.md", "README.zh-CN.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            links = re.findall(r"\]\((published/[^)]+)\)", text)
            self.assertEqual(2, len(set(links)))
            for link in links:
                self.assertTrue((ROOT / link).exists(), link)

    def test_progress_distinguishes_protocol_from_completed_results(self):
        progress = (ROOT / "PROGRESS.md").read_text(encoding="utf-8")
        self.assertIn("未包括经全量审计的最终结果包", progress)
        self.assertIn("不在仓库中报告该批次的性能或因果结果", progress)
        self.assertIn("Windows Docker Desktop", progress)


if __name__ == "__main__":
    unittest.main()

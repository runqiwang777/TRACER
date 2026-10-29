import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_v3_formal.ps1"


class V3RunnerScriptTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.script = SCRIPT.read_text(encoding="utf-8")

    def test_uses_independent_batch_directories_and_frozen_inputs(self):
        self.assertIn('Directory = "extended"', self.script)
        self.assertIn('Directory = "minimax-confirmatory"', self.script)
        self.assertIn("tracer_extended_v3.json", self.script)
        self.assertIn("tracer_minimax_confirmatory_v3.json", self.script)
        self.assertIn("tracer_real_v2/manifest.json", self.script)
        self.assertIn('"v3-formal-$stamp-$suffix"', self.script)

    def test_resume_is_explicit_and_preserves_completed_batches(self):
        self.assertIn("-Resume requires the exact existing -RunRoot", self.script)
        self.assertIn("superseded v1/v2 protocol", self.script)
        self.assertIn("tracer-causal-study-protocol-v3", self.script)
        self.assertIn('Write-Host "v3 run root: $RunRoot"', self.script)
        self.assertIn('$runArguments += "--resume"', self.script)
        self.assertIn("already complete and passed audit; skipping it", self.script)
        self.assertNotIn("Remove-Item -Recurse", self.script)

    def test_failure_logs_and_artifacts_are_retained(self):
        self.assertIn('schema_version = "tracer-v3-runner-failure-v1"', self.script)
        self.assertIn("artifacts_retained = $true", self.script)
        self.assertIn("Tee-Object -FilePath $LogPath", self.script)

    def test_keys_are_hidden_and_removed(self):
        self.assertIn("Read-Host $Prompt -AsSecureString", self.script)
        for name in (
            "TRACER_V3_DEEPSEEK_KEY",
            "TRACER_V3_GLM_KEY",
            "TRACER_V3_MINIMAX_KEY",
        ):
            self.assertIn(f"Remove-Item Env:{name}", self.script)

    def test_all_pending_preflights_finish_before_any_formal_batch(self):
        preflight_loop = self.script.index("foreach ($preflightBatchName in $pending)")
        formal_loop = self.script.index("foreach ($batchName in $pending)", preflight_loop)
        self.assertLess(preflight_loop, formal_loop)
        self.assertLess(formal_loop, self.script.index('$runArguments = @(', formal_loop))

    def test_cost_limit_requires_explicit_choice(self):
        self.assertIn("Provide -ExtendedBudgetUsd or explicitly use -NoCostLimit", self.script)
        self.assertIn("Provide -MiniMaxBudgetUsd or explicitly use -NoCostLimit", self.script)
        self.assertIn("has frozen unknown prices", self.script)
        self.assertIn("the preregistered call-count limit still applies", self.script)
        self.assertIn('"--max-reserved-usd"', self.script)
        self.assertIn('"--no-cost-limit"', self.script)


if __name__ == "__main__":
    unittest.main()

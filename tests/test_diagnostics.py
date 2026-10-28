import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from diagnostics import normalize_diagnostics
from cache import canonical_request


class DiagnosticsTest(unittest.TestCase):
    def test_type_mismatch_is_compact(self):
        result = normalize_diagnostics(
            "C:/tmp/benchmark.lean:7:5: error: Type mismatch\n" + "x" * 5000,
            returncode=1,
        )
        self.assertEqual(result["category"], "type_mismatch")
        self.assertLessEqual(len(result["feedback"]), 1200)

    def test_timeout_category(self):
        result = normalize_diagnostics("Lean 编译超时（1s）", timed_out=True)
        self.assertEqual(result["category"], "timeout")

    def test_exact_request_key_is_stable(self):
        left = canonical_request("and_swap", "类别=type_mismatch", 2)
        right = canonical_request("and_swap", "类别=type_mismatch", 2)
        self.assertEqual(left, right)


if __name__ == "__main__":
    unittest.main()

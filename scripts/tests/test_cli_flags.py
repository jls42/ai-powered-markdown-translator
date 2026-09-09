"""`scripts/cli_flags.py` lit les flags sur le parser construit, pas sur un fichier."""

import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.cli_flags import cli_flags


class CliFlagsProbe(unittest.TestCase):
    def test_reads_at_least_the_documented_flag_count(self):
        flags = cli_flags()
        # 23 mesurés le 2026-09-07 ; le plancher de check-release-ready.sh est 22.
        self.assertGreaterEqual(len(flags), 22)
        self.assertIn("--use_codex", flags)
        self.assertIn("--target_lang", flags)

    def test_builtin_help_is_not_a_documented_flag(self):
        self.assertNotIn("--help", cli_flags())

    def test_only_long_options(self):
        self.assertTrue(all(flag.startswith("--") for flag in cli_flags()))


if __name__ == "__main__":
    unittest.main()

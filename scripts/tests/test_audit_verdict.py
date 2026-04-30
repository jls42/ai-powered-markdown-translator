"""Tests unittest pour scripts/audit_verdict.py.

Couvre les verdicts attendus sur la shape JSON de `pip-audit --format=json`.
"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

# Permet l'import de `scripts.audit_verdict` quand les tests tournent depuis
# scripts/tests/. La racine du projet est deux niveaux au-dessus.
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.audit_verdict import compute_audit_verdict


class TestAuditVerdict(unittest.TestCase):
    def test_ok_no_dependencies(self) -> None:
        self.assertEqual(compute_audit_verdict('{"dependencies": []}'), "ok")

    def test_ok_dependency_without_vulns(self) -> None:
        payload = json.dumps(
            {"dependencies": [{"name": "requests", "version": "2.32.3", "vulns": []}]}
        )
        self.assertEqual(compute_audit_verdict(payload), "ok")

    def test_vulnerable_one(self) -> None:
        payload = json.dumps(
            {
                "dependencies": [
                    {
                        "name": "requests",
                        "version": "2.0.0",
                        "vulns": [{"id": "GHSA-xxx", "fix_versions": ["2.32.0"]}],
                    }
                ]
            }
        )
        self.assertEqual(compute_audit_verdict(payload), "vulnerable:1")

    def test_vulnerable_multiple_across_deps(self) -> None:
        payload = json.dumps(
            {
                "dependencies": [
                    {
                        "name": "pkg-a",
                        "vulns": [{"id": "1"}, {"id": "2"}],
                    },
                    {
                        "name": "pkg-b",
                        "vulns": [{"id": "3"}, {"id": "4"}, {"id": "5"}],
                    },
                ]
            }
        )
        self.assertEqual(compute_audit_verdict(payload), "vulnerable:5")

    def test_parse_error_invalid_json(self) -> None:
        self.assertEqual(compute_audit_verdict("not-json"), "parse-error")

    def test_parse_error_empty_string(self) -> None:
        self.assertEqual(compute_audit_verdict(""), "parse-error")

    def test_no_metadata_root_not_object(self) -> None:
        self.assertEqual(compute_audit_verdict("[]"), "no-metadata")

    def test_no_metadata_missing_dependencies_key(self) -> None:
        self.assertEqual(compute_audit_verdict('{"foo": "bar"}'), "no-metadata")

    def test_no_metadata_dependencies_not_list(self) -> None:
        self.assertEqual(compute_audit_verdict('{"dependencies": "oops"}'), "no-metadata")

    def test_parse_error_dep_not_object(self) -> None:
        self.assertEqual(
            compute_audit_verdict('{"dependencies": ["not-a-dict"]}'), "parse-error"
        )

    def test_parse_error_vulns_not_list(self) -> None:
        payload = json.dumps(
            {"dependencies": [{"name": "x", "vulns": "not-a-list"}]}
        )
        self.assertEqual(compute_audit_verdict(payload), "parse-error")


if __name__ == "__main__":
    unittest.main()

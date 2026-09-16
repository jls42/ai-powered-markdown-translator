"""Tests de scripts/pypi_versions.py : le retard ne compte qu'après le délai.

Le contrôle de fraîcheur est un gate : s'il crie au loup sur une version que
Dependabot n'a pas encore le droit de proposer, on apprend à ne plus le lire ;
s'il se tait sur une version réellement bloquée, il ne sert plus à rien. Les
deux sens sont vérifiés, ainsi que l'alignement du délai sur dependabot.yml.
"""

from __future__ import annotations

import io
import json
import re
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.pypi_versions import (
    classify,
    main,
    published_final_releases,
    version_key,
)

# `timezone.utc` et non `datetime.UTC` : ces tests tournent aussi en 3.10.
NOW = datetime(2026, 9, 16, 12, 0, tzinfo=timezone.utc)  # noqa: UP017


def _file(days_ago: float, yanked: bool = False) -> dict:
    """Un fichier au format exact de PyPI, suffixe `Z` compris."""
    uploaded = NOW - timedelta(days=days_ago)
    return {"upload_time_iso_8601": uploaded.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), "yanked": yanked}


def _releases(**ages: float) -> dict[str, datetime]:
    """`_releases(**{"3.13.0": 6})` : version → publiée il y a N jours."""
    return {version: NOW - timedelta(days=days) for version, days in ages.items()}


class TestVersionKey(unittest.TestCase):
    def test_ordre_numerique_et_non_lexical(self) -> None:
        self.assertGreater(version_key("3.10.0"), version_key("3.9.0"))

    def test_zeros_finaux_sans_effet(self) -> None:
        self.assertEqual(version_key("3.10"), version_key("3.10.0"))
        self.assertEqual(version_key("0.0.0"), (0,))

    def test_version_non_finale_refusee(self) -> None:
        for version in ("3.15.0rc1", "2.9.0.post0", "1.0.dev1", ""):
            with self.subTest(version=version), self.assertRaises(ValueError):
                version_key(version)


class TestPublishedFinalReleases(unittest.TestCase):
    def test_ignore_preversions_fichiers_absents_et_retraits(self) -> None:
        payload = {
            "releases": {
                "3.14.0": [_file(2)],
                "3.15.0rc1": [_file(1)],
                "3.13.1.post1": [_file(1)],
                "3.12.0": [],
                "3.11.0": [_file(9, yanked=True), _file(9, yanked=True)],
                "3.10.0": [_file(12, yanked=True), _file(11)],
            }
        }
        self.assertEqual(sorted(published_final_releases(payload)), ["3.10.0", "3.14.0"])

    def test_date_du_premier_fichier(self) -> None:
        payload = {"releases": {"1.6.0": [_file(1), _file(3), _file(2)]}}
        self.assertEqual(published_final_releases(payload)["1.6.0"], NOW - timedelta(days=3))

    def test_releases_mal_forme(self) -> None:
        with self.assertRaises(ValueError):
            published_final_releases({"releases": []})
        with self.assertRaises(KeyError):
            published_final_releases({})


class TestClassify(unittest.TestCase):
    def test_a_jour(self) -> None:
        verdict = classify("3.14.1", _releases(**{"3.14.1": 1, "3.13.0": 6}), NOW, 5)
        self.assertEqual(verdict.status, "a-jour")

    def test_version_recente_en_route_et_non_en_retard(self) -> None:
        # Le cas du 2026-09-16 : 3.14.1 publiée la veille, épinglage 3.13.0.
        verdict = classify("3.13.0", _releases(**{"3.14.1": 0.8, "3.13.0": 5.7}), NOW, 5)
        self.assertEqual(verdict.status, "en-route")
        self.assertEqual((verdict.newest, verdict.newest_age), ("3.14.1", 0))

    def test_mineure_en_retard_au_dela_du_delai(self) -> None:
        verdict = classify("3.10.0", _releases(**{"3.14.1": 0.8, "3.13.0": 5.7}), NOW, 5)
        self.assertEqual(verdict.status, "mineure")
        self.assertEqual((verdict.eligible, verdict.eligible_age), ("3.13.0", 5))

    def test_majeure_en_retard(self) -> None:
        verdict = classify("2.9.4", _releases(**{"3.0.0": 8, "2.9.4": 30}), NOW, 5)
        self.assertEqual(verdict.status, "majeure")

    def test_majeure_recente_reste_en_route(self) -> None:
        verdict = classify("2.9.4", _releases(**{"3.0.0": 2, "2.9.4": 30}), NOW, 5)
        self.assertEqual(verdict.status, "en-route")

    def test_epinglage_en_avance_sur_la_version_eligible(self) -> None:
        # Bump manuel avant la fin du délai : la version éligible est plus
        # ancienne que l'épinglage, ce n'est pas un retard.
        verdict = classify("3.14.1", _releases(**{"3.14.1": 0.8, "3.13.0": 5.7}), NOW, 5)
        self.assertEqual(verdict.status, "a-jour")
        self.assertEqual(verdict.eligible, "3.13.0")

    def test_borne_du_delai_incluse(self) -> None:
        verdict = classify("1.5.0", _releases(**{"1.6.0": 5, "1.5.0": 20}), NOW, 5)
        self.assertEqual(verdict.status, "mineure")

    def test_versionnage_par_date_de_certifi(self) -> None:
        releases = _releases(**{"2026.9.1": 10, "2026.7.22": 60})
        self.assertEqual(classify("2026.7.22", releases, NOW, 5).status, "mineure")
        releases = _releases(**{"2027.1.5": 10, "2026.7.22": 200})
        self.assertEqual(classify("2026.7.22", releases, NOW, 5).status, "majeure")

    def test_aucune_publication(self) -> None:
        verdict = classify("1.0.0", {}, NOW, 5)
        self.assertEqual(verdict.as_line(), "a-jour\t1.0.0\t-\t-\t-\t-")


class TestMain(unittest.TestCase):
    def _run(self, payload: str, *argv: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = main(list(argv), stdin=io.StringIO(payload), now=NOW)
        return code, out.getvalue(), err.getvalue()

    def test_ligne_tabulee(self) -> None:
        payload = json.dumps({"releases": {"3.14.1": [_file(0.8)], "3.13.0": [_file(5.7)]}})
        code, out, _ = self._run(payload, "--pinned", "3.10.0", "--grace-days", "5")
        self.assertEqual(code, 0)
        self.assertEqual(out, "mineure\t3.10.0\t3.13.0\t5\t3.14.1\t0\n")

    def test_json_illisible(self) -> None:
        code, out, err = self._run("<html>", "--pinned", "1.0.0", "--grace-days", "5")
        self.assertEqual((code, out), (2, ""))
        self.assertIn("pypi_versions", err)

    def test_epinglage_non_comparable(self) -> None:
        payload = json.dumps({"releases": {"1.0.0": [_file(9)]}})
        code, _, err = self._run(payload, "--pinned", "1.0.0rc1", "--grace-days", "5")
        self.assertEqual(code, 2)
        self.assertIn("non comparable", err)

    def test_delai_invalide_refuse(self) -> None:
        for delai in ("-1", "nan", "abc"):
            with self.subTest(delai=delai), self.assertRaises(SystemExit) as ctx:
                self._run("{}", "--pinned", "1.0.0", "--grace-days", delai)
            self.assertEqual(ctx.exception.code, 2)


CADENCE_DAYS = {"daily": 1, "weekly": 7, "monthly": 31}


class TestAlignementSurDependabot(unittest.TestCase):
    """Le délai du gate se déduit de dependabot.yml ; une dérive les désaccorde."""

    def _search(self, pattern: str, text: str, what: str, flags: int = re.M) -> str:
        match = re.search(pattern, text, flags)
        if match is None:
            self.fail(f"{what} introuvable")
        return match.group(1)

    def test_delai_du_gate_egal_refroidissement_plus_cadence_plus_un(self) -> None:
        config = (ROOT / ".github" / "dependabot.yml").read_text(encoding="utf-8")
        pip_entry = r"- package-ecosystem: pip\n(.*?)(?=\n  - package-ecosystem:|\Z)"
        block = self._search(pip_entry, config, "entrée pip de dependabot.yml", re.S)
        interval = self._search(r"^\s+interval: (\w+)", block, "schedule.interval (pip)")
        cooldown = self._search(r"^\s+default-days: (\d+)", block, "cooldown.default-days (pip)")
        expected = int(cooldown) + CADENCE_DAYS[interval] + 1

        script = (ROOT / "scripts" / "check-deps-fresh.sh").read_text(encoding="utf-8")
        grace = self._search(r"^GRACE_DAYS=(\d+)$", script, "GRACE_DAYS de check-deps-fresh.sh")
        self.assertEqual(int(grace), expected)


if __name__ == "__main__":
    unittest.main()

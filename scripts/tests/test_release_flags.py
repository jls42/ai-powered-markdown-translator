"""Tests unittest sur l'analyse des options de release.sh.

Régression couverte : `--dry-run` assignait `MODE="dry-run"`, écrasant le
`--tag-only` posé avant lui. Comme `MODE` n'est comparé qu'à `"tag-only"`,
cette assignation n'apportait rien — mais elle faisait basculer
`--tag-only --dry-run` dans le mode principal, dont le pré-check refuse de
tourner depuis `main`. La simulation de la phase 2 échouait donc sur
« Refus de release depuis 'main' », un diagnostic sans aucun rapport avec ce
qu'elle prétendait simuler. Le plus gênant n'est pas l'échec : c'est qu'il
ressemblait à un vrai garde-fou.
"""

from __future__ import annotations

import subprocess  # nosec B404 — exécute release.sh du dépôt pour observer son dispatch
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RELEASE_SH = ROOT / "release.sh"
VENV_ACTIVATE = ROOT / "venv" / "bin" / "activate"

TAG_ONLY_BANNER = "Mode tag-only"
MAIN_MODE_BANNER = "Pré-checks..."


def _run_release(*flags: str) -> str:
    """Lance release.sh et renvoie sa sortie combinée.

    Toutes les invocations testées portent `--dry-run`, donc `run()` n'exécute
    aucune commande mutante. Le script sort de toute façon en erreur peu après
    la bannière de mode (working tree, tag déjà présent…) : seule la bannière
    nous intéresse, elle est émise avant tout effet.
    """
    # Délai court et TimeoutExpired traité comme un résultat, pas comme une
    # erreur. Sous la régression, `--tag-only --dry-run` tombe dans le mode
    # principal — qui relance TOUTE la suite de tests, donc depuis ces tests
    # eux-mêmes. Mesuré avec le bug réintroduit : 120 s au lieu de 0,04 s. On
    # veut que le test échoue VITE et sur la bonne raison (bannière absente),
    # pas qu'il traîne sur un chemin qu'il n'aurait jamais dû emprunter.
    try:
        proc = subprocess.run(  # nosec B603 — chemin absolu du script du dépôt
            # Chemin ABSOLU du script, et pas `["bash", ...]` : un `bash` nu se
            # résout via le PATH (Bandit B607), et surtout on veut exercer
            # l'invocation telle qu'un utilisateur la fait — shebang compris.
            [str(RELEASE_SH), *flags],  # nosemgrep
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=20,
            check=False,
        )
    except subprocess.TimeoutExpired as expired:
        return (expired.stdout or b"").decode("utf-8", "replace") + (expired.stderr or b"").decode(
            "utf-8", "replace"
        )
    return proc.stdout + proc.stderr


@unittest.skipUnless(
    VENV_ACTIVATE.is_file(),
    "release.sh source venv/bin/activate avant de dispatcher : sans venv, "
    "il sort avant la bannière de mode et le test ne prouverait rien.",
)
class TestDryRunIsOrthogonalToMode(unittest.TestCase):
    """`--dry-run` est un MODIFICATEUR, pas un mode."""

    def test_tag_only_then_dry_run_stays_in_tag_only(self) -> None:
        out = _run_release("--tag-only", "--dry-run")
        self.assertIn(TAG_ONLY_BANNER, out)
        self.assertNotIn("Refus de release", out)

    def test_dry_run_then_tag_only_stays_in_tag_only(self) -> None:
        """L'ordre des options ne doit rien changer."""
        out = _run_release("--dry-run", "--tag-only")
        self.assertIn(TAG_ONLY_BANNER, out)
        self.assertNotIn("Refus de release", out)


class TestDryRunNeverAssignsMode(unittest.TestCase):
    """Verrou statique sur la CAUSE, en plus du verrou comportemental.

    Les tests d'exécution ci-dessus dépendent du venv et sont donc skippés en
    CI. Celui-ci lit la source : il tient partout, et il échouerait dès qu'un
    refactor réintroduirait l'assignation fautive.
    """

    @staticmethod
    def _case_code(flag: str) -> str:
        """Corps d'un `case` donné, COMMENTAIRES RETIRÉS.

        Le commentaire qui explique la régression cite forcément `MODE=` : sans
        ce filtrage, l'assertion échouerait sur sa propre documentation.
        """
        src = RELEASE_SH.read_text(encoding="utf-8")
        start = src.index(flag)
        end = src.index(";;", start)
        lines = src[start:end].splitlines()
        return "\n".join(ln for ln in lines if not ln.lstrip().startswith("#"))

    def test_dry_run_case_does_not_touch_mode(self) -> None:
        body = self._case_code("--dry-run)")
        self.assertIn("DRY_RUN=true", body)
        self.assertNotIn(
            "MODE=",
            body,
            "`--dry-run` ne doit pas assigner MODE : il écraserait --tag-only",
        )

    def test_other_modes_still_assign_mode(self) -> None:
        """Garde-fou du garde-fou : si plus aucun mode n'assignait MODE, le
        test ci-dessus passerait au vert en ne vérifiant plus rien."""
        for flag in ("--auto)", "--local-only)", "--tag-only)"):
            self.assertIn("MODE=", self._case_code(flag), f"{flag} devrait assigner MODE")


if __name__ == "__main__":
    unittest.main()

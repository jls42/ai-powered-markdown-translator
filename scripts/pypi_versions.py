#!/usr/bin/env python3
"""Situe une version épinglée par rapport aux publications PyPI, délai compris.

Raison d'être : Dependabot ne propose une version que trois jours après sa
publication (délai de refroidissement, par défaut depuis juillet 2026), puis la
fusionne au passage suivant. Comparer l'épinglage à la toute dernière version
de PyPI signalait donc comme « en retard » des versions que l'automatisation
n'avait pas encore le droit de proposer — un avertissement faux, et un
avertissement faux apprend à ne plus lire les vrais.

Une version n'est donc comptée en retard qu'une fois publiée depuis au moins
`--grace-days` jours. Avant, elle est « en route ».

Lit sur stdin le JSON de https://pypi.org/pypi/<paquet>/json et écrit une ligne
séparée par des tabulations :

    STATUT  ÉPINGLÉE  ÉLIGIBLE  ÂGE_ÉLIGIBLE  DERNIÈRE  ÂGE_DERNIÈRE

(`-` quand une valeur n'existe pas ; les âges sont en jours entiers.)

STATUT vaut `a-jour`, `en-route`, `mineure` ou `majeure`. « Majeure » compare le
PREMIER composant : cela couvre le versionnage sémantique comme le versionnage
par date de certifi (2024.x → 2026.x).

Seules les versions finales purement numériques comptent : pré-versions,
`.post` et `.dev` sont ignorées, de même qu'une version dont tous les fichiers
ont été retirés (yanked). Code de sortie 2 si le JSON est illisible ou si la
version épinglée n'est pas comparable.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, TextIO

_FINAL_VERSION = re.compile(r"^\d+(?:\.\d+)*$")
_SECONDS_PER_DAY = 86400
# `datetime.UTC` n'existe qu'à partir de 3.11, et la matrice de tests.yml
# exécute scripts/tests en 3.10 : mesuré, l'import cassait toute la suite.
_UTC = timezone.utc  # noqa: UP017


def version_key(version: str) -> tuple[int, ...]:
    """Clé de tri numérique ; `3.10` et `3.10.0` sont égales."""
    if not _FINAL_VERSION.match(version):
        raise ValueError(f"version non comparable : {version!r}")
    parts = [int(part) for part in version.split(".")]
    while len(parts) > 1 and parts[-1] == 0:
        parts.pop()
    return tuple(parts)


def published_final_releases(payload: dict[str, Any]) -> dict[str, datetime]:
    """Versions finales publiées, avec la date de leur premier fichier."""
    releases = payload["releases"]
    if not isinstance(releases, dict):
        raise ValueError("champ `releases` mal formé")
    published = {}
    for version, files in releases.items():
        if not _FINAL_VERSION.match(version) or not files:
            continue
        if all(entry.get("yanked", False) for entry in files):
            continue
        uploads = [_parse_upload_time(entry["upload_time_iso_8601"]) for entry in files]
        published[version] = min(uploads)
    return published


def _parse_upload_time(raw: str) -> datetime:
    # PyPI écrit `2026-09-15T23:13:33.164661Z`, et `fromisoformat` n'accepte le
    # suffixe `Z` qu'à partir de 3.11.
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))


def _age_days(published_at: datetime, now: datetime) -> float:
    return (now - published_at).total_seconds() / _SECONDS_PER_DAY


def _newest(versions: list[str]) -> str | None:
    return max(versions, key=version_key) if versions else None


@dataclass(frozen=True)
class Verdict:
    status: str
    pinned: str
    eligible: str | None
    eligible_age: int | None
    newest: str | None
    newest_age: int | None

    def as_line(self) -> str:
        fields = (
            self.status,
            self.pinned,
            self.eligible,
            self.eligible_age,
            self.newest,
            self.newest_age,
        )
        return "\t".join("-" if value is None else str(value) for value in fields)


def _status(pinned_key: tuple[int, ...], eligible: str | None, newest: str | None) -> str:
    if eligible is not None and version_key(eligible) > pinned_key:
        return "majeure" if version_key(eligible)[0] > pinned_key[0] else "mineure"
    if newest is not None and version_key(newest) > pinned_key:
        return "en-route"
    return "a-jour"


def classify(
    pinned: str, releases: dict[str, datetime], now: datetime, grace_days: float
) -> Verdict:
    """Compare l'épinglage à la version la plus récente sortie du délai de grâce."""
    pinned_key = version_key(pinned)
    ages = {version: _age_days(published_at, now) for version, published_at in releases.items()}
    newest = _newest(list(ages))
    eligible = _newest([version for version, age in ages.items() if age >= grace_days])
    return Verdict(
        status=_status(pinned_key, eligible, newest),
        pinned=pinned,
        eligible=eligible,
        eligible_age=None if eligible is None else int(ages[eligible]),
        newest=newest,
        newest_age=None if newest is None else int(ages[newest]),
    )


def _non_negative_days(raw: str) -> float:
    value = float(raw)
    # `nan` passerait `value < 0` et rendrait toute version inéligible en silence.
    if not math.isfinite(value) or value < 0:
        raise argparse.ArgumentTypeError("le délai doit être un nombre positif ou nul")
    return value


def main(
    argv: list[str] | None = None, stdin: TextIO | None = None, now: datetime | None = None
) -> int:
    parser = argparse.ArgumentParser(description="Situe une version épinglée face à PyPI.")
    parser.add_argument("--pinned", required=True, help="version épinglée dans requirements.txt")
    parser.add_argument("--grace-days", required=True, type=_non_negative_days, help="en jours")
    args = parser.parse_args(argv)
    try:
        payload = json.load(stdin if stdin is not None else sys.stdin)
        releases = published_final_releases(payload)
        verdict = classify(args.pinned, releases, now or datetime.now(_UTC), args.grace_days)
    except (ValueError, KeyError, TypeError, AttributeError) as exc:
        print(f"pypi_versions : {exc}", file=sys.stderr)
        return 2
    print(verdict.as_line())
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# Calcule un verdict bash-friendly à partir du JSON de `pip-audit --format=json`.
# Lecture stdin pour rester compatible avec le pipe utilisé par check-pip-audit.sh.
# Sortie : `ok` | `vulnerable:N` | `parse-error` | `no-metadata`.
#
# Adapté de scripts/audit-verdict.py de jls42-astro (qui ciblait npm audit).
# Voir scripts/tests/test_audit_verdict.py pour les invariants couverts.

from __future__ import annotations

import json
import sys
from typing import Any


def compute_audit_verdict(raw_json: str) -> str:
    """Classifie le JSON `pip-audit` en un verdict short-string."""
    try:
        parsed = json.loads(raw_json)
    except json.JSONDecodeError:
        return "parse-error"

    if not isinstance(parsed, dict):
        return "no-metadata"

    dependencies = parsed.get("dependencies")
    if not isinstance(dependencies, list):
        return "no-metadata"

    total = _count_vulnerabilities(dependencies)
    if total is None:
        return "parse-error"
    return f"vulnerable:{total}" if total > 0 else "ok"


def _count_vulnerabilities(dependencies: list[Any]) -> int | None:
    """Compte le total de vulns sur toutes les dépendances. None si shape invalide."""
    total = 0
    for dep in dependencies:
        if not isinstance(dep, dict):
            return None
        vulns = dep.get("vulns", [])
        if not isinstance(vulns, list):
            return None
        total += len(vulns)
    return total


def main() -> int:
    raw = sys.stdin.read()
    sys.stdout.write(compute_audit_verdict(raw) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())

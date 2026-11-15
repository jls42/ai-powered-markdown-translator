#!/usr/bin/env python3
"""Tour des catalogues : ce que chaque API et chaque CLI sert vraiment, comparé
aux modèles par défaut d'aipmt.

Tout est gratuit : endpoints de liste des API, `agy models`, `grok models`,
cache du catalogue Codex. Les clés sont lues dans le .env du dépôt et ne sont
jamais affichées.

    venv/bin/python .claude/skills/aipmt-tour-modeles/scripts/catalogues.py [DÉPÔT]

À lancer avec le python du venv du dépôt (il faut python-dotenv et le paquet
aipmt de `src/`). Code retour 1 si un modèle par défaut n'est plus servi.
"""

import datetime
import json
import os
import shutil
import subprocess  # nosec B404 — lit le catalogue des CLI, argv fixes
import sys
import urllib.error
import urllib.request

REPO = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.getcwd())
sys.path.insert(0, os.path.join(REPO, "src"))

# Environnement des CLI, copié AVANT l'import d'aipmt : `aipmt.config` charge le
# .env dans os.environ, et un `grok models` qui hérite de XAI_API_KEY liste le
# catalogue de l'API (auth_method api_key) au lieu de celui de l'abonnement —
# constaté le 2026-11-15. Les variables de clé déjà présentes sont retirées aussi.
CLI_ENV = {
    k: v
    for k, v in os.environ.items()
    if not k.endswith(("_API_KEY", "_AUTH_TOKEN")) and k not in ("GOOGLE_APPLICATION_CREDENTIALS",)
}
CLI_ENV["AGY_CLI_DISABLE_AUTO_UPDATE"] = "true"

from dotenv import dotenv_values  # noqa: E402

from aipmt.providers import (  # noqa: E402
    anthropic,
    antigravity,
    codex,
    gemini,
    grok,
    mistral,
    openai,
)

ENV = dotenv_values(os.path.join(REPO, ".env"))


def get(url, headers):
    request = urllib.request.Request(url, headers={"User-Agent": "aipmt-audit", **headers})
    # URL https écrites en dur dans ce fichier, jamais reçues de l'extérieur.
    with urllib.request.urlopen(request, timeout=30) as response:  # nosec B310
        return json.load(response)


def day(value):
    try:
        return datetime.datetime.fromtimestamp(int(value), datetime.UTC).strftime("%Y-%m-%d")
    except (TypeError, ValueError):
        return str(value or "")[:10]


def api_openai():
    data = get(
        "https://api.openai.com/v1/models", {"Authorization": f"Bearer {ENV['OPENAI_API_KEY']}"}
    )
    return {m["id"]: day(m["created"]) for m in data["data"] if m["id"].startswith("gpt-")}


def api_anthropic():
    data = get(
        "https://api.anthropic.com/v1/models?limit=1000",
        {"x-api-key": ENV["ANTHROPIC_API_KEY"], "anthropic-version": "2023-06-01"},
    )
    return {m["id"]: m.get("created_at", "")[:10] for m in data["data"]}


def api_mistral():
    data = get(
        "https://api.mistral.ai/v1/models", {"Authorization": f"Bearer {ENV['MISTRAL_API_KEY']}"}
    )
    served = {}
    for m in data["data"]:
        if (m.get("capabilities") or {}).get("completion_chat"):
            aliases = ",".join(m.get("aliases") or [])
            served[m["id"]] = f"ctx={m.get('max_context_length')} alias={aliases}"[:90]
    return served


def api_xai():
    data = get("https://api.x.ai/v1/models", {"Authorization": f"Bearer {ENV['XAI_API_KEY']}"})
    return {m["id"]: day(m.get("created")) for m in data["data"]}


def api_gemini():
    key = ENV.get("GOOGLE_API_KEY") or ENV.get("GEMINI_API_KEY")
    data = get(
        "https://generativelanguage.googleapis.com/v1beta/models?pageSize=1000",
        {"x-goog-api-key": key},
    )
    return {
        m["name"].removeprefix(
            "models/"
        ): f"in={m.get('inputTokenLimit')} out={m.get('outputTokenLimit')}"
        for m in data.get("models", [])
        if "generateContent" in m.get("supportedGenerationMethods", [])
    }


def cli_path(name):
    """Chemin absolu d'un CLI : un nom nu laisserait le PATH choisir le binaire."""
    path = shutil.which(name)
    if path is None:
        raise FileNotFoundError(f"{name} introuvable dans le PATH")
    return path


def run_cli(argv, timeout):
    """Lance un CLI avec un argv fixe, sans shell, et sans les clés d'API."""
    return subprocess.run(  # nosec B603
        argv, capture_output=True, text=True, env=CLI_ENV, timeout=timeout, check=False
    )


def cli_agy():
    # agy se met à jour seul quand on le lance hors d'aipmt : on le lui interdit,
    # pour que la version annoncée soit celle qui a produit la liste.
    agy = cli_path("agy")
    version = run_cli([agy, "--version"], timeout=60)
    out = run_cli([agy, "models"], timeout=90)
    served = {}
    for line in out.stdout.splitlines():
        if "\t" in line:
            slug, label = line.split("\t", 1)
            served[slug.strip()] = label.strip()
    print(f"  (agy {version.stdout.strip()})")
    return served


def cli_codex():
    # Jamais ~/.codex/auth.json : seulement le cache du catalogue.
    path = os.path.expanduser("~/.codex/models_cache.json")
    with open(path, encoding="utf-8") as f:
        cache = json.load(f)
    print(f"  (cache du {cache.get('fetched_at', '?')[:10]}, client {cache.get('client_version')})")
    return {
        m["slug"]: f"priorité {m.get('priority')} ctx={m.get('context_window')}"
        for m in cache["models"]
        if m.get("visibility") == "list"
    }


def cli_grok():
    out = run_cli([cli_path("grok"), "models"], timeout=90)
    text = out.stdout + out.stderr
    if "not authenticated" in text.lower():
        print("  ⚠ grok : « You are not authenticated. » — catalogue non fiable (grok login)")
    served = {}
    for line in text.splitlines():
        line = line.strip()
        if line.startswith(("* ", "- ")):
            served[line[2:].split()[0]] = line[2:]
    return served


SOURCES = [
    ("OpenAI (API)", api_openai, openai.DEFAULT_MODEL_OPENAI, openai.ECO_MODEL_OPENAI),
    ("Claude (API)", api_anthropic, anthropic.DEFAULT_MODEL_CLAUDE, anthropic.ECO_MODEL_CLAUDE),
    ("Mistral (API)", api_mistral, mistral.DEFAULT_MODEL_MISTRAL, mistral.ECO_MODEL_MISTRAL),
    ("Gemini (API)", api_gemini, gemini.DEFAULT_MODEL_GEMINI, gemini.ECO_MODEL_GEMINI),
    ("Grok (API)", api_xai, grok.DEFAULT_MODEL_GROK, grok.ECO_MODEL_GROK),
    (
        "Antigravity (agy)",
        cli_agy,
        antigravity.DEFAULT_MODEL_ANTIGRAVITY,
        antigravity.ECO_MODEL_ANTIGRAVITY,
    ),
    ("Codex (cache)", cli_codex, codex.DEFAULT_MODEL_CODEX, codex.ECO_MODEL_CODEX),
    ("Grok CLI", cli_grok, grok.DEFAULT_MODEL_GROK_CLI, grok.ECO_MODEL_GROK_CLI),
]


def main():
    missing = 0
    for name, fetch, default, eco in SOURCES:
        print(f"\n===== {name} =====")
        try:
            served = fetch()
        except (
            urllib.error.URLError,
            OSError,
            KeyError,
            ValueError,
            subprocess.SubprocessError,
        ) as e:
            print(f"  ERREUR {type(e).__name__}: {str(e)[:200]}")
            continue
        for role, model in (("défaut", default), ("éco", eco)):
            ok = model in served
            missing += not ok
            print(f"  {'✓' if ok else '✗ ABSENT'} {role} : {model}")
        for model, info in served.items():
            print(f"    {model:44} {info}")
    print(f"\n{missing} modèle(s) par défaut absent(s) de son catalogue.")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())

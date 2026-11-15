#!/usr/bin/env python3
"""Recoupement des prix, gratuit : `GET /v1/language-models` de xAI (ses propres
prix) et le catalogue public d'OpenRouter (prix de revente, à ne citer que comme
recoupement). La source qui fait foi reste la page de prix de l'éditeur.

    venv/bin/python .claude/skills/aipmt-tour-modeles/scripts/prix.py [DÉPÔT] [préfixe...]

Sans préfixe : les familles suivies par aipmt.
"""

import json
import os
import sys
import urllib.error
import urllib.request

from dotenv import dotenv_values

REPO = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.getcwd())
PREFIXES = tuple(sys.argv[2:]) or (
    "google/gemini-4",
    "google/gemini-3.8",
    "google/gemini-3.5-flash",
    "google/gemini-3.1-flash-lite",
    "openai/gpt-6",
    "openai/gpt-5.6",
    "x-ai/grok-4",
    "mistralai/mistral-large",
    "mistralai/mistral-small",
    "mistralai/mistral-medium",
    "anthropic/claude-",
)


def get(url, headers=None):
    request = urllib.request.Request(url, headers={"User-Agent": "aipmt-audit", **(headers or {})})
    # URL https écrite en dur dans ce fichier, jamais reçue de l'extérieur.
    with urllib.request.urlopen(request, timeout=30) as response:  # nosec B310
        return json.load(response)


def per_million(price):
    """Prix par token d'OpenRouter, ramené au million."""
    return f"{float(price) * 1e6:g}" if price not in (None, "") else "?"


def main():
    env = dotenv_values(os.path.join(REPO, ".env"))
    print(
        "== xAI /v1/language-models ($ par million : la valeur vaut des dix-millièmes de cent par million) =="
    )
    try:
        data = get(
            "https://api.x.ai/v1/language-models", {"Authorization": f"Bearer {env['XAI_API_KEY']}"}
        )
        for m in data.get("models", []):
            price_in = m.get("prompt_text_token_price", 0) / 10000
            price_out = m.get("completion_text_token_price", 0) / 10000
            print(f"  {m['id']:36} entrée={price_in:g} sortie={price_out:g}")
    except (urllib.error.URLError, OSError, KeyError, ValueError) as e:
        print(f"  ERREUR {type(e).__name__}: {str(e)[:200]}")
    print("\n== OpenRouter ($ par million) ==")
    for m in sorted(get("https://openrouter.ai/api/v1/models")["data"], key=lambda m: m["id"]):
        if m["id"].startswith(PREFIXES) and ":" not in m["id"]:
            pricing = m.get("pricing", {})
            print(
                f"  {m['id']:44} entrée={per_million(pricing.get('prompt')):>6} "
                f"sortie={per_million(pricing.get('completion')):>6} ctx={m.get('context_length')}"
            )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Sonde des niveaux de `reasoning_effort` qu'un modèle accepte sur une API
compatible OpenAI, et de ce que chacun coûte en tokens de raisonnement.
Quelques centimes au plus : un petit segment par niveau.

    venv/bin/python .claude/skills/aipmt-tour-modeles/scripts/effort.py xai grok-4.7,grok-4.3 [DÉPÔT]
    venv/bin/python .claude/skills/aipmt-tour-modeles/scripts/effort.py openai gpt-6.1-terra

Le refus de xAI ne se lit que dans le corps de l'erreur : on l'affiche.
"""

import os
import sys
import time

from dotenv import dotenv_values
from openai import BadRequestError, OpenAI

PROVIDERS = {"xai": ("XAI_API_KEY", "https://api.x.ai/v1"), "openai": ("OPENAI_API_KEY", None)}
SEGMENT = (
    "# Installer l'outil\n\nCe guide explique comment installer l'outil. Lancez `pip install aipmt` "
    "dans un environnement virtuel, puis tapez `aipmt --help`. Voir [la suite](#verifier).\n"
)


def main():
    provider, models = sys.argv[1], sys.argv[2].split(",")
    repo = os.path.abspath(sys.argv[3] if len(sys.argv) > 3 else os.getcwd())
    key_name, base_url = PROVIDERS[provider]
    key = dotenv_values(os.path.join(repo, ".env"))[key_name]
    client = OpenAI(api_key=key, base_url=base_url, timeout=120, max_retries=0)
    messages = [
        {
            "role": "system",
            "content": "Translate the Markdown from French to English. Output only the translation.",
        },
        {"role": "user", "content": SEGMENT},
    ]
    for model in models:
        for effort in (None, "none", "minimal", "low", "medium", "high"):
            kwargs = {} if effort is None else {"reasoning_effort": effort}
            start = time.time()
            try:
                response = client.chat.completions.create(model=model, messages=messages, **kwargs)
            except BadRequestError as e:
                print(f"{model} effort={effort}: 400 {str(e.body)[:140]}")
                continue
            usage = response.usage
            details = getattr(usage, "completion_tokens_details", None)
            print(
                f"{model} effort={effort}: {time.time() - start:.1f}s sortie={usage.completion_tokens} "
                f"raisonnement={getattr(details, 'reasoning_tokens', '?')}"
            )


if __name__ == "__main__":
    main()

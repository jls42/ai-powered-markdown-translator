"""Provider Mistral AI (API).

Le SDK `mistralai` ne réessaie RIEN par défaut, contrairement à ceux d'OpenAI
et d'Anthropic : sans `retry_config`, un seul HTTP 429 faisait échouer le
fichier entier. Or les plafonds sont bas et propres à chaque modèle — mesurés
le 2026-09-17 sur le compte du dépôt : 15 requêtes/min pour Large 3, 100 000
tokens/min pour Small 4. Une campagne à quatre traductions simultanées sur
Small en a perdu cinq sur quatre-vingt-quatre.
"""

import os

from mistralai.client import Mistral
from mistralai.client.utils import BackoffStrategy, RetryConfig

from ..config import _missing_key_message
from .base import _reason_name

DEFAULT_MISTRAL_API_KEY = "votre-cle-api-mistral-par-defaut"  # pragma: allowlist secret


DEFAULT_MODEL_MISTRAL = "mistral-large-latest"


ECO_MODEL_MISTRAL = "mistral-small-latest"


# Réessais sur 429, 500, 502, 503 et 504 — la liste que le SDK applique à
# `chat.complete` — et sur les erreurs de connexion. Le 429 de Mistral ne porte
# AUCUN `Retry-After` (mesuré : seulement `x-ratelimit-remaining-req-minute: 0`),
# donc le SDK ne sait pas combien attendre : c'est le backoff qui doit couvrir
# une fenêtre d'une minute. 2 s, 4 s, 8 s… plafonné à 60 s, plus une gigue de 0
# à 1 s ; abandon cinq minutes après le premier essai, et le 429 remonte alors
# comme avant.
MISTRAL_RETRY_CONFIG = RetryConfig(
    "backoff",
    BackoffStrategy(
        initial_interval=2_000, max_interval=60_000, exponent=2.0, max_elapsed_time=300_000
    ),
    retry_connection_errors=True,
)


# Types de blocs qui ne portent pas de texte traduit. Small 4 et Medium 3.5
# raisonnent quand on le leur demande (`reasoning_effort`) : la réponse devient
# alors une LISTE de blocs `thinking` puis `text` au lieu d'une chaîne (mesuré le
# 2026-09-17). Rien ne le demande ici, mais un défaut qui change côté
# fournisseur ne doit pas finir en AttributeError opaque sur `.strip()` — même
# garde-fou que pour Claude.
_MISTRAL_NON_TEXT_CHUNK_TYPES = frozenset({"thinking"})


def _mistral_text(content, model):
    """Texte d'une réponse Mistral : chaîne telle quelle, ou blocs de texte d'une
    liste dont les blocs de raisonnement sont écartés."""
    # Même garde que sur le chemin OpenAI : un `content` à None produisait un
    # AttributeError opaque sur `.strip()` au lieu d'un message exploitable.
    if content is None:
        raise RuntimeError(f"Mistral returned no content (model={model})")
    if isinstance(content, str):
        return content
    texts = [
        chunk.text
        for chunk in content
        if getattr(chunk, "type", None) not in _MISTRAL_NON_TEXT_CHUNK_TYPES
        and isinstance(getattr(chunk, "text", None), str)
    ]
    if not texts:
        types = [getattr(chunk, "type", "?") for chunk in content]
        raise RuntimeError(
            f"Mistral n'a renvoyé aucun bloc de texte (model={model}, blocs={types})"
        )
    # Bout à bout, sans séparateur : les blocs `text` d'une même réponse se
    # suivent, et en insérer un inventerait une structure absente de la sortie.
    return "".join(texts)


def _call_mistral(client, args, prompt, segment):
    messages = [{"role": "user", "content": prompt + "\n\n" + segment}]
    response = client.chat.complete(model=args.model, messages=messages)
    finish = _reason_name(response.choices[0].finish_reason)
    if finish not in ("stop", "STOP", None):
        raise RuntimeError(f"Mistral abnormal finish_reason={finish!r} (model={args.model})")
    return _mistral_text(response.choices[0].message.content, args.model).strip()


def _init_mistral_client(args):
    args.model = args.model or (ECO_MODEL_MISTRAL if args.eco else DEFAULT_MODEL_MISTRAL)
    api_key = os.getenv("MISTRAL_API_KEY", DEFAULT_MISTRAL_API_KEY)
    if not api_key or api_key == DEFAULT_MISTRAL_API_KEY:
        raise ValueError(_missing_key_message("Mistral", ["MISTRAL_API_KEY"]))
    return Mistral(api_key=api_key, retry_config=MISTRAL_RETRY_CONFIG)

"""Provider Mistral AI (API)."""

import os

from mistralai.client import Mistral

from ..config import _missing_key_message
from .base import _reason_name

DEFAULT_MISTRAL_API_KEY = "votre-cle-api-mistral-par-defaut"  # pragma: allowlist secret


DEFAULT_MODEL_MISTRAL = "mistral-large-latest"


ECO_MODEL_MISTRAL = "mistral-small-latest"


def _call_mistral(client, args, prompt, segment):
    messages = [{"role": "user", "content": prompt + "\n\n" + segment}]
    response = client.chat.complete(model=args.model, messages=messages)
    finish = _reason_name(response.choices[0].finish_reason)
    if finish not in ("stop", "STOP", None):
        raise RuntimeError(f"Mistral abnormal finish_reason={finish!r} (model={args.model})")
    # Même garde que sur le chemin OpenAI : un `content` à None produisait un
    # AttributeError opaque sur `.strip()` au lieu d'un message exploitable.
    content = response.choices[0].message.content
    if content is None:
        raise RuntimeError(f"Mistral returned no content (model={args.model})")
    return content.strip()


def _init_mistral_client(args):
    args.model = args.model or (ECO_MODEL_MISTRAL if args.eco else DEFAULT_MODEL_MISTRAL)
    api_key = os.getenv("MISTRAL_API_KEY", DEFAULT_MISTRAL_API_KEY)
    if not api_key or api_key == DEFAULT_MISTRAL_API_KEY:
        raise ValueError(_missing_key_message("Mistral", ["MISTRAL_API_KEY"]))
    return Mistral(api_key=api_key)

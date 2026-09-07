import argparse
import json
import os
import sys
import time
import traceback
import urllib.request
from dataclasses import dataclass

from openai import OpenAI

from .config import _missing_key_message
from .guards import _validate_translation_output
from .naming import (
    _ensure_within_directory,
    _existing_translation_exists,
    _resolve_output_filename,
    _resolve_relative_paths,
    _resolve_single_output_filename,
    _should_skip_walk_dir,
    _validate_input_paths,
    _write_output_file,
    is_excluded,
)
from .news import (
    _cleanup_source_flag,
    _protect_news_quotes,
    _restore_news_quotes,
    _validate_news_placeholders_intact,
    _validate_news_post,
)
from .notes import (
    _assemble_translation_note_paragraphs,
    _build_translation_note_phrase,
    _compose_with_notes,
)
from .placeholders import (
    _extract_heading_slugs,
    _normalize_collapsed_markdown,
    _protect_anchors,
    _protect_code_blocks,
    _protect_inline_code,
    _protect_ref_labels,
    _protect_urls,
    _restore_anchors,
    _restore_code,
    _restore_ref_labels,
    _restore_urls,
    _validate_code_placeholders_present,
    _validate_no_code_placeholder_leftover,
    _validate_segment_placeholders,
)
from .prompts import _build_system_instructions
from .providers.anthropic import _call_claude, _init_claude_client
from .providers.base import (
    _NAMESPACED_MODEL_REGEX,
    _reason_name,
)
from .providers.codex import _call_codex, _init_codex_client
from .providers.gemini import _call_gemini, _init_gemini_client
from .providers.grok import _call_grok_cli, _init_grok_cli_client, _init_grok_client
from .providers.mistral import _call_mistral, _init_mistral_client
from .providers.openai import (
    _build_openai_messages,
    _call_openai,
    _init_openai_client,
)
from .providers.opencode import _call_opencode, _init_opencode_client
from .segmentation import DEFAULT_TOKEN_LIMIT, MODEL_TOKEN_LIMITS, segment_text

DEFAULT_OPENROUTER_API_KEY = "votre-cle-api-openrouter-par-defaut"  # pragma: allowlist secret


# --- Provider OpenRouter (routeur, facturé à l'usage) -----------------------
# Endpoint compatible OpenAI lui aussi ; ce qui change est en amont de
# l'appel, dans le préflight qui épingle les hébergeurs (cf. _openrouter_pin).
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_TIMEOUT = float(os.getenv("OPENROUTER_TIMEOUT", "900"))
OPENROUTER_PREFLIGHT_TIMEOUT = float(os.getenv("OPENROUTER_PREFLIGHT_TIMEOUT", "30"))
# Plancher de sortie exigé d'un hébergeur. 8 000 tokens couvrent largement un
# segment de 16 000 tokens d'entrée traduit ; le seuil sert à écarter les
# hébergeurs à 2 048 qui tronqueraient sans le dire, pas à dimensionner.
OPENROUTER_MIN_COMPLETION_TOKENS = 8000
# Enveloppe demandée. Généreuse à dessein : sur un modèle qui impose le
# raisonnement, celui-ci se sert en premier dans cette enveloppe.
OPENROUTER_MAX_TOKENS = 32768
# Efforts de raisonnement du moins au plus coûteux, tels que le catalogue les
# nomme. L'ordre sert à choisir le PLUS BAS que le modèle accepte quand il
# impose de raisonner : mesuré sur z-ai/glm-5.3-flash, dont le défaut est
# `max`, laisser ce défaut sature les 32 768 tokens de sortie AVANT la fin de
# la traduction — l'effort alloue un pourcentage de l'enveloppe, et augmenter
# l'enveloppe augmente le raisonnement d'autant.
OPENROUTER_EFFORTS_CROISSANTS = ("minimal", "low", "medium", "high", "xhigh", "max")


DEFAULT_SOURCE_LANG = "fr"
DEFAULT_TARGET_LANG = "en"
DEFAULT_SOURCE_DIR = "content/posts"
DEFAULT_TARGET_DIR = "traductions_en"


# --- Provider OpenRouter (routeur multi-fournisseurs, facturé à l'usage) -----
#
# OpenRouter n'est pas un fournisseur, c'est un routeur devant ~430 modèles
# hébergés par des tiers. Deux mesures dictent tout ce qui suit.
#
# 1. Un même slug est servi par des dizaines d'hébergeurs aux plafonds
#    différents. Sur `z-ai/glm-5.3-flash` : 23 hébergeurs, dont un plafonné à
#    2 048 tokens de sortie. Sans épinglage, une traduction longue sur 23
#    partait tronquée, au hasard du routage et sans le moindre signal. D'où le
#    préflight, qui est fail-closed : pas de catalogue, pas de traduction.
# 2. Le raisonnement est facturé au tarif de sortie. Même requête sur
#    `z-ai/glm-5.2`, réponse « OK » : 107 tokens de complétion au défaut du
#    modèle, 2 avec le raisonnement coupé. Un facteur 18 sur chaque segment de
#    chaque fichier, pour une tâche à laquelle le raisonnement n'apporte rien.
def _openrouter_http_get(base_url, path):
    """GET JSON sur l'API OpenRouter. Le catalogue est public : pas de clé ici,
    donc rien à fuiter si l'URL de base est détournée.

    `urllib` plutôt que `httpx` : le préflight tient en deux GET, et déclarer
    une dépendance directe de plus n'aurait acheté que du bruit."""
    base = os.getenv("OPENROUTER_BASE_URL", OPENROUTER_BASE_URL) if base_url is None else base_url
    if not base.startswith("https://"):
        raise ValueError(f"OPENROUTER_BASE_URL doit commencer par https:// (reçu {base!r})")
    url = f"{base.rstrip('/')}/{path.lstrip('/')}"
    # Le marqueur est SUR la ligne de l'appel : bandit ne le lit pas une ligne
    # plus haut, contrairement à semgrep. Le délai est sorti en variable courte
    # pour que ruff-format ne puisse pas scinder la ligne et emporter le
    # marqueur ailleurs — le même piège avait déjà défait un `# nosemgrep`.
    delai = OPENROUTER_PREFLIGHT_TIMEOUT
    try:
        with urllib.request.urlopen(url, timeout=delai) as reponse:  # nosec B310 — https vérifié
            return json.loads(reponse.read().decode("utf-8"))
    except (OSError, ValueError) as e:
        raise ValueError(f"Préflight OpenRouter injoignable ({url}) : {e}") from e


def _openrouter_catalog_entry(base_url, model):
    """Fiche catalogue du modèle demandé.

    Fail-closed : un slug absent du catalogue est une faute de frappe, pas un
    modèle à tenter quand même. Le laisser passer produirait un 400 opaque au
    milieu d'un lot de fichiers, après la première facturation."""
    payload = _openrouter_http_get(base_url, "models")
    for entry in payload.get("data") or []:
        if entry.get("id") == model:
            return entry
    raise ValueError(
        f"Modèle OpenRouter inconnu : {model!r}. Catalogue sur "
        "https://openrouter.ai/models, au format « fournisseur/modèle »."
    )


def _openrouter_endpoints(base_url, model):
    payload = _openrouter_http_get(base_url, f"models/{model}/endpoints")
    return (payload.get("data") or {}).get("endpoints") or []


def _openrouter_pin(endpoints):
    """Hébergeurs retenus, et plafond de sortie commun à ceux-là.

    Deux filtres, tous deux mesurés. Un `status` négatif marque un hébergeur
    que le routeur lui-même déprioritise (3 sur 23 pour glm-5.3-flash). Un
    plafond de sortie sous OPENROUTER_MIN_COMPLETION_TOKENS tronque une
    traduction longue en silence — c'est le défaut que le préflight existe pour
    empêcher. Un plafond non déclaré (`None`) est un inconnu, donc écarté :
    l'objet de cette fonction est justement de ne rien laisser au hasard."""
    usable = [
        e
        for e in endpoints
        if (e.get("status") or 0) >= 0
        and (e.get("max_completion_tokens") or 0) >= OPENROUTER_MIN_COMPLETION_TOKENS
    ]
    tags = tuple(e["tag"] for e in usable if e.get("tag"))
    ceiling = min((e["max_completion_tokens"] for e in usable), default=0)
    return tags, ceiling


@dataclass
class _OpenRouterClient:
    """Client OpenRouter : le client OpenAI, plus ce que le préflight a mesuré.

    Ces trois champs ne sont pas des préférences, ce sont des contraintes lues
    sur le catalogue au démarrage — la liste d'hébergeurs dont aucun ne
    tronque, le plafond de sortie qu'ils tiennent tous, et le fait que le
    modèle impose ou non de raisonner."""

    client: object
    providers: tuple = ()
    max_tokens: int = OPENROUTER_MAX_TOKENS
    reasoning_mandatory: bool = False
    supported_efforts: tuple = ()


def _openrouter_reasoning(client, args):
    """Bloc `reasoning` de la requête, ou `None` pour n'en envoyer aucun.

    Par défaut le raisonnement est COUPÉ quand le modèle le permet : mesuré sur
    z-ai/glm-5.2, la même réponse coûte 2 tokens de complétion au lieu de 107.
    Quand le modèle l'impose, on n'envoie rien plutôt que de deviner un effort —
    l'effort alloue un pourcentage de `max_tokens` et le raisonnement se sert en
    premier, si bien qu'une valeur choisie au hasard déplace le risque de page
    blanche au lieu de le réduire."""
    effort = getattr(args, "reasoning_effort", None)
    if effort not in (None, "none"):
        return {"effort": effort}
    if not client.reasoning_mandatory:
        return {"enabled": False}
    plus_bas = _openrouter_lowest_effort(client.supported_efforts)
    return {"effort": plus_bas} if plus_bas else None


def _openrouter_lowest_effort(supported):
    """Le plus bas effort que le modèle déclare accepter, ou `None`.

    Mesuré : laisser son défaut à un modèle qui impose le raisonnement — `max`
    pour z-ai/glm-5.3-flash — fait dépasser l'enveloppe de sortie AVANT la fin
    de la traduction, et l'erreur est alors une troncature, pas une page
    blanche. Augmenter `max_tokens` n'y changerait rien : l'effort alloue un
    pourcentage de cette enveloppe, le raisonnement grandit avec elle."""
    connus = [e for e in OPENROUTER_EFFORTS_CROISSANTS if e in (supported or ())]
    return connus[0] if connus else None


def _openrouter_reasoning_label(client, args):
    """Décrit le raisonnement tel qu'il sera ENVOYÉ. Le dériver de
    `mandatory` seul annonçait « coupé » alors qu'un `--reasoning_effort`
    explicite partait dans la requête."""
    reasoning = _openrouter_reasoning(client, args)
    if reasoning is None:
        return "imposé par le modèle, à son réglage par défaut"
    if reasoning.get("enabled") is False:
        return "coupé"
    # Un effort non demandé par l'utilisateur a été choisi ici : le dire, sinon
    # le message laisse croire qu'il vient de la ligne de commande.
    demande = getattr(args, "reasoning_effort", None)
    origine = (
        "" if demande and demande != "none" else " (imposé par le modèle, le plus bas accepté)"
    )
    return f"effort {reasoning['effort']!r}{origine}"


def _openrouter_extra_body(client, args):
    """`allow_fallbacks: false` est indispensable : sans lui, `only` n'est
    qu'une préférence et le routeur repart vers un hébergeur écarté, ce qui vide
    le préflight de son sens."""
    body = {"provider": {"only": list(client.providers), "allow_fallbacks": False}}
    reasoning = _openrouter_reasoning(client, args)
    if reasoning is not None:
        body["reasoning"] = reasoning
    return body


def _openrouter_first_choice(response, args):
    """Premier choix de la réponse, ou une erreur qui nomme la vraie cause.

    OpenRouter répond 200 avec un corps qui ne porte qu'une erreur quand
    l'hébergeur amont échoue. Sans cette garde, `choices[0]` levait un
    TypeError opaque qui masquait le message du routeur."""
    error = getattr(response, "error", None) or (
        response.get("error") if isinstance(response, dict) else None
    )
    if error:
        raise RuntimeError(f"OpenRouter a répondu une erreur (model={args.model}) : {error}")
    choices = getattr(response, "choices", None)
    if not choices:
        raise RuntimeError(
            f"OpenRouter n'a renvoyé aucun choix (model={args.model}) — "
            "réponse sans contenu ni erreur exploitable"
        )
    return choices[0]


def _openrouter_check_finish(choice, client, args, content):
    """Contrat de sortie : distingue la page blanche de la vraie troncature.

    `finish_reason=length` avec un texte vide n'est pas une traduction trop
    longue, c'est le budget de sortie consommé par le raisonnement avant le
    premier caractère utile — mesuré à 15 850 tokens de raisonnement pour 148
    utiles. Les deux cas demandent des gestes opposés, les confondre envoie
    l'utilisateur réduire une taille de segment qui n'est pas en cause."""
    finish = _reason_name(choice.finish_reason)
    native = _reason_name(getattr(choice, "native_finish_reason", None))
    if finish == "length":
        if not content:
            raise RuntimeError(
                f"OpenRouter : budget de sortie ({client.max_tokens} tokens) consommé par le "
                f"raisonnement avant tout texte (model={args.model}). Relancer à l'identique "
                "ne changera rien : couper le raisonnement, ou choisir un modèle qui ne l'impose pas."
            )
        raise RuntimeError(
            f"OpenRouter : sortie tronquée à {client.max_tokens} tokens "
            f"(model={args.model}, finish_reason=length)"
        )
    # `error` est la valeur que le routeur NORMALISE quand l'hébergeur amont
    # échoue en cours de génération. Mesuré sur z-ai/glm-5.3-flash : deux
    # segments coupés à 750 s exactement, `native_finish_reason` à None. Le dire
    # évite de chercher un défaut dans le document ou dans le découpage.
    if finish == "error":
        raise RuntimeError(
            f"OpenRouter : l'hébergeur a interrompu la génération (model={args.model}, "
            f"finish_reason=error, natif={native!r}). Panne côté fournisseur, pas côté "
            "document : réessayer, ou restreindre les hébergeurs retenus."
        )
    # `end_turn` est la forme émise par certains hébergeurs là où OpenAI émet
    # `stop` ; `native_finish_reason` porte la valeur non normalisée de l'amont.
    if finish not in ("stop", "STOP", "end_turn", None):
        raise RuntimeError(
            f"OpenRouter finish_reason anormal={finish!r} (natif={native!r}, model={args.model})"
        )


def _call_openrouter(client, args, prompt, segment):
    messages = _build_openai_messages(args, prompt, segment)
    response = client.client.chat.completions.create(
        model=args.model,
        messages=messages,
        max_tokens=client.max_tokens,
        extra_body=_openrouter_extra_body(client, args),
    )
    choice = _openrouter_first_choice(response, args)
    content = (getattr(choice.message, "content", None) or "").strip()
    _openrouter_check_finish(choice, client, args, content)
    if not content:
        raise RuntimeError(
            f"OpenRouter returned empty content (model={args.model}, "
            f"finish_reason={_reason_name(choice.finish_reason)!r})"
        )
    return content


def _resolve_provider(args, use_mistral=False, use_claude=False, use_gemini=False):
    """Nom du provider à utiliser. Les booléens explicites priment (plusieurs
    tests appellent `translate(..., use_mistral=True)` avec un Namespace qui
    n'a aucun attribut `use_*`), `args` ne sert que de repli."""
    if use_mistral:
        return "mistral"
    if use_claude:
        return "claude"
    if use_gemini:
        return "gemini"
    if getattr(args, "use_codex", False):
        return "codex"
    if getattr(args, "use_grok_cli", False):
        return "grok_cli"
    if getattr(args, "use_grok", False):
        return "grok"
    if getattr(args, "use_opencode", False):
        return "opencode"
    if getattr(args, "use_openrouter", False):
        return "openrouter"
    return "openai"


# `provider` sert de clé de dispatch, pas de libellé : `.capitalize()` affichait
# « Grok_cli » et « Openai » à l'utilisateur.
_PROVIDER_LABELS = {
    "openai": "OpenAI",
    "mistral": "Mistral",
    "claude": "Claude",
    "gemini": "Gemini",
    "codex": "Codex CLI",
    "grok": "Grok (API xAI)",
    "grok_cli": "Grok CLI",
    "opencode": "OpenCode",
    "openrouter": "OpenRouter",
}


def _dispatch_provider_call(client, args, prompt, segment, provider, is_translation_note):
    if provider == "mistral":
        text = _call_mistral(client, args, prompt, segment)
    elif provider == "claude":
        text = _call_claude(client, args, prompt, segment)
    elif provider == "gemini":
        text = _call_gemini(client, args, prompt, segment)
    elif provider == "codex":
        text = _call_codex(client, args, prompt, segment)
    elif provider == "grok_cli":
        text = _call_grok_cli(client, args, prompt, segment)
    elif provider == "opencode":
        text = _call_opencode(client, args, prompt, segment)
    elif provider == "openrouter":
        text = _call_openrouter(client, args, prompt, segment)
    else:
        # `grok` (API xAI) inclus : endpoint compatible OpenAI, donc même appel.
        text = _call_openai(client, args, prompt, segment, is_translation_note)
    # Empty-content guard : un provider qui retourne "" avec finish_reason="stop"
    # produirait sinon un fichier vide marqué success.
    if not text.strip():
        raise RuntimeError(
            f"{_PROVIDER_LABELS[provider]} returned empty content (model={args.model})"
        )
    return text


@dataclass
class _LLMCallSpec:
    """Regroupe les paramètres d'un appel LLM (provider + flags) pour réduire
    la signature de `_translate_segment_with_retry` et `_dispatch_provider_call`."""

    client: object
    args: object
    system_instructions: str
    provider: str = "openai"
    is_translation_note: bool = False


def _translate_segment_with_retry(segment, idx, total, spec, max_retries=1):
    """Appelle le LLM puis valide placeholders + langue/passthrough. En cas de
    fail récupérable (non-déterminisme LLM), retry 1 fois max. Les fails non-
    récupérables (finish_reason anormal, sortie vide) ne sont pas retryés —
    ils indiquent un problème API, pas un problème de qualité de traduction."""
    last_exc = None
    for attempt in range(max_retries + 1):
        translated_text = _dispatch_provider_call(
            spec.client,
            spec.args,
            spec.system_instructions,
            segment,
            spec.provider,
            spec.is_translation_note,
        )
        try:
            _validate_segment_placeholders(segment, translated_text)
            _validate_translation_output(
                segment, translated_text, spec.args, spec.is_translation_note
            )
            if attempt > 0:
                print(
                    f"✓ Segment {idx}/{total} validated on retry {attempt}/{max_retries}",
                    file=sys.stderr,
                )
            return translated_text
        except RuntimeError as e:
            last_exc = e
            if attempt >= max_retries:
                raise
            print(
                f"⚠ Segment {idx}/{total} validation failed "
                f"(attempt {attempt + 1}/{max_retries + 1}): {e}. Retrying...",
                file=sys.stderr,
            )
    raise last_exc  # unreachable, garde de sécurité


def translate(
    text,
    client,
    args,
    use_mistral=False,
    use_claude=False,
    use_gemini=False,
    is_translation_note=False,
):
    """Segmente puis traduit le texte, et lève RuntimeError si une garde de
    silent-failure se déclenche (finish_reason anormal, sortie vide, extrait
    source verbatim, ratio source/output trop faible, langue source détectée).
    """
    model_limit = MODEL_TOKEN_LIMITS.get(args.model, DEFAULT_TOKEN_LIMIT)
    segments = segment_text(text, min(16000, model_limit))
    system_instructions = _build_system_instructions(args, is_translation_note)

    spec = _LLMCallSpec(
        client=client,
        args=args,
        system_instructions=system_instructions,
        provider=_resolve_provider(args, use_mistral, use_claude, use_gemini),
        is_translation_note=is_translation_note,
    )
    translated_segments = []
    for idx, segment in enumerate(segments, start=1):
        try:
            translated_text = _translate_segment_with_retry(segment, idx, len(segments), spec)
        except Exception as e:
            # On préserve le type d'origine dans le message ET la chaîne via `from e`
            # (le traceback complet reste accessible par traceback.print_exc en haut).
            raise RuntimeError(
                f"Erreur lors de la traduction (segment {idx}/{len(segments)}, "
                f"{type(e).__name__}): {e}"
            ) from e
        translated_segments.append(translated_text)

    # Jonction par "\n" : les segments coupés sur "\n\n" / "\n## " préservent
    # leur newline structurant, et les coupures sur ". " ou hard-cut (max_length)
    # ne sont pas garanties de finir/commencer par "\n" — un "\n" explicite ici
    # évite de coller deux paragraphes ou de fusionner un heading avec sa prose.
    return "\n".join(translated_segments)


def _append_translation_note(translated_content, client, args, use_mistral, use_claude, use_gemini):
    # On ne soumet au LLM QUE la phrase descriptive : titre du repo et lien
    # GitHub sont assemblés côté Python pour garantir l'invariance du slug
    # `ai-powered-markdown-translator` et de l'URL (que la fonction
    # `translate()` n'aurait protégés ni via `_protect_inline_code`, ni via
    # `_protect_code_blocks` — ces protections vivent dans `_translate_pipeline`).
    fmt = getattr(args, "note_format", "legacy")
    phrase_source = _build_translation_note_phrase(args)
    translated_phrase = translate(
        phrase_source, client, args, use_mistral, use_claude, use_gemini, True
    ).strip()
    if fmt == "marker":
        translation_note = _assemble_translation_note_paragraphs(
            translated_phrase, args.target_lang
        )
    else:
        translation_note = translated_phrase
    return _compose_with_notes(translated_content, args, translation_note, fmt)


@dataclass
class _PipelineState:
    """Artefacts collectés lors de la phase `protect` du pipeline, conservés
    pour la phase `restore` post-LLM."""

    code_blocks: list
    block_placeholders: list
    inline_codes: list
    inline_placeholders: list
    original_quotes: list
    attribution_urls: list
    source_heading_slugs: list
    anchors: list
    anchor_placeholders: list
    anchor_metadata: list
    ref_labels: list
    ref_label_placeholders: list
    urls: list
    url_placeholders: list


def _protect_pipeline_inputs(content, args):
    """Phase `protect` du pipeline : extrait dans l'ordre code/news/anchors/
    ref-labels/urls. L'ordre est critique (cf. commentaires inline) — toute
    inversion casse soit la capture des `attribution_urls` news, soit le
    matching des regex de placeholder qui peuvent se confondre."""
    content, code_blocks, block_placeholders = _protect_code_blocks(content)
    content, inline_codes, inline_placeholders = _protect_inline_code(content)
    # News quotes AVANT URLs : capture les `attribution_urls` réelles avant
    # qu'elles ne soient remplacées par `#URL{n}#`.
    content, original_quotes, attribution_urls = _protect_news_quotes(content, args)
    # Capture les slugs des headings source pour resync TOC post-LLM.
    source_heading_slugs = _extract_heading_slugs(content)
    # Anchors AVANT urls : éviter que `\(#[^)\s]+\)` matche `(#URL\d+#)`.
    content, anchors, anchor_placeholders, anchor_metadata = _protect_anchors(content)
    # Reference-style labels avant URLs : la def `[label]: URL` doit garder
    # sa structure `[#REFLABEL{n}#]: #URL{n}#`.
    content, ref_labels, ref_label_placeholders = _protect_ref_labels(content)
    content, urls, url_placeholders = _protect_urls(content)

    state = _PipelineState(
        code_blocks=code_blocks,
        block_placeholders=block_placeholders,
        inline_codes=inline_codes,
        inline_placeholders=inline_placeholders,
        original_quotes=original_quotes,
        attribution_urls=attribution_urls,
        source_heading_slugs=source_heading_slugs,
        anchors=anchors,
        anchor_placeholders=anchor_placeholders,
        anchor_metadata=anchor_metadata,
        ref_labels=ref_labels,
        ref_label_placeholders=ref_label_placeholders,
        urls=urls,
        url_placeholders=url_placeholders,
    )
    return content, state


def _restore_pipeline_outputs(translated_content, state, args):
    """Phase `restore` du pipeline : valide placeholders → restore en ordre
    inverse (urls → ref_labels → anchors → code) → news/cleanup → validate."""
    _validate_code_placeholders_present(
        translated_content,
        state.block_placeholders,
        state.inline_placeholders,
        state.url_placeholders,
        state.anchor_placeholders,
        state.ref_label_placeholders,
    )
    target_heading_slugs = _extract_heading_slugs(translated_content)
    translated_content = _restore_urls(translated_content, state.urls, state.url_placeholders)
    translated_content = _restore_ref_labels(
        translated_content, state.ref_labels, state.ref_label_placeholders
    )
    translated_content = _restore_anchors(
        translated_content,
        state.anchors,
        state.anchor_placeholders,
        state.anchor_metadata,
        state.source_heading_slugs,
        target_heading_slugs,
    )
    translated_content = _restore_code(
        translated_content,
        state.inline_codes,
        state.inline_placeholders,
        state.code_blocks,
        state.block_placeholders,
    )
    _validate_no_code_placeholder_leftover(translated_content)

    if args.news and state.original_quotes:
        _validate_news_placeholders_intact(translated_content, len(state.original_quotes))
    translated_content = _restore_news_quotes(translated_content, state.original_quotes)
    translated_content = _normalize_collapsed_markdown(translated_content)
    translated_content = _cleanup_source_flag(translated_content, args)

    if args.news and state.original_quotes:
        _validate_news_post(translated_content, state.original_quotes, state.attribution_urls, args)
    return translated_content


@dataclass
class _TranslationConfig:
    """Regroupe les paramètres de traduction (client + flags providers + flags
    fonctionnels) pour réduire les signatures publiques `translate_markdown_file`,
    `translate_directory` et helpers internes (passaient 7-9 params positionnels)."""

    client: object
    args: object
    use_mistral: bool = False
    use_claude: bool = False
    use_gemini: bool = False
    add_translation_note: bool = False
    force: bool = False


def _translate_pipeline(content, config):
    """Pipeline complet : protect → translate → restore → validate."""
    content, state = _protect_pipeline_inputs(content, config.args)
    translated_content = translate(
        content,
        config.client,
        config.args,
        config.use_mistral,
        config.use_claude,
        config.use_gemini,
    )
    return _restore_pipeline_outputs(translated_content, state, config.args)


def _read_translatable_source(file_path, relative_file_path):
    """Lit le fichier source. Retourne (content, status) où status est `None`
    si OK, `"skipped"` si vide (le caller propage).

    Aucune garde de périmètre ici, contrairement aux chemins d'ÉCRITURE : ce
    chemin est soit `--file`, que l'utilisateur nomme explicitement et dont la
    lecture est la raison d'être du programme, soit une entrée produite par
    `os.walk` sous `--source_dir`. Il n'existe pas de racine dont il faudrait
    l'empêcher de sortir — la limite est celle des droits du processus.
    """
    # NOSONAR pythonsecurity:S8707 — lecture d'un chemin nommé par l'utilisateur,
    # sans périmètre à faire respecter (cf. docstring). Les chemins d'écriture,
    # eux, sont bornés par _ensure_within_directory.
    with open(file_path, encoding="utf-8") as f:  # NOSONAR pythonsecurity:S8707
        content = f.read()
    if not content:
        print(f"Le fichier '{relative_file_path}' est vide, aucune traduction n'est effectuée.")
        return content, "skipped"
    return content, None


def _translate_one_file(file_path, output_path, config):
    """Cœur de `translate_markdown_file` sans la gestion d'erreurs externes.
    Lève toute exception au caller, qui la convertit en status `"failure"`."""
    relative_file_path, relative_output_path = _resolve_relative_paths(
        file_path, output_path, config.args
    )
    print(f"Traitement du fichier : {relative_file_path}")
    start_time = time.time()

    content, status = _read_translatable_source(file_path, relative_file_path)
    if status is not None:
        return status

    translated_content = _translate_pipeline(content, config)
    if config.add_translation_note:
        translated_content = _append_translation_note(
            translated_content,
            config.client,
            config.args,
            config.use_mistral,
            config.use_claude,
            config.use_gemini,
        )

    status = _write_output_file(output_path, translated_content, config.force, relative_output_path)
    if status == "success":
        print(
            f"Fichier '{relative_file_path}' traduit en {time.time() - start_time:.2f} secondes "
            f"et enregistré sous : {relative_output_path}"
        )
    return status


def translate_markdown_file(file_path, output_path, config):
    """Retourne "success" / "skipped" (vide ou déjà traduit) / "failure"
    (toute exception est attrapée et propagée par status, sans écrire le fichier)."""
    relative_file_path = file_path
    try:
        return _translate_one_file(file_path, output_path, config)
    except OSError as e:
        print(f"Erreur lors du traitement du fichier '{relative_file_path}': {e}", file=sys.stderr)
        traceback.print_exc()
        return "failure"
    except Exception as e:
        print(
            f"Une erreur inattendue est survenue lors de la traduction du fichier "
            f"'{relative_file_path}' ({type(e).__name__}): {e}\n"
            "Veuillez relancer le traitement pour ce fichier.",
            file=sys.stderr,
        )
        traceback.print_exc()
        return "failure"


def _record_translation_status(status, file, file_path, failed_files, skipped_files):
    if status == "success":
        print(f"Fichier '{file}' traité.")
    elif status == "skipped":
        skipped_files.append(file_path)
    elif status == "failure":
        failed_files.append(file_path)
    else:
        # Default-fail sur statut inattendu (régression future).
        print(
            f"WARNING: Statut inattendu pour '{file}': {status!r} -> traité comme échec",
            file=sys.stderr,
        )
        failed_files.append(file_path)


@dataclass
class _DirectoryWalkContext:
    """Contexte d'un walk récursif `translate_directory` : config + chemins
    racines + accumulateurs. Réduit la signature de `_process_one_markdown_file`
    à 3 params (file, root, ctx)."""

    input_dir: str
    output_dir: str
    config: _TranslationConfig
    failed_files: list
    skipped_files: list


def _process_one_markdown_file(file, root, ctx):
    file_path = os.path.join(root, file)
    base, _ext = os.path.splitext(file)
    output_file = _resolve_output_filename(file, base, ctx.config.args)
    relative_path = os.path.relpath(root, ctx.input_dir)
    # Avant le makedirs, et non après : celui-ci s'exécute avant le premier
    # appel au modèle, donc une arborescence hors périmètre serait créée même
    # si la traduction échouait ensuite.
    output_path = _ensure_within_directory(
        ctx.output_dir, os.path.join(ctx.output_dir, relative_path, output_file)
    )
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    already_exists = _existing_translation_exists(
        output_path, ctx.output_dir, base, ctx.config.args
    )
    if already_exists and not ctx.config.force:
        print(f"La traduction de '{file}' existe déjà, aucune action effectuée.")
        ctx.skipped_files.append(file_path)
        return

    status = translate_markdown_file(file_path, output_path, ctx.config)
    _record_translation_status(status, file, file_path, ctx.failed_files, ctx.skipped_files)


def _is_translatable_markdown(file):
    return (file.endswith(".md") or file.endswith(".mdx")) and not is_excluded(file)


def translate_directory(input_dir, output_dir, config):
    """Walk récursif. Retourne {"failed": [...], "skipped": [...]} avec les
    chemins absolus des fichiers ; le caller agrège pour décider de exit(1)."""
    input_dir = os.path.abspath(input_dir)
    output_dir = os.path.abspath(output_dir)
    if not os.path.exists(output_dir):
        # NOSONAR pythonsecurity:S8707 — création de la RACINE que l'utilisateur
        # a nommée (--target_dir), pas d'un chemin calculé. Il n'existe pas de
        # périmètre dont l'empêcher de sortir ; ce qui est écrit DEDANS, si.
        os.makedirs(output_dir)  # NOSONAR
    output_base_dir = os.path.basename(output_dir)

    ctx = _DirectoryWalkContext(
        input_dir=input_dir,
        output_dir=output_dir,
        config=config,
        failed_files=[],
        skipped_files=[],
    )

    for root, _dirs, files in os.walk(input_dir, topdown=True):
        if _should_skip_walk_dir(root, output_dir, output_base_dir, input_dir):
            continue
        for file in files:
            if not _is_translatable_markdown(file):
                continue
            _process_one_markdown_file(file, root, ctx)

    return {"failed": ctx.failed_files, "skipped": ctx.skipped_files}


def _add_io_args(parser):
    parser.add_argument(
        "--force",
        action="store_true",
        help="Forcer la traduction même si une traduction existe déjà",
    )
    parser.add_argument(
        "--file",
        type=str,
        help="Fichier Markdown unique à traduire (alternative à --source_dir)",
    )
    parser.add_argument(
        "--source_dir",
        type=str,
        default=DEFAULT_SOURCE_DIR,
        help="Répertoire source contenant les fichiers Markdown",
    )
    parser.add_argument(
        "--target_dir",
        type=str,
        default=DEFAULT_TARGET_DIR,
        help="Répertoire cible pour sauvegarder les traductions",
    )


def _add_lang_args(parser):
    parser.add_argument(
        "--target_lang",
        type=str,
        default=DEFAULT_TARGET_LANG,
        help="Langue cible pour la traduction",
    )
    parser.add_argument(
        "--source_lang",
        type=str,
        default=DEFAULT_SOURCE_LANG,
        help="Langue source pour la traduction",
    )


def _add_provider_args(parser):
    parser.add_argument(
        "--model",
        type=str,
        help=(
            "Modèle à utiliser pour la traduction ; la valeur par défaut dépend du "
            "provider sélectionné. Obligatoire avec --use_opencode et "
            "--use_openrouter, au format provider/modèle (liste : "
            "`opencode models`, https://openrouter.ai/models)"
        ),
    )
    # Groupe exclusif : deux flags provider simultanés étaient acceptés en
    # silence, et la précédence divergeait entre _select_provider_client (qui
    # teste Mistral en premier) et _resolve_provider (qui donne priorité aux
    # booléens explicites). `--use_codex --use_mistral` instanciait donc un
    # client Mistral ET dispatchait vers Mistral : la traduction partait en
    # facturation à l'usage alors que l'utilisateur avait demandé son quota
    # d'abonnement — exactement ce que --use_codex existe pour empêcher, et
    # sans le moindre avertissement. argparse refuse désormais la combinaison.
    provider_group = parser.add_mutually_exclusive_group()
    provider_group.add_argument(
        "--use_mistral", action="store_true", help="Utiliser l'API Mistral AI pour la traduction"
    )
    provider_group.add_argument(
        "--use_claude",
        action="store_true",
        help="Utiliser l'API Claude d'Anthropic pour la traduction",
    )
    provider_group.add_argument(
        "--use_gemini",
        action="store_true",
        help="Utiliser l'API Gemini de Google pour la traduction",
    )
    provider_group.add_argument(
        "--use_grok",
        action="store_true",
        help="Utiliser l'API xAI (Grok) — nécessite XAI_API_KEY, facturé à l'usage",
    )
    provider_group.add_argument(
        "--use_grok_cli",
        action="store_true",
        help=(
            "Utiliser le CLI Grok sur le quota de l'abonnement Grok "
            "(nécessite `grok login` ; confinement plus faible que --use_codex)"
        ),
    )
    provider_group.add_argument(
        "--use_codex",
        action="store_true",
        help=(
            "Utiliser le CLI Codex sur le quota de l'abonnement ChatGPT "
            "(aucune facturation à l'usage ; nécessite `codex login`)"
        ),
    )
    provider_group.add_argument(
        "--use_opencode",
        action="store_true",
        help=(
            "Utiliser OpenCode (agent open source) vers le fournisseur configuré "
            "dans OpenCode — modèle local, gratuit, abonnement ou clé ; exige "
            "--model provider/modèle"
        ),
    )
    provider_group.add_argument(
        "--use_openrouter",
        action="store_true",
        help=(
            "Utiliser OpenRouter (routeur vers ~430 modèles) — nécessite "
            "OPENROUTER_API_KEY, facturé à l'usage ; exige --model fournisseur/modèle"
        ),
    )
    parser.add_argument(
        "--eco",
        action="store_true",
        help="Utiliser les modèles économiques (mini/flash) au lieu des modèles qualité",
    )
    parser.add_argument(
        "--reasoning_effort",
        choices=("none", "low", "medium", "high", "xhigh"),
        default=None,
        help=(
            "Effort de raisonnement OpenAI GPT-5.x. Par défaut : 'none' avec "
            "--eco (le raisonnement n'apporte rien à une traduction et double "
            "les tokens de sortie), 'medium' sinon. Toutes les valeurs ne sont "
            "pas acceptées par tous les modèles ; un refus déclenche un retry "
            "sans le paramètre."
        ),
    )


def _add_output_naming_args(parser):
    parser.add_argument(
        "--include_model",
        action="store_true",
        help="Inclure le nom du modèle dans le fichier de sortie (ex: README-en-gpt-5.md)",
    )
    parser.add_argument(
        "--keep_filename",
        action="store_true",
        help="Conserver le nom et l'extension du fichier original (pour Astro, Hugo, etc.)",
    )


def _add_note_args(parser):
    parser.add_argument(
        "--add_translation_note",
        action="store_true",
        help="Ajouter une note de traduction au contenu traduit",
    )
    parser.add_argument(
        "--note_position",
        choices=["top", "bottom", "both"],
        default="bottom",
        help="Position de la note de traduction (défaut: bottom). Requiert --add_translation_note.",
    )
    parser.add_argument(
        "--note_format",
        choices=["legacy", "marker"],
        default="legacy",
        help=(
            "Format de la note de traduction (défaut: legacy = paragraphe gras compatible v1.9). "
            "'marker' produit une link reference definition + blockquote (consommable par un plugin "
            "Markdown comme remark-translation-banner)."
        ),
    )


def _add_news_args(parser):
    parser.add_argument(
        "--news",
        action="store_true",
        help="Active les règles de traduction des citations news (drapeaux + quotes EN protégées)",
    )


def _build_arg_parser():
    parser = argparse.ArgumentParser(prog="aipmt", description="Traduit les fichiers Markdown.")
    _add_io_args(parser)
    _add_lang_args(parser)
    _add_provider_args(parser)
    _add_output_naming_args(parser)
    _add_note_args(parser)
    _add_news_args(parser)
    return parser


def _openrouter_validate_model(model):
    """Valide la FORME du slug avant tout appel réseau.

    Ce slug est interpolé dans l'URL de préflight : la validation n'est pas une
    politesse d'ergonomie mais la garde qui empêche d'y injecter un chemin. La
    regex commune aux deux providers namespacés accepte `a/b/..`, d'où le refus
    explicite du segment parent."""
    if not model:
        raise ValueError(
            "--use_openrouter exige --model au format fournisseur/modèle. OpenRouter "
            "n'est pas un fournisseur mais un routeur vers ~430 modèles tiers, et "
            "aucun défaut n'est choisi à votre place — le choix engage le prix, la "
            "licence et le traitement de vos données.\n"
            "  Catalogue : https://openrouter.ai/models\n"
            "  Exemples : --model z-ai/glm-5.2, --model qwen/qwen3.8-flash"
        )
    if not _NAMESPACED_MODEL_REGEX.match(model) or ".." in model.split("/"):
        raise ValueError(
            f"Modèle OpenRouter invalide : {model!r}. Attendu fournisseur/modèle, "
            "ex. z-ai/glm-5.2 (catalogue : https://openrouter.ai/models)."
        )


def _init_openrouter_client(args):
    """Provider OpenRouter. L'appel est compatible OpenAI ; ce qui distingue ce
    provider tient dans le préflight, dont le résultat est affiché parce qu'il
    engage la dépense et la fidélité de la sortie."""
    _openrouter_validate_model(args.model)
    api_key = os.getenv("OPENROUTER_API_KEY", DEFAULT_OPENROUTER_API_KEY)
    if not api_key or api_key == DEFAULT_OPENROUTER_API_KEY:
        raise ValueError(
            _missing_key_message(
                "OpenRouter",
                ["OPENROUTER_API_KEY"],
                hint=" Clé à obtenir sur openrouter.ai/keys.",
            )
        )
    if args.eco:
        print(
            "⚠ --eco est sans effet avec --use_openrouter : le modèle est celui de --model.",
            file=sys.stderr,
        )
    base_url = os.getenv("OPENROUTER_BASE_URL", OPENROUTER_BASE_URL)
    entry = _openrouter_catalog_entry(base_url, args.model)
    endpoints = _openrouter_endpoints(base_url, args.model)
    providers, ceiling = _openrouter_pin(endpoints)
    if not providers:
        raise ValueError(
            f"Aucun hébergeur utilisable pour {args.model!r} : {len(endpoints)} évalué(s), "
            f"aucun ne déclare au moins {OPENROUTER_MIN_COMPLETION_TOKENS} tokens de sortie "
            "avec un statut sain. Traduire ici reviendrait à accepter une troncature "
            "silencieuse — choisir un autre modèle."
        )
    # Le catalogue connaît la vraie fenêtre : la renseigner évite que la
    # segmentation retombe sur DEFAULT_TOKEN_LIMIT, faux pour 44 des 431
    # modèles — dont deux plafonnés à 4 095 tokens.
    context_length = int(entry.get("context_length") or DEFAULT_TOKEN_LIMIT)
    MODEL_TOKEN_LIMITS[args.model] = context_length
    reasoning = entry.get("reasoning") or {}
    mandatory = bool(reasoning.get("mandatory"))
    client = _OpenRouterClient(
        client=OpenAI(api_key=api_key, base_url=base_url, timeout=OPENROUTER_TIMEOUT),
        providers=providers,
        max_tokens=min(OPENROUTER_MAX_TOKENS, ceiling),
        reasoning_mandatory=mandatory,
        supported_efforts=tuple(reasoning.get("supported_efforts") or ()),
    )
    if mandatory and getattr(args, "reasoning_effort", None) == "none":
        print(
            f"⚠ --reasoning_effort=none ignoré : {args.model} impose le raisonnement "
            "(reasoning.mandatory sur le catalogue OpenRouter)",
            file=sys.stderr,
        )
    print(
        f"→ OpenRouter : {len(providers)} hébergeur(s) épinglé(s) sur {len(endpoints)}, "
        f"contexte {context_length} tokens, sortie plafonnée à {client.max_tokens}, "
        f"raisonnement {_openrouter_reasoning_label(client, args)}"
    )
    return client


def _select_provider_client(args):
    if args.use_mistral:
        return _init_mistral_client(args)
    if args.use_claude:
        return _init_claude_client(args)
    if args.use_gemini:
        return _init_gemini_client(args)
    if getattr(args, "use_codex", False):
        return _init_codex_client(args)
    if getattr(args, "use_grok_cli", False):
        return _init_grok_cli_client(args)
    if getattr(args, "use_grok", False):
        return _init_grok_client(args)
    if getattr(args, "use_opencode", False):
        return _init_opencode_client(args)
    if getattr(args, "use_openrouter", False):
        return _init_openrouter_client(args)
    return _init_openai_client(args)


def _build_translation_config(args, client):
    return _TranslationConfig(
        client=client,
        args=args,
        use_mistral=args.use_mistral,
        use_claude=args.use_claude,
        use_gemini=args.use_gemini,
        add_translation_note=args.add_translation_note,
        force=args.force,
    )


def _run_single_file(args, client):
    output_file = _resolve_single_output_filename(args)
    output_path = _ensure_within_directory(
        args.target_dir, os.path.join(args.target_dir, output_file)
    )
    config = _build_translation_config(args, client)
    status = translate_markdown_file(args.file, output_path, config)
    # default-fail: tout statut hors {"success", "skipped"} compte comme échec
    return [] if status in ("success", "skipped") else [args.file]


def _run_directory(args, client):
    config = _build_translation_config(args, client)
    result = translate_directory(args.source_dir, args.target_dir, config)
    # default-fail jusqu'au bout : dict mal formé → traiter comme échec.
    return result.get("failed", ["<unexpected translate_directory result>"])


def main():
    """Entrée CLI : exit(1) si au moins un fichier a échoué, exit(0) sinon."""
    args = _build_arg_parser().parse_args()
    # `ValueError` EXCLUSIVEMENT, et seulement sur la phase de CONFIGURATION.
    # Une clé absente ou un chemin invalide sont des erreurs d'utilisation :
    # elles méritent un message, pas une trace d'appel pointant vers
    # site-packages, où l'utilisateur n'a rien à faire.
    #
    # Le périmètre est étroit à dessein. Envelopper toute l'exécution
    # transformerait un vrai bug survenu pendant la traduction en message
    # rassurant — précisément le mode de défaillance que ce dépôt traque. Tout
    # ce qui n'est pas une ValueError de configuration garde sa trace complète.
    try:
        _validate_input_paths(args)
        client = _select_provider_client(args)
    except ValueError as err:
        print(f"✗ {err}", file=sys.stderr)
        sys.exit(2)

    # Avec OpenCode le modèle est `provider/modèle`, jamais catalogué ici : le
    # rappel serait systématique, donc ignoré, donc un masque.
    if args.model not in MODEL_TOKEN_LIMITS and not getattr(args, "use_opencode", False):
        print(
            f"⚠ Modèle '{args.model}' non listé, utilisation de la limite par défaut ({DEFAULT_TOKEN_LIMIT} tokens)"
        )

    failed_files = _run_single_file(args, client) if args.file else _run_directory(args, client)

    if failed_files:
        print(
            f"ERROR: {len(failed_files)} file(s) failed: {failed_files}",
            file=sys.stderr,
        )
        sys.exit(1)

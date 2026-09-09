"""Le pipeline de traduction : d'un texte segmenté à un fichier écrit.

`translate` segmente, construit les instructions, dispatche vers le provider
et valide chaque segment (placeholders, langue, passthrough) avec un second
essai sur échec récupérable. `translate_markdown_file` enchaîne protection
des fragments, traduction, restauration, validations du mode news, note de
traduction et écriture au chemin reçu — borné par `_ensure_within_directory`
chez ses appelants, `cli` et `translate_directory` ; `translate_directory`
parcourt une arborescence en respectant `EXCLUDE_PATTERNS`. Toute garde lève :
rien n'est rattrapé en silence, un fichier en échec est rapporté comme tel.
"""

import os
import sys
import time
import traceback
from dataclasses import dataclass

from .guards import _validate_translation_output
from .naming import (
    _ensure_within_directory,
    _existing_translation_exists,
    _resolve_output_filename,
    _resolve_relative_paths,
    _should_skip_walk_dir,
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
from .providers.registry import (
    _dispatch_provider_call,
    _resolve_provider,
)
from .segmentation import DEFAULT_TOKEN_LIMIT, MODEL_TOKEN_LIMITS, segment_text


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
    return file.endswith((".md", ".mdx")) and not is_excluded(file)


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

import argparse
import os
import sys

from .naming import (
    _ensure_within_directory,
    _resolve_single_output_filename,
    _validate_input_paths,
)
from .pipeline import _TranslationConfig, translate_directory, translate_markdown_file
from .providers.registry import (
    _add_provider_args,
    _select_provider_client,
)
from .segmentation import DEFAULT_TOKEN_LIMIT, MODEL_TOKEN_LIMITS

DEFAULT_SOURCE_LANG = "fr"
DEFAULT_TARGET_LANG = "en"
DEFAULT_SOURCE_DIR = "content/posts"
DEFAULT_TARGET_DIR = "traductions_en"


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

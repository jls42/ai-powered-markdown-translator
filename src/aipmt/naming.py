"""Nommage des fichiers de sortie et garde anti-traversée.

`EXCLUDE_PATTERNS`, le nom de fichier cible (`{base}-{lang}.md`, avec ou sans
modèle, ou conservé tel quel), la détection d'une traduction déjà présente, et
la vérification qu'aucun chemin construit à partir des arguments ne sort du
répertoire cible — deux couches : le refus des séparateurs dans les composants
du nom, puis la borne du chemin résolu.
"""

import glob
import os
import re

EXCLUDE_PATTERNS = ["traductions_", "venv", "PRIVACY.md"]


def _resolve_relative_paths(file_path, output_path, args):
    relative_file_path = os.path.join(
        args.source_dir, os.path.relpath(file_path, start=args.source_dir)
    )
    relative_output_path = os.path.join(
        args.target_dir, os.path.relpath(output_path, start=args.target_dir)
    )
    return relative_file_path, relative_output_path


def _write_output_file(output_path, translated_content, force, relative_output_path):
    """Écrit le fichier ou skippe si destination existe sans --force.

    Returns "success" si écrit, "skipped" si destination déjà présente.
    """
    clean_output_path = os.path.normpath(output_path)
    if os.path.exists(clean_output_path) and not force:
        print(
            f"Le fichier '{relative_output_path}' existe déjà, aucune traduction n'est effectuée."
        )
        return "skipped"
    # NOSONAR pythonsecurity:S8707 — chemin borné en amont par
    # _ensure_within_directory, dont les deux appelants consomment la valeur
    # de retour. Le moteur de contamination de Sonar ne reconnaît que ses
    # propres assainisseurs et ne peut pas suivre une fonction maison ; la
    # garde est vérifiée par tests, et l'évasion mesurée avant correctif
    # (--target_lang '../../tmp/X' → /tmp/X.md) est aujourd'hui refusée.
    with open(clean_output_path, "w", encoding="utf-8") as f:  # NOSONAR
        f.write(translated_content)
    return "success"


def is_excluded(path):
    return any(pattern in path for pattern in EXCLUDE_PATTERNS)


def _should_skip_walk_dir(root, output_dir, output_base_dir, input_dir):
    if is_excluded(root) or root.startswith(output_dir):
        return True
    # Skip un sous-répertoire direct d'input qui porte le même nom que le dossier de sortie.
    return (
        os.path.basename(root) == output_base_dir
        and os.path.abspath(os.path.join(root, "..")) == input_dir
    )


def _model_filename_label(model):
    """`provider/modèle` (OpenCode) contient un séparateur de chemin, et
    `ollama/qwen2.5:7b` un deux-points : dans un nom de fichier
    `--include_model`, le premier créerait un sous-répertoire, le second est
    illégal sous Windows. Les noms des autres providers ressortent inchangés."""
    return re.sub(r"[/:\\]", "-", model or "")


def _resolve_output_filename(file, base, args):
    if args.keep_filename:
        return file
    if args.include_model:
        return f"{base}-{args.target_lang}-{_model_filename_label(args.model)}.md"
    return f"{base}-{args.target_lang}.md"


def _existing_translation_exists(output_path, output_dir, base, args):
    if args.keep_filename:
        return os.path.exists(output_path)
    target_language_files = glob.glob(
        f"{output_dir}/**/{base}-{args.target_lang}*.md", recursive=True
    ) + glob.glob(f"{output_dir}/**/{base}-*{args.target_lang}.md", recursive=True)
    return any(os.path.exists(f) for f in target_language_files)


# Composants de nom de fichier fournis en ligne de commande. `--target_lang` et
# `--model` sont interpolés dans le nom du fichier de sortie
# (`{base}-{target_lang}.md`) : sans contrôle, une valeur contenant un
# séparateur de chemin sort du répertoire cible.
#
# Mesuré avant correction, avec --target_dir out/ :
#   --target_lang '../../../../../../tmp/EVASION'
#     → nom calculé  : doc-../../../../../../tmp/EVASION.md
#     → écriture     : /tmp/EVASION.md
# En mode répertoire c'est pire : `os.makedirs(os.path.dirname(...))` a lieu
# AVANT le premier appel au modèle, donc l'arborescence hors périmètre est
# créée même si la traduction échoue ensuite.
_FILENAME_COMPONENT_FLAGS = ("target_lang", "source_lang", "model")


def _looks_like_path_component(value):
    """True si `value` porte un séparateur de chemin ou désigne un répertoire."""
    if value in (".", ".."):
        return True
    return any(sep and sep in value for sep in (os.sep, os.altsep, "/"))


def _reject_path_separators_in_components(args):
    """Refuse tout composant de nom de fichier porteur d'un séparateur.

    Contrôle en amont, pour échouer avec un message qui nomme le flag fautif
    plutôt que de laisser la garde de périmètre parler d'un chemin calculé.
    """
    for flag in _FILENAME_COMPONENT_FLAGS:
        value = getattr(args, flag, None)
        if not (isinstance(value, str) and value):
            continue
        # Le contrôle porte sur la valeur telle qu'elle sera INTERPOLÉE. Pour
        # `--model`, c'est le libellé de nom de fichier : `provider/modèle`
        # est la forme légitime d'OpenCode et d'OpenRouter, et son « / » est remplacé avant
        # toute interpolation (cf. _model_filename_label) — il n'est donc plus
        # un séparateur de chemin, là où `..` en reste un.
        component = _model_filename_label(value) if flag == "model" else value
        if _looks_like_path_component(component):
            raise ValueError(
                f"--{flag} ne peut pas contenir de séparateur de chemin "
                f"(valeur reçue : {value!r}) : cette valeur est interpolée dans "
                "le nom du fichier de sortie."
            )


def _ensure_within_directory(base_dir, path, what="chemin de sortie"):
    """Garde de périmètre : `path` doit rester sous `base_dir`.

    Deuxième couche, indépendante du contrôle des composants : elle attrape
    tout chemin calculé qui sortirait du répertoire cible, quelle qu'en soit
    l'origine. `realpath` des deux côtés pour que la comparaison résiste aux
    liens symboliques et aux `..` intermédiaires.
    """
    base = os.path.realpath(base_dir)
    resolved = os.path.realpath(path)
    if resolved != base and not resolved.startswith(base + os.sep):
        raise ValueError(f"{what} sort du répertoire cible : {resolved!r} n'est pas sous {base!r}")
    # On renvoie le chemin NORMALISÉ, pas le realpath : la comparaison ci-dessus
    # a besoin de résoudre les liens symboliques, mais l'écriture doit rester au
    # chemin que l'utilisateur reconnaît. Les appelants consomment cette valeur
    # de retour au lieu de la variable d'origine — la validation fait ainsi
    # partie du flot de données, et non d'un simple effet de bord qu'un lecteur
    # (ou un analyseur) pourrait croire optionnel.
    return os.path.normpath(path)


def _validate_input_paths(args):
    _reject_path_separators_in_components(args)
    if args.file:
        if not os.path.isfile(args.file):
            raise ValueError(f"Le fichier spécifié n'existe pas : {args.file}")
    elif not os.path.isdir(args.source_dir):
        raise ValueError(f"Le répertoire source spécifié n'existe pas : {args.source_dir}")
    if not os.path.exists(args.target_dir):
        # `target_dir` est nommé par l'utilisateur : c'est la racine choisie, pas
        # un chemin calculé. Rien à valider ici — c'est ce qui est écrit DEDANS
        # qui doit rester dedans, ce que garantit _ensure_within_directory.
        # NOSONAR pythonsecurity:S8707 — cf. ci-dessus.
        os.makedirs(args.target_dir)  # NOSONAR


def _resolve_single_output_filename(args):
    if args.keep_filename:
        return os.path.basename(args.file)
    base = os.path.splitext(os.path.basename(args.file))[0]
    if args.include_model:
        return f"{base}-{args.target_lang}-{_model_filename_label(args.model)}.md"
    return f"{base}-{args.target_lang}.md"

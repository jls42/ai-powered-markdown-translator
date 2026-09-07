#!/usr/bin/env python3
"""Prouve que le découpage de `src/aipmt/translate.py` est un déplacement pur.

Outil de refactor, temporaire par construction : il gèle le contenu du paquet
`aipmt` au niveau de l'AST pendant que ses 4 253 lignes sont réparties en
modules. Il disparaît avec la pull request qui suit le découpage, quand le
code recommence légitimement à changer.

Ce qu'il vérifie, et pourquoi chaque point existe :

1. **Multiensemble des nœuds de premier niveau.** Chaque fonction, classe,
   constante et expression de premier niveau (docstrings comprises, imports
   exclus) est hachée sur son texte normalisé — commentaires retirés, blancs
   ignorés ; pas `ast.dump()`, qui change d'une version de Python à l'autre. L'ensemble courant, réuni sur
   tous les modules de `src/aipmt/`, doit valoir le snapshot de référence plus
   le manifeste cumulatif (ajouts, retraits, modifications déclarés), ni plus
   ni moins. Un symbole déplacé mais laissé en place compte deux fois et
   échoue ; un symbole perdu manque et échoue ; un corps retouché change de
   haché et échoue tant qu'il n'est pas déclaré.
2. **Emplacement.** Un symbole nommé dans la table cible ne peut vivre que
   dans `translate.py` (pas encore déplacé) ou dans son module cible. La
   structure annoncée est ainsi vérifiée, pas seulement le contenu.
3. **Marqueurs de sécurité.** Chaque ligne portant `# nosec`, `# nosemgrep` ou
   `NOSONAR` dans la référence doit exister verbatim dans un module — les
   lignes d'import exceptées, dont la justification est réécrite par module.
   Et tout `import subprocess` du paquet doit porter `# nosec B404`. Un
   marqueur perdu ne se voit qu'au pre-push ou chez Sonar, trop tard pour
   savoir quel commit l'a perdu.
4. **Fichiers non suivis.** pre-commit ne voit que l'index : un module créé
   sans `git add` passait tous les hooks et le commit partait sans lui. Tout
   `.py` non suivi sous `src/aipmt/`, `tests/` ou `scripts/tests/` est refusé.

Le snapshot est stocké dans le dépôt (et non lu par `git show`) parce que la
CI fait un checkout superficiel : la révision de référence n'y existe pas.

Usage :
    scripts/check-split-purity.py                 # vérifie
    scripts/check-split-purity.py --write-snapshot  # (re)génère la référence
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import io
import json
import os
import pathlib
import subprocess  # nosec B404 — interroge git pour les fichiers non suivis, argv littéral
import sys
import tokenize
from collections import Counter

ORIGIN_NAME = "translate.py"
PACKAGE = pathlib.Path("src/aipmt")
ORIGIN = PACKAGE / ORIGIN_NAME
SNAPSHOT = pathlib.Path("scripts/split-reference/package-6ae1505.json")
MANIFEST = pathlib.Path("scripts/split-reference/manifest.json")
REFERENCE_REVISION = "6ae1505"
MARKERS = ("# nosec", "# nosemgrep", "NOSONAR")
GUARDED_DIRS = ("src/aipmt", "tests", "scripts/tests")

# Table cible du découpage : module (relatif à src/aipmt/, sans .py) → symboles.
# C'est la structure annoncée dans le plan ; la règle 2 la rend vérifiable.
TARGET_MODULES: dict[str, tuple[str, ...]] = {
    "config": ("_user_config_path", "_load_configuration", "_missing_key_message"),
    "markdown": (
        "news_quote_placeholder",
        "news_quote_placeholder_regex",
        "_STRUCTURAL_LINE",
        "_INLINE_MD_PREFIX",
        "_EMPTY_BLOCKQUOTE_LINE",
        "_BLOCKQUOTE_PREFIX",
        "_URL_OR_PLACEHOLDER",
        "_NEWSQUOTE_PLACEHOLDER_REGEX",
        "_MARKDOWN_LINK",
        "_HTML_TAG_REGEX",
        "_LANG_SCRIPT_RANGES",
        "_LANG_SCRIPT_NAMES",
    ),
    "segmentation": (
        "DEFAULT_TOKEN_LIMIT",
        "MODEL_TOKEN_LIMITS",
        "_find_last_h2_h3_match",
        "_find_segment_breakpoint",
        "segment_text",
    ),
    "guards": (
        "_looks_like_proper_noun_list",
        "_clean_for_language_detection",
        "_count_chars_in_ranges",
        "_has_target_script_signal",
        "_line_is_droppable",
        "_clean_paragraph_for_window",
        "_windows_from_clean_text",
        "_extract_source_windows",
        "_check_output_short_ratio",
        "_check_passthrough_excerpt",
        "_check_output_language",
        "_validate_translation_output",
    ),
    "placeholders": (
        "_SEGMENT_PLACEHOLDER_REGEX",
        "_validate_segment_placeholders",
        "_FENCED_CODE_REGEX",
        "_INLINE_CODE_REGEX",
        "_protect_code_blocks",
        "_protect_inline_code",
        "_URL_PROTECTION_REGEX",
        "_protect_urls",
        "_restore_urls",
        "_ANCHOR_NAME_REGEX",
        "_ANCHOR_LINK_REGEX",
        "_HTML_HREF_ANCHOR_REGEX",
        "_HEADING_REGEX",
        "_github_slug",
        "_extract_heading_slugs",
        "_classify_anchor_target",
        "_collect_md_anchor_links",
        "_collect_html_href_anchors",
        "_protect_anchors",
        "_restore_anchors",
        "_build_heading_slug_map",
        "_REF_DEFINITION_REGEX",
        "_protect_ref_labels",
        "_restore_ref_labels",
        "_restore_code",
        "_CODE_PLACEHOLDER_LEFTOVER_REGEX",
        "_check_placeholders_present",
        "_validate_code_placeholders_present",
        "_validate_ref_label_placeholders_present",
        "_validate_no_code_placeholder_leftover",
        "_normalize_collapsed_markdown",
    ),
    "news": (
        "LANG_FLAGS",
        "_build_news_rules_en",
        "_build_news_placeholder_rule",
        "_build_news_flag_rule",
        "_NEWS_RULES_EXAMPLES",
        "_build_news_result_format",
        "_build_news_rules_other",
        "_NEWS_FINAL_CHECKS",
        "_build_news_addendum",
        "_NEWS_CITATION_REGEX",
        "_RESIDUAL_NEWS_PLACEHOLDER_REGEX",
        "_protect_news_quotes",
        "_validate_news_placeholders_intact",
        "_restore_news_quotes",
        "_cleanup_source_flag_for_en",
        "_cleanup_source_flag_swap",
        "_cleanup_source_flag",
        "_validate_news_flags_for_en",
        "_validate_news_flags_for_other",
        "_validate_news_post",
    ),
    "prompts": (
        "_build_translation_note_prompt",
        "_build_base_markdown_prompt",
        "_MARKDOWN_TRANSLATION_CONTRACT",
        "_PLACEHOLDER_PRESERVATION_CONTRACT",
        "_HEADING_ANCHOR_CONSISTENCY_CONTRACT",
        "_build_non_latin_script_addendum",
        "_build_system_instructions",
    ),
    "notes": (
        "_VIEW_PROJECT_LABELS",
        "_translation_note_invariants",
        "_build_translation_note_phrase",
        "_assemble_translation_note_paragraphs",
        "_build_translation_note_source",
        "_sanitize_model",
        "_quote_lines",
        "_split_frontmatter",
        "_build_translation_note_block",
        "_compose_with_notes",
    ),
    "naming": (
        "EXCLUDE_PATTERNS",
        "_resolve_relative_paths",
        "_write_output_file",
        "is_excluded",
        "_should_skip_walk_dir",
        "_model_filename_label",
        "_resolve_output_filename",
        "_existing_translation_exists",
        "_FILENAME_COMPONENT_FLAGS",
        "_looks_like_path_component",
        "_reject_path_separators_in_components",
        "_ensure_within_directory",
        "_validate_input_paths",
        "_resolve_single_output_filename",
    ),
    "pipeline": (
        "_LLMCallSpec",
        "_translate_segment_with_retry",
        "translate",
        "_append_translation_note",
        "_PipelineState",
        "_protect_pipeline_inputs",
        "_restore_pipeline_outputs",
        "_TranslationConfig",
        "_translate_pipeline",
        "_read_translatable_source",
        "_translate_one_file",
        "translate_markdown_file",
        "_record_translation_status",
        "_DirectoryWalkContext",
        "_process_one_markdown_file",
        "_is_translatable_markdown",
        "translate_directory",
    ),
    "cli": (
        "DEFAULT_SOURCE_LANG",
        "DEFAULT_TARGET_LANG",
        "DEFAULT_SOURCE_DIR",
        "DEFAULT_TARGET_DIR",
        "_add_io_args",
        "_add_lang_args",
        "_add_output_naming_args",
        "_add_note_args",
        "_add_news_args",
        "_build_arg_parser",
        "_build_translation_config",
        "_run_single_file",
        "_run_directory",
        "main",
    ),
    "providers/registry": (
        "_resolve_provider",
        "_PROVIDER_LABELS",
        "_dispatch_provider_call",
        "_add_provider_args",
        "_select_provider_client",
    ),
    "providers/base": (
        "CODEX_TERM_GRACE",
        "_NAMESPACED_MODEL_REGEX",
        "_reason_name",
        "_SECRET_ENV_NAME_PATTERNS",
        "_strip_secret_env",
        "_codex_kill_group",
        "_CLI_TIMEOUT_ENV_VARS",
        "_codex_run_process",
        "_stderr_tail",
        "_CliCallError",
        "_retry_on_rate_limit",
        "_CLI_PROVIDER_CI_FALLBACK",
        "_codex_reject_ci_environment",
    ),
    "providers/openai": (
        "DEFAULT_OPENAI_API_KEY",
        "DEFAULT_MODEL_OPENAI",
        "ECO_MODEL_OPENAI",
        "_O1_SERIES",
        "_resolve_reasoning_effort",
        "_build_openai_messages",
        "_openai_extra_kwargs",
        "_openai_create_with_fallback",
        "_call_openai",
        "_init_openai_client",
    ),
    "providers/mistral": (
        "DEFAULT_MISTRAL_API_KEY",
        "DEFAULT_MODEL_MISTRAL",
        "ECO_MODEL_MISTRAL",
        "_call_mistral",
        "_init_mistral_client",
    ),
    "providers/anthropic": (
        "DEFAULT_ANTHROPIC_API_KEY",
        "DEFAULT_MODEL_CLAUDE",
        "ECO_MODEL_CLAUDE",
        "CLAUDE_MAX_TOKENS",
        "CLAUDE_TIMEOUT",
        "_CLAUDE_NON_TEXT_BLOCK_TYPES",
        "_call_claude",
        "_init_claude_client",
    ),
    "providers/gemini": (
        "DEFAULT_GEMINI_API_KEY",
        "DEFAULT_MODEL_GEMINI",
        "ECO_MODEL_GEMINI",
        "_gemini_config",
        "_GEMINI_THINKING_LEVELS",
        "_GEMINI_ACCEPTED_THINKING_LEVEL",
        "_gemini_generate_with_fallback",
        "_call_gemini",
        "_init_gemini_client",
    ),
    "providers/grok": (
        "DEFAULT_XAI_API_KEY",
        "DEFAULT_MODEL_GROK",
        "ECO_MODEL_GROK",
        "DEFAULT_MODEL_GROK_CLI",
        "ECO_MODEL_GROK_CLI",
        "XAI_BASE_URL",
        "GROK_TIMEOUT",
        "GROK_PROMPT_FILENAME",
        "GROK_DENY_RULES",
        "GROK_MAX_TURNS",
        "GROK_STRIPPED_ENV_VARS",
        "GROK_ENV_KILL_SWITCHES",
        "GROK_SANDBOX_ENV_VAR",
        "GROK_AGENT_CONTRACT",
        "_GrokCliClient",
        "_grok_env",
        "_grok_write_prompt",
        "_grok_argv",
        "_grok_parse_payload",
        "_GROK_RATE_LIMIT_MARKERS",
        "_grok_check_payload",
        "_grok_extract_text",
        "_GrokCallError",
        "_grok_attempt",
        "_call_grok_cli",
        "_resolve_grok_binary",
        "_grok_preflight",
        "_grok_sandbox_profile",
        "_init_grok_cli_client",
        "_init_grok_client",
    ),
    "providers/openrouter": (
        "DEFAULT_OPENROUTER_API_KEY",
        "OPENROUTER_BASE_URL",
        "OPENROUTER_TIMEOUT",
        "OPENROUTER_PREFLIGHT_TIMEOUT",
        "OPENROUTER_MIN_COMPLETION_TOKENS",
        "OPENROUTER_MAX_TOKENS",
        "OPENROUTER_EFFORTS_CROISSANTS",
        "_openrouter_http_get",
        "_openrouter_catalog_entry",
        "_openrouter_endpoints",
        "_openrouter_pin",
        "_OpenRouterClient",
        "_openrouter_reasoning",
        "_openrouter_lowest_effort",
        "_openrouter_reasoning_label",
        "_openrouter_extra_body",
        "_openrouter_first_choice",
        "_openrouter_check_finish",
        "_call_openrouter",
        "_openrouter_validate_model",
        "_init_openrouter_client",
    ),
    "providers/codex": (
        "DEFAULT_MODEL_CODEX",
        "ECO_MODEL_CODEX",
        "CODEX_TIMEOUT",
        "CODEX_MODEL_PREFIXES",
        "CODEX_STRIPPED_ENV_VARS",
        "CODEX_AGENT_CONTRACT",
        "_CodexClient",
        "_codex_env_base",
        "_codex_env",
        "_codex_argv",
        "_codex_run",
        "_codex_unwrap_error",
        "_codex_error_from_events",
        "_codex_is_rate_limited",
        "_codex_describe_error",
        "_codex_read_output",
        "_codex_attempt",
        "_CodexCallError",
        "_call_codex",
        "_resolve_codex_binary",
        "_codex_preflight",
        "_codex_warn_unexpected_model",
        "_init_codex_client",
    ),
    "providers/opencode": (
        "OPENCODE_TIMEOUT",
        "OPENCODE_AGENT_NAME",
        "OPENCODE_SESSION_TITLE",
        "OPENCODE_ENV_KILL_SWITCHES",
        "OPENCODE_KEPT_ENV_VARS",
        "_OPENCODE_RATE_LIMIT_MARKERS",
        "_OPENCODE_LOG_ERROR_REGEX",
        "_OPENCODE_AGENT_FALLBACK_REGEX",
        "OPENCODE_AGENT_CONTRACT",
        "_OpencodeClient",
        "_OpencodeCallError",
        "_opencode_env_base",
        "_opencode_config_content",
        "_opencode_env",
        "_opencode_argv",
        "_opencode_events",
        "_opencode_stderr_cause",
        "_opencode_error_data",
        "_opencode_is_rate_limited",
        "_opencode_raise_reported_error",
        "_opencode_raise_exit_code",
        "_opencode_check_completion",
        "_opencode_raise_on_failure",
        "_opencode_text_parts",
        "_opencode_extract_text",
        "_opencode_attempt",
        "_call_opencode",
        "_resolve_opencode_binary",
        "_opencode_preflight",
        "_init_opencode_client",
    ),
}
TARGET_OF: dict[str, str] = {
    name: module for module, names in TARGET_MODULES.items() for name in names
}


def _within_root(path: pathlib.Path) -> pathlib.Path:
    """Refuse tout chemin qui sortirait de la racine courante.

    Les chemins viennent de la ligne de commande d'un outil de développement ;
    les borner n'en fait pas une surface d'attaque, mais dit explicitement où
    l'outil a le droit de lire et d'écrire : sous la racine, jamais ailleurs.
    """
    root = pathlib.Path.cwd().resolve()
    resolved = (root / path).resolve()
    if resolved != root and root not in resolved.parents:
        raise SystemExit(f"chemin hors de la racine refusé : {path}")
    return resolved


def _is_main_guard(node: ast.AST) -> bool:
    return isinstance(node, ast.If) and "__name__" in ast.dump(node.test)


def _node_name(node: ast.AST) -> str:
    if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef):
        return node.name
    if isinstance(node, ast.Assign):
        return ",".join(ast.unparse(target) for target in node.targets)
    if isinstance(node, ast.AnnAssign | ast.AugAssign):
        return ast.unparse(node.target)
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant):
        return "<docstring>"
    return "<" + ast.unparse(node).splitlines()[0][:60] + ">"


def _strip_comments(source: str) -> list[str]:
    """Lignes du source sans leurs commentaires, via les positions de `tokenize`.

    Les commentaires sont vérifiés à part (marqueurs de sécurité) ; ici on hache
    le CODE. Retirer les commentaires par leurs positions de jeton, et non par
    regex, laisse intact un `#` à l'intérieur d'une chaîne.
    """
    lines = source.splitlines()
    comments: dict[int, int] = {}
    tokens = tokenize.generate_tokens(io.StringIO(source).readline)
    for token in tokens:
        if token.type == tokenize.COMMENT:
            comments[token.start[0] - 1] = token.start[1]
    return [line[: comments[i]] if i in comments else line for i, line in enumerate(lines)]


def _node_digest(node: ast.stmt, lines: list[str]) -> str:
    """Haché du texte normalisé du nœud : commentaires retirés, blancs de fin et
    lignes vides ignorés. Le texte, et non `ast.dump()`, parce que ce dernier
    change d'une version de Python à l'autre — mesuré en CI : les f-strings de
    3.12 ne se représentent pas comme celles de 3.10 et 3.11, et 44 nœuds
    identiques passaient pour perdus. Le texte d'un même code est le même
    partout."""
    start = node.lineno
    decorators = getattr(node, "decorator_list", None)
    if decorators:
        start = min(start, min(d.lineno for d in decorators))
    segment = [line.rstrip() for line in lines[start - 1 : node.end_lineno]]
    text = "\n".join(line for line in segment if line.strip())
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def collect_nodes(package: pathlib.Path) -> list[dict[str, str]]:
    """Nœuds de premier niveau de tous les modules, imports et garde `__main__` exclus."""
    nodes = []
    for path in sorted(package.rglob("*.py")):
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(path))
        lines = _strip_comments(source)
        for node in tree.body:
            if isinstance(node, ast.Import | ast.ImportFrom) or _is_main_guard(node):
                continue
            digest = _node_digest(node, lines)
            nodes.append(
                {
                    "hash": digest,
                    "name": _node_name(node),
                    "kind": type(node).__name__,
                    "file": path.as_posix(),
                }
            )
    return nodes


def collect_markers(origin: pathlib.Path) -> list[str]:
    """Lignes porteuses d'un marqueur de sécurité, hors imports, dédoublonnées."""
    seen: list[str] = []
    for line in origin.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith(("import ", "from ")):
            continue
        if any(marker in stripped for marker in MARKERS) and stripped not in seen:
            seen.append(stripped)
    return seen


def write_snapshot(package: pathlib.Path, origin: pathlib.Path, snapshot: pathlib.Path) -> int:
    nodes = collect_nodes(package)
    payload = {
        "reference": REFERENCE_REVISION,
        "package": package.as_posix(),
        "nodes": nodes,
        "markers": collect_markers(origin),
    }
    snapshot.parent.mkdir(parents=True, exist_ok=True)
    # NOSONAR pythonsecurity:S2083 pythonsecurity:S8707 — chemin borné à la racine
    # par _within_root avant tout accès ; outil de développement lancé par un
    # mainteneur, sans entrée réseau.
    snapshot.write_text(
        json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )  # NOSONAR
    print(f"snapshot écrit : {snapshot} ({len(nodes)} nœuds, {len(payload['markers'])} marqueurs)")
    return 0


def _load_manifest(manifest: pathlib.Path) -> dict[str, list[dict[str, str]]]:
    if not manifest.exists():
        return {"added": [], "removed": [], "modified": []}
    # NOSONAR pythonsecurity:S8707 — cf. write_snapshot, même borne.
    data = json.loads(manifest.read_text(encoding="utf-8"))  # NOSONAR
    return {key: list(data.get(key, [])) for key in ("added", "removed", "modified")}


def _expected_counter(
    snapshot_nodes: list[dict[str, str]], manifest: dict[str, list[dict[str, str]]]
) -> Counter[str]:
    expected: Counter[str] = Counter(node["hash"] for node in snapshot_nodes)
    for entry in manifest["added"]:
        expected[entry["hash"]] += 1
    for entry in manifest["removed"]:
        expected[entry["hash"]] -= 1
    for entry in manifest["modified"]:
        expected[entry["old_hash"]] -= 1
        expected[entry["new_hash"]] += 1
    return +expected


def check_nodes(
    current: list[dict[str, str]],
    snapshot_nodes: list[dict[str, str]],
    manifest: dict[str, list[dict[str, str]]],
) -> list[str]:
    problems = []
    expected = _expected_counter(snapshot_nodes, manifest)
    actual: Counter[str] = Counter(node["hash"] for node in current)
    names = {node["hash"]: node["name"] for node in snapshot_nodes + current}
    for entry in manifest["added"] + manifest["modified"]:
        names.setdefault(entry.get("hash", entry.get("new_hash", "")), entry["name"])
    for digest, count in (actual - expected).items():
        where = sorted({node["file"] for node in current if node["hash"] == digest})
        problems.append(
            f"nœud inattendu x{count} : {names.get(digest, '?')} dans {', '.join(where)} "
            "— déclarer l'ajout ou la modification dans le manifeste, ou retirer le doublon"
        )
    for digest, count in (expected - actual).items():
        problems.append(
            f"nœud manquant x{count} : {names.get(digest, digest[:12])} — perdu ou modifié "
            "sans déclaration"
        )
    return problems


def check_locations(current: list[dict[str, str]], package: pathlib.Path) -> list[str]:
    origin = (package / ORIGIN_NAME).as_posix()
    problems = []
    for node in current:
        for name in node["name"].split(","):
            target = TARGET_OF.get(name)
            if target is None:
                continue
            allowed = {origin, (package / f"{target}.py").as_posix()}
            if node["file"] not in allowed:
                problems.append(
                    f"{name} est dans {node['file']} ; sa cible est {package.as_posix()}/{target}.py"
                )
    return problems


def check_markers(package: pathlib.Path, markers: list[str]) -> list[str]:
    present: set[str] = set()
    problems = []
    for path in sorted(package.rglob("*.py")):
        for line in path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            present.add(stripped)
            if stripped.startswith("import subprocess") and "# nosec B404" not in stripped:
                problems.append(f"{path.as_posix()} : `import subprocess` sans `# nosec B404`")
    for marker in markers:
        if marker not in present:
            problems.append(f"marqueur perdu : {marker}")
    return problems


def check_untracked(root: pathlib.Path) -> list[str]:
    argv = ["git", "ls-files", "--others", "--exclude-standard", "--", *GUARDED_DIRS]
    # nosemgrep
    result = subprocess.run(  # nosec B603 B607 # nosemgrep — argv littéral, git du PATH
        argv,  # nosemgrep
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return [f"git ls-files a échoué (rc={result.returncode}) : {result.stderr.strip()}"]
    untracked = [line for line in result.stdout.splitlines() if line.endswith(".py")]
    return [
        f"fichier non suivi : {path} — `git add` avant de commiter, les hooks ne voient que l'index"
        for path in untracked
    ]


def check(
    root: pathlib.Path, package: pathlib.Path, snapshot: pathlib.Path, manifest: pathlib.Path
) -> int:
    if not snapshot.exists():
        print(f"✗ snapshot absent : {snapshot} — générer avec --write-snapshot", file=sys.stderr)
        return 1
    # NOSONAR pythonsecurity:S8707 — cf. write_snapshot, même borne.
    reference = json.loads(snapshot.read_text(encoding="utf-8"))  # NOSONAR
    current = collect_nodes(package)
    declared = _load_manifest(manifest)
    problems = (
        check_nodes(current, reference["nodes"], declared)
        + check_locations(current, package)
        + check_markers(package, reference["markers"])
        + check_untracked(root)
    )
    if problems:
        print("✗ le découpage n'est plus un déplacement pur :", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        return 1
    modules = sorted({node["file"] for node in current})
    print(
        f"✓ pureté : {len(current)} nœuds sur {len(modules)} module(s), "
        f"{len(reference['markers'])} marqueurs, référence {reference['reference']}"
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path("."))
    parser.add_argument("--package", type=pathlib.Path, default=PACKAGE)
    parser.add_argument("--snapshot", type=pathlib.Path, default=SNAPSHOT)
    parser.add_argument("--manifest", type=pathlib.Path, default=MANIFEST)
    parser.add_argument("--write-snapshot", action="store_true")
    args = parser.parse_args(argv)
    # Chemins relatifs à la racine, pour que le snapshot soit portable d'un
    # poste à la CI : un chemin absolu y serait faux par construction.
    previous = os.getcwd()
    os.chdir(args.root)
    for path in (args.package, args.snapshot, args.manifest):
        _within_root(path)
    try:
        if args.write_snapshot:
            return write_snapshot(args.package, args.package / ORIGIN_NAME, args.snapshot)
        return check(pathlib.Path("."), args.package, args.snapshot, args.manifest)
    finally:
        os.chdir(previous)


if __name__ == "__main__":
    sys.exit(main())

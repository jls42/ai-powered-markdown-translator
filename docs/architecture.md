# Architecture

**Paquet installable, découpé par responsabilité** : le paquet est `src/aipmt/`.
`__init__.py` importe `config` EN PREMIER (il charge `.env` à l'import, avant
que les providers lisent `os.getenv` au niveau module) puis expose `main` (cité
par `[project.scripts] aipmt`) ; `__main__.py` permet `python -m aipmt`.
L'exécution directe du fichier (`python src/aipmt/translate.py`) n'existe plus
depuis le découpage : les imports sont relatifs.

Le nom d'import est `aipmt` et **jamais** `translate` : le paquet PyPI `translate`
(v3.8.1, actif) installe un répertoire homonyme qui masquerait le module — le
point d'entrée casse alors sur `AttributeError` et `pip check` ne voit rien.

Modules, dans l'ordre topologique des imports : chaque flèche de dépendance va vers
un module plus HAUT dans le tableau, jamais l'inverse.

| Module                  | Rôle                                                                                                                          |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `config.py`             | Trois couches de clés (env, `.env`, `~/.config/aipmt/.env`), `_missing_key_message`                                           |
| `markdown.py`           | Lexique partagé : regex de lignes structurelles, liens, balises, placeholders ; plages d'écritures                            |
| `segmentation.py`       | `segment_text()`, `MODEL_TOKEN_LIMITS` (objet unique, OpenRouter y écrit la fenêtre lue au préflight)                         |
| `naming.py`             | `EXCLUDE_PATTERNS`, nom de sortie, traduction déjà présente, garde anti-traversée, écriture                                   |
| `notes.py`              | Note de traduction (constructeurs purs)                                                                                       |
| `guards.py`             | Gardes de sortie : langue détectée, extrait source verbatim, ratio, écriture cible ; graine langdetect                        |
| `placeholders.py`       | Protection/restauration des blocs de code, code inline, URL, ancres, labels — et leurs validations                            |
| `news.py`               | Mode `--news` : `<NEWSQUOTE id="N"/>`, drapeaux par langue, règles du prompt et validations                                   |
| `prompts.py`            | Instructions système : contrat Markdown, placeholders, ancres, addenda news et écritures non latines                          |
| `providers/base.py`     | Socle des CLI : sous-processus, secrets, back-off, erreurs, refus en CI                                                       |
| `providers/<nom>.py`    | Un module par provider : `openai`, `mistral`, `anthropic`, `gemini`, `codex`, `grok`, `antigravity`, `opencode`, `openrouter` |
| `providers/registry.py` | `_resolve_provider`, `_PROVIDER_LABELS`, `_dispatch_provider_call`, `_select_provider_client`, flags                          |
| `pipeline.py`           | `translate()`, `translate_markdown_file()`, `translate_directory()`, `_append_translation_note()`                             |
| `cli.py`                | argparse hors providers, validation des chemins, `main()`                                                                     |
| `translate.py`          | FAÇADE de compatibilité : les 64 noms publics de l'ancien module unique, par identité ; `__all__` à 9                         |

Deux règles qui découlent du découpage, verrouillées par `tests/test_facade_contract.py` :

- **Un patch de test vise le module qui CONSULTE le nom, jamais la façade.**
  `patch("aipmt.translate.translate_markdown_file")` réussissait sans rien
  intercepter (le nom consommé est celui de `aipmt.cli`) — et deux tests
  restaient verts sans leur patch. Détection par AST dans `tests/` et
  `scripts/tests/`, quotes simples et appels multilignes compris.
- **La façade ne ré-exporte ni nom privé, ni SDK, ni module stdlib.** Un patch
  posé au mauvais endroit lève `AttributeError` au lieu de ne plus mordre.

**Vérificateur de pureté du découpage, retiré en 1.17.0** : il comparait les
nœuds AST du paquet à un snapshot pris au découpage de la 1.13.0, et devait
partir avec la PR suivante. Il est resté huit releases, et chaque PR de code
devait déclarer ses écarts dans son manifeste (#48, #49, #50). Son refus des
`.py` non suivis par git — pre-commit ne voit que l'index — vit désormais dans
la section 6 de `check-release-ready.sh`. Le reste est dans l'historique git
(`scripts/check-split-purity.py`, `scripts/split-reference/`).

**Output naming**:

- Default: `{base}-{target_lang}.md` (e.g., `README-en.md`)
- With `--include_model`: `{base}-{target_lang}-{model}.md`
- With `--keep_filename`: original filename (for destination folder workflows)

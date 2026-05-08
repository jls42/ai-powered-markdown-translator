# Traducteur de Markdown AI-Powered

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

<h4 align="center">📊 Qualité du code</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Quality Gate Status"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Security Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Reliability Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Maintainability Rating"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Coverage"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilities"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Duplicated Lines (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Technical Debt"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Lines of Code"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy Badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Traducteur de fichiers Markdown utilisant **OpenAI**, **Mistral AI**, **Claude (Anthropic)** et **Google Gemini**.

Ce script Python traduit des fichiers Markdown d'une langue source vers une langue cible tout en préservant le formatage, les blocs de code et les métadonnées front matter.

## Caractéristiques Principales

- **Multi-Provider**: Support de 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **Modèles 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Mode Économique**: Option `--eco` pour utiliser des modèles plus rapides et moins coûteux
- **Fichier Unique**: Option `--file` pour traduire un seul fichier
- **Segmentation Intelligente**: Gestion des textes longs avec limites de tokens par modèle
- **Préservation du Code**: Les blocs de code ET le code inline (`` `...` ``) sont préservés
- **Nom de Fichier**: Option `--keep_filename` pour conserver le nom original
- **Mode News**: Option `--news` pour protéger les citations anglaises et gérer les drapeaux dans les articles d'actualité
- **Configuration .env**: Support du fichier `.env` pour les clés API
- **Note de Traduction**: Ajout optionnel d'une note en fin de document

## Installation

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Outillage qualité (optionnel mais recommandé)

Le projet utilise [`pre-commit`](https://pre-commit.com) pour empêcher de committer du code mal formaté, vulnérable ou contenant un secret. Installation :

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hooks actifs : ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexité), detect-secrets (clés API), mypy (typage progressif), Opengrep (SAST), pip-audit (CVE deps), unittest. Voir `CLAUDE.md` section _Quality / pre-commit_ pour les détails.

## Configuration

Créez un fichier `.env` à la racine du projet ou définissez les variables d'environnement :

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

## Utilisation

### Traduire un fichier unique

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Traduire un répertoire

```bash
# Avec OpenAI (défaut: gpt-5.5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### Mode économique

Utilise des modèles plus rapides et moins coûteux (gpt-5.4-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Options

| Option                   | Description                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Fichier Markdown unique à traduire                                       |
| `--source_dir`           | Répertoire source contenant les fichiers Markdown                        |
| `--target_dir`           | Répertoire de sortie pour les fichiers traduits                          |
| `--source_lang`          | Langue source (défaut: `fr`)                                             |
| `--target_lang`          | Langue cible (défaut: `en`)                                              |
| `--model`                | Modèle spécifique à utiliser                                             |
| `--eco`                  | Utiliser les modèles économiques                                         |
| `--use_mistral`          | Utiliser l'API Mistral AI                                                |
| `--use_claude`           | Utiliser l'API Claude                                                    |
| `--use_gemini`           | Utiliser l'API Gemini                                                    |
| `--force`                | Forcer la re-traduction                                                  |
| `--keep_filename`        | Conserver le nom de fichier original                                     |
| `--news`                 | Mode actualités : protège les citations EN, gère les drapeaux par langue |
| `--add_translation_note` | Ajouter une note de traduction                                           |
| `--note_position`        | Position de la note : `top`, `bottom` (défaut), ou `both`                |
| `--note_format`          | Format de la note : `legacy` (défaut, paragraphe gras) ou `marker`       |
| `--include_model`        | Inclure le nom du modèle dans le fichier de sortie                       |

### Note de traduction : positions et formats

Avec `--add_translation_note`, le translator peut placer la note en haut, en bas, ou aux deux endroits, et la rendre soit en format texte simple (rétrocompatible) soit en format `marker` consommable par un plugin Markdown.

**Position** (`--note_position`) :

- `bottom` (défaut) : note en fin de fichier, comme historiquement.
- `top` : note insérée **après le frontmatter YAML** (sécurité Astro Content Collections, gray-matter, etc.).
- `both` : note insérée en haut ET en bas (un seul appel LLM, contenu réutilisé pour les deux placements).

**Format** (`--note_format`) :

- `legacy` (défaut) : paragraphe gras `**...**` — comportement strictement identique à v1.8, byte-for-byte. Compatible avec Hugo, GitHub, GitLab, et tout renderer Markdown.
- `marker` : link reference definition Markdown invisible (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) suivie d'un blockquote en gras. Lisible nativement sur GitHub/GitLab, et exploitable au build par un plugin remark côté Astro pour produire une bannière stylisée (cf. blog jls42.org).

```bash
# Compatibilité legacy (rien ne change vs v1.8)
python translate.py --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### Modèles par défaut (2026)

| Provider | Qualité (défaut)         | Économique (`--eco`)            |
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **Recommandation traductions long-form** : `--use_gemini` (défaut = `gemini-3.1-pro-preview` qualité, `--eco` = `gemini-3.1-flash-lite-preview`) tend à mieux préserver la structure markdown sur les scripts non-latins (PL, JA, ZH, AR, HI), notamment en mode `--news` où la fidélité des placeholders compte. OpenAI reste le défaut pour la rétrocompatibilité.

## Projets utilisant ce script

- **[jls42.org](https://jls42.org)** - Blog personnel multilingue (15 langues)

## Auteur

Julien LE SAUX
Email : contact@jls42.org

## Licence

GNU GENERAL PUBLIC LICENSE Version 3. Voir [LICENSE](LICENSE).

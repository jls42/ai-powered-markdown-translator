# AI-Powered Markdown Translator

🌍 [French](README.md) | [English](README-en.md) | [Spanish](README-es.md) | [Chinese](README-zh.md) | [German](README-de.md) | [Japanese](README-ja.md) | [Korean](README-ko.md) | [Arabic](README-ar.md) | [Hindi](README-hi.md) | [Italian](README-it.md) | [Dutch](README-nl.md) | [Polish](README-pl.md) | [Portuguese](README-pt.md) | [Romanian](README-ro.md) | [Swedish](README-sv.md)

<h4 align="center">📊 Code Quality</h4>

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

Markdown file translator using **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, and **Google Gemini**.

This Python script translates Markdown files from a source language to a target language while preserving formatting, code blocks, and front matter metadata.

## Key Features

- **Multi-Provider**: Support for 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **2026 Models**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Economy Mode**: Option `--eco` to use faster, lower-cost models
- **Single File**: Option `--file` to translate a single file
- **Intelligent Segmentation**: Handles long texts with model token limits
- **Code Preservation**: Code blocks AND inline code (`` `...` ``) are preserved
- **File Name**: Option `--keep_filename` to keep the original name
- **News Mode**: Option `--news` to protect English quotes and handle flags in news articles
- **.env Configuration**: Support for the `.env` file for API keys
- **Translation Note**: Optional note added at the end of the document

## Installation

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Quality tooling (optional but recommended)

The project uses [`pre-commit`](https://pre-commit.com) to prevent committing badly formatted, vulnerable, or secret-containing code. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Active hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexity), detect-secrets (API keys), mypy (gradual typing), Opengrep (SAST), pip-audit (CVE deps), unittest. See `CLAUDE.md` section _Quality / pre-commit_ for details.

## Configuration

Create a `.env` file in the project root or define the environment variables:

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

## Usage

### Translate a single file

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Translate a directory

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

### Economy mode

Uses faster, lower-cost models (gpt-5.4-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Options

| Option                   | Description                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Single Markdown file to translate                                       |
| `--source_dir`           | Source directory containing Markdown files                               |
| `--target_dir`           | Output directory for translated files                                   |
| `--source_lang`          | Source language (default: `fr`)                                             |
| `--target_lang`          | Target language (default: `en`)                                              |
| `--model`                | Specific model to use                                                   |
| `--eco`                  | Use economy models                                                     |
| `--use_mistral`          | Use the Mistral AI API                                                |
| `--use_claude`           | Use the Claude API                                                    |
| `--use_gemini`           | Use the Gemini API                                                    |
| `--force`                | Force re-translation                                                  |
| `--keep_filename`        | Keep the original file name                                     |
| `--news`                 | News mode: protects EN quotes, handles language flags |
| `--add_translation_note` | Add a translation note                                           |
| `--note_position`        | Note position: `top`, `bottom` (default), or `both`                |
| `--note_format`          | Note format: `legacy` (default, bold paragraph) or `marker`       |
| `--include_model`        | Include the model name in the output file                       |

### Translation note: positions and formats

With `--add_translation_note`, the translator can place the note at the top, bottom, or both, and render it either as plain text (backward-compatible) or as `marker` format consumable by a Markdown plugin.

**Position** (`--note_position`) :

- `bottom` (default): note at the end of the file, as historically.
- `top`: note inserted **after the YAML front matter** (Astro Content Collections safety, gray-matter, etc.).
- `both`: note inserted at the top AND at the bottom (a single LLM call, content reused for both placements).

**Format** (`--note_format`) :

- `legacy` (default): bold paragraph `**...**` — behavior strictly identical to v1.8, byte-for-byte. Compatible with Hugo, GitHub, GitLab, and any Markdown renderer.
- `marker`: invisible Markdown link reference definition (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) followed by a bold blockquote. Natively readable on GitHub/GitLab, and usable at build time by a remark plugin on the Astro side to produce a stylized banner (see jls42.org blog).

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

### Default Models (2026)

| Provider | Quality (default)         | Economy (`--eco`)            |
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **Long-form translation recommendation** : `--use_gemini` (default = `gemini-3.1-pro-preview` quality, `--eco` = `gemini-3.1-flash-lite-preview`) tends to better preserve markdown structure on non-Latin scripts (PL, JA, ZH, AR, HI), especially in `--news` mode where placeholder fidelity matters. OpenAI remains the default for backward compatibility.

## Projects Using This Script

- **[jls42.org](https://jls42.org)** - Multilingual personal blog (15 languages)

## Author

Julien LE SAUX  
Email: contact@jls42.org

## License

GNU GENERAL PUBLIC LICENSE Version 3. See [LICENSE](LICENSE).

**Article translated from fr to en with gpt-5.4-mini.**

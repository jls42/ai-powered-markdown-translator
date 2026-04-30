# AI-Powered Markdown Translator

🌍 [French](README.md) | [English](README-en.md) | [Spanish](README-es.md) | [Chinese](README-zh.md) | [German](README-de.md) | [Japanese](README-ja.md) | [Korean](README-ko.md) | [Arabic](README-ar.md) | [Hindi](README-hi.md) | [Italian](README-it.md) | [Dutch](README-nl.md) | [Polish](README-pl.md) | [Portuguese](README-pt.md) | [Romanian](README-ro.md) | [Swedish](README-sv.md)

Markdown file translator using **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, and **Google Gemini**.

This Python script translates Markdown files from a source language to a target language while preserving formatting, code blocks, and front matter metadata.

## Key Features

- **Multi-Provider**: Support for 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **2026 Models**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Economy Mode**: Option `--eco` to use faster and less expensive models
- **Single File**: Option `--file` to translate a single file
- **Intelligent Segmentation**: Handles long texts with model token limits
- **Code Preservation**: Code blocks AND inline code (`` `...` ``) are preserved
- **Filename**: Option `--keep_filename` to keep the original name
- **News Mode**: Option `--news` to protect English quotes and handle flags in news articles
- **.env Configuration**: Support for the `.env` file for API keys
- **Translation Note**: Optional addition of a note at the end of the document

## Installation

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
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

Active hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexity), detect-secrets (API keys), mypy (progressive typing), Opengrep (SAST), pip-audit (CVE deps), unittest. See section `CLAUDE.md` _Quality / pre-commit_ for details.

## Configuration

Create a `.env` file at the root of the project or define the environment variables:

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

Uses faster and less expensive models (gpt-5.4-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Options

| Option                   | Description                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Single Markdown file to translate                                       |
| `--source_dir`           | Source directory containing Markdown files                                |
| `--target_dir`           | Output directory for translated files                          |
| `--source_lang`          | Source language (default: `fr`)                                             |
| `--target_lang`          | Target language (default: `en`)                                              |
| `--model`                | Specific model to use                                             |
| `--eco`                  | Use economy models                                         |
| `--use_mistral`          | Use the Mistral AI API                                                |
| `--use_claude`           | Use the Claude API                                                    |
| `--use_gemini`           | Use the Gemini API                                                    |
| `--force`                | Force re-translation                                                  |
| `--keep_filename`        | Keep the original filename                                     |
| `--news`                 | News mode: protects EN quotes, handles flags by language |
| `--add_translation_note` | Add a translation note                                           |
| `--include_model`        | Include the model name in the output file                       |

### Default models (2026)

| Provider | Quality (default)         | Economy (`--eco`)     |
| -------- | ------------------------ | ------------------------ |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`           |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5`       |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`   |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3-flash-preview` |

> **Recommendation for long-form translations**: `--use_gemini` (default = `gemini-3.1-pro-preview` quality, `--eco` = `gemini-3-flash-preview`) tends to better preserve Markdown structure on non-Latin scripts (PL, JA, ZH, AR, HI), especially in `--news` mode where placeholder fidelity matters. OpenAI remains the default for backward compatibility.

## Projects using this script

- **[jls42.org](https://jls42.org)** - Multilingual personal blog (15 languages)

## Author

Julien LE SAUX
Email: contact@jls42.org

## License

GNU GENERAL PUBLIC LICENSE Version 3. See [LICENSE](LICENSE).

**This document has been translated from the fr version into the en language using the gpt-5.4-mini model. For more information about the translation process, see https://gitlab.com/jls42/ai-powered-markdown-translator**


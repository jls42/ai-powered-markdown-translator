# AI-Powered Markdown Translator

🌍 [English](README-en.md) | [Spanish](README-es.md) | [Chinese](README-zh.md) | [German](README-de.md) | [Japanese](README-ja.md) | [Korean](README-ko.md) | [Arabic](README-ar.md) | [Hindi](README-hi.md) | [Italian](README-it.md) | [Dutch](README-nl.md) | [Polish](README-pl.md) | [Portuguese](README-pt.md) | [Romanian](README-ro.md) | [Swedish](README-sv.md)

Markdown file translator using **OpenAI**, **Mistral AI**, **Claude (Anthropic)** and **Google Gemini**.

This Python script translates Markdown files from a source language to a target language while preserving formatting, code blocks and front matter metadata.

## Main Features

- **Multi-Provider**: Support for 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **Models 2026**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **Economy Mode**: Option `--eco` to use faster, lower-cost models
- **Single File**: Option `--file` to translate a single file
- **Smart Segmentation**: Handles long texts with model token limits
- **Code Preservation**: Code blocks AND inline code (`` `...` ``) are preserved
- **File Name**: Option `--keep_filename` to keep the original name
- **.env Configuration**: Support for the `.env` file for API keys
- **Translation Note**: Optional addition of a note at the end of the document

## Installation

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Configuration

Create a `.env` file at the project root or set the environment variables:

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
# Avec OpenAI (défaut: gpt-5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### Economy mode

Uses faster, lower-cost models (gpt-5-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Options

| Option | Description |
|--------|-------------|
| `--file` | Single Markdown file to translate |
| `--source_dir` | Source directory containing Markdown files |
| `--target_dir` | Output directory for translated files |
| `--source_lang` | Source language (default: `fr`) |
| `--target_lang` | Target language (default: `en`) |
| `--model` | Specific model to use |
| `--eco` | Use economy models |
| `--use_mistral` | Use the Mistral AI API |
| `--use_claude` | Use the Claude API |
| `--use_gemini` | Use the Gemini API |
| `--force` | Force re-translation |
| `--keep_filename` | Keep the original file name |
| `--add_translation_note` | Add a translation note |
| `--include_model` | Include the model name in the output file |

### Default Models (2026)

| Provider | Quality (default) | Economy (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Projects using this script

- **[jls42.org](https://jls42.org)** - Personal blog translated into 15 languages (364 files, 22 articles + 4 projects)

## Author

Julien LE SAUX
Email: contact@jls42.org

## License

GNU GENERAL PUBLIC LICENSE Version 3. See [LICENSE](LICENSE).

**This document was translated from the fr version into the en language using the gpt-5-mini model. For more information on the translation process, consult https://gitlab.com/jls42/ai-powered-markdown-translator**


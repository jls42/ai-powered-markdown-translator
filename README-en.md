# AI-Powered Markdown Translator

🌍 [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

Markdown file translator using **OpenAI**, **Mistral AI**, **Claude (Anthropic)** and **Google Gemini**.

This Python script translates Markdown files from a source language to a target language while preserving formatting, code blocks, and front matter metadata.

## Key Features

- **Multi-Provider**: Support for 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **2026 Models**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **Economy Mode**: `--eco` option to use faster and cheaper models
- **Single File**: `--file` option to translate a single file
- **Smart Segmentation**: Handles long texts with per-model token limits
- **Code Preservation**: Code blocks are not translated
- **Translation Note**: Optional addition of a note at the end of the document

## Installation

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Configuration

Set the environment variable for the API you want to use:

```bash
export OPENAI_API_KEY='votre-clé-api-openai'
export MISTRAL_API_KEY='votre-clé-api-mistral'
export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
export GOOGLE_API_KEY='votre-clé-api-google'
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

Uses faster and cheaper models (gpt-5-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Options

| Option | Description |
|--------|-------------|
| `--file` | Single Markdown file to translate |
| `--source_dir` | Source directory containing the Markdown files |
| `--target_dir` | Output directory for the translated files |
| `--source_lang` | Source language (default: `fr`) |
| `--target_lang` | Target language (default: `en`) |
| `--model` | Specific model to use |
| `--eco` | Use economy models |
| `--use_mistral` | Use the Mistral AI API |
| `--use_claude` | Use the Claude API |
| `--use_gemini` | Use the Gemini API |
| `--force` | Force re-translation |
| `--add_translation_note` | Add a translation note |

### Default models (2026)

| Provider | Quality (default) | Economy (`--eco`) |
|----------|-------------------|-------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Author

Julien LE SAUX
Email : contact@jls42.org

## License

GNU GENERAL PUBLIC LICENSE Version 3. See [LICENSE](LICENSE).
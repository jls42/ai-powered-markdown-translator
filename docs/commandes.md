# Projet et commandes

## Project Overview

AI-powered Markdown translator that uses OpenAI, Mistral AI, Claude (Anthropic), Google Gemini and Grok (xAI) APIs — or the ChatGPT (Codex), Grok, Google (Antigravity) and Claude (Claude Code) subscription CLIs, with no per-use billing — or OpenCode, the open-source agent, routed to whatever provider the user configured in OpenCode (local model, free gateway, subscription or key) — or OpenRouter, a paid router to ~430 hosted models — to translate Markdown files while preserving formatting, code blocks, and front matter metadata.

## Commands

### Run a translation

```bash
# Activate virtual environment first
source venv/bin/activate

# Translate a single file
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'

# Translate a directory with OpenAI (default: gpt-5.6-terra)
aipmt --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Use economic models (--eco): gpt-5.6-luna, claude-haiku-5-5, gemini-3.1-flash-lite
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'

# Translate with Mistral AI
aipmt --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Translate with Claude
aipmt --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Translate with Gemini
aipmt --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Force retranslation of existing files
aipmt --force --source_dir 'content/fr' --target_dir 'content/en'

# Add translation note at end of document
aipmt --add_translation_note --source_dir 'content/fr' --target_dir 'content/en'

# News mode: protect EN quotes, manage flags per language
aipmt --news --file 'article.md' --target_dir 'output/' --target_lang 'es'
```

### Install dependencies

```bash
pip install -r requirements.txt
```

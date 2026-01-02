# KI-gestützter Markdown-Übersetzer

🌍 [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

Übersetzer für Markdown-Dateien unter Verwendung von **OpenAI**, **Mistral AI**, **Claude (Anthropic)** und **Google Gemini**.

Dieses Python-Skript übersetzt Markdown-Dateien von einer Ausgangssprache in eine Zielsprache, wobei Formatierung, Codeblöcke und Front-Matter-Metadaten erhalten bleiben.

## Hauptfunktionen

- **Multi-Provider**: Unterstützung für 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **Modelle 2026**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **Sparmodus**: Option `--eco`, um schnellere und kostengünstigere Modelle zu verwenden
- **Einzeldatei**: Option `--file`, um eine einzelne Datei zu übersetzen
- **Intelligente Segmentierung**: Handhabung langer Texte mit Token-Grenzen pro Modell
- **Code-Beibehaltung**: Codeblöcke werden nicht übersetzt
- **Übersetzungshinweis**: Optionaler Hinweis am Ende des Dokuments

## Installation

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Konfiguration

Legen Sie die Umgebungsvariable für die API fest, die Sie verwenden möchten :

```bash
export OPENAI_API_KEY='votre-clé-api-openai'
export MISTRAL_API_KEY='votre-clé-api-mistral'
export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
export GOOGLE_API_KEY='votre-clé-api-google'
```

## Verwendung

### Eine einzelne Datei übersetzen

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Ein Verzeichnis übersetzen

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

### Sparmodus

Verwendet schnellere und kostengünstigere Modelle (gpt-5-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Optionen

| Option | Beschreibung |
|--------|--------------|
| `--file` | Einzelne zu übersetzende Markdown-Datei |
| `--source_dir` | Quellverzeichnis mit den Markdown-Dateien |
| `--target_dir` | Ausgabeverzeichnis für die übersetzten Dateien |
| `--source_lang` | Ausgangssprache (Standard: `fr`) |
| `--target_lang` | Zielsprache (Standard: `en`) |
| `--model` | Zu verwendendes spezifisches Modell |
| `--eco` | Kostengünstige Modelle verwenden |
| `--use_mistral` | Mistral-AI-API verwenden |
| `--use_claude` | Claude-API verwenden |
| `--use_gemini` | Gemini-API verwenden |
| `--force` | Neuübersetzung erzwingen |
| `--add_translation_note` | Übersetzungshinweis hinzufügen |

### Standardmodelle (2026)

| Provider | Qualität (Standard) | Kostengünstig (`--eco`) |
|----------|---------------------|-------------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Autor

Julien LE SAUX
E-Mail : contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](LICENSE).
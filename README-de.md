# KI-gestützter Markdown-Übersetzer

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

Markdown-Datei-Übersetzer mit **OpenAI**, **Mistral AI**, **Claude (Anthropic)** und **Google Gemini**.

Dieses Python-Skript übersetzt Markdown-Dateien von einer Quellsprache in eine Zielsprache und bewahrt dabei Formatierung, Codeblöcke und Front-Matter-Metadaten.

## Hauptmerkmale

- **Multi-Anbieter**: Unterstützung von 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **Modelle 2026**: GPT-5.4, Claude Sonnet 4.5, Gemini 3.1 Pro
- **Sparmodus**: Option `--eco` zur Verwendung schnellerer und kostengünstigerer Modelle
- **Einzeldatei**: Option `--file` zum Übersetzen einer einzelnen Datei
- **Intelligente Segmentierung**: Verarbeitung langer Texte mit modellabhängigen Token-Grenzen
- **Code-Erhaltung**: Codeblöcke UND Inline-Code (`` `...` ``) werden beibehalten
- **Dateiname**: Option `--keep_filename` zum Beibehalten des Originalnamens
- **News-Modus**: Option `--news` zum Schutz englischer Zitate und zur Handhabung von Flaggen in Nachrichtenartikeln
- **.env-Konfiguration**: Unterstützung der Datei `.env` für API-Schlüssel
- **Übersetzerhinweis**: Optionaler Hinweis am Ende des Dokuments

## Installation

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Konfiguration

Erstellen Sie eine Datei `.env` im Stammverzeichnis des Projekts oder definieren Sie die Umgebungsvariablen:

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

## Verwendung

### Eine einzelne Datei übersetzen

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Ein Verzeichnis übersetzen

```bash
# Avec OpenAI (défaut: gpt-5.4)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### Sparmodus

Verwendet schnellere und kostengünstigere Modelle (gpt-5-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Optionen

| Option | Beschreibung |
|--------|-------------|
| `--file` | Einzelne Markdown-Datei zum Übersetzen |
| `--source_dir` | Quellverzeichnis mit den Markdown-Dateien |
| `--target_dir` | Ausgabeverzeichnis für die übersetzten Dateien |
| `--source_lang` | Quellsprache (Standard: `fr`) |
| `--target_lang` | Zielsprache (Standard: `en`) |
| `--model` | Zu verwendendes spezifisches Modell |
| `--eco` | Sparmodelle verwenden |
| `--use_mistral` | Mistral-AI-API verwenden |
| `--use_claude` | Claude-API verwenden |
| `--use_gemini` | Gemini-API verwenden |
| `--force` | Neuübersetzung erzwingen |
| `--keep_filename` | Den ursprünglichen Dateinamen beibehalten |
| `--news` | Nachrichtenmodus: schützt EN-Zitate, verwaltet Flaggen nach Sprache |
| `--add_translation_note` | Einen Übersetzerhinweis hinzufügen |
| `--include_model` | Den Modellnamen in die Ausgabedatei aufnehmen |

### Standardmodelle (2026)

| Anbieter | Qualität (Standard) | Sparmodus (`--eco`) |
|----------|---------------------|----------------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** - Mehrsprachiger persönlicher Blog (15 Sprachen)

## Autor

Julien LE SAUX
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](LICENSE).
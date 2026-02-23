# Markdown-Übersetzer mit KI-Unterstützung

🌍 [Französisch](README.md) | [Englisch](README-en.md) | [Spanisch](README-es.md) | [Chinesisch](README-zh.md) | [Deutsch](README-de.md) | [Japanisch](README-ja.md) | [Koreanisch](README-ko.md) | [Arabisch](README-ar.md) | [Hindi](README-hi.md) | [Italienisch](README-it.md) | [Niederländisch](README-nl.md) | [Polnisch](README-pl.md) | [Portugiesisch](README-pt.md) | [Rumänisch](README-ro.md) | [Schwedisch](README-sv.md)

Übersetzer für Markdown-Dateien, der **OpenAI**, **Mistral AI**, **Claude (Anthropic)** und **Google Gemini** verwendet.

Dieses Python-Skript übersetzt Markdown-Dateien von einer Quellsprache in eine Zielsprache und bewahrt dabei Formatierung, Codeblöcke und Front-Matter-Metadaten.

## Hauptmerkmale

- **Multi-Provider**: Unterstützung für 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **Modelle 2026**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **Sparmodus**: Option `--eco` zur Verwendung schnellerer und kostengünstigerer Modelle
- **Einzeldatei**: Option `--file` zum Übersetzen einer einzelnen Datei
- **Intelligente Segmentierung**: Verwaltung langer Texte mit Token-Limits pro Modell
- **Code-Erhaltung**: Codeblöcke UND Inline-Code (`` `...` ``) werden beibehalten
- **Dateiname**: Option `--keep_filename` zum Beibehalten des Originalnamens
- **News-Modus**: Option `--news` zum Schutz englischer Zitate und zur Verwaltung von Flaggen in Nachrichtenartikeln
- **.env-Konfiguration**: Unterstützung der Datei `.env` für API-Schlüssel
- **Übersetzungsnotiz**: Optionale Ergänzung einer Anmerkung am Ende des Dokuments

## Installation

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Konfiguration

Erstellen Sie eine Datei `.env` im Projektstamm oder setzen Sie die Umgebungsvariablen:

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

Verwendet schnellere und kostengünstigere Modelle (gpt-5-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Optionen

| Option | Beschreibung |
|--------|-------------|
| `--file` | Einzelne Markdown-Datei zum Übersetzen |
| `--source_dir` | Quellverzeichnis mit Markdown-Dateien |
| `--target_dir` | Ausgabeverzeichnis für die übersetzten Dateien |
| `--source_lang` | Quellsprache (Standard: `fr`) |
| `--target_lang` | Zielsprache (Standard: `en`) |
| `--model` | Bestimmtes Modell verwenden |
| `--eco` | Wirtschaftliche Modelle verwenden |
| `--use_mistral` | Mistral AI API verwenden |
| `--use_claude` | Claude API verwenden |
| `--use_gemini` | Gemini API verwenden |
| `--force` | Übersetzung erzwingen (erneut übersetzen) |
| `--keep_filename` | Originalen Dateinamen beibehalten |
| `--news` | Nachrichtenmodus: schützt englische Zitate, verwaltet Flaggen pro Sprache |
| `--add_translation_note` | Übersetzungsnotiz hinzufügen |
| `--include_model` | Modellnamen in der Ausgabedatei einfügen |

### Standardmodelle (2026)

| Anbieter | Qualität (Standard) | Wirtschaftlich (`--eco`) |
|----------|---------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** - Persönlicher mehrsprachiger Blog (15 Sprachen)

## Autor

Julien LE SAUX  
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LIZENZ](LICENSE).

**Dieses Dokument wurde aus der französischen Version (fr) ins Englische (en) mithilfe des Modells gpt-5-mini übersetzt. Für weitere Informationen zum Übersetzungsprozess siehe https://gitlab.com/jls42/ai-powered-markdown-translator**


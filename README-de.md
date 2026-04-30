# KI-gestützter Markdown-Übersetzer

🌍 [Französisch](README.md) | [Englisch](README-en.md) | [Spanisch](README-es.md) | [Chinesisch](README-zh.md) | [Deutsch](README-de.md) | [Japanisch](README-ja.md) | [Koreanisch](README-ko.md) | [Arabisch](README-ar.md) | [Hindi](README-hi.md) | [Italienisch](README-it.md) | [Niederländisch](README-nl.md) | [Polnisch](README-pl.md) | [Portugiesisch](README-pt.md) | [Rumänisch](README-ro.md) | [Schwedisch](README-sv.md)

Markdown-Dateiübersetzer mit **OpenAI**, **Mistral AI**, **Claude (Anthropic)** und **Google Gemini**.

Dieses Python-Skript übersetzt Markdown-Dateien von einer Quellsprache in eine Zielsprache und bewahrt dabei die Formatierung, Codeblöcke und Front-Matter-Metadaten.

## Hauptmerkmale

- **Mehrere Anbieter**: Unterstützung für 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **Modelle 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Sparmodus**: Option `--eco`, um schnellere und kostengünstigere Modelle zu verwenden
- **Einzeldatei**: Option `--file`, um eine einzelne Datei zu übersetzen
- **Intelligente Segmentierung**: Verarbeitung langer Texte mit modellspezifischen Token-Grenzen
- **Code-Erhaltung**: Codeblöcke UND Inline-Code (`` `...` ``) bleiben erhalten
- **Dateiname**: Option `--keep_filename`, um den ursprünglichen Namen beizubehalten
- **News-Modus**: Option `--news`, um englische Zitate zu schützen und Flaggen in Nachrichtenartikeln zu behandeln
- **.env-Konfiguration**: Unterstützung der Datei `.env` für API-Schlüssel
- **Übersetzungsnotiz**: Optionale Hinzufügung einer Notiz am Ende des Dokuments

## Installation

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Qualitätswerkzeuge (optional, aber empfohlen)

Das Projekt verwendet [`pre-commit`](https://pre-commit.com), um zu verhindern, dass schlecht formatiierter, unsicherer oder geheimnisbehafteter Code committet wird. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktive Hooks: ruff (Linting+Formatierung), shellcheck (bash), prettier (markdown/yaml/json), Lizard (Komplexität), detect-secrets (API-Schlüssel), mypy (schrittweise Typisierung), Opengrep (SAST), pip-audit (CVE-Abhängigkeiten), unittest. Siehe Abschnitt `CLAUDE.md` _Quality / pre-commit_ für Details.

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
# Avec OpenAI (défaut: gpt-5.5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### Sparmodus

Verwendet schnellere und kostengünstigere Modelle (gpt-5.4-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Optionen

| Option                   | Beschreibung                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Einzige zu übersetzende Markdown-Datei                                   |
| `--source_dir`           | Quellverzeichnis mit den Markdown-Dateien                                |
| `--target_dir`           | Ausgabeverzeichnis für die übersetzten Dateien                           |
| `--source_lang`          | Quellsprache (Standard: `fr`)                                             |
| `--target_lang`          | Zielsprache (Standard: `en`)                                              |
| `--model`                | Zu verwendendes spezifisches Modell                                        |
| `--eco`                  | Sparmodelle verwenden                                                  |
| `--use_mistral`          | Die Mistral-AI-API verwenden                                               |
| `--use_claude`           | Die Claude-API verwenden                                                   |
| `--use_gemini`           | Die Gemini-API verwenden                                                   |
| `--force`                | Neuerliche Übersetzung erzwingen                                           |
| `--keep_filename`        | Den ursprünglichen Dateinamen beibehalten                                  |
| `--news`                 | Nachrichtenmodus: schützt EN-Zitate, behandelt Flaggen nach Sprache |
| `--add_translation_note` | Übersetzungsnotiz hinzufügen                                           |
| `--include_model`        | Den Modellnamen in die Ausgabedatei aufnehmen                       |

### Standardmodelle (2026)

| Anbieter | Qualität (Standard)         | Sparmodus (`--eco`)     |
| -------- | ------------------------ | ------------------------ |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`           |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5`       |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`   |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3-flash-preview` |

> **Empfehlung für Long-Form-Übersetzungen**: `--use_gemini` (Standard = `gemini-3.1-pro-preview` Qualität, `--eco` = `gemini-3-flash-preview`) bewahrt die Markdown-Struktur bei nicht-lateinischen Skripten (PL, JA, ZH, AR, HI) tendenziell besser, insbesondere im `--news`-Modus, in dem die Treue der Platzhalter zählt. OpenAI bleibt aus Gründen der Abwärtskompatibilität der Standardwert.

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** - Mehrsprachiger persönlicher Blog (15 Sprachen)

## Autor

Julien LE SAUX
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](LICENSE).

**Dieses Dokument wurde von der Version fr in die Sprache de unter Verwendung des Modells gpt-5.4-mini übersetzt. Für weitere Informationen über den Übersetzungsprozess besuchen Sie https://github.com/jls42/ai-powered-markdown-translator**

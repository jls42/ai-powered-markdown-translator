# KI-gestützter Markdown-Übersetzer

🌍 [Französisch](README.md) | [Englisch](README-en.md) | [Spanisch](README-es.md) | [Chinesisch](README-zh.md) | [Deutsch](README-de.md) | [Japanisch](README-ja.md) | [Koreanisch](README-ko.md) | [Arabisch](README-ar.md) | [Hindi](README-hi.md) | [Italienisch](README-it.md) | [Niederländisch](README-nl.md) | [Polnisch](README-pl.md) | [Portugiesisch](README-pt.md) | [Rumänisch](README-ro.md) | [Schwedisch](README-sv.md)

<h4 align="center">📊 Codequalität</h4>

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

Markdown-Datei-Übersetzer, der **OpenAI**, **Mistral AI**, **Claude (Anthropic)** und **Google Gemini** verwendet.

Dieses Python-Skript übersetzt Markdown-Dateien von einer Quellsprache in eine Zielsprache und bewahrt dabei die Formatierung, Codeblöcke und die Front-Matter-Metadaten.

## Hauptmerkmale

- **Multi-Provider**: Unterstützung für 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **Modelle 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Sparmodus**: Option `--eco` zur Verwendung schnellerer und kostengünstigerer Modelle
- **Einzeldatei**: Option `--file`, um nur eine einzelne Datei zu übersetzen
- **Intelligente Segmentierung**: Verarbeitung langer Texte mit tokenbasierten Modellgrenzen
- **Code-Erhaltung**: Codeblöcke UND Inline-Code (`` `...` ``) werden beibehalten
- **Dateiname**: Option `--keep_filename`, um den ursprünglichen Namen beizubehalten
- **News-Modus**: Option `--news`, um englische Anführungszeichen zu schützen und Flaggen in Nachrichtenartikeln zu verarbeiten
- **.env-Konfiguration**: Unterstützung der Datei `.env` für API-Schlüssel
- **Übersetzungshinweis**: Optionales Hinzufügen eines Hinweises am Ende des Dokuments

## Installation

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Qualitätstools (optional, aber empfohlen)

Das Projekt verwendet [`pre-commit`](https://pre-commit.com), um zu verhindern, dass schlecht formatierter, unsicherer oder geheime Daten enthaltender Code eingecheckt wird. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktive Hooks: ruff (Linting+Formatierung), shellcheck (bash), prettier (markdown/yaml/json), Lizard (Komplexität), detect-secrets (API-Schlüssel), mypy (schrittweise Typisierung), Opengrep (SAST), pip-audit (CVE-Dependencies), unittest. Siehe Abschnitt `CLAUDE.md` _Quality / pre-commit_ für Details.

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
| `--file`                 | Einzelne zu übersetzende Markdown-Datei                                  |
| `--source_dir`           | Quellverzeichnis mit den Markdown-Dateien                                |
| `--target_dir`           | Ausgabeverzeichnis für die übersetzten Dateien                           |
| `--source_lang`          | Quellsprache (Standard: `fr`)                                             |
| `--target_lang`          | Zielsprache (Standard: `en`)                                              |
| `--model`                | Zu verwendendes spezifisches Modell                                      |
| `--eco`                  | Wirtschaftliche Modelle verwenden                                         |
| `--use_mistral`          | Die Mistral-AI-API verwenden                                              |
| `--use_claude`           | Die Claude-API verwenden                                                  |
| `--use_gemini`           | Die Gemini-API verwenden                                                  |
| `--force`                | Neuübersetzung erzwingen                                                  |
| `--keep_filename`        | Ursprünglichen Dateinamen beibehalten                                     |
| `--news`                 | Nachrichtenmodus: schützt EN-Zitate, verarbeitet Flaggen nach Sprache     |
| `--add_translation_note` | Einen Übersetzungshinweis hinzufügen                                        |
| `--include_model`        | Den Modellnamen in der Ausgabedatei einfügen                               |

### Standardmodelle (2026)

| Anbieter | Qualität (Standard)         | Wirtschaftlich (`--eco`)            |
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **Empfehlung für Langform-Übersetzungen**: `--use_gemini` (Standard = `gemini-3.1-pro-preview` Qualität, `--eco` = `gemini-3.1-flash-lite-preview`) bewahrt die Markdown-Struktur bei nicht-lateinischen Skripten (PL, JA, ZH, AR, HI) tendenziell besser, insbesondere im `--news`-Modus, in dem die Genauigkeit der Platzhalter zählt. OpenAI bleibt aus Gründen der Rückwärtskompatibilität der Standardwert.

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** - Mehrsprachiger persönlicher Blog (15 Sprachen)

## Autor

Julien LE SAUX
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](LICENSE).

**Dieses Dokument wurde von der Version fr in die Sprache de unter Verwendung des Modells gpt-5.4-mini übersetzt. Für weitere Informationen zum Übersetzungsprozess besuchen Sie https://github.com/jls42/ai-powered-markdown-translator**

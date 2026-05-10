# KI-gestützter Markdown-Übersetzer

🌍 [Französisch](README.md) | [Englisch](README-en.md) | [Spanisch](README-es.md) | [Chinesisch](README-zh.md) | [Deutsch](README-de.md) | [Japanisch](README-ja.md) | [Koreanisch](README-ko.md) | [Arabisch](README-ar.md) | [Hindi](README-hi.md) | [Italienisch](README-it.md) | [Niederländisch](README-nl.md) | [Polnisch](README-pl.md) | [Portugiesisch](README-pt.md) | [Rumänisch](README-ro.md) | [Schwedisch](README-sv.md)

<h4 align="center">📊 Codequalität</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status des Qualitäts-Gates"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Sicherheitsbewertung"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Zuverlässigkeitsbewertung"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Wartbarkeitsbewertung"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Abdeckung"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Schwachstellen"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Fehler"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Doppelte Zeilen (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Technische Schuld"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Codezeilen"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy Badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Markdown-Datei-Übersetzer mit **OpenAI**, **Mistral AI**, **Claude (Anthropic)** und **Google Gemini**.

Dieses Python-Skript übersetzt Markdown-Dateien von einer Quellsprache in eine Zielsprache und bewahrt dabei die Formatierung, Codeblöcke und Front-matter-Metadaten.

## Hauptmerkmale

- **Multi-Provider**: Unterstützung von 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **Modelle 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Sparmodus**: Option `--eco`, um schnellere und kostengünstigere Modelle zu verwenden
- **Einzeldatei**: Option `--file`, um eine einzelne Datei zu übersetzen
- **Intelligente Segmentierung**: Verwaltung langer Texte mit Token-Grenzen pro Modell
- **Code-Erhaltung**: Die Codeblöcke UND der Inline-Code (`` `...` ``) werden beibehalten
- **Dateiname**: Option `--keep_filename`, um den ursprünglichen Namen beizubehalten
- **Nachrichtenmodus**: Option `--news`, um englische Zitate zu schützen und Flaggen in Nachrichtenartikeln zu verwalten
- **.env-Konfiguration**: Unterstützung der Datei `.env` für API-Schlüssel
- **Übersetzungsnotiz**: Optionale Hinzufügung einer Notiz am Ende des Dokuments

## Installation

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Qualitäts-Tooling (optional, aber empfohlen)

Das Projekt verwendet [`pre-commit`](https://pre-commit.com), um zu verhindern, dass schlecht formatierter, verwundbarer oder geheime Informationen enthaltender Code committet wird. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktive Hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (Komplexität), detect-secrets (API-Schlüssel), mypy (schrittweise Typisierung), Opengrep (SAST), pip-audit (CVE-Abhängigkeiten), unittest. Siehe Abschnitt `CLAUDE.md` _Qualität / pre-commit_ für Details.

## Konfiguration

Erstellen Sie eine Datei `.env` im Projektstamm oder definieren Sie die Umgebungsvariablen:

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
| `--file`                 | Einzige Markdown-Datei, die übersetzt werden soll                        |
| `--source_dir`           | Quellverzeichnis mit den Markdown-Dateien                                |
| `--target_dir`           | Ausgabeverzeichnis für die übersetzten Dateien                           |
| `--source_lang`          | Quellsprache (Standard: `fr`)                                             |
| `--target_lang`          | Zielsprache (Standard: `en`)                                              |
| `--model`                | Spezifisches zu verwendendes Modell                                     |
| `--eco`                  | Sparmodelle verwenden                                                   |
| `--use_mistral`          | Die Mistral-AI-API verwenden                                             |
| `--use_claude`           | Die Claude-API verwenden                                                 |
| `--use_gemini`           | Die Gemini-API verwenden                                                 |
| `--force`                | Erneute Übersetzung erzwingen                                            |
| `--keep_filename`        | Ursprünglichen Dateinamen beibehalten                                    |
| `--news`                 | Nachrichtenmodus: schützt EN-Zitate, behandelt Flaggen je Sprache       |
| `--add_translation_note` | Übersetzungsnotiz hinzufügen                                           |
| `--note_position`        | Position der Notiz: `top`, `bottom` (Standard) oder `both`                |
| `--note_format`          | Format der Notiz: `legacy` (Standard, fetter Absatz) oder `marker`       |
| `--include_model`        | Den Modellnamen in die Ausgabedatei aufnehmen                            |

### Übersetzungsnotiz: Positionen und Formate

Mit `--add_translation_note` kann der Übersetzer die Notiz oben, unten oder an beiden Stellen platzieren und sie entweder als einfachen Text (rückwärtskompatibel) oder als von einem Markdown-Plugin verarbeitbares `marker`-Format darstellen.

**Position** (`--note_position`) :

- `bottom` (Standard): Notiz am Dateiende, wie historisch üblich.
- `top` : Notiz, die **nach dem YAML-Frontmatter** eingefügt wird (Sicherheit für Astro Content Collections, gray-matter usw.).
- `both` : Notiz oben UND unten eingefügt (ein einziger LLM-Aufruf, Inhalt wird für beide Platzierungen wiederverwendet).

**Format** (`--note_format`) :

- `legacy` (Standard): fetter Absatz `**...**` — Verhalten strikt identisch zu v1.8, Byte für Byte. Kompatibel mit Hugo, GitHub, GitLab und jedem Markdown-Renderer.
- `marker` : unsichtbare Markdown-Link-Referenzdefinition (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) gefolgt von einem fett gesetzten Blockquote. Nativ auf GitHub/GitLab lesbar und beim Build durch ein remark-Plugin in Astro nutzbar, um ein stilisiertes Banner zu erzeugen (siehe Blog jls42.org).

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

### Standardmodelle (2026)

| Provider | Qualität (Standard)         | Sparmodus (`--eco`)            |
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **Empfehlung für Long-Form-Übersetzungen**: `--use_gemini` (Standard = `gemini-3.1-pro-preview` Qualität, `--eco` = `gemini-3.1-flash-lite-preview`) tendiert dazu, die Markdown-Struktur bei nicht-lateinischen Skripten (PL, JA, ZH, AR, HI) besser zu bewahren, insbesondere im `--news`-Modus, in dem es auf die Treue der Platzhalter ankommt. OpenAI bleibt aus Gründen der Rückwärtskompatibilität die Standardoption.

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** - Mehrsprachiger persönlicher Blog (15 Sprachen)

## Autor

Julien LE SAUX  
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](LICENSE).

**Artikel übersetzt vom FR ins DE mit gpt-5.4-mini.**

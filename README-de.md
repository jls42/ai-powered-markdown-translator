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

Markdown-Dateiübersetzer mit **OpenAI**, **Mistral AI**, **Claude (Anthropic)** und **Google Gemini**.

Dieses Python-Skript übersetzt Markdown-Dateien von einer Quellsprache in eine Zielsprache, wobei Formatierung, Codeblöcke und Front-Matter-Metadaten erhalten bleiben.

## Hauptmerkmale

- **Multi-Provider**: Unterstützung von 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **Modelle 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Sparmodus**: Option `--eco` zur Verwendung schnellerer und günstigerer Modelle
- **Einzeldatei**: Option `--file`, um eine einzelne Datei zu übersetzen
- **Intelligente Segmentierung**: Verarbeitung langer Texte mit modellabhängigen Token-Grenzen
- **Code-Erhaltung**: Die Codeblöcke UND der Inline-Code (`` `...` ``) bleiben erhalten
- **Dateiname**: Option `--keep_filename`, um den ursprünglichen Namen beizubehalten
- **News-Modus**: Option `--news`, um englische Zitate zu schützen und Flaggen in Nachrichtenartikeln zu behandeln
- **.env-Konfiguration**: Unterstützung der Datei `.env` für API-Schlüssel
- **Übersetzungshinweis**: Optionales Hinzufügen eines Hinweises am Ende des Dokuments

## Installation

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Qualitäts-Tooling (optional, aber empfohlen)

Das Projekt verwendet [`pre-commit`](https://pre-commit.com), um zu verhindern, dass schlecht formatierter, verwundbarer oder geheimhaltiger Code committet wird. Installation:

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

Verwendet schnellere und günstigere Modelle (gpt-5.4-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Optionen

| Option                   | Beschreibung                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Einzelne Markdown-Datei zum Übersetzen                                   |
| `--source_dir`           | Quellverzeichnis mit den Markdown-Dateien                                |
| `--target_dir`           | Ausgabeverzeichnis für die übersetzten Dateien                           |
| `--source_lang`          | Quellsprache (Standard: `fr`)                                             |
| `--target_lang`          | Zielsprache (Standard: `en`)                                              |
| `--model`                | Spezifisches zu verwendendes Modell                                      |
| `--eco`                  | Sparmodelle verwenden                                                  |
| `--use_mistral`          | Mistral-AI-API verwenden                                               |
| `--use_claude`           | Claude-API verwenden                                                    |
| `--use_gemini`           | Gemini-API verwenden                                                    |
| `--force`                | Neuübersetzung erzwingen                                                |
| `--keep_filename`        | Ursprünglichen Dateinamen beibehalten                                    |
| `--news`                 | Nachrichtenmodus: schützt EN-Zitate, behandelt Flaggen nach Sprache      |
| `--add_translation_note` | Übersetzungshinweis hinzufügen                                           |
| `--note_position`        | Position des Hinweises: `top`, `bottom` (Standard) oder `both`                |
| `--note_format`          | Format des Hinweises: `legacy` (Standard, fetter Absatz) oder `marker`       |
| `--include_model`        | Modellnamen in der Ausgabedatei einfügen                                  |

### Übersetzungshinweis: Positionen und Formate

Mit `--add_translation_note` kann der Übersetzer den Hinweis oben, unten oder an beiden Stellen platzieren und ihn entweder im einfachen Textformat (rückwärtskompatibel) oder im von einem Markdown-Plugin verarbeitbaren `marker`-Format ausgeben.

**Position** (`--note_position`) :

- `bottom` (Standard): Hinweis am Dateiende, wie historisch üblich.
- `top` : Hinweis **nach dem YAML-Frontmatter** eingefügt (Sicherheit für Astro Content Collections, gray-matter usw.).
- `both` : Hinweis oben UND unten eingefügt (ein einziger LLM-Aufruf, Inhalt für beide Platzierungen wiederverwendet).

**Format** (`--note_format`) :

- `legacy` (Standard): fett gedruckter Absatz `**...**` — strikt identisches Verhalten wie v1.8, bytegenau. Kompatibel mit Hugo, GitHub, GitLab und jedem Markdown-Renderer.
- `marker` : unsichtbare Markdown-Link-Referenzdefinition `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`, gefolgt von einem fett gedruckten Blockzitat. Nativ auf GitHub/GitLab lesbar und beim Build durch ein remark-Plugin auf Astro-Seite nutzbar, um ein stilisiertes Banner zu erzeugen (vgl. Blog jls42.org).

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

| Anbieter | Qualität (Standard)         | Sparmodus (`--eco`)            |
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **Empfehlung für Long-Form-Übersetzungen**: `--use_gemini` (Standard = `gemini-3.1-pro-preview` Qualität, `--eco` = `gemini-3.1-flash-lite-preview`) bewahrt die Markdown-Struktur bei nicht-lateinischen Skripten (PL, JA, ZH, AR, HI) tendenziell besser, insbesondere im `--news`-Modus, in dem die Genauigkeit der Platzhalter wichtig ist. OpenAI bleibt aus Gründen der Rückwärtskompatibilität die Standardwahl.

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** - Mehrsprachiger persönlicher Blog (15 Sprachen)

## Autor

Julien LE SAUX  
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](LICENSE).

**Übersetzter Artikel vom Fr ins De mit gpt-5.4-mini.**

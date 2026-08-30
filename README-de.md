# AI-gestützter Markdown-Übersetzer

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

<h4 align="center">📊 Codequalität</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status des Quality Gates"></a>
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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Duplizierte Zeilen (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Technische Schulden"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Codezeilen"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy-Badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Übersetzer für Markdown-Dateien unter Verwendung von **OpenAI**, **Mistral AI**, **Claude (Anthropic)** und **Google Gemini**.

Dieses Python-Skript übersetzt Markdown-Dateien aus einer Ausgangssprache in eine Zielsprache und bewahrt dabei Formatierung, Codeblöcke und Front-Matter-Metadaten.

## Hauptmerkmale

- **Multi-Provider**: Unterstützung für 4 APIs (OpenAI, Mistral, Claude, Gemini) sowie das Codex CLI über ein ChatGPT-Abonnement
- **Modelle 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Sparmodus**: Option `--eco` zur Verwendung schnellerer und kostengünstigerer Modelle
- **Einzeldatei**: Option `--file` zum Übersetzen einer einzelnen Datei
- **Intelligente Segmentierung**: Verarbeitung langer Texte unter Berücksichtigung der Token-Limits jedes Modells
- **Bewahrung von Code**: Codeblöcke UND Inline-Code (`` `...` ``) bleiben erhalten
- **Dateiname**: Option `--keep_filename` zum Beibehalten des ursprünglichen Namens
- **News-Modus**: Option `--news` zum Schutz englischer Zitate und zur Verarbeitung von Flaggen in Nachrichtenartikeln
- **.env-Konfiguration**: Unterstützung der Datei `.env` für API-Schlüssel
- **Übersetzungshinweis**: Optionales Hinzufügen eines Hinweises am Ende des Dokuments

## Installation

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Qualitätswerkzeuge (optional, aber empfohlen)

Das Projekt verwendet [`pre-commit`](https://pre-commit.com), um zu verhindern, dass schlecht formatierter, anfälliger oder ein Geheimnis enthaltender Code committet wird. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktive Hooks: ruff (Linting und Formatierung), shellcheck (bash), prettier (markdown/yaml/json), Lizard (Komplexität), detect-secrets (API-Schlüssel), mypy (schrittweise Typisierung), Opengrep (SAST), pip-audit (CVE-Abhängigkeiten), unittest. Einzelheiten finden Sie in `CLAUDE.md` im Abschnitt _Quality / pre-commit_.

## Konfiguration

Erstellen Sie eine Datei `.env` im Stammverzeichnis des Projekts oder definieren Sie die Umgebungsvariablen:

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

`GEMINI_API_KEY` wird als Alternative zu `GOOGLE_API_KEY` akzeptiert (AI-Studio-Konvention). Optionale Variablen: `XAI_BASE_URL` (xAI-Endpunkt, Standard
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (Sekunden pro Anthropic-Aufruf, Standard
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`
und `GROK_TRANSLATE_SANDBOX` (siehe Abschnitt Grok CLI). Für
`regen_translations.sh`: `REGEN_PROVIDER`, `REGEN_MODEL` und
`REGEN_JOB_TIMEOUT` (Obergrenze pro Job, Standard 600 s).

## Verwendung

### Eine einzelne Datei übersetzen

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Ein Verzeichnis übersetzen

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
python translate.py --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
python translate.py --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
python translate.py --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'
```

### Über das eigene ChatGPT-Abonnement übersetzen (`--use_codex`)

Dieser Provider benötigt keinen API-Schlüssel: Er steuert das offizielle Codex CLI im
nicht interaktiven Modus, sodass die Übersetzung auf das Kontingent des bereits
bezahlten ChatGPT-Abonnements (Plus, Pro, Business …) angerechnet wird. Dies ist der
einzige von OpenAI dokumentierte Weg für diese Nutzung — die Tokens von
`~/.codex/auth.json` authentifizieren keine Aufrufe der API Platform und werden von
diesem Skript ohnehin niemals gelesen.

**Voraussetzungen:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Die Binärdatei wird in dieser Reihenfolge gesucht: die Variable `CODEX_BIN`, der `PATH`
und anschließend das Python-Paket `openai-codex-cli-bin`. Letzteres ist bewusst
nicht in `requirements.txt` enthalten: Es ist etwa 250 MB groß, was allen
Benutzern für einen optionalen Provider auferlegt würde.

**Wissenswertes:**

- **Es wird kein API-Schlüssel verwendet.** `OPENAI_API_KEY` und `CODEX_API_KEY` werden
  aus der Umgebung des Unterprozesses entfernt. Dadurch wird sichergestellt, dass ein in
  `.env` vorhandener Schlüssel niemals dazu führt, dass die Übersetzung nutzungsabhängig
  abgerechnet wird.
- **Ein Segment = eine „lokale Nachricht“** im 5-Stunden-Fenster des Tarifs.
  Verwenden Sie `--eco` (Modell `gpt-5.6-luna`, 250–2.000 Nachrichten/5 h bei Plus)
  anstelle des Qualitätsmodells (`gpt-5.6-sol`, 10–100 Nachrichten/5 h).
- **Langsamer** als ein API-Aufruf: Für eine vollständige README sind etwa 45 s
  einzuplanen, gegenüber wenigen Sekunden bei einem direkten Aufruf.
- **In CI abgelehnt** (wenn `CI` oder `GITHUB_ACTIONS` definiert ist): Die
  Abonnementauthentifizierung ist nicht für einen gemeinsam genutzten Runner vorgesehen,
  und OpenAI rät von diesem Workflow in öffentlichen Repositories ab. Verwenden Sie für
  diesen Weg einen API-Schlüssel.
- Umgebungsvariablen: `CODEX_BIN` (expliziter Pfad zur Binärdatei) und
  `CODEX_TIMEOUT` (Sekunden pro Segment, Standard `600`).

### Über das eigene Grok-Abonnement übersetzen (`--use_grok_cli`)

Dasselbe Prinzip wie bei `--use_codex`, mit dem offiziellen CLI **Grok Build**: Die
Übersetzung wird auf das Grok-Abonnement (SuperGrok / X Premium+) angerechnet,
anstatt pro Token abgerechnet zu werden.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Isolation — vor der Verwendung lesen.** Dieser Provider ist strukturell
**schwächer** als `--use_codex`, und das ist beabsichtigt:

- Codex läuft in `--sandbox read-only`, einer vom System erzwungenen Grenze.
- Die Grok-Sandbox **kann auf vielen aktuellen Linux-Systemen nicht angewendet
  werden**: AppArmor blockiert seit Ubuntu 24.04 nicht privilegierte User Namespaces,
  und die Deny-Liste für Sockets der Container-Runtime schlägt fehl, wenn
  `/run/podman` auf `0700` gesetzt ist. Ein **integriertes** Profil, das
  nicht angewendet werden kann, startet jedoch **stillschweigend ohne Isolation**.
- Das Skript fordert daher standardmäßig kein Profil an und **greift niemals
  stillschweigend auf einen unsicheren Zustand zurück**: Es zeigt eine Warnung an.
  Die Isolation beruht auf den `--deny`-Regeln des CLI (einschließlich der
  Catch-all-Regel `*`), der einzigen als _fail-closed_ gemessenen Schicht —
  eine unbekannte Regel verhindert den Start, anstatt den Schutz ohne Hinweis zu
  entfernen.
- So **erzwingen** Sie die OS-Sandbox: `GROK_TRANSLATE_SANDBOX=read-only`. Der
  Start schlägt fehl, wenn der Rechner sie nicht einhalten kann, was dem
  gewünschten Verhalten entspricht.

**Kontingent**: Der Grok-Pool ist **wöchentlich und wird gemeinsam** mit Chat,
Imagine und Voice genutzt; zudem gibt es keinen Befehl, mit dem er ausgelesen
werden kann. Eine Stapelverarbeitung kann daher Ihre Nutzung für Unterhaltungen
beeinträchtigen, ohne dass darauf hingewiesen wird — daher ist die Parallelität
auf 2 begrenzt und `regen_translations.sh` enthält eine Warnung.

Weitere Variablen: `GROK_BIN` (Pfad zur Binärdatei), `GROK_TIMEOUT` (Standard 900 s).

Zur Neugenerierung der 28 Übersetzungen:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### Sparmodus

Verwendet schnellere und kostengünstigere Modelle (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Optionen

| Option                   | Beschreibung                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Einzelne zu übersetzende Markdown-Datei                                  |
| `--source_dir`           | Quellverzeichnis mit den Markdown-Dateien                                |
| `--target_dir`           | Ausgabeverzeichnis für die übersetzten Dateien                           |
| `--source_lang`          | Ausgangssprache (Standard: `fr`)                               |
| `--target_lang`          | Zielsprache (Standard: `en`)                                   |
| `--model`                | Zu verwendendes spezifisches Modell                                     |
| `--eco`                  | Sparmodelle verwenden                                                    |
| `--use_mistral`          | Mistral-AI-API verwenden                                                 |
| `--use_claude`           | Claude-API verwenden                                                     |
| `--use_gemini`           | Gemini-API verwenden                                                     |
| `--use_codex`            | Codex CLI mit dem Kontingent des ChatGPT-Abonnements verwenden           |
| `--use_grok`             | xAI-API (Grok) verwenden — erfordert `XAI_API_KEY`                       |
| `--use_grok_cli`         | Grok CLI mit dem Kontingent des Grok-Abonnements verwenden               |
| `--force`                | Erneute Übersetzung erzwingen                                            |
| `--keep_filename`        | Ursprünglichen Dateinamen beibehalten                                    |
| `--news`                 | Nachrichtenmodus: schützt EN-Zitate und verwaltet Flaggen je Sprache     |
| `--add_translation_note` | Übersetzungshinweis hinzufügen                                           |
| `--note_position`        | Position des Hinweises: `top`, `bottom` (Standard) oder `both` |
| `--note_format`          | Format des Hinweises: `legacy` (Standard, fettgedruckter Absatz) oder `marker` |
| `--include_model`        | Modellnamen in die Ausgabedatei aufnehmen                                |
| `--reasoning_effort`     | GPT-5.x-Reasoning-Aufwand: `none`/`low`/`medium`/`high`/`xhigh` |

> **Die sechs Provider-Flags schließen sich gegenseitig aus.** Zuvor wurde eine
> Kombination aus zwei Flags stillschweigend akzeptiert und auf den zuerst
> geprüften Provider aufgelöst: Eine Übersetzung, die über das
> Abonnementkontingent angefordert wurde (`--use_codex`, `--use_grok_cli`),
> konnte dadurch ohne jede Warnung nutzungsabhängig abgerechnet werden.
> `argparse` lehnt die Kombination nun ab.

### Übersetzungshinweis: Positionen und Formate

Mit `--add_translation_note` kann der Übersetzer den Hinweis oben, unten oder an beiden Stellen platzieren und ihn entweder als einfachen Text (abwärtskompatibel) oder im von einem Markdown-Plugin verarbeitbaren Format `marker` ausgeben.

**Position** (`--note_position`):

- `bottom` (Standard): Hinweis am Dateiende, wie bisher.
- `top`: Hinweis wird **nach dem YAML-Front-Matter** eingefügt (sicher für Astro Content Collections, gray-matter usw.).
- `both`: Hinweis wird oben UND unten eingefügt (ein einziger LLM-Aufruf, dessen Inhalt für beide Positionen wiederverwendet wird).

**Format** (`--note_format`):

- `legacy` (Standard): fettgedruckter Absatz `**...**` — exakt dasselbe Verhalten wie in v1.8, Byte für Byte. Kompatibel mit Hugo, GitHub, GitLab und jedem Markdown-Renderer.
- `marker`: unsichtbare Markdown-Linkreferenzdefinition (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), gefolgt von einem fettgedruckten Blockquote. Nativ auf GitHub/GitLab lesbar und beim Build von einem Remark-Plugin in Astro nutzbar, um ein stilisiertes Banner zu erzeugen (siehe Blog jls42.org).

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

| Provider | Qualität (Standard)     | Sparmodell (`--eco`) |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **Empfehlung für Langform-Übersetzungen**: `--use_gemini` (Standard = `gemini-3.7-flash`)
> bewahrt die Markdown-Struktur bei nicht lateinischen Schriften (PL, JA, ZH, AR, HI)
> zuverlässig, auch im Modus `--news`, in dem die Platzhaltertreue entscheidend
> ist. Gemessen anhand dieser ins Japanische übersetzten README: identische Struktur
> wie bei `gemini-3.1-pro-preview` (21 Listen, 18 Codeblöcke, 13 HTML-Links, 13 Bilder, alle
> URLs erhalten) bei etwa sechsmal geringerer Latenz. OpenAI bleibt aus Gründen der
> Abwärtskompatibilität die Standardeinstellung.

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** – Persönlicher mehrsprachiger Blog (15 Sprachen)

## Autor

Julien LE SAUX
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](LICENSE).

**Artikel, übersetzt aus dem Französischen ins Deutsche mit gpt-5.6-sol.**

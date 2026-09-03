# KI-gestützter Markdown-Übersetzer

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Codequalität</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status des Quality Gate"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Sicherheitsbewertung"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Zuverlässigkeitsbewertung"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Wartbarkeitsbewertung"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Abdeckung"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Sicherheitslücken"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Fehler"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code-Smells"></a>
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

Markdown-Dateiübersetzer mit **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** und **Grok (xAI)** — per API oder über das Kontingent eines ChatGPT-(Codex)- oder Grok-Abonnements, ohne nutzungsabhängige Abrechnung.

Dieses Python-Skript übersetzt Markdown-Dateien aus einer Ausgangssprache in eine Zielsprache und bewahrt dabei Formatierung, Codeblöcke und Front-Matter-Metadaten.

## Wichtigste Funktionen

- **Multi-Provider**: 5 APIs (OpenAI, Mistral, Claude, Gemini, Grok) + 2 abonnementbasierte CLIs, ohne nutzungsabhängige Abrechnung — Codex (ChatGPT) und Grok
- **Modelle 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Sparmodus**: Option `--eco` zur Verwendung schnellerer und kostengünstigerer Modelle
- **Einzeldatei**: Option `--file` zum Übersetzen einer einzelnen Datei
- **Intelligente Segmentierung**: Verarbeitung langer Texte mit modellabhängigen Token-Limits
- **Code-Erhaltung**: Codeblöcke UND Inline-Code (`` `...` ``) werden bewahrt
- **Dateiname**: Option `--keep_filename` zum Beibehalten des ursprünglichen Namens
- **News-Modus**: Option `--news` zum Schützen englischer Zitate und Verarbeiten von Flaggen in Nachrichtenartikeln
- **.env-Konfiguration**: Unterstützung der Datei `.env` für API-Schlüssel
- **Übersetzungsnotiz**: Optionale Notiz am Ende des Dokuments

## Installation

### Verwendung des Tools

```bash
pip install ai-powered-markdown-translator
```

Der Befehl `aipmt` ist anschließend überall verfügbar. Wenn sich das Python-Skriptverzeichnis nicht in deinem `PATH` befindet, bewirkt `python -m aipmt` genau dasselbe. Python 3.10 oder neuer.

Für eine vom Rest deiner Pakete isolierte Installation:

```bash
pipx install ai-powered-markdown-translator
```

### Mitarbeit am Projekt

Das geklonte Repository bleibt für die Entwicklung erforderlich: Dort befinden sich die Tests, die 28 Übersetzungen und alle Qualitätstools.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` ist eine **vollständig gepinnte Lock-Datei**, die exakt die getestete Umgebung widerspiegelt. Die in `pyproject.toml` veröffentlichten Grenzen sind absichtlich weiter gefasst: Sie machen keinerlei Vorgaben für deine anderen Pakete.

### Qualitätstools (optional, aber empfohlen)

Das Projekt verwendet [`pre-commit`](https://pre-commit.com), um zu verhindern, dass schlecht formatierter, anfälliger oder ein Geheimnis enthaltender Code committet wird. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktive Hooks: ruff (Lint+Format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (Komplexität), detect-secrets (API-Schlüssel), mypy (progressive Typisierung), Opengrep (SAST), pip-audit (CVE-Abhängigkeiten), unittest. Siehe den Abschnitt _Quality / pre-commit_ in `CLAUDE.md` für Details.

## Konfiguration

Die Schlüssel werden an **drei Stellen** gesucht, von der höchsten zur niedrigsten Priorität.
Jede Stelle ergänzt nur, was die vorherige leer lässt.

|     | Wo                                            | Wofür                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Umgebungsvariablen                     | CI, Container, gelegentliche Überschreibung |
| 2   | `.env` des aktuellen Verzeichnisses (oder eines übergeordneten Verzeichnisses) | ein projektspezifischer Schlüssel            |
| 3   | `~/.config/aipmt/.env`                        | **einmal installiert, überall gültig**   |

Am einfachsten nach einem `pip install` ist die dritte Variante:

```bash
mkdir -p ~/.config/aipmt
cat > ~/.config/aipmt/.env <<'EOF'
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google
EOF
chmod 600 ~/.config/aipmt/.env
```

Diese Datei folgt `XDG_CONFIG_HOME`, wenn die Variable einen absoluten Pfad angibt (andernfalls wird sie gemäß der Spezifikation ignoriert), sowie `%APPDATA%` unter Windows.

Die zweite Variante bleibt nützlich, wenn ein Repository einen eigenen Schlüssel besitzt: Ein `.env` in seinem Stammverzeichnis hat dann Vorrang vor der Benutzerkonfiguration, ohne diese zu ändern. Und eine bereits in der Umgebung definierte Variable hat Vorrang vor beiden:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Wenn kein Schlüssel gefunden wird, gibt der Befehl keinen Aufruf-Trace aus: Er listet die drei Speicherorte mit ihrem exakten Pfad auf.

`GEMINI_API_KEY` wird als Alternative zu `GOOGLE_API_KEY` akzeptiert (AI-Studio-Konvention). Optionale Variablen: `XAI_BASE_URL` (xAI-Endpunkt, Standardwert `https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (Sekunden pro Anthropic-Aufruf, Standardwert 900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT` sowie `GROK_TRANSLATE_SANDBOX` (siehe Abschnitt Grok CLI). Für `regen_translations.sh`: `REGEN_PROVIDER`, `REGEN_MODEL` und `REGEN_JOB_TIMEOUT` (Limit pro Job, Standardwert 600 s).

## Verwendung

### Eine einzelne Datei übersetzen

```bash
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Ein Verzeichnis übersetzen

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
aipmt --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
aipmt --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
aipmt --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
aipmt --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
aipmt --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
aipmt --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
aipmt --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'
```

### Über das ChatGPT-Abonnement übersetzen (`--use_codex`)

Dieser Provider verbraucht keinen API-Schlüssel: Er steuert die offizielle Codex-CLI im nicht-interaktiven Modus, sodass die Übersetzung vom Kontingent des bereits bezahlten ChatGPT-Abonnements (Plus, Pro, Business …) abgezogen wird. Dies ist der einzige von OpenAI dokumentierte Weg für diesen Zweck — die Tokens von `~/.codex/auth.json` authentifizieren keine Aufrufe der Platform API und werden von diesem Skript außerdem niemals gelesen.

**Voraussetzungen:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Die Binärdatei wird in dieser Reihenfolge gesucht: die Variable `CODEX_BIN`, der `PATH` und anschließend das Python-Paket `openai-codex-cli-bin`. Letzteres ist absichtlich nicht in `requirements.txt` enthalten: Es ist etwa 250 MB groß, was allen Benutzern für einen optionalen Provider auferlegt würde.

**Wissenswertes:**

- **Es wird kein API-Schlüssel verwendet.** `OPENAI_API_KEY` und `CODEX_API_KEY` werden aus der Umgebung des Unterprozesses entfernt. Dadurch wird garantiert, dass ein in `.env` vorhandener Schlüssel die Übersetzung niemals in eine nutzungsabhängige Abrechnung umleitet.
- **Ein Segment = eine „lokale Nachricht“** des 5-Stunden-Fensters des Tarifs. `--eco` (Modell `gpt-5.6-luna`, 250–2.000 Nachrichten/5 h bei Plus) sollte statt des Qualitätsmodells (`gpt-5.6-sol`, 10–100 Nachrichten/5 h) verwendet werden.
- **Langsamer** als ein API-Aufruf: Für eine vollständige README-Datei etwa 45 s einplanen, im Vergleich zu wenigen Sekunden direkt.
- **In CI abgelehnt** (`CI` oder `GITHUB_ACTIONS` gesetzt): Die abonnementbasierte Authentifizierung ist nicht für einen gemeinsam genutzten Runner vorgesehen, und OpenAI rät von diesem Workflow in öffentlichen Repositories ab. Auf diesem Pfad einen API-Schlüssel verwenden.
- Umgebungsvariablen: `CODEX_BIN` (expliziter Pfad zur Binärdatei) und `CODEX_TIMEOUT` (Sekunden pro Segment, Standardwert `600`).

### Über das Grok-Abonnement übersetzen (`--use_grok_cli`)

Dasselbe Prinzip wie bei `--use_codex`, mit der offiziellen **Grok Build**-CLI: Die Übersetzung wird vom Grok-Abonnement (SuperGrok / X Premium+) abgezogen, statt pro Token berechnet zu werden.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Einschränkung — vor der Verwendung lesen.** Dieser Provider ist strukturell **schwächer** als `--use_codex`, und das ist beabsichtigt:

- Codex läuft in `--sandbox read-only`, einer vom System vorgegebenen Grenze.
- Die Grok-Sandbox kann auf vielen aktuellen Linux-Systemen **nicht angewendet werden**: AppArmor blockiert seit Ubuntu 24.04 nicht privilegierte User Namespaces, und die Deny-Liste der Container-Runtime-Sockets schlägt fehl, wenn `/run/podman` in `0700` enthalten ist. Ein **integriertes** Profil, das nicht angewendet werden kann, startet jedoch **still und ohne Einschränkung**.
- Das Skript fordert daher standardmäßig kein Profil an und fällt **niemals stillschweigend zurück**: Es zeigt eine Warnung an. Die Einschränkung beruht auf den `--deny`-Regeln der CLI (einschließlich des Catch-all `*`), der einzigen gemessenen _fail-closed_-Schicht — eine unbekannte Regel führt dazu, dass der Start verweigert wird, anstatt den Schutz unbemerkt zu entfernen.
- Um die **OS-Sandbox zu erzwingen**: `GROK_TRANSLATE_SANDBOX=read-only`. Der Start schlägt fehl, wenn der Rechner sie nicht einhalten kann — genau das gewünschte Verhalten.

**Kontingent**: Der Grok-Pool ist **wöchentlich und gemeinsam genutzt** mit Chat, Imagine und Voice, und kein Befehl ermöglicht es, ihn auszulesen. Eine Batch-Verarbeitung kann daher deine Chat-Nutzung verringern, ohne dass dies angezeigt wird — daher die Begrenzung der Parallelität auf 2 und eine Warnung in `regen_translations.sh`.

Weitere Variablen: `GROK_BIN` (Pfad zur Binärdatei), `GROK_TIMEOUT` (Standardwert 900 s).

Zur Regenerierung der 28 Übersetzungen:

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
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Optionen

| Option                   | Beschreibung                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Einzelne zu übersetzende Markdown-Datei                                       |
| `--source_dir`           | Quellverzeichnis mit den Markdown-Dateien                        |
| `--target_dir`           | Ausgabeverzeichnis für die übersetzten Dateien                          |
| `--source_lang`          | Ausgangssprache (Standard: `fr`)                                             |
| `--target_lang`          | Zielsprache (Standard: `en`)                                              |
| `--model`                | Zu verwendendes spezifisches Modell                                             |
| `--eco`                  | Kostengünstige Modelle verwenden                                         |
| `--use_mistral`           | Mistral-AI-API verwenden                                                |
| `--use_claude`           | Claude-API verwenden                                                    |
| `--use_gemini`           | Gemini-API verwenden                                                    |
| `--use_codex`            | Codex-CLI über das Kontingent des ChatGPT-Abonnements verwenden               |
| `--use_grok`             | xAI-API (Grok) verwenden — erfordert `XAI_API_KEY`                      |
| `--use_grok_cli`         | Grok-CLI über das Kontingent des Grok-Abonnements verwenden                   |
| `--force`                | Erneute Übersetzung erzwingen                                                  |
| `--keep_filename`        | Ursprünglichen Dateinamen beibehalten                                     |
| `--news`                 | Nachrichtenmodus: EN-Zitate schützen, Flaggen nach Sprache verarbeiten |
| `--add_translation_note` | Übersetzungsnotiz hinzufügen                                           |
| `--note_position`        | Position der Notiz: `top`, `bottom` (Standard) oder `both`                |
| `--note_format`          | Format der Notiz: `legacy` (Standard, fetter Absatz) oder `marker`       |
| `--include_model`        | Modellnamen in die Ausgabedatei aufnehmen                       |
| `--reasoning_effort`     | GPT-5.x-Reasoning-Aufwand: `none`/`low`/`medium`/`high`/`xhigh`    |

> **Die sechs Provider-Flags schließen sich gegenseitig aus.** Ihre Kombination wurde zuvor stillschweigend akzeptiert und auf den zuerst geprüften Provider aufgelöst: Eine auf dem Abonnementkontingent angeforderte Übersetzung (`--use_codex`, `--use_grok_cli`) konnte dadurch ohne jede Warnung in eine nutzungsabhängige Abrechnung umgeleitet werden.
> `argparse` lehnt diese Kombination jetzt ab.

### Übersetzungsnotiz: Positionen und Formate

Mit `--add_translation_note` kann der Translator die Notiz oben, unten oder an beiden Stellen platzieren und sie entweder als einfachen Text (abwärtskompatibel) oder im von einem Markdown-Plugin verarbeitbaren Format `marker` ausgeben.

**Position** (`--note_position`):

- `bottom` (Standard): Notiz am Ende der Datei, wie bisher.
- `top`: Notiz **nach dem YAML-Frontmatter** eingefügt (Sicherheit für Astro Content Collections, gray-matter usw.).
- `both`: Notiz OBEN UND UNTEN eingefügt (ein einziger LLM-Aufruf, Inhalt für beide Platzierungen wiederverwendet).

**Format** (`--note_format`):

- `legacy` (Standard): fetter Absatz `**...**` — exakt dasselbe Verhalten wie in v1.8, Byte für Byte. Kompatibel mit Hugo, GitHub, GitLab und jedem Markdown-Renderer.
- `marker`: unsichtbare Markdown-Link-Referenzdefinition (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), gefolgt von einem fetten Blockquote. Auf GitHub/GitLab nativ lesbar und beim Build von einem remark-Plugin auf Astro-Seite nutzbar, um ein stilisiertes Banner zu erzeugen (siehe Blog jls42.org).

```bash
# Compatibilité legacy (rien ne change vs v1.8)
aipmt --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
aipmt --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
aipmt --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### Standardmodelle (2026)

| Provider | Qualität (Standard)       | Sparmodus (`--eco`)    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **Empfehlung für Long-Form-Übersetzungen**: `--use_gemini` (Standard = `gemini-3.7-flash`) bewahrt die Markdown-Struktur bei nicht-lateinischen Skripten (PL, JA, ZH, AR, HI) zuverlässig, auch im `--news`-Modus, in dem die Genauigkeit der Platzhalter entscheidend ist. Gemessen an dieser ins Japanische übersetzten README: identische Struktur wie bei `gemini-3.1-pro-preview` (21 Listen, 18 Codeblöcke, 13 HTML-Links, 13 Bilder, alle URLs bewahrt) bei etwa sechsmal geringerer Latenz. OpenAI bleibt aus Gründen der Abwärtskompatibilität der Standard.

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** - Mehrsprachiger persönlicher Blog (15 Sprachen)

## Autor

Julien LE SAUX  
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artikel vom Französischen ins Deutsche mit gpt-5.6-luna übersetzt.**

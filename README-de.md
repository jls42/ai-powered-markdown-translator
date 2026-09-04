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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Schwachstellen"></a>
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

Übersetzer für Markdown-Dateien mit **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** und **Grok (xAI)** — per API, über das Kontingent eines ChatGPT-(Codex)- oder Grok-Abonnements ohne nutzungsabhängige Abrechnung oder über **OpenCode**, den Open-Source-Agenten, zum Anbieter Ihrer Wahl: lokales Modell (Ollama), kostenloses Modell, Abonnement (GitHub Copilot …) oder API-Schlüssel.

Dieses Python-Skript übersetzt Markdown-Dateien von einer Ausgangssprache in eine Zielsprache und bewahrt dabei Formatierung, Codeblöcke und Front-Matter-Metadaten.

## Hauptfunktionen

- **Multi-Provider**: 5 APIs (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLI-Tools im Abonnement ohne nutzungsabhängige Abrechnung — Codex (ChatGPT) und Grok — + OpenCode (Open Source, MIT) zu jedem in OpenCode konfigurierten Anbieter, einschließlich eines lokalen Modells
- **Modelle 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Sparmodus**: Option `--eco`, um schnellere und kostengünstigere Modelle zu verwenden
- **Einzeldatei**: Option `--file`, um nur eine Datei zu übersetzen
- **Intelligente Segmentierung**: Verarbeitung langer Texte mit modellabhängigen Token-Limits
- **Codeerhalt**: Codeblöcke UND Inline-Code (`` `...` ``) werden bewahrt
- **Dateiname**: Option `--keep_filename`, um den ursprünglichen Namen beizubehalten
- **News-Modus**: Option `--news`, um englische Zitate zu schützen und Flaggen in Nachrichtenartikeln zu verarbeiten
- **.env-Konfiguration**: Unterstützung der Datei `.env` für API-Schlüssel
- **Übersetzungsnotiz**: Optionales Hinzufügen einer Notiz am Ende des Dokuments

## Installation

### Verwendung des Tools

```bash
pip install ai-powered-markdown-translator
```

Der Befehl `aipmt` ist anschließend überall verfügbar. Falls sich das Python-Skriptverzeichnis nicht in Ihrem `PATH` befindet, erledigt `python -m aipmt` genau dasselbe. Python 3.10 oder neuer.

Für eine vom Rest Ihrer Pakete isolierte Installation:

```bash
pipx install ai-powered-markdown-translator
```

### Zum Mitwirken am Projekt

Das geklonte Repository bleibt für die Entwicklung erforderlich: Dort befinden sich die Tests, die 28 Übersetzungen und die gesamte Qualitätssicherung.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` ist ein **vollständig festgeschriebener Lock**, ein exaktes Abbild der getesteten Umgebung. Die in `pyproject.toml` veröffentlichten Grenzen sind absichtlich weiter gefasst: Sie erzwingen nichts für Ihre anderen Pakete.

### Qualitätssicherung (optional, aber empfohlen)

Das Projekt verwendet [`pre-commit`](https://pre-commit.com), um zu verhindern, dass schlecht formatierten oder unsicheren Code beziehungsweise Code mit einem Secret committed wird. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktive Hooks: ruff (Linting+Formatierung), shellcheck (bash), prettier (markdown/yaml/json), Lizard (Komplexität), detect-secrets (API-Schlüssel), mypy (progressive Typisierung), Opengrep (SAST), pip-audit (CVE-Abhängigkeiten), unittest. Einzelheiten finden Sie in `CLAUDE.md` im Abschnitt _Quality / pre-commit_.

## Konfiguration

Die Schlüssel werden an **drei Stellen** gesucht, von der höchsten zur niedrigsten Priorität.
Jede Stelle ergänzt nur, was die vorherige nicht festlegt.

|     | Wo                                            | Wofür                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Umgebungsvariablen                            | CI, Container, einmalige Ausnahme    |
| 2   | `.env` des aktuellen Verzeichnisses (oder eines übergeordneten Verzeichnisses) | ein projektspezifischer Schlüssel |
| 3   | `~/.config/aipmt/.env`                                 | **einmal installiert, überall gültig** |

Nach einem `pip install` ist die dritte Variante am einfachsten:

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

Diese Datei folgt `XDG_CONFIG_HOME`, wenn die Variable einen absoluten Pfad angibt (andernfalls wird sie gemäß der Spezifikation ignoriert), und `%APPDATA%` unter Windows.

Die zweite Variante bleibt nützlich, wenn ein Repository einen eigenen Schlüssel besitzt: Ein `.env` in seinem Stammverzeichnis hat dann Vorrang vor der Benutzerkonfiguration, ohne diese zu ändern. Eine bereits in der Umgebung definierte Variable hat wiederum Vorrang vor beiden:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Wenn kein Schlüssel gefunden wird, gibt der Befehl keine Aufrufspur aus, sondern listet die drei Speicherorte mit ihrem exakten Pfad auf.

`GEMINI_API_KEY` wird als Alternative zu `GOOGLE_API_KEY` akzeptiert (AI-Studio-Konvention). Optionale Variablen: `XAI_BASE_URL` (xAI-Endpunkt, Standardwert `https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (Sekunden pro Anthropic-Aufruf, Standardwert 900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`, `GROK_TRANSLATE_SANDBOX` (siehe Abschnitt „Grok CLI“) und `OPENCODE_BIN` / `OPENCODE_TIMEOUT` (siehe Abschnitt „OpenCode“). Für `regen_translations.sh`: `REGEN_PROVIDER`, `REGEN_MODEL` und `REGEN_JOB_TIMEOUT` (Limit pro Job, Standardwert 600 s).

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

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### Mit dem ChatGPT-Abonnement übersetzen (`--use_codex`)

Dieser Provider benötigt keinen API-Schlüssel: Er steuert das offizielle Codex-CLI im nicht-interaktiven Modus, sodass die Übersetzung vom bereits bezahlten Kontingent des ChatGPT-Abonnements (Plus, Pro, Business …) abgezogen wird. Dies ist der einzige von OpenAI dokumentierte Weg für diese Nutzung — die Tokens von `~/.codex/auth.json` authentifizieren keine Aufrufe der Platform API und werden von diesem Skript außerdem niemals gelesen.

**Voraussetzungen:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Die Binärdatei wird in dieser Reihenfolge gesucht: in der Variable `CODEX_BIN`, im `PATH` und anschließend im Python-Paket `openai-codex-cli-bin`. Letzteres befindet sich absichtlich nicht in `requirements.txt`: Es ist etwa 250 MB groß, was allen Benutzern für einen optionalen Provider auferlegt würde.

**Wissenswertes:**

- **Es wird kein API-Schlüssel verwendet.** `OPENAI_API_KEY` und `CODEX_API_KEY` werden aus der Umgebung des Unterprozesses entfernt. Dadurch wird garantiert, dass ein in `.env` vorhandener Schlüssel die Übersetzung niemals versehentlich auf nutzungsabhängige Abrechnung umstellt.
- **Ein Segment = eine „lokale Nachricht“** des 5-Stunden-Fensters des Tarifs. Verwenden Sie `--eco` (Modell `gpt-5.6-luna`, 250–2.000 Nachrichten/5 h bei Plus) statt des Qualitätsmodells (`gpt-5.6-sol`, 10–100 Nachrichten/5 h).
- **Langsamer** als ein API-Aufruf: Für ein vollständiges README sind etwa 45 s einzuplanen, gegenüber wenigen Sekunden direkt.
- **In CI abgelehnt** (`CI` oder `GITHUB_ACTIONS` definiert): Die Authentifizierung über ein Abonnement ist nicht für einen gemeinsam genutzten Runner vorgesehen, und OpenAI rät von diesem Workflow in öffentlichen Repositories ab. Verwenden Sie auf diesem Weg einen API-Schlüssel.
- Umgebungsvariablen: `CODEX_BIN` (expliziter Pfad zur Binärdatei) und `CODEX_TIMEOUT` (Sekunden pro Segment, Standardwert `600`).

### Mit dem Grok-Abonnement übersetzen (`--use_grok_cli`)

Dasselbe Prinzip wie bei `--use_codex`, mit dem offiziellen CLI **Grok Build**: Die Übersetzung wird vom Grok-Abonnement (SuperGrok / X Premium+) abgezogen, anstatt nach Token abgerechnet zu werden.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Einschränkung — vor der Verwendung lesen.** Dieser Provider ist strukturell **schwächer** als `--use_codex`, und das ist beabsichtigt:

- Codex läuft in `--sandbox read-only`, einer vom System vorgegebenen Grenze.
- Die Grok-Sandbox kann auf vielen aktuellen Linux-Systemen **nicht angewendet werden**: AppArmor blockiert seit Ubuntu 24.04 nicht privilegierte User-Namespaces, und die Denylist der Container-Runtime-Sockets schlägt fehl, wenn `/run/podman` auf `0700` gesetzt ist. Ein **integriertes** Profil, das nicht angewendet werden kann, startet jedoch **still und ungeschützt**.
- Das Skript fordert daher standardmäßig kein Profil an und fällt **niemals stillschweigend zurück**: Es zeigt eine Warnung an. Die Einschränkung beruht auf den `--deny`-Regeln des CLI (einschließlich des Catch-all `*`), der einzigen gemessenen _fail-closed_-Schicht — eine unbekannte Regel führt dazu, dass der Start verweigert wird, anstatt den Schutz unbemerkt zu entfernen.
- Um die **OS-Sandbox zu erzwingen**: `GROK_TRANSLATE_SANDBOX=read-only`. Der Start schlägt fehl, wenn der Rechner sie nicht einhalten kann — genau dieses Verhalten ist beabsichtigt.

**Kontingent**: Der Grok-Pool ist **wöchentlich und gemeinsam** für Chat, Imagine und Voice, und kein Befehl ermöglicht es, ihn auszulesen. Eine Stapelverarbeitung kann daher Ihre Gesprächsnutzung beeinträchtigen, ohne dass dies angezeigt wird — daher die Begrenzung der Parallelität auf 2 und eine Warnung in `regen_translations.sh`.

Weitere Variablen: `GROK_BIN` (Pfad zur Binärdatei), `GROK_TIMEOUT` (Standardwert 900 s).

Zur erneuten Erzeugung der 28 Übersetzungen:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
```

### Mit OpenCode zum Anbieter Ihrer Wahl übersetzen (`--use_opencode`)

[OpenCode](https://opencode.ai) ist ein **Open-Source-Code-Agent (MIT)** für das Terminal. Es ist kein Modellanbieter, sondern ein **Router** zu den Anbietern, die Sie in OpenCode selbst konfiguriert haben: ein API-Schlüssel, ein Abonnement (GitHub Copilot, ChatGPT, SuperGrok), das OpenCode-Zen-Gateway mit kostenlosen Modellen **ohne Konto** oder ein **lokales** Modell (Ollama, LM Studio, llama.cpp). Dieser Provider steuert `opencode run` im nicht-interaktiven Modus und beschränkt den Aufruf auf genau einen Hin- und Rücklauf ohne Tools.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` ist **erforderlich**, im Format `provider/modèle`. OpenCode ist kein Anbieter, und es wird keine Standardeinstellung für Sie ausgewählt: Sein eigener Fallback wäre ein kostenloses Modell, dessen Interaktionen zum Training verwendet werden können.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Einschränkung — was das Skript bei jedem Aufruf tut:**

- Eine Inline-Konfiguration (`OPENCODE_CONFIG_CONTENT`), die Vorrang vor Ihrer Konfiguration hat, definiert einen `aipmt`-Agenten, dessen **sämtliche Tools verweigert werden** (`permission: { "*": "deny" }`): Das Modell kann weder lesen noch schreiben noch Befehle ausführen — in Messungen versucht es dies nicht einmal. Die gemeinsame Sitzungsnutzung ist deaktiviert, `--pure` schließt externe Plugins aus, niemals jedoch `--auto`.
- Der Aufruf läuft in einem **leeren, temporären Verzeichnis** mit den Schaltern `OPENCODE_DISABLE_PROJECT_CONFIG` und `OPENCODE_DISABLE_CLAUDE_CODE`: Ohne diese fügt OpenCode jedem Prompt die `AGENTS.md` des aktuellen Verzeichnisses und Ihre `~/.claude/CLAUDE.md` hinzu — in einer Messung wurde eine Anweisung „jede Antwort mit BANANA beenden“, die in einem `AGENTS.md` hinterlegt war, auf die Übersetzung angewendet. Die globalen Regeln von `~/.config/opencode/AGENTS.md` bleiben dagegen aktiv: OpenCode erlaubt nicht, sie auszuschließen.
- Der Ausgabevertrag verlangt gleichzeitig: Rückgabecode 0, kein `error`-Ereignis, keinen Tool-Aufruf, einen letzten Schritt mit dem Status `stop`, einen nicht leeren Text und einen tatsächlich geladenen Agenten — ein unbekannter `--agent` lässt OpenCode nicht fehlschlagen, sondern fällt **still** auf den Coding-Agenten mit aktiven Tools zurück. Auch ein `exit 0` beweist hier nichts.
- **Kein aipmt-Schlüssel wird** an den Unterprozess übergeben (dieselbe Filterung wie bei Codex und Grok), mit einer ausdrücklich benannten Ausnahme: `OPENCODE_API_KEY`, der Schlüssel von OpenCode selbst (Zen, Go). Die Anbieter werden in OpenCode (`opencode auth login`, `opencode.json`) konfiguriert, nicht in der `.env` von aipmt.

**Wissenswertes:**

- **Die kostenlosen Zen-Modelle sind „Stealth“- oder Contributor-Modelle**, ändern sich, haben nicht dokumentierte Limits, und ihre Interaktionen können zum Training verwendet werden: ideal für öffentliche Dokumentation, zu vermeiden bei privaten Inhalten. Gemessen wurde: `opencode/mimo-v2.5-free` übersetzt dieses README in einem Durchlauf; `opencode/big-pickle` ist langsamer, und zwei gleichzeitige Anfragen blieben ohne Antwort.
- **Ein lokales Modell muss mindestens 16 k Kontext bereitstellen** — die Segmente sind bis zu 16.000 Zeichen lang — während Ollama häufig standardmäßig 4.096 konfiguriert. Mit Ollama: ein `Modelfile` mit `PARAMETER num_ctx 32768`, anschließend `ollama create`. Die Qualität hängt vom Modell ab: Ein 7B-Modell vertauschte in einer Testdatei eine Liste und beschädigte den Abschluss eines Codeblocks, während ein Gateway-Modell alles bewahrte.
- `--eco` hat keine Wirkung (das Modell wird von `--model` bestimmt); `--reasoning_effort` wird unverändert als `--variant` von OpenCode übergeben und sollte nur angefordert werden, wenn das Modell es kennt.
- Die Sitzungen werden von OpenCode in seiner Datenbank (`~/.local/share/opencode/`) protokolliert, wie jede OpenCode-Sitzung.
- Umgebungsvariablen: `OPENCODE_BIN` (expliziter Pfad zur Binärdatei, andernfalls zuerst `PATH` und dann `~/.opencode/bin/opencode`) und `OPENCODE_TIMEOUT` (Sekunden pro Segment, Standardwert `600`). `OPENCODE_CONFIG` wird berücksichtigt, wenn Sie die Variable exportieren.

### Sparmodus

Verwendet schnellere und kostengünstigere Modelle (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### Optionen

| Option | Beschreibung |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
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
| `--use_codex` | Codex-CLI über das Kontingent des ChatGPT-Abonnements verwenden |
| `--use_grok` | xAI-API (Grok) verwenden — erfordert `XAI_API_KEY` |
| `--use_grok_cli` | Grok-CLI über das Kontingent des Grok-Abonnements verwenden |
| `--use_opencode` | OpenCode (Open Source) mit dem in OpenCode konfigurierten Anbieter verwenden; erfordert `--model provider/modèle` |
| `--force` | Neuübersetzung erzwingen |
| `--keep_filename` | Originalen Dateinamen beibehalten |
| `--news` | Nachrichtenmodus: schützt EN-Zitate und verwaltet Sprach-Flags |
| `--add_translation_note` | Übersetzungsnotiz hinzufügen |
| `--note_position` | Position der Notiz: `top`, `bottom` (Standard) oder `both` |
| `--note_format` | Format der Notiz: `legacy` (Standard, fettgedruckter Absatz) oder `marker` |
| `--include_model` | Modellnamen in die Ausgabedatei aufnehmen |
| `--reasoning_effort` | GPT-5.x-Reasoning-Aufwand: `none`/`low`/`medium`/`high`/`xhigh` |

> **Die sieben Provider-Flags schließen sich gegenseitig aus.** Früher war es möglich, zwei davon zu kombinieren; stillschweigend wurde dann der zuerst geprüfte verwendet: Eine angeforderte Übersetzung über das Abonnementkontingent (`--use_codex`, `--use_grok_cli`) konnte dadurch ohne Warnung zur nutzungsbasierten Abrechnung wechseln.
> `argparse` lehnt diese Kombination nun ab.

### Übersetzungsnotiz: Positionen und Formate

Mit `--add_translation_note` kann der Translator die Notiz oben, unten oder an beiden Stellen platzieren und sie entweder als einfachen Text (abwärtskompatibel) oder im von einem Markdown-Plugin verarbeitbaren Format `marker` ausgeben.

**Position** (`--note_position`):

- `bottom` (Standard): Notiz am Ende der Datei, wie bisher.
- `top`: Notiz **nach dem YAML-Frontmatter** eingefügt (Sicherheit für Astro Content Collections, gray-matter usw.).
- `both`: Notiz oben UND unten eingefügt (ein einziger LLM-Aufruf, Inhalt wird für beide Platzierungen wiederverwendet).

**Format** (`--note_format`):

- `legacy` (Standard): fettgedruckter Absatz `**...**` — exakt dasselbe Verhalten wie in v1.8, Byte für Byte. Kompatibel mit Hugo, GitHub, GitLab und jedem Markdown-Renderer.
- `marker`: unsichtbare Markdown-Link-Referenzdefinition (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), gefolgt von einem fettgedruckten Blockquote. Nativ auf GitHub/GitLab lesbar und beim Build von einem remark-Plugin auf Astro-Seite zur Erzeugung eines stilisierten Banners nutzbar (siehe Blog jls42.org).

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

| Anbieter | Qualität (Standard) | Kostengünstig (`--eco`) |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI | `gpt-5.6-terra` | `gpt-5.6-luna` |
| Claude | `claude-sonnet-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3.7-flash` | `gemini-3.1-flash-lite` |
| Codex | `gpt-5.6-sol` | `gpt-5.6-luna` |
| Grok API | `grok-4.6` | `grok-4.3` |
| Grok CLI | `grok-4.6` | `grok-4.5` |
| OpenCode | `--model provider/modèle` obligatorisch | ebenso — `--eco` ohne Wirkung |

> **Empfehlung für Langform-Übersetzungen**: `--use_gemini` (Standard = `gemini-3.7-flash`) bewahrt die Markdown-Struktur bei nicht-lateinischen Schriften (PL, JA, ZH, AR, HI) originalgetreu, auch im `--news`-Modus, in dem die Genauigkeit der Platzhalter entscheidend ist. Gemessen an dieser ins Japanische übersetzten README: identische Struktur wie bei `gemini-3.1-pro-preview` (21 Listen, 18 Codeblöcke, 13 HTML-Links, 13 Bilder, alle URLs erhalten) bei etwa sechsmal geringerer Latenz. OpenAI bleibt aus Gründen der Abwärtskompatibilität der Standard.

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** – Mehrsprachiger persönlicher Blog (15 Sprachen)

## Autor

Julien LE SAUX
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artikel vom Französischen ins Deutsche mit gpt-5.6-luna übersetzt.**

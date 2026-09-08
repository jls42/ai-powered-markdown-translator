# KI-gestützter Markdown-Übersetzer

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Codequalität</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status des Qualitäts-Gates"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Sicherheitsbewertung"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Zuverlässigkeitsbewertung"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Wartbarkeitsbewertung"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Testabdeckung"></a>
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
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy-Abzeichen"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Übersetzer für Markdown-Dateien mit **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** und **Grok (xAI)** — per API, über das Kontingent eines ChatGPT- (Codex) oder Grok-Abonnements ohne nutzungsabhängige Abrechnung oder über **OpenCode**, den Open-Source-Agenten, mit einem Anbieter Ihrer Wahl: lokales Modell (Ollama), kostenloser Anbieter, Abonnement (GitHub Copilot …) oder Schlüssel.

Dieses Python-Skript übersetzt Markdown-Dateien aus einer Ausgangssprache in eine Zielsprache und bewahrt dabei die Formatierung, Codeblöcke und Front-Matter-Metadaten.

## Hauptmerkmale

- **Mehrere Anbieter**: 5 APIs (OpenAI, Mistral, Claude, Gemini, Grok) + 2 abonnementbasierte CLIs ohne nutzungsabhängige Abrechnung — Codex (ChatGPT) und Grok — + OpenCode (Open Source, MIT) für jeden in OpenCode konfigurierten Anbieter, einschließlich eines lokalen Modells
- **Modelle 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Sparmodus**: Option `--eco` zur Verwendung schnellerer und kostengünstigerer Modelle
- **Einzeldatei**: Option `--file` zum Übersetzen einer einzelnen Datei
- **Intelligente Segmentierung**: Verarbeitung langer Texte unter Berücksichtigung der Token-Limits des jeweiligen Modells
- **Bewahrung von Code**: Codeblöcke UND Inline-Code (`` `...` ``) bleiben erhalten
- **Dateiname**: Option `--keep_filename` zum Beibehalten des ursprünglichen Namens
- **News-Modus**: Option `--news` zum Schutz englischer Zitate und zur Handhabung von Flaggen in Nachrichtenartikeln
- **.env-Konfiguration**: Unterstützung der Datei `.env` für API-Schlüssel
- **Übersetzungshinweis**: Optionales Hinzufügen eines Hinweises am Ende des Dokuments

## Installation

### Zur Verwendung des Tools

```bash
pip install ai-powered-markdown-translator
```

Der Befehl `aipmt` ist anschließend überall verfügbar. Falls sich das Verzeichnis der Python-Skripte
nicht in Ihrem `PATH` befindet, bewirkt `python -m aipmt` genau dasselbe.
Python 3.10 oder neuer.

Für eine von Ihren übrigen Paketen isolierte Installation:

```bash
pipx install ai-powered-markdown-translator
```

### Zur Mitwirkung am Projekt

Das geklonte Repository ist weiterhin für die Entwicklung erforderlich: Dort befinden sich die Tests,
die 28 Übersetzungen und sämtliche Werkzeuge zur Qualitätssicherung.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` ist eine **vollständig festgeschriebene Lock-Datei**, die exakt der
getesteten Umgebung entspricht. Die in `pyproject.toml` veröffentlichten Versionsgrenzen sind
bewusst weiter gefasst: Sie schreiben Ihren anderen Paketen nichts vor.

### Werkzeuge zur Qualitätssicherung (optional, aber empfohlen)

Das Projekt verwendet [`pre-commit`](https://pre-commit.com), um zu verhindern, dass schlecht formatierter, anfälliger oder ein Geheimnis enthaltender Code committet wird. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktive Hooks: ruff (Linting und Formatierung), shellcheck (bash), prettier (markdown/yaml/json), Lizard (Komplexität), detect-secrets (API-Schlüssel), mypy (schrittweise Typisierung), Opengrep (SAST), pip-audit (CVE-Abhängigkeiten), unittest. Einzelheiten finden Sie in `CLAUDE.md` im Abschnitt _Quality / pre-commit_.

## Konfiguration

Die Schlüssel werden an **drei Stellen** gesucht, von der höchsten bis zur niedrigsten Priorität.
Jede Stelle ergänzt lediglich, was die vorherige offengelassen hat.

|     | Wo                                            | Wofür                                      |
| --- | --------------------------------------------- | ------------------------------------------ |
| 1   | Umgebungsvariablen                            | CI, Container, punktuelle Überschreibung   |
| 2   | `.env` im aktuellen Verzeichnis (oder einem übergeordneten Verzeichnis) | projektspezifischer Schlüssel |
| 3   | `~/.config/aipmt/.env`                        | **einmal installiert, überall gültig**     |

Nach einem `pip install` ist die dritte Möglichkeit am einfachsten:

```bash
mkdir -p ~/.config/aipmt
cat > ~/.config/aipmt/.env <<'EOF'
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google
OPENROUTER_API_KEY=votre-clé-api-openrouter
EOF
chmod 600 ~/.config/aipmt/.env
```

Diese Datei folgt `XDG_CONFIG_HOME`, wenn die Variable einen absoluten Pfad bezeichnet
(andernfalls wird sie gemäß der Spezifikation ignoriert), und unter Windows `%APPDATA%`.

Die zweite Möglichkeit bleibt nützlich, wenn ein Repository einen eigenen Schlüssel besitzt: Eine Datei `.env` in seinem Stammverzeichnis
hat dann Vorrang vor der Benutzerkonfiguration, ohne diese zu verändern. Eine
bereits in der Umgebung definierte Variable hat wiederum Vorrang vor beiden:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Wenn kein Schlüssel gefunden wird, zeigt der Befehl keinen Aufruf-Trace an, sondern
listet die drei Speicherorte mit ihrem exakten Pfad auf.

`GEMINI_API_KEY` wird als Alternative zu `GOOGLE_API_KEY` akzeptiert (AI-Studio-Konvention).
Optionale Variablen: `XAI_BASE_URL` (xAI-Endpunkt, Standardwert
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (Sekunden pro Anthropic-Aufruf, Standardwert
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (siehe Abschnitt Grok CLI), `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (siehe Abschnitt OpenCode) und `OPENROUTER_BASE_URL` /
`OPENROUTER_TIMEOUT` / `OPENROUTER_PREFLIGHT_TIMEOUT` (siehe Abschnitt
OpenRouter). Für
`regen_translations.sh`: `REGEN_PROVIDER` (Standardwert `codex`, abonnementbasiert),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (obligatorische Überschreibung für eine
kostenpflichtige API) und `REGEN_JOB_TIMEOUT` (Obergrenze pro Auftrag, standardmäßig 600 s, bei Codex 1.800 s).

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

# Avec OpenRouter (routeur vers ~430 modèles ; --model obligatoire)
aipmt --use_openrouter --model 'z-ai/glm-5.2' --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### Über das eigene ChatGPT-Abonnement übersetzen (`--use_codex`)

Dieser Provider verwendet keinen API-Schlüssel: Er steuert die offizielle Codex CLI im
nicht interaktiven Modus, sodass die Übersetzung vom Kontingent des bereits bezahlten
ChatGPT-Abonnements (Plus, Pro, Business …) abgezogen wird. Dies ist der einzige von
OpenAI für diesen Anwendungsfall dokumentierte Weg — die Tokens von `~/.codex/auth.json` authentifizieren keine
Aufrufe der API Platform und werden von diesem Skript ohnehin niemals gelesen.

**Voraussetzungen:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Die Binärdatei wird in dieser Reihenfolge gesucht: in der Variablen `CODEX_BIN`, im `PATH`
und anschließend im Python-Paket `openai-codex-cli-bin`. Letzteres ist bewusst
nicht in `requirements.txt` enthalten: Es ist etwa 250 MB groß, was allen
Benutzern für einen optionalen Provider auferlegt würde.

**Wissenswertes:**

- **Es wird kein API-Schlüssel verwendet.** `OPENAI_API_KEY` und `CODEX_API_KEY` werden
  aus der Umgebung des Unterprozesses entfernt. Dadurch ist gewährleistet, dass ein in
  `.env` vorhandener Schlüssel niemals dazu führt, dass die Übersetzung auf eine nutzungsabhängige
  Abrechnung umgestellt wird.
- **Ein Segment = eine „lokale Nachricht“** im 5-Stunden-Zeitfenster des Tarifs.
  Verwenden Sie `--eco` (Modell `gpt-5.6-luna`, 250–2.000 Nachrichten/5 h bei Plus)
  anstelle des Qualitätsmodells (`gpt-5.6-sol`, 10–100 Nachrichten/5 h).
- **Langsamer** als ein API-Aufruf: Rechnen Sie mit etwa 45 s für eine vollständige README,
  gegenüber wenigen Sekunden bei einem direkten Aufruf.
- **In CI abgelehnt** (wenn `CI` oder `GITHUB_ACTIONS` definiert ist): Das Abonnement
  authentifiziert sich über eine persönliche Sitzungsdatei. Diese auf einen gemeinsam genutzten Runner
  zu übertragen, käme dem Hinterlegen einer Identität gleich, die von allem dort
  Ausgeführten wiederverwendet werden könnte. Verwenden Sie für diesen Weg einen API-Schlüssel.
- Umgebungsvariablen: `CODEX_BIN` (expliziter Pfad zur Binärdatei) und
  `CODEX_TIMEOUT` (Sekunden pro Segment, Standardwert `600`).

### Über das eigene Grok-Abonnement übersetzen (`--use_grok_cli`)

Dasselbe Prinzip wie bei `--use_codex`, jedoch mit der offiziellen CLI **Grok Build**: Die
Übersetzung wird vom Grok-Abonnement (SuperGrok / X Premium+) abgezogen, anstatt
pro Token abgerechnet zu werden.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Abschirmung — vor der Verwendung lesen.** Dieser Provider ist strukturell **schwächer**
als `--use_codex`, und das ist eine bewusste Entscheidung:

- Codex läuft in `--sandbox read-only`, einer vom System erzwungenen Grenze.
- Die Sandbox von Grok **kann auf vielen aktuellen Linux-Systemen nicht angewendet werden**:
  AppArmor blockiert seit Ubuntu 24.04 unprivilegierte User Namespaces, und die Deny-Liste
  für Container-Runtime-Sockets schlägt fehl, wenn `/run/podman` in `0700` enthalten ist.
  Ein **integriertes** Profil, das nicht angewendet werden kann, startet jedoch **unbemerkt ohne Abschirmung**.
- Das Skript fordert daher standardmäßig kein Profil an und **greift niemals unbemerkt
  auf einen Fallback zurück**: Es zeigt eine Warnung an. Die Abschirmung beruht auf den
  `--deny`-Regeln der CLI (einschließlich der Catch-all-Regel `*`), der einzigen gemessenen
  _fail-closed_-Schicht — eine unbekannte Regel führt dazu, dass der Start verweigert wird, anstatt
  den Schutz stillschweigend zu entfernen.
- So **erzwingen** Sie die OS-Sandbox: `GROK_TRANSLATE_SANDBOX=read-only`. Der
  Start schlägt fehl, wenn das System sie nicht umsetzen kann; dies ist das
  beabsichtigte Verhalten.

**Kontingent**: Der Grok-Pool gilt **wöchentlich und wird gemeinsam** mit Chat, Imagine und
Voice genutzt; es gibt keinen Befehl, mit dem er sich auslesen lässt. Eine Stapelverarbeitung kann daher
Ihre Nutzung für Unterhaltungen beeinträchtigen, ohne dass Sie darauf hingewiesen werden — daher die
auf 2 begrenzte Parallelität und eine Warnung in `regen_translations.sh`.

Weitere Variablen: `GROK_BIN` (Pfad zur Binärdatei), `GROK_TIMEOUT` (Standardwert 900 s).

Zur Neugenerierung der 28 Übersetzungen:

```bash
# Défaut : Codex sur l'abonnement ChatGPT, modèle qualité gpt-5.6-sol, 0 € à l'usage
./regen_translations.sh --force

# Le modèle éco de Codex, si le volume l'impose
REGEN_MODEL=gpt-5.6-luna ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Une API facturée (openai, gemini, grok, openrouter) est REFUSÉE sans cette dérogation nommée
REGEN_PROVIDER=openai REGEN_ALLOW_PAID_API=1 ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force

# Via OpenRouter : API facturée, donc dérogation ET modèle obligatoires
REGEN_PROVIDER=openrouter REGEN_ALLOW_PAID_API=1 REGEN_MODEL=z-ai/glm-5.2 ./regen_translations.sh --force
```
### Mit OpenCode übersetzen, zum Anbieter Ihrer Wahl (`--use_opencode`)

[OpenCode](https://opencode.ai) ist ein **Open-Source-Code-Agent (MIT)** für das
Terminal. Es ist kein Modellanbieter, sondern ein **Router** zu den Anbietern,
die Sie in OpenCode selbst konfiguriert haben: ein API-Schlüssel, ein Abonnement,
das OpenCode-Zen-Gateway – das kostenlose Modelle **ohne Konto** bereitstellt –
oder ein **lokales** Modell. Dieser Provider steuert `opencode run` im
nicht interaktiven Modus und beschränkt den Aufruf auf genau einen Durchlauf,
ganz ohne Tools.

Zwei dieser Wege wurden hier vollständig gemessen: das **Zen-Gateway** und
**Ollama** lokal. Die anderen von OpenCode angekündigten Wege (GitHub Copilot,
LM Studio, llama.cpp) sollten konstruktionsbedingt funktionieren, da der
Provider nur mit OpenCode kommuniziert – sie wurden jedoch nicht erprobt, und
dieses README beschreibt ausschließlich, was überprüft wurde.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` ist im Format `provider/modèle` **obligatorisch**. OpenCode ist kein
Anbieter, und es wird nicht in Ihrem Namen eine Standardeinstellung gewählt:
Sein eigener Fallback wäre ein kostenloses Modell, dessen Interaktionen zum
Training verwendet werden können.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Einschränkung – was das Skript bei jedem Aufruf tut:**

- Eine Inline-Konfiguration (`OPENCODE_CONFIG_CONTENT`), die Vorrang vor Ihrer eigenen hat,
  definiert einen Agenten `aipmt`, für den **alle Tools abgelehnt werden**
  (`permission: { "*": "deny" }`): Das Modell kann weder lesen noch schreiben noch Befehle
  ausführen – den Messungen zufolge versucht es dies nicht einmal. Das Teilen
  von Sitzungen ist deaktiviert, `--pure` schließt externe Plugins aus,
  niemals `--auto`.
- Der Aufruf läuft in einem **temporären, leeren Verzeichnis** mit den Schaltern
  `OPENCODE_DISABLE_PROJECT_CONFIG` und `OPENCODE_DISABLE_CLAUDE_CODE`: Ohne sie fügt OpenCode jedem Prompt die
  `AGENTS.md` des aktuellen Verzeichnisses und Ihre `~/.claude/CLAUDE.md` hinzu –
  bei Messungen wurde eine in einer `AGENTS.md` hinterlegte Anweisung,
  „jede Antwort mit BANANA beenden“, auf die Übersetzung angewendet. Die
  globalen Regeln von `~/.config/opencode/AGENTS.md` bleiben dagegen aktiv: OpenCode ermöglicht
  es nicht, sie auszuschließen.
- Der Ausgabevertrag verlangt gleichzeitig: Rückgabecode 0, kein
  `error`-Ereignis, keinen Tool-Aufruf, einen letzten in
  `stop` abgeschlossenen Schritt, einen nicht leeren Text und den
  tatsächlich geladenen Agenten – ein unbekannter `--agent` führt bei
  OpenCode nicht zu einem Fehler, sondern es **fällt stillschweigend** auf den
  Coding-Agenten mit aktiven Tools zurück. Auch ein `exit 0` beweist hier
  nichts.
- **Kein aipmt-Schlüssel wird an den Unterprozess weitergegeben** (dieselbe
  Filterung wie bei Codex und Grok), mit genau einer namentlich festgelegten
  Ausnahme: `OPENCODE_API_KEY`, dem Schlüssel von OpenCode selbst (Zen, Go). Die
  Anbieter werden in OpenCode konfiguriert (`opencode auth login`, `opencode.json`),
  nicht in der `.env` von aipmt.

**Wissenswertes:**

- **Die kostenlosen Zen-Modelle sind „Stealth“- oder Community-Modelle**,
  wechseln häufig, haben nicht dokumentierte Limits, und ihre Interaktionen
  können zum Training verwendet werden: ideal für öffentliche Dokumentation,
  für private Inhalte jedoch zu vermeiden. Gemessen: `opencode/mimo-v2.5-free` übersetzt
  dieses README in einem Durchlauf; `opencode/big-pickle` ist langsamer, und zwei
  gleichzeitige Anfragen blieben dort unbeantwortet.
- **Ein lokales Modell muss mindestens 16 k Kontext bieten** – die Segmente
  umfassen bis zu 16.000 Zeichen –, während Ollama häufig standardmäßig 4.096
  konfiguriert. Mit Ollama: eine `Modelfile` mit `PARAMETER num_ctx 32768`, dann
  `ollama create`. Die Qualität hängt vom Modell ab: Ein 7B-Modell kehrte in
  einer Testdatei eine Liste um und beschädigte die Begrenzung eines Codeblocks,
  während ein Gateway-Modell alles bewahrte.
- `--eco` hat keine Wirkung (das Modell ist das aus `--model`);
  `--reasoning_effort` wird unverändert als `--variant` von OpenCode
  weitergegeben und sollte nur angefordert werden, wenn das Modell es kennt.
- Die Sitzungen werden von OpenCode wie jede OpenCode-Sitzung in seiner
  Datenbank (`~/.local/share/opencode/`) protokolliert.
- Umgebungsvariablen: `OPENCODE_BIN` (expliziter Pfad zur Binärdatei,
  andernfalls `PATH` und anschließend `~/.opencode/bin/opencode`) sowie
  `OPENCODE_TIMEOUT` (Sekunden pro Segment, Standardwert `600`).
  `OPENCODE_CONFIG` wird, falls exportiert, nicht von `aipmt` gelesen:
  Es wird unverändert an OpenCode weitergegeben, das es berücksichtigt.

**Gemessenes Beispiel: ein lokales Modell über Ollama** (RTX 3060 12 GB, 62 GB RAM, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # conserve les modèles déjà téléchargés
ollama pull gpt-oss:20b                         # 13 Go, Apache 2.0 — le seul modèle local retenu ici

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

Anschließend der Anbieter in `~/.config/opencode/opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": { "baseURL": "http://127.0.0.1:11434/v1" },
      "models": {
        "gpt-oss-20b-32k": {
          "name": "gpt-oss 20B (32k, sans réflexion)",
          "limit": { "context": 32768, "output": 8192 },
          "options": { "reasoningEffort": "none" }
        }
      }
    }
  }
}
```

`reasoningEffort: "none"` ist kein Detail: Ollama aktiviert bei diesen Modellen
standardmäßig das Reasoning, und eine Modelfile kann es nicht deaktivieren.
Über OpenCode gemessen: Ohne die Option kostet „Die Katze schläft auf dem
Teppich“ 919 Reasoning-Tokens und 68 s; mit ihr 9 Tokens.

```bash
aipmt --use_opencode --model ollama/gpt-oss-20b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

Ergebnisse mit einem echten Blogartikel von 589 Zeilen (140 Links, 21
Abschnitte, 3 durch den Modus `--news` geschützte englische Zitate), mit
demselben Befehl und drei Modellen:

| Modell                                   | Dauer       | Struktur                                                     | Abweichungen                                                                                  |
| ---------------------------------------- | ----------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free` (Zen, kostenlos) | 4 min 26 s  | identisch mit der Quelle                                     | keine                                                                                         |
| `ollama/gemma4-12b-32k` (lokal)          | 10 min 10 s | Links, URLs, Tabellen, Tags, Fettdruck und Inline-Code identisch | eine erfundene Zitatzeile (🇺🇸 + Paraphrase), eine doppelte Zuschreibung                    |
| `ollama/qwen3.5-9b-32k` (lokal)          | 8 min 18 s  | Links, URLs, Tabellen und Tags identisch                     | eine erfundene Zitatzeile, einige hinzugefügte Fettdruck- und Inline-Code-Elemente, ein erneut verarbeitetes Segment |

Diese beiden lokalen Modelle wurden inzwischen **aussortiert**: Eine einzige
Eigenmächtigkeit pro Artikel genügt, um ein Modell für veröffentlichte
Übersetzungen zu disqualifizieren. Fünf weitere wurden aus denselben Gründen
oder wegen Zeitüberschreitungen aussortiert (`gemma4:26b-a4b`,
`qwen3.6:35b-a3b`, `ministral-3:14b`, `mistral-small3.2`, `hy-mt2:7b`). Nur
`gpt-oss:20b` wurde beibehalten – und selbst dieses lässt in einem dichten
Artikel französische Passagen stehen; siehe die Tabelle der empfohlenen
Modelle.

Während der lokalen Übersetzung: GPU-Auslastung von 98 % bei 170 W, 10 GB
belegter VRAM (Modell und Cache für 32 k Tokens, nichts in den RAM ausgelagert),
7,5 GB RAM für den Ollama-Server. Ein Modell mit 9 bis 12 Milliarden Parametern
bewahrt die Struktur, nimmt sich aber pro Artikel eine Freiheit, während das
Gateway-Modell sich keine nahm: vor der Veröffentlichung Korrektur lesen oder
nur für Entwürfe verwenden.

### Über OpenRouter übersetzen (`--use_openrouter`)

OpenRouter ist ein **Router** vor mehr als 400 von Drittanbietern gehosteten
Modellen, deren Nutzung über ein gemeinsames Guthaben abgerechnet wird. Mit
einem einzigen Schlüssel bietet er Zugriff auf Modelle, die keiner der anderen
Provider bereitstellt, insbesondere offene chinesische Modelle.

```bash
# --model est OBLIGATOIRE : aucun défaut n'est choisi à votre place
aipmt --use_openrouter --model 'z-ai/glm-5.2' --file README.md \
  --target_dir . --source_lang fr --target_lang en
```

Zwei Besonderheiten des Routings bestimmten die Implementierung, und beide sind
messbar:

- **Dasselbe Modell wird von Dutzenden Hostern mit unterschiedlichen Limits
  bereitgestellt.** Bei `z-ai/glm-5.3-flash` gibt es 23 Hoster, darunter einen mit
  einem Limit von 2.048 Ausgabe-Tokens: Ohne Vorsichtsmaßnahme wurde eine von 23
  langen Übersetzungen abgeschnitten, zufällig durch das Routing und ohne
  jeglichen Hinweis. Ein Preflight liest `/api/v1/models/{modèle}/endpoints`, schließt Hoster mit
  weniger als 8.000 Ausgabe-Tokens oder mit beeinträchtigtem Status aus und
  fixiert anschließend die übrigen mit `allow_fallbacks: false` – andernfalls wechselt
  der Router wieder zu einem ausgeschlossenen Hoster.
- **Reasoning wird zum Ausgabetarif abgerechnet.** Dieselbe Anfrage an
  `z-ai/glm-5.2`, Antwort „OK“: 107 Completion-Tokens mit der
  Standardeinstellung des Modells, 2 bei deaktiviertem Reasoning. Daher ist es
  bei Modellen, die dies erlauben, standardmäßig deaktiviert. Modelle, die es
  erzwingen – `reasoning.mandatory`, 288 der 431 Modelle im Katalog –, erhalten den
  **niedrigsten von ihnen als akzeptiert angegebenen Aufwand** und nicht ihre
  Standardeinstellung: Die von `z-ai/glm-5.3-flash` ist `max` und
  verbrauchte die 32.768 Ausgabe-Tokens vollständig, bevor die Übersetzung
  beendet war. Eine Vergrößerung des Budgets hätte daran nichts geändert, da
  der Aufwand einen prozentualen Anteil davon belegt. `--reasoning_effort` behält
  Vorrang, und `none` wird bei einem Modell, das Reasoning erzwingt,
  gemeldet, statt umgangen zu werden.

Der Preflight arbeitet **fail-closed** und zeigt seine Auswahl an:

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

Ein im Katalog fehlender Slug, ein nicht erreichbarer Katalog oder das Fehlen
eines Hosters, der das Limit erfüllt, beendet den Befehl vor jeder Abrechnung.

Weitere Punkte:

- Das Kontextfenster stammt aus dem Katalog und nicht aus einer Konstanten:
  Die Segmentierung passt sich tatsächlich daran an, auch bei Modellen mit
  4.095 Tokens.
- `--eco` hat keine Wirkung (das Modell ist das aus `--model`).
- `finish_reason=length` mit leerer Ausgabe bedeutet keine Abschneidung, sondern ein
  durch das Reasoning aufgebrauchtes Budget; die Meldung weist darauf hin, da
  beide Fälle gegensätzliche Maßnahmen erfordern.
- Umgebungsvariablen: `OPENROUTER_API_KEY` (Schlüssel, unter
  <https://openrouter.ai/keys>), `OPENROUTER_BASE_URL` (Standardwert
  `https://openrouter.ai/api/v1`, `https://` erforderlich), `OPENROUTER_TIMEOUT`
  (Sekunden pro Aufruf, Standardwert `900`) und `OPENROUTER_PREFLIGHT_TIMEOUT`
  (Standardwert `30`).

### Sparmodus

Verwendet schnellere und kostengünstigere Modelle (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Optionen

| Option                   | Beschreibung                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Einzelne zu übersetzende Markdown-Datei                                                                       |
| `--source_dir`           | Quellverzeichnis mit den Markdown-Dateien                                                                     |
| `--target_dir`           | Ausgabeverzeichnis für die übersetzten Dateien                                                                |
| `--source_lang`          | Ausgangssprache (Standardwert: `fr`)                                                               |
| `--target_lang`          | Zielsprache (Standardwert: `en`)                                                                   |
| `--model`                | Zu verwendendes spezifisches Modell                                                                           |
| `--eco`                  | Kostengünstige Modelle verwenden                                                                              |
| `--use_mistral`          | Mistral-AI-API verwenden                                                                                      |
| `--use_claude`           | Claude-API verwenden                                                                                          |
| `--use_gemini`           | Gemini-API verwenden                                                                                          |
| `--use_codex`            | Codex CLI mit dem Kontingent des ChatGPT-Abonnements verwenden                                                |
| `--use_grok`             | xAI-API (Grok) verwenden – erfordert `XAI_API_KEY`                                                          |
| `--use_openrouter`       | OpenRouter verwenden – erfordert `OPENROUTER_API_KEY` und `--model fournisseur/modèle`                                          |
| `--use_grok_cli`         | Grok CLI mit dem Kontingent des Grok-Abonnements verwenden                                                    |
| `--use_opencode`         | OpenCode (Open Source) mit dem in OpenCode konfigurierten Anbieter verwenden; erfordert `--model provider/modèle`       |
| `--force`                | Erneute Übersetzung erzwingen                                                                                  |
| `--keep_filename`        | Ursprünglichen Dateinamen beibehalten                                                                          |
| `--news`                 | Nachrichtenmodus: schützt englische Zitate und verwaltet Flaggen nach Sprache                                 |
| `--add_translation_note` | Übersetzungshinweis hinzufügen                                                                                 |
| `--note_position`        | Position des Hinweises: `top`, `bottom` (Standardwert) oder `both`                  |
| `--note_format`          | Format des Hinweises: `legacy` (Standardwert, fett gedruckter Absatz) oder `marker`             |
| `--include_model`        | Modellnamen in die Ausgabedatei aufnehmen                                                                      |
| `--reasoning_effort`     | GPT-5.x-Reasoning-Aufwand: `none`/`low`/`medium`/`high`/`xhigh`     |

> **Die acht Provider-Flags schließen sich gegenseitig aus.** Zuvor wurde eine
> Kombination aus zwei Flags stillschweigend akzeptiert und auf das zuerst
> geprüfte aufgelöst: Eine über das Abonnementkontingent angeforderte Übersetzung
> (`--use_codex`, `--use_grok_cli`) konnte dadurch ohne jede Warnung über die
> nutzungsabhängige Abrechnung laufen. `argparse` lehnt die Kombination
> nun ab.

### Übersetzungshinweis: Positionen und Formate

Mit `--add_translation_note` kann der Translator den Hinweis oben, unten oder an beiden
Stellen platzieren und ihn entweder im einfachen Textformat
(abwärtskompatibel) oder im von einem Markdown-Plugin verarbeitbaren Format
`marker` ausgeben.

**Position** (`--note_position`):

- `bottom` (Standardwert): Hinweis am Dateiende, wie bisher.
- `top`: Hinweis wird **nach dem YAML-Frontmatter** eingefügt
  (sicher für Astro Content Collections, gray-matter usw.).
- `both`: Hinweis wird oben UND unten eingefügt (ein einziger
  LLM-Aufruf, dessen Inhalt für beide Positionen wiederverwendet wird).

**Format** (`--note_format`):

- `legacy` (Standardwert): fett gedruckter Absatz `**...**` –
  Verhalten strikt identisch mit v1.8, Byte für Byte. Kompatibel mit Hugo,
  GitHub, GitLab und jedem Markdown-Renderer.
- `marker`: unsichtbare Markdown-Linkreferenzdefinition
  (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), gefolgt von einem fett gedruckten Blockquote. Nativ auf
  GitHub/GitLab lesbar und beim Build von einem Remark-Plugin auf der
  Astro-Seite nutzbar, um ein stilisiertes Banner zu erzeugen (siehe Blog
  jls42.org).

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

| Provider   | Qualität (Standardwert)                 | Sparmodus (`--eco`) |
| ---------- | ---------------------------------------- | --------------------------- |
| OpenAI     | `gpt-5.6-terra`                          | `gpt-5.6-luna`             |
| Claude     | `claude-sonnet-5`                          | `claude-haiku-4-5`             |
| Mistral    | `mistral-large-latest`                          | `mistral-small-latest`             |
| Gemini     | `gemini-3.7-flash`                          | `gemini-3.1-flash-lite`             |
| Codex      | `gpt-5.6-sol`                          | `gpt-5.6-luna`             |
| Grok API   | `grok-4.6`                          | `grok-4.3`             |
| Grok CLI   | `grok-4.6`                          | `grok-4.5`             |
| OpenCode   | `--model provider/modèle` obligatorisch            | identisch – `--eco` ohne Wirkung |
| OpenRouter | `--model fournisseur/modèle` obligatorisch            | identisch – `--eco` ohne Wirkung |
## Welche Modelle sich bewähren

Ein Modell, das einen Absatz gut übersetzt, bewahrt nicht zwangsläufig die Struktur
eines gesamten Dokuments. Diese Messwerte stammen aus **tatsächlich
ausgeführten Übersetzungen** mit dem weiter oben beschriebenen Befehl, anhand von drei
Dokumentsätzen und vierzehn Zielsprachen: en, es, de, it, pt, nl, pl, sv, ro, ja,
ko, zh, ar, hi.

Zwei Spalten, die nicht dasselbe aussagen. **Erstellt** zählt die
erfolgreich abgeschlossenen Übersetzungen – die Schutzmechanismen des Skripts
gegen unbemerkte Fehler lassen die Datei passieren. **Ohne Abweichung** zählt diejenigen, deren Struktur
mit der Quelle identisch ist: dieselben Abschnitte, dieselben Links, dieselben URLs, dieselben Blöcke und
Inline-Codes, dieselben Tabellen, dieselben Zitate, dieselben Flags.

### Detaillierter Blogartikel, Modus `--news`

589 Zeilen, 140 Links, 21 Abschnitte, 3 geschützte englische Zitate. Dies ist das
anspruchsvollste der drei Dokumente: Der Modus `--news` ergänzt die Markdown-Struktur um
zusätzliche Anforderungen an Flags und Zitate.

| Modell                            | Zugang              | Erstellt | Ohne Abweichung | Median/Sprache |
| --------------------------------- | ------------------ | ------- | ---------- | -------------- |
| `gemini-3.7-flash`                | Google API         | 14/14   | **14/14**  | 1 Min. 18 Sek.     |
| `gpt-5.6-sol` (`--use_codex`)     | ChatGPT-Abonnement | 14/14   | **14/14**  | 11 Min. 28 Sek.    |
| `z-ai/glm-5.2`                    | OpenRouter         | 14/14   | **14/14**  | 5 Min. 37 Sek.     |
| `qwen/qwen3.8-flash`              | OpenRouter         | 14/14   | 13/14      | 26 Min. 23 Sek.    |
| `z-ai/glm-5.3-flash`              | OpenRouter         | 12/14   | 12/14      | 15 Min. 49 Sek.    |
| `qwen/qwen3.5-27b`                | OpenRouter         | 7/9     | 7/9        | 20 Min. 33 Sek.    |
| `claude-sonnet-5`                 | Anthropic API      | 14/14   | 11/14      | 6 Min. 31 Sek.     |
| `opencode/mimo-v2.5-free`         | OpenCode Zen       | 13/14   | 11/14      | 9 Min. 27 Sek.     |
| `qwen/qwen3.7-flash`              | OpenRouter         | 13/14   | 7/14       | 10 Min. 09 Sek.    |
| `ollama/gpt-oss-20b-32k`          | lokal              | 10/14   | 7/14       | 12 Min. 39 Sek.    |
| `mistral-large-latest`            | Mistral API        | 11/14   | 5/14       | 5 Min. 32 Sek.     |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter         | 4/14    | 3/14       | 37 Min. 27 Sek.    |
| `grok-4.6` (`--use_grok_cli`)     | Grok-Abonnement    | 1/14    | 1/14       | 23 Min. 11 Sek.    |
| `moonshotai/kimi-k2.6`            | OpenRouter         | 1/4     | 1/4        | 23 Min. 00 Sek.    |

Zwei Durchläufe wurden **wegen fehlenden Guthabens abgebrochen**, was sich in ihrem Nenner widerspiegelt:
`qwen3.5-27b` stoppte nach neun Sprachen, `kimi-k2.6` nach vier – Letzteres
nach einer Zeitüberschreitung von vierzig Minuten und zwei Ablehnungen, bei fast
0,33 $ pro Sprache.

Ein methodischer Vorbehalt zu den OpenRouter-Zeilen: Sie wurden mit den
**Standardeinstellungen des Routers** gemessen, bevor `--use_openrouter` existierte.
`z-ai/glm-5.2` wurde inzwischen mit dem mitgelieferten Provider und deaktiviertem Reasoning
erneut gemessen und erzielt exakt dasselbe Ergebnis von 14/14. `z-ai/glm-5.3-flash` scheiterte zweimal,
weil das standardmäßige Ausgabelimit des Routers ausgeschöpft war; der Provider fordert von
diesen Modellen nun die niedrigste von ihnen akzeptierte Reasoning-Stufe an, und der Kontrolltest mit den
betroffenen Sprachen ist erfolgreich.

### README dieses Projekts, Standard-Markdown

508 Zeilen, 219 Inline-Codes, 40 Blockbegrenzungen, 45 Tabellenzeilen. Hier gibt es
keinen Modus `--news`: Die Schwierigkeit liegt in der hohen Code-Dichte.

| Modell                        | Erstellt | Ohne Abweichung | Median/Sprache |
| ----------------------------- | ------- | ---------- | -------------- |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14   | 11/14      | 1 Min. 22 Sek.     |
| `gemini-3.7-flash`            | 14/14   | 13/14      | 21 Sek.           |
| `gpt-5.6-sol` (`--use_codex`) | 14/14   | 12/14      | 2 Min. 04 Sek.     |
| `opencode/mimo-v2.5-free`     | 9/14    | 7/14       | 3 Min. 25 Sek.     |
| `ollama/gpt-oss-20b-32k`      | 9/14    | 1/14       | 3 Min. 38 Sek.     |

### Vier README-Dateien bekannter Projekte

FastAPI, Ollama, tldr-pages und Vue.js, unverändert von GitHub übernommen. Diese Dokumente
sind **einfacher** als die beiden vorherigen, wie die Tabelle zeigt.

| Modell                    | Umfang                  | Erstellt | Ohne Abweichung |
| ------------------------- | -------------------------- | ------- | ---------- |
| `opencode/mimo-v2.5-free` | 4 Projekte × 14 Sprachen     | 55/56   | 47/56      |
| `grok-4.6` (Abonnement)   | 4 Projekte × ar, hi, ja, zh | 16/16   | 14/16      |
| `ollama/gpt-oss-20b-32k`  | 4 Projekte × ar, hi, ja, zh | 15/16   | 9/16       |

### Was wir daraus lernen

- **Drei Modelle haben bei den beiden umfangreichen Dokumenten nie Informationen verloren**:
  `gemini-3.7-flash`, `gpt-5.6-sol` über das ChatGPT-Abonnement und
  `z-ai/glm-5.2` über OpenRouter. Ihre einzigen Abweichungen im Standardmodus bestehen aus einem
  Paar nicht übernommener `**` in einer oder zwei Sprachen, niemals aus einer URL, einem Codeblock
  oder einem Zitat.
- **Der entscheidende Faktor ist die Dokumentdichte, nicht der Modus `--news`.**
  Grok über das Abonnement scheitert beim Blogartikel in 13 von 14 Fällen und bewältigt 14
  von 16 öffentlichen README-Dateien: Die Fehlerursache ist ein Abbruch bei langen Segmenten,
  was durch einen Kontrolltest bestätigt wurde – die isolierte Passage wird korrekt übersetzt.
- **Nichtlateinische Schriften sind nicht die erwartete Trennlinie.** `gpt-oss` lässt
  Passagen auf Französisch im Arabischen, Japanischen, Polnischen **und Rumänischen** stehen; Mistral
  und MiMo verlieren Inline-Codes nur bei nichtlateinischen Schriften.
- **Das Deaktivieren des Reasonings beeinträchtigt die Qualität nicht.** `z-ai/glm-5.2` bewältigt
  unter beiden Bedingungen vierzehn Sprachen ohne eine einzige Abweichung – mit dem standardmäßig
  aktiven Reasoning des Routers und anschließend durch `--use_openrouter` deaktiviert – bei achtzehnmal
  weniger abgerechneten Ausgabe-Tokens. Diese Messung rechtfertigt die
  Standardeinstellung des Providers.
- **Ein langsames Modell ist kein sicheres Modell.** `deepseek-v4-flash-0731` benötigt 37
  Minuten pro Sprache für 4 von 14 Übersetzungen, `qwen3.8-flash` 26 Minuten für
  ein nahezu perfektes Ergebnis und Gemini 1 Minute 18 Sekunden für ein fehlerfreies Ergebnis.

### Was diese Tabelle nicht ist

- **Sie ist keine umfassende Rangliste.** Allein OpenRouter bietet mehr als
  vierhundert Modelle an; etwa fünfzehn wurden hier gemessen. Das Fehlen eines
  Modells sagt nichts über seine Qualität aus, sondern lediglich, dass es nicht getestet wurde.
- **Diese Messwerte haben ein Datum**: den 4. und 5. September 2026. Modelle ändern sich
  unter demselben Namen, Hostinganbieter passen Quantisierung und Limits an, und jede
  Woche erscheinen neue Modelle.
- **Die Laufzeiten stellen keine Rangfolge dar.** Je nach Testreihe liefen 3 bis 6 Übersetzungen
  gleichzeitig, und der Durchsatz eines Anbieters schwankt im Tagesverlauf.
  Sie liefern eine Größenordnung, keinen Vergleich.
- **Ein Ergebnis hängt ebenso sehr vom Dokument wie vom Modell ab.** Dasselbe Modell
  bewältigt vierzehn Sprachen bei einem Artikel und neun bei diesem README. Ihre Dateien sind nicht
  unsere.
- **Der richtige Ansatz bleibt, selbst zu messen**: Übersetzen Sie eines Ihrer
  Dokumente in Ihre Zielsprachen und vergleichen Sie anschließend die Struktur – die Anzahl der
  Abschnitte, Links, unterschiedlichen URLs, Codeblöcke, Inline-Codes und
  Tabellenzeilen. Genau das leistet das oben beschriebene Protokoll, und es
  passt in eine Schleife über `aipmt`.

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** - Mehrsprachiger persönlicher Blog (15 Sprachen)

## Autor

Julien LE SAUX
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artikel, mit gpt-5.6-sol aus dem Französischen ins Deutsche übersetzt.**

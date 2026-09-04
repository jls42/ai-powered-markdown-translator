# KI-gestützter Markdown-Übersetzer

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Codequalität</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status des Quality Gates"></a>
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
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy-Badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Übersetzer für Markdown-Dateien mit **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** und **Grok (xAI)** — per API, über das Kontingent eines ChatGPT- (Codex) oder Grok-Abonnements ohne nutzungsabhängige Abrechnung oder über **OpenCode**, den Open-Source-Agenten, mit einem Anbieter Ihrer Wahl: lokales Modell (Ollama), kostenloser Anbieter, Abonnement (GitHub Copilot …) oder Schlüssel.

Dieses Python-Skript übersetzt Markdown-Dateien von einer Ausgangssprache in eine Zielsprache und bewahrt dabei Formatierung, Codeblöcke und Front-Matter-Metadaten.

## Hauptmerkmale

- **Mehrere Anbieter**: 5 APIs (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLIs über ein Abonnement ohne nutzungsabhängige Abrechnung — Codex (ChatGPT) und Grok — + OpenCode (Open Source, MIT) für jeden in OpenCode konfigurierten Anbieter, einschließlich eines lokalen Modells
- **Modelle 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Sparmodus**: Option `--eco` zur Verwendung schnellerer und kostengünstigerer Modelle
- **Einzelne Datei**: Option `--file` zur Übersetzung einer einzelnen Datei
- **Intelligente Segmentierung**: Verarbeitung langer Texte unter Berücksichtigung der Token-Limits jedes Modells
- **Bewahrung von Code**: Codeblöcke UND Inline-Code (`` `...` ``) bleiben erhalten
- **Dateiname**: Option `--keep_filename` zur Beibehaltung des ursprünglichen Namens
- **Nachrichtenmodus**: Option `--news` zum Schutz englischer Zitate und zur Behandlung von Flaggen in Nachrichtenartikeln
- **.env-Konfiguration**: Unterstützung der Datei `.env` für API-Schlüssel
- **Übersetzungshinweis**: Optionales Hinzufügen eines Hinweises am Dokumentende

## Installation

### Zur Verwendung des Werkzeugs

```bash
pip install ai-powered-markdown-translator
```

Der Befehl `aipmt` ist anschließend überall verfügbar. Falls sich das Verzeichnis der Python-Skripte nicht in Ihrem `PATH` befindet, bewirkt `python -m aipmt` genau dasselbe. Python 3.10 oder neuer.

Für eine von Ihren übrigen Paketen isolierte Installation:

```bash
pipx install ai-powered-markdown-translator
```

### Zur Mitarbeit am Projekt

Das geklonte Repository bleibt für die Entwicklung erforderlich: Dort befinden sich die Tests, die 28 Übersetzungen und sämtliche Werkzeuge zur Qualitätssicherung.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` ist eine **vollständig festgeschriebene Lockdatei**, die exakt die getestete Umgebung widerspiegelt. Die in `pyproject.toml` veröffentlichten Versionsgrenzen sind bewusst weiter gefasst: Sie schreiben Ihren anderen Paketen nichts vor.

### Werkzeuge zur Qualitätssicherung (optional, aber empfohlen)

Das Projekt verwendet [`pre-commit`](https://pre-commit.com), um zu verhindern, dass falsch formatierter, anfälliger oder ein Geheimnis enthaltender Code committet wird. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktive Hooks: ruff (Linting und Formatierung), shellcheck (Bash), prettier (Markdown/YAML/JSON), Lizard (Komplexität), detect-secrets (API-Schlüssel), mypy (schrittweise Typisierung), Opengrep (SAST), pip-audit (CVE-Abhängigkeiten), unittest. Einzelheiten finden Sie in `CLAUDE.md` im Abschnitt _Quality / pre-commit_.

## Konfiguration

Die Schlüssel werden an **drei Stellen** gesucht, von der höchsten bis zur niedrigsten Priorität.
Jede Stelle ergänzt lediglich, was die vorherige offenlässt.

|     | Wo                                            | Wofür                                  |
| --- | --------------------------------------------- | -------------------------------------- |
| 1   | Umgebungsvariablen                            | CI, Container, punktuelle Abweichungen |
| 2   | `.env` im aktuellen Verzeichnis (oder einem übergeordneten Verzeichnis) | projektspezifischer Schlüssel          |
| 3   | `~/.config/aipmt/.env`                        | **einmal installiert, überall gültig** |

Nach einem `pip install` ist die dritte Möglichkeit am einfachsten:

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

Diese Datei folgt `XDG_CONFIG_HOME`, wenn die Variable einen absoluten Pfad bezeichnet
(andernfalls wird sie gemäß der Spezifikation ignoriert), sowie `%APPDATA%`
unter Windows.

Die zweite Möglichkeit bleibt nützlich, wenn ein Repository über einen eigenen Schlüssel verfügt: Eine Datei `.env` in seinem Stammverzeichnis hat dann Vorrang vor der Benutzerkonfiguration, ohne diese zu verändern. Eine bereits in der Umgebung definierte Variable hat wiederum Vorrang vor beiden:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Wird kein Schlüssel gefunden, zeigt der Befehl keinen Aufruf-Trace an, sondern
listet die drei Speicherorte mit ihrem exakten Pfad auf.

`GEMINI_API_KEY` wird als Alternative zu `GOOGLE_API_KEY` akzeptiert (AI-Studio-Konvention). Optionale Variablen: `XAI_BASE_URL` (xAI-Endpunkt, Standardwert
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (Sekunden pro Anthropic-Aufruf, Standardwert
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (siehe Abschnitt Grok CLI) und `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (siehe Abschnitt OpenCode). Für
`regen_translations.sh`: `REGEN_PROVIDER` (Standardwert `codex`, über ein Abonnement),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (zwingend erforderliche Ausnahme für eine
kostenpflichtige API) und `REGEN_JOB_TIMEOUT` (Obergrenze pro Job, standardmäßig 600 s, 1.800 s unter Codex).

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

### Über das eigene ChatGPT-Abonnement übersetzen (`--use_codex`)

Dieser Anbieter verwendet keinen API-Schlüssel: Er steuert die offizielle Codex CLI im nicht interaktiven Modus, sodass die Übersetzung auf das Kontingent des bereits bezahlten ChatGPT-Abonnements (Plus, Pro, Business …) angerechnet wird. Dies ist der einzige von OpenAI dokumentierte Weg für diese Verwendung — die Token von `~/.codex/auth.json` authentifizieren keine Aufrufe der API Platform und werden von diesem Skript auch niemals gelesen.

**Voraussetzungen:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Die Binärdatei wird in dieser Reihenfolge gesucht: in der Variablen `CODEX_BIN`, im `PATH` und anschließend im Python-Paket `openai-codex-cli-bin`. Letzteres ist bewusst nicht in `requirements.txt` enthalten: Es ist etwa 250 MB groß, was sonst allen Benutzern für einen optionalen Anbieter auferlegt würde.

**Wissenswertes:**

- **Es wird kein API-Schlüssel verwendet.** `OPENAI_API_KEY` und `CODEX_API_KEY` werden
  aus der Umgebung des Unterprozesses entfernt. Dadurch ist gewährleistet, dass ein in
  `.env` vorhandener Schlüssel die Übersetzung niemals auf eine nutzungsabhängige
  Abrechnung umstellt.
- **Ein Segment = eine „lokale Nachricht“** im 5-Stunden-Fenster des Tarifs.
  Verwenden Sie `--eco` (Modell `gpt-5.6-luna`, 250–2.000 Nachrichten/5 h bei Plus)
  anstelle des Qualitätsmodells (`gpt-5.6-sol`, 10–100 Nachrichten/5 h).
- **Langsamer** als ein API-Aufruf: Rechnen Sie mit etwa 45 s für eine vollständige README,
  gegenüber wenigen Sekunden bei einem direkten Aufruf.
- **In CI abgelehnt** (`CI` oder `GITHUB_ACTIONS` definiert): Die Authentifizierung
  über ein Abonnement ist nicht für einen gemeinsam genutzten Runner vorgesehen, und OpenAI
  rät von diesem Workflow in öffentlichen Repositorys ab. Verwenden Sie für diesen Weg einen API-Schlüssel.
- Umgebungsvariablen: `CODEX_BIN` (expliziter Pfad zur Binärdatei) und
  `CODEX_TIMEOUT` (Sekunden pro Segment, Standardwert `600`).

### Über das eigene Grok-Abonnement übersetzen (`--use_grok_cli`)

Dasselbe Prinzip wie bei `--use_codex`, jedoch mit der offiziellen CLI **Grok Build**: Die Übersetzung wird auf das Grok-Abonnement (SuperGrok / X Premium+) angerechnet, anstatt pro Token abgerechnet zu werden.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Abschirmung — vor der Verwendung lesen.** Dieser Anbieter ist strukturell **schwächer** als `--use_codex`, und das ist eine bewusste Entscheidung:

- Codex läuft in `--sandbox read-only`, einer vom System vorgegebenen Grenze.
- Die Sandbox von Grok **kann auf vielen aktuellen Linux-Rechnern nicht angewendet werden**:
  AppArmor blockiert seit Ubuntu 24.04 unprivilegierte User Namespaces, und die Deny-Liste
  für Sockets der Container-Runtime schlägt fehl, wenn `/run/podman` in `0700`
  enthalten ist. Ein **integriertes** Profil, das nicht angewendet werden kann, startet jedoch
  **stillschweigend ohne Abschirmung**.
- Das Skript fordert daher standardmäßig kein Profil an und **weicht niemals stillschweigend
  aus**: Es zeigt eine Warnung an. Die Abschirmung beruht auf den Regeln `--deny`
  der CLI (einschließlich der Catch-all-Regel `*`), der einzigen gemessenen
  _Fail-Closed_-Schicht — eine unbekannte Regel verhindert den Start, anstatt den Schutz
  kommentarlos zu entfernen.
- Um die Betriebssystem-Sandbox **zwingend vorauszusetzen**: `GROK_TRANSLATE_SANDBOX=read-only`. Der Start
  schlägt fehl, wenn der Rechner sie nicht umsetzen kann; dies ist das beabsichtigte
  Verhalten.

**Kontingent**: Der Grok-Pool gilt **wöchentlich und wird gemeinsam** mit Chat, Imagine und
Voice genutzt; außerdem kann er mit keinem Befehl abgefragt werden. Eine Stapelverarbeitung
kann daher Ihre Nutzung für Unterhaltungen einschränken, ohne dass darauf hingewiesen wird —
deshalb ist die Parallelität auf 2 begrenzt und `regen_translations.sh` enthält eine Warnung.

Weitere Variablen: `GROK_BIN` (Pfad zur Binärdatei), `GROK_TIMEOUT` (Standardwert 900 s).

Zur Neugenerierung der 28 Übersetzungen:

```bash
# Défaut : Codex sur l'abonnement ChatGPT, modèle qualité gpt-5.6-sol, 0 € à l'usage
./regen_translations.sh --force

# Le modèle éco de Codex, si le volume l'impose
REGEN_MODEL=gpt-5.6-luna ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Une API facturée (openai, gemini, grok) est REFUSÉE sans cette dérogation nommée
REGEN_PROVIDER=openai REGEN_ALLOW_PAID_API=1 ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
```

### Mit OpenCode über einen beliebigen Anbieter übersetzen (`--use_opencode`)

[OpenCode](https://opencode.ai) ist ein **Open-Source-Code-Agent (MIT)** für das
Terminal. Es ist kein Modellanbieter, sondern ein **Router** zu den Anbietern,
die Sie in OpenCode selbst konfiguriert haben: ein API-Schlüssel, ein Abonnement
(GitHub Copilot, ChatGPT, SuperGrok), das OpenCode-Zen-Gateway — das kostenlose
Modelle **ohne Konto** bereitstellt — oder ein **lokales** Modell (Ollama, LM Studio,
llama.cpp). Dieser Anbieter steuert `opencode run` im nicht interaktiven Modus und
beschränkt den Aufruf auf einen einzigen Austausch ohne jegliche Werkzeuge.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` ist **zwingend erforderlich**, im Format `provider/modèle`. OpenCode ist
kein Anbieter, und es wird kein Standardwert für Sie ausgewählt: Der eigene Fallback
wäre ein kostenloses Modell, dessen Interaktionen zu Trainingszwecken verwendet werden können.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Abschirmung — was das Skript bei jedem Aufruf tut:**

- Eine Inline-Konfiguration (`OPENCODE_CONFIG_CONTENT`), die Vorrang vor Ihrer
  Konfiguration hat, definiert einen Agenten `aipmt`, für den **alle Werkzeuge
  abgelehnt werden** (`permission: { "*": "deny" }`): Das Modell kann weder lesen noch schreiben
  noch Befehle ausführen — Messungen zufolge versucht es dies nicht einmal. Die
  Sitzungsfreigabe ist deaktiviert, `--pure` schließt externe Plugins aus,
  niemals `--auto`.
- Der Aufruf läuft in einem **temporären und leeren Verzeichnis** mit den Schaltern
  `OPENCODE_DISABLE_PROJECT_CONFIG` und `OPENCODE_DISABLE_CLAUDE_CODE`: Ohne sie fügt OpenCode jedem Prompt die Datei
  `AGENTS.md` des aktuellen Verzeichnisses und Ihre Datei `~/.claude/CLAUDE.md` hinzu —
  Messungen zufolge wurde eine Anweisung „jede Antwort mit BANANA beenden“ aus einer
  Datei `AGENTS.md` auf die Übersetzung angewendet. Die globalen Regeln von
  `~/.config/opencode/AGENTS.md` werden dagegen weiterhin angewendet: OpenCode bietet keine Möglichkeit,
  sie auszuschließen.
- Der Ausgabevertrag verlangt gleichzeitig: Rückgabecode 0, kein Ereignis
  `error`, keinen Werkzeugaufruf, einen letzten mit `stop`
  abgeschlossenen Schritt, einen nicht leeren Text und einen tatsächlich geladenen
  Agenten — ein unbekannter `--agent` führt bei OpenCode nicht zu einem Fehler,
  sondern es **fällt stillschweigend** auf den Coding-Agenten mit aktiven Werkzeugen
  zurück. Auch ein `exit 0` beweist hier nichts.
- **Kein Schlüssel von aipmt wird an den Unterprozess weitergegeben** (dieselbe Filterung
  wie bei Codex und Grok), mit einer namentlich festgelegten Ausnahme: `OPENCODE_API_KEY`,
  dem Schlüssel von OpenCode selbst (Zen, Go). Die Anbieter werden in OpenCode
  (`opencode auth login`, `opencode.json`) konfiguriert, nicht in der Datei `.env`
  von aipmt.

**Wissenswertes:**

- **Die kostenlosen Zen-Modelle sind „Stealth“- oder Contributor-Modelle**,
  wechseln häufig, haben undokumentierte Limits und ihre Interaktionen können
  zu Trainingszwecken verwendet werden: ideal für öffentliche Dokumentation,
  aber bei privaten Inhalten zu vermeiden. Gemessen: `opencode/mimo-v2.5-free` übersetzt
  diese README in einem Durchgang; `opencode/big-pickle` ist langsamer, und zwei
  gleichzeitige Anfragen blieben dort unbeantwortet.
- **Ein lokales Modell muss mindestens 16 k Kontext bieten** — die Segmente umfassen
  bis zu 16.000 Zeichen — während Ollama standardmäßig häufig 4.096 konfiguriert.
  Mit Ollama: eine Datei `Modelfile` mit `PARAMETER num_ctx 32768`, anschließend
  `ollama create`. Die Qualität hängt vom Modell ab: Ein 7B-Modell kehrte in einer
  Testdatei eine Liste um und beschädigte den Abschluss eines Codeblocks, während
  ein Gateway-Modell alles bewahrte.
- `--eco` hat keine Wirkung (das Modell wird durch `--model` festgelegt);
  `--reasoning_effort` wird unverändert als `--variant` von OpenCode weitergegeben und
  sollte nur angefordert werden, wenn das Modell ihn kennt.
- Die Sitzungen werden von OpenCode wie jede andere OpenCode-Sitzung in seiner
  Datenbank (`~/.local/share/opencode/`) protokolliert.
- Umgebungsvariablen: `OPENCODE_BIN` (expliziter Pfad zur Binärdatei,
  andernfalls `PATH` und anschließend `~/.opencode/bin/opencode`) sowie `OPENCODE_TIMEOUT`
  (Sekunden pro Segment, Standardwert `600`). `OPENCODE_CONFIG` wird
  berücksichtigt, wenn Sie es exportieren.

**Gemessenes Beispiel: ein lokales Modell über Ollama** (RTX 3060 12 GB, 62 GB RAM, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # Ollama ≥ 0.30 pour gemma4 ; conserve les modèles déjà téléchargés
ollama pull gemma4:12b                          # 7,6 Go, Apache 2.0, 140+ langues
ollama pull qwen3.5:9b                          # 6,6 Go, Apache 2.0, 201 langues

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gemma4:12b\nPARAMETER num_ctx 32768\n' > gemma4-12b-32k.Modelfile
ollama create gemma4-12b-32k -f gemma4-12b-32k.Modelfile
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
        "gemma4-12b-32k": {
          "name": "Gemma 4 12B (32k, sans réflexion)",
          "limit": { "context": 32768, "output": 8192 },
          "options": { "reasoningEffort": "none" }
        }
      }
    }
  }
}
```

`reasoningEffort: "none"` ist kein unwichtiges Detail: Ollama aktiviert Reasoning bei
Gemma 4 und Qwen 3.5 standardmäßig, und eine Modelfile kann es nicht deaktivieren.
Über OpenCode gemessen: Ohne die Option kostet „Die Katze schläft auf dem Teppich“
919 Reasoning-Token und 68 s; mit der Option 9 Token.

```bash
aipmt --use_opencode --model ollama/gemma4-12b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

Ergebnisse für einen echten Blogartikel mit 589 Zeilen (140 Links, 21 Abschnitte,
3 englische Zitate, die durch den Modus `--news` geschützt wurden), mit
demselben Befehl und drei Modellen:

| Modell                                   | Dauer       | Struktur                                                   | Abweichungen                                                                               |
| ---------------------------------------- | ----------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `opencode/mimo-v2.5-free` (Zen, kostenlos) | 4 min 26 s  | identisch mit der Quelle                                   | keine                                                                                      |
| `ollama/gemma4-12b-32k` (lokal)          | 10 min 10 s | Links, URLs, Tabellen, Tags, Fettdruck und Inline-Code identisch | eine erfundene Zitatzeile (🇺🇸 + Paraphrase), eine doppelte Zuschreibung               |
| `ollama/qwen3.5-9b-32k` (lokal)          | 8 min 18 s  | Links, URLs, Tabellen und Tags identisch                   | eine erfundene Zitatzeile, einige hinzugefügte Fettungen und Inline-Codes, ein erneut verarbeitetes Segment |

Während der lokalen Übersetzung: GPU zu 98 % ausgelastet und 170 W, 10 GB VRAM belegt
(Modell und Cache mit 32 k Token, nichts in den RAM ausgelagert), 7,5 GB RAM für den
Ollama-Server. Ein Modell mit 9 bis 12 Milliarden Parametern bewahrt die Struktur,
nimmt sich jedoch pro Artikel eine Freiheit heraus, während sich das Gateway-Modell
keine einzige erlaubt hat: vor der Veröffentlichung gegenlesen oder auf Entwürfe beschränken.

### Sparmodus

Verwendet schnellere und kostengünstigere Modelle (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### Optionen

| Option                   | Beschreibung                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Einzelne zu übersetzende Markdown-Datei                                                                        |
| `--source_dir`           | Quellverzeichnis mit den Markdown-Dateien                                                                      |
| `--target_dir`           | Ausgabeverzeichnis für die übersetzten Dateien                                                                 |
| `--source_lang`          | Ausgangssprache (Standard: `fr`)                                                                     |
| `--target_lang`          | Zielsprache (Standard: `en`)                                                                         |
| `--model`                | Zu verwendendes spezifisches Modell                                                                            |
| `--eco`                  | Kostengünstige Modelle verwenden                                                                               |
| `--use_mistral`          | Mistral-AI-API verwenden                                                                                       |
| `--use_claude`           | Claude-API verwenden                                                                                           |
| `--use_gemini`           | Gemini-API verwenden                                                                                           |
| `--use_codex`            | Codex CLI mit dem Kontingent des ChatGPT-Abonnements verwenden                                                 |
| `--use_grok`             | xAI-API (Grok) verwenden — erfordert `XAI_API_KEY`                                                            |
| `--use_grok_cli`         | Grok CLI mit dem Kontingent des Grok-Abonnements verwenden                                                     |
| `--use_opencode`         | OpenCode (Open Source) mit dem in OpenCode konfigurierten Provider verwenden; erfordert `--model provider/modèle` |
| `--force`                | Erneute Übersetzung erzwingen                                                                                  |
| `--keep_filename`        | Ursprünglichen Dateinamen beibehalten                                                                           |
| `--news`                 | Nachrichtenmodus: schützt englische Zitate und verwaltet Kennzeichnungen nach Sprache                         |
| `--add_translation_note` | Übersetzungshinweis hinzufügen                                                                                 |
| `--note_position`        | Position des Hinweises: `top`, `bottom` (Standard) oder `both`                        |
| `--note_format`          | Format des Hinweises: `legacy` (Standard, fett gedruckter Absatz) oder `marker`                  |
| `--include_model`        | Modellnamen in die Ausgabedatei aufnehmen                                                                       |
| `--reasoning_effort`     | GPT-5.x-Reasoning-Aufwand: `none`/`low`/`medium`/`high`/`xhigh`     |

> **Die sieben Provider-Flags schließen sich gegenseitig aus.** Die Kombination zweier Flags
> wurde zuvor stillschweigend akzeptiert und auf das zuerst geprüfte aufgelöst: Eine
> über das Abonnementkontingent angeforderte Übersetzung (`--use_codex`, `--use_grok_cli`)
> konnte dadurch ohne jede Warnung nutzungsabhängig abgerechnet werden.
> `argparse` lehnt diese Kombination nun ab.

### Übersetzungshinweis: Positionen und Formate

Mit `--add_translation_note` kann der Übersetzer den Hinweis oben, unten oder an beiden Stellen platzieren und ihn entweder als einfachen Text (abwärtskompatibel) oder im von einem Markdown-Plugin verarbeitbaren Format `marker` ausgeben.

**Position** (`--note_position`):

- `bottom` (Standard): Hinweis am Dateiende, wie bisher.
- `top`: Hinweis **nach dem YAML-Frontmatter** eingefügt (sicher für Astro Content Collections, gray-matter usw.).
- `both`: Hinweis oben UND unten eingefügt (ein einziger LLM-Aufruf, dessen Inhalt für beide Positionen wiederverwendet wird).

**Format** (`--note_format`):

- `legacy` (Standard): fett gedruckter Absatz `**...**` — Byte für Byte exakt dasselbe Verhalten wie in v1.8. Kompatibel mit Hugo, GitHub, GitLab und jedem Markdown-Renderer.
- `marker`: unsichtbare Markdown-Linkreferenzdefinition (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), gefolgt von einem fett gedruckten Blockquote. Nativ auf GitHub/GitLab lesbar und beim Build durch ein Astro-seitiges remark-Plugin nutzbar, um ein stilisiertes Banner zu erzeugen (siehe Blog jls42.org).

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

| Provider | Qualität (Standard)                    | Kostengünstig (`--eco`) |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI   | `gpt-5.6-terra`                       | `gpt-5.6-luna`            |
| Claude   | `claude-sonnet-5`                     | `claude-haiku-4-5`        |
| Mistral  | `mistral-large-latest`                | `mistral-small-latest`    |
| Gemini   | `gemini-3.7-flash`                    | `gemini-3.1-flash-lite`   |
| Codex    | `gpt-5.6-sol`                         | `gpt-5.6-luna`            |
| Grok API | `grok-4.6`                            | `grok-4.3`                |
| Grok CLI | `grok-4.6`                            | `grok-4.5`                |
| OpenCode | `--model provider/modèle` erforderlich | identisch — `--eco` ohne Wirkung |

> **Empfehlung für Long-form-Übersetzungen**: `--use_gemini` (Standard = `gemini-3.7-flash`) bewahrt die Markdown-Struktur bei nicht-lateinischen Schriften (PL, JA, ZH, AR, HI) zuverlässig, einschließlich im Modus `--news`, in dem es auf die exakte Beibehaltung der Platzhalter ankommt. Gemessen anhand dieses ins Japanische übersetzten README: identische Struktur wie bei `gemini-3.1-pro-preview` (21 Listen, 18 Codeblöcke, 13 HTML-Links, 13 Bilder, alle URLs beibehalten) bei etwa sechsmal geringerer Latenz. OpenAI bleibt aus Gründen der Abwärtskompatibilität die Standardeinstellung.

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** - Mehrsprachiger persönlicher Blog (15 Sprachen)

## Autor

Julien LE SAUX
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artikel mit gpt-5.6-sol aus dem Französischen ins Deutsche übersetzt.**

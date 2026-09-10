# KI-gestützter Markdown-Übersetzer

🌍 [Französisch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [Englisch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Spanisch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Chinesisch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Japanisch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Koreanisch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Arabisch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italienisch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Niederländisch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polnisch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Portugiesisch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Rumänisch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Schwedisch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Codequalität</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Quality-Gate-Status"></a>
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

Übersetzt Markdown-Dateien von einer Sprache in eine andere und bewahrt dabei die
Struktur: Codeblöcke, Inline-Code, URLs, Anker, Tabellen und Front
Matter. Neun Möglichkeiten, ein Modell aufzurufen — fünf APIs, zwei Abonnements ohne
nutzungsabhängige Abrechnung, zwei Router — sowie eine veröffentlichte Messung dessen, was jedes
Modell tatsächlich bewahrt.

## Kurz gesagt

- **Neun Provider-Wege**: APIs von OpenAI, Mistral, Claude, Gemini und Grok;
  ChatGPT- (Codex) und Grok-Abonnements ohne nutzungsabhängige Abrechnung; Router
  OpenCode (Open Source, kostenlos oder lokal) und OpenRouter (mehr als 400 Modelle).
- **Keine fehlerhaften Ergebnisse wegen eines verlorenen Tokens**: Codeblöcke, Inline-Code,
  URLs, Anker und Zitate werden vor dem Aufruf durch Tokens ersetzt und
  bei der Rückgabe überprüft. Fehlt eines davon, wird die Datei nicht geschrieben.
- **Lange Dokumente**: Segmentierung entsprechend dem Kontextfenster des Modells.
- **Modus `--news`**: Englische Zitate werden geschützt und Flaggen
  sprachabhängig verwaltet, für Monitoring-Artikel.
- **Modus `--eco`**: schnellere und günstigere Modelle.
- Optionale **Übersetzungsnotiz**, oben, unten oder an beiden Stellen.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 oder neuer. Zur Installation aus dem Repository siehe
[Mitwirken](#mitwirken).

## Konfiguration

Die Schlüssel werden an drei Stellen gelesen, von der höchsten bis zur niedrigsten Priorität; jede
ergänzt nur das, was die vorherige leer lässt.

|     | Wo                                            | Wofür                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Umgebungsvariablen                     | CI, Container, einmalige Abweichung |
| 2   | `.env` des aktuellen Verzeichnisses (oder eines übergeordneten Verzeichnisses) | ein projektspezifischer Schlüssel            |
| 3   | `~/.config/aipmt/.env`                        | einmal installiert, gilt überall       |

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

`GEMINI_API_KEY` wird anstelle von `GOOGLE_API_KEY` akzeptiert. Die
Benutzerdatei folgt `XDG_CONFIG_HOME` (nur absoluter Pfad) und `%APPDATA%`
unter Windows. Ohne Schlüssel listet der Befehl die drei Speicherorte auf.

**Die `.env` eines Projekts kann Aufrufe nicht umleiten.** Sie stellt Schlüssel bereit,
niemals ein Ziel: Alle Variablen in `_BASE_URL`, `_API_BASE` oder
`_ENDPOINT`, Proxys (`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`), die
Zertifikatsspeicher (`SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`,
`CURL_CA_BUNDLE`) sowie `XDG_CONFIG_HOME` / `APPDATA` werden dort unter Ausgabe
einer Warnung ignoriert. Ein geklontes Repository darf Ihren Schlüssel nicht umleiten können. Diese
Datei wird außerdem ohne Interpolation gelesen: `NOM=${OPENAI_API_KEY}` kopiert den
Schlüssel dort nicht hinein. Legen Sie diese Variablen in der Umgebung oder in
`~/.config/aipmt/.env` fest.

Optionale Variablen: `XAI_BASE_URL` (Standard `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (Sekunden pro Aufruf, Standard 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(Standard 600), `GROK_BIN`, `GROK_HOME` (Standard `~/.grok`), `GROK_TIMEOUT`
(Standard 900), `GROK_TRANSLATE_SANDBOX`, `OPENCODE_BIN`, `OPENCODE_TIMEOUT`
(Standard 600), `OPENROUTER_BASE_URL` (`https://` erforderlich), `OPENROUTER_TIMEOUT`
(Standard 900), `OPENROUTER_PREFLIGHT_TIMEOUT` (Standard 30). Jede davon wird im Abschnitt
ihres Providers ausführlich beschrieben.

## Erste Schritte

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` ins Spanische übersetzt ergibt `document-es.md` in `--target_dir`;
mit `--include_model` ergibt es `document-es-gpt-5.6-terra.md`. Die Erweiterung wird
immer zu `.md` — `article.mdx` ergibt `article-en.md` — außer mit
`--keep_filename`, wodurch der ursprüngliche Name beibehalten wird. Eine bereits vorhandene
Übersetzung wird ohne `--force` übersprungen.

Exit-Codes: `0`, wenn alles erfolgreich abgeschlossen oder übersprungen wurde, `1`, wenn noch eine
Datei fehlgeschlagen ist (Liste auf der Fehlerausgabe), `2`, wenn die Konfiguration die Ursache ist.
Eine fehlgeschlagene Datei wird niemals geschrieben, selbst wenn der Schreibvorgang selbst fehlschlägt:
Der Inhalt wird daneben geschrieben und anschließend umbenannt. Ein erneuter Start genügt.

## Welches Modell wählen?

Gemessen anhand zweier realer Dokumente, die von jedem Modell in dieselben vierzehn Sprachen
übersetzt wurden. **Die Zahl gibt die Anzahl der Sprachen von insgesamt vierzehn an, bei denen die
Übersetzung geschrieben wird und nichts von der Quelle abweicht.**

| Modell               | Zugriffsmethode                 | Dicht geschriebener Monitoring-Artikel | Diese README-Datei    | Was abweicht und bei wie vielen Sprachen                                                                                             |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | Google-API-Schlüssel                    | ✅ 14/14                | ⚠️ 13/14     | 1 von 14 Sprachen: ein zusätzlich fett gesetztes Wort (ja)                                                                                         |
| **GPT-5.6 Sol**      | ChatGPT-Abonnement oder OpenAI-Schlüssel | ✅ 14/14                | ⚠️ 12/14     | 2 von 14 Sprachen: ein fett gesetztes Wort weniger (ar, ja)                                                                                   |
| **GLM-5.2**          | OpenRouter-Schlüssel                    | ✅ 14/14                | ⚠️ 11/14     | 3 von 14 Sprachen: ein fett gesetztes Wort weniger (hi, ja, ko)                                                                               |
| Claude Sonnet 5      | Anthropic-API-Schlüssel                 | ⚠️ 11/14                | ⚠️ 12/14     | 3 Sprachen im Artikel: ein Codeblock ist aufgetaucht (es, de, hi); 2 in dieser README-Datei: ein Link ohne seine Auszeichnung (sv), ein fett gesetztes Wort (zh) |
| Qwen 3.7 Flash       | OpenRouter-Schlüssel                    | ❌ 8/14                 | ⚠️ 10/14     | 1 Sprache im Artikel abgelehnt, 5 weitere weichen ab; in dieser README-Datei wurden etwa vierzig Wörter in `code` gesetzt (ar)                       |
| Grok 4.6             | Grok-Abonnement                   | ❌ 8/14                 | nicht bewertet     | 5 von 14 Sprachen abgelehnt, weil Inline-Code und URLs nicht zurückgegeben wurden; Niederländisch weicht vollständig ab                                  |
| GPT-OSS 20B          | lokales Modell (Ollama)             | ❌ 7/14                 | nicht erneut gemessen | 4 von 14 Sprachen abgelehnt: Das Modell ließ dort französische Passagen stehen, die Schutzprüfung hat sie gestoppt                                     |
| MiMo v2.5 (kostenlos)  | OpenCode Zen, ohne Konto         | ❌ 11/14                | nicht erneut gemessen | 1 Sprache abgelehnt; ein Abschnitt auf Polnisch verloren                                                                                     |
| Mistral Large        | Mistral-API-Schlüssel                   | ❌ 5/14                 | ❌ 1/14      | **Ein vollständiger Abschnitt verschwindet**: 1 Sprache im Artikel (hi), 3 in dieser README-Datei (ar, hi, ko) — und 3 im Artikel abgelehnte Sprachen   |
| DeepSeek V4 Flash    | OpenRouter-Schlüssel                    | ❌ 3/14                 | nicht erneut gemessen | 10 von 14 Sprachen abgelehnt; 37 Minuten pro Sprache                                                                                    |

|     | Bedeutung des Symbols                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alle vierzehn Sprachen übersetzt, und nichts weicht von der Quelle ab                                                                                                                                       |
| ⚠️  | alle vierzehn Sprachen übersetzt; die Abweichungen betreffen die **Auszeichnung** — ein fett gesetztes Wort, ein `code`, ein Link, der seine eckigen Klammern verliert. Kein Text, keine URL, kein Codeblock und kein Abschnitt fehlt |
| ❌  | mindestens eine Sprache konnte nicht übersetzt werden — die Datei wird abgelehnt und nicht geschrieben — **oder** in einer geschriebenen Datei fehlt Inhalt                                                                      |

Die wichtigsten Erkenntnisse:

- **Eine abgelehnte Übersetzung ist keine beschädigte Übersetzung.** Wenn bei der Rückgabe ein Token
  fehlt, wird die Datei nicht geschrieben und die Sprache als
  abgelehnt gezählt. Das passiert Grok beim Artikel: vier Inline-Code-Elemente und
  drei URLs gehen bereits im ersten Segment bei den fünf nicht lateinischen Schriften verloren.
- **Dieses Sicherheitsnetz deckt Überschriften, Tabellen, Front Matter und
  Text nicht ab.** Ein Modell, das einen Abschnitt entfernt, liefert eine Datei, die das Werkzeug
  ohne Beanstandung schreibt — das ist bei Mistral der Fall. Diese Elemente können nicht
  durch ein Token ersetzt werden, und die aktuellen Schutzprüfungen kontrollieren sie nicht;
  `scripts/compare_structure.py` erkennt einen verlorenen Abschnitt, allerdings erst im Nachhinein.
- **Grok hat keine Bewertung für diese README-Datei**: Seine CLI-Sitzung lief nach zwölf
  Sprachen ab, von denen elf keine Abweichung aufwiesen. Eine unterbrochene Testkampagne wird nicht bewertet.
- **Die Dichte des Dokuments ist wichtiger als die Sprache.** Grok bewältigt gewöhnliche
  README-Dateien und scheitert bei einem linkreichen Artikel, auch auf
  Niederländisch.

Daten und Dokumente: Die Spalte „Diese README-Datei“ wurde am 9. September 2026
anhand einer fixierten Revision dieser Datei (785 Zeilen, 285 Inline-Code-Elemente, 89
Tabellenzeilen) gemessen, die seither überarbeitet wurde. Die Spalte „Dicht geschriebener Monitoring-Artikel“ stammt aus
der Testkampagne vom 4. und 5. September mit einem 589 Zeilen langen Artikel, mit Ausnahme der
Grok-Zeile, die am 9. September anhand einer anderen Ausgabe desselben Monitoring-Artikels erneut gemessen wurde. Die
vollständigen Tabellen, Laufzeiten und das Protokoll befinden sich unter
[Detaillierte Messungen](#detaillierte-messungen).

## Alle Optionen

| Option                   | Beschreibung                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Einzelne zu übersetzende Markdown-Datei (Alternative zu `--source_dir`)                                             |
| `--source_dir`           | Quellverzeichnis mit den Markdown-Dateien (Standard: `content/posts`)                                   |
| `--target_dir`           | Ausgabeverzeichnis für die übersetzten Dateien (Standard: `traductions_en`)                                    |
| `--source_lang`          | Ausgangssprache (Standard: `fr`)                                                                                  |
| `--target_lang`          | Zielsprache (Standard: `en`)                                                                                   |
| `--model`                | Zu verwendendes spezifisches Modell                                                                                  |
| `--eco`                  | Kostengünstige Modelle verwenden                                                                              |
| `--use_mistral`          | Mistral-AI-API verwenden                                                                                     |
| `--use_claude`           | Claude-API verwenden                                                                                         |
| `--use_gemini`           | Gemini-API verwenden                                                                                         |
| `--use_grok`             | xAI-API (Grok) verwenden — erfordert `XAI_API_KEY`                                                           |
| `--use_codex`            | Codex CLI mit dem Kontingent des ChatGPT-Abonnements verwenden                                                    |
| `--use_grok_cli`         | Grok CLI mit dem Kontingent des Grok-Abonnements verwenden                                                        |
| `--use_opencode`         | OpenCode (Open Source) mit dem in OpenCode konfigurierten Anbieter verwenden; erfordert `--model provider/modèle` |
| `--use_openrouter`       | OpenRouter verwenden — erfordert `OPENROUTER_API_KEY` und `--model fournisseur/modèle`                          |
| `--force`                | Erneute Übersetzung erzwingen                                                                                       |
| `--keep_filename`        | Ursprünglichen Dateinamen beibehalten                                                                          |
| `--news`                 | Nachrichtenmodus: schützt englische Zitate und verwaltet Flaggen sprachabhängig                                      |
| `--add_translation_note` | Eine Übersetzungsnotiz hinzufügen                                                                                |
| `--note_position`        | Position der Notiz: `top`, `bottom` (Standard) oder `both`                                                     |
| `--note_format`          | Format der Notiz: `legacy` (Standard, fett gesetzter Absatz) oder `marker`                                            |
| `--include_model`        | Modellnamen in die Ausgabedatei aufnehmen                                                            |
| `--reasoning_effort`     | GPT-5.x-Reasoning-Aufwand: `none`/`low`/`medium`/`high`/`xhigh`                                         |

Die acht `--use_*`-Flags schließen sich gegenseitig aus: Die Kombination von zwei Flags wird
abgelehnt.

## Provider

### Per API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` wechselt zur kostengünstigen Stufe des jeweiligen Anbieters.

| Provider   | Qualität (Standard)                                      | Kostengünstig (`--eco`)      |
| ---------- | ----------------------------------------------------- | ------------------------- |
| OpenAI     | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude     | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral    | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini     | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex      | `gpt-5.6-sol` (auch `terra` und `luna` über `--model`) | `gpt-5.6-luna`            |
| Grok API   | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI   | `grok-4.6`                                            | `grok-4.5`                |
| OpenCode   | `--model provider/modèle` erforderlich                 | identisch — `--eco` ohne Wirkung |
| OpenRouter | `--model fournisseur/modèle` erforderlich              | identisch — `--eco` ohne Wirkung |
### Mit dem ChatGPT-Abonnement: `--use_codex`

Steuert die offizielle Codex CLI: Die Übersetzung wird auf das Kontingent des
ChatGPT-Abonnements angerechnet, ohne API-Schlüssel oder nutzungsabhängige Abrechnung.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Die Binärdatei wird zuerst in `CODEX_BIN`, dann im `PATH` und anschließend im Paket
  `openai-codex-cli-bin` gesucht. `~/.codex/auth.json` wird niemals gelesen.
- `OPENAI_API_KEY` und `CODEX_API_KEY` werden aus der Umgebung des
  Unterprozesses entfernt: Ein vorhandener Schlüssel bewirkt niemals einen Wechsel zur API.
- Jedes Segment kostet mindestens eine „Nachricht“ des 5-Stunden-Fensters — zwei,
  wenn seine Validierung fehlschlägt und es erneut versucht wird. OpenAI nennt als
  Schätzung 250–2.000 Nachrichten/5 Std. für `gpt-5.6-luna` (`--eco`) und
  10–100 für `gpt-5.6-sol` mit einem Plus-Tarif.
- `--model gpt-5.6-terra` und `--model gpt-5.6-luna` laufen ebenfalls über
  das Abonnement. Ein Modell, auf das das Konto keinen Anspruch hat, gibt einen 400-Fehler
  „model is not supported when using Codex with a ChatGPT account“ zurück.
- Langsamer als eine API, wobei der Abstand mit der Dokumentgröße wächst: bei diesem README
  im Median 6 Min. 46 Sek. pro Sprache mit `gpt-5.6-sol`, gegenüber 36 Sek. mit
  `gemini-3.7-flash`.
- In CI abgelehnt (`CI` oder `GITHUB_ACTIONS` definiert): Das Abonnement authentifiziert sich
  über eine persönliche Sitzungsdatei, die auf einem gemeinsam genutzten Runner nichts
  zu suchen hat.
- Variablen: `CODEX_BIN`, `CODEX_TIMEOUT` (Sekunden pro Segment, Standardwert 600).

### Mit dem Grok-Abonnement: `--use_grok_cli`

Dasselbe Prinzip mit der offiziellen Grok Build CLI, über das SuperGrok- oder
X-Premium+-Abonnement.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Schwächere Isolierung als bei Codex.** Die OS-Sandbox von Grok funktioniert
  auf vielen neueren Linux-Systemen nicht (AppArmor, Sockets der Container-Runtime),
  und ein Profil, das nicht angewendet werden kann, startet stillschweigend ohne
  Isolierung. Das Skript fordert daher standardmäßig kein Profil an, weist darauf hin und
  stützt sich auf die `--deny`-Regeln der CLI, einschließlich der Catch-all-Regel `*` — der einzigen
  Schicht, die den Start verweigert, statt den Schutz kommentarlos zu
  entfernen. `GROK_TRANSLATE_SANDBOX=read-only` erzwingt die OS-Sandbox, und der Start
  schlägt fehl, wenn das System diese Anforderung nicht erfüllen kann.
- Das Kontingent gilt wöchentlich und wird mit Chat, Imagine und Voice geteilt; es gibt
  keinen Befehl, um es auszulesen: Ein Batch kann die Nutzung für Unterhaltungen
  ohne Warnung beeinträchtigen.
- Variablen: `GROK_BIN`, `GROK_HOME` (CLI-Verzeichnis, Standardwert `~/.grok`),
  `GROK_TIMEOUT` (Standardwert 900), `GROK_TRANSLATE_SANDBOX`.

### Zu einem Anbieter Ihrer Wahl: `--use_opencode`

[OpenCode](https://opencode.ai) ist ein Open-Source-Code-Agent (MIT), der
Anfragen an die darin konfigurierten Anbieter weiterleitet: API-Schlüssel, Abonnement,
OpenCode-Zen-Gateway (kostenlose Modelle, ohne Konto) oder lokales Modell. Zwei
Wege wurden hier von Anfang bis Ende gemessen: Zen und Ollama.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur

# gratuit, sans compte ni clé — données utilisables pour l'entraînement
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en
# local, hors ligne
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de
# sur un abonnement déjà payé
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

`--model` ist obligatorisch: Ohne diese Angabe würde OpenCode auf ein kostenloses Modell
zurückfallen, dessen Interaktionen für das Training verwendet werden können; diese Entscheidung
wird Ihnen nicht abgenommen.

Isolierung bei jedem Aufruf:

- Eine Inline-Konfiguration, die Vorrang vor Ihrer eigenen hat, definiert einen Agenten `aipmt`,
  für den alle Tools gesperrt sind (`permission: { "*": "deny" }`), die
  Sitzungsfreigabe deaktiviert ist und `--pure`, niemals `--auto`, verwendet wird;
- ein leeres temporäres Arbeitsverzeichnis sowie gesetzte Werte für `OPENCODE_DISABLE_PROJECT_CONFIG` und
  `OPENCODE_DISABLE_CLAUDE_CODE` — ohne sie fügt OpenCode dem
  Prompt die `AGENTS.md` des aktuellen Verzeichnisses und `~/.claude/CLAUDE.md` hinzu. Die
  globale `~/.config/opencode/AGENTS.md` wird weiterhin eingefügt; OpenCode erlaubt
  nicht, sie auszuschließen;
- Ausgabevertrag: Rückgabecode 0, kein Ereignis `error`, kein
  Tool-Aufruf, letzter Schritt in `stop`, nicht leerer Text und der Agent `aipmt`
  tatsächlich geladen — bei einem unbekannten `--agent` schlägt OpenCode nicht fehl, sondern
  fällt stillschweigend auf den Coding-Agenten zurück;
- Kein Schlüssel aus `aipmt` wird weitergegeben, außer `OPENCODE_API_KEY`, dem
  Schlüssel von OpenCode selbst. Die Anbieter werden in OpenCode konfiguriert, nicht in
  der `.env` von `aipmt`.

Wissenswertes:

- Die kostenlosen Zen-Modelle wechseln, haben nicht dokumentierte Limits und
  ihre Interaktionen können für das Training verwendet werden: geeignet für öffentliche
  Dokumentation, nicht für private Inhalte.
- Ein lokales Modell muss mindestens 16 k Kontext-Tokens unterstützen, da die Segmente
  bis zu 16.000 Zeichen umfassen. Ollama konfiguriert häufig 4.096: Verwenden Sie
  eine `Modelfile` mit `PARAMETER num_ctx 32768`.
- `--eco` hat keine Wirkung; `--reasoning_effort` wird unverändert als
  `--variant` von OpenCode übergeben.
- OpenCode protokolliert jede Sitzung in `~/.local/share/opencode/`.
- Variablen: `OPENCODE_BIN` (andernfalls `PATH`, dann `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (Sekunden pro Segment, Standardwert 600). `OPENCODE_CONFIG`
  wird unverändert an OpenCode übergeben.

Beispiel für ein lokales Modell über Ollama in `~/.config/opencode/opencode.json`:

```bash
ollama pull gpt-oss:20b
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

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

`reasoningEffort: "none"` deaktiviert den Denkprozess, den Ollama bei diesen
Modellen standardmäßig aktiviert und den eine Modelfile nicht deaktivieren kann. Gemessen anhand eines
Satzes mit sechs Wörtern: 919 Denk-Tokens und 68 Sekunden ohne die Option, 9 Tokens mit ihr.

### Zugriff auf mehr als 400 Modelle: `--use_openrouter`

OpenRouter ist ein nutzungsabhängig abgerechneter Router mit einem einmaligen Guthaben für
von Drittanbietern gehostete Modelle — darunter offene chinesische Modelle, die kein
anderer Anbieter hier bereitstellt.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` ist obligatorisch. Ein vor jeder Abrechnung ausgeführter Preflight
behandelt zwei Besonderheiten des Routings:

- **Dasselbe Modell wird von Dutzenden Hostern mit unterschiedlichen
  Limits bereitgestellt** — bei `z-ai/glm-5.3-flash` sind es 23 Hoster, von denen einer auf
  2.048 Ausgabe-Tokens begrenzt ist. Der Preflight liest `/api/v1/models/{modèle}/endpoints`,
  schließt Hoster mit weniger als 8.000 Ausgabe-Tokens oder beeinträchtigtem Status aus und
  fixiert die übrigen mit `allow_fallbacks: false`.
- **Reasoning wird zum Ausgabetarif abgerechnet** — 107 Tokens gegenüber 2 bei
  einer „OK“-Antwort von `z-ai/glm-5.2`. Es ist standardmäßig deaktiviert; Modelle,
  die es erzwingen, erhalten den niedrigsten von ihnen akzeptierten Aufwand, da der
  Katalogstandard die Ausgabe vor dem Ende der Übersetzung ausschöpfen kann.
  `--reasoning_effort` hat weiterhin Vorrang.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Das Kontextfenster stammt aus dem Katalog. Ein Modell mit weniger als 16.400 Tokens wird
  vor jedem Aufruf abgelehnt: 8.400 für Prompt und Segment, mindestens 8.000 für die Ausgabe.
- Ein im Katalog fehlender Slug, ein nicht erreichbarer Katalog oder das Fehlen
  eines Hosters, der das Limit einhalten kann, brechen den Befehl ab.
- `finish_reason=length` mit leerer Ausgabe bedeutet ein durch
  Reasoning verbrauchtes Budget, keine Kürzung: Die Meldung unterscheidet beides.
- `--eco` hat keine Wirkung.
- Variablen: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (Standardwert `https://openrouter.ai/api/v1`, `https://`
  erforderlich), `OPENROUTER_TIMEOUT` (Standardwert 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (Standardwert 30).

### Übersetzungshinweis

`--add_translation_note` fügt einen Hinweis in `bottom` (Standardwert), `top` (nach dem
Front Matter) oder `both` (`--note_position`) hinzu, im Format `legacy` (fett
formatierter Absatz, Standardwert) oder `marker` (`--note_format`). Das Format `marker` ist eine
unsichtbare Markdown-Referenzdefinition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
gefolgt von einem fett formatierten Zitat: auf GitHub lesbar und beim Build durch ein
remark-Plugin auswertbar.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detaillierte Messungen

Alle Messungen sind tatsächlich mit `aipmt` ausgeführte Übersetzungen in
vierzehn Sprachen: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Geschrieben** zählt die Dateien, welche die Prüfmechanismen passieren ließen; **Ohne
Abweichung** diejenigen, bei denen `scripts/compare_structure.py` nichts feststellt — dieselbe Anzahl von
Abschnitten, Untertiteln, Links, unterschiedlichen URLs, Codeblöcken,
Inline-Code-Elementen, Tabellenzeilen, Blockzitaten und fett formatierten Wörtern.

„Ohne Abweichung“ bedeutet „nichts erkannt“, nicht „identisch“: Der Vergleicher
zählt Elemente, ohne deren Inhalt zu lesen. Er erkennt weder eine entfernte Überschrift
der Ebene 4 noch den ersetzten Text eines Inline-Code-Elements oder eine
vertauschte Flag und beurteilt auch nicht die Sprache.

### Dicht geschriebener Monitoring-Artikel, Modus `--news`

Eine Ausgabe der [KI-Beobachtung von jls42.org](https://jls42.org/fr/news):
589 Zeilen, 140 Links, 21 Abschnitte, 3 geschützte englische Zitate. Testreihe
vom 4. und 5. September 2026.

| Modell                            | Zugriff              | Geschrieben | Ohne Abweichung | Median/Sprache |
| --------------------------------- | -------------------- | ----------- | --------------- | -------------- |
| `gemini-3.7-flash`                | Google API           | 14/14       | ✅ **14/14**    | 1 Min. 18 Sek. |
| `gpt-5.6-sol` (`--use_codex`)     | ChatGPT-Abonnement   | 14/14       | ✅ **14/14**    | 11 Min. 28 Sek. |
| `z-ai/glm-5.2`                    | OpenRouter           | 14/14       | ✅ **14/14**    | 5 Min. 37 Sek. |
| `qwen/qwen3.8-flash`              | OpenRouter           | 14/14       | ✅ **14/14**    | 26 Min. 23 Sek. |
| `claude-sonnet-5`                 | Anthropic API        | 14/14       | ⚠️ 11/14        | 6 Min. 31 Sek. |
| `opencode/mimo-v2.5-free`         | OpenCode Zen         | 13/14       | ❌ 11/14        | 9 Min. 27 Sek. |
| `qwen/qwen3.7-flash`              | OpenRouter           | 13/14       | ❌ 8/14         | 10 Min. 09 Sek. |
| `ollama/gpt-oss-20b-32k`          | lokal                | 10/14       | ❌ 7/14         | 12 Min. 39 Sek. |
| `mistral-large-latest`            | Mistral API          | 11/14       | ❌ 5/14         | 5 Min. 32 Sek. |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter           | 4/14        | ❌ 3/14         | 37 Min. 27 Sek. |
| `grok-4.6` (`--use_grok_cli`)     | Grok-Abonnement      | 1/14        | ❌ 1/14         | 23 Min. 11 Sek. |

Grok wurde am 9. September mit einer anderen Ausgabe derselben Beobachtung
(356 Zeilen) erneut gemessen: 9 von 14 Sprachen wurden geschrieben, 8 ohne Abweichung. Diese Zahl
steht in der Übersichtstabelle. Drei abgebrochene Testreihen werden nicht
aufgeführt: `qwen3.5-27b` (9 Sprachen) und `kimi-k2.6` (4) wegen fehlenden Guthabens sowie
`z-ai/glm-5.3-flash`, dessen beide Fehlschläge durch eine Reasoning-Einstellung verursacht wurden,
die der Anbieter inzwischen korrigiert. Die OpenRouter-Zeilen wurden mit den
Standardeinstellungen des Routers vor `--use_openrouter` gemessen; `z-ai/glm-5.2`,
erneut mit dem bereitgestellten Anbieter gemessen, erzielt dasselbe Ergebnis von 14/14. Die Zahlen wurden
am 10. September mit dem aktuellen Vergleicher neu berechnet: `qwen3.8-flash` und
`qwen3.7-flash` gewinnen gegenüber der ersten Veröffentlichung jeweils eine Sprache hinzu,
die übrigen bleiben unverändert.

### README dieses Projekts, Standard-Markdown

Festgeschriebene Revision vom 9. September 2026: 785 Zeilen, 285 Inline-Code-Elemente, 40
Codeblock-Begrenzungen, 89 Tabellenzeilen. Vier parallele Übersetzungen.

| Modell                        | Geschrieben | Ohne Abweichung | Median/Sprache | Abweichungen                                                              |
| ----------------------------- | ----------- | --------------- | -------------- | ------------------------------------------------------------------------- |
| `gemini-3.7-flash`            | 14/14       | ⚠️ 13/14        | 36 Sek.        | ein fett formatiertes Wort (ja)                                           |
| `claude-sonnet-5`             | 14/14       | ⚠️ 12/14        | 2 Min. 56 Sek. | ein Link (sv), ein fett formatiertes Wort (zh)                             |
| `gpt-5.6-sol` (`--use_codex`) | 14/14       | ⚠️ 12/14        | 6 Min. 46 Sek. | ein fett formatiertes Wort (ar, ja)                                        |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14       | ⚠️ 11/14        | 2 Min. 34 Sek. | ein fett formatiertes Wort (hi, ja, ko)                                    |
| `qwen/qwen3.7-flash`          | 14/14       | ⚠️ 10/14        | 2 Min. 17 Sek. | 40 auf Arabisch hinzugefügte Inline-Code-Elemente; Fettschrift (hi, ja, ko) |
| `mistral-large-latest`        | 14/14       | ❌ 1/14          | 2 Min. 44 Sek. | ein verlorener Abschnitt (ar, hi, ko); hinzugefügte Codeblöcke (ja, ko, ro, zh) |

Zwei abgebrochene Testreihen werden nicht aufgeführt: Grok, dessen CLI-Sitzung
nach zwölf Sprachen ablief (elf ohne Abweichung), und `qwen3.8-flash`, HTTP 429 seines
Hosters nach zwei Sprachen. `opencode/mimo-v2.5-free` und `ollama/gpt-oss-20b-32k`
wurden mit dieser Revision nicht erneut gemessen; mit der um 277 Zeilen kürzeren
Revision vom 4. und 5. September schrieben sie jeweils 9 von 14 Übersetzungen, davon 7
beziehungsweise 1 ohne Abweichung.

### Vier README-Dateien bekannter Projekte

FastAPI, Ollama, tldr-pages und Vue.js, unverändert von GitHub übernommen — diese
Dokumente sind einfacher als die beiden vorherigen. Die Testreihe zielte auf die
Modelle mit Schwierigkeiten ab; Gemini dient dort als Vergleichspunkt.

| Modell                    | Umfang                     | Geschrieben | Ohne Abweichung |
| ------------------------- | -------------------------- | ----------- | --------------- |
| `gemini-3.7-flash`        | 4 Projekte × 14 Sprachen   | 56/56       | ✅ **55/56**    |
| `opencode/mimo-v2.5-free` | 4 Projekte × 14 Sprachen   | 55/56       | ❌ 47/56        |
| `grok-4.6` (Abonnement)   | 4 Projekte × ar, hi, ja, zh | 16/16       | ❌ 14/16        |
| `ollama/gpt-oss-20b-32k`  | 4 Projekte × ar, hi, ja, zh | 15/16       | ❌ 9/16         |

### Was diese Messungen nicht sind

- **Keine umfassende Rangliste**: Allein OpenRouter bietet mehr als vierhundert
  Modelle an; etwa fünfzehn wurden gemessen.
- **Nur Richtwerte für die Dauer**: Je nach Testreihe liefen drei bis sechs Übersetzungen
  parallel, und der Durchsatz eines Anbieters schwankt im Tagesverlauf.
- **Zeitgebundene Beobachtungen**: Modelle verändern sich unter demselben Namen, und Ihre
  Dokumente sind nicht unsere.

Um die Messung mit Ihren Dokumenten auf einer festgeschriebenen Kopie der Datei zu wiederholen:

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## Mitwirken

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

Beide Zeilen sind erforderlich: Ohne `pip install -e .` antwortet `python -m aipmt`
mit `No module named aipmt`.

Optionale, aber empfohlene Qualitätswerkzeuge:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Die 28 Übersetzungen des Repositorys (README und CHANGELOG, vierzehn Sprachen) werden
mit `./regen_translations.sh --force` neu erzeugt — standardmäßig Codex und `gpt-5.6-sol` über
das ChatGPT-Abonnement, vier parallel. `REGEN_PROVIDER` und
`REGEN_MODEL` ändern den Pfad; eine kostenpflichtige API (`openai`, `gemini`,
`grok`, `openrouter`) wird ohne `REGEN_ALLOW_PAID_API=1` abgelehnt;
`REGEN_JOB_TIMEOUT` begrenzt jeden Job zeitlich (600 Sek., 1.800 Sek. bei Codex). Einzelheiten
zu den Werkzeugen stehen in `CLAUDE.md`.

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** — persönlicher Blog, der in 15 Sprachen veröffentlicht wird. Seine
  [tägliche KI-Beobachtung](https://jls42.org/fr/news) wird jeden Tag
  mit diesem Werkzeug übersetzt und dient als Referenzdokument für die obigen Messungen.

## Autor

Julien LE SAUX
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Haftungsausschluss

Dieses Programm wird gemäß den Bedingungen der Abschnitte 15 und 16 der GPL v3
**ohne jegliche Gewährleistung** verbreitet: Es wird „wie besehen“ bereitgestellt,
ohne Gewährleistung der Marktgängigkeit oder Eignung für einen bestimmten Zweck,
und sein Autor kann nicht für Schäden haftbar gemacht werden, die aus seiner
Verwendung entstehen. Der Lizenztext hat Vorrang vor dieser Zusammenfassung.

- **Lesen Sie alles vor der Veröffentlichung Korrektur.** Die Schutzmechanismen decken Codeblöcke,
  Inline-Code, URLs, Anker und Zitate des Modus `--news` ab — nicht jedoch
  Überschriften, Tabellen, Front Matter oder die Bedeutung Ihrer Sätze.
- **Ihre Dokumente werden an den gewählten Anbieter gesendet**, gemäß dessen
  Nutzungsbedingungen und Datenrichtlinie. Manche kostenlosen Modelle können
  Ihre Interaktionen für das Training wiederverwenden; ein lokales Modell ist der einzige
  Weg, bei dem keine Daten Ihren Rechner verlassen.
- **API-Aufrufe werden Ihnen in Rechnung gestellt.** Dieses Programm begrenzt die
  Ausgaben nicht: Ein langes Dokument, eine Wiederaufnahme nach einem Fehler oder ein Modell mit
  umfangreichem Reasoning verursachen höhere Kosten.
- **Die veröffentlichten Messungen sind zeitgebundene Beobachtungen**, keine Garantien.

Die genannten Produkt- und Unternehmensnamen gehören ihren jeweiligen
Inhabern. Dieses Projekt ist mit keinem von ihnen verbunden.

**Artikel, der mit gpt-5.6-sol aus dem Französischen ins Deutsche übersetzt wurde.**

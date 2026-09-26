# AI-gestützter Markdown-Übersetzer

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

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
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy Badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Übersetzt Markdown-Dateien von einer Sprache in eine andere und bewahrt dabei die
Struktur: Codeblöcke, Inline-Code, URLs, Anker, Tabellen und Frontmatter.
Elf Möglichkeiten, ein Modell aufzurufen – fünf APIs, vier Abonnements ohne
nutzungsbasierte Abrechnung, zwei Router – und eine veröffentlichte Messung dessen, was jedes
Modell tatsächlich bewahrt.

## Auf einen Blick

- **Elf Provider-Pfade**: OpenAI-, Mistral-, Claude-, Gemini- und Grok-APIs;
  ChatGPT- (Codex), Grok-, Google- (Antigravity) und Claude- (Claude
  Code) Abonnements ohne nutzungsbasierte Abrechnung; OpenCode- (Open Source, kostenlos oder lokal) und OpenRouter-Router
  (über 400 Modelle).
- **Keine Fehler durch verlorene Token**: Codeblöcke, Inline-Code,
  URLs, Anker und Zitate werden vor dem Aufruf durch Token ersetzt und
  bei der Rückgabe überprüft. Fehlt auch nur eines, wird die Datei nicht geschrieben.
- **Lange Dokumente**: Segmentierung entsprechend dem Kontextfenster des Modells.
- **Modus `--news`**: geschützte englische Zitate und sprachspezifisch verwaltete
  Flaggen für Recherche- und Monitoring-Artikel.
- **Modus `--eco`**: schnelle und günstigere Modelle.
- Optionale **Übersetzungsnotiz**, oben, unten oder an beiden Stellen.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 oder neuer. Zur Installation aus dem Repository siehe
[Mitwirken](#mitwirken).

## Konfiguration

Schlüssel werden an drei Orten gelesen, von der höchsten zur niedrigsten Priorität; jeder
füllt nur das aus, was der vorherige leer lässt.

|     | Wo                                            | Wofür                                 |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Umgebungsvariablen                            | CI, Container, punktuelle Überschreibungen |
| 2   | `.env` des aktuellen Verzeichnisses (oder eines übergeordneten) | ein projektspezifischer Schlüssel     |
| 3   | `~/.config/aipmt/.env`                        | einmal installiert, gilt überall      |

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
unter Windows. Ohne Schlüssel listet der Befehl alle drei Speicherorte auf.

**Die `.env` eines Projekts kann weder Aufrufe umleiten noch das ausgeführte
Programm bestimmen.** Sie liefert Schlüssel, aber niemals ein Ziel oder ein Binary: Jede
Variable mit `_BASE_URL`, `_API_BASE`, `_ENDPOINT` oder `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, Proxys (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), Zertifikatsspeicher (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) sowie `XDG_CONFIG_HOME` /
`APPDATA` werden darin mit einer Warnung ignoriert. Ein geklontes Repository darf
weder Ihren Schlüssel abfangen noch Sie dazu bringen, bei der
ersten Übersetzung ein eigenes Programm auszuführen. Diese Datei wird zudem ohne Interpolation gelesen:
`NOM=${OPENAI_API_KEY}` kopiert den Schlüssel dort nicht. Setzen Sie diese Variablen in
der Umgebung oder in `~/.config/aipmt/.env`.

Optionale Variablen: `XAI_BASE_URL` (Standardwert `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (Sekunden pro Aufruf, Standardwert 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(Standardwert 600), `GROK_BIN`, `GROK_HOME` (Standardwert `~/.grok`), `GROK_TIMEOUT`
(Standardwert 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (Standardwert 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (Standardwert 600), `OPENROUTER_BASE_URL`
(`https://` erforderlich), `OPENROUTER_TIMEOUT` (Standardwert 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (Standardwert 30). Jede einzelne wird im
Abschnitt ihres Providers detailliert beschrieben.

## Erste Schritte

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

Die Übersetzung von `document.md` ins Spanische ergibt `document-es.md` in `--target_dir`;
mit `--include_model` wird daraus `document-es-gpt-5.6-terra.md`. Die Dateiendung wird
immer zu `.md` – `article.mdx` ergibt `article-en.md` – außer bei
`--keep_filename`, wodurch der ursprüngliche Name beibehalten wird. Eine bereits vorhandene Übersetzung
wird ohne `--force` übersprungen.

Exit-Codes: `0`, wenn alles erfolgreich war oder übersprungen wurde, `1`, wenn mindestens eine Datei
fehlgeschlagen ist (Auflistung auf der Standardfehlerausgabe), `2`, wenn ein Konfigurationsproblem vorliegt.
Eine fehlgeschlagene Datei wird niemals geschrieben, selbst wenn der Schreibvorgang selbst fehlschlägt:
Der Inhalt wird temporär daneben geschrieben und anschließend umbenannt. Ein erneutes Ausführen genügt.

## Welches Modell wählen?

Gemessen an zwei realen Dokumenten, die von jedem Modell in dieselben vierzehn Sprachen übersetzt
wurden. **Die Zahl gibt an, in wie vielen von vierzehn Sprachen die
Übersetzung geschrieben wurde und keinerlei Abweichungen zur Quelle aufweist.**

| Modell               | Zugangsweg                        | Dichter Monitoring-Artikel | Diese README | Was abweicht und in wie vielen Sprachen                                                                                                                            |
| -------------------- | --------------------------------- | -------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash** | Google-Abonnement (Antigravity)   | ✅ 14/14                   | ✅ 14/14     | nichts, bei keinem der beiden Dokumente                                                                                                                            |
| **Gemini 3.7 Flash** | Google-API-Schlüssel              | ✅ 14/14                   | ⚠️ 13/14     | 1 von 14 Sprachen: ein fettgedrucktes Wort mehr (ja)                                                                                                               |
| **Gemini 3.7 Flash** | Google-Abonnement (Antigravity)   | ✅ 14/14                   | ⚠️ 13/14     | 1 von 14 Sprachen: ein fettgedrucktes Wort weniger (ko)                                                                                                            |
| **GPT-5.6 Sol**      | ChatGPT-Abonnement oder OpenAI-Schlüssel | ✅ 14/14             | ⚠️ 12/14     | 2 von 14 Sprachen: ein fettgedrucktes Wort weniger (ar, ja)                                                                                                        |
| **GLM-5.2**          | OpenRouter-Schlüssel              | ✅ 14/14                   | ⚠️ 11/14     | 3 von 14 Sprachen: ein fettgedrucktes Wort weniger (hi, ja, ko)                                                                                                    |
| Claude Sonnet 5      | Claude-Abonnement (Claude Code)   | ⚠️ 13/14                   | ⚠️ 13/14     | 1 von 14 Sprachen beim Artikel: ein fettgedrucktes Wort mehr (zh); 1 bei dieser README: eine Tabellenzeile an die vorherige angehängt, bei der Anzeige ausgeblendet (ar) |
| Claude Haiku 4.5     | Claude-Abonnement (Claude Code)   | ⚠️ 11/14                   | ✅ 14/14     | 3 Sprachen beim Artikel: eine Abschnittsüberschrift auf Ebene 1 heraufgestuft (en, pl, ro); bei dieser README nichts für das Vergleichstool, aber interne Links auf Englisch verdoppelt |
| Claude Sonnet 5      | Anthropic-API-Schlüssel           | ⚠️ 11/14                   | ⚠️ 12/14     | 3 Sprachen beim Artikel: ein zusätzlicher Codeblock aufgetaucht (es, de, hi); 2 bei dieser README: ein Link ohne Markup (sv), ein fettgedrucktes Wort (zh)         |
| Qwen 3.7 Flash       | OpenRouter-Schlüssel              | ❌ 8/14                    | ⚠️ 10/14     | 1 Sprache beim Artikel abgelehnt, 5 weitere weichen ab; bei dieser README rund 40 Wörter in `code` gesetzt (ar)                                            |
| Grok 4.6             | Grok-Abonnement                   | ❌ 8/14                    | nicht bewertet | 5 von 14 Sprachen abgelehnt, da Inline-Code und URLs nicht gerendert wurden; Niederländisch weicht in allem ab                                                     |
| GPT-OSS 20B          | lokales Modell (Ollama)           | ❌ 7/14                    | nicht erneut gemessen | 4 von 14 Sprachen abgelehnt: Das Modell ließ französische Passagen stehen, die Guardrails stoppten sie                                                            |
| MiMo v2.5 (kostenlos) | OpenCode Zen, ohne Konto         | ❌ 11/14                   | nicht erneut gemessen | 1 Sprache abgelehnt; ein verlorener Abschnitt auf Polnisch                                                                                                        |
| Mistral Large        | Mistral-API-Schlüssel             | ❌ 5/14                    | ❌ 1/14      | **ein ganzer Abschnitt verschwindet**: 1 Sprache beim Artikel (hi), 3 bei dieser README (ar, hi, ko) – und 3 Sprachen beim Artikel abgelehnt                        |
| DeepSeek V4 Flash    | OpenRouter-Schlüssel              | ❌ 3/14                    | nicht erneut gemessen | 10 von 14 Sprachen abgelehnt; 37 Minuten pro Sprache                                                                                                              |
| Claude Opus 5.5      | Claude-Abonnement (Claude Code)   | ❌ 0/14                    | ✅ 14/14     | der Artikel wurde in allen 14 Sprachen von den Opus-Guardrails wegen einer Biologie-Kurzmeldung abgelehnt; nichts bei dieser README                                |

|     | Was das Symbol bedeutet                                                                                                                                                                               |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alle vierzehn Sprachen übersetzt, und nichts weicht von der Quelle ab                                                                                                                                |
| ⚠️  | alle vierzehn Sprachen übersetzt; was abweicht, ist reine **Formatierung** – ein fettgedrucktes Wort, ein `code`, ein Link, der seine eckigen Klammern verliert. Kein Text, keine URL, kein Codeblock, kein Abschnitt fehlt |
| ❌  | mindestens eine Sprache konnte nicht übersetzt werden – die Datei wird abgelehnt, nicht geschrieben – **oder** in einer geschriebenen Datei fehlen Inhalte                                            |

Was man daraus mitnehmen sollte:

- **Eine abgelehnte Übersetzung ist keine beschädigte Übersetzung.** Wenn ein Token
  bei der Rückgabe fehlt, wird die Datei nicht geschrieben und die Sprache zählt als
  abgelehnt. Genau das passiert Grok beim Artikel: Vier Inline-Codes und
  drei URLs gingen gleich im ersten Segment bei den fünf nicht-lateinischen Schriftsystemen verloren.
- **Ein Modell kann ein ganzes Dokument wegen eines einzigen Satzes ablehnen.** Opus 5.5
  übersetzt diese README ohne eine einzige Abweichung, aber keinen einzigen Monitoring-Artikel: Seine
  Guardrails brechen die Antwort wegen einer Kurzmeldung über Biologie ab. Die Datei wird nicht
  geschrieben, und aipmt nennt den Grund.
- **Dieses Sicherheitsnetz deckt keine Überschriften, Tabellen, kein Frontmatter und keinen
  Fließtext ab.** Ein Modell, das einen Abschnitt löscht, liefert eine Datei, die das Werkzeug
  anstandslos schreibt – so geschehen bei Mistral. Diese Elemente können nicht
  durch Token ersetzt werden, und die aktuellen Schutzmechanismen prüfen sie nicht;
  `scripts/compare_structure.py` erkennt einen verlorenen Abschnitt zwar, aber erst im Nachhinein.
- **Grok hat keine Wertung für diese README**: Die CLI-Sitzung ist nach zwölf
  Sprachen abgelaufen, von denen elf ohne jede Abweichung waren. Ein abgebrochener Testlauf wird nicht bewertet.
- **Die Dichte des Dokuments wiegt schwerer als die Sprache.** Grok bewältigt
  gewöhnliche READMEs problemlos und scheitert an einem linkreichen Artikel – selbst auf
  Niederländisch.

Daten und Dokumente: Die Spalte „Diese README“ wurde am 9. September 2026
anhand einer eingefrorenen Revision dieser Datei gemessen (785 Zeilen, 285 Inline-Codes, 89 Tabellenzeilen),
die seither überarbeitet wurde – mit Ausnahme der Zeilen zu Antigravity und Claude Code,
die am 26. September anhand der mit 1.14.0 veröffentlichten, kürzeren Revision gemessen wurden
(600 Zeilen, 257 Inline-Codes, 85 Tabellenzeilen). Die Spalte „Dichter Monitoring-Artikel“
stammt aus der Testreihe vom 4. und 5. September mit einem 589 Zeilen langen Artikel,
mit Ausnahme der Zeile zu Grok, die am 9. September anhand einer anderen Ausgabe desselben
Newsletters/Monitoring-Artikels erneut gemessen wurde, und der Zeilen zu Antigravity und Claude Code, die am 26. September
anhand desselben Artikels gemessen wurden. Vollständige Tabellen, Laufzeiten und das Protokoll finden sich unter
[Detaillierte Messungen](#detaillierte-messungen).

## Alle Optionen

| Option                   | Beschreibung                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Einzelne zu übersetzende Markdown-Datei (Alternative zu `--source_dir`)                                        |
| `--source_dir`           | Quellverzeichnis mit den Markdown-Dateien (Standard: `content/posts`)                                          |
| `--target_dir`           | Ausgabeverzeichnis für die übersetzten Dateien (Standard: `traductions_en`)                                     |
| `--source_lang`          | Quellsprache (Standard: `fr`)                                                                       |
| `--target_lang`          | Zielsprache (Standard: `en`)                                                                        |
| `--model`                | Spezifisches zu verwendendes Modell                                                                           |
| `--eco`                  | Sparsame Modelle verwenden                                                                                    |
| `--use_mistral`          | Mistral-AI-API verwenden                                                                                      |
| `--use_claude`           | Claude-API verwenden                                                                                          |
| `--use_gemini`           | Gemini-API verwenden                                                                                          |
| `--use_grok`             | xAI-API (Grok) verwenden — erfordert `XAI_API_KEY`                                                           |
| `--use_codex`            | Codex-CLI über das Kontingent des ChatGPT-Abonnements verwenden                                               |
| `--use_grok_cli`         | Grok-CLI über das Kontingent des Grok-Abonnements verwenden                                                   |
| `--use_antigravity`      | Antigravity-CLI (`agy`) über das Kontingent des Google AI Pro- oder Ultra-Abonnements verwenden         |
| `--use_claude_code`      | Claude Code-CLI (`claude -p`) über das Kontingent des Claude Pro- oder Max-Abonnements verwenden          |
| `--use_opencode`         | OpenCode (Open Source) mit dem in OpenCode konfigurierten Anbieter verwenden; erfordert `--model provider/modèle`        |
| `--use_openrouter`       | OpenRouter verwenden — erfordert `OPENROUTER_API_KEY` und `--model fournisseur/modèle`                                            |
| `--force`                | Neuübersetzung erzwingen                                                                                      |
| `--keep_filename`        | Ursprünglichen Dateinamen beibehalten                                                                         |
| `--news`                 | Nachrichtenmodus: schützt EN-Zitate, verwaltet Flaggen nach Sprache                                           |
| `--add_translation_note` | Übersetzungshinweis hinzufügen                                                                                |
| `--note_position`        | Position des Hinweises: `top`, `bottom` (Standard) oder `both`                         |
| `--note_format`          | Format des Hinweises: `legacy` (Standard, fetter Absatz) oder `marker`                          |
| `--include_model`        | Modellnamen in die Ausgabedatei aufnehmen                                                                     |
| `--reasoning_effort`     | GPT-5.x-Reasoning-Aufwand: `none`/`low`/`medium`/`high`/`xhigh`   |

Die neun `--use_*`-Flags schließen sich gegenseitig aus: Die Kombination von zwei Flags wird abgelehnt.

## Provider

### Per API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` wechselt bei jedem Anbieter auf die Sparstufe.

| Provider    | Qualität (Standard)                                   | Sparsam (`--eco`) |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol` (auch `terra` und `luna` über `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, Aufwand `low`                               | identisch — `--eco` ohne Wirkung |
| OpenCode    | `--model provider/modèle` erforderlich                 | identisch — `--eco` ohne Wirkung |
| OpenRouter  | `--model fournisseur/modèle` erforderlich              | identisch — `--eco` ohne Wirkung |

### Über das ChatGPT-Abonnement: `--use_codex`

Steuert die offizielle Codex-CLI: Die Übersetzung wird vom Kontingent des
ChatGPT-Abonnements abgezogen, ohne API-Schlüssel oder nutzungsbasierte Abrechnung.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Die Binärdatei wird in `CODEX_BIN`, dann im `PATH` und schließlich im Paket
  `openai-codex-cli-bin` gesucht. `~/.codex/auth.json` wird niemals gelesen.
- `OPENAI_API_KEY` und `CODEX_API_KEY` werden aus der Umgebung des
  Subprozesses entfernt: Ein vorhandener Schlüssel führt niemals zu einem Wechsel zur API.
- Jedes Segment kostet mindestens eine „Nachricht“ des 5-Stunden-Fensters — zwei,
  wenn die Validierung fehlschlägt und es wiederholt wird. OpenAI gibt als
  Schätzung 250–2.000 Nachrichten/5 Std. für `gpt-5.6-luna` (`--eco`) und
  10–100 für `gpt-5.6-sol` bei einem Plus-Tarif an.
- `--model gpt-5.6-terra` und `--model gpt-5.6-luna` laufen ebenfalls über
  das Abonnement. Ein Modell, für das das Konto nicht berechtigt ist, liefert einen 400er-Fehler
  „model is not supported when using Codex with a ChatGPT account“.
- Langsamer als eine API, und der Unterschied wächst mit der Dokumentgröße: bei dieser README
  im Median 6 Min. 46 Sek. pro Sprache mit `gpt-5.6-sol`, gegenüber 36 Sek. bei
  `gemini-3.7-flash`.
- In CI verweigert (`CI` oder `GITHUB_ACTIONS` gesetzt): Das Abonnement authentifiziert
  sich über eine persönliche Sitzungsdatei, die auf einem geteilten Runner
  nichts zu suchen hat.
- Variablen: `CODEX_BIN`, `CODEX_TIMEOUT` (Sekunden pro Segment, Standard: 600).

### Über das Grok-Abonnement: `--use_grok_cli`

Dasselbe Prinzip mit der offiziellen Grok Build-CLI über das SuperGrok- oder
X Premium+-Abonnement.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Geringere Isolation als bei Codex.** Die OS-Sandbox von Grok greift
  auf vielen neueren Linux-Rechnern nicht (AppArmor, Container-Runtime-Sockets),
  und ein Profil, das nicht angewendet werden kann, startet stillschweigend ohne
  Isolation. Das Skript fordert daher standardmäßig kein Profil an, weist darauf hin und
  stützt sich auf die `--deny`-Regeln der CLI, einschließlich des Catch-All `*` — die einzige
  Schicht, die den Start verweigert, anstatt den Schutz wortlos
  aufzuheben. `GROK_TRANSLATE_SANDBOX=read-only` erzwingt die OS-Sandbox, und der Start
  schlägt fehl, wenn die Maschine dies nicht einhalten kann.
- Das Kontingent gilt wöchentlich, wird mit Chat, Imagine und Voice geteilt, und kein
  Befehl erlaubt es, dieses abzufragen: Ein Batch-Lauf kann das Kontingent für Konversationen
  ohne Vorwarnung aufbrauchen.
- Variablen: `GROK_BIN`, `GROK_HOME` (CLI-Verzeichnis, Standard: `~/.grok`),
  `GROK_TIMEOUT` (Standard: 900), `GROK_TRANSLATE_SANDBOX`.

### Über das Google-Abonnement: `--use_antigravity`

Dasselbe Prinzip mit `agy`, der offiziellen CLI von Antigravity: Wer Google
AI Pro oder Ultra bezahlt, bei dem wird die Übersetzung vom Kontingent des Abonnements abgezogen,
anstatt tokenbasiert abgerechnet zu werden. Dies ist der einzige Weg zu diesem Kontingent: Die Gemini-CLI
bedient diese Konten seit dem 18. Juni 2026 nicht mehr
([Ankündigung](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
und das Antigravity-SDK akzeptiert nur einen API-Schlüssel oder ein Google Cloud-Projekt.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Kein kostenpflichtiger Kanal bleibt offen.** agy erhält aus Ihrer
  Umgebung nur eine geschlossene Liste von Variablen — `PATH`, Sprache und Zeitzone,
  Terminal, Identität, Proxys und Zertifikate, Sitzungsbus — und keinerlei Schlüssel:
  Mehrere seiner Variablen lenken einen Aufruf um, ohne etwas anzuzeigen (gemessen:
  eine sendet das Dokument an ein Drittanbieter-Gateway, eine andere an ein kostenpflichtiges
  Google Cloud-Projekt), und eine Denylist vergaß bei jedem Review Variablen.
  Vor jedem Segment muss `agy -p /config`, was kein Kontingent kostet, zeigen,
  dass kostenpflichtige KI-Guthaben deaktiviert sind, ohne API-Schlüssel oder Google Cloud-Projekt — eine
  fehlende Einstellung gilt als Ablehnung —, andernfalls wird nichts übersetzt; das Protokoll jedes
  Aufrufs muss anschließend das Abonnement bestätigen (`authMethod=consumer`), andernfalls wird die
  Antwort abgelehnt.
- **Isolation.** Jeder Aufruf läuft in einem privaten, temporären
  Home-Verzeichnis mit einem werkzeuglosen Übersetzungsagenten: Ihre agy-Einstellungen, Regeln,
  Plugins, MCP-Server und Hooks gelangen nicht dorthin, nichts wird Ihrem Verlauf hinzugefügt,
  und die Verbindung verbleibt im Schlüsselbund, den aipmt niemals ausliest.
  Ein nicht gefundener Agent führt dazu, dass agy stillschweigend auf seinen Coding-Agenten
  und dessen Werkzeuge zurückgreift: Eine vollständige Zeile im Protokoll muss den korrekten Agenten bestätigen — ein
  Dokument, das diese Meldung zitiert, ersetzt dies nicht —, andernfalls erfolgt eine Ablehnung.
- **Plattformen**: Linux, in einer Sitzung mit Schlüsselbund (D-Bus-Sitzungsbus,
  Secret Service); macOS wird akzeptiert, ohne dort gemessen worden zu sein. Unter Windows
  abgelehnt, da agy die Variablen, die jeden Aufruf isolieren, nicht liest, und unter Linux
  ohne Sitzungsbus — SSH-Sitzung, Container, Server: agy legt sein Token dort in einer
  Datei unter `~/.gemini` ab, die durch die Isolation verborgen wird. Die
  Ablehnung erfolgt vor jedem Start samt Begründung, anstatt eine Minute
  auf einen Verbindungscode zu warten.
- **Modelle**: die von `agy models`. Die Gemini-Modelle tragen den Aufwand im Namen
  (`gemini-3.8-flash-medium`…): Ein Name ohne Suffix wird vor dem Aufruf abgelehnt,
  und `--reasoning_effort` ist wirkungslos. Standardmäßig `gemini-3.8-flash-medium`,
  und `gemini-3.7-flash-low` unter `--eco`; die Testläufe, mit denen sie festgelegt wurden,
  sind in [Detaillierte Messungen](#detaillierte-messungen) beschrieben. Claude und GPT-OSS
  haben ihr eigenes, deutlich kleineres Kontingent: etwa 1 % des 5-Stunden-Fensters
  pro gemessenem Aufruf, gegenüber 0,05 % bei Flash.
- **Kontingent**: pro Gruppe ein 5-Stunden-Fenster und ein wöchentliches Fenster,
  anteilig nach Token-Kosten. Gemessen auf dem Konto des Autors: etwa
  16 Punkte des 5-Stunden-Fensters pro Million Quellzeichen bei
  `gemini-3.8-flash-medium`, 14 bei `gemini-3.7-flash-medium` und 7 bis 8 bei
  niedrigem Aufwand — eine README mit 40.000 Zeichen kostet somit etwas mehr als einen
  halben Punkt. Das wöchentliche Limit hängt wiederum vom Tarif ab. Wiederholungsversuche
  richten sich nach dem, was agy als wiederholbar deklariert; andernfalls wird ein erschöpftes Fenster niemals
  erneut versucht: Es lässt jede Datei bis zum Reset fehlschlagen,
  den `/usage` anzeigt.
- **Langsamer als die API**: beim dichten Messartikel im Median 3 Min. 59 Sek. pro
  Sprache bei `gemini-3.8-flash-medium` und 3 Min. 14 Sek. bei
  `gemini-3.7-flash-medium`, gegenüber 1 Min. 18 Sek. für Gemini 3.7 Flash über die API.
- **Unterbrechung**: Strg+C oder ein geschlossenes Terminal stoppen agy zusammen mit dem
  Befehl, anstatt es den Durchlauf auf Kosten Ihres Kontingents beenden zu lassen; dasselbe
  gilt für Codex, die Grok-CLI und OpenCode. Unter `nohup` wird die Übersetzung fortgesetzt.
- In CI verweigert (`CI` oder `GITHUB_ACTIONS` gesetzt): Die Verbindung verbleibt in einem
  persönlichen Schlüsselbund. Auf einem Runner: `--use_gemini` mit `GOOGLE_API_KEY`.
- Variablen: `AGY_BIN` (sonst im `PATH`, danach `~/.local/bin/agy`),
  `AGY_TIMEOUT` (Sekunden pro Segment, einschließlich Start, Standard: 900).

**Nutzungsbedingungen: Sie haften mit Ihrem Konto.** Die
[Nutzungsbedingungen von Antigravity](https://antigravity.google/terms) (Abschnitt 6) und die zugehörige
[FAQ](https://antigravity.google/docs/faq/) untersagen den Zugriff auf den Dienst
über Software von Drittanbietern mithilfe des Antigravity-Logins — Claude Code,
OpenClaw und OpenCode werden dort genannt —, unter Androhung einer Kontosperrung. aipmt
liest das Token weder aus noch verwendet es dieses wieder: Es startet die offizielle Binärdatei im
[Headless-Modus](https://antigravity.google/docs/cli/headless/), den Google
für Skripte und CI dokumentiert. Ein Google-Mitarbeiter bezeichnete es als „üblich“,
`agy -p` aus einem lokalen Skript für die eigene Arbeit zu starten
([offizielles Forum, 25. September 2026, unverbindliche Antwort](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
kein Text regelt den Fall eines verbreiteten Tools wie diesem eindeutig.

**Nur öffentliche Dokumente.** Gemäß Abschnitt 5 derselben Bedingungen können
Interaktionen — Prompts, Antworten, Metadaten — zur Verbesserung der
Produkte und des maschinellen Lernens von Google verwendet und von Menschen
überprüft werden, auch bei einem kostenpflichtigen Abonnement. Das Opt-out erfolgt über die Einstellung
`enableTelemetry`, deren Wirkung nicht dokumentiert ist und die aipmt nicht setzt; Ihre agy-Einstellungen
werden in die isolierte Umgebung nicht übernommen. Verarbeiten Sie darüber nichts Vertrauliches.

### Über das Claude-Abonnement: `--use_claude_code`

Gleiches Prinzip bei `claude`, dem offiziellen CLI von Claude Code, im Modus `-p`: Für
Nutzer von Claude Pro oder Max wird die Übersetzung auf das Kontingent des
Abonnements angerechnet, statt pro Token abgerechnet zu werden. Nicht zu verwechseln mit
`--use_claude`, der API von Anthropic, die nach Nutzung abgerechnet wird.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Kein kostenpflichtiger Pfad bleibt offen, und jeder Aufruf belegt dies.** Claude
  Code erhält aus Ihrer Umgebung nur eine geschlossene Liste von Variablen – weder
  API-Schlüssel, noch Token, noch Cloud-Anbieter, noch Markierungen der Claude-Code-Sitzung,
  aus der aipmt gestartet worden sein könnte. Vor dem ersten Segment muss `claude auth status`
  die Abonnement-Verbindung ohne Console-Schlüssel anzeigen, und `/usage`, was
  kein Kontingent verbraucht, muss dies bestätigen; jeder Aufruf bestätigt dies wiederum in seinem
  Initialisierungsereignis, andernfalls wird die Antwort abgelehnt.
- **Deaktivieren Sie „Extra Usage“** (claude.ai, Einstellungen → Nutzung),
  damit es bei null Euro bleibt: Wenn es aktiviert ist, springt es bei einem erschöpften Zeitfenster
  ein und rechnet ab, ohne einen Fehler anzuzeigen. aipmt bricht die Übersetzung ab, sobald der
  Kontingentbericht eines Aufrufs dies meldet, aber dieser Aufruf wird bereits berechnet.
- **Geteiltes Kontingent mit Ihren Claude-Code-Sitzungen.** Jeder Aufruf meldet
  die Nutzung der 5-Stunden- und Wochen-Zeitfenster; ab 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) wird kein weiteres Segment mehr gestartet,
  um nicht die Ressourcen aufzubrauchen, die für Ihre Arbeit dienen.
- **Isolation.** Jeder Aufruf läuft ohne Tools in einem privaten und
  temporären Verzeichnis im Modus ohne Personalisierung: Weder Ihre `CLAUDE.md`, noch Ihre Plugins,
  Hooks, MCP-Server oder Einstellungen werden geladen, und aus der Sitzung wird
  nichts aufbewahrt. Anhänge sind gekappt: Ein `@chemin` in Ihrem Dokument
  bleibt reiner Text und öffnet keine Datei (gemessen).
- **Modelle**: standardmäßig `sonnet`, mit Aufwand `low`, und ebenso in `--eco`:
  `--eco` ändert auf diesem Pfad nichts. Auf denselben Dokumenten gemessen, ist `haiku`
  doppelt so langsam – es schlussfolgert, ohne dass man es daran hindern könnte – bei
  kaum geringeren Kosten, und `opus` lehnt biologische Inhalte ab (nächster
  Punkt). Beide bleiben über `--model` zugänglich; diese Aliase folgen dem
  neuesten Modell ihrer Familie. `fable` und die Varianten `[1m]` werden abgelehnt,
  da sie über kostenpflichtige Credits laufen. `--reasoning_effort` steuert den Aufwand,
  aus dem eine Übersetzung keinen Nutzen zieht: Das gemessene Reasoning ist gleich null oder fast null.
- **Opus lehnt bestimmte biologische Inhalte ab.** Seine Guardrails sind
  strenger als die von Sonnet, und die Fehlermeldung von Anthropic warnt, dass sie
  „can sometimes flag biology-research-adjacent work“. Gemessen: Eine kurze
  Meldung über 279 generierte Moleküle führte dazu, dass der Artikel in allen vierzehn
  Sprachen abgelehnt wurde. Nichts wird geschrieben: aipmt lehnt die abgeschnittene Antwort ab, benennt die
  Guardrails und empfiehlt `--model sonnet`.
- Abgelehnt in CI (`CI` oder `GITHUB_ACTIONS` gesetzt) und unter Windows (nicht gemessen).
- Variablen: `AIPMT_CLAUDE_BIN` (sonst `PATH`, dann `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (Sekunden pro Segment, Standard 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (Standard 0.8), `CLAUDE_CONFIG_DIR` (das Konto von
  Claude Code, niemals aus einer Projekt-`.env` bezogen); Arbeitsverzeichnisse unter
  `XDG_CACHE_HOME/aipmt/claude-code` (Standard `~/.cache`).

**Nutzungsbedingungen: Sie haften mit Ihrem Konto.** Die
[Rechtshinweisseite von Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
untersagt es nicht, dass „an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription“: Genau das tut aipmt, indem es die offizielle Binärdatei
startet und das Token niemals liest. Anthropic „does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users“, bevorzugt den API-Schlüssel für
Drittanbieter-Tools, „including open-source projects“, und behält sich vor, deren
Nutzung über kostenpflichtige Credits abzurechnen
([Claude-Hilfe](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Kein Text regelt ausdrücklich den Fall eines distribuierten Tools, das die Binärdatei ausführt.

**Daten**: Bei Free-, Pro- und Max-Konten gilt das Training der Modelle
auch für Claude Code, wenn die Datenschutzeinstellung dies zulässt
([Datenseite](https://code.claude.com/docs/en/data-usage)). aipmt speichert
keine lokalen Transkriptionen (`--no-session-persistence`). Übertragen Sie
darüber nichts Vertrauliches.

### Zum Anbieter eigener Wahl: `--use_opencode`

[OpenCode](https://opencode.ai) ist ein Open-Source-Code-Agent (MIT), der
Anfragen an die darin konfigurierten Anbieter weiterleitet: API-Schlüssel, Abonnement,
OpenCode Zen-Gateway (kostenlose Modelle, ohne Konto) oder lokales Modell. Zwei
Pfade wurden hier von Ende zu Ende gemessen: Zen und Ollama.

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

`--model` ist obligatorisch: Ohne diese Angabe würde OpenCode auf ein kostenloses Modell zurückgreifen,
dessen Dialoge für das Training verwendet werden können, und diese Entscheidung wird nicht
an Ihrer Stelle getroffen.

Isolation bei jedem Aufruf:

- Eine Inline-Konfiguration mit Vorrang vor Ihrer eigenen definiert einen Agenten `aipmt`,
  dessen Tools alle verweigert werden (`permission: { "*": "deny" }`), Sitzungsfreigabe
  deaktiviert, `--pure`, niemals `--auto`;
- temporäres und leeres Arbeitsverzeichnis, `OPENCODE_DISABLE_PROJECT_CONFIG` und
  `OPENCODE_DISABLE_CLAUDE_CODE` abgelegt – ohne sie fügt OpenCode die `AGENTS.md`
  des aktuellen Verzeichnisses und `~/.claude/CLAUDE.md` in den Prompt ein. Die
  globale `~/.config/opencode/AGENTS.md` bleibt injiziert, OpenCode erlaubt es nicht,
  sie zu übergehen;
- Ausgabevertrag: Rückgabecode 0, kein `error`-Ereignis, kein
  Tool-Aufruf, letzter Schritt als `stop`, nicht-leerer Text und der Agent `aipmt`
  tatsächlich geladen – ein unbekanntes `--agent` bringt OpenCode nicht zum Scheitern, es
  fällt stillschweigend auf den Coding-Agenten zurück;
- es wird kein Schlüssel aus `aipmt` übertragen, außer `OPENCODE_API_KEY`, dem Schlüssel
  von OpenCode selbst. Die Anbieter werden in OpenCode konfiguriert, nicht in
  der `.env` von `aipmt`.

Wichtig zu wissen:

- Die kostenlosen Modelle von Zen ändern sich ständig, haben undokumentierte Limits, und
  ihre Dialoge können für das Training verwendet werden: für öffentliche Dokumentation
  geeignet, nicht für private Inhalte.
- Ein lokales Modell muss mindestens 16 k Kontext-Tokens bieten, da Segmente
  bis zu 16.000 Zeichen umfassen. Ollama konfiguriert oft 4.096: Nutzen Sie
  ein `Modelfile` mit `PARAMETER num_ctx 32768`.
- `--eco` ist wirkungslos; `--reasoning_effort` wird unverändert als
  `--variant` von OpenCode übergeben.
- OpenCode protokolliert jede Sitzung in `~/.local/share/opencode/`.
- Variablen: `OPENCODE_BIN` (sonst `PATH`, dann `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (Sekunden pro Segment, Standard 600). `OPENCODE_CONFIG`
  wird unverändert an OpenCode durchgereicht.

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

`reasoningEffort: "none"` schaltet das Reasoning ab, das Ollama bei diesen
Modellen standardmäßig aktiviert und das ein Modelfile nicht deaktivieren kann. Gemessen an einem Satz
von sechs Wörtern: 919 Reasoning-Tokens und 68 Sekunden ohne diese Option, 9 Tokens mit ihr.

### Zu mehr als 400 Modellen: `--use_openrouter`

OpenRouter ist ein Router mit nutzungsbasierter Abrechnung über ein zentrales Guthaben für
Modelle, die von Drittanbietern gehostet werden – darunter offene chinesische Modelle, die kein
anderer Provider hier anbietet.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` ist obligatorisch. Ein Preflight, der vor jeder Abrechnung ausgeführt wird, regelt
zwei Besonderheiten des Routings:

- **Dasselbe Modell wird von Dutzenden Hostern mit unterschiedlichen Limits bereitgestellt** –
  bei `z-ai/glm-5.3-flash` sind es 23 Hoster, darunter einer mit einem Limit von
  2.048 Output-Tokens. Der Preflight liest `/api/v1/models/{modèle}/endpoints`,
  schließt Hoster mit unter 8.000 Output-Tokens oder herabgestuftem Status aus und
  pinnt die übrigen mit `allow_fallbacks: false` fest.
- **Reasoning wird zum Ausgabetarif abgerechnet** – 107 Tokens gegenüber 2 bei
  einer „OK“-Antwort von `z-ai/glm-5.2`. Es ist standardmäßig deaktiviert; Modelle,
  die es erzwingen, erhalten den geringstmöglichen Aufwand, den sie akzeptieren, da der
  Katalogstandard die Ausgabe vor dem Ende der Übersetzung erschöpfen kann.
  `--reasoning_effort` bleibt vorrangig.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Das Kontextfenster stammt aus dem Katalog. Ein Modell mit weniger als 16.400 Tokens wird
  vor jedem Aufruf abgelehnt: 8.400 für Prompt und Segment, mindestens 8.000
  für die Ausgabe.
- Ein im Katalog fehlender Slug, ein nicht erreichbarer Katalog oder das Fehlen
  eines Hosters, der das Limit einhält, stoppen den Befehl.
- `finish_reason=length` mit leerer Ausgabe bedeutet ein durch Reasoning
  aufgebrauchtes Budget, keine Kürzungsmaßnahme: Die Meldung unterscheidet dies.
- `--eco` ist wirkungslos.
- Variablen: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (Standard `https://openrouter.ai/api/v1`, `https://`
  erforderlich), `OPENROUTER_TIMEOUT` (Standard 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (Standard 30).

### Übersetzungshinweis

`--add_translation_note` fügt einen Hinweis hinzu, an Position `bottom` (Standard), `top` (nach dem
Frontmatter) oder `both` (`--note_position`), im Format `legacy` (fetter
Absatz, Standard) oder `marker` (`--note_format`). Das Format `marker` ist eine
unsichtbare Markdown-Referenzdefinition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
gefolgt von einem fetten Zitat: lesbar auf GitHub, beim Build durch ein
remark-Plugin verwertbar.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detaillierte Messungen

Alle Messungen basieren auf tatsächlich mit `aipmt` durchgeführten Übersetzungen in
vierzehn Sprachen: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Geschrieben** zählt die Dateien, die die Sicherheitsprüfungen passiert haben; **Ohne
Abweichung** jene, bei denen `scripts/compare_structure.py` nichts beanstandet – gleiche Anzahl an
Abschnitten, Untertiteln, Links, eindeutigen URLs, Codeblöcken,
Inline-Code-Elementen, Tabellenzeilen, Zitatblöcken und fettgedruckten Wörtern.

„Ohne Abweichung“ bedeutet „nichts erkannt“, nicht „identisch“: Der Vergleicher
zählt Elemente, ohne deren Inhalt zu lesen. Er bemerkt weder eine gelöschte
Überschrift der Ebene 4, noch ersetzten Text innerhalb eines Inline-Codes, noch vertauschte
Flaggen, noch einen internen Link, der mit einer schließenden Klammer zu viel ausgegeben wurde,
`[texte]((#ancre))`, sodass er ins Leere führt – und er beurteilt nicht die
Sprachqualität.

### Dichter Watch-Artikel, Modus `--news`

Eine Ausgabe der [KI-Watch von jls42.org](https://jls42.org/fr/news):
589 Zeilen, 140 Links, 21 Abschnitte, 3 geschützte englische Zitate. Testreihe
vom 4. und 5. September 2026.

| Modell                                          | Zugang             | Geschrieben | Ohne Abweichung | Median/Sprache |
| ----------------------------------------------- | ------------------ | ----------- | --------------- | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14       | ✅ **14/14**    | 1 Min. 18 Sek. |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google-Abonnement  | 14/14       | ✅ **14/14**    | 3 Min. 59 Sek. |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google-Abonnement  | 14/14       | ✅ **14/14**    | 3 Min. 14 Sek. |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT-Abonnement | 14/14       | ✅ **14/14**    | 11 Min. 28 Sek.|
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14       | ✅ **14/14**    | 5 Min. 37 Sek. |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14       | ✅ **14/14**    | 26 Min. 23 Sek.|
| `sonnet` (`--use_claude_code`)                  | Claude-Abonnement  | 14/14       | ⚠️ 13/14        | 6 Min. 49 Sek. |
| `claude-sonnet-5`                               | Anthropic API      | 14/14       | ⚠️ 11/14        | 6 Min. 31 Sek. |
| `haiku` (`--use_claude_code`)                   | Claude-Abonnement  | 14/14       | ⚠️ 11/14        | 15 Min. 54 Sek.|
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14       | ❌ 11/14        | 9 Min. 27 Sek. |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14       | ❌ 8/14         | 10 Min. 09 Sek.|
| `ollama/gpt-oss-20b-32k`                        | lokal              | 10/14       | ❌ 7/14         | 12 Min. 39 Sek.|
| `mistral-large-latest`                          | Mistral API        | 11/14       | ❌ 5/14         | 5 Min. 32 Sek. |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14        | ❌ 3/14         | 37 Min. 27 Sek.|
| `grok-4.6` (`--use_grok_cli`)                   | Grok-Abonnement    | 1/14        | ❌ 1/14         | 23 Min. 11 Sek.|
| `opus` (`--use_claude_code`)                    | Claude-Abonnement  | 0/14        | ❌ 0/14         | —              |

Grok wurde am 9. September bei einer anderen Ausgabe derselben Watch
(356 Zeilen) erneut gemessen: 9 von 14 Sprachen geschrieben, 8 ohne Abweichung. Diese Zahl
erscheint in der oberen Tabelle. Drei abgebrochene Kampagnen sind nicht
aufgeführt: `qwen3.5-27b` (9 Sprachen) und `kimi-k2.6` (4) mangels Guthaben,
`z-ai/glm-5.3-flash`, dessen zwei Fehlschläge auf eine Reasoning-Einstellung zurückzuführen waren,
die der Provider inzwischen korrigiert hat. Die OpenRouter-Zeilen wurden mit den
Standardeinstellungen des Routers vor `--use_openrouter` gemessen; `z-ai/glm-5.2`,
erneut gemessen mit dem ausgelieferten Provider, liefert dieselben 14/14. Die Zahlen wurden
am 10. September mit dem aktuellen Vergleicher neu berechnet: `qwen3.8-flash` und
`qwen3.7-flash` gewinnen jeweils eine Sprache im Vergleich zur ersten
Veröffentlichung, die übrigen bleiben unverändert.

Die Zeilen zu `--use_antigravity` wurden am 26. September auf demselben
Artikel gemessen, vier Übersetzungen parallel: `gemini-3.7-flash-medium` am Vormittag,
`gemini-3.8-flash-medium` am Nachmittag. Im Englischen entfernte jedes Modell selbstständig
die drei Zeilen mit französischer Übersetzung unter den Zitaten, ohne Flaggen zu
erfinden, und die englischen Zitate blieben intakt: Die Ausweichbereinigung musste
nicht eingreifen. Bei `--eco` (`gemini-3.7-flash-low`), auf nur vier Sprachen
(en, ja, ar, hi): 4 von 4 geschrieben, alle ohne Abweichung, 1 Min. 52 Sek.
Median. Gegenprobe am selben Tag bei einer neueren Ausgabe der Watch,
jener vom 25. September (438 Zeilen, 2 englische Zitate), übersetzt außerhalb des
Blogs mit `gemini-3.7-flash-medium`: 14 von 14 geschrieben, alle ohne Abweichung, 87 bis
128 Sek. pro Sprache.

Die Zeilen zu `--use_claude_code` wurden am 26. September auf demselben
Artikel gemessen, vier Übersetzungen parallel, mit Aufwand `low`. Mit `sonnet` blieben
die englischen Zitate in allen vierzehn Sprachen intakt und im Englischen entfernte das
Modell selbstständig die französischen Übersetzungszeilen, ohne Flaggen zu
erfinden. `opus` schrieb in keiner Sprache: In jeder Sprache stoppten seine Guardrails
die Antwort beim letzten Segment aufgrund einer kurzen Meldung über 279 generierte
Moleküle für eine Bindungsstelle. Isoliert gesendet, wird diese Meldung unter der
Kategorie „Bio“ abgelehnt; `sonnet` übersetzte sie überall. `haiku` schrieb
alle vierzehn Sprachen; in drei (en, pl, ro) wechselte eine Abschnittsüberschrift von
Ebene 2 auf Ebene 1. Es schlussfolgert, ohne dass man es daran hindern könnte – 61 %
seiner Output-Tokens –, daher benötigte es mehr als die doppelte Zeit von `sonnet`.

### README dieses Projekts, Standard-Markdown

Eingefrorene Revision vom 9. September 2026: 785 Zeilen, 285 Inline-Codes, 40
Blockabschlüsse, 89 Tabellenzeilen. Vier parallele Übersetzungen.

| Modell                                          | Geschrieben | Ohne Abweichung | Median/Sprache | Was sich unterscheidet                                                   |
| ----------------------------------------------- | ----------- | --------------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14       | ✅ 14/14        | 1 Min. 43 s    | nichts                                                                   |
| `opus` (`--use_claude_code`)                    | 14/14       | ✅ 14/14        | 1 Min. 48 s    | nichts                                                                   |
| `haiku` (`--use_claude_code`)                   | 14/14       | ✅ 14/14        | 4 Min. 02 s    | nichts für das Vergleichstool; interne Links verdoppelt (en)             |
| `gemini-3.7-flash`                              | 14/14       | ⚠️ 13/14        | 36 s           | ein fettgedrucktes Wort (ja)                                             |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14       | ⚠️ 13/14        | 1 Min. 22 s    | ein fettgedrucktes Wort (ko)                                             |
| `sonnet` (`--use_claude_code`)                  | 14/14       | ⚠️ 13/14        | 2 Min. 20 s    | eine Tabellenzeile an die vorherige angehängt (ar)                       |
| `claude-sonnet-5`                               | 14/14       | ⚠️ 12/14        | 2 Min. 56 s    | ein Link (sv), ein fettgedrucktes Wort (zh)                              |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14       | ⚠️ 12/14        | 6 Min. 46 s    | ein fettgedrucktes Wort (ar, ja)                                         |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14       | ⚠️ 11/14        | 2 Min. 34 s    | ein fettgedrucktes Wort (hi, ja, ko)                                     |
| `qwen/qwen3.7-flash`                            | 14/14       | ⚠️ 10/14        | 2 Min. 17 s    | 40 Inline-Codes auf Arabisch hinzugefügt; fett (hi, ja, ko)               |
| `mistral-large-latest`                          | 14/14       | ❌ 1/14         | 2 Min. 44 s    | ein verlorener Abschnitt (ar, hi, ko); Codeblöcke hinzugefügt (ja, ko, ro, zh) |

Zwei abgebrochene Testläufe sind nicht aufgeführt: Grok, CLI-Sitzung nach
zwölf Sprachen abgelaufen (elf ohne Abweichung), und `qwen3.8-flash`, HTTP 429
von dessen Hoster nach zwei. `opencode/mimo-v2.5-free` und `ollama/gpt-oss-20b-32k`
wurden bei dieser Revision nicht erneut gemessen; bei der vom 4. und 5. September,
die um 277 Zeilen kürzer war, erstellten sie jeweils 9 von 14 Übersetzungen, davon 7
und 1 ohne Abweichung.

Die Zeilen `--use_antigravity` und `--use_claude_code` wurden nicht an
der eingefrorenen Revision gemessen, sondern am 26. September an der mit 1.14.0
veröffentlichten Version: 600 Zeilen, 257 Inline-Codes, 30 Blockabschlüsse, 85
Tabellenzeilen. Da sie 185 Zeilen kürzer ist, lässt sie sich nicht eins zu eins mit
den anderen Zeilen vergleichen; diese Zeilen lassen sich jedoch untereinander vergleichen.
Bei den internen Links, die das Vergleichstool nicht prüft, behielt `gemini-3.8-flash-medium`
sie in allen vierzehn Sprachen intakt, `gemini-3.7-flash-medium` beschädigte sie auf Italienisch;
`sonnet` und `opus` behielten sie überall intakt, `haiku` verdoppelte sie auf
Englisch.

### Vier README bekannter Projekte

FastAPI, Ollama, tldr-pages und Vue.js, unverändert von GitHub übernommen –
einfachere Dokumente als die beiden vorherigen. Der Testlauf zielte auf die
Modelle mit Schwierigkeiten ab; Gemini dient hierbei als Vergleichspunkt.

| Modell                    | Umfang                     | Geschrieben | Ohne Abweichung |
| ------------------------- | -------------------------- | ----------- | --------------- |
| `gemini-3.7-flash`        | 4 Projekte × 14 Sprachen   | 56/56       | ✅ **55/56**    |
| `opencode/mimo-v2.5-free` | 4 Projekte × 14 Sprachen   | 55/56       | ❌ 47/56        |
| `grok-4.6` (Abonnement)   | 4 Projekte × ar, hi, ja, zh | 16/16       | ❌ 14/16        |
| `ollama/gpt-oss-20b-32k`  | 4 Projekte × ar, hi, ja, zh | 15/16       | ❌ 9/16         |

### Was diese Messungen nicht sind

- **Keine erschöpfende Rangliste**: Allein OpenRouter bietet mehr als vierhundert
  Modelle an, rund fünfzehn wurden gemessen.
- **Richtwerte für die Dauer**: je nach Testlauf drei bis sechs parallele
  Übersetzungen, und der Durchsatz eines Anbieters schwankt im Tagesverlauf.
- **Zeitgebundene Beobachtungen**: Modelle ändern sich unter demselben Namen, und Ihre
  Dokumente sind nicht unsere.

Um die Messung mit Ihren Dokumenten anhand einer eingefrorenen Kopie der Datei zu wiederholen:

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

Qualitätswerkzeuge, optional, aber empfohlen:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Die 28 Übersetzungen des Repositorys (README und CHANGELOG, vierzehn Sprachen)
werden mit `./regen_translations.sh --force` neu generiert – standardmäßig Codex und `gpt-5.6-sol`
über das ChatGPT-Abonnement, vier parallel. `REGEN_PROVIDER` und
`REGEN_MODEL` ändern den Pfad: `antigravity` bleibt bei einem Abonnement, dem
von Google, und läuft ohne Ausnahmeregelung durch; eine kostenpflichtige API (`openai`, `gemini`,
`grok`, `openrouter`) wird ohne `REGEN_ALLOW_PAID_API=1` abgelehnt;
`REGEN_JOB_TIMEOUT` begrenzt jeden Job zeitlich (600 s, 1.800 s bei Codex und
Antigravity). Details zu den Werkzeugen finden sich in `CLAUDE.md`.

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** – persönlicher Blog, der in 15 Sprachen veröffentlicht wird. Seine
  [tägliche KI-Beobachtung](https://jls42.org/fr/news) wird täglich mit diesem Tool übersetzt
  und dient als Referenzdokument für die obigen Messungen.

## Autor

Julien LE SAUX
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Haftungsausschluss

Dieses Programm wird **ohne jede Gewährleistung** gemäß den Abschnitten
15 und 16 der GPL v3 verbreitet: Es wird „wie besehen“ bereitgestellt, ohne ausdrückliche
oder stillschweigende Garantie der Marktreife oder der Eignung für einen bestimmten Zweck,
und der Autor kann für Schäden, die aus seiner Nutzung entstehen, nicht haftbar
gemacht werden. Der Text der Lizenz hat Vorrang vor dieser Zusammenfassung.

- **Lesen Sie vor der Veröffentlichung Korrektur.** Die Schutzmechanismen decken die
  Codeblöcke, den Inline-Code, die URLs, die Anker und die Zitate im Modus `--news` ab – weder
  die Überschriften, noch die Tabellen, noch das Frontmatter, noch den Sinn Ihrer Sätze.
- **Ihre Dokumente werden an den ausgewählten Anbieter übermittelt**, gemäß dessen
  Nutzungsbedingungen und Datenschutzrichtlinien. Einige kostenlose Modelle können
  Ihre Konversationen für das Training wiederverwenden, und die Bedingungen von Antigravity
  erlauben Google, diese wiederzuverwenden und durch Menschen prüfen zu lassen,
  auch bei einem kostenpflichtigen Abonnement; ein lokales Modell ist die einzige Möglichkeit,
  bei der keine Daten Ihren Rechner verlassen.
- **API-Aufrufe werden Ihnen in Rechnung gestellt.** Dieses Programm deckelt die
  Ausgaben nicht: Ein langes Dokument, eine Wiederholung nach einem Fehler oder ein
  Modell, das viel nachdenkt (Reasoning), kosten mehr.
- **Die veröffentlichten Messungen sind zeitgebundene Beobachtungen**, keine Garantien.

Die genannten Produkt- und Firmennamen gehören ihren jeweiligen Inhabern.
Dieses Projekt steht in keiner Verbindung zu einem von ihnen.

**Artikel übersetzt aus dem Französischen ins Deutsche mit gemini-3.8-flash-medium.**

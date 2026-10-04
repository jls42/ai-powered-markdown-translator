# AI-Powered Markdown-Übersetzer

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Code-Qualität</h4>

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

Übersetzt Markdown-Dateien von einer Sprache in eine andere unter Beibehaltung der
Struktur: Code-Blöcke, Inline-Code, URLs, Anker, Tabellen und Frontmatter.
Elf Möglichkeiten, ein Modell aufzurufen – fünf APIs, vier Abonnements ohne
nutzungsbasierte Abrechnung, zwei Router – und ein veröffentlichter Vergleich dessen, was jedes
Modell tatsächlich bewahrt.

## Auf einen Blick

- **Elf Provider-Pfade**: APIs von OpenAI, Mistral, Claude, Gemini und Grok;
  ChatGPT- (Codex), Grok-, Google- (Antigravity) und Claude-Abonnements (Claude
  Code) ohne nutzungsbasierte Abrechnung; Router OpenCode (Open Source, kostenlos oder lokal) und OpenRouter
  (über 400 Modelle).
- **Keine Verfälschungen durch verlorene Tokens**: Code-Blöcke, Inline-Code,
  URLs, Anker und Zitate werden vor dem Aufruf durch Tokens ersetzt und
  bei der Rückgabe überprüft. Fehlt auch nur ein einzelnes, wird die Datei nicht geschrieben.
- **Lange Dokumente**: Segmentierung basierend auf dem Kontextfenster des Modells.
- **`--news`-Modus**: geschützte englische Zitate und sprachspezifisch verwaltete
  Flaggen für Monitoring- und News-Artikel.
- **`--eco`-Modus**: schnellere und kostengünstigere Modelle.
- **Optionale Übersetzungsnotiz**, oben, unten oder an beiden Stellen.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 oder neuer. Zur Installation aus dem Repository siehe
[Mitwirken](#mitwirken).

## Konfiguration

Schlüssel werden an drei Orten gelesen, in absteigender Priorität; jeder füllt
nur das aus, was der vorherige offengelassen hat.

|     | Wo                                            | Wofür                                 |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Umgebungsvariablen                            | CI, Container, einmalige Überschreibung |
| 2   | `.env` des aktuellen Verzeichnisses (oder eines übergeordneten) | ein projektspezifischer Schlüssel     |
| 3   | `~/.config/aipmt/.env`                                 | einmal installiert, gilt überall      |

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

`GEMINI_API_KEY` wird anstelle von `GOOGLE_API_KEY` akzeptiert. Die Benutzerdatei
folgt `XDG_CONFIG_HOME` (nur absoluter Pfad) und `%APPDATA%`
unter Windows. Ohne Schlüssel listet der Befehl alle drei Speicherorte auf.

**Die `.env` eines Projekts kann weder Aufrufe umleiten noch das ausgeführte Programm
festlegen.** Sie liefert Schlüssel, niemals ein Ziel oder ein Binary: Alle
Variablen mit `_BASE_URL`, `_API_BASE`, `_ENDPOINT` oder `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, Proxys (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), Zertifikatsspeicher (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) sowie `XDG_CONFIG_HOME` /
`APPDATA` werden darin ignoriert, begleitet von einer Warnung. Ein geklontes Repository darf
weder Ihren Schlüssel abfangen noch Sie dazu bringen, bei der ersten Übersetzung dessen eigenes
Programm auszuführen. Diese Datei wird zudem ohne Interpolation gelesen:
`NOM=${OPENAI_API_KEY}` kopiert den Schlüssel darin nicht. Setzen Sie diese Variablen in
der Umgebung oder in `~/.config/aipmt/.env`.

Optionale Variablen: `XAI_BASE_URL` (Standardwert `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (Sekunden pro Aufruf, Standardwert 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(Standardwert 600), `GROK_BIN`, `GROK_HOME` (Standardwert `~/.grok`), `GROK_TIMEOUT`
(Standardwert 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (Standardwert 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (Standardwert 600), `OPENROUTER_BASE_URL`
(`https://` erforderlich), `OPENROUTER_TIMEOUT` (Standardwert 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (Standardwert 30). Jede davon wird im
Abschnitt des jeweiligen Providers ausführlich beschrieben.

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
mit `--include_model`, `document-es-gpt-5.6-terra.md`. Die Dateiendung wird
immer `.md` – `article.mdx` ergibt `article-en.md` – außer bei
`--keep_filename`, wodurch der ursprüngliche Name beibehalten wird. Eine bereits vorhandene
Übersetzung wird ohne `--force` übersprungen.

Exit-Codes: `0`, wenn alles erfolgreich war oder übersprungen wurde, `1`, wenn mindestens eine Datei
fehlgeschlagen ist (Auflistung auf der Fehlerausgabe), `2`, wenn ein Konfigurationsproblem vorliegt.
Eine fehlgeschlagene Datei wird niemals geschrieben, selbst wenn der Schreibvorgang selbst fehlschlägt:
Der Inhalt wird temporär daneben geschrieben und anschließend umbenannt. Ein erneutes Ausführen genügt.

## Welches Modell wählen

Gemessen an zwei realen Dokumenten, die von jedem Modell in dieselben vierzehn Sprachen
übersetzt wurden. **Die Zahl gibt an, in wie vielen von vierzehn Sprachen die
Übersetzung geschrieben wurde und keinerlei Abweichungen zur Quelle aufweist.**

| Modell               | Zugang                            | Dichter Monitoring-Artikel | Diese README | Was abweicht, und in wie vielen Sprachen                                                                                                                           |
| -------------------- | --------------------------------- | -------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash** | Google-Abonnement (Antigravity)   | ✅ 14/14                   | ✅ 14/14     | nichts, bei keinem der beiden Dokumente                                                                                                                            |
| **Gemini 3.7 Flash** | Google-API-Schlüssel              | ✅ 14/14                   | ⚠️ 13/14     | 1 von 14 Sprachen: ein zusätzliches fettgedrucktes Wort (ja)                                                                                                       |
| **Gemini 3.7 Flash** | Google-Abonnement (Antigravity)   | ✅ 14/14                   | ⚠️ 13/14     | 1 von 14 Sprachen: ein fettgedrucktes Wort weniger (ko)                                                                                                            |
| **GPT-5.6 Sol**      | ChatGPT-Abonnement oder OpenAI-Schlüssel | ✅ 14/14            | ⚠️ 12/14     | 2 von 14 Sprachen: ein fettgedrucktes Wort weniger (ar, ja)                                                                                                       |
| **GLM-5.2**          | OpenRouter-Schlüssel              | ✅ 14/14                   | ⚠️ 11/14     | 3 von 14 Sprachen: ein fettgedrucktes Wort weniger (hi, ja, ko)                                                                                                    |
| Claude Sonnet 5      | Claude-Abonnement (Claude Code)   | ⚠️ 13/14                   | ⚠️ 13/14     | 1 von 14 Sprachen beim Artikel: ein zusätzliches fettgedrucktes Wort (zh); 1 bei dieser README: eine Tabellenzeile an die vorherige angehängt, bei der Anzeige ausgeblendet (ar) |
| Claude Haiku 4.5     | Claude-Abonnement (Claude Code)   | ⚠️ 11/14                   | ✅ 14/14     | 3 Sprachen beim Artikel: eine Abschnittsüberschrift auf Ebene 1 heraufgestuft (en, pl, ro); bei dieser README nichts für den Vergleicher, aber interne Links auf Englisch dupliziert |
| Claude Sonnet 5      | Anthropic-API-Schlüssel            | ⚠️ 11/14                   | ⚠️ 12/14     | 3 Sprachen beim Artikel: ein Code-Block aufgetaucht (es, de, hi); 2 bei dieser README: ein Link ohne Formatierung (sv), ein fettgedrucktes Wort (zh)                |
| Qwen 3.7 Flash       | OpenRouter-Schlüssel              | ❌ 8/14                    | ⚠️ 10/14     | 1 Sprache beim Artikel abgelehnt, 5 weitere weichen ab; bei dieser README rund vierzig Wörter in `code` gesetzt (ar)                                       |
| Grok 4.6             | Grok-Abonnement                   | ❌ 8/14                    | nicht bewertet | 5 von 14 Sprachen abgelehnt, da Inline-Codes und URLs fehlten; Niederländisch weicht vollständig ab                                                               |
| GPT-OSS 20B          | lokales Modell (Ollama)           | ❌ 7/14                    | nicht erneut gemessen | 4 von 14 Sprachen abgelehnt: Das Modell beließ Passagen auf Französisch, die Sicherheitsprüfung stoppte sie                                                        |
| MiMo v2.5 (kostenlos) | OpenCode Zen, ohne Konto         | ❌ 11/14                   | nicht erneut gemessen | 1 Sprache abgelehnt; ein verlorener Abschnitt auf Polnisch                                                                                                        |
| Mistral Large        | Mistral-API-Schlüssel             | ❌ 5/14                    | ❌ 1/14      | **ein kompletter Abschnitt verschwindet**: 1 Sprache beim Artikel (hi), 3 bei dieser README (ar, hi, ko) – und 3 Sprachen beim Artikel abgelehnt                   |
| DeepSeek V4 Flash    | OpenRouter-Schlüssel              | ❌ 3/14                    | nicht erneut gemessen | 10 von 14 Sprachen abgelehnt; 37 Minuten pro Sprache                                                                                                              |
| Claude Opus 5.5      | Claude-Abonnement (Claude Code)   | ❌ 0/14                    | ✅ 14/14     | der Artikel in allen 14 Sprachen durch die Sicherheitsfilter von Opus abgelehnt, wegen einer biologischen Kurzmeldung; nichts bei dieser README                    |

|     | Bedeutung des Symbols                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alle vierzehn Sprachen übersetzt und keinerlei Abweichung von der Quelle                                                                                                                              |
| ⚠️  | alle vierzehn Sprachen übersetzt; was abweicht, ist reine **Formatierung** – ein fettgedrucktes Wort, ein `code`, ein Link, der seine eckigen Klammern verliert. Kein Text, keine URL, kein Code-Block, kein Abschnitt fehlt |
| ❌  | mindestens eine Sprache konnte nicht übersetzt werden – die Datei wird abgelehnt, nicht geschrieben – **oder** in einer geschriebenen Datei fehlt Inhalt                                              |

Was man daraus mitnehmen sollte:

- **Eine abgelehnte Übersetzung ist keine beschädigte Übersetzung.** Wenn bei
  der Rückgabe ein Token fehlt, wird die Datei nicht geschrieben und die Sprache gilt als
  abgelehnt. Genau das passiert Grok beim Artikel: Vier Inline-Codes und
  drei URLs gingen bereits im ersten Segment bei den fünf nicht-lateinischen Schriften verloren.
- **Ein Modell kann ein ganzes Dokument wegen eines einzigen Satzes ablehnen.** Opus 5.5
  übersetzt diese README ohne jede Abweichung, aber keinen einzigen Monitoring-Artikel: Seine
  Guardrails brechen die Antwort bei einer biologischen Kurzmeldung ab. Die Datei wird nicht
  geschrieben, und aipmt nennt den Grund dafür.
- **Dieses Sicherheitsnetz deckt weder Überschriften, Tabellen, Frontmatter noch den
  Fliesstext ab.** Ein Modell, das einen Abschnitt entfernt, liefert eine Datei zurück, die das Tool
  beanstandungslos schreibt – so der Fall bei Mistral. Diese Elemente lassen sich nicht
  durch Tokens ersetzen, und die aktuellen Schutzmechanismen prüfen sie nicht;
  `scripts/compare_structure.py` erkennt einen verlorenen Abschnitt zwar, jedoch erst im Nachhinein.
- **Grok hat keine Bewertung für diese README**: Die CLI-Sitzung lief nach zwölf
  Sprachen ab, von denen elf fehlerfrei waren. Eine abgebrochene Testreihe wird nicht bewertet.
- **Die Informationsdichte des Dokuments wiegt schwerer als die Sprache.** Grok bewältigt
  gewöhnliche READMEs problemlos, bricht jedoch bei einem stark verlinkten Artikel ein, selbst auf
  Niederländisch.

Daten und Dokumente: Die Spalte „Diese README“ wurde am 9. September 2026
anhand einer eingefrorenen Revision dieser Datei gemessen (785 Zeilen, 285 Inline-Codes, 89 Tabellenzeilen),
die seither überarbeitet wurde – mit Ausnahme der Zeilen für Antigravity und Claude Code,
die am 26. September auf der mit 1.14.0 veröffentlichten, kürzeren Revision gemessen wurden
(600 Zeilen, 257 Inline-Codes, 85 Tabellenzeilen). Die Spalte „Dichter Monitoring-Artikel“
stammt aus der Testreihe vom 4. und 5. September mit einem 589 Zeilen langen Artikel, mit Ausnahme
der Grok-Zeile, die am 9. September anhand einer anderen Ausgabe desselben Newsletters nachgemessen wurde,
sowie der Zeilen für Antigravity und Claude Code, die am 26. September anhand desselben Artikels gemessen wurden.
Vollständige Tabellen, Laufzeiten und das Testprotokoll finden sich unter
[Detaillierte Messungen](#detaillierte-messwerte).

## Alle Optionen

| Option                   | Beschreibung                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Einzelne Markdown-Datei zum Übersetzen (Alternative zu `--source_dir`)                                             |
| `--source_dir`           | Quellverzeichnis mit den Markdown-Dateien (Standard: `content/posts`)                                   |
| `--target_dir`           | Ausgabeverzeichnis für die übersetzten Dateien (Standard: `traductions_en`)                                    |
| `--source_lang`          | Quellsprache (Standard: `fr`)                                                                                  |
| `--target_lang`          | Zielsprache (Standard: `en`)                                                                                   |
| `--model`                | Spezifisches zu verwendendes Modell                                                                                  |
| `--eco`                  | Kostengünstige Modelle verwenden                                                                              |
| `--use_mistral`          | Mistral-AI-API verwenden                                                                                     |
| `--use_claude`           | Claude-API verwenden                                                                                         |
| `--use_gemini`           | Gemini-API verwenden                                                                                         |
| `--use_grok`             | xAI-API (Grok) verwenden — erfordert `XAI_API_KEY`                                                           |
| `--use_codex`            | Codex-CLI über das Kontingent des ChatGPT-Abonnements verwenden                                                    |
| `--use_grok_cli`         | Grok-CLI über das Kontingent des Grok-Abonnements verwenden                                                        |
| `--use_antigravity`      | Antigravity-CLI (`agy`) über das Kontingent des Google AI Pro- oder Ultra-Abonnements verwenden                       |
| `--use_claude_code`      | Claude-Code-CLI (`claude -p`) über das Kontingent des Claude Pro- oder Max-Abonnements verwenden                      |
| `--use_opencode`         | OpenCode (Open Source) mit dem in OpenCode konfigurierten Provider verwenden; erfordert `--model provider/modèle` |
| `--use_openrouter`       | OpenRouter verwenden — erfordert `OPENROUTER_API_KEY` und `--model fournisseur/modèle`                          |
| `--force`                | Neuübersetzung erzwingen                                                                                       |
| `--keep_filename`        | Ursprünglichen Dateinamen beibehalten                                                                          |
| `--news`                 | Nachrichtenmodus: schützt EN-Zitate, verwaltet Flaggen nach Sprache                                      |
| `--add_translation_note` | Übersetzungshinweis hinzufügen                                                                                |
| `--note_position`        | Position des Hinweises: `top`, `bottom` (Standard) oder `both`                                                     |
| `--note_format`          | Format des Hinweises: `legacy` (Standard, fetter Absatz) oder `marker`                                            |
| `--include_model`        | Modellnamen in der Ausgabedatei angeben                                                            |
| `--reasoning_effort`     | GPT-5.x-Reasoning-Aufwand: `none`/`low`/`medium`/`high`/`xhigh`                                         |

Die neun Flags `--use_*` schließen sich gegenseitig aus: Die Kombination von zweien wird
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

`--eco` wechselt auf die kostengünstige Stufe des jeweiligen Providers.

| Provider    | Qualität (Standard)                                   | Kostengünstig (`--eco`) |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol` (auch `terra` und `luna` über `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, Aufwand `low`                                | ebenso — `--eco` ohne Wirkung |
| OpenCode    | `--model provider/modèle` erforderlich                 | ebenso — `--eco` ohne Wirkung |
| OpenRouter  | `--model fournisseur/modèle` erforderlich              | ebenso — `--eco` ohne Wirkung |

### Über das ChatGPT-Abonnement: `--use_codex`

Steuert die offizielle Codex-CLI: Die Übersetzung wird vom Kontingent des
ChatGPT-Abonnements abgebucht, ohne API-Schlüssel oder nutzungsbasierte Abrechnung.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Die Binärdatei wird in `CODEX_BIN`, dann im `PATH` und anschließend im Paket
  `openai-codex-cli-bin` gesucht. `~/.codex/auth.json` wird nie gelesen.
- `OPENAI_API_KEY` und `CODEX_API_KEY` werden aus der Umgebung des
  Subprozesses entfernt: Ein vorhandener Schlüssel führt niemals zu einem Wechsel zur API.
- Jedes Segment kostet mindestens eine „Nachricht“ des 5-Stunden-Fensters — zwei,
  falls dessen Validierung fehlschlägt und es wiederholt wird. OpenAI gibt als
  Schätzung 250–2.000 Nachrichten/5 Std. für `gpt-5.6-luna` (`--eco`) und
  10–100 für `gpt-5.6-sol` bei einem Plus-Tarif an.
- `--model gpt-5.6-terra` und `--model gpt-5.6-luna` laufen ebenfalls über
  das Abonnement. Ein Modell, für das das Konto nicht berechtigt ist, liefert einen 400-Fehler „model is
  not supported when using Codex with a ChatGPT account“.
- Langsamer als eine API, und der Abstand vergrößert sich mit dem Dokument: Bei dieser README betrug der
  Median 6 Min. 46 Sek. pro Sprache mit `gpt-5.6-sol`, gegenüber 36 Sek. für
  `gemini-3.7-flash`.
- In CI abgelehnt (`CI` oder `GITHUB_ACTIONS` definiert): Das Abonnement authentifiziert sich
  über eine persönliche Sitzungsdatei, die auf einem geteilten Runner
  nichts zu suchen hat.
- Variablen: `CODEX_BIN`, `CODEX_TIMEOUT` (Sekunden pro Segment, Standard 600).

### Über das Grok-Abonnement: `--use_grok_cli`

Gleiches Prinzip mit der offiziellen CLI Grok Build, über das SuperGrok- oder
X-Premium+-Abonnement.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Schwächere Isolation als Codex.** Die OS-Sandbox von Grok greift
  auf vielen aktuellen Linux-Systemen nicht (AppArmor, Container-Runtime-Sockets),
  und ein Profil, das nicht angewendet werden kann, startet stillschweigend ungeschützt.
  Das Skript fordert daher standardmäßig kein Profil an, weist darauf hin und
  stützt sich auf die `--deny`-Regeln der CLI, einschließlich des Catch-All `*` — die einzige
  Schicht, die den Start verweigert, anstatt den Schutz wortlos zu entfernen.
  `GROK_TRANSLATE_SANDBOX=read-only` erzwingt die OS-Sandbox, und der Start
  schlägt fehl, wenn die Maschine sie nicht bereitstellen kann.
- Das Kontingent ist wöchentlich, wird mit Chat, Imagine und Voice geteilt, und kein
  Befehl erlaubt dessen Einsicht: Ein Batch-Lauf kann die Nutzung im Chat
  ohne Warnung aufbrauchen.
- Variablen: `GROK_BIN`, `GROK_HOME` (CLI-Verzeichnis, Standard `~/.grok`),
  `GROK_TIMEOUT` (Standard 900), `GROK_TRANSLATE_SANDBOX`.

### Über das Google-Abonnement: `--use_antigravity`

Gleiches Prinzip mit `agy`, der offiziellen CLI von Antigravity: Für Nutzer mit Google
AI Pro oder Ultra wird die Übersetzung vom Kontingent des Abonnements abgebucht, anstatt
nach Tokens abgerechnet zu werden. Dies ist der einzige Weg zu diesem Kontingent: Die Gemini CLI
unterstützt diese Konten seit dem 18. Juni 2026 nicht mehr
([Ankündigung](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
und das SDK von Antigravity akzeptiert nur einen API-Schlüssel oder ein Google-Cloud-Projekt.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Kein kostenpflichtiger Pfad bleibt offen.** agy erhält aus Ihrer
  Umgebung nur eine geschlossene Liste von Variablen — `PATH`, Sprache und Zeitzone,
  Terminal, Identität, Proxys und Zertifikate, Sitzungsbus — und keinen Schlüssel:
  Mehrere seiner Variablen leiten einen Aufruf unbemerkt um (gemessen:
  eine sendet das Dokument an ein Drittanbieter-Gateway, eine andere an ein kostenpflichtiges
  Google-Cloud-Projekt), und eine Denylist vergaß bei jeder Prüfung Einträge.
  Vor jedem Segment muss `agy -p /config`, was kein Kontingent verbraucht,
  zeigen, dass kostenpflichtige KI-Credits deaktiviert sind, ohne API-Schlüssel oder Google-Cloud-Projekt — eine
  fehlende Einstellung gilt als Ablehnung —, andernfalls wird nichts übersetzt; das Protokoll jedes
  Aufrufs muss anschließend das Abonnement bestätigen (`authMethod=consumer`), andernfalls wird die
  Antwort abgelehnt.
- **Isolation.** Jeder Aufruf läuft in einem privaten, temporären
  Home-Verzeichnis mit einem werkzeuglosen Übersetzungsagenten: Ihre Einstellungen, Regeln,
  Plugins, MCP-Server und Hooks von agy gelangen nicht hinein, nichts wird Ihrem
  Verlauf hinzugefügt, und die Verbindung verbleibt im Schlüsselbund, den aipmt niemals ausliest.
  Ein nicht gefundener Agent lässt agy stillschweigend auf seinen Programmier-Agenten
  und dessen Werkzeuge zurückgreifen: Eine vollständige Protokollzeile muss den richtigen Agenten bestätigen — ein
  Dokument, das diese Meldung zitiert, ersetzt sie nicht —, andernfalls erfolgt eine Ablehnung.
- **Plattformen**: Linux, in einer Sitzung mit Schlüsselbund (D-Bus-Sitzungsbus,
  Secret Service); macOS wird akzeptiert, wurde dort jedoch nicht gemessen. Abgelehnt
  unter Windows, wo agy die Variablen zur Isolation der Aufrufe nicht liest, und
  unter Linux ohne Sitzungsbus — SSH-Sitzung, Container, Server: agy speichert
  sein Token dort in einer Datei unter `~/.gemini`, die durch die Isolation verdeckt wird. Die
  Ablehnung erfolgt vor jedem Start mitsamt Begründung, anstatt nach einer Minute
  Wartezeit auf einen Anmeldecode.
- **Modelle**: diejenigen aus `agy models`. Die Gemini-Modelle tragen den Aufwand im Namen
  (`gemini-3.8-flash-medium`…): Ein Name ohne Suffix wird vor dem Aufruf abgelehnt,
  und `--reasoning_effort` bleibt wirkungslos. Standardmäßig `gemini-3.8-flash-medium`,
  und `gemini-3.7-flash-low` bei `--eco`; die Testläufe, mit denen sie festgelegt wurden,
  sind in [Mesures détaillées](#detaillierte-messwerte) beschrieben. Claude und GPT-OSS
  haben ihr eigenes, deutlich kleineres Kontingent: etwa 1 % des 5-Stunden-Fensters
  pro gemessenem Aufruf, gegenüber 0,05 % bei Flash.
- **Kontingent**: pro Gruppe, ein 5-Stunden-Fenster und ein wöchentliches Fenster,
  anteilig an den Token-Kosten. Auf dem Konto des Autors gemessen: etwa
  16 Punkte des 5-Stunden-Fensters pro Million Quellzeichen bei
  `gemini-3.8-flash-medium`, 14 bei `gemini-3.7-flash-medium` und 7 bis 8 bei
  niedrigem Aufwand — eine README mit 40.000 Zeichen kostet somit etwas mehr als einen
  halben Punkt. Das wöchentliche Limit hängt von der Tarifstufe ab. Der Wiederholungsversuch folgt
  den Angaben von agy zur Wiederholbarkeit; andernfalls wird ein erschöpftes Fenster niemals
  erneut versucht: Es lässt jede Datei bis zum Reset fehlschlagen,
  der von `/usage` angezeigt wird.
- **Langsamer als die API**: Beim dichten Messungsartikel betrug der Median
  3 Min. 59 Sek. pro Sprache bei `gemini-3.8-flash-medium` und 3 Min. 14 Sek. bei
  `gemini-3.7-flash-medium`, gegenüber 1 Min. 18 Sek. für Gemini 3.7 Flash über die API.
- **Abbruch**: Strg-C oder ein geschlossenes Terminal beenden agy zusammen mit dem
  Befehl, anstatt den Vorgang auf Kosten Ihres Kontingents zu Ende laufen zu lassen; das
  Gleiche gilt für Codex, Grok CLI und OpenCode. Unter `nohup` läuft die Übersetzung weiter.
- In CI abgelehnt (`CI` oder `GITHUB_ACTIONS` definiert): Die Anmeldung liegt in einem
  persönlichen Schlüsselbund. Auf einem Runner nutzen Sie `--use_gemini` mit `GOOGLE_API_KEY`.
- Variablen: `AGY_BIN` (sonst im `PATH`, danach `~/.local/bin/agy`),
  `AGY_TIMEOUT` (Sekunden pro Segment, einschließlich Start, Standard 900).

**Nutzungsbedingungen: Es wird Ihr eigenes Konto verwendet.** Die
[Antigravity-Bedingungen](https://antigravity.google/terms) (Abschnitt 6) und deren
[FAQ](https://antigravity.google/docs/faq/) untersagen den Zugriff auf den Dienst
über Drittanbieter-Software mittels der Antigravity-Verbindung — Claude Code,
OpenClaw und OpenCode werden dort genannt —, unter Androhung der Kontosperrung. aipmt
liest das Token weder aus noch verwendet es dieses wieder: Es startet die offizielle Binärdatei im
[Headless-Modus](https://antigravity.google/docs/cli/headless/), den Google
für Skripte und CI dokumentiert. Ein Google-Mitarbeiter bezeichnete es als „üblich“,
`agy -p` aus einem lokalen Skript für die eigene Arbeit zu starten
([offizielles Forum, 25. September 2026, unverbindliche Antwort](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
keine offizielle Richtlinie regelt den Fall eines verbreiteten Werkzeugs wie diesem eindeutig.

**Nur für öffentliche Dokumente.** Gemäß Abschnitt 5 derselben Bedingungen können die
Interaktionen — Prompts, Antworten, Metadaten — zur Verbesserung der
Google-Produkte und des maschinellen Lernens verwendet und von Menschen
überprüft werden, auch bei kostenpflichtigen Abonnements. Die Deaktivierung erfolgt über die Einstellung
`enableTelemetry` mit undokumentierter Wirkung, die aipmt nicht setzt; Ihre agy-Einstellungen
werden nicht in dessen Isolation übernommen. Übermitteln Sie darüber keine vertraulichen Inhalte.

### Über das Claude-Abonnement: `--use_claude_code`

Dasselbe Prinzip bei `claude`, dem offiziellen CLI von Claude Code, im Modus `-p`: Für alle, die Claude Pro oder Max bezahlen, wird die Übersetzung auf das Kontingent des Abonnements angerechnet, anstatt nach Tokens abgerechnet zu werden. Nicht zu verwechseln mit `--use_claude`, der API von Anthropic, die nach Nutzung abgerechnet wird.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Kein kostenpflichtiger Kanal bleibt offen, und jeder Aufruf belegt dies.** Claude
  Code erhält aus Ihrer Umgebung nur eine geschlossene Liste von Variablen – weder
  API-Schlüssel noch Token, Cloud-Provider oder Marker der Claude-Code-Sitzung,
  von der aus aipmt gestartet werden könnte. Vor dem ersten Segment muss `claude auth status`
  die Abonnement-Verbindung ohne Console-Schlüssel anzeigen, und `/usage`, das
  kein Kontingent verbraucht, muss dies bestätigen; jeder Aufruf bestätigt dies wiederum
  in seinem Initialisierungsereignis, andernfalls wird die Antwort abgewiesen.
- **Deaktivieren Sie die „Extra Usage“** (claude.ai, Einstellungen → Nutzung), damit
  die Null-Euro-Garantie greift: Wenn sie aktiviert ist, springt sie bei einem erschöpften
  Zeitfenster ein und rechnet kostenpflichtig ab, ohne einen Fehler anzuzeigen. aipmt
  bricht die Übersetzung ab, sobald der Kontingentbericht eines Aufrufs dies meldet,
  aber dieser spezifische Aufruf wurde bereits verbucht.
- **Geteiltes Kontingent mit Ihren Claude-Code-Sitzungen.** Jeder Aufruf meldet
  die Auslastung des 5-Stunden- sowie des Wochenfensters; oberhalb von 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) wird kein weiteres Segment gestartet, um das für
  Ihre Arbeit benötigte Kontingent nicht aufzubrauchen.
- **Isolation.** Jeder Aufruf läuft ohne Tools, in einem privaten und temporären
  Verzeichnis, im Modus ohne Personalisierung: Weder Ihre `CLAUDE.md` noch Ihre
  Plugins, Hooks, MCP-Server oder Einstellungen werden geladen, und nichts aus der
  Sitzung bleibt erhalten. Dateianhänge sind deaktiviert: Ein `@chemin` in Ihrem
  Dokument bleibt einfacher Text und öffnet keine Datei (gemessen).
- **Modelle**: standardmäßig `sonnet`, mit Effort `low`, und auch in
  `--eco`: `--eco` ändert auf diesem Pfad nichts. Auf denselben Dokumenten
  gemessen ist `haiku` doppelt so langsam – es führt Reasoning durch, ohne dass
  man es daran hindern könnte – bei kaum geringeren Kosten, und `opus` verweigert
  Biologie-Inhalte (nächster Punkt). Beide bleiben über `--model` zugänglich; diese
  Aliase folgen dem jeweils neuesten Modell ihrer Familie. `fable` und die Varianten
  `[1m]` werden abgewiesen, da sie über kostenpflichtige Guthaben laufen.
  `--reasoning_effort` steuert den Reasoning-Effort, von dem eine Übersetzung nicht profitiert:
  Das gemessene Reasoning ist gleich null oder fast null.
- **Opus verweigert bestimmte Biologie-Inhalte.** Seine Guardrails sind strenger
  als die von Sonnet, und die Fehlermeldung von Anthropic warnt davor, dass sie
  „can sometimes flag biology-research-adjacent work“. Gemessen: Eine Kurzmeldung
  über 279 generierte Moleküle führte dazu, dass der Artikel in allen vierzehn
  Sprachen verweigert wurde. Es wird nichts geschrieben: aipmt weist die
  abgeschnittene Antwort zurück, benennt die Guardrails und empfiehlt `--model sonnet`.
- Verweigert in CI (`CI` oder `GITHUB_ACTIONS` definiert) und unter Windows (nicht gemessen).
- Variablen: `AIPMT_CLAUDE_BIN` (sonst das `PATH`, dann `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (Sekunden pro Segment, Standardwert 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (Standardwert 0.8), `CLAUDE_CONFIG_DIR` (das Konto von
  Claude Code, niemals aus einer Projekt-`.env` bezogen); Arbeitsverzeichnisse unter
  `XDG_CACHE_HOME/aipmt/claude-code` (Standardwert `~/.cache`).

**Nutzungsbedingungen: Es wird Ihr eigenes Konto genutzt.** Die
[Rechtsseite von Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
verbietet es nicht, dass „an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription“: Genau das tut aipmt, das die offizielle
Binärdatei ausführt und das Token niemals ausliest. Anthropic „does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users“, bevorzugt den API-Schlüssel für
Drittanbieter-Tools, „including open-source projects“, und behält sich vor, deren
Nutzung über kostenpflichtige Guthaben abzurechnen
([Claude-Hilfe](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Kein Text regelt ausdrücklich den Fall eines distribuierten Tools, das die Binärdatei startet.

**Daten**: Bei Free-, Pro- und Max-Konten gilt das Modell-Training auch für Claude Code,
wenn die Datenschutzeinstellung dies erlaubt
([Datenseite](https://code.claude.com/docs/en/data-usage)). aipmt behält
kein lokales Transkript (`--no-session-persistence`). Übertragen Sie hierüber
nichts Vertrauliches.

### Zum Provider nach Wahl: `--use_opencode`

[OpenCode](https://opencode.ai) ist ein quelloffener Code-Agent (MIT), der an
die in ihm konfigurierten Provider weiterleitet: API-Schlüssel, Abonnement,
OpenCode Zen Gateway (kostenlose Modelle, ohne Konto) oder lokales Modell. Hier
wurden zwei Wege durchgängig gemessen: Zen und Ollama.

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

`--model` ist obligatorisch: Ohne diese Angabe würde OpenCode auf ein kostenloses
Modell zurückfallen, dessen Datenverkehr für das Training genutzt werden kann – und diese
Entscheidung wird nicht für Sie getroffen.

Isolation bei jedem Aufruf:

- Eine Inline-Konfiguration mit Vorrang vor Ihrer eigenen definiert einen Agenten `aipmt`,
  dessen Tools ausnahmslos verweigert werden (`permission: { "*": "deny" }`),
  Session-Sharing deaktiviert, `--pure`, niemals `--auto`;
- Leeres temporäres Arbeitsverzeichnis, `OPENCODE_DISABLE_PROJECT_CONFIG` und
  `OPENCODE_DISABLE_CLAUDE_CODE` angelegt – ohne diese injiziert OpenCode die
  `AGENTS.md` des aktuellen Verzeichnisses sowie `~/.claude/CLAUDE.md` in den Prompt. Die
  globale `~/.config/opencode/AGENTS.md` wird weiterhin injiziert; OpenCode erlaubt es nicht,
  sie auszuschließen;
- Ausgabevertrag: Exit-Code 0, kein `error`-Ereignis, kein Tool-Aufruf,
  letzter Schritt als `stop`, nicht-leerer Text und tatsächlich geladener
  `aipmt`-Agent – ein unbekannter `--agent` lässt OpenCode nicht fehlschlagen,
  sondern fällt stillschweigend auf den Coding-Agenten zurück;
- Es wird kein Schlüssel aus `aipmt` übergeben, außer `OPENCODE_API_KEY`, dem Schlüssel
  von OpenCode selbst. Provider werden in OpenCode konfiguriert, nicht in
  der `.env` von `aipmt`.

Wichtig zu wissen:

- Die kostenlosen Modelle von Zen unterliegen ständigen Änderungen mit undokumentierten
  Limits, und ihr Datenverkehr kann für das Training verwendet werden: für eine öffentliche
  Dokumentation geeignet, nicht für private Inhalte.
- Ein lokales Modell muss mindestens 16k Kontext-Tokens bieten, da die Segmente
  bis zu 16.000 Zeichen umfassen. Ollama konfiguriert standardmäßig oft 4.096:
  Nutzen Sie ein `Modelfile` mit `PARAMETER num_ctx 32768`.
- `--eco` bleibt ohne Wirkung; `--reasoning_effort` wird unverändert als
  `--variant` von OpenCode übergeben.
- OpenCode protokolliert jede Sitzung in `~/.local/share/opencode/`.
- Variablen: `OPENCODE_BIN` (sonst das `PATH`, dann `~/.opencode/bin/opencode`),
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

`reasoningEffort: "none"` deaktiviert das Reasoning (Nachdenken), das Ollama bei diesen
Modellen standardmäßig aktiviert und das über ein Modelfile nicht abgeschaltet werden kann.
Gemessen an einem Satz aus sechs Wörtern: 919 Reasoning-Tokens und 68 Sekunden ohne
diese Option, 9 Tokens mit ihr.

### Zu mehr als 400 Modellen: `--use_openrouter`

OpenRouter ist ein nach Nutzung abgerechneter Router mit einheitlichem Guthaben
vor Modellen, die von Drittanbietern gehostet werden – darunter offene
chinesische Modelle, die kein anderer Provider hier anbietet.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` ist obligatorisch. Ein Preflight-Check, der vor jeglicher Abrechnung
ausgeführt wird, regelt zwei Besonderheiten des Routings:

- **Dasselbe Modell wird von Dutzenden Hostern mit unterschiedlichen Obergrenzen
  bereitgestellt** – bei `z-ai/glm-5.3-flash` sind es 23 Hoster, von denen einer auf
  2.048 Ausgabe-Tokens begrenzt ist. Der Preflight liest `/api/v1/models/{modèle}/endpoints`,
  schließt Hoster mit unter 8.000 Ausgabe-Tokens oder herabgestuftem Status aus und
  pinnt die übrigen mit `allow_fallbacks: false` an.
- **Reasoning wird zum Ausgabetarif abgerechnet** – 107 Tokens gegenüber 2 bei
  einer „OK“-Antwort von `z-ai/glm-5.2`. Es ist standardmäßig deaktiviert; Modelle,
  die es erzwingen, erhalten den geringstmöglichen akzeptierten Effort, da der
  Katalog-Standardwert die Ausgabe vor Ende der Übersetzung sättigen könnte.
  `--reasoning_effort` hat weiterhin Vorrang.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Das Kontextfenster stammt aus dem Katalog. Ein Modell unter 16.400 Tokens wird
  vor jedem Aufruf abgelehnt: 8.400 für den Prompt und das Segment, mindestens
  8.000 für die Ausgabe.
- Ein im Katalog fehlender Slug, ein nicht erreichbarer Katalog oder das Fehlen eines
  Hosters, der die Obergrenze erfüllt, brechen den Befehl ab.
- `finish_reason=length` mit leerer Ausgabe bedeutet, dass das Budget durch Reasoning
  aufgebraucht wurde, nicht durch eine Kürzung: Die Meldung unterscheidet dies.
- `--eco` bleibt ohne Wirkung.
- Variablen: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (Standardwert `https://openrouter.ai/api/v1`, `https://`
  erforderlich), `OPENROUTER_TIMEOUT` (Standardwert 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (Standardwert 30).

### Übersetzungshinweis

`--add_translation_note` fügt einen Hinweis hinzu, als `bottom` (Standard), `top` (nach
dem Frontmatter) oder `both` (`--note_position`), im Format `legacy` (fettgedruckter
Absatz, Standard) oder `marker` (`--note_format`). Das Format `marker` ist eine
unsichtbare Markdown-Referenzdefinition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
gefolgt von einem fettgedruckten Zitat: lesbar auf GitHub, beim Build von einem
remark-Plugin nutzbar.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detaillierte Messwerte

Alle Messungen sind real mit `aipmt` durchgeführte Übersetzungen in
vierzehn Sprachen: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Geschrieben** zählt die Dateien, die von den Prüfungen durchgelassen wurden; **Ohne
Abweichung** diejenigen, bei denen `scripts/compare_structure.py` keine Unstimmigkeit meldet –
identische Anzahl von Abschnitten, Untertiteln, Links, eindeutigen URLs, Codeblöcken,
Inline-Code, Tabellenzeilen, Zitatblöcken und fettgedruckten Wörtern.

„Ohne Abweichung“ bedeutet „nichts erkannt“, nicht „identisch“: Der Vergleicher
zählt Elemente, ohne deren Inhalt zu lesen. Er meldet weder eine gelöschte
Überschrift der Ebene 4 noch den geänderten Text eines Inline-Codes, vertauschte
Flaggen oder einen internen Link, der mit einer schließenden Klammer zu viel
(`[texte]((#ancre))`) gerendert wurde und ins Leere führt – und er beurteilt nicht
die sprachliche Qualität.

### Dichter Monitoring-Artikel, Modus `--news`

Eine Ausgabe des [KI-Monitors von jls42.org](https://jls42.org/fr/news):
589 Zeilen, 140 Links, 21 Abschnitte, 3 geschützte englische Zitate. Testlauf
vom 4. und 5. September 2026.

| Modell                                          | Zugang             | Geschrieben | Ohne Abweichung | Median/Sprache |
| ----------------------------------------------- | ------------------ | ----------- | --------------- | -------------- |
| `gemini-3.7-flash`                              | Google-API         | 14/14       | ✅ **14/14**    | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google-Abonnement  | 14/14       | ✅ **14/14**    | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google-Abonnement  | 14/14       | ✅ **14/14**    | 3 min 14 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT-Abonnement | 14/14       | ✅ **14/14**    | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14       | ✅ **14/14**    | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14       | ✅ **14/14**    | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | Claude-Abonnement  | 14/14       | ⚠️ 13/14        | 6 min 49 s     |
| `claude-sonnet-5`                               | Anthropic-API      | 14/14       | ⚠️ 11/14        | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | Claude-Abonnement  | 14/14       | ⚠️ 11/14        | 15 min 54 s    |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14       | ❌ 11/14        | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14       | ❌ 8/14         | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | lokal              | 10/14       | ❌ 7/14         | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral-API        | 11/14       | ❌ 5/14         | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14        | ❌ 3/14         | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok-Abonnement    | 1/14        | ❌ 1/14         | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | Claude-Abonnement  | 0/14        | ❌ 0/14         | —              |

Grok wurde am 9. September bei einer anderen Ausgabe desselben Monitors
(356 Zeilen) erneut gemessen: 9 von 14 Sprachen geschrieben, 8 ohne Abweichung.
Dieser Wert ist in der Übersichtstabelle aufgeführt. Drei abgebrochene Testläufe
sind nicht aufgeführt: `qwen3.5-27b` (9 Sprachen) und `kimi-k2.6` (4)
mangels Guthaben, `z-ai/glm-5.3-flash`, dessen zwei Fehlschläge auf eine
Reasoning-Einstellung zurückzuführen waren, die der Provider seither korrigiert hat.
Die OpenRouter-Zeilen wurden mit den Standardeinstellungen des Routers vor
`--use_openrouter` gemessen; `z-ai/glm-5.2`, nachgemessen mit dem ausgelieferten
Provider, liefert dasselbe Ergebnis von 14/14. Die Zahlen wurden am 10. September
mit dem aktuellen Vergleicher neu berechnet: `qwen3.8-flash` und
`qwen3.7-flash` gewinnen im Vergleich zur Erstveröffentlichung jeweils eine
Sprache hinzu, die übrigen bleiben unverändert.

Die Zeilen für `--use_antigravity` wurden am 26. September anhand desselben
Artikels mit vier parallelen Übersetzungen gemessen: `gemini-3.7-flash-medium` am Vormittag,
`gemini-3.8-flash-medium` am Nachmittag. Im Englischen entfernte jedes Modell
die drei Zeilen der französischen Übersetzung unter den Zitaten selbstständig,
ohne Flaggen zu erfinden, und die englischen Zitate blieben intakt: Die
Fallback-Bereinigung musste nicht eingreifen. Bei `--eco` (`gemini-3.7-flash-low`)
für lediglich vier Sprachen (en, ja, ar, hi): 4 von 4 geschrieben, alle ohne Abweichung,
Median 1 min 52 s. Gegenprobe am selben Tag bei einer neueren Ausgabe des Monitors
vom 25. September (438 Zeilen, 2 englische Zitate), außerhalb des Blogs mit
`gemini-3.7-flash-medium` übersetzt: 14 von 14 geschrieben, alle ohne Abweichung, 87 bis
128 s pro Sprache.

Die Zeilen für `--use_claude_code` wurden am 26. September anhand desselben
Artikels mit vier parallelen Übersetzungen beim Effort `low` gemessen. Bei `sonnet`
sind die englischen Zitate in allen vierzehn Sprachen intakt geblieben, und im
Englischen hat das Modell die Zeilen der französischen Übersetzung selbstständig
entfernt, ohne Flaggen zu erfinden. `opus` hat keine einzige Sprache
geschrieben: In jeder einzelnen Sprache stoppten seine Guardrails die Antwort beim
letzten Segment aufgrund einer Kurzmeldung über 279 für eine Bindungsstelle generierte
Moleküle. Separat eingereicht wird diese Kurzmeldung unter der Kategorie „Bio“
verweigert; `sonnet` übersetzte sie überall. `haiku` schreibt
alle vierzehn Sprachen; in drei davon (en, pl, ro) rutscht eine Abschnittsüberschrift
von Ebene 2 auf Ebene 1. Es führt Reasoning durch, ohne dass man es daran
hindern könnte – 61 % seiner Ausgabe-Tokens –, woraus mehr als die doppelte
Laufzeit gegenüber `sonnet` resultiert.

### README dieses Projekts, Standard-Markdown

Eingefrorene Revision vom 9. September 2026: 785 Zeilen, 285 Inline-Codes, 40
Blockabschlüsse, 89 Tabellenzeilen. Vier Übersetzungen parallel.

| Modell                                          | Geschrieben | Ohne Abweichung | Median/Sprache | Was abweicht                                                             |
| ----------------------------------------------- | ----------- | --------------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14       | ✅ 14/14        | 1 Min. 43 Sek. | nichts                                                                   |
| `opus` (`--use_claude_code`)                    | 14/14       | ✅ 14/14        | 1 Min. 48 Sek. | nichts                                                                   |
| `haiku` (`--use_claude_code`)                   | 14/14       | ✅ 14/14        | 4 Min. 02 Sek. | nichts für das Vergleichstool; interne Links verdoppelt (en)             |
| `gemini-3.7-flash`                              | 14/14       | ⚠️ 13/14        | 36 Sek.        | ein Wort in Fettschrift (ja)                                             |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14       | ⚠️ 13/14        | 1 Min. 22 Sek. | ein Wort in Fettschrift (ko)                                             |
| `sonnet` (`--use_claude_code`)                  | 14/14       | ⚠️ 13/14        | 2 Min. 20 Sek. | eine Tabellenzeile an die vorherige angehängt (ar)                       |
| `claude-sonnet-5`                               | 14/14       | ⚠️ 12/14        | 2 Min. 56 Sek. | ein Link (sv), ein Wort in Fettschrift (zh)                              |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14       | ⚠️ 12/14        | 6 Min. 46 Sek. | ein Wort in Fettschrift (ar, ja)                                         |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14       | ⚠️ 11/14        | 2 Min. 34 Sek. | ein Wort in Fettschrift (hi, ja, ko)                                     |
| `qwen/qwen3.7-flash`                            | 14/14       | ⚠️ 10/14        | 2 Min. 17 Sek. | 40 Inline-Codes auf Arabisch hinzugefügt; Fettschrift (hi, ja, ko)        |
| `mistral-large-latest`                          | 14/14       | ❌ 1/14         | 2 Min. 44 Sek. | ein Abschnitt verloren (ar, hi, ko); Codeblöcke hinzugefügt (ja, ko, ro, zh) |

Zwei abgebrochene Testläufe sind nicht aufgeführt: Grok, CLI-Sitzung nach
zwölf Sprachen abgelaufen (elf ohne Abweichung), und `qwen3.8-flash`, HTTP 429
von seinem Hoster nach zwei. `opencode/mimo-v2.5-free` und `ollama/gpt-oss-20b-32k`
wurden bei dieser Revision nicht erneut gemessen; bei der vom 4. und 5. September,
die um 277 Zeilen kürzer war, erstellten sie jeweils 9 von 14 Übersetzungen, davon 7
und 1 ohne Abweichung.

Die Zeilen `--use_antigravity` und `--use_claude_code` wurden nicht anhand der
eingefrorenen Revision gemessen, sondern am 26. September anhand der mit 1.14.0
veröffentlichten Fassung: 600 Zeilen, 257 Inline-Codes, 30 Blockabschlüsse,
85 Tabellenzeilen. Da sie um 185 Zeilen kürzer ist, lässt sie sich nicht direkt mit
den anderen Zeilen vergleichen; diese Zeilen wiederum lassen sich untereinander
vergleichen. Bei den internen Links, die das Vergleichstool nicht prüft, hat
`gemini-3.8-flash-medium` sie in allen vierzehn Sprachen intakt gelassen, `gemini-3.7-flash-medium` hat
sie auf Italienisch beschädigt; `sonnet` und `opus` haben sie
überall intakt gehalten, `haiku` hat sie auf Englisch verdoppelt.

### Vier READMEs bekannter Projekte

FastAPI, Ollama, tldr-pages und Vue.js, unverändert von GitHub übernommen –
einfachere Dokumente als die beiden vorherigen. Die Testreihe zielte auf Modelle
mit Schwierigkeiten ab; Gemini dient hierbei als Vergleichsmaßstab.

| Modell                    | Umfang                     | Geschrieben | Ohne Abweichung |
| ------------------------- | -------------------------- | ----------- | --------------- |
| `gemini-3.7-flash`        | 4 Projekte × 14 Sprachen   | 56/56       | ✅ **55/56**    |
| `opencode/mimo-v2.5-free` | 4 Projekte × 14 Sprachen   | 55/56       | ❌ 47/56        |
| `grok-4.6` (Abonnement)   | 4 Projekte × ar, hi, ja, zh| 16/16       | ❌ 14/16        |
| `ollama/gpt-oss-20b-32k`  | 4 Projekte × ar, hi, ja, zh| 15/16       | ❌ 9/16         |

### Was diese Messungen nicht sind

- **Kein vollständiges Ranking**: Allein OpenRouter bietet über vierhundert
  Modelle an, gemessen wurden etwa fünfzehn.
- **Richtwerte für die Dauer**: drei bis sechs parallele Übersetzungen je nach
  Testlauf, und der Durchsatz eines Anbieters schwankt im Tagesverlauf.
- **Zeitpunktbezogene Beobachtungen**: Modelle ändern sich unter demselben
  Namen, und Ihre Dokumente sind nicht die unseren.

Um die Messung für Ihre eigenen Dokumente anhand einer eingefrorenen Kopie der Datei zu wiederholen:

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
über das ChatGPT-Abonnement, vier parallel. `REGEN_PROVIDER` und `REGEN_MODEL`
ändern den Pfad: `antigravity` bleibt bei einem Abonnement, dem von Google,
und läuft ohne Ausnahmeregelung durch; eine kostenpflichtige API (`openai`, `gemini`,
`grok`, `openrouter`) wird ohne `REGEN_ALLOW_PAID_API=1` abgewiesen;
`REGEN_JOB_TIMEOUT` deckelt jeden Job (600 s, 1.800 s bei Codex und
Antigravity). Details zu den Werkzeugen finden sich in `CLAUDE.md`.

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** — persönlicher Blog, der in 15 Sprachen veröffentlicht
  wird. Seine [tägliche KI-Beobachtung](https://jls42.org/fr/news) wird jeden Tag
  von diesem Tool übersetzt und dient als Referenzdokument für die obigen Messungen.

## Autor

Julien LE SAUX
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Haftungsausschluss

Dieses Programm wird **ohne jede Gewährleistung** im Sinne der Abschnitte 15
und 16 der GPL v3 vertrieben: bereitgestellt „wie besehen“, ohne ausdrückliche
oder stillschweigende Gewährleistung der Marktgängigkeit oder der Eignung für
einen bestimmten Zweck, und sein Autor kann nicht für Schäden haftbar gemacht
werden, die aus seiner Nutzung entstehen. Der Wortlaut der Lizenz hat Vorrang
vor dieser Zusammenfassung.

- **Vor der Veröffentlichung Korrektur lesen.** Die Schutzmechanismen decken
  Codeblöcke, Inline-Code, URLs, Anker und Zitate des Modus `--news` ab –
  jedoch weder Überschriften, Tabellen noch Frontmatter oder den Sinn Ihrer Sätze.
- **Ihre Dokumente werden an den ausgewählten Anbieter übermittelt**, gemäß dessen
  Nutzungsbedingungen und Datenschutzrichtlinien. Einige kostenlose Modelle können
  Ihre Interaktionen für das Training wiederverwenden, und die Bedingungen von Antigravity
  erlauben es Google, sie wiederzuverwenden und von Menschen überprüfen zu lassen,
  auch bei einem kostenpflichtigen Abonnement; ein lokales Modell ist der einzige
  Weg, bei dem keinerlei Daten Ihren Rechner verlassen.
- **API-Aufrufe werden Ihnen in Rechnung gestellt.** Dieses Programm begrenzt
  die Ausgaben nicht: Ein langes Dokument, eine Wiederholung nach einem Fehlschlag
  oder ein Modell mit intensiven Denkprozessen verursachen höhere Kosten.
- **Die veröffentlichten Messungen sind zeitpunktbezogene Beobachtungen**, keine
  Garantien.

Die genannten Produkt- und Unternehmensnamen sind Eigentum der jeweiligen
Inhaber. Dieses Projekt ist mit keinem von ihnen verbunden.

**Artikel übersetzt aus dem Französischen ins Deutsche mit gemini-3.8-flash-medium.**

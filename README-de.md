# AI-Powered Markdown-Übersetzer

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

- **Elf Provider-Wege**: APIs von OpenAI, Mistral, Claude, Gemini und Grok;
  ChatGPT- (Codex), Grok-, Google- (Antigravity) und Claude-Abonnements (Claude
  Code) ohne nutzungsbasierte Abrechnung; Router OpenCode (Open Source, kostenlos oder lokal) und OpenRouter
  (über 400 Modelle).
- **Keine Fehler durch verlorene Tokens**: Codeblöcke, Inline-Code,
  URLs, Anker und Zitate werden vor dem Aufruf durch Tokens ersetzt und
  bei der Rückgabe überprüft. Fehlt auch nur eines, wird die Datei nicht geschrieben.
- **Lange Dokumente**: Segmentierung basierend auf dem Modell-Kontextfenster.
- **`--news`-Modus**: geschützte englische Zitate und sprachspezifisch verwaltete
  Flaggen für Monitoring- und Recherche-Artikel.
- **`--eco`-Modus**: schnelle und kostengünstigere Modelle.
- Optionale **Übersetzungsnotiz**, oben, unten oder an beiden Stellen.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11 oder neuer. Für die Installation aus dem Repository siehe
[Mitwirken](#mitwirken).

## Konfiguration

Schlüssel werden an drei Orten gelesen, von der höchsten zur niedrigsten Priorität; jeder
füllt nur das aus, was der vorherige leer lässt.

|     | Wo                                            | Wofür                                 |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Umgebungsvariablen                            | CI, Container, punktuelle Ausnahme    |
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
unter Windows. Ohne Schlüssel listet der Befehl die drei Speicherorte auf.

**Die `.env` eines Projekts kann weder Aufrufe umleiten noch das ausgeführte
Programm bestimmen.** Sie liefert Schlüssel, niemals ein Ziel oder eine Binärdatei: Jede
Variable in `_BASE_URL`, `_API_BASE`, `_ENDPOINT` oder `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, Proxys (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), Zertifikatsspeicher (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) und `XDG_CONFIG_HOME` /
`APPDATA` wird dort ignoriert, mit einer Warnung. Ein geklontes Repository darf weder
Ihren Schlüssel abfangen noch Sie dazu bringen, bei der
ersten Übersetzung ein eigenes Programm auszuführen. Diese Datei wird zudem ohne Interpolation gelesen:
`NOM=${OPENAI_API_KEY}` kopiert den Schlüssel dort nicht. Setzen Sie diese Variablen in
der Umgebung oder in `~/.config/aipmt/.env`.

Optionale Variablen: `XAI_BASE_URL` (Standard `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (Sekunden pro Aufruf, Standard 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(Standard 600), `GROK_BIN`, `GROK_HOME` (Standard `~/.grok`), `GROK_TIMEOUT`
(Standard 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (Standard 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (Standard 600), `OPENROUTER_BASE_URL`
(`https://` erforderlich), `OPENROUTER_TIMEOUT` (Standard 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (Standard 30). Jede einzelne wird im
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
mit `--include_model` wird es zu `document-es-gpt-6.1-terra.md`. Die Dateiendung wird
immer zu `.md` – `article.mdx` ergibt `article-en.md` – außer mit
`--keep_filename`, wodurch der ursprüngliche Name beibehalten wird. Eine bereits vorhandene Übersetzung
wird ohne `--force` übersprungen.

Exit-Codes: `0`, wenn alles erfolgreich war oder übersprungen wurde, `1`, wenn mindestens eine Datei
fehlgeschlagen ist (Liste auf der Standardfehlerausgabe), `2`, wenn die Konfiguration die Ursache ist.
Eine fehlgeschlagene Datei wird niemals geschrieben, selbst wenn das Schreiben selbst fehlschlägt:
Der Inhalt wird daneben geschrieben und anschließend umbenannt. Ein erneuter Durchlauf genügt.

## Welches Modell wählen

Gemessen an zwei realen Dokumenten, die von jedem Modell in dieselben vierzehn Sprachen
übersetzt wurden. **Die Zahl gibt an, in wie vielen von vierzehn Sprachen die
Übersetzung geschrieben wird und keinerlei Abweichungen von der Quelle aufweist.**

| Modell                | Zugriffsmethode                   | Dichter Monitoring-Artikel | Diese README | Was abweicht und in wie vielen Sprachen                                                                                                                            |
| --------------------- | --------------------------------- | -------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google-Abonnement (Antigravity)   | ✅ 14/14                   | ✅ 14/14     | nichts, bei keinem der beiden Dokumente                                                                                                                            |
| **Claude Sonnet 5.5** | Anthropic-API-Schlüssel           | ✅ 14/14                   | ✅ 14/14     | nichts, bei keinem der beiden Dokumente                                                                                                                            |
| **Gemini 3.7 Flash**  | Google-API-Schlüssel              | ✅ 14/14                   | ⚠️ 13/14     | 1 von 14 Sprachen: ein fettgedrucktes Wort mehr (ja)                                                                                                               |
| **Gemini 3.7 Flash**  | Google-Abonnement (Antigravity)   | ✅ 14/14                   | ⚠️ 13/14     | 1 von 14 Sprachen: ein fettgedrucktes Wort weniger (ko)                                                                                                            |
| **GPT-5.6 Sol**       | ChatGPT-Abonnement oder OpenAI-Schlüssel | ✅ 14/14            | ⚠️ 12/14     | 2 von 14 Sprachen: ein fettgedrucktes Wort weniger (ar, ja)                                                                                                        |
| **GLM-5.2**           | OpenRouter-Schlüssel              | ✅ 14/14                   | ⚠️ 11/14     | 3 von 14 Sprachen: ein fettgedrucktes Wort weniger (hi, ja, ko)                                                                                                     |
| Claude Sonnet 5       | Claude-Abonnement (Claude Code)   | ⚠️ 13/14                   | ⚠️ 13/14     | 1 von 14 Sprachen beim Artikel: ein fettgedrucktes Wort mehr (zh); 1 bei dieser README: eine Tabellenzeile mit der vorherigen verschmolzen, in der Anzeige verborgen (ar) |
| Claude Haiku 4.5      | Claude-Abonnement (Claude Code)   | ⚠️ 11/14                   | ✅ 14/14     | 3 von 14 Sprachen beim Artikel: eine Abschnittsüberschrift auf Ebene 1 heraufgestuft (en, pl, ro); bei dieser README nichts für das Vergleichstool, aber interne Links auf Englisch dupliziert |
| Claude Sonnet 5       | Anthropic-API-Schlüssel           | ⚠️ 11/14                   | ⚠️ 12/14     | 3 von 14 Sprachen beim Artikel: ein zusätzlicher Codeblock aufgetaucht (es, de, hi); 2 bei dieser README: ein Link ohne Markup (sv), ein fettgedrucktes Wort (zh) |
| Claude Haiku 4.5      | Anthropic-API-Schlüssel           | ⚠️ 7/14                    | ✅ 14/14     | 7 von 14 Sprachen beim Artikel: eine Abschnittsüberschrift auf Ebene 1 heraufgestuft – auf Japanisch auf Französisch geblieben; nichts bei dieser README          |
| Claude Haiku 5.5      | Anthropic-API-Schlüssel           | ⚠️ 11/14                   | ❌ 12/14     | 3 von 14 Sprachen beim Artikel: eine Abschnittsüberschrift in der Ebene geändert oder verdoppelt (ja, ko, zh); bei dieser README 2 Sprachen abgelehnt, Inline-Code verloren gegangen (ar, hi) |
| Qwen 3.7 Flash        | OpenRouter-Schlüssel              | ❌ 8/14                    | ⚠️ 10/14     | 1 Sprache beim Artikel abgelehnt, 5 weitere weichen ab; bei dieser README rund vierzig Wörter in `code` gesetzt (ar)                                       |
| Grok 4.6              | Grok-Abonnement                   | ❌ 8/14                    | nicht bewertet | 5 von 14 Sprachen abgelehnt, da Inline-Code und URLs nicht zurückgegeben wurden; Niederländisch weicht in allem ab                                                  |
| GPT-OSS 20B           | lokales Modell (Ollama)           | ❌ 7/14                    | nicht erneut gemessen | 4 von 14 Sprachen abgelehnt: Das Modell ließ dort Passagen auf Französisch stehen, der Schutzmechanismus stoppte sie                                       |
| MiMo v2.5 (kostenlos) | OpenCode Zen, ohne Konto          | ❌ 11/14                   | nicht erneut gemessen | 1 Sprache abgelehnt; ein Abschnitt auf Polnisch verloren                                                                                                           |
| Mistral Large         | Mistral-API-Schlüssel             | ❌ 5/14                    | ❌ 1/14      | **ein ganzer Abschnitt verschwindet**: 1 Sprache beim Artikel (hi), 3 bei dieser README (ar, hi, ko) – und 3 Sprachen beim Artikel abgelehnt                         |
| DeepSeek V4 Flash     | OpenRouter-Schlüssel              | ❌ 3/14                    | nicht erneut gemessen | 10 von 14 Sprachen abgelehnt; 37 Minuten pro Sprache                                                                                                              |
| Claude Opus 5.5       | Claude-Abonnement (Claude Code)   | ❌ 0/14                    | ✅ 14/14     | der Artikel in allen 14 Sprachen durch die Guardrails von Opus abgelehnt, wegen einer Biologie-Kurzmeldung; nichts bei dieser README                                |

|     | Bedeutung des Symbols                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alle vierzehn Sprachen übersetzt und keinerlei Abweichungen von der Quelle                                                                                                                           |
| ⚠️  | alle vierzehn Sprachen übersetzt; was abweicht, ist **Markup** – ein fettgedrucktes Wort, ein `code`, ein Link ohne eckige Klammern. Kein Text, keine URL, kein Codeblock und kein Abschnitt fehlt |
| ❌  | mindestens eine Sprache konnte nicht übersetzt werden – die Datei wird abgelehnt, nicht geschrieben – **oder** in einer geschriebenen Datei fehlt Inhalt                                            |

Was man beachten sollte:

- **Eine abgelehnte Übersetzung ist keine beschädigte Übersetzung.** Wenn bei
  der Rückgabe ein Token fehlt, wird die Datei nicht geschrieben und die Sprache zählt
  als abgelehnt. Genau das passiert Grok beim Artikel: Vier Inline-Codes und
  drei URLs gingen bereits im ersten Segment bei den fünf nicht-lateinischen Schriftsystemen verloren.
- **Ein Modell kann ein ganzes Dokument wegen eines einzigen Satzes ablehnen.** Opus 5.5
  übersetzt diese README ohne jede Abweichung, aber keinen einzigen Monitoring-Artikel: Seine
  Guardrails stoppen die Antwort bei einer Biologie-Kurzmeldung. Die Datei wird
  nicht geschrieben, und aipmt gibt den Grund an.
- **Dieses Sicherheitsnetz deckt weder Überschriften, Tabellen, Frontmatter noch
  Fließtext ab.** Ein Modell, das einen Abschnitt löscht, liefert eine Datei zurück, die das Tool
  anstandslos schreibt – wie es bei Mistral der Fall ist. Diese Elemente können nicht
  durch Tokens ersetzt werden, und die aktuellen Schutzmechanismen prüfen sie nicht;
  `scripts/compare_structure.py` erkennt einen verlorenen Abschnitt erst im Nachhinein.
- **Grok hat für diese README keine Bewertung**: Seine CLI-Sitzung ist nach zwölf
  Sprachen abgelaufen, davon elf ohne Abweichung. Ein abgebrochener Durchlauf wird nicht bewertet.
- **Die Dichte des Dokuments zählt mehr als die Sprache.** Grok bewältigt
  gewöhnliche READMEs, scheitert jedoch an einem stark verlinkten Artikel, selbst auf
  Niederländisch.

Daten und Dokumente: Die Spalte „Diese README“ wurde am 9. September 2026
anhand einer eingefrorenen Revision dieser Datei gemessen (785 Zeilen, 285 Inline-Codes, 89 Tabellenzeilen),
die seither überarbeitet wurde – mit Ausnahme der Zeilen zu Antigravity und Claude Code,
die am 26. September anhand der mit 1.14.0 veröffentlichten, kürzeren Revision gemessen wurden
(600 Zeilen, 257 Inline-Codes, 85 Tabellenzeilen), sowie der Zeilen zu Claude
Sonnet 5.5, Haiku 5.5 und Haiku 4.5 über die API, gemessen am 18. Oktober anhand der
selben Revision. Die Spalte „Dichter Monitoring-Artikel“ stammt aus dem Testlauf vom
4. und 5. September mit einem 589 Zeilen langen Artikel, mit Ausnahme der Grok-Zeile, die am
9. September anhand einer anderen Ausgabe desselben Monitorings erneut gemessen wurde, der Zeilen zu Antigravity und
Claude Code, die am 26. September anhand desselben Artikels gemessen wurden, und jener drei Claude-Zeilen
vom 18. Oktober. Die vollständigen Tabellen, Laufzeiten und das Protokoll finden sich
unter [Detaillierte Messungen](#detaillierte-messungen).

## Alle Optionen

| Option                   | Beschreibung                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Einzelne zu übersetzende Markdown-Datei (Alternative zu `--source_dir`)                                       |
| `--source_dir`           | Quellverzeichnis mit den Markdown-Dateien (Standard: `content/posts`)                                         |
| `--target_dir`           | Ausgabeverzeichnis für die übersetzten Dateien (Standard: `traductions_en`)                                    |
| `--source_lang`          | Quellsprache (Standard: `fr`)                                                                                  |
| `--target_lang`          | Zielsprache (Standard: `en`)                                                                                   |
| `--model`                | Zu verwendendes spezifisches Modell                                                                           |
| `--eco`                  | Sparsame Modelle verwenden                                                                                    |
| `--use_mistral`          | Mistral AI-API verwenden                                                                                      |
| `--use_claude`           | Claude-API verwenden                                                                                          |
| `--use_gemini`           | Gemini-API verwenden                                                                                          |
| `--use_grok`             | xAI-API (Grok) verwenden — erfordert `XAI_API_KEY`                                                           |
| `--use_codex`            | Codex-CLI über das Kontingent des ChatGPT-Abonnements verwenden                                               |
| `--use_grok_cli`         | Grok-CLI über das Kontingent des Grok-Abonnements verwenden                                                   |
| `--use_antigravity`      | Antigravity-CLI (`agy`) über das Kontingent des Google AI Pro- oder Ultra-Abonnements verwenden                       |
| `--use_claude_code`      | Claude Code-CLI (`claude -p`) über das Kontingent des Claude Pro- oder Max-Abonnements verwenden                      |
| `--use_opencode`         | OpenCode (Open Source) mit dem in OpenCode konfigurierten Provider verwenden; erfordert `--model provider/modèle` |
| `--use_openrouter`       | OpenRouter verwenden — erfordert `OPENROUTER_API_KEY` und `--model fournisseur/modèle`                          |
| `--force`                | Erneutes Übersetzen erzwingen                                                                                 |
| `--keep_filename`        | Ursprünglichen Dateinamen beibehalten                                                                          |
| `--news`                 | Nachrichtenmodus: schützt EN-Zitate, verwaltet Sprachflaggen                                      |
| `--add_translation_note` | Übersetzungshinweis hinzufügen                                                                                |
| `--note_position`        | Position des Hinweises: `top`, `bottom` (Standard) oder `both`                                                     |
| `--note_format`          | Format des Hinweises: `legacy` (Standard, fetter Absatz) oder `marker`                                            |
| `--include_model`        | Modellnamen in die Ausgabedatei aufnehmen                                                            |
| `--reasoning_effort`     | Reasoning-Aufwand GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

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

`--eco` wechselt auf die Sparstufe jedes Anbieters.

| Provider    | Qualität (Standard)                                                  | Sparsam (`--eco`) |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-6.1-terra`                                                      | `gpt-6-luna`              |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-4-hydrogen`                                                  | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (auch `gpt-5.6-sol`, `terra` und `luna` über `--model`) | `gpt-6-luna`              |
| Grok API    | `grok-4.7`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | ebenso — `--eco` wirkungslos |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.8-flash-low`    |
| Claude Code | `sonnet`, effort `low`                                               | ebenso — `--eco` wirkungslos |
| OpenCode    | `--model provider/modèle` erforderlich                                | ebenso — `--eco` wirkungslos |
| OpenRouter  | `--model fournisseur/modèle` erforderlich                             | ebenso — `--eco` wirkungslos |

Die Standards folgen der neuesten Generation jedes Anbieters, die vor
ihrer Übernahme gemessen wurde: GPT-6 bei OpenAI, Gemini 4 Hydrogen bei Google,
Grok 4.7 bei xAI seit 1.19.0. Ältere Modelle werden weiterhin über
`--model` akzeptiert (`gpt-5.6-terra`, `gemini-3.8-flash`, `grok-4.6`…), ebenso wie
Gemini 4 Argon und Carbon, das High-End von Google. aipmt regelt den
Reasoning-Aufwand für GPT und Grok selbst, abgeschaltet in `--eco`, und
`--reasoning_effort` erzwingt ihn; ein Gemini erhält immer die niedrigste
Stufe, die es akzeptiert.
Ein vorübergehender Ausfall der Gemini-API (503, 429, Zeitüberschreitung) startet
den Aufruf bis zu dreimal neu, nach 10, 20 und dann 40 Sekunden. Ein Versuch
ohne Antwort wird nach 5 Minuten abgebrochen und dann ebenso wiederholt:
Ein stummer Server lässt das Segment in höchstens etwa zwanzig Minuten
fehlschlagen, anstatt unbegrenzt zu blockieren.

### Über das ChatGPT-Abonnement: `--use_codex`

Steuert die offizielle Codex-CLI: Die Übersetzung wird vom Kontingent des
ChatGPT-Abonnements abgezogen, ohne API-Schlüssel oder nutzungsbasierte Abrechnung.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Die Binärdatei wird in `CODEX_BIN`, dann im `PATH`, dann im Paket
  `openai-codex-cli-bin` gesucht. `~/.codex/auth.json` wird niemals gelesen.
- `OPENAI_API_KEY` und `CODEX_API_KEY` werden aus der Umgebung des
  Unterprozesses entfernt: Ein vorhandener Schlüssel führt niemals zu einem Wechsel zur API.
- Jedes Segment kostet mindestens eine „Nachricht“ des 5-Stunden-Fensters – zwei,
  wenn die Validierung fehlschlägt und es wiederholt wird. OpenAI gibt als
  Schätzung 250–2.000 Nachrichten/5 Std. für `gpt-5.6-luna` an, das Sparmodell bis
  1.18.0, und 10–100 für `gpt-5.6-sol` bei einem Plus-Plan.
- `--model gpt-5.6-sol`, der Standard bis 1.16.3, `--model gpt-5.6-terra`
  und `--model gpt-5.6-luna` laufen ebenfalls über das Abonnement.
- Ein 429-Fehler des Servers führt nicht zum Verlust der Datei: Codex verbindet sich selbstständig neu,
  aipmt wartet auf das Ende der Runde, und wenn der 429 das letzte Wort hat, startet das Segment
  nach 30 und dann 60 Sekunden erneut. Ein Modell, für das der Account nicht berechtigt ist, liefert einen 400-Fehler „model is
  not supported when using Codex with a ChatGPT account“.
- Langsamer als eine API, und der Unterschied wächst mit dem Dokument: bei dieser README
  im Median 6 Min. 46 Sek. pro Sprache mit `gpt-5.6-sol`, gegenüber 36 Sek. für
  `gemini-3.7-flash`.
- In CI abgelehnt (`CI` oder `GITHUB_ACTIONS` definiert): Das Abonnement authentifiziert sich
  über eine persönliche Sitzungsdatei, die auf einem geteilten Runner
  nichts zu suchen hat.
- Variablen: `CODEX_BIN`, `CODEX_TIMEOUT` (Sekunden pro Segment, Standard 600).

### Über das Grok-Abonnement: `--use_grok_cli`

Dasselbe Prinzip mit der offiziellen Grok Build-CLI über das SuperGrok- oder
X Premium+-Abonnement.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Schwächere Isolation als Codex.** Die OS-Sandbox von Grok greift auf
  vielen neueren Linux-Rechnern nicht (AppArmor, Container-Runtime-Sockets),
  und ein Profil, das nicht angewendet werden kann, startet stillschweigend ohne Isolation.
  Das Skript fordert daher standardmäßig kein Profil an, weist darauf hin und
  stützt sich auf die `--deny`-Regeln der CLI, einschließlich des Catch-All `*` — die einzige
  Ebene, die den Start verweigert, anstatt den Schutz stillschweigend
  aufzuheben. `GROK_TRANSLATE_SANDBOX=read-only` erzwingt die OS-Sandbox, und der Start
  schlägt fehl, wenn das System dies nicht gewährleisten kann.
- Das Kontingent ist wöchentlich, wird mit Chat, Imagine und Voice geteilt, und keine
  Befehl erlaubt es auszulesen: Ein Batch kann das Kontingent für Konversationen
  ohne Vorwarnung aufbrauchen.
- Variablen: `GROK_BIN`, `GROK_HOME` (Verzeichnis der CLI, Standard `~/.grok`),
  `GROK_TIMEOUT` (Standard 900), `GROK_TRANSLATE_SANDBOX`.

### Über das Google-Abonnement: `--use_antigravity`

Dasselbe Prinzip mit `agy`, der offiziellen CLI von Antigravity: Wer Google
AI Pro oder Ultra bezahlt, dessen Übersetzung wird vom Kontingent des Abonnements abgezogen,
anstatt pro Token abgerechnet zu werden. Dies ist der einzige Weg zu diesem Kontingent: Die Gemini-CLI
bedient diese Konten seit dem 18. Juni 2026 nicht mehr
([Ankündigung](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
und das SDK von Antigravity akzeptiert nur einen API-Schlüssel oder ein Google Cloud-Projekt.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Kein kostenpflichtiger Pfad bleibt offen.** agy erhält aus Ihrer
  Umgebung nur eine geschlossene Liste von Variablen — `PATH`, Sprache und Zeitzone,
  Terminal, Identität, Proxies und Zertifikate, Sitzungsbus — und keinen Schlüssel:
  Mehrere seiner Variablen schalten einen Aufruf um, ohne etwas anzuzeigen (gemessen:
  eine sendet das Dokument an ein Drittanbieter-Gateway, eine andere an ein abgerechnetes
  Google Cloud-Projekt), und eine Sperrliste übersah bei jeder Überprüfung welche.
  Vor jedem Segment muss `agy -p /config`, das kein Kontingent kostet, zeigen,
  dass kostenpflichtige KI-Guthaben deaktiviert sind, ohne API-Schlüssel oder Google Cloud-Projekt — eine
  fehlende Einstellung gilt als Ablehnung —, andernfalls wird nichts übersetzt; das Protokoll jedes
  Aufrufs muss anschließend das Abonnement bestätigen (`authMethod=consumer`), andernfalls wird die
  Antwort abgelehnt.
- **Isolation.** Jeder Aufruf läuft in einem privaten, temporären
  Home-Verzeichnis mit einem tool-losen Übersetzungsagenten: Ihre agy-Einstellungen, -Regeln,
  -Plugins, -MCP-Server und -Hooks gelangen nicht hinein, nichts wird Ihrem
  Verlauf hinzugefügt, und die Anmeldung verbleibt im Schlüsselbund, den aipmt niemals ausliest.
  Ein nicht gefundener Agent lässt agy stillschweigend auf seinen Coding-Agenten
  und dessen Tools zurückgreifen: Eine vollständige Protokollzeile muss den richtigen Agenten bestätigen — ein
  Dokument, das diese Meldung zitiert, ersetzt sie nicht —, andernfalls erfolgt eine Ablehnung.
- **Plattformen**: Linux, in einer Sitzung mit Schlüsselbund (D-Bus-Sitzungsbus,
  Secret Service); macOS wird akzeptiert, wurde dort aber nicht gemessen. Abgelehnt
  unter Windows, wo agy die Variablen zur Isolierung einzelner Aufrufe nicht liest, und
  unter Linux ohne Sitzungsbus — SSH-Sitzung, Container, Server: agy speichert
  sein Token dort in einer Datei in `~/.gemini`, die durch die Isolation verdeckt wird. Die
  Ablehnung erfolgt vor jedem Start samt Angabe des Grundes, anstatt eine Minute
  auf einen Login-Code zu warten.
- **Modelle**: die von `agy models`. Die Gemini-Modelle tragen den Aufwand im Namen
  (`gemini-3.8-flash-medium`…): Ein Name ohne Suffix wird vor dem Aufruf abgelehnt,
  und `--reasoning_effort` bleibt wirkungslos. Standardmäßig `gemini-3.8-flash-medium`,
  und `gemini-3.8-flash-low` in `--eco`, seitdem agy Gemini 3.7
  Flash nicht mehr bedient; die Kampagne, die den Standard festgelegt hat, ist
  in [Detaillierte Messungen](#detaillierte-messungen) beschrieben. Gemini 4 Hydrogen
  (`gemini-4-hydrogen-low`…) teilt sich das Kontingent mit 3.8 Flash und verbraucht
  mehr davon: 0,95 Punkte des 5-Stunden-Fensters für diese README bei mittlerem
  Aufwand, gegenüber 0,32. Claude und GPT-OSS
  haben ihr eigenes, viel kleineres Kontingent: etwa 1 % des 5-Stunden-Fensters
  pro gemessenem Aufruf, gegenüber 0,05 % bei Flash. Gemini 4 Argon hat ein
  eigenes, wöchentliches Kontingent: Diese README beansprucht 1,35 % davon.
- **Kontingent**: pro Gruppe ein 5-Stunden- und ein wöchentliches Fenster, anteilig
  nach Tokenkosten. Gemessen auf dem Konto des Autors: etwa
  16 Punkte des 5-Stunden-Fensters pro Million Quellzeichen bei
  `gemini-3.8-flash-medium`, 14 bei `gemini-3.7-flash-medium` und 7 bis 8 bei
  geringem Aufwand — eine README mit 40.000 Zeichen kostet also etwas mehr als einen
  halben Punkt. Das wöchentliche Limit hängt wiederum von der Stufe ab. Die Wiederholung folgt
  dem, was agy als wiederholbar einstuft; andernfalls wird ein erschöpftes Fenster niemals
  erneut versucht: Es lässt jede Datei bis zum von `/usage` angezeigten Reset fehlschlagen.
- **Langsamer als die API**: beim dichten Messungs-Artikel im Median 3 Min. 59 Sek. pro
  Sprache bei `gemini-3.8-flash-medium` und 3 Min. 14 Sek. bei
  `gemini-3.7-flash-medium`, gegenüber 1 Min. 18 Sek. für Gemini 3.7 Flash über die API.
- **Unterbrechung**: Strg+C oder ein geschlossenes Terminal stoppen agy zusammen mit
  dem Befehl, anstatt es seine Runde auf Kosten Ihres Kontingents beenden zu lassen; dasselbe
  gilt für Codex, die Grok-CLI und OpenCode. Unter `nohup` läuft die Übersetzung weiter.
- In CI abgelehnt (`CI` oder `GITHUB_ACTIONS` definiert): Die Anmeldung befindet sich in einem
  persönlichen Schlüsselbund. Auf einem Runner: `--use_gemini` mit `GOOGLE_API_KEY`.
- Variablen: `AGY_BIN` (sonst der `PATH`, dann `~/.local/bin/agy`),
  `AGY_TIMEOUT` (Sekunden pro Segment, einschließlich Start, Standard 900).

**Nutzungsbedingungen: Es ist Ihr Konto betroffen.** Die
[Antigravity-Bedingungen](https://antigravity.google/terms) (Abschnitt 6) und deren
[FAQ](https://antigravity.google/docs/faq/) untersagen den Zugriff auf den Dienst
über Software von Drittanbietern unter Verwendung der Antigravity-Anmeldung — Claude Code,
OpenClaw und OpenCode werden dort genannt —, unter Androhung der Kontosperrung. aipmt
liest das Token weder aus noch verwendet es dieses wieder: Es startet die offizielle Binärdatei im
[Headless-Modus](https://antigravity.google/docs/cli/headless/), den Google
für Skripte und CI dokumentiert. Ein Mitarbeiter von Google bezeichnete es als „üblich“,
`agy -p` aus einem lokalen Skript für die eigene Arbeit zu starten
([offizielles Forum, 25. September 2026, unverbindliche Antwort](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
kein Text regelt den Fall eines verteilten Tools wie diesem eindeutig.

**Nur öffentliche Dokumente.** Gemäß Abschnitt 5 derselben Bedingungen können die
Interaktionen — Prompts, Antworten, Metadaten — zur Verbesserung der
Produkte und des maschinellen Lernens von Google verwendet und von
Menschen überprüft werden, auch bei einem kostenpflichtigen Abonnement. Das Opt-out erfolgt über die Einstellung
`enableTelemetry` mit undokumentierter Wirkung, die aipmt nicht setzt; Ihre agy-Einstellungen
werden in die Isolation nicht übernommen. Verarbeiten Sie darüber nichts Vertrauliches.

### Über das Claude-Abonnement: `--use_claude_code`

Dasselbe Prinzip gilt für `claude`, die offizielle CLI von Claude Code, im Modus `-p`: Für
Abonnenten von Claude Pro oder Max wird die Übersetzung auf das Kontingent des
Abonnements angerechnet, anstatt pro Token abgerechnet zu werden. Nicht zu verwechseln mit
`--use_claude`, der API von Anthropic, die nach Nutzung abgerechnet wird.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Kein kostenpflichtiger Pfad bleibt offen, und jeder Aufruf belegt dies.** Claude
  Code erhält aus Ihrer Umgebung nur eine geschlossene Liste von Variablen – weder
  API-Schlüssel noch Token, Cloud-Provider oder Marker der Claude-Code-Sitzung,
  aus der aipmt gestartet worden sein könnte. Vor dem ersten Segment muss `claude auth status`
  die Abonnementverbindung ohne Console-Schlüssel anzeigen, und `/usage`, was
  kein Kontingent verbraucht, muss dies bestätigen; jeder Aufruf bestätigt dies seinerseits
  in seinem Initialisierungs-Event, andernfalls wird die Antwort abgewiesen.
- **Deaktivieren Sie „Extra usage“** (claude.ai, Einstellungen → Nutzung), damit
  die Null-Euro-Garantie greift: Wenn aktiviert, springt dies bei einem erschöpften Zeitfenster
  ein und rechnet ab, ohne einen Fehler anzuzeigen. aipmt stoppt die Übersetzung, sobald
  der Kontingentbericht eines Aufrufs dies signalisiert, aber jener Aufruf wird bereits angerechnet.
- **Geteiltes Kontingent mit Ihren Claude-Code-Sitzungen.** Jeder Aufruf meldet
  die Nutzung des 5-Stunden- sowie des Wochenfensters; ab 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) wird kein weiteres Segment gestartet, um das Kontingent
  für Ihre Arbeit nicht zu erschöpfen.
- **Isolation.** Jeder Aufruf läuft ohne Tools, in einem privaten und
  temporären Verzeichnis im Modus ohne Anpassungen: Weder Ihre `CLAUDE.md` noch Ihre Plugins,
  Hooks, MCP-Server oder Einstellungen werden geladen, und aus der Sitzung wird nichts
  aufbewahrt. Anhänge sind deaktiviert: Ein `@chemin` in Ihrem Dokument
  bleibt Text und öffnet keine Dateien (gemessen).
- **Modelle**: Standardmäßig `sonnet`, bei Effort-Stufe `low`, und auch in `--eco`:
  `--eco` ändert auf diesem Pfad nichts. Anhand denselben Dokumenten gemessen, ist `haiku`
  doppelt so langsam – es schlussfolgert, ohne dass man es daran hindern könnte – bei
  kaum niedrigeren Kosten, und `opus` verweigert biologiebezogene Inhalte (nächster
  Punkt). Beide bleiben über `--model` zugänglich; diese Aliase folgen dem
  neuesten Modell ihrer Familie. `fable` und die Varianten `[1m]` werden abgelehnt,
  da sie über kostenpflichtige Guthaben abgerechnet werden. `--reasoning_effort` regelt den Effort,
  woraus eine Übersetzung keinen Nutzen zieht: Das gemessene Reasoning ist gleich null oder fast null.
- **Opus verweigert bestimmte biologiebezogene Inhalte.** Seine Guardrails sind
  strenger als die von Sonnet, und die Fehlermeldung von Anthropic warnt, dass sie
  „can sometimes flag biology-research-adjacent work“. Gemessen: Eine Kurzmeldung
  über 279 generierte Moleküle führte zur Verweigerung des Artikels in allen vierzehn
  Sprachen. Es wird nichts geschrieben: aipmt lehnt die unvollständige Antwort ab, benennt die
  Guardrails und empfiehlt `--model sonnet`.
- In CI abgelehnt (`CI` oder `GITHUB_ACTIONS` gesetzt) und unter Windows (nicht gemessen).
- Variablen: `AIPMT_CLAUDE_BIN` (sonst das `PATH`, dann `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (Sekunden pro Segment, Standard 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (Standard 0.8), `CLAUDE_CONFIG_DIR` (das Konto von
  Claude Code, niemals aus einer `.env` eines Projekts bezogen); Arbeitsverzeichnisse unter
  `XDG_CACHE_HOME/aipmt/claude-code` (Standard `~/.cache`).

**Nutzungsbedingungen: Ihr eigenes Konto ist gebunden.** Die
[Rechtshinweis-Seite von Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
verbietet einem Endbenutzer nicht, „an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription“: Genau das tut aipmt, indem es die offizielle
Binärdatei startet und das Token niemals liest. Anthropic gestattet es Drittentwicklern jedoch nicht
(„does not permit third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users“), bevorzugt den API-Schlüssel für Drittanbieter-Tools,
„including open-source projects“, und behält sich das Recht vor, deren Nutzung
über kostenpflichtige Guthaben abzurechnen
([Claude-Hilfe](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Kein Text regelt den Fall eines distribuierten Tools, das die Binärdatei ausführt.

**Daten**: Bei Free-, Pro- und Max-Konten gilt das Modelltraining
auch für Claude Code, wenn die Datenschutzeinstellung dies erlaubt
([Datenseite](https://code.claude.com/docs/en/data-usage)). aipmt speichert
keine lokalen Transkripte (`--no-session-persistence`). Lassen Sie darüber
nichts Vertrauliches laufen.

### Zum Anbieter eigener Wahl: `--use_opencode`

[OpenCode](https://opencode.ai) ist ein Open-Source-Code-Agent (MIT), der
Anfragen an die intern konfigurierten Anbieter weiterleitet: API-Schlüssel, Abonnement,
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

`--model` ist obligatorisch: Ohne diese Angabe würde OpenCode auf ein kostenloses Modell zurückgreifen,
dessen Dialoge für das Training verwendet werden können, und diese Entscheidung wird Ihnen
nicht abgenommen.

Isolation bei jedem Aufruf:

- Eine Inline-Konfiguration, die Vorrang vor Ihrer eigenen hat, definiert einen Agenten `aipmt`,
  dessen Tools alle verweigert werden (`permission: { "*": "deny" }`), Session-Sharing
  deaktiviert, `--pure`, niemals `--auto`;
- temporäres und leeres Arbeitsverzeichnis, `OPENCODE_DISABLE_PROJECT_CONFIG` und
  `OPENCODE_DISABLE_CLAUDE_CODE` angelegt – ohne diese injiziert OpenCode die
  `AGENTS.md` des aktuellen Verzeichnisses sowie `~/.claude/CLAUDE.md` in den Prompt. Die
  globale `~/.config/opencode/AGENTS.md` wird weiterhin injiziert, OpenCode erlaubt es nicht,
  sie zu übergehen;
- Ausgabe-Vertrag: Exit-Code 0, kein `error`-Event, kein Tool-Aufruf,
  letzter Schritt in `stop`, nicht-leerer Text und der Agent `aipmt`
  tatsächlich geladen – ein unbekanntes `--agent` führt bei OpenCode nicht zum Abbruch, es
  fällt stillschweigend auf den Coding-Agenten zurück;
- Es wird kein `aipmt`-Schlüssel übermittelt, außer `OPENCODE_API_KEY`, dem Schlüssel
  von OpenCode selbst. Die Provider werden in OpenCode konfiguriert, nicht in
  der `.env` von `aipmt`.

Wissenswertes:

- Die kostenlosen Modelle von Zen sind veränderlich, haben undokumentierte Limits, und
  ihre Dialoge können für das Training verwendet werden: für öffentliche Dokumentation
  geeignet, nicht für vertrauliche Inhalte.
- Ein lokales Modell muss mindestens 16k Kontext-Token bieten, da Segmente
  bis zu 16.000 Zeichen lang sein können. Ollama ist oft auf 4.096 konfiguriert: Verwenden
  Sie ein `Modelfile` mit `PARAMETER num_ctx 32768`.
- `--eco` hat keine Wirkung; `--reasoning_effort` wird unverändert als
  `--variant` von OpenCode übergeben.
- OpenCode protokolliert jede Sitzung in `~/.local/share/opencode/`.
- Variablen: `OPENCODE_BIN` (sonst das `PATH`, dann `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (Sekunden pro Segment, Standard 600). `OPENCODE_CONFIG`
  wird unverändert an OpenCode übergeben.

Beispiel für ein lokales Modell via Ollama in `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` schaltet das Reasoning aus, das Ollama bei diesen
Modellen standardmäßig aktiviert und das ein Modelfile nicht deaktivieren kann. Gemessen an einem Satz mit
sechs Wörtern: 919 Reasoning-Token und 68 Sekunden ohne die Option, 9 Token mit ihr.

### Zu mehr als 400 Modellen: `--use_openrouter`

OpenRouter ist ein nach Nutzung abgerechneter Router mit einheitlichem Guthaben vor
von Dritten gehosteten Modellen – einschließlich offener chinesischer Modelle, die hier
kein anderer Provider anbietet.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` ist obligatorisch. Ein Preflight, der vor jeder Abrechnung ausgeführt wird, regelt
zwei Besonderheiten des Routings:

- **Dasselbe Modell wird von Dutzenden Hostern mit unterschiedlichen Limits bereitgestellt**
  – bei `z-ai/glm-5.3-flash` sind es 23 Hoster, von denen einer auf
  2.048 Ausgabe-Token begrenzt ist. Der Preflight liest `/api/v1/models/{modèle}/endpoints`,
  schließt Hoster unter 8.000 Ausgabe-Token oder mit beeinträchtigtem Status aus und
  pinnt die übrigen mit `allow_fallbacks: false` fest.
- **Reasoning wird zum Ausgabetarif abgerechnet** – 107 Token gegenüber 2 bei
  einer „OK“-Antwort von `z-ai/glm-5.2`. Es ist standardmäßig deaktiviert; Modelle,
  die es erzwingen, erhalten die niedrigste Effort-Stufe, die sie akzeptieren, da der Standardwert
  des Katalogs die Ausgabe vor dem Ende der Übersetzung sättigen könnte.
  `--reasoning_effort` behält Vorrang.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Das Kontextfenster stammt aus dem Katalog. Ein Modell unter 16.400 Token wird
  vor jedem Aufruf abgewiesen: 8.400 für Prompt und Segment, mindestens 8.000
  für die Ausgabe.
- Ein Slug, der nicht im Katalog vorhanden ist, ein nicht erreichbarer Katalog oder das Fehlen
  eines Hosters, der das Limit einhält, stoppen den Befehl.
- `finish_reason=length` mit einer leeren Ausgabe bedeutet ein durch
  Reasoning aufgebrauchtes Budget, kein Abschneiden: Die Meldung unterscheidet dies.
- `--eco` hat keine Wirkung.
- Variablen: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (Standard `https://openrouter.ai/api/v1`, `https://`
  erforderlich), `OPENROUTER_TIMEOUT` (Standard 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (Standard 30).

### Übersetzungshinweis

`--add_translation_note` fügt einen Hinweis hinzu, als `bottom` (Standard), `top` (nach dem
Front Matter) oder `both` (`--note_position`), im Format `legacy` (fetter Absatz,
Standard) oder `marker` (`--note_format`). Das Format `marker` ist eine
unsichtbare Markdown-Referenzdefinition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
gefolgt von einem fettgedruckten Zitat: auf GitHub lesbar, beim Build durch ein
remark-Plugin verwertbar.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detaillierte Messungen

Alle Messungen sind tatsächlich mit `aipmt` ausgeführte Übersetzungen in
vierzehn Sprachen: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Geschrieben** zählt die Dateien, die die Guardrails passiert haben; **Ohne Abweichung**
jene, bei denen `scripts/compare_structure.py` nichts beanstandet – gleiche Anzahl an
Abschnitten, Untertiteln, Links, unterschiedlichen URLs, Codeblöcken,
Inline-Codes, Tabellenzeilen, Blockzitaten und fettgedruckten Wörtern.

„Ohne Abweichung“ bedeutet „nichts erkannt“, nicht „identisch“: Der Vergleicher
zählt Elemente, ohne deren Inhalt zu lesen. Er meldet weder eine gelöschte
Überschrift der Ebene 4 noch den ersetzten Text eines Inline-Codes, eine vertauschte
Flagge oder einen internen Link, der mit einer Klammer zu viel ausgegeben wurde,
`[texte]((#ancre))`, der ins Leere führt – und er beurteilt nicht die
Sprache.

### Dichter Marktbeobachtungsartikel, Modus `--news`

Eine Ausgabe der [KI-Marktbeobachtung von jls42.org](https://jls42.org/fr/news):
589 Zeilen, 140 Links, 21 Abschnitte, 3 geschützte englische Zitate. Testlauf
vom 4. und 5. September 2026.

| Modell                                          | Zugang             | Geschrieben | Ohne Abweichung | Median/Sprache |
| ----------------------------------------------- | ------------------ | ----------- | --------------- | -------------- |
| `gemini-3.7-flash`                              | Google-API         | 14/14       | ✅ **14/14**    | 1 Min. 18 Sek. |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google-Abonnement  | 14/14       | ✅ **14/14**    | 3 Min. 59 Sek. |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google-Abonnement  | 14/14       | ✅ **14/14**    | 3 Min. 14 Sek. |
| `claude-sonnet-5-5`                             | Anthropic-API      | 14/14       | ✅ **14/14**    | 3 Min. 37 Sek. |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT-Abonnement | 14/14       | ✅ **14/14**    | 11 Min. 28 Sek.|
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14       | ✅ **14/14**    | 5 Min. 37 Sek. |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14       | ✅ **14/14**    | 26 Min. 23 Sek.|
| `sonnet` (`--use_claude_code`)                  | Claude-Abonnement  | 14/14       | ⚠️ 13/14        | 6 Min. 49 Sek. |
| `claude-sonnet-5`                               | Anthropic-API      | 14/14       | ⚠️ 11/14        | 6 Min. 31 Sek. |
| `haiku` (`--use_claude_code`)                   | Claude-Abonnement  | 14/14       | ⚠️ 11/14        | 15 Min. 54 Sek.|
| `claude-haiku-5-5`                              | Anthropic-API      | 14/14       | ⚠️ 11/14        | 2 Min. 54 Sek. |
| `claude-haiku-4-5`                              | Anthropic-API      | 14/14       | ⚠️ 7/14         | 6 Min. 00 Sek. |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14       | ❌ 11/14        | 9 Min. 27 Sek. |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14       | ❌ 8/14         | 10 Min. 09 Sek.|
| `ollama/gpt-oss-20b-32k`                        | lokal              | 10/14       | ❌ 7/14         | 12 Min. 39 Sek.|
| `mistral-large-latest`                          | Mistral-API        | 11/14       | ❌ 5/14         | 5 Min. 32 Sek. |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14        | ❌ 3/14         | 37 Min. 27 Sek.|
| `grok-4.6` (`--use_grok_cli`)                   | Grok-Abonnement    | 1/14        | ❌ 1/14         | 23 Min. 11 Sek.|
| `opus` (`--use_claude_code`)                    | Claude-Abonnement  | 0/14        | ❌ 0/14         | —              |

Grok wurde am 9. September an einer anderen Ausgabe derselben Marktbeobachtung
(356 Zeilen) erneut gemessen: 9 geschriebene Sprachen von 14, 8 ohne Abweichung. Dieser
Wert steht in der Kopf-Tabelle. Drei abgebrochene Kampagnen sind nicht
aufgeführt: `qwen3.5-27b` (9 Sprachen) und `kimi-k2.6` (4) aus Mangel an Guthaben,
`z-ai/glm-5.3-flash`, dessen zwei Fehlschläge auf eine Reasoning-Einstellung zurückzuführen waren,
die der Provider inzwischen korrigiert hat. Die OpenRouter-Zeilen wurden mit den
Standardeinstellungen des Routers vor `--use_openrouter` gemessen; `z-ai/glm-5.2`,
erneut mit dem mitgelieferten Provider gemessen, liefert dasselbe Ergebnis von 14/14. Die Zahlen wurden
am 10. September mit dem aktuellen Vergleicher neu berechnet: `qwen3.8-flash` und
`qwen3.7-flash` gewinnen jeweils eine Sprache im Vergleich zur ersten
Veröffentlichung, die übrigen bleiben unverändert.

Die Zeilen `--use_antigravity` wurden am 26. September an demselben
Artikel mit vier parallelen Übersetzungen gemessen: `gemini-3.7-flash-medium` am Vormittag,
`gemini-3.8-flash-medium` am Nachmittag. Im Englischen entfernte jedes Modell die drei
Zeilen französischer Übersetzung unter den Zitaten selbstständig, ohne Flaggen zu erfinden,
und die englischen Zitate blieben intakt: Die Fallback-Bereinigung musste
nichts korrigieren. Bei `--eco` (`gemini-3.7-flash-low`), bei nur vier Sprachen
(en, ja, ar, hi): 4 von 4 geschrieben, alle ohne Abweichung, 1 Min. 52 Sek.
Median. Gegenprobe am selben Tag an einer neueren Ausgabe der Marktbeobachtung,
jener vom 25. September (438 Zeilen, 2 englische Zitate), außerhalb des
Blogs übersetzt durch `gemini-3.7-flash-medium`: 14 von 14 geschrieben, alle ohne Abweichung, 87 bis
128 Sek. pro Sprache.

Die Zeilen `--use_claude_code` wurden am 26. September an demselben
Artikel mit vier parallelen Übersetzungen bei Effort-Stufe `low` gemessen. Bei `sonnet` sind die
englischen Zitate in allen vierzehn Sprachen intakt, und im Englischen entfernte das
Modell die französischen Übersetzungszeilen selbstständig, ohne Flaggen zu erfinden.
`opus` schrieb keine einzige Sprache: In jeder stoppten die Guardrails
die Antwort beim letzten Segment wegen einer Kurzmeldung über 279 Moleküle,
die für eine Bindungsstelle generiert wurden. Einzeln gesendet, wird diese Kurzmeldung unter
der Kategorie „Bio“ verweigert; `sonnet` übersetzte sie überall. `haiku` schreibt
alle vierzehn Sprachen; in dreien (en, pl, ro) wechselt eine Abschnittsüberschrift von
Ebene 2 zu Ebene 1. Es schlussfolgert, ohne dass man es daran hindern könnte – 61 %
seiner Ausgabe-Token –, was zu mehr als der doppelten Zeit von `sonnet` führt.

Die Zeilen `claude-sonnet-5-5`, `claude-haiku-5-5` und `claude-haiku-4-5` wurden
am 18. Oktober über die Anthropic-API am selben Artikel mit vier
parallelen Übersetzungen pro Modell gemessen. Sonnet 5.5 verweigert die Deaktivierung
seines Reasoning: aipmt übergibt die niedrigste Stufe, die es akzeptiert, und seine
Antworten weisen keines auf. Es schreibt alle vierzehn Sprachen ohne Abweichung und ohne
ein Segment wiederholen zu müssen; im Englischen entfernte es die französischen
Übersetzungszeilen selbstständig, ohne Flaggen zu erfinden, und die englischen Zitate blieben
überall intakt. Haiku 5.5 wurde mit adaptivem Reasoning gemessen: Bei deaktiviertem
Reasoning blieben ganze Absätze auf Französisch stehen, was die Guardrails ablehnen –
3 von 14 Sprachen geschrieben. Beide Haiku scheitern an derselben Kurzmeldung: Haiku 5.5
ändert die Ebene ihrer Überschrift oder verdoppelt sie auf Japanisch, Koreanisch und
Chinesisch; Haiku 4.5 stuft sie in sieben Sprachen auf Ebene 1 hoch und belässt sie auf
Japanisch auf Französisch. Haiku 4.5 kostet 3,67 $ für die beiden Dokumente in allen
vierzehn Sprachen, Haiku 5.5 0,57 $, Sonnet 5.5 9,21 $.

### README dieses Projekts, Standard-Markdown

Eingefrorene Revision vom 9. September 2026: 785 Zeilen, 285 Inline-Codes, 40
Block-Abschlüsse, 89 Tabellenzeilen. Vier Übersetzungen parallel.

| Modell                                          | Geschrieben | Ohne Abweichung | Median/Sprache | Was abweicht                                                             |
| ----------------------------------------------- | ----------- | --------------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14       | ✅ 14/14        | 1 Min. 43 s    | nichts                                                                   |
| `opus` (`--use_claude_code`)                    | 14/14       | ✅ 14/14        | 1 Min. 48 s    | nichts                                                                   |
| `haiku` (`--use_claude_code`)                   | 14/14       | ✅ 14/14        | 4 Min. 02 s    | nichts für den Vergleicher; interne Links verdoppelt (en)                |
| `claude-sonnet-5-5`                             | 14/14       | ✅ 14/14        | 1 Min. 18 s    | nichts                                                                   |
| `claude-haiku-4-5`                              | 14/14       | ✅ 14/14        | 2 Min. 06 s    | nichts                                                                   |
| `gemini-3.7-flash`                              | 14/14       | ⚠️ 13/14        | 36 s           | ein Wort fett (ja)                                                       |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14       | ⚠️ 13/14        | 1 Min. 22 s    | ein Wort fett (ko)                                                       |
| `sonnet` (`--use_claude_code`)                  | 14/14       | ⚠️ 13/14        | 2 Min. 20 s    | eine Tabellenzeile an die vorherige angehängt (ar)                       |
| `claude-sonnet-5`                               | 14/14       | ⚠️ 12/14        | 2 Min. 56 s    | ein Link (sv), ein Wort fett (zh)                                       |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14       | ⚠️ 12/14        | 6 Min. 46 s    | ein Wort fett (ar, ja)                                                   |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14       | ⚠️ 11/14        | 2 Min. 34 s    | ein Wort fett (hi, ja, ko)                                               |
| `qwen/qwen3.7-flash`                            | 14/14       | ⚠️ 10/14        | 2 Min. 17 s    | 40 Inline-Codes auf Arabisch hinzugefügt; fett (hi, ja, ko)              |
| `claude-haiku-5-5`                              | 12/14       | ❌ 12/14        | 1 Min. 14 s    | 2 Sprachen abgelehnt (ar, hi): Inline-Codes bei der Rückgabe verloren     |
| `mistral-large-latest`                          | 14/14       | ❌ 1/14         | 2 Min. 44 s    | ein Abschnitt verloren (ar, hi, ko); Codeblöcke hinzugefügt (ja, ko, ro, zh) |

Zwei abgebrochene Durchläufe werden nicht bewertet: Grok, CLI-Sitzung abgelaufen
nach zwölf Sprachen (elf ohne Abweichung), und `qwen3.8-flash`, HTTP 429 seines
Hosters nach zwei. `opencode/mimo-v2.5-free` und `ollama/gpt-oss-20b-32k`
wurden bei dieser Revision nicht erneut gemessen; bei jener vom 4. und 5. September,
die um 277 Zeilen kürzer war, schrieben sie jeweils 9 von 14 Übersetzungen, davon 7
und 1 ohne Abweichung.

Die Zeilen `--use_antigravity` und `--use_claude_code` wurden nicht auf
der eingefrorenen Revision gemessen, sondern am 26. September auf der mit 1.14.0 veröffentlichten — und
die Zeilen `claude-sonnet-5-5`, `claude-haiku-5-5` und `claude-haiku-4-5` am 18.
Oktober auf derselben: 600 Zeilen, 257 Inline-Codes, 30 Block-Abschlüsse, 85
Tabellenzeilen. Da sie um
185 Zeilen kürzer ist, lässt sie sich nicht direkt mit den anderen Zeilen vergleichen;
diese Zeilen untereinander lassen sich jedoch vergleichen. Bei den internen Links, die der
Vergleicher nicht prüft, behielt `gemini-3.8-flash-medium` sie in
allen vierzehn Sprachen intakt, `gemini-3.7-flash-medium` beschädigte sie auf Italienisch;
`sonnet` und `opus` behielten sie überall intakt, `haiku` verdoppelte sie auf
Englisch; `claude-sonnet-5-5` und `claude-haiku-4-5` behielten sie in
allen vierzehn Sprachen intakt, `claude-haiku-5-5` in den zwölf, die es geschrieben hat.

### Vier READMEs bekannter Projekte

FastAPI, Ollama, tldr-pages und Vue.js, unverändert von GitHub übernommen —
einfachere Dokumente als die beiden vorherigen. Der Durchlauf zielte auf die Modelle
mit Schwierigkeiten ab; Gemini dient hierbei als Vergleichsbasis.

| Modell                    | Umfang                     | Geschrieben | Ohne Abweichung |
| ------------------------- | -------------------------- | ----------- | --------------- |
| `gemini-3.7-flash`        | 4 Projekte × 14 Sprachen   | 56/56       | ✅ **55/56**    |
| `opencode/mimo-v2.5-free` | 4 Projekte × 14 Sprachen   | 55/56       | ❌ 47/56        |
| `grok-4.6` (Abonnement)   | 4 Projekte × ar, hi, ja, zh | 16/16       | ❌ 14/16        |
| `ollama/gpt-oss-20b-32k`  | 4 Projekte × ar, hi, ja, zh | 15/16       | ❌ 9/16         |

### Was diese Messungen nicht sind

- **Kein erschöpfendes Ranking**: OpenRouter allein bietet über vierhundert
  Modelle an, etwa fünfzehn wurden gemessen.
- **Richtwerte für die Dauer**: je nach Durchlauf drei bis sechs Übersetzungen
  parallel, und der Durchsatz eines Anbieters schwankt im Tagesverlauf.
- **Zeitgebundene Momentaufnahmen**: Modelle ändern sich unter demselben Namen,
  und Ihre Dokumente sind nicht die unseren.

Um die Messung mit Ihren Dokumenten auf einer eingefrorenen Kopie der Datei zu wiederholen:

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

Beide Zeilen sind erforderlich: Ohne `pip install -e .` antwortet
`python -m aipmt` mit `No module named aipmt`.

Qualitätswerkzeuge, optional, aber empfohlen:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Die 28 Übersetzungen des Repositorys (README und CHANGELOG, vierzehn Sprachen) lassen
sich mit `./regen_translations.sh --force` neu generieren — standardmäßig Codex und `gpt-6.1-sol` über
das ChatGPT-Abonnement, vier parallel. `REGEN_PROVIDER` und
`REGEN_MODEL` ändern den Pfad: `antigravity` bleibt bei einem Abonnement, dem
von Google, und läuft ohne Ausnahmegenehmigung durch; eine kostenpflichtige API (`openai`, `gemini`,
`grok`, `openrouter`) wird ohne `REGEN_ALLOW_PAID_API=1` abgelehnt;
`REGEN_JOB_TIMEOUT` begrenzt jeden Job (600 s, 1.800 s bei Codex und
Antigravity). Details zu den Werkzeugen finden sich in `CLAUDE.md`.

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** — persönlicher Blog, veröffentlicht in 15 Sprachen. Seine
  [tägliche KI-Beobachtung](https://jls42.org/fr/news) wird täglich
  mit diesem Werkzeug übersetzt und dient als Referenzdokument für die obigen Messungen.

## Autor

Julien LE SAUX
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Warnhinweis

Dieses Programm wird **ohne jede Gewährleistung** gemäß den Bedingungen der
Abschnitte 15 und 16 der GPL v3 vertrieben: bereitgestellt „wie besehen“, ohne ausdrückliche
oder stillschweigende Gewährleistung der Marktgängigkeit oder der Eignung für einen bestimmten
Zweck, und sein Autor kann nicht für Schäden haftbar gemacht werden, die aus seiner Nutzung entstehen.
Der Wortlaut der Lizenz hat Vorrang vor dieser Zusammenfassung.

- **Vor der Veröffentlichung Korrektur lesen.** Die Schutzmechanismen decken Codeblöcke,
  Inline-Code, URLs, Anker und Zitate des Modus `--news` ab — weder
  Überschriften noch Tabellen, Frontmatter oder den Sinn Ihrer Sätze.
- **Ihre Dokumente werden an den gewählten Anbieter gesendet**, gemäß dessen
  Nutzungsbedingungen und Datenschutzrichtlinien. Einige kostenlose Modelle können
  Ihre Interaktionen für das Training wiederverwenden, und die Bedingungen von Antigravity
  erlauben es Google, sie wiederzuverwenden und von Menschen überprüfen zu lassen,
  auch bei kostenpflichtigen Abonnements; ein lokales Modell ist der einzige Weg, bei dem
  keine Daten Ihren Rechner verlassen.
- **API-Aufrufe werden Ihnen in Rechnung gestellt.** Dieses Programm begrenzt die
  Ausgaben nicht: Ein langes Dokument, eine Wiederholung nach einem Fehler oder ein Modell, das
  viel nachdenkt (Reasoning), kosten mehr.
- **Die veröffentlichten Messungen sind zeitgebundene Momentaufnahmen**, keine Garantien.

Die genannten Produkt- und Firmennamen gehören ihren jeweiligen
Inhabern. Dieses Projekt ist mit keinem von ihnen verbunden.

**Artikel übersetzt von fr nach de mit gemini-3.8-flash-medium.**

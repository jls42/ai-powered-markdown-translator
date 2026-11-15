# KI-gestützter Markdown-Übersetzer

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

Übersetzt Markdown-Dateien von einer Sprache in eine andere unter Beibehaltung der
Struktur: Codeblöcke, Inline-Code, URLs, Anker, Tabellen und Front
Matter. Elf Möglichkeiten, ein Modell aufzurufen – fünf APIs, vier Abonnements ohne
nutzungsbasierte Abrechnung, zwei Router – und eine veröffentlichte Messung dessen, was jedes
Modell tatsächlich beibehält.

## Auf einen Blick

- **Elf Provider-Wege**: APIs von OpenAI, Mistral, Claude, Gemini und Grok;
  Abonnements für ChatGPT (Codex), Grok, Google (Antigravity) und Claude (Claude
  Code) ohne nutzungsbasierte Abrechnung; OpenCode-Router (Open Source, kostenlos oder lokal) und OpenRouter
  (über 400 Modelle).
- **Keine Fehler durch verloren gegangene Tokens**: Codeblöcke, Inline-Code,
  URLs, Anker und Zitate werden vor dem Aufruf durch Tokens ersetzt und
  bei der Rückgabe überprüft. Fehlt auch nur eines, wird die Datei nicht geschrieben.
- **Lange Dokumente**: Segmentierung passend zum Kontextfenster des Modells.
- **`--news`-Modus**: Geschützte englische Zitate und sprachspezifisch verwaltete Flaggen
  für News- und Monitoring-Artikel.
- **`--eco`-Modus**: Schnelle und kostengünstigere Modelle.
- Optionale **Übersetzungsnotiz**, oben, unten oder an beiden Stellen.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11 oder neuer. Zur Installation aus dem Repository siehe
[Beitragen](#mitwirken).

## Konfiguration

Schlüssel werden an drei Orten gelesen, nach absteigender Priorität; jeder füllt
nur das aus, was der vorherige leer lässt.

|     | Wo                                                    | Wofür                                 |
| --- | ----------------------------------------------------- | ------------------------------------- |
| 1   | Umgebungsvariablen                                    | CI, Container, punktuelle Ausnahme    |
| 2   | `.env` des aktuellen Verzeichnisses (oder eines übergeordneten) | ein projektspezifischer Schlüssel     |
| 3   | `~/.config/aipmt/.env`                                         | einmal installiert, gilt überall      |

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
unter Windows. Liegt kein Schlüssel vor, listet der Befehl alle drei Speicherorte auf.

**Die `.env` eines Projekts kann weder Aufrufe umleiten noch das ausgeführte
Programm festlegen.** Sie liefert Schlüssel, niemals ein Ziel oder eine Binärdatei: Jede
Variable mit `_BASE_URL`, `_API_BASE`, `_ENDPOINT` oder `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, Proxys (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), Zertifikatsspeicher (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) und `XDG_CONFIG_HOME` /
`APPDATA` wird darin mit einer Warnung ignoriert. Ein geklontes Repository darf
weder Ihren Schlüssel abfangen noch Sie dazu bringen, bei der ersten
Übersetzung dessen eigenes Programm auszuführen. Diese Datei wird zudem ohne Interpolation gelesen:
`NOM=${OPENAI_API_KEY}` kopiert den Schlüssel darin nicht. Setzen Sie diese Variablen in
der Umgebung oder in `~/.config/aipmt/.env`.

Optionale Variablen: `XAI_BASE_URL` (Standard `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (Sekunden pro Aufruf, Standard 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(Standard 600), `GROK_BIN`, `GROK_HOME` (Standard `~/.grok`), `GROK_TIMEOUT`
(Standard 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (Standard 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (Standard 600), `OPENROUTER_BASE_URL`
(`https://` erforderlich), `OPENROUTER_TIMEOUT` (Standard 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (Standard 30). Jede wird im Abschnitt
ihres Providers näher beschrieben.

## Erste Schritte

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

Wird `document.md` ins Spanische übersetzt, ergibt sich `document-es.md` in `--target_dir`;
mit `--include_model` entsteht `document-es-gpt-6.1-terra.md`. Die Dateiendung wird
stets zu `.md` – aus `article.mdx` wird `article-en.md` – außer bei
`--keep_filename`, wodurch der ursprüngliche Name beibehalten wird. Eine bereits vorhandene Übersetzung
wird ohne `--force` übersprungen.

Exit-Codes: `0`, wenn alles erfolgreich war oder übersprungen wurde, `1`, wenn mindestens eine Datei
fehlgeschlagen ist (Liste auf der Standardfehlerausgabe), `2`, wenn die Ursache an der Konfiguration liegt.
Eine fehlgeschlagene Datei wird niemals geschrieben, selbst wenn der Schreibvorgang selbst fehlschlägt:
Der Inhalt wird daneben geschrieben und anschließend umbenannt. Ein erneutes Ausführen genügt.

## Welches Modell wählen

Gemessen an zwei realen Dokumenten, die von jedem Modell in dieselben vierzehn
Sprachen übersetzt wurden. **Die Zahl steht für die Anzahl der Sprachen von vierzehn, bei denen die
Übersetzung geschrieben wurde und nichts von der Quelle abweicht.**

| Modell                | Zugriffsmethode                   | Dichter News-Artikel    | Diese README | Was abweicht und bei wie vielen Sprachen                                                                                                                           |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google-Abonnement (Antigravity)   | ✅ 14/14                | ✅ 14/14     | nichts, bei keinem der beiden Dokumente                                                                                                                            |
| **Claude Sonnet 5.5** | Anthropic-API-Schlüssel           | ✅ 14/14                | ✅ 14/14     | nichts, bei keinem der beiden Dokumente                                                                                                                            |
| **Gemini 3.7 Flash**  | Google-API-Schlüssel              | ✅ 14/14                | ⚠️ 13/14     | 1 von 14 Sprachen: ein fett gedrucktes Wort mehr (ja)                                                                                                              |
| **Gemini 3.7 Flash**  | Google-Abonnement (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 1 von 14 Sprachen: ein fett gedrucktes Wort weniger (ko)                                                                                                           |
| **GPT-5.6 Sol**       | ChatGPT-Abonnement oder OpenAI-Schlüssel | ✅ 14/14         | ⚠️ 12/14     | 2 von 14 Sprachen: ein fett gedrucktes Wort weniger (ar, ja)                                                                                                       |
| **GLM-5.2**           | OpenRouter-Schlüssel              | ✅ 14/14                | ⚠️ 11/14     | 3 von 14 Sprachen: ein fett gedrucktes Wort weniger (hi, ja, ko)                                                                                                   |
| Claude Sonnet 5       | Claude-Abonnement (Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 1 von 14 Sprachen beim Artikel: ein fett gedrucktes Wort mehr (zh); 1 bei dieser README: eine Tabellenzeile an die vorherige angehängt, bei der Anzeige ausgeblendet (ar) |
| Claude Haiku 4.5      | Claude-Abonnement (Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 3 Sprachen beim Artikel: eine Abschnittsüberschrift auf Ebene 1 heraufgestuft (en, pl, ro); bei dieser README nichts für den Vergleicher, aber interne Links auf Englisch verdoppelt |
| Claude Sonnet 5       | Anthropic-API-Schlüssel           | ⚠️ 11/14                | ⚠️ 12/14     | 3 Sprachen beim Artikel: ein zusätzlicher Codeblock aufgetaucht (es, de, hi); 2 bei dieser README: ein Link ohne Formatierung (sv), ein fett gedrucktes Wort (zh) |
| Claude Haiku 4.5      | Anthropic-API-Schlüssel           | ⚠️ 7/14                 | ✅ 14/14     | 7 Sprachen beim Artikel: eine Abschnittsüberschrift auf Ebene 1 heraufgestuft – auf Japanisch auf Französisch geblieben; nichts bei dieser README                 |
| Claude Haiku 5.5      | Anthropic-API-Schlüssel           | ⚠️ 11/14                | ❌ 12/14     | 3 Sprachen beim Artikel: Ebene einer Abschnittsüberschrift geändert oder verdoppelt (ja, ko, zh); bei dieser README 2 Sprachen abgelehnt, Inline-Code-Fragmente verloren (ar, hi) |
| Qwen 3.7 Flash        | OpenRouter-Schlüssel              | ❌ 8/14                 | ⚠️ 10/14     | 1 Sprache beim Artikel abgelehnt, 5 weitere weichen ab; bei dieser README rund 40 Wörter als `code` formatiert (ar)                                       |
| Grok 4.6              | Grok-Abonnement                   | ❌ 8/14                 | nicht bewertet | 5 von 14 Sprachen abgelehnt, da Inline-Codes und URLs fehlten; Niederländisch weicht komplett ab                                                                   |
| GPT-OSS 20B           | Lokales Modell (Ollama)           | ❌ 7/14                 | nicht erneut gemessen | 4 von 14 Sprachen abgelehnt: Das Modell beließ dort Passagen auf Französisch, die Sicherheitsprüfung fing sie ab                                           |
| MiMo v2.5 (kostenlos) | OpenCode Zen, ohne Konto          | ❌ 11/14                | nicht erneut gemessen | 1 Sprache abgelehnt; ein Abschnitt auf Polnisch verloren gegangen                                                                                         |
| Mistral Large         | Mistral-API-Schlüssel             | ❌ 5/14                 | ❌ 1/14      | **Ein ganzer Abschnitt verschwindet**: 1 Sprache beim Artikel (hi), 3 bei dieser README (ar, hi, ko) – und 3 Sprachen beim Artikel abgelehnt                      |
| DeepSeek V4 Flash     | OpenRouter-Schlüssel              | ❌ 3/14                 | nicht erneut gemessen | 10 von 14 Sprachen abgelehnt; 37 Minuten pro Sprache                                                                                                      |
| Claude Opus 5.5       | Claude-Abonnement (Claude Code)   | ❌ 0/14                 | ✅ 14/14     | Artikel in allen 14 Sprachen durch die Guardrails von Opus abgelehnt, wegen einer biologischen Kurzmeldung; nichts bei dieser README                               |

|     | Bedeutung des Symbols                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | Alle vierzehn Sprachen übersetzt und nichts weicht von der Quelle ab                                                                                                                                  |
| ⚠️  | Alle vierzehn Sprachen übersetzt; was abweicht, ist **Formatierung** – ein fett gedrucktes Wort, ein `code`, ein Link ohne eckige Klammern. Kein Text, keine URL, kein Codeblock und kein Abschnitt fehlt |
| ❌  | Mindestens eine Sprache konnte nicht übersetzt werden – die Datei wird abgelehnt, nicht geschrieben – **oder** in einer geschriebenen Datei fehlt Inhalt                                              |

Die wichtigsten Erkenntnisse:

- **Eine abgelehnte Übersetzung ist keine beschädigte Übersetzung.** Wenn bei der
  Rückgabe ein Token fehlt, wird die Datei nicht geschrieben und die Sprache zählt als
  abgelehnt. Genau das passiert Grok beim Artikel: Vier Inline-Codes und
  drei URLs gingen bereits im ersten Segment bei den fünf nicht-lateinischen Schriftsystemen verloren.
- **Ein Modell kann ein ganzes Dokument wegen eines einzigen Satzes ablehnen.** Opus 5.5
  übersetzt diese README ohne jede Abweichung, aber keinen einzigen News-Artikel: Seine
  Guardrails brechen die Antwort bei einer biologischen Kurzmeldung ab. Die Datei wird
  nicht geschrieben, und aipmt gibt den Grund an.
- **Dieses Sicherheitsnetz deckt weder Überschriften, Tabellen, Front Matter noch den
  Text ab.** Entfernt ein Modell einen Abschnitt, liefert es eine Datei, die das Tool
  anstandslos schreibt – so geschieht es bei Mistral. Diese Elemente können nicht
  durch ein Token ersetzt werden und die aktuellen Schutzprüfungen kontrollieren sie nicht;
  `scripts/compare_structure.py` erkennt einen verlorenen Abschnitt, allerdings erst im Nachhinein.
- **Grok hat keine Bewertung für diese README**: Die CLI-Sitzung lief nach zwölf
  Sprachen ab, davon elf ohne Abweichung. Ein abgebrochener Durchlauf wird nicht bewertet.
- **Die Dichte des Dokuments wiegt schwerer als die Sprache.** Grok bewältigt
  gewöhnliche READMEs problemlos, bricht jedoch bei einem linkreichen Artikel ein,
  selbst auf Niederländisch.

Daten und Dokumente: Die Spalte „Diese README“ wurde am 9. September 2026
anhand einer fixierten Version dieser Datei gemessen (785 Zeilen, 285 Inline-Codes, 89 Tabellenzeilen),
die seither überarbeitet wurde – mit Ausnahme der Zeilen zu Antigravity und Claude Code,
die am 26. September anhand der mit Version 1.14.0 veröffentlichten, kürzeren Fassung
(600 Zeilen, 257 Inline-Codes, 85 Tabellenzeilen) gemessen wurden, sowie der Zeilen zu Claude
Sonnet 5.5, Haiku 5.5 und Haiku 4.5 über die API, gemessen am 18. Oktober anhand
derselben Version. Die Spalte „Dichter News-Artikel“ stammt aus dem Testlauf vom
4. und 5. September mit einem 589 Zeilen langen Artikel, abgesehen von der Grok-Zeile, die am
9. September anhand einer anderen Ausgabe desselben Newsletters nachgemessen wurde, den Zeilen zu Antigravity und
Claude Code, gemessen am 26. September am selben Artikel, und diesen drei Claude-Zeilen am 18. Oktober.
Vollständige Tabellen, Laufzeiten und das Protokoll finden sich unter [Detaillierte Messungen](#detaillierte-messungen).

## Alle Optionen

| Option                   | Beschreibung                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Einzelne zu übersetzende Markdown-Datei (Alternative zu `--source_dir`)                                            |
| `--source_dir`           | Quellverzeichnis mit den Markdown-Dateien (Standard: `content/posts`)                                  |
| `--target_dir`           | Ausgabeverzeichnis für übersetzte Dateien (Standard: `traductions_en`)                                   |
| `--source_lang`          | Quellsprache (Standard: `fr`)                                                                                 |
| `--target_lang`          | Zielsprache (Standard: `en`)                                                                                  |
| `--model`                | Bestimmtes zu verwendendes Modell                                                                                 |
| `--eco`                  | Sparsame Modelle verwenden                                                                             |
| `--use_mistral`          | Mistral AI-API verwenden                                                                                    |
| `--use_claude`           | Claude-API verwenden                                                                                        |
| `--use_gemini`           | Gemini-API verwenden                                                                                        |
| `--use_grok`             | xAI-API (Grok) verwenden — erfordert `XAI_API_KEY`                                                          |
| `--use_codex`            | Codex-CLI über das Kontingent des ChatGPT-Abonnements verwenden                                                   |
| `--use_grok_cli`         | Grok-CLI über das Kontingent des Grok-Abonnements verwenden                                                       |
| `--use_antigravity`      | Antigravity-CLI (`agy`) über das Kontingent des Google AI Pro- oder Ultra-Abonnements verwenden                      |
| `--use_claude_code`      | Claude Code-CLI (`claude -p`) über das Kontingent des Claude Pro- oder Max-Abonnements verwenden                     |
| `--use_opencode`         | OpenCode (Open Source) mit dem in OpenCode konfigurierten Provider verwenden; erfordert `--model provider/modèle` |
| `--use_openrouter`       | OpenRouter verwenden — erfordert `OPENROUTER_API_KEY` und `--model fournisseur/modèle`                         |
| `--force`                | Erneute Übersetzung erzwingen                                                                                      |
| `--keep_filename`        | Ursprünglichen Dateinamen beibehalten                                                                         |
| `--news`                 | Nachrichtenmodus: schützt EN-Zitate, verwaltet Sprachflaggen                                     |
| `--add_translation_note` | Übersetzungshinweis hinzufügen                                                                               |
| `--note_position`        | Position des Hinweises: `top`, `bottom` (Standard) oder `both`                                                    |
| `--note_format`          | Format des Hinweises: `legacy` (Standard, fettgedruckter Absatz) oder `marker`                                           |
| `--include_model`        | Modellnamen in der Ausgabedatei angeben                                                           |
| `--reasoning_effort`     | GPT-5.x-Reasoning-Aufwand: `none`/`low`/`medium`/`high`/`xhigh`                                        |

Die neun Flags `--use_*` schließen sich gegenseitig aus: Das Kombinieren von zweien wird
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
| Codex       | `gpt-6.1-sol` (auch `gpt-5.6-sol`, `terra` und `luna` per `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.7`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | ebenso — `--eco` wirkungslos |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.8-flash-low`    |
| Claude Code | `sonnet`, Aufwand `low`                                              | ebenso — `--eco` wirkungslos |
| OpenCode    | `--model provider/modèle` erforderlich                                | ebenso — `--eco` wirkungslos |
| OpenRouter  | `--model fournisseur/modèle` erforderlich                             | ebenso — `--eco` wirkungslos |

Die Standardeinstellungen folgen der neuesten Generation jedes Anbieters, die vor
ihrer Übernahme gemessen wurde: GPT-6 bei OpenAI, Gemini 4 Hydrogen bei Google,
Grok 4.7 bei xAI seit 1.19.0. Frühere Modelle werden über `--model` weiterhin akzeptiert
(`gpt-5.6-terra`, `gemini-3.8-flash`, `grok-4.6`…), ebenso wie Gemini 4 Argon und Carbon,
das High-End-Segment von Google. aipmt regelt den Reasoning-Aufwand der GPTs und Groks selbst,
deaktiviert in `--eco`, und `--reasoning_effort` erzwingt ihn; ein Gemini erhält immer die
niedrigste Stufe, die es akzeptiert.
Ein vorübergehender Ausfall der Gemini-API (503, 429, Zeitüberschreitung) wiederholt
den Aufruf bis zu dreimal nach 10, 20 und 40 Sekunden. Ein unbeantworteter
Versuch wird nach 5 Minuten abgebrochen und auf dieselbe Weise wiederholt:
Ein stummer Server führt dazu, dass das Segment nach höchstens etwa zwanzig Minuten
fehlschlägt, anstatt unbegrenzt zu blockieren.

### Über das ChatGPT-Abonnement: `--use_codex`

Steuert das offizielle Codex-CLI: Die Übersetzung wird vom Kontingent des
ChatGPT-Abonnements abgebucht, ohne API-Schlüssel oder nutzungsbasierte Abrechnung.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Die Binärdatei wird in `CODEX_BIN`, dann in `PATH` und schließlich im Paket
  `openai-codex-cli-bin` gesucht. `~/.codex/auth.json` wird niemals gelesen.
- `OPENAI_API_KEY` und `CODEX_API_KEY` werden aus der Umgebung des
  Subprozesses entfernt: Ein vorhandener Schlüssel führt niemals zu einem Wechsel zur API.
- Jedes Segment kostet mindestens eine „Nachricht“ des 5-Stunden-Fensters — zwei,
  wenn die Validierung fehlschlägt und es wiederholt wird. OpenAI gibt als
  Schätzung 250–2.000 Nachrichten/5 Std. für `gpt-5.6-luna` (`--eco`) und
  10–100 für `gpt-5.6-sol` bei einem Plus-Tarif an.
- `--model gpt-5.6-sol`, der Standard bis Version 1.16.3, `--model gpt-5.6-terra`
  und `--model gpt-5.6-luna` laufen ebenfalls über das Abonnement.
- Ein 429 des Servers führt nicht zum Verlust der Datei: Codex verbindet sich selbstständig neu,
  aipmt wartet das Ende der Runde ab, und falls der 429-Fehler bestehen bleibt, startet das Segment
  nach 30 und dann 60 Sekunden erneut. Ein Modell, zu dem das Konto nicht berechtigt ist, liefert einen 400er-Fehler „model is
  not supported when using Codex with a ChatGPT account“.
- Langsamer als eine API, und der Abstand wächst mit der Größe des Dokuments: Bei dieser README
  betrug der Median 6 Min. 46 Sek. pro Sprache mit `gpt-5.6-sol`, verglichen mit 36 Sek. für
  `gemini-3.7-flash`.
- In CI abgelehnt (`CI` oder `GITHUB_ACTIONS` definiert): Das Abonnement authentifiziert
  sich über eine persönliche Sitzungsdatei, die auf einem geteilten Runner
  nichts zu suchen hat.
- Variablen: `CODEX_BIN`, `CODEX_TIMEOUT` (Sekunden pro Segment, Standard 600).

### Über das Grok-Abonnement: `--use_grok_cli`

Gleiches Prinzip mit dem offiziellen CLI Grok Build über das SuperGrok- oder
X Premium+-Abonnement.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Schwächere Isolation als bei Codex.** Die OS-Sandbox von Grok funktioniert
  auf vielen modernen Linux-Rechnern nicht (AppArmor, Container-Runtime-Sockets),
  und ein Profil, das nicht angewendet werden kann, startet stillschweigend ohne
  Isolation. Das Skript fordert daher standardmäßig kein Profil an, meldet dies und
  stützt sich auf die `--deny`-Regeln des CLI, einschließlich des Catch-All `*` — der einzigen
  Schicht, die den Start verweigert, anstatt den Schutz unbemerkt aufzuheben.
  `GROK_TRANSLATE_SANDBOX=read-only` erzwingt die OS-Sandbox, und der Start
  schlägt fehl, wenn das System dies nicht gewährleisten kann.
- Das Kontingent gilt wöchentlich, wird mit Chat, Imagine und Voice geteilt, und
  es gibt keinen Befehl, um es abzufragen: Ein Batch kann die Nutzung für
  Unterhaltungen unbemerkt aufbrauchen.
- Variablen: `GROK_BIN`, `GROK_HOME` (CLI-Verzeichnis, Standard `~/.grok`),
  `GROK_TIMEOUT` (Standard 900), `GROK_TRANSLATE_SANDBOX`.

### Über das Google-Abonnement: `--use_antigravity`

Gleiches Prinzip mit `agy`, dem offiziellen CLI von Antigravity: Wer für Google
AI Pro oder Ultra bezahlt, bei dem wird die Übersetzung vom Kontingent des Abonnements abgebucht,
anstatt pro Token abgerechnet zu werden. Dies ist der einzige Weg zu diesem Kontingent: Das Gemini-CLI
bedient diese Konten seit dem 18. Juni 2026 nicht mehr
([Ankündigung](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
und das Antigravity-SDK akzeptiert nur einen API-Schlüssel oder ein Google Cloud-Projekt.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Kein kostenpflichtiger Pfad bleibt offen.** agy erhält aus Ihrer
  Umgebung nur eine geschlossene Liste von Variablen — `PATH`, Sprache und Zeitzone,
  Terminal, Identität, Proxys und Zertifikate, Session-Bus — und keine Schlüssel:
  Mehrere seiner Variablen schalten einen Aufruf um, ohne etwas anzuzeigen (gemessen:
  eine sendet das Dokument an ein Drittanbieter-Gateway, eine andere an ein abgerechnetes
  Google Cloud-Projekt), und eine Ausschlussliste vergaß bei jeder Prüfung welche.
  Vor jedem Segment muss `agy -p /config`, was kein Kontingent verbraucht, zeigen,
  dass kostenpflichtige KI-Credits deaktiviert sind, ohne API-Schlüssel oder Google Cloud-Projekt — eine
  fehlende Einstellung gilt als Ablehnung —, andernfalls wird nichts übersetzt; das Protokoll jedes
  Aufrufs muss anschließend das Abonnement bestätigen (`authMethod=consumer`), sonst wird die
  Antwort abgelehnt.
- **Isolation.** Jeder Aufruf läuft in einem privaten, temporären
  Home-Verzeichnis mit einem werkzeuglosen Übersetzungsagenten: Ihre agy-Einstellungen, -Regeln,
  -Plugins, -MCP-Server und -Hooks gelangen nicht dorthin, nichts wird Ihrem
  Verlauf hinzugefügt, und die Verbindung verbleibt im Schlüsselbund, den aipmt niemals liest.
  Wenn ein Agent nicht gefunden wird, fällt agy stillschweigend auf seinen Programmieragenten
  und dessen Werkzeuge zurück: Eine vollständige Protokollzeile muss den korrekten Agenten bestätigen — ein
  Dokument, das diese Nachricht zitiert, ersetzt dies nicht —, andernfalls erfolgt eine Ablehnung.
- **Plattformen**: Linux, in einer Sitzung mit Schlüsselbund (D-Bus-Session-Bus,
  Secret Service); macOS wird akzeptiert, wurde dort jedoch nicht gemessen. Unter
  Windows abgelehnt, da agy dort die Variablen nicht liest, die jeden Aufruf isolieren,
  sowie unter Linux ohne Session-Bus — SSH-Sitzung, Container, Server: Dort
  speichert agy sein Token in einer Datei von `~/.gemini`, die durch die Isolation verborgen wird. Die
  Ablehnung erfolgt vor jedem Start samt Angabe der Ursache, statt einer einminütigen
  Wartezeit auf einen Anmeldecode.
- **Modelle**: die von `agy models`. Bei Gemini-Modellen ist der Aufwand im Namen
  enthalten (`gemini-3.8-flash-medium`…): Ein Name ohne Suffix wird vor dem Aufruf abgelehnt,
  und `--reasoning_effort` ist wirkungslos. Standardmäßig `gemini-3.8-flash-medium`,
  und `gemini-3.8-flash-low` bei `--eco`, seitdem agy Gemini 3.7
  Flash nicht mehr anbietet; die Messreihe, die den Standard festgelegt hat, ist
  in [Detaillierte Messungen](#detaillierte-messungen) beschrieben. Gemini 4 Hydrogen
  (`gemini-4-hydrogen-low`…) teilt sich das Kontingent mit 3.8 Flash und verbraucht
  mehr davon: 0,95 Punkte des 5-Stunden-Fensters für diese README bei mittlerem
  Aufwand, verglichen mit 0,32. Claude und GPT-OSS
  haben ihr eigenes, viel kleineres Kontingent: etwa 1 % des 5-Stunden-Fensters
  pro gemessenem Aufruf, gegenüber 0,05 % bei Flash. Gemini 4 Argon hat ein
  eigenes, wöchentliches Kontingent: Diese README verbraucht davon 1,35 %.
- **Kontingent**: pro Gruppe ein 5-Stunden-Fenster und ein wöchentliches, anteilig
  nach Token-Kosten. Auf dem Konto des Autors gemessen: etwa
  16 Punkte des 5-Stunden-Fensters pro Million Quellzeichen bei
  `gemini-3.8-flash-medium`, 14 bei `gemini-3.7-flash-medium` und 7 bis 8 bei
  niedrigem Aufwand — eine README mit 40.000 Zeichen kostet somit etwas mehr als einen
  halben Punkt. Das wöchentliche Limit hängt wiederum von der Tarifstufe ab. Wiederholungsversuche
  richten sich nach dem, was agy als wiederholbar deklariert; andernfalls wird ein erschöpftes
  Fenster niemals wiederholt: Jede Datei schlägt fehl bis zu dem Reset,
  den `/usage` anzeigt.
- **Langsamer als die API**: Beim dichten Messungsartikel lag der Median bei
  3 Min. 59 Sek. pro Sprache bei `gemini-3.8-flash-medium` und 3 Min. 14 Sek. bei
  `gemini-3.7-flash-medium`, verglichen mit 1 Min. 18 Sek. für Gemini 3.7 Flash über die API.
- **Unterbrechung**: Strg-C oder ein geschlossenes Terminal beenden agy zusammen mit
  dem Befehl, anstatt es seine Runde auf Kosten Ihres Kontingents beenden zu lassen;
  das Gleiche gilt für Codex, Grok CLI und OpenCode. Unter `nohup` läuft die Übersetzung weiter.
- In CI abgelehnt (`CI` oder `GITHUB_ACTIONS` definiert): Die Verbindung liegt in einem
  persönlichen Schlüsselbund. Auf einem Runner `--use_gemini` mit `GOOGLE_API_KEY` verwenden.
- Variablen: `AGY_BIN` (sonst `PATH`, dann `~/.local/bin/agy`),
  `AGY_TIMEOUT` (Sekunden pro Segment, einschließlich Start, Standard 900).

**Nutzungsbedingungen: Sie haften mit Ihrem eigenen Konto.** Die
[Nutzungsbedingungen von Antigravity](https://antigravity.google/terms) (Abschnitt 6) und dessen
[FAQ](https://antigravity.google/docs/faq/) untersagen den Zugriff auf den Dienst
über Drittanbietersoftware mithilfe des Antigravity-Logins — Claude Code,
OpenClaw und OpenCode werden dort genannt —, andernfalls droht eine Kontosperrung. aipmt
liest das Token weder aus noch verwendet es dieses wieder: Es startet die offizielle Binärdatei im
[Headless-Modus](https://antigravity.google/docs/cli/headless/), den Google
für Skripte und CI dokumentiert. Ein Google-Mitarbeiter bezeichnete das Ausführen von
`agy -p` über ein lokales Skript für die eigene Arbeit als „Standard“
([offizielles Forum, 25. September 2026, unverbindliche Antwort](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
kein Text regelt den Fall eines distribuierten Werkzeugs wie diesem eindeutig.

**Nur öffentliche Dokumente.** Gemäß Abschnitt 5 derselben Bedingungen können
Interaktionen — Prompts, Antworten, Metadaten — zur Verbesserung von
Google-Produkten und des maschinellen Lernens verwendet und von Menschen
überprüft werden, auch bei einem kostenpflichtigen Abonnement. Das Opt-out erfolgt über die Einstellung
`enableTelemetry` mit undokumentierter Wirkung, die aipmt nicht setzt; Ihre agy-Einstellungen
werden nicht in dessen Isolation übernommen. Verarbeiten Sie darüber keine vertraulichen Inhalte.

### Über das Claude-Abonnement: `--use_claude_code`

Dasselbe Prinzip gilt für `claude`, das offizielle CLI von Claude Code, im `-p`-Modus: Wer für Claude Pro oder Max bezahlt, bei dem wird die Übersetzung vom Abonnement-Kontingent abgezogen, anstatt pro Token abgerechnet zu werden. Nicht zu verwechseln mit `--use_claude`, der nach Verbrauch abgerechneten API von Anthropic.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Kein kostenpflichtiger Pfad bleibt offen, und jeder Aufruf beweist es.** Claude
  Code erhält aus Ihrer Umgebung nur eine geschlossene Liste von Variablen – weder
  API-Schlüssel noch Token, Cloud-Provider oder Marker der Claude-Code-Sitzung,
  aus der aipmt gestartet wurde. Vor dem ersten Segment muss `claude auth status` die
  Abonnement-Verbindung ohne Console-Schlüssel anzeigen, und `/usage`, das kein
  Kontingent verbraucht, muss dies bestätigen; jeder Aufruf bestätigt dies seinerseits in seinem
  Initialisierungsereignis, andernfalls wird die Antwort abgelehnt.
- **Deaktivieren Sie die „Extra-Nutzung“** (claude.ai, Einstellungen → Nutzung),
  damit die Null-Euro-Garantie greift: Wenn sie aktiviert ist, springt sie bei einem erschöpften
  Zeitfenster ein und rechnet kostenpflichtig ab, ohne einen Fehler anzuzeigen. aipmt stoppt die Übersetzung,
  sobald der Kontingentbericht eines Aufrufs dies meldet, aber dieser Aufruf ist bereits gezählt.
- **Geteiltes Kontingent mit Ihren Claude-Code-Sitzungen.** Jeder Aufruf meldet
  die Auslastung der 5-Stunden- und Wochenfenster; ab 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) wird kein weiteres Segment gestartet,
  um das Kontingent für Ihre reguläre Arbeit nicht aufzubrauchen.
- **Isolierung.** Jeder Aufruf läuft ohne Tools in einem privaten,
  temporären Verzeichnis im Modus ohne Anpassungen: Weder Ihre `CLAUDE.md` noch Ihre Plugins,
  Hooks, MCP-Server oder Einstellungen werden geladen, und nichts aus der Sitzung wird
  beibehalten. Anhänge sind deaktiviert: Ein `@chemin` in Ihrem Dokument
  bleibt reiner Text und öffnet keine Datei (gemessen).
- **Modelle**: `sonnet` standardmäßig, mit Effort `low`, und ebenso in `--eco`:
  `--eco` ändert auf diesem Pfad nichts. Anhand derselben Dokumente gemessen, ist `haiku`
  doppelt so langsam – es denkt nach (Reasoning), ohne dass man es daran hindern könnte –, bei
  kaum geringeren Kosten, und `opus` verweigert biologiebezogene Inhalte (nächster
  Punkt). Beide bleiben über `--model` zugänglich; diese Aliase folgen dem
  neuesten Modell ihrer Familie. `fable` und `[1m]`-Varianten werden abgewiesen,
  da sie kostenpflichtige Credits verbrauchen. `--reasoning_effort` regelt den Effort,
  von dem eine Übersetzung nicht profitiert: Das gemessene Reasoning ist gleich oder nahezu null.
- **Opus lehnt bestimmte biologiebezogene Inhalte ab.** Dessen Schutzmechanismen
  (Guardrails) sind strenger als die von Sonnet, und die Fehlermeldung von Anthropic warnt davor,
  dass sie „can sometimes flag biology-research-adjacent work“. Gemessen: Eine kurze Notiz
  über 279 generierte Moleküle führte dazu, dass der Artikel in allen vierzehn
  Sprachen abgelehnt wurde. Nichts wird geschrieben: aipmt weist die abgeschnittene Antwort zurück,
  benennt die Guardrails und empfiehlt `--model sonnet`.
- In CI (`CI` oder `GITHUB_ACTIONS` definiert) und unter Windows abgelehnt (nicht gemessen).
- Variablen: `AIPMT_CLAUDE_BIN` (andernfalls `PATH`, dann `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (Sekunden pro Segment, Standard 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (Standard 0.8), `CLAUDE_CONFIG_DIR` (das Claude-Code-Konto,
  niemals aus einer Projekt-`.env` übernommen); Arbeitsverzeichnisse unter
  `XDG_CACHE_HOME/aipmt/claude-code` (Standard `~/.cache`).

**Nutzungsbedingungen: Sie haften mit Ihrem eigenen Konto.** Die
[rechtliche Seite von Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
verbietet es nicht, dass „an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription“: Genau das tut aipmt, indem es die
offizielle Binärdatei startet und das Token niemals ausliest. Anthropic „does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users“, bevorzugt den API-Schlüssel für
Drittanbieter-Tools, „including open-source projects“, und behält sich das Recht vor, deren Nutzung
über kostenpflichtige Credits abzurechnen
([Claude-Hilfe](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Kein Text regelt eindeutig den Fall eines verteilten Tools, das die Binärdatei startet.

**Daten**: Bei Free-, Pro- und Max-Konten gilt das Modelltraining
auch für Claude Code, wenn die Datenschutzeinstellung dies erlaubt
([Datenseite](https://code.claude.com/docs/en/data-usage)). aipmt speichert
keine lokalen Transkriptionen (`--no-session-persistence`). Übertragen Sie darüber
keine vertraulichen Inhalte.

### Zum Anbieter der Wahl: `--use_opencode`

[OpenCode](https://opencode.ai) ist ein quelloffener Code-Agent (MIT), der
Anfragen an die darin konfigurierten Anbieter weiterleitet: API-Schlüssel, Abonnement,
OpenCode-Zen-Gateway (kostenlose Modelle ohne Konto) oder lokales Modell. Hier
wurden zwei Pfade durchgängig gemessen: Zen und Ollama.

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
zurückgreifen, dessen Konversationen zum Training verwendet werden können – und diese Entscheidung wird nicht
für Sie getroffen.

Isolierung bei jedem Aufruf:

- Eine Inline-Konfiguration mit Vorrang vor Ihrer eigenen definiert einen Agenten `aipmt`,
  dessen Tools alle abgelehnt werden (`permission: { "*": "deny" }`), Session-Sharing
  deaktiviert, `--pure`, niemals `--auto`;
- Leeres temporäres Arbeitsverzeichnis, `OPENCODE_DISABLE_PROJECT_CONFIG` und
  `OPENCODE_DISABLE_CLAUDE_CODE` angelegt – ohne diese fügt OpenCode die
  `AGENTS.md` des aktuellen Verzeichnisses sowie `~/.claude/CLAUDE.md` in den Prompt ein. Die
  globale `~/.config/opencode/AGENTS.md` wird weiterhin eingefügt; OpenCode bietet keine
  Möglichkeit, dies zu verhindern;
- Ausgabevertrag: Exit-Code 0, kein `error`-Ereignis, kein Tool-Aufruf,
  letzter Schritt als `stop`, nicht-leerer Text und der Agent `aipmt`
  tatsächlich geladen – ein unbekanntes `--agent` lässt OpenCode nicht scheitern, sondern
  fällt stillschweigend auf den Coding-Agenten zurück;
- Es wird kein Schlüssel von `aipmt` übermittelt, außer `OPENCODE_API_KEY`, dem Schlüssel
  von OpenCode selbst. Anbieter werden in OpenCode konfiguriert, nicht im
  `.env` von `aipmt`.

Wissenswert:

- Die kostenlosen Zen-Modelle unterliegen Änderungen mit undokumentierten Limits, und
  ihre Konversationen können für das Training verwendet werden: geeignet für öffentliche
  Dokumentation, nicht für vertrauliche Inhalte.
- Ein lokales Modell muss mindestens 16k Token Kontext bieten, da die Segmente
  bis zu 16.000 Zeichen umfassen. Ollama konfiguriert oft 4.096: Nutzen Sie
  ein `Modelfile` mit `PARAMETER num_ctx 32768`.
- `--eco` ist wirkungslos; `--reasoning_effort` wird unverändert als
  `--variant` von OpenCode übergeben.
- OpenCode protokolliert jede Sitzung in `~/.local/share/opencode/`.
- Variablen: `OPENCODE_BIN` (andernfalls `PATH`, dann `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (Sekunden pro Segment, Standard 600). `OPENCODE_CONFIG`
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
Modellen standardmäßig aktiviert und das eine Modelfile-Konfigurationsdatei nicht abschalten kann. Gemessen an einem Satz
aus sechs Wörtern: 919 Reasoning-Tokens und 68 Sekunden ohne diese Option, 9 Tokens mit.

### Zu mehr als 400 Modellen: `--use_openrouter`

OpenRouter ist ein nach Verbrauch über ein zentrales Guthaben abgerechneter Router vor von
Drittanbietern gehosteten Modellen – einschließlich der offenen chinesischen Modelle, die kein
anderer Provider hier anbietet.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` ist obligatorisch. Ein Preflight-Check, der vor jeglicher Abrechnung ausgeführt wird, regelt
zwei Besonderheiten des Routings:

- **Dasselbe Modell wird von Dutzenden Hostern mit unterschiedlichen Limits
  bereitgestellt** – bei `z-ai/glm-5.3-flash` 23 Hoster, darunter einer mit einem Limit von
  2.048 Output-Tokens. Der Preflight liest `/api/v1/models/{modèle}/endpoints`,
  schließt Hoster mit weniger als 8.000 Output-Tokens oder mit herabgesetztem Status aus und
  pinnt die übrigen mit `allow_fallbacks: false` fest.
- **Reasoning wird zum Ausgabetarif abgerechnet** – 107 Tokens gegenüber 2 bei
  einer „OK“-Antwort von `z-ai/glm-5.2`. Es ist standardmäßig deaktiviert; Modelle,
  die es erzwingen, erhalten den niedrigsten von ihnen akzeptierten Effort, da der Katalogstandard
  die Ausgabe vor dem Ende der Übersetzung sättigen könnte.
  `--reasoning_effort` bleibt vorrangig.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Das Kontextfenster stammt aus dem Katalog. Ein Modell mit weniger als 16.400 Tokens wird
  vor jedem Aufruf abgelehnt: 8.400 für Prompt und Segment, mindestens
  8.000 für die Ausgabe.
- Ein im Katalog fehlender Slug, ein nicht erreichbarer Katalog oder das Fehlen eines
  Hosters, der das Limit einhält, brechen den Befehl ab.
- `finish_reason=length` mit leerer Ausgabe bedeutet, dass das Budget durch
  Reasoning aufgebraucht wurde, nicht durch eine Kürzungsbeschränkung: Die Meldung unterscheidet dies.
- `--eco` ist wirkungslos.
- Variablen: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (Standard `https://openrouter.ai/api/v1`, `https://`
  erforderlich), `OPENROUTER_TIMEOUT` (Standard 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (Standard 30).

### Übersetzungshinweis

`--add_translation_note` fügt einen Hinweis hinzu: als `bottom` (Standard), `top` (nach dem
Frontmatter) oder `both` (`--note_position`), im Format `legacy` (fetter
Absatz, Standard) oder `marker` (`--note_format`). Das Format `marker` ist eine
unsichtbare Markdown-Referenzdefinition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
gefolgt von einem fetten Zitat: lesbar auf GitHub, beim Build durch ein
Remark-Plugin nutzbar.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detaillierte Messungen

Alle Messungen sind tatsächlich mit `aipmt` durchgeführte Übersetzungen in
vierzehn Sprachen: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Geschrieben** zählt die Dateien, die die Guardrails passieren ließen; **Ohne
Abweichung** diejenigen, bei denen `scripts/compare_structure.py` nichts beanstandet – gleiche Anzahl von
Abschnitten, Untertiteln, Links, unterschiedlichen URLs, Codeblöcken,
Inline-Codes, Tabellenzeilen, Zitatblöcken und fettgedruckten Wörtern.

„Ohne Abweichung“ bedeutet „nichts erkannt“, nicht „identisch“: Der Vergleicher
zählt Elemente, ohne deren Inhalt zu lesen. Er meldet weder eine gelöschte
Überschrift der Ebene 4 noch den ersetzten Text eines Inline-Codes, eine vertauschte
Flagge oder einen internen Link, der mit einer überflüssigen Klammer gerendert wurde
(`[texte]((#ancre))`) und nirgendwo mehr hinführt – und er bewertet die
Sprache nicht.

### Dichter Rechercheartikel, Modus `--news`

Eine Ausgabe des [KI-Radars von jls42.org](https://jls42.org/fr/news):
589 Zeilen, 140 Links, 21 Abschnitte, 3 geschützte englische Zitate. Kampagne
vom 4. und 5. September 2026.

| Modell                                          | Zugriff            | Geschrieben | Ohne Abweichung | Median/Sprache |
| ----------------------------------------------- | ------------------ | ----------- | --------------- | -------------- |
| `gemini-3.7-flash`                              | Google-API         | 14/14       | ✅ **14/14**    | 1 Min. 18 s    |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google-Abonnement  | 14/14       | ✅ **14/14**    | 3 Min. 59 s    |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google-Abonnement  | 14/14       | ✅ **14/14**    | 3 Min. 14 s    |
| `claude-sonnet-5-5`                             | Anthropic-API      | 14/14       | ✅ **14/14**    | 3 Min. 37 s    |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT-Abonnement | 14/14       | ✅ **14/14**    | 11 Min. 28 s   |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14       | ✅ **14/14**    | 5 Min. 37 s    |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14       | ✅ **14/14**    | 26 Min. 23 s   |
| `sonnet` (`--use_claude_code`)                  | Claude-Abonnement  | 14/14       | ⚠️ 13/14        | 6 Min. 49 s    |
| `claude-sonnet-5`                               | Anthropic-API      | 14/14       | ⚠️ 11/14        | 6 Min. 31 s    |
| `haiku` (`--use_claude_code`)                   | Claude-Abonnement  | 14/14       | ⚠️ 11/14        | 15 Min. 54 s   |
| `claude-haiku-5-5`                              | Anthropic-API      | 14/14       | ⚠️ 11/14        | 2 Min. 54 s    |
| `claude-haiku-4-5`                              | Anthropic-API      | 14/14       | ⚠️ 7/14         | 6 Min. 00 s    |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14       | ❌ 11/14        | 9 Min. 27 s    |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14       | ❌ 8/14         | 10 Min. 09 s   |
| `ollama/gpt-oss-20b-32k`                        | lokal              | 10/14       | ❌ 7/14         | 12 Min. 39 s   |
| `mistral-large-latest`                          | Mistral-API        | 11/14       | ❌ 5/14         | 5 Min. 32 s    |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14        | ❌ 3/14         | 37 Min. 27 s   |
| `grok-4.6` (`--use_grok_cli`)                   | Grok-Abonnement    | 1/14        | ❌ 1/14         | 23 Min. 11 s   |
| `opus` (`--use_claude_code`)                    | Claude-Abonnement  | 0/14        | ❌ 0/14         | —              |

Grok wurde am 9. September anhand einer anderen Ausgabe desselben Radars
(356 Zeilen) erneut gemessen: 9 von 14 Sprachen geschrieben, 8 ohne Abweichung. Diese Zahl steht
in der Haupttabelle. Drei unterbrochene Kampagnen sind nicht
aufgeführt: `qwen3.5-27b` (9 Sprachen) und `kimi-k2.6` (4) mangels Guthaben sowie
`z-ai/glm-5.3-flash`, dessen zwei Fehlschläge auf eine Reasoning-Einstellung
zurückzuführen waren, die der Provider seither korrigiert. Die OpenRouter-Zeilen wurden mit den
Standardeinstellungen des Routers vor `--use_openrouter` gemessen; `z-ai/glm-5.2`,
mit dem mitgelieferten Provider erneut gemessen, liefert dasselbe Ergebnis von 14/14. Die Zahlen wurden
am 10. September mit dem aktuellen Vergleicher neu berechnet: `qwen3.8-flash` und
`qwen3.7-flash` gewinnen jeweils eine Sprache gegenüber der ersten
Veröffentlichung hinzu, die übrigen bleiben unverändert.

Die `--use_antigravity`-Zeilen wurden am 26. September am selben
Artikel gemessen, vier Übersetzungen parallel: `gemini-3.7-flash-medium` am Vormittag,
`gemini-3.8-flash-medium` am Nachmittag. Im Englischen entfernte jedes Modell selbst
die drei Zeilen der französischen Übersetzung unter den Zitaten, ohne eine Flagge zu erfinden,
und die englischen Zitate blieben intakt: Die Fallback-Bereinigung musste
nicht eingreifen. Bei `--eco` (`gemini-3.7-flash-low`), bei nur vier Sprachen
(en, ja, ar, hi): 4 von 4 geschrieben, alle ohne Abweichung, Median von 1 Min. 52 s.
Gegenprobe am selben Tag an einer neueren Ausgabe des Radars vom
25. September (438 Zeilen, 2 englische Zitate), außerhalb des
Blogs durch `gemini-3.7-flash-medium` übersetzt: 14 von 14 geschrieben, alle ohne Abweichung, 87 bis
128 s pro Sprache.

Die `--use_claude_code`-Zeilen wurden am 26. September am selben
Artikel gemessen, vier Übersetzungen parallel, mit Effort `low`. Mit `sonnet` sind die
englischen Zitate in allen vierzehn Sprachen intakt, und im Englischen entfernte das
Modell selbst die französischen Übersetzungszeilen, ohne eine Flagge zu
erfinden. `opus` hat keine einzige Sprache geschrieben: In jeder Sprache stoppten seine Guardrails
die Antwort beim letzten Segment aufgrund einer Kurzmeldung über 279 Moleküle,
die für eine Bindungsstelle generiert wurden. Einzeln gesendet wird diese Kurzmeldung
unter der Kategorie „Bio“ abgelehnt; `sonnet` hat sie überall übersetzt. `haiku` schreibt
alle vierzehn Sprachen; in dreien (en, pl, ro) wechselt eine Abschnittsüberschrift von
Ebene 2 zu Ebene 1. Es führt Reasoning durch, ohne dass man es daran hindern könnte – 61 %
seiner Output-Tokens –, was zu mehr als der doppelten Zeit von `sonnet` führt.

Die Zeilen `claude-sonnet-5-5`, `claude-haiku-5-5` und `claude-haiku-4-5` wurden
am 18. Oktober über die Anthropic-API am selben Artikel gemessen, vier
parallele Übersetzungen pro Modell. Sonnet 5.5 verweigert die Deaktivierung seines
Reasonings: aipmt übergibt ihm die niedrigste Einstellung, die es akzeptiert, und seine
Antworten enthalten keines. Es schreibt alle vierzehn Sprachen ohne Abweichung und ohne
ein Segment erneut zu durchlaufen; im Englischen entfernte es selbst die Zeilen der
französischen Übersetzung, ohne eine Flagge zu erfinden, und die englischen Zitate sind
überall intakt. Haiku 5.5 wurde mit adaptivem Reasoning gemessen: Bei deaktiviertem
Reasoning blieben ganze Absätze auf Französisch stehen, was von der Guardrail abgewiesen wird –
3 von 14 geschriebene Sprachen. Beide Haiku-Modelle stolpern über dieselbe Kurzmeldung: Haiku 5.5
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
| `haiku` (`--use_claude_code`)                   | 14/14       | ✅ 14/14        | 4 Min. 02 s    | nichts für den Komparator; interne Links verdoppelt (en)                 |
| `claude-sonnet-5-5`                             | 14/14       | ✅ 14/14        | 1 Min. 18 s    | nichts                                                                   |
| `claude-haiku-4-5`                              | 14/14       | ✅ 14/14        | 2 Min. 06 s    | nichts                                                                   |
| `gemini-3.7-flash`                              | 14/14       | ⚠️ 13/14        | 36 s           | ein fettgedrucktes Wort (ja)                                             |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14       | ⚠️ 13/14        | 1 Min. 22 s    | ein fettgedrucktes Wort (ko)                                             |
| `sonnet` (`--use_claude_code`)                  | 14/14       | ⚠️ 13/14        | 2 Min. 20 s    | eine Tabellenzeile an die vorherige angehängt (ar)                       |
| `claude-sonnet-5`                               | 14/14       | ⚠️ 12/14        | 2 Min. 56 s    | ein Link (sv), ein fettgedrucktes Wort (zh)                              |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14       | ⚠️ 12/14        | 6 Min. 46 s    | ein fettgedrucktes Wort (ar, ja)                                         |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14       | ⚠️ 11/14        | 2 Min. 34 s    | ein fettgedrucktes Wort (hi, ja, ko)                                     |
| `qwen/qwen3.7-flash`                            | 14/14       | ⚠️ 10/14        | 2 Min. 17 s    | 40 Inline-Codes auf Arabisch hinzugefügt; Fettdruck (hi, ja, ko)         |
| `claude-haiku-5-5`                              | 12/14       | ❌ 12/14        | 1 Min. 14 s    | 2 Sprachen abgelehnt (ar, hi): Inline-Codes bei Rückgabe verloren        |
| `mistral-large-latest`                          | 14/14       | ❌ 1/14         | 2 Min. 44 s    | ein Abschnitt verloren (ar, hi, ko); Codeblöcke hinzugefügt (ja, ko, ro, zh) |

Zwei unterbrochene Kampagnen wurden nicht gewertet: Grok, CLI-Sitzung abgelaufen
nach zwölf Sprachen (elf ohne Abweichung), und `qwen3.8-flash`, HTTP 429 seines
Hosters nach zwei. `opencode/mimo-v2.5-free` und `ollama/gpt-oss-20b-32k`
wurden auf dieser Revision nicht erneut gemessen; auf derjenigen vom 4. und 5. September,
die um 277 Zeilen kürzer war, schrieben sie jeweils 9 von 14 Übersetzungen, davon 7
und 1 ohne Abweichung.

Die Zeilen `--use_antigravity` und `--use_claude_code` wurden nicht auf
der eingefrorenen Revision gemessen, sondern am 26. September auf der mit 1.14.0 veröffentlichten — und
die Zeilen `claude-sonnet-5-5`, `claude-haiku-5-5` und `claude-haiku-4-5` am 18.
Oktober auf derselben: 600 Zeilen, 257 Inline-Codes, 30 Block-Abschlüsse, 85
Tabellenzeilen. Da sie
um 185 Zeilen kürzer ist, lässt sie sich nicht direkt mit den anderen Zeilen vergleichen;
diese Zeilen untereinander lassen sich jedoch vergleichen. Bei den internen Links, die der
Komparator nicht prüft, behielt `gemini-3.8-flash-medium` sie in
allen vierzehn Sprachen intakt, `gemini-3.7-flash-medium` zerstörte sie auf Italienisch;
`sonnet` und `opus` behielten sie überall intakt, `haiku` verdoppelte sie auf
Englisch; `claude-sonnet-5-5` und `claude-haiku-4-5` behielten sie in
allen vierzehn Sprachen intakt, `claude-haiku-5-5` in den zwölf, die es schrieb.

### Vier READMEs bekannter Projekte

FastAPI, Ollama, tldr-pages und Vue.js, unverändert von GitHub übernommen —
einfachere Dokumente als die beiden vorherigen. Die Kampagne zielte auf die Modelle
mit Schwierigkeiten ab; Gemini dient hierbei als Vergleichsmaßstab.

| Modell                    | Umfang                     | Geschrieben | Ohne Abweichung |
| ------------------------- | -------------------------- | ----------- | --------------- |
| `gemini-3.7-flash`        | 4 Projekte × 14 Sprachen   | 56/56       | ✅ **55/56**    |
| `opencode/mimo-v2.5-free` | 4 Projekte × 14 Sprachen   | 55/56       | ❌ 47/56        |
| `grok-4.6` (Abonnement)   | 4 Projekte × ar, hi, ja, zh | 16/16       | ❌ 14/16        |
| `ollama/gpt-oss-20b-32k`  | 4 Projekte × ar, hi, ja, zh | 15/16       | ❌ 9/16         |

### Was diese Messungen nicht sind

- **Kein erschöpfendes Ranking**: OpenRouter allein bietet über vierhundert
  Modelle an, rund fünfzehn wurden gemessen.
- **Richtwerte für die Dauer**: je nach Kampagne drei bis sechs Übersetzungen
  parallel, und der Durchsatz eines Anbieters schwankt im Tagesverlauf.
- **Zeitgebundene Beobachtungen**: Modelle ändern sich unter demselben Namen, und Ihre
  Dokumente sind nicht die unseren.

Um die Messung auf Ihren Dokumenten anhand einer eingefrorenen Kopie der Datei zu wiederholen:

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
sich mit `./regen_translations.sh --force` neu generieren — Codex und `gpt-6.1-sol` standardmäßig
über das ChatGPT-Abonnement, vier parallel. `REGEN_PROVIDER` und
`REGEN_MODEL` ändern den Pfad: `antigravity` bleibt bei einem Abonnement, dem
von Google, und läuft ohne Ausnahmeregelung durch; eine kostenpflichtige API (`openai`, `gemini`,
`grok`, `openrouter`) wird ohne `REGEN_ALLOW_PAID_API=1` abgelehnt;
`REGEN_JOB_TIMEOUT` deckelt jeden Job (600 s, 1.800 s bei Codex und
Antigravity). Einzelheiten zu den Werkzeugen finden sich in `CLAUDE.md`.

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** — persönlicher Blog, der in 15 Sprachen veröffentlicht wird. Seine
  [tägliche KI-Presseschau](https://jls42.org/fr/news) wird jeden Tag
  mit diesem Tool übersetzt und dient als Referenzdokument für die obigen Messungen.

## Autor

Julien LE SAUX
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Haftungsausschluss

Dieses Programm wird **ohne jede Gewährleistung** gemäß den Bedingungen der
Abschnitte 15 und 16 der GPL v3 vertrieben: bereitgestellt „wie besehen“, ohne Garantie auf
Marktgängigkeit oder Eignung für einen bestimmten Zweck, und sein Autor kann nicht für
Schäden haftbar gemacht werden, die aus seiner Verwendung resultieren. Der Wortlaut der
Lizenz hat Vorrang vor dieser Zusammenfassung.

- **Vor der Veröffentlichung Korrektur lesen.** Die Schutzmechanismen decken Codeblöcke,
  Inline-Code, URLs, Anker und Zitate des Modus `--news` ab — weder
  Überschriften noch Tabellen, Front Matter oder den Sinn Ihrer Sätze.
- **Ihre Dokumente werden an den ausgewählten Anbieter übertragen**, gemäß dessen
  Nutzungsbedingungen und Datenschutzrichtlinien. Einige kostenlose Modelle können
  Ihre Interaktionen für das Training wiederverwenden, und die Bedingungen von Antigravity
  erlauben es Google, diese wiederzuverwenden und von Menschen überprüfen zu lassen,
  einschließlich kostenpflichtiger Abonnements; ein lokales Modell ist die einzige Möglichkeit,
  bei der keinerlei Daten Ihr System verlassen.
- **API-Aufrufe werden Ihnen in Rechnung gestellt.** Dieses Programm deckelt die
  Ausgaben nicht: Ein langes Dokument, ein Neustart nach einem Fehler oder ein Modell, das
  viel nachdenkt (Reasoning), verursachen höhere Kosten.
- **Die veröffentlichten Messungen sind zeitgebundene Beobachtungen**, keine Garantien.

Die genannten Produkt- und Firmennamen gehören ihren jeweiligen
Inhabern. Dieses Projekt ist mit keinem von ihnen verbunden.

**Artikel übersetzt aus dem Französischen ins Deutsche mit gemini-3.8-flash-medium.**

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Testabdeckung"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Schwachstellen"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Doppelte Zeilen (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Technische Schulden"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Codezeilen"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy-Abzeichen"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Übersetzt Markdown-Dateien von einer Sprache in eine andere und bewahrt dabei die
Struktur: Codeblöcke, Inline-Code, URLs, Anker, Tabellen und Front
Matter. Elf Möglichkeiten, ein Modell aufzurufen — fünf APIs, vier Abonnements ohne
nutzungsabhängige Abrechnung, zwei Router — und eine veröffentlichte Messung dessen, was jedes
Modell tatsächlich bewahrt.

## Kurzüberblick

- **Elf Provider-Zugangswege**: APIs von OpenAI, Mistral, Claude, Gemini und Grok;
  Abonnements von ChatGPT (Codex), Grok, Google (Antigravity) und Claude (Claude
  Code) ohne nutzungsabhängige Abrechnung; Router OpenCode (Open Source, kostenlos oder lokal) und OpenRouter
  (über 400 Modelle).
- **Keine Fehler durch verlorene Tokens**: Codeblöcke, Inline-Code,
  URLs, Anker und Zitate werden vor dem Aufruf durch Tokens ersetzt und
  nach der Rückgabe überprüft. Fehlt eines, wird die Datei nicht geschrieben.
- **Lange Dokumente**: Segmentierung entsprechend dem Kontextfenster des Modells.
- **Modus `--news`**: geschützte englische Zitate und sprachabhängig
  verwaltete Flags für Nachrichtenübersichten.
- **Modus `--eco`**: schnelle und günstigere Modelle.
- Optionale **Übersetzungsnotiz**, oben, unten oder an beiden Stellen.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11 oder neuer. Zur Installation aus dem Repository siehe
[Mitwirken](#mitwirken).

## Konfiguration

Die Schlüssel werden an drei Stellen gelesen, von der höchsten zur niedrigsten Priorität; jede
ergänzt nur das, was die vorherige offenlässt.

|     | Wo                                            | Wofür                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Umgebungsvariablen                     | CI, Container, einmalige Überschreibung |
| 2   | `.env` im aktuellen Verzeichnis (oder einem übergeordneten) | ein projektspezifischer Schlüssel            |
| 3   | `~/.config/aipmt/.env`                        | einmal eingerichtet, überall gültig       |

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
Benutzerdatei berücksichtigt `XDG_CONFIG_HOME` (nur absolute Pfade) und `%APPDATA%`
unter Windows. Ohne Schlüssel listet der Befehl die drei Speicherorte auf.

**Die `.env` eines Projekts kann weder Aufrufe umleiten noch das ausgeführte Programm
auswählen.** Sie liefert Schlüssel, niemals ein Ziel oder eine Binärdatei: Alle
Variablen mit `_BASE_URL`, `_API_BASE`, `_ENDPOINT` oder `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, Proxys (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), Zertifikatsspeicher (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) und `XDG_CONFIG_HOME` /
`APPDATA` werden dort mit einer Warnung ignoriert. Ein geklontes Repository darf
weder Ihren Schlüssel abfangen noch Sie bei der ersten Übersetzung sein eigenes Programm
ausführen lassen. Diese Datei wird außerdem ohne Interpolation gelesen:
`NOM=${OPENAI_API_KEY}` kopiert dort den Schlüssel nicht. Setzen Sie diese Variablen in
der Umgebung oder in `~/.config/aipmt/.env`.

Optionale Variablen: `XAI_BASE_URL` (Standard `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (Sekunden pro Aufruf, Standard 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(Standard 600), `GROK_BIN`, `GROK_HOME` (Standard `~/.grok`), `GROK_TIMEOUT`
(Standard 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (Standard 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (Standard 600), `OPENROUTER_BASE_URL`
(`https://` erforderlich), `OPENROUTER_TIMEOUT` (Standard 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (Standard 30). Jede wird im
Abschnitt ihres Providers ausführlich beschrieben.

## Erste Schritte

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` ergibt bei der Übersetzung ins Spanische `document-es.md` in `--target_dir`;
mit `--include_model` hingegen `document-es-gpt-5.6-terra.md`. Die Dateiendung wird
immer zu `.md` — aus `article.mdx` wird `article-en.md` — außer bei
`--keep_filename`, das den ursprünglichen Namen beibehält. Eine bereits vorhandene Übersetzung
wird ohne `--force` übersprungen.

Exit-Codes: `0`, wenn alles erfolgreich war oder übersprungen wurde, `1`, wenn noch eine Datei
fehlgeschlagen ist (Liste auf der Standardfehlerausgabe), `2`, wenn die Konfiguration die Ursache ist.
Eine fehlgeschlagene Datei wird niemals geschrieben, selbst wenn das Schreiben selbst fehlschlägt:
Der Inhalt wird zunächst daneben geschrieben und anschließend umbenannt. Ein erneuter Aufruf genügt.

## Welches Modell wählen

Gemessen anhand zweier echter Dokumente, die von jedem Modell in dieselben vierzehn
Sprachen übersetzt wurden. **Die Zahl gibt an, in wie vielen der vierzehn Sprachen die
Übersetzung geschrieben wird und nichts von der Quelle abweicht.**

| Modell                | Zugang                 | Dichte Nachrichtenübersicht | Dieses README    | Was abweicht und in wie vielen Sprachen                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google-Abonnement (Antigravity)   | ✅ 14/14                | ✅ 14/14     | nichts, in keinem der beiden Dokumente                                                                                                                                 |
| **Claude Sonnet 5.5** | API-Schlüssel von Anthropic                 | ✅ 14/14                | ✅ 14/14     | nichts, in keinem der beiden Dokumente                                                                                                                                 |
| **Gemini 3.7 Flash**  | API-Schlüssel von Google                    | ✅ 14/14                | ⚠️ 13/14     | 1 von 14 Sprachen: ein zusätzliches fett gedrucktes Wort (ja)                                                                                                                      |
| **Gemini 3.7 Flash**  | Google-Abonnement (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 1 von 14 Sprachen: ein fett gedrucktes Wort weniger (ko)                                                                                                                     |
| **GPT-5.6 Sol**       | ChatGPT-Abonnement oder OpenAI-Schlüssel | ✅ 14/14                | ⚠️ 12/14     | 2 von 14 Sprachen: ein fett gedrucktes Wort weniger (ar, ja)                                                                                                                |
| **GLM-5.2**           | OpenRouter-Schlüssel                    | ✅ 14/14                | ⚠️ 11/14     | 3 von 14 Sprachen: ein fett gedrucktes Wort weniger (hi, ja, ko)                                                                                                            |
| Claude Sonnet 5       | Claude-Abonnement (Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 1 von 14 Sprachen beim Artikel: ein zusätzliches fett gedrucktes Wort (zh); 1 bei diesem README: eine Tabellenzeile mit der vorherigen verbunden und dadurch in der Darstellung verborgen (ar)            |
| Claude Haiku 4.5      | Claude-Abonnement (Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 3 Sprachen beim Artikel: eine Abschnittsüberschrift auf Ebene 1 verschoben (en, pl, ro); bei diesem README erkennt der Vergleicher nichts, aber die internen Links sind zusätzlich auf Englisch vorhanden |
| Claude Sonnet 5       | API-Schlüssel von Anthropic                 | ⚠️ 11/14                | ⚠️ 12/14     | 3 Sprachen beim Artikel: ein zusätzlicher Codeblock (es, de, hi); 2 bei diesem README: ein Link ohne seine Auszeichnung (sv), ein fett gedrucktes Wort (zh)                              |
| Claude Haiku 4.5      | API-Schlüssel von Anthropic                 | ⚠️ 7/14                 | ✅ 14/14     | 7 Sprachen beim Artikel: eine Abschnittsüberschrift auf Ebene 1 verschoben — im Japanischen auf Französisch geblieben; nichts bei diesem README                                              |
| Claude Haiku 5.5      | API-Schlüssel von Anthropic                 | ⚠️ 11/14                | ❌ 12/14     | 3 Sprachen beim Artikel: eine Abschnittsüberschrift auf eine andere Ebene verschoben oder verdoppelt (ja, ko, zh); bei diesem README 2 Sprachen abgelehnt, Inline-Code verloren (ar, hi)    |
| Qwen 3.7 Flash        | OpenRouter-Schlüssel                    | ❌ 8/14                 | ⚠️ 10/14     | 1 Sprache beim Artikel abgelehnt, 5 weitere weichen ab; bei diesem README etwa vierzig Wörter in `code` gesetzt (ar)                                                    |
| Grok 4.6              | Grok-Abonnement                   | ❌ 8/14                 | nicht bewertet     | 5 von 14 Sprachen abgelehnt, weil Inline-Code und URLs nicht zurückgegeben wurden; die niederländische Fassung weicht durchgehend ab                                                               |
| GPT-OSS 20B           | lokales Modell (Ollama)             | ❌ 7/14                 | nicht erneut gemessen | 4 von 14 Sprachen abgelehnt: Das Modell ließ darin französische Passagen stehen, die Schutzprüfung stoppte sie                                                                  |
| MiMo v2.5 (kostenlos)   | OpenCode Zen, ohne Konto         | ❌ 11/14                | nicht erneut gemessen | 1 Sprache abgelehnt; ein Abschnitt im Polnischen verloren                                                                                                                  |
| Mistral Large         | API-Schlüssel von Mistral                   | ❌ 5/14                 | ❌ 1/14      | **Ein ganzer Abschnitt verschwindet**: 1 Sprache beim Artikel (hi), 3 bei diesem README (ar, hi, ko) — und 3 Sprachen beim Artikel abgelehnt                                |
| DeepSeek V4 Flash     | OpenRouter-Schlüssel                    | ❌ 3/14                 | nicht erneut gemessen | 10 von 14 Sprachen abgelehnt; 37 Minuten pro Sprache                                                                                                                 |
| Claude Opus 5.5       | Claude-Abonnement (Claude Code)   | ❌ 0/14                 | ✅ 14/14     | Der Artikel wurde wegen einer Kurzmeldung zur Biologie in allen 14 Sprachen von den Schutzmechanismen von Opus abgelehnt; nichts bei diesem README                                               |

|     | Bedeutung des Symbols                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alle vierzehn Sprachen übersetzt, und nichts weicht von der Quelle ab                                                                                                                                       |
| ⚠️  | alle vierzehn Sprachen übersetzt; die Abweichungen betreffen die **Auszeichnung** — ein fett gedrucktes Wort, ein `code`, ein Link, der seine Klammern verliert. Es fehlen weder Text noch URLs, Codeblöcke oder Abschnitte |
| ❌  | mindestens eine Sprache konnte nicht übersetzt werden — die Datei wird abgelehnt und nicht geschrieben — **oder** in einer geschriebenen Datei fehlen Inhalte                                                                      |

Was sich daraus mitnehmen lässt:

- **Eine abgelehnte Übersetzung ist keine beschädigte Übersetzung.** Wenn bei der Rückgabe ein Token
  fehlt, wird die Datei nicht geschrieben und die Sprache zählt als
  abgelehnt. Genau das passiert Grok beim Artikel: vier Inline-Code-Elemente und
  drei URLs gehen schon im ersten Segment in den fünf nichtlateinischen Schriftsystemen verloren.
- **Ein Modell kann wegen eines einzigen Satzes ein ganzes Dokument ablehnen.** Opus 5.5
  übersetzt dieses README ohne jede Abweichung, aber keinen Artikel der Nachrichtenübersicht: Seine
  Schutzmechanismen stoppen die Antwort bei einer Kurzmeldung zur Biologie. Die Datei wird
  nicht geschrieben, und aipmt nennt den Grund.
- **Dieses Sicherheitsnetz erfasst weder Überschriften noch Tabellen, Front Matter oder
  Text.** Entfernt ein Modell einen Abschnitt, liefert es eine Datei, die das Tool
  anstandslos schreibt — so bei Mistral. Diese Elemente lassen sich nicht
  durch ein Token ersetzen, und die aktuellen Schutzprüfungen kontrollieren sie nicht;
  `scripts/compare_structure.py` erkennt einen verlorenen Abschnitt, allerdings erst im Nachhinein.
- **Grok hat für dieses README keine Bewertung**: Seine CLI-Sitzung lief nach zwölf
  Sprachen ab, davon elf ohne Abweichung. Ein unterbrochener Testlauf wird nicht bewertet.
- **Die Dichte des Dokuments zählt mehr als die Sprache.** Grok kommt mit
  gewöhnlichen READMEs zurecht und scheitert an einem Artikel voller Links, auch auf
  Niederländisch.

Daten und Dokumente: Die Spalte „Dieses README“ wurde am 9. September 2026
anhand einer eingefrorenen Version dieser Datei gemessen (785 Zeilen, 285 Inline-Code-Elemente, 89
Tabellenzeilen), die seitdem überarbeitet wurde — ausgenommen die Zeilen für Antigravity und Claude Code,
die am 26. September anhand der mit 1.14.0 veröffentlichten, kürzeren Version gemessen wurden
(600 Zeilen, 257 Inline-Code-Elemente, 85 Tabellenzeilen), sowie die Zeilen für Claude
Sonnet 5.5, Haiku 5.5 und Haiku 4.5 über die API, die am 18. Oktober anhand
derselben Version gemessen wurden. Die Spalte „Dichte Nachrichtenübersicht“ stammt aus dem Testlauf vom
4. und 5. September anhand eines Artikels mit 589 Zeilen, ausgenommen die Zeile für Grok, die am
9. September anhand einer anderen Ausgabe derselben Nachrichtenübersicht erneut gemessen wurde, die Zeilen für Antigravity und
Claude Code, die am 26. September anhand desselben Artikels gemessen wurden, sowie diese drei
Claude-Zeilen vom 18. Oktober. Die vollständigen Tabellen, Laufzeiten und das Testverfahren finden
Sie unter [Detaillierte Messungen](#detaillierte-messungen).
## Alle Optionen

| Option                   | Beschreibung                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Einzelne zu übersetzende Markdown-Datei (Alternative zu `--source_dir`)                                             |
| `--source_dir`           | Quellverzeichnis mit Markdown-Dateien (Standard: `content/posts`)                                   |
| `--target_dir`           | Ausgabeverzeichnis für die übersetzten Dateien (Standard: `traductions_en`)                                    |
| `--source_lang`          | Quellsprache (Standard: `fr`)                                                                                  |
| `--target_lang`          | Zielsprache (Standard: `en`)                                                                                   |
| `--model`                | Zu verwendendes spezifisches Modell                                                                                  |
| `--eco`                  | Kostengünstige Modelle verwenden                                                                              |
| `--use_mistral`          | Die API von Mistral AI verwenden                                                                                     |
| `--use_claude`           | Die Claude-API verwenden                                                                                         |
| `--use_gemini`           | Die Gemini-API verwenden                                                                                         |
| `--use_grok`             | Die xAI-API (Grok) verwenden — erfordert `XAI_API_KEY`                                                           |
| `--use_codex`            | Die Codex-CLI mit dem Kontingent des ChatGPT-Abonnements verwenden                                                    |
| `--use_grok_cli`         | Die Grok-CLI mit dem Kontingent des Grok-Abonnements verwenden                                                        |
| `--use_antigravity`      | Die Antigravity-CLI (`agy`) mit dem Kontingent des Google-AI-Pro- oder Ultra-Abonnements verwenden                       |
| `--use_claude_code`      | Die Claude-Code-CLI (`claude -p`) mit dem Kontingent des Claude-Pro- oder Max-Abonnements verwenden                      |
| `--use_opencode`         | OpenCode (Open Source) mit dem in OpenCode konfigurierten Anbieter verwenden; erfordert `--model provider/modèle` |
| `--use_openrouter`       | OpenRouter verwenden — erfordert `OPENROUTER_API_KEY` und `--model fournisseur/modèle`                          |
| `--force`                | Erneute Übersetzung erzwingen                                                                                       |
| `--keep_filename`        | Ursprünglichen Dateinamen beibehalten                                                                          |
| `--news`                 | Nachrichtenmodus: schützt EN-Zitate, verwaltet Flags pro Sprache                                      |
| `--add_translation_note` | Einen Übersetzungshinweis hinzufügen                                                                                |
| `--note_position`        | Position des Hinweises: `top`, `bottom` (Standard) oder `both`                                                     |
| `--note_format`          | Format des Hinweises: `legacy` (Standard, fett gedruckter Absatz) oder `marker`                                            |
| `--include_model`        | Den Modellnamen in die Ausgabedatei aufnehmen                                                            |
| `--reasoning_effort`     | Reasoning-Aufwand für GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

Die neun Flags `--use_*` schließen sich gegenseitig aus: Zwei davon zu kombinieren wird
abgelehnt.

## Providers

### Per API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` schaltet auf die kostengünstige Stufe des jeweiligen Anbieters um.

| Provider    | Qualität (Standard)                                                     | Kostengünstig (`--eco`)      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                                      | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-3.8-flash`                                                   | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (auch `gpt-5.6-sol`, `terra` und `luna` über `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | wie zuvor — `--eco` ohne Wirkung |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, Aufwand `low`                                               | wie zuvor — `--eco` ohne Wirkung |
| OpenCode    | `--model provider/modèle` erforderlich                                | wie zuvor — `--eco` ohne Wirkung |
| OpenRouter  | `--model fournisseur/modèle` erforderlich                             | wie zuvor — `--eco` ohne Wirkung |

Gemini 3.7 Flash, bis Version 1.17.1 der Standard, ist veraltet: Google stellt
stattdessen Gemini 3.8 Flash bereit, und `--model gemini-3.7-flash` wird weiterhin akzeptiert.
Bei einer vorübergehenden Störung der Gemini-API (503, 429, Zeitüberschreitung) wird
der Aufruf bis zu dreimal wiederholt, nach 10, 20 und dann 40 Sekunden. Ein Versuch,
der ohne Antwort bleibt, wird nach 5 Minuten abgebrochen und anschließend auf
dieselbe Weise wiederholt: Ein stummer Server lässt das Segment nach höchstens
etwa zwanzig Minuten fehlschlagen, statt es unbegrenzt zu blockieren.

### Über das ChatGPT-Abonnement: `--use_codex`

Steuert die offizielle Codex-CLI: Die Übersetzung wird vom Kontingent des
ChatGPT-Abonnements abgezogen, ohne API-Schlüssel oder nutzungsabhängige Abrechnung.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Die ausführbare Datei wird zuerst in `CODEX_BIN`, dann im `PATH` und schließlich im Package
  `openai-codex-cli-bin` gesucht. `~/.codex/auth.json` wird niemals gelesen.
- `OPENAI_API_KEY` und `CODEX_API_KEY` werden aus der Umgebung des
  Unterprozesses entfernt: Ein vorhandener Schlüssel führt niemals zu einem Wechsel zur API.
- Jedes Segment verbraucht mindestens eine „Nachricht“ des 5-Stunden-Fensters — zwei,
  wenn seine Validierung fehlschlägt und es erneut versucht wird. OpenAI nennt als
  Schätzung 250-2 000 Nachrichten/5 h für `gpt-5.6-luna` (`--eco`) und
  10-100 für `gpt-5.6-sol` bei einem Plus-Tarif.
- `--model gpt-5.6-sol`, bis Version 1.16.3 der Standard, `--model gpt-5.6-terra`
  und `--model gpt-5.6-luna` laufen ebenfalls über das Abonnement.
- Ein 429 vom Server führt nicht zum Verlust der Datei: Codex verbindet sich selbst erneut,
  aipmt wartet das Ende des Durchlaufs ab, und wenn der 429 bestehen bleibt, wird das Segment
  nach 30 und dann 60 Sekunden erneut gestartet. Ein Modell, für das das Konto keine Berechtigung hat, liefert einen 400 „Modell wird
  bei der Verwendung von Codex mit einem ChatGPT-Konto nicht unterstützt“.
- Langsamer als eine API, und der Abstand wächst mit dem Dokument: Bei diesem README
  beträgt der Median mit `gpt-5.6-sol` 6 min 46 s pro Sprache, gegenüber 36 s mit
  `gemini-3.7-flash`.
- In CI abgelehnt (`CI` oder `GITHUB_ACTIONS` gesetzt): Das Abonnement authentifiziert sich
  über eine persönliche Sitzungsdatei, die auf einem gemeinsam genutzten Runner
  nichts zu suchen hat.
- Variablen: `CODEX_BIN`, `CODEX_TIMEOUT` (Sekunden pro Segment, Standard 600).

### Über das Grok-Abonnement: `--use_grok_cli`

Dasselbe Prinzip mit der offiziellen CLI Grok Build, über das SuperGrok- oder
X-Premium+-Abonnement.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Schwächere Isolation als bei Codex.** Die OS-Sandbox von Grok greift
  auf vielen neueren Linux-Rechnern nicht (AppArmor, Sockets der Container-Runtime),
  und ein Profil, das nicht angewendet werden kann, startet stillschweigend
  ohne Isolation. Das Skript fordert daher standardmäßig kein Profil an, weist darauf hin und
  stützt sich auf die Regeln `--deny` der CLI, darunter die Catch-all-Regel `*` — die einzige
  Schutzschicht, die den Start verweigert, statt den Schutz ohne
  Hinweis aufzuheben. `GROK_TRANSLATE_SANDBOX=read-only` verlangt die OS-Sandbox, und der Start
  schlägt fehl, wenn der Rechner diese Anforderung nicht erfüllen kann.
- Das Kontingent gilt wöchentlich, wird mit Chat, Imagine und Voice geteilt und lässt sich
  mit keinem Befehl abfragen: Eine Stapelverarbeitung kann das Kontingent für Unterhaltungen
  ohne Hinweis aufbrauchen.
- Variablen: `GROK_BIN`, `GROK_HOME` (CLI-Verzeichnis, Standard `~/.grok`),
  `GROK_TIMEOUT` (Standard 900), `GROK_TRANSLATE_SANDBOX`.

### Über das Google-Abonnement: `--use_antigravity`

Dasselbe Prinzip mit `agy`, der offiziellen Antigravity-CLI: Wer Google
AI Pro oder Ultra bezahlt, erhält die Übersetzung aus dem Kontingent des Abonnements,
statt sie pro Token abzurechnen. Dies ist der einzige Zugang zu diesem Kontingent: Gemini CLI
bedient diese Konten seit dem 18. Juni 2026 nicht mehr
([Ankündigung](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
und das Antigravity-SDK akzeptiert nur einen API-Schlüssel oder ein Google-Cloud-Projekt.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Kein kostenpflichtiger Zugangsweg bleibt offen.** agy erhält aus Ihrer
  Umgebung nur eine festgelegte Liste von Variablen — `PATH`, Sprache und Zeitzone,
  Terminal, Identität, Proxys und Zertifikate, Sitzungsbus — und keinerlei Schlüssel:
  Mehrere seiner Variablen leiten einen Aufruf ohne jede Anzeige um (gemessen:
  Eine sendet das Dokument an ein Gateway eines Drittanbieters, eine andere an ein
  kostenpflichtig abgerechnetes Google-Cloud-Projekt), und bei jeder erneuten Prüfung fehlten weitere in einer Sperrliste.
  Vor jedem Segment muss `agy -p /config`, das kein Kontingent verbraucht, anzeigen,
  dass kostenpflichtige KI-Credits deaktiviert sind und weder ein API-Schlüssel noch ein Google-Cloud-Projekt vorliegen — eine
  fehlende Einstellung gilt als Ablehnungsgrund —, andernfalls wird nichts übersetzt; das Protokoll jedes
  Aufrufs muss anschließend die Nutzung des Abonnements bestätigen (`authMethod=consumer`), andernfalls wird die
  Antwort abgelehnt.
- **Isolation.** Jeder Aufruf läuft in einem privaten, temporären Home-Verzeichnis
  mit einem Übersetzungsagenten ohne Tools: Ihre Einstellungen, Regeln,
  Plugins, MCP-Server und Hooks von agy werden dort nicht übernommen, Ihrem
  Verlauf wird nichts hinzugefügt, und die Anmeldung bleibt im Schlüsselbund, den aipmt niemals liest.
  Ein nicht auffindbarer Agent lässt agy stillschweigend auf seinen Coding-Agenten
  und dessen Tools zurückfallen: Eine vollständige Protokollzeile muss den richtigen Agenten bestätigen — ein
  Dokument, das diese Meldung zitiert, ersetzt sie nicht —, andernfalls wird der Aufruf abgelehnt.
- **Plattformen**: Linux in einer Sitzung mit Schlüsselbund (D-Bus-Sitzungsbus,
  Secret Service); macOS wird akzeptiert, wurde dort aber nicht vermessen. Unter
  Windows wird der Aufruf abgelehnt, da agy dort die Variablen zur Isolation der einzelnen Aufrufe nicht liest, ebenso
  unter Linux ohne Sitzungsbus — SSH-Sitzung, Container, Server: agy
  speichert sein Token dort in einer Datei unter `~/.gemini`, die durch die Isolation verborgen wird. Die
  Ablehnung erfolgt vor jedem Start mit Angabe der Ursache, statt eine Minute
  auf einen Anmeldecode zu warten.
- **Modelle**: diejenigen aus `agy models`. Bei Gemini ist der Aufwand im Namen enthalten
  (`gemini-3.8-flash-medium`…): Ein Name ohne Suffix wird vor dem Aufruf abgelehnt,
  und `--reasoning_effort` hat keine Wirkung. Standardmäßig `gemini-3.8-flash-medium`,
  und `gemini-3.7-flash-low` bei `--eco`; die Messreihen, anhand derer diese festgelegt wurden, sind
  unter [Detaillierte Messungen](#detaillierte-messungen) beschrieben. Claude und GPT-OSS
  haben ein eigenes, deutlich kleineres Kontingent: etwa 1 % des
  5-Stunden-Fensters pro gemessenem Aufruf, gegenüber 0,05 % bei Flash.
- **Kontingent**: Pro Gruppe gelten ein 5-Stunden-Fenster und ein Wochenfenster,
  anteilig nach den Token-Kosten. Auf dem Konto des Autors gemessen: etwa
  16 Punkte des 5-Stunden-Fensters pro Million Quellzeichen mit
  `gemini-3.8-flash-medium`, 14 mit `gemini-3.7-flash-medium` und 7 bis 8 bei
  niedrigem Aufwand — ein README mit 40 000 Zeichen kostet also etwas mehr als einen
  halben Punkt. Das Wochenlimit hängt dagegen von der Tarifstufe ab. Wiederholungen richten sich
  danach, was agy als wiederholbar ausweist; andernfalls wird bei einem erschöpften Fenster niemals
  erneut versucht: Jede Datei schlägt bis zu dem von `/usage` angezeigten
  Zurücksetzungszeitpunkt fehl.
- **Langsamer als die API**: Beim dichten Artikel zu den Messungen beträgt der Median
  pro Sprache 3 min 59 s mit `gemini-3.8-flash-medium` und 3 min 14 s mit
  `gemini-3.7-flash-medium`, gegenüber 1 min 18 s für Gemini 3.7 Flash über die API.
- **Unterbrechung**: Ctrl-C oder das Schließen des Terminals beenden agy zusammen mit dem
  Befehl, statt den laufenden Durchlauf weiter Ihr Kontingent verbrauchen zu lassen; dasselbe gilt
  für Codex, Grok CLI und OpenCode. Unter `nohup` läuft die Übersetzung weiter.
- In CI abgelehnt (`CI` oder `GITHUB_ACTIONS` gesetzt): Die Anmeldung liegt in einem
  persönlichen Schlüsselbund. Auf einem Runner: `--use_gemini` mit `GOOGLE_API_KEY`.
- Variablen: `AGY_BIN` (andernfalls der `PATH`, dann `~/.local/bin/agy`),
  `AGY_TIMEOUT` (Sekunden pro Segment einschließlich Start, Standard 900).

**Nutzungsbedingungen: Sie tragen die Verantwortung für Ihr Konto.** Die
[Antigravity-Nutzungsbedingungen](https://antigravity.google/terms) (Abschnitt 6) und die
[FAQ](https://antigravity.google/docs/faq/) untersagen den Zugriff auf den Dienst
durch Drittsoftware mit der Antigravity-Anmeldung — Claude Code,
OpenClaw und OpenCode werden darin genannt — und drohen eine Kontosperrung an. aipmt
liest das Token weder aus noch verwendet es erneut: Es startet die offizielle ausführbare Datei im
[Headless-Modus](https://antigravity.google/docs/cli/headless/), den Google
für Skripte und CI dokumentiert. Ein Google-Mitarbeiter bezeichnete es als „üblich“,
`agy -p` aus einem lokalen Skript für die eigene Arbeit aufzurufen
([offizielles Forum, 25. September 2026, unverbindliche Antwort](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
kein Text klärt den Fall eines verbreiteten Tools wie diesem.

**Nur öffentliche Dokumente.** Laut Abschnitt 5 derselben Bedingungen können die
ausgetauschten Inhalte — Prompts, Antworten, Metadaten — zur Verbesserung der
Produkte und des maschinellen Lernens von Google verwendet und von
Menschen gelesen werden, auch bei einem kostenpflichtigen Abonnement. Der Widerspruch erfolgt über die Einstellung
`enableTelemetry`, deren Wirkung nicht dokumentiert ist und die aipmt nicht setzt; Ihre Einstellungen
von agy werden in dessen isolierter Umgebung nicht übernommen. Übermitteln Sie darüber keine vertraulichen Inhalte.
### Mit dem Claude-Abonnement: `--use_claude_code`

Dasselbe Prinzip gilt für `claude`, die offizielle CLI von Claude Code, im Modus `-p`: Wer
Claude Pro oder Max bezahlt, dem wird die Übersetzung vom Kontingent des
Abonnements abgezogen, statt pro Token abgerechnet zu werden. Nicht zu verwechseln mit
`--use_claude`, der nutzungsabhängig abgerechneten API von Anthropic.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Kein kostenpflichtiger Weg bleibt offen, und jeder Aufruf weist das nach.** Claude
  Code erhält aus Ihrer Umgebung nur eine abgeschlossene Liste von Variablen — weder
  API-Schlüssel noch Token, Cloud-Anbieter oder Kennzeichen der Claude-Code-Sitzung,
  aus der aipmt gestartet würde. Vor dem ersten Segment muss `claude auth status`
  die Anmeldung über das Abonnement ohne Console-Schlüssel anzeigen, und `/usage`, das
  kein Kontingent verbraucht, muss dies bestätigen; jeder Aufruf bestätigt es seinerseits in seinem
  Initialisierungsereignis, andernfalls wird die Antwort abgelehnt.
- **Deaktivieren Sie „extra usage“** (claude.ai, Einstellungen → Nutzung), damit
  es bei null Euro bleibt: Ist diese Option aktiviert, übernimmt sie bei einem ausgeschöpften Zeitfenster und
  rechnet ab, ohne einen Fehler anzuzeigen. aipmt stoppt die Übersetzung, sobald die
  Kontingentmeldung eines Aufrufs dies anzeigt, aber dieser Aufruf wird bereits angerechnet.
- **Gemeinsames Kontingent mit Ihren Claude-Code-Sitzungen.** Jeder Aufruf meldet
  die Nutzung der 5-Stunden- und Wochenfenster; oberhalb von 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) wird kein weiteres Segment gestartet, um
  das für Ihre Arbeit benötigte Kontingent nicht aufzubrauchen.
- **Isolation.** Jeder Aufruf läuft ohne Tools in einem privaten,
  temporären Verzeichnis und ohne Anpassungen: Weder Ihre `CLAUDE.md` noch Ihre Plugins,
  Hooks, MCP-Server oder Einstellungen werden geladen, und von der
  Sitzung wird nichts gespeichert. Anhänge sind deaktiviert: Ein `@chemin` in Ihrem Dokument
  bleibt Text und öffnet keine Datei (gemessen).
- **Modelle**: Standardmäßig `sonnet` mit dem Aufwand `low`, auch in `--eco`:
  `--eco` ändert auf diesem Weg nichts. Bei Messungen mit denselben Dokumenten ist `haiku`
  doppelt so langsam — es führt Reasoning aus, ohne dass sich das unterbinden lässt — bei
  kaum geringeren Kosten, und `opus` verweigert biologische Inhalte (nächster
  Punkt). Beide bleiben über `--model` verfügbar; diese Aliasse folgen dem
  neuesten Modell ihrer Familie. `fable` und die Varianten `[1m]` werden abgelehnt,
  weil sie kostenpflichtiges Guthaben verbrauchen. `--reasoning_effort` regelt den Aufwand,
  von dem eine Übersetzung nicht profitiert: Das gemessene Reasoning ist null oder nahezu null.
- **Opus verweigert bestimmte biologische Inhalte.** Seine Schutzmechanismen sind
  strenger als die von Sonnet, und die Fehlermeldung von Anthropic weist darauf hin, dass sie
  „mitunter auch Arbeiten im Umfeld biologischer Forschung markieren können“. Gemessen: Eine Kurzmeldung
  über 279 generierte Moleküle führte dazu, dass der Artikel in allen vierzehn
  Sprachen abgelehnt wurde. Es wird nichts geschrieben: aipmt lehnt die abgebrochene Antwort ab, nennt die
  Schutzmechanismen und empfiehlt `--model sonnet`.
- In CI abgelehnt (`CI` oder `GITHUB_ACTIONS` gesetzt) sowie unter Windows (nicht gemessen).
- Variablen: `AIPMT_CLAUDE_BIN` (sonst `PATH`, dann `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (Sekunden pro Segment, Standard 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (Standard 0.8), `CLAUDE_CONFIG_DIR` (das Konto von
  Claude Code, niemals aus einer `.env` eines Projekts übernommen); Arbeitsverzeichnisse unter
  `XDG_CACHE_HOME/aipmt/claude-code` (Standard `~/.cache`).

**Nutzungsbedingungen: Ihr Konto trägt die Verantwortung.** Die
[Seite zu den rechtlichen Bedingungen von Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
hindert „Endnutzer nicht daran, sich mit ihrem eigenen Claude-Abonnement bei der unveränderten Claude-Code-Binärdatei
anzumelden“: Genau das tut aipmt, das die
offizielle Binärdatei startet und niemals das Token liest. Anthropic „gestattet es
Drittentwicklern […] jedoch nicht, Anfragen im Namen ihrer Nutzer über Zugangsdaten für Free-, Pro- oder Max-Tarife
weiterzuleiten“, bevorzugt für Drittanbieter-Tools den API-Schlüssel,
„einschließlich Open-Source-Projekten“, und behält sich vor, deren
Nutzung vom kostenpflichtigen Guthaben abzuziehen
([Claude-Hilfe](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Kein Text klärt den Fall eines verbreiteten Tools, das die Binärdatei startet.

**Daten**: Bei Free-, Pro- und Max-Konten gilt das Modelltraining
auch für Claude Code, wenn die Datenschutzeinstellung es erlaubt
([Datenseite](https://code.claude.com/docs/en/data-usage)). aipmt speichert
keine lokalen Transkripte (`--no-session-persistence`). Übermitteln Sie darüber
keine vertraulichen Inhalte.

### Zum Anbieter Ihrer Wahl: `--use_opencode`

[OpenCode](https://opencode.ai) ist ein Open-Source-Coding-Agent (MIT), der
Anfragen an die darin konfigurierten Anbieter weiterleitet: API-Schlüssel, Abonnement,
OpenCode-Zen-Gateway (kostenlose Modelle, ohne Konto) oder lokales Modell. Zwei
Wege wurden hier durchgängig gemessen: Zen und Ollama.

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

`--model` ist erforderlich: Ohne diese Angabe würde OpenCode auf ein kostenloses Modell zurückfallen,
dessen Dialoge für das Training verwendet werden können, und diese Entscheidung wird nicht
für Sie getroffen.

Isolation bei jedem Aufruf:

- Eine Inline-Konfiguration, die Vorrang vor Ihrer eigenen hat, definiert einen Agenten `aipmt`,
  dessen sämtliche Tools gesperrt sind (`permission: { "*": "deny" }`), mit deaktivierter
  Sitzungsfreigabe, `--pure`, niemals `--auto`;
- leeres temporäres Arbeitsverzeichnis, `OPENCODE_DISABLE_PROJECT_CONFIG` und
  `OPENCODE_DISABLE_CLAUDE_CODE` gesetzt — ohne sie fügt OpenCode die
  `AGENTS.md` des aktuellen Verzeichnisses und `~/.claude/CLAUDE.md` in den Prompt ein. Die
  globale `~/.config/opencode/AGENTS.md` wird weiterhin eingefügt; OpenCode erlaubt nicht,
  sie auszuschließen;
- Ausgabeanforderungen: Rückgabecode 0, kein Ereignis `error`, kein
  Tool-Aufruf, letzter Schritt in `stop`, nicht leerer Text und der Agent `aipmt`
  tatsächlich geladen — ein unbekanntes `--agent` lässt OpenCode nicht fehlschlagen, es
  fällt stillschweigend auf den Coding-Agenten zurück;
- kein Schlüssel aus `aipmt` wird übergeben, außer `OPENCODE_API_KEY`, dem Schlüssel
  von OpenCode selbst. Die Anbieter werden in OpenCode konfiguriert, nicht in
  der `.env` von `aipmt`.

Gut zu wissen:

- Die kostenlosen Modelle von Zen wechseln, ihre Grenzen sind nicht dokumentiert, und
  ihre Dialoge können für das Training verwendet werden: für öffentliche
  Dokumentation, nicht für private Inhalte.
- Ein lokales Modell muss mindestens 16 k Tokens Kontext bieten, da die Segmente
  bis zu 16 000 Zeichen lang sind. Ollama konfiguriert häufig 4 096: Verwenden Sie
  ein `Modelfile` mit `PARAMETER num_ctx 32768`.
- `--eco` hat keine Wirkung; `--reasoning_effort` wird unverändert als
  `--variant` von OpenCode übergeben.
- OpenCode protokolliert jede Sitzung in `~/.local/share/opencode/`.
- Variablen: `OPENCODE_BIN` (sonst `PATH`, dann `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (Sekunden pro Segment, Standard 600). `OPENCODE_CONFIG`
  wird unverändert an OpenCode übergeben.

Beispiel eines lokalen Modells über Ollama, in `~/.config/opencode/opencode.json`:

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
Modellen standardmäßig aktiviert und das ein Modelfile nicht deaktivieren kann. Gemessen an einem Satz mit
sechs Wörtern: 919 Reasoning-Tokens und 68 Sekunden ohne die Option, 9 Tokens mit ihr.

### Zu mehr als 400 Modellen: `--use_openrouter`

OpenRouter ist ein nutzungsabhängig abgerechneter Router mit einem gemeinsamen Guthaben für
Modelle, die von Dritten gehostet werden — darunter offene chinesische Modelle, die hier kein
anderer Provider anbietet.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` ist erforderlich. Eine Vorabprüfung, die vor jeder Abrechnung ausgeführt wird, regelt
zwei Besonderheiten des Routings:

- **Dasselbe Modell wird von Dutzenden Hosting-Anbietern mit unterschiedlichen
  Obergrenzen bereitgestellt** — bei `z-ai/glm-5.3-flash` sind es 23 Anbieter, darunter einer mit einer Grenze von
  2 048 Ausgabe-Tokens. Die Vorabprüfung liest `/api/v1/models/{modèle}/endpoints`,
  schließt Anbieter mit weniger als 8 000 Ausgabe-Tokens oder beeinträchtigtem Status aus und
  legt die übrigen mit `allow_fallbacks: false` fest.
- **Reasoning wird zum Ausgabetarif abgerechnet** — 107 Tokens gegenüber 2 bei
  einer „OK“-Antwort von `z-ai/glm-5.2`. Es ist standardmäßig abgeschaltet; Modelle,
  die es erzwingen, erhalten den niedrigsten von ihnen akzeptierten Aufwand, da der Standardwert des
  Katalogs die Ausgabe ausschöpfen kann, bevor die Übersetzung abgeschlossen ist.
  `--reasoning_effort` behält Vorrang.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Das Kontextfenster stammt aus dem Katalog. Ein Modell mit weniger als 16 400 Tokens wird
  vor jedem Aufruf abgelehnt: 8 400 für Prompt und Segment, mindestens 8 000 für die
  Ausgabe.
- Ein im Katalog fehlender Slug, ein nicht erreichbarer Katalog oder das Fehlen
  eines Hosting-Anbieters, der die Obergrenze einhält, stoppen den Befehl.
- `finish_reason=length` mit leerer Ausgabe bedeutet, dass das Budget durch
  Reasoning aufgebraucht wurde, nicht dass die Ausgabe abgeschnitten wurde: Die Meldung unterscheidet dies.
- `--eco` hat keine Wirkung.
- Variablen: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (Standard `https://openrouter.ai/api/v1`, `https://`
  erforderlich), `OPENROUTER_TIMEOUT` (Standard 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (Standard 30).

### Übersetzungshinweis

`--add_translation_note` fügt einen Hinweis hinzu, in `bottom` (Standard), `top` (nach dem
Front Matter) oder `both` (`--note_position`), im Format `legacy` (fettgedruckter
Absatz, Standard) oder `marker` (`--note_format`). Das Format `marker` ist eine
unsichtbare Markdown-Referenzdefinition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
gefolgt von einem fettgedruckten Zitat: auf GitHub lesbar, beim Build durch ein
remark-Plugin auswertbar.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detaillierte Messungen

Alle Messungen sind tatsächlich mit `aipmt` ausgeführte Übersetzungen in
vierzehn Sprachen: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Geschrieben** zählt die Dateien, die die Prüfungen bestanden haben; **Ohne
Abweichung** diejenigen, bei denen `scripts/compare_structure.py` nichts feststellt — gleiche Anzahl an
Abschnitten, Unterüberschriften, Links, unterschiedlichen URLs, Codeblöcken,
Inline-Code-Elementen, Tabellenzeilen, Zitatblöcken und fettgedruckten Wörtern.

„Ohne Abweichung“ bedeutet „nichts erkannt“, nicht „identisch“: Das Vergleichswerkzeug
zählt Elemente, ohne ihren Inhalt zu lesen. Es meldet weder eine gelöschte Überschrift der
Ebene 4 noch ersetzten Inline-Code-Text, eine ausgetauschte Flagge
oder einen internen Link mit einer überzähligen Klammer,
`[texte]((#ancre))`, der nirgendwo mehr hinführt — und es beurteilt die
Sprache nicht.

### Umfangreicher Nachrichtenartikel, Modus `--news`

Eine Ausgabe der [KI-Nachrichten von jls42.org](https://jls42.org/fr/news):
589 Zeilen, 140 Links, 21 Abschnitte, 3 geschützte englische Zitate. Messreihe
vom 4. und 5. September 2026.

| Modell                                          | Zugang              | Geschrieben | Ohne Abweichung   | Median/Sprache |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google-API         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google-Abonnement  | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google-Abonnement  | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `claude-sonnet-5-5`                             | Anthropic-API      | 14/14   | ✅ **14/14** | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT-Abonnement | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | Claude-Abonnement  | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | Anthropic-API      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | Claude-Abonnement  | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `claude-haiku-5-5`                              | Anthropic-API      | 14/14   | ⚠️ 11/14     | 2 min 54 s     |
| `claude-haiku-4-5`                              | Anthropic-API      | 14/14   | ⚠️ 7/14      | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | lokal              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral-API        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok-Abonnement    | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | Claude-Abonnement  | 0/14    | ❌ 0/14      | —              |

Grok wurde am 9. September anhand einer anderen Ausgabe derselben Nachrichten
(356 Zeilen) erneut gemessen: 9 von 14 Sprachen geschrieben, 8 ohne Abweichung. Dieser Wert
steht in der Übersichtstabelle am Anfang. Drei abgebrochene Messreihen sind nicht
aufgeführt: `qwen3.5-27b` (9 Sprachen) und `kimi-k2.6` (4) wegen fehlenden Guthabens,
`z-ai/glm-5.3-flash`, dessen zwei Fehlschläge auf eine Reasoning-Einstellung zurückgingen,
die der Provider inzwischen korrigiert. Die OpenRouter-Zeilen wurden mit den
Standardeinstellungen des Routers vor `--use_openrouter` gemessen; `z-ai/glm-5.2`,
mit dem ausgelieferten Provider erneut gemessen, liefert dieselben 14/14. Die Werte wurden
am 10. September mit dem aktuellen Vergleichswerkzeug neu berechnet: `qwen3.8-flash` und
`qwen3.7-flash` gewinnen gegenüber der ersten
Veröffentlichung jeweils eine Sprache hinzu, die übrigen bleiben unverändert.

Die Zeilen `--use_antigravity` wurden am 26. September am selben
Artikel mit vier parallelen Übersetzungen gemessen: `gemini-3.7-flash-medium` am Vormittag,
`gemini-3.8-flash-medium` am Nachmittag. Im Englischen entfernten beide selbst
die drei Zeilen mit französischen Übersetzungen unter den Zitaten, ohne eine
Flagge zu erfinden, und die englischen Zitate sind unverändert: Die ersatzweise Bereinigung musste
nichts tun. In `--eco` (`gemini-3.7-flash-low`), bei nur vier Sprachen
(en, ja, ar, hi): 4 von 4 geschrieben, alle ohne Abweichung, 1 min 52 s
Median. Gegenprobe am selben Tag mit einer neueren Nachrichtenausgabe,
der vom 25. September (438 Zeilen, 2 englische Zitate), außerhalb des
Blogs mit `gemini-3.7-flash-medium` übersetzt: 14 von 14 geschrieben, alle ohne Abweichung, 87 bis
128 s pro Sprache.

Die Zeilen `--use_claude_code` wurden am 26. September am selben
Artikel mit vier parallelen Übersetzungen und dem Aufwand `low` gemessen. Mit `sonnet` sind die
englischen Zitate in allen vierzehn Sprachen unverändert, und im Englischen hat das
Modell die Zeilen mit französischen Übersetzungen selbst entfernt, ohne eine
Flagge zu erfinden. `opus` schrieb keine Sprache: In jeder stoppten seine Schutzmechanismen
die Antwort beim letzten Segment wegen einer Kurzmeldung über 279 Moleküle,
die für eine Bindungsstelle generiert wurden. Einzeln übermittelt, wird diese Kurzmeldung
unter der Kategorie „bio“ abgelehnt; `sonnet` übersetzte sie in alle Sprachen. `haiku` schreibt
alle vierzehn Sprachen; in drei davon (en, pl, ro) wechselt eine Abschnittsüberschrift von
Ebene 2 auf Ebene 1. Es führt Reasoning aus, ohne dass sich das unterbinden lässt — 61 % seiner
Ausgabe-Tokens —, daher benötigt es mehr als doppelt so viel Zeit wie `sonnet`.

Die Zeilen `claude-sonnet-5-5`, `claude-haiku-5-5` und `claude-haiku-4-5` wurden
am 18. Oktober über die Anthropic-API am selben Artikel mit vier
parallelen Übersetzungen pro Modell gemessen. Sonnet 5.5 verweigert das Abschalten seines
Reasonings: aipmt sendet ihm die niedrigste akzeptierte Einstellung, und seine
Antworten enthalten keines. Es schreibt alle vierzehn Sprachen ohne Abweichung und ohne
ein Segment erneut zu verarbeiten; im Englischen hat es die Zeilen mit
französischen Übersetzungen selbst entfernt, ohne eine Flagge zu erfinden, und die englischen Zitate sind
überall unverändert. Haiku 5.5 wird mit seinem adaptiven Reasoning gemessen: Bei abgeschaltetem
Reasoning ließ es ganze Absätze auf Französisch stehen, was die Prüfung ablehnt —
3 von 14 Sprachen geschrieben. Beide Haiku scheitern an derselben Kurzmeldung: Haiku 5.5
ändert im Japanischen, Koreanischen und Chinesischen die Ebene ihrer Überschrift oder verdoppelt sie,
Haiku 4.5 setzt sie in sieben Sprachen auf Ebene 1 und lässt sie
im Japanischen auf Französisch stehen. Haiku 4.5 kostet 3,67 $ für beide Dokumente in allen
vierzehn Sprachen, Haiku 5.5 0,57 $, Sonnet 5.5 9,21 $.
### README dieses Projekts, Standard-Markdown

Stand vom 9. September 2026: 785 Zeilen, 285 Inline-Code-Elemente, 40
Blockabschlussmarkierungen, 89 Tabellenzeilen. Vier Übersetzungen parallel.

| Modell                                          | Geschrieben | Ohne Abweichung | Median/Sprache | Was abweicht                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | nichts                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | nichts                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | nichts im Vergleichstool; interne Links verdoppelt (en)                   |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | nichts                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | nichts                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | ein fettgedrucktes Wort (ja)                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | ein fettgedrucktes Wort (ko)                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | eine Tabellenzeile mit der vorherigen zusammengefügt (ar)                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | ein Link (sv), ein fettgedrucktes Wort (zh)                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | ein fettgedrucktes Wort (ar, ja)                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | ein fettgedrucktes Wort (hi, ja, ko)                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 40 Inline-Code-Elemente im Arabischen hinzugefügt; Fettdruck (hi, ja, ko)                   |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2 Sprachen abgelehnt (ar, hi): Inline-Code-Elemente bei der Rückgabe verloren        |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | ein Abschnitt verloren (ar, hi, ko); Codeblöcke hinzugefügt (ja, ko, ro, zh) |

Zwei abgebrochene Durchläufe sind nicht aufgeführt: Grok, dessen CLI-Sitzung
nach zwölf Sprachen ablief (elf ohne Abweichung), und `qwen3.8-flash`, dessen
Hosting-Anbieter nach zwei Sprachen HTTP 429 zurückgab. `opencode/mimo-v2.5-free` und `ollama/gpt-oss-20b-32k`
wurden auf diesem Stand nicht erneut gemessen; auf dem Stand vom 4. und 5. September,
der um 277 Zeilen kürzer war, schrieben beide jeweils 9 von 14 Übersetzungen, davon 7
beziehungsweise 1 ohne Abweichung.

Die Zeilen `--use_antigravity` und `--use_claude_code` wurden nicht auf dem
eingefrorenen Stand gemessen, sondern am 26. September auf dem mit 1.14.0 veröffentlichten Stand — und
die Zeilen `claude-sonnet-5-5`, `claude-haiku-5-5` und `claude-haiku-4-5` am 18.
Oktober auf demselben Stand: 600 Zeilen, 257 Inline-Code-Elemente, 30 Blockabschlussmarkierungen, 85
Tabellenzeilen. Da dieser Stand
um 185 Zeilen kürzer ist, lässt er sich nicht direkt mit den anderen Zeilen vergleichen;
diese Zeilen lassen sich jedoch untereinander vergleichen. Bei den internen Links, die das
Vergleichstool nicht prüft, hat `gemini-3.8-flash-medium` sie in
allen vierzehn Sprachen intakt erhalten, `gemini-3.7-flash-medium` hat sie im Italienischen beschädigt;
`sonnet` und `opus` haben sie überall intakt erhalten, `haiku` hat sie im
Englischen verdoppelt; `claude-sonnet-5-5` und `claude-haiku-4-5` haben sie in
allen vierzehn Sprachen intakt erhalten, `claude-haiku-5-5` in den zwölf Sprachen, die es geschrieben hat.

### Vier README-Dateien bekannter Projekte

FastAPI, Ollama, tldr-pages und Vue.js, unverändert von GitHub übernommen —
einfachere Dokumente als die beiden vorherigen. Der Durchlauf zielte auf Modelle
mit Schwierigkeiten ab; Gemini dient hier als Vergleichspunkt.

| Modell                    | Umfang                  | Geschrieben | Ohne Abweichung   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 Projekte × 14 Sprachen     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 Projekte × 14 Sprachen     | 55/56   | ❌ 47/56     |
| `grok-4.6` (Abonnement)   | 4 Projekte × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 Projekte × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### Was diese Messungen nicht sind

- **Keine vollständige Rangliste**: Allein OpenRouter bietet mehr als vierhundert
  Modelle an, etwa fünfzehn wurden gemessen.
- **Nur ungefähre Zeitangaben**: Je nach Durchlauf liefen drei bis sechs Übersetzungen
  parallel, und der Durchsatz eines Anbieters schwankt im Tagesverlauf.
- **Zeitgebundene Beobachtungen**: Modelle ändern sich unter demselben Namen, und Ihre
  Dokumente sind andere als unsere.

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

Beide Zeilen sind erforderlich: Ohne `pip install -e .` antwortet `python -m aipmt`
mit `No module named aipmt`.

Werkzeuge zur Qualitätssicherung, optional, aber empfohlen:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Die 28 Übersetzungen des Repositorys (README und CHANGELOG, vierzehn Sprachen) lassen sich
mit `./regen_translations.sh --force` neu erzeugen — standardmäßig mit Codex und `gpt-6.1-sol` über
das ChatGPT-Abonnement, vier parallel. `REGEN_PROVIDER` und
`REGEN_MODEL` ändern den Zugriffsweg: `antigravity` nutzt weiterhin ein Abonnement, das
von Google, und wird ohne Ausnahmegenehmigung zugelassen; eine kostenpflichtige API (`openai`, `gemini`,
`grok`, `openrouter`) wird ohne `REGEN_ALLOW_PAID_API=1` abgelehnt;
`REGEN_JOB_TIMEOUT` begrenzt jeden Job (600 s, 1 800 s bei Codex und
Antigravity). Einzelheiten zu den Werkzeugen stehen in `CLAUDE.md`.

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** — persönlicher Blog, der in 15 Sprachen veröffentlicht wird. Seine
  [tägliche KI-Nachrichtenübersicht](https://jls42.org/fr/news) wird jeden Tag
  mit diesem Werkzeug übersetzt und dient als Referenzdokument für die obigen Messungen.

## Autor

Julien LE SAUX
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Haftungsausschluss

Dieses Programm wird **ohne jegliche Gewährleistung** gemäß den
Abschnitten 15 und 16 der GPL v3 verbreitet: Es wird „wie besehen“ bereitgestellt, ohne Gewährleistung
der Marktgängigkeit oder der Eignung für einen bestimmten Zweck, und sein Autor kann
nicht für Schäden haftbar gemacht werden, die aus seiner Nutzung entstehen. Der
Lizenztext hat Vorrang vor dieser Zusammenfassung.

- **Lesen Sie vor der Veröffentlichung Korrektur.** Die Schutzmechanismen decken Codeblöcke,
  Inline-Code, URLs, Anker und Zitate des Modus `--news` ab — weder
  Überschriften noch Tabellen, Front Matter oder die Bedeutung Ihrer Sätze.
- **Ihre Dokumente werden an den gewählten Anbieter übermittelt**, gemäß dessen
  Nutzungsbedingungen und Datenrichtlinie. Manche kostenlosen Modelle können
  Ihre Unterhaltungen für das Training wiederverwenden, und die Bedingungen von Antigravity
  erlauben Google, diese wiederzuverwenden und von Menschen prüfen zu lassen,
  auch bei einem kostenpflichtigen Abonnement; ein lokales Modell ist der einzige Weg, bei dem
  keine Daten Ihren Rechner verlassen.
- **API-Aufrufe werden Ihnen in Rechnung gestellt.** Dieses Programm begrenzt die
  Ausgaben nicht: Ein langes Dokument, ein erneuter Versuch nach einem Fehler oder ein Modell mit umfangreichen
  Reasoning-Prozessen verursachen höhere Kosten.
- **Die veröffentlichten Messungen sind zeitgebundene Beobachtungen**, keine Garantien.

Die genannten Produkt- und Firmennamen gehören ihren jeweiligen
Inhabern. Dieses Projekt ist mit keinem von ihnen verbunden.

**Artikel mit gpt-6.1-sol aus dem Französischen ins Deutsche übersetzt.**

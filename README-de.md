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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Sicherheitslücken"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
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
Matter. Elf Möglichkeiten, ein Modell aufzurufen — fünf APIs, vier Abonnements ohne
nutzungsabhängige Abrechnung, zwei Router — und veröffentlichte Messungen dazu, was jedes
Modell tatsächlich bewahrt.

## Auf einen Blick

- **Elf Provider-Zugangswege**: APIs von OpenAI, Mistral, Claude, Gemini und Grok;
  Abonnements von ChatGPT (Codex), Grok, Google (Antigravity) und Claude (Claude
  Code) ohne nutzungsabhängige Abrechnung; Router OpenCode (Open Source, kostenlos oder lokal) und OpenRouter
  (über 400 Modelle).
- **Keine Fehler durch verlorene Tokens**: Codeblöcke, Inline-Code,
  URLs, Anker und Zitate werden vor dem Aufruf durch Tokens ersetzt und
  bei der Rückgabe geprüft. Fehlt eines, wird die Datei nicht geschrieben.
- **Lange Dokumente**: Aufteilung entsprechend dem Kontextfenster des Modells.
- **Modus `--news`**: geschützte englische Zitate und sprachweise verwaltete
  Flags für Artikel zur Nachrichtenbeobachtung.
- **Modus `--eco`**: schnelle und günstigere Modelle.
- Optionaler **Übersetzungshinweis**, oben, unten oder an beiden Stellen.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 oder neuer. Zur Installation aus dem Repository siehe
[Mitwirken](#mitwirken).

## Konfiguration

Die Schlüssel werden an drei Stellen gelesen, mit absteigender Priorität; jede
ergänzt nur, was die vorherige offenlässt.

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
Benutzerdatei richtet sich nach `XDG_CONFIG_HOME` (nur absolute Pfade) und `%APPDATA%`
unter Windows. Ohne Schlüssel listet der Befehl die drei Speicherorte auf.

**Die `.env` eines Projekts kann weder Aufrufe umleiten noch das ausgeführte
Programm auswählen.** Sie liefert Schlüssel, niemals ein Ziel oder eine Binärdatei: Alle
Variablen mit `_BASE_URL`, `_API_BASE`, `_ENDPOINT` oder `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, Proxys (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), Zertifikatsspeicher (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) und `XDG_CONFIG_HOME` /
`APPDATA` werden dort mit einer Warnung ignoriert. Ein geklontes Repository darf
weder Ihren Schlüssel abfangen noch Sie dazu bringen können, bei der
ersten Übersetzung sein eigenes Programm zu starten. Diese Datei wird außerdem ohne Interpolation gelesen:
`NOM=${OPENAI_API_KEY}` kopiert den Schlüssel dort nicht hinein. Setzen Sie diese Variablen in
der Umgebung oder in `~/.config/aipmt/.env`.

Optionale Variablen: `XAI_BASE_URL` (Standard `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (Sekunden pro Aufruf, Standard 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(Standard 600), `GROK_BIN`, `GROK_HOME` (Standard `~/.grok`), `GROK_TIMEOUT`
(Standard 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (Standard 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (Standard 600), `OPENROUTER_BASE_URL`
(`https://` erforderlich), `OPENROUTER_TIMEOUT` (Standard 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (Standard 30). Jede wird im Abschnitt
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

`document.md` ergibt bei der Übersetzung ins Spanische `document-es.md` in `--target_dir`;
mit `--include_model` ergibt sich `document-es-gpt-5.6-terra.md`. Die Dateiendung wird
immer zu `.md` — aus `article.mdx` wird `article-en.md` — außer mit
`--keep_filename`, wodurch der ursprüngliche Name erhalten bleibt. Eine bereits vorhandene Übersetzung
wird ohne `--force` übersprungen.

Exit-Codes: `0`, wenn alles erfolgreich war oder übersprungen wurde, `1`, wenn noch eine Datei
fehlgeschlagen ist (Liste auf der Standardfehlerausgabe), `2`, wenn die Konfiguration die Ursache ist.
Eine fehlgeschlagene Datei wird niemals geschrieben, auch wenn das Schreiben selbst scheitert:
Der Inhalt wird zunächst in eine danebenliegende Datei geschrieben und diese anschließend umbenannt. Ein erneuter Aufruf genügt.

## Welches Modell wählen

Gemessen an zwei echten Dokumenten, die von jedem Modell in dieselben vierzehn Sprachen
übersetzt wurden. **Die Zahl gibt an, in wie vielen der vierzehn Sprachen die
Übersetzung geschrieben wird und nichts von der Quelle abweicht.**

| Modell                | Zugang                 | Dichter Nachrichtenüberblick | Diese README    | Was abweicht und in wie vielen Sprachen                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google-Abonnement (Antigravity)   | ✅ 14/14                | ✅ 14/14     | nichts, in keinem der beiden Dokumente                                                                                                                                 |
| **Claude Sonnet 5.5** | Anthropic-API-Schlüssel                 | ✅ 14/14                | ✅ 14/14     | nichts, in keinem der beiden Dokumente                                                                                                                                 |
| **Gemini 3.7 Flash**  | Google-API-Schlüssel                    | ✅ 14/14                | ⚠️ 13/14     | 1 von 14 Sprachen: ein zusätzliches fett gedrucktes Wort (ja)                                                                                                                      |
| **Gemini 3.7 Flash**  | Google-Abonnement (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 1 von 14 Sprachen: ein fett gedrucktes Wort weniger (ko)                                                                                                                     |
| **GPT-5.6 Sol**       | ChatGPT-Abonnement oder OpenAI-Schlüssel | ✅ 14/14                | ⚠️ 12/14     | 2 von 14 Sprachen: ein fett gedrucktes Wort weniger (ar, ja)                                                                                                                |
| **GLM-5.2**           | OpenRouter-Schlüssel                    | ✅ 14/14                | ⚠️ 11/14     | 3 von 14 Sprachen: ein fett gedrucktes Wort weniger (hi, ja, ko)                                                                                                            |
| Claude Sonnet 5       | Claude-Abonnement (Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 1 von 14 Sprachen beim Artikel: ein zusätzliches fett gedrucktes Wort (zh); 1 bei dieser README: eine Tabellenzeile hängt an der vorherigen und wird bei der Anzeige verborgen (ar)            |
| Claude Haiku 4.5      | Claude-Abonnement (Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 3 Sprachen beim Artikel: eine Abschnittsüberschrift auf Ebene 1 verschoben (en, pl, ro); bei dieser README erkennt das Vergleichswerkzeug nichts, aber die internen Links sind zusätzlich auf Englisch vorhanden |
| Claude Sonnet 5       | Anthropic-API-Schlüssel                 | ⚠️ 11/14                | ⚠️ 12/14     | 3 Sprachen beim Artikel: ein zusätzlicher Codeblock (es, de, hi); 2 bei dieser README: ein Link ohne sein Markup (sv), ein fett gedrucktes Wort (zh)                              |
| Claude Haiku 4.5      | Anthropic-API-Schlüssel                 | ⚠️ 7/14                 | ✅ 14/14     | 7 Sprachen beim Artikel: eine Abschnittsüberschrift auf Ebene 1 verschoben — im Japanischen auf Französisch geblieben; nichts bei dieser README                                              |
| Claude Haiku 5.5      | Anthropic-API-Schlüssel                 | ⚠️ 11/14                | ❌ 12/14     | 3 Sprachen beim Artikel: eine Abschnittsüberschrift auf eine andere Ebene verschoben oder verdoppelt (ja, ko, zh); bei dieser README 2 Sprachen abgelehnt, verlorener Inline-Code (ar, hi)    |
| Qwen 3.7 Flash        | OpenRouter-Schlüssel                    | ❌ 8/14                 | ⚠️ 10/14     | 1 Sprache beim Artikel abgelehnt, 5 weitere weichen ab; bei dieser README etwa vierzig Wörter in `code` gesetzt (ar)                                                    |
| Grok 4.6              | Grok-Abonnement                   | ❌ 8/14                 | nicht bewertet     | 5 von 14 Sprachen abgelehnt, weil Inline-Code und URLs nicht zurückgegeben wurden; Niederländisch weicht überall ab                                                               |
| GPT-OSS 20B           | lokales Modell (Ollama)             | ❌ 7/14                 | nicht erneut gemessen | 4 von 14 Sprachen abgelehnt: Das Modell ließ darin Passagen auf Französisch stehen, die Schutzprüfung stoppte sie                                                                  |
| MiMo v2.5 (kostenlos)   | OpenCode Zen, ohne Konto         | ❌ 11/14                | nicht erneut gemessen | 1 Sprache abgelehnt; ein Abschnitt im Polnischen verloren                                                                                                                  |
| Mistral Large         | Mistral-API-Schlüssel                   | ❌ 5/14                 | ❌ 1/14      | **ein ganzer Abschnitt verschwindet**: 1 Sprache beim Artikel (hi), 3 bei dieser README (ar, hi, ko) — und 3 Sprachen beim Artikel abgelehnt                                |
| DeepSeek V4 Flash     | OpenRouter-Schlüssel                    | ❌ 3/14                 | nicht erneut gemessen | 10 von 14 Sprachen abgelehnt; 37 Minuten pro Sprache                                                                                                                 |
| Claude Opus 5.5       | Claude-Abonnement (Claude Code)   | ❌ 0/14                 | ✅ 14/14     | der Artikel wurde wegen einer biologischen Kurzmeldung von den Schutzmechanismen von Opus in allen 14 Sprachen abgelehnt; nichts bei dieser README                                               |

|     | Bedeutung des Symbols                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alle vierzehn Sprachen übersetzt, und nichts weicht von der Quelle ab                                                                                                                                       |
| ⚠️  | alle vierzehn Sprachen übersetzt; die Abweichungen betreffen das **Markup** — ein fett gedrucktes Wort, ein `code`, ein Link, der seine eckigen Klammern verliert. Es fehlen weder Text noch URLs, Codeblöcke oder Abschnitte |
| ❌  | mindestens eine Sprache konnte nicht übersetzt werden — die Datei wird abgelehnt und nicht geschrieben — **oder** in einer geschriebenen Datei fehlt Inhalt                                                                      |

Was sich daraus ableiten lässt:

- **Eine abgelehnte Übersetzung ist keine beschädigte Übersetzung.** Wenn bei der Rückgabe ein Token
  fehlt, wird die Datei nicht geschrieben und die Sprache als
  abgelehnt gezählt. Das passiert bei Grok mit dem Artikel: Vier Inline-Code-Elemente und
  drei URLs gehen bereits im ersten Segment verloren, und zwar bei den fünf nichtlateinischen Schriftsystemen.
- **Ein Modell kann wegen eines einzigen Satzes ein ganzes Dokument ablehnen.** Opus 5.5
  übersetzt diese README ohne Abweichung, aber keinen Nachrichtenüberblick: Seine
  Schutzmechanismen stoppen die Antwort bei einer biologischen Kurzmeldung. Die Datei wird
  nicht geschrieben, und aipmt gibt den Grund an.
- **Dieses Sicherheitsnetz deckt weder Überschriften, Tabellen, Front Matter noch
  Text ab.** Wenn ein Modell einen Abschnitt entfernt, liefert es eine Datei, die das Tool
  anstandslos schreibt — so geschehen bei Mistral. Diese Elemente lassen sich nicht
  durch Tokens ersetzen, und die aktuellen Schutzprüfungen kontrollieren sie nicht;
  `scripts/compare_structure.py` erkennt einen verlorenen Abschnitt, allerdings erst im Nachhinein.
- **Grok erhält für diese README keine Bewertung**: Seine CLI-Sitzung lief nach zwölf
  Sprachen ab, darunter elf ohne Abweichung. Ein abgebrochener Messdurchlauf wird nicht bewertet.
- **Die Dichte des Dokuments zählt mehr als die Sprache.** Grok kommt mit
  gewöhnlichen READMEs zurecht und scheitert an einem Artikel voller Links, auch auf
  Niederländisch.

Daten und Dokumente: Die Spalte „Diese README“ wurde am 9. September 2026
an einer eingefrorenen Revision dieser Datei gemessen (785 Zeilen, 285 Inline-Code-Elemente, 89
Tabellenzeilen), die seitdem überarbeitet wurde — ausgenommen die Zeilen für Antigravity und Claude Code,
die am 26. September an der mit Version 1.14.0 veröffentlichten, kürzeren Revision
gemessen wurden (600 Zeilen, 257 Inline-Code-Elemente, 85 Tabellenzeilen), sowie die Zeilen für Claude
Sonnet 5.5, Haiku 5.5 und Haiku 4.5 über die API, die am 18. Oktober an
derselben Revision gemessen wurden. Die Spalte „Dichter Nachrichtenüberblick“ stammt aus dem Messdurchlauf vom
4. und 5. September mit einem Artikel von 589 Zeilen, ausgenommen die Grok-Zeile, die am
9. September an einer anderen Ausgabe desselben Nachrichtenüberblicks erneut gemessen wurde, die Zeilen für Antigravity und
Claude Code, die am 26. September am selben Artikel gemessen wurden, sowie diese drei
Claude-Zeilen vom 18. Oktober. Die vollständigen Tabellen, Laufzeiten und das Messprotokoll stehen
unter [Detaillierte Messungen](#detaillierte-messungen).
## Alle Optionen

| Option                   | Beschreibung                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Einzelne zu übersetzende Markdown-Datei (Alternative zu `--source_dir`)                                             |
| `--source_dir`           | Quellverzeichnis mit den Markdown-Dateien (Standard: `content/posts`)                                   |
| `--target_dir`           | Ausgabeverzeichnis für die übersetzten Dateien (Standard: `traductions_en`)                                    |
| `--source_lang`          | Ausgangssprache (Standard: `fr`)                                                                                  |
| `--target_lang`          | Zielsprache (Standard: `en`)                                                                                   |
| `--model`                | Bestimmtes zu verwendendes Modell                                                                                  |
| `--eco`                  | Kostengünstige Modelle verwenden                                                                              |
| `--use_mistral`          | Die API von Mistral AI verwenden                                                                                     |
| `--use_claude`           | Die Claude-API verwenden                                                                                         |
| `--use_gemini`           | Die Gemini-API verwenden                                                                                         |
| `--use_grok`             | Die xAI-API (Grok) verwenden — erfordert `XAI_API_KEY`                                                           |
| `--use_codex`            | Die Codex-CLI mit dem Kontingent des ChatGPT-Abonnements verwenden                                                    |
| `--use_grok_cli`         | Die Grok-CLI mit dem Kontingent des Grok-Abonnements verwenden                                                        |
| `--use_antigravity`      | Die Antigravity-CLI (`agy`) mit dem Kontingent des Google AI Pro- oder Ultra-Abonnements verwenden                       |
| `--use_claude_code`      | Die Claude Code-CLI (`claude -p`) mit dem Kontingent des Claude Pro- oder Max-Abonnements verwenden                      |
| `--use_opencode`         | OpenCode (Open Source) mit dem in OpenCode konfigurierten Anbieter verwenden; erfordert `--model provider/modèle` |
| `--use_openrouter`       | OpenRouter verwenden — erfordert `OPENROUTER_API_KEY` und `--model fournisseur/modèle`                          |
| `--force`                | Erneute Übersetzung erzwingen                                                                                       |
| `--keep_filename`        | Ursprünglichen Dateinamen beibehalten                                                                          |
| `--news`                 | Nachrichtenmodus: schützt EN-Zitate, verwaltet Flaggen je Sprache                                      |
| `--add_translation_note` | Einen Übersetzungshinweis hinzufügen                                                                                |
| `--note_position`        | Position des Hinweises: `top`, `bottom` (Standard) oder `both`                                                     |
| `--note_format`          | Format des Hinweises: `legacy` (Standard, fettgedruckter Absatz) oder `marker`                                            |
| `--include_model`        | Modellnamen in die Ausgabedatei aufnehmen                                                            |
| `--reasoning_effort`     | Reasoning-Aufwand von GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

Die neun Flags `--use_*` schließen sich gegenseitig aus: Zwei davon zu kombinieren wird
abgelehnt.

## Anbieter

### Per API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` schaltet bei jedem Anbieter auf die kostengünstige Stufe um.

| Anbieter    | Qualität (Standard)                                                     | Kostengünstig (`--eco`)      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                                      | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                                   | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (auch `gpt-5.6-sol`, `terra` und `luna` über `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                                           | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, Aufwand `low`                                               | unverändert — `--eco` ohne Wirkung |
| OpenCode    | `--model provider/modèle` erforderlich                                | unverändert — `--eco` ohne Wirkung |
| OpenRouter  | `--model fournisseur/modèle` erforderlich                             | unverändert — `--eco` ohne Wirkung |

### Über das ChatGPT-Abonnement: `--use_codex`

Steuert die offizielle Codex-CLI: Die Übersetzung wird auf das Kontingent des
ChatGPT-Abonnements angerechnet, ohne API-Schlüssel oder nutzungsabhängige Abrechnung.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Die ausführbare Datei wird zunächst in `CODEX_BIN`, dann im `PATH` und schließlich im Package
  `openai-codex-cli-bin` gesucht. `~/.codex/auth.json` wird niemals gelesen.
- `OPENAI_API_KEY` und `CODEX_API_KEY` werden aus der Umgebung des
  Unterprozesses entfernt: Ein vorhandener Schlüssel führt niemals zu einem Wechsel zur API.
- Jedes Segment kostet mindestens eine „Nachricht“ im 5-Stunden-Fenster — zwei,
  wenn seine Validierung fehlschlägt und es erneut versucht wird. OpenAI nennt als
  Schätzung 250-2 000 Nachrichten/5 h für `gpt-5.6-luna` (`--eco`) und
  10-100 für `gpt-5.6-sol` im Plus-Tarif.
- `--model gpt-5.6-sol`, bis Version 1.16.3 der Standard, `--model gpt-5.6-terra`
  und `--model gpt-5.6-luna` laufen ebenfalls über das Abonnement.
- Ein 429 vom Server führt nicht zum Verlust der Datei: Codex verbindet sich selbstständig neu,
  aipmt wartet auf das Ende des Durchlaufs, und wenn der 429 bestehen bleibt, wird das Segment
  nach 30 und dann 60 Sekunden erneut gestartet. Ein Modell, für das das Konto keine Berechtigung hat, liefert einen 400 mit der Meldung „model is
  not supported when using Codex with a ChatGPT account“.
- Langsamer als eine API, und der Abstand wächst mit dem Dokument: Bei diesem README
  beträgt der Median mit `gpt-5.6-sol` 6 min 46 s pro Sprache, gegenüber 36 s für
  `gemini-3.7-flash`.
- In CI abgelehnt (`CI` oder `GITHUB_ACTIONS` gesetzt): Das Abonnement authentifiziert sich
  über eine persönliche Sitzungsdatei, die auf einem gemeinsam genutzten Runner
  nichts zu suchen hat.
- Variablen: `CODEX_BIN`, `CODEX_TIMEOUT` (Sekunden pro Segment, Standard 600).

### Über das Grok-Abonnement: `--use_grok_cli`

Dasselbe Prinzip mit der offiziellen Grok Build-CLI über das SuperGrok- oder
X Premium+-Abonnement.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Schwächere Abschottung als bei Codex.** Die OS-Sandbox von Grok greift
  auf vielen neueren Linux-Systemen nicht (AppArmor, Sockets von Container-Runtimes),
  und ein Profil, das nicht angewendet werden kann, startet stillschweigend ohne
  Abschottung. Das Skript fordert daher standardmäßig kein Profil an, weist darauf hin und
  stützt sich auf die `--deny`-Regeln der CLI, darunter die Catch-all-Regel `*` — die einzige
  Schutzschicht, die den Start verweigert, anstatt den Schutz unbemerkt
  aufzuheben. `GROK_TRANSLATE_SANDBOX=read-only` verlangt die OS-Sandbox, und der Start
  schlägt fehl, wenn das System sie nicht bereitstellen kann.
- Das Kontingent gilt wöchentlich, wird mit Chat, Imagine und Voice geteilt und lässt sich
  durch keinen Befehl abfragen: Ein Stapellauf kann das Kontingent für Unterhaltungen
  ohne Hinweis aufbrauchen.
- Variablen: `GROK_BIN`, `GROK_HOME` (CLI-Verzeichnis, Standard `~/.grok`),
  `GROK_TIMEOUT` (Standard 900), `GROK_TRANSLATE_SANDBOX`.

### Über das Google-Abonnement: `--use_antigravity`

Dasselbe Prinzip mit `agy`, der offiziellen Antigravity-CLI: Wer Google
AI Pro oder Ultra bezahlt, lässt die Übersetzung auf das Kontingent des Abonnements anrechnen,
anstatt sie pro Token abzurechnen. Dies ist der einzige Zugang zu diesem Kontingent: Gemini CLI
unterstützt diese Konten seit dem 18. Juni 2026 nicht mehr
([Ankündigung](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
und das Antigravity-SDK akzeptiert nur einen API-Schlüssel oder ein Google Cloud-Projekt.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Kein kostenpflichtiger Zugangsweg bleibt offen.** agy erhält aus Ihrer
  Umgebung nur eine abschließend festgelegte Liste von Variablen — `PATH`, Sprache und Zeitzone,
  Terminal, Identität, Proxys und Zertifikate, Sitzungsbus — und keinerlei Schlüssel:
  Mehrere seiner Variablen schalten einen Aufruf ohne sichtbaren Hinweis um (gemessen:
  Eine sendet das Dokument an ein Gateway eines Drittanbieters, eine andere an ein
  kostenpflichtiges Google Cloud-Projekt), und bei jeder erneuten Prüfung fehlten Einträge in einer Sperrliste.
  Vor jedem Segment muss `agy -p /config`, das kein Kontingent verbraucht, anzeigen,
  dass kostenpflichtige KI-Credits deaktiviert sind und weder ein API-Schlüssel noch ein Google Cloud-Projekt vorliegt — eine
  fehlende Einstellung führt zur Ablehnung —, andernfalls wird nichts übersetzt; anschließend muss das Protokoll jedes
  Aufrufs die Nutzung des Abonnements bestätigen (`authMethod=consumer`), andernfalls wird die
  Antwort abgelehnt.
- **Abschottung.** Jeder Aufruf läuft in einem privaten, temporären Home-Verzeichnis,
  mit einem Übersetzungsagenten ohne Tools: Ihre Einstellungen, Regeln,
  Plugins, MCP-Server und agy-Hooks gelangen nicht hinein, Ihrem
  Verlauf wird nichts hinzugefügt, und die Anmeldung bleibt im Schlüsselbund, den aipmt niemals liest.
  Wenn ein Agent nicht gefunden wird, fällt agy stillschweigend auf seinen Coding-Agenten
  und dessen Tools zurück: Eine vollständige Protokollzeile muss den richtigen Agenten bestätigen — ein
  Dokument, das diese Meldung zitiert, ersetzt sie nicht —, andernfalls wird der Vorgang abgelehnt.
- **Plattformen**: Linux in einer Sitzung mit Schlüsselbund (D-Bus-Sitzungsbus,
  Secret Service); macOS wird akzeptiert, wurde dort jedoch nicht vermessen. Abgelehnt
  unter Windows, wo agy die Variablen zur Isolation einzelner Aufrufe nicht liest, sowie
  unter Linux ohne Sitzungsbus — SSH-Sitzung, Container, Server: Dort speichert agy
  sein Token in einer Datei unter `~/.gemini`, die durch die Isolation verborgen wird. Die
  Ablehnung erfolgt vor jedem Start unter Angabe des Grundes, statt eine Minute
  auf einen Anmeldecode zu warten.
- **Modelle**: die von `agy models`. Bei Gemini ist der Aufwand im Namen enthalten
  (`gemini-3.8-flash-medium`…): Ein Name ohne Suffix wird vor dem Aufruf abgelehnt,
  und `--reasoning_effort` hat keine Wirkung. Standardmäßig `gemini-3.8-flash-medium`,
  und `gemini-3.7-flash-low` bei `--eco`; die Messreihen, auf deren Grundlage sie festgelegt wurden, sind
  unter [Detaillierte Messungen](#detaillierte-messungen) beschrieben. Claude und GPT-OSS
  haben ein eigenes, deutlich kleineres Kontingent: etwa 1 % des
  5-Stunden-Fensters pro gemessenem Aufruf, gegenüber 0,05 % bei Flash.
- **Kontingent**: pro Gruppe ein 5-Stunden-Fenster und ein wöchentliches Fenster,
  anteilig nach den Token-Kosten. Gemessen mit dem Konto des Autors: etwa
  16 Punkte des 5-Stunden-Fensters pro Million Quellzeichen bei
  `gemini-3.8-flash-medium`, 14 bei `gemini-3.7-flash-medium` und 7 bis 8 bei
  niedrigem Aufwand — ein README mit 40 000 Zeichen kostet also etwas mehr als einen
  halben Punkt. Das wöchentliche Limit hängt hingegen von der Tarifstufe ab. Wiederholungen richten
  sich danach, was agy als wiederholbar angibt; andernfalls wird bei einem ausgeschöpften Fenster niemals
  erneut versucht: Jede Datei schlägt bis zum Zurücksetzen fehl,
  dessen Zeitpunkt `/usage` anzeigt.
- **Langsamer als die API**: Beim dichten Artikel zu den Messungen beträgt der Median
  pro Sprache 3 min 59 s bei `gemini-3.8-flash-medium` und 3 min 14 s bei
  `gemini-3.7-flash-medium`, gegenüber 1 min 18 s für Gemini 3.7 Flash über die API.
- **Unterbrechung**: Ctrl-C oder das Schließen des Terminals beenden agy zusammen mit dem
  Befehl, statt den Durchlauf weiter Ihr Kontingent verbrauchen zu lassen; dasselbe gilt
  für Codex, Grok CLI und OpenCode. Unter `nohup` läuft die Übersetzung weiter.
- In CI abgelehnt (`CI` oder `GITHUB_ACTIONS` gesetzt): Die Anmeldung liegt in einem
  persönlichen Schlüsselbund. Auf einem Runner: `--use_gemini` mit `GOOGLE_API_KEY`.
- Variablen: `AGY_BIN` (ansonsten der `PATH`, dann `~/.local/bin/agy`),
  `AGY_TIMEOUT` (Sekunden pro Segment einschließlich Start, Standard 900).

**Nutzungsbedingungen: Sie tragen das Risiko für Ihr Konto.** Die
[Antigravity-Nutzungsbedingungen](https://antigravity.google/terms) (Abschnitt 6) und die
[FAQ](https://antigravity.google/docs/faq/) untersagen den Zugriff auf den Dienst
durch Drittsoftware mittels der Antigravity-Anmeldung — Claude Code,
OpenClaw und OpenCode werden dort genannt —, andernfalls droht eine Kontosperrung. aipmt
liest das Token weder aus noch verwendet es erneut: Es startet die offizielle ausführbare Datei im
[Headless-Modus](https://antigravity.google/docs/cli/headless/), den Google
für Skripte und CI dokumentiert. Ein Google-Mitarbeiter bezeichnete es als „Standard“,
`agy -p` aus einem lokalen Skript für die eigene Arbeit aufzurufen
([offizielles Forum, 25. September 2026, rechtlich unverbindliche Antwort](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
kein Text klärt den Fall eines verbreiteten Tools wie dieses.

**Nur öffentliche Dokumente.** Gemäß Abschnitt 5 derselben Bedingungen können die
Interaktionen — Prompts, Antworten, Metadaten — zur Verbesserung der
Google-Produkte und des maschinellen Lernens verwendet und von
Menschen geprüft werden, auch bei einem kostenpflichtigen Abonnement. Ein Widerspruch erfolgt über die Einstellung
`enableTelemetry`, deren Wirkung nicht dokumentiert ist und die aipmt nicht setzt; Ihre agy-Einstellungen
werden nicht in die isolierte Umgebung übernommen. Übermitteln Sie darüber keine vertraulichen Inhalte.
### Mit dem Claude-Abonnement: `--use_claude_code`

Dasselbe Prinzip gilt für `claude`, die offizielle CLI von Claude Code, im Modus `-p`: Wer
Claude Pro oder Max bezahlt, dessen Übersetzung wird vom Kontingent des
Abonnements abgezogen, statt pro Token abgerechnet zu werden. Nicht zu verwechseln mit
`--use_claude`, der nutzungsabhängig abgerechneten API von Anthropic.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Kein kostenpflichtiger Zugangsweg bleibt offen, und jeder Aufruf belegt das.** Claude
  Code erhält aus Ihrer Umgebung nur eine festgelegte Liste von Variablen — weder
  API-Schlüssel noch Token, Cloud-Anbieter oder Kennzeichnung der Claude-Code-Sitzung,
  aus der aipmt gestartet würde. Vor dem ersten Segment muss `claude auth status`
  die Anmeldung über das Abonnement ohne Console-Schlüssel anzeigen, und `/usage`, das
  kein Kontingent verbraucht, muss dies bestätigen; jeder Aufruf bestätigt es seinerseits in seinem
  Initialisierungsereignis, andernfalls wird die Antwort abgewiesen.
- **Deaktivieren Sie „Extra Usage“** (claude.ai, Einstellungen → Nutzung), damit
  es bei null Euro bleibt: Ist die Funktion aktiviert, übernimmt sie bei einem ausgeschöpften Zeitfenster und
  rechnet ab, ohne einen Fehler anzuzeigen. aipmt stoppt die Übersetzung, sobald die
  Kontingentmeldung eines Aufrufs dies anzeigt, aber dieser Aufruf wird bereits angerechnet.
- **Gemeinsames Kontingent mit Ihren Claude-Code-Sitzungen.** Jeder Aufruf meldet
  die Nutzung der 5-Stunden- und Wochenfenster; oberhalb von 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) wird kein weiteres Segment gestartet, damit
  das für Ihre Arbeit benötigte Kontingent nicht aufgebraucht wird.
- **Abschottung.** Jeder Aufruf läuft ohne Tools in einem privaten,
  temporären Verzeichnis und in einem Modus ohne Anpassungen: Weder Ihre `CLAUDE.md` noch Ihre Plugins,
  Hooks, MCP-Server oder Einstellungen werden geladen, und von der
  Sitzung bleibt nichts erhalten. Anhänge sind deaktiviert: Ein `@chemin` in Ihrem Dokument
  bleibt Text und öffnet keine Datei (gemessen).
- **Modelle**: Standardmäßig `sonnet` mit dem Aufwand `low`, auch in `--eco`:
  `--eco` ändert an diesem Zugangsweg nichts. Bei Messungen mit denselben Dokumenten ist `haiku`
  doppelt so langsam — sein Reasoning lässt sich nicht unterbinden — bei
  kaum geringeren Kosten, und `opus` lehnt biologische Inhalte ab (nächster
  Punkt). Beide bleiben über `--model` zugänglich; diese Aliase verweisen auf das
  neueste Modell ihrer Familie. `fable` und die Varianten `[1m]` werden abgewiesen,
  weil sie kostenpflichtige Guthaben verwenden. `--reasoning_effort` regelt den Aufwand,
  der einer Übersetzung nichts bringt: Das gemessene Reasoning liegt bei null oder fast null.
- **Opus lehnt bestimmte biologische Inhalte ab.** Seine Schutzmechanismen sind
  strenger als die von Sonnet, und die Fehlermeldung von Anthropic weist darauf hin, dass sie
  „manchmal auch Arbeiten im Umfeld biologischer Forschung markieren können“. Gemessen: Eine Kurzmeldung
  über 279 generierte Moleküle führte dazu, dass der Artikel in allen vierzehn
  Sprachen abgelehnt wurde. Es wird nichts geschrieben: aipmt weist die abgeschnittene Antwort zurück, benennt die
  Schutzmechanismen und empfiehlt `--model sonnet`.
- In CI (`CI` oder `GITHUB_ACTIONS` gesetzt) und unter Windows (nicht gemessen) abgewiesen.
- Variablen: `AIPMT_CLAUDE_BIN` (sonst `PATH`, dann `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (Sekunden pro Segment, Standard 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (Standard 0.8), `CLAUDE_CONFIG_DIR` (das Konto von
  Claude Code, niemals aus einer projektbezogenen `.env` übernommen); Arbeitsverzeichnisse unter
  `XDG_CACHE_HOME/aipmt/claude-code` (Standard `~/.cache`).

**Nutzungsbedingungen: Sie tragen mit Ihrem Konto die Verantwortung.** Die
[Rechtliche Seite zu Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
hindert „Endnutzer nicht daran, sich mit ihrem eigenen Claude-Abonnement bei der unveränderten Claude-Code-Binärdatei
anzumelden“: Genau das tut aipmt, das die
offizielle Binärdatei startet und niemals das Token liest. Anthropic „gestattet
Drittentwicklern […] jedoch nicht, Anfragen im Namen ihrer Nutzer über Zugangsdaten für Free-, Pro- oder Max-Tarife
weiterzuleiten“, bevorzugt API-Schlüssel für
Drittanbieter-Tools, „einschließlich Open-Source-Projekten“, und behält sich vor, deren
Nutzung auf kostenpflichtige Guthaben anzurechnen
([Claude-Hilfe](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Kein Text klärt den Fall eines verbreiteten Tools, das die Binärdatei startet, abschließend.

**Daten**: Bei Free-, Pro- und Max-Konten gilt die Nutzung zum Modelltraining
auch für Claude Code, wenn die Datenschutzeinstellung dies erlaubt
([Datenseite](https://code.claude.com/docs/en/data-usage)). aipmt speichert
keine lokalen Transkripte (`--no-session-persistence`). Verarbeiten Sie damit
keine vertraulichen Inhalte.

### Zum Anbieter Ihrer Wahl: `--use_opencode`

[OpenCode](https://opencode.ai) ist ein Open-Source-Coding-Agent (MIT), der
Anfragen an die in ihm konfigurierten Anbieter weiterleitet: API-Schlüssel, Abonnement,
OpenCode-Zen-Gateway (kostenlose Modelle, ohne Konto) oder lokales Modell. Zwei
Zugangswege wurden hier vollständig gemessen: Zen und Ollama.

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

`--model` ist erforderlich: Ohne diese Angabe würde OpenCode auf ein kostenloses Modell zurückgreifen,
dessen Datenaustausch zum Training verwendet werden kann, und diese Entscheidung wird Ihnen nicht
abgenommen.

Abschottung bei jedem Aufruf:

- Eine Inline-Konfiguration, die Vorrang vor Ihrer eigenen hat, definiert einen Agenten `aipmt`,
  dessen sämtliche Tools gesperrt sind (`permission: { "*": "deny" }`), mit deaktivierter
  Sitzungsfreigabe, `--pure`, niemals `--auto`;
- leeres temporäres Arbeitsverzeichnis, `OPENCODE_DISABLE_PROJECT_CONFIG` und
  `OPENCODE_DISABLE_CLAUDE_CODE` gesetzt — ohne sie fügt OpenCode
  `AGENTS.md` aus dem aktuellen Verzeichnis und `~/.claude/CLAUDE.md` in den Prompt ein. Die
  globale `~/.config/opencode/AGENTS.md` wird weiterhin eingefügt; OpenCode erlaubt es nicht,
  sie auszuschließen;
- Ausgabevertrag: Rückgabecode 0, kein Ereignis `error`, kein
  Tool-Aufruf, letzter Schritt in `stop`, nicht leerer Text und tatsächlich geladener Agent `aipmt`
  — ein unbekannter `--agent` lässt OpenCode nicht fehlschlagen, sondern
  stillschweigend auf den Coding-Agenten zurückfallen;
- kein Schlüssel aus `aipmt` wird übergeben, außer `OPENCODE_API_KEY`, dem Schlüssel
  von OpenCode selbst. Anbieter werden in OpenCode konfiguriert, nicht in
  der `.env` von `aipmt`.

Wissenswertes:

- Die kostenlosen Modelle von Zen wechseln, ihre Grenzen sind nicht dokumentiert, und
  ihr Datenaustausch kann zum Training verwendet werden: geeignet für öffentliche
  Dokumentation, nicht für private Inhalte.
- Ein lokales Modell muss mindestens 16 k Tokens Kontext bieten, da die Segmente
  bis zu 16 000 Zeichen umfassen. Ollama konfiguriert oft 4 096: Verwenden Sie
  ein `Modelfile` mit `PARAMETER num_ctx 32768`.
- `--eco` hat keine Wirkung; `--reasoning_effort` wird unverändert als
  `--variant` an OpenCode übergeben.
- OpenCode protokolliert jede Sitzung in `~/.local/share/opencode/`.
- Variablen: `OPENCODE_BIN` (sonst `PATH`, dann `~/.opencode/bin/opencode`),
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

`reasoningEffort: "none"` deaktiviert das Reasoning, das Ollama bei diesen Modellen standardmäßig
aktiviert und das ein Modelfile nicht deaktivieren kann. Gemessen an einem Satz mit
sechs Wörtern: 919 Reasoning-Tokens und 68 Sekunden ohne die Option, 9 Tokens mit ihr.

### Zu mehr als 400 Modellen: `--use_openrouter`

OpenRouter ist ein nutzungsabhängig abgerechneter Router mit einem einzigen Guthaben für
Modelle, die von Drittanbietern gehostet werden — darunter offene chinesische Modelle, die hier kein
anderer Provider anbietet.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` ist erforderlich. Ein Preflight, der vor jeder Abrechnung ausgeführt wird, berücksichtigt
zwei Besonderheiten des Routings:

- **Dasselbe Modell wird von Dutzenden Hosting-Anbietern mit unterschiedlichen
  Obergrenzen bereitgestellt** — bei `z-ai/glm-5.3-flash` sind es 23 Hosting-Anbieter, darunter einer mit einer Grenze von
  2 048 Ausgabe-Tokens. Der Preflight liest `/api/v1/models/{modèle}/endpoints`,
  schließt Hosting-Anbieter mit weniger als 8 000 Ausgabe-Tokens oder eingeschränktem Status aus und
  legt die übrigen mit `allow_fallbacks: false` fest.
- **Reasoning wird zum Ausgabepreis abgerechnet** — 107 Tokens gegenüber 2 für
  eine Antwort „OK“ von `z-ai/glm-5.2`. Es ist standardmäßig deaktiviert; Modelle,
  die es erzwingen, erhalten den niedrigsten unterstützten Aufwand, da die Standardeinstellung des
  Katalogs die Ausgabe vor Abschluss der Übersetzung ausschöpfen kann.
  `--reasoning_effort` hat weiterhin Vorrang.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Das Kontextfenster stammt aus dem Katalog. Ein Modell mit weniger als 16 400 Tokens wird
  vor jedem Aufruf abgewiesen: 8 400 für Prompt und Segment, mindestens 8 000 für die
  Ausgabe.
- Ein nicht im Katalog vorhandener Slug, ein nicht erreichbarer Katalog oder das Fehlen
  eines Hosting-Anbieters, der die Obergrenze erfüllt, stoppen den Befehl.
- `finish_reason=length` mit leerer Ausgabe bedeutet, dass das Budget durch
  Reasoning verbraucht wurde, nicht dass die Ausgabe abgeschnitten wurde: Die Meldung unterscheidet dies.
- `--eco` hat keine Wirkung.
- Variablen: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (Standard `https://openrouter.ai/api/v1`, `https://`
  erforderlich), `OPENROUTER_TIMEOUT` (Standard 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (Standard 30).

### Übersetzungshinweis

`--add_translation_note` fügt einen Hinweis ein, als `bottom` (Standard), `top` (nach dem
Front Matter) oder `both` (`--note_position`), im Format `legacy` (fettgedruckter
Absatz, Standard) oder `marker` (`--note_format`). Das Format `marker` ist eine
unsichtbare Markdown-Referenzdefinition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
gefolgt von einem fettgedruckten Zitat: auf GitHub lesbar und beim Build durch ein
remark-Plugin auswertbar.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detaillierte Messungen

Alle Messungen beruhen auf tatsächlich mit `aipmt` ausgeführten Übersetzungen in
vierzehn Sprachen: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Geschrieben** zählt die Dateien, die die Schutzprüfungen bestanden haben; **Ohne
Abweichung** diejenigen, bei denen `scripts/compare_structure.py` nichts feststellt — dieselbe Anzahl
von Abschnitten, Zwischenüberschriften, Links, unterschiedlichen URLs, Codeblöcken,
Inline-Codes, Tabellenzeilen, Blockzitaten und fettgedruckten Wörtern.

„Ohne Abweichung“ bedeutet „nichts erkannt“, nicht „identisch“: Der Vergleicher
zählt Elemente, ohne ihren Inhalt zu lesen. Er meldet weder eine gelöschte Überschrift der
Ebene 4 noch ersetzten Inline-Code-Text, eine ausgetauschte
Flagge oder einen internen Link mit einer schließenden Klammer zu viel,
`[texte]((#ancre))`, der nirgendwo mehr hinführt — und er beurteilt nicht die
Sprache.

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

Grok wurde am 9. September mit einer anderen Ausgabe derselben Nachrichten
(356 Zeilen) erneut gemessen: 9 von 14 Sprachen geschrieben, 8 ohne Abweichung. Diese Zahl
steht in der Tabelle am Anfang. Drei abgebrochene Messreihen sind nicht
aufgeführt: `qwen3.5-27b` (9 Sprachen) und `kimi-k2.6` (4) wegen fehlenden Guthabens,
`z-ai/glm-5.3-flash`, dessen zwei Fehlschläge auf eine Reasoning-Einstellung zurückgingen,
die der Provider inzwischen korrigiert. Die OpenRouter-Zeilen wurden mit den
Standardeinstellungen des Routers vor `--use_openrouter` gemessen; `z-ai/glm-5.2`,
erneut mit dem ausgelieferten Provider gemessen, liefert dieselben 14/14. Die Zahlen wurden
am 10. September mit dem aktuellen Vergleicher neu berechnet: `qwen3.8-flash` und
`qwen3.7-flash` gewinnen gegenüber der ersten
Veröffentlichung jeweils eine Sprache hinzu, die übrigen bleiben unverändert.

Die Zeilen `--use_antigravity` wurden am 26. September mit demselben
Artikel gemessen, jeweils vier Übersetzungen parallel: `gemini-3.7-flash-medium` am Vormittag,
`gemini-3.8-flash-medium` am Nachmittag. Im Englischen entfernten beide selbst
die drei Zeilen der französischen Übersetzung unter den Zitaten, ohne eine
Flagge zu erfinden, und die englischen Zitate blieben unverändert: Die nachgeschaltete Bereinigung musste
nichts tun. In `--eco` (`gemini-3.7-flash-low`), mit nur vier Sprachen
(en, ja, ar, hi): 4 von 4 geschrieben, alle ohne Abweichung, bei einem Median von
1 min 52 s. Gegenprobe am selben Tag mit einer neueren Ausgabe der Nachrichten,
der vom 25. September (438 Zeilen, 2 englische Zitate), außerhalb des
Blogs mit `gemini-3.7-flash-medium` übersetzt: 14 von 14 geschrieben, alle ohne Abweichung, 87 bis
128 s pro Sprache.

Die Zeilen `--use_claude_code` wurden am 26. September mit demselben
Artikel gemessen, jeweils vier Übersetzungen parallel, mit dem Aufwand `low`. Bei `sonnet` bleiben die
englischen Zitate in allen vierzehn Sprachen unverändert, und im Englischen entfernte das
Modell selbst die Zeilen der französischen Übersetzung, ohne eine
Flagge zu erfinden. `opus` schrieb keine einzige Sprache: In jeder stoppten seine Schutzmechanismen
die Antwort beim letzten Segment wegen einer Kurzmeldung über 279 für eine Bindungsstelle
generierte Moleküle. Einzeln übermittelt wird diese Kurzmeldung
aufgrund der Kategorie „bio“ abgelehnt; `sonnet` übersetzte sie in alle Sprachen. `haiku` schreibt
alle vierzehn Sprachen; in dreien (en, pl, ro) wird eine Abschnittsüberschrift von
Ebene 2 auf Ebene 1 angehoben. Sein Reasoning lässt sich nicht unterbinden — 61 % seiner
Ausgabe-Tokens entfallen darauf —, weshalb es mehr als doppelt so lange braucht wie `sonnet`.

Die Zeilen `claude-sonnet-5-5`, `claude-haiku-5-5` und `claude-haiku-4-5` wurden
am 18. Oktober über die Anthropic-API mit demselben Artikel gemessen, jeweils vier
Übersetzungen parallel pro Modell. Sonnet 5.5 erlaubt es nicht, sein
Reasoning abzuschalten: aipmt sendet ihm die niedrigste unterstützte Einstellung, und seine
Antworten enthalten keines. Es schreibt alle vierzehn Sprachen ohne Abweichung und ohne
ein Segment erneut zu verarbeiten; im Englischen entfernte es selbst die Zeilen der
französischen Übersetzung, ohne eine Flagge zu erfinden, und die englischen Zitate bleiben
überall unverändert. Haiku 5.5 wird mit adaptivem Reasoning gemessen: Bei deaktiviertem
Reasoning ließ es ganze Absätze auf Französisch stehen, die die Schutzprüfung abweist —
3 von 14 Sprachen geschrieben. Beide Haiku-Modelle scheitern an derselben Kurzmeldung: Haiku 5.5
ändert die Ebene ihrer Überschrift oder dupliziert sie im Japanischen, Koreanischen und
Chinesischen; Haiku 4.5 hebt sie in sieben Sprachen auf Ebene 1 an und lässt sie
im Japanischen auf Französisch stehen. Haiku 4.5 kostet für beide Dokumente in allen
vierzehn Sprachen 3,67 $, Haiku 5.5 0,57 $, Sonnet 5.5 9,21 $.
### README dieses Projekts, Standard-Markdown

Stand vom 9. September 2026: 785 Zeilen, 285 Inline-Code-Elemente, 40
Blockabschlüsse, 89 Tabellenzeilen. Vier Übersetzungen parallel.

| Modell                                          | Geschrieben | Ohne Abweichung | Median/Sprache | Was abweicht                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | nichts                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | nichts                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | nichts laut Vergleichstool; interne Links verdoppelt (en)                   |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | nichts                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | nichts                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | ein fett gedrucktes Wort (ja)                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | ein fett gedrucktes Wort (ko)                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | eine Tabellenzeile mit der vorherigen zusammengezogen (ar)                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | ein Link (sv), ein fett gedrucktes Wort (zh)                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | ein fett gedrucktes Wort (ar, ja)                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | ein fett gedrucktes Wort (hi, ja, ko)                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 40 Inline-Code-Elemente im Arabischen hinzugefügt; Fettdruck (hi, ja, ko)                   |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2 Sprachen abgelehnt (ar, hi): Inline-Code-Elemente in der Rückgabe verloren        |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | ein Abschnitt verloren (ar, hi, ko); Codeblöcke hinzugefügt (ja, ko, ro, zh) |

Zwei abgebrochene Testreihen werden nicht bewertet: Grok, dessen CLI-Sitzung
nach zwölf Sprachen ablief (elf ohne Abweichung), und `qwen3.8-flash`, dessen
Hosting-Anbieter nach zwei Sprachen HTTP 429 zurückgab. `opencode/mimo-v2.5-free` und `ollama/gpt-oss-20b-32k`
wurden mit diesem Stand nicht erneut gemessen; mit dem um 277 Zeilen kürzeren
Stand vom 4. und 5. September schrieben sie jeweils 9 von 14 Übersetzungen, davon 7
beziehungsweise 1 ohne Abweichung.

Die Zeilen `--use_antigravity` und `--use_claude_code` wurden nicht mit dem
festgeschriebenen Stand gemessen, sondern am 26. September mit dem zusammen mit 1.14.0 veröffentlichten Stand — und
die Zeilen `claude-sonnet-5-5`, `claude-haiku-5-5` und `claude-haiku-4-5` am 18.
Oktober mit demselben Stand: 600 Zeilen, 257 Inline-Code-Elemente, 30 Blockabschlüsse, 85
Tabellenzeilen. Da dieser Stand
um 185 Zeilen kürzer ist, lässt er sich nicht unmittelbar mit den anderen Zeilen vergleichen;
diese Zeilen untereinander hingegen schon. Bei den internen Links, die das
Vergleichstool nicht prüft, hat `gemini-3.8-flash-medium` sie in
allen vierzehn Sprachen intakt gelassen, `gemini-3.7-flash-medium` hat sie im Italienischen beschädigt;
`sonnet` und `opus` haben sie überall intakt gelassen, `haiku` hat sie im
Englischen verdoppelt; `claude-sonnet-5-5` und `claude-haiku-4-5` haben sie in
allen vierzehn Sprachen intakt gelassen, `claude-haiku-5-5` in den zwölf Sprachen, die es geschrieben hat.

### Vier README-Dateien bekannter Projekte

FastAPI, Ollama, tldr-pages und Vue.js, unverändert von GitHub übernommen —
einfachere Dokumente als die beiden vorherigen. Die Testreihe zielte auf Modelle
mit Schwierigkeiten ab; Gemini dient dabei als Vergleichsmaßstab.

| Modell                    | Umfang                  | Geschrieben | Ohne Abweichung   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 Projekte × 14 Sprachen     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 Projekte × 14 Sprachen     | 55/56   | ❌ 47/56     |
| `grok-4.6` (Abonnement)   | 4 Projekte × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 Projekte × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### Was diese Messungen nicht sind

- **Keine vollständige Rangliste**: Allein OpenRouter bietet mehr als vierhundert
  Modelle an, etwa fünfzehn wurden gemessen.
- **Unverbindliche Zeitangaben**: je nach Testreihe drei bis sechs Übersetzungen
  parallel, und der Durchsatz eines Anbieters schwankt im Tagesverlauf.
- **Zeitgebundene Beobachtungen**: Modelle ändern sich unter demselben Namen, und Ihre
  Dokumente unterscheiden sich von unseren.

Um die Messung mit Ihren Dokumenten auf einer unveränderlichen Kopie der Datei zu wiederholen:

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
`REGEN_MODEL` ändern den Zugriffsweg: `antigravity` verwendet weiterhin ein Abonnement, das
von Google, und wird ohne Ausnahmegenehmigung zugelassen; eine kostenpflichtige API (`openai`, `gemini`,
`grok`, `openrouter`) wird ohne `REGEN_ALLOW_PAID_API=1` abgelehnt;
`REGEN_JOB_TIMEOUT` begrenzt jeden Job zeitlich (600 s, 1 800 s bei Codex und
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
Abschnitten 15 und 16 der GPL v3 verbreitet: Es wird „wie besehen“ bereitgestellt, ohne Gewährleistung der
Marktgängigkeit oder der Eignung für einen bestimmten Zweck, und sein Autor kann
nicht für Schäden haftbar gemacht werden, die aus seiner Nutzung entstehen. Der Text der
Lizenz hat Vorrang vor dieser Zusammenfassung.

- **Lesen Sie vor der Veröffentlichung Korrektur.** Die Schutzmechanismen erfassen Codeblöcke,
  Inline-Code, URLs, Anker und Zitate im Modus `--news` — weder
  Überschriften noch Tabellen, Front Matter oder den Sinn Ihrer Sätze.
- **Ihre Dokumente werden an den gewählten Anbieter übermittelt**, gemäß dessen
  Nutzungsbedingungen und Datenrichtlinien. Einige kostenlose Modelle können
  Ihre Unterhaltungen für das Training wiederverwenden, und die Bedingungen von Antigravity
  erlauben Google, sie wiederzuverwenden und von Menschen prüfen zu lassen,
  auch bei einem kostenpflichtigen Abonnement; ein lokales Modell ist der einzige Weg, bei dem
  keine Daten Ihren Rechner verlassen.
- **API-Aufrufe werden Ihnen in Rechnung gestellt.** Dieses Programm begrenzt die
  Ausgaben nicht: Ein langes Dokument, ein erneuter Versuch nach einem Fehler oder ein Modell, das viel nachdenkt,
  verursachen höhere Kosten.
- **Die veröffentlichten Messungen sind zeitgebundene Beobachtungen**, keine Garantien.

Die genannten Produkt- und Unternehmensnamen gehören ihren jeweiligen
Inhabern. Dieses Projekt ist mit keinem von ihnen verbunden.

**Artikel mit gpt-6.1-sol aus dem Französischen ins Deutsche übersetzt.**

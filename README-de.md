# AI-gestützter Markdown-Übersetzer

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Codequalität</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status des Quality Gates"></a>
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

Übersetzt Markdown-Dateien von einer Sprache in eine andere und bewahrt dabei
die Struktur: Codeblöcke, Inline-Code, URLs, Anker, Tabellen und Front
Matter. Elf Möglichkeiten, ein Modell aufzurufen – fünf APIs, vier Abonnements ohne
nutzungsabhängige Abrechnung, zwei Router – sowie eine veröffentlichte Messung dessen, was jedes
Modell tatsächlich bewahrt.

## Kurz gesagt

- **Elf Provider-Pfade**: APIs von OpenAI, Mistral, Claude, Gemini und Grok;
  Abonnements von ChatGPT (Codex), Grok, Google (Antigravity) und Claude (Claude
  Code) ohne nutzungsabhängige Abrechnung; Router OpenCode (Open Source, kostenlos oder lokal) und OpenRouter
  (mehr als 400 Modelle).
- **Keine fehlerhaften Ergebnisse wegen eines verlorenen Tokens**: Codeblöcke, Inline-Code,
  URLs, Anker und Zitate werden vor dem Aufruf durch Tokens ersetzt und
  nach der Rückgabe überprüft. Fehlt eines davon, wird die Datei nicht geschrieben.
- **Lange Dokumente**: Segmentierung entsprechend dem Kontextfenster des Modells.
- **Modus `--news`**: Englische Zitate werden geschützt und Kennzeichnungen
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

Die Schlüssel werden an drei Stellen gelesen, von der höchsten zur niedrigsten Priorität; jede
füllt nur aus, was die vorherige offengelassen hat.

|     | Wo                                            | Wofür                                |
| --- | --------------------------------------------- | ------------------------------------ |
| 1   | Umgebungsvariablen                            | CI, Container, punktuelle Ausnahme   |
| 2   | `.env` des aktuellen Verzeichnisses (oder eines übergeordneten Verzeichnisses) | ein projektspezifischer Schlüssel    |
| 3   | `~/.config/aipmt/.env`                        | einmal installiert, überall gültig   |

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

`GEMINI_API_KEY` wird anstelle von `GOOGLE_API_KEY` akzeptiert. Die Benutzerdatei folgt
`XDG_CONFIG_HOME` (nur absoluter Pfad) und unter Windows `%APPDATA%`.
Ohne Schlüssel listet der Befehl die drei Speicherorte auf.

**Die `.env` eines Projekts kann weder Aufrufe umleiten noch das ausgeführte
Programm auswählen.** Sie stellt Schlüssel bereit, niemals ein Ziel oder eine Binärdatei: Alle
Variablen in `_BASE_URL`, `_API_BASE`, `_ENDPOINT` oder `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, die Proxys (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), die Zertifikatsspeicher (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) sowie `XDG_CONFIG_HOME` /
`APPDATA` werden darin mit einer Warnung ignoriert. Ein geklontes Repository darf
weder Ihren Schlüssel abfangen noch Sie bei der ersten Übersetzung sein eigenes Programm
ausführen lassen. Diese Datei wird außerdem ohne Interpolation gelesen:
`NOM=${OPENAI_API_KEY}` kopiert den Schlüssel dort nicht hinein. Setzen Sie diese Variablen in
der Umgebung oder in `~/.config/aipmt/.env`.

Optionale Variablen: `XAI_BASE_URL` (Standard `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (Sekunden pro Aufruf, Standard 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(Standard 600), `GROK_BIN`, `GROK_HOME` (Standard `~/.grok`), `GROK_TIMEOUT`
(Standard 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (Standard 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (Standard 600), `OPENROUTER_BASE_URL`
(`https://` erforderlich), `OPENROUTER_TIMEOUT` (Standard 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (Standard 30). Jede wird im Abschnitt des jeweiligen
Providers ausführlich beschrieben.

## Erste Schritte

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` übersetzt ins Spanische und erzeugt `document-es.md` in `--target_dir`;
mit `--include_model` entsteht `document-es-gpt-5.6-terra.md`. Die Erweiterung wird
immer zu `.md` – `article.mdx` ergibt `article-en.md` – außer bei
`--keep_filename`, wodurch der ursprüngliche Name beibehalten wird. Eine bereits vorhandene
Übersetzung wird ohne `--force` übersprungen.

Exit-Codes: `0`, wenn alles erfolgreich war oder übersprungen wurde, `1`, wenn noch eine Datei
fehlgeschlagen ist (Liste in der Fehlerausgabe), `2`, wenn die Konfiguration die Ursache ist.
Eine fehlgeschlagene Datei wird niemals geschrieben, selbst wenn der Schreibvorgang selbst fehlschlägt:
Der Inhalt wird daneben geschrieben und anschließend umbenannt. Ein erneuter Aufruf genügt.

## Welches Modell wählen?

Gemessen anhand von zwei realen Dokumenten, die von jedem Modell in dieselben vierzehn Sprachen
übersetzt wurden. **Die Zahl gibt an, bei wie vielen der vierzehn Sprachen die
Übersetzung geschrieben wird und nichts von der Quelle abweicht.**

| Modell                | Zugriff                          | Dicht gepackter Monitoring-Artikel | Dieses README | Was abweicht und bei wie vielen Sprachen                                                                                                                            |
| --------------------- | -------------------------------- | ---------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.8 Flash**  | Google-Abonnement (Antigravity)  | ✅ 14/14                           | ✅ 14/14      | nichts, bei keinem der beiden Dokumente                                                                                                                             |
| **Claude Sonnet 5.5** | Anthropic-API-Schlüssel          | ✅ 14/14                           | ✅ 14/14      | nichts, bei keinem der beiden Dokumente                                                                                                                             |
| **Gemini 3.7 Flash**  | Google-API-Schlüssel             | ✅ 14/14                           | ⚠️ 13/14      | 1 von 14 Sprachen: ein zusätzliches fettgedrucktes Wort (ja)                                                                                                       |
| **Gemini 3.7 Flash**  | Google-Abonnement (Antigravity)  | ✅ 14/14                           | ⚠️ 13/14      | 1 von 14 Sprachen: ein fettgedrucktes Wort weniger (ko)                                                                                                             |
| **GPT-5.6 Sol**       | ChatGPT-Abonnement oder OpenAI-Schlüssel | ✅ 14/14                    | ⚠️ 12/14      | 2 von 14 Sprachen: ein fettgedrucktes Wort weniger (ar, ja)                                                                                                        |
| **GLM-5.2**           | OpenRouter-Schlüssel             | ✅ 14/14                           | ⚠️ 11/14      | 3 von 14 Sprachen: ein fettgedrucktes Wort weniger (hi, ja, ko)                                                                                                    |
| Claude Sonnet 5       | Claude-Abonnement (Claude Code)  | ⚠️ 13/14                           | ⚠️ 13/14      | 1 von 14 Sprachen beim Artikel: ein zusätzliches fettgedrucktes Wort (zh); 1 bei diesem README: eine Tabellenzeile an die vorherige angehängt und bei der Anzeige verborgen (ar) |
| Claude Haiku 4.5      | Claude-Abonnement (Claude Code)  | ⚠️ 11/14                           | ✅ 14/14      | 3 Sprachen beim Artikel: eine Abschnittsüberschrift wurde zu Ebene 1 (en, pl, ro); bei diesem README nichts für den Vergleicher, aber die internen Links wurden im Englischen verdoppelt |
| Claude Sonnet 5       | Anthropic-API-Schlüssel          | ⚠️ 11/14                           | ⚠️ 12/14      | 3 Sprachen beim Artikel: ein Codeblock ist hinzugekommen (es, de, hi); 2 bei diesem README: ein Link ohne seine Auszeichnung (sv), ein fettgedrucktes Wort (zh)     |
| Claude Haiku 4.5      | Anthropic-API-Schlüssel          | ⚠️ 7/14                            | ✅ 14/14      | 7 Sprachen beim Artikel: eine Abschnittsüberschrift wurde zu Ebene 1 – auf Japanisch blieb sie auf Französisch; nichts bei diesem README                            |
| Claude Haiku 5.5      | Anthropic-API-Schlüssel          | ⚠️ 11/14                           | ❌ 12/14      | 3 Sprachen beim Artikel: eine Abschnittsüberschrift änderte ihre Ebene oder wurde dupliziert (ja, ko, zh); bei diesem README wurden 2 Sprachen abgelehnt und Inline-Codes gingen verloren (ar, hi) |
| Qwen 3.7 Flash        | OpenRouter-Schlüssel             | ❌ 8/14                            | ⚠️ 10/14      | 1 Sprache beim Artikel abgelehnt, 5 weitere weichen ab; bei diesem README wurden etwa vierzig Wörter in `code` gesetzt (ar)                                 |
| Grok 4.6              | Grok-Abonnement                  | ❌ 8/14                            | nicht bewertet | 5 von 14 Sprachen abgelehnt, weil Inline-Codes und URLs nicht zurückgegeben wurden; das Niederländische weicht vollständig ab                                     |
| GPT-OSS 20B           | lokales Modell (Ollama)          | ❌ 7/14                            | nicht erneut gemessen | 4 von 14 Sprachen abgelehnt: Das Modell ließ dort französische Passagen stehen, die Schutzprüfung stoppte sie                                                |
| MiMo v2.5 (kostenlos) | OpenCode Zen, ohne Konto         | ❌ 11/14                           | nicht erneut gemessen | 1 Sprache abgelehnt; ein Abschnitt ging im Polnischen verloren                                                                                              |
| Mistral Large         | Mistral-API-Schlüssel            | ❌ 5/14                            | ❌ 1/14       | **ein ganzer Abschnitt verschwindet**: 1 Sprache beim Artikel (hi), 3 bei diesem README (ar, hi, ko) – außerdem 3 beim Artikel abgelehnte Sprachen                  |
| DeepSeek V4 Flash     | OpenRouter-Schlüssel             | ❌ 3/14                            | nicht erneut gemessen | 10 von 14 Sprachen abgelehnt; 37 Minuten pro Sprache                                                                                                        |
| Claude Opus 5.5       | Claude-Abonnement (Claude Code)  | ❌ 0/14                            | ✅ 14/14      | Der Artikel wurde aufgrund einer kurzen Biologiemeldung in allen 14 Sprachen von Opus' Schutzmechanismen abgelehnt; nichts bei diesem README                       |

|     | Bedeutung des Symbols                                                                                                                                                                                    |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alle vierzehn Sprachen übersetzt und keinerlei Abweichung von der Quelle                                                                                                                                  |
| ⚠️  | alle vierzehn Sprachen übersetzt; die Abweichungen betreffen die **Auszeichnung** – ein fettgedrucktes Wort, ein `code`, ein Link, der seine Klammern verliert. Kein Text, keine URL, kein Codeblock und kein Abschnitt fehlt |
| ❌  | Mindestens eine Sprache konnte nicht übersetzt werden – die Datei wird abgelehnt und nicht geschrieben – **oder** in einer geschriebenen Datei fehlt Inhalt                                                |

Das Wichtigste daraus:

- **Eine abgelehnte Übersetzung ist keine beschädigte Übersetzung.** Wenn bei der Rückgabe ein Token
  fehlt, wird die Datei nicht geschrieben und die Sprache gilt als
  abgelehnt. Genau das geschieht bei Grok mit dem Artikel: Vier Inline-Codes und
  drei URLs gehen bereits im ersten Segment bei den fünf nicht lateinischen Schriften verloren.
- **Ein Modell kann wegen eines einzigen Satzes ein ganzes Dokument ablehnen.** Opus 5.5
  übersetzt dieses README ohne jede Abweichung, aber keinen einzigen Monitoring-Artikel: Seine
  Schutzmechanismen stoppen die Antwort bei einer kurzen Biologiemeldung. Die Datei wird
  nicht geschrieben, und aipmt erklärt, warum.
- **Dieses Sicherheitsnetz deckt Überschriften, Tabellen, Front Matter und
  Text nicht ab.** Ein Modell, das einen Abschnitt entfernt, liefert eine Datei zurück, die das Tool
  ohne Beanstandung schreibt – das ist bei Mistral der Fall. Diese Elemente lassen sich nicht
  durch ein Token ersetzen, und die aktuellen Prüfungen kontrollieren sie nicht;
  `scripts/compare_structure.py` erkennt einen verlorenen Abschnitt, aber erst im Nachhinein.
- **Grok hat für dieses README keine Bewertung**: Seine CLI-Sitzung lief nach zwölf
  Sprachen ab, von denen elf keine Abweichung aufwiesen. Eine unterbrochene Testkampagne wird nicht bewertet.
- **Die Dichte des Dokuments ist wichtiger als die Sprache.** Grok kommt mit gewöhnlichen
  README-Dateien zurecht und scheitert an einem Artikel mit vielen Links, auch auf
  Niederländisch.

Daten und Dokumente: Die Spalte „Dieses README“ wurde am 9. September 2026
anhand einer fixierten Revision dieser Datei gemessen (785 Zeilen, 285 Inline-Codes, 89
Tabellenzeilen), die seitdem überarbeitet wurde – mit Ausnahme der Zeilen zu Antigravity und Claude Code,
die am 26. September anhand der mit Version 1.14.0 veröffentlichten, kürzeren Revision
gemessen wurden (600 Zeilen, 257 Inline-Codes, 85 Tabellenzeilen), sowie der über die API
gemessenen Zeilen zu Claude Sonnet 5.5, Haiku 5.5 und Haiku 4.5, die am 18. Oktober anhand
derselben Revision gemessen wurden. Die Spalte „Dicht gepackter Monitoring-Artikel“ stammt aus der Testkampagne vom
4. und 5. September mit einem 589 Zeilen langen Artikel, ausgenommen die Grok-Zeile, die am
9. September anhand einer anderen Ausgabe desselben Monitoring-Artikels erneut gemessen wurde, die Zeilen zu Antigravity und
Claude Code, die am 26. September anhand desselben Artikels gemessen wurden, sowie diese drei
Claude-Zeilen vom 18. Oktober. Die vollständigen Tabellen, Laufzeiten und das Protokoll stehen
unter [Detaillierte Messungen](#detaillierte-messungen).
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
| `--use_antigravity`      | Antigravity CLI (`agy`) mit dem Kontingent des Google-AI-Pro- oder -Ultra-Abonnements verwenden                       |
| `--use_claude_code`      | Claude Code CLI (`claude -p`) mit dem Kontingent des Claude-Pro- oder -Max-Abonnements verwenden                      |
| `--use_opencode`         | OpenCode (Open Source) mit dem in OpenCode konfigurierten Anbieter verwenden; erfordert `--model provider/modèle` |
| `--use_openrouter`       | OpenRouter verwenden — erfordert `OPENROUTER_API_KEY` und `--model fournisseur/modèle`                          |
| `--force`                | Erneute Übersetzung erzwingen                                                                                       |
| `--keep_filename`        | Ursprünglichen Dateinamen beibehalten                                                                          |
| `--news`                 | Nachrichtenmodus: schützt englische Zitate und verwaltet Kennzeichnungen nach Sprache                                      |
| `--add_translation_note` | Übersetzungshinweis hinzufügen                                                                                |
| `--note_position`        | Position des Hinweises: `top`, `bottom` (Standard) oder `both`                                                     |
| `--note_format`          | Format des Hinweises: `legacy` (Standard, fett gesetzter Absatz) oder `marker`                                            |
| `--include_model`        | Modellnamen in die Ausgabedatei aufnehmen                                                            |
| `--reasoning_effort`     | GPT-5.x-Reasoning-Aufwand: `none`/`low`/`medium`/`high`/`xhigh`                                         |

Die neun `--use_*`-Flags schließen sich gegenseitig aus: Werden zwei davon
kombiniert, wird dies abgelehnt.

## Anbieter

### Per API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` wechselt bei jedem Anbieter zur kostengünstigen Stufe.

| Anbieter    | Qualität (Standard)                                      | Kostengünstig (`--eco`)      |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                   | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol` (auch `terra` und `luna` über `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, Aufwand `low`                                | identisch — `--eco` ohne Wirkung |
| OpenCode    | `--model provider/modèle` erforderlich                 | identisch — `--eco` ohne Wirkung |
| OpenRouter  | `--model fournisseur/modèle` erforderlich              | identisch — `--eco` ohne Wirkung |

### Mit dem ChatGPT-Abonnement: `--use_codex`

Steuert das offizielle Codex CLI: Die Übersetzung wird vom Kontingent des
ChatGPT-Abonnements abgezogen, ohne API-Schlüssel oder nutzungsabhängige Abrechnung.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Die Binärdatei wird in `CODEX_BIN`, dann im `PATH` und anschließend im Package
  `openai-codex-cli-bin` gesucht. `~/.codex/auth.json` wird niemals gelesen.
- `OPENAI_API_KEY` und `CODEX_API_KEY` werden aus der Umgebung des
  Unterprozesses entfernt: Ein vorhandener Schlüssel führt niemals zu einem Wechsel zur API.
- Jedes Segment kostet mindestens eine „Nachricht“ des 5-Stunden-Fensters — zwei,
  wenn seine Validierung fehlschlägt und es erneut versucht wird. OpenAI nennt als
  Schätzung 250–2.000 Nachrichten/5 h für `gpt-5.6-luna` (`--eco`) und
  10–100 für `gpt-5.6-sol` mit einem Plus-Tarif.
- `--model gpt-5.6-terra` und `--model gpt-5.6-luna` laufen ebenfalls über
  das Abonnement. Ein Modell, für das das Konto nicht berechtigt ist, gibt einen 400-Fehler „model is
  not supported when using Codex with a ChatGPT account“ zurück.
- Langsamer als eine API, wobei der Unterschied mit der Dokumentlänge wächst: bei diesem README
  im Median 6 min 46 s pro Sprache mit `gpt-5.6-sol`, gegenüber 36 s mit
  `gemini-3.7-flash`.
- In CI abgelehnt (`CI` oder `GITHUB_ACTIONS` definiert): Das Abonnement authentifiziert sich
  über eine persönliche Sitzungsdatei, die auf einem gemeinsam genutzten Runner nichts
  zu suchen hat.
- Variablen: `CODEX_BIN`, `CODEX_TIMEOUT` (Sekunden pro Segment, Standard 600).

### Mit dem Grok-Abonnement: `--use_grok_cli`

Dasselbe Prinzip mit dem offiziellen Grok Build CLI und dem SuperGrok- oder
X-Premium+-Abonnement.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Schwächere Isolation als bei Codex.** Die OS-Sandbox von Grok greift
  auf vielen aktuellen Linux-Systemen nicht (AppArmor, Sockets der
  Container-Runtime), und ein Profil, das nicht angewendet werden kann, startet stillschweigend
  ohne Isolation. Das Skript fordert daher standardmäßig kein Profil an, weist darauf hin und
  stützt sich auf die `--deny`-Regeln des CLI einschließlich des Catch-all `*` — die einzige
  Schicht, die den Start verweigert, statt den Schutz unangekündigt zu
  entfernen. `GROK_TRANSLATE_SANDBOX=read-only` erzwingt die OS-Sandbox, und der Start
  schlägt fehl, wenn das System sie nicht gewährleisten kann.
- Das Kontingent gilt wöchentlich, wird mit Chat, Imagine und Voice geteilt, und kein
  Befehl kann es auslesen: Ein Batch kann die Nutzung für Unterhaltungen
  ohne Warnsignal beeinträchtigen.
- Variablen: `GROK_BIN`, `GROK_HOME` (CLI-Verzeichnis, Standard `~/.grok`),
  `GROK_TIMEOUT` (Standard 900), `GROK_TRANSLATE_SANDBOX`.

### Mit dem Google-Abonnement: `--use_antigravity`

Dasselbe Prinzip mit `agy`, dem offiziellen Antigravity CLI: Wer Google
AI Pro oder Ultra bezahlt, kann die Übersetzung vom Kontingent des Abonnements abziehen lassen,
anstatt sie nach Tokens abzurechnen. Dies ist der einzige Weg zu diesem Kontingent: Gemini CLI
bedient diese Konten seit dem 18. Juni 2026 nicht mehr
([Ankündigung](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
und das Antigravity SDK akzeptiert nur einen API-Schlüssel oder ein Google-Cloud-Projekt.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Kein kostenpflichtiger Weg bleibt offen.** agy erhält aus Ihrer
  Umgebung nur eine feste Liste von Variablen — `PATH`, Sprache und Zeitzone,
  Terminal, Identität, Proxys und Zertifikate, Sitzungsbus — und keinen Schlüssel:
  Mehrere seiner Variablen leiten einen Aufruf ohne Anzeige um (gemessen:
  Eine sendet das Dokument an ein Drittanbieter-Gateway, eine andere an ein
  kostenpflichtiges Google-Cloud-Projekt), und bei jeder erneuten Prüfung fehlten Einträge
  in einer Sperrliste. Vor jedem Segment muss `agy -p /config`, das kein Kontingent
  verbraucht, anzeigen, dass kostenpflichtige KI-Guthaben deaktiviert sind und weder
  ein API-Schlüssel noch ein Google-Cloud-Projekt vorhanden ist — eine fehlende
  Einstellung führt zur Ablehnung —, andernfalls wird nichts übersetzt; anschließend muss das
  Protokoll jedes Aufrufs das Abonnement bestätigen (`authMethod=consumer`), andernfalls wird die
  Antwort abgelehnt.
- **Isolation.** Jeder Aufruf läuft in einem privaten, temporären Home-Verzeichnis
  mit einem Übersetzungsagenten ohne Tools: Ihre Einstellungen, Regeln,
  Plugins, MCP-Server und agy-Hooks gelangen nicht dorthin, Ihrem
  Verlauf wird nichts hinzugefügt, und die Anmeldung verbleibt im Schlüsselbund, den aipmt niemals liest.
  Wird ein Agent nicht gefunden, fällt agy stillschweigend auf seinen Coding-Agenten
  und dessen Tools zurück: Eine vollständige Protokollzeile muss den richtigen Agenten bestätigen — ein
  Dokument, das diese Meldung zitiert, ersetzt sie nicht —, andernfalls erfolgt eine Ablehnung.
- **Plattformen**: Linux in einer Sitzung mit Schlüsselbund (D-Bus-Sitzungsbus,
  Secret Service); macOS wird akzeptiert, wurde dort jedoch nicht gemessen. Unter
  Windows wird der Vorgang abgelehnt, da agy die Variablen zur Isolation der einzelnen Aufrufe nicht liest,
  ebenso unter Linux ohne Sitzungsbus — SSH-Sitzung, Container, Server: Dort
  speichert agy sein Token in einer Datei unter `~/.gemini`, die durch die Isolation verborgen wird. Die
  Ablehnung erfolgt noch vor jedem Start mit Angabe des Grundes, statt eine Minute
  auf einen Anmeldecode zu warten.
- **Modelle**: diejenigen von `agy models`. Bei den Gemini-Modellen ist der Aufwand im Namen enthalten
  (`gemini-3.8-flash-medium`…): Ein Name ohne Suffix wird vor dem Aufruf abgelehnt,
  und `--reasoning_effort` hat keine Wirkung. Standardmäßig `gemini-3.8-flash-medium`
  und `gemini-3.7-flash-low` mit `--eco`; die Kampagnen, die zu ihrer Festlegung führten, werden
  unter [Detaillierte Messungen](#detaillierte-messungen) beschrieben. Claude und GPT-OSS
  verfügen über ein eigenes, deutlich kleineres Kontingent: ungefähr 1 % des
  5-Stunden-Fensters pro gemessenem Aufruf gegenüber 0,05 % bei Flash.
- **Kontingent**: Pro Gruppe gibt es ein 5-Stunden- und ein Wochenfenster,
  anteilig nach Token-Kosten. Gemessen mit dem Konto des Autors: ungefähr
  16 Punkte des 5-Stunden-Fensters pro Million Quellzeichen mit
  `gemini-3.8-flash-medium`, 14 mit `gemini-3.7-flash-medium` und 7 bis 8 bei
  niedrigem Aufwand — ein README mit 40.000 Zeichen kostet somit etwas mehr als einen
  halben Punkt. Das Wochenlimit hängt hingegen von der Stufe ab. Wiederholungsversuche richten sich
  danach, was agy als wiederholbar ausweist; andernfalls wird nach Ausschöpfung eines Fensters
  niemals erneut versucht: Jede Datei schlägt dann bis zu dem von
  `/usage` angezeigten Zurücksetzen fehl.
- **Langsamer als die API**: Beim inhaltsreichen Messartikel im Median 3 min 59 s pro
  Sprache mit `gemini-3.8-flash-medium` und 3 min 14 s mit
  `gemini-3.7-flash-medium`, gegenüber 1 min 18 s für Gemini 3.7 Flash über die API.
- **Unterbrechung**: Strg-C oder das Schließen des Terminals beenden agy zusammen mit dem
  Befehl, statt es seinen Durchlauf auf Kosten Ihres Kontingents abschließen zu lassen; dasselbe gilt
  für Codex, Grok CLI und OpenCode. Unter `nohup` läuft die Übersetzung weiter.
- In CI abgelehnt (`CI` oder `GITHUB_ACTIONS` definiert): Die Anmeldung befindet sich in einem
  persönlichen Schlüsselbund. Auf einem Runner: `--use_gemini` mit `GOOGLE_API_KEY`.
- Variablen: `AGY_BIN` (andernfalls `PATH`, dann `~/.local/bin/agy`),
  `AGY_TIMEOUT` (Sekunden pro Segment einschließlich Start, Standard 900).

**Nutzungsbedingungen: Es geht um Ihr Konto.** Die
[Antigravity-Nutzungsbedingungen](https://antigravity.google/terms) (Abschnitt 6) und die
[FAQ](https://antigravity.google/docs/faq/) verbieten den Zugriff auf den Dienst
durch Drittsoftware mithilfe der Antigravity-Anmeldung — Claude Code,
OpenClaw und OpenCode werden dort genannt —; bei Verstößen droht die Sperrung des Kontos. aipmt
liest das Token weder aus noch verwendet es erneut: Es startet die offizielle Binärdatei im
[Headless-Modus](https://antigravity.google/docs/cli/headless/), den Google
für Skripte und CI dokumentiert. Ein Google-Mitarbeiter bezeichnete es als „üblich“,
`agy -p` aus einem lokalen Skript für die eigene Arbeit zu starten
([offizielles Forum, 25. September 2026, unverbindliche Antwort](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
kein Text klärt den Fall eines wie dieses vertriebenen Tools.

**Nur öffentliche Dokumente.** Gemäß Abschnitt 5 derselben Bedingungen können die
Interaktionen — Prompts, Antworten, Metadaten — zur Verbesserung der
Produkte und des maschinellen Lernens von Google verwendet und von
Menschen überprüft werden, auch bei einem kostenpflichtigen Abonnement. Der Ausschluss erfolgt über die Einstellung
`enableTelemetry`, deren Wirkung nicht dokumentiert ist und die aipmt nicht setzt; Ihre
agy-Einstellungen werden nicht in dessen isolierte Umgebung übernommen. Leiten Sie darüber keine vertraulichen Inhalte weiter.
### Zum Claude-Abonnement: `--use_claude_code`

Dasselbe Prinzip gilt mit `claude`, dem offiziellen CLI von Claude Code, im Modus `-p`: Wer
Claude Pro oder Max bezahlt, dessen Übersetzung wird vom Kontingent des
Abonnements abgezogen, statt nach Tokens abgerechnet zu werden. Nicht zu verwechseln mit
`--use_claude`, der nutzungsbasiert abgerechneten API von Anthropic.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Kein kostenpflichtiger Weg bleibt offen, und jeder Aufruf weist dies nach.** Claude
  Code erhält aus Ihrer Umgebung nur eine geschlossene Liste von Variablen — weder
  API-Schlüssel noch Token, Cloud-Anbieter oder Kennzeichnung der Claude-Code-Sitzung,
  aus der aipmt gestartet würde. Vor dem ersten Segment muss `claude auth status`
  die Abonnementverbindung ohne Console-Schlüssel anzeigen, und `/usage`, das kein
  Kontingent verbraucht, muss dies bestätigen; jeder Aufruf bestätigt es wiederum in seinem
  Initialisierungsereignis, andernfalls wird die Antwort abgelehnt.
- **Deaktivieren Sie „extra usage“** (claude.ai, Einstellungen → Nutzung), damit
  es bei null Euro bleibt: Ist es aktiviert, übernimmt es bei einem ausgeschöpften Zeitfenster und
  stellt Kosten in Rechnung, ohne einen Fehler anzuzeigen. aipmt beendet die Übersetzung, sobald die
  Kontingentanzeige eines Aufrufs dies meldet, doch dieser Aufruf wurde dann bereits berechnet.
- **Mit Ihren Claude-Code-Sitzungen geteiltes Kontingent.** Jeder Aufruf meldet
  die Auslastung der 5-Stunden- und Wochenfenster; oberhalb von 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) wird kein weiteres Segment gestartet, damit
  das für Ihre Arbeit benötigte Kontingent nicht aufgebraucht wird.
- **Isolation.** Jeder Aufruf läuft ohne Tool, in einem privaten und
  temporären Verzeichnis, im Modus ohne Personalisierung: Weder Ihre `CLAUDE.md` noch Ihre Plugins,
  Hooks, MCP-Server oder Einstellungen werden geladen, und aus der
  Sitzung wird nichts gespeichert. Anhänge sind deaktiviert: Ein `@chemin` in Ihrem Dokument
  bleibt Text und öffnet keine Datei (gemessen).
- **Modelle**: Standardmäßig `sonnet`, mit dem Aufwand `low`, ebenso bei `--eco`:
  `--eco` ändert auf diesem Weg nichts. An denselben Dokumenten gemessen ist `haiku`
  doppelt so langsam — es führt Reasoning aus, ohne dass man es daran hindern kann — bei
  nur geringfügig niedrigeren Kosten, und `opus` lehnt biologische Inhalte ab (siehe
  nächsten Punkt). Beide bleiben über `--model` erreichbar; diese Aliasse folgen dem
  neuesten Modell ihrer Familie. `fable` und die Varianten `[1m]` werden abgelehnt,
  weil sie kostenpflichtige Credits verwenden. `--reasoning_effort` legt den Aufwand fest,
  von dem eine Übersetzung nicht profitiert: Das gemessene Reasoning ist null oder nahezu null.
- **Opus lehnt bestimmte biologische Inhalte ab.** Seine Schutzmechanismen sind
  strenger als die von Sonnet, und die Fehlermeldung von Anthropic warnt davor, dass sie
  „manchmal Arbeiten kennzeichnen können, die an biologische Forschung angrenzen“. Gemessen: Eine Kurzmeldung
  über 279 erzeugte Moleküle führte dazu, dass der Artikel in allen vierzehn
  Sprachen abgelehnt wurde. Nichts wird geschrieben: aipmt lehnt die abgebrochene
  Antwort ab, nennt die Schutzmechanismen und empfiehlt `--model sonnet`.
- In CI (`CI` oder `GITHUB_ACTIONS` definiert) und unter Windows abgelehnt (nicht gemessen).
- Variablen: `AIPMT_CLAUDE_BIN` (andernfalls `PATH`, dann `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (Sekunden pro Segment, Standardwert 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (Standardwert 0.8), `CLAUDE_CONFIG_DIR` (das Konto von
  Claude Code, niemals aus einem `.env` des Projekts übernommen); Arbeitsverzeichnisse unter
  `XDG_CACHE_HOME/aipmt/claude-code` (Standardwert `~/.cache`).

**Nutzungsbedingungen: Ihr Konto ist davon betroffen.** Die
[Rechtsseite von Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
hindert „einen Endnutzer nicht daran, sich mit seinem eigenen Claude-Abonnement
bei der unveränderten Claude-Code-Binärdatei anzumelden“: Genau das tut aipmt, indem es die
offizielle Binärdatei startet und das Token niemals liest. Anthropic „gestattet
Drittentwicklern jedoch nicht, […] Anfragen im Namen ihrer Nutzer über
Zugangsdaten von Free-, Pro- oder Max-Tarifen weiterzuleiten“, bevorzugt für
Drittanbieter-Tools den API-Schlüssel, „einschließlich Open-Source-Projekten“,
und behält sich vor, deren Nutzung von kostenpflichtigen Credits abzuziehen
([Claude-Hilfe](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Kein Text klärt den Fall eines vertriebenen Tools, das die Binärdatei startet.

**Daten**: Bei Free-, Pro- und Max-Konten gilt das Modelltraining
auch für Claude Code, wenn die Datenschutzeinstellung dies erlaubt
([Datenseite](https://code.claude.com/docs/en/data-usage)). aipmt speichert
keine lokale Transkription (`--no-session-persistence`). Lassen Sie darüber
keine vertraulichen Inhalte laufen.

### Zum Anbieter Ihrer Wahl: `--use_opencode`

[OpenCode](https://opencode.ai) ist ein Open-Source-Code-Agent (MIT), der
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

`--model` ist obligatorisch: Ohne diese Angabe würde OpenCode auf ein kostenloses Modell
zurückfallen, dessen Interaktionen möglicherweise zum Training verwendet werden, und diese Wahl wird Ihnen nicht
abgenommen.

Isolation bei jedem Aufruf:

- Eine Inline-Konfiguration mit Vorrang vor Ihrer eigenen definiert einen Agenten `aipmt`,
  für den alle Tools abgelehnt werden (`permission: { "*": "deny" }`), das Teilen der
  Sitzung deaktiviert ist, `--pure`, niemals `--auto`;
- temporäres und leeres Arbeitsverzeichnis, `OPENCODE_DISABLE_PROJECT_CONFIG` und
  `OPENCODE_DISABLE_CLAUDE_CODE` gesetzt — ohne sie fügt OpenCode dem
  Prompt die `AGENTS.md` des aktuellen Verzeichnisses und `~/.claude/CLAUDE.md` hinzu. Die
  globale `~/.config/opencode/AGENTS.md` bleibt enthalten; OpenCode erlaubt nicht,
  sie auszuschließen;
- Ausgabevertrag: Rückgabecode 0, kein Ereignis `error`, kein
  Tool-Aufruf, letzter Schritt in `stop`, nicht leerer Text und der Agent `aipmt`
  tatsächlich geladen — ein unbekannter `--agent` lässt OpenCode nicht fehlschlagen, sondern
  bewirkt einen stillen Rückfall auf den Coding-Agenten;
- Kein Schlüssel von `aipmt` wird übermittelt, außer `OPENCODE_API_KEY`, dem Schlüssel
  von OpenCode selbst. Die Anbieter werden in OpenCode konfiguriert, nicht in
  `.env` von `aipmt`.

Wissenswertes:

- Die kostenlosen Zen-Modelle wechseln, ihre Limits sind nicht dokumentiert, und
  ihre Interaktionen können zum Training verwendet werden: geeignet für öffentliche
  Dokumentation, nicht für private Inhalte.
- Ein lokales Modell muss mindestens 16 k Tokens Kontext bieten, da die Segmente
  bis zu 16.000 Zeichen umfassen. Ollama konfiguriert häufig 4.096: Verwenden Sie
  ein `Modelfile` mit `PARAMETER num_ctx 32768`.
- `--eco` hat keine Wirkung; `--reasoning_effort` wird unverändert als
  `--variant` von OpenCode übermittelt.
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

`reasoningEffort: "none"` deaktiviert das Reasoning, das Ollama bei diesen
Modellen standardmäßig aktiviert und das sich mit einem Modelfile nicht deaktivieren lässt. Gemessen an einem Satz mit
sechs Wörtern: 919 Reasoning-Tokens und 68 Sekunden ohne die Option, 9 Tokens mit ihr.

### Zu mehr als 400 Modellen: `--use_openrouter`

OpenRouter ist ein nutzungsbasiert abgerechneter Router mit einem einzigen Guthaben vor
von Drittanbietern gehosteten Modellen — darunter offene chinesische Modelle, die kein
anderer Anbieter hier verfügbar macht.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` ist obligatorisch. Ein vor jeder Abrechnung ausgeführter Preflight regelt
zwei Besonderheiten des Routings:

- **Dasselbe Modell wird von Dutzenden Hostern mit unterschiedlichen
  Obergrenzen bereitgestellt** — bei `z-ai/glm-5.3-flash` sind es 23 Hoster, darunter einer mit einer
  Obergrenze von 2.048 Ausgabe-Tokens. Der Preflight liest `/api/v1/models/{modèle}/endpoints`,
  schließt Hoster mit weniger als 8.000 Ausgabe-Tokens oder beeinträchtigtem Status aus und
  fixiert die übrigen mit `allow_fallbacks: false`.
- **Reasoning wird zum Ausgabetarif abgerechnet** — 107 Tokens gegenüber 2 bei
  einer „OK“-Antwort von `z-ai/glm-5.2`. Es ist standardmäßig deaktiviert; Modelle,
  die es erzwingen, erhalten den niedrigsten von ihnen akzeptierten Aufwand, da die
  Katalogvorgabe die Ausgabe vor Abschluss der Übersetzung ausschöpfen kann.
  `--reasoning_effort` hat weiterhin Vorrang.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Das Kontextfenster stammt aus dem Katalog. Ein Modell mit weniger als 16.400 Tokens wird
  vor jedem Aufruf abgelehnt: 8.400 für Prompt und Segment, mindestens 8.000 für die Ausgabe.
- Ein im Katalog fehlender Slug, ein nicht erreichbarer Katalog oder das Fehlen
  eines Hosters, der die Obergrenze einhält, beendet den Befehl.
- `finish_reason=length` mit leerer Ausgabe ist ein durch
  Reasoning verbrauchtes Budget und keine Trunkierung: Die Meldung unterscheidet beides.
- `--eco` hat keine Wirkung.
- Variablen: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (Standardwert `https://openrouter.ai/api/v1`, `https://`
  erforderlich), `OPENROUTER_TIMEOUT` (Standardwert 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (Standardwert 30).

### Übersetzungshinweis

`--add_translation_note` fügt einen Hinweis hinzu, in `bottom` (Standardwert), `top` (nach dem
Front Matter) oder `both` (`--note_position`), im Format `legacy` (fett gesetzter
Absatz, Standardwert) oder `marker` (`--note_format`). Das Format `marker` ist eine
unsichtbare Markdown-Referenzdefinition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
gefolgt von einem fett gesetzten Zitat: auf GitHub lesbar und beim Build durch ein
remark-Plugin nutzbar.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detaillierte Messungen

Alle Messungen sind tatsächlich mit `aipmt` ausgeführte Übersetzungen in
vierzehn Sprachen: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Geschrieben** zählt die Dateien, welche die Prüfmechanismen passieren ließen; **Ohne
Abweichung** diejenigen, bei denen `scripts/compare_structure.py` nichts feststellt — dieselbe Anzahl an
Abschnitten, Zwischenüberschriften, Links, eindeutigen URLs, Codeblöcken,
Inline-Code-Elementen, Tabellenzeilen, Zitatblöcken und fett gesetzten Wörtern.

„Ohne Abweichung“ bedeutet „nichts erkannt“, nicht „identisch“: Der Vergleicher
zählt Elemente, ohne ihren Inhalt zu lesen. Er meldet weder eine entfernte Überschrift
der Ebene 4 noch den ersetzten Text eines Inline-Code-Elements, eine vertauschte
Flagge oder einen internen Link, der mit einer überzähligen Klammer ausgegeben wurde,
`[texte]((#ancre))`, und nirgendwo mehr hinführt — und er beurteilt
die Sprache nicht.

### Dicht geschriebener Monitoring-Artikel, Modus `--news`

Eine Ausgabe des [KI-Monitorings von jls42.org](https://jls42.org/fr/news):
589 Zeilen, 140 Links, 21 Abschnitte, 3 geschützte englische Zitate. Kampagne
vom 4. und 5. September 2026.

| Modell                                          | Zugang              | Geschrieben | Ohne Abweichung | Median/Sprache |
| ----------------------------------------------- | ------------------- | ----------- | --------------- | -------------- |
| `gemini-3.7-flash`                              | Google API          | 14/14       | ✅ **14/14**    | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google-Abonnement   | 14/14       | ✅ **14/14**    | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google-Abonnement   | 14/14       | ✅ **14/14**    | 3 min 14 s     |
| `claude-sonnet-5-5`                             | Anthropic API       | 14/14       | ✅ **14/14**    | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT-Abonnement  | 14/14       | ✅ **14/14**    | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter          | 14/14       | ✅ **14/14**    | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter          | 14/14       | ✅ **14/14**    | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | Claude-Abonnement   | 14/14       | ⚠️ 13/14       | 6 min 49 s     |
| `claude-sonnet-5`                               | Anthropic API       | 14/14       | ⚠️ 11/14       | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | Claude-Abonnement   | 14/14       | ⚠️ 11/14       | 15 min 54 s    |
| `claude-haiku-5-5`                              | Anthropic API       | 14/14       | ⚠️ 11/14       | 2 min 54 s     |
| `claude-haiku-4-5`                              | Anthropic API       | 14/14       | ⚠️ 7/14        | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen        | 13/14       | ❌ 11/14       | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter          | 13/14       | ❌ 8/14        | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | lokal               | 10/14       | ❌ 7/14        | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral API         | 11/14       | ❌ 5/14        | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter          | 4/14        | ❌ 3/14        | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok-Abonnement     | 1/14        | ❌ 1/14        | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | Claude-Abonnement   | 0/14        | ❌ 0/14        | —              |

Grok wurde am 9. September an einer anderen Ausgabe desselben Monitorings
(356 Zeilen) erneut gemessen: 9 von 14 Sprachen geschrieben, 8 ohne Abweichung. Diese Zahl
steht in der Übersichtstabelle. Drei abgebrochene Kampagnen werden nicht
aufgeführt: `qwen3.5-27b` (9 Sprachen) und `kimi-k2.6` (4) wegen fehlenden Guthabens,
`z-ai/glm-5.3-flash`, dessen beide Fehlschläge auf eine Reasoning-Einstellung zurückzuführen waren,
die der Anbieter inzwischen korrigiert. Die OpenRouter-Zeilen wurden mit den
Standardeinstellungen des Routers vor `--use_openrouter` gemessen; `z-ai/glm-5.2`,
erneut mit dem ausgelieferten Anbieter gemessen, erreicht ebenfalls 14/14. Die Zahlen wurden
am 10. September mit dem aktuellen Vergleicher neu berechnet: `qwen3.8-flash` und
`qwen3.7-flash` gewinnen gegenüber der ersten Veröffentlichung jeweils eine Sprache hinzu,
die übrigen bleiben unverändert.

Die Zeilen `--use_antigravity` wurden am 26. September an demselben
Artikel gemessen, mit vier parallelen Übersetzungen: `gemini-3.7-flash-medium` am Vormittag,
`gemini-3.8-flash-medium` am Nachmittag. Im Englischen entfernten beide selbst
die drei französischen Übersetzungszeilen unter den Zitaten, ohne eine
Flagge zu erfinden, und die englischen Zitate blieben unverändert: Die Fallback-Bereinigung musste
nichts tun. Mit `--eco` (`gemini-3.7-flash-low`), nur für vier Sprachen
(en, ja, ar, hi): 4 von 4 geschrieben, alle ohne Abweichung, Median 1 min 52 s.
Gegenprobe am selben Tag mit einer neueren Ausgabe des Monitorings,
der vom 25. September (438 Zeilen, 2 englische Zitate), außerhalb des
Blogs durch `gemini-3.7-flash-medium` übersetzt: 14 von 14 geschrieben, alle ohne Abweichung, 87 bis
128 s pro Sprache.

Die Zeilen `--use_claude_code` wurden am 26. September an demselben
Artikel gemessen, mit vier parallelen Übersetzungen und dem Aufwand `low`. Mit `sonnet` blieben die
englischen Zitate in allen vierzehn Sprachen unverändert, und im Englischen entfernte das
Modell selbst die französischen Übersetzungszeilen, ohne eine Flagge zu erfinden.
`opus` schrieb keine Sprache: In jeder Sprache stoppten seine Schutzmechanismen
die Antwort beim letzten Segment wegen einer Kurzmeldung über 279 Moleküle,
die für eine Bindungsstelle erzeugt worden waren. Für sich allein eingesendet wird diese Kurzmeldung
aufgrund der Kategorie „Bio“ abgelehnt; `sonnet` übersetzte sie überall. `haiku` schreibt
alle vierzehn Sprachen; in drei davon (en, pl, ro) wechselt eine Abschnittsüberschrift von
Ebene 2 zu Ebene 1. Es führt Reasoning aus, ohne dass man es daran hindern kann — 61 % seiner
Ausgabe-Tokens —, weshalb es mehr als doppelt so lange wie `sonnet` benötigt.

Die Zeilen `claude-sonnet-5-5`, `claude-haiku-5-5` und `claude-haiku-4-5` wurden
am 18. Oktober über die API von Anthropic am selben Artikel gemessen, mit vier
parallelen Übersetzungen pro Modell. Sonnet 5.5 lässt das Abschalten seines
Reasonings nicht zu: aipmt sendet ihm die niedrigste akzeptierte Einstellung, und seine
Antworten enthalten keines. Es schreibt alle vierzehn Sprachen ohne Abweichung und ohne
ein Segment erneut zu verarbeiten; im Englischen entfernte es selbst die französischen
Übersetzungszeilen, ohne eine Flagge zu erfinden, und die englischen Zitate blieben
überall unverändert. Haiku 5.5 wurde mit seinem adaptiven Reasoning gemessen: Bei
deaktiviertem Reasoning ließ es ganze Absätze auf Französisch stehen, was der Prüfmechanismus ablehnt —
3 von 14 Sprachen geschrieben. Beide Haiku-Modelle scheitern an derselben Kurzmeldung: Haiku 5.5
ändert die Ebene ihrer Überschrift oder verdoppelt sie auf Japanisch, Koreanisch und
Chinesisch; Haiku 4.5 setzt sie in sieben Sprachen auf Ebene 1 und belässt sie
im Japanischen auf Französisch. Haiku 4.5 kostet für beide Dokumente in allen
vierzehn Sprachen 3,67 $, Haiku 5.5 0,57 $, Sonnet 5.5 9,21 $.
### README dieses Projekts, Standard-Markdown

Eingefrorene Revision vom 9. September 2026: 785 Zeilen, 285 Inline-Codes, 40
Blockabschlüsse, 89 Tabellenzeilen. Vier Übersetzungen parallel.

| Modell                                          | Erstellt | Ohne Abweichung | Median/Sprache | Abweichungen                                                             |
| ----------------------------------------------- | -------- | --------------- | --------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14    | ✅ 14/14        | 1 min 43 s      | keine                                                                    |
| `opus` (`--use_claude_code`)                    | 14/14    | ✅ 14/14        | 1 min 48 s      | keine                                                                    |
| `haiku` (`--use_claude_code`)                   | 14/14    | ✅ 14/14        | 4 min 02 s      | keine für das Vergleichswerkzeug; interne Links verdoppelt (en)          |
| `claude-sonnet-5-5`                             | 14/14    | ✅ 14/14        | 1 min 18 s      | keine                                                                    |
| `claude-haiku-4-5`                              | 14/14    | ✅ 14/14        | 2 min 06 s      | keine                                                                    |
| `gemini-3.7-flash`                              | 14/14    | ⚠️ 13/14        | 36 s            | ein fett gedrucktes Wort (ja)                                            |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14    | ⚠️ 13/14        | 1 min 22 s      | ein fett gedrucktes Wort (ko)                                            |
| `sonnet` (`--use_claude_code`)                  | 14/14    | ⚠️ 13/14        | 2 min 20 s      | eine Tabellenzeile mit der vorherigen zusammengefügt (ar)                |
| `claude-sonnet-5`                               | 14/14    | ⚠️ 12/14        | 2 min 56 s      | ein Link (sv), ein fett gedrucktes Wort (zh)                              |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14    | ⚠️ 12/14        | 6 min 46 s      | ein fett gedrucktes Wort (ar, ja)                                        |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14    | ⚠️ 11/14        | 2 min 34 s      | ein fett gedrucktes Wort (hi, ja, ko)                                    |
| `qwen/qwen3.7-flash`                            | 14/14    | ⚠️ 10/14        | 2 min 17 s      | 40 Inline-Codes im Arabischen hinzugefügt; Fettdruck (hi, ja, ko)         |
| `claude-haiku-5-5`                              | 12/14    | ❌ 12/14        | 1 min 14 s      | 2 Sprachen abgelehnt (ar, hi): Inline-Codes bei der Rückgabe verloren    |
| `mistral-large-latest`                          | 14/14    | ❌ 1/14         | 2 min 44 s      | ein Abschnitt verloren (ar, hi, ko); Codeblöcke hinzugefügt (ja, ko, ro, zh) |

Zwei abgebrochene Durchläufe werden nicht bewertet: Grok, dessen CLI-Sitzung
nach zwölf Sprachen ablief (elf ohne Abweichung), und `qwen3.8-flash`, bei dem
der Hoster nach zwei Sprachen HTTP 429 zurückgab. `opencode/mimo-v2.5-free` und
`ollama/gpt-oss-20b-32k` wurden bei dieser Revision nicht erneut gemessen; bei der
um 277 Zeilen kürzeren Revision vom 4. und 5. September erstellten beide jeweils
9 von 14 Übersetzungen, davon 7 beziehungsweise 1 ohne Abweichung.

Die Zeilen `--use_antigravity` und `--use_claude_code` wurden nicht bei der
eingefrorenen Revision gemessen, sondern am 26. September bei der mit Version
1.14.0 veröffentlichten Revision — und die Zeilen `claude-sonnet-5-5`,
`claude-haiku-5-5` und `claude-haiku-4-5` am 18. Oktober bei derselben:
600 Zeilen, 257 Inline-Codes, 30 Blockabschlüsse, 85 Tabellenzeilen. Da sie
185 Zeilen kürzer ist, lässt sie sich nicht Punkt für Punkt mit den anderen
Zeilen vergleichen; diese Zeilen untereinander hingegen schon. Bei den
internen Links, die das Vergleichswerkzeug nicht überprüft, behielt
`gemini-3.8-flash-medium` sie in allen vierzehn Sprachen unverändert bei,
`gemini-3.7-flash-medium` beschädigte sie im Italienischen; `sonnet` und
`opus` behielten sie überall unverändert bei, `haiku`
verdoppelte sie im Englischen; `claude-sonnet-5-5` und `claude-haiku-4-5` behielten
sie in allen vierzehn Sprachen unverändert bei, `claude-haiku-5-5` in den zwölf,
die es erstellte.

### Vier README-Dateien bekannter Projekte

FastAPI, Ollama, tldr-pages und Vue.js, unverändert von GitHub übernommen —
Dokumente, die einfacher sind als die beiden vorherigen. Der Durchlauf
konzentrierte sich auf Modelle mit Schwierigkeiten; Gemini dient dabei als
Vergleichspunkt.

| Modell                    | Umfang                     | Erstellt | Ohne Abweichung |
| ------------------------- | -------------------------- | -------- | --------------- |
| `gemini-3.7-flash`        | 4 Projekte × 14 Sprachen   | 56/56    | ✅ **55/56**    |
| `opencode/mimo-v2.5-free` | 4 Projekte × 14 Sprachen   | 55/56    | ❌ 47/56        |
| `grok-4.6` (Abonnement)   | 4 Projekte × ar, hi, ja, zh | 16/16    | ❌ 14/16        |
| `ollama/gpt-oss-20b-32k`  | 4 Projekte × ar, hi, ja, zh | 15/16    | ❌ 9/16         |

### Was diese Messungen nicht sind

- **Keine umfassende Rangliste**: Allein OpenRouter bietet mehr als vierhundert
  Modelle an, etwa fünfzehn davon wurden gemessen.
- **Nur Richtwerte für die Dauer**: je nach Durchlauf drei bis sechs
  Übersetzungen parallel, und der Durchsatz eines Anbieters schwankt im
  Tagesverlauf.
- **Zeitgebundene Beobachtungen**: Modelle ändern sich unter demselben Namen,
  und Ihre Dokumente sind nicht unsere.

So wiederholen Sie die Messung mit Ihren Dokumenten und einer eingefrorenen
Kopie der Datei:

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

Werkzeuge zur Qualitätssicherung, optional, aber empfohlen:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Die 28 Übersetzungen des Repositorys (README und CHANGELOG, vierzehn Sprachen)
werden mit `./regen_translations.sh --force` neu erzeugt — standardmäßig Codex und
`gpt-5.6-sol` über das ChatGPT-Abonnement, vier parallel.
`REGEN_PROVIDER` und `REGEN_MODEL` ändern den Pfad: `antigravity` bleibt
bei einem Abonnement, dem von Google, und wird ohne Sondergenehmigung
ausgeführt; eine kostenpflichtige API (`openai`, `gemini`,
`grok`, `openrouter`) wird ohne `REGEN_ALLOW_PAID_API=1` abgelehnt;
`REGEN_JOB_TIMEOUT` begrenzt jeden Job (600 s, 1 800 s bei Codex und
Antigravity). Einzelheiten zu den Werkzeugen stehen in `CLAUDE.md`.

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** — persönlicher Blog, der in 15 Sprachen
  veröffentlicht wird. Seine [tägliche KI-Übersicht](https://jls42.org/fr/news) wird jeden Tag
  mit diesem Werkzeug übersetzt und dient als Referenzdokument für die oben
  genannten Messungen.

## Autor

Julien LE SAUX
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Haftungsausschluss

Dieses Programm wird **ohne jegliche Gewährleistung** gemäß den Bestimmungen
der Abschnitte 15 und 16 der GPL v3 verbreitet: Es wird „wie besehen“
bereitgestellt, ohne Gewährleistung der Marktgängigkeit oder Eignung für einen
bestimmten Zweck, und sein Autor kann nicht für Schäden haftbar gemacht werden,
die aus seiner Verwendung entstehen. Der Lizenztext hat Vorrang vor dieser
Zusammenfassung.

- **Lesen Sie alles vor der Veröffentlichung Korrektur.** Die
  Schutzmechanismen decken Codeblöcke, Inline-Code, URLs, Anker und Zitate im
  Modus `--news` ab — weder Überschriften noch Tabellen, Front Matter
  oder die Bedeutung Ihrer Sätze.
- **Ihre Dokumente werden an den ausgewählten Anbieter übermittelt**, gemäß
  dessen Nutzungsbedingungen und Datenrichtlinie. Einige kostenlose Modelle
  können Ihre Interaktionen für das Training wiederverwenden, und die
  Bedingungen von Antigravity erlauben Google, sie wiederzuverwenden und von
  Menschen überprüfen zu lassen, auch bei einem kostenpflichtigen Abonnement;
  ein lokales Modell ist die einzige Möglichkeit, bei der keine Daten Ihren
  Rechner verlassen.
- **Die API-Aufrufe werden Ihnen in Rechnung gestellt.** Dieses Programm
  begrenzt die Ausgaben nicht: Ein langes Dokument, eine Wiederaufnahme nach
  einem Fehler oder ein Modell, das besonders viel Reasoning betreibt,
  verursachen höhere Kosten.
- **Die veröffentlichten Messungen sind zeitgebundene Beobachtungen**, keine
  Garantien.

Die genannten Produkt- und Unternehmensnamen gehören ihren jeweiligen
Rechteinhabern. Dieses Projekt ist mit keinem von ihnen verbunden.

**Artikel mit gpt-5.6-sol aus dem Französischen ins Deutsche übersetzt.**

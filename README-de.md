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

Übersetzt Markdown-Dateien von einer Sprache in eine andere und behält dabei die
Struktur bei: Code-Blöcke, Inline-Code, URLs, Anker, Tabellen und Frontmatter.
Zehn Möglichkeiten, ein Modell aufzurufen – fünf APIs, drei Abonnements ohne
nutzungsbasierte Abrechnung, zwei Router – und eine veröffentlichte Messung
dessen, was jedes Modell tatsächlich beibehält.

## Auf einen Blick

- **Zehn Provider-Wege**: APIs von OpenAI, Mistral, Claude, Gemini und Grok;
  Abonnements für ChatGPT (Codex), Grok und Google (Antigravity) ohne
  nutzungsbasierte Abrechnung; OpenCode-Router (Open Source, kostenlos oder
  lokal) und OpenRouter (über 400 Modelle).
- **Nichts fehlerhaft durch ein verlorenes Token**: Code-Blöcke, Inline-Code,
  URLs, Anker und Zitate werden vor dem Aufruf durch Tokens ersetzt und bei
  der Rückgabe überprüft. Fehlt eines davon, wird die Datei nicht geschrieben.
- **Lange Dokumente**: Segmentierung anhand des Kontextfensters des Modells.
- **Modus `--news`**: Englische Zitate geschützt und Flaggen sprachspezifisch
  verwaltet, für Monitoring-Artikel.
- **Modus `--eco`**: Schnelle und kostengünstigere Modelle.
- **Übersetzungshinweis** optional, oben, unten oder an beiden Stellen.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 oder neuer. Zur Installation aus dem Repository siehe
[Mitwirken](#mitwirken).

## Konfiguration

Schlüssel werden an drei Orten gelesen, in absteigender Priorität; jeder füllt
nur das aus, was der vorherige leer lässt.

|     | Wo                                            | Wofür                                 |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Umgebungsvariablen                            | CI, Container, punktuelle Ausnahmen   |
| 2   | `.env` des aktuellen Verzeichnisses (oder eines übergeordneten) | ein projektspezifischer Schlüssel     |
| 3   | `~/.config/aipmt/.env`                                 | einmal eingerichtet, gilt überall     |

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
folgt `XDG_CONFIG_HOME` (nur absolute Pfade) und `%APPDATA%`
unter Windows. Ohne Schlüssel listet der Befehl alle drei Speicherorte auf.

**Die `.env` eines Projekts kann weder Aufrufe umleiten noch das ausgeführte
Programm bestimmen.** Sie liefert Schlüssel, niemals ein Ziel oder eine Binärdatei:
Jede Variable mit `_BASE_URL`, `_API_BASE`, `_ENDPOINT` oder `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, Proxies (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), Zertifikatsspeicher (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) sowie `XDG_CONFIG_HOME` /
`APPDATA` werden darin mit einer Warnung ignoriert. Ein geklontes Repository darf
weder Ihre Schlüssel abfangen noch Sie dazu bringen, bei der ersten Übersetzung ein
eigenes Programm auszuführen. Diese Datei wird zudem ohne Interpolation gelesen:
`NOM=${OPENAI_API_KEY}` kopiert den Schlüssel darin nicht. Setzen Sie diese Variablen in der
Umgebung oder in `~/.config/aipmt/.env`.

Optionale Variablen: `XAI_BASE_URL` (Standard `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (Sekunden pro Aufruf, Standard 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(Standard 600), `GROK_BIN`, `GROK_HOME` (Standard `~/.grok`), `GROK_TIMEOUT`
(Standard 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (Standard 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (Standard 600), `OPENROUTER_BASE_URL`
(`https://` erforderlich), `OPENROUTER_TIMEOUT` (Standard 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (Standard 30). Jede wird im Abschnitt des jeweiligen Providers
näher erläutert.

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
immer zu `.md` – `article.mdx` ergibt `article-en.md` – außer bei
`--keep_filename`, wodurch der ursprüngliche Name beibehalten wird. Eine bereits vorhandene
Übersetzung wird ohne `--force` übersprungen.

Exit-Codes: `0`, wenn alles erfolgreich war oder übersprungen wurde, `1`, wenn mindestens eine Datei
fehlgeschlagen ist (Liste in der Fehlerausgabe), `2`, wenn ein Konfigurationsfehler vorliegt.
Eine fehlgeschlagene Datei wird niemals geschrieben, selbst wenn der Schreibvorgang selbst fehlschlägt:
Der Inhalt wird temporär daneben geschrieben und anschließend umbenannt. Ein erneuter Aufruf genügt.

## Welches Modell wählen?

Gemessen an zwei realen Dokumenten, die von jedem Modell in dieselben vierzehn
Sprachen übersetzt wurden. **Die Zahl gibt an, in wie vielen von vierzehn Sprachen
die Übersetzung geschrieben wurde und keinerlei Abweichungen von der Quelle aufweist.**

| Modell               | Zugangsweg                        | Dichter Monitoring-Artikel | Diese README | Was abweicht und in wie vielen Sprachen                                                                                               |
| -------------------- | --------------------------------- | -------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | Google-API-Schlüssel              | ✅ 14/14                   | ⚠️ 13/14     | 1 von 14 Sprachen: ein fettgedrucktes Wort zusätzlich (ja)                                                                            |
| **Gemini 3.7 Flash** | Google-Abonnement (Antigravity)   | ✅ 14/14                   | ⚠️ 13/14     | 1 von 14 Sprachen: ein fettgedrucktes Wort weniger (ko)                                                                               |
| **GPT-5.6 Sol**      | ChatGPT-Abonnement oder OpenAI-Schlüssel | ✅ 14/14            | ⚠️ 12/14     | 2 von 14 Sprachen: ein fettgedrucktes Wort weniger (ar, ja)                                                                           |
| **GLM-5.2**          | OpenRouter-Schlüssel              | ✅ 14/14                   | ⚠️ 11/14     | 3 von 14 Sprachen: ein fettgedrucktes Wort weniger (hi, ja, ko)                                                                       |
| Claude Sonnet 5      | Anthropic-API-Schlüssel           | ⚠️ 11/14                   | ⚠️ 12/14     | 3 Sprachen beim Artikel: ein zusätzlicher Code-Block (es, de, hi); 2 bei dieser README: ein Link ohne Formatierung (sv), ein fettgedrucktes Wort (zh) |
| Qwen 3.7 Flash       | OpenRouter-Schlüssel              | ❌ 8/14                    | ⚠️ 10/14     | 1 Sprache beim Artikel abgelehnt, 5 weitere weichen ab; bei dieser README rund 40 Wörter fälschlich als `code` formatiert (ar) |
| Grok 4.6             | Grok-Abonnement                   | ❌ 8/14                    | nicht bewertet | 5 von 14 Sprachen abgelehnt, da Inline-Code und URLs fehlten; Niederländisch weicht komplett ab                                       |
| GPT-OSS 20B          | lokales Modell (Ollama)           | ❌ 7/14                    | nicht erneut gemessen | 4 von 14 Sprachen abgelehnt: Das Modell beließ Passagen auf Französisch, die Schutzprüfung stoppte sie                              |
| MiMo v2.5 (kostenlos) | OpenCode Zen, ohne Konto         | ❌ 11/14                   | nicht erneut gemessen | 1 Sprache abgelehnt; ein Abschnitt auf Polnisch verloren                                                                              |
| Mistral Large        | Mistral-API-Schlüssel             | ❌ 5/14                    | ❌ 1/14      | **ein kompletter Abschnitt fehlt**: 1 Sprache beim Artikel (hi), 3 bei dieser README (ar, hi, ko) – und 3 Sprachen beim Artikel abgelehnt |
| DeepSeek V4 Flash    | OpenRouter-Schlüssel              | ❌ 3/14                    | nicht erneut gemessen | 10 von 14 Sprachen abgelehnt; 37 Minuten pro Sprache                                                                                 |

|     | Bedeutung des Symbols                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alle vierzehn Sprachen übersetzt, keinerlei Abweichungen von der Quelle                                                                                                                               |
| ⚠️  | alle vierzehn Sprachen übersetzt; Abweichungen betreffen nur **Formatierungen** – ein fettgedrucktes Wort, ein `code`, ein Link verliert eckige Klammern. Kein Text, keine URL, kein Code-Block, kein Abschnitt fehlt |
| ❌  | mindestens eine Sprache konnte nicht übersetzt werden – Datei abgelehnt, nicht geschrieben – **oder** Inhalte fehlen in einer geschriebenen Datei                                                    |

Wichtigste Erkenntnisse:

- **Eine abgelehnte Übersetzung ist keine beschädigte Übersetzung.** Wenn bei
  der Rückgabe ein Token fehlt, wird die Datei nicht geschrieben und die Sprache
  gilt als abgelehnt. Genau das passiert Grok beim Artikel: Vier Inline-Codes
  und drei URLs gingen bereits im ersten Segment bei allen fünf nicht-lateinischen
  Schriften verloren.
- **Dieses Sicherheitsnetz deckt keine Überschriften, Tabellen, Frontmatter oder
  Fließtext ab.** Wenn ein Modell einen Abschnitt löscht, wird die Datei vom
  Tool dennoch anstandslos geschrieben – wie es bei Mistral der Fall ist.
  Diese Elemente lassen sich nicht durch Tokens ersetzen und werden von den
  aktuellen Prüfungen nicht kontrolliert; `scripts/compare_structure.py` erkennt einen
  verlorenen Abschnitt erst im Nachhinein.
- **Grok hat keine Wertung für diese README**: Die CLI-Sitzung lief nach zwölf
  Sprachen ab, davon elf fehlerfrei. Ein abgebrochener Testlauf wird nicht
  bewertet.
- **Die Dichte des Dokuments ist entscheidender als die Sprache.** Grok bewältigt
  gewöhnliche READMEs problemlos, scheitert jedoch an einem stark verlinkten
  Artikel – selbst auf Niederländisch.

Daten und Dokumente: Die Spalte „Diese README“ wurde am 9. September 2026
anhand einer fixierten Revision dieser Datei gemessen (785 Zeilen, 285 Inline-Codes,
89 Tabellenzeilen), die seither überarbeitet wurde – mit Ausnahme der
Antigravity-Zeile, die am 26. September auf der mit Version 1.14.0 veröffentlichten,
kürzeren Revision gemessen wurde (600 Zeilen, 257 Inline-Codes, 85 Tabellenzeilen).
Die Spalte „Dichter Monitoring-Artikel“ stammt aus dem Testlauf vom 4. und 5. September
mit einem 589-zeiligen Artikel, außer der Grok-Zeile (am 9. September anhand einer
anderen Ausgabe desselben Monitorings nachgemessen) und der Antigravity-Zeile
(am 26. September anhand desselben Artikels gemessen). Die vollständigen Tabellen,
Laufzeiten und das Protokoll finden sich unter [Detaillierte Messwerte](#detaillierte-messungen).

## Alle Optionen

| Option                   | Beschreibung                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`           | Einzelne zu übersetzende Markdown-Datei (Alternative zu `--source_dir`)                                        |
| `--source_dir`           | Quellverzeichnis mit den Markdown-Dateien (Standard: `content/posts`)                                          |
| `--target_dir`           | Ausgabeverzeichnis für die übersetzten Dateien (Standard: `traductions_en`)                                    |
| `--source_lang`           | Quellsprache (Standard: `fr`)                                                                       |
| `--target_lang`           | Zielsprache (Standard: `en`)                                                                        |
| `--model`           | Bestimmtes zu verwendendes Modell                                                                             |
| `--eco`           | Kostengünstige Modelle verwenden                                                                              |
| `--use_mistral`           | Mistral-AI-API verwenden                                                                                      |
| `--use_claude`           | Claude-API verwenden                                                                                          |
| `--use_gemini`           | Gemini-API verwenden                                                                                          |
| `--use_grok`           | xAI-API (Grok) verwenden – erfordert `XAI_API_KEY`                                                           |
| `--use_codex`           | Codex-CLI über das Kontingent des ChatGPT-Abonnements verwenden                                               |
| `--use_grok_cli`           | Grok-CLI über das Kontingent des Grok-Abonnements verwenden                                                   |
| `--use_antigravity`           | Antigravity-CLI (`agy`) über das Kontingent des Google AI Pro- oder Ultra-Abonnements verwenden       |
| `--use_opencode`           | OpenCode (Open Source) mit dem in OpenCode konfigurierten Provider verwenden; erfordert `--model provider/modèle`        |
| `--use_openrouter`           | OpenRouter verwenden – erfordert `OPENROUTER_API_KEY` und `--model fournisseur/modèle`                                            |
| `--force`           | Erneute Übersetzung erzwingen                                                                                 |
| `--keep_filename`           | Ursprünglichen Dateinamen beibehalten                                                                         |
| `--news`           | News-Modus: schützt englische Zitate, verwaltet Flaggen je Sprache                                            |
| `--add_translation_note`           | Übersetzungshinweis hinzufügen                                                                                |
| `--note_position`           | Position des Hinweises: `top`, `bottom` (Standard) oder `both`                         |
| `--note_format`           | Format des Hinweises: `legacy` (Standard, fetter Absatz) oder `marker`                            |
| `--include_model`          | Modellnamen in die Ausgabedatei aufnehmen                                                                     |
| `--reasoning_effort`          | GPT-5.x-Reasoning-Aufwand: `none`/`low`/`medium`/`high`/`xhigh`   |

Die neun `--use_*`-Flags schließen sich gegenseitig aus: Das Kombinieren zweier Flags wird
abgelehnt.

## Provider

### Über API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` schaltet auf die Sparstufe jedes Anbieters um.

| Provider    | Qualität (Standard)                                   | Sparsam (`--eco`) |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol` (auch `terra` und `luna` über `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.7-flash-medium`                             | `gemini-3.7-flash-low`    |
| OpenCode    | `--model provider/modèle` erforderlich                 | ebenso — `--eco` ohne Wirkung |
| OpenRouter  | `--model fournisseur/modèle` erforderlich              | ebenso — `--eco` ohne Wirkung |

### Über das ChatGPT-Abonnement: `--use_codex`

Steuert die offizielle Codex-CLI: Die Übersetzung wird vom Kontingent des
ChatGPT-Abonnements abgezogen, ohne API-Schlüssel oder nutzungsbasierte Abrechnung.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Die Binärdatei wird in `CODEX_BIN`, dann im `PATH`, dann im Paket
  `openai-codex-cli-bin` gesucht. `~/.codex/auth.json` wird nie gelesen.
- `OPENAI_API_KEY` und `CODEX_API_KEY` werden aus der Umgebung des
  Subprozesses entfernt: Ein vorhandener Schlüssel führt niemals zu einem Wechsel zur API.
- Jedes Segment kostet mindestens eine „Nachricht“ des 5-Stunden-Fensters — zwei,
  wenn dessen Validierung fehlschlägt und es wiederholt wird. OpenAI gibt als
  Schätzung 250–2.000 Nachrichten/5 h für `gpt-5.6-luna` (`--eco`) und
  10–100 für `gpt-5.6-sol` bei einem Plus-Tarif an.
- `--model gpt-5.6-terra` und `--model gpt-5.6-luna` laufen ebenfalls über das
  Abonnement. Ein Modell, für das das Konto nicht berechtigt ist, gibt einen 400-Fehler „model is
  not supported when using Codex with a ChatGPT account“ zurück.
- Langsamer als eine API, und der Abstand wächst mit dem Dokument: bei dieser README
  im Median 6 Min. 46 Sek. pro Sprache mit `gpt-5.6-sol`, gegenüber 36 Sek. für
  `gemini-3.7-flash`.
- In CI verweigert (`CI` oder `GITHUB_ACTIONS` gesetzt): Das Abonnement authentifiziert
  sich über eine persönliche Sitzungsdatei, die auf einem geteilten Runner
  nichts zu suchen hat.
- Variablen: `CODEX_BIN`, `CODEX_TIMEOUT` (Sekunden pro Segment, Standard 600).

### Über das Grok-Abonnement: `--use_grok_cli`

Gleiches Prinzip mit der offiziellen CLI Grok Build über das Abonnement SuperGrok oder
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Schwächere Isolation als bei Codex.** Die OS-Sandbox von Grok greift
  auf vielen aktuellen Linux-Rechnern nicht (AppArmor, Container-Runtime-Sockets),
  und ein Profil, das nicht angewendet werden kann, startet stillschweigend ungeschützt.
  Das Skript fordert daher standardmäßig kein Profil an, weist darauf hin und
  stützt sich auf die `--deny`-Regeln der CLI, darunter das Catch-all `*` — die
  einzige Schicht, die den Start verweigert, anstatt den Schutz stillschweigend
  aufzuheben. `GROK_TRANSLATE_SANDBOX=read-only` erzwingt die OS-Sandbox, und der Start
  schlägt fehl, wenn die Maschine dies nicht erfüllen kann.
- Das Kontingent ist wöchentlich, wird mit Chat, Imagine und Voice geteilt, und kein
  Befehl erlaubt das Auslesen: Ein Batch kann das Kontingent für Konversationen
  ohne Vorwarnung aufbrauchen.
- Variablen: `GROK_BIN`, `GROK_HOME` (CLI-Verzeichnis, Standard `~/.grok`),
  `GROK_TIMEOUT` (Standard 900), `GROK_TRANSLATE_SANDBOX`.

### Über das Google-Abonnement: `--use_antigravity`

Gleiches Prinzip mit `agy`, der offiziellen CLI von Antigravity: Wer Google
AI Pro oder Ultra bezahlt, für den wird die Übersetzung vom Kontingent des Abonnements abgezogen,
anstatt tokenbasiert abgerechnet zu werden. Dies ist der einzige Weg zu diesem Kontingent: Gemini CLI
bedient diese Konten seit dem 18. Juni 2026 nicht mehr
([Ankündigung](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
und das Antigravity-SDK akzeptiert nur einen API-Schlüssel oder ein Google-Cloud-Projekt.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Kein kostenpflichtiger Weg bleibt offen.** agy erhält aus Ihrer
  Umgebung nur eine geschlossene Liste von Variablen — `PATH`, Sprache und Zeitzone,
  Terminal, Identität, Proxys und Zertifikate, Sitzungsbus — und keine Schlüssel:
  Mehrere seiner Variablen leiten einen Aufruf stillschweigend um (gemessen:
  eine sendet das Dokument an ein Drittanbieter-Gateway, eine andere an ein abgerechnetes
  Google-Cloud-Projekt), und eine Denylist vergaß bei jeder Prüfung etwas.
  Vor jedem Segment muss `agy -p /config`, das kein Kontingent verbraucht,
  zeigen, dass kostenpflichtige KI-Guthaben deaktiviert sind, ohne API-Schlüssel oder Google-Cloud-Projekt — eine
  fehlende Einstellung gilt als Ablehnung —, andernfalls wird nichts übersetzt; das Protokoll jedes
  Aufrufs muss anschließend das Abonnement bestätigen (`authMethod=consumer`), andernfalls wird die
  Antwort abgelehnt.
- **Isolation.** Jeder Aufruf läuft in einem privaten, temporären
  Benutzerverzeichnis mit einem Übersetzungsmagenten ohne Werkzeuge: Ihre Einstellungen, Regeln,
  Plugins, MCP-Server und Hooks von agy gelangen nicht dorthin, nichts wird zu Ihrem
  Verlauf hinzugefügt, und die Anmeldung verbleibt im Schlüsselbund, den aipmt niemals ausliest.
  Ein nicht gefundener Agent lässt agy stillschweigend auf seinen Coding-Agenten
  und dessen Werkzeuge zurückfallen: Eine vollständige Protokollzeile muss den richtigen Agenten bestätigen — ein
  Dokument, das diese Meldung zitiert, ersetzt dies nicht —, andernfalls erfolgt eine Ablehnung.
- **Plattformen**: Linux, in einer Sitzung mit Schlüsselbund (D-Bus-Sitzungsbus,
  Secret Service); macOS wird akzeptiert, wurde dort jedoch nicht gemessen. Abgelehnt
  unter Windows, wo agy die Variablen zur Isolation der einzelnen Aufrufe nicht liest, und
  unter Linux ohne Sitzungsbus — SSH-Sitzung, Container, Server: agy speichert
  sein Token dort in einer Datei unter `~/.gemini`, die durch die Isolation verdeckt wird. Die
  Ablehnung erfolgt vor jedem Start samt Ursache, statt einer Minute
  Wartezeit auf einen Login-Code.
- **Modelle**: diejenigen aus `agy models`. Die Gemini-Modelle tragen den Effort in ihrem Namen
  (`gemini-3.7-flash-low`…): Ein Name ohne Suffix wird vor dem Aufruf abgelehnt, und
  `--reasoning_effort` ist wirkungslos. Die beiden Standardwerte wurden im Rahmen einer
  Testreihe über vierzehn Sprachen festgelegt (siehe [Detaillierte Messungen](#detaillierte-messungen)).
  Claude und GPT-OSS haben ihr eigenes, viel kleineres Kontingent: etwa 1 % des
  5-Stunden-Fensters pro gemessenem Aufruf, gegenüber 0,05 % bei Flash.
- **Kontingent**: pro Gruppe, ein 5-Stunden- und ein wöchentliches Fenster,
  anteilig nach Tokenkosten. Gemessen auf dem Konto des Autors anhand einer
  Testreihe von 32 Übersetzungen: etwa ein halber Prozentpunkt des 5-Stunden-Fensters
  für eine README mit 40.000 Zeichen in `gemini-3.7-flash-medium`; das wöchentliche Limit
  hängt hingegen von der Tarifstufe ab. Wiederholungsversuche richten sich nach dem, was agy als
  wiederholbar einstuft; andernfalls wird ein erschöpftes Fenster niemals wiederholt: Es lässt
  jede Datei fehlschlagen, bis der von `/usage` angezeigte Reset erfolgt.
- **Langsamer als die API**: Beim dichten Testartikel benötigt Gemini 3.7 Flash
  über das Abonnement im Median 3 Min. 14 Sek. pro Sprache, gegenüber 1 Min. 18 Sek. über
  die API.
- **Abbruch**: Strg-C oder ein geschlossenes Terminal stoppen agy zusammen mit dem
  Befehl, anstatt ihn seinen Durchlauf auf Ihrem Kontingent beenden zu lassen; das Gleiche
  gilt für Codex, Grok CLI und OpenCode. Unter `nohup` läuft die Übersetzung weiter.
- In CI verweigert (`CI` oder `GITHUB_ACTIONS` gesetzt): Der Login befindet sich in einem
  persönlichen Schlüsselbund. Auf einem Runner: `--use_gemini` mit `GOOGLE_API_KEY`.
- Variablen: `AGY_BIN` (sonst `PATH`, dann `~/.local/bin/agy`),
  `AGY_TIMEOUT` (Sekunden pro Segment inklusive Start, Standard 900).

**Nutzungsbedingungen: Es ist Ihr Konto gebunden.** Die
[Antigravity-Nutzungsbedingungen](https://antigravity.google/terms) (Abschnitt 6) und deren
[FAQ](https://antigravity.google/docs/faq/) untersagen den Zugriff auf den Dienst
über Software von Drittanbietern unter Verwendung des Antigravity-Logins — Claude Code,
OpenClaw und OpenCode werden dort genannt —, unter Androhung einer Kontosperrung. aipmt
liest oder verwendet das Token nicht wieder: Es startet die offizielle Binärdatei im
[Headless-Modus](https://antigravity.google/docs/cli/headless/), den Google
für Skripte und CI dokumentiert. Ein Google-Mitarbeiter bezeichnete es als „üblich“,
`agy -p` aus einem lokalen Skript für die eigene Arbeit auszuführen
([offizielles Forum, 25. September 2026, unverbindliche Antwort](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
kein Text regelt den Fall eines verteilten Werkzeugs wie diesem eindeutig.

**Nur öffentliche Dokumente.** Gemäß Abschnitt 5 derselben Bedingungen können
Interaktionen — Prompts, Antworten, Metadaten — dazu verwendet werden, die
Produkte und das maschinelle Lernen von Google zu verbessern, und von Menschen
überprüft werden, auch bei einem kostenpflichtigen Abonnement. Das Opt-out erfolgt über die Einstellung
`enableTelemetry` mit nicht dokumentierter Wirkung, die aipmt nicht setzt; Ihre agy-Einstellungen
werden nicht in die Isolation übernommen. Übermitteln Sie hierüber nichts Vertrauliches.

### Zum Anbieter der Wahl: `--use_opencode`

[OpenCode](https://opencode.ai) ist ein Open-Source-Code-Agent (MIT), der
Anfragen an die darin konfigurierten Anbieter weiterleitet: API-Schlüssel, Abonnement,
OpenCode-Zen-Gateway (kostenlose Modelle, ohne Konto) oder lokales Modell. Zwei
Wege wurden hier von Ende zu Ende gemessen: Zen und Ollama.

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

`--model` ist erforderlich: Ohne diesen würde OpenCode auf ein kostenloses Modell zurückfallen,
dessen Interaktionen für das Training verwendet werden können, und diese Entscheidung wird nicht für
Sie getroffen.

Isolation bei jedem Aufruf:

- Eine Inline-Konfiguration mit Vorrang vor Ihrer eigenen definiert einen Agenten `aipmt`,
  dessen Werkzeuge alle abgelehnt werden (`permission: { "*": "deny" }`), Sitzungsteilung
  deaktiviert, `--pure`, niemals `--auto`;
- Temporäres und leeres Arbeitsverzeichnis, `OPENCODE_DISABLE_PROJECT_CONFIG` und
  `OPENCODE_DISABLE_CLAUDE_CODE` gesetzt — ohne diese schleust OpenCode die `AGENTS.md` des
  aktuellen Verzeichnisses sowie `~/.claude/CLAUDE.md` in den Prompt ein. Die
  globale `~/.config/opencode/AGENTS.md` bleibt eingeschleust, OpenCode erlaubt es nicht,
  sie auszuschließen;
- Ausgabevertrag: Rückgabecode 0, kein `error`-Ereignis, kein
  Tool-Aufruf, letzter Schritt als `stop`, nicht-leerer Text und der Agent `aipmt`
  tatsächlich geladen — ein unbekanntes `--agent` lässt OpenCode nicht fehlschlagen, sondern
  stillschweigend auf den Coding-Agenten zurückfallen;
- Es wird kein Schlüssel von `aipmt` übergeben, außer `OPENCODE_API_KEY`, dem Schlüssel
  von OpenCode selbst. Die Anbieter werden in OpenCode konfiguriert, nicht in
  der `.env` von `aipmt`.

Zu beachten:

- Die kostenlosen Modelle von Zen ändern sich ständig, haben undokumentierte Limits und
  ihre Interaktionen können für das Training verwendet werden: für öffentliche Dokumentation
  geeignet, nicht für private Inhalte.
- Ein lokales Modell muss mindestens 16k Kontext-Tokens bieten, da Segmente
  bis zu 16.000 Zeichen umfassen. Ollama konfiguriert oft nur 4.096: über
  ein `Modelfile` mit `PARAMETER num_ctx 32768` anpassen.
- `--eco` ist wirkungslos; `--reasoning_effort` wird unverändert als
  `--variant` von OpenCode übergeben.
- OpenCode protokolliert jede Sitzung in `~/.local/share/opencode/`.
- Variablen: `OPENCODE_BIN` (sonst `PATH`, dann `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (Sekunden pro Segment, Standard 600). `OPENCODE_CONFIG`
  wird unverändert an OpenCode übergeben.

Beispiel eines lokalen Modells über Ollama in `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` schaltet das Reasoning ab, das Ollama standardmäßig bei diesen
Modellen aktiviert und das ein Modelfile nicht deaktivieren kann. Gemessen an einem Satz aus
sechs Wörtern: 919 Reasoning-Tokens und 68 Sekunden ohne diese Option, 9 Tokens mit.

### Zu über 400 Modellen: `--use_openrouter`

OpenRouter ist ein nutzungsbasiert über ein einzelnes Guthaben abgerechneter Router vor
von Dritten gehosteten Modellen — darunter die offenen chinesischen Modelle, die kein
anderer Provider hier anbietet.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` ist erforderlich. Ein Preflight, der vor jeder Abrechnung ausgeführt wird, regelt
zwei Besonderheiten des Routings:

- **Dasselbe Modell wird von Dutzenden Hostern mit unterschiedlichen Limits
  bereitgestellt** — bei `z-ai/glm-5.3-flash` sind es 23 Hoster, von denen einer auf
  2.048 Ausgabe-Tokens begrenzt ist. Der Preflight liest `/api/v1/models/{modèle}/endpoints`,
  schließt Hoster mit unter 8.000 Ausgabe-Tokens oder herabgestuftem Status aus und
  pinnt die übrigen mit `allow_fallbacks: false` fest.
- **Reasoning wird zum Ausgabetarif abgerechnet** — 107 Tokens gegenüber 2 bei
  einer „OK“-Antwort von `z-ai/glm-5.2`. Es ist standardmäßig deaktiviert; Modelle,
  die es erzwingen, erhalten die niedrigste Stufe, die sie akzeptieren, da der Standardwert des
  Katalogs das Ausgabelimit vor dem Ende der Übersetzung ausschöpfen könnte.
  `--reasoning_effort` bleibt vorrangig.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Das Kontextfenster stammt aus dem Katalog. Ein Modell mit unter 16.400 Tokens wird
  vor jedem Aufruf abgelehnt: 8.400 für den Prompt und das Segment, mindestens 8.000 für die Ausgabe.
- Ein im Katalog nicht vorhandener Slug, ein nicht erreichbarer Katalog oder das Fehlen
  eines Hosters, der das Limit einhält, stoppen den Befehl.
- `finish_reason=length` mit einer leeren Ausgabe bedeutet ein durch Reasoning verbrauchtes
  Budget, kein Abschneiden: Die Meldung unterscheidet dies.
- `--eco` ist wirkungslos.
- Variablen: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (Standard `https://openrouter.ai/api/v1`, `https://`
  erforderlich), `OPENROUTER_TIMEOUT` (Standard 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (Standard 30).

### Übersetzungshinweis

`--add_translation_note` fügt einen Hinweis hinzu, am `bottom` (Standard), `top` (nach dem
Frontmatter) oder `both` (`--note_position`), im Format `legacy` (Absatz in
Fettschrift, Standard) oder `marker` (`--note_format`). Das Format `marker` ist eine
unsichtbare Markdown-Referenzdefinition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
gefolgt von einem Zitatblock in Fettschrift: lesbar auf GitHub, beim Build durch ein
remark-Plugin nutzbar.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detaillierte Messungen

Alle Messungen sind tatsächlich mit `aipmt` durchgeführte Übersetzungen in
vierzehn Sprachen: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Geschrieben** zählt die Dateien, die die Guardrails passieren ließen; **Ohne
Abweichung** diejenigen, bei denen `scripts/compare_structure.py` nichts beanstandet — gleiche Anzahl an
Abschnitten, Untertiteln, Links, eindeutigen URLs, Codeblöcken,
Inline-Codes, Tabellenzeilen, Zitatblöcken und fettgedruckten Wörtern.

„Ohne Abweichung“ bedeutet „nichts erkannt“, nicht „identisch“: Der Vergleicher
zählt Elemente, ohne deren Inhalt zu lesen. Er meldet weder eine gelöschte Überschrift der
Ebene 4 noch ersetzten Text innerhalb eines Inline-Codes oder eine vertauschte
Flagge und beurteilt nicht die Sprache.

### Dichter Monitoring-Artikel, Modus `--news`

Eine Ausgabe des [KI-Monitors von jls42.org](https://jls42.org/fr/news):
589 Zeilen, 140 Links, 21 Abschnitte, 3 geschützte englische Zitate. Testreihe
vom 4. und 5. September 2026.

| Modell                                          | Zugriff            | Geschrieben | Ohne Abweichung | Median/Sprache |
| ----------------------------------------------- | ------------------ | ----------- | --------------- | -------------- |
| `gemini-3.7-flash`                              | Google-API         | 14/14       | ✅ **14/14**    | 1 min 18 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google-Abonnement  | 14/14       | ✅ **14/14**    | 3 min 14 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT-Abonnement | 14/14       | ✅ **14/14**    | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14       | ✅ **14/14**    | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14       | ✅ **14/14**    | 26 min 23 s    |
| `claude-sonnet-5`                               | Anthropic-API      | 14/14       | ⚠️ 11/14        | 6 min 31 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14       | ❌ 11/14        | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14       | ❌ 8/14         | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | lokal              | 10/14       | ❌ 7/14         | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral-API        | 11/14       | ❌ 5/14         | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14        | ❌ 3/14         | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok-Abonnement    | 1/14        | ❌ 1/14         | 23 min 11 s    |

Grok wurde am 9. September an einer anderen Ausgabe desselben Monitorings
(356 Zeilen) erneut gemessen: 9 von 14 Sprachen geschrieben, 8 ohne Abweichung.
Diese Zahl steht in der Übersichtstabelle oben. Drei abgebrochene Testreihen
sind nicht aufgeführt: `qwen3.5-27b` (9 Sprachen) und `kimi-k2.6` (4) aus
Mangel an Guthaben, `z-ai/glm-5.3-flash`, dessen zwei Fehlschläge auf eine
Reasoning-Einstellung zurückzuführen waren, die der Provider seither korrigiert
hat. Die OpenRouter-Zeilen wurden mit den Standardeinstellungen des Routers
gemessen, vor `--use_openrouter`; `z-ai/glm-5.2`, erneut mit dem mitgelieferten
Provider gemessen, liefert dasselbe 14/14. Die Zahlen wurden am 10. September
mit dem aktuellen Vergleichstool neu berechnet: `qwen3.8-flash` und
`qwen3.7-flash` gewinnen jeweils eine Sprache im Vergleich zur Erstveröffentlichung
hinzu, die anderen sind unverändert.

Die Zeile `--use_antigravity` wurde am 26. September am selben Artikel gemessen,
vier Übersetzungen parallel. Im Englischen entfernte das Modell die drei
französischen Übersetzungszeilen unter den Zitaten selbstständig, ohne Flaggen zu
erfinden, und die englischen Zitate blieben intakt: Die Fallback-Bereinigung
musste nicht eingreifen. Unter `--eco` (`gemini-3.7-flash-low`), bei nur vier
Sprachen (en, ja, ar, hi): 4 von 4 geschrieben, alle ohne Abweichung, 1 min 52 s
Median.

### README dieses Projekts, Standard-Markdown

Revision eingefroren am 9. September 2026: 785 Zeilen, 285 Inline-Codes, 40
Blockabschlüsse, 89 Tabellenzeilen. Vier Übersetzungen parallel.

| Modell                                          | Geschrieben | Ohne Abweichung | Median/Sprache | Was abweicht                                                               |
| ----------------------------------------------- | ----------- | --------------- | -------------- | -------------------------------------------------------------------------- |
| `gemini-3.7-flash`                              | 14/14       | ⚠️ 13/14        | 36 s           | ein Wort in Fettschrift (ja)                                               |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14       | ⚠️ 13/14        | 1 min 22 s     | ein Wort in Fettschrift (ko)                                               |
| `claude-sonnet-5`                               | 14/14       | ⚠️ 12/14        | 2 min 56 s     | ein Link (sv), ein Wort in Fettschrift (zh)                                |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14       | ⚠️ 12/14        | 6 min 46 s     | ein Wort in Fettschrift (ar, ja)                                           |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14       | ⚠️ 11/14        | 2 min 34 s     | ein Wort in Fettschrift (hi, ja, ko)                                       |
| `qwen/qwen3.7-flash`                            | 14/14       | ⚠️ 10/14        | 2 min 17 s     | 40 Inline-Codes auf Arabisch hinzugefügt; Fettschrift (hi, ja, ko)         |
| `mistral-large-latest`                          | 14/14       | ❌ 1/14         | 2 min 44 s     | ein verlorener Abschnitt (ar, hi, ko); Codeblöcke hinzugefügt (ja, ko, ro, zh) |

Zwei abgebrochene Testreihen sind nicht aufgeführt: Grok, CLI-Sitzung nach
zwölf Sprachen abgelaufen (elf ohne Abweichung), und `qwen3.8-flash`, HTTP 429
vom Hoster nach zwei. `opencode/mimo-v2.5-free` und `ollama/gpt-oss-20b-32k` wurden bei dieser
Revision nicht erneut gemessen; bei jener vom 4. und 5. September, die um 277
Zeilen kürzer war, schrieben sie jeweils 9 von 14 Übersetzungen, davon 7 bzw. 1
ohne Abweichung.

Die Zeile `--use_antigravity` wurde nicht auf der eingefrorenen Revision gemessen,
sondern am 26. September auf der mit Version 1.14.0 veröffentlichten: 600 Zeilen,
257 Inline-Codes, 30 Blockabschlüsse, 85 Tabellenzeilen. Da sie um 185 Zeilen
kürzer ist, lässt sie sich nicht direkt mit den anderen Zeilen vergleichen.

### Vier READMEs bekannter Projekte

FastAPI, Ollama, tldr-pages und Vue.js, unverändert von GitHub übernommen –
einfachere Dokumente als die beiden vorherigen. Die Testreihe richtete sich an
Modelle mit Schwierigkeiten; Gemini dient hierbei als Vergleichsreferenz.

| Modell                         | Umfang                     | Geschrieben | Ohne Abweichung |
| ------------------------------ | -------------------------- | ----------- | --------------- |
| `gemini-3.7-flash`             | 4 Projekte × 14 Sprachen   | 56/56       | ✅ **55/56**    |
| `opencode/mimo-v2.5-free`      | 4 Projekte × 14 Sprachen   | 55/56       | ❌ 47/56        |
| `grok-4.6` (Abonnement)   | 4 Projekte × ar, hi, ja, zh | 16/16       | ❌ 14/16        |
| `ollama/gpt-oss-20b-32k`       | 4 Projekte × ar, hi, ja, zh | 15/16       | ❌ 9/16         |

### Was diese Messungen nicht sind

- **Kein vollständiges Ranking**: OpenRouter allein bietet über vierhundert
  Modelle an, etwa fünfzehn wurden gemessen.
- **Richtwerte für die Dauer**: je nach Testreihe drei bis sechs parallele
  Übersetzungen, und der Durchsatz eines Anbieters schwankt im Tagesverlauf.
- **Zeitgebundene Momentaufnahmen**: Modelle verändern sich unter demselben
  Namen, und Ihre Dokumente sind nicht die unseren.

Um die Messung an Ihren eigenen Dokumenten auf einer eingefrorenen Kopie der
Datei zu wiederholen:

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

Die 28 Übersetzungen des Repositories (README und CHANGELOG, vierzehn Sprachen)
werden mit `./regen_translations.sh --force` neu generiert – standardmäßig Codex und
`gpt-5.6-sol` über das ChatGPT-Abonnement, vier parallel. `REGEN_PROVIDER` und
`REGEN_MODEL` ändern den Pfad: `antigravity` bleibt bei einem Abonnement,
dem von Google, und läuft ohne Ausnahmegenehmigung durch; eine kostenpflichtige
API (`openai`, `gemini`, `grok`, `openrouter`) wird
ohne `REGEN_ALLOW_PAID_API=1` verweigert; `REGEN_JOB_TIMEOUT` begrenzt jeden Job zeitlich
(600 s, 1.800 s bei Codex und Antigravity). Einzelheiten zu den Tools finden
sich in `CLAUDE.md`.

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** – persönlicher Blog, der in 15 Sprachen
  veröffentlicht wird. Dessen [tägliches KI-Monitoring](https://jls42.org/fr/news) wird jeden Tag
  mit diesem Werkzeug übersetzt und dient als Referenzdokument für die obigen
  Messungen.

## Autor

Julien LE SAUX
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Haftungsausschluss

Dieses Programm wird **ohne jegliche Gewährleistung** gemäß den Bestimmungen
der Abschnitte 15 und 16 der GPL v3 vertrieben: bereitgestellt „wie besehen“,
ohne Gewährleistung der Marktgängigkeit oder der Eignung für einen bestimmten
Zweck, und der Autor kann für Schäden, die aus seiner Nutzung entstehen, nicht
haftbar gemacht werden. Der Wortlaut der Lizenz hat Vorrang vor dieser
Zusammenfassung.

- **Vor der Veröffentlichung Korrektur lesen.** Die Schutzmechanismen decken
  Codeblöcke, Inline-Code, URLs, Anker und Zitate im Modus `--news` ab –
  weder Überschriften, Tabellen, Front Matter noch die Bedeutung Ihrer Sätze.
- **Ihre Dokumente werden an den ausgewählten Anbieter übermittelt**, gemäß
  dessen Nutzungsbedingungen und Datenschutzrichtlinien. Einige kostenlose
  Modelle können Ihre Interaktionen für das Training wiederverwenden, und die
  Bedingungen von Antigravity gestatten es Google, diese wiederzuverwenden und
  von Menschen überprüfen zu lassen, auch bei einem kostenpflichtigen
  Abonnement; ein lokales Modell ist die einzige Möglichkeit, bei der keine
  Daten Ihren Rechner verlassen.
- **API-Aufrufe werden Ihnen in Rechnung gestellt.** Dieses Programm deckelt
  die Kosten nicht: Ein langes Dokument, eine Wiederholung nach einem Fehler
  oder ein Modell mit intensivem Reasoning verursachen höhere Kosten.
- **Die veröffentlichten Messungen sind zeitgebundene Momentaufnahmen**, keine
  Garantien.

Die genannten Produkt- und Firmennamen gehören ihren jeweiligen Eigentümern.
Dieses Projekt ist mit keinem von ihnen verbunden.

**Artikel aus dem Französischen ins Deutsche übersetzt mit gemini-3.7-flash-medium.**

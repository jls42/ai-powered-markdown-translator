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
Zehn Möglichkeiten, ein Modell aufzurufen – fünf APIs, drei Abonnements ohne
nutzungsbasierte Abrechnung, zwei Router – und eine veröffentlichte Messung dessen,
was jedes Modell tatsächlich bewahrt.

## Auf einen Blick

- **Zehn Provider-Wege**: APIs von OpenAI, Mistral, Claude, Gemini und Grok;
  ChatGPT- (Codex), Grok- und Google-Abonnements (Antigravity) ohne nutzungsbasierte
  Abrechnung; Router OpenCode (Open Source, kostenlos oder lokal) und OpenRouter
  (mehr als 400 Modelle).
- **Keine Verfälschung durch verlorene Token**: Codeblöcke, Inline-Code,
  URLs, Anker und Zitate werden vor dem Aufruf durch Token ersetzt und
  bei der Rückgabe überprüft. Fehlt auch nur einer, wird die Datei nicht geschrieben.
- **Lange Dokumente**: Segmentierung entsprechend dem Kontextfenster des Modells.
- **`--news`-Modus**: geschützte englische Zitate und sprachspezifisch
  verwaltete Flaggen, für Monitoring- und News-Artikel.
- **`--eco`-Modus**: schnelle und kostengünstigere Modelle.
- Optionale **Übersetzungsnotiz**, oben, unten oder an beiden Stellen.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 oder neuer. Zur Installation aus dem Repository siehe
[Mitwirken](#mitwirken).

## Konfiguration

Schlüssel werden an drei Stellen gelesen, in absteigender Priorität; jede Stelle
füllt nur das aus, was die vorherige offen lässt.

|     | Wo                                            | Wofür                                 |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Umgebungsvariablen                            | CI, Container, einmalige Überschreibung |
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

`GEMINI_API_KEY` wird anstelle von `GOOGLE_API_KEY` akzeptiert. Die Benutzerdatei
folgt `XDG_CONFIG_HOME` (nur absoluter Pfad) und `%APPDATA%` unter
Windows. Ohne Schlüssel listet der Befehl alle drei Speicherorte auf.

**Die `.env` eines Projekts kann weder Aufrufe umleiten noch das ausgeführte
Programm bestimmen.** Sie liefert Schlüssel, niemals ein Ziel oder ein Binary:
Jede Variable mit `_BASE_URL`, `_API_BASE`, `_ENDPOINT` oder `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, Proxys (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), Zertifikatsspeicher (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) und `XDG_CONFIG_HOME` /
`APPDATA` werden darin mit einer Warnung ignoriert. Ein geklontes Repository darf
weder Ihren Schlüssel abfangen noch Sie dazu bringen, bei der ersten Übersetzung
sein eigenes Programm auszuführen. Diese Datei wird zudem ohne Interpolation gelesen:
`NOM=${OPENAI_API_KEY}` kopiert den Schlüssel darin nicht. Setzen Sie diese Variablen in
der Umgebung oder in `~/.config/aipmt/.env`.

Optionale Variablen: `XAI_BASE_URL` (Standard `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (Sekunden pro Aufruf, Standard 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(Standard 600), `GROK_BIN`, `GROK_HOME` (Standard `~/.grok`), `GROK_TIMEOUT`
(Standard 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (Standard 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (Standard 600), `OPENROUTER_BASE_URL`
(`https://` erforderlich), `OPENROUTER_TIMEOUT` (Standard 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (Standard 30). Jede wird im Abschnitt ihres Providers ausführlich
beschrieben.

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
mit `--include_model` ergibt es `document-es-gpt-5.6-terra.md`. Die Dateiendung wird
immer zu `.md` – `article.mdx` wird zu `article-en.md` – außer mit
`--keep_filename`, wodurch der ursprüngliche Name beibehalten wird. Eine bereits vorhandene
Übersetzung wird ohne `--force` übersprungen.

Exit-Codes: `0`, wenn alles erfolgreich war oder übersprungen wurde, `1`, wenn mindestens eine Datei
fehlgeschlagen ist (Auflistung auf der Standardfehlerausgabe), `2`, wenn die Konfiguration die Ursache ist.
Eine fehlgeschlagene Datei wird niemals geschrieben, selbst wenn das Schreiben selbst fehlschlägt:
Der Inhalt wird daneben geschrieben und anschließend umbenannt. Ein erneutes Ausführen genügt.

## Welches Modell wählen?

Gemessen an zwei realen Dokumenten, die von jedem Modell in dieselben vierzehn Sprachen
übersetzt wurden. **Die Zahl gibt an, in wie vielen von vierzehn Sprachen die
Übersetzung geschrieben wird und nichts von der Quelle abweicht.**

| Modell               | Zugriffsmethode                   | Dichter Monitoring-Artikel | Diese README | Was abweicht und in wie vielen Sprachen                                                                                               |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.8 Flash** | Google-Abonnement (Antigravity)   | ✅ 14/14                | ✅ 14/14     | nichts, bei keinem der beiden Dokumente                                                                                               |
| **Gemini 3.7 Flash** | Google-API-Schlüssel              | ✅ 14/14                | ⚠️ 13/14     | 1 von 14 Sprachen: ein fettgedrucktes Wort mehr (ja)                                                                                  |
| **Gemini 3.7 Flash** | Google-Abonnement (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 1 von 14 Sprachen: ein fettgedrucktes Wort weniger (ko)                                                                               |
| **GPT-5.6 Sol**      | ChatGPT-Abonnement oder OpenAI-Schlüssel | ✅ 14/14          | ⚠️ 12/14     | 2 von 14 Sprachen: ein fettgedrucktes Wort weniger (ar, ja)                                                                           |
| **GLM-5.2**          | OpenRouter-Schlüssel              | ✅ 14/14                | ⚠️ 11/14     | 3 von 14 Sprachen: ein fettgedrucktes Wort weniger (hi, ja, ko)                                                                       |
| Claude Sonnet 5      | Anthropic-API-Schlüssel           | ⚠️ 11/14                | ⚠️ 12/14     | 3 Sprachen beim Artikel: ein zusätzlicher Codeblock aufgetaucht (es, de, hi); 2 bei dieser README: ein Link ohne Markup (sv), ein fettgedrucktes Wort (zh) |
| Qwen 3.7 Flash       | OpenRouter-Schlüssel              | ❌ 8/14                 | ⚠️ 10/14     | 1 Sprache beim Artikel abgelehnt, 5 weitere weichen ab; bei dieser README rund vierzig Wörter in `code` gesetzt (ar)                  |
| Grok 4.6             | Grok-Abonnement                   | ❌ 8/14                 | nicht bewertet | 5 von 14 Sprachen abgelehnt mangels zurückgegebener Inline-Codes und URLs; Niederländisch weicht in allem ab                          |
| GPT-OSS 20B          | lokales Modell (Ollama)           | ❌ 7/14                 | nicht erneut gemessen | 4 von 14 Sprachen abgelehnt: Das Modell hinterließ französische Passagen, die Schutzprüfung stoppte sie                              |
| MiMo v2.5 (kostenlos) | OpenCode Zen, ohne Konto          | ❌ 11/14                | nicht erneut gemessen | 1 Sprache abgelehnt; ein Abschnitt auf Polnisch verloren gegangen                                                                    |
| Mistral Large        | Mistral-API-Schlüssel             | ❌ 5/14                 | ❌ 1/14      | **ein ganzer Abschnitt verschwindet**: 1 Sprache beim Artikel (hi), 3 bei dieser README (ar, hi, ko) – und 3 Sprachen beim Artikel abgelehnt |
| DeepSeek V4 Flash    | OpenRouter-Schlüssel              | ❌ 3/14                 | nicht erneut gemessen | 10 von 14 Sprachen abgelehnt; 37 Minuten pro Sprache                                                                                  |

|     | Bedeutung des Symbols                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alle vierzehn Sprachen übersetzt, und nichts weicht von der Quelle ab                                                                                                                                 |
| ⚠️  | alle vierzehn Sprachen übersetzt; was abweicht, ist reines **Markup** – ein fettgedrucktes Wort, ein `code`, ein Link, der seine eckigen Klammern verliert. Kein Text, keine URL, kein Codeblock und kein Abschnitt fehlt |
| ❌  | mindestens eine Sprache konnte nicht übersetzt werden – die Datei wurde abgelehnt, nicht geschrieben – **oder** in einer geschriebenen Datei fehlt Inhalt                                            |

Wichtige Erkenntnisse:

- **Eine abgelehnte Übersetzung ist keine beschädigte Übersetzung.** Wenn bei der Rückgabe
  ein Token fehlt, wird die Datei nicht geschrieben und die Sprache gilt als
  abgelehnt. Genau das passiert Grok beim Artikel: vier Inline-Codes und
  drei URLs gingen bereits im ersten Segment bei den fünf nicht-lateinischen Schriftsystemen verloren.
- **Dieses Fangnetz deckt weder Überschriften, Tabellen, Frontmatter noch den
  eigentlichen Text ab.** Ein Modell, das einen Abschnitt entfernt, liefert eine Datei,
  die das Tool anstandslos schreibt – so der Fall bei Mistral. Diese Elemente
  können nicht durch Token ersetzt werden, und die aktuellen Schutzprüfungen
  kontrollieren sie nicht; `scripts/compare_structure.py` erkennt einen verlorenen Abschnitt erst im Nachhinein.
- **Grok hat keine Bewertung für diese README**: Die CLI-Sitzung lief nach zwölf
  Sprachen ab, davon elf ohne Abweichung. Ein abgebrochener Durchlauf wird nicht bewertet.
- **Die Dichte des Dokuments wiegt schwerer als die Sprache.** Grok bewährt sich bei
  gewöhnlichen READMEs und steigt bei einem stark verlinkten Artikel aus, selbst auf
  Niederländisch.

Daten und Dokumente: Die Spalte „Diese README“ wurde am 9. September 2026
anhand einer eingefrorenen Version dieser Datei gemessen (785 Zeilen, 285 Inline-Codes, 89 Tabellenzeilen),
die seither überarbeitet wurde – mit Ausnahme der beiden Antigravity-Zeilen, gemessen am
26. September anhand der mit 1.14.0 veröffentlichten, kürzeren Version (600 Zeilen,
257 Inline-Codes, 85 Tabellenzeilen). Die Spalte „Dichter Monitoring-Artikel“ stammt
aus dem Durchlauf vom 4. und 5. September auf einem 589-zeiligen Artikel, mit Ausnahme
der Grok-Zeile, die am 9. September auf einer anderen Ausgabe desselben Newsletters
erneut gemessen wurde, sowie der beiden Antigravity-Zeilen, gemessen am 26. September auf
demselben Artikel.
Die vollständigen Tabellen, Laufzeiten und das Protokoll finden sich in
[Detaillierte Messungen](#detaillierte-messwerte).

## Alle Optionen

| Option                   | Description                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Einzelne zu übersetzende Markdown-Datei (Alternative zu `--source_dir`)                                             |
| `--source_dir`           | Quellverzeichnis mit den Markdown-Dateien (Standard: `content/posts`)                                   |
| `--target_dir`           | Ausgabeverzeichnis für die übersetzten Dateien (Standard: `traductions_en`)                                    |
| `--source_lang`          | Ausgangssprache (Standard: `fr`)                                                                                  |
| `--target_lang`          | Zielsprache (Standard: `en`)                                                                                   |
| `--model`                | Spezifisches zu verwendendes Modell                                                                                  |
| `--eco`                  | Kostengünstige Modelle verwenden                                                                              |
| `--use_mistral`          | Mistral AI API verwenden                                                                                     |
| `--use_claude`           | Claude API verwenden                                                                                         |
| `--use_gemini`           | Gemini API verwenden                                                                                         |
| `--use_grok`             | xAI API (Grok) verwenden – erfordert `XAI_API_KEY`                                                           |
| `--use_codex`            | Codex-CLI über das ChatGPT-Abonnementkontingent verwenden                                                    |
| `--use_grok_cli`         | Grok-CLI über das Grok-Abonnementkontingent verwenden                                                        |
| `--use_antigravity`      | Antigravity-CLI (`agy`) über das Abonnementkontingent von Google AI Pro oder Ultra verwenden                       |
| `--use_opencode`         | OpenCode (Open Source) mit dem in OpenCode konfigurierten Provider verwenden; erfordert `--model provider/modèle` |
| `--use_openrouter`       | OpenRouter verwenden – erfordert `OPENROUTER_API_KEY` und `--model fournisseur/modèle`                          |
| `--force`                | Neuübersetzung erzwingen                                                                                       |
| `--keep_filename`        | Ursprünglichen Dateinamen beibehalten                                                                          |
| `--news`                 | News-Modus: schützt englische Zitate, verwaltet Flaggen je Sprache                                      |
| `--add_translation_note` | Übersetzungsnotiz hinzufügen                                                                                |
| `--note_position`        | Position der Notiz: `top`, `bottom` (Standard) oder `both`                                                     |
| `--note_format`          | Format der Notiz: `legacy` (Standard, fetter Absatz) oder `marker`                                            |
| `--include_model`        | Modellnamen in der Ausgabedatei angeben                                                            |
| `--reasoning_effort`     | GPT-5.x Reasoning-Aufwand: `none`/`low`/`medium`/`high`/`xhigh`                                         |

Die neun `--use_*`-Flags schließen sich gegenseitig aus: Die Kombination von zweien
wird abgelehnt.

## Provider

### Per API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` wechselt auf die kostengünstige Stufe jedes Anbieters.

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
| OpenCode    | `--model provider/modèle` erforderlich                 | ebenso – `--eco` wirkungslos |
| OpenRouter  | `--model fournisseur/modèle` erforderlich              | ebenso – `--eco` wirkungslos |

### Über das ChatGPT-Abonnement: `--use_codex`

Steuert die offizielle Codex-CLI: Die Übersetzung wird auf das Kontingent des
ChatGPT-Abonnements angerechnet, ohne API-Schlüssel oder nutzungsbasierte
Abrechnung.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Die Binärdatei wird in `CODEX_BIN`, dann im `PATH` und schließlich im Paket
  `openai-codex-cli-bin` gesucht. `~/.codex/auth.json` wird niemals gelesen.
- `OPENAI_API_KEY` und `CODEX_API_KEY` werden aus der Umgebung des
  Unterprozesses entfernt: Ein vorhandener Schlüssel führt niemals zu einem Wechsel zur API.
- Jedes Segment kostet mindestens eine „Nachricht“ des 5-Stunden-Fensters – zwei,
  wenn die Validierung fehlschlägt und es wiederholt wird. OpenAI gibt als
  Schätzung 250–2.000 Nachrichten/5 Std. für `gpt-5.6-luna` (`--eco`) und
  10–100 für `gpt-5.6-sol` bei einem Plus-Tarif an.
- `--model gpt-5.6-terra` und `--model gpt-5.6-luna` laufen ebenfalls über
  das Abonnement. Ein Modell, für das der Account nicht berechtigt ist, liefert einen 400-Fehler „model is
  not supported when using Codex with a ChatGPT account“.
- Langsamer als eine API, und der Abstand wächst mit der Dokumentgröße: bei dieser README
  im Median 6 Min. 46 Sek. pro Sprache mit `gpt-5.6-sol`, verglichen mit 36 Sek. für
  `gemini-3.7-flash`.
- In CI verweigert (`CI` oder `GITHUB_ACTIONS` gesetzt): Das Abonnement authentifiziert
  sich über eine persönliche Sitzungsdatei, die auf einem geteilten Runner
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

- **Schwächere Isolation als bei Codex.** Die OS-Sandbox von Grok greift
  auf vielen modernen Linux-Rechnern nicht (AppArmor, Sockets von
  Container-Runtimes), und ein Profil, das nicht angewendet werden kann, startet stillschweigend
  ohne Isolation. Das Skript fordert daher standardmäßig kein Profil an, weist darauf hin und
  stützt sich auf die `--deny`-Regeln der CLI, einschließlich des Catch-Alls `*` — der
  einzigen Schicht, die den Start verweigert, anstatt den Schutz wortlos aufzuheben.
  `GROK_TRANSLATE_SANDBOX=read-only` erzwingt die OS-Sandbox, und der Start
  schlägt fehl, wenn das System dies nicht gewährleisten kann.
- Das Kontingent ist wöchentlich, wird mit Chat, Imagine und Voice geteilt, und
  kein Befehl erlaubt es, dieses abzufragen: Ein Batch-Lauf kann das Konversationskontingent
  unbemerkt aufbrauchen.
- Variablen: `GROK_BIN`, `GROK_HOME` (CLI-Verzeichnis, Standard `~/.grok`),
  `GROK_TIMEOUT` (Standard 900), `GROK_TRANSLATE_SANDBOX`.

### Über das Google-Abonnement: `--use_antigravity`

Dasselbe Prinzip mit `agy`, der offiziellen CLI von Antigravity: Wer für Google
AI Pro oder Ultra zahlt, dessen Übersetzung wird auf das Abonnement-Kontingent angerechnet,
anstatt tokenbasiert abgerechnet zu werden. Dies ist der einzige Weg zu diesem Kontingent: Die Gemini CLI
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
  Mehrere seiner Variablen lenken einen Aufruf ohne Anzeige um (gemessen:
  eine sendet das Dokument an ein Drittanbieter-Gateway, eine andere an ein kostenpflichtiges
  Google Cloud-Projekt), und eine Sperrliste übersah bei jeder Überprüfung welche.
  Vor jedem Segment muss `agy -p /config`, das kein Kontingent verbraucht,
  zeigen, dass kostenpflichtige KI-Guthaben deaktiviert sind, ohne API-Schlüssel oder Google Cloud-Projekt — ein
  Fehlen dieser Einstellung gilt als Ablehnung —, andernfalls wird nichts übersetzt; das Protokoll
  jedes Aufrufs muss anschließend das Abonnement bestätigen (`authMethod=consumer`), andernfalls
  wird die Antwort abgelehnt.
- **Isolation.** Jeder Aufruf läuft in einem privaten, temporären
  Home-Verzeichnis mit einem Übersetzungsmagenten ohne Werkzeuge: Ihre Einstellungen, Regeln,
  Plugins, MCP-Server und agy-Hooks gelangen nicht hinein, nichts wird Ihrem
  Verlauf hinzugefügt, und der Login verbleibt im Schlüsselbund, den aipmt niemals ausliest.
  Wird der Agent nicht gefunden, fällt agy stillschweigend auf seinen Coding-Agenten
  und dessen Werkzeuge zurück: Eine vollständige Zeile im Protokoll muss den korrekten Agenten bestätigen — ein
  Dokument, das diese Nachricht zitiert, ersetzt sie nicht —, andernfalls erfolgt eine Ablehnung.
- **Plattformen**: Linux, innerhalb einer Sitzung mit Schlüsselbund (D-Bus-Sitzungsbus,
  Secret Service); macOS wird akzeptiert, wurde jedoch nicht gemessen. Abgelehnt
  unter Windows, wo agy die Variablen zur Isolation der Aufrufe nicht liest, und
  unter Linux ohne Sitzungsbus — SSH-Sitzung, Container, Server: agy speichert
  sein Token dort in einer Datei unter `~/.gemini`, die durch die Isolation verdeckt wird. Die
  Ablehnung erfolgt vor jeglichem Start samt Begründung, anstatt eine Minute
  auf einen Login-Code zu warten.
- **Modelle**: diejenigen von `agy models`. Die Gemini-Modelle tragen den Aufwand im Namen
  (`gemini-3.8-flash-medium`…): Ein Name ohne Suffix wird vor dem Aufruf abgelehnt,
  und `--reasoning_effort` bleibt wirkungslos. Standardmäßig `gemini-3.8-flash-medium`,
  und `gemini-3.7-flash-low` bei `--eco`; die Testläufe, mit denen sie festgelegt wurden, sind
  unter [Detaillierte Messwerte](#detaillierte-messwerte) beschrieben. Claude und GPT-OSS
  haben ihr eigenes, deutlich kleineres Kontingent: etwa 1 % des 5-Stunden-Fensters
  pro gemessenem Aufruf, gegenüber 0,05 % bei Flash.
- **Kontingent**: pro Gruppe ein 5-Stunden-Fenster und ein wöchentliches Fenster,
  anteilig nach Tokenkosten. Gemessen auf dem Account des Autors: etwa
  16 Punkte des 5-Stunden-Fensters pro Million Quellzeichen bei
  `gemini-3.8-flash-medium`, 14 bei `gemini-3.7-flash-medium` und 7 bis 8 bei
  geringem Aufwand — eine README mit 40.000 Zeichen kostet somit etwas mehr als einen
  halben Punkt. Das wöchentliche Limit hängt von der Tarifstufe ab. Wiederholungsversuche
  richten sich danach, was agy als wiederholbar einstuft; andernfalls wird ein erschöpftes Fenster niemals
  erneut versucht: Es lässt jede Datei bis zu dem von `/usage` angezeigten
  Reset fehlschlagen.
- **Langsamer als die API**: beim dichten Benchmark-Artikel im Median 3 Min. 59 Sek. pro
  Sprache bei `gemini-3.8-flash-medium` und 3 Min. 14 Sek. bei
  `gemini-3.7-flash-medium`, verglichen mit 1 Min. 18 Sek. für Gemini 3.7 Flash über die API.
- **Abbruch**: Strg-C oder ein geschlossenes Terminal stoppen agy zusammen mit dem
  Befehl, anstatt ihn seinen Durchlauf auf Kosten Ihres Kontingents beenden zu lassen; dasselbe
  gilt für Codex, Grok CLI und OpenCode. Unter `nohup` läuft die Übersetzung weiter.
- In CI verweigert (`CI` oder `GITHUB_ACTIONS` gesetzt): Der Login liegt in einem
  persönlichen Schlüsselbund. Auf einem Runner: `--use_gemini` mit `GOOGLE_API_KEY`.
- Variablen: `AGY_BIN` (sonst `PATH`, dann `~/.local/bin/agy`),
  `AGY_TIMEOUT` (Sekunden pro Segment einschließlich Start, Standard 900).

**Nutzungsbedingungen: Sie haften mit Ihrem Account.** Die
[Nutzungsbedingungen von Antigravity](https://antigravity.google/terms) (Abschnitt 6) und deren
[FAQ](https://antigravity.google/docs/faq/) untersagen den Zugriff auf den Dienst
über Drittanbietersoftware unter Verwendung des Antigravity-Logins — Claude Code,
OpenClaw und OpenCode werden dort genannt —, unter Androhung einer Kontosperrung. aipmt
liest das Token weder aus noch verwendet es dieses wieder: Es startet die offizielle Binärdatei im
[Headless-Modus](https://antigravity.google/docs/cli/headless/), den Google
für Skripte und CI dokumentiert. Ein Google-Mitarbeiter bezeichnete es als „üblich“,
`agy -p` aus einem lokalen Skript für die eigene Arbeit aufzurufen
([offizielles Forum, 25. September 2026, unverbindliche Antwort](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
kein offizieller Text regelt den Fall eines distribuierten Werkzeugs wie diesem.

**Nur für öffentliche Dokumente.** Gemäß Abschnitt 5 derselben Bedingungen können die
Kommunikationsdaten — Prompts, Antworten, Metadaten — dazu verwendet werden, die
Produkte und das maschinelle Lernen von Google zu verbessern, und von Menschen
überprüft werden, auch bei einem kostenpflichtigen Abonnement. Die Abmeldung erfolgt über die Einstellung
`enableTelemetry` mit undokumentierter Wirkung, die aipmt nicht setzt; Ihre agy-Einstellungen
werden nicht in dessen isolierte Umgebung übernommen. Verarbeiten Sie darüber keine vertraulichen Inhalte.

### Zum Anbieter eigener Wahl: `--use_opencode`

[OpenCode](https://opencode.ai) ist ein quelloffener Coding-Agent (MIT), der
Anfragen an die darin konfigurierten Anbieter weiterleitet: API-Schlüssel, Abonnement,
OpenCode Zen-Gateway (kostenlose Modelle, ohne Account) oder lokales Modell. Zwei
Wege wurden hier durchgehend gemessen: Zen und Ollama.

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

`--model` ist erforderlich: Ohne diesen Parameter würde OpenCode auf ein kostenloses Modell zurückgreifen,
dessen Daten für das Training genutzt werden können, und diese Entscheidung wird Ihnen nicht
abgenommen.

Isolation bei jedem Aufruf:

- eine Inline-Konfiguration mit Vorrang vor Ihrer eigenen definiert einen Agenten `aipmt`,
  dessen Werkzeuge alle verweigert werden (`permission: { "*": "deny" }`), Sitzungsfreigabe
  deaktiviert, `--pure`, niemals `--auto`;
- temporäres und leeres Arbeitsverzeichnis, `OPENCODE_DISABLE_PROJECT_CONFIG` und
  `OPENCODE_DISABLE_CLAUDE_CODE` gesetzt — ohne diese injiziert OpenCode die
  `AGENTS.md` des aktuellen Verzeichnisses sowie `~/.claude/CLAUDE.md` in den Prompt. Die
  globale `~/.config/opencode/AGENTS.md` wird weiterhin injiziert, da OpenCode kein
  Ausschließen erlaubt;
- Ausgabevertrag: Exit-Code 0, kein `error`-Ereignis, kein Werkzeugaufruf,
  letzter Schritt mit `stop`, nicht-leerer Text und tatsächlich
  geladener Agent `aipmt` — ein unbekannter `--agent` lässt OpenCode nicht fehlschlagen,
  sondern fällt stillschweigend auf den Coding-Agenten zurück;
- es wird kein Schlüssel von `aipmt` übergeben, außer `OPENCODE_API_KEY`, dem Schlüssel
  von OpenCode selbst. Die Anbieter werden in OpenCode konfiguriert, nicht in
  der `.env` von `aipmt`.

Wissenswertes:

- Die kostenlosen Modelle von Zen sind wechselhaft, haben undokumentierte Limits und
  ihre Daten können für das Training genutzt werden: geeignet für öffentliche
  Dokumentationen, nicht für private Inhalte.
- Ein lokales Modell muss mindestens 16k Tokens Kontext bieten, da die Segmente
  bis zu 16.000 Zeichen umfassen. Ollama konfiguriert oft 4.096: nutzen
  Sie ein `Modelfile` mit `PARAMETER num_ctx 32768`.
- `--eco` ist wirkungslos; `--reasoning_effort` wird unverändert als
  `--variant` von OpenCode weitergegeben.
- OpenCode protokolliert jede Sitzung in `~/.local/share/opencode/`.
- Variablen: `OPENCODE_BIN` (sonst `PATH`, dann `~/.opencode/bin/opencode`),
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

`reasoningEffort: "none"` deaktiviert das Reasoning (Denkprozess), das Ollama bei diesen
Modellen standardmäßig aktiviert und das eine Modelfile nicht abschalten kann. Gemessen an einem Satz aus
sechs Wörtern: 919 Tokens für das Reasoning und 68 Sekunden ohne diese Option, 9 Tokens mit ihr.

### Zu über 400 Modellen: `--use_openrouter`

OpenRouter ist ein nach Verbrauch abgerechneter Router mit einem zentralen Guthaben für
von Dritten gehostete Modelle — darunter offene chinesische Modelle, die kein
anderer Anbieter hier bereitstellt.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` ist erforderlich. Ein Preflight-Check vor jeder Abrechnung regelt
zwei Besonderheiten des Routings:

- **Dasselbe Modell wird von Dutzenden Hostern mit unterschiedlichen Limits bereitgestellt** —
  bei `z-ai/glm-5.3-flash` sind es 23 Hoster, von denen einer auf
  2.048 Ausgabetokens gedeckelt ist. Der Preflight-Check liest `/api/v1/models/{modèle}/endpoints` aus,
  schließt Hoster mit weniger als 8.000 Ausgabetokens oder herabgesetztem Status aus und
  pinnt die übrigen mittels `allow_fallbacks: false` fest.
- **Reasoning wird zum Ausgabetarif abgerechnet** — 107 Tokens gegenüber 2 bei
  einer Antwort „OK“ von `z-ai/glm-5.2`. Es ist standardmäßig deaktiviert; Modelle,
  die es erzwingen, erhalten die geringste Aufwandsstufe, die sie akzeptieren, da der
  Katalogstandard die Ausgabe vor dem Ende der Übersetzung überlaufen lassen könnte.
  `--reasoning_effort` bleibt vorrangig.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Das Kontextfenster stammt aus dem Katalog. Ein Modell mit weniger als 16.400 Tokens wird
  vor jedem Aufruf abgelehnt: 8.400 für Prompt und Segment, mindestens 8.000
  für die Ausgabe.
- Ein Slug, der nicht im Katalog vorhanden ist, ein nicht erreichbarer Katalog oder das Fehlen
  eines Hosters, der das Limit erfüllt, brechen den Befehl ab.
- `finish_reason=length` mit leerer Ausgabe bedeutet, dass das Budget durch das
  Reasoning aufgebraucht wurde, nicht durch eine Kürzung: Die Meldung unterscheidet dies.
- `--eco` ist wirkungslos.
- Variablen: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (Standard `https://openrouter.ai/api/v1`, `https://`
  erforderlich), `OPENROUTER_TIMEOUT` (Standard 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (Standard 30).

### Übersetzungshinweis

`--add_translation_note` fügt einen Hinweis hinzu, als `bottom` (Standard), `top` (nach dem
Frontmatter) oder `both` (`--note_position`), im Format `legacy` (Absatz in
Fettschrift, Standard) oder `marker` (`--note_format`). Das Format `marker` ist eine
unsichtbare Markdown-Referenzdefinition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
gefolgt von einem Zitat in Fettschrift: lesbar auf GitHub, beim Build von einem
remark-Plugin nutzbar.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detaillierte Messwerte

Alle Messungen sind real durchgeführte Übersetzungen mit `aipmt` in
vierzehn Sprachen: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Geschrieben** zählt die Dateien, die von den Schutzprüfungen durchgelassen wurden; **Ohne
Abweichung** diejenigen, bei denen `scripts/compare_structure.py` nichts beanstandet — gleiche Anzahl an
Abschnitten, Zwischenüberschriften, Links, eindeutigen URLs, Code-Blöcken,
Inline-Code, Tabellenzeilen, Zitatblöcken und fettgedruckten Wörtern.

„Ohne Abweichung“ bedeutet „nichts erkannt“, nicht „identisch“: Der Vergleicher
zählt Elemente, ohne deren Inhalt zu lesen. Er meldet weder eine gelöschte Überschrift der
Ebene 4 noch den ersetzten Text eines Inline-Codes, eine vertauschte Flagge
oder einen internen Link, der mit einer Klammer zu viel wiedergegeben wurde,
`[texte]((#ancre))`, wodurch er ins Leere führt — und er beurteilt nicht die
sprachliche Qualität.

### Dichter Monitoring-Artikel, Modus `--news`

Eine Ausgabe des [KI-Monitors auf jls42.org](https://jls42.org/fr/news):
589 Zeilen, 140 Links, 21 Abschnitte, 3 geschützte englische Zitate. Testreihe
vom 4. und 5. September 2026.

| Modell                                          | Zugang             | Geschrieben | Ohne Abweichung | Median/Sprache |
| ----------------------------------------------- | ------------------ | ----------- | --------------- | -------------- |
| `gemini-3.7-flash`                              | Google-API         | 14/14       | ✅ **14/14**    | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google-Abonnement  | 14/14       | ✅ **14/14**    | 3 min 59 s     |
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

Grok wurde am 9. September anhand einer anderen Ausgabe desselben Monitors
neu gemessen (356 Zeilen): 9 von 14 Sprachen geschrieben, 8 ohne Abweichung.
Diese Zahl steht in der Übersichtstabelle oben. Drei abgebrochene Kampagnen sind
nicht aufgeführt: `qwen3.5-27b` (9 Sprachen) und `kimi-k2.6` (4) mangels
Guthaben, `z-ai/glm-5.3-flash`, dessen zwei Fehler auf eine Reasoning-Einstellung
zurückzuführen waren, die der Provider seither korrigiert hat. Die OpenRouter-Zeilen
wurden mit den Standardeinstellungen des Routers gemessen, vor `--use_openrouter`;
`z-ai/glm-5.2`, neu gemessen mit dem mitgelieferten Provider, erzielt dasselbe 14/14.
Die Zahlen wurden am 10. September mit dem aktuellen Vergleichstool neu berechnet:
`qwen3.8-flash` und `qwen3.7-flash` gewinnen jeweils eine Sprache gegenüber der
Erstveröffentlichung hinzu, die übrigen bleiben unverändert.

Die Zeilen `--use_antigravity` wurden am 26. September anhand desselben
Artikels gemessen, vier Übersetzungen parallel: `gemini-3.7-flash-medium` am Vormittag,
`gemini-3.8-flash-medium` am Nachmittag. Im Englischen entfernte jedes Modell die drei Zeilen
französischer Übersetzung unter den Zitaten selbstständig, ohne Flags zu erfinden,
und die englischen Zitate blieben intakt: Die Fallback-Bereinigung musste nicht
eingreifen. Bei `--eco` (`gemini-3.7-flash-low`), bei nur vier Sprachen
(en, ja, ar, hi): 4 von 4 geschrieben, alle ohne Abweichung, Median 1 min 52 s.
Gegenprobe am selben Tag anhand einer neueren Ausgabe des Monitors, jener vom
25. September (438 Zeilen, 2 englische Zitate), außerhalb des Blogs übersetzt
durch `gemini-3.7-flash-medium`: 14 von 14 geschrieben, alle ohne Abweichung, 87 bis
128 s pro Sprache.

### README dieses Projekts, Standard-Markdown

Eingefrorene Revision vom 9. September 2026: 785 Zeilen, 285 Inline-Code-Elemente,
40 Block-Abschlüsse, 89 Tabellenzeilen. Vier Übersetzungen parallel.

| Modell                                          | Geschrieben | Ohne Abweichung | Median/Sprache | Was abweicht                                                             |
| ----------------------------------------------- | ----------- | --------------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14       | ✅ 14/14        | 1 min 43 s     | nichts                                                                   |
| `gemini-3.7-flash`                              | 14/14       | ⚠️ 13/14        | 36 s           | ein fettgedrucktes Wort (ja)                                             |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14       | ⚠️ 13/14        | 1 min 22 s     | ein fettgedrucktes Wort (ko)                                             |
| `claude-sonnet-5`                               | 14/14       | ⚠️ 12/14        | 2 min 56 s     | ein Link (sv), ein fettgedrucktes Wort (zh)                              |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14       | ⚠️ 12/14        | 6 min 46 s     | ein fettgedrucktes Wort (ar, ja)                                         |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14       | ⚠️ 11/14        | 2 min 34 s     | ein fettgedrucktes Wort (hi, ja, ko)                                     |
| `qwen/qwen3.7-flash`                            | 14/14       | ⚠️ 10/14        | 2 min 17 s     | 40 Inline-Codes auf Arabisch hinzugefügt; Fettdruck (hi, ja, ko)          |
| `mistral-large-latest`                          | 14/14       | ❌ 1/14         | 2 min 44 s     | ein verlorener Abschnitt (ar, hi, ko); Codeblöcke hinzugefügt (ja, ko, ro, zh) |

Zwei abgebrochene Kampagnen sind nicht aufgeführt: Grok, CLI-Sitzung nach
zwölf Sprachen abgelaufen (elf ohne Abweichung), und `qwen3.8-flash`, HTTP 429
seines Hosters nach zwei. `opencode/mimo-v2.5-free` und `ollama/gpt-oss-20b-32k`
wurden auf dieser Revision nicht neu gemessen; auf jener vom 4. und 5. September,
die um 277 Zeilen kürzer war, schrieben sie jeweils 9 von 14 Übersetzungen, davon 7
und 1 ohne Abweichung.

Die Zeilen `--use_antigravity` wurden nicht anhand der eingefrorenen Revision gemessen,
sondern am 26. September anhand der mit Version 1.14.0 veröffentlichten: 600 Zeilen,
257 Inline-Codes, 30 Block-Abschlüsse, 85 Tabellenzeilen. Da sie um 185 Zeilen
kürzer ist, lässt sie sich nicht 1:1 mit den anderen Zeilen vergleichen; die beiden
Antigravity-Zeilen lassen sich jedoch untereinander vergleichen. Bei den internen
Links, die das Vergleichstool nicht prüft, behielt `gemini-3.8-flash-medium` diese
in allen vierzehn Sprachen intakt, während `gemini-3.7-flash-medium` sie auf Italienisch
beschädigte.

### Vier READMEs bekannter Projekte

FastAPI, Ollama, tldr-pages und Vue.js, unverändert von GitHub übernommen –
einfachere Dokumente als die beiden vorherigen. Die Kampagne zielte auf Modelle
mit Schwierigkeiten ab; Gemini dient hier als Vergleichsmaßstab.

| Modell                    | Umfang                     | Geschrieben | Ohne Abweichung |
| ------------------------- | -------------------------- | ----------- | --------------- |
| `gemini-3.7-flash`        | 4 Projekte × 14 Sprachen   | 56/56       | ✅ **55/56**    |
| `opencode/mimo-v2.5-free` | 4 Projekte × 14 Sprachen   | 55/56       | ❌ 47/56        |
| `grok-4.6` (Abonnement)   | 4 Projekte × ar, hi, ja, zh | 16/16       | ❌ 14/16        |
| `ollama/gpt-oss-20b-32k`  | 4 Projekte × ar, hi, ja, zh | 15/16       | ❌ 9/16         |

### Was diese Messungen nicht sind

- **Keine vollständige Rangliste**: OpenRouter allein bietet über vierhundert
  Modelle, gemessen wurden etwa fünfzehn.
- **Richtwerte für die Dauer**: je nach Testreihe drei bis sechs parallele Übersetzungen,
  und der Durchsatz eines Anbieters schwankt im Tagesverlauf.
- **Zeitpunktbezogene Beobachtungen**: Modelle ändern sich unter demselben Namen, und Ihre
  Dokumente sind nicht die unseren.

Um die Messung anhand Ihrer Dokumente auf einer festen Kopie der Datei zu wiederholen:

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

Qualitäts-Tooling, optional, aber empfohlen:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Die 28 Übersetzungen des Repositories (README und CHANGELOG, vierzehn Sprachen)
werden mit `./regen_translations.sh --force` neu generiert – standardmäßig Codex und `gpt-5.6-sol`
über das ChatGPT-Abonnement, vier parallel. `REGEN_PROVIDER` und `REGEN_MODEL`
ändern den Pfad: `antigravity` bleibt bei einem Abonnement, dem von Google,
und läuft ohne Ausnahme durch; eine kostenpflichtige API (`openai`, `gemini`,
`grok`, `openrouter`) wird ohne `REGEN_ALLOW_PAID_API=1` abgelehnt;
`REGEN_JOB_TIMEOUT` begrenzt jeden Job (600 s, 1.800 s bei Codex und
Antigravity). Details zum Tooling finden sich in `CLAUDE.md`.

## Projekte, die dieses Skript verwenden

- **[jls42.org](https://jls42.org)** — persönlicher Blog, veröffentlicht in 15 Sprachen. Sein
  [täglicher KI-Monitor](https://jls42.org/fr/news) wird jeden Tag mit diesem Werkzeug übersetzt
  und dient als Referenzdokument für die obigen Messungen.

## Autor

Julien LE SAUX
E-Mail: contact@jls42.org

## Lizenz

GNU GENERAL PUBLIC LICENSE Version 3. Siehe [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Warnhinweis

Dieses Programm wird **ohne jegliche Gewährleistung** gemäß den Abschnitten
15 und 16 der GPL v3 vertrieben: bereitgestellt „wie besehen“, ohne Garantie
für Marktgängigkeit oder Eignung für einen bestimmten Zweck, und sein Autor
kann nicht für Schäden haftbar gemacht werden, die aus seiner Nutzung resultieren.
Der Lizenztext hat Vorrang vor dieser Zusammenfassung.

- **Vor der Veröffentlichung Korrektur lesen.** Die Schutzmechanismen decken Codeblöcke,
  Inline-Code, URLs, Anker und Zitate im Modus `--news` ab – weder
  Überschriften noch Tabellen, Frontmatter oder den Sinn Ihrer Sätze.
- **Ihre Dokumente werden an den ausgewählten Anbieter übertragen**, gemäß dessen
  Nutzungsbedingungen und Datenschutzrichtlinien. Einige kostenlose Modelle können
  Ihre Interaktionen für das Training wiederverwenden, und die Bedingungen von Antigravity
  erlauben es Google, diese wiederzuverwenden und von Menschen überprüfen zu lassen,
  auch bei kostenpflichtigem Abonnement; ein lokales Modell ist der einzige Weg,
  bei dem keine Daten Ihre Maschine verlassen.
- **API-Aufrufe werden Ihnen in Rechnung gestellt.** Dieses Programm begrenzt die
  Ausgaben nicht: Ein langes Dokument, ein Neustart nach einem Fehler oder ein Modell,
  das viel Reasoning betreibt, verursachen höhere Kosten.
- **Die veröffentlichten Messungen sind zeitpunktbezogene Beobachtungen**, keine Garantien.

Die genannten Produkt- und Firmennamen gehören ihren jeweiligen Eigentümern.
Dieses Projekt steht in keiner Verbindung zu diesen.

**Artikel übersetzt aus dem Französischen ins Deutsche mit gemini-3.8-flash-medium.**

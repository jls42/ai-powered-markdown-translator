# AI-Powered Markdown-vertaler

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Codekwaliteit</h4>

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

Vertaalt Markdown-bestanden van de ene taal naar de andere met behoud van de
structuur: codeblokken, inline code, URL's, ankers, tabellen en frontmatter.
Elf manieren om een model aan te roepen — vijf API's, vier abonnementen zonder
facturatie per gebruik, twee routers — en een gepubliceerde meting van wat elk
model daadwerkelijk behoudt.

## In het kort

- **Elf providerpaden**: OpenAI-, Mistral-, Claude-, Gemini- en Grok-API's;
  ChatGPT- (Codex), Grok-, Google- (Antigravity) en Claude-abonnementen (Claude
  Code) zonder facturatie per gebruik; OpenCode- (open source, gratis of lokaal) en OpenRouter-routers
  (meer dan 400 modellen).
- **Niets fout door een verloren token**: codeblokken, inline code,
  URL's, ankers en citaten worden vóór de aanroep vervangen door tokens en
  bij terugkomst gecontroleerd. Als er één ontbreekt, wordt het bestand niet weggeschreven.
- **Lange documenten**: segmentatie volgens het contextvenster van het model.
- **Modus `--news`**: Engelse citaten beschermd en vlaggen per
  taal beheerd, voor curatie-artikelen.
- **Modus `--eco`**: snellere en goedkopere modellen.
- Optionele **vertaalnotitie**, bovenaan, onderaan of beide.

## Installatie

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11 of nieuwer. Zie [Bijdragen](#bijdragen) om te installeren vanuit
de repository.

## Configuratie

Sleutels worden op drie locaties gelezen, van hoogste naar laagste prioriteit; elk
vult alleen aan wat de vorige leeg laat.

|     | Waar                                          | Waarvoor                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Omgevingsvariabelen                           | CI, containers, eenmalige afwijking   |
| 2   | `.env` van de huidige map (of een bovenliggende) | een projectspecifieke sleutel         |
| 3   | `~/.config/aipmt/.env`                        | eenmalig geïnstalleerd, overal geldig |

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

`GEMINI_API_KEY` wordt geaccepteerd in plaats van `GOOGLE_API_KEY`. Het gebruikersbestand
volgt `XDG_CONFIG_HOME` (alleen absoluut pad) en `%APPDATA%`
onder Windows. Zonder sleutel somt de opdracht de drie locaties op.

**Het `.env`-bestand van een project kan aanroepen niet omleiden noch het uitgevoerde programma
kiezen.** Het levert sleutels, nooit een bestemming of een binary: elke
variabele in `_BASE_URL`, `_API_BASE`, `_ENDPOINT` of `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, de proxy's (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), de certificaatopslaglocaties (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) en `XDG_CONFIG_HOME` /
`APPDATA` worden daarin genegeerd, met een waarschuwing. Een gekloonde repository mag niet
in staat zijn om uw sleutel te kapen, noch u ertoe aan te zetten zijn eigen programma uit te voeren
bij de eerste vertaling. Dit bestand wordt ook gelezen zonder interpolatie:
`NOM=${OPENAI_API_KEY}` kopieert de sleutel daar niet in. Plaats deze variabelen in
de omgeving of in `~/.config/aipmt/.env`.

Optionele variabelen: `XAI_BASE_URL` (standaard `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (seconden per aanroep, standaard 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(standaard 600), `GROK_BIN`, `GROK_HOME` (standaard `~/.grok`), `GROK_TIMEOUT`
(standaard 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (standaard 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (standaard 600), `OPENROUTER_BASE_URL`
(`https://` vereist), `OPENROUTER_TIMEOUT` (standaard 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (standaard 30). Elke variabele wordt nader toegelicht in de
sectie van de bijbehorende provider.

## Aan de slag

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` vertaald naar het Spaans levert `document-es.md` op in `--target_dir`;
met `--include_model`, `document-es-gpt-6.1-terra.md`. De extensie wordt
altijd `.md` — `article.mdx` levert `article-en.md` op — behalve met
`--keep_filename`, dat de oorspronkelijke naam behoudt. Een reeds aanwezige vertaling
wordt overgeslagen zonder `--force`.

Exitcodes: `0` als alles is geslaagd of overgeslagen, `1` als er een bestand
is mislukt (lijst op standaardfoutuitvoer), `2` als de configuratie het probleem is.
Een mislukt bestand wordt nooit weggeschreven, zelfs niet als het schrijven zelf mislukt:
de inhoud wordt ernaast geschreven en vervolgens hernoemd. Opnieuw uitvoeren volstaat.

## Welk model kiezen

Gemeten op twee echte documenten, door elk model vertaald in dezelfde veertien talen.
**Het cijfer is het aantal talen, op veertien, waarin de vertaling is weggeschreven en
waarin niets verschilt van de bron.**

| Model                 | Toegangswijze                     | Compact curatie-artikel | Deze README  | Wat verschilt, en in hoeveel talen                                                                                                                                 |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google-abonnement (Antigravity)   | ✅ 14/14                | ✅ 14/14     | niets, op geen van beide documenten                                                                                                                                |
| **Claude Sonnet 5.5** | Anthropic API-sleutel             | ✅ 14/14                | ✅ 14/14     | niets, op geen van beide documenten                                                                                                                                |
| **Gemini 3.7 Flash**  | Google API-sleutel                | ✅ 14/14                | ⚠️ 13/14     | 1 op 14 talen: een extra vetgedrukt woord (ja)                                                                                                                     |
| **Gemini 3.7 Flash**  | Google-abonnement (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 1 op 14 talen: een vetgedrukt woord minder (ko)                                                                                                                    |
| **GPT-5.6 Sol**       | ChatGPT-abonnement of OpenAI-sleutel | ✅ 14/14             | ⚠️ 12/14     | 2 op 14 talen: een vetgedrukt woord minder (ar, ja)                                                                                                                |
| **GLM-5.2**           | OpenRouter-sleutel                | ✅ 14/14                | ⚠️ 11/14     | 3 op 14 talen: een vetgedrukt woord minder (hi, ja, ko)                                                                                                            |
| Claude Sonnet 5       | Claude-abonnement (Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 1 op 14 talen bij het artikel: een extra vetgedrukt woord (zh); 1 bij deze README: een tabelrij vastgeplakt aan de vorige, verborgen bij weergave (ar)            |
| Claude Haiku 4.5      | Claude-abonnement (Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 3 talen bij het artikel: een sectiekop veranderd naar niveau 1 (en, pl, ro); bij deze README niets voor de vergelijker, maar interne links gedupliceerd in het Engels |
| Claude Sonnet 5       | Anthropic API-sleutel             | ⚠️ 11/14                | ⚠️ 12/14     | 3 talen bij het artikel: een codeblok verschenen (es, de, hi); 2 bij deze README: een link zonder mark-up (sv), een vetgedrukt woord (zh)                              |
| Claude Haiku 4.5      | Anthropic API-sleutel             | ⚠️ 7/14                 | ✅ 14/14     | 7 talen bij het artikel: een sectiekop veranderd naar niveau 1 — in het Japans in het Frans gebleven; niets bij deze README                                              |
| Claude Haiku 5.5      | Anthropic API-sleutel             | ⚠️ 11/14                | ❌ 12/14     | 3 talen bij het artikel: een sectiekop van niveau veranderd of gedupliceerd (ja, ko, zh); bij deze README 2 talen geweigerd, inline codes verloren gegaan (ar, hi)    |
| Qwen 3.7 Flash        | OpenRouter-sleutel                | ❌ 8/14                 | ⚠️ 10/14     | 1 taal geweigerd bij het artikel, 5 andere wijken af; bij deze README ongeveer veertig woorden in `code` geplaatst (ar)                                           |
| Grok 4.6              | Grok-abonnement                   | ❌ 8/14                 | niet beoordeeld | 5 op 14 talen geweigerd wegens ontbrekende inline codes en gerenderde URL's; het Nederlands wijkt op alles af                                                      |
| GPT-OSS 20B           | lokaal model (Ollama)             | ❌ 7/14                 | niet opnieuw gemeten | 4 op 14 talen geweigerd: het model liet er Franse passages in staan, de beveiliging heeft ze tegengehouden                                                   |
| MiMo v2.5 (gratis)   | OpenCode Zen, zonder account      | ❌ 11/14                | niet opnieuw gemeten | 1 taal geweigerd; een sectie verloren gegaan in het Pools                                                                                                          |
| Mistral Large         | Mistral API-sleutel               | ❌ 5/14                 | ❌ 1/14      | **een hele sectie verdwijnt**: 1 taal bij het artikel (hi), 3 bij deze README (ar, hi, ko) — en 3 talen geweigerd bij het artikel                                |
| DeepSeek V4 Flash     | OpenRouter-sleutel                | ❌ 3/14                 | niet opnieuw gemeten | 10 op 14 talen geweigerd; 37 minuten per taal                                                                                                                 |
| Claude Opus 5.5       | Claude-abonnement (Claude Code)   | ❌ 0/14                 | ✅ 14/14     | het artikel in alle 14 talen geweigerd door de vangrails van Opus, vanwege een kort biologienieuwsbericht; niets bij deze README                                         |

|     | Wat het symbool betekent                                                                                                                                                                              |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alle veertien talen vertaald, en niets verschilt van de bron                                                                                                                                          |
| ⚠️  | alle veertien talen vertaald; wat verschilt is **opmaak** — een vetgedrukt woord, een `code`, een link die zijn haken verliest. Er ontbreekt geen tekst, geen URL, geen codeblok, geen sectie |
| ❌  | minstens één taal kon niet worden vertaald — het bestand is geweigerd, niet weggeschreven — **of** er ontbreekt inhoud in een weggeschreven bestand                                                  |

Belangrijkste inzichten:

- **Een geweigerde vertaling is geen beschadigde vertaling.** Wanneer er bij
  terugkomst een token ontbreekt, wordt het bestand niet weggeschreven en telt
  de taal als geweigerd. Dit is wat er bij Grok gebeurt bij het artikel: vier inline
  codes en drie URL's verloren gegaan vanaf het eerste segment, bij de vijf niet-Latijnse schriften.
- **Een model kan een heel document weigeren vanwege één enkele zin.** Opus 5.5
  vertaalt deze README zonder enige afwijking, maar geen enkel curatie-artikel:
  de vangrails stoppen de respons bij een kort biologiebericht. Het bestand wordt niet
  weggeschreven en aipmt geeft aan waarom.
- **Dit vangnet dekt geen koppen, tabellen, frontmatter of tekst.** Een
  model dat een sectie verwijdert, levert een bestand op dat de tool zonder morren
  wegschrijft — dat is het geval bij Mistral. Deze elementen kunnen niet worden
  vervangen door een token en de huidige controles controleren ze niet;
  `scripts/compare_structure.py` detecteert een verloren sectie, maar pas achteraf.
- **Grok heeft geen score voor deze README**: de CLI-sessie verliep na twaalf
  talen, waarvan elf zonder afwijking. Een onderbroken testronde krijgt geen score.
- **De dichtheid van het document weegt zwaarder dan de taal.** Grok houdt stand bij
  gewone README's en haakt af bij een artikel vol links, zelfs in het
  Nederlands.

Data en documenten: de kolom "Deze README" is gemeten op 9 september 2026
op een bevroren revisie van dit bestand (785 regels, 285 inline codes, 89 tabelrijen),
sindsdien bijgewerkt — behalve de regels voor Antigravity en Claude Code,
gemeten op 26 september op de revisie gepubliceerd met 1.14.0, die korter is
(600 regels, 257 inline codes, 85 tabelrijen), en de regels voor Claude
Sonnet 5.5, Haiku 5.5 en Haiku 4.5 via de API, gemeten op 18 oktober op
dezelfde revisie. De kolom "Compact curatie-artikel" is afkomstig van de testronde van
4 en 5 september op een artikel van 589 regels, behalve de regel voor Grok, opnieuw gemeten op
9 september op een andere editie van dezelfde curatie, de regels voor Antigravity en
Claude Code, gemeten op 26 september op hetzelfde artikel, en deze drie Claude-regels op
18 oktober. De volledige tabellen, tijdsduren en het protocol zijn te vinden
in [Gedetailleerde metingen](#gedetailleerde-metingen).

## Alle opties

| Optie                    | Beschrijving                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Enkel Markdown-bestand om te vertalen (alternatief voor `--source_dir`)                                       |
| `--source_dir`           | Bronmap met de Markdown-bestanden (standaard: `content/posts`)                                                |
| `--target_dir`           | Uitvoermap voor de vertaalde bestanden (standaard: `traductions_en`)                                           |
| `--source_lang`          | Brontaal (standaard: `fr`)                                                                                   |
| `--target_lang`          | Doeltaal (standaard: `en`)                                                                                   |
| `--model`                | Specifiek te gebruiken model                                                                                  |
| `--eco`                  | Voordelige modellen gebruiken                                                                                 |
| `--use_mistral`          | De Mistral AI-API gebruiken                                                                                  |
| `--use_claude`           | De Claude-API gebruiken                                                                                       |
| `--use_gemini`           | De Gemini-API gebruiken                                                                                       |
| `--use_grok`             | De xAI-API (Grok) gebruiken — vereist `XAI_API_KEY`                                                         |
| `--use_codex`            | De Codex-CLI gebruiken op het tegoed van het ChatGPT-abonnement                                               |
| `--use_grok_cli`         | De Grok-CLI gebruiken op het tegoed van het Grok-abonnement                                                   |
| `--use_antigravity`      | De Antigravity-CLI (`agy`) gebruiken op het tegoed van het Google AI Pro- of Ultra-abonnement                 |
| `--use_claude_code`      | De Claude Code-CLI (`claude -p`) gebruiken op het tegoed van het Claude Pro- of Max-abonnement                    |
| `--use_opencode`         | OpenCode (open source) gebruiken naar de in OpenCode geconfigureerde provider; vereist `--model provider/modèle`        |
| `--use_openrouter`       | OpenRouter gebruiken — vereist `OPENROUTER_API_KEY` en `--model fournisseur/modèle`                                              |
| `--force`                | Opnieuw vertalen forceren                                                                                     |
| `--keep_filename`        | Originele bestandsnaam behouden                                                                               |
| `--news`                 | Nieuwsmodus: beschermt EN-citaten, beheert vlaggen per taal                                                  |
| `--add_translation_note` | Een vertaalnotitie toevoegen                                                                                  |
| `--note_position`        | Positie van de notitie: `top`, `bottom` (standaard), of `both`                                         |
| `--note_format`          | Opmaak van de notitie: `legacy` (standaard, vette alinea) of `marker`                                         |
| `--include_model`        | De modelnaam opnemen in het uitvoerbestand                                                                    |
| `--reasoning_effort`     | Redeneerinspanning GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                   |

De negen `--use_*`-vlaggen sluiten elkaar wederzijds uit: het combineren van twee vlaggen wordt
geweigerd.

## Providers

### Via API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` schakelt over naar de voordelige tier van elke provider.

| Provider    | Kwaliteit (standaard)                                                | Voordelig (`--eco`)      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-6.1-terra`                                                      | `gpt-6-luna`              |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-4-hydrogen`                                                  | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (ook `gpt-5.6-sol`, `terra` en `luna` via `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.7`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | idem — `--eco` zonder effect |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.8-flash-low`    |
| Claude Code | `sonnet`, inspanning `low`                                          | idem — `--eco` zonder effect |
| OpenCode    | `--model provider/modèle` verplicht                                  | idem — `--eco` zonder effect |
| OpenRouter  | `--model fournisseur/modèle` verplicht                               | idem — `--eco` zonder effect |

De standaardwaarden volgen de nieuwste generatie van elke provider, gemeten
voordat ze worden overgenomen: GPT-6 bij OpenAI, Gemini 4 Hydrogen bij Google,
Grok 4.7 bij xAI sinds 1.19.0. Eerdere modellen blijven geaccepteerd
via `--model` (`gpt-5.6-terra`, `gemini-3.8-flash`, `grok-4.6`…), evenals
Gemini 4 Argon en Carbon, het topsegment van Google. aipmt stelt zelf
de redeneerinspanning van de GPT's en Groks in, uitgeschakeld in `--eco`, en
`--reasoning_effort` forceert dit; een Gemini krijgt altijd het laagste
niveau dat hij accepteert.
Een tijdelijke storing van de Gemini-API (503, 429, time-out) probeert
de aanroep tot drie keer opnieuw, na respectievelijk 10, 20 en 40 seconden. Een poging
die onbeantwoord blijft, wordt na 5 minuten afgebroken en op dezelfde
manier opnieuw geprobeerd: een niet-reagerende server laat het segment in maximaal zo'n
twintig minuten mislukken, in plaats van oneindig te blokkeren.

### Met het ChatGPT-abonnement: `--use_codex`

Stuurt de officiële Codex-CLI aan: de vertaling wordt afgeboekt van het tegoed van
het ChatGPT-abonnement, zonder API-sleutel of betaling per verbruik.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Het binaire bestand wordt gezocht in `CODEX_BIN`, daarna in de `PATH`, en vervolgens in het package
  `openai-codex-cli-bin`. `~/.codex/auth.json` wordt nooit gelezen.
- `OPENAI_API_KEY` en `CODEX_API_KEY` worden verwijderd uit de omgeving van het
  subproces: een aanwezige sleutel zorgt er nooit voor dat naar de API wordt overgeschakeld.
- Elk segment kost ten minste één "bericht" uit het venster van 5 uur — twee
  als de validatie mislukt en het opnieuw wordt geprobeerd. OpenAI geeft ter indicatie
  een schatting van 250-2.000 berichten/5 uur voor `gpt-5.6-luna` (`--eco`) en
  10-100 voor `gpt-5.6-sol` bij een Plus-abonnement.
- `--model gpt-5.6-sol`, de standaard tot 1.16.3, `--model gpt-5.6-terra`
  en `--model gpt-5.6-luna` werken ook via het abonnement.
- Een 429 van de server zorgt er niet voor dat het bestand verloren gaat: Codex maakt zelf opnieuw verbinding,
  aipmt wacht tot de beurt voorbij is, en als de 429 aanhoudt, start het segment
  na 30 en vervolgens na 60 seconden opnieuw. Een model waar het account geen recht op heeft, retourneert een 400 "model is
  not supported when using Codex with a ChatGPT account".
- Langzamer dan een API, en het verschil wordt groter naarmate het document groeit: voor deze README
  een mediaan van 6 min 46 s per taal met `gpt-5.6-sol`, tegenover 36 s voor
  `gemini-3.7-flash`.
- Geweigerd in CI (`CI` of `GITHUB_ACTIONS` gedefinieerd): het abonnement verifieert
  via een persoonlijk sessiebestand, dat niet thuishoort op een gedeelde
  runner.
- Variabelen: `CODEX_BIN`, `CODEX_TIMEOUT` (seconden per segment, standaard 600).

### Met het Grok-abonnement: `--use_grok_cli`

Hetzelfde principe met de officiële Grok Build-CLI, op basis van het SuperGrok- of
X Premium+-abonnement.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Minder strikte isolatie dan Codex.** De OS-sandbox van Grok werkt niet
  op veel recente Linux-systemen (AppArmor, container-runtime-sockets),
  en een profiel dat niet kan worden toegepast, start stilletjes zonder isolatie op.
  Het script vraagt daarom standaard geen enkel profiel aan, meldt dit, en
  leunt op de `--deny`-regels van de CLI, waaronder de catch-all `*` — de enige
  laag die weigert te starten in plaats van stilletjes de beveiliging uit te schakelen.
  `GROK_TRANSLATE_SANDBOX=read-only` vereist de OS-sandbox, en het starten
  mislukt als het systeem hieraan niet kan voldoen.
- Het tegoed is op weekbasis en wordt gedeeld met Chat, Imagine en Voice, en er is geen
  commando om dit uit te lezen: een batch kan het gebruik voor conversaties
  ongemerkt verbruiken.
- Variabelen: `GROK_BIN`, `GROK_HOME` (map van de CLI, standaard `~/.grok`),
  `GROK_TIMEOUT` (standaard 900), `GROK_TRANSLATE_SANDBOX`.

### Met het Google-abonnement: `--use_antigravity`

Hetzelfde principe met `agy`, de officiële CLI van Antigravity: voor wie betaalt voor Google
AI Pro of Ultra, wordt de vertaling afgeboekt van het tegoed van het abonnement in plaats
van per token te worden gefactureerd. Dit is de enige manier om dit tegoed te gebruiken: Gemini CLI bedient
deze accounts niet meer sinds 18 juni 2026
([aankondiging](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
en de SDK van Antigravity accepteert enkel een API-sleutel of een Google Cloud-project.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Er blijft geen enkele betaalde route open.** agy ontvangt uit uw
  omgeving enkel een gesloten lijst met variabelen — `PATH`, taal en tijdzone,
  terminal, identiteit, proxy's en certificaten, sessiebus — en geen enkele sleutel:
  meerdere variabelen kunnen een aanroep geruisloos laten overschakelen (in metingen geconstateerd:
  de ene stuurt het document naar een gateway van derden, een andere naar een gefactureerd
  Google Cloud-project), en een blokkeerlijst zag er bij elke controle wel een paar over het hoofd.
  Voor elk segment moet `agy -p /config`, wat geen tegoed kost, aantonen
  dat betaalde AI-tegoeden zijn uitgeschakeld, zonder API-sleutel of Google Cloud-project — een
  ontbrekende instelling leidt tot weigering —, anders wordt er niets vertaald; het logboek van elke
  aanroep moet vervolgens het abonnement bevestigen (`authMethod=consumer`), anders wordt het
  antwoord geweigerd.
- **Isolatie.** Elke aanroep draait in een eigen, tijdelijke privégids
  met een vertaalagent zonder tools: uw instellingen, regels,
  plug-ins, MCP-servers en hooks van agy komen er niet in, er wordt niets toegevoegd aan uw
  geschiedenis en de authenticatie blijft in de sleutelbos, die aipmt nooit uitleest.
  Als een agent niet kan worden gevonden, valt agy stilletjes terug op zijn codeeragent
  en bijbehorende tools: een volledige regel in het logboek moet de juiste agent bevestigen — een
  document dat dit bericht citeert volstaat niet —, anders volgt weigering.
- **Platformen**: Linux, binnen een sessie met een sleutelbos (D-Bus-sessiebus,
  Secret Service); macOS wordt geaccepteerd, maar is niet nagemeten. Geweigerd
  onder Windows, waar agy de variabelen die elke aanroep isoleren niet leest, en
  onder Linux zonder sessiebus — SSH-sessie, container, server: agy slaat zijn
  token daar op in een bestand in `~/.gemini`, dat door de isolatie wordt verborgen. De
  weigering vindt plaats vóór het starten, met opgave van reden, in plaats van een minuut
  wachten op een inlogcode.
- **Modellen**: die van `agy models`. De Gemini's bevatten het redeneerniveau in hun naam
  (`gemini-3.8-flash-medium`…): een naam zonder achtervoegsel wordt vóór de aanroep geweigerd,
  en `--reasoning_effort` heeft geen effect. Standaard `gemini-3.8-flash-medium`,
  en `gemini-3.8-flash-low` in `--eco`, sinds agy Gemini 3.7
  Flash niet meer aanbiedt; de testsessie die de standaard heeft bepaald, wordt
  beschreven in [Gedetailleerde metingen](#gedetailleerde-metingen). Gemini 4 Hydrogen
  (`gemini-4-hydrogen-low`…) deelt het tegoed van 3.8 Flash en verbruikt
  meer: 0,95 punt van het 5-uursvenster voor deze README bij een gemiddelde
  inspanning, tegenover 0,32. Claude en GPT-OSS
  hebben hun eigen tegoed, dat aanzienlijk kleiner is: ongeveer 1% van het venster van
  5 uur per gemeten aanroep, tegenover 0,05% bij Flash. Gemini 4 Argon heeft een
  eigen weektegoed: deze README verbruikt daar 1,35% van.
- **Tegoed**: per groep een 5-uursvenster en een weekvenster, naar
  rato van de tokenkosten. Gemeten op het account van de auteur: ongeveer
  16 punten van het 5-uursvenster per miljoen brontekens in
  `gemini-3.8-flash-medium`, 14 in `gemini-3.7-flash-medium` en 7 tot 8 bij
  een lage inspanning — een README van 40.000 tekens kost dus iets meer dan een
  half punt. De wekelijkse limiet hangt af van het abonnementstype. Het opnieuw proberen volgt
  wat agy als 'retryable' aangeeft; bij gebrek daaraan wordt een uitgeput venster nooit
  opnieuw geprobeerd: elk bestand mislukt dan tot de reset
  die door `/usage` wordt weergegeven.
- **Langzamer dan de API**: bij het omvangrijke meetartikel een mediaan van 3 min 59 s per
  taal in `gemini-3.8-flash-medium` en 3 min 14 s in
  `gemini-3.7-flash-medium`, tegenover 1 min 18 s voor Gemini 3.7 Flash via de API.
- **Onderbreking**: Ctrl-C of een gesloten terminal stopt agy tegelijk met het
  commando in plaats van de beurt op uw tegoed af te laten maken; hetzelfde geldt
  voor Codex, Grok CLI en OpenCode. Onder `nohup` gaat de vertaling door.
- Geweigerd in CI (`CI` of `GITHUB_ACTIONS` gedefinieerd): de authenticatie bevindt zich in een
  persoonlijke sleutelbos. Gebruik op een runner `--use_gemini` met `GOOGLE_API_KEY`.
- Variabelen: `AGY_BIN` (anders de `PATH`, daarna `~/.local/bin/agy`),
  `AGY_TIMEOUT` (seconden per segment, inclusief opstarten, standaard 900).

**Gebruiksvoorwaarden: u bent zelf verantwoordelijk voor uw account.** De
[voorwaarden van Antigravity](https://antigravity.google/terms) (sectie 6) en de bijbehorende
[FAQ](https://antigravity.google/docs/faq/) verbieden toegang tot de dienst
via software van derden met behulp van de Antigravity-aanmelding — Claude Code,
OpenClaw en OpenCode worden daarin met name genoemd —, op straffe van accountopschorting. aipmt
leest noch hergebruikt het token: het start het officiële binaire bestand in de
[headless-modus](https://antigravity.google/docs/cli/headless/) die Google
documenteert voor scripts en CI. Een medewerker van Google noemde het starten van
`agy -p` vanuit een lokaal script voor eigen werk "standaard"
([officieel forum, 25 september 2026, niet-bindend antwoord](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
geen enkele formele tekst geeft uitsluitsel over een gedistribueerde tool zoals deze.

**Uitsluitend openbare documenten.** Volgens sectie 5 van dezelfde voorwaarden kunnen
interacties — prompts, antwoorden, metadata — worden gebruikt om producten en machine
learning van Google te verbeteren en kunnen deze door mensen worden beoordeeld,
ook bij een betaald abonnement. Afmelden verloopt via de instelling
`enableTelemetry`, met een ongedocumenteerde werking, die aipmt niet instelt; uw instellingen
van agy worden niet meegenomen in de geïsoleerde omgeving. Laat hier niets vertrouwelijks doorheen gaan.

### Over het Claude-abonnement: `--use_claude_code`

Hetzelfde principe met `claude`, de officiële CLI van Claude Code, in de modus `-p`: voor
wie betaalt voor Claude Pro of Max, wordt de vertaling verrekend met het quotum van
het abonnement in plaats van gefactureerd per token. Niet te verwarren met
`--use_claude`, de API van Anthropic, die wordt gefactureerd naar gebruik.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Er blijft geen enkele betaalde route openstaan, en elke aanroep bewijst dat.** Claude
  Code ontvangt vanuit uw omgeving slechts een gesloten lijst van variabelen — geen
  API-sleutel, geen token, geen cloudprovider en geen markering van de Claude Code-sessie
  van waaruit aipmt zou zijn gestart. Vóór het eerste segment moet `claude auth status`
  de abonnementsverbinding tonen, zonder Console-sleutel, en `/usage`, dat
  geen enkel quotum kost, moet dit bevestigen; elke aanroep bevestigt dit op zijn beurt in zijn
  initialisatie-event, anders wordt het antwoord geweigerd.
- **Schakel « extra usage » uit** (claude.ai, Instellingen → Gebruik) om
  het nultarief te behouden: ingeschakeld neemt het het over van een uitgeput venster en
  factureert het zonder een foutmelding te tonen. aipmt stopt de vertaling zodra de
  quotumstatus van een aanroep dit aangeeft, maar die specifieke aanroep is dan al meegeteld.
- **Gedeeld quotum met uw Claude Code-sessies.** Elke aanroep rapporteert
  het gebruik van de vensters van 5 uur en van de week; boven de 80%
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) wordt er geen segment meer gestart, om
  niet uit te putten wat nodig is voor uw werk.
- **Insluiting (confinement).** Elke aanroep draait zonder tools, in een privé en
  wegwerpbare directory, in een modus zonder aanpassingen: noch uw `CLAUDE.md`, noch uw plug-ins,
  hooks, MCP-servers of instellingen worden geladen, en er wordt niets bewaard van de
  sessie. Bijlagen zijn uitgeschakeld: een `@chemin` in uw document
  blijft tekst en opent geen enkel bestand (gemeten).
- **Modellen**: standaard `sonnet`, met inspanning `low`, en ook in `--eco`:
  `--eco` verandert niets op dit pad. Gemeten op dezelfde documenten is `haiku`
  twee keer zo traag — het redeneert zonder dat men dit kan verhinderen — tegen
  nauwelijks lagere kosten, en `opus` weigert biologische inhoud (volgend
  punt). Beide blijven toegankelijk via `--model`; deze aliassen volgen het
  nieuwste model van hun familie. `fable` en de `[1m]`-varianten worden geweigerd,
  omdat ze overgaan op betaalde credits. `--reasoning_effort` regelt de inspanning,
  waar een vertaling niets aan heeft: het gemeten redeneren is nihil of vrijwel nihil.
- **Opus weigert bepaalde biologische inhoud.** De vangrails zijn
  strenger dan die van Sonnet, en de foutmelding van Anthropic waarschuwt dat ze
  « can sometimes flag biology-research-adjacent work ». Gemeten: een kort
  overzichtsbericht over 279 gegenereerde moleculen leidde ertoe dat het artikel in alle veertien
  talen werd geweigerd. Er wordt niets geschreven: aipmt weigert het afgekapte antwoord, noemt de
  vangrails en adviseert `--model sonnet`.
- Geweigerd in CI (`CI` of `GITHUB_ACTIONS` gedefinieerd) en onder Windows (niet gemeten).
- Variabelen: `AIPMT_CLAUDE_BIN` (anders de `PATH`, daarna `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (seconden per segment, standaard 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (standaard 0.8), `CLAUDE_CONFIG_DIR` (het account van
  Claude Code, nooit overgenomen van een project-`.env`); werkmappen onder
  `XDG_CACHE_HOME/aipmt/claude-code` (standaard `~/.cache`).

**Gebruiksvoorwaarden: het is uw account dat eraan verbonden is.** De
[juridische pagina van Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
belet « an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription » niet: dat is wat aipmt doet, dat het
officiële binaire bestand start en het token nooit leest. Maar Anthropic « does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users », geeft de voorkeur aan de API-sleutel voor tools
van derden, « including open-source projects », en behoudt zich het recht voor om hun
gebruik te verrekenen met de betaalde credits
([Claude Help](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Geen enkele tekst hakt de knoop door over het geval van een gedistribueerde tool die het binaire bestand start.

**Gegevens**: bij Free-, Pro- en Max-accounts is de training van modellen
ook van toepassing op Claude Code wanneer de privacy-instelling dit toestaat
([gegevenspagina](https://code.claude.com/docs/en/data-usage)). aipmt bewaart
geen enkele lokale transcriptie (`--no-session-persistence`). Laat er
niets vertrouwelijks doorheen gaan.

### Naar de provider naar keuze: `--use_opencode`

[OpenCode](https://opencode.ai) is een open-source code-agent (MIT) die
routeert naar de daarin geconfigureerde providers: API-sleutel, abonnement,
OpenCode Zen-gateway (gratis modellen, zonder account) of een lokaal model. Twee
routes zijn hier van begin tot eind gemeten: Zen en Ollama.

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

`--model` is verplicht: zonder dit zou OpenCode terugvallen op een gratis model
waarvan de interacties kunnen worden gebruikt voor training, en die keuze wordt niet in
uw plaats gemaakt.

Insluiting (confinement) bij elke aanroep:

- een inline-configuratie, die voorrang heeft op die van u, definieert een agent `aipmt`
  waarvan alle tools worden geweigerd (`permission: { "*": "deny" }`), sessiedeling
  uitgeschakeld, `--pure`, nooit `--auto`;
- wegwerpbare en lege werkmap, `OPENCODE_DISABLE_PROJECT_CONFIG` en
  `OPENCODE_DISABLE_CLAUDE_CODE` geplaatst — zonder deze injecteert OpenCode in de
  prompt het `AGENTS.md` van de huidige map en `~/.claude/CLAUDE.md`. Het
  globale `~/.config/opencode/AGENTS.md` blijft geïnjecteerd; OpenCode biedt geen mogelijkheid
  om dit uit te sluiten;
- uitvoercontract: exitcode 0, geen enkel `error`-event, geen enkele aanroep
  van tools, laatste stap in `stop`, niet-lege tekst, en de agent `aipmt`
  daadwerkelijk geladen — een onbekende `--agent` zorgt er niet voor dat OpenCode faalt, het
  valt geruisloos terug op de codeeragent;
- er wordt geen enkele sleutel van `aipmt` doorgegeven, behalve `OPENCODE_API_KEY`, de sleutel
  van OpenCode zelf. Providers worden geconfigureerd in OpenCode, niet in
  het `.env` van `aipmt`.

Goed om te weten:

- De gratis modellen van Zen zijn veranderlijk, met ongedocumenteerde limieten, en
  hun interacties kunnen worden gebruikt voor training: geschikt voor openbare
  documentatie, niet voor privé-inhoud.
- Een lokaal model moet ten minste 16k contexttokens bieden, aangezien segmenten
  tot 16.000 tekens kunnen beslaan. Ollama configureert er vaak 4.096: gebruik
  een `Modelfile` met `PARAMETER num_ctx 32768`.
- `--eco` heeft geen effect; `--reasoning_effort` wordt ongewijzigd doorgegeven als
  `--variant` van OpenCode.
- OpenCode logt elke sessie in `~/.local/share/opencode/`.
- Variabelen: `OPENCODE_BIN` (anders de `PATH`, daarna `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (seconden per segment, standaard 600). `OPENCODE_CONFIG`
  wordt ongewijzigd doorgegeven aan OpenCode.

Voorbeeld van een lokaal model via Ollama, in `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` schakelt de reflectie uit die Ollama standaard activeert op deze
modellen, en die een Modelfile niet kan uitschakelen. Gemeten op een zin van
zes woorden: 919 reflectietokens en 68 seconden zonder de optie, 9 tokens ermee.

### Naar meer dan 400 modellen: `--use_openrouter`

OpenRouter is een router die naar verbruik factureert, op één enkel tegoed, voor
modellen die door derden worden gehost — waaronder de open Chinese modellen die geen
enkele andere provider hier aanbiedt.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` is verplicht. Een preflight, uitgevoerd vóór elke facturatie, regelt
twee specifieke eigenschappen van de routering:

- **Hetzelfde model wordt aangeboden door tientallen hosts met verschillende
  limieten** — op `z-ai/glm-5.3-flash`, 23 hosts waarvan er één beperkt is tot
  2.048 uitvoertokens. De preflight leest `/api/v1/models/{modèle}/endpoints`,
  sluit hosts uit met minder dan 8.000 uitvoertokens of met een gedegradeerde status, en
  zet de overige vast met `allow_fallbacks: false`.
- **Redeneren wordt gefactureerd tegen het uitvoertarief** — 107 tokens tegenover 2 bij
  een « OK »-antwoord van `z-ai/glm-5.2`. Het staat standaard uitgeschakeld; modellen
  die dit vereisen, ontvangen de laagste inspanning die ze accepteren, aangezien de standaardwaarde
  van de catalogus de uitvoer kan verzadigen vóór het einde van de vertaling.
  `--reasoning_effort` behoudt voorrang.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Het contextvenster is afkomstig uit de catalogus. Een model onder de 16.400 tokens wordt
  vóór elke aanroep geweigerd: 8.400 voor de prompt en het segment, minimaal 8.000
  voor uitvoer.
- Een slug die ontbreekt in de catalogus, een onbereikbare catalogus of het ontbreken
  van een host die de limiet aankan, stopt het commando.
- `finish_reason=length` met een lege uitvoer is een budget dat is verbruikt door het
  redeneren, geen afkapping: het bericht maakt dit onderscheid.
- `--eco` heeft geen effect.
- Variabelen: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (standaard `https://openrouter.ai/api/v1`, `https://`
  vereist), `OPENROUTER_TIMEOUT` (standaard 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (standaard 30).

### Vertaalnotitie

`--add_translation_note` voegt een notitie toe, in `bottom` (standaard), `top` (na de
front matter) of `both` (`--note_position`), in het formaat `legacy` (vetgedrukte
alinea, standaard) of `marker` (`--note_format`). Het formaat `marker` is een
onzichtbare Markdown-referentiedefinitie,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
gevolgd door een vetgedrukt citaat: leesbaar op GitHub, bruikbaar bij de build door een
remark-plugin.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Gedetailleerde metingen

Alle metingen zijn daadwerkelijk uitgevoerde vertalingen met `aipmt`, naar
veertien talen: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Geschreven** telt de bestanden die de bewakers hebben doorgelaten; **Zonder
afwijking** die waarbij `scripts/compare_structure.py` niets opmerkt — hetzelfde aantal
secties, subtitels, links, unieke URL's, codeblokken,
inline codes, tabelrijen, citaatblokken en vetgedrukte woorden.

« Zonder afwijking » betekent « niets gedetecteerd », niet « identiek »: de vergelijker
telt elementen zonder de inhoud ervan te lezen. Het meldt noch een verwijderde kop van
niveau 4, noch de tekst van een vervangen inline code, noch een verwisselde vlag,
noch een interne link die is weergegeven met een haakje te veel,
`[texte]((#ancre))`, die nergens meer naartoe leidt — en het beoordeelt de
taal niet.

### Dicht overzichtsartikel, modus `--news`

Een editie van het [AI-overzicht van jls42.org](https://jls42.org/fr/news):
589 regels, 140 links, 21 secties, 3 beschermde Engelse citaten. Campagne
van 4 en 5 september 2026.

| Model                                          | Toegang            | Geschreven | Zonder afwijking | Mediaan/taal |
| ----------------------------------------------- | ------------------ | ---------- | ---------------- | ------------ |
| `gemini-3.7-flash`                              | Google API         | 14/14      | ✅ **14/14**     | 1 min 18 s   |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google-abonnement  | 14/14      | ✅ **14/14**     | 3 min 59 s   |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google-abonnement  | 14/14      | ✅ **14/14**     | 3 min 14 s   |
| `claude-sonnet-5-5`                             | Anthropic API      | 14/14      | ✅ **14/14**     | 3 min 37 s   |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT-abonnement | 14/14      | ✅ **14/14**     | 11 min 28 s  |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14      | ✅ **14/14**     | 5 min 37 s   |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14      | ✅ **14/14**     | 26 min 23 s  |
| `sonnet` (`--use_claude_code`)                  | Claude-abonnement  | 14/14      | ⚠️ 13/14         | 6 min 49 s   |
| `claude-sonnet-5`                               | Anthropic API      | 14/14      | ⚠️ 11/14         | 6 min 31 s   |
| `haiku` (`--use_claude_code`)                   | Claude-abonnement  | 14/14      | ⚠️ 11/14         | 15 min 54 s  |
| `claude-haiku-5-5`                              | Anthropic API      | 14/14      | ⚠️ 11/14         | 2 min 54 s   |
| `claude-haiku-4-5`                              | Anthropic API      | 14/14      | ⚠️ 7/14          | 6 min 00 s   |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14      | ❌ 11/14         | 9 min 27 s   |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14      | ❌ 8/14          | 10 min 09 s  |
| `ollama/gpt-oss-20b-32k`                        | lokaal             | 10/14      | ❌ 7/14          | 12 min 39 s  |
| `mistral-large-latest`                          | Mistral API        | 11/14      | ❌ 5/14          | 5 min 32 s   |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14       | ❌ 3/14          | 37 min 27 s  |
| `grok-4.6` (`--use_grok_cli`)                   | Grok-abonnement    | 1/14       | ❌ 1/14          | 23 min 11 s  |
| `opus` (`--use_claude_code`)                    | Claude-abonnement  | 0/14       | ❌ 0/14          | —            |

Grok is op 9 september opnieuw gemeten op een andere editie van hetzelfde overzicht
(356 regels): 9 talen geschreven van de 14, 8 zonder afwijking. Dit is het cijfer dat
in de hoofdtabel staat. Drie onderbroken campagnes zijn niet
opgenomen: `qwen3.5-27b` (9 talen) en `kimi-k2.6` (4) wegens gebrek aan credits,
`z-ai/glm-5.3-flash` waarvan de twee mislukkingen te wijten waren aan een instelling voor redeneren
die de provider sindsdien heeft gecorrigeerd. De OpenRouter-regels zijn gemeten met de
standaardinstellingen van de router, vóór `--use_openrouter`; `z-ai/glm-5.2`,
opnieuw gemeten met de geleverde provider, behaalt dezelfde 14/14. De cijfers zijn
op 10 september herberekend met de huidige vergelijker: `qwen3.8-flash` en
`qwen3.7-flash` winnen elk één taal ten opzichte van de eerste
publicatie, de overige zijn ongewijzigd.

De regels voor `--use_antigravity` zijn op 26 september gemeten op hetzelfde
artikel, met vier vertalingen parallel: `gemini-3.7-flash-medium` 's ochtends,
`gemini-3.8-flash-medium` 's middags. In het Engels heeft elk model zelf
de drie Franse vertaalregels onder de citaten verwijderd, zonder een vlag te verzinnen,
en de Engelse citaten zijn intact: de fallback-opschoning hoefde
niets te doen. In `--eco` (`gemini-3.7-flash-low`), op slechts vier talen
(en, ja, ar, hi): 4 geschreven van de 4, allemaal zonder afwijking, 1 min 52 s als
mediaan. Tegenproef op dezelfde dag op een recentere editie van het overzicht,
die van 25 september (438 regels, 2 Engelse citaten), buiten de
blog vertaald door `gemini-3.7-flash-medium`: 14 geschreven van de 14, allemaal zonder afwijking, 87 tot
128 s per taal.

De regels voor `--use_claude_code` zijn op 26 september gemeten op hetzelfde
artikel, met vier vertalingen parallel, met de inspanning `low`. Met `sonnet` zijn de
Engelse citaten intact in alle veertien talen en in het Engels heeft het
model zelf de Franse vertaalregels verwijderd, zonder een vlag te
verzinnen. `opus` heeft geen enkele taal geschreven: in elke taal stopten de vangrails
het antwoord bij het laatste segment, vanwege een kort bericht over 279 gegenereerde moleculen
voor een bindingslocatie. Afzonderlijk verzonden wordt dit korte bericht geweigerd onder
de categorie « bio »; `sonnet` heeft het overal vertaald. `haiku` schrijft
de veertien talen; in drie talen (en, pl, ro) gaat een sectietitel van
niveau 2 naar niveau 1. Het redeneert zonder dat men dit kan verhinderen — 61% van
zijn uitvoertokens —, vandaar meer dan het dubbele van de tijd van `sonnet`.

De regels voor `claude-sonnet-5-5`, `claude-haiku-5-5` en `claude-haiku-4-5` zijn
op 18 oktober gemeten via de API van Anthropic, op hetzelfde artikel, met vier
vertalingen parallel per model. Sonnet 5.5 weigert dat de reflectie
wordt uitgeschakeld: aipmt stuurt de laagste instelling die het accepteert, en de
antwoorden bevatten er geen enkele van. Het schrijft de veertien talen zonder afwijking en zonder
een segment opnieuw te moeten doen; in het Engels heeft het zelf de Franse
vertaalregels verwijderd, zonder een vlag te verzinnen, en de Engelse citaten zijn
overal intact. Haiku 5.5 is gemeten met zijn adaptieve reflectie: met uitgeschakelde
reflectie liet het hele alinea's in het Frans staan, wat door de bewaker wordt geweigerd —
3 talen geschreven van de 14. Beide Haiku-modellen lopen vast op hetzelfde korte bericht: Haiku 5.5
verandert het niveau van de titel of verdubbelt deze in het Japans, Koreaans en
Chinees; Haiku 4.5 zet deze in zeven talen op niveau 1 en laat hem in het Japans in het
Frans staan. Haiku 4.5 kost $ 3,67 voor de twee documenten in de
veertien talen, Haiku 5.5 $ 0,57, Sonnet 5.5 $ 9,21.

### README van dit project, standaard Markdown

Revisie bevroren op 9 september 2026: 785 regels, 285 inline codes, 40
afsluitingen van blokken, 89 tabelrijen. Vier vertalingen parallel.

| Model                                           | Geschreven | Zonder afwijking | Mediaan/taal | Wat verschilt                                                            |
| ----------------------------------------------- | ---------- | ---------------- | ------------ | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14      | ✅ 14/14         | 1 min 43 s   | niets                                                                    |
| `opus` (`--use_claude_code`)                    | 14/14      | ✅ 14/14         | 1 min 48 s   | niets                                                                    |
| `haiku` (`--use_claude_code`)                   | 14/14      | ✅ 14/14         | 4 min 02 s   | niets voor de comparator; interne links gedupliceerd (en)                |
| `claude-sonnet-5-5`                             | 14/14      | ✅ 14/14         | 1 min 18 s   | niets                                                                    |
| `claude-haiku-4-5`                              | 14/14      | ✅ 14/14         | 2 min 06 s   | niets                                                                    |
| `gemini-3.7-flash`                              | 14/14      | ⚠️ 13/14         | 36 s         | één woord vetgedrukt (ja)                                                |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14      | ⚠️ 13/14         | 1 min 22 s   | één woord vetgedrukt (ko)                                                |
| `sonnet` (`--use_claude_code`)                  | 14/14      | ⚠️ 13/14         | 2 min 20 s   | één tabelrij geplakt aan de vorige (ar)                                  |
| `claude-sonnet-5`                               | 14/14      | ⚠️ 12/14         | 2 min 56 s   | één link (sv), één woord vetgedrukt (zh)                                 |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14      | ⚠️ 12/14         | 6 min 46 s   | één woord vetgedrukt (ar, ja)                                            |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14      | ⚠️ 11/14         | 2 min 34 s   | één woord vetgedrukt (hi, ja, ko)                                        |
| `qwen/qwen3.7-flash`                            | 14/14      | ⚠️ 10/14         | 2 min 17 s   | 40 inline codes toegevoegd in het Arabisch; vetgedrukt (hi, ja, ko)      |
| `claude-haiku-5-5`                              | 12/14      | ❌ 12/14         | 1 min 14 s   | 2 talen geweigerd (ar, hi): inline codes verloren gegaan bij terugkeer   |
| `mistral-large-latest`                          | 14/14      | ❌ 1/14          | 2 min 44 s   | één sectie verloren (ar, hi, ko); codeblokken toegevoegd (ja, ko, ro, zh) |

Twee onderbroken campagnes zijn niet opgenomen: Grok, CLI-sessie verlopen
na twaalf talen (elf zonder afwijking), en `qwen3.8-flash`, HTTP 429 van zijn
host na twee. `opencode/mimo-v2.5-free` en `ollama/gpt-oss-20b-32k`
zijn niet opnieuw gemeten op deze revisie; op die van 4 en 5 september,
die 277 regels korter was, schreven ze elk 9 van de 14 vertalingen, waarvan 7
en 1 zonder afwijking.

De rijen `--use_antigravity` en `--use_claude_code` zijn niet gemeten op
de bevroren revisie, maar op 26 september op die welke werd gepubliceerd bij 1.14.0 — en
de rijen `claude-sonnet-5-5`, `claude-haiku-5-5` en `claude-haiku-4-5` op 18
oktober, op dezelfde: 600 regels, 257 inline codes, 30 afsluitingen van blokken, 85
tabelrijen. Omdat ze
185 regels korter is, laat ze zich niet één-op-één vergelijken met de andere rijen;
deze rijen onderling kunnen echter wel met elkaar worden vergeleken. Wat betreft interne links, die de
comparator niet controleert, behield `gemini-3.8-flash-medium` ze intact in
alle veertien talen, brak `gemini-3.7-flash-medium` ze in het Italiaans;
`sonnet` en `opus` behielden ze overal intact, `haiku` verdubbelde ze in
het Engels; `claude-sonnet-5-5` en `claude-haiku-4-5` behielden ze intact in
alle veertien talen, `claude-haiku-5-5` in de twaalf die het heeft geschreven.

### Vier README's van bekende projecten

FastAPI, Ollama, tldr-pages en Vue.js, overgenomen zoals ze zijn op GitHub —
documenten die eenvoudiger zijn dan de twee voorgaande. De campagne richtte zich op de modellen
die moeite hadden; Gemini dient hierbij als vergelijkingspunt.

| Model                     | Bereik                     | Geschreven | Zonder afwijking |
| ------------------------- | -------------------------- | ---------- | ---------------- |
| `gemini-3.7-flash`        | 4 projecten × 14 talen     | 56/56      | ✅ **55/56**     |
| `opencode/mimo-v2.5-free` | 4 projecten × 14 talen     | 55/56      | ❌ 47/56         |
| `grok-4.6` (abonnement)   | 4 projecten × ar, hi, ja, zh | 16/16      | ❌ 14/16         |
| `ollama/gpt-oss-20b-32k`  | 4 projecten × ar, hi, ja, zh | 15/16      | ❌ 9/16          |

### Wat deze metingen niet zijn

- **Geen uitputtende ranglijst**: OpenRouter alleen al biedt meer dan vierhonderd
  modellen aan, er zijn er een vijftiental gemeten.
- **Indicatieve tijdsduren**: drie tot zes vertalingen parallel afhankelijk van
  de campagnes, en de doorvoersnelheid van een provider varieert gedurende de dag.
- **Gedateerde observaties**: modellen veranderen onder dezelfde naam, en uw
  documenten zijn niet de onze.

Om de meting opnieuw uit te voeren op uw documenten, op een bevroren kopie van het bestand:

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## Bijdragen

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

Beide regels zijn noodzakelijk: zonder `pip install -e .`
antwoordt `python -m aipmt` met `No module named aipmt`.

Kwaliteitstools, optioneel maar aanbevolen:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

De 28 vertalingen van de repository (README en CHANGELOG, veertien talen) worden
opnieuw gegenereerd met `./regen_translations.sh --force` — Codex en `gpt-6.1-sol` via
het standaard ChatGPT-abonnement, vier parallel. `REGEN_PROVIDER` en
`REGEN_MODEL` wijzigen het pad: `antigravity` blijft op een abonnement, dat
van Google, en passeert zonder uitzondering; een betaalde API (`openai`, `gemini`,
`grok`, `openrouter`) wordt geweigerd zonder `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` stelt een limiet aan elke taak (600 s, 1.800 s voor Codex en
Antigravity). De details van de tools zijn te vinden in `CLAUDE.md`.

## Projecten die dit script gebruiken

- **[jls42.org](https://jls42.org)** — persoonlijk blog gepubliceerd in 15 talen. De
  [dagelijkse AI-monitoring](https://jls42.org/fr/news) wordt elke dag
  door deze tool vertaald en dient als referentiedocument voor de bovenstaande metingen.

## Auteur

Julien LE SAUX
E-mail: contact@jls42.org

## Licentie

GNU GENERAL PUBLIC LICENSE Versie 3. Zie [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Waarschuwing

Dit programma wordt verspreid **zonder enige garantie**, onder de voorwaarden van
secties 15 en 16 van de GPL v3: geleverd "zoals het is", zonder garantie van verkoopbaarheid
of geschiktheid voor een bepaald doel, en de auteur kan niet
aansprakelijk worden gesteld voor schade die voortvloeit uit het gebruik ervan. De tekst van de
licentie prevaleert boven deze samenvatting.

- **Lees na vóór publicatie.** De beschermingen dekken codeblokken,
  inline code, URL's, ankers en citaten in de modus `--news` — noch de
  koppen, noch de tabellen, noch de front matter, noch de betekenis van uw zinnen.
- **Uw documenten worden naar de gekozen provider verzonden**, onder diens
  gebruiksvoorwaarden en gegevensbeleid. Sommige gratis modellen kunnen
  uw interacties hergebruiken voor training, en de voorwaarden van Antigravity
  staan Google toe om ze te hergebruiken en door mensen te laten nalezen,
  inclusief bij een betaald abonnement; een lokaal model is de enige manier waarbij
  geen gegevens uw machine verlaten.
- **API-aanroepen worden aan u gefactureerd.** Dit programma stelt geen limiet aan de
  kosten: een lang document, een herstart na een fout of een model dat veel
  redeneert, kost meer.
- **De gepubliceerde metingen zijn gedateerde observaties**, geen garanties.

De genoemde product- en bedrijfsnamen behoren toe aan hun respectieve
eigenaars. Dit project is aan geen daarvan gelieerd.

**Artikel vertaald van het Frans naar het Nederlands met gemini-3.8-flash-medium.**

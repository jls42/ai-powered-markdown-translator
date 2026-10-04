# AI-gestuurde Markdown-vertaler

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
gebruikskosten, twee routers — en een gepubliceerde meting van wat elk model
daadwerkelijk behoudt.

## In het kort

- **Elf providerpaden**: OpenAI-, Mistral-, Claude-, Gemini- en Grok-API's;
  ChatGPT- (Codex), Grok-, Google- (Antigravity) en Claude- (Claude
  Code) abonnementen zonder gebruikskosten; OpenCode- (open source, gratis of lokaal) en OpenRouter-routers
  (meer dan 400 modellen).
- **Niets fout door een verloren token**: codeblokken, inline code,
  URL's, ankers en citaten worden vóór de aanroep vervangen door tokens en
  bij terugkeer gecontroleerd. Als er één ontbreekt, wordt het bestand niet geschreven.
- **Lange documenten**: segmentatie volgens het contextvenster van het model.
- **`--news`-modus**: Engelse citaten beschermd en vlaggen beheerd per
  taal, voor monitoringartikelen.
- **`--eco`-modus**: snelle en goedkopere modellen.
- Optionele **vertaalnotitie**, bovenaan, onderaan of beide.

## Installatie

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 of nieuwer. Zie [Bijdragen](#bijdragen) om vanuit de repository
te installeren.

## Configuratie

Sleutels worden op drie plaatsen gelezen, van hoogste naar laagste prioriteit;
elke plek vult alleen aan wat de vorige leeg laat.

|     | Waar                                          | Waarvoor                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Omgevingsvariabelen                           | CI, containers, eenmalige afwijking   |
| 2   | `.env` van de huidige map (of een bovenliggende) | een projectspecifieke sleutel         |
| 3   | `~/.config/aipmt/.env`                        | eenmaal ingesteld, overal geldig      |

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

`GEMINI_API_KEY` wordt geaccepteerd in plaats van `GOOGLE_API_KEY`. Het
gebruikersbestand volgt `XDG_CONFIG_HOME` (alleen absoluut pad) en `%APPDATA%`
onder Windows. Zonder sleutel geeft het commando de drie locaties weer.

**Het `.env` van een project kan oproepen niet omleiden noch het uitgevoerde
programma kiezen.** Het levert sleutels, nooit een bestemming of een binair bestand: elke
variabele in `_BASE_URL`, `_API_BASE`, `_ENDPOINT` of `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, de proxy's (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), de certificaatarchieven (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) en `XDG_CONFIG_HOME` /
`APPDATA` worden daarin genegeerd, met een waarschuwing. Een gekloonde repository mag uw sleutel
niet kunnen kapen, noch u ertoe brengen zijn eigen programma uit te voeren bij de
eerste vertaling. Dit bestand wordt ook gelezen zonder interpolatie:
`NOM=${OPENAI_API_KEY}` kopieert de sleutel daarin niet. Plaats deze variabelen in
de omgeving of in `~/.config/aipmt/.env`.

Optionele variabelen: `XAI_BASE_URL` (standaard `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (seconden per aanroep, standaard 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(standaard 600), `GROK_BIN`, `GROK_HOME` (standaard `~/.grok`), `GROK_TIMEOUT`
(standaard 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (standaard 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (standaard 600), `OPENROUTER_BASE_URL`
(`https://` vereist), `OPENROUTER_TIMEOUT` (standaard 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (standaard 30). Elke variabele wordt in detail beschreven in de
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
met `--include_model`, `document-es-gpt-5.6-terra.md`. De extensie wordt
altijd `.md` — `article.mdx` levert `article-en.md` op — behalve met
`--keep_filename`, dat de oorspronkelijke naam behoudt. Een reeds aanwezige vertaling
wordt overgeslagen zonder `--force`.

Exitcodes: `0` als alles geslaagd of overgeslagen is, `1` als er een mislukt bestand
overblijft (lijst op de foutuitvoer), `2` als de configuratie het probleem is.
Een mislukt bestand wordt nooit geschreven, zelfs niet als het schrijven zelf mislukt:
de inhoud wordt ernaast geschreven en vervolgens hernoemd. Opnieuw uitvoeren volstaat.

## Welk model kiezen

Gemeten op twee echte documenten, door elk model vertaald in dezelfde veertien
talen. **Het cijfer is het aantal talen, op veertien, waar de
vertaling is geschreven en niets afwijkt van de bron.**

| Model                | Hoe toegang te krijgen            | Dicht monitoringartikel | Deze README  | Wat er verschilt, en in hoeveel talen                                                                                                                              |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash** | Google-abonnement (Antigravity)   | ✅ 14/14                | ✅ 14/14     | niets, op geen van beide documenten                                                                                                                                |
| **Gemini 3.7 Flash** | Google API-sleutel                | ✅ 14/14                | ⚠️ 13/14     | 1 taal op 14: een vetgedrukt woord meer (ja)                                                                                                                       |
| **Gemini 3.7 Flash** | Google-abonnement (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 1 taal op 14: een vetgedrukt woord minder (ko)                                                                                                                     |
| **GPT-5.6 Sol**      | ChatGPT-abonnement, of OpenAI-sleutel | ✅ 14/14            | ⚠️ 12/14     | 2 talen op 14: een vetgedrukt woord minder (ar, ja)                                                                                                                |
| **GLM-5.2**          | OpenRouter-sleutel                | ✅ 14/14                | ⚠️ 11/14     | 3 talen op 14: een vetgedrukt woord minder (hi, ja, ko)                                                                                                            |
| Claude Sonnet 5      | Claude-abonnement (Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 1 taal op 14 in het artikel: een vetgedrukt woord meer (zh); 1 in deze README: een tabelrij vastgeplakt aan de vorige, verborgen bij weergave (ar)               |
| Claude Haiku 4.5     | Claude-abonnement (Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 3 talen op het artikel: een sectietitel naar niveau 1 gegaan (en, pl, ro); in deze README niets voor de vergelijker, maar de interne links gedupliceerd in het Engels |
| Claude Sonnet 5      | Anthropic API-sleutel             | ⚠️ 11/14                | ⚠️ 12/14     | 3 talen op het artikel: een codeblok verschenen (es, de, hi); 2 in deze README: een link zonder markering (sv), een vetgedrukt woord (zh)                          |
| Qwen 3.7 Flash       | OpenRouter-sleutel                | ❌ 8/14                 | ⚠️ 10/14     | 1 taal geweigerd op het artikel, 5 andere wijken af; in deze README een veertigtal woorden in `code` gezet (ar)                                         |
| Grok 4.6             | Grok-abonnement                   | ❌ 8/14                 | niet beoordeeld | 5 talen op 14 geweigerd vanwege ontbrekende inline codes en URL's; het Nederlands wijkt op alles af                                                             |
| GPT-OSS 20B          | lokaal model (Ollama)             | ❌ 7/14                 | niet opnieuw gemeten | 4 talen op 14 geweigerd: het model liet daarin Franse passages achter, de vangrail heeft ze tegengehouden                                                  |
| MiMo v2.5 (gratis)   | OpenCode Zen, zonder account      | ❌ 11/14                | niet opnieuw gemeten | 1 taal geweigerd; een sectie verloren gegaan in het Pools                                                                                                          |
| Mistral Large        | Mistral API-sleutel               | ❌ 5/14                 | ❌ 1/14      | **een hele sectie verdwijnt**: 1 taal op het artikel (hi), 3 in deze README (ar, hi, ko) — en 3 talen geweigerd op het artikel                                    |
| DeepSeek V4 Flash    | OpenRouter-sleutel                | ❌ 3/14                 | niet opnieuw gemeten | 10 talen op 14 geweigerd; 37 minuten per taal                                                                                                                      |
| Claude Opus 5.5      | Claude-abonnement (Claude Code)   | ❌ 0/14                 | ✅ 14/14     | het artikel in alle 14 talen geweigerd door de vangrails van Opus vanwege een biologiebericht; niets in deze README                                               |

|     | Wat het symbool betekent                                                                                                                                                                             |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alle veertien talen vertaald, en niets wijkt af van de bron                                                                                                                                          |
| ⚠️  | alle veertien talen vertaald; wat verschilt is **opmaak** — een vetgedrukt woord, een `code`, een link die zijn haken verliest. Er ontbreekt geen tekst, geen URL, geen codeblok en geen sectie |
| ❌  | minstens één taal kon niet worden vertaald — het bestand is geweigerd, niet geschreven — **of** er ontbreekt inhoud in een geschreven bestand                                                       |

Wat u moet onthouden:

- **Een geweigerde vertaling is geen beschadigde vertaling.** Wanneer er bij terugkeer
  een token ontbreekt, wordt het bestand niet geschreven en telt de taal als
  geweigerd. Dit is wat er gebeurt bij Grok op het artikel: vier inline codes en
  drie URL's verloren vanaf het eerste segment, op de vijf niet-Latijnse schriften.
- **Een model kan een heel document weigeren vanwege één enkele zin.** Opus 5.5
  vertaalt deze README zonder enige afwijking, maar geen enkel monitoringartikel: zijn
  vangrails stoppen het antwoord bij een kort biologiebericht. Het bestand wordt niet
  geschreven en aipmt legt uit waarom.
- **Dit vangnet dekt geen koppen, tabellen, frontmatter of tekst.** Een model
  dat een sectie verwijdert, levert een bestand op dat de tool zonder morren
  wegschrijft — dat is het geval bij Mistral. Deze elementen kunnen niet worden
  vervangen door een token en de huidige beveiligingen controleren ze niet;
  `scripts/compare_structure.py` detecteert een verloren sectie, maar pas achteraf.
- **Grok heeft geen score voor deze README**: de CLI-sessie verliep na twaalf
  talen, waarvan elf zonder afwijking. Een onderbroken campagne krijgt geen score.
- **De dichtheid van het document weegt zwaarder dan de taal.** Grok houdt stand bij
  gewone README's en haakt af bij een artikel vol links, zelfs in het
  Nederlands.

Data en documenten: de kolom "Deze README" werd gemeten op 9 september 2026
op een bevroren revisie van dit bestand (785 regels, 285 inline codes, 89 tabelrijen),
sindsdien bijgewerkt — behalve de Antigravity- en Claude Code-rijen,
gemeten op 26 september op de revisie gepubliceerd met 1.14.0, die korter is
(600 regels, 257 inline codes, 85 tabelrijen). De kolom "Dicht monitoringartikel"
is afkomstig van de campagne van 4 en 5 september op een artikel van 589
regels, behalve de Grok-rij, opnieuw gemeten op 9 september op een andere editie van hetzelfde
monitoringartikel, en de Antigravity- en Claude Code-rijen, gemeten op 26 september
op hetzelfde artikel. De volledige tabellen, doorlooptijden en het protocol zijn te vinden in
[Gedetailleerde metingen](#gedetailleerde-metingen).

## Alle opties

| Optie                    | Beschrijving                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Enkel Markdown-bestand om te vertalen (alternatief voor `--source_dir`)                                        |
| `--source_dir`           | Bronmap met de Markdown-bestanden (standaard: `content/posts`)                                                 |
| `--target_dir`           | Uitvoermap voor de vertaalde bestanden (standaard: `traductions_en`)                                            |
| `--source_lang`          | Brontaal (standaard: `fr`)                                                                          |
| `--target_lang`          | Doeltaal (standaard: `en`)                                                                          |
| `--model`                | Specifiek te gebruiken model                                                                                  |
| `--eco`                  | Economische modellen gebruiken                                                                                |
| `--use_mistral`          | De Mistral AI-API gebruiken                                                                                   |
| `--use_claude`           | De Claude-API gebruiken                                                                                       |
| `--use_gemini`           | De Gemini-API gebruiken                                                                                       |
| `--use_grok`             | De xAI-API (Grok) gebruiken — vereist `XAI_API_KEY`                                                          |
| `--use_codex`            | De Codex-CLI gebruiken via het quotum van het ChatGPT-abonnement                                               |
| `--use_grok_cli`         | De Grok-CLI gebruiken via het quotum van het Grok-abonnement                                                   |
| `--use_antigravity`      | De Antigravity-CLI (`agy`) gebruiken via het quotum van het Google AI Pro- of Ultra-abonnement          |
| `--use_claude_code`      | De Claude Code-CLI (`claude -p`) gebruiken via het quotum van het Claude Pro- of Max-abonnement               |
| `--use_opencode`         | OpenCode (open source) gebruiken naar de in OpenCode geconfigureerde provider; vereist `--model provider/modèle`        |
| `--use_openrouter`       | OpenRouter gebruiken — vereist `OPENROUTER_API_KEY` en `--model fournisseur/modèle`                                                |
| `--force`                | Hervertaling forceren                                                                                         |
| `--keep_filename`        | Oorspronkelijke bestandsnaam behouden                                                                         |
| `--news`                 | Nieuwsmodus: beschermt EN-citaten, beheert vlaggen per taal                                                   |
| `--add_translation_note` | Een vertaalnotitie toevoegen                                                                                  |
| `--note_position`        | Positie van de notitie: `top`, `bottom` (standaard) of `both`                                  |
| `--note_format`          | Indeling van de notitie: `legacy` (standaard, vette alinea) of `marker`                                 |
| `--include_model`        | Modelnaam opnemen in het uitvoerbestand                                                                       |
| `--reasoning_effort`     | Redeneerinspanning GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                   |

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

`--eco` schakelt over naar het economische niveau van elke provider.

| Provider    | Kwaliteit (standaard)                                 | Economisch (`--eco`)      |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol` (ook `terra` en `luna` via `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, inspanning `low`                            | idem — `--eco` heeft geen effect |
| OpenCode    | `--model provider/modèle` verplicht                             | idem — `--eco` heeft geen effect |
| OpenRouter  | `--model fournisseur/modèle` verplicht                          | idem — `--eco` heeft geen effect |

### Via het ChatGPT-abonnement: `--use_codex`

Bestuurt de officiële Codex-CLI: de vertaling wordt afgeboekt van het quotum van
het ChatGPT-abonnement, zonder API-sleutel of facturering op basis van verbruik.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Het binaire bestand wordt gezocht in `CODEX_BIN`, daarna in `PATH`, en vervolgens in het package
  `openai-codex-cli-bin`. `~/.codex/auth.json` wordt nooit gelezen.
- `OPENAI_API_KEY` en `CODEX_API_KEY` worden verwijderd uit de omgeving van het
  subproces: een aanwezige sleutel zorgt er nooit voor dat er wordt overgeschakeld naar de API.
- Elk segment kost ten minste één "bericht" uit het 5-uursvenster — twee
  als de validatie mislukt en het opnieuw wordt geprobeerd. OpenAI geeft bij wijze van
  schatting 250–2.000 berichten/5 uur aan voor `gpt-5.6-luna` (`--eco`) en
  10–100 voor `gpt-5.6-sol` op een Plus-abonnement.
- `--model gpt-5.6-terra` en `--model gpt-5.6-luna` lopen eveneens via
  het abonnement. Een model waar het account geen recht op heeft, retourneert een 400 "model is
  not supported when using Codex with a ChatGPT account".
- Trager dan een API, en het verschil wordt groter naarmate het document toeneemt: op deze README
  een mediaan van 6 min 46 s per taal met `gpt-5.6-sol`, tegenover 36 s voor
  `gemini-3.7-flash`.
- Geweigerd in CI (`CI` of `GITHUB_ACTIONS` ingesteld): het abonnement verifieert
  via een persoonlijk sessiebestand, dat niet thuishoort op een gedeelde
  runner.
- Variabelen: `CODEX_BIN`, `CODEX_TIMEOUT` (seconden per segment, standaard 600).

### Via het Grok-abonnement: `--use_grok_cli`

Hetzelfde principe met de officiële Grok Build-CLI, via het SuperGrok- of
X Premium+-abonnement.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Zwakkere isolatie dan Codex.** De OS-sandbox van Grok werkt niet
  op veel recente Linux-systemen (AppArmor, container-runtime-sockets),
  en een profiel dat niet kan worden toegepast, start stilletjes zonder isolatie.
  Het script vraagt daarom standaard geen enkel profiel aan, meldt dit en
  vertrouwt op de `--deny`-regels van de CLI, waaronder de catch-all `*` — de enige
  laag die weigert te starten in plaats van geruisloos de beveiliging te verwijderen.
  `GROK_TRANSLATE_SANDBOX=read-only` vereist de OS-sandbox, en het opstarten
  mislukt als de machine hieraan niet kan voldoen.
- Het quotum is wekelijks, gedeeld met Chat, Imagine en Voice, en er is geen
  commando om dit uit te lezen: een batch kan het conversationele gebruik
  aantasten zonder waarschuwing.
- Variabelen: `GROK_BIN`, `GROK_HOME` (CLI-map, standaard `~/.grok`),
  `GROK_TIMEOUT` (standaard 900), `GROK_TRANSLATE_SANDBOX`.

### Via het Google-abonnement: `--use_antigravity`

Hetzelfde principe met `agy`, de officiële CLI van Antigravity: voor wie betaalt voor Google
AI Pro of Ultra wordt de vertaling afgeboekt van het abonnementsquotum in plaats
van gefactureerd per token. Dit is de enige weg naar dit quotum: Gemini CLI
bedient deze accounts niet meer sinds 18 juni 2026
([aankondiging](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
en de SDK van Antigravity accepteert enkel een API-sleutel of een Google Cloud-project.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Er blijft geen betaalde route open.** agy ontvangt vanuit uw
  omgeving slechts een gesloten lijst met variabelen — `PATH`, taal en tijdzone,
  terminal, identiteit, proxy's en certificaten, sessiebus — en geen enkele sleutel:
  meerdere variabelen schakelen een aanroep om zonder iets weer te geven (gemeten:
  een ervan stuurt het document naar een externe gateway, een andere naar een gefactureerd
  Google Cloud-project), en een weigeringslijst zag er bij elke controle wel een over het hoofd.
  Vóór elk segment moet `agy -p /config`, wat geen quotum kost, aantonen dat
  betaalde AI-tegoeden zijn uitgeschakeld, zonder API-sleutel of Google Cloud-project — een
  ontbrekende instelling geldt als weigering —, anders wordt er niets vertaald; het logboek van elke
  aanroep moet vervolgens het abonnement bevestigen (`authMethod=consumer`), anders wordt het
  antwoord geweigerd.
- **Isolatie.** Elke aanroep draait in een tijdelijke, afgeschermde
  privédirectory, met een vertaalagent zonder tools: uw instellingen, regels,
  plug-ins, MCP-servers en hooks van agy komen er niet in, er wordt niets toegevoegd aan uw
  geschiedenis en de inloggegevens blijven in de sleutelbos, die aipmt nooit leest.
  Een onvindbare agent zorgt ervoor dat agy geruisloos terugvalt op zijn programmeeragent
  en diens tools: een volledige regel in het logboek moet de juiste agent bevestigen — een
  document dat dit bericht citeert vervangt dit niet —, anders volgt een weigering.
- **Platformen**: Linux, binnen een sessie met een sleutelbos (D-Bus-sessiebus,
  Secret Service); macOS wordt geaccepteerd, maar is niet getest. Geweigerd
  onder Windows, waar agy de variabelen die elke aanroep isoleren niet leest, en
  onder Linux zonder sessiebus — SSH-sessie, container, server: agy bewaart
  zijn token daar in een bestand van `~/.gemini`, dat door de isolatie wordt verborgen. De
  weigering volgt vóór elke start, inclusief de reden, in plaats van een minuut
  te moeten wachten op een inlogcode.
- **Modellen**: die van `agy models`. Bij Gemini zit de inspanning in de naam verwerkt
  (`gemini-3.8-flash-medium`…): een naam zonder achtervoegsel wordt vóór de aanroep geweigerd,
  en `--reasoning_effort` heeft geen effect. Standaard `gemini-3.8-flash-medium`,
  en `gemini-3.7-flash-low` in `--eco`; de benchmarks die deze hebben bepaald, worden
  beschreven in [Gedetailleerde metingen](#gedetailleerde-metingen). Claude en GPT-OSS
  hebben een eigen quotum dat veel kleiner is: ongeveer 1% van het 5-uursvenster
  per gemeten aanroep, vergeleken met 0,05% bij Flash.
- **Quotum**: per groep, een venster van 5 uur en een wekelijks venster, naar
  rato van de tokenkosten. Gemeten op het account van de auteur: ongeveer
  16 punten van het 5-uursvenster per miljoen brontekens in
  `gemini-3.8-flash-medium`, 14 in `gemini-3.7-flash-medium` en 7 tot 8 bij
  een lage inspanning — een README van 40.000 tekens kost dus iets meer dan een
  half punt. De wekelijkse limiet hangt af van het niveau. Opnieuw proberen volgt
  wat agy als herkansbaar aangeeft; bij gebrek daaraan wordt een uitgeput venster nooit
  opnieuw geprobeerd: het laat elk bestand mislukken tot de reset
  die `/usage` aangeeft.
- **Trager dan de API**: bij het dichte artikel met de metingen was de mediaan 3 min 59 s per
  taal in `gemini-3.8-flash-medium` en 3 min 14 s in
  `gemini-3.7-flash-medium`, vergeleken met 1 min 18 s voor Gemini 3.7 Flash via de API.
- **Onderbreking**: Ctrl-C of een gesloten terminal stopt agy samen met het
  commando in plaats van het zijn beurt te laten afmaken op uw quotum; hetzelfde
  geldt voor Codex, Grok CLI en OpenCode. Onder `nohup` gaat de vertaling door.
- Geweigerd in CI (`CI` of `GITHUB_ACTIONS` ingesteld): de inloggegevens bevinden zich in een
  persoonlijke sleutelbos. Gebruik op een runner `--use_gemini` met `GOOGLE_API_KEY`.
- Variabelen: `AGY_BIN` (anders de `PATH`, vervolgens `~/.local/bin/agy`),
  `AGY_TIMEOUT` (seconden per segment, inclusief opstarten, standaard 900).

**Gebruiksvoorwaarden: uw account staat op het spel.** De
[voorwaarden van Antigravity](https://antigravity.google/terms) (sectie 6) en de
[FAQ](https://antigravity.google/docs/faq/) verbieden toegang tot de dienst
via software van derden met behulp van de Antigravity-inloggegevens — Claude Code,
OpenClaw en OpenCode worden daarin genoemd —, op straffe van opschorting van het account. aipmt
leest noch hergebruikt het token: het start het officiële binaire bestand in de
[headless-modus](https://antigravity.google/docs/cli/headless/) die Google
documenteert voor scripts en CI. Een medewerker van Google noemde het starten van
`agy -p` vanuit een lokaal script voor eigen werk "standaard"
([officieel forum, 25 september 2026, niet-bindend antwoord](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
geen enkele tekst geeft uitsluitsel over het geval van een gedistribueerde tool zoals deze.

**Alleen openbare documenten.** Volgens sectie 5 van dezelfde voorwaarden kunnen de
interacties — prompts, antwoorden, metadata — worden gebruikt om de producten en de
machine learning van Google te verbeteren en kunnen deze door mensen worden nagekeken,
ook bij een betaald abonnement. Afmelden verloopt via de instelling
`enableTelemetry`, waarvan het effect niet gedocumenteerd is en die aipmt niet instelt; uw agy-instellingen
worden niet meegenomen in de geïsoleerde omgeving. Stuur hier niets vertrouwelijks doorheen.

### Via het Claude-abonnement: `--use_claude_code`

Hetzelfde principe geldt voor `claude`, de officiële CLI van Claude Code, in de modus `-p`: voor
wie betaalt voor Claude Pro of Max, wordt de vertaling verrekend met het quotum van
het abonnement in plaats van gefactureerd per token. Niet te verwarren met
`--use_claude`, de API van Anthropic, die wordt gefactureerd naar verbruik.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Er blijft geen enkele betaalde route openstaan, en elke aanroep bewijst dat.** Claude
  Code ontvangt uit uw omgeving uitsluitend een gesloten lijst van variabelen — geen
  API-sleutel, geen token, geen cloudprovider, noch enige markering van de Claude Code-sessie
  vanuit waar aipmt zou zijn gestart. Vóór het eerste segment moet `claude auth status`
  de abonnementsverbinding tonen, zonder Console-sleutel, en `/usage`, wat
  geen quotum kost, moet dit bevestigen; elke aanroep bevestigt dit op zijn beurt in het
  initialisatie-event, anders wordt het antwoord geweigerd.
- **Schakel "extra usage" uit** (claude.ai, Instellingen → Verbruik) om
  de nul euro te handhaven: wanneer dit is ingeschakeld, neemt het het over van een uitgeput venster en
  brengt het kosten in rekening zonder een foutmelding te tonen. aipmt stopt de vertaling zodra het
  quotumoverzicht van een aanroep dit aangeeft, maar die aanroep is dan al meegeteld.
- **Gedeeld quotum met uw Claude Code-sessies.** Elke aanroep rapporteert
  het verbruik van de vensters van 5 uur en van de week; boven de 80%
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) wordt er geen segment meer gestart, om
  niet uit te putten wat nodig is voor uw werk.
- **Inperking.** Elke aanroep draait zonder tools, in een privé en
  wegwerpmap, in een modus zonder aanpassingen: noch uw `CLAUDE.md`, noch uw plug-ins,
  hooks, MCP-servers of instellingen worden geladen, en er wordt niets bewaard van de
  sessie. Bijlagen zijn uitgeschakeld: een `@chemin` in uw document
  blijft tekst en opent geen enkel bestand (gemeten).
- **Modellen**: standaard `sonnet`, met inspanningsniveau `low`, en ook in `--eco`:
  `--eco` verandert niets op dit pad. Gemeten op dezelfde documenten is `haiku`
  twee keer zo traag — het redeneert zonder dat dit kan worden verhinderd — voor
  nauwelijks lagere kosten, en `opus` weigert biologische content (zie volgend
  punt). Beide blijven toegankelijk via `--model`; deze aliassen volgen het
  nieuwste model uit hun familie. `fable` en de `[1m]`-varianten worden geweigerd,
  omdat ze via betaalde credits verlopen. `--reasoning_effort` regelt de inspanning,
  waar een vertaling niets aan heeft: het gemeten redeneren is nihil of vrijwel nihil.
- **Opus weigert bepaalde biologiegerelateerde content.** De vangrails zijn
  strenger dan die van Sonnet, en de foutmelding van Anthropic waarschuwt dat ze
  "can sometimes flag biology-research-adjacent work". Gemeten: een kort
  nieuwsbericht over 279 gegenereerde moleculen leidde tot weigering van het artikel in alle veertien
  talen. Er wordt niets geschreven: aipmt weigert het afgekapte antwoord, noemt de
  vangrails en adviseert `--model sonnet`.
- Geweigerd in CI (`CI` of `GITHUB_ACTIONS` gedefinieerd) en onder Windows (niet gemeten).
- Variabelen: `AIPMT_CLAUDE_BIN` (anders de `PATH`, daarna `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (seconden per segment, standaard 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (standaard 0.8), `CLAUDE_CONFIG_DIR` (het account van
  Claude Code, nooit overgenomen uit een `.env` van het project); werkmappen onder
  `XDG_CACHE_HOME/aipmt/claude-code` (standaard `~/.cache`).

**Gebruiksvoorwaarden: het is uw eigen account dat wordt gebruikt.** De
[juridische pagina van Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
verbiedt niet "an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription": dit is wat aipmt doet, dat de officiële
binary start en het token nooit uitleest. Maar Anthropic "does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users", geeft de voorkeur aan de API-sleutel voor tools van derden,
"including open-source projects", en behoudt zich het recht voor om hun
verbruik in mindering te brengen op betaalde credits
([Claude-helpcentrum](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Geen enkele tekst geeft uitsluitsel over het geval van een gedistribueerde tool die de binary start.

**Gegevens**: bij Free-, Pro- en Max-accounts is modeltraining
ook van toepassing op Claude Code wanneer de privacyinstelling dit toestaat
([gegevenspagina](https://code.claude.com/docs/en/data-usage)). aipmt bewaart
geen enkele lokale transcriptie (`--no-session-persistence`). Laat hier
niets vertrouwelijks doorheen lopen.

### Naar de provider van uw keuze: `--use_opencode`

[OpenCode](https://opencode.ai) is een open-source code-agent (MIT) die
verzoeken routeert naar de daarin geconfigureerde providers: API-sleutel, abonnement,
de OpenCode Zen-gateway (gratis modellen, zonder account) of een lokaal model. Twee
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

`--model` is verplicht: zonder deze optie zou OpenCode terugvallen op een gratis model
waarvan de uitwisselingen voor training kunnen worden gebruikt, en die keuze wordt niet voor
u gemaakt.

Inperking bij elke aanroep:

- een inline configuratie, die voorrang heeft op die van uzelf, definieert een agent `aipmt`
  waarvan alle tools worden geweigerd (`permission: { "*": "deny" }`), sessiedeling
  uitgeschakeld, `--pure`, nooit `--auto`;
- een lege wegwerpwerkmap, met `OPENCODE_DISABLE_PROJECT_CONFIG` en
  `OPENCODE_DISABLE_CLAUDE_CODE` geplaatst — zonder deze injecteert OpenCode in de
  prompt het `AGENTS.md` van de huidige map en `~/.claude/CLAUDE.md`. De
  globale `~/.config/opencode/AGENTS.md` blijft geïnjecteerd; OpenCode biedt geen mogelijkheid
  om deze uit te sluiten;
- outputcontract: returncode 0, geen enkel `error`-event, geen enkele aanroep
  van tools, laatste stap in `stop`, niet-lege tekst, en de agent `aipmt`
  daadwerkelijk geladen — een onbekende `--agent` zorgt er niet voor dat OpenCode faalt, het
  valt stilzwijgend terug op de codeeragent;
- er wordt geen enkele sleutel van `aipmt` doorgegeven, behalve `OPENCODE_API_KEY`, de sleutel
  van OpenCode zelf. Providers worden geconfigureerd in OpenCode, niet in
  het `.env` van `aipmt`.

Goed om te weten:

- De gratis modellen van Zen zijn veranderlijk, met ongedocumenteerde limieten, en
  de uitwisselingen ermee kunnen worden gebruikt voor training: geschikt voor openbare documentatie,
  niet voor privégegevens.
- Een lokaal model moet ten minste 16k context-tokens bieden, aangezien segmenten
  tot 16.000 tekens groot kunnen zijn. Ollama configureert er vaak 4.096: gebruik
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

`reasoningEffort: "none"` schakelt het redeneerproces (thinking) uit dat Ollama standaard activeert op deze
modellen, en dat niet kan worden uitgeschakeld via een Modelfile. Gemeten bij een zin van
zes woorden: 919 redeneertokens en 68 seconden zonder de optie, 9 tokens mét.

### Naar meer dan 400 modellen: `--use_openrouter`

OpenRouter is een router die naar verbruik factureert vanuit één enkel tegoed, vóór modellen
die door derden worden gehost — waaronder open Chinese modellen die geen
enkele andere provider hier aanbiedt.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` is verplicht. Een preflight-controle, uitgevoerd vóór enige facturatie, regelt
twee bijzonderheden van de routering:

- **Hetzelfde model wordt aangeboden door tientallen hosts met verschillende
  limieten** — bij `z-ai/glm-5.3-flash` zijn er 23 hosts, waarvan er één begrensd is op
  2.048 output-tokens. De preflight leest `/api/v1/models/{modèle}/endpoints`,
  sluit hosts met minder dan 8.000 output-tokens of een gedegradeerde status uit, en
  zet de overige vast met `allow_fallbacks: false`.
- **Redeneren wordt gefactureerd tegen het output-tarief** — 107 tokens tegenover 2 bij
  een "OK"-respons van `z-ai/glm-5.2`. Het staat standaard uitgeschakeld; modellen
  die dit vereisen, krijgen het laagst mogelijke inspanningsniveau dat ze accepteren, aangezien de standaardwaarde
  uit de catalogus de output kan verzadigen vóór het einde van de vertaling.
  `--reasoning_effort` behoudt voorrang.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Het contextvenster is afkomstig uit de catalogus. Een model met minder dan 16.400 tokens wordt
  vóór elke aanroep geweigerd: minimaal 8.400 voor de prompt en het segment, en 8.000 voor de output.
- Een slug die ontbreekt in de catalogus, een onbereikbare catalogus of het ontbreken
  van een host die aan de limiet voldoet, breekt het commando af.
- `finish_reason=length` met een lege output betekent dat het budget is verbruikt door het
  redeneren, niet een afkapping: de melding maakt dit onderscheid.
- `--eco` heeft geen effect.
- Variabelen: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (standaard `https://openrouter.ai/api/v1`, `https://`
  vereist), `OPENROUTER_TIMEOUT` (standaard 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (standaard 30).

### Vertaalnotitie

`--add_translation_note` voegt een notitie toe, aan `bottom` (standaard), `top` (na de
front matter) of `both` (`--note_position`), in de indeling `legacy` (vetgedrukte
paragraaf, standaard) of `marker` (`--note_format`). De indeling `marker` is een
onzichtbare Markdown-referentiedefinitie,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
gevolgd door een vetgedrukt citaat: leesbaar op GitHub, bruikbaar tijdens de build via een
remark-plugin.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Gedetailleerde metingen

Alle metingen zijn daadwerkelijk uitgevoerde vertalingen met `aipmt`, naar
veertien talen: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Geschreven** telt de bestanden die door de checks zijn goedgekeurd; **Zonder
afwijking** telt de bestanden waarin `scripts/compare_structure.py` niets opmerkt — hetzelfde aantal
secties, tussenkopjes, links, unieke URL's, codeblokken,
inline code, tabelrijen, blockquotes en vetgedrukte woorden.

"Zonder afwijking" betekent "niets gedetecteerd", niet "identiek": de vergelijker
telt elementen zonder de inhoud ervan te lezen. Hij meldt geen verwijderde kop op
niveau 4, geen vervangen inline-codetekst, geen verwisselde vlag, noch een interne link die wordt weergegeven met een haakje te veel,
`[texte]((#ancre))`, waardoor deze nergens meer naartoe leidt — en hij beoordeelt het
taalgebruik niet.

### Dicht curatie-artikel, modus `--news`

Een editie van het [AI-overzicht van jls42.org](https://jls42.org/fr/news):
589 regels, 140 links, 21 secties, 3 beschermde Engelse citaten. Campagne
van 4 en 5 september 2026.

| Model                                           | Toegang            | Geschreven | Zonder afwijking | Mediaan/taal   |
| ----------------------------------------------- | ------------------ | ---------- | ---------------- | -------------- |
| `gemini-3.7-flash`                              | Google-API         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google-abonnement  | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google-abonnement  | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT-abonnement | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | Claude-abonnement  | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | Anthropic-API      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | Claude-abonnement  | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | lokaal             | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral-API        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok-abonnement    | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | Claude-abonnement  | 0/14    | ❌ 0/14      | —              |

Grok werd op 9 september opnieuw gemeten op een andere editie van hetzelfde overzicht
(356 regels): 9 talen geschreven van de 14, 8 zonder afwijking. Dat is het cijfer dat
in de hoofdtabel staat. Drie afgebroken campagnes zijn niet
opgenomen: `qwen3.5-27b` (9 talen) en `kimi-k2.6` (4) wegens gebrek aan credits,
`z-ai/glm-5.3-flash` waarvan de twee mislukkingen te wijten waren aan een redeneerinstelling
die de provider sindsdien heeft gecorrigeerd. De OpenRouter-regels zijn gemeten met de
standaardinstellingen van de router, vóór `--use_openrouter`; `z-ai/glm-5.2`,
opnieuw gemeten met de meegeleverde provider, levert hetzelfde resultaat van 14/14 op. De cijfers zijn
op 10 september herberekend met de huidige vergelijker: `qwen3.8-flash` en
`qwen3.7-flash` winnen elk één taal ten opzichte van de eerste
publicatie, de overige blijven ongewijzigd.

De `--use_antigravity`-regels zijn op 26 september gemeten op hetzelfde
artikel, met vier vertalingen parallel: `gemini-3.7-flash-medium` in de ochtend,
`gemini-3.8-flash-medium` in de middag. In het Engels heeft elk model zelf
de drie regels Franse vertaling onder de citaten verwijderd, zonder een vlag te
verzinnen, en de Engelse citaten zijn intact gebleven: de fallback-opschoning hoefde
niets te doen. In `--eco` (`gemini-3.7-flash-low`), op slechts vier talen
(en, ja, ar, hi): 4 geschreven van de 4, allemaal zonder afwijking, mediaan van
1 min 52 s. Een tegenproef op dezelfde dag met een recentere editie van het overzicht,
die van 25 september (438 regels, 2 Engelse citaten), buiten de blog vertaald
met `gemini-3.7-flash-medium`: 14 geschreven van de 14, allemaal zonder afwijking, 87 tot
128 s per taal.

De `--use_claude_code`-regels zijn op 26 september gemeten op hetzelfde
artikel, met vier vertalingen parallel, bij inspanning `low`. Met `sonnet` zijn de
Engelse citaten intact in alle veertien talen en in het Engels heeft het
model zelf de regels met Franse vertaling verwijderd, zonder een vlag te
verzinnen. `opus` heeft geen enkele taal geschreven: in elke taal stopten de vangrails
het antwoord bij het laatste segment vanwege een kort bericht over 279 gegenereerde
moleculen voor een bindingslocatie. Als dit bericht afzonderlijk wordt verzonden, wordt het geweigerd
onder de categorie "bio"; `sonnet` heeft het overal vertaald. `haiku` schrijft
alle veertien talen; in drie daarvan (en, pl, ro) verspringt een sectietitel van
niveau 2 naar niveau 1. Het model redeneert zonder dat dit kan worden verhinderd — 61% van
zijn output-tokens —, wat resulteert in meer dan het dubbele van de tijd van `sonnet`.

### README van dit project, standaard Markdown

Vastgezette revisie op 9 september 2026: 785 regels, 285 inline-codes, 40
blokafsluitingen, 89 tabelrijen. Vier vertalingen parallel.

| Model                                           | Geschreven | Zonder afwijking | Mediaan/taal   | Wat verschilt                                                            |
| ----------------------------------------------- | ---------- | ---------------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14      | ✅ 14/14         | 1 min 43 s     | niets                                                                    |
| `opus` (`--use_claude_code`)                    | 14/14      | ✅ 14/14         | 1 min 48 s     | niets                                                                    |
| `haiku` (`--use_claude_code`)                   | 14/14      | ✅ 14/14         | 4 min 02 s     | niets voor de vergelijker; interne links gedupliceerd (en)               |
| `gemini-3.7-flash`                              | 14/14      | ⚠️ 13/14         | 36 s           | een vetgedrukt woord (ja)                                                |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14      | ⚠️ 13/14         | 1 min 22 s     | een vetgedrukt woord (ko)                                                |
| `sonnet` (`--use_claude_code`)                  | 14/14      | ⚠️ 13/14         | 2 min 20 s     | een tabelrij vastgeplakt aan de vorige (ar)                              |
| `claude-sonnet-5`                               | 14/14      | ⚠️ 12/14         | 2 min 56 s     | een link (sv), een vetgedrukt woord (zh)                                 |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14      | ⚠️ 12/14         | 6 min 46 s     | een vetgedrukt woord (ar, ja)                                            |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14      | ⚠️ 11/14         | 2 min 34 s     | een vetgedrukt woord (hi, ja, ko)                                        |
| `qwen/qwen3.7-flash`                            | 14/14      | ⚠️ 10/14         | 2 min 17 s     | 40 inline-codes toegevoegd in het Arabisch; vetgedrukt (hi, ja, ko)       |
| `mistral-large-latest`                          | 14/14      | ❌ 1/14          | 2 min 44 s     | een sectie verloren gegaan (ar, hi, ko); codeblokken toegevoegd (ja, ko, ro, zh) |

Twee onderbroken campagnes zijn niet opgenomen: Grok, CLI-sessie verlopen
na twaalf talen (elf zonder afwijking), en `qwen3.8-flash`, HTTP 429 van zijn
host na twee. `opencode/mimo-v2.5-free` en `ollama/gpt-oss-20b-32k`
zijn niet opnieuw gemeten op deze revisie; op die van 4 en 5 september,
die 277 regels korter was, schreven ze elk 9 van de 14 vertalingen, waarvan 7
en 1 zonder afwijking.

De rijen `--use_antigravity` en `--use_claude_code` zijn niet gemeten op
de vastgezette revisie, maar op 26 september op de versie die met 1.14.0 is gepubliceerd: 600
regels, 257 inline-codes, 30 blokafsluitingen, 85 tabelrijen. Omdat
deze 185 regels korter is, kan ze niet één-op-één worden vergeleken met de andere rijen;
die rijen kunnen onderling wel worden vergeleken. Wat betreft de interne links, die de
vergelijker niet controleert: `gemini-3.8-flash-medium` hield ze intact in
alle veertien talen, `gemini-3.7-flash-medium` brak ze in het Italiaans;
`sonnet` en `opus` hielden ze overal intact, `haiku` dupliceerde ze in het
Engels.

### Vier README's van bekende projecten

FastAPI, Ollama, tldr-pages en Vue.js, rechtstreeks overgenomen van GitHub —
eenvoudigere documenten dan de twee voorgaande. De campagne richtte zich op de modellen
die moeite hadden; Gemini dient hierbij als vergelijkingspunt.

| Model                     | Bereik                     | Geschreven | Zonder afwijking |
| ------------------------- | -------------------------- | ---------- | ---------------- |
| `gemini-3.7-flash`        | 4 projecten × 14 talen     | 56/56      | ✅ **55/56**     |
| `opencode/mimo-v2.5-free` | 4 projecten × 14 talen     | 55/56      | ❌ 47/56         |
| `grok-4.6` (abonnement)   | 4 projecten × ar, hi, ja, zh | 16/16      | ❌ 14/16         |
| `ollama/gpt-oss-20b-32k`  | 4 projecten × ar, hi, ja, zh | 15/16      | ❌ 9/16          |

### Wat deze metingen niet zijn

- **Geen uitputtende ranglijst**: OpenRouter alleen al biedt meer dan vierhonderd
  modellen aan, waarvan er ongeveer vijftien zijn gemeten.
- **Indicatieve tijdsduren**: drie tot zes vertalingen tegelijk afhankelijk
  van de campagnes, en de doorvoersnelheid van een provider varieert gedurende de dag.
- **Tijdsgebonden observaties**: modellen veranderen onder dezelfde naam, en uw
  documenten zijn niet de onze.

Om de meting op uw eigen documenten te herhalen, op een vastgezette kopie van het bestand:

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

Beide regels zijn noodzakelijk: zonder `pip install -e .` antwoordt `python -m aipmt`
met `No module named aipmt`.

Kwaliteitstools, optioneel maar aanbevolen:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

De 28 vertalingen van de repository (README en CHANGELOG, veertien talen) worden
opnieuw gegenereerd met `./regen_translations.sh --force` — standaard Codex en `gpt-5.6-sol` via
het ChatGPT-abonnement, vier parallel. `REGEN_PROVIDER` en
`REGEN_MODEL` wijzigen het pad: `antigravity` blijft op een abonnement, dat
van Google, en slaagt zonder uitzondering; een gefactureerde API (`openai`, `gemini`,
`grok`, `openrouter`) wordt geweigerd zonder `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` maximeert elke taak (600 s, 1.800 s voor Codex en
Antigravity). Details over de tools zijn te vinden in `CLAUDE.md`.

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

Dit programma wordt gedistribueerd **zonder enige garantie**, onder de voorwaarden van
secties 15 en 16 van de GPL v3: geleverd "in de huidige staat", zonder garantie van verkoopbaarheid
of geschiktheid voor een bepaald doel, en de auteur kan niet aansprakelijk worden gesteld
voor schade die voortvloeit uit het gebruik ervan. De tekst van de
licentie heeft voorrang op deze samenvatting.

- **Lees na vóór publicatie.** De beschermingen dekken codeblokken, inline-code,
  URL's, ankers en citaten in de modus `--news` — noch titels,
  noch tabellen, noch de frontmatter, noch de betekenis van uw zinnen.
- **Uw documenten worden verzonden naar de gekozen provider**, onder diens gebruiksvoorwaarden
  en gegevensbeleid. Sommige gratis modellen kunnen uw interacties hergebruiken voor training,
  en de voorwaarden van Antigravity staan Google toe om ze te hergebruiken en door mensen te laten nalezen,
  inclusief bij een betaald abonnement; een lokaal model is de enige manier waarbij er geen
  gegevens van uw machine naar buiten gaan.
- **API-aanroepen worden aan u gefactureerd.** Dit programma stelt geen limiet
  aan de uitgaven: een lang document, een herstart na een fout of een model dat veel redeneert,
  kosten meer.
- **De gepubliceerde metingen zijn tijdsgebonden observaties**, geen garanties.

De genoemde product- en bedrijfsnamen zijn eigendom van hun respectievelijke
houders. Dit project is aan geen van hen gelieerd.

**Artikel vertaald van het Frans naar het Nederlands met gemini-3.8-flash-medium.**

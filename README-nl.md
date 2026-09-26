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
structuur: codeblokken, inline code, URL's, ankers, tabellen en front
matter. Tien manieren om een model aan te roepen — vijf API's, drie abonnementen zonder
facturering op basis van verbruik, twee routers — en een gepubliceerde meting van wat elk
model daadwerkelijk behoudt.

## In het kort

- **Tien provider-paden**: API's van OpenAI, Mistral, Claude, Gemini en Grok;
  ChatGPT- (Codex), Grok- en Google-abonnementen (Antigravity) zonder facturering op
  basis van verbruik; OpenCode- (open source, gratis of lokaal) en OpenRouter-routers
  (meer dan 400 modellen).
- **Geen fouten door een verloren token**: codeblokken, inline code,
  URL's, ankers en citaten worden vóór de aanroep vervangen door tokens en
  bij terugkomst gecontroleerd. Als er één ontbreekt, wordt het bestand niet weggeschreven.
- **Lange documenten**: segmentatie volgens het contextvenster van het model.
- **Modus `--news`**: beschermde Engelse citaten en vlaggen beheerd per
  taal, voor curatie-artikelen.
- **Modus `--eco`**: snelle en goedkopere modellen.
- **Optionele vertaalnotitie**, bovenaan, onderaan of beide.

## Installatie

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 of nieuwer. Zie
[Bijdragen](#bijdragen) om vanuit de repository te installeren.

## Configuratie

Sleutels worden op drie plaatsen gelezen, van hoogste naar laagste prioriteit; elke stap
vult alleen aan wat de vorige leeg laat.

|     | Waar                                          | Waarvoor                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Omgevingsvariabelen                           | CI, containers, eenmalige afwijking   |
| 2   | `.env` van de huidige map (of een bovenliggende) | een projectspecifieke sleutel         |
| 3   | `~/.config/aipmt/.env`                        | eenmaal geïnstalleerd, overal geldig  |

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

**De `.env` van een project kan noch aanroepen omleiden noch het uitgevoerde programma
kiezen.** Het levert sleutels, nooit een bestemming of een binair bestand: elke
variabele in `_BASE_URL`, `_API_BASE`, `_ENDPOINT` of `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, de proxy's (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), de certificaatarchieven (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) en `XDG_CONFIG_HOME` /
`APPDATA` worden daarin genegeerd, met een waarschuwing. Een gekloonde repository mag niet
in staat zijn uw sleutel te kapen, noch u ertoe brengen zijn eigen programma uit te voeren bij de
eerste vertaling. Dit bestand wordt ook zonder interpolatie gelezen:
`NOM=${OPENAI_API_KEY}` kopieert de sleutel daarin niet. Plaats deze variabelen in
de omgeving of in `~/.config/aipmt/.env`.

Optionele variabelen: `XAI_BASE_URL` (standaard `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (seconden per aanroep, standaard 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(standaard 600), `GROK_BIN`, `GROK_HOME` (standaard `~/.grok`), `GROK_TIMEOUT`
(standaard 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (standaard 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (standaard 600), `OPENROUTER_BASE_URL`
(`https://` vereist), `OPENROUTER_TIMEOUT` (standaard 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (standaard 30). Elk hiervan wordt gedetailleerd beschreven in de
sectie van de desbetreffende provider.

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

Exitcodes: `0` als alles is geslaagd of overgeslagen, `1` als er een mislukt bestand
overblijft (lijst op standaardfoutuitvoer), `2` als de configuratie de oorzaak is.
Een mislukt bestand wordt nooit weggeschreven, zelfs niet als het schrijven zelf mislukt:
de inhoud wordt ernaast geschreven en vervolgens hernoemd. Opnieuw uitvoeren volstaat.

## Welk model te kiezen

Gemeten op twee echte documenten, door elk model vertaald naar dezelfde veertien talen.
**Het cijfer is het aantal talen, op veertien, waar de vertaling is weggeschreven en
waarin niets verschilt van de bron.**

| Model                | Toegangswijze                     | Dicht curatie-artikel   | Deze README  | Wat verschilt, en in hoeveel talen                                                                                                    |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | Google API-sleutel                | ✅ 14/14                | ⚠️ 13/14     | 1 taal op 14: een vetgedrukt woord extra (ja)                                                                                         |
| **Gemini 3.7 Flash** | Google-abonnement (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 1 taal op 14: een vetgedrukt woord minder (ko)                                                                                        |
| **GPT-5.6 Sol**      | ChatGPT-abonnement, of OpenAI-sleutel | ✅ 14/14            | ⚠️ 12/14     | 2 talen op 14: een vetgedrukt woord minder (ar, ja)                                                                                   |
| **GLM-5.2**          | OpenRouter-sleutel                | ✅ 14/14                | ⚠️ 11/14     | 3 talen op 14: een vetgedrukt woord minder (hi, ja, ko)                                                                               |
| Claude Sonnet 5      | Anthropic API-sleutel             | ⚠️ 11/14                | ⚠️ 12/14     | 3 talen op het artikel: een codeblok verschenen (es, de, hi); 2 op deze README: een link zonder opmaak (sv), een vetgedrukt woord (zh) |
| Qwen 3.7 Flash       | OpenRouter-sleutel                | ❌ 8/14                 | ⚠️ 10/14     | 1 taal geweigerd op het artikel, 5 andere wijken af; op deze README ongeveer veertig woorden in `code` geplaatst (ar)        |
| Grok 4.6             | Grok-abonnement                   | ❌ 8/14                 | niet beoordeeld | 5 talen geweigerd op 14, door ontbreken van inline codes en gerenderde URL's; het Nederlands wijkt op alles af                       |
| GPT-OSS 20B          | lokaal model (Ollama)             | ❌ 7/14                 | niet opnieuw gemeten | 4 talen geweigerd op 14: het model liet Franse passages achter, de vangrail heeft ze tegengehouden                               |
| MiMo v2.5 (gratis)   | OpenCode Zen, zonder account      | ❌ 11/14                | niet opnieuw gemeten | 1 taal geweigerd; een sectie verloren in het Pools                                                                                    |
| Mistral Large        | Mistral API-sleutel               | ❌ 5/14                 | ❌ 1/14      | **een volledige sectie verdwijnt**: 1 taal op het artikel (hi), 3 op deze README (ar, hi, ko) — en 3 talen geweigerd op het artikel   |
| DeepSeek V4 Flash    | OpenRouter-sleutel                | ❌ 3/14                 | niet opnieuw gemeten | 10 talen geweigerd op 14; 37 minuten per taal                                                                                         |

|     | Wat het symbool betekent                                                                                                                                                                             |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alle veertien talen vertaald, en niets wijkt af van de bron                                                                                                                                          |
| ⚠️  | alle veertien talen vertaald; wat afwijkt is **opmaak** — een vetgedrukt woord, een `code`, een link die zijn haken verliest. Geen tekst, geen URL, geen codeblok, geen sectie ontbreekt     |
| ❌  | ten minste één taal kon niet worden vertaald — het bestand is geweigerd, niet weggeschreven — **of** er ontbreekt inhoud in een weggeschreven bestand                                               |

Wat hiervan te onthouden:

- **Een geweigerde vertaling is geen beschadigde vertaling.** Wanneer er bij terugkomst
  een token ontbreekt, wordt het bestand niet weggeschreven en telt de taal als
  geweigerd. Dit is wat er gebeurt bij Grok op het artikel: vier inline codes en
  drie URL's verloren vanaf het eerste segment, bij de vijf niet-Latijnse schriften.
- **Dit vangnet dekt geen titels, tabellen, frontmatter of
  tekst.** Een model dat een sectie verwijdert, levert een bestand op dat de tool
  zonder morren wegschrijft — dit is het geval bij Mistral. Deze elementen kunnen niet
  worden vervangen door een token, en de huidige vangrails controleren ze niet;
  `scripts/compare_structure.py` detecteert een verloren sectie, maar pas achteraf.
- **Grok heeft geen beoordeling op deze README**: de CLI-sessie verliep na twaalf
  talen, waarvan elf zonder afwijking. Een onderbroken campagne wordt niet beoordeeld.
- **De dichtheid van het document weegt zwaarder dan de taal.** Grok houdt stand op
  gewone README's en haakt af op een artikel vol links, ook in het
  Nederlands.

Datums en documenten: de kolom "Deze README" werd gemeten op 9 september 2026
op een bevroren revisie van dit bestand (785 regels, 285 inline codes, 89 tabelregels),
sindsdien bijgewerkt — behalve de regel Antigravity, gemeten op
26 september op de revisie gepubliceerd bij 1.14.0, die korter is (600 regels,
257 inline codes, 85 tabelregels). De kolom "Dicht curatie-artikel"
is afkomstig van de campagne van 4 en 5 september op een artikel van 589 regels,
behalve de regel Grok, opnieuw gemeten op 9 september op een andere editie van dezelfde
curatie, en de regel Antigravity, gemeten op 26 september op hetzelfde artikel.
De volledige tabellen, tijdsduren en het protocol zijn te vinden in
[Gedetailleerde metingen](#gedetailleerde-metingen).

## Alle opties

| Optie                    | Beschrijving                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Enkel Markdown-bestand om te vertalen (alternatief voor `--source_dir`)                                      |
| `--source_dir`           | Bronmap met de Markdown-bestanden (standaard: `content/posts`)                                                 |
| `--target_dir`           | Uitvoermap voor de vertaalde bestanden (standaard: `traductions_en`)                                            |
| `--source_lang`          | Brontaal (standaard: `fr`)                                                                          |
| `--target_lang`          | Doeltaal (standaard: `en`)                                                                          |
| `--model`                | Specifiek te gebruiken model                                                                                  |
| `--eco`                  | Voordelige modellen gebruiken                                                                                 |
| `--use_mistral`          | Mistral AI API gebruiken                                                                                      |
| `--use_claude`           | Claude API gebruiken                                                                                          |
| `--use_gemini`           | Gemini API gebruiken                                                                                          |
| `--use_grok`             | xAI (Grok) API gebruiken — vereist `XAI_API_KEY`                                                             |
| `--use_codex`            | Codex CLI gebruiken op het quotum van het ChatGPT-abonnement                                                  |
| `--use_grok_cli`         | Grok CLI gebruiken op het quotum van het Grok-abonnement                                                      |
| `--use_antigravity`      | Antigravity CLI (`agy`) gebruiken op het quotum van het Google AI Pro- of Ultra-abonnement           |
| `--use_opencode`         | OpenCode (open source) gebruiken naar de provider geconfigureerd in OpenCode; vereist `--model provider/modèle`         |
| `--use_openrouter`       | OpenRouter gebruiken — vereist `OPENROUTER_API_KEY` en `--model fournisseur/modèle`                                               |
| `--force`                | Hervertaling forceren                                                                                         |
| `--keep_filename`        | Oorspronkelijke bestandsnaam behouden                                                                         |
| `--news`                 | Nieuwsmodus: beschermt EN-citaten, beheert vlaggen per taal                                                  |
| `--add_translation_note` | Vertaalnotitie toevoegen                                                                                      |
| `--note_position`        | Positie van de notitie: `top`, `bottom` (standaard), of `both`                         |
| `--note_format`          | Opmaak van de notitie: `legacy` (standaard, vette alinea) of `marker`                            |
| `--include_model`        | Naam van het model opnemen in het uitvoerbestand                                                              |
| `--reasoning_effort`     | Redeneerinspanning GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`  |

De negen vlaggen `--use_*` sluiten elkaar wederzijds uit: het combineren van twee vlaggen wordt
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
| Antigravity | `gemini-3.7-flash-medium`                             | `gemini-3.7-flash-low`    |
| OpenCode    | `--model provider/modèle` verplicht                   | idem — `--eco` zonder effect |
| OpenRouter  | `--model fournisseur/modèle` verplicht                | idem — `--eco` zonder effect |

### Via het ChatGPT-abonnement: `--use_codex`

Bestuurt de officiële Codex CLI: de vertaling wordt in mindering gebracht op het quotum van
het ChatGPT-abonnement, zonder API-sleutel of facturering naar verbruik.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Het binaire bestand wordt gezocht in `CODEX_BIN`, vervolgens het `PATH`, daarna het package
  `openai-codex-cli-bin`. `~/.codex/auth.json` wordt nooit gelezen.
- `OPENAI_API_KEY` en `CODEX_API_KEY` worden verwijderd uit de omgeving van het
  subproces: een aanwezige sleutel zorgt er nooit voor dat wordt overgeschakeld naar de API.
- Elk segment kost minstens één "bericht" uit het venster van 5 uur — twee
  als de validatie mislukt en het opnieuw wordt geprobeerd. OpenAI geeft ter
  schatting 250-2.000 berichten/5 uur aan voor `gpt-5.6-luna` (`--eco`) en
  10-100 voor `gpt-5.6-sol` bij een Plus-abonnement.
- `--model gpt-5.6-terra` en `--model gpt-5.6-luna` lopen ook via
  het abonnement. Een model waar het account geen recht op heeft, retourneert een 400 "model is
  not supported when using Codex with a ChatGPT account".
- Langzamer dan een API, en het verschil wordt groter naarmate het document groeit: op deze README
  mediaan 6 min 46 s per taal met `gpt-5.6-sol`, tegenover 36 s voor
  `gemini-3.7-flash`.
- Geweigerd in CI (`CI` of `GITHUB_ACTIONS` gedefinieerd): het abonnement verifieert
  via een persoonlijk sessiebestand, dat niet thuishoort op een gedeelde runner.
- Variabelen: `CODEX_BIN`, `CODEX_TIMEOUT` (seconden per segment, standaard 600).

### Via het Grok-abonnement: `--use_grok_cli`

Hetzelfde principe met de officiële Grok Build CLI, via het SuperGrok- of
X Premium+-abonnement.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Zwakkere isolatie dan Codex.** De OS-sandbox van Grok is niet van toepassing
  op veel recente Linux-systemen (AppArmor, container-runtime sockets), en een profiel dat niet kan
  worden toegepast start geruisloos zonder isolatie op. Het script vraagt daarom standaard geen profiel aan,
  meldt dit en leunt op de `--deny`-regels van de CLI, waaronder de catch-all `*` — de enige
  laag die weigert te starten in plaats van de beveiliging stilletjes in te trekken.
  `GROK_TRANSLATE_SANDBOX=read-only` vereist de OS-sandbox, en het opstarten
  mislukt als het systeem hier niet aan kan voldoen.
- Het quotum is wekelijks, gedeeld met Chat, Imagine en Voice, en er is geen
  opdracht om dit uit te lezen: een batch kan het conversationele gebruik
  onaangekondigd aanspreken.
- Variabelen: `GROK_BIN`, `GROK_HOME` (CLI-map, standaard `~/.grok`),
  `GROK_TIMEOUT` (standaard 900), `GROK_TRANSLATE_SANDBOX`.

### Via het Google-abonnement: `--use_antigravity`

Hetzelfde principe met `agy`, de officiële CLI van Antigravity: voor wie betaalt voor Google
AI Pro of Ultra, wordt de vertaling verrekend met het abonnementsquotum in plaats van
gefactureerd per token. Dit is de enige route naar dit quotum: Gemini CLI ondersteunt
deze accounts niet meer sinds 18 juni 2026
([aankondiging](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
en de SDK van Antigravity accepteert alleen een API-sleutel of een Google Cloud-project.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Geen enkele betaalde route blijft open.** agy ontvangt vanuit uw
  omgeving slechts een gesloten lijst van variabelen — `PATH`, taal en tijdzone,
  terminal, identiteit, proxy's en certificaten, sessiebus — en geen enkele sleutel:
  verschillende variabelen schakelen een aanroep over zonder iets weer te geven (gemeten:
  de ene stuurt het document naar een gateway van derden, een andere naar een gefactureerd
  Google Cloud-project), en een weigeringslijst liet er bij elke controle wel een paar liggen.
  Voorafgaand aan elk segment moet `agy -p /config`, wat geen quotum kost, aantonen
  dat betaalde AI-tegoeden zijn uitgeschakeld, zonder API-sleutel of Google Cloud-project — een
  ontbrekende instelling geldt als weigering —, anders wordt er niets vertaald; het logboek van elke
  aanroep moet vervolgens het abonnement bevestigen (`authMethod=consumer`), anders wordt het
  antwoord geweigerd.
- **Isolatie.** Elke aanroep draait in een tijdelijke, afgeschermde persoonlijke map,
  met een vertaalagent zonder tools: uw instellingen, regels,
  plug-ins, MCP-servers en hooks van agy komen er niet in, er wordt niets toegevoegd aan uw
  geschiedenis, en de login blijft in de sleutelhanger, die aipmt nooit leest.
  Een onvindbare agent zorgt ervoor dat agy geruisloos terugvalt op zijn codeeragent
  en diens tools: een volledige regel in het logboek moet de juiste agent bevestigen — een
  document dat dit bericht citeert vervangt deze regel niet —, anders volgt weigering.
- **Platformen**: Linux, binnen een sessie met een sleutelhanger (D-Bus-sessiebus,
  Secret Service); macOS wordt geaccepteerd, zonder daarop gemeten te zijn. Geweigerd
  onder Windows, waar agy de variabelen die elke aanroep isoleren niet leest, en
  onder Linux zonder sessiebus — SSH-sessie, container, server: agy slaat zijn token
  daar op in een bestand in `~/.gemini`, dat door de isolatie wordt verborgen. De
  weigering vindt plaats vóór het starten, met opgave van de reden, in plaats van een minuut
  te moeten wachten op een inlogcode.
- **Modellen**: die van `agy models`. De Gemini-modellen dragen de inspanning in hun naam
  (`gemini-3.7-flash-low`…): een naam zonder achtervoegsel wordt geweigerd vóór de aanroep, en
  `--reasoning_effort` heeft geen effect. De twee standaarden zijn vastgesteld door een
  testcampagne over veertien talen (zie [Gedetailleerde metingen](#gedetailleerde-metingen)).
  Claude en GPT-OSS hebben hun eigen quotum, dat veel kleiner is: ongeveer 1% van het
  venster van 5 uur per gemeten aanroep, vergeleken met 0,05% bij Flash.
- **Quotum**: per groep, een venster van 5 uur en een wekelijks venster, naar
  rato van de tokenkosten. Gemeten op het account van de auteur, op basis van een
  campagne van 32 vertalingen: ongeveer een half procentpunt van het venster van 5 uur
  voor een README van 40.000 tekens in `gemini-3.7-flash-medium`; de wekelijkse
  limiet hangt af van het abonnementsniveau. Herhaling volgt wat agy als
  herhaalbaar markeert; bij gebrek daaraan wordt een uitgeput venster nooit opnieuw geprobeerd: elk
  bestand mislukt dan tot de reset die door `/usage` wordt weergegeven.
- **Langzamer dan de API**: op het dichte artikel van de metingen doet Gemini 3.7 Flash
  er mediaan 3 min 14 s per taal over via het abonnement, vergeleken met 1 min 18 s via
  de API.
- **Onderbreking**: Ctrl-C, of een gesloten terminal, stopt agy direct samen met de
  opdracht in plaats van deze zijn beurt te laten afmaken op uw quotum; hetzelfde
  geldt voor Codex, Grok CLI en OpenCode. Onder `nohup` gaat het vertalen door.
- Geweigerd in CI (`CI` of `GITHUB_ACTIONS` gedefinieerd): de login bevindt zich in een
  persoonlijke sleutelhanger. Gebruik op een runner `--use_gemini` met `GOOGLE_API_KEY`.
- Variabelen: `AGY_BIN` (anders het `PATH`, daarna `~/.local/bin/agy`),
  `AGY_TIMEOUT` (seconden per segment, inclusief opstarten, standaard 900).

**Gebruiksvoorwaarden: uw account is uw eigen verantwoordelijkheid.** De
[voorwaarden van Antigravity](https://antigravity.google/terms) (sectie 6) en de
[FAQ](https://antigravity.google/docs/faq/) verbieden toegang tot de dienst
via software van derden met behulp van de Antigravity-login — Claude Code,
OpenClaw en OpenCode worden hierin genoemd —, op straffe van schorsing van het account. aipmt
leest noch hergebruikt het token: het start het officiële binaire bestand in de
[headless-modus](https://antigravity.google/docs/cli/headless/) die Google
documenteert voor scripts en CI. Een medewerker van Google noemde het "standaard"
om `agy -p` vanuit een lokaal script uit te voeren voor eigen werk
([officieel forum, 25 september 2026, niet-bindend antwoord](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
geen enkele richtlijn geeft uitsluitsel over een gedistribueerde tool als deze.

**Alleen openbare documenten.** Volgens sectie 5 van dezelfde voorwaarden kunnen de
interacties — prompts, antwoorden, metadata — worden gebruikt om de producten en
machine learning van Google te verbeteren en kunnen deze worden nagekeken door
mensen, ook bij een betaald abonnement. Afmelden verloopt via de instelling
`enableTelemetry`, met een ongedocumenteerd effect, die aipmt niet instelt; uw agy-instellingen
worden door de isolatie niet overgenomen. Verwerk hierin niets vertrouwelijks.

### Naar de gewenste provider: `--use_opencode`

[OpenCode](https://opencode.ai) is een open-source code-agent (MIT) die
routeert naar de daarin geconfigureerde providers: API-sleutel, abonnement,
OpenCode Zen-gateway (gratis modellen, zonder account) of lokaal model. Twee
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

`--model` is verplicht: zonder deze optie valt OpenCode terug op een gratis model
waarvan de interacties gebruikt kunnen worden voor training, en die keuze wordt niet voor
u gemaakt.

Isolatie bij elke aanroep:

- een inline-configuratie, met voorrang op die van uzelf, definieert een agent `aipmt`
  waarvan alle tools geweigerd zijn (`permission: { "*": "deny" }`), sessiedeling
  uitgeschakeld, `--pure`, nooit `--auto`;
- tijdelijke en lege werkmap, `OPENCODE_DISABLE_PROJECT_CONFIG` en
  `OPENCODE_DISABLE_CLAUDE_CODE` ingesteld — zonder deze injecteert OpenCode de `AGENTS.md`
  van de huidige map en `~/.claude/CLAUDE.md` in de prompt. Het globale
  `~/.config/opencode/AGENTS.md` blijft geïnjecteerd, OpenCode biedt geen mogelijkheid
  om dit uit te sluiten;
- uitvoercontract: exitcode 0, geen `error`-event, geen aanroep
  van tools, laatste stap in `stop`, niet-lege tekst, en de agent `aipmt`
  daadwerkelijk geladen — een onbekende `--agent` laat OpenCode niet falen, het
  valt geruisloos terug op de codeeragent;
- er wordt geen enkele sleutel uit `aipmt` doorgegeven, behalve `OPENCODE_API_KEY`, de sleutel
  van OpenCode zelf. Providers worden geconfigureerd in OpenCode, niet in
  het `.env` van `aipmt`.

Goed om te weten:

- De gratis modellen van Zen zijn veranderlijk, hebben ongedocumenteerde limieten en
  hun interacties kunnen gebruikt worden voor training: geschikt voor openbare documentatie,
  niet voor privé-inhoud.
- Een lokaal model moet ten minste 16k context-tokens bieden, aangezien segmenten
  tot 16.000 tekens bevatten. Ollama stelt vaak 4.096 in: gebruik
  een `Modelfile` met `PARAMETER num_ctx 32768`.
- `--eco` heeft geen effect; `--reasoning_effort` wordt ongewijzigd doorgegeven als
  `--variant` van OpenCode.
- OpenCode logt elke sessie in `~/.local/share/opencode/`.
- Variabelen: `OPENCODE_BIN` (anders het `PATH`, daarna `~/.opencode/bin/opencode`),
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

`reasoningEffort: "none"` schakelt het redeneren uit dat Ollama standaard activeert op deze
modellen, en wat een Modelfile niet kan uitschakelen. Gemeten op een zin van
zes woorden: 919 denk-tokens en 68 seconden zonder de optie, 9 tokens ermee.

### Naar meer dan 400 modellen: `--use_openrouter`

OpenRouter is een router die factureert op basis van verbruik, via één gezamenlijk tegoed,
vóór modellen die worden gehost door derden — waaronder de open Chinese modellen die
geen enkele andere provider hier aanbiedt.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` is verplicht. Een preflight, uitgevoerd vóór elke facturering, regelt
twee bijzonderheden van de routering:

- **Een en hetzelfde model wordt aangeboden door tientallen hosters met verschillende
  limieten** — op `z-ai/glm-5.3-flash` zijn er 23 hosters, waarvan één begrensd op
  2.048 output-tokens. De preflight leest `/api/v1/models/{modèle}/endpoints`,
  sluit hosters uit met minder dan 8.000 output-tokens of met een gedegradeerde status, en
  zet de overige vast met `allow_fallbacks: false`.
- **Het redeneren wordt gefactureerd tegen het output-tarief** — 107 tokens tegenover 2 bij
  een "OK"-antwoord van `z-ai/glm-5.2`. Dit staat standaard uitgeschakeld; modellen
  die dit vereisen, krijgen de laagst mogelijke inspanning die ze accepteren, aangezien de
  catalogusstandaard de uitvoer kan verzadigen vóór het einde van de vertaling.
  `--reasoning_effort` blijft prioritair.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Het contextvenster is afkomstig uit de catalogus. Een model met minder dan 16.400 tokens wordt
  voorafgaand aan elke aanroep geweigerd: 8.400 voor de prompt en het segment, minimaal
  8.000 voor de uitvoer.
- Een slug die ontbreekt in de catalogus, een onbereikbare catalogus of het ontbreken
  van een hoster die aan het plafond voldoet, stopt de opdracht.
- `finish_reason=length` met een lege uitvoer is een budget dat is verbruikt door
  het redeneren, geen afkapping: de melding maakt dit onderscheid.
- `--eco` heeft geen effect.
- Variabelen: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (standaard `https://openrouter.ai/api/v1`, `https://`
  vereist), `OPENROUTER_TIMEOUT` (standaard 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (standaard 30).

### Vertaalnotitie

`--add_translation_note` voegt een notitie toe, aan `bottom` (standaard), `top` (na de
front-matter) of `both` (`--note_position`), in het formaat `legacy` (vetgedrukte
paragraaf, standaard) of `marker` (`--note_format`). Het formaat `marker` is een
onzichtbare Markdown-referentiedefinitie,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
gevolgd door een vetgedrukt citaat: leesbaar op GitHub, bruikbaar tijdens de build door een
remark-plugin.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Gedetailleerde metingen

Alle metingen zijn vertalingen die daadwerkelijk zijn uitgevoerd met `aipmt`, naar
veertien talen: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Geschreven** telt de bestanden die door de beveiligingen zijn goedgekeurd; **Zonder
afwijking** die waarbij `scripts/compare_structure.py` niets opmerkt — hetzelfde aantal
secties, tussenkopjes, links, unieke URL's, codeblokken,
inline-code, tabelrijen, citaatblokken en vetgedrukte woorden.

"Zonder afwijking" betekent "niets gedetecteerd", niet "identiek": de vergelijker
telt elementen zonder de inhoud ervan te lezen. Hij meldt noch een verwijderde kop op
niveau 4, noch de tekst van een vervangen inline-code, noch een verwisselde vlag,
en beoordeelt de taal niet.

### Dicht monitoringartikel, modus `--news`

Een editie van de [AI-monitoring van jls42.org](https://jls42.org/fr/news):
589 regels, 140 links, 21 secties, 3 beschermde Engelse citaten. Campagne
van 4 en 5 september 2026.

| Model                                           | Toegang            | Geschreven | Zonder afwijking | Mediaan/taal   |
| ----------------------------------------------- | ------------------ | ---------- | ---------------- | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14      | ✅ **14/14**     | 1 min 18 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google-abonnement  | 14/14      | ✅ **14/14**     | 3 min 14 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT-abonnement | 14/14      | ✅ **14/14**     | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14      | ✅ **14/14**     | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14      | ✅ **14/14**     | 26 min 23 s    |
| `claude-sonnet-5`                               | Anthropic API      | 14/14      | ⚠️ 11/14         | 6 min 31 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14      | ❌ 11/14         | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14      | ❌ 8/14          | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | lokaal             | 10/14      | ❌ 7/14          | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral API        | 11/14      | ❌ 5/14          | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14       | ❌ 3/14          | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok-abonnement    | 1/14       | ❌ 1/14          | 23 min 11 s    |

Grok werd op 9 september opnieuw gemeten op een andere editie van hetzelfde monitoringoverzicht
(356 regels): 9 geschreven talen van de 14, 8 zonder afwijking. Dat is het cijfer
dat in de hoofdtabel staat. Drie onderbroken campagnes zijn niet
opgenomen: `qwen3.5-27b` (9 talen) en `kimi-k2.6` (4) wegens gebrek aan tegoed,
`z-ai/glm-5.3-flash` waarvan de twee fouten het gevolg waren van een redeneerinstelling
die de provider sindsdien heeft gecorrigeerd. De OpenRouter-regels zijn gemeten met
de standaardinstellingen van de router, vóór `--use_openrouter`; `z-ai/glm-5.2`,
opnieuw gemeten met de meegeleverde provider, behaalt dezelfde 14/14. De cijfers zijn
op 10 september herberekend met de huidige vergelijker: `qwen3.8-flash` en
`qwen3.7-flash` winnen elk één taal ten opzichte van de eerste
publicatie, de overige zijn ongewijzigd.

De regel `--use_antigravity` werd op 26 september gemeten op hetzelfde artikel,
vier vertalingen parallel. In het Engels verwijderde het model zelf de
drie Franse vertaalregels onder de citaten, zonder een vlag te verzinnen,
en de Engelse citaten zijn intact: de fallback-opschoning hoefde
niets te doen. In `--eco` (`gemini-3.7-flash-low`), op slechts vier talen
(en, ja, ar, hi): 4 van de 4 geschreven, allemaal zonder afwijking, 1 min 52 s als
mediaan.

### README van dit project, standaard Markdown

Vaste revisie op 9 september 2026: 785 regels, 285 inline code-elementen, 40
blokafsluitingen, 89 tabelregels. Vier vertalingen parallel.

| Model                                           | Geschreven | Zonder afwijking | Mediaan/taal   | Wat verschilt                                                                |
| ----------------------------------------------- | ---------- | ---------------- | -------------- | ---------------------------------------------------------------------------- |
| `gemini-3.7-flash`                              | 14/14      | ⚠️ 13/14         | 36 s           | één vetgedrukt woord (ja)                                                    |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14      | ⚠️ 13/14         | 1 min 22 s     | één vetgedrukt woord (ko)                                                    |
| `claude-sonnet-5`                               | 14/14      | ⚠️ 12/14         | 2 min 56 s     | één link (sv), één vetgedrukt woord (zh)                                     |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14      | ⚠️ 12/14         | 6 min 46 s     | één vetgedrukt woord (ar, ja)                                                |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14      | ⚠️ 11/14         | 2 min 34 s     | één vetgedrukt woord (hi, ja, ko)                                            |
| `qwen/qwen3.7-flash`                            | 14/14      | ⚠️ 10/14         | 2 min 17 s     | 40 inline code-elementen toegevoegd in het Arabisch; vetgedrukt (hi, ja, ko) |
| `mistral-large-latest`                          | 14/14      | ❌ 1/14          | 2 min 44 s     | één ontbrekende sectie (ar, hi, ko); codeblokken toegevoegd (ja, ko, ro, zh) |

Twee onderbroken campagnes zijn niet opgenomen: Grok, CLI-sessie verlopen
na twaalf talen (elf zonder afwijking), en `qwen3.8-flash`, HTTP 429 van zijn
host na twee. `opencode/mimo-v2.5-free` en `ollama/gpt-oss-20b-32k`
zijn niet opnieuw gemeten op deze revisie; op die van 4 en 5 september,
die 277 regels korter was, schreven ze elk 9 van de 14 vertalingen, waarvan 7
en 1 zonder afwijking.

De regel `--use_antigravity` is niet gemeten op de vastgelegde revisie, maar op
26 september op de revisie die met 1.14.0 werd gepubliceerd: 600 regels, 257 inline code-elementen,
30 blokafsluitingen, 85 tabelregels. Omdat deze 185 regels korter is, kan deze niet
één-op-één worden vergeleken met de andere regels.

### Vier README's van bekende projecten

FastAPI, Ollama, tldr-pages en Vue.js, overgenomen zoals ze zijn op GitHub —
eenvoudigere documenten dan de twee voorgaande. De campagne richtte zich op modellen
die moeite hadden; Gemini dient hierbij als vergelijkingspunt.

| Model                     | Bereik                     | Geschreven | Zonder afwijking |
| ------------------------- | -------------------------- | ---------- | ---------------- |
| `gemini-3.7-flash`        | 4 projecten × 14 talen     | 56/56      | ✅ **55/56**     |
| `opencode/mimo-v2.5-free` | 4 projecten × 14 talen     | 55/56      | ❌ 47/56         |
| `grok-4.6` (abonnement)   | 4 projecten × ar, hi, ja, zh | 16/16      | ❌ 14/16         |
| `ollama/gpt-oss-20b-32k`  | 4 projecten × ar, hi, ja, zh | 15/16      | ❌ 9/16          |

### Wat deze metingen niet zijn

- **Geen uitputtende ranglijst**: OpenRouter alleen al biedt meer dan vierhonderd
  modellen aan; ongeveer vijftien zijn gemeten.
- **Indicatieve tijdsduren**: drie tot zes parallelle vertalingen afhankelijk
  van de campagnes, en de doorvoersnelheid van een provider varieert gedurende de dag.
- **Gedateerde waarnemingen**: modellen veranderen onder dezelfde naam, en uw
  documenten zijn niet de onze.

Om de meting op uw eigen documenten te herhalen, op een vastgelegde kopie van het bestand:

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
opnieuw gegenereerd met `./regen_translations.sh --force` — Codex en `gpt-5.6-sol` standaard
via het ChatGPT-abonnement, vier parallel. `REGEN_PROVIDER` en
`REGEN_MODEL` wijzigen het pad: `antigravity` blijft op een abonnement, dat
van Google, en verloopt zonder uitzondering; een gefactureerde API (`openai`, `gemini`,
`grok`, `openrouter`) wordt geweigerd zonder `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` stelt een limiet per taak in (600 s, 1.800 s voor Codex en
Antigravity). De details van de tooling zijn te vinden in `CLAUDE.md`.

## Projecten die dit script gebruiken

- **[jls42.org](https://jls42.org)** — persoonlijke blog gepubliceerd in 15 talen. De
  [dagelijkse AI-monitoring](https://jls42.org/fr/news) ervan wordt elke dag
  vertaald met deze tool en dient als referentiedocument voor bovenstaande metingen.

## Auteur

Julien LE SAUX
E-mail: contact@jls42.org

## Licentie

GNU GENERAL PUBLIC LICENSE Versie 3. Zie [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Waarschuwing

Dit programma wordt gedistribueerd **zonder enige garantie**, onder de voorwaarden van
secties 15 en 16 van de GPL v3: geleverd 'zoals het is', zonder garantie van verkoopbaarheid
of geschiktheid voor een bepaald doel, en de auteur kan niet aansprakelijk worden
gesteld voor schade die voortvloeit uit het gebruik ervan. De tekst van de
licentie heeft voorrang op deze samenvatting.

- **Lees na vóór publicatie.** De beveiligingen dekken codeblokken, inline
  code, URL's, ankers en citaten in modus `--news` — niet de
  koppen, tabellen, frontmatter of de betekenis van uw zinnen.
- **Uw documenten worden verzonden naar de gekozen provider**, onder diens
  gebruiksvoorwaarden en gegevensbeleid. Sommige gratis modellen kunnen uw interacties
  hergebruiken voor training, en de voorwaarden van Antigravity staan Google toe deze
  te hergebruiken en door mensen te laten beoordelen, inclusief bij een betaald abonnement;
  een lokaal model is de enige manier waarbij er geen gegevens van uw machine worden verstuurd.
- **API-aanroepen worden aan u gefactureerd.** Dit programma stelt geen limiet
  aan de uitgaven: een lang document, een herhaling na een fout of een model dat
  veel redeneert, kost meer.
- **De gepubliceerde metingen zijn gedateerde waarnemingen**, geen garanties.

De vermelde product- en bedrijfsnamen zijn eigendom van hun respectieve
houders. Dit project is aan geen van hen gelieerd.

**Artikel vertaald van fr naar nl met gemini-3.7-flash-medium.**

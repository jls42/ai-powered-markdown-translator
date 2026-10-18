# AI-aangedreven Markdown-vertaler

🌍 [Frans](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [Engels](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Spaans](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Chinees](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Duits](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Japans](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Koreaans](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Arabisch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiaans](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Pools](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Portugees](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Roemeens](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Zweeds](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Codekwaliteit</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status van de kwaliteitscontrole"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Beveiligingsscore"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Betrouwbaarheidsscore"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Onderhoudbaarheidsscore"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Dekking"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Kwetsbaarheden"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Dubbele regels (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Technische schuld"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Aantal coderegels"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy-badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Vertaalt Markdown-bestanden van de ene taal naar de andere met behoud van de
structuur: codeblokken, inline code, URL's, ankers, tabellen en front
matter. Elf manieren om een model aan te roepen — vijf API's, vier abonnementen
zonder facturering op basis van gebruik en twee routers — plus een gepubliceerde
meting van wat elk model daadwerkelijk behoudt.

## In het kort

- **Elf providerpaden**: API's van OpenAI, Mistral, Claude, Gemini en Grok;
  abonnementen op ChatGPT (Codex), Grok, Google (Antigravity) en Claude (Claude
  Code) zonder facturering op basis van gebruik; routers OpenCode (open source, gratis of lokaal) en OpenRouter
  (meer dan 400 modellen).
- **Geen onjuiste uitvoer door een verloren token**: codeblokken, inline code,
  URL's, ankers en blokcitaten worden vóór de aanroep door tokens vervangen en
  bij terugkeer gecontroleerd. Als er één ontbreekt, wordt het bestand niet geschreven.
- **Lange documenten**: segmentatie op basis van het contextvenster van het model.
- **Modus `--news`**: Engelse citaten worden beschermd en vlaggen worden per
  taal beheerd, voor artikelen met nieuwsoverzichten.
- **Modus `--eco`**: snellere en goedkopere modellen.
- Optionele **vertaalnotitie**, bovenaan, onderaan of op beide plaatsen.

## Installatie

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 of recenter. Zie
[Bijdragen](#bijdragen) om vanuit de repository te installeren.

## Configuratie

De sleutels worden op drie plaatsen gelezen, van hoogste naar laagste
prioriteit; elke plaats vult alleen aan wat de vorige leeg heeft gelaten.

|     | Waar                                          | Waarvoor                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Omgevingsvariabelen                           | CI, containers, eenmalige uitzondering |
| 2   | `.env` van de huidige map (of een bovenliggende map) | een projectspecifieke sleutel         |
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
gebruikersbestand volgt `XDG_CONFIG_HOME` (alleen een absoluut pad) en `%APPDATA%`
onder Windows. Zonder sleutel somt de opdracht de drie locaties op.

**De `.env` van een project kan aanroepen niet omleiden en evenmin het
uitgevoerde programma kiezen.** Het levert sleutels, nooit een bestemming of
binair bestand: alle variabelen in `_BASE_URL`, `_API_BASE`, `_ENDPOINT`
of `_BIN` (`CODEX_BIN`, `GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`),
`GROK_HOME`, de proxies (`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`), de
certificaatarchieven (`SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`,
`CURL_CA_BUNDLE`) en `XDG_CONFIG_HOME` / `APPDATA` worden daarin genegeerd, met
een waarschuwing. Een gekloonde repository mag uw sleutel niet kunnen omleiden
of u bij de eerste vertaling zijn eigen programma laten uitvoeren. Dit bestand
wordt ook zonder interpolatie gelezen: `NOM=${OPENAI_API_KEY}` kopieert de sleutel er
niet naartoe. Stel deze variabelen in de omgeving of in `~/.config/aipmt/.env` in.

Optionele variabelen: `XAI_BASE_URL` (standaard `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (seconden per aanroep, standaard 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(standaard 600), `GROK_BIN`, `GROK_HOME` (standaard `~/.grok`), `GROK_TIMEOUT`
(standaard 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (standaard 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (standaard 600), `OPENROUTER_BASE_URL`
(`https://` vereist), `OPENROUTER_TIMEOUT` (standaard 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (standaard 30). Elk daarvan wordt toegelicht in de
sectie van de betreffende provider.

## Aan de slag

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` vertaalt naar het Spaans en levert `document-es.md` op in
`--target_dir`; met `--include_model`, `document-es-gpt-5.6-terra.md`. De extensie wordt
altijd `.md` — `article.mdx` levert `article-en.md` op — behalve met
`--keep_filename`, dat de oorspronkelijke naam behoudt. Een reeds aanwezige
vertaling wordt zonder `--force` overgeslagen.

Exitcodes: `0` als alles is voltooid of overgeslagen, `1`
als er nog een mislukt bestand is (lijst op de foutuitvoer), `2` als
de configuratie het probleem veroorzaakt. Een mislukt bestand wordt nooit
geschreven, zelfs niet als het schrijven zelf mislukt: de inhoud wordt ernaast
geschreven en vervolgens hernoemd. Opnieuw uitvoeren volstaat.

## Welk model kiezen

Gemeten op twee echte documenten, die door elk model naar dezelfde veertien
talen zijn vertaald. **Het getal is het aantal talen, van de veertien, waarvoor
de vertaling wordt geschreven en niets van de bron afwijkt.**

| Model                 | Toegangsmethode                    | Dicht nieuwsoverzicht | Deze README  | Wat afwijkt en in hoeveel talen                                                                                                                                     |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google-abonnement (Antigravity)   | ✅ 14/14                | ✅ 14/14     | niets, in geen van beide documenten                                                                                                                                |
| **Claude Sonnet 5.5** | Anthropic-API-sleutel             | ✅ 14/14                | ✅ 14/14     | niets, in geen van beide documenten                                                                                                                                |
| **Gemini 3.7 Flash**  | Google-API-sleutel                | ✅ 14/14                | ⚠️ 13/14     | 1 taal van de 14: één extra vetgedrukt woord (ja)                                                                                                                  |
| **Gemini 3.7 Flash**  | Google-abonnement (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 1 taal van de 14: één vetgedrukt woord minder (ko)                                                                                                                 |
| **GPT-5.6 Sol**       | ChatGPT-abonnement of OpenAI-sleutel | ✅ 14/14             | ⚠️ 12/14     | 2 talen van de 14: één vetgedrukt woord minder (ar, ja)                                                                                                            |
| **GLM-5.2**           | OpenRouter-sleutel                | ✅ 14/14                | ⚠️ 11/14     | 3 talen van de 14: één vetgedrukt woord minder (hi, ja, ko)                                                                                                        |
| Claude Sonnet 5       | Claude-abonnement (Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 1 taal van de 14 in het artikel: één extra vetgedrukt woord (zh); 1 in deze README: een tabelregel vastgeplakt aan de vorige, verborgen bij weergave (ar)          |
| Claude Haiku 4.5      | Claude-abonnement (Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 3 talen in het artikel: een sectiekop gewijzigd naar niveau 1 (en, pl, ro); in deze README niets voor de vergelijker, maar de interne links zijn in het Engels verdubbeld |
| Claude Sonnet 5       | Anthropic-API-sleutel             | ⚠️ 11/14                | ⚠️ 12/14     | 3 talen in het artikel: een codeblok is verschenen (es, de, hi); 2 in deze README: een link zonder zijn opmaak (sv), een vetgedrukt woord (zh)                     |
| Claude Haiku 4.5      | Anthropic-API-sleutel             | ⚠️ 7/14                 | ✅ 14/14     | 7 talen in het artikel: een sectiekop gewijzigd naar niveau 1 — in het Japans bleef die in het Frans; niets in deze README                                         |
| Claude Haiku 5.5      | Anthropic-API-sleutel             | ⚠️ 11/14                | ❌ 12/14     | 3 talen in het artikel: een sectiekop kreeg een ander niveau of werd verdubbeld (ja, ko, zh); in deze README werden 2 talen geweigerd en ging inline code verloren (ar, hi) |
| Qwen 3.7 Flash        | OpenRouter-sleutel                | ❌ 8/14                 | ⚠️ 10/14     | 1 taal geweigerd in het artikel, 5 andere wijken af; in deze README zijn ongeveer veertig woorden in `code` geplaatst (ar)                                 |
| Grok 4.6              | Grok-abonnement                   | ❌ 8/14                 | niet beoordeeld | 5 talen van de 14 geweigerd doordat inline code en URL's niet werden teruggegeven; het Nederlands wijkt overal af                                               |
| GPT-OSS 20B           | lokaal model (Ollama)             | ❌ 7/14                 | niet opnieuw gemeten | 4 talen van de 14 geweigerd: het model liet daarin Franse passages staan en de controle hield ze tegen                                                    |
| MiMo v2.5 (gratis)    | OpenCode Zen, zonder account      | ❌ 11/14                | niet opnieuw gemeten | 1 taal geweigerd; een sectie ontbreekt in het Pools                                                                                                       |
| Mistral Large         | Mistral-API-sleutel               | ❌ 5/14                 | ❌ 1/14      | **een volledige sectie verdwijnt**: 1 taal in het artikel (hi), 3 in deze README (ar, hi, ko) — en 3 talen geweigerd in het artikel                              |
| DeepSeek V4 Flash     | OpenRouter-sleutel                | ❌ 3/14                 | niet opnieuw gemeten | 10 talen van de 14 geweigerd; 37 minuten per taal                                                                                                         |
| Claude Opus 5.5       | Claude-abonnement (Claude Code)   | ❌ 0/14                 | ✅ 14/14     | het artikel werd in alle 14 talen geweigerd door de beveiligingsmaatregelen van Opus vanwege een kort biologiebericht; niets in deze README                      |

|     | Betekenis van het symbool                                                                                                                                                                              |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ✅  | alle veertien talen vertaald en niets wijkt af van de bron                                                                                                                                             |
| ⚠️  | alle veertien talen vertaald; wat afwijkt is **opmaak** — een vetgedrukt woord, een `code`, een link die zijn vierkante haken verliest. Er ontbreekt geen tekst, URL, codeblok of sectie              |
| ❌  | ten minste één taal kon niet worden vertaald — het bestand wordt geweigerd en niet geschreven — **of** er ontbreekt inhoud in een geschreven bestand                                                    |

Dit zijn de belangrijkste conclusies:

- **Een geweigerde vertaling is geen beschadigde vertaling.** Wanneer bij
  terugkeer een token ontbreekt, wordt het bestand niet geschreven en telt de
  taal als geweigerd. Dat gebeurt bij Grok met het artikel: vier inline codes
  en drie URL's gaan al in het eerste segment verloren, bij de vijf niet-Latijnse
  schriften.
- **Een model kan een volledig document vanwege één enkele zin weigeren.**
  Opus 5.5 vertaalt deze README zonder enige afwijking, maar geen enkel
  nieuwsoverzicht: zijn beveiligingsmaatregelen stoppen de reactie bij een kort
  biologiebericht. Het bestand wordt niet geschreven en aipmt vermeldt waarom.
- **Dit vangnet dekt koppen, tabellen, front matter en tekst niet.** Een model
  dat een sectie verwijdert, levert een bestand op dat het hulpmiddel zonder
  protest schrijft — zoals bij Mistral. Deze elementen kunnen niet door een
  token worden vervangen en de huidige controles verifiëren ze niet;
  `scripts/compare_structure.py` detecteert een ontbrekende sectie, maar pas achteraf.
- **Grok heeft geen score voor deze README**: zijn CLI-sessie verliep na twaalf
  talen, waarvan elf zonder afwijking. Een onderbroken meetcampagne krijgt geen
  score.
- **De dichtheid van het document is belangrijker dan de taal.** Grok houdt
  stand bij gewone README's en haakt af bij een artikel vol links, ook in het
  Nederlands.

Datums en documenten: de kolom ‘Deze README’ is op 9 september 2026 gemeten op
een vastgezette revisie van dit bestand (785 regels, 285 inline codes, 89
tabelregels), die sindsdien is bijgewerkt — met uitzondering van de regels voor
Antigravity en Claude Code, die op 26 september zijn gemeten op de kortere
revisie die met versie 1.14.0 is gepubliceerd (600 regels, 257 inline codes, 85
tabelregels), en de regels voor Claude Sonnet 5.5, Haiku 5.5 en Haiku 4.5 via de
API, die op 18 oktober op dezelfde revisie zijn gemeten. De kolom ‘Dicht
nieuwsoverzicht’ komt uit de meetcampagne van 4 en 5 september op een artikel
van 589 regels, met uitzondering van de regel voor Grok, die op 9 september
opnieuw is gemeten op een andere editie van hetzelfde nieuwsoverzicht, de
regels voor Antigravity en Claude Code, die op 26 september op hetzelfde
artikel zijn gemeten, en deze drie regels voor Claude, op 18 oktober. De
volledige tabellen, de tijdsduren en het protocol staan in
[Gedetailleerde metingen](#gedetailleerde-metingen).
## Alle opties

| Optie                    | Beschrijving                                                                                                   |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| `--file`           | Eén Markdown-bestand om te vertalen (alternatief voor `--source_dir`)                                          |
| `--source_dir`           | Bronmap met Markdown-bestanden (standaard: `content/posts`)                                                     |
| `--target_dir`           | Uitvoermap voor vertaalde bestanden (standaard: `traductions_en`)                                                |
| `--source_lang`           | Brontaal (standaard: `fr`)                                                                           |
| `--target_lang`           | Doeltaal (standaard: `en`)                                                                           |
| `--model`           | Specifiek te gebruiken model                                                                                   |
| `--eco`           | Voordelige modellen gebruiken                                                                                  |
| `--use_mistral`           | De Mistral AI-API gebruiken                                                                                    |
| `--use_claude`           | De Claude-API gebruiken                                                                                        |
| `--use_gemini`           | De Gemini-API gebruiken                                                                                        |
| `--use_grok`           | De xAI-API (Grok) gebruiken — vereist `XAI_API_KEY`                                                           |
| `--use_codex`           | De Codex CLI gebruiken binnen het quotum van het ChatGPT-abonnement                                            |
| `--use_grok_cli`           | De Grok CLI gebruiken binnen het quotum van het Grok-abonnement                                                |
| `--use_antigravity`           | De Antigravity CLI (`agy`) gebruiken binnen het quotum van het Google AI Pro- of Ultra-abonnement     |
| `--use_claude_code`           | De Claude Code CLI (`claude -p`) gebruiken binnen het quotum van het Claude Pro- of Max-abonnement          |
| `--use_opencode`           | OpenCode (open source) gebruiken met de in OpenCode geconfigureerde provider; vereist `--model provider/modèle`           |
| `--use_openrouter`           | OpenRouter gebruiken — vereist `OPENROUTER_API_KEY` en `--model fournisseur/modèle`                                                |
| `--force`           | Opnieuw vertalen afdwingen                                                                                     |
| `--keep_filename`           | De oorspronkelijke bestandsnaam behouden                                                                       |
| `--news`           | Nieuwsmodus: beschermt Engelse citaten en verwerkt vlaggen per taal                                            |
| `--add_translation_note`           | Een vertaalnotitie toevoegen                                                                                   |
| `--note_position`           | Positie van de notitie: `top`, `bottom` (standaard) of `both`                           |
| `--note_format`           | Indeling van de notitie: `legacy` (standaard, vetgedrukte alinea) of `marker`                    |
| `--include_model`          | De modelnaam opnemen in het uitvoerbestand                                                                     |
| `--reasoning_effort`          | Redeneerinspanning van GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

De negen `--use_*`-flags sluiten elkaar wederzijds uit: een combinatie van
twee wordt geweigerd.

## Providers

### Via API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` schakelt over naar het voordelige niveau van elke provider.

| Provider    | Kwaliteit (standaard)                                | Voordelig (`--eco`)            |
| ----------- | ----------------------------------------------------- | --------------------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`                         |
| Claude      | `claude-sonnet-5-5`                                       | `claude-haiku-5-5`                         |
| Mistral     | `mistral-large-latest`                                       | `mistral-small-latest`                         |
| Gemini      | `gemini-3.7-flash`                                       | `gemini-3.1-flash-lite`                         |
| Codex       | `gpt-5.6-sol` (ook `terra` en `luna` via `--model`) | `gpt-5.6-luna` |
| Grok API    | `grok-4.6`                                       | `grok-4.3`                         |
| Grok CLI    | `grok-4.6`                                       | `grok-4.5`                         |
| Antigravity | `gemini-3.8-flash-medium`                                       | `gemini-3.7-flash-low`                         |
| Claude Code | `sonnet`, inspanning `low`           | hetzelfde — `--eco` zonder effect |
| OpenCode    | `--model provider/modèle` verplicht                             | hetzelfde — `--eco` zonder effect |
| OpenRouter  | `--model fournisseur/modèle` verplicht                             | hetzelfde — `--eco` zonder effect |

### Via het ChatGPT-abonnement: `--use_codex`

Stuurt de officiële Codex CLI aan: de vertaling wordt afgetrokken van het quotum
van het ChatGPT-abonnement, zonder API-sleutel of facturering naar gebruik.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Het binaire bestand wordt gezocht in `CODEX_BIN`, vervolgens in `PATH` en daarna in het package
  `openai-codex-cli-bin`. `~/.codex/auth.json` wordt nooit gelezen.
- `OPENAI_API_KEY` en `CODEX_API_KEY` worden verwijderd uit de omgeving van het
  subprocess: een aanwezige sleutel veroorzaakt nooit een overschakeling naar de API.
- Elk segment kost ten minste één ‘bericht’ uit het venster van 5 uur — twee
  als de validatie mislukt en het opnieuw wordt geprobeerd. OpenAI vermeldt ter
  indicatie 250-2.000 berichten per 5 uur voor `gpt-5.6-luna` (`--eco`) en
  10-100 voor `gpt-5.6-sol` met een Plus-abonnement.
- `--model gpt-5.6-terra` en `--model gpt-5.6-luna` verlopen eveneens via
  het abonnement. Een model waartoe het account geen toegang heeft, levert een 400-foutmelding op: ‘model is
  not supported when using Codex with a ChatGPT account’.
- Langzamer dan een API, waarbij het verschil toeneemt met de documentgrootte: voor deze README
  mediaan 6 min 46 s per taal met `gpt-5.6-sol`, tegenover 36 s met
  `gemini-3.7-flash`.
- Geweigerd in CI (als `CI` of `GITHUB_ACTIONS` is ingesteld): het abonnement verifieert
  zich via een persoonlijk sessiebestand, dat niet thuishoort op een gedeelde
  runner.
- Variabelen: `CODEX_BIN`, `CODEX_TIMEOUT` (seconden per segment, standaard 600).

### Via het Grok-abonnement: `--use_grok_cli`

Hetzelfde principe met de officiële Grok Build CLI, via het SuperGrok- of
X Premium+-abonnement.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Minder sterke isolatie dan Codex.** De OS-sandbox van Grok werkt
  niet op veel recente Linux-systemen (AppArmor, sockets van de container-runtime),
  en een profiel dat niet kan worden toegepast, start stilzwijgend zonder
  isolatie. Het script vraagt daarom standaard geen profiel aan, meldt dit en
  steunt op de `--deny`-regels van de CLI, waaronder de catch-all `*` — de enige
  laag die weigert te starten in plaats van de bescherming zonder melding
  weg te nemen. `GROK_TRANSLATE_SANDBOX=read-only` vereist de OS-sandbox, waarna het opstarten
  mislukt als het systeem hieraan niet kan voldoen.
- Het quotum is wekelijks, wordt gedeeld met Chat, Imagine en Voice, en kan met
  geen enkele opdracht worden uitgelezen: een batch kan zonder waarschuwing
  het gebruik voor gesprekken verminderen.
- Variabelen: `GROK_BIN`, `GROK_HOME` (CLI-map, standaard `~/.grok`),
  `GROK_TIMEOUT` (standaard 900), `GROK_TRANSLATE_SANDBOX`.

### Via het Google-abonnement: `--use_antigravity`

Hetzelfde principe met `agy`, de officiële CLI van Antigravity: voor wie Google
AI Pro of Ultra betaalt, wordt de vertaling afgetrokken van het abonnementsquotum in plaats
van per token te worden gefactureerd. Dit is de enige route naar dat quotum: Gemini CLI
bedient deze accounts sinds 18 juni 2026 niet meer
([aankondiging](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
en de Antigravity SDK accepteert alleen een API-sleutel of een Google Cloud-project.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Er blijft geen betaalde route open.** agy ontvangt uit uw
  omgeving uitsluitend een vaste lijst met variabelen — `PATH`, taal en tijdzone,
  terminal, identiteit, proxy's en certificaten, sessiebus — en geen enkele sleutel:
  diverse variabelen ervan laten een aanroep zonder enige melding overschakelen (gemeten:
  de ene stuurt het document naar een gateway van derden, een andere naar een
  gefactureerd Google Cloud-project), en bij elke controle bleek een blokkeerlijst
  er weer enkele te missen. Vóór elk segment moet `agy -p /config`, dat geen quotum
  kost, aantonen dat betaalde AI-tegoeden zijn uitgeschakeld, zonder API-sleutel
  of Google Cloud-project — een ontbrekende instelling geldt als weigering —;
  anders wordt niets vertaald. Het logboek van elke aanroep moet vervolgens het
  abonnement bevestigen (`authMethod=consumer`), anders wordt het antwoord geweigerd.
- **Isolatie.** Elke aanroep draait in een eigen tijdelijke persoonlijke map,
  met een vertaalagent zonder tools: uw instellingen, regels, plugins,
  MCP-servers en hooks van agy komen daar niet terecht, er wordt niets aan uw
  geschiedenis toegevoegd en de aanmelding blijft in de sleutelbos, die aipmt nooit leest.
  Als een agent niet wordt gevonden, valt agy stilzwijgend terug op zijn coding agent
  en de bijbehorende tools: een volledige regel in het logboek moet de juiste agent bevestigen — een
  document dat dit bericht citeert, geldt niet als vervanging —, anders volgt een weigering.
- **Platformen**: Linux, binnen een sessie met een sleutelbos (D-Bus-sessiebus,
  Secret Service); macOS wordt geaccepteerd, maar is niet gemeten. Geweigerd
  onder Windows, waar agy de variabelen die elke aanroep isoleren niet leest, en
  onder Linux zonder sessiebus — SSH-sessie, container, server: agy slaat zijn
  token daar op in een bestand in `~/.gemini`, dat door de isolatie wordt verborgen. De
  weigering vindt vóór het starten plaats en vermeldt de oorzaak, in plaats van
  een minuut te wachten op een aanmeldcode.
- **Modellen**: die van `agy models`. Bij Gemini staat de inspanning in de naam
  (`gemini-3.8-flash-medium`…): een naam zonder achtervoegsel wordt vóór de aanroep geweigerd,
  en `--reasoning_effort` heeft geen effect. Standaard `gemini-3.8-flash-medium`,
  en `gemini-3.7-flash-low` met `--eco`; de campagnes waarin deze zijn vastgelegd,
  worden beschreven in [Gedetailleerde metingen](#gedetailleerde-metingen). Claude en GPT-OSS
  hebben hun eigen, veel kleinere quotum: ongeveer 1% van het venster van
  5 uur per gemeten aanroep, tegenover 0,05% in Flash.
- **Quotum**: per groep een venster van 5 uur en een wekelijks venster, naar
  rato van de tokenkosten. Gemeten met het account van de auteur: ongeveer
  16 punten van het venster van 5 uur per miljoen brontekens met
  `gemini-3.8-flash-medium`, 14 met `gemini-3.7-flash-medium` en 7 tot 8 bij
  lage inspanning — een README van 40.000 tekens kost dus iets meer dan een
  half punt. De wekelijkse limiet hangt af van het niveau. Nieuwe pogingen volgen
  wat agy als opnieuw uitvoerbaar aanmerkt; bij gebrek daaraan wordt bij een uitgeput
  venster nooit opnieuw geprobeerd: elk bestand mislukt totdat de door
  `/usage` getoonde reset plaatsvindt.
- **Langzamer dan de API**: voor het inhoudelijk complexe artikel over de metingen,
  mediaan 3 min 59 s per taal met `gemini-3.8-flash-medium` en 3 min 14 s met
  `gemini-3.7-flash-medium`, tegenover 1 min 18 s voor Gemini 3.7 Flash via de API.
- **Onderbreking**: Ctrl-C of een gesloten terminal stopt agy samen met de
  opdracht, in plaats van het zijn beurt ten koste van uw quotum te laten voltooien; hetzelfde
  geldt voor Codex, Grok CLI en OpenCode. Onder `nohup` gaat de vertaling door.
- Geweigerd in CI (als `CI` of `GITHUB_ACTIONS` is ingesteld): de aanmelding bevindt zich in een
  persoonlijke sleutelbos. Gebruik op een runner `--use_gemini` met `GOOGLE_API_KEY`.
- Variabelen: `AGY_BIN` (anders `PATH`, gevolgd door `~/.local/bin/agy`),
  `AGY_TIMEOUT` (seconden per segment, inclusief opstarten, standaard 900).

**Gebruiksvoorwaarden: uw account staat op het spel.** De
[voorwaarden van Antigravity](https://antigravity.google/terms) (sectie 6) en de
[FAQ](https://antigravity.google/docs/faq/) verbieden toegang tot de dienst
via software van derden met behulp van de Antigravity-aanmelding — Claude Code,
OpenClaw en OpenCode worden daarbij genoemd — op straffe van opschorting van het account. aipmt
leest of hergebruikt de token niet: het start het officiële binaire bestand in de
[headless-modus](https://antigravity.google/docs/cli/headless/), die Google
documenteert voor scripts en CI. Een medewerker van Google noemde het ‘standaard’
om `agy -p` vanuit een lokaal script voor eigen werk te starten
([officieel forum, 25 september 2026, niet-bindend antwoord](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
geen enkele tekst geeft uitsluitsel over het geval van een gedistribueerde tool zoals deze.

**Alleen openbare documenten.** Volgens sectie 5 van dezelfde voorwaarden kunnen
de uitwisselingen — prompts, antwoorden, metadata — worden gebruikt om de
producten en machine learning van Google te verbeteren en door mensen worden
beoordeeld, ook met een betaald abonnement. Afmelden verloopt via de instelling
`enableTelemetry`, waarvan het effect niet is gedocumenteerd en die aipmt niet instelt; uw
agy-instellingen worden niet meegenomen in de geïsoleerde omgeving. Verwerk hiermee niets vertrouwelijks.
### Over het Claude-abonnement: `--use_claude_code`

Hetzelfde principe geldt voor `claude`, de officiële CLI van Claude Code, in de modus `-p`: voor
wie voor Claude Pro of Max betaalt, wordt de vertaling afgetrokken van het quotum van
het abonnement in plaats van per token te worden gefactureerd. Niet te verwarren met
`--use_claude`, de API van Anthropic, die op basis van gebruik wordt gefactureerd.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Geen enkele betaalde route blijft open en elke aanroep bewijst dat.** Claude
  Code ontvangt uit uw omgeving slechts een gesloten lijst met variabelen — geen
  API-sleutel, token, cloudprovider of markering van de Claude Code-sessie
  waaruit aipmt zou worden gestart. Vóór het eerste segment moet `claude auth status`
  de abonnementsverbinding tonen, zonder Console-sleutel, en moet `/usage`, dat
  geen quotum kost, dit bevestigen; elke aanroep bevestigt dit op zijn beurt in
  zijn initialisatiegebeurtenis, anders wordt het antwoord geweigerd.
- **Schakel „extra usage” uit** (claude.ai, Instellingen → Gebruik) zodat
  nul euro ook echt nul blijft: wanneer dit is ingeschakeld, neemt het de verwerking over zodra
  een venster is opgebruikt en worden kosten in rekening gebracht zonder een foutmelding weer te geven. aipmt stopt de vertaling zodra het quotumoverzicht
  van een aanroep dit meldt, maar die aanroep is dan al meegerekend.
- **Quotum gedeeld met uw Claude Code-sessies.** Elke aanroep meldt
  het gebruik van de vensters van 5 uur en van de week; boven 80%
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) wordt geen extra segment gestart, om
  niet op te gebruiken wat u voor uw werk nodig hebt.
- **Isolatie.** Elke aanroep draait zonder tools, in een persoonlijke,
  tijdelijke map, in een modus zonder personalisatie: noch uw `CLAUDE.md`, noch uw plugins,
  hooks, MCP-servers of instellingen worden geladen, en er wordt niets van de
  sessie bewaard. Bijlagen zijn uitgeschakeld: een `@chemin` in uw document
  blijft tekst en opent geen enkel bestand (gemeten).
- **Modellen**: standaard `sonnet`, met inspanning `low`, en ook in `--eco`:
  `--eco` verandert niets via deze route. Gemeten op dezelfde documenten is `haiku`
  twee keer zo langzaam — het redeneert zonder dat dit kan worden verhinderd — tegen
  nauwelijks lagere kosten, en `opus` weigert biologische inhoud (zie het
  volgende punt). Beide blijven toegankelijk via `--model`; deze aliassen volgen het
  nieuwste model van hun familie. `fable` en de varianten `[1m]` worden geweigerd,
  omdat ze betaalde tegoeden gebruiken. `--reasoning_effort` stelt de inspanning in,
  waar een vertaling niets aan heeft: de gemeten redenering is nul of vrijwel nul.
- **Opus weigert bepaalde biologische inhoud.** De beveiligingen ervan zijn
  strenger dan die van Sonnet, en de foutmelding van Anthropic waarschuwt dat ze
  „soms werk kunnen markeren dat aan biologisch onderzoek grenst”. Gemeten: een kort
  monitoringbericht over 279 gegenereerde moleculen leidde ertoe dat het artikel in alle veertien
  talen werd geweigerd. Er wordt niets geschreven: aipmt weigert het afgebroken antwoord, noemt de
  beveiligingen en adviseert `--model sonnet`.
- Geweigerd in CI (als `CI` of `GITHUB_ACTIONS` is ingesteld) en onder Windows (niet gemeten).
- Variabelen: `AIPMT_CLAUDE_BIN` (anders de `PATH`, daarna `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (seconden per segment, standaard 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (standaard 0.8), `CLAUDE_CONFIG_DIR` (het account van
  Claude Code, nooit overgenomen uit een `.env` van een project); werkmappen onder
  `XDG_CACHE_HOME/aipmt/claude-code` (standaard `~/.cache`).

**Gebruiksvoorwaarden: uw account wordt hiervoor gebruikt.** De
[juridische pagina van Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
verhindert niet dat „een eindgebruiker zich met zijn eigen Claude-abonnement
aanmeldt bij het ongewijzigde binaire bestand van Claude Code”: dat is wat aipmt doet; het start het
officiële binaire bestand en leest het token nooit. Anthropic „staat externe
ontwikkelaars echter niet toe […] om namens hun gebruikers verzoeken via
inloggegevens van een Free-, Pro- of Max-abonnement te routeren”, geeft voor tools
van derden, „waaronder open-sourceprojecten”, de voorkeur aan de API-sleutel en behoudt zich het recht voor om het
gebruik ervan af te trekken van betaalde tegoeden
([Claude-help](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Geen enkele tekst geeft uitsluitsel over het geval van een gedistribueerde tool die het binaire bestand start.

**Gegevens**: voor Free-, Pro- en Max-accounts geldt modeltraining
ook voor Claude Code wanneer de privacyinstelling dit toestaat
([gegevenspagina](https://code.claude.com/docs/en/data-usage)). aipmt bewaart
lokaal geen transcripties (`--no-session-persistence`). Verwerk er
niets vertrouwelijks mee.

### Naar de provider van uw keuze: `--use_opencode`

[OpenCode](https://opencode.ai) is een open-source code-agent (MIT) die
routeert naar de providers die erin zijn geconfigureerd: API-sleutel, abonnement,
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

`--model` is verplicht: zonder deze variabele zou OpenCode terugvallen op een gratis model
waarvan de uitwisselingen voor training kunnen worden gebruikt, en die keuze wordt niet
voor u gemaakt.

Isolatie bij elke aanroep:

- een inline configuratie, die voorrang heeft op die van u, definieert een agent `aipmt`
  waarvoor alle tools worden geweigerd (`permission: { "*": "deny" }`), het delen van
  sessies is uitgeschakeld, `--pure`, nooit `--auto`;
- tijdelijke en lege werkmap, met `OPENCODE_DISABLE_PROJECT_CONFIG` en
  `OPENCODE_DISABLE_CLAUDE_CODE` ingesteld — zonder deze variabelen injecteert OpenCode
  de `AGENTS.md` van de huidige map en `~/.claude/CLAUDE.md` in de
  prompt. De globale `~/.config/opencode/AGENTS.md` blijft geïnjecteerd; OpenCode maakt het niet
  mogelijk deze uit te sluiten;
- uitvoercontract: exitcode 0, geen enkele gebeurtenis `error`, geen
  toolaanroep, laatste stap in `stop`, niet-lege tekst en de agent `aipmt`
  daadwerkelijk geladen — een onbekende `--agent` laat OpenCode niet mislukken; het
  valt stilzwijgend terug op de codeeragent;
- er wordt geen sleutel voor `aipmt` doorgegeven, behalve `OPENCODE_API_KEY`, de eigen
  sleutel van OpenCode. Providers worden in OpenCode geconfigureerd, niet in
  de `.env` van `aipmt`.

Goed om te weten:

- De gratis Zen-modellen veranderen geregeld, hebben niet-gedocumenteerde limieten en
  hun uitwisselingen kunnen voor training worden gebruikt: geschikt voor openbare
  documentatie, niet voor privé-inhoud.
- Een lokaal model moet minstens 16k contexttokens bieden, aangezien de segmenten
  maximaal 16.000 tekens lang zijn. Ollama configureert er vaak 4.096: gebruik
  een `Modelfile` met `PARAMETER num_ctx 32768`.
- `--eco` heeft geen effect; `--reasoning_effort` wordt ongewijzigd doorgegeven als
  `--variant` van OpenCode.
- OpenCode registreert elke sessie in `~/.local/share/opencode/`.
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

`reasoningEffort: "none"` schakelt het nadenken uit dat Ollama standaard voor deze
modellen activeert en dat niet via een Modelfile kan worden uitgeschakeld. Gemeten op een zin van
zes woorden: 919 redeneertokens en 68 seconden zonder de optie, 9 tokens met de optie.

### Naar meer dan 400 modellen: `--use_openrouter`

OpenRouter is een router die op basis van gebruik wordt gefactureerd, vanuit één tegoed, voor
modellen die door derden worden gehost — waaronder de open Chinese modellen die geen enkele
andere provider hier aanbiedt.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` is verplicht. Een preflight, uitgevoerd voordat er kosten in rekening worden gebracht, regelt
twee bijzonderheden van de routering:

- **Hetzelfde model wordt aangeboden door tientallen hostingproviders met verschillende
  limieten** — voor `z-ai/glm-5.3-flash` zijn er 23 hostingproviders, waarvan er één is beperkt tot
  2.048 uitvoertokens. De preflight leest `/api/v1/models/{modèle}/endpoints`,
  sluit hostingproviders uit met minder dan 8.000 uitvoertokens of met een verminderde status en
  zet de overige vast met `allow_fallbacks: false`.
- **Redeneren wordt gefactureerd tegen het uitvoertarief** — 107 tokens tegenover 2 voor
  een „OK”-antwoord van `z-ai/glm-5.2`. Het is standaard uitgeschakeld; modellen
  die het verplichten, krijgen de laagste inspanning die ze accepteren, omdat de standaardwaarde van de
  catalogus de uitvoer kan verzadigen voordat de vertaling is voltooid.
  `--reasoning_effort` behoudt voorrang.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Het contextvenster komt uit de catalogus. Een model met minder dan 16.400 tokens wordt
  vóór elke aanroep geweigerd: 8.400 voor de prompt en het segment, minimaal 8.000
  voor de uitvoer.
- Een slug die niet in de catalogus staat, een onbereikbare catalogus of het ontbreken
  van een hostingprovider die de limiet aankan, stopt de opdracht.
- `finish_reason=length` met lege uitvoer is een door
  redeneren verbruikt budget, geen afkapping: de melding maakt dit onderscheid.
- `--eco` heeft geen effect.
- Variabelen: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (standaard `https://openrouter.ai/api/v1`, `https://`
  vereist), `OPENROUTER_TIMEOUT` (standaard 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (standaard 30).

### Vertaalnotitie

`--add_translation_note` voegt een notitie toe, in `bottom` (standaard), `top` (na de
front matter) of `both` (`--note_position`), in de indeling `legacy` (vetgedrukte
alinea, standaard) of `marker` (`--note_format`). De indeling `marker` is een
onzichtbare Markdown-referentiedefinitie,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
gevolgd door een vetgedrukt citaat: leesbaar op GitHub en tijdens het bouwen te verwerken door een
remark-plugin.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Gedetailleerde metingen

Alle metingen zijn daadwerkelijk met `aipmt` uitgevoerde vertalingen naar
veertien talen: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Geschreven** telt de bestanden die door de controles zijn doorgelaten; **Zonder
afwijking** de bestanden waarin `scripts/compare_structure.py` niets vaststelt — hetzelfde aantal
secties, tussenkoppen, links, afzonderlijke URL's, codeblokken,
inline codes, tabelregels, citaatblokken en vetgedrukte woorden.

„Zonder afwijking” betekent „niets gedetecteerd”, niet „identiek”: de vergelijker
telt elementen zonder hun inhoud te lezen. Hij meldt noch een verwijderde kop
van niveau 4, noch de vervangen tekst van een inline code, noch een verwisselde
vlag, noch een interne link die met een haakje te veel is weergegeven,
`[texte]((#ancre))`, die nergens meer naartoe leidt — en hij beoordeelt de
taal niet.

### Dicht monitoringartikel, modus `--news`

Een editie van het [AI-monitoringoverzicht van jls42.org](https://jls42.org/fr/news):
589 regels, 140 links, 21 secties, 3 beschermde Engelse citaten. Campagne
van 4 en 5 september 2026.

| Model                                           | Toegang            | Geschreven | Zonder afwijking | Mediaan/taal |
| ----------------------------------------------- | ------------------ | ---------- | ---------------- | ------------ |
| `gemini-3.7-flash`                              | Google API         | 14/14      | ✅ **14/14**      | 1 min 18 s   |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google-abonnement  | 14/14      | ✅ **14/14**      | 3 min 59 s   |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google-abonnement  | 14/14      | ✅ **14/14**      | 3 min 14 s   |
| `claude-sonnet-5-5`                             | Anthropic API      | 14/14      | ✅ **14/14**      | 3 min 37 s   |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT-abonnement | 14/14      | ✅ **14/14**      | 11 min 28 s  |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14      | ✅ **14/14**      | 5 min 37 s   |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14      | ✅ **14/14**      | 26 min 23 s  |
| `sonnet` (`--use_claude_code`)                  | Claude-abonnement  | 14/14      | ⚠️ 13/14          | 6 min 49 s   |
| `claude-sonnet-5`                               | Anthropic API      | 14/14      | ⚠️ 11/14          | 6 min 31 s   |
| `haiku` (`--use_claude_code`)                   | Claude-abonnement  | 14/14      | ⚠️ 11/14          | 15 min 54 s  |
| `claude-haiku-5-5`                              | Anthropic API      | 14/14      | ⚠️ 11/14          | 2 min 54 s   |
| `claude-haiku-4-5`                              | Anthropic API      | 14/14      | ⚠️ 7/14           | 6 min 00 s   |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14      | ❌ 11/14          | 9 min 27 s   |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14      | ❌ 8/14           | 10 min 09 s  |
| `ollama/gpt-oss-20b-32k`                        | lokaal             | 10/14      | ❌ 7/14           | 12 min 39 s  |
| `mistral-large-latest`                          | Mistral API        | 11/14      | ❌ 5/14           | 5 min 32 s   |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14       | ❌ 3/14           | 37 min 27 s  |
| `grok-4.6` (`--use_grok_cli`)                   | Grok-abonnement    | 1/14       | ❌ 1/14           | 23 min 11 s  |
| `opus` (`--use_claude_code`)                    | Claude-abonnement  | 0/14       | ❌ 0/14           | —            |

Grok is op 9 september opnieuw gemeten op een andere editie van hetzelfde monitoringoverzicht
(356 regels): 9 van de 14 talen geschreven, 8 zonder afwijking. Dat is het cijfer dat
in de overzichtstabel staat. Drie afgebroken campagnes zijn niet
opgenomen: `qwen3.5-27b` (9 talen) en `kimi-k2.6` (4) wegens onvoldoende tegoed,
`z-ai/glm-5.3-flash`, waarvan de twee mislukkingen het gevolg waren van een instelling voor redeneren
die de provider sindsdien heeft gecorrigeerd. De OpenRouter-regels zijn gemeten met de
standaardinstellingen van de router, vóór `--use_openrouter`; `z-ai/glm-5.2`,
opnieuw gemeten met de meegeleverde provider, behaalt eveneens 14/14. De cijfers zijn op
10 september opnieuw berekend met de huidige vergelijker: `qwen3.8-flash` en
`qwen3.7-flash` winnen elk één taal ten opzichte van de eerste
publicatie; de overige zijn ongewijzigd.

De regels voor `--use_antigravity` zijn op 26 september op hetzelfde
artikel gemeten, met vier parallelle vertalingen: `gemini-3.7-flash-medium` 's ochtends,
`gemini-3.8-flash-medium` 's middags. In het Engels verwijderden beide modellen zelf
de drie regels met de Franse vertaling onder de citaten, zonder een vlag te
verzinnen, en de Engelse citaten zijn intact: de noodopschoning hoefde
niets te doen. Met `--eco` (`gemini-3.7-flash-low`), voor slechts vier talen
(en, ja, ar, hi): 4 van de 4 geschreven, allemaal zonder afwijking, met een mediaan van
1 min 52 s. Controletest op dezelfde dag met een recentere editie van het monitoringoverzicht,
die van 25 september (438 regels, 2 Engelse citaten), buiten de
blog vertaald door `gemini-3.7-flash-medium`: 14 van de 14 geschreven, allemaal zonder afwijking, 87 tot
128 s per taal.

De regels voor `--use_claude_code` zijn op 26 september op hetzelfde
artikel gemeten, met vier parallelle vertalingen en inspanning `low`. Met `sonnet` zijn de
Engelse citaten intact in alle veertien talen en heeft het model in het Engels
zelf de regels met de Franse vertaling verwijderd, zonder een vlag te verzinnen.
`opus` heeft geen enkele taal geschreven: in elke taal stopten de beveiligingen
het antwoord bij het laatste segment wegens een kort bericht over 279 moleculen
die voor een bindingsplaats waren gegenereerd. Wanneer alleen dit bericht werd verzonden, werd het geweigerd
op grond van de categorie „bio”; `sonnet` vertaalde het overal. `haiku` schrijft
alle veertien talen; in drie daarvan (en, pl, ro) verandert een sectiekop van
niveau 2 in niveau 1. Het redeneert zonder dat dit kan worden verhinderd — 61% van
zijn uitvoertokens — en doet er daarom ruim twee keer zo lang over als `sonnet`.

De regels voor `claude-sonnet-5-5`, `claude-haiku-5-5` en `claude-haiku-4-5` zijn
op 18 oktober via de API van Anthropic gemeten, op hetzelfde artikel, met vier
parallelle vertalingen per model. Sonnet 5.5 weigert dat zijn
redenering wordt uitgeschakeld: aipmt stuurt het de laagste instelling die het accepteert, en zijn
antwoorden bevatten geen redenering. Het schrijft alle veertien talen zonder afwijking en zonder
een segment opnieuw te verwerken; in het Engels verwijderde het zelf de regels met de
Franse vertaling, zonder een vlag te verzinnen, en de Engelse citaten zijn
overal intact. Haiku 5.5 is gemeten met zijn adaptieve redenering: met de redenering
uitgeschakeld liet het volledige alinea's in het Frans staan, wat door de controle wordt geweigerd —
3 van de 14 talen geschreven. Beide Haiku-modellen lopen vast op hetzelfde korte bericht: Haiku 5.5
wijzigt het niveau van de titel of verdubbelt die in het Japans, Koreaans en
Chinees; Haiku 4.5 maakt er in zeven talen niveau 1 van en laat hem in het
Japans in het Frans staan. Haiku 4.5 kost $ 3,67 voor beide documenten in de
veertien talen, Haiku 5.5 $ 0,57 en Sonnet 5.5 $ 9,21.
### README van dit project, standaard Markdown

Vastgelegde revisie van 9 september 2026: 785 regels, 285 inlinecodes, 40
afsluitingen van blokken, 89 tabelregels. Vier vertalingen parallel.

| Model                                           | Geschreven | Zonder afwijking | Mediaan/taal | Wat afwijkt                                                               |
| ----------------------------------------------- | ---------- | ---------------- | ------------ | ------------------------------------------------------------------------- |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14      | ✅ 14/14         | 1 min 43 s   | niets                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14      | ✅ 14/14         | 1 min 48 s   | niets                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14      | ✅ 14/14         | 4 min 02 s   | niets volgens de vergelijker; interne links verdubbeld (en)               |
| `claude-sonnet-5-5`                             | 14/14      | ✅ 14/14         | 1 min 18 s   | niets                                                                     |
| `claude-haiku-4-5`                              | 14/14      | ✅ 14/14         | 2 min 06 s   | niets                                                                     |
| `gemini-3.7-flash`                              | 14/14      | ⚠️ 13/14         | 36 s         | één vetgedrukt woord (ja)                                                 |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14      | ⚠️ 13/14         | 1 min 22 s   | één vetgedrukt woord (ko)                                                 |
| `sonnet` (`--use_claude_code`)                  | 14/14      | ⚠️ 13/14         | 2 min 20 s   | één tabelregel aan de vorige vastgeplakt (ar)                             |
| `claude-sonnet-5`                               | 14/14      | ⚠️ 12/14         | 2 min 56 s   | één link (sv), één vetgedrukt woord (zh)                                  |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14      | ⚠️ 12/14         | 6 min 46 s   | één vetgedrukt woord (ar, ja)                                             |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14      | ⚠️ 11/14         | 2 min 34 s   | één vetgedrukt woord (hi, ja, ko)                                         |
| `qwen/qwen3.7-flash`                            | 14/14      | ⚠️ 10/14         | 2 min 17 s   | 40 inlinecodes toegevoegd in het Arabisch; vet (hi, ja, ko)               |
| `claude-haiku-5-5`                              | 12/14      | ❌ 12/14         | 1 min 14 s   | 2 talen geweigerd (ar, hi): inlinecodes verloren bij teruggave            |
| `mistral-large-latest`                          | 14/14      | ❌ 1/14          | 2 min 44 s   | één sectie verloren (ar, hi, ko); codeblokken toegevoegd (ja, ko, ro, zh) |

Twee afgebroken campagnes zijn niet opgenomen: Grok, waarvan de CLI-sessie
na twaalf talen verliep (elf zonder afwijking), en `qwen3.8-flash`, met HTTP 429 van zijn
host na twee. `opencode/mimo-v2.5-free` en `ollama/gpt-oss-20b-32k`
zijn niet opnieuw gemeten op deze revisie; op die van 4 en 5 september,
die 277 regels korter was, schreven ze elk 9 vertalingen van de 14, waarvan
respectievelijk 7 en 1 zonder afwijking.

De regels `--use_antigravity` en `--use_claude_code` zijn niet gemeten op
de vastgelegde revisie, maar op 26 september op de revisie die met 1.14.0 werd gepubliceerd — en
de regels `claude-sonnet-5-5`, `claude-haiku-5-5` en `claude-haiku-4-5` op 18
oktober, op dezelfde revisie: 600 regels, 257 inlinecodes, 30 afsluitingen van blokken, 85
tabelregels. Omdat deze revisie 185 regels
korter is, kan ze niet rechtstreeks met de andere regels worden vergeleken;
deze regels kunnen onderling wel worden vergeleken. Wat de interne links betreft, die de
vergelijker niet controleert, heeft `gemini-3.8-flash-medium` ze in
alle veertien talen intact gehouden en heeft `gemini-3.7-flash-medium` ze in het Italiaans verbroken;
`sonnet` en `opus` hebben ze overal intact gehouden, terwijl `haiku` ze in
het Engels heeft verdubbeld; `claude-sonnet-5-5` en `claude-haiku-4-5` hebben ze in
alle veertien talen intact gehouden, en `claude-haiku-5-5` in de twaalf die het heeft geschreven.

### Vier README's van bekende projecten

FastAPI, Ollama, tldr-pages en Vue.js, ongewijzigd overgenomen van GitHub —
documenten die eenvoudiger zijn dan de twee voorgaande. De campagne was gericht op de modellen
die moeite hadden; Gemini dient daarbij als vergelijkingspunt.

| Model                     | Bereik                     | Geschreven | Zonder afwijking |
| ------------------------- | -------------------------- | ---------- | ---------------- |
| `gemini-3.7-flash`        | 4 projecten × 14 talen     | 56/56      | ✅ **55/56**     |
| `opencode/mimo-v2.5-free` | 4 projecten × 14 talen     | 55/56      | ❌ 47/56         |
| `grok-4.6` (abonnement)   | 4 projecten × ar, hi, ja, zh | 16/16      | ❌ 14/16         |
| `ollama/gpt-oss-20b-32k`  | 4 projecten × ar, hi, ja, zh | 15/16      | ❌ 9/16          |

### Wat deze metingen niet zijn

- **Geen uitputtende ranglijst**: alleen OpenRouter biedt al meer dan vierhonderd
  modellen, waarvan er ongeveer vijftien zijn gemeten.
- **Indicatieve doorlooptijden**: afhankelijk van de campagne liepen er drie tot zes vertalingen
  parallel, en de verwerkingssnelheid van een leverancier varieert gedurende de dag.
- **Tijdgebonden waarnemingen**: modellen veranderen onder dezelfde naam, en uw
  documenten zijn niet de onze.

Om de meting opnieuw uit te voeren op uw documenten, op een vastgelegde kopie van het bestand:

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

Optionele maar aanbevolen kwaliteitsinstrumenten:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

De 28 vertalingen van de repository (README en CHANGELOG, veertien talen) worden
opnieuw gegenereerd met `./regen_translations.sh --force` — standaard Codex en `gpt-5.6-sol` via
het ChatGPT-abonnement, vier parallel. `REGEN_PROVIDER` en
`REGEN_MODEL` wijzigen de route: `antigravity` blijft op een abonnement, dat
van Google, en wordt zonder uitzondering toegestaan; een betaalde API (`openai`, `gemini`,
`grok`, `openrouter`) wordt zonder `REGEN_ALLOW_PAID_API=1` geweigerd;
`REGEN_JOB_TIMEOUT` begrenst elke job (600 s, 1 800 s op Codex en
Antigravity). De details van de hulpmiddelen staan in `CLAUDE.md`.

## Projecten die dit script gebruiken

- **[jls42.org](https://jls42.org)** — persoonlijke blog gepubliceerd in 15 talen. De
  [dagelijkse AI-monitoring](https://jls42.org/fr/news) wordt elke dag
  door dit hulpmiddel vertaald en dient als referentiedocument voor de bovenstaande metingen.

## Auteur

Julien LE SAUX
E-mail: contact@jls42.org

## Licentie

GNU GENERAL PUBLIC LICENSE Version 3. Zie [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Waarschuwing

Dit programma wordt gedistribueerd **zonder enige garantie**, volgens de voorwaarden van
secties 15 en 16 van de GPL v3: geleverd „zoals het is”, zonder garantie van
verkoopbaarheid of geschiktheid voor een bepaald doel, en de auteur kan niet
aansprakelijk worden gesteld voor schade die voortvloeit uit het gebruik ervan. De tekst van de
licentie heeft voorrang op deze samenvatting.

- **Lees alles na voordat u publiceert.** De beveiligingen omvatten codeblokken,
  inlinecode, URL's, ankers en citaten in de modus `--news` — maar niet
  koppen, tabellen, front matter of de betekenis van uw zinnen.
- **Uw documenten worden naar de gekozen leverancier verzonden**, onder diens
  gebruiksvoorwaarden en gegevensbeleid. Sommige gratis modellen kunnen
  uw uitwisselingen hergebruiken voor training, en de voorwaarden van Antigravity
  staan Google toe ze te hergebruiken en door mensen te laten nalezen,
  ook met een betaald abonnement; een lokaal model is de enige manier waarop
  geen gegevens uw machine verlaten.
- **De API-aanroepen worden bij u in rekening gebracht.** Dit programma stelt geen maximum aan de
  uitgaven: een lang document, een hervatting na een fout of een model dat veel redeneert,
  kost meer.
- **De gepubliceerde metingen zijn tijdgebonden waarnemingen**, geen garanties.

De genoemde product- en bedrijfsnamen behoren toe aan hun respectieve
eigenaren. Dit project is niet aan een van hen verbonden.

**Artikel vertaald van het Frans naar het Nederlands met gpt-5.6-sol.**

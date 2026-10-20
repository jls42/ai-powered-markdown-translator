# AI-Powered Markdown-vertaler

🌍 [Frans](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [Engels](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Spaans](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Chinees](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Duits](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Japans](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Koreaans](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Arabisch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiaans](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Pools](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Portugees](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Roemeens](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Zweeds](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Codekwaliteit</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status van de kwaliteitscontrole"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Beveiligingsbeoordeling"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Betrouwbaarheidsbeoordeling"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Onderhoudbaarheidsbeoordeling"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Testdekking"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Kwetsbaarheden"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Gedupliceerde regels (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Technische schuld"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Regels code"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy-badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Vertaalt Markdown-bestanden van de ene taal naar de andere met behoud van de
structuur: codeblokken, inline code, URL's, ankers, tabellen en front
matter. Elf manieren om een model aan te roepen — vijf API's, vier abonnementen zonder
gebruiksafhankelijke facturering, twee routers — en een gepubliceerde meting van wat elk
model daadwerkelijk behoudt.

## In het kort

- **Elf providerroutes**: API's van OpenAI, Mistral, Claude, Gemini en Grok;
  abonnementen op ChatGPT (Codex), Grok, Google (Antigravity) en Claude (Claude
  Code) zonder gebruiksafhankelijke facturering; routers OpenCode (open source, gratis of lokaal) en OpenRouter
  (meer dan 400 modellen).
- **Geen fouten door een verloren token**: codeblokken, inline code,
  URL's, ankers en citaten worden vóór de aanroep vervangen door tokens en
  na afloop gecontroleerd. Ontbreekt er één, dan wordt het bestand niet geschreven.
- **Lange documenten**: opdeling volgens het contextvenster van het model.
- **Modus `--news`**: beschermde Engelse citaten en vlaggen beheerd per
  taal, voor nieuwsmonitoringartikelen.
- **Modus `--eco`**: snelle en goedkopere modellen.
- Optionele **vertaalnotitie**, bovenaan, onderaan of op beide plaatsen.

## Installatie

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 of nieuwer. Zie voor installatie vanuit de repository
[Bijdragen](#bijdragen).

## Configuratie

Sleutels worden op drie plaatsen gelezen, van hoogste naar laagste prioriteit; elke plaats
vult alleen aan wat de vorige leeg laat.

|     | Waar                                            | Waarvoor                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Omgevingsvariabelen                     | CI, containers, eenmalige overschrijving |
| 2   | `.env` in de huidige map (of een bovenliggende map) | een projectspecifieke sleutel            |
| 3   | `~/.config/aipmt/.env`                        | eenmaal ingesteld, overal geldig       |

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
onder Windows. Zonder sleutel vermeldt de opdracht de drie locaties.

**De `.env` van een project kan geen aanroepen omleiden of het uit te voeren programma
kiezen.** Het levert sleutels, nooit een bestemming of een uitvoerbaar bestand: elke
variabele met `_BASE_URL`, `_API_BASE`, `_ENDPOINT` of `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, de proxy's (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), de certificaatopslagplaatsen (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) en `XDG_CONFIG_HOME` /
`APPDATA` worden er genegeerd, met een waarschuwing. Een gekloonde repository mag
uw sleutel niet kunnen kapen of u bij de eerste vertaling zijn eigen programma laten
uitvoeren. Dit bestand wordt ook zonder interpolatie gelezen:
`NOM=${OPENAI_API_KEY}` kopieert de sleutel er niet in. Stel deze variabelen in
de omgeving of in `~/.config/aipmt/.env` in.

Optionele variabelen: `XAI_BASE_URL` (standaard `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (seconden per aanroep, standaard 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(standaard 600), `GROK_BIN`, `GROK_HOME` (standaard `~/.grok`), `GROK_TIMEOUT`
(standaard 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (standaard 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (standaard 600), `OPENROUTER_BASE_URL`
(`https://` vereist), `OPENROUTER_TIMEOUT` (standaard 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (standaard 30). Elk wordt toegelicht in de
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

`document.md` vertaald naar het Spaans levert `document-es.md` op in `--target_dir`;
met `--include_model`, `document-es-gpt-5.6-terra.md`. De extensie wordt
altijd `.md` — `article.mdx` levert `article-en.md` op — behalve met
`--keep_filename`, dat de oorspronkelijke naam behoudt. Een reeds aanwezige vertaling
wordt overgeslagen zonder `--force`.

Exitcodes: `0` als alles is geslaagd of overgeslagen, `1` als er nog een bestand
is mislukt (lijst op de standaardfoutuitvoer), `2` als de configuratie de oorzaak is.
Een mislukt bestand wordt nooit geschreven, ook niet als het schrijven zelf mislukt:
de inhoud wordt ernaast geschreven en vervolgens hernoemd. Opnieuw uitvoeren volstaat.

## Welk model kiezen

Gemeten op twee echte documenten, door elk model vertaald naar
dezelfde veertien talen. **Het cijfer is het aantal talen, van de veertien, waarin de
vertaling wordt geschreven en niets afwijkt van de bron.**

| Model                | Toegang                 | Dicht nieuwsmonitoringartikel | Deze README    | Wat afwijkt, en in hoeveel talen                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google-abonnement (Antigravity)   | ✅ 14/14                | ✅ 14/14     | niets, in geen van beide documenten                                                                                                                                 |
| **Claude Sonnet 5.5** | API-sleutel van Anthropic                 | ✅ 14/14                | ✅ 14/14     | niets, in geen van beide documenten                                                                                                                                 |
| **Gemini 3.7 Flash**  | API-sleutel van Google                    | ✅ 14/14                | ⚠️ 13/14     | 1 taal van de 14: één extra vetgedrukt woord (ja)                                                                                                                      |
| **Gemini 3.7 Flash**  | Google-abonnement (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 1 taal van de 14: één vetgedrukt woord minder (ko)                                                                                                                     |
| **GPT-5.6 Sol**       | ChatGPT-abonnement of OpenAI-sleutel | ✅ 14/14                | ⚠️ 12/14     | 2 talen van de 14: één vetgedrukt woord minder (ar, ja)                                                                                                                |
| **GLM-5.2**           | OpenRouter-sleutel                    | ✅ 14/14                | ⚠️ 11/14     | 3 talen van de 14: één vetgedrukt woord minder (hi, ja, ko)                                                                                                            |
| Claude Sonnet 5       | Claude-abonnement (Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 1 taal van de 14 in het artikel: één extra vetgedrukt woord (zh); 1 in deze README: een tabelrij vastgeplakt aan de vorige, onzichtbaar bij weergave (ar)            |
| Claude Haiku 4.5      | Claude-abonnement (Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 3 talen in het artikel: een sectiekop naar niveau 1 verplaatst (en, pl, ro); in deze README niets volgens de vergelijker, maar de interne links ook in het Engels herhaald |
| Claude Sonnet 5       | API-sleutel van Anthropic                 | ⚠️ 11/14                | ⚠️ 12/14     | 3 talen in het artikel: een codeblok verschenen (es, de, hi); 2 in deze README: een link zonder opmaak (sv), een vetgedrukt woord (zh)                              |
| Claude Haiku 4.5      | API-sleutel van Anthropic                 | ⚠️ 7/14                 | ✅ 14/14     | 7 talen in het artikel: een sectiekop naar niveau 1 verplaatst — in het Japans in het Frans gebleven; niets in deze README                                              |
| Claude Haiku 5.5      | API-sleutel van Anthropic                 | ⚠️ 11/14                | ❌ 12/14     | 3 talen in het artikel: een sectiekop van niveau veranderd of gedupliceerd (ja, ko, zh); in deze README 2 talen geweigerd, inline code verloren (ar, hi)    |
| Qwen 3.7 Flash        | OpenRouter-sleutel                    | ❌ 8/14                 | ⚠️ 10/14     | 1 taal geweigerd voor het artikel, 5 andere wijken af; in deze README ongeveer veertig woorden in `code` gezet (ar)                                                    |
| Grok 4.6              | Grok-abonnement                   | ❌ 8/14                 | niet beoordeeld     | 5 talen van de 14 geweigerd omdat inline code en URL's niet werden teruggegeven; het Nederlands wijkt op alle punten af                                                               |
| GPT-OSS 20B           | lokaal model (Ollama)             | ❌ 7/14                 | niet opnieuw gemeten | 4 talen van de 14 geweigerd: het model liet passages in het Frans staan, de controle hield ze tegen                                                                  |
| MiMo v2.5 (gratis)   | OpenCode Zen, zonder account         | ❌ 11/14                | niet opnieuw gemeten | 1 taal geweigerd; een sectie verloren in het Pools                                                                                                                  |
| Mistral Large         | API-sleutel van Mistral                   | ❌ 5/14                 | ❌ 1/14      | **een volledige sectie verdwijnt**: 1 taal in het artikel (hi), 3 in deze README (ar, hi, ko) — en 3 talen geweigerd voor het artikel                                |
| DeepSeek V4 Flash     | OpenRouter-sleutel                    | ❌ 3/14                 | niet opnieuw gemeten | 10 talen van de 14 geweigerd; 37 minuten per taal                                                                                                                 |
| Claude Opus 5.5       | Claude-abonnement (Claude Code)   | ❌ 0/14                 | ✅ 14/14     | het artikel in alle 14 talen geweigerd door de veiligheidscontroles van Opus vanwege een kort biologiebericht; niets in deze README                                               |

|     | Wat het symbool betekent                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alle veertien talen vertaald, en niets wijkt af van de bron                                                                                                                                       |
| ⚠️  | alle veertien talen vertaald; de afwijkingen betreffen **opmaak** — een vetgedrukt woord, een `code`, een link die zijn haakjes verliest. Er ontbreekt geen tekst, URL, codeblok of sectie |
| ❌  | minstens één taal kon niet worden vertaald — het bestand wordt geweigerd en niet geschreven — **of** er ontbreekt inhoud in een geschreven bestand                                                                      |

Wat u hiervan moet onthouden:

- **Een geweigerde vertaling is geen beschadigde vertaling.** Als er bij
  terugkomst een token ontbreekt, wordt het bestand niet geschreven en telt de taal als
  geweigerd. Dat gebeurt bij Grok voor het artikel: vier stukken inline code en
  drie URL's gaan al in het eerste segment verloren, bij de vijf niet-Latijnse schriftsystemen.
- **Een model kan een heel document weigeren vanwege één zin.** Opus 5.5
  vertaalt deze README zonder enige afwijking, maar geen enkel nieuwsmonitoringartikel: zijn
  veiligheidscontroles stoppen het antwoord bij een kort biologiebericht. Het bestand wordt
  niet geschreven en aipmt vertelt waarom.
- **Dit vangnet dekt geen koppen, tabellen, front matter of
  tekst.** Een model dat een sectie verwijdert, levert een bestand op dat de tool
  zonder bezwaar schrijft — dat gebeurt bij Mistral. Deze elementen kunnen niet
  door een token worden vervangen en de huidige controles controleren ze niet;
  `scripts/compare_structure.py` detecteert een verloren sectie, maar pas achteraf.
- **Grok heeft geen beoordeling voor deze README**: de CLI-sessie verliep na twaalf
  talen, waarvan elf zonder afwijking. Een onderbroken meetronde krijgt geen beoordeling.
- **De dichtheid van het document telt zwaarder dan de taal.** Grok houdt stand bij
  gewone README's en haakt af bij een artikel vol links, ook in
  het Nederlands.

Datums en documenten: de kolom ‘Deze README’ is op 9 september 2026 gemeten
op een vastgezette revisie van dit bestand (785 regels, 285 stukken inline code, 89
tabelrijen), die sindsdien is aangepast — behalve de rijen voor Antigravity en Claude Code,
gemeten op 26 september op de kortere revisie die met 1.14.0 is gepubliceerd
(600 regels, 257 stukken inline code, 85 tabelrijen), en de rijen voor Claude
Sonnet 5.5, Haiku 5.5 en Haiku 4.5 via de API, gemeten op 18 oktober op
dezelfde revisie. De kolom ‘Dicht nieuwsmonitoringartikel’ komt uit de meetronde van
4 en 5 september op een artikel van 589 regels, behalve de rij voor Grok, opnieuw gemeten op
9 september op een andere editie van dezelfde nieuwsmonitoring, de rijen voor Antigravity en
Claude Code, gemeten op 26 september op hetzelfde artikel, en deze drie rijen voor
Claude, op 18 oktober. De volledige tabellen, de tijdsduren en het protocol staan
in [Gedetailleerde metingen](#gedetailleerde-metingen).
## Alle opties

| Optie                   | Beschrijving                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Eén Markdown-bestand om te vertalen (alternatief voor `--source_dir`)                                             |
| `--source_dir`           | Bronmap met Markdown-bestanden (standaard: `content/posts`)                                   |
| `--target_dir`           | Uitvoermap voor vertaalde bestanden (standaard: `traductions_en`)                                    |
| `--source_lang`          | Brontaal (standaard: `fr`)                                                                                  |
| `--target_lang`          | Doeltaal (standaard: `en`)                                                                                   |
| `--model`                | Specifiek te gebruiken model                                                                                  |
| `--eco`                  | Goedkope modellen gebruiken                                                                              |
| `--use_mistral`          | De Mistral AI API gebruiken                                                                                     |
| `--use_claude`           | De Claude API gebruiken                                                                                         |
| `--use_gemini`           | De Gemini API gebruiken                                                                                         |
| `--use_grok`             | De xAI API (Grok) gebruiken — vereist `XAI_API_KEY`                                                           |
| `--use_codex`            | De Codex CLI gebruiken met het quotum van het ChatGPT-abonnement                                                    |
| `--use_grok_cli`         | De Grok CLI gebruiken met het quotum van het Grok-abonnement                                                        |
| `--use_antigravity`      | De Antigravity CLI (`agy`) gebruiken met het quotum van het Google AI Pro- of Ultra-abonnement                       |
| `--use_claude_code`      | De Claude Code CLI (`claude -p`) gebruiken met het quotum van het Claude Pro- of Max-abonnement                      |
| `--use_opencode`         | OpenCode (open source) gebruiken met de in OpenCode ingestelde provider; vereist `--model provider/modèle` |
| `--use_openrouter`       | OpenRouter gebruiken — vereist `OPENROUTER_API_KEY` en `--model fournisseur/modèle`                          |
| `--force`                | Opnieuw vertalen afdwingen                                                                                       |
| `--keep_filename`        | De oorspronkelijke bestandsnaam behouden                                                                          |
| `--news`                 | Nieuwsmodus: beschermt EN-citaten, beheert vlaggen per taal                                      |
| `--add_translation_note` | Een vertaalnotitie toevoegen                                                                                |
| `--note_position`        | Positie van de notitie: `top`, `bottom` (standaard), of `both`                                                     |
| `--note_format`          | Opmaak van de notitie: `legacy` (standaard, vetgedrukte alinea) of `marker`                                            |
| `--include_model`        | De modelnaam opnemen in het uitvoerbestand                                                            |
| `--reasoning_effort`     | Redeneerinspanning van GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

De negen flags `--use_*` sluiten elkaar uit: twee ervan combineren wordt
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

`--eco` schakelt over naar de goedkope variant van elke provider.

| Provider    | Kwaliteit (standaard)                                                     | Goedkoop (`--eco`)      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                                      | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                                   | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (ook `gpt-5.6-sol`, `terra` en `luna` via `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                                           | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, inspanning `low`                                               | idem — `--eco` heeft geen effect |
| OpenCode    | `--model provider/modèle` vereist                                | idem — `--eco` heeft geen effect |
| OpenRouter  | `--model fournisseur/modèle` vereist                             | idem — `--eco` heeft geen effect |

### Via het ChatGPT-abonnement: `--use_codex`

Stuurt de officiële Codex CLI aan: de vertaling gaat van het quotum van het
ChatGPT-abonnement af, zonder API-sleutel of facturering per gebruik.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Het uitvoerbare bestand wordt gezocht in `CODEX_BIN`, vervolgens in `PATH`, en daarna in het package
  `openai-codex-cli-bin`. `~/.codex/auth.json` wordt nooit gelezen.
- `OPENAI_API_KEY` en `CODEX_API_KEY` worden verwijderd uit de omgeving van het
  subproces: een aanwezige sleutel leidt nooit tot overschakeling naar de API.
- Elk segment kost minstens één ‘bericht’ van het venster van 5 uur — twee
  als de validatie mislukt en het opnieuw wordt geprobeerd. OpenAI noemt als
  schatting 250-2 000 berichten/5 h voor `gpt-5.6-luna` (`--eco`) en
  10-100 voor `gpt-5.6-sol` met een Plus-abonnement.
- `--model gpt-5.6-sol`, de standaard tot en met 1.16.3, `--model gpt-5.6-terra`
  en `--model gpt-5.6-luna` werken ook via het abonnement.
- Bij een 429 van de server gaat het bestand niet verloren: Codex maakt zelf opnieuw verbinding,
  aipmt wacht tot de beurt is afgelopen, en als de 429 aanhoudt, wordt het segment
  na 30 en vervolgens 60 seconden opnieuw geprobeerd. Een model waartoe het account geen toegang heeft, geeft een 400 met de melding ‘het model wordt
  niet ondersteund bij gebruik van Codex met een ChatGPT-account’.
- Langzamer dan een API, en het verschil groeit met het document: voor deze README
  is de mediaan 6 min 46 s per taal met `gpt-5.6-sol`, tegenover 36 s voor
  `gemini-3.7-flash`.
- Geweigerd in CI (als `CI` of `GITHUB_ACTIONS` is ingesteld): het abonnement gebruikt
  een persoonlijk sessiebestand voor authenticatie, dat niet thuishoort op een gedeelde
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

- **Zwakkere isolatie dan bij Codex.** De OS-sandbox van Grok werkt
  niet op veel recente Linux-systemen (AppArmor, sockets van de
  container-runtime), en een profiel dat niet kan worden toegepast, start stilzwijgend zonder
  isolatie. Het script vraagt daarom standaard geen profiel aan, meldt dit, en
  vertrouwt op de `--deny`-regels van de CLI, waaronder de catch-all `*` — de enige
  laag die weigert te starten in plaats van de bescherming zonder
  melding uit te schakelen. `GROK_TRANSLATE_SANDBOX=read-only` vereist de OS-sandbox, en het starten
  mislukt als de machine die niet kan toepassen.
- Het quotum is wekelijks, wordt gedeeld met Chat, Imagine en Voice, en geen
  enkel commando kan het uitlezen: een batch kan het beschikbare gespreksgebruik
  ongemerkt verminderen.
- Variabelen: `GROK_BIN`, `GROK_HOME` (CLI-map, standaard `~/.grok`),
  `GROK_TIMEOUT` (standaard 900), `GROK_TRANSLATE_SANDBOX`.

### Via het Google-abonnement: `--use_antigravity`

Hetzelfde principe met `agy`, de officiële CLI van Antigravity: voor wie Google
AI Pro of Ultra betaalt, gaat de vertaling van het abonnementsquotum af in plaats
van per token te worden gefactureerd. Dit is de enige manier om dat quotum te gebruiken: Gemini CLI
bedient deze accounts niet meer sinds 18 juni 2026
([aankondiging](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
en de SDK van Antigravity accepteert alleen een API-sleutel of een Google Cloud-project.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Er blijft geen betaalde route open.** agy ontvangt uit uw
  omgeving alleen een vaste lijst variabelen — `PATH`, taal en tijdzone,
  terminal, identiteit, proxies en certificaten, sessiebus — en geen enkele sleutel:
  meerdere van zijn variabelen schakelen een aanroep ongemerkt om (gemeten:
  één stuurt het document naar een gateway van een derde partij, een andere naar een
  gefactureerd Google Cloud-project), en bij elke herlezing bleek een blokkeerlijst er enkele te missen.
  Vóór elk segment moet `agy -p /config`, dat geen quotum verbruikt, aantonen
  dat betaalde AI-credits zijn uitgeschakeld, zonder API-sleutel of Google Cloud-project — een
  ontbrekende instelling geldt als weigering — anders wordt niets vertaald; het log van elke
  aanroep moet vervolgens het gebruik van het abonnement bevestigen (`authMethod=consumer`), anders wordt het
  antwoord geweigerd.
- **Isolatie.** Elke aanroep draait in een privé, tijdelijke persoonlijke map,
  met een vertaalagent zonder tools: uw instellingen, regels,
  plugins, MCP-servers en agy-hooks komen daar niet terecht, er wordt niets aan uw
  geschiedenis toegevoegd, en de aanmelding blijft in de sleutelbos, die aipmt nooit leest.
  Als een agent niet wordt gevonden, valt agy stilzwijgend terug op zijn codeeragent
  en diens tools: een volledige logregel moet de juiste agent bevestigen — een
  document dat deze melding citeert, volstaat niet — anders volgt weigering.
- **Platforms**: Linux, in een sessie met een sleutelbos (D-Bus-sessiebus,
  Secret Service); macOS wordt geaccepteerd, maar is niet gemeten. Geweigerd
  onder Windows, waar agy de variabelen die elke aanroep isoleren niet leest, en
  onder Linux zonder sessiebus — SSH-sessie, container, server: agy slaat daar
  zijn token op in een bestand in `~/.gemini`, dat door de isolatie wordt verborgen. De
  weigering gebeurt vóór het starten, met de reden erbij, in plaats van een minuut
  te wachten op een aanmeldcode.
- **Modellen**: die van `agy models`. Bij Gemini staat de inspanning in de naam
  (`gemini-3.8-flash-medium`…): een naam zonder suffix wordt vóór de aanroep geweigerd,
  en `--reasoning_effort` heeft geen effect. Standaard `gemini-3.8-flash-medium`,
  en `gemini-3.7-flash-low` bij `--eco`; de meetcampagnes waarop deze keuzes berusten, worden
  beschreven in [Gedetailleerde metingen](#gedetailleerde-metingen). Claude en GPT-OSS
  hebben hun eigen, veel kleinere quotum: ongeveer 1 % van het venster van
  5 uur per gemeten aanroep, tegenover 0,05 % bij Flash.
- **Quotum**: per groep een venster van 5 uur en een weekvenster, naar
  verhouding van de kosten in tokens. Gemeten op het account van de auteur: ongeveer
  16 punten van het venster van 5 uur per miljoen brontekens met
  `gemini-3.8-flash-medium`, 14 met `gemini-3.7-flash-medium` en 7 tot 8 bij
  lage inspanning — een README van 40 000 tekens kost dus iets meer dan een
  half punt. De wekelijkse limiet hangt af van het abonnementsniveau. Opnieuw proberen volgt
  wat agy als herhaalbaar aangeeft; anders wordt bij een uitgeput venster nooit
  opnieuw geprobeerd: elk bestand mislukt dan tot de reset
  die `/usage` weergeeft.
- **Langzamer dan de API**: voor het compacte meetartikel is de mediaan 3 min 59 s per
  taal met `gemini-3.8-flash-medium` en 3 min 14 s met
  `gemini-3.7-flash-medium`, tegenover 1 min 18 s voor Gemini 3.7 Flash via de API.
- **Onderbreking**: Ctrl-C of het sluiten van een terminal stoppen agy samen met het
  commando, zodat het zijn beurt niet blijft afmaken ten koste van uw quotum; hetzelfde geldt
  voor Codex, Grok CLI en OpenCode. Onder `nohup` gaat de vertaling door.
- Geweigerd in CI (als `CI` of `GITHUB_ACTIONS` is ingesteld): de aanmelding bevindt zich in een
  persoonlijke sleutelbos. Gebruik op een runner `--use_gemini` met `GOOGLE_API_KEY`.
- Variabelen: `AGY_BIN` (anders `PATH`, vervolgens `~/.local/bin/agy`),
  `AGY_TIMEOUT` (seconden per segment, inclusief opstarten, standaard 900).

**Gebruiksvoorwaarden: uw account staat op het spel.** De
[voorwaarden van Antigravity](https://antigravity.google/terms) (sectie 6) en de
[FAQ](https://antigravity.google/docs/faq/) verbieden toegang tot de dienst
via software van derden met de Antigravity-aanmelding — Claude Code,
OpenClaw en OpenCode worden daarbij genoemd — op straffe van opschorting van het account. aipmt
leest of hergebruikt het token niet: het start het officiële uitvoerbare bestand in de
[headless-modus](https://antigravity.google/docs/cli/headless/) die Google
documenteert voor scripts en CI. Een medewerker van Google noemde het ‘standaard’
om `agy -p` vanuit een lokaal script voor eigen werk te starten
([officieel forum, 25 september 2026, niet-bindend antwoord](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
geen enkele tekst geeft uitsluitsel over een gedistribueerde tool zoals deze.

**Alleen openbare documenten.** Volgens sectie 5 van dezelfde voorwaarden kunnen
uitwisselingen — prompts, antwoorden, metadata — worden gebruikt om de
producten en machine learning van Google te verbeteren en door
mensen worden gelezen, ook bij een betaald abonnement. Afmelden gebeurt via de instelling
`enableTelemetry`, waarvan het effect niet is gedocumenteerd en die aipmt niet instelt; uw
agy-instellingen worden niet meegenomen in de geïsoleerde omgeving. Laat er niets vertrouwelijks doorheen gaan.
### Via het Claude-abonnement: `--use_claude_code`

Hetzelfde principe met `claude`, de officiële CLI van Claude Code, in de modus `-p`: voor
wie voor Claude Pro of Max betaalt, gaat de vertaling van het
abonnementsquotum af in plaats van per token te worden gefactureerd. Niet te verwarren met
`--use_claude`, de API van Anthropic, die naar gebruik wordt gefactureerd.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Er blijft geen betaalde route open, en elke aanroep bewijst dat.** Claude
  Code ontvangt uit uw omgeving alleen een vaste lijst variabelen — geen
  API-sleutel, token, cloudprovider of markering van de Claude Code-sessie
  van waaruit aipmt zou worden gestart. Vóór het eerste segment moet `claude auth status`
  de abonnementsverbinding tonen, zonder Console-sleutel, en moet `/usage`, dat
  geen quotum verbruikt, dit bevestigen; elke aanroep bevestigt dit op zijn beurt in zijn
  initialisatie-event, anders wordt het antwoord geweigerd.
- **Schakel ‘extra usage’ uit** (claude.ai, Instellingen → Gebruik) om
  de kosten op nul euro te houden: als dit is ingeschakeld, neemt het over zodra het quotum van een tijdvenster is opgebruikt en
  worden kosten berekend zonder foutmelding. aipmt stopt de vertaling zodra het
  quotumoverzicht van een aanroep dit meldt, maar die aanroep wordt al meegerekend.
- **Quotum gedeeld met uw Claude Code-sessies.** Elke aanroep rapporteert
  het gebruik binnen het tijdvenster van 5 uur en dat van de week; boven 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) wordt geen volgend segment gestart, om
  het quotum dat u voor uw werk nodig hebt niet uit te putten.
- **Isolatie.** Elke aanroep draait zonder tools, in een besloten
  tijdelijke directory, in een modus zonder personalisatie: uw `CLAUDE.md`, plugins,
  hooks, MCP-servers en instellingen worden niet geladen, en niets van de
  sessie wordt bewaard. Bijlagen zijn uitgeschakeld: een `@chemin` in uw document
  blijft tekst en opent geen bestand (gemeten).
- **Modellen**: standaard `sonnet`, met inspanningsniveau `low`, ook in `--eco`:
  `--eco` verandert niets aan deze route. Gemeten op dezelfde documenten is `haiku`
  twee keer zo traag — het redeneert zonder dat dit kan worden uitgeschakeld — tegen
  nauwelijks lagere kosten, en weigert `opus` biologische inhoud (volgend
  punt). Beide blijven toegankelijk via `--model`; deze aliassen volgen het
  nieuwste model binnen hun familie. `fable` en de varianten `[1m]` worden geweigerd,
  omdat ze betaalde credits gebruiken. `--reasoning_effort` stelt het inspanningsniveau in,
  waar een vertaling niets aan heeft: de gemeten redeneeractiviteit is nul of vrijwel nul.
- **Opus weigert bepaalde biologische inhoud.** Zijn veiligheidsfilters zijn
  strenger dan die van Sonnet, en de foutmelding van Anthropic waarschuwt dat ze
  ‘soms werk kunnen markeren dat aan biologisch onderzoek raakt’. Gemeten: een kort
  nieuwsbericht over 279 gegenereerde moleculen zorgde ervoor dat het artikel in alle veertien
  talen werd geweigerd. Er wordt niets geschreven: aipmt weigert het afgebroken antwoord, benoemt de
  veiligheidsfilters en raadt `--model sonnet` aan.
- Geweigerd in CI (als `CI` of `GITHUB_ACTIONS` is ingesteld) en onder Windows (niet gemeten).
- Variabelen: `AIPMT_CLAUDE_BIN` (anders `PATH`, daarna `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (seconden per segment, standaard 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (standaard 0.8), `CLAUDE_CONFIG_DIR` (het account van
  Claude Code, nooit overgenomen uit een `.env` van een project); werkdirectories onder
  `XDG_CACHE_HOME/aipmt/claude-code` (standaard `~/.cache`).

**Gebruiksvoorwaarden: het is uw account dat wordt gebruikt.** De
[juridische pagina van Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
verbiedt niet dat ‘een eindgebruiker zich met zijn eigen Claude-abonnement aanmeldt bij de ongewijzigde Claude Code-binary’:
dat is wat aipmt doet; het start de
officiële binary en leest het token nooit. Maar Anthropic ‘staat externe
ontwikkelaars […] niet toe om namens hun gebruikers verzoeken via de inloggegevens
van Free-, Pro- of Max-abonnementen te routeren’, geeft voor externe tools de voorkeur aan een API-sleutel,
‘inclusief opensourceprojecten’, en behoudt zich het recht voor om hun
gebruik van betaalde credits af te trekken
([Claude-help](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Geen enkele tekst geeft uitsluitsel over een gedistribueerde tool die de binary start.

**Gegevens**: bij Free-, Pro- en Max-accounts geldt modeltraining
ook voor Claude Code wanneer de privacyinstelling dit toestaat
([gegevenspagina](https://code.claude.com/docs/en/data-usage)). aipmt bewaart
geen lokaal transcript (`--no-session-persistence`). Laat er
geen vertrouwelijke informatie doorheen gaan.

### Naar de provider van uw keuze: `--use_opencode`

[OpenCode](https://opencode.ai) is een opensource-codeagent (MIT) die
verzoeken routeert naar de daarin geconfigureerde providers: API-sleutel, abonnement,
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

`--model` is verplicht: zonder deze optie zou OpenCode terugvallen op een gratis model
waarvan de uitwisselingen voor training kunnen worden gebruikt, en die keuze wordt niet
voor u gemaakt.

Isolatie bij elke aanroep:

- een inline configuratie, die voorrang heeft op de uwe, definieert een agent `aipmt`
  waarvoor alle tools worden geweigerd (`permission: { "*": "deny" }`), sessiedeling
  uitgeschakeld, `--pure`, nooit `--auto`;
- lege tijdelijke werkdirectory, met `OPENCODE_DISABLE_PROJECT_CONFIG` en
  `OPENCODE_DISABLE_CLAUDE_CODE` ingesteld — zonder deze instellingen voegt OpenCode
  `AGENTS.md` uit de huidige directory en `~/.claude/CLAUDE.md` aan de prompt toe. De
  globale `~/.config/opencode/AGENTS.md` wordt nog steeds toegevoegd; OpenCode biedt geen mogelijkheid
  om die uit te sluiten;
- uitvoercontract: exitcode 0, geen `error`-event, geen
  toolaanroep, laatste stap in `stop`, niet-lege tekst, en de agent `aipmt`
  daadwerkelijk geladen — een onbekende `--agent` laat OpenCode niet mislukken; het
  valt stilzwijgend terug op de codeagent;
- geen sleutel van `aipmt` wordt doorgegeven, behalve `OPENCODE_API_KEY`, de sleutel
  van OpenCode zelf. Providers worden in OpenCode geconfigureerd, niet in
  de `.env` van `aipmt`.

Goed om te weten:

- De gratis modellen van Zen wisselen, hebben ongedocumenteerde limieten, en
  hun uitwisselingen kunnen voor training worden gebruikt: geschikt voor openbare
  documentatie, niet voor privé-inhoud.
- Een lokaal model moet minimaal 16 k tokens context bieden, aangezien segmenten
  tot 16 000 tekens bevatten. Ollama configureert vaak 4 096: gebruik
  een `Modelfile` met `PARAMETER num_ctx 32768`.
- `--eco` heeft geen effect; `--reasoning_effort` wordt ongewijzigd doorgegeven als
  `--variant` van OpenCode.
- OpenCode logt elke sessie in `~/.local/share/opencode/`.
- Variabelen: `OPENCODE_BIN` (anders `PATH`, daarna `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (seconden per segment, standaard 600). `OPENCODE_CONFIG`
  wordt ongewijzigd aan OpenCode doorgegeven.

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

`reasoningEffort: "none"` schakelt het redeneren uit dat Ollama standaard voor deze
modellen inschakelt en dat een Modelfile niet kan uitschakelen. Gemeten op een zin van
zes woorden: 919 redeneertokens en 68 seconden zonder de optie, 9 tokens met de optie.

### Naar meer dan 400 modellen: `--use_openrouter`

OpenRouter is een router die naar gebruik factureert, vanuit één tegoed, voor
modellen die door derden worden gehost — waaronder open Chinese modellen die geen
andere provider hier aanbiedt.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` is verplicht. Een preflight, uitgevoerd voordat er kosten worden gemaakt, regelt
twee bijzonderheden van de routering:

- **Hetzelfde model wordt door tientallen hostingproviders met verschillende
  limieten aangeboden** — bij `z-ai/glm-5.3-flash` zijn er 23 hostingproviders, waarvan één met een limiet van
  2 048 uitvoertokens. De preflight leest `/api/v1/models/{modèle}/endpoints`,
  sluit hostingproviders uit met minder dan 8 000 uitvoertokens of een verminderde servicestatus, en
  legt de overige vast met `allow_fallbacks: false`.
- **Redeneren wordt tegen het uitvoertarief gefactureerd** — 107 tokens tegenover 2 voor
  een antwoord ‘OK’ van `z-ai/glm-5.2`. Het is standaard uitgeschakeld; modellen
  die het verplicht stellen, krijgen het laagste inspanningsniveau dat ze accepteren, aangezien de standaardinstelling uit
  de catalogus de uitvoerruimte kan vullen voordat de vertaling is voltooid.
  `--reasoning_effort` blijft voorrang houden.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Het contextvenster komt uit de catalogus. Een model met minder dan 16 400 tokens wordt
  vóór elke aanroep geweigerd: 8 400 voor de prompt en het segment, minimaal 8 000
  voor de uitvoer.
- Een slug die niet in de catalogus staat, een onbereikbare catalogus of het ontbreken
  van een hostingprovider die aan de limiet voldoet, stopt de opdracht.
- `finish_reason=length` met lege uitvoer betekent dat het budget door het
  redeneren is opgebruikt, niet dat de uitvoer is afgekapt: de melding maakt dit onderscheid.
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
gevolgd door een vetgedrukt citaat: leesbaar op GitHub en tijdens de build te verwerken door een
remark-plugin.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Gedetailleerde metingen

Alle metingen zijn daadwerkelijk uitgevoerde vertalingen met `aipmt`, naar
veertien talen: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Geschreven** telt de bestanden die de controles hebben doorgelaten; **Zonder
afwijking** de bestanden waarin `scripts/compare_structure.py` niets vaststelt — hetzelfde aantal
secties, subkoppen, links, verschillende URL's, codeblokken,
inline codefragmenten, tabelrijen, citaatblokken en vetgedrukte woorden.

‘Zonder afwijking’ betekent ‘niets gedetecteerd’, niet ‘identiek’: de vergelijker
telt elementen zonder hun inhoud te lezen. Hij meldt geen verwijderde kop van
niveau 4, vervangen tekst in een inline codefragment, verwisselde vlag
of interne link met een haakje te veel,
`[texte]((#ancre))`, die nergens meer naartoe leidt — en hij beoordeelt de
taal niet.

### Informatiedicht nieuwsartikel, modus `--news`

Een editie van het [AI-nieuwsoverzicht van jls42.org](https://jls42.org/fr/news):
589 regels, 140 links, 21 secties, 3 beschermde Engelse citaten. Meetronde
van 4 en 5 september 2026.

| Model                                           | Toegang            | Geschreven | Zonder afwijking | Mediaan/taal |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google-abonnement  | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google-abonnement  | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `claude-sonnet-5-5`                             | Anthropic API      | 14/14   | ✅ **14/14** | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT-abonnement | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | Claude-abonnement  | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | Claude-abonnement  | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `claude-haiku-5-5`                              | Anthropic API      | 14/14   | ⚠️ 11/14     | 2 min 54 s     |
| `claude-haiku-4-5`                              | Anthropic API      | 14/14   | ⚠️ 7/14      | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | lokaal             | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok-abonnement    | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | Claude-abonnement  | 0/14    | ❌ 0/14      | —              |

Grok is op 9 september opnieuw gemeten op een andere editie van hetzelfde nieuwsoverzicht
(356 regels): 9 van de 14 talen geschreven, 8 zonder afwijking. Dat is het cijfer
dat in de tabel bovenaan staat. Drie afgebroken meetrondes zijn niet
opgenomen: `qwen3.5-27b` (9 talen) en `kimi-k2.6` (4) wegens gebrek aan tegoed,
en `z-ai/glm-5.3-flash`, waarvan de twee mislukkingen voortkwamen uit een redeneerinstelling
die de provider inmiddels corrigeert. De OpenRouter-rijen zijn gemeten met de
standaardinstellingen van de router, vóór `--use_openrouter`; `z-ai/glm-5.2`,
opnieuw gemeten met de meegeleverde provider, behaalt dezelfde 14/14. De cijfers zijn
op 10 september opnieuw berekend met de huidige vergelijker: `qwen3.8-flash` en
`qwen3.7-flash` winnen elk één taal ten opzichte van de eerste
publicatie; de overige zijn ongewijzigd.

De rijen `--use_antigravity` zijn op 26 september gemeten op hetzelfde
artikel, met vier vertalingen parallel: `gemini-3.7-flash-medium` in de ochtend,
`gemini-3.8-flash-medium` in de middag. In het Engels verwijderde elk model zelf
de drie regels Franse vertaling onder de citaten, zonder een
vlag te verzinnen, en de Engelse citaten zijn intact: de opruimroutine als terugvaloptie hoefde
niets te doen. In `--eco` (`gemini-3.7-flash-low`), voor slechts vier
talen (en, ja, ar, hi): 4 van de 4 geschreven, allemaal zonder afwijking, met een
mediaan van 1 min 52 s. Controlemeting op dezelfde dag op een recentere editie van het nieuwsoverzicht,
die van 25 september (438 regels, 2 Engelse citaten), buiten de
blog vertaald door `gemini-3.7-flash-medium`: 14 van de 14 geschreven, allemaal zonder afwijking, 87 tot
128 s per taal.

De rijen `--use_claude_code` zijn op 26 september gemeten op hetzelfde
artikel, met vier vertalingen parallel, op inspanningsniveau `low`. Met `sonnet` zijn de
Engelse citaten in alle veertien talen intact en heeft het
model in het Engels zelf de regels Franse vertaling verwijderd, zonder een
vlag te verzinnen. `opus` heeft geen enkele taal geschreven: bij elke taal stopten zijn
veiligheidsfilters het antwoord bij het laatste segment, vanwege een kort bericht over 279
moleculen die voor een bindingsplaats waren gegenereerd. Afzonderlijk verstuurd wordt dit bericht geweigerd
onder de categorie ‘bio’; `sonnet` heeft het in alle talen vertaald. `haiku` schrijft
alle veertien talen; in drie ervan (en, pl, ro) gaat een sectiekop van
niveau 2 naar niveau 1. Het redeneert zonder dat dit kan worden uitgeschakeld — 61 % van
zijn uitvoertokens —, waardoor het meer dan twee keer zoveel tijd kost als `sonnet`.

De rijen `claude-sonnet-5-5`, `claude-haiku-5-5` en `claude-haiku-4-5` zijn
op 18 oktober gemeten via de API van Anthropic, op hetzelfde artikel, met vier
vertalingen parallel per model. Sonnet 5.5 staat niet toe dat zijn
redeneren wordt uitgeschakeld: aipmt stuurt het de laagste instelling die het accepteert, en zijn
antwoorden bevatten geen redeneerinhoud. Het schrijft alle veertien talen zonder afwijking en zonder
een segment opnieuw te verwerken; in het Engels heeft het zelf de regels
Franse vertaling verwijderd, zonder een vlag te verzinnen, en de Engelse citaten zijn
overal intact. Haiku 5.5 is gemeten met adaptief redeneren: met redeneren
uitgeschakeld liet het hele alinea's in het Frans staan, wat de controle afwijst —
3 van de 14 talen geschreven. Beide Haiku-modellen struikelen over hetzelfde korte bericht: Haiku 5.5
verandert het niveau van de kop of verdubbelt die in het Japans, Koreaans en
Chinees; Haiku 4.5 zet die in zeven talen op niveau 1 en laat die in de
Japanse vertaling in het Frans staan. Haiku 4.5 kost 3,67 $ voor beide documenten in alle
veertien talen, Haiku 5.5 0,57 $, Sonnet 5.5 9,21 $.
### README van dit project, standaard Markdown

Revisie vastgezet op 9 september 2026: 785 regels, 285 inline codes, 40
blokafsluitingen, 89 tabelregels. Vier vertalingen parallel.

| Model                                          | Geschreven | Zonder afwijkingen | Mediaan/taal | Wat afwijkt                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | niets                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | niets                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | niets voor de comparator; interne links verdubbeld (en)                   |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | niets                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | niets                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | één vetgedrukt woord (ja)                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | één vetgedrukt woord (ko)                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | een tabelregel aan de vorige vastgeplakt (ar)                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | één link (sv), één vetgedrukt woord (zh)                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | één vetgedrukt woord (ar, ja)                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | één vetgedrukt woord (hi, ja, ko)                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 40 inline codes toegevoegd in het Arabisch; vetgedrukt (hi, ja, ko)                   |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2 talen geweigerd (ar, hi): inline codes verloren in het antwoord        |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | een sectie verloren (ar, hi, ko); codeblokken toegevoegd (ja, ko, ro, zh) |

Twee afgebroken meetrondes zijn niet beoordeeld: Grok, CLI-sessie verlopen
na twaalf talen (elf zonder afwijkingen), en `qwen3.8-flash`, HTTP 429 van zijn
hostingprovider na twee. `opencode/mimo-v2.5-free` en `ollama/gpt-oss-20b-32k`
zijn niet opnieuw gemeten op deze revisie; op die van 4 en 5 september,
die 277 regels korter was, schreven ze elk 9 vertalingen van de 14, waarvan 7
en 1 zonder afwijkingen.

De rijen `--use_antigravity` en `--use_claude_code` zijn niet gemeten op
de vastgezette revisie, maar op 26 september op de revisie die met 1.14.0 is gepubliceerd — en
de rijen `claude-sonnet-5-5`, `claude-haiku-5-5` en `claude-haiku-4-5` op 18
oktober, op dezelfde revisie: 600 regels, 257 inline codes, 30 blokafsluitingen, 85
tabelregels. Omdat deze
185 regels korter is, kan ze niet één op één met de andere rijen worden vergeleken;
die rijen kunnen onderling wel worden vergeleken. Wat de interne links betreft, die de
comparator niet controleert, heeft `gemini-3.8-flash-medium` ze intact gehouden in
alle veertien talen, terwijl `gemini-3.7-flash-medium` ze in het Italiaans heeft verbroken;
`sonnet` en `opus` hebben ze overal intact gehouden, `haiku` heeft ze verdubbeld in
het Engels; `claude-sonnet-5-5` en `claude-haiku-4-5` hebben ze intact gehouden in
alle veertien talen, `claude-haiku-5-5` in de twaalf die het heeft geschreven.

### Vier README's van bekende projecten

FastAPI, Ollama, tldr-pages en Vue.js, ongewijzigd overgenomen van GitHub — 
documenten die eenvoudiger zijn dan de twee voorgaande. De meetronde richtte zich op de modellen
die moeite hadden; Gemini dient hier als vergelijkingspunt.

| Model                    | Reikwijdte                  | Geschreven | Zonder afwijkingen   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 projecten × 14 talen     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 projecten × 14 talen     | 55/56   | ❌ 47/56     |
| `grok-4.6` (abonnement)   | 4 projecten × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 projecten × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### Wat deze metingen niet zijn

- **Geen uitputtende rangschikking**: alleen al OpenRouter biedt meer dan vierhonderd
  modellen aan; er zijn er ongeveer vijftien gemeten.
- **Indicatieve doorlooptijden**: drie tot zes vertalingen parallel, afhankelijk van
  de meetronde, en de verwerkingssnelheid van een aanbieder varieert gedurende de dag.
- **Gedateerde waarnemingen**: modellen veranderen onder dezelfde naam, en uw
  documenten zijn anders dan de onze.

Om de meting op uw documenten te herhalen, op een vastgezette kopie van het bestand:

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

Beide regels zijn nodig: zonder `pip install -e .` antwoordt `python -m aipmt`
met `No module named aipmt`.

Kwaliteitstools, optioneel maar aanbevolen:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

De 28 vertalingen in de repository (README en CHANGELOG, veertien talen) worden
opnieuw gegenereerd met `./regen_translations.sh --force` — standaard Codex en `gpt-6.1-sol` via
het ChatGPT-abonnement, vier parallel. `REGEN_PROVIDER` en
`REGEN_MODEL` wijzigen de werkwijze: `antigravity` blijft op een abonnement, dat
van Google, en wordt zonder uitzondering toegestaan; een betaalde API (`openai`, `gemini`,
`grok`, `openrouter`) wordt geweigerd zonder `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` begrenst elke job (600 s, 1 800 s op Codex en
Antigravity). De details van de tools staan in `CLAUDE.md`.

## Projecten die dit script gebruiken

- **[jls42.org](https://jls42.org)** — persoonlijke blog gepubliceerd in 15 talen. Het
  [dagelijkse AI-nieuwsoverzicht](https://jls42.org/fr/news) wordt elke dag vertaald
  door deze tool en dient als referentiedocument voor de bovenstaande metingen.

## Auteur

Julien LE SAUX
E-mail: contact@jls42.org

## Licentie

GNU GENERAL PUBLIC LICENSE Version 3. Zie [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Waarschuwing

Dit programma wordt **zonder enige garantie** verspreid, overeenkomstig de
artikelen 15 en 16 van de GPL v3: geleverd « zoals het is », zonder garantie van
verkoopbaarheid of geschiktheid voor een bepaald doel, en de auteur kan niet
aansprakelijk worden gesteld voor schade die voortvloeit uit het gebruik ervan. De tekst van de
licentie heeft voorrang op deze samenvatting.

- **Lees alles na voordat u publiceert.** De beveiligingen dekken codeblokken,
  inline code, URL's, ankers en citaten in de modus `--news` — niet de
  koppen, tabellen, front matter of de betekenis van uw zinnen.
- **Uw documenten worden naar de gekozen aanbieder verzonden**, onder diens
  gebruiksvoorwaarden en gegevensbeleid. Sommige gratis modellen kunnen
  uw gesprekken hergebruiken voor training, en de voorwaarden van Antigravity
  staan Google toe ze te hergebruiken en door mensen te laten nalezen,
  ook bij een betaald abonnement; een lokaal model is de enige optie waarbij
  geen gegevens uw computer verlaten.
- **API-aanroepen worden aan u in rekening gebracht.** Dit programma begrenst de
  uitgaven niet: een lang document, een nieuwe poging na een fout of een model dat veel redeneert
  brengt meer kosten met zich mee.
- **De gepubliceerde metingen zijn gedateerde waarnemingen**, geen garanties.

De genoemde product- en bedrijfsnamen behoren toe aan hun respectieve
eigenaren. Dit project is met geen van hen verbonden.

**Artikel vertaald van het Frans naar het Nederlands met gpt-6.1-sol.**

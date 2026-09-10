# AI-aangedreven Markdown-vertaler

🌍 [Frans](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [Engels](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Spaans](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Chinees](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Duits](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Japans](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Koreaans](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Arabisch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiaans](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Pools](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Portugees](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Roemeens](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Zweeds](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Codekwaliteit</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status van de kwaliteitscontrole"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Beveiligingsbeoordeling"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Betrouwbaarheidsbeoordeling"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Onderhoudbaarheidsbeoordeling"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Dekking"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Kwetsbaarheden"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Gedupliceerde regels (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Technische schuld"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Aantal coderegels"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy-badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Vertaalt Markdown-bestanden van de ene taal naar de andere met behoud van de
structuur: codeblokken, inline code, URL's, anchors, tabellen en front
matter. Negen manieren om een model aan te roepen — vijf API's, twee abonnementen
zonder facturering per gebruik, twee routers — en een gepubliceerde meting van wat elk
model daadwerkelijk behoudt.

## In het kort

- **Negen providerroutes**: API's van OpenAI, Mistral, Claude, Gemini en Grok;
  ChatGPT- (Codex) en Grok-abonnementen zonder facturering per gebruik; routers
  OpenCode (open source, gratis of lokaal) en OpenRouter (meer dan 400 modellen).
- **Geen onjuiste uitvoer door een ontbrekend token**: codeblokken, inline code,
  URL's, anchors en citaten worden vóór de aanroep vervangen door tokens en
  bij terugkeer gecontroleerd. Als er één ontbreekt, wordt het bestand niet geschreven.
- **Lange documenten**: segmentatie op basis van het contextvenster van het model.
- **Modus `--news`**: Engelse citaten worden beschermd en vlaggen worden per
  taal beheerd, voor monitoringartikelen.
- **Modus `--eco`**: snellere en goedkopere modellen.
- Optionele **vertaalnotitie**, bovenaan, onderaan of op beide plaatsen.

## Installatie

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 of nieuwer. Zie voor installatie vanuit de repository
[Bijdragen](#bijdragen).

## Configuratie

De sleutels worden op drie plaatsen ingelezen, van hoogste naar laagste prioriteit; elke plaats
vult alleen in wat de voorgaande leeg heeft gelaten.

|     | Waar                                          | Waarvoor                                  |
| --- | --------------------------------------------- | ----------------------------------------- |
| 1   | Omgevingsvariabelen                           | CI, containers, eenmalige uitzondering    |
| 2   | `.env` van de huidige map (of een bovenliggende map) | een projectspecifieke sleutel              |
| 3   | `~/.config/aipmt/.env`                        | eenmaal geïnstalleerd, overal geldig       |

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
onder Windows. Zonder sleutel vermeldt de opdracht de drie locaties.

**De `.env` van een project kan aanroepen niet omleiden.** Het bestand levert sleutels,
nooit een bestemming: alle variabelen in `_BASE_URL`, `_API_BASE` of
`_ENDPOINT`, proxies (`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`),
certificaatopslagplaatsen (`SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`,
`CURL_CA_BUNDLE`) en `XDG_CONFIG_HOME` / `APPDATA` worden daarin genegeerd, met een
waarschuwing. Een gekloonde repository mag uw sleutel niet kunnen omleiden. Dit
bestand wordt ook zonder interpolatie gelezen: `NOM=${OPENAI_API_KEY}` neemt de sleutel
daarin niet over. Stel deze variabelen in de omgeving of in
`~/.config/aipmt/.env` in.

Optionele variabelen: `XAI_BASE_URL` (standaard `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (seconden per aanroep, standaard 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(standaard 600), `GROK_BIN`, `GROK_HOME` (standaard `~/.grok`), `GROK_TIMEOUT`
(standaard 900), `GROK_TRANSLATE_SANDBOX`, `OPENCODE_BIN`, `OPENCODE_TIMEOUT`
(standaard 600), `OPENROUTER_BASE_URL` (`https://` vereist), `OPENROUTER_TIMEOUT`
(standaard 900), `OPENROUTER_PREFLIGHT_TIMEOUT` (standaard 30). Elke variabele wordt nader toegelicht
in de sectie van de betreffende provider.

## Aan de slag

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` vertaalt naar het Spaans en levert `document-es.md` op in `--target_dir`;
met `--include_model`, `document-es-gpt-5.6-terra.md`. De extensie wordt
altijd `.md` — `article.mdx` levert `article-en.md` op — behalve met
`--keep_filename`, waarmee de oorspronkelijke naam behouden blijft. Een reeds aanwezige
vertaling wordt zonder `--force` overgeslagen.

Exitcodes: `0` als alles is voltooid of overgeslagen, `1` als er nog een mislukt
bestand overblijft (vermeld in de foutuitvoer), `2` als de configuratie het probleem vormt.
Een mislukt bestand wordt nooit geschreven, zelfs niet als het schrijven zelf mislukt:
de inhoud wordt ernaast geschreven en vervolgens hernoemd. Opnieuw uitvoeren volstaat.

## Welk model kiezen

Gemeten op twee echte documenten, die door elk model naar dezelfde veertien talen
zijn vertaald. **Het getal is het aantal talen, van de veertien, waarvoor de
vertaling wordt geschreven en niets afwijkt van de bron.**

| Model                | Toegangsmethode                    | Dicht monitoringartikel | Deze README   | Wat afwijkt en in hoeveel talen                                                                                                       |
| -------------------- | --------------------------------- | ----------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | Google API-sleutel                | ✅ 14/14                | ⚠️ 13/14      | 1 van de 14 talen: één extra vetgedrukt woord (ja)                                                                                     |
| **GPT-5.6 Sol**      | ChatGPT-abonnement of OpenAI-sleutel | ✅ 14/14             | ⚠️ 12/14      | 2 van de 14 talen: één vetgedrukt woord minder (ar, ja)                                                                                |
| **GLM-5.2**          | OpenRouter-sleutel                | ✅ 14/14                | ⚠️ 11/14      | 3 van de 14 talen: één vetgedrukt woord minder (hi, ja, ko)                                                                            |
| Claude Sonnet 5      | Anthropic API-sleutel             | ⚠️ 11/14                | ⚠️ 12/14      | 3 talen in het artikel: een codeblok is verschenen (es, de, hi); 2 in deze README: een link zonder mark-up (sv), een vetgedrukt woord (zh) |
| Qwen 3.7 Flash       | OpenRouter-sleutel                | ❌ 8/14                 | ⚠️ 10/14      | 1 taal geweigerd voor het artikel, 5 andere wijken af; in deze README zijn ongeveer veertig woorden in `code` geplaatst (ar)   |
| Grok 4.6             | Grok-abonnement                   | ❌ 8/14                 | niet beoordeeld | 5 van de 14 talen geweigerd wegens ontbrekende inline code en URL's; het Nederlands wijkt overal af                                   |
| GPT-OSS 20B          | lokaal model (Ollama)             | ❌ 7/14                 | niet opnieuw gemeten | 4 van de 14 talen geweigerd: het model liet daarin Franse passages staan, waarna de beveiliging ze heeft tegengehouden            |
| MiMo v2.5 (gratis)   | OpenCode Zen, zonder account      | ❌ 11/14                | niet opnieuw gemeten | 1 taal geweigerd; een sectie ontbreekt in het Pools                                                                               |
| Mistral Large        | Mistral API-sleutel               | ❌ 5/14                 | ❌ 1/14       | **een volledige sectie verdwijnt**: 1 taal in het artikel (hi), 3 in deze README (ar, hi, ko) — en 3 talen geweigerd voor het artikel  |
| DeepSeek V4 Flash    | OpenRouter-sleutel                | ❌ 3/14                 | niet opnieuw gemeten | 10 van de 14 talen geweigerd; 37 minuten per taal                                                                                 |

|     | Betekenis van het symbool                                                                                                                                                                             |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alle veertien talen vertaald en niets wijkt af van de bron                                                                                                                                             |
| ⚠️  | alle veertien talen vertaald; wat afwijkt is **mark-up** — een vetgedrukt woord, een `code`, een link die zijn vierkante haken verliest. Er ontbreekt geen tekst, URL, codeblok of sectie |
| ❌  | ten minste één taal kon niet worden vertaald — het bestand wordt geweigerd en niet geschreven — **of** er ontbreekt inhoud in een geschreven bestand                                                  |

Wat u hiervan moet onthouden:

- **Een geweigerde vertaling is geen beschadigde vertaling.** Wanneer bij terugkeer een token
  ontbreekt, wordt het bestand niet geschreven en telt de taal als
  geweigerd. Dat gebeurt met Grok bij het artikel: vier stukken inline code en
  drie URL's gaan al in het eerste segment verloren, bij de vijf niet-Latijnse schriften.
- **Dit vangnet dekt geen koppen, tabellen, front matter of
  tekst.** Een model dat een sectie verwijdert, levert een bestand op dat de tool
  zonder bezwaar schrijft — dat is het geval bij Mistral. Deze elementen kunnen niet
  door een token worden vervangen en worden door de huidige controles niet gecontroleerd;
  `scripts/compare_structure.py` detecteert een ontbrekende sectie, maar pas achteraf.
- **Grok heeft geen beoordeling voor deze README**: de CLI-sessie verliep na twaalf
  talen, waarvan er elf geen afwijking vertoonden. Een onderbroken testcampagne krijgt geen beoordeling.
- **De dichtheid van het document is belangrijker dan de taal.** Grok houdt stand bij gewone
  README-bestanden, maar haakt af bij een artikel vol links, ook in het
  Nederlands.

Datums en documenten: de kolom ‘Deze README’ is op 9 september 2026
gemeten op een vastgezette revisie van dit bestand (785 regels, 285 stukken inline code, 89
tabelregels), die sindsdien is bijgewerkt. De kolom ‘Dicht monitoringartikel’ komt uit
de testcampagne van 4 en 5 september op een artikel van 589 regels, behalve de rij
voor Grok, die op 9 september opnieuw is gemeten met een andere editie van hetzelfde monitoringartikel. De
volledige tabellen, doorlooptijden en het protocol staan in
[Gedetailleerde metingen](#gedetailleerde-metingen).

## Alle opties

| Optie                    | Beschrijving                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`           | Eén Markdown-bestand om te vertalen (alternatief voor `--source_dir`)                                         |
| `--source_dir`           | Bronmap met Markdown-bestanden (standaard: `content/posts`)                                                     |
| `--target_dir`           | Uitvoermap voor de vertaalde bestanden (standaard: `traductions_en`)                                            |
| `--source_lang`           | Brontaal (standaard: `fr`)                                                                          |
| `--target_lang`           | Doeltaal (standaard: `en`)                                                                          |
| `--model`           | Specifiek te gebruiken model                                                                                  |
| `--eco`           | De voordelige modellen gebruiken                                                                              |
| `--use_mistral`           | De Mistral AI API gebruiken                                                                                   |
| `--use_claude`           | De Claude API gebruiken                                                                                       |
| `--use_gemini`           | De Gemini API gebruiken                                                                                       |
| `--use_grok`           | De xAI API (Grok) gebruiken — vereist `XAI_API_KEY`                                                          |
| `--use_codex`           | De Codex CLI gebruiken met het quotum van het ChatGPT-abonnement                                              |
| `--use_grok_cli`           | De Grok CLI gebruiken met het quotum van het Grok-abonnement                                                  |
| `--use_opencode`           | OpenCode (open source) gebruiken met de in OpenCode geconfigureerde provider; vereist `--model provider/modèle`          |
| `--use_openrouter`           | OpenRouter gebruiken — vereist `OPENROUTER_API_KEY` en `--model fournisseur/modèle`                                               |
| `--force`           | Opnieuw vertalen afdwingen                                                                                    |
| `--keep_filename`           | De oorspronkelijke bestandsnaam behouden                                                                      |
| `--news`           | Nieuwsmodus: beschermt Engelse citaten en beheert vlaggen per taal                                             |
| `--add_translation_note`           | Een vertaalnotitie toevoegen                                                                                  |
| `--note_position`           | Positie van de notitie: `top`, `bottom` (standaard) of `both`                          |
| `--note_format`           | Indeling van de notitie: `legacy` (standaard, vetgedrukte alinea) of `marker`                     |
| `--include_model`           | De modelnaam opnemen in het uitvoerbestand                                                                    |
| `--reasoning_effort`           | Redeneerinspanning van GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`    |

De acht flags `--use_*` sluiten elkaar uit: een combinatie van twee wordt
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

| Provider   | Kwaliteit (standaard)                                | Voordelig (`--eco`) |
| ---------- | ----------------------------------------------------- | --------------------------- |
| OpenAI     | `gpt-5.6-terra`                                       | `gpt-5.6-luna`             |
| Claude     | `claude-sonnet-5`                                       | `claude-haiku-4-5`             |
| Mistral    | `mistral-large-latest`                                       | `mistral-small-latest`             |
| Gemini     | `gemini-3.7-flash`                                       | `gemini-3.1-flash-lite`             |
| Codex      | `gpt-5.6-sol` (ook `terra` en `luna` via `--model`) | `gpt-5.6-luna` |
| Grok API   | `grok-4.6`                                       | `grok-4.3`             |
| Grok CLI   | `grok-4.6`                                       | `grok-4.5`             |
| OpenCode   | `--model provider/modèle` verplicht                             | idem — `--eco` zonder effect |
| OpenRouter | `--model fournisseur/modèle` verplicht                             | idem — `--eco` zonder effect |
### Via het ChatGPT-abonnement: `--use_codex`

Stuurt de officiële Codex CLI aan: de vertaling wordt afgetrokken van het quotum van
het ChatGPT-abonnement, zonder API-sleutel of facturering per gebruik.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Het binaire bestand wordt gezocht in `CODEX_BIN`, daarna in `PATH` en vervolgens in het package
  `openai-codex-cli-bin`. `~/.codex/auth.json` wordt nooit gelezen.
- `OPENAI_API_KEY` en `CODEX_API_KEY` worden uit de omgeving van het
  subproces verwijderd: een aanwezige sleutel schakelt nooit over naar de API.
- Elk segment kost minstens één ‘bericht’ uit het venster van 5 uur — twee
  als de validatie mislukt en het opnieuw wordt geprobeerd. OpenAI noemt als
  schatting 250-2.000 berichten/5 u voor `gpt-5.6-luna` (`--eco`) en
  10-100 voor `gpt-5.6-sol` met een Plus-abonnement.
- `--model gpt-5.6-terra` en `--model gpt-5.6-luna` lopen eveneens via
  het abonnement. Een model waartoe het account geen toegang heeft, geeft een 400-foutmelding: ‘model is
  not supported when using Codex with a ChatGPT account’.
- Langzamer dan een API, waarbij het verschil toeneemt met de grootte van het document: voor deze README
  bedraagt de mediaan per taal 6 min 46 s met `gpt-5.6-sol`, tegenover 36 s met
  `gemini-3.7-flash`.
- Geweigerd in CI (als `CI` of `GITHUB_ACTIONS` is ingesteld): het abonnement gebruikt voor authenticatie
  een persoonlijk sessiebestand, dat niet op een gedeelde runner thuishoort.
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
  niet op veel recente Linux-systemen (AppArmor, sockets van de
  container-runtime), en een profiel dat niet kan worden toegepast, start ongemerkt zonder
  isolatie. Het script vraagt daarom standaard geen profiel aan, meldt dit en
  vertrouwt op de `--deny`-regels van de CLI, waaronder de catch-all `*` — de enige
  laag die weigert te starten in plaats van de bescherming stilzwijgend te
  verwijderen. `GROK_TRANSLATE_SANDBOX=read-only` vereist de OS-sandbox en het opstarten
  mislukt als de machine daaraan niet kan voldoen.
- Het quotum is wekelijks, wordt gedeeld met Chat, Imagine en Voice, en kan met geen
  enkele opdracht worden uitgelezen: een batch kan zonder waarschuwing ten koste gaan van
  het gebruik voor gesprekken.
- Variabelen: `GROK_BIN`, `GROK_HOME` (CLI-map, standaard `~/.grok`),
  `GROK_TIMEOUT` (standaard 900), `GROK_TRANSLATE_SANDBOX`.

### Naar een provider naar keuze: `--use_opencode`

[OpenCode](https://opencode.ai) is een open-source code-agent (MIT) die
verzoeken doorstuurt naar de daarin geconfigureerde providers: API-sleutel, abonnement,
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

`--model` is verplicht: zonder deze instelling zou OpenCode terugvallen op een gratis model
waarvan de interacties voor training kunnen worden gebruikt, en die keuze wordt niet
namens u gemaakt.

Isolatie bij elke aanroep:

- een inline configuratie, die voorrang heeft op die van u, definieert een agent `aipmt`
  waarvoor alle tools worden geweigerd (`permission: { "*": "deny" }`), het delen van
  sessies is uitgeschakeld, `--pure`, nooit `--auto`;
- een tijdelijke, lege werkmap, met `OPENCODE_DISABLE_PROJECT_CONFIG` en
  `OPENCODE_DISABLE_CLAUDE_CODE` ingesteld — zonder deze variabelen voegt OpenCode de
  `AGENTS.md` van de huidige map en `~/.claude/CLAUDE.md` aan de prompt toe. De
  globale `~/.config/opencode/AGENTS.md` blijft toegevoegd; OpenCode biedt geen
  mogelijkheid om deze uit te sluiten;
- uitvoercontract: exitcode 0, geen `error`-event, geen aanroep
  van tools, laatste stap in `stop`, niet-lege tekst en de agent `aipmt`
  daadwerkelijk geladen — bij een onbekende `--agent` geeft OpenCode geen fout,
  maar valt het ongemerkt terug op de codeeragent;
- er wordt geen `aipmt`-sleutel doorgegeven, behalve `OPENCODE_API_KEY`, de sleutel
  van OpenCode zelf. Providers worden in OpenCode geconfigureerd, niet in
  de `.env` van `aipmt`.

Goed om te weten:

- De gratis Zen-modellen veranderen geregeld, hebben ongedocumenteerde limieten en
  hun interacties kunnen voor training worden gebruikt: geschikt voor openbare
  documentatie, niet voor privé-inhoud.
- Een lokaal model moet een context van minstens 16k tokens bieden, aangezien segmenten
  maximaal 16.000 tekens bevatten. Ollama configureert vaak 4.096: gebruik
  een `Modelfile` met `PARAMETER num_ctx 32768`.
- `--eco` heeft geen effect; `--reasoning_effort` wordt ongewijzigd doorgegeven als
  `--variant` van OpenCode.
- OpenCode registreert elke sessie in `~/.local/share/opencode/`.
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

`reasoningEffort: "none"` schakelt de redeneermodus uit die Ollama standaard voor deze
modellen activeert en die niet via een Modelfile kan worden uitgeschakeld. Gemeten met een zin van
zes woorden: 919 redeneertokens en 68 seconden zonder de optie, 9 tokens met de optie.

### Naar meer dan 400 modellen: `--use_openrouter`

OpenRouter is een router met facturering per gebruik, vanuit één tegoed, voor
modellen die door derden worden gehost — waaronder open Chinese modellen die geen
enkele andere provider hier aanbiedt.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` is verplicht. Een preflight, uitgevoerd voordat er kosten worden gemaakt, behandelt
twee bijzonderheden van de routering:

- **Hetzelfde model wordt aangeboden door tientallen hostingproviders met
  verschillende limieten** — voor `z-ai/glm-5.3-flash` zijn dat 23 providers, waarvan één is beperkt tot
  2.048 uitvoertokens. De preflight leest `/api/v1/models/{modèle}/endpoints`,
  sluit providers met minder dan 8.000 uitvoertokens of met een verminderde status uit en
  legt de overige vast met `allow_fallbacks: false`.
- **Redeneren wordt tegen het uitvoertarief gefactureerd** — 107 tokens tegenover 2 voor
  een ‘OK’-antwoord van `z-ai/glm-5.2`. Het is standaard uitgeschakeld; modellen
  die het verplichten, krijgen de laagste inspanning die ze accepteren, omdat de standaardinstelling van
  de catalogus de uitvoer al vóór het einde van de vertaling kan vullen.
  `--reasoning_effort` behoudt voorrang.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Het contextvenster komt uit de catalogus. Een model met minder dan 16.400 tokens wordt
  vóór elke aanroep geweigerd: 8.400 voor de prompt en het segment, minimaal 8.000 voor de uitvoer.
- Een slug die niet in de catalogus staat, een onbereikbare catalogus of het ontbreken
  van een provider die aan de limiet voldoet, breekt de opdracht af.
- `finish_reason=length` met lege uitvoer betekent dat het budget door het
  redeneren is verbruikt, niet dat de uitvoer is afgekapt: de melding maakt dit onderscheid.
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
gevolgd door een vetgedrukt citaat: leesbaar op GitHub en tijdens het buildproces te verwerken door een
remark-plugin.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Gedetailleerde metingen

Alle metingen betreffen daadwerkelijk met `aipmt` uitgevoerde vertalingen naar
veertien talen: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Geschreven** telt de bestanden die door de controles zijn toegelaten; **Zonder
afwijking** de bestanden waarin `scripts/compare_structure.py` niets vaststelt — hetzelfde aantal
secties, tussenkoppen, links, unieke URL's, codeblokken,
inline code, tabelregels, citaatblokken en vetgedrukte woorden.

‘Zonder afwijking’ betekent ‘niets gedetecteerd’, niet ‘identiek’: de vergelijker
telt elementen zonder hun inhoud te lezen. Hij signaleert noch een verwijderde
kop van niveau 4, noch vervangen tekst in inline code, noch een verwisselde
vlag, en beoordeelt de taal niet.

### Dicht overzichtsartikel, modus `--news`

Een editie van het [AI-overzicht van jls42.org](https://jls42.org/fr/news):
589 regels, 140 links, 21 secties, 3 beschermde Engelse citaten. Campagne
van 4 en 5 september 2026.

| Model                             | Toegang            | Geschreven | Zonder afwijking | Mediaan/taal |
| --------------------------------- | ------------------ | ---------- | ---------------- | ------------ |
| `gemini-3.7-flash`                | Google API         | 14/14      | ✅ **14/14**      | 1 min 18 s   |
| `gpt-5.6-sol` (`--use_codex`)     | ChatGPT-abonnement | 14/14      | ✅ **14/14**      | 11 min 28 s  |
| `z-ai/glm-5.2`                    | OpenRouter         | 14/14      | ✅ **14/14**      | 5 min 37 s   |
| `qwen/qwen3.8-flash`              | OpenRouter         | 14/14      | ✅ **14/14**      | 26 min 23 s  |
| `claude-sonnet-5`                 | Anthropic API      | 14/14      | ⚠️ 11/14          | 6 min 31 s   |
| `opencode/mimo-v2.5-free`         | OpenCode Zen       | 13/14      | ❌ 11/14          | 9 min 27 s   |
| `qwen/qwen3.7-flash`              | OpenRouter         | 13/14      | ❌ 8/14           | 10 min 09 s  |
| `ollama/gpt-oss-20b-32k`          | lokaal             | 10/14      | ❌ 7/14           | 12 min 39 s  |
| `mistral-large-latest`            | Mistral API        | 11/14      | ❌ 5/14           | 5 min 32 s   |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter         | 4/14       | ❌ 3/14           | 37 min 27 s  |
| `grok-4.6` (`--use_grok_cli`)     | Grok-abonnement    | 1/14       | ❌ 1/14           | 23 min 11 s  |

Grok is op 9 september opnieuw gemeten met een andere editie van hetzelfde overzicht
(356 regels): 9 van de 14 talen geschreven, waarvan 8 zonder afwijking. Dat cijfer
staat in de overzichtstabel. Drie afgebroken campagnes zijn niet
opgenomen: `qwen3.5-27b` (9 talen) en `kimi-k2.6` (4) wegens onvoldoende tegoed,
en `z-ai/glm-5.3-flash`, waarvan beide mislukkingen werden veroorzaakt door een instelling voor redeneren
die de provider inmiddels corrigeert. De OpenRouter-regels zijn gemeten met de
standaardinstellingen van de router, vóór `--use_openrouter`; `z-ai/glm-5.2`,
opnieuw gemeten met de meegeleverde provider, levert dezelfde 14/14 op. De cijfers zijn
op 10 september opnieuw berekend met de huidige vergelijker: `qwen3.8-flash` en
`qwen3.7-flash` winnen elk één taal ten opzichte van de eerste
publicatie; de overige zijn ongewijzigd.

### README van dit project, standaard-Markdown

Vastgelegde revisie van 9 september 2026: 785 regels, 285 inline codes, 40
afsluitingen van blokken, 89 tabelregels. Vier vertalingen parallel.

| Model                         | Geschreven | Zonder afwijking | Mediaan/taal | Wat afwijkt                                                               |
| ----------------------------- | ---------- | ---------------- | ------------ | ------------------------------------------------------------------------- |
| `gemini-3.7-flash`            | 14/14      | ⚠️ 13/14          | 36 s         | één vetgedrukt woord (ja)                                                 |
| `claude-sonnet-5`             | 14/14      | ⚠️ 12/14          | 2 min 56 s   | één link (sv), één vetgedrukt woord (zh)                                  |
| `gpt-5.6-sol` (`--use_codex`) | 14/14      | ⚠️ 12/14          | 6 min 46 s   | één vetgedrukt woord (ar, ja)                                             |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14      | ⚠️ 11/14          | 2 min 34 s   | één vetgedrukt woord (hi, ja, ko)                                         |
| `qwen/qwen3.7-flash`          | 14/14      | ⚠️ 10/14          | 2 min 17 s   | 40 inline codes toegevoegd in het Arabisch; vetdruk (hi, ja, ko)          |
| `mistral-large-latest`        | 14/14      | ❌ 1/14           | 2 min 44 s   | één sectie verloren (ar, hi, ko); codeblokken toegevoegd (ja, ko, ro, zh) |

Twee afgebroken campagnes zijn niet opgenomen: Grok, waarvan de CLI-sessie
na twaalf talen verliep (elf zonder afwijking), en `qwen3.8-flash`, met HTTP 429 van zijn
hostingprovider na twee talen. `opencode/mimo-v2.5-free` en `ollama/gpt-oss-20b-32k`
zijn niet opnieuw gemeten op deze revisie; op die van 4 en 5 september,
die 277 regels korter was, schreven ze elk 9 van de 14 vertalingen, waarvan
respectievelijk 7 en 1 zonder afwijking.

### Vier README's van bekende projecten

FastAPI, Ollama, tldr-pages en Vue.js, ongewijzigd overgenomen van GitHub —
documenten die eenvoudiger zijn dan de twee voorgaande. De campagne was gericht op de modellen
die moeite hadden; Gemini dient daarbij als vergelijkingspunt.

| Model                     | Bereik                     | Geschreven | Zonder afwijking |
| ------------------------- | -------------------------- | ---------- | ---------------- |
| `gemini-3.7-flash`        | 4 projecten × 14 talen     | 56/56      | ✅ **55/56**      |
| `opencode/mimo-v2.5-free` | 4 projecten × 14 talen     | 55/56      | ❌ 47/56          |
| `grok-4.6` (abonnement)   | 4 projecten × ar, hi, ja, zh | 16/16      | ❌ 14/16          |
| `ollama/gpt-oss-20b-32k`  | 4 projecten × ar, hi, ja, zh | 15/16      | ❌ 9/16           |

### Wat deze metingen niet zijn

- **Geen volledige rangschikking**: alleen OpenRouter biedt al meer dan vierhonderd
  modellen; ongeveer vijftien daarvan zijn gemeten.
- **Indicatieve tijdsduren**: afhankelijk van de campagne liepen drie tot zes vertalingen
  parallel, en de doorvoersnelheid van een provider varieert gedurende de dag.
- **Tijdgebonden waarnemingen**: modellen veranderen onder dezelfde naam, en uw
  documenten zijn niet de onze.

Om de meting opnieuw uit te voeren op uw documenten, met een vastgelegde kopie van het bestand:

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

De 28 vertalingen van de repository (README en CHANGELOG, veertien talen) worden
opnieuw gegenereerd met `./regen_translations.sh --force` — standaard Codex en `gpt-5.6-sol` via
het ChatGPT-abonnement, vier parallel. `REGEN_PROVIDER` en
`REGEN_MODEL` wijzigen het pad; een betaalde API (`openai`, `gemini`,
`grok`, `openrouter`) wordt geweigerd zonder `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` begrenst elke job (600 s, 1.800 s voor Codex). De details
van de tooling staan in `CLAUDE.md`.

## Projecten die dit script gebruiken

- **[jls42.org](https://jls42.org)** — persoonlijke blog die in 15 talen wordt gepubliceerd. Het
  [dagelijkse AI-overzicht](https://jls42.org/fr/news) wordt elke dag
  door deze tool vertaald en dient als referentiedocument voor de bovenstaande metingen.

## Auteur

Julien LE SAUX
E-mail: contact@jls42.org

## Licentie

GNU GENERAL PUBLIC LICENSE Version 3. Zie [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Waarschuwing

Dit programma wordt verspreid **zonder enige garantie**, overeenkomstig
secties 15 en 16 van de GPL v3: geleverd ‘zoals het is’, zonder garantie van
verhandelbaarheid of geschiktheid voor een bepaald doel, en de auteur kan niet
aansprakelijk worden gesteld voor schade die voortvloeit uit het gebruik ervan. De tekst van de
licentie heeft voorrang op deze samenvatting.

- **Lees alles na voordat u publiceert.** De beschermingen gelden voor codeblokken,
  inline code, URL's, ankers en citaten in de modus `--news` — niet voor
  koppen, tabellen, front matter of de betekenis van uw zinnen.
- **Uw documenten worden naar de gekozen provider verzonden**, onder diens
  gebruiksvoorwaarden en gegevensbeleid. Sommige gratis modellen kunnen
  uw interacties hergebruiken voor training; een lokaal model is de enige
  manier waarop geen gegevens uw machine verlaten.
- **API-aanroepen worden aan u gefactureerd.** Dit programma begrenst de
  uitgaven niet: een lang document, een hervatting na een fout of een model dat veel redeneert,
  kost meer.
- **De gepubliceerde metingen zijn tijdgebonden waarnemingen**, geen garanties.

De vermelde product- en bedrijfsnamen behoren toe aan hun respectieve
eigenaren. Dit project is niet aan een van hen gelieerd.

**Artikel vertaald van het Frans naar het Nederlands met gpt-5.6-sol.**

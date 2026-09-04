# AI-aangedreven Markdown-vertaler

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Codekwaliteit</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status van Quality Gate"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Beveiligingsclassificatie"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Betrouwbaarheidsclassificatie"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Onderhoudbaarheidsclassificatie"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Dekking"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Kwetsbaarheden"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Codegeuren"></a>
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

Bestanden in Markdown vertalen met **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** en **Grok (xAI)** — via API, met het quotum van een ChatGPT-abonnement (Codex) of Grok zonder gebruiksafhankelijke facturering, of via **OpenCode**, de open source-agent, naar de provider van uw keuze: lokaal model (Ollama), gratis, abonnement (GitHub Copilot…) of sleutel.

Dit Python-script vertaalt Markdown-bestanden van een brontaal naar een doeltaal en behoudt daarbij de opmaak, codeblokken en front-mattermetadata.

## Belangrijkste kenmerken

- **Multi-provider**: 5 API's (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLI's op abonnementsbasis, zonder gebruiksafhankelijke facturering — Codex (ChatGPT) en Grok — + OpenCode (open source, MIT) naar elke provider die in OpenCode is geconfigureerd, inclusief een lokaal model
- **Modellen 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Economische modus**: Optie `--eco` om snellere en goedkopere modellen te gebruiken
- **Eén bestand**: Optie `--file` om één bestand te vertalen
- **Intelligente segmentatie**: Verwerking van lange teksten met tokenlimieten per model
- **Codebehoud**: Codeblokken EN inline code (`` `...` ``) worden behouden
- **Bestandsnaam**: Optie `--keep_filename` om de oorspronkelijke naam te behouden
- **Nieuwsmodus**: Optie `--news` om Engelse citaten te beschermen en vlaggen in nieuwsartikelen te verwerken
- **.env-configuratie**: Ondersteuning voor het bestand `.env` voor API-sleutels
- **Vertaalnotitie**: Optioneel een notitie aan het einde van het document toevoegen

## Installatie

### De tool gebruiken

```bash
pip install ai-powered-markdown-translator
```

De opdracht `aipmt` is dan overal beschikbaar. Als de map met Python-scripts niet in uw `PATH` staat, doet `python -m aipmt` precies hetzelfde. Python 3.10 of nieuwer.

Voor een installatie die geïsoleerd blijft van uw andere pakketten:

```bash
pipx install ai-powered-markdown-translator
```

### Bijdragen aan het project

De gekloonde repository blijft nodig voor ontwikkeling: daar staan de tests,
de 28 vertalingen en alle kwaliteitscontroles.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` is een **volledig vastgezette lockfile**, een exacte afspiegeling van de geteste omgeving. De grenzen die in `pyproject.toml` zijn gepubliceerd, zijn bewust ruimer: ze leggen niets op aan uw andere pakketten.

### Kwaliteitscontroles (optioneel maar aanbevolen)

Het project gebruikt [`pre-commit`](https://pre-commit.com) om te voorkomen dat slecht geformatteerde of kwetsbare code, of code die een geheim bevat, wordt gecommit. Installatie:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Actieve hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexiteit), detect-secrets (API-sleutels), mypy (geleidelijke typecontrole), Opengrep (SAST), pip-audit (CVE-afhankelijkheden), unittest. Zie de sectie _Quality / pre-commit_ in `CLAUDE.md` voor details.

## Configuratie

De sleutels worden op **drie plaatsen** gezocht, van meest naar minst belangrijk.
Elke plaats vult alleen aan wat de vorige leeg laat.

|     | Waar                                         | Waarvoor                            |
| --- | -------------------------------------------- | ------------------------------------ |
| 1   | Omgevingsvariabelen                          | CI, containers, eenmalige afwijking  |
| 2   | `.env` van de huidige map (of een bovenliggende map) | een sleutel die specifiek is voor een project |
| 3   | `~/.config/aipmt/.env`                         | **eenmalig geïnstalleerd, overal geldig** |

Na een `pip install` is de derde optie het eenvoudigst:

```bash
mkdir -p ~/.config/aipmt
cat > ~/.config/aipmt/.env <<'EOF'
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google
EOF
chmod 600 ~/.config/aipmt/.env
```

Dit bestand volgt `XDG_CONFIG_HOME` wanneer de variabele een absoluut pad bevat (anders wordt het genegeerd, zoals voorgeschreven door de specificatie), en `%APPDATA%` op Windows.

De tweede optie blijft nuttig wanneer een repository een eigen sleutel heeft: een `.env` in de hoofdmap heeft dan voorrang op de gebruikersconfiguratie, zonder die te wijzigen. En een variabele die al in de omgeving is gedefinieerd, heeft voorrang op beide:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Als er geen sleutel wordt gevonden, toont de opdracht geen aanroeplog: ze vermeldt de drie locaties met hun exacte pad.

`GEMINI_API_KEY` wordt geaccepteerd als alternatief voor `GOOGLE_API_KEY` (AI Studio-conventie). Optionele variabelen: `XAI_BASE_URL` (xAI-endpoint, standaard `https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (seconden per Anthropic-aanroep, standaard 900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`, `GROK_TRANSLATE_SANDBOX` (zie de sectie Grok CLI) en `OPENCODE_BIN` / `OPENCODE_TIMEOUT` (zie de sectie OpenCode). Voor `regen_translations.sh`: `REGEN_PROVIDER`, `REGEN_MODEL` en `REGEN_JOB_TIMEOUT` (limiet per taak, standaard 600 s).

## Gebruik

### Eén bestand vertalen

```bash
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Een map vertalen

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
aipmt --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
aipmt --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
aipmt --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
aipmt --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
aipmt --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
aipmt --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
aipmt --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### Vertalen met het ChatGPT-abonnement (`--use_codex`)

Deze provider gebruikt geen API-sleutel: hij bestuurt de officiële Codex CLI in niet-interactieve modus, zodat de vertaling wordt afgetrokken van het quotum van het reeds betaalde ChatGPT-abonnement (Plus, Pro, Business…). Dit is de enige door OpenAI gedocumenteerde manier voor dit gebruik — de tokens van `~/.codex/auth.json` authenticeren geen aanroepen naar de Platform-API en worden bovendien nooit door dit script gelezen.

**Vereisten:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Het binaire bestand wordt in deze volgorde gezocht: de variabele `CODEX_BIN`, de `PATH`, en vervolgens het Python-pakket `openai-codex-cli-bin`. Dit laatste maakt bewust geen deel uit van `requirements.txt`: het is ongeveer 250 MB groot, wat aan alle gebruikers zou worden opgelegd voor een optionele provider.

**Goed om te weten:**

- **Er wordt geen API-sleutel gebruikt.** `OPENAI_API_KEY` en `CODEX_API_KEY` worden uit de omgeving van het subprocess verwijderd, zodat een sleutel in `.env` de vertaling nooit kan laten overschakelen naar gebruiksafhankelijke facturering.
- **Eén segment = één ‘lokaal bericht’** van het venster van 5 uur van het abonnement. Gebruik `--eco` (model `gpt-5.6-luna`, 250–2.000 berichten/5 uur op Plus) in plaats van het kwaliteitsmodel (`gpt-5.6-sol`, 10–100 berichten/5 uur).
- **Trager** dan een API-aanroep: reken op ongeveer 45 s voor een volledige README, tegenover enkele seconden rechtstreeks.
- **Geweigerd in CI** (`CI` of `GITHUB_ACTIONS` gedefinieerd): authenticatie via een abonnement is niet bedoeld voor een gedeelde runner, en OpenAI raadt deze workflow op openbare repositories af. Gebruik op dit pad een API-sleutel.
- Omgevingsvariabelen: `CODEX_BIN` (expliciet pad naar het binaire bestand) en `CODEX_TIMEOUT` (seconden per segment, standaard `600`).

### Vertalen met het Grok-abonnement (`--use_grok_cli`)

Hetzelfde principe als `--use_codex`, met de officiële CLI **Grok Build**: de vertaling wordt afgetrokken van het Grok-abonnement (SuperGrok / X Premium+) in plaats van per token te worden gefactureerd.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Inperking — lees dit vóór gebruik.** Deze provider is structureel **zwakker** dan `--use_codex`, en dat is bewust:

- Codex draait in `--sandbox read-only`, een door het systeem opgelegde grens.
- De sandbox van Grok kan op veel recente Linux-systemen niet worden toegepast: AppArmor blokkeert onbevoegde user namespaces sinds Ubuntu 24.04, en de deny-list voor sockets van de container-runtime faalt als `/run/podman` `0700` is. Een **ingebouwd** profiel dat niet kan worden toegepast, start daarentegen **stilzwijgend niet-ingeperkt**.
- Het script vraagt daarom standaard geen profiel aan en valt **nooit stilzwijgend terug**: het toont een waarschuwing. De inperking berust op de regels `--deny` van de CLI (waaronder de catch-all `*`), de enige gemeten _fail-closed_-laag — een onbekende regel zorgt ervoor dat het starten wordt geweigerd in plaats van de bescherming ongemerkt te verwijderen.
- Om de **OS-sandbox af te dwingen**: `GROK_TRANSLATE_SANDBOX=read-only`. Het starten mislukt als de machine deze niet kan naleven, wat het gewenste gedrag is.

**Quotum**: de Grok-pool is **wekelijks en gedeeld** met Chat, Imagine en Voice, en geen enkele opdracht kan dit uitlezen. Een batchverwerking kan dus uw conversationele gebruik aanspreken zonder dat dit wordt gemeld — vandaar een gelijktijdigheid van maximaal 2 en een waarschuwing in `regen_translations.sh`.

Andere variabelen: `GROK_BIN` (pad naar het binaire bestand), `GROK_TIMEOUT` (standaard 900 s).

Voor het opnieuw genereren van de 28 vertalingen:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
```

### Vertalen met OpenCode, naar de provider van uw keuze (`--use_opencode`)

[OpenCode](https://opencode.ai) is een **open source-agent (MIT)** in de terminal. Het is geen modelprovider maar een **router** naar de providers die u zelf in OpenCode hebt geconfigureerd: een API-sleutel, een abonnement (GitHub Copilot, ChatGPT, SuperGrok), de OpenCode Zen-gateway — die gratis modellen **zonder account** aanbiedt — of een **lokaal** model (Ollama, LM Studio, llama.cpp). Deze provider bestuurt `opencode run` in niet-interactieve modus en beperkt de aanroep tot één heen-en-teruguitwisseling, zonder tools.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` is **verplicht**, in de indeling `provider/modèle`. OpenCode is geen provider en er wordt niet namens u een standaard gekozen: de eigen terugvaloptie zou een gratis model zijn waarvan de uitwisselingen voor training kunnen worden gebruikt.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Inperking — wat het script bij elke aanroep doet:**

- Een inlineconfiguratie (`OPENCODE_CONFIG_CONTENT`), die voorrang heeft op die van u, definieert een agent `aipmt` waarvan **alle tools worden geweigerd** (`permission: { "*": "deny" }`): het model kan niets lezen, schrijven of uitvoeren — bij metingen probeert het dit zelfs niet. Sessiedeling is uitgeschakeld, `--pure` sluit externe plugins uit, nooit `--auto`.
- De aanroep draait in een **tijdelijke en lege map**, met de schakelaars `OPENCODE_DISABLE_PROJECT_CONFIG` en `OPENCODE_DISABLE_CLAUDE_CODE`: zonder deze schakelaars injecteert OpenCode in elke prompt de `AGENTS.md` van de huidige map en uw `~/.claude/CLAUDE.md` — bij metingen werd een instructie ‘elke reactie eindigen met BANANA’ in een `AGENTS.md` toegepast op de vertaling. De globale regels van `~/.config/opencode/AGENTS.md` blijven daarentegen toegepast: OpenCode staat niet toe deze te omzeilen.
- Het uitvoercontract vereist alles tegelijk: retourcode 0, geen `error`-gebeurtenis, geen toolaanroep, een laatste stap die is voltooid in `stop`, niet-lege tekst en een daadwerkelijk geladen agent — een onbekende `--agent` laat OpenCode niet falen, maar laat het **stilzwijgend terugvallen** op de codeeragent, met actieve tools. Een `exit 0` bewijst hier evenmin iets.
- **Er wordt geen aipmt-sleutel** aan het subprocess doorgegeven (dezelfde filtering als bij Codex en Grok), met één benoemde uitzondering: `OPENCODE_API_KEY`, de sleutel van OpenCode zelf (Zen, Go). De providers worden in OpenCode geconfigureerd (`opencode auth login`, `opencode.json`), niet in het `.env` van aipmt.

**Goed om te weten:**

- **De gratis Zen-modellen zijn ‘stealth’- of contributormodellen**, wisselend, met niet-gedocumenteerde limieten; hun uitwisselingen kunnen voor training worden gebruikt: geschikt voor openbare documentatie, te vermijden voor privé-inhoud. Bij metingen vertaalt `opencode/mimo-v2.5-free` deze README in één doorgang; `opencode/big-pickle` is trager en twee gelijktijdige aanvragen bleven onbeantwoord.
- **Een lokaal model moet minimaal 16 k context bieden** — de segmenten kunnen maximaal 16.000 tekens bevatten — terwijl Ollama vaak standaard 4.096 configureert. Met Ollama: een `Modelfile` met `PARAMETER num_ctx 32768`, daarna `ollama create`. De kwaliteit hangt af van het model: een 7B-model keerde een lijst om en beschadigde een afsluiting van een codeblok in een testbestand, terwijl een model van de gateway alles behield.
- `--eco` heeft geen effect (het model is dat van `--model`); `--reasoning_effort` wordt ongewijzigd doorgegeven als `--variant` van OpenCode en moet alleen worden opgevraagd als het model dit kent.
- Sessies worden door OpenCode vastgelegd in zijn database (`~/.local/share/opencode/`), zoals elke OpenCode-sessie.
- Omgevingsvariabelen: `OPENCODE_BIN` (expliciet pad naar het binaire bestand, anders eerst `PATH` en vervolgens `~/.opencode/bin/opencode`) en `OPENCODE_TIMEOUT` (seconden per segment, standaard `600`). `OPENCODE_CONFIG` wordt gerespecteerd als u deze exporteert.

### Economische modus

Gebruikt snellere en goedkopere modellen (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### Opties

| Optie                   | Beschrijving                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Eén te vertalen Markdown-bestand                                                                            |
| `--source_dir`           | Bronmap met de Markdown-bestanden                                                             |
| `--target_dir`           | Uitvoermap voor de vertaalde bestanden                                                               |
| `--source_lang`          | Brontaal (standaard: `fr`)                                                                                  |
| `--target_lang`          | Doeltaal (standaard: `en`)                                                                                   |
| `--model`                | Te gebruiken specifiek model                                                                                  |
| `--eco`                  | Goedkopere modellen gebruiken                                                                              |
| `--use_mistral`          | De Mistral AI-API gebruiken                                                                                     |
| `--use_claude`           | De Claude-API gebruiken                                                                                         |
| `--use_gemini`           | De Gemini-API gebruiken                                                                                         |
| `--use_codex`            | De Codex-CLI gebruiken met het abonnementsquotum van ChatGPT                                                    |
| `--use_grok`             | De xAI-API (Grok) gebruiken — vereist `XAI_API_KEY`                                                           |
| `--use_grok_cli`         | De Grok-CLI gebruiken met het abonnementsquotum van Grok                                                        |
| `--use_opencode`         | OpenCode (open source) gebruiken met de in OpenCode geconfigureerde provider; vereist `--model provider/modèle` |
| `--force`                | Hervertaling forceren                                                                                       |
| `--keep_filename`        | Oorspronkelijke bestandsnaam behouden                                                                          |
| `--news`                 | Nieuwsmodus: EN-citaten beschermen en taalvlaggen beheren                                      |
| `--add_translation_note` | Een vertaalnotitie toevoegen                                                                                |
| `--note_position`        | Positie van de notitie: `top`, `bottom` (standaard) of `both`                                                     |
| `--note_format`          | Indeling van de notitie: `legacy` (standaard, vetgedrukte alinea) of `marker`                                            |
| `--include_model`        | Modelnaam opnemen in het uitvoerbestand                                                            |
| `--reasoning_effort`     | Redeneerinspanning van GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

> **De zeven provider-flags sluiten elkaar onderling uit.** Voorheen werd het stilzwijgend geaccepteerd om er twee te combineren en werd de combinatie opgelost naar de eerst geteste optie: een vertaling die was aangevraagd met abonnementsquotum (`--use_codex`, `--use_grok_cli`)
> kon daardoor zonder enige waarschuwing leiden tot gebruiksgebaseerde facturering.
> `argparse` weigert deze combinatie voortaan.

### Vertaalnotitie: posities en indelingen

Met `--add_translation_note` kan de translator de notitie bovenaan, onderaan of op beide plaatsen zetten en deze weergeven als gewone tekst (achterwaarts compatibel) of als `marker`-indeling die door een Markdown-plugin kan worden verwerkt.

**Positie** (`--note_position`):

- `bottom` (standaard): notitie aan het einde van het bestand, zoals historisch gebruikelijk.
- `top`: notitie ingevoegd **na de YAML-frontmatter** (veilig voor Astro Content Collections, gray-matter enzovoort).
- `both`: notitie bovenaan EN onderaan ingevoegd (één LLM-aanroep, inhoud hergebruikt voor beide posities).

**Indeling** (`--note_format`):

- `legacy` (standaard): vetgedrukte alinea `**...**` — exact hetzelfde gedrag als in v1.8, byte-for-byte. Compatibel met Hugo, GitHub, GitLab en elke Markdown-renderer.
- `marker`: onzichtbare Markdown-linkreferentiedefinitie (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), gevolgd door een vetgedrukte blockquote. Native leesbaar op GitHub/GitLab en tijdens de build te gebruiken door een remark-plugin aan de Astro-zijde om een gestileerde banner te produceren (zie de blog op jls42.org).

```bash
# Compatibilité legacy (rien ne change vs v1.8)
aipmt --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
aipmt --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
aipmt --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### Standaardmodellen (2026)

| Provider | Kwaliteit (standaard)                      | Goedkoop (`--eco`)      |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI   | `gpt-5.6-terra`                       | `gpt-5.6-luna`            |
| Claude   | `claude-sonnet-5`                     | `claude-haiku-4-5`        |
| Mistral  | `mistral-large-latest`                | `mistral-small-latest`    |
| Gemini   | `gemini-3.7-flash`                    | `gemini-3.1-flash-lite`   |
| Codex    | `gpt-5.6-sol`                         | `gpt-5.6-luna`            |
| Grok API | `grok-4.6`                            | `grok-4.3`                |
| Grok CLI | `grok-4.6`                            | `grok-4.5`                |
| OpenCode | `--model provider/modèle` verplicht | idem — `--eco` zonder effect |

> **Aanbeveling voor long-formvertalingen**: `--use_gemini` (standaard = `gemini-3.7-flash`) behoudt de Markdown-structuur getrouw in niet-Latijnse scripts (PL, JA, ZH, AR, HI), ook in `--news`-modus, waarin het behoud van placeholders belangrijk is. Gemeten op deze naar het Japans vertaalde README: identieke structuur als `gemini-3.1-pro-preview` (21 lijsten, 18 codeblokken, 13 HTML-links, 13 afbeeldingen, alle URL's behouden) met ongeveer 6× minder latentie. OpenAI blijft de standaard voor achterwaartse compatibiliteit.

## Projecten die dit script gebruiken

- **[jls42.org](https://jls42.org)** - Meertalige persoonlijke blog (15 talen)

## Auteur

Julien LE SAUX
E-mail: contact@jls42.org

## Licentie

GNU GENERAL PUBLIC LICENSE Version 3. Zie [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artikel vertaald van het Frans naar het Nederlands met gpt-5.6-luna.**

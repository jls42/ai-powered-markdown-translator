# AI-aangedreven Markdown-vertaler

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Codekwaliteit</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status Quality Gate"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Beveiligingsbeoordeling"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Betrouwbaarheidsbeoordeling"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Onderhoudbaarheidsbeoordeling"></a>
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

Vertaler van Markdown-bestanden die **OpenAI**, **Mistral AI**, **Claude (Anthropic)** en **Google Gemini** gebruikt.

Dit Python-script vertaalt Markdown-bestanden van een brontaal naar een doeltaal, met behoud van de opmaak, codeblokken en frontmatter-metadata.

## Belangrijkste functies

- **Multi-Provider**: Ondersteuning voor 4 API's (OpenAI, Mistral, Claude, Gemini) + de Codex CLI met een ChatGPT-abonnement
- **Modellen 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Economische modus**: Optie `--eco` om snellere en goedkopere modellen te gebruiken
- **Eén bestand**: Optie `--file` om één bestand te vertalen
- **Intelligente segmentatie**: Verwerking van lange teksten met tokenlimieten per model
- **Codebehoud**: Codeblokken EN inline code (`` `...` ``) blijven behouden
- **Bestandsnaam**: Optie `--keep_filename` om de oorspronkelijke naam te behouden
- **Nieuwsmodus**: Optie `--news` om Engelse citaten te beschermen en vlaggen in nieuwsartikelen te beheren
- **.env-configuratie**: Ondersteuning voor het bestand `.env` voor API-sleutels
- **Vertaalnotitie**: Optioneel toevoegen van een notitie aan het einde van het document

## Installatie

### De tool gebruiken

```bash
pip install ai-powered-markdown-translator
```

De opdracht `aipmt` is daarna overal beschikbaar. Als de map met
Python-scripts niet in je `PATH` staat, doet `python -m aipmt` precies hetzelfde.
Python 3.10 of nieuwer.

Voor een installatie die geïsoleerd blijft van de rest van je pakketten:

```bash
pipx install ai-powered-markdown-translator
```

### Bijdragen aan het project

De gekloonde repository blijft nodig voor ontwikkeling: daar bevinden zich de tests,
de 28 vertalingen en alle kwaliteits tooling.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` is een **volledig vastgezette lock**, een exacte weerspiegeling van
de geteste omgeving. De gepubliceerde grenzen in `pyproject.toml` zijn
bewust ruimer: ze leggen niets op aan je andere pakketten.

### Kwaliteitstooling (optioneel maar aanbevolen)

Het project gebruikt [`pre-commit`](https://pre-commit.com) om te voorkomen dat slecht opgemaakte,
kwetsbare code of code met een geheim wordt gecommit. Installatie:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Actieve hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexiteit), detect-secrets (API-sleutels), mypy (geleidelijke typing), Opengrep (SAST), pip-audit (CVE-deps), unittest. Zie de sectie _Quality / pre-commit_ in `CLAUDE.md` voor meer informatie.

## Configuratie

De sleutels worden op **drie plaatsen** gezocht, van meest naar minst
prioritair. Elke plaats vult alleen aan wat de vorige leeg laat.

|     | Waar                                         | Waarvoor                            |
| --- | -------------------------------------------- | ------------------------------------ |
| 1   | Omgevingsvariabelen                          | CI, containers, eenmalige afwijking  |
| 2   | `.env` van de huidige map (of een bovenliggende map) | een sleutel voor één project         |
| 3   | `~/.config/aipmt/.env`                       | **één keer geïnstalleerd, overal geldig** |

Het eenvoudigst na een `pip install` is de derde optie:

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

Dit bestand volgt `XDG_CONFIG_HOME` wanneer de variabele naar een absoluut pad verwijst
(anders wordt deze genegeerd, zoals de specificatie voorschrijft), en `%APPDATA%`
op Windows.

De tweede optie blijft nuttig wanneer een repository een eigen sleutel heeft: een
`.env` in de hoofdmap krijgt dan voorrang op de gebruikersconfiguratie,
zonder die te wijzigen. En een variabele die al in de omgeving is gedefinieerd,
heeft voorrang op beide:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Als er geen sleutel wordt gevonden, toont de opdracht geen call trace: ze
somt de drie locaties op met hun exacte pad.

`GEMINI_API_KEY` wordt geaccepteerd als alternatief voor `GOOGLE_API_KEY` (AI
Studio-conventie). Optionele variabelen: `XAI_BASE_URL` (xAI-endpoint, standaard
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (seconden per Anthropic-aanroep, standaard
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
en `GROK_TRANSLATE_SANDBOX` (zie de sectie Grok CLI). Voor
`regen_translations.sh`: `REGEN_PROVIDER`, `REGEN_MODEL` en
`REGEN_JOB_TIMEOUT` (limiet per job, standaard 600 s).

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
```

### Vertalen met je ChatGPT-abonnement (`--use_codex`)

Deze provider gebruikt geen API-sleutel: hij stuurt de officiële Codex CLI aan in
niet-interactieve modus. De vertaling wordt dus afgetrokken van het quotum van het
reeds betaalde ChatGPT-abonnement (Plus, Pro, Business…). Dit is de enige door
OpenAI gedocumenteerde manier voor dit gebruik — de tokens van `~/.codex/auth.json`
authenticeren geen oproepen naar de Platform API en worden bovendien nooit door
dit script gelezen.

**Vereisten:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Het binaire bestand wordt in deze volgorde gezocht: de variabele `CODEX_BIN`, de
`PATH`, en vervolgens het Python-pakket `openai-codex-cli-bin`. Dit laatste staat
bewust niet in `requirements.txt`: het is ongeveer 250 MB groot, wat aan alle
gebruikers zou worden opgelegd voor een optionele provider.

**Goed om te weten:**

- **Er wordt geen API-sleutel gebruikt.** `OPENAI_API_KEY` en `CODEX_API_KEY` worden
  uit de omgeving van het subprocess verwijderd. Zo wordt gegarandeerd dat een sleutel
  in `.env` de vertaling nooit laat overschakelen naar facturering op basis
  van gebruik.
- **Eén segment = één “lokaal bericht”** binnen het venster van 5 uur van het plan.
  Gebruik `--eco` (model `gpt-5.6-luna`, 250–2.000 berichten/5 uur op Plus)
  in plaats van het kwaliteitsmodel (`gpt-5.6-sol`, 10–100 berichten/5 uur).
- **Trager** dan een API-aanroep: reken op ongeveer 45 seconden voor een volledige
  README, tegenover enkele seconden rechtstreeks.
- **Geweigerd in CI** (`CI` of `GITHUB_ACTIONS` ingesteld): authenticatie
  via een abonnement is niet bedoeld voor een gedeelde runner en OpenAI raadt deze
  workflow af voor openbare repositories. Gebruik op dit pad een API-sleutel.
- Omgevingsvariabelen: `CODEX_BIN` (expliciet pad naar het binaire bestand) en
  `CODEX_TIMEOUT` (seconden per segment, standaard `600`).

### Vertalen met je Grok-abonnement (`--use_grok_cli`)

Hetzelfde principe als bij `--use_codex`, met de officiële CLI **Grok Build**:
de vertaling wordt afgetrokken van het Grok-abonnement (SuperGrok / X Premium+)
in plaats van per token te worden gefactureerd.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Beperking — lees dit vóór gebruik.** Deze provider is structureel **zwakker**
dan `--use_codex`, en dat is bewust:

- Codex draait in `--sandbox read-only`, een door het systeem opgelegde grens.
- De sandbox van Grok kan op veel recente Linux-systemen **niet** worden toegepast:
  AppArmor blokkeert niet-bevoorrechte user namespaces sinds Ubuntu 24.04, en de
  deny-list van containersockets faalt wanneer `/run/podman` op `0700` staat.
  Een **ingebouwd** profiel dat niet kan worden toegepast, start echter
  **stilzwijgend onbegrensd**.
- Het script vraagt daarom standaard geen profiel aan en valt **nooit stilzwijgend
  terug**: het toont een waarschuwing. De beveiliging berust op de regels `--deny`
  van de CLI (waaronder de catch-all `*`), de enige laag die
  _fail-closed_ wordt gemeten — een onbekende regel weigert het opstarten in plaats
  van de bescherming ongemerkt te verwijderen.
- Om de OS-sandbox **af te dwingen**: `GROK_TRANSLATE_SANDBOX=read-only`. Het opstarten mislukt als de
  machine deze niet kan uitvoeren, wat het gewenste gedrag is.

**Quotum**: de Grok-pool is **wekelijks en gedeeld** met Chat, Imagine en
Voice, en geen enkele opdracht kan dit uitlezen. Een batchverwerking kan dus je
conversationele gebruik verminderen zonder dat dit wordt gemeld — vandaar een
concurrentie beperkt tot 2 en een waarschuwing in `regen_translations.sh`.

Andere variabelen: `GROK_BIN` (pad naar het binaire bestand), `GROK_TIMEOUT` (standaard 900 s).

Voor het opnieuw genereren van de 28 vertalingen:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### Economische modus

Gebruikt snellere en goedkopere modellen (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opties

| Optie                   | Beschrijving                                                              |
| ----------------------- | ------------------------------------------------------------------------ |
| `--file`                 | Eén Markdown-bestand om te vertalen                                       |
| `--source_dir`           | Bronmap met de Markdown-bestanden                        |
| `--target_dir`           | Uitvoermap voor de vertaalde bestanden                          |
| `--source_lang`          | Brontaal (standaard: `fr`)                                             |
| `--target_lang`          | Doeltaal (standaard: `en`)                                              |
| `--model`                | Te gebruiken specifiek model                                             |
| `--eco`                  | Economische modellen gebruiken                                         |
| `--use_mistral`          | De Mistral AI API gebruiken                                                |
| `--use_claude`                  | De Claude API gebruiken                                                    |
| `--use_gemini`                  | De Gemini API gebruiken                                                    |
| `--use_codex`            | De Codex CLI gebruiken met het abonnementsquotum van ChatGPT               |
| `--use_grok`             | De xAI API gebruiken (Grok) — vereist `XAI_API_KEY`                      |
| `--use_grok_cli`         | De Grok CLI gebruiken met het abonnementsquotum van Grok                   |
| `--force`                | Hervertaling forceren                                                  |
| `--keep_filename`        | De oorspronkelijke bestandsnaam behouden                                     |
| `--news`                 | Nieuwsmodus: beschermt EN-citaten en beheert vlaggen per taal |
| `--add_translation_note` | Een vertaalnotitie toevoegen                                           |
| `--note_position`        | Positie van de notitie: `top`, `bottom` (standaard) of `both`                |
| `--note_format`          | Opmaak van de notitie: `legacy` (standaard, vetgedrukte alinea) of `marker`       |
| `--include_model`        | Modelnaam opnemen in het uitvoerbestand                       |
| `--reasoning_effort`     | GPT-5.x-redeneringsinspanning: `none`/`low`/`medium`/`high`/`xhigh`    |

> **De zes providerflags sluiten elkaar uit.** Voorheen werd het combineren van twee
> flags stilzwijgend geaccepteerd en werd de eerste geteste gebruikt: een vertaling
> die op een abonnementsquotum was aangevraagd (`--use_codex`, `--use_grok_cli`)
> kon zo zonder enige waarschuwing worden uitgevoerd met facturering op basis van gebruik.
> `argparse` weigert deze combinatie nu.

### Vertaalnotitie: posities en formaten

Met `--add_translation_note` kan de vertaler de notitie bovenaan, onderaan of op beide
plaatsen zetten, en deze weergeven als eenvoudige tekst (achterwaarts compatibel)
of als `marker`-formaat dat door een Markdown-plugin kan worden gebruikt.

**Positie** (`--note_position`):

- `bottom` (standaard): notitie aan het einde van het bestand, zoals historisch gebruikelijk.
- `top`: notitie ingevoegd **na de YAML-frontmatter** (veilig voor Astro Content Collections, gray-matter enz.).
- `both`: notitie bovenaan EN onderaan (één LLM-aanroep, inhoud hergebruikt voor beide posities).

**Formaat** (`--note_format`):

- `legacy` (standaard): vetgedrukte alinea `**...**` — exact hetzelfde gedrag als in v1.8, byte-for-byte. Compatibel met Hugo, GitHub, GitLab en elke Markdown-renderer.
- `marker`: onzichtbare Markdown-linkreferentiedefinitie (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), gevolgd door een vetgedrukte blockquote. Native leesbaar op GitHub/GitLab en tijdens de build te gebruiken door een remark-plugin aan Astro-zijde om een gestileerde banner te produceren (zie blog jls42.org).

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

| Provider | Kwaliteit (standaard)       | Economisch (`--eco`)    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **Aanbeveling voor long-formvertalingen**: `--use_gemini` (standaard = `gemini-3.7-flash`)
> behoudt de Markdown-structuur getrouw bij scripts in niet-Latijnse talen (PL, JA, ZH, AR, HI),
> ook in `--news`-modus, waarin het behoud van placeholders van belang is. Gemeten
> op deze naar het Japans vertaalde README: identieke structuur aan `gemini-3.1-pro-preview` (21 lijsten,
> 18 codeblokken, 13 HTML-links, 13 afbeeldingen, alle URL's behouden) bij ongeveer 6 keer
> minder latentie. OpenAI blijft de standaard voor achterwaartse compatibiliteit.

## Projecten die dit script gebruiken

- **[jls42.org](https://jls42.org)** - Meertalige persoonlijke blog (15 talen)

## Auteur

Julien LE SAUX
E-mail: contact@jls42.org

## Licentie

GNU GENERAL PUBLIC LICENSE Versie 3. Zie [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artikel vertaald van het Frans naar het Nederlands met gpt-5.6-luna.**

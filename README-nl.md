# AI-Powered Markdown-vertaler

🌍 [Frans](README.md) | [Engels](README-en.md) | [Spaans](README-es.md) | [Chinees](README-zh.md) | [Duits](README-de.md) | [Japans](README-ja.md) | [Koreaans](README-ko.md) | [Arabisch](README-ar.md) | [Hindi](README-hi.md) | [Italiaans](README-it.md) | [Nederlands](README-nl.md) | [Pools](README-pl.md) | [Portugees](README-pt.md) | [Roemeens](README-ro.md) | [Zweeds](README-sv.md)

<h4 align="center">📊 Codekwaliteit</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status van kwaliteitscontrole"></a>
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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Coderegels"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy-badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Vertaler voor Markdown-bestanden die **OpenAI**, **Mistral AI**, **Claude (Anthropic)** en **Google Gemini** gebruikt.

Dit Python-script vertaalt Markdown-bestanden van een brontaal naar een doeltaal, met behoud van de opmaak, codeblokken en front-mattermetadata.

## Belangrijkste kenmerken

- **Multi-Provider**: Ondersteuning voor 4 API's (OpenAI, Mistral, Claude, Gemini) + de Codex CLI via een ChatGPT-abonnement
- **Modellen van 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Voordelige modus**: Optie `--eco` om snellere en goedkopere modellen te gebruiken
- **Enkel bestand**: Optie `--file` om één bestand te vertalen
- **Intelligente segmentatie**: Verwerking van lange teksten met tokenlimieten per model
- **Behoud van code**: Codeblokken EN inline code (`` `...` ``) blijven behouden
- **Bestandsnaam**: Optie `--keep_filename` om de oorspronkelijke naam te behouden
- **Nieuwsmodus**: Optie `--news` om Engelse citaten te beschermen en vlaggen in nieuwsartikelen te beheren
- **.env-configuratie**: Ondersteuning voor het bestand `.env` voor API-sleutels
- **Vertaalnotitie**: Optioneel een notitie aan het einde van het document toevoegen

## Installatie

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Kwaliteitstools (optioneel maar aanbevolen)

Het project gebruikt [`pre-commit`](https://pre-commit.com) om te voorkomen dat slecht geformatteerde, kwetsbare of geheime gegevens bevattende code wordt gecommit. Installatie:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Actieve hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexiteit), detect-secrets (API-sleutels), mypy (progressieve typering), Opengrep (SAST), pip-audit (CVE-afhankelijkheden), unittest. Zie de sectie _Quality / pre-commit_ in `CLAUDE.md` voor details.

## Configuratie

Maak een bestand `.env` in de hoofdmap van het project of stel de omgevingsvariabelen in:

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

`GEMINI_API_KEY` wordt geaccepteerd als alternatief voor `GOOGLE_API_KEY` (AI
Studio-conventie). Optionele variabelen: `XAI_BASE_URL` (xAI-endpoint, standaard
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (seconden per Anthropic-aanroep, standaard
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
en `GROK_TRANSLATE_SANDBOX` (zie de sectie Grok CLI). Voor
`regen_translations.sh`: `REGEN_PROVIDER`, `REGEN_MODEL` en
`REGEN_JOB_TIMEOUT` (limiet per taak, standaard 600 s).

## Gebruik

### Eén bestand vertalen

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Een map vertalen

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
python translate.py --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
python translate.py --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
python translate.py --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'
```

### Vertalen via je ChatGPT-abonnement (`--use_codex`)

Deze provider gebruikt geen enkele API-sleutel: hij stuurt de officiële Codex CLI
aan in niet-interactieve modus, zodat de vertaling wordt afgetrokken van het
reeds betaalde quotum van het ChatGPT-abonnement (Plus, Pro, Business…).
Dit is de enige door OpenAI gedocumenteerde methode voor dit gebruik — de tokens
van `~/.codex/auth.json` verifiëren aanroepen naar de API Platform niet en worden
door dit script bovendien nooit gelezen.

**Vereisten:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Het binaire bestand wordt in deze volgorde gezocht: de variabele `CODEX_BIN`, het `PATH`,
en vervolgens het Python-package `openai-codex-cli-bin`. Dit laatste staat bewust
niet in `requirements.txt`: het is ongeveer 250 MB groot, wat anders aan alle
gebruikers zou worden opgelegd voor een optionele provider.

**Goed om te weten:**

- **Er wordt geen API-sleutel gebruikt.** `OPENAI_API_KEY` en `CODEX_API_KEY` worden
  uit de omgeving van het subproces verwijderd, wat garandeert dat een sleutel
  in `.env` de vertaling nooit ongemerkt naar facturering per gebruik
  laat overschakelen.
- **Eén segment = één „lokaal bericht”** binnen het venster van 5 uur van het abonnement.
  Gebruik `--eco` (model `gpt-5.6-luna`, 250-2.000 berichten/5 u met Plus)
  in plaats van het kwaliteitsmodel (`gpt-5.6-sol`, 10-100 berichten/5 u).
- **Langzamer** dan een API-aanroep: reken op ongeveer 45 s voor een volledige README,
  tegenover enkele seconden bij een rechtstreekse aanroep.
- **Geweigerd in CI** (als `CI` of `GITHUB_ACTIONS` is ingesteld):
  abonnementsverificatie is niet bedoeld voor een gedeelde runner en OpenAI
  raadt deze workflow af voor openbare repositories. Gebruik hiervoor een API-sleutel.
- Omgevingsvariabelen: `CODEX_BIN` (expliciet pad naar het binaire bestand) en
  `CODEX_TIMEOUT` (seconden per segment, standaard `600`).

### Vertalen via je Grok-abonnement (`--use_grok_cli`)

Hetzelfde principe als `--use_codex`, met de officiële CLI **Grok Build**:
de vertaling wordt afgetrokken van het Grok-abonnement (SuperGrok / X Premium+)
in plaats van per token te worden gefactureerd.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Isolatie — lees dit vóór gebruik.** Deze provider is structureel **zwakker**
dan `--use_codex`, en dat is een bewuste keuze:

- Codex draait in `--sandbox read-only`, een door het systeem opgelegde grens.
- De sandbox van Grok **kan op veel recente Linux-systemen niet worden toegepast**:
  AppArmor blokkeert niet-geprivilegieerde user namespaces sinds Ubuntu 24.04,
  en de deny-list voor sockets van de container-runtime mislukt als
  `/run/podman` in `0700` staat. Een **ingebouwd** profiel dat niet kan
  worden toegepast, start echter **stilzwijgend zonder isolatie**.
- Het script vraagt daarom standaard geen profiel aan en **valt nooit
  stilzwijgend terug**: het toont een waarschuwing. De isolatie berust op de
  regels `--deny` van de CLI (waaronder de catch-all `*`), de enige
  gemeten _fail-closed_-laag — een onbekende regel zorgt ervoor dat het opstarten
  wordt geweigerd in plaats van de bescherming zonder melding te verwijderen.
- Om de OS-sandbox **verplicht te stellen**: `GROK_TRANSLATE_SANDBOX=read-only`. Het
  opstarten mislukt als de machine hier niet aan kan voldoen, wat het
  gewenste gedrag is.

**Quotum**: de Grok-pool is **wekelijks en gedeeld** met Chat, Imagine en
Voice, en geen enkele opdracht kan het quotum uitlezen. Een batchverwerking kan
dus je gespreksgebruik verminderen zonder enige melding — vandaar een
concurrentielimiet van 2 en een waarschuwing in `regen_translations.sh`.

Andere variabelen: `GROK_BIN` (pad naar het binaire bestand), `GROK_TIMEOUT` (standaard 900 s).

Voor het opnieuw genereren van de 28 vertalingen:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### Voordelige modus

Gebruikt snellere en goedkopere modellen (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opties

| Optie                    | Beschrijving                                                              |
| ------------------------ | ------------------------------------------------------------------------- |
| `--file`                 | Eén Markdown-bestand om te vertalen                                       |
| `--source_dir`           | Bronmap met de Markdown-bestanden                                          |
| `--target_dir`           | Uitvoermap voor de vertaalde bestanden                                     |
| `--source_lang`          | Brontaal (standaard: `fr`)                                       |
| `--target_lang`          | Doeltaal (standaard: `en`)                                       |
| `--model`                | Specifiek te gebruiken model                                               |
| `--eco`                  | De voordelige modellen gebruiken                                          |
| `--use_mistral`          | De Mistral AI API gebruiken                                                |
| `--use_claude`           | De Claude API gebruiken                                                    |
| `--use_gemini`           | De Gemini API gebruiken                                                    |
| `--use_codex`            | De Codex CLI gebruiken met het quotum van het ChatGPT-abonnement           |
| `--use_grok`             | De xAI API (Grok) gebruiken — vereist `XAI_API_KEY`                        |
| `--use_grok_cli`         | De Grok CLI gebruiken met het quotum van het Grok-abonnement               |
| `--force`                | Opnieuw vertalen afdwingen                                                 |
| `--keep_filename`        | De oorspronkelijke bestandsnaam behouden                                   |
| `--news`                 | Nieuwsmodus: beschermt Engelse citaten en beheert vlaggen per taal         |
| `--add_translation_note` | Een vertaalnotitie toevoegen                                                |
| `--note_position`        | Positie van de notitie: `top`, `bottom` (standaard) of `both` |
| `--note_format`          | Formaat van de notitie: `legacy` (standaard, vetgedrukte alinea) of `marker` |
| `--include_model`        | De modelnaam opnemen in het uitvoerbestand                                 |
| `--reasoning_effort`     | Redeneerinspanning voor GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

> **De zes provider-flags sluiten elkaar wederzijds uit.** Het combineren van
> twee flags werd voorheen stilzwijgend geaccepteerd en leidde naar de eerst
> geteste provider: een vertaling die via een abonnementsquotum was aangevraagd
> (`--use_codex`, `--use_grok_cli`), kon daardoor zonder waarschuwing per gebruik
> worden gefactureerd. `argparse` weigert de combinatie voortaan.

### Vertaalnotitie: posities en formaten

Met `--add_translation_note` kan de vertaler de notitie bovenaan, onderaan of op beide plaatsen zetten en deze weergeven als eenvoudige tekst (achterwaarts compatibel) of in een door een Markdown-plugin verwerkbaar `marker`-formaat.

**Positie** (`--note_position`):

- `bottom` (standaard): notitie aan het einde van het bestand, zoals van oudsher.
- `top`: notitie ingevoegd **na de YAML-frontmatter** (veilig voor Astro Content Collections, gray-matter, enz.).
- `both`: notitie bovenaan EN onderaan ingevoegd (één LLM-aanroep, inhoud wordt voor beide posities hergebruikt).

**Formaat** (`--note_format`):

- `legacy` (standaard): vetgedrukte alinea `**...**` — gedrag dat byte-for-byte identiek is aan v1.8. Compatibel met Hugo, GitHub, GitLab en elke Markdown-renderer.
- `marker`: onzichtbare Markdown-linkreferentiedefinitie (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), gevolgd door een vetgedrukt blockquote. Rechtstreeks leesbaar op GitHub/GitLab en tijdens het buildproces bruikbaar door een remark-plugin voor Astro om een gestileerde banner te maken (zie blog jls42.org).

```bash
# Compatibilité legacy (rien ne change vs v1.8)
python translate.py --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### Standaardmodellen (2026)

| Provider | Kwaliteit (standaard)   | Voordelig (`--eco`) |
| -------- | ---------------------- | --------------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`             |
| Claude   | `claude-sonnet-5`        | `claude-haiku-4-5`             |
| Mistral  | `mistral-large-latest`        | `mistral-small-latest`             |
| Gemini   | `gemini-3.7-flash`        | `gemini-3.1-flash-lite`             |
| Codex    | `gpt-5.6-sol`        | `gpt-5.6-luna`             |
| Grok API | `grok-4.6`        | `grok-4.3`             |
| Grok CLI | `grok-4.6`        | `grok-4.5`             |

> **Aanbeveling voor long-formvertalingen**: `--use_gemini` (standaard = `gemini-3.7-flash`)
> behoudt de Markdown-structuur nauwkeurig bij niet-Latijnse schriften (PL, JA, ZH,
> AR, HI), ook in de modus `--news`, waarin de getrouwheid van placeholders
> belangrijk is. Gemeten op deze naar het Japans vertaalde README: een structuur
> die identiek is aan `gemini-3.1-pro-preview` (21 lijsten, 18 codeblokken, 13 HTML-links,
> 13 afbeeldingen, alle URL's behouden) met ongeveer 6x minder latentie. OpenAI
> blijft de standaard voor achterwaartse compatibiliteit.

## Projecten die dit script gebruiken

- **[jls42.org](https://jls42.org)** - Meertalige persoonlijke blog (15 talen)

## Auteur

Julien LE SAUX
E-mail: contact@jls42.org

## Licentie

GNU GENERAL PUBLIC LICENSE Version 3. Zie [LICENSE](LICENSE).

**Artikel vertaald van het Frans naar het Nederlands met gpt-5.6-sol.**

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

Vertaler voor Markdown-bestanden die **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** en **Grok (xAI)** gebruikt — via een API, met het quotum van een ChatGPT-abonnement (Codex) of Grok zonder facturering per gebruik, of via **OpenCode**, de open-sourceagent, met de provider van jouw keuze: een lokaal model (Ollama), gratis, een abonnement (GitHub Copilot…) of een sleutel.

Dit Python-script vertaalt Markdown-bestanden van een brontaal naar een doeltaal, met behoud van de opmaak, codeblokken en frontmatter-metadata.

## Belangrijkste kenmerken

- **Meerdere providers**: 5 API's (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLI's via een abonnement, zonder facturering per gebruik — Codex (ChatGPT) en Grok — + OpenCode (open source, MIT) met elke in OpenCode geconfigureerde provider, waaronder een lokaal model
- **Modellen uit 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Voordelige modus**: Optie `--eco` om snellere en goedkopere modellen te gebruiken
- **Eén bestand**: Optie `--file` om één bestand te vertalen
- **Intelligente segmentatie**: Verwerking van lange teksten met tokenlimieten per model
- **Behoud van code**: Codeblokken EN inline code (`` `...` ``) blijven behouden
- **Bestandsnaam**: Optie `--keep_filename` om de oorspronkelijke naam te behouden
- **Nieuwsmodus**: Optie `--news` om Engelse citaten te beschermen en vlaggen in nieuwsartikelen te verwerken
- **.env-configuratie**: Ondersteuning voor het bestand `.env` voor API-sleutels
- **Vertaalnotitie**: Optioneel toevoegen van een notitie aan het einde van het document

## Installatie

### Om de tool te gebruiken

```bash
pip install ai-powered-markdown-translator
```

De opdracht `aipmt` is daarna overal beschikbaar. Als de map met Python-scripts
niet in je `PATH` staat, doet `python -m aipmt` precies hetzelfde.
Python 3.10 of nieuwer.

Voor een installatie die van de rest van je pakketten is geïsoleerd:

```bash
pipx install ai-powered-markdown-translator
```

### Om aan het project bij te dragen

De gekloonde repository blijft nodig voor ontwikkeling: daar bevinden zich de tests,
de 28 vertalingen en alle tools voor kwaliteitscontrole.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` is een **volledig vastgezette lockfile**, die exact overeenkomt met
de geteste omgeving. De in `pyproject.toml` gepubliceerde grenzen zijn
bewust ruimer: ze leggen geen beperkingen op aan je andere pakketten.

### Tools voor kwaliteitscontrole (optioneel maar aanbevolen)

Het project gebruikt [`pre-commit`](https://pre-commit.com) om te voorkomen dat slecht opgemaakte, kwetsbare code of code met een geheim wordt gecommit. Installatie:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Actieve hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexiteit), detect-secrets (API-sleutels), mypy (geleidelijke typering), Opengrep (SAST), pip-audit (CVE's in afhankelijkheden), unittest. Zie in `CLAUDE.md` de sectie _Quality / pre-commit_ voor details.

## Configuratie

Er wordt op **drie locaties** naar sleutels gezocht, van hoogste naar laagste prioriteit.
Elke locatie vult alleen aan wat op de vorige locatie ontbreekt.

|     | Waar                                          | Waarvoor                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Omgevingsvariabelen                           | CI, containers, eenmalige uitzondering |
| 2   | `.env` van de huidige map (of een bovenliggende map) | een projectspecifieke sleutel         |
| 3   | `~/.config/aipmt/.env`                        | **eenmaal geïnstalleerd, overal geldig** |

Na een `pip install` is de derde optie het eenvoudigst:

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

Dit bestand volgt `XDG_CONFIG_HOME` wanneer de variabele naar een absoluut pad verwijst
(anders wordt deze genegeerd, zoals de specificatie voorschrijft), en `%APPDATA%`
onder Windows.

De tweede optie blijft nuttig wanneer een repository een eigen sleutel heeft: een `.env` in de hoofdmap
heeft dan voorrang op de gebruikersconfiguratie, zonder die te wijzigen. Een
variabele die al in de omgeving is gedefinieerd, heeft voorrang op beide:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Als er geen sleutel wordt gevonden, toont de opdracht geen aanroeptrace: ze
vermeldt de drie locaties met hun exacte pad.

`GEMINI_API_KEY` wordt geaccepteerd als alternatief voor `GOOGLE_API_KEY` (AI
Studio-conventie). Optionele variabelen: `XAI_BASE_URL` (xAI-endpoint, standaard
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (seconden per Anthropic-aanroep, standaard
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (zie de sectie over Grok CLI), `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (zie de sectie over OpenCode) en `OPENROUTER_BASE_URL` /
`OPENROUTER_TIMEOUT` / `OPENROUTER_PREFLIGHT_TIMEOUT` (zie de sectie over
OpenRouter). Voor
`regen_translations.sh`: `REGEN_PROVIDER` (standaard `codex`, via een abonnement),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (verplichte uitzondering voor een
gefactureerde API) en `REGEN_JOB_TIMEOUT` (limiet per taak, standaard 600 s, 1.800 s met Codex).

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

# Avec OpenRouter (routeur vers ~430 modèles ; --model obligatoire)
aipmt --use_openrouter --model 'z-ai/glm-5.2' --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### Vertalen via je ChatGPT-abonnement (`--use_codex`)

Deze provider gebruikt geen API-sleutel: hij bestuurt de officiële Codex CLI in
niet-interactieve modus, waardoor de vertaling wordt afgetrokken van het quotum van het
reeds betaalde ChatGPT-abonnement (Plus, Pro, Business…). Dit is de enige door
OpenAI gedocumenteerde methode voor dit gebruik — de tokens van `~/.codex/auth.json` verifiëren
aanroepen naar de API Platform niet en worden door dit script bovendien nooit gelezen.

**Vereisten:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Het binaire bestand wordt in deze volgorde gezocht: de variabele `CODEX_BIN`, de `PATH`,
en vervolgens het Python-pakket `openai-codex-cli-bin`. Dat laatste staat bewust
niet in `requirements.txt`: het is ongeveer 250 MB groot, wat anders aan alle
gebruikers zou worden opgelegd voor een optionele provider.

**Goed om te weten:**

- **Er wordt geen API-sleutel gebruikt.** `OPENAI_API_KEY` en `CODEX_API_KEY` worden
  uit de omgeving van het subprocess verwijderd, zodat een sleutel
  in `.env` er nooit toe kan leiden dat de vertaling per gebruik wordt
  gefactureerd.
- **Eén segment = één ‘lokaal bericht’** binnen het venster van 5 uur van het abonnement.
  Gebruik `--eco` (model `gpt-5.6-luna`, 250-2.000 berichten/5 uur met Plus)
  in plaats van het kwaliteitsmodel (`gpt-5.6-sol`, 10-100 berichten/5 uur).
- **Langzamer** dan een API-aanroep: reken op ongeveer 45 s voor een volledige README, tegenover
  enkele seconden bij een directe aanroep.
- **Geweigerd in CI** (wanneer `CI` of `GITHUB_ACTIONS` is gedefinieerd): het abonnement
  wordt geverifieerd met een persoonlijk sessiebestand, en dit naar een gedeelde runner
  overbrengen komt erop neer dat daar een identiteit wordt geplaatst die door alles wat
  erop wordt uitgevoerd opnieuw kan worden gebruikt. Gebruik hiervoor een API-sleutel.
- Omgevingsvariabelen: `CODEX_BIN` (expliciet pad naar het binaire bestand) en
  `CODEX_TIMEOUT` (seconden per segment, standaard `600`).

### Vertalen via je Grok-abonnement (`--use_grok_cli`)

Hetzelfde principe als `--use_codex`, met de officiële CLI **Grok Build**: de
vertaling wordt afgetrokken van het Grok-abonnement (SuperGrok / X Premium+) in plaats
van per token te worden gefactureerd.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Isolatie — lees dit vóór gebruik.** Deze provider is structureel **minder
sterk** dan `--use_codex`, en dat is een bewuste keuze:

- Codex draait in `--sandbox read-only`, een door het systeem opgelegde grens.
- De sandbox van Grok **kan niet worden toegepast** op veel recente Linux-systemen:
  AppArmor blokkeert sinds Ubuntu 24.04 niet-bevoorrechte user namespaces, en de
  denylist voor sockets van de container-runtime faalt als
  `/run/podman` op `0700` staat. Een **ingebouwd** profiel dat niet kan
  worden toegepast, start echter **stilzwijgend zonder isolatie**.
- Het script vraagt daarom standaard geen enkel profiel aan en **valt nooit
  stilzwijgend terug**: het toont een waarschuwing. De isolatie steunt op de
  `--deny`-regels van de CLI (waaronder de catch-all `*`), de enige laag met
  gemeten _fail-closed_-gedrag — een onbekende regel zorgt ervoor dat het opstarten wordt
  geweigerd, in plaats van de bescherming zonder melding te verwijderen.
- Om de OS-sandbox **verplicht te stellen**: `GROK_TRANSLATE_SANDBOX=read-only`. Het
  opstarten mislukt als de machine hier niet aan kan voldoen, wat het
  gewenste gedrag is.

**Quotum**: de Grok-pool is **wekelijks en gedeeld** met Chat, Imagine en
Voice, en geen enkele opdracht kan deze uitlezen. Een batchverwerking kan dus
je gebruik voor gesprekken verminderen zonder dat dit ergens wordt gemeld — vandaar
een gelijktijdigheidslimiet van 2 en een waarschuwing in `regen_translations.sh`.

Andere variabelen: `GROK_BIN` (pad naar het binaire bestand), `GROK_TIMEOUT` (standaard 900 s).

Voor het opnieuw genereren van de 28 vertalingen:

```bash
# Défaut : Codex sur l'abonnement ChatGPT, modèle qualité gpt-5.6-sol, 0 € à l'usage
./regen_translations.sh --force

# Le modèle éco de Codex, si le volume l'impose
REGEN_MODEL=gpt-5.6-luna ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Une API facturée (openai, gemini, grok, openrouter) est REFUSÉE sans cette dérogation nommée
REGEN_PROVIDER=openai REGEN_ALLOW_PAID_API=1 ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force

# Via OpenRouter : API facturée, donc dérogation ET modèle obligatoires
REGEN_PROVIDER=openrouter REGEN_ALLOW_PAID_API=1 REGEN_MODEL=z-ai/glm-5.2 ./regen_translations.sh --force
```
### Vertalen met OpenCode, naar de provider van uw keuze (`--use_opencode`)

[OpenCode](https://opencode.ai) is een **open source (MIT)** code-agent in de
terminal. Het is geen modelprovider, maar een **router** naar de providers
die u in OpenCode zelf hebt geconfigureerd: een API-sleutel, een abonnement,
de OpenCode Zen-gateway — die gratis modellen **zonder account** aanbiedt — of
een **lokaal** model. Deze provider stuurt `opencode run` aan in niet-interactieve modus
en beperkt de aanroep tot één enkele heen-en-terugronde, zonder enig hulpmiddel.

Twee van deze routes zijn hier van begin tot eind gemeten: de **Zen-gateway** en
**Ollama** lokaal. De andere die OpenCode vermeldt (GitHub Copilot, LM Studio,
llama.cpp) zouden door hun opzet moeten werken, aangezien de provider alleen
met OpenCode communiceert — maar ze zijn niet getest, en deze README vermeldt
alleen wat is geverifieerd.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` is **verplicht**, in de indeling `provider/modèle`. OpenCode is geen
provider en er wordt niet namens u een standaardwaarde gekozen: de eigen fallback
zou een gratis model zijn waarvan de uitwisselingen voor training kunnen worden gebruikt.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Inperking — wat het script bij elke aanroep doet:**

- Een inline configuratie (`OPENCODE_CONFIG_CONTENT`), die voorrang heeft op
  die van u, definieert een agent `aipmt` waarvoor **alle hulpmiddelen worden geweigerd**
  (`permission: { "*": "deny" }`): het model kan niet lezen, schrijven of
  opdrachten uitvoeren — volgens metingen probeert het dat zelfs niet. Het delen van sessies
  is uitgeschakeld, `--pure` sluit externe plugins uit, nooit `--auto`.
- De aanroep draait in een **tijdelijke, lege map**, met de schakelaars
  `OPENCODE_DISABLE_PROJECT_CONFIG` en `OPENCODE_DISABLE_CLAUDE_CODE`: zonder
  deze schakelaars injecteert OpenCode in elke prompt het `AGENTS.md` van de huidige map
  en uw `~/.claude/CLAUDE.md` — volgens metingen werd een instructie om „elk antwoord
  met BANANA af te sluiten” die in een `AGENTS.md` stond, op de vertaling toegepast. De
  algemene regels van `~/.config/opencode/AGENTS.md` blijven daarentegen
  van toepassing: OpenCode staat niet toe ze uit te sluiten.
- Het uitvoercontract vereist tegelijkertijd: exitcode 0, geen gebeurtenis
  `error`, geen aanroep van hulpmiddelen, een laatste stap die is voltooid met `stop`, niet-lege
  tekst en de agent die daadwerkelijk is geladen — een onbekende `--agent` laat OpenCode niet
  mislukken; het **valt stilzwijgend terug** op de codeeragent, met actieve
  hulpmiddelen. Een `exit 0` bewijst hier evenmin iets.
- **Geen enkele aipmt-sleutel wordt doorgegeven** aan het subproces (dezelfde filtering
  als bij Codex en Grok), met één expliciet genoemde uitzondering: `OPENCODE_API_KEY`,
  de sleutel van OpenCode zelf (Zen, Go). Providers worden in
  OpenCode geconfigureerd (`opencode auth login`, `opencode.json`), niet in het `.env` van aipmt.

**Goed om te weten:**

- **De gratis Zen-modellen zijn „stealth”- of bijdragende modellen**,
  veranderlijk, met niet-gedocumenteerde limieten, en hun uitwisselingen kunnen voor
  training worden gebruikt: perfect voor openbare documentatie, te vermijden voor
  privé-inhoud. Gemeten: `opencode/mimo-v2.5-free` vertaalt deze README in één
  doorgang; `opencode/big-pickle` is trager en twee gelijktijdige verzoeken bleven
  er onbeantwoord.
- **Een lokaal model moet een context van minstens 16 k bieden** — de segmenten bevatten
  maximaal 16.000 tekens — terwijl Ollama vaak standaard 4.096
  configureert. Met Ollama: een `Modelfile` met `PARAMETER num_ctx 32768`, daarna
  `ollama create`. De kwaliteit hangt af van het model: een 7B-model keerde een lijst om en
  beschadigde de afsluiting van een codeblok in een testbestand, terwijl een model van
  de gateway alles intact hield.
- `--eco` heeft geen effect (het model is dat van `--model`);
  `--reasoning_effort` wordt ongewijzigd doorgegeven als `--variant` van OpenCode en moet alleen
  worden aangevraagd als het model dit kent.
- Sessies worden door OpenCode vastgelegd in zijn database
  (`~/.local/share/opencode/`), zoals elke OpenCode-sessie.
- Omgevingsvariabelen: `OPENCODE_BIN` (expliciet pad naar het uitvoerbare bestand,
  anders het `PATH` en vervolgens `~/.opencode/bin/opencode`) en `OPENCODE_TIMEOUT`
  (seconden per segment, standaard `600`). `OPENCODE_CONFIG` wordt gerespecteerd als u
  dit exporteert.

**Gemeten voorbeeld: een lokaal model via Ollama** (RTX 3060 12 GB, 62 GB RAM, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # conserve les modèles déjà téléchargés
ollama pull gpt-oss:20b                         # 13 Go, Apache 2.0 — le seul modèle local retenu ici

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

Vervolgens de provider in `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` is geen detail: Ollama schakelt redeneren standaard
in voor deze modellen en een Modelfile kan dit niet uitschakelen. Gemeten via
OpenCode: zonder de optie kost „De kat slaapt op het tapijt” 919 redeneertokens
en 68 s; met de optie 9 tokens.

```bash
aipmt --use_opencode --model ollama/gpt-oss-20b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

Resultaten voor een echt blogartikel van 589 regels (140 links, 21 secties,
3 Engelse citaten beschermd door de modus `--news`), dezelfde opdracht, drie
modellen:

| Model                                    | Duur         | Structuur                                                  | Afwijkingen                                                                                 |
| ---------------------------------------- | ------------ | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free` (Zen, gratis) | 4 min 26 s   | identiek aan de bron                                       | geen                                                                                        |
| `ollama/gemma4-12b-32k` (lokaal)         | 10 min 10 s  | links, URL's, tabellen, tags, vetdruk en inline code identiek | één verzonnen citaatregel (🇺🇸 + parafrase), één dubbele bronvermelding                      |
| `ollama/qwen3.5-9b-32k` (lokaal)         | 8 min 18 s   | links, URL's, tabellen en tags identiek                    | één verzonnen citaatregel, wat toegevoegde vetdruk en inline code, één segment opnieuw verwerkt |

Deze twee lokale modellen zijn sindsdien **afgekeurd**: één vrijheid per artikel
volstaat om een model te diskwalificeren voor gepubliceerde vertalingen. Vijf andere zijn
om dezelfde redenen of wegens een time-out afgekeurd (`gemma4:26b-a4b`,
`qwen3.6:35b-a3b`, `ministral-3:14b`, `mistral-small3.2`, `hy-mt2:7b`). Alleen
`gpt-oss:20b` is behouden — en zelfs dat model laat passages in het Frans staan in
een inhoudelijk rijk artikel; zie de tabel met aanbevolen modellen.

Tijdens de lokale vertaling: GPU op 98% en 170 W, 10 GB VRAM in gebruik
(model en cache van 32 k tokens, niets naar RAM overgeheveld), 7,5 GB RAM voor de
Ollama-server. Een model met 9 tot 12 miljard parameters respecteert de
structuur, maar veroorlooft zich één vrijheid per artikel, terwijl het gatewaymodel
er geen enkele nam: nalezen vóór publicatie of voorbehouden aan concepten.

### Vertalen via OpenRouter (`--use_openrouter`)

OpenRouter is een **router** vóór meer dan 400 modellen die door derden worden gehost,
waarbij het gebruik van één tegoed wordt afgerekend. Met één sleutel biedt het toegang tot modellen
die geen enkele andere provider beschikbaar stelt, waaronder open Chinese modellen.

```bash
# --model est OBLIGATOIRE : aucun défaut n'est choisi à votre place
aipmt --use_openrouter --model 'z-ai/glm-5.2' --file README.md \
  --target_dir . --source_lang fr --target_lang en
```

Twee bijzonderheden van de routering hebben de implementatie bepaald, en beide zijn
meetbaar:

- **Hetzelfde model wordt aangeboden door tientallen hostingproviders met
  verschillende limieten.** Voor `z-ai/glm-5.3-flash` zijn er 23 hostingproviders, waarvan één een limiet van
  2.048 uitvoertokens heeft: zonder voorzorgsmaatregelen werd een lange vertaling in 1 van de 23 gevallen
  afgekapt, willekeurig door de routering en zonder enig signaal. Een preflight leest
  `/api/v1/models/{modèle}/endpoints`, sluit hostingproviders uit met minder dan 8.000
  uitvoertokens of een verminderde status, en zet de overige vervolgens vast met
  `allow_fallbacks: false` — anders schakelt de router weer over naar een
  uitgesloten hostingprovider.
- **Redeneren wordt tegen het uitvoertarief afgerekend.** Hetzelfde verzoek voor
  `z-ai/glm-5.2`, antwoord „OK”: 107 voltooiingstokens met de standaardinstelling van het model,
  2 met redeneren uitgeschakeld. Daarom is het standaard uitgeschakeld voor modellen
  die dat toestaan. Modellen die het verplichten — `reasoning.mandatory`, 288 van de 431
  modellen in de catalogus — krijgen de **laagste inspanning die ze naar eigen opgave
  accepteren**, en niet hun standaardinstelling: die van `z-ai/glm-5.3-flash` is
  `max`, en daarmee raakten de 32.768 uitvoertokens vóór het einde van de
  vertaling uitgeput. Het verhogen van het budget zou niets hebben veranderd, omdat de inspanning er een
  percentage van toewijst. `--reasoning_effort` behoudt voorrang, en `none` bij een model
  dat redeneren verplicht stelt, wordt gemeld in plaats van omzeild.

De preflight is **fail-closed** en toont wat is geselecteerd:

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

Een slug die niet in de catalogus staat, een onbereikbare catalogus of het ontbreken van een hostingprovider
die aan de limiet voldoet, stopt de opdracht vóór enige facturering.

Andere punten:

- Het contextvenster komt uit de catalogus, niet uit een constante: de
  segmentering past zich daar daadwerkelijk aan aan, ook voor modellen met 4.095 tokens.
- `--eco` heeft geen effect (het model is dat van `--model`).
- `finish_reason=length` met lege uitvoer is geen afkapping, maar een
  door het redeneren verbruikt budget; de melding maakt dit duidelijk, omdat beide
  gevallen tegengestelde handelingen vereisen.
- Omgevingsvariabelen: `OPENROUTER_API_KEY` (sleutel, op
  <https://openrouter.ai/keys>), `OPENROUTER_BASE_URL` (standaard
  `https://openrouter.ai/api/v1`, `https://` vereist), `OPENROUTER_TIMEOUT`
  (seconden per aanroep, standaard `900`) en `OPENROUTER_PREFLIGHT_TIMEOUT`
  (standaard `30`).

### Voordelige modus

Gebruikt snellere en goedkopere modellen (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opties

| Optie                    | Beschrijving                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Eén Markdown-bestand om te vertalen                                                                           |
| `--source_dir`           | Bronmap met Markdown-bestanden                                                                                 |
| `--target_dir`           | Uitvoermap voor de vertaalde bestanden                                                                         |
| `--source_lang`          | Brontaal (standaard: `fr`)                                                                          |
| `--target_lang`          | Doeltaal (standaard: `en`)                                                                          |
| `--model`                | Specifiek te gebruiken model                                                                                   |
| `--eco`                  | Voordelige modellen gebruiken                                                                                  |
| `--use_mistral`          | De Mistral AI API gebruiken                                                                                    |
| `--use_claude`           | De Claude API gebruiken                                                                                        |
| `--use_gemini`           | De Gemini API gebruiken                                                                                        |
| `--use_codex`            | De Codex CLI gebruiken met het quotum van het ChatGPT-abonnement                                               |
| `--use_grok`             | De xAI API (Grok) gebruiken — vereist `XAI_API_KEY`                                                          |
| `--use_openrouter`       | OpenRouter gebruiken — vereist `OPENROUTER_API_KEY` en `--model fournisseur/modèle`                              |
| `--use_grok_cli`         | De Grok CLI gebruiken met het quotum van het Grok-abonnement                                                   |
| `--use_opencode`         | OpenCode (open source) gebruiken met de in OpenCode geconfigureerde provider; vereist `--model provider/modèle` |
| `--force`                | Opnieuw vertalen afdwingen                                                                                     |
| `--keep_filename`        | De oorspronkelijke bestandsnaam behouden                                                                       |
| `--news`                 | Nieuwsmodus: beschermt EN-citaten en beheert vlaggen per taal                                                  |
| `--add_translation_note` | Een vertaalnotitie toevoegen                                                                                    |
| `--note_position`        | Positie van de notitie: `top`, `bottom` (standaard) of `both`                         |
| `--note_format`          | Indeling van de notitie: `legacy` (standaard, vetgedrukte alinea) of `marker`                     |
| `--include_model`        | De modelnaam in het uitvoerbestand opnemen                                                                      |
| `--reasoning_effort`     | Redeneerinspanning voor GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

> **De zeven provider-flags sluiten elkaar wederzijds uit.** Het combineren van twee
> werd voorheen stilzwijgend geaccepteerd en koos de eerste die werd getest: een
> vertaling die via een abonnementsquotum was aangevraagd (`--use_codex`, `--use_grok_cli`)
> kon zo zonder enige waarschuwing op gebruiksbasis worden gefactureerd.
> `argparse` weigert de combinatie voortaan.

### Vertaalnotitie: posities en indelingen

Met `--add_translation_note` kan de translator de notitie bovenaan, onderaan of op beide plaatsen zetten en deze als gewone tekstindeling (achterwaarts compatibel) of als door een Markdown-plugin verwerkbare `marker`-indeling weergeven.

**Positie** (`--note_position`):

- `bottom` (standaard): notitie aan het einde van het bestand, zoals vanouds.
- `top`: notitie ingevoegd **na de YAML-frontmatter** (veilig voor Astro Content Collections, gray-matter, enz.).
- `both`: notitie bovenaan EN onderaan ingevoegd (één LLM-aanroep, inhoud hergebruikt voor beide posities).

**Indeling** (`--note_format`):

- `legacy` (standaard): vetgedrukte alinea `**...**` — gedrag volledig identiek aan v1.8, byte voor byte. Compatibel met Hugo, GitHub, GitLab en elke Markdown-renderer.
- `marker`: onzichtbare Markdown-linkreferentiedefinitie (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), gevolgd door een vetgedrukte blockquote. Rechtstreeks leesbaar op GitHub/GitLab en tijdens het buildproces bruikbaar door een remark-plugin aan Astro-zijde om een gestileerde banner te produceren (zie blog jls42.org).

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

| Provider   | Kwaliteit (standaard)                    | Voordelig (`--eco`) |
| ---------- | ---------------------------------------- | --------------------------- |
| OpenAI     | `gpt-5.6-terra`                          | `gpt-5.6-luna`             |
| Claude     | `claude-sonnet-5`                          | `claude-haiku-4-5`             |
| Mistral    | `mistral-large-latest`                          | `mistral-small-latest`             |
| Gemini     | `gemini-3.7-flash`                          | `gemini-3.1-flash-lite`             |
| Codex      | `gpt-5.6-sol`                          | `gpt-5.6-luna`             |
| Grok API   | `grok-4.6`                          | `grok-4.3`             |
| Grok CLI   | `grok-4.6`                          | `grok-4.5`             |
| OpenCode   | `--model provider/modèle` verplicht                | hetzelfde — `--eco` zonder effect |
| OpenRouter | `--model fournisseur/modèle` verplicht                | hetzelfde — `--eco` zonder effect |
## Welke modellen presteren goed

Een model dat een alinea goed vertaalt, behoudt niet noodzakelijk de structuur
van een volledig document. Deze metingen zijn afkomstig van **daadwerkelijk
uitgevoerde vertalingen**, met het commando dat u hierboven zou lezen, op drie
documentverzamelingen en veertien doeltalen: en, es, de, it, pt, nl, pl, sv, ro,
ja, ko, zh, ar, hi.

Twee kolommen, en ze zeggen niet hetzelfde. **Geschreven** telt de voltooide
vertalingen — de beveiligingen van het script tegen stilzwijgende fouten laten
het bestand door. **Zonder afwijking** telt de vertalingen waarvan de structuur
identiek is aan de bron: dezelfde secties, dezelfde links, dezelfde URL's,
dezelfde blokken en inline code, dezelfde tabellen, dezelfde citaten, dezelfde
vlaggen.

### Dicht blogartikel, modus `--news`

589 regels, 140 links, 21 secties, 3 beveiligde Engelse citaten. Dit is het
veeleisendste van de drie documenten: de modus `--news` voegt boven op de
Markdown-structuur beperkingen voor vlaggen en citaten toe.

| Model                             | Toegang            | Geschreven | Zonder afwijking | Mediaan/taal |
| --------------------------------- | ------------------ | ---------- | ---------------- | ------------ |
| `gemini-3.7-flash`                | Google API         | 14/14      | **14/14**        | 1 min 18 s   |
| `gpt-5.6-sol` (`--use_codex`)     | ChatGPT-abonnement | 14/14      | **14/14**        | 11 min 28 s  |
| `z-ai/glm-5.2`                    | OpenRouter         | 14/14      | **14/14**        | 5 min 37 s   |
| `qwen/qwen3.8-flash`              | OpenRouter         | 14/14      | 13/14            | 26 min 23 s  |
| `z-ai/glm-5.3-flash`              | OpenRouter         | 12/14      | 12/14            | 15 min 49 s  |
| `qwen/qwen3.5-27b`                | OpenRouter         | 7/9        | 7/9              | 20 min 33 s  |
| `claude-sonnet-5`                 | Anthropic API      | 14/14      | 11/14            | 6 min 31 s   |
| `opencode/mimo-v2.5-free`         | OpenCode Zen       | 13/14      | 11/14            | 9 min 27 s   |
| `qwen/qwen3.7-flash`              | OpenRouter         | 13/14      | 7/14             | 10 min 09 s  |
| `ollama/gpt-oss-20b-32k`          | lokaal             | 10/14      | 7/14             | 12 min 39 s  |
| `mistral-large-latest`            | Mistral API       | 11/14      | 5/14             | 5 min 32 s   |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter         | 4/14       | 3/14             | 37 min 27 s  |
| `grok-4.6` (`--use_grok_cli`)     | Grok-abonnement    | 1/14       | 1/14             | 23 min 11 s  |
| `moonshotai/kimi-k2.6`            | OpenRouter         | 1/4        | 1/4              | 23 min 00 s  |

Twee reeksen werden **onderbroken wegens onvoldoende tegoed**, wat blijkt uit
hun noemer: `qwen3.5-27b` stopte na negen talen, `kimi-k2.6` na vier — die
laatste na een time-out van veertig minuten en twee weigeringen, tegen bijna
$ 0,33 per taal.

Een methodologische kanttekening bij de OpenRouter-regels: ze werden gemeten met
de **standaardinstellingen van de router**, voordat `--use_openrouter` bestond.
`z-ai/glm-5.2` is sindsdien opnieuw gemeten met de meegeleverde provider, met
redeneren uitgeschakeld, en behaalt exact dezelfde 14/14. `z-ai/glm-5.3-flash` mislukte
tweemaal doordat het uitvoerbudget met de standaardinstelling van de router was
opgebruikt; de provider vraagt deze modellen voortaan om het laagste
redeneerniveau dat ze accepteren, en de controletest voor de problematische
talen slaagt.

### README van dit project, standaard-Markdown

508 regels, 219 inline codes, 40 blokafsluitingen, 45 tabelregels. Hier is geen
modus `--news`: de moeilijkheid komt voort uit de hoge codedichtheid.

| Model                         | Geschreven | Zonder afwijking | Mediaan/taal |
| ----------------------------- | ---------- | ---------------- | ------------ |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14      | 11/14            | 1 min 22 s   |
| `gemini-3.7-flash`            | 14/14      | 13/14            | 21 s         |
| `gpt-5.6-sol` (`--use_codex`) | 14/14      | 12/14            | 2 min 04 s   |
| `opencode/mimo-v2.5-free`     | 9/14       | 7/14             | 3 min 25 s   |
| `ollama/gpt-oss-20b-32k`      | 9/14       | 1/14             | 3 min 38 s   |

### Vier README's van bekende projecten

FastAPI, Ollama, tldr-pages en Vue.js, ongewijzigd overgenomen van GitHub. Deze
documenten zijn **gemakkelijker** dan de vorige twee, en dat blijkt uit de
tabel.

| Model                     | Bereik                     | Geschreven | Zonder afwijking |
| ------------------------- | -------------------------- | ---------- | ---------------- |
| `opencode/mimo-v2.5-free` | 4 projecten × 14 talen      | 55/56      | 47/56            |
| `grok-4.6` (abonnement)   | 4 projecten × ar, hi, ja, zh | 16/16      | 14/16            |
| `ollama/gpt-oss-20b-32k`  | 4 projecten × ar, hi, ja, zh | 15/16      | 9/16             |

### Wat we hieruit leren

- **Drie modellen hebben nooit informatie verloren** in de twee dichte
  documenten: `gemini-3.7-flash`, `gpt-5.6-sol` via het ChatGPT-abonnement en
  `z-ai/glm-5.2` via OpenRouter. Hun enige afwijkingen in de standaardmodus
  zijn een paar niet-overgenomen `**` in één of twee talen, maar
  nooit een URL, codeblok of citaat.
- **De onderscheidende factor is de dichtheid van het document, niet de modus `--news`.**
  Grok via een abonnement mislukt 13 van de 14 keer bij het blogartikel en
  slaagt voor 14 van de 16 openbare README's: de oorzaak is afhaken bij een lang
  segment, bevestigd door een controletest — de geïsoleerde passage wordt
  correct vertaald.
- **Niet-Latijnse schriften vormen niet de verwachte scheidslijn.**
  `gpt-oss` laat Franse passages staan in het Arabisch, Japans, Pools
  **en Roemeens**; Mistral en MiMo verliezen alleen inline code bij
  niet-Latijnse schriften.
- **Het uitschakelen van redeneren kost geen kwaliteit.** `z-ai/glm-5.2`
  verwerkt veertien talen zonder één afwijking onder beide omstandigheden —
  redeneren standaard ingeschakeld door de router en vervolgens uitgeschakeld
  via `--use_openrouter` — met achttien keer minder gefactureerde uitvoertokens.
  Deze meting rechtvaardigt de standaardinstelling van de provider.
- **Een langzaam model is geen veilig model.** `deepseek-v4-flash-0731` doet 37 minuten
  per taal over 4 vertalingen van de 14, `qwen3.8-flash` 26 minuten over een
  bijna perfect resultaat, en Gemini 1 minuut 18 over een foutloos resultaat.

### Wat deze tabel niet is

- **Dit is geen uitputtende ranglijst.** Alleen OpenRouter biedt al meer dan
  vierhonderd modellen aan; hier zijn er ongeveer vijftien gemeten. De
  afwezigheid van een model zegt niets over de kwaliteit ervan, alleen dat het
  niet is getest.
- **Deze metingen hebben een datum**: 4 en 5 september 2026. Modellen veranderen
  onder dezelfde naam, hostingproviders passen quantization en limieten aan, en
  elke week verschijnen er nieuwe modellen.
- **De tijdsduren vormen geen ranglijst.** Afhankelijk van de meetreeks werden
  3 tot 6 vertalingen parallel uitgevoerd, en de verwerkingssnelheid van een
  leverancier varieert gedurende de dag. Ze geven een orde van grootte, geen
  vergelijking.
- **Een resultaat hangt evenzeer af van het document als van het model.**
  Hetzelfde model slaagt voor veertien talen bij een artikel en voor negen bij
  deze README. Uw bestanden zijn niet de onze.
- **De juiste aanpak blijft om zelf te meten**: vertaal een van uw documenten
  naar uw doeltalen en vergelijk vervolgens de structuur — het aantal secties,
  links, afzonderlijke URL's, codeblokken, inline codes en tabelregels. Dat is
  precies wat het bovenstaande protocol doet, en het past in één lus over
  `aipmt`.

## Projecten die dit script gebruiken

- **[jls42.org](https://jls42.org)** - Meertalige persoonlijke blog (15 talen)

## Auteur

Julien LE SAUX
E-mail: contact@jls42.org

## Licentie

GNU GENERAL PUBLIC LICENSE Version 3. Zie [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artikel vertaald van het Frans naar het Nederlands met gpt-5.6-sol.**

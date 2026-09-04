# AI-Powered Markdown-vertaler

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Codekwaliteit</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status van de kwaliteitspoort"></a>
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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Coderegels"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy-badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Vertaler voor Markdown-bestanden die **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** en **Grok (xAI)** gebruikt — via een API, met het quotum van een ChatGPT- (Codex) of Grok-abonnement zonder facturering per gebruik, of via **OpenCode**, de open-source-agent, met de provider van uw keuze: lokaal model (Ollama), gratis, abonnement (GitHub Copilot…) of sleutel.

Dit Python-script vertaalt Markdown-bestanden van een brontaal naar een doeltaal, met behoud van de opmaak, codeblokken en frontmatter-metadata.

## Belangrijkste kenmerken

- **Multi-Provider**: 5 API's (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLI's via een abonnement, zonder facturering per gebruik — Codex (ChatGPT) en Grok — + OpenCode (open source, MIT) voor elke in OpenCode geconfigureerde provider, inclusief een lokaal model
- **Modellen van 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
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

De opdracht `aipmt` is dan overal beschikbaar. Als de map met Python-scripts
niet in uw `PATH` staat, doet `python -m aipmt` precies hetzelfde.
Python 3.10 of nieuwer.

Voor een installatie die van de rest van uw pakketten is geïsoleerd:

```bash
pipx install ai-powered-markdown-translator
```

### Om aan het project bij te dragen

De gekloonde repository blijft nodig voor ontwikkeling: daar bevinden zich de tests,
de 28 vertalingen en alle kwaliteitstools.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` is een **volledig vastgezette lockfile**, een exacte weergave van
de geteste omgeving. De bereiken die in `pyproject.toml` zijn gepubliceerd, zijn
bewust ruimer: ze leggen uw andere pakketten niets op.

### Kwaliteitstools (optioneel maar aanbevolen)

Het project gebruikt [`pre-commit`](https://pre-commit.com) om te voorkomen dat slecht opgemaakte, kwetsbare code of code met een geheim wordt gecommit. Installatie:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Actieve hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexiteit), detect-secrets (API-sleutels), mypy (geleidelijke typering), Opengrep (SAST), pip-audit (CVE's in afhankelijkheden), unittest. Zie `CLAUDE.md`, sectie _Quality / pre-commit_, voor details.

## Configuratie

De sleutels worden op **drie locaties** gezocht, van de hoogste naar de laagste
prioriteit. Elke locatie vult alleen in wat bij de vorige nog ontbreekt.

|     | Waar                                          | Waarvoor                                      |
| --- | --------------------------------------------- | --------------------------------------------- |
| 1   | Omgevingsvariabelen                           | CI, containers, tijdelijke uitzondering       |
| 2   | `.env` van de huidige map (of een bovenliggende map) | een projectspecifieke sleutel                  |
| 3   | `~/.config/aipmt/.env`                        | **eenmaal geïnstalleerd, overal geldig**       |

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

Dit bestand volgt `XDG_CONFIG_HOME` wanneer de variabele naar een absoluut pad verwijst
(anders wordt ze genegeerd, zoals de specificatie voorschrijft), en `%APPDATA%`
onder Windows.

De tweede optie blijft nuttig wanneer een repository een eigen sleutel heeft: een
`.env` in de hoofdmap daarvan heeft dan voorrang op de gebruikersconfiguratie,
zonder die te wijzigen. En een variabele die al in de omgeving is gedefinieerd,
heeft voorrang op beide:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Als er geen sleutel wordt gevonden, toont de opdracht geen stacktrace: ze vermeldt
de drie locaties met hun exacte pad.

`GEMINI_API_KEY` wordt als alternatief voor `GOOGLE_API_KEY` geaccepteerd (AI
Studio-conventie). Optionele variabelen: `XAI_BASE_URL` (xAI-endpoint, standaard
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (seconden per Anthropic-aanroep, standaard
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (zie de sectie over Grok CLI) en `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (zie de sectie over OpenCode). Voor
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

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### Vertalen via uw ChatGPT-abonnement (`--use_codex`)

Deze provider gebruikt geen API-sleutel: hij bestuurt de officiële Codex CLI in
niet-interactieve modus, zodat de vertaling wordt afgetrokken van het quotum van
het reeds betaalde ChatGPT-abonnement (Plus, Pro, Business…). Dit is de enige door
OpenAI gedocumenteerde methode voor dit gebruik — de tokens van `~/.codex/auth.json`
authenticeren geen aanroepen naar de Platform API en worden bovendien nooit door
dit script gelezen.

**Vereisten:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Het uitvoerbare bestand wordt in deze volgorde gezocht: de variabele `CODEX_BIN`,
het `PATH` en vervolgens het Python-pakket `openai-codex-cli-bin`. Dat laatste staat
bewust niet in `requirements.txt`: het is ongeveer 250 MB groot, wat anders aan alle
gebruikers zou worden opgelegd voor een optionele provider.

**Goed om te weten:**

- **Er wordt geen API-sleutel gebruikt.** `OPENAI_API_KEY` en `CODEX_API_KEY` worden
  uit de omgeving van het subprocess verwijderd. Dit garandeert dat een sleutel
  in `.env` de vertaling nooit ongemerkt laat overschakelen naar
  facturering per gebruik.
- **Eén segment = één ‘lokaal bericht’** binnen het venster van 5 uur van het abonnement.
  Gebruik `--eco` (model `gpt-5.6-luna`, 250-2.000 berichten/5 uur met Plus)
  in plaats van het kwaliteitsmodel (`gpt-5.6-sol`, 10-100 berichten/5 uur).
- **Langzamer** dan een API-aanroep: reken op ongeveer 45 s voor een volledige README,
  tegenover enkele seconden bij een rechtstreekse aanroep.
- **Geweigerd in CI** (wanneer `CI` of `GITHUB_ACTIONS` is ingesteld):
  authenticatie via een abonnement is niet bedoeld voor een gedeelde runner en
  OpenAI raadt deze workflow af voor openbare repositories. Gebruik hiervoor een API-sleutel.
- Omgevingsvariabelen: `CODEX_BIN` (expliciet pad naar het uitvoerbare bestand) en
  `CODEX_TIMEOUT` (seconden per segment, standaard `600`).

### Vertalen via uw Grok-abonnement (`--use_grok_cli`)

Hetzelfde principe als `--use_codex`, met de officiële **Grok Build** CLI: de
vertaling wordt afgetrokken van het Grok-abonnement (SuperGrok / X Premium+) in
plaats van per token te worden gefactureerd.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Isolatie — lees dit vóór gebruik.** Deze provider is structureel **zwakker**
dan `--use_codex`, en dat is een bewuste keuze:

- Codex draait in `--sandbox read-only`, een door het systeem opgelegde grens.
- De sandbox van Grok **kan niet worden toegepast** op veel recente Linux-systemen:
  AppArmor blokkeert sinds Ubuntu 24.04 niet-geprivilegieerde user namespaces,
  en de deny-list voor sockets van de container-runtime faalt als
  `/run/podman` in `0700` staat. Een **ingebouwd** profiel dat niet kan
  worden toegepast, start echter **stilzwijgend zonder isolatie**.
- Het script vraagt daarom standaard geen profiel aan en **valt nooit
  stilzwijgend terug**: het toont een waarschuwing. De isolatie berust op de
  `--deny`-regels van de CLI (waaronder de catch-all `*`), de enige
  gemeten _fail-closed_-laag — een onbekende regel verhindert het starten in plaats
  van de bescherming zonder melding te verwijderen.
- Om de OS-sandbox **verplicht te stellen**: `GROK_TRANSLATE_SANDBOX=read-only`.
  Het starten mislukt als de machine hieraan niet kan voldoen, wat het gewenste
  gedrag is.

**Quotum**: de Grok-pool is **wekelijks en gedeeld** met Chat, Imagine en
Voice, en geen enkele opdracht kan deze uitlezen. Een batchverwerking kan dus uw
conversatiegebruik verminderen zonder dat dit ergens wordt gemeld — vandaar een
gelijktijdigheidslimiet van 2 en een waarschuwing in `regen_translations.sh`.

Andere variabelen: `GROK_BIN` (pad naar het uitvoerbare bestand), `GROK_TIMEOUT` (standaard 900 s).

Voor het opnieuw genereren van de 28 vertalingen:

```bash
# Défaut : Codex sur l'abonnement ChatGPT, modèle qualité gpt-5.6-sol, 0 € à l'usage
./regen_translations.sh --force

# Le modèle éco de Codex, si le volume l'impose
REGEN_MODEL=gpt-5.6-luna ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Une API facturée (openai, gemini, grok) est REFUSÉE sans cette dérogation nommée
REGEN_PROVIDER=openai REGEN_ALLOW_PAID_API=1 ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
```

### Vertalen met OpenCode, via de provider van uw keuze (`--use_opencode`)

[OpenCode](https://opencode.ai) is een **open-source (MIT)** coding agent voor de
terminal. Het is geen modelprovider, maar een **router** naar de providers die
u in OpenCode zelf hebt geconfigureerd: een API-sleutel, een abonnement
(GitHub Copilot, ChatGPT, SuperGrok), de OpenCode Zen-gateway — die gratis
modellen **zonder account** aanbiedt — of een **lokaal** model (Ollama, LM Studio,
llama.cpp). Deze provider bestuurt `opencode run` in niet-interactieve modus en
beperkt de aanroep tot één enkele heen-en-teruginteractie, zonder tools.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` is **verplicht**, met de indeling `provider/modèle`. OpenCode is geen
provider en er wordt geen standaardkeuze voor u gemaakt: zijn eigen fallback
zou een gratis model zijn waarvan de uitwisselingen voor training kunnen worden gebruikt.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Isolatie — wat het script bij elke aanroep doet:**

- Een inline configuratie (`OPENCODE_CONFIG_CONTENT`), die voorrang heeft op die van
  u, definieert een agent `aipmt` waarvoor **alle tools worden geweigerd**
  (`permission: { "*": "deny" }`): het model kan niets lezen of schrijven en
  geen opdrachten uitvoeren — uit metingen blijkt dat het dit zelfs niet probeert.
  Het delen van sessies is uitgeschakeld, `--pure` sluit externe plugins uit,
  nooit `--auto`.
- De aanroep draait in een **lege tijdelijke map**, met de schakelaars
  `OPENCODE_DISABLE_PROJECT_CONFIG` en `OPENCODE_DISABLE_CLAUDE_CODE`: zonder
  deze schakelaars injecteert OpenCode in elke prompt het `AGENTS.md` van de huidige
  map en uw `~/.claude/CLAUDE.md` — uit metingen bleek dat een instructie ‘eindig elk antwoord
  met BANANA’ in een `AGENTS.md` op de vertaling werd toegepast. De algemene
  regels van `~/.config/opencode/AGENTS.md` blijven daarentegen
  van toepassing: OpenCode laat niet toe ze uit te schakelen.
- Het uitvoercontract vereist alles tegelijk: exitcode 0, geen gebeurtenis
  `error`, geen toolaanroep, een laatste stap die eindigt met `stop`,
  niet-lege tekst en dat de agent daadwerkelijk is geladen — bij een onbekende
  `--agent` laat OpenCode de uitvoering niet mislukken, maar **valt het
  stilzwijgend terug** op de coding agent, met actieve tools. Ook een
  `exit 0` bewijst hier niets.
- **Geen enkele aipmt-sleutel wordt doorgegeven** aan het subprocess (dezelfde
  filtering als bij Codex en Grok), met één expliciete uitzondering:
  `OPENCODE_API_KEY`, de sleutel van OpenCode zelf (Zen, Go). Providers worden in
  OpenCode geconfigureerd (`opencode auth login`, `opencode.json`), niet in het
  `.env` van aipmt.

**Goed om te weten:**

- **De gratis modellen van Zen zijn ‘stealth’- of bijdragende modellen**,
  die veranderen, ongedocumenteerde limieten hebben en waarvan de uitwisselingen
  voor training kunnen worden gebruikt: ideaal voor openbare documentatie, maar
  te vermijden voor privé-inhoud. Gemeten: `opencode/mimo-v2.5-free` vertaalt deze README
  in één passage; `opencode/big-pickle` is langzamer en twee gelijktijdige verzoeken
  bleven daarbij onbeantwoord.
- **Een lokaal model moet minstens 16k context bieden** — segmenten kunnen
  tot 16.000 tekens bevatten — terwijl Ollama vaak standaard 4.096 configureert.
  Met Ollama: een `Modelfile` met `PARAMETER num_ctx 32768`, gevolgd door
  `ollama create`. De kwaliteit hangt af van het model: een 7B-model keerde een
  lijst om en beschadigde de afsluiting van een codeblok in een testbestand,
  terwijl een gatewaymodel alles intact hield.
- `--eco` heeft geen effect (het model is dat van `--model`);
  `--reasoning_effort` wordt ongewijzigd doorgegeven als `--variant` van OpenCode en
  moet alleen worden aangevraagd als het model dit kent.
- Sessies worden door OpenCode in zijn database vastgelegd
  (`~/.local/share/opencode/`), net als elke andere OpenCode-sessie.
- Omgevingsvariabelen: `OPENCODE_BIN` (expliciet pad naar het uitvoerbare bestand,
  anders het `PATH` en vervolgens `~/.opencode/bin/opencode`) en `OPENCODE_TIMEOUT`
  (seconden per segment, standaard `600`). `OPENCODE_CONFIG` wordt
  gerespecteerd als u die exporteert.

**Gemeten voorbeeld: een lokaal model via Ollama** (RTX 3060 12 GB, 62 GB RAM, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # Ollama ≥ 0.30 pour gemma4 ; conserve les modèles déjà téléchargés
ollama pull gemma4:12b                          # 7,6 Go, Apache 2.0, 140+ langues
ollama pull qwen3.5:9b                          # 6,6 Go, Apache 2.0, 201 langues

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gemma4:12b\nPARAMETER num_ctx 32768\n' > gemma4-12b-32k.Modelfile
ollama create gemma4-12b-32k -f gemma4-12b-32k.Modelfile
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
        "gemma4-12b-32k": {
          "name": "Gemma 4 12B (32k, sans réflexion)",
          "limit": { "context": 32768, "output": 8192 },
          "options": { "reasoningEffort": "none" }
        }
      }
    }
  }
}
```

`reasoningEffort: "none"` is geen detail: Ollama schakelt redeneren standaard in
voor Gemma 4 en Qwen 3.5, en een Modelfile kan dit niet uitschakelen. Gemeten via
OpenCode: zonder de optie kost ‘De kat slaapt op het tapijt’ 919 redeneertokens
en 68 s; met de optie 9 tokens.

```bash
aipmt --use_opencode --model ollama/gemma4-12b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

Resultaten voor een echt blogartikel van 589 regels (140 links, 21 secties,
3 Engelse citaten beschermd door de modus `--news`), met dezelfde opdracht
en drie modellen:

| Model                                    | Duur         | Structuur                                                     | Afwijkingen                                                                                      |
| ---------------------------------------- | ------------ | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `opencode/mimo-v2.5-free` (Zen, gratis) | 4 min 26 s   | identiek aan de bron                                          | geen                                                                                             |
| `ollama/gemma4-12b-32k` (lokaal)        | 10 min 10 s  | links, URL's, tabellen, tags, vet en inline code identiek      | één verzonnen citaatregel (🇺🇸 + parafrase), één dubbele bronvermelding                           |
| `ollama/qwen3.5-9b-32k` (lokaal)        | 8 min 18 s   | links, URL's, tabellen en tags identiek                        | één verzonnen citaatregel, enkele toegevoegde vetgedrukte teksten en inline codes, één segment opnieuw verwerkt |

Tijdens de lokale vertaling: GPU op 98% en 170 W, 10 GB VRAM in gebruik
(model en cache van 32k tokens, niets naar RAM overgeheveld), 7,5 GB RAM voor de
Ollama-server. Een model met 9 tot 12 miljard parameters respecteert de
structuur, maar neemt zich per artikel één vrijheid, terwijl het gatewaymodel
zich geen enkele vrijheid permitteerde: nalezen vóór publicatie of alleen voor
concepten gebruiken.

### Voordelige modus

Gebruikt snellere en goedkopere modellen (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### Opties

| Optie                   | Beschrijving                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Eén Markdown-bestand om te vertalen                                                                            |
| `--source_dir`           | Bronmap met de Markdown-bestanden                                                             |
| `--target_dir`           | Uitvoermap voor de vertaalde bestanden                                                               |
| `--source_lang`          | Brontaal (standaard: `fr`)                                                                                  |
| `--target_lang`          | Doeltaal (standaard: `en`)                                                                                   |
| `--model`                | Specifiek te gebruiken model                                                                                  |
| `--eco`                  | Voordelige modellen gebruiken                                                                              |
| `--use_mistral`          | De Mistral AI-API gebruiken                                                                                     |
| `--use_claude`           | De Claude-API gebruiken                                                                                         |
| `--use_gemini`           | De Gemini-API gebruiken                                                                                         |
| `--use_codex`            | De Codex CLI gebruiken via het quotum van het ChatGPT-abonnement                                                    |
| `--use_grok`             | De xAI-API (Grok) gebruiken — vereist `XAI_API_KEY`                                                           |
| `--use_grok_cli`         | De Grok CLI gebruiken via het quotum van het Grok-abonnement                                                        |
| `--use_opencode`         | OpenCode (open source) gebruiken met de in OpenCode geconfigureerde provider; vereist `--model provider/modèle` |
| `--force`                | Opnieuw vertalen afdwingen                                                                                       |
| `--keep_filename`        | De oorspronkelijke bestandsnaam behouden                                                                          |
| `--news`                 | Nieuwsmodus: beschermt Engelse citaten en beheert vlaggen per taal                                      |
| `--add_translation_note` | Een vertaalnotitie toevoegen                                                                                |
| `--note_position`        | Positie van de notitie: `top`, `bottom` (standaard) of `both`                                                     |
| `--note_format`          | Indeling van de notitie: `legacy` (standaard, vetgedrukte alinea) of `marker`                                            |
| `--include_model`        | De modelnaam opnemen in het uitvoerbestand                                                            |
| `--reasoning_effort`     | Redeneerinspanning van GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

> **De zeven provider-flags sluiten elkaar wederzijds uit.** Het combineren van twee
> werd voorheen stilzwijgend geaccepteerd en leidde tot het eerste geteste exemplaar: een
> vertaling die via een abonnementsquotum was aangevraagd (`--use_codex`, `--use_grok_cli`)
> kon daardoor zonder enige waarschuwing op basis van gebruik worden gefactureerd.
> `argparse` weigert deze combinatie voortaan.

### Vertaalnotitie: posities en indelingen

Met `--add_translation_note` kan de translator de notitie bovenaan, onderaan of op beide plaatsen zetten en deze weergeven als eenvoudige tekst (achterwaarts compatibel) of in een `marker`-indeling die door een Markdown-plugin kan worden verwerkt.

**Positie** (`--note_position`):

- `bottom` (standaard): notitie aan het einde van het bestand, zoals vanouds.
- `top`: notitie ingevoegd **na de YAML-frontmatter** (veilig voor Astro Content Collections, gray-matter enz.).
- `both`: notitie zowel bovenaan ALS onderaan ingevoegd (één LLM-aanroep, inhoud hergebruikt voor beide plaatsingen).

**Indeling** (`--note_format`):

- `legacy` (standaard): vetgedrukte alinea `**...**` — exact hetzelfde gedrag als v1.8, byte-for-byte. Compatibel met Hugo, GitHub, GitLab en elke Markdown-renderer.
- `marker`: onzichtbare Markdown-linkreferentiedefinitie (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), gevolgd door een vetgedrukt blockquote. Standaard leesbaar op GitHub/GitLab en tijdens het buildproces te verwerken door een remark-plugin aan de Astro-kant om een gestileerde banner te produceren (zie blog jls42.org).

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

| Provider | Kwaliteit (standaard)                      | Voordelig (`--eco`)      |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI   | `gpt-5.6-terra`                       | `gpt-5.6-luna`            |
| Claude   | `claude-sonnet-5`                     | `claude-haiku-4-5`        |
| Mistral  | `mistral-large-latest`                | `mistral-small-latest`    |
| Gemini   | `gemini-3.7-flash`                    | `gemini-3.1-flash-lite`   |
| Codex    | `gpt-5.6-sol`                         | `gpt-5.6-luna`            |
| Grok API | `grok-4.6`                            | `grok-4.3`                |
| Grok CLI | `grok-4.6`                            | `grok-4.5`                |
| OpenCode | `--model provider/modèle` verplicht | hetzelfde — `--eco` zonder effect |

> **Aanbeveling voor long-formvertalingen**: `--use_gemini` (standaard = `gemini-3.7-flash`) behoudt de Markdown-structuur getrouw voor niet-Latijnse schriften (PL, JA, ZH, AR, HI), ook in de modus `--news`, waarin de betrouwbaarheid van placeholders telt. Gemeten op deze naar het Japans vertaalde README: dezelfde structuur als `gemini-3.1-pro-preview` (21 lijsten, 18 codeblokken, 13 HTML-links, 13 afbeeldingen, alle URL's behouden) met ongeveer 6x minder latentie. OpenAI blijft de standaard voor achterwaartse compatibiliteit.

## Projecten die dit script gebruiken

- **[jls42.org](https://jls42.org)** - Meertalige persoonlijke blog (15 talen)

## Auteur

Julien LE SAUX
E-mail: contact@jls42.org

## Licentie

GNU GENERAL PUBLIC LICENSE versie 3. Zie [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artikel vertaald van het Frans naar het Nederlands met gpt-5.6-sol.**

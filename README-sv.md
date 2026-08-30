# AI-driven Markdown-översättare

🌍 [Franska](README.md) | [Engelska](README-en.md) | [Spanska](README-es.md) | [Kinesiska](README-zh.md) | [Tyska](README-de.md) | [Japanska](README-ja.md) | [Koreanska](README-ko.md) | [Arabiska](README-ar.md) | [Hindi](README-hi.md) | [Italienska](README-it.md) | [Nederländska](README-nl.md) | [Polska](README-pl.md) | [Portugisiska](README-pt.md) | [Rumänska](README-ro.md) | [Svenska](README-sv.md)

<h4 align="center">📊 Kodkvalitet</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status för kvalitetsgrind"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Säkerhetsbetyg"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Tillförlitlighetsbetyg"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Underhållbarhetsbetyg"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Täckning"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Sårbarheter"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Buggar"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Kodlukt"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Duplicerade rader (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Teknisk skuld"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Kodrader"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy-märke"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Översättare för Markdown-filer som använder **OpenAI**, **Mistral AI**, **Claude (Anthropic)** och **Google Gemini**.

Det här Python-skriptet översätter Markdown-filer från ett källspråk till ett målspråk samtidigt som formatering, kodblock och front matter-metadata bevaras.

## Huvudfunktioner

- **Flera providers**: Stöd för 4 API:er (OpenAI, Mistral, Claude, Gemini) samt Codex CLI via ett ChatGPT-abonnemang
- **2026-modeller**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Ekonomiläge**: Alternativet `--eco` för att använda snabbare och billigare modeller
- **Enskild fil**: Alternativet `--file` för att översätta en enda fil
- **Intelligent segmentering**: Hantering av långa texter med tokengränser per modell
- **Bevarande av kod**: Både kodblock OCH inline-kod (`` `...` ``) bevaras
- **Filnamn**: Alternativet `--keep_filename` för att behålla det ursprungliga namnet
- **Nyhetsläge**: Alternativet `--news` för att skydda engelska citat och hantera flaggor i nyhetsartiklar
- **.env-konfiguration**: Stöd för filen `.env` för API-nycklar
- **Översättningsnotis**: Valfri notis i slutet av dokumentet

## Installation

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Kvalitetsverktyg (valfritt men rekommenderat)

Projektet använder [`pre-commit`](https://pre-commit.com) för att förhindra att felaktigt formaterad eller sårbar kod, eller kod som innehåller en hemlighet, committas. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktiva hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (komplexitet), detect-secrets (API-nycklar), mypy (progressiv typning), Opengrep (SAST), pip-audit (CVE-beroenden), unittest. Se avsnittet _Quality / pre-commit_ i `CLAUDE.md` för mer information.

## Konfiguration

Skapa en fil med namnet `.env` i projektets rotkatalog eller ange miljövariablerna:

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

`GEMINI_API_KEY` godtas som alternativ till `GOOGLE_API_KEY` (AI
Studio-konvention). Valfria variabler: `XAI_BASE_URL` (xAI-endpoint, standardvärde
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (sekunder per Anthropic-anrop, standardvärde
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`
och `GROK_TRANSLATE_SANDBOX` (se avsnittet Grok CLI). För
`regen_translations.sh`: `REGEN_PROVIDER`, `REGEN_MODEL` och
`REGEN_JOB_TIMEOUT` (gräns per jobb, standardvärde 600 s).

## Användning

### Översätta en enskild fil

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Översätta en katalog

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

### Översätta via ditt ChatGPT-abonnemang (`--use_codex`)

Denna provider använder ingen API-nyckel: den styr den officiella Codex CLI-klienten i
icke-interaktivt läge, så översättningen räknas av från kvoten i det redan betalda
ChatGPT-abonnemanget (Plus, Pro, Business…). Detta är det enda sätt som dokumenterats av
OpenAI för detta användningsområde — tokens från `~/.codex/auth.json` autentiserar inte
anrop till API Platform och läses dessutom aldrig av det här skriptet.

**Förutsättningar:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Binärfilen söks i följande ordning: variabeln `CODEX_BIN`, `PATH`
och därefter Python-paketet `openai-codex-cli-bin`. Det sistnämnda ingår avsiktligt
inte i `requirements.txt`: det är cirka 250 MB stort, vilket annars skulle belasta alla
användare för en valfri provider.

**Bra att veta:**

- **Ingen API-nyckel används.** `OPENAI_API_KEY` och `CODEX_API_KEY`
  tas bort från underprocessens miljö, vilket garanterar att en nyckel
  i `.env` aldrig gör att översättningen övergår till
  användningsbaserad debitering.
- **Ett segment = ett ”lokalt meddelande”** i planens femtimmarsfönster.
  Använd `--eco` (modellen `gpt-5.6-luna`, 250–2 000 meddelanden/5 h med Plus)
  i stället för kvalitetsmodellen (`gpt-5.6-sol`, 10–100 meddelanden/5 h).
- **Långsammare** än ett API-anrop: räkna med cirka 45 s för en fullständig README,
  jämfört med några sekunder direkt.
- **Avvisas i CI** (om `CI` eller `GITHUB_ACTIONS` har angetts):
  abonnemangsautentisering är inte avsedd för en delad runner, och OpenAI avråder från
  detta arbetsflöde i offentliga repositories. Använd en API-nyckel för denna väg.
- Miljövariabler: `CODEX_BIN` (explicit sökväg till binärfilen) och
  `CODEX_TIMEOUT` (sekunder per segment, standardvärde `600`).

### Översätta via ditt Grok-abonnemang (`--use_grok_cli`)

Samma princip som för `--use_codex`, med den officiella CLI-klienten **Grok Build**:
översättningen räknas av från Grok-abonnemanget (SuperGrok/X Premium+) i stället
för att debiteras per token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Isolering – läs före användning.** Denna provider är strukturellt **svagare**
än `--use_codex`, och det är ett medvetet val:

- Codex körs i `--sandbox read-only`, en gräns som upprätthålls av systemet.
- Groks sandbox **kan inte tillämpas** på många moderna Linux-datorer:
  AppArmor blockerar oprivilegierade user namespaces sedan Ubuntu
  24.04, och deny-listan för sockets till container-runtime misslyckas om
  `/run/podman` finns i `0700`. En **inbyggd** profil som inte kan
  tillämpas startar dock **oisolerad utan att meddela det**.
- Skriptet begär därför ingen profil som standard och **faller aldrig tillbaka
  utan att meddela det**: det visar en varning. Isoleringen bygger på CLI-klientens
  `--deny`-regler (inklusive catch-all-regeln `*`), det enda lager som
  har uppmätts som _fail-closed_ – en okänd regel gör att starten avvisas i stället
  för att skyddet tas bort utan förvarning.
- För att **kräva** operativsystemets sandbox: `GROK_TRANSLATE_SANDBOX=read-only`.
  Starten misslyckas om datorn inte kan uppfylla kravet, vilket är det
  avsedda beteendet.

**Kvot**: Grok-poolen är **veckovis och delas** med Chat, Imagine och
Voice, och det finns inget kommando för att läsa av den. En batchbearbetning kan därför
minska din tillgängliga konversationsanvändning utan att något meddelar det – därför
begränsas samtidigheten till 2 och en varning visas i `regen_translations.sh`.

Andra variabler: `GROK_BIN` (sökväg till binärfilen), `GROK_TIMEOUT` (standardvärde 900 s).

För att generera de 28 översättningarna på nytt:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### Ekonomiläge

Använder snabbare och billigare modeller (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Alternativ

| Alternativ                | Beskrivning                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Enskild Markdown-fil som ska översättas                                  |
| `--source_dir`           | Källkatalog som innehåller Markdown-filer                                |
| `--target_dir`           | Utdatakatalog för de översatta filerna                                   |
| `--source_lang`          | Källspråk (standardvärde: `fr`)                                |
| `--target_lang`          | Målspråk (standardvärde: `en`)                                 |
| `--model`                | Specifik modell som ska användas                                         |
| `--eco`                  | Använd ekonomimodeller                                                   |
| `--use_mistral`          | Använd Mistral AI API                                                    |
| `--use_claude`           | Använd Claude API                                                        |
| `--use_gemini`           | Använd Gemini API                                                        |
| `--use_codex`            | Använd Codex CLI med kvoten för ChatGPT-abonnemanget                     |
| `--use_grok`             | Använd xAI API (Grok) – kräver `XAI_API_KEY`                            |
| `--use_grok_cli`         | Använd Grok CLI med kvoten för Grok-abonnemanget                         |
| `--force`                | Tvinga fram en ny översättning                                           |
| `--keep_filename`        | Behåll det ursprungliga filnamnet                                        |
| `--news`                 | Nyhetsläge: skyddar engelska citat och hanterar flaggor per språk        |
| `--add_translation_note` | Lägg till en översättningsnotis                                          |
| `--note_position`        | Notisens position: `top`, `bottom` (standardvärde) eller `both` |
| `--note_format`          | Notisens format: `legacy` (standardvärde, fetstilt stycke) eller `marker` |
| `--include_model`        | Inkludera modellnamnet i utdatafilen                                     |
| `--reasoning_effort`     | Resonemangsnivå för GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

> **De sex provider-flaggorna utesluter varandra.** Tidigare accepterades en
> kombination av två utan något meddelande och den först testade användes: en
> översättning som begärts med abonnemangskvoten (`--use_codex`, `--use_grok_cli`)
> kunde därför övergå till användningsbaserad debitering utan någon varning.
> `argparse` avvisar numera kombinationen.

### Översättningsnotis: positioner och format

Med `--add_translation_note` kan översättaren placera notisen högst upp, längst ned eller på båda ställena och visa den antingen i enkelt textformat (bakåtkompatibelt) eller i formatet `marker`, som kan användas av ett Markdown-plugin.

**Position** (`--note_position`):

- `bottom` (standardvärde): notis i slutet av filen, som tidigare.
- `top`: notis som infogas **efter YAML-front matter** (säkert för Astro Content Collections, gray-matter osv.).
- `both`: notis som infogas både högst upp OCH längst ned (ett enda LLM-anrop, vars innehåll återanvänds på båda platserna).

**Format** (`--note_format`):

- `legacy` (standardvärde): fetstilt stycke `**...**` – beteendet är exakt identiskt med v1.8, byte för byte. Kompatibelt med Hugo, GitHub, GitLab och alla Markdown-renderare.
- `marker`: osynlig Markdown-definition av en länkreferens (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), följd av ett fetstilt blockcitat. Kan läsas direkt på GitHub/GitLab och användas vid build av ett remark-plugin i Astro för att skapa en stiliserad banner (se bloggen jls42.org).

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

### Standardmodeller (2026)

| Provider | Kvalitet (standardvärde) | Ekonomi (`--eco`) |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **Rekommendation för långa översättningar**: `--use_gemini` (standardvärde = `gemini-3.7-flash`) bevarar Markdown-strukturen korrekt för icke-latinska skriftsystem (PL, JA, ZH, AR, HI), även i läget `--news` där platshållarnas exakthet är viktig. Uppmätt med denna README översatt till japanska: samma struktur som med `gemini-3.1-pro-preview` (21 listor, 18 kodblock, 13 HTML-länkar, 13 bilder och alla URL:er bevarade) med cirka 6 gånger kortare latens. OpenAI förblir standardvalet för bakåtkompatibilitet.

## Projekt som använder detta skript

- **[jls42.org](https://jls42.org)** – Flerspråkig personlig blogg (15 språk)

## Författare

Julien LE SAUX
E-post: contact@jls42.org

## Licens

GNU GENERAL PUBLIC LICENSE Version 3. Se [LICENSE](LICENSE).

**Artikel översatt från franska till svenska med gpt-5.6-sol.**

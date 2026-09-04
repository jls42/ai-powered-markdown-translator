# AI-driven Markdown-översättare

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Kodkvalitet</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status för Quality Gate"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Säkerhetsklassning"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Tillförlitlighetsklassning"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Underhållbarhetsklassning"></a>
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

Översättare av Markdown-filer som använder **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** och **Grok (xAI)** — via API, på kvoten för en ChatGPT-prenumeration (Codex) eller Grok utan användningsbaserad debitering, eller via **OpenCode**, open source-agenten, till valfri leverantör: lokal modell (Ollama), kostnadsfri, prenumeration (GitHub Copilot…) eller nyckel.

Detta Python-skript översätter Markdown-filer från ett källspråk till ett målspråk samtidigt som formatering, kodblock och front matter-metadata bevaras.

## Huvudfunktioner

- **Multi-Provider**: 5 API:er (OpenAI, Mistral, Claude, Gemini, Grok) + 2 prenumerationsbaserade CLI:er utan användningsbaserad debitering — Codex (ChatGPT) och Grok — + OpenCode (open source, MIT) till valfri leverantör som konfigurerats i OpenCode, inklusive en lokal modell
- **Modeller 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Ekonomiskt läge**: Alternativet `--eco` för att använda snabbare och billigare modeller
- **Enskild fil**: Alternativet `--file` för att översätta en enda fil
- **Intelligent segmentering**: Hantering av långa texter med tokenbegränsningar per modell
- **Kodbevarande**: Kodblock OCH inline-kod (`` `...` ``) bevaras
- **Filnamn**: Alternativet `--keep_filename` för att behålla originalnamnet
- **News-läge**: Alternativet `--news` för att skydda engelska citat och hantera flaggor i nyhetsartiklar
- **.env-konfiguration**: Stöd för filen `.env` för API-nycklar
- **Översättningsnotis**: Valfritt tillägg av en notis i slutet av dokumentet

## Installation

### Använda verktyget

```bash
pip install ai-powered-markdown-translator
```

Kommandot `aipmt` är då tillgängligt överallt. Om katalogen med
Python-skript inte finns i din `PATH`, gör `python -m aipmt` exakt samma
sak. Python 3.10 eller senare.

För en isolerad installation, separat från dina övriga paket:

```bash
pipx install ai-powered-markdown-translator
```

### Bidra till projektet

Det klonade arkivet behövs fortfarande för utveckling: det är där testerna,
de 28 översättningarna och alla kvalitetsverktyg finns.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` är en **helt låst lock-fil**, en exakt spegling av den testade
miljön. Gränserna som publiceras i `pyproject.toml` är medvetet bredare:
de ställer inga krav på dina övriga paket.

### Kvalitetsverktyg (valfritt men rekommenderat)

Projektet använder [`pre-commit`](https://pre-commit.com) för att förhindra att fel-
formaterad kod, sårbar kod eller kod som innehåller en hemlighet committas. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktiva hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (komplexitet), detect-secrets (API-nycklar), mypy (gradvis typning), Opengrep (SAST), pip-audit (CVE-beroenden), unittest. Se avsnittet _Quality / pre-commit_ i `CLAUDE.md` för mer information.

## Konfiguration

Nycklar söks på **tre platser**, från högst till lägst prioritet.
Varje plats fyller endast i det som den föregående lämnar tomt.

|     | Var                                            | För vad                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Miljövariabler                                 | CI, containrar, tillfälligt undantag |
| 2   | `.env` i aktuell katalog (eller en överordnad katalog) | en projektspecifik nyckel            |
| 3   | `~/.config/aipmt/.env`                        | **installeras en gång, gäller överallt**   |

Efter en `pip install` är den tredje platsen enklast:

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

Filen följer `XDG_CONFIG_HOME` när variabeln anger en absolut sökväg
(annars ignoreras den, enligt specifikationen), och `%APPDATA%`
i Windows.

Den andra platsen är fortfarande användbar när ett arkiv har en egen nyckel: en
`.env` i dess rot har då företräde framför användarkonfigurationen utan
att ändra den. Och en variabel som redan definierats i miljön har företräde
framför båda:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Om ingen nyckel hittas visar kommandot ingen anropslogg: det listar de tre
platserna med deras exakta sökvägar.

`GEMINI_API_KEY` accepteras som alternativ till `GOOGLE_API_KEY` (AI
Studio-konvention). Valfria variabler: `XAI_BASE_URL` (xAI-endpoint, standardvärde
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (sekunder per Anthropic-anrop, standardvärde
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (se avsnittet om Grok CLI) och `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (se avsnittet om OpenCode). För
`regen_translations.sh`: `REGEN_PROVIDER`, `REGEN_MODEL` och
`REGEN_JOB_TIMEOUT` (gräns per jobb, standardvärde 600 s).

## Användning

### Översätta en enskild fil

```bash
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Översätta en katalog

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

### Översätta med sin ChatGPT-prenumeration (`--use_codex`)

Denna provider förbrukar ingen API-nyckel: den styr det officiella Codex-CLI:t i
icke-interaktivt läge, så översättningen räknas av från kvoten för den
redan betalda ChatGPT-prenumerationen (Plus, Pro, Business…). Detta är den
enda dokumenterade vägen från OpenAI för denna användning — tokens från
`~/.codex/auth.json` autentiserar inte anrop till Platform API och läses dessutom
aldrig av detta skript.

**Förutsättningar:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Binären söks i denna ordning: variabeln `CODEX_BIN`, `PATH`,
därefter Python-paketet `openai-codex-cli-bin`. Det sistnämnda finns avsiktligt
inte i `requirements.txt`: det är cirka 250 MB stort, vilket annars skulle
tvingas på alla användare för en valfri provider.

**Bra att veta:**

- **Ingen API-nyckel används.** `OPENAI_API_KEY` och `CODEX_API_KEY` tas
  bort från underprocessens miljö, vilket garanterar att en nyckel i
  `.env` aldrig växlar över översättningen till användningsbaserad
  debitering.
- **Ett segment = ett ”lokalt meddelande”** i planens femtimmarsfönster.
  Använd `--eco` (modell `gpt-5.6-luna`, 250–2 000 meddelanden/5 h på Plus)
  i stället för kvalitetsmodellen (`gpt-5.6-sol`, 10–100 meddelanden/5 h).
- **Långsammare** än ett API-anrop: räkna med cirka 45 s för en komplett README,
  jämfört med några sekunder direkt.
- **Nekas i CI** (`CI` eller `GITHUB_ACTIONS` definierad): autentisering
  via prenumeration är inte avsedd för en delad runner, och OpenAI avråder från
  detta arbetsflöde i offentliga arkiv. Använd en API-nyckel i detta läge.
- Miljövariabler: `CODEX_BIN` (explicit sökväg till binären) och
  `CODEX_TIMEOUT` (sekunder per segment, standardvärde `600`).

### Översätta med sin Grok-prenumeration (`--use_grok_cli`)

Samma princip som `--use_codex`, med det officiella CLI:t **Grok Build**:
översättningen räknas av från Grok-prenumerationen (SuperGrok / X Premium+)
i stället för att debiteras per token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Isolering — läs före användning.** Denna provider är strukturellt **svagare
än `--use_codex`**, och det är avsiktligt:

- Codex körs i `--sandbox read-only`, en gräns som påtvingas av systemet.
- Groks sandbox **kan inte tillämpas** på många nyare Linux-system:
  AppArmor blockerar opriviligierade user namespaces sedan Ubuntu 24.04, och
  deny-listan för containrars runtime-sockets misslyckas om
  `/run/podman` är `0700`. En **inbyggd** profil som inte kan
  tillämpas startar då **oavskärmad, i tysthet**.
- Skriptet begär därför ingen profil som standard och faller **aldrig tyst
  tillbaka**: det visar en varning. Isoleringen bygger på CLI:ts
  `--deny`-regler (inklusive catch-all `*`), det enda
  _fail-closed_-lagret som har uppmätts — en okänd regel gör att starten
  nekas i stället för att skyddet tas bort utan information.
- För att **kräva** OS-sandbox: `GROK_TRANSLATE_SANDBOX=read-only`. Starten misslyckas om
  maskinen inte kan uppfylla det, vilket är det avsedda beteendet.

**Kvot**: Grok-poolen är **veckovis och gemensam** med Chat, Imagine och
Voice, och inget kommando kan läsa den. En batchkörning kan därför förbruka
din konversationsanvändning utan att något signalerar det — därav en
begränsning till 2 samtidiga körningar och en varning i `regen_translations.sh`.

Övriga variabler: `GROK_BIN` (sökväg till binären), `GROK_TIMEOUT` (standardvärde 900 s).

För att återskapa de 28 översättningarna:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
```

### Översätta med OpenCode, till valfri leverantör (`--use_opencode`)

[OpenCode](https://opencode.ai) är en **open source-agent (MIT)** i terminalen. Den är
inte en modellprovider utan en **router** till dem som du har konfigurerat
i OpenCode självt: en API-nyckel, en prenumeration (GitHub Copilot, ChatGPT,
SuperGrok), OpenCode Zen-gatewayen — som tillhandahåller kostnadsfria modeller
**utan konto** — eller en **lokal** modell (Ollama, LM Studio, llama.cpp).
Denna provider styr `opencode run` i icke-interaktivt läge och begränsar
anropet till en enda tur utan några verktyg.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` är **obligatoriskt**, i formatet `provider/modèle`. OpenCode är
inte en provider, och inget standardval görs åt dig: dess eget fallback-val
skulle vara en kostnadsfri modell vars konversationer kan användas för träning.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Isolering — detta gör skriptet vid varje anrop:**

- En inline-konfiguration (`OPENCODE_CONFIG_CONTENT`), med företräde framför din,
  definierar en agent `aipmt` där **alla verktyg nekas**
  (`permission: { "*": "deny" }`): modellen kan varken läsa, skriva eller köra kommandon —
  i mätningar försöker den inte ens. Sessionsdelning är avstängd,
  `--pure` utesluter externa plugins, aldrig `--auto`.
- Anropet körs i en **tom och tillfällig katalog**, med flaggorna
  `OPENCODE_DISABLE_PROJECT_CONFIG` och `OPENCODE_DISABLE_CLAUDE_CODE`: utan dem injicerar OpenCode i varje
  prompt katalogens `AGENTS.md` och din `~/.claude/CLAUDE.md` — i mätningar
  tillämpades instruktionen ”avsluta varje svar med BANANA” från en
  `AGENTS.md` på översättningen. De globala reglerna i `~/.config/opencode/AGENTS.md`
  fortsätter däremot att tillämpas: OpenCode tillåter inte att de kringgås.
- Utmatningskontraktet kräver allt på en gång: returvärde 0, ingen
  `error`-händelse, inget verktygsanrop, ett sista steg avslutat i
  `stop`, icke-tom text och att agenten faktiskt har laddats — ett
  okänt `--agent` får inte OpenCode att misslyckas, utan **faller tyst
  tillbaka** till kodningsagenten med aktiva verktyg. Ett `exit 0`
  bevisar inte heller något här.
- **Ingen aipmt-nyckel skickas** till underprocessen (samma filtrering som
  med Codex och Grok), med ett namngivet undantag: `OPENCODE_API_KEY`, själva
  OpenCode-nyckeln (Zen, Go). Providers konfigureras i OpenCode
  (`opencode auth login`, `opencode.json`), inte i aipmts `.env`.

**Bra att veta:**

- Zens kostnadsfria modeller är ”stealth”-modeller eller bidragsgivarmodeller,
  föränderliga och med odokumenterade gränser, och deras konversationer kan
  användas för träning: perfekta för offentlig dokumentation, men bör undvikas
  för privat innehåll. Uppmätt: `opencode/mimo-v2.5-free` översätter denna README i en
  enda körning; `opencode/big-pickle` är långsammare och två samtidiga förfrågningar
  förblev obesvarade.
- **En lokal modell måste erbjuda minst 16 k kontext** — segmenten är upp till
  16 000 tecken — medan Ollama ofta konfigureras med 4 096 som standard. Med
  Ollama: en `Modelfile` med `PARAMETER num_ctx 32768`, därefter
  `ollama create`. Kvaliteten beror på modellen: en 7B-modell vände på en lista
  och förstörde avslutningen av ett kodblock i en testfil, medan en modell från
  gatewayen bevarade allt.
- `--eco` har ingen effekt (modellen är den från `--model`);
  `--reasoning_effort` skickas oförändrat som `--variant` i OpenCode och bör
  endast begäras om modellen känner till det.
- Sessionerna loggas av OpenCode i dess databas
  (`~/.local/share/opencode/`), precis som alla OpenCode-sessioner.
- Miljövariabler: `OPENCODE_BIN` (explicit sökväg till binären, annars
  `PATH` och därefter `~/.opencode/bin/opencode`) och `OPENCODE_TIMEOUT`
  (sekunder per segment, standardvärde `600`). `OPENCODE_CONFIG` respekteras
  om du exporterar den.

### Ekonomiskt läge

Använder snabbare och billigare modeller (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### Alternativ

| Alternativ                   | Beskrivning                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | En enda Markdown-fil att översätta                                                                            |
| `--source_dir`           | Källkatalog som innehåller Markdown-filerna                                                             |
| `--target_dir`           | Utdat katalog för de översatta filerna                                                               |
| `--source_lang`          | Källspråk (standard: `fr`)                                                                                  |
| `--target_lang`          | Målspråk (standard: `en`)                                                                                   |
| `--model`                | Specifik modell att använda                                                                                  |
| `--eco`                  | Använd ekonomiska modeller                                                                              |
| `--use_mistral`          | Använd Mistral AI API                                                                                     |
| `--use_claude`           | Använd Claude API                                                                                         |
| `--use_gemini`           | Använd Gemini API                                                                                         |
| `--use_codex`            | Använd Codex CLI med ChatGPT-prenumerationens kvot                                                    |
| `--use_grok`             | Använd xAI API (Grok) — kräver `XAI_API_KEY`                                                           |
| `--use_grok_cli`         | Använd Grok CLI med Grok-prenumerationens kvot                                                        |
| `--use_opencode`         | Använd OpenCode (öppen källkod) med leverantören som konfigurerats i OpenCode; kräver `--model provider/modèle` |
| `--force`                | Tvinga ny översättning                                                                                       |
| `--keep_filename`        | Behåll det ursprungliga filnamnet                                                                          |
| `--news`                 | Nyhetsläge: skyddar citat på engelska, hanterar flaggor per språk                                      |
| `--add_translation_note` | Lägg till en översättningsnotis                                                                                |
| `--note_position`        | Notisens placering: `top`, `bottom` (standard), eller `both`                                                     |
| `--note_format`          | Notisformat: `legacy` (standard, fetstilat stycke) eller `marker`                                            |
| `--include_model`        | Inkludera modellnamnet i utdatafilen                                                            |
| `--reasoning_effort`     | GPT-5.x:s resonemangsinsats: `none`/`low`/`medium`/`high`/`xhigh`                                         |

> **De sju provider-flaggorna är ömsesidigt uteslutande.** Att kombinera två
> accepterades tidigare tyst och resulterade i den första som testades:
> en översättning som begärdes med prenumerationskvot (`--use_codex`, `--use_grok_cli`)
> kunde därmed debiteras enligt användning utan någon varning.
> `argparse` avvisar numera kombinationen.

### Översättningsnotis: placeringar och format

Med `--add_translation_note` kan translator placera notisen högst upp, längst ned eller på båda platserna, och återge den antingen i enkelt textformat (bakåtkompatibelt) eller i formatet `marker` som kan användas av ett Markdown-plugin.

**Placering** (`--note_position`):

- `bottom` (standard): notis i slutet av filen, som historiskt.
- `top`: notis infogad **efter YAML-frontmatter** (säkerhet för Astro Content Collections, gray-matter, etc.).
- `both`: notis infogad både högst upp OCH längst ned (ett enda LLM-anrop, innehållet återanvänds för båda placeringarna).

**Format** (`--note_format`):

- `legacy` (standard): fetstilt stycke `**...**` — exakt samma beteende som i v1.8, byte-för-byte. Kompatibelt med Hugo, GitHub, GitLab och alla Markdown-renderare.
- `marker`: osynlig Markdown-definition för länkreferens (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) följd av ett fetstilt blockquote. Läsbart direkt på GitHub/GitLab och kan användas vid byggprocessen av ett remark-plugin på Astro-sidan för att skapa en stiliserad banner (se bloggen jls42.org).

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

### Standardmodeller (2026)

| Provider | Kvalitet (standard)                      | Ekonomisk (`--eco`)      |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI   | `gpt-5.6-terra`                       | `gpt-5.6-luna`            |
| Claude   | `claude-sonnet-5`                     | `claude-haiku-4-5`        |
| Mistral  | `mistral-large-latest`                | `mistral-small-latest`    |
| Gemini   | `gemini-3.7-flash`                    | `gemini-3.1-flash-lite`   |
| Codex    | `gpt-5.6-sol`                         | `gpt-5.6-luna`            |
| Grok API | `grok-4.6`                            | `grok-4.3`                |
| Grok CLI | `grok-4.6`                            | `grok-4.5`                |
| OpenCode | `--model provider/modèle` obligatorisk | samma — `--eco` utan effekt |

> **Rekommendation för långformade översättningar**: `--use_gemini` (standard = `gemini-3.7-flash`) bevarar Markdown-strukturen troget för icke-latinska skript (PL, JA, ZH, AR, HI), även i `--news`-läge där det är viktigt att placeholders bevaras. Uppmätt på denna README översatt till japanska: identisk struktur med `gemini-3.1-pro-preview` (21 listor, 18 kodblock, 13 HTML-länkar, 13 bilder, alla URL:er bevarade) med cirka 6 gånger lägre latens. OpenAI är fortfarande standard för bakåtkompatibilitet.

## Projekt som använder detta skript

- **[jls42.org](https://jls42.org)** - Flerspråkig personlig blogg (15 språk)

## Författare

Julien LE SAUX
E-post: contact@jls42.org

## Licens

GNU GENERAL PUBLIC LICENSE Version 3. Se [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artikel översatt från franska till svenska med gpt-5.6-luna.**

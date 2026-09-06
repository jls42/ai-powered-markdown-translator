# AI-driven Markdown-översättare

🌍 [Franska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [Engelska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Spanska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Kinesiska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Tyska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Japanska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Koreanska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Arabiska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italienska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederländska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Portugisiska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Rumänska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Kodproblem"></a>
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

Översättare för Markdown-filer som använder **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** och **Grok (xAI)** – via API, med kvoten från en ChatGPT- (Codex) eller Grok-prenumeration utan användningsbaserad debitering, eller via **OpenCode**, open source-agenten, med valfri leverantör: lokal modell (Ollama), kostnadsfri tjänst, prenumeration (GitHub Copilot…) eller nyckel.

Detta Python-skript översätter Markdown-filer från ett källspråk till ett målspråk samtidigt som formatering, kodblock och front matter-metadata bevaras.

## Huvudfunktioner

- **Flera leverantörer**: 5 API:er (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLI:er via prenumeration, utan användningsbaserad debitering – Codex (ChatGPT) och Grok – + OpenCode (open source, MIT) med valfri leverantör som konfigurerats i OpenCode, inklusive en lokal modell
- **2026 års modeller**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Ekonomiläge**: Alternativet `--eco` för att använda snabbare och billigare modeller
- **Enskild fil**: Alternativet `--file` för att översätta en enda fil
- **Intelligent segmentering**: Hantering av långa texter med tokensgränser per modell
- **Bevarande av kod**: Kodblock OCH inline-kod (`` `...` ``) bevaras
- **Filnamn**: Alternativet `--keep_filename` för att behålla det ursprungliga namnet
- **Nyhetsläge**: Alternativet `--news` för att skydda engelska citat och hantera flaggor i nyhetsartiklar
- **.env-konfiguration**: Stöd för filen `.env` för API-nycklar
- **Översättningsnotering**: Valfri notering i slutet av dokumentet

## Installation

### För att använda verktyget

```bash
pip install ai-powered-markdown-translator
```

Kommandot `aipmt` är därefter tillgängligt överallt. Om katalogen för
Python-skript inte finns i din `PATH` gör `python -m aipmt` exakt samma
sak. Python 3.10 eller senare.

För en installation som är isolerad från dina övriga paket:

```bash
pipx install ai-powered-markdown-translator
```

### För att bidra till projektet

Det klonade repositoriet behövs fortfarande för utveckling: där finns testerna,
de 28 översättningarna och alla kvalitetsverktyg.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` är en **fullständigt låst lock-fil**, en exakt avbildning av
den testade miljön. Gränserna som publiceras i `pyproject.toml` är
avsiktligt bredare: de ålägger inte dina andra paket några begränsningar.

### Kvalitetsverktyg (valfritt men rekommenderas)

Projektet använder [`pre-commit`](https://pre-commit.com) för att förhindra commits av dåligt formaterad eller sårbar kod eller kod som innehåller en hemlighet. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktiva hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (komplexitet), detect-secrets (API-nycklar), mypy (progressiv typning), Opengrep (SAST), pip-audit (CVE-beroenden), unittest. Se avsnittet _Quality / pre-commit_ i `CLAUDE.md` för mer information.

## Konfiguration

Nycklar söks på **tre platser**, från högsta till lägsta prioritet.
Varje plats fyller endast i det som den föregående lämnat tomt.

|     | Var                                           | För vad                               |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Miljövariabler                                | CI, containrar, tillfälliga undantag  |
| 2   | `.env` i den aktuella katalogen (eller en överordnad katalog) | en projektspecifik nyckel             |
| 3   | `~/.config/aipmt/.env`                        | **installeras en gång, gäller överallt** |

Det enklaste efter en `pip install` är det tredje alternativet:

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

Den här filen följer `XDG_CONFIG_HOME` när variabeln anger en absolut sökväg
(annars ignoreras den, i enlighet med specifikationen), och `%APPDATA%`
i Windows.

Det andra alternativet är fortfarande användbart när ett repositorium har en egen nyckel: en `.env` i dess rot
har då företräde framför användarkonfigurationen utan att ändra den. En
variabel som redan har definierats i miljön har företräde framför båda:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Om ingen nyckel hittas visar kommandot ingen anropsspårning: det
listar de tre platserna med deras exakta sökvägar.

`GEMINI_API_KEY` accepteras som alternativ till `GOOGLE_API_KEY` (AI
Studio-konvention). Valfria variabler: `XAI_BASE_URL` (xAI-endpoint, standard
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (sekunder per Anthropic-anrop, standard
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (se avsnittet om Grok CLI), `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (se avsnittet om OpenCode) och `OPENROUTER_BASE_URL` /
`OPENROUTER_TIMEOUT` / `OPENROUTER_PREFLIGHT_TIMEOUT` (se avsnittet om
OpenRouter). För
`regen_translations.sh`: `REGEN_PROVIDER` (standard `codex`, via prenumeration),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (obligatoriskt undantag för ett
debiterat API) och `REGEN_JOB_TIMEOUT` (tidsgräns per jobb, standard 600 s, 1 800 s med Codex).

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

# Avec OpenRouter (routeur vers ~430 modèles ; --model obligatoire)
aipmt --use_openrouter --model 'z-ai/glm-5.2' --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### Översätta via sin ChatGPT-prenumeration (`--use_codex`)

Den här leverantören använder ingen API-nyckel: den styr Codex officiella CLI i
icke-interaktivt läge, så översättningen räknas av från kvoten i den redan
betalda ChatGPT-prenumerationen (Plus, Pro, Business…). Det är den enda metoden
som OpenAI dokumenterar för detta ändamål – tokens från `~/.codex/auth.json` autentiserar
inte anrop till API Platform och läses dessutom aldrig av detta skript.

**Förutsättningar:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Binärfilen söks i följande ordning: variabeln `CODEX_BIN`, `PATH`,
sedan Python-paketet `openai-codex-cli-bin`. Det sistnämnda ingår avsiktligt
inte i `requirements.txt`: det är cirka 250 MB stort, vilket annars skulle påtvingas alla
användare för en valfri leverantör.

**Bra att veta:**

- **Ingen API-nyckel används.** `OPENAI_API_KEY` och `CODEX_API_KEY`
  tas bort från underprocessens miljö, vilket garanterar att en nyckel
  i `.env` aldrig gör att översättningen övergår till användningsbaserad
  debitering.
- **Ett segment = ett ”lokalt meddelande”** i abonnemangets femtimmarsfönster.
  Använd `--eco` (modellen `gpt-5.6-luna`, 250–2 000 meddelanden/5 h med Plus)
  i stället för kvalitetsmodellen (`gpt-5.6-sol`, 10–100 meddelanden/5 h).
- **Långsammare** än ett API-anrop: räkna med cirka 45 s för en fullständig README, jämfört med
  några sekunder vid ett direktanrop.
- **Nekas i CI** (`CI` eller `GITHUB_ACTIONS` definierad): prenumerationen
  autentiseras via en personlig sessionsfil, och att överföra den till en delad runner
  innebär att en återanvändbar identitet placeras där och kan utnyttjas av allt som
  körs på den. Använd en API-nyckel på den här vägen.
- Miljövariabler: `CODEX_BIN` (uttrycklig sökväg till binärfilen) och
  `CODEX_TIMEOUT` (sekunder per segment, standard `600`).

### Översätta via sin Grok-prenumeration (`--use_grok_cli`)

Samma princip som `--use_codex`, med det officiella CLI-verktyget **Grok Build**:
översättningen räknas av från Grok-prenumerationen (SuperGrok / X Premium+) i stället
för att debiteras per token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Isolering – läs före användning.** Den här leverantören är strukturellt **svagare**
än `--use_codex`, och detta är avsiktligt:

- Codex körs i `--sandbox read-only`, en gräns som upprätthålls av systemet.
- Groks sandbox **kan inte tillämpas** på många moderna Linux-datorer:
  AppArmor blockerar oprivilegierade user namespaces sedan Ubuntu
  24.04, och deny-listan för sockets till containrarnas runtime misslyckas om
  `/run/podman` finns i `0700`. En **inbyggd** profil som inte kan
  tillämpas startar dock **oisolerad, utan varning**.
- Skriptet begär därför ingen profil som standard och **faller aldrig tillbaka
  utan varning**: det visar en varning. Isoleringen bygger på CLI-verktygets
  `--deny`-regler (inklusive catch-all-regeln `*`), det enda lager som uppmätts vara
  _fail-closed_ – en okänd regel gör att starten nekas i stället för att
  skyddet tas bort utan att det meddelas.
- För att **kräva** operativsystemets sandbox: `GROK_TRANSLATE_SANDBOX=read-only`.
  Starten misslyckas om datorn inte kan upprätthålla den, vilket är det
  avsedda beteendet.

**Kvot**: Grok-poolen är **veckovis och delas** med Chat, Imagine och
Voice, och inget kommando kan läsa av den. En batchkörning kan därför
förbruka en del av din kvot för konversationer utan att något meddelar det – därav en
samtidighetsgräns på 2 och en varning i `regen_translations.sh`.

Övriga variabler: `GROK_BIN` (sökväg till binärfilen), `GROK_TIMEOUT` (standard 900 s).

För att generera om de 28 översättningarna:

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
### Översätta med OpenCode, till valfri leverantör (`--use_opencode`)

[OpenCode](https://opencode.ai) är en **open source-agent (MIT)** för
terminalen. Det är inte en modellleverantör utan en **router** till dem
som du har konfigurerat i själva OpenCode: en API-nyckel, en prenumeration,
OpenCode Zen-gatewayen – som erbjuder kostnadsfria modeller **utan konto** – eller
en **lokal** modell. Denna provider kör `opencode run` i icke-interaktivt läge och
begränsar anropet till en enda tur och retur, utan några verktyg.

Två av dessa vägar har mätts från början till slut här: **Zen-gatewayen** och
lokal **Ollama**. De andra som OpenCode tillkännager (GitHub Copilot, LM Studio,
llama.cpp) bör fungera genom konstruktionen, eftersom providern endast kommunicerar
med OpenCode – men de har inte testats, och denna README beskriver endast det
som har verifierats.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` är **obligatorisk**, i formatet `provider/modèle`. OpenCode är inte
en leverantör, och inget standardval görs åt dig: dess egen fallback
skulle vara en kostnadsfri modell vars interaktioner kan användas för träning.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Isolering – detta gör skriptet vid varje anrop:**

- En inline-konfiguration (`OPENCODE_CONFIG_CONTENT`), som har företräde framför
  din egen, definierar en agent `aipmt` där **alla verktyg nekas**
  (`permission: { "*": "deny" }`): modellen kan varken läsa, skriva eller
  köra kommandon – enligt mätning försöker den inte ens. Sessionsdelning
  är inaktiverad, `--pure` utesluter externa plugins, aldrig `--auto`.
- Anropet körs i en **tillfällig och tom katalog**, med växlarna
  `OPENCODE_DISABLE_PROJECT_CONFIG` och `OPENCODE_DISABLE_CLAUDE_CODE`: utan
  dem injicerar OpenCode `AGENTS.md` från den aktuella katalogen
  och din `~/.claude/CLAUDE.md` i varje prompt – enligt mätning tillämpades en instruktion
  om att ”avsluta varje svar med BANANA”, placerad i en `AGENTS.md`, på översättningen. De
  globala reglerna i `~/.config/opencode/AGENTS.md` tillämpas däremot fortfarande:
  OpenCode tillåter inte att de utesluts.
- Utdatakontraktet kräver allt detta samtidigt: returkod 0, ingen händelse
  `error`, inget verktygsanrop, ett sista steg slutfört med `stop`, icke-tom
  text och att agenten faktiskt har lästs in – en okänd `--agent` får inte
  OpenCode att misslyckas, utan programmet **faller tyst tillbaka** till kodningsagenten, med
  aktiva verktyg. En `exit 0` bevisar inte heller något här.
- **Ingen aipmt-nyckel överförs** till underprocessen (samma filtrering
  som med Codex och Grok), med ett uttryckligt undantag: `OPENCODE_API_KEY`,
  OpenCodes egen nyckel (Zen, Go). Leverantörerna konfigureras i
  OpenCode (`opencode auth login`, `opencode.json`), inte i aipmts `.env`.

**Bra att veta:**

- **Zens kostnadsfria modeller är ”stealth”- eller bidragsgivarmodeller**,
  föränderliga, med odokumenterade gränser, och deras interaktioner kan användas för
  träning: perfekta för offentlig dokumentation, men bör undvikas för
  privat innehåll. Uppmätt: `opencode/mimo-v2.5-free` översätter denna README i en
  omgång; `opencode/big-pickle` är långsammare och två samtidiga förfrågningar
  förblev obesvarade.
- **En lokal modell måste erbjuda minst 16 k i kontext** – segmenten är
  upp till 16 000 tecken – medan Ollama ofta konfigurerar 4 096 som
  standard. Med Ollama: en `Modelfile` med `PARAMETER num_ctx 32768`, sedan
  `ollama create`. Kvaliteten beror på modellen: en 7B-modell vände på en lista och
  skadade avslutningen på ett kodblock i en testfil, medan en modell från
  gatewayen bevarade allt.
- `--eco` har ingen effekt (modellen är den i `--model`);
  `--reasoning_effort` skickas oförändrad som OpenCodes `--variant` och bör endast
  begäras om modellen känner till den.
- Sessionerna loggas av OpenCode i dess databas
  (`~/.local/share/opencode/`), precis som alla OpenCode-sessioner.
- Miljövariabler: `OPENCODE_BIN` (explicit sökväg till binärfilen,
  annars `PATH` och därefter `~/.opencode/bin/opencode`) och `OPENCODE_TIMEOUT`
  (sekunder per segment, standard `600`). `OPENCODE_CONFIG` respekteras om du
  exporterar den.

**Uppmätt exempel: en lokal modell via Ollama** (RTX 3060 12 GB, 62 GB RAM, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # conserve les modèles déjà téléchargés
ollama pull gpt-oss:20b                         # 13 Go, Apache 2.0 — le seul modèle local retenu ici

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

Sedan leverantören i `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` är ingen detalj: Ollama aktiverar resonemang som
standard för dessa modeller, och en Modelfile kan inte stänga av det. Uppmätt
via OpenCode: utan alternativet kostar ”Katten sover på mattan” 919 tokens
för resonemang och 68 s; med alternativet 9 tokens.

```bash
aipmt --use_opencode --model ollama/gpt-oss-20b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

Resultat för ett verkligt blogginlägg på 589 rader (140 länkar, 21 avsnitt,
3 engelska citat skyddade av läget `--news`), samma kommando, tre
modeller:

| Modell                                   | Tid          | Struktur                                                    | Avvikelser                                                                                      |
| ---------------------------------------- | ------------ | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free` (Zen, kostnadsfri) | 4 min 26 s   | identisk med källan                                         | inga                                                                                            |
| `ollama/gemma4-12b-32k` (lokal)          | 10 min 10 s  | identiska länkar, URL:er, tabeller, taggar, fetstil och inline-kod | en påhittad citatrad (🇺🇸 + parafras), en duplicerad attribuering                                 |
| `ollama/qwen3.5-9b-32k` (lokal)          | 8 min 18 s   | identiska länkar, URL:er, tabeller och taggar               | en påhittad citatrad, viss tillagd fetstil och inline-kod, ett segment som kördes om             |

Dessa två lokala modeller har sedan dess **uteslutits**: en enda frihet per artikel
räcker för att diskvalificera en modell för publicerad översättning. Fem andra har
uteslutits av samma skäl eller på grund av timeout (`gemma4:26b-a4b`,
`qwen3.6:35b-a3b`, `ministral-3:14b`, `mistral-small3.2`, `hy-mt2:7b`). Endast
`gpt-oss:20b` har behållits – och även den lämnar passager på franska i
en innehållsrik artikel, se tabellen över rekommenderade modeller.

Under den lokala översättningen: GPU på 98 % och 170 W, 10 GB VRAM använt
(modell och cache på 32 k tokens, inget avlastat till RAM), 7,5 GB RAM för
Ollama-servern. En modell med 9 till 12 miljarder parametrar respekterar
strukturen men tar sig en frihet per artikel, medan gatewaymodellen
inte tog sig någon: korrekturläs före publicering eller använd den endast för utkast.

### Översätta via OpenRouter (`--use_openrouter`)

OpenRouter är en **router** framför fler än 400 modeller som drivs av tredje part,
med användningsbaserad debitering från ett gemensamt saldo. Med en enda nyckel ger den åtkomst till modeller
som ingen av de andra providers erbjuder, särskilt öppna kinesiska modeller.

```bash
# --model est OBLIGATOIRE : aucun défaut n'est choisi à votre place
aipmt --use_openrouter --model 'z-ai/glm-5.2' --file README.md \
  --target_dir . --source_lang fr --target_lang en
```

Två egenskaper hos routingen har styrt implementationen, och båda är
mätbara:

- **Samma modell tillhandahålls av dussintals värdar med olika
  gränser.** För `z-ai/glm-5.3-flash` finns 23 värdar, varav en är begränsad till
  2 048 tokens i utdata: utan försiktighetsåtgärder blev en av 23 långa översättningar
  trunkerad, slumpmässigt beroende på routingen och utan minsta varning. En preflight läser
  `/api/v1/models/{modèle}/endpoints`, utesluter värdar med mindre än 8 000 tokens
  i utdata eller degraderad status och fäster sedan de övriga med
  `allow_fallbacks: false` – annars återgår routern till en
  utesluten värd.
- **Resonemang debiteras enligt utdatataxan.** Samma förfrågan till
  `z-ai/glm-5.2`, svaret ”OK”: 107 slutförandetokens med modellens standardinställning,
  2 med resonemang avstängt. Det är därför avstängt som standard för de modeller
  som tillåter det. De som kräver det – `reasoning.mandatory`, 288 av katalogens 431
  modeller – får den **lägsta nivå de uppger att de
  accepterar**, inte sin standardinställning: för `z-ai/glm-5.3-flash` är den
  `max`, och den förbrukade alla 32 768 utdatatokens innan
  översättningen var klar. Att höja gränsen hade inte förändrat något, eftersom nivån tilldelar
  en procentandel av den. `--reasoning_effort` har fortsatt företräde, och `none` för en modell
  som kräver resonemang rapporteras i stället för att kringgås.

Preflight-kontrollen är **fail-closed** och visar vad den har valt:

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

En slug som saknas i katalogen, en katalog som inte kan nås eller avsaknad av en värd
som klarar gränsen stoppar kommandot före all debitering.

Övriga punkter:

- Kontextfönstret hämtas från katalogen, inte från en konstant:
  segmenteringen anpassas faktiskt efter det, även för modeller med 4 095 tokens.
- `--eco` har ingen effekt (modellen är den i `--model`).
- `finish_reason=length` med tom utdata är inte en trunkering utan en
  budget som förbrukats av resonemang; meddelandet anger det, eftersom de två
  fallen kräver motsatta åtgärder.
- Miljövariabler: `OPENROUTER_API_KEY` (nyckel, på
  <https://openrouter.ai/keys>), `OPENROUTER_BASE_URL` (standard
  `https://openrouter.ai/api/v1`, `https://` krävs), `OPENROUTER_TIMEOUT`
  (sekunder per anrop, standard `900`) och `OPENROUTER_PREFLIGHT_TIMEOUT`
  (standard `30`).

### Ekonomiläge

Använder snabbare och billigare modeller (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Alternativ

| Alternativ                | Beskrivning                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | En enskild Markdown-fil att översätta                                                                         |
| `--source_dir`           | Källkatalog som innehåller Markdown-filer                                                                     |
| `--target_dir`           | Utdatakatalog för de översatta filerna                                                                        |
| `--source_lang`          | Källspråk (standard: `fr`)                                                                                  |
| `--target_lang`          | Målspråk (standard: `en`)                                                                                   |
| `--model`                | Specifik modell att använda                                                                                   |
| `--eco`                  | Använd ekonomimodeller                                                                                        |
| `--use_mistral`          | Använd Mistral AI API                                                                                         |
| `--use_claude`           | Använd Claude API                                                                                             |
| `--use_gemini`           | Använd Gemini API                                                                                             |
| `--use_codex`            | Använd Codex CLI med ChatGPT-prenumerationens kvot                                                            |
| `--use_grok`             | Använd xAI API (Grok) – kräver `XAI_API_KEY`                                                                  |
| `--use_openrouter`       | Använd OpenRouter – kräver `OPENROUTER_API_KEY` och `--model fournisseur/modèle`                             |
| `--use_grok_cli`         | Använd Grok CLI med Grok-prenumerationens kvot                                                                |
| `--use_opencode`         | Använd OpenCode (open source) med leverantören som konfigurerats i OpenCode; kräver `--model provider/modèle` |
| `--force`                | Tvinga fram en ny översättning                                                                                |
| `--keep_filename`        | Behåll det ursprungliga filnamnet                                                                             |
| `--news`                 | Nyhetsläge: skyddar engelska citat och hanterar flaggor efter språk                                           |
| `--add_translation_note` | Lägg till en översättningsnot                                                                                 |
| `--note_position`        | Notens placering: `top`, `bottom` (standard) eller `both`                                                     |
| `--note_format`          | Notens format: `legacy` (standard, stycke i fetstil) eller `marker`                                            |
| `--include_model`        | Inkludera modellnamnet i utdatafilen                                                                          |
| `--reasoning_effort`     | Resonemangsnivå för GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

> **De sju provider-flaggorna är ömsesidigt uteslutande.** Att kombinera två
> accepterades tidigare tyst och valde den första som testades: en
> översättning som begärdes mot en prenumerationskvot (`--use_codex`, `--use_grok_cli`)
> kunde därmed gå över till användningsbaserad debitering utan någon varning.
> `argparse` nekar numera kombinationen.

### Översättningsnot: placeringar och format

Med `--add_translation_note` kan översättaren placera noten högst upp, längst ned eller på båda ställena och återge den antingen som enkel text (bakåtkompatibelt) eller i ett `marker`-format som kan användas av ett Markdown-plugin.

**Placering** (`--note_position`):

- `bottom` (standard): noten placeras sist i filen, som tidigare.
- `top`: noten infogas **efter YAML-frontmatter** (säkert för Astro Content Collections, gray-matter osv.).
- `both`: noten infogas både högst upp OCH längst ned (ett enda LLM-anrop, innehållet återanvänds för båda placeringarna).

**Format** (`--note_format`):

- `legacy` (standard): stycke i fetstil `**...**` – beteendet är strikt identiskt med v1.8, byte för byte. Kompatibelt med Hugo, GitHub, GitLab och alla Markdown-renderare.
- `marker`: osynlig Markdown-definition för länkreferens (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), följd av ett blockquote i fetstil. Läsbart direkt på GitHub/GitLab och användbart under bygget av ett remark-plugin på Astro-sidan för att skapa en stiliserad banner (se bloggen jls42.org).

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

| Provider   | Kvalitet (standard)                       | Ekonomisk (`--eco`)      |
| ---------- | ---------------------------------------- | ------------------------- |
| OpenAI     | `gpt-5.6-terra`                          | `gpt-5.6-luna`            |
| Claude     | `claude-sonnet-5`                        | `claude-haiku-4-5`        |
| Mistral    | `mistral-large-latest`                   | `mistral-small-latest`    |
| Gemini     | `gemini-3.7-flash`                       | `gemini-3.1-flash-lite`   |
| Codex      | `gpt-5.6-sol`                            | `gpt-5.6-luna`            |
| Grok API   | `grok-4.6`                               | `grok-4.3`                |
| Grok CLI   | `grok-4.6`                               | `grok-4.5`                |
| OpenCode   | `--model provider/modèle` obligatorisk    | samma – `--eco` utan effekt |
| OpenRouter | `--model fournisseur/modèle` obligatorisk | samma – `--eco` utan effekt |
## Vilka modeller håller måttet

En modell som översätter ett stycke bra bevarar inte nödvändigtvis strukturen
i ett helt dokument. Dessa mätningar kommer från **faktiskt genomförda
översättningar**, med kommandot som visas ovan, på tre dokumentuppsättningar
och fjorton målspråk: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.

Två kolumner, och de säger inte samma sak. **Slutförda** räknar de
översättningar som lyckas — scriptets skydd mot tysta fel släpper igenom filen.
**Utan avvikelse** räknar dem vars struktur är identisk med källan: samma
avsnitt, samma länkar, samma URL:er, samma block och inline-kod, samma tabeller,
samma citat, samma flaggor.

### Innehållsrik bloggartikel, läget `--news`

589 rader, 140 länkar, 21 avsnitt, 3 skyddade engelska citat. Det är det mest
krävande av de tre dokumenten: läget `--news` lägger till begränsningar
för flaggor och citat utöver Markdown-strukturen.

| Modell                            | Åtkomst             | Slutförda | Utan avvikelse | Median/språk |
| --------------------------------- | ------------------- | --------- | -------------- | ------------ |
| `gemini-3.7-flash`                | Google API          | 14/14     | **14/14**      | 1 min 18 s   |
| `gpt-5.6-sol` (`--use_codex`)     | ChatGPT-abonnemang  | 14/14     | **14/14**      | 11 min 28 s  |
| `z-ai/glm-5.2`                    | OpenRouter          | 14/14     | **14/14**      | 5 min 37 s   |
| `qwen/qwen3.8-flash`              | OpenRouter          | 14/14     | 13/14          | 26 min 23 s  |
| `z-ai/glm-5.3-flash`              | OpenRouter          | 12/14     | 12/14          | 15 min 49 s  |
| `qwen/qwen3.5-27b`                | OpenRouter          | 7/9       | 7/9            | 20 min 33 s  |
| `claude-sonnet-5`                 | Anthropic API       | 14/14     | 11/14          | 6 min 31 s   |
| `opencode/mimo-v2.5-free`         | OpenCode Zen        | 13/14     | 11/14          | 9 min 27 s   |
| `qwen/qwen3.7-flash`              | OpenRouter          | 13/14     | 714           | 10 min 09 s  |
| `ollama/gpt-oss-20b-32k`          | lokalt              | 10/14     | 714           | 12 min 39 s  |
| `mistral-large-latest`            | Mistral API         | 11/14     | 5/14           | 5 min 32 s   |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter          | 4/14      | 3/14           | 37 min 27 s  |
| `grok-4.6` (`--use_grok_cli`)     | Grok-abonnemang     | 1/14      | 1/14           | 23 min 11 s  |
| `moonshotai/kimi-k2.6`            | OpenRouter          | 1/4       | 1/4            | 23 min 00 s  |

Två körningar **avbröts på grund av bristande saldo**, vilket framgår av deras
nämnare: `qwen3.5-27b` stannade efter nio språk och `kimi-k2.6` efter fyra
— den senare efter en timeout på fyrtio minuter och två avslag, till en kostnad
på nästan 0,33 $ per språk.

En metodanmärkning om OpenRouter-raderna: de mättes med routerns
**standardinställningar**, innan `--use_openrouter` fanns. `z-ai/glm-5.2` har
sedan dess mätts på nytt med den medföljande providern, med reasoning avstängt,
och ger exakt samma 14/14. `z-ai/glm-5.3-flash` misslyckades två gånger eftersom
routerns standardbudget för utdata tog slut; providern begär numera den lägsta
reasoning-nivå som dessa modeller accepterar, och kontrolltestet på de berörda
språken lyckas.

### Projektets README, standard-Markdown

508 rader, 219 inline-koder, 40 blockavgränsare, 45 tabellrader. Inget
`--news`-läge här: svårigheten beror på den höga kodtätheten.

| Modell                        | Slutförda | Utan avvikelse | Median/språk |
| ----------------------------- | --------- | -------------- | ------------ |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14     | 11/14          | 1 min 22 s   |
| `gemini-3.7-flash`            | 14/14     | 13/14          | 21 s         |
| `gpt-5.6-sol` (`--use_codex`) | 14/14     | 12/14          | 2 min 04 s   |
| `opencode/mimo-v2.5-free`     | 9/14      | 714           | 3 min 25 s   |
| `ollama/gpt-oss-20b-32k`      | 9/14      | 1/14           | 3 min 38 s   |

### Fyra README-filer från välkända projekt

FastAPI, Ollama, tldr-pages och Vue.js, hämtade i befintligt skick från GitHub.
Dessa dokument är **enklare** än de två föregående, vilket tabellen visar.

| Modell                    | Omfattning                 | Slutförda | Utan avvikelse |
| ------------------------- | -------------------------- | --------- | -------------- |
| `opencode/mimo-v2.5-free` | | 4 projekt × 14 språk       | 55/56     | 47/56          |
| `grok-4.6` (abonnemang)   | 4 projekt × ar, hi, ja, zh | 16/16     | 14/16          |
| `ollama/gpt-oss-20b-32k`  | 4 projekt × ar, hi, ja, zh | 15/16     | 9/16           |

### Vad vi kan dra för slutsatser

- **Tre modeller har aldrig förlorat information** i de två innehållsrika
  dokumenten: `gemini-3.7-flash`, `gpt-5.6-sol` via ChatGPT-abonnemanget och
  `z-ai/glm-5.2` via OpenRouter. Deras enda avvikelser i standardläget är ett
  par `**` som inte återges på ett eller två språk, aldrig en URL,
  ett kodblock eller ett citat.
- **Den avgörande faktorn är dokumentets täthet, inte läget `--news`.**
  Grok via abonnemang misslyckas 13 gånger av 14 på bloggartikeln och lyckas
  med 14 offentliga README-filer av 16: orsaken till misslyckandet är att den
  tappar tråden i ett långt segment, vilket har verifierats med ett
  kontrolltest — det isolerade avsnittet översätts korrekt.
- **Icke-latinska skriftsystem är inte den förväntade skiljelinjen.**
  `gpt-oss` lämnar kvar franska avsnitt på arabiska, japanska, polska
  **och rum rumänska**; Mistral och MiMo tappar endast inline-kod i
  icke-latinska skriftsystem.
- **Att stänga av reasoning kostar inget i kvalitet.** `z-ai/glm-5.2` klarar
  fjorton språk utan en enda avvikelse under båda förutsättningarna — reasoning
  aktiverat enligt routerns standardinställning och sedan avstängt av
  `--use_openrouter` — med arton gånger färre fakturerade utdatatokens. Det är
  denna mätning som motiverar providerns standardinställning.
- **En långsam modell är inte en säker modell.** `deepseek-v4-flash-0731` tar 37 minuter
  per språk för 4 översättningar av 14, `qwen3.8-flash` tar 26 minuter för ett
  nästan perfekt resultat och Gemini tar 1 minut och 18 sekunder för ett
  felfritt resultat.

### Vad den här tabellen inte är

- **Det är inte en uttömmande rangordning.** Enbart OpenRouter erbjuder fler än
  fyrahundra modeller; ett femtontal har mätts här. Att en modell saknas säger
  ingenting om dess kvalitet, bara att den inte har testats.
- **Dessa mätningar har ett datum**: den 4 och 5 september 2026. Modeller ändras
  under samma namn, leverantörerna justerar kvantiseringar och gränser och nya
  modeller lanseras varje vecka.
- **Tiderna rangordnar ingenting.** Parallelliteten varierade mellan 3 och 6
  samtidiga översättningar beroende på körning, och en leverantörs
  genomströmning varierar under dagen. De ger en storleksordning, inte en
  jämförelse.
- **Ett resultat beror lika mycket på dokumentet som på modellen.** Samma modell
  klarar fjorton språk för en artikel och nio för denna README. Era filer är
  inte våra.
- **Rätt tillvägagångssätt är fortfarande att mäta hos er**: översätt ett av
  era dokument till era målspråk och jämför sedan strukturen — antalet avsnitt,
  länkar, unika URL:er, kodblock, inline-koder och tabellrader. Det är exakt vad
  protokollet ovan gör, och det ryms i en loop över `aipmt`.

## Projekt som använder detta script

- **[jls42.org](https://jls42.org)** - Flerspråkig personlig blogg (15 språk)

## Författare

Julien LE SAUX
E-post: contact@jls42.org

## Licens

GNU GENERAL PUBLIC LICENSE Version 3. Se [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artikel översatt från franska till svenska med gpt-5.6-sol.**

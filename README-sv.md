# AI-driven Markdown-översättare

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

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

Översättare för Markdown-filer som använder **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** och **Grok (xAI)** – via API, genom kvoten i ett ChatGPT- (Codex) eller Grok-abonnemang utan användningsbaserad debitering, eller via **OpenCode**, agenten med öppen källkod, till valfri leverantör: lokal modell (Ollama), kostnadsfri tjänst, abonnemang (GitHub Copilot…) eller nyckel.

Det här Python-skriptet översätter Markdown-filer från ett källspråk till ett målspråk samtidigt som formatering, kodblock och front matter-metadata bevaras.

## Huvudfunktioner

- **Flera leverantörer**: 5 API:er (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLI:er via abonnemang, utan användningsbaserad debitering – Codex (ChatGPT) och Grok – samt OpenCode (öppen källkod, MIT) till valfri leverantör som konfigurerats i OpenCode, inklusive en lokal modell
- **2026-modeller**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Ekonomiläge**: Alternativet `--eco` för att använda snabbare och billigare modeller
- **Enskild fil**: Alternativet `--file` för att översätta en enda fil
- **Smart segmentering**: Hantering av långa texter med token-gränser per modell
- **Bevarande av kod**: Både kodblock OCH inline-kod (`` `...` ``) bevaras
- **Filnamn**: Alternativet `--keep_filename` för att behålla det ursprungliga namnet
- **Nyhetsläge**: Alternativet `--news` för att skydda engelska citat och hantera flaggor i nyhetsartiklar
- **.env-konfiguration**: Stöd för filen `.env` för API-nycklar
- **Översättningsanmärkning**: Valfritt tillägg av en anmärkning i slutet av dokumentet

## Installation

### För att använda verktyget

```bash
pip install ai-powered-markdown-translator
```

Kommandot `aipmt` är därefter tillgängligt överallt. Om katalogen för
Python-skript inte finns i din `PATH` gör `python -m aipmt` exakt samma
sak. Python 3.10 eller senare.

För en installation som är isolerad från resten av dina paket:

```bash
pipx install ai-powered-markdown-translator
```

### För att bidra till projektet

Det klonade repot behövs fortfarande för utveckling: där finns testerna,
de 28 översättningarna och alla kvalitetsverktyg.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` är en **helt låst lock-fil** som exakt återspeglar
den testade miljön. Gränserna som publiceras i `pyproject.toml` är
avsiktligt bredare: de ålägger inte dina andra paket några begränsningar.

### Kvalitetsverktyg (valfritt men rekommenderat)

Projektet använder [`pre-commit`](https://pre-commit.com) för att förhindra commits av dåligt formaterad eller sårbar kod samt kod som innehåller hemligheter. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktiva hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (komplexitet), detect-secrets (API-nycklar), mypy (progressiv typning), Opengrep (SAST), pip-audit (CVE-beroenden), unittest. Se avsnittet _Quality / pre-commit_ i `CLAUDE.md` för mer information.

## Konfiguration

Nycklar söks på **tre platser**, från högsta till lägsta prioritet.
Varje plats fyller endast i det som den föregående har lämnat tomt.

|     | Var                                           | För vad                                 |
| --- | --------------------------------------------- | --------------------------------------- |
| 1   | Miljövariabler                                | CI, containrar, tillfälliga åsidosättningar |
| 2   | `.env` i den aktuella katalogen (eller en överordnad) | en projektspecifik nyckel               |
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
EOF
chmod 600 ~/.config/aipmt/.env
```

Den här filen följer `XDG_CONFIG_HOME` när variabeln anger en absolut sökväg
(annars ignoreras den, enligt specifikationen), och `%APPDATA%`
i Windows.

Det andra alternativet är fortfarande användbart när ett repo har en egen nyckel: en `.env` i dess rot
har då företräde framför användarkonfigurationen utan att ändra den. Och en
variabel som redan har definierats i miljön har företräde framför båda:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Om ingen nyckel hittas visar kommandot ingen anropsstack: det
listar de tre platserna med deras exakta sökvägar.

`GEMINI_API_KEY` godtas som alternativ till `GOOGLE_API_KEY` (AI
Studio-konvention). Valfria variabler: `XAI_BASE_URL` (xAI-endpoint, standardvärde
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (sekunder per Anthropic-anrop, standardvärde
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (se avsnittet om Grok CLI) och `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (se avsnittet om OpenCode). För
`regen_translations.sh`: `REGEN_PROVIDER` (standardvärde `codex`, via abonnemang),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (obligatorisk åsidosättning för ett
debiterat API) och `REGEN_JOB_TIMEOUT` (gräns per jobb, standardvärde 600 s, 1 800 s med Codex).

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

### Översätta via sitt ChatGPT-abonnemang (`--use_codex`)

Den här leverantören använder ingen API-nyckel: den styr det officiella Codex CLI
i icke-interaktivt läge, så översättningen räknas av från kvoten i det redan
betalda ChatGPT-abonnemanget (Plus, Pro, Business…). Det är den enda metod som
OpenAI har dokumenterat för denna användning – token från `~/.codex/auth.json` autentiserar inte
anrop till API Platform och läses dessutom aldrig av det här skriptet.

**Förutsättningar:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Den körbara filen söks i följande ordning: variabeln `CODEX_BIN`, `PATH`,
och därefter Python-paketet `openai-codex-cli-bin`. Det sistnämnda ingår avsiktligt
inte i `requirements.txt`: det är cirka 250 MB stort, vilket annars skulle belasta alla
användare för en valfri leverantör.

**Bra att veta:**

- **Ingen API-nyckel används.** `OPENAI_API_KEY` och `CODEX_API_KEY`
  tas bort från underprocessens miljö, vilket garanterar att en nyckel
  i `.env` aldrig får översättningen att växla till användningsbaserad
  debitering.
- **Ett segment = ett ”lokalt meddelande”** i abonnemangets femtimmarsfönster.
  Använd `--eco` (modellen `gpt-5.6-luna`, 250–2 000 meddelanden/5 h med Plus)
  i stället för kvalitetsmodellen (`gpt-5.6-sol`, 10–100 meddelanden/5 h).
- **Långsammare** än ett API-anrop: räkna med cirka 45 s för en fullständig README,
  jämfört med några sekunder direkt.
- **Nekas i CI** (om `CI` eller `GITHUB_ACTIONS` har definierats): autentisering via
  abonnemang är inte avsedd för en delad runner, och OpenAI avråder från detta
  arbetsflöde i offentliga repon. Använd en API-nyckel på den här vägen.
- Miljövariabler: `CODEX_BIN` (uttrycklig sökväg till den körbara filen) och
  `CODEX_TIMEOUT` (sekunder per segment, standardvärde `600`).

### Översätta via sitt Grok-abonnemang (`--use_grok_cli`)

Samma princip som för `--use_codex`, med det officiella CLI-verktyget **Grok Build**:
översättningen räknas av från Grok-abonnemanget (SuperGrok/X Premium+) i stället
för att debiteras per token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Isolering – läs före användning.** Den här leverantören är strukturellt **svagare**
än `--use_codex`, och det är ett medvetet val:

- Codex körs i `--sandbox read-only`, en gräns som upprätthålls av systemet.
- Groks sandbox **kan inte tillämpas** på många moderna Linux-datorer:
  AppArmor blockerar icke-privilegierade user namespaces sedan Ubuntu
  24.04, och spärrlistan för containerns runtime-sockets misslyckas om
  `/run/podman` finns i `0700`. En **inbyggd** profil som inte kan
  tillämpas startar då **oisolerad utan någon varning**.
- Skriptet begär därför ingen profil som standard och **faller aldrig tillbaka
  i tysthet**: det visar en varning. Isoleringen bygger på CLI-verktygets
  `--deny`-regler (inklusive den heltäckande regeln `*`), det enda uppmätta lagret
  som fungerar enligt principen _fail-closed_ – en okänd regel gör att starten nekas i stället för att
  skyddet tas bort utan att det meddelas.
- För att **kräva** operativsystemets sandbox: `GROK_TRANSLATE_SANDBOX=read-only`.
  Starten misslyckas om datorn inte kan uppfylla kravet, vilket är det
  avsedda beteendet.

**Kvot**: Grok-poolen är **veckovis och delas** med Chat, Imagine och
Voice, och det finns inget kommando för att läsa av den. En batchbearbetning kan därför
förbruka en del av din användning för konversationer utan att något meddelar det – därav en
samtidighetsgräns på 2 och en varning i `regen_translations.sh`.

Övriga variabler: `GROK_BIN` (sökväg till den körbara filen), `GROK_TIMEOUT` (standardvärde 900 s).

För att generera de 28 översättningarna på nytt:

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

### Översätta med OpenCode till valfri leverantör (`--use_opencode`)

[OpenCode](https://opencode.ai) är en kodagent med **öppen källkod (MIT)** för
terminalen. Det är inte en modellleverantör utan en **router** till de
leverantörer som du själv har konfigurerat i OpenCode: en API-nyckel, ett abonnemang
(GitHub Copilot, ChatGPT, SuperGrok), gatewayen OpenCode Zen – som erbjuder
kostnadsfria modeller **utan konto** – eller en **lokal** modell (Ollama, LM Studio,
llama.cpp). Den här leverantören styr `opencode run` i icke-interaktivt läge och begränsar
anropet till en enda tur och retur, helt utan verktyg.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` är **obligatoriskt** och ska anges i formatet `provider/modèle`. OpenCode är inte
en leverantör, och inget standardval görs åt dig: dess egen reservlösning
skulle vara en kostnadsfri modell vars konversationer kan användas för träning.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Isolering – det här gör skriptet vid varje anrop:**

- En inline-konfiguration (`OPENCODE_CONFIG_CONTENT`) som har företräde framför
  din egen definierar en agent, `aipmt`, där **alla verktyg nekas**
  (`permission: { "*": "deny" }`): modellen kan varken läsa, skriva eller
  köra kommandon – enligt mätningar försöker den inte ens. Sessionsdelning
  är inaktiverad, `--pure` utesluter externa plugins, aldrig `--auto`.
- Anropet körs i en **tom temporär katalog**, med växlarna
  `OPENCODE_DISABLE_PROJECT_CONFIG` och `OPENCODE_DISABLE_CLAUDE_CODE`: utan
  dem infogar OpenCode katalogens `AGENTS.md` och din `~/.claude/CLAUDE.md` i varje prompt
  – enligt mätningar tillämpades en instruktion om att ”avsluta varje svar
  med BANANA” från en `AGENTS.md` på översättningen. De
  globala reglerna i `~/.config/opencode/AGENTS.md` fortsätter däremot att
  gälla: OpenCode tillåter inte att de utesluts.
- Utmatningskontraktet kräver allt detta samtidigt: returkod 0, ingen
  `error`-händelse, inget verktygsanrop, ett sista steg som slutförts med `stop`, en
  icke-tom text och att agenten faktiskt har lästs in – en okänd `--agent` får inte
  OpenCode att misslyckas, utan verktyget **faller i tysthet tillbaka** på kodningsagenten med
  aktiva verktyg. Inte heller en `exit 0` bevisar något här.
- **Ingen nyckel från aipmt skickas** till underprocessen (samma filtrering
  som med Codex och Grok), med ett uttryckligt undantag: `OPENCODE_API_KEY`,
  OpenCodes egen nyckel (Zen, Go). Leverantörerna konfigureras i
  OpenCode (`opencode auth login`, `opencode.json`), inte i aipmt:s `.env`.

**Bra att veta:**

- **Zens kostnadsfria modeller är ”stealth”-modeller eller bidragsgivarmodeller**,
  som förändras, har odokumenterade gränser och vars konversationer kan användas för
  träning: utmärkta för offentlig dokumentation, men bör undvikas för
  privat innehåll. Uppmätt: `opencode/mimo-v2.5-free` översätter denna README i en
  enda omgång; `opencode/big-pickle` är långsammare och två samtidiga förfrågningar
  förblev obesvarade.
- **En lokal modell måste erbjuda minst 16 k kontext** – segmenten är
  upp till 16 000 tecken långa – medan Ollama ofta konfigurerar 4 096 som
  standard. Med Ollama: en `Modelfile` med `PARAMETER num_ctx 32768`, och sedan
  `ollama create`. Kvaliteten beror på modellen: en 7B-modell vände på en lista och
  skadade avslutningen på ett kodblock i en testfil, medan en modell från
  gatewayen bevarade allt.
- `--eco` har ingen effekt (modellen är den i `--model`);
  `--reasoning_effort` skickas vidare oförändrat som OpenCodes `--variant` och bör endast
  begäras om modellen känner till det.
- Sessionerna loggas av OpenCode i dess databas
  (`~/.local/share/opencode/`), precis som alla andra OpenCode-sessioner.
- Miljövariabler: `OPENCODE_BIN` (uttrycklig sökväg till den körbara filen,
  annars `PATH` och sedan `~/.opencode/bin/opencode`) samt `OPENCODE_TIMEOUT`
  (sekunder per segment, standardvärde `600`). `OPENCODE_CONFIG` respekteras om du
  exporterar den.

**Uppmätt exempel: en lokal modell via Ollama** (RTX 3060 12 GB, 62 GB RAM, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # Ollama ≥ 0.30 pour gemma4 ; conserve les modèles déjà téléchargés
ollama pull gemma4:12b                          # 7,6 Go, Apache 2.0, 140+ langues
ollama pull qwen3.5:9b                          # 6,6 Go, Apache 2.0, 201 langues

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gemma4:12b\nPARAMETER num_ctx 32768\n' > gemma4-12b-32k.Modelfile
ollama create gemma4-12b-32k -f gemma4-12b-32k.Modelfile
```

Därefter leverantören i `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` är ingen detalj: Ollama aktiverar resonemang som
standard för Gemma 4 och Qwen 3.5, och en Modelfile kan inte stänga av det. Uppmätt
via OpenCode: utan alternativet kostar ”Katten sover på mattan” 919
resonemangstoken och 68 s; med alternativet 9 token.

```bash
aipmt --use_opencode --model ollama/gemma4-12b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

Resultat för en verklig bloggartikel med 589 rader (140 länkar, 21 avsnitt,
3 engelska citat skyddade av läget `--news`), samma kommando, tre
modeller:

| Modell                                   | Tid         | Struktur                                                   | Avvikelser                                                                                 |
| ---------------------------------------- | ----------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `opencode/mimo-v2.5-free` (Zen, kostnadsfri) | 4 min 26 s  | identisk med källan                                        | inga                                                                                       |
| `ollama/gemma4-12b-32k` (lokal)          | 10 min 10 s | länkar, URL:er, tabeller, taggar, fetstil och inline-kod identiska | en påhittad citatrad (🇺🇸 + parafras), en duplicerad attribuering                            |
| `ollama/qwen3.5-9b-32k` (lokal)          | 8 min 18 s  | länkar, URL:er, tabeller och taggar identiska              | en påhittad citatrad, viss tillagd fetstil och inline-kod, ett segment bearbetat på nytt    |

Under den lokala översättningen: GPU på 98 % och 170 W, 10 GB VRAM används
(modell och cache för 32 k token, inget avlastat till RAM), 7,5 GB RAM för
Ollama-servern. En modell med 9 till 12 miljarder parametrar bevarar
strukturen men tar sig en frihet per artikel, medan gatewaymodellen
inte tog sig någon: korrekturläs före publicering eller använd endast för utkast.

### Ekonomiläge

Använder snabbare och billigare modeller (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### Alternativ

| Alternativ                   | Beskrivning                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Enskild Markdown-fil som ska översättas                                                                            |
| `--source_dir`           | Källkatalog som innehåller Markdown-filer                                                             |
| `--target_dir`           | Utdatakatalog för de översatta filerna                                                               |
| `--source_lang`          | Källspråk (standard: `fr`)                                                                                  |
| `--target_lang`          | Målspråk (standard: `en`)                                                                                   |
| `--model`                | Specifik modell som ska användas                                                                                  |
| `--eco`                  | Använd ekonomiska modeller                                                                              |
| `--use_mistral`          | Använd Mistral AI API                                                                                     |
| `--use_claude`           | Använd Claude API                                                                                         |
| `--use_gemini`           | Använd Gemini API                                                                                         |
| `--use_codex`            | Använd Codex CLI med ChatGPT-prenumerationens kvot                                                    |
| `--use_grok`             | Använd xAI API (Grok) — kräver `XAI_API_KEY`                                                           |
| `--use_grok_cli`         | Använd Grok CLI med Grok-prenumerationens kvot                                                        |
| `--use_opencode`         | Använd OpenCode (open source) med leverantören som konfigurerats i OpenCode; kräver `--model provider/modèle` |
| `--force`                | Tvinga ny översättning                                                                                       |
| `--keep_filename`        | Behåll det ursprungliga filnamnet                                                                          |
| `--news`                 | Nyhetsläge: skyddar engelska citat och hanterar flaggor per språk                                      |
| `--add_translation_note` | Lägg till en översättningsnotering                                                                                |
| `--note_position`        | Noteringens placering: `top`, `bottom` (standard) eller `both`                                                     |
| `--note_format`          | Noteringens format: `legacy` (standard, stycke i fetstil) eller `marker`                                            |
| `--include_model`        | Inkludera modellnamnet i utdatafilen                                                            |
| `--reasoning_effort`     | Resoneringsansträngning för GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

> **De sju leverantörsflaggorna utesluter varandra.** Tidigare accepterades en kombination av två
> utan varning och den första som testades valdes: en översättning som begärts med
> prenumerationskvot (`--use_codex`, `--use_grok_cli`) kunde därmed debiteras efter användning
> utan någon varning. `argparse` avvisar numera kombinationen.

### Översättningsnotering: placeringar och format

Med `--add_translation_note` kan translator placera noteringen högst upp, längst ned eller på båda ställena och återge den antingen i enkelt textformat (bakåtkompatibelt) eller i formatet `marker` som kan bearbetas av ett Markdown-plugin.

**Placering** (`--note_position`):

- `bottom` (standard): notering i slutet av filen, som tidigare.
- `top`: notering infogad **efter YAML-frontmatter** (säkert för Astro Content Collections, gray-matter osv.).
- `both`: notering infogad både högst upp OCH längst ned (ett enda LLM-anrop, innehållet återanvänds för båda placeringarna).

**Format** (`--note_format`):

- `legacy` (standard): stycke i fetstil `**...**` — exakt samma beteende som i v1.8, byte-for-byte. Kompatibelt med Hugo, GitHub, GitLab och alla Markdown-renderare.
- `marker`: osynlig Markdown-definition av en länkreferens (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), följd av ett blockcitat i fetstil. Kan läsas direkt på GitHub/GitLab och användas vid bygget av ett remark-plugin på Astro-sidan för att skapa en formgiven banner (se bloggen jls42.org).

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

| Leverantör | Kvalitet (standard)                      | Ekonomisk (`--eco`)      |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI   | `gpt-5.6-terra`                       | `gpt-5.6-luna`            |
| Claude   | `claude-sonnet-5`                     | `claude-haiku-4-5`        |
| Mistral  | `mistral-large-latest`                | `mistral-small-latest`    |
| Gemini   | `gemini-3.7-flash`                    | `gemini-3.1-flash-lite`   |
| Codex    | `gpt-5.6-sol`                         | `gpt-5.6-luna`            |
| Grok API | `grok-4.6`                            | `grok-4.3`                |
| Grok CLI | `grok-4.6`                            | `grok-4.5`                |
| OpenCode | `--model provider/modèle` obligatorisk | samma — `--eco` utan effekt |

> **Rekommendation för längre översättningar**: `--use_gemini` (standard = `gemini-3.7-flash`) bevarar Markdown-strukturen korrekt för icke-latinska skriftsystem (PL, JA, ZH, AR, HI), även i läget `--news` där exaktheten hos placeholders är viktig. Uppmätt på denna README översatt till japanska: identisk struktur med `gemini-3.1-pro-preview` (21 listor, 18 kodblock, 13 HTML-länkar, 13 bilder, alla URL:er bevarade) med cirka 6 gånger kortare svarstid. OpenAI förblir standard för bakåtkompatibilitet.

## Projekt som använder detta skript

- **[jls42.org](https://jls42.org)** - Flerspråkig personlig blogg (15 språk)

## Författare

Julien LE SAUX
E-post: contact@jls42.org

## Licens

GNU GENERAL PUBLIC LICENSE version 3. Se [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artikel översatt från franska till svenska med gpt-5.6-sol.**

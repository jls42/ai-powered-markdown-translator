# AI-driven Markdown-översättare

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Kodkvalitet</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status för kvalitetskontroll"></a>
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

Översätter Markdown-filer från ett språk till ett annat samtidigt som
strukturen bevaras: kodblock, inline-kod, URL:er, ankare, tabeller och front
matter. Nio sätt att anropa en modell – fem API:er, två abonnemang utan
användningsbaserad debitering och två routrar – samt ett publicerat mått på vad
varje modell faktiskt bevarar.

## Kort sagt

- **Nio provider-vägar**: API:er från OpenAI, Mistral, Claude, Gemini och Grok;
  ChatGPT- (Codex) och Grok-abonnemang utan användningsbaserad debitering;
  routrarna OpenCode (open source, kostnadsfri eller lokal) och OpenRouter
  (över 400 modeller).
- **Inget felaktigt på grund av en förlorad token**: kodblock, inline-kod,
  URL:er, ankare och citat ersätts med tokens före anropet och
  kontrolleras vid återkomsten. Om en saknas skrivs filen inte.
- **Långa dokument**: segmentering efter modellens kontextfönster.
- **Läget `--news`**: engelska citat skyddas och flaggor hanteras per
  språk för omvärldsbevakningsartiklar.
- **Läget `--eco`**: snabbare och billigare modeller.
- Valfri **översättningsnot**, längst upp, längst ned eller på båda ställena.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 eller senare. För installation från arkivet, se
[Bidra](#bidra).

## Konfiguration

Nycklarna läses från tre platser, från högsta till lägsta prioritet; var och en
fyller endast i det som den föregående lämnar tomt.

|     | Var                                           | För vad                                  |
| --- | --------------------------------------------- | ---------------------------------------- |
| 1   | Miljövariabler                                | CI, containrar, tillfällig åsidosättning |
| 2   | `.env` i aktuell katalog (eller en överordnad) | en projektspecifik nyckel                 |
| 3   | `~/.config/aipmt/.env`                        | installeras en gång, gäller överallt     |

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

`GEMINI_API_KEY` godtas i stället för `GOOGLE_API_KEY`. Användarfilen följer
`XDG_CONFIG_HOME` (endast absolut sökväg) och `%APPDATA%` i Windows. Utan
nyckel listar kommandot de tre platserna.

**Ett projekts `.env` kan inte omdirigera anrop.** Det tillhandahåller
nycklar, aldrig en destination: alla variabler i `_BASE_URL`, `_API_BASE`
eller `_ENDPOINT`, proxyinställningarna (`HTTP_PROXY`, `HTTPS_PROXY`,
`ALL_PROXY`), certifikatlagren (`SSL_CERT_FILE`, `SSL_CERT_DIR`,
`REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) och `XDG_CONFIG_HOME` / `APPDATA` ignoreras
där, med en varning. Ett klonat arkiv ska inte kunna kapa din nyckel. Den här
filen läses även utan interpolering: `NOM=${OPENAI_API_KEY}` kopierar inte
nyckeln dit. Ange dessa variabler i miljön eller i
`~/.config/aipmt/.env`.

Valfria variabler: `XAI_BASE_URL` (standard `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (sekunder per anrop, standard 900), `CODEX_BIN`,
`CODEX_TIMEOUT` (standard 600), `GROK_BIN`, `GROK_HOME` (standard
`~/.grok`), `GROK_TIMEOUT` (standard 900), `GROK_TRANSLATE_SANDBOX`,
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (standard 600), `OPENROUTER_BASE_URL`
(`https://` krävs), `OPENROUTER_TIMEOUT` (standard 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
(standard 30). Var och en beskrivs i detalj i avsnittet för respektive
provider.

## Kom igång

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` översätter till spanska och skapar `document-es.md` i
`--target_dir`; med `--include_model`, `document-es-gpt-5.6-terra.md`. Filändelsen blir alltid
`.md` – `article.mdx` ger `article-en.md` – utom med
`--keep_filename`, som behåller det ursprungliga namnet. En redan befintlig
översättning hoppas över utan `--force`.

Slutkoder: `0` om allt lyckades eller hoppades över,
`1` om någon fil fortfarande misslyckades (listas i felutmatningen),
`2` om problemet gäller konfigurationen. En fil som misslyckas skrivs
aldrig, inte ens om själva skrivningen misslyckas: innehållet skrivs bredvid
och får sedan ett nytt namn. Det räcker att köra igen.

## Vilken modell ska du välja?

Mätt på två verkliga dokument som översattes till samma fjorton språk av varje
modell. **Siffran är antalet språk, av fjorton, där översättningen skrivs och
ingenting skiljer sig från källan.**

| Modell               | Så får du åtkomst                  | Tät omvärldsbevakningsartikel | Denna README | Vad som skiljer sig och på hur många språk                                                                                                         |
| -------------------- | ---------------------------------- | ----------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | API-nyckel från Google             | ✅ 14/14                      | ⚠️ 13/14     | 1 språk av 14: ett extra ord i fetstil (ja)                                                                                                        |
| **GPT-5.6 Sol**      | ChatGPT-abonnemang eller OpenAI-nyckel | ✅ 14/14                  | ⚠️ 12/14     | 2 språk av 14: ett ord mindre i fetstil (ar, ja)                                                                                                   |
| **GLM-5.2**          | OpenRouter-nyckel                  | ✅ 14/14                      | ⚠️ 11/14     | 3 språk av 14: ett ord mindre i fetstil (hi, ja, ko)                                                                                               |
| Claude Sonnet 5      | API-nyckel från Anthropic          | ⚠️ 11/14                      | ⚠️ 12/14     | 3 språk i artikeln: ett kodblock tillkom (es, de, hi); 2 i denna README: en länk utan sin uppmärkning (sv), ett ord i fetstil (zh)                  |
| Qwen 3.7 Flash       | OpenRouter-nyckel                  | ❌ 8/14                       | ⚠️ 10/14     | 1 språk avvisades för artikeln, 5 andra avviker; i denna README sattes ett fyrtiotal ord i `code` (ar)                                      |
| Grok 4.6             | Grok-abonnemang                    | ❌ 8/14                       | ej betygsatt | 5 språk av 14 avvisades eftersom inline-kod och URL:er inte återgavs; nederländskan avviker genomgående                                             |
| GPT-OSS 20B          | lokal modell (Ollama)              | ❌ 7/14                       | inte ommätt  | 4 språk av 14 avvisades: modellen lämnade kvar franska textavsnitt, som skyddet stoppade                                                            |
| MiMo v2.5 (kostnadsfri) | OpenCode Zen, utan konto        | ❌ 11/14                      | inte ommätt  | 1 språk avvisades; ett avsnitt försvann på polska                                                                                                  |
| Mistral Large        | API-nyckel från Mistral            | ❌ 5/14                       | ❌ 1/14      | **ett helt avsnitt försvinner**: 1 språk i artikeln (hi), 3 i denna README (ar, hi, ko) – och 3 språk avvisades för artikeln                        |
| DeepSeek V4 Flash    | OpenRouter-nyckel                  | ❌ 3/14                       | inte ommätt  | 10 språk av 14 avvisades; 37 minuter per språk                                                                                                     |

|     | Vad symbolen betyder                                                                                                                                                                                          |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alla fjorton språk översattes och ingenting skiljer sig från källan                                                                                                                                            |
| ⚠️  | alla fjorton språk översattes; det som skiljer sig är **uppmärkning** – ett ord i fetstil, en `code`, en länk som förlorar sina hakparenteser. Ingen text, URL, kodblock eller avsnitt saknas             |
| ❌  | minst ett språk kunde inte översättas – filen avvisas och skrivs inte – **eller** innehåll saknas i en skriven fil                                                                                              |

Detta är slutsatserna:

- **En avvisad översättning är inte en skadad översättning.** När en token
  saknas i svaret skrivs filen inte och språket räknas som avvisat. Det är vad
  som händer med Grok för artikeln: fyra inline-koder och tre URL:er förloras
  redan i det första segmentet för de fem icke-latinska skriftsystemen.
- **Det här skyddsnätet omfattar inte rubriker, tabeller, front matter eller
  text.** En modell som tar bort ett avsnitt returnerar en fil som verktyget
  skriver utan invändning – så är fallet med Mistral. Dessa element kan inte
  ersättas med en token, och de nuvarande kontrollerna granskar dem inte;
  `scripts/compare_structure.py` upptäcker ett förlorat avsnitt, men först i efterhand.
- **Grok har inget betyg för denna README**: dess CLI-session löpte ut efter
  tolv språk, varav elva utan avvikelse. En avbruten körning betygsätts inte.
- **Dokumentets täthet spelar större roll än språket.** Grok klarar vanliga
  README-filer men faller bort i en länkintensiv artikel, även på nederländska.

Datum och dokument: kolumnen ”Denna README” mättes den 9 september 2026
på en låst version av den här filen (785 rader, 285 inline-koder, 89
tabellrader), som sedan dess har justerats. Kolumnen ”Tät
omvärldsbevakningsartikel” kommer från körningen den 4 och 5 september på en
artikel med 589 rader, förutom raden för Grok, som mättes på nytt den 9
september på en annan utgåva av samma omvärldsbevakning. De fullständiga
tabellerna, tidsåtgången och protokollet finns i
[Detaljerade mätningar](#detaljerade-mätningar).

## Alla alternativ

| Alternativ                | Beskrivning                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `--file`            | En enda Markdown-fil att översätta (alternativ till `--source_dir`)                                          |
| `--source_dir`            | Källkatalog som innehåller Markdown-filerna (standard: `content/posts`)                                       |
| `--target_dir`            | Utdatakatalog för de översatta filerna (standard: `traductions_en`)                                           |
| `--source_lang`            | Källspråk (standard: `fr`)                                                                         |
| `--target_lang`            | Målspråk (standard: `en`)                                                                          |
| `--model`            | Specifik modell att använda                                                                                  |
| `--eco`            | Använd de ekonomiska modellerna                                                                              |
| `--use_mistral`            | Använd Mistral AI API                                                                                        |
| `--use_claude`            | Använd Claude API                                                                                            |
| `--use_gemini`            | Använd Gemini API                                                                                            |
| `--use_grok`            | Använd xAI API (Grok) – kräver `XAI_API_KEY`                                                                |
| `--use_codex`            | Använd Codex CLI med kvoten från ChatGPT-abonnemanget                                                       |
| `--use_grok_cli`            | Använd Grok CLI med kvoten från Grok-abonnemanget                                                           |
| `--use_opencode`            | Använd OpenCode (open source) mot den provider som konfigurerats i OpenCode; kräver `--model provider/modèle`           |
| `--use_openrouter`            | Använd OpenRouter – kräver `OPENROUTER_API_KEY` och `--model fournisseur/modèle`                                                |
| `--force`            | Tvinga en ny översättning                                                                                    |
| `--keep_filename`            | Behåll det ursprungliga filnamnet                                                                            |
| `--news`            | Nyhetsläge: skyddar engelska citat och hanterar flaggor per språk                                            |
| `--add_translation_note`            | Lägg till en översättningsnot                                                                                |
| `--note_position`            | Notens placering: `top`, `bottom` (standard) eller `both`                            |
| `--note_format`            | Notens format: `legacy` (standard, stycke i fetstil) eller `marker`                             |
| `--include_model`            | Inkludera modellnamnet i utdatafilen                                                                         |
| `--reasoning_effort`            | Resoneringsansträngning för GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

De åtta `--use_*`-flaggorna är ömsesidigt uteslutande: att kombinera två
avvisas.

## Providers

### Via API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` växlar till varje providers ekonomiska nivå.

| Provider   | Kvalitet (standard)                                  | Ekonomisk (`--eco`)       |
| ---------- | ---------------------------------------------------- | -------------------------------- |
| OpenAI     | `gpt-5.6-terra`                                      | `gpt-5.6-luna`                  |
| Claude     | `claude-sonnet-5`                                      | `claude-haiku-4-5`                  |
| Mistral    | `mistral-large-latest`                                      | `mistral-small-latest`                  |
| Gemini     | `gemini-3.7-flash`                                      | `gemini-3.1-flash-lite`                  |
| Codex      | `gpt-5.6-sol` (även `terra` och `luna` via `--model`) | `gpt-5.6-luna` |
| Grok API   | `grok-4.6`                                      | `grok-4.3`                  |
| Grok CLI   | `grok-4.6`                                      | `grok-4.5`                  |
| OpenCode   | `--model provider/modèle` krävs                                | samma – `--eco` utan effekt |
| OpenRouter | `--model fournisseur/modèle` krävs                                | samma – `--eco` utan effekt |
### Med ChatGPT-prenumerationen: `--use_codex`

Styr det officiella Codex CLI: översättningen räknas av från kvoten för
ChatGPT-prenumerationen, utan API-nyckel eller användningsbaserad debitering.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Binärfilen söks efter i `CODEX_BIN`, därefter i `PATH` och sedan i paketet
  `openai-codex-cli-bin`. `~/.codex/auth.json` läses aldrig.
- `OPENAI_API_KEY` och `CODEX_API_KEY` tas bort från underprocessens
  miljö: en befintlig nyckel leder aldrig till en övergång till API:t.
- Varje segment kostar minst ett ”meddelande” i 5-timmarsfönstret – två
  om valideringen misslyckas och det görs ett nytt försök. OpenAI anger som
  uppskattning 250–2 000 meddelanden/5 h för `gpt-5.6-luna` (`--eco`) och
  10–100 för `gpt-5.6-sol` med ett Plus-abonnemang.
- `--model gpt-5.6-terra` och `--model gpt-5.6-luna` går också via
  prenumerationen. En modell som kontot saknar behörighet till returnerar ett 400-fel: ”model is
  not supported when using Codex with a ChatGPT account”.
- Långsammare än ett API, och skillnaden växer med dokumentet: för denna README,
  6 min 46 s per språk i median med `gpt-5.6-sol`, jämfört med 36 s för
  `gemini-3.7-flash`.
- Nekas i CI (`CI` eller `GITHUB_ACTIONS` definierad): prenumerationen autentiseras
  via en personlig sessionsfil som inte hör hemma på en delad runner.
- Variabler: `CODEX_BIN`, `CODEX_TIMEOUT` (sekunder per segment, standardvärde 600).

### Med Grok-prenumerationen: `--use_grok_cli`

Samma princip med det officiella Grok Build CLI, via en SuperGrok- eller
X Premium+-prenumeration.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Svagare isolering än Codex.** Groks OS-sandbox fungerar inte
  på många moderna Linux-datorer (AppArmor, sockets för container-runtime),
  och en profil som inte kan tillämpas startar tyst utan isolering.
  Skriptet begär därför ingen profil som standard, upplyser om detta och
  förlitar sig på CLI-reglerna `--deny`, inklusive catch-all-regeln `*` – det enda
  lagret som vägrar starta i stället för att ta bort skyddet utan att
  meddela det. `GROK_TRANSLATE_SANDBOX=read-only` kräver OS-sandboxen, och starten
  misslyckas om datorn inte kan tillhandahålla den.
- Kvoten är veckovis, delas med Chat, Imagine och Voice, och inget
  kommando kan läsa av den: en batch kan förbruka en del av den konversationsbaserade
  användningen utan någon varning.
- Variabler: `GROK_BIN`, `GROK_HOME` (CLI-katalog, standardvärde `~/.grok`),
  `GROK_TIMEOUT` (standardvärde 900), `GROK_TRANSLATE_SANDBOX`.

### Till valfri leverantör: `--use_opencode`

[OpenCode](https://opencode.ai) är en kodagent med öppen källkod (MIT) som
dirigerar till leverantörer som konfigurerats i den: API-nyckel, prenumeration,
OpenCode Zen-gateway (kostnadsfria modeller utan konto) eller lokal modell. Två
alternativ har mätts från början till slut här: Zen och Ollama.

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

`--model` är obligatorisk: utan den skulle OpenCode falla tillbaka på en kostnadsfri modell
vars interaktioner kan användas för träning, och det valet görs inte åt
dig.

Isolering vid varje anrop:

- en inline-konfiguration som har företräde framför din definierar en agent `aipmt`
  där alla verktyg nekas (`permission: { "*": "deny" }`), sessionsdelning är
  inaktiverad, `--pure`, aldrig `--auto`;
- en tillfällig och tom arbetskatalog, med `OPENCODE_DISABLE_PROJECT_CONFIG` och
  `OPENCODE_DISABLE_CLAUDE_CODE` angivna – utan dem infogar OpenCode
  `AGENTS.md` från den aktuella katalogen och `~/.claude/CLAUDE.md` i prompten. Den
  globala `~/.config/opencode/AGENTS.md` infogas fortfarande; OpenCode tillåter inte
  att den utesluts;
- utdatakontrakt: returkod 0, ingen `error`-händelse, inget
  verktygsanrop, sista steget i `stop`, icke-tom text och agenten `aipmt`
  faktiskt inläst – en okänd `--agent` får inte OpenCode att misslyckas, utan
  den faller tyst tillbaka på kodningsagenten;
- ingen nyckel från `aipmt` skickas vidare, förutom `OPENCODE_API_KEY`, OpenCodes
  egen nyckel. Leverantörerna konfigureras i OpenCode, inte i
  `.env` för `aipmt`.

Bra att veta:

- Zens kostnadsfria modeller förändras, har odokumenterade gränser och
  deras interaktioner kan användas för träning: lämpligt för offentlig
  dokumentation, inte för privat innehåll.
- En lokal modell måste erbjuda minst 16 k tokens kontext eftersom segmenten
  kan omfatta upp till 16 000 tecken. Ollama konfigurerar ofta 4 096: använd
  en `Modelfile` med `PARAMETER num_ctx 32768`.
- `--eco` har ingen effekt; `--reasoning_effort` skickas oförändrad som
  OpenCodes `--variant`.
- OpenCode loggar varje session i `~/.local/share/opencode/`.
- Variabler: `OPENCODE_BIN` (annars `PATH`, därefter `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (sekunder per segment, standardvärde 600). `OPENCODE_CONFIG`
  skickas oförändrad till OpenCode.

Exempel på en lokal modell via Ollama, i `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` stänger av den reflektion som Ollama aktiverar som standard för dessa
modeller och som en Modelfile inte kan inaktivera. Uppmätt för en mening på
sex ord: 919 reflektionstokens och 68 sekunder utan alternativet, 9 tokens med det.

### Till fler än 400 modeller: `--use_openrouter`

OpenRouter är en användningsdebiterad router, med ett samlat saldo, framför
modeller som drivs av tredje part – däribland öppna kinesiska modeller som ingen
annan leverantör erbjuder här.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` är obligatorisk. En preflight-kontroll som körs före all debitering hanterar
två särskilda egenskaper hos routningen:

- **Samma modell tillhandahålls av dussintals värdar med olika
  gränser** – för `z-ai/glm-5.3-flash`, 23 värdar, varav en är begränsad till
  2 048 tokens i utdata. Preflight-kontrollen läser `/api/v1/models/{modèle}/endpoints`,
  utesluter värdar med mindre än 8 000 tokens i utdata eller försämrad status och
  fäster de övriga med `allow_fallbacks: false`.
- **Resonemang debiteras enligt utdatataxan** – 107 tokens jämfört med 2 för
  ett ”OK”-svar från `z-ai/glm-5.2`. Det stängs av som standard; modeller
  som kräver det får den lägsta ansträngningsnivå de accepterar, eftersom
  katalogens standardvärde kan fylla hela utdatan innan översättningen är färdig.
  `--reasoning_effort` har fortfarande företräde.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Kontextfönstret hämtas från katalogen. En modell med färre än 16 400 tokens
  nekas före alla anrop: 8 400 för prompten och segmentet, minst 8 000 för
  utdata.
- En slug som saknas i katalogen, en katalog som inte kan nås eller avsaknaden
  av en värd som klarar gränsen stoppar kommandot.
- `finish_reason=length` med tom utdata innebär att budgeten har förbrukats av
  resonemanget, inte att svaret har trunkerats: meddelandet skiljer mellan dessa fall.
- `--eco` har ingen effekt.
- Variabler: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (standardvärde `https://openrouter.ai/api/v1`, `https://`
  krävs), `OPENROUTER_TIMEOUT` (standardvärde 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (standardvärde 30).

### Översättningsnotering

`--add_translation_note` lägger till en notering, i `bottom` (standardvärde), `top` (efter
front matter) eller `both` (`--note_position`), i formatet `legacy` (stycke i
fetstil, standardvärde) eller `marker` (`--note_format`). Formatet `marker` är en
osynlig Markdown-referensdefinition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
följd av ett citat i fetstil: läsbart på GitHub och tillgängligt under bygget för ett
remark-plugin.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detaljerade mätningar

Alla mätningar är faktiskt utförda översättningar med `aipmt`, till
fjorton språk: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Skrivna** räknar de filer som kontrollerna släppte igenom; **Utan
avvikelse** de där `scripts/compare_structure.py` inte hittar något – samma antal
avsnitt, underrubriker, länkar, unika URL:er, kodblock,
inline-koder, tabellrader, blockcitat och ord i fetstil.

”Utan avvikelse” betyder ”inget upptäckt”, inte ”identisk”: jämföraren
räknar element utan att läsa deras innehåll. Den upptäcker varken en borttagen
rubrik på nivå 4, texten i en inline-kod som ersatts eller en utbytt
flagga, och den bedömer inte språket.

### Omfattande bevakningsartikel, läget `--news`

En utgåva av [AI-bevakningen på jls42.org](https://jls42.org/fr/news):
589 rader, 140 länkar, 21 avsnitt, 3 skyddade engelska citat. Kampanj
den 4 och 5 september 2026.

| Modell                            | Åtkomst              | Skrivna | Utan avvikelse | Median/språk |
| --------------------------------- | -------------------- | ------- | -------------- | ------------ |
| `gemini-3.7-flash`                | Google API           | 14/14   | ✅ **14/14**   | 1 min 18 s   |
| `gpt-5.6-sol` (`--use_codex`)     | ChatGPT-prenumeration | 14/14   | ✅ **14/14**   | 11 min 28 s  |
| `z-ai/glm-5.2`                    | OpenRouter           | 14/14   | ✅ **14/14**   | 5 min 37 s   |
| `qwen/qwen3.8-flash`              | OpenRouter           | 14/14   | ✅ **14/14**   | 26 min 23 s  |
| `claude-sonnet-5`                 | Anthropic API        | 14/14   | ⚠️ 11/14      | 6 min 31 s   |
| `opencode/mimo-v2.5-free`         | OpenCode Zen         | 13/14   | ❌ 11/14       | 9 min 27 s   |
| `qwen/qwen3.7-flash`              | OpenRouter           | 13/14   | ❌ 8/14        | 10 min 09 s  |
| `ollama/gpt-oss-20b-32k`          | lokal                | 10/14   | ❌ 7/14        | 12 min 39 s  |
| `mistral-large-latest`            | Mistral API          | 11/14   | ❌ 5/14        | 5 min 32 s   |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter           | 4/14    | ❌ 3/14        | 37 min 27 s  |
| `grok-4.6` (`--use_grok_cli`)     | Grok-prenumeration   | 1/14    | ❌ 1/14        | 23 min 11 s  |

Grok mättes på nytt den 9 september med en annan utgåva av samma bevakning
(356 rader): 9 språk skrivna av 14, varav 8 utan avvikelse. Det är denna siffra som
visas i den inledande tabellen. Tre avbrutna kampanjer redovisas inte:
`qwen3.5-27b` (9 språk) och `kimi-k2.6` (4) på grund av brist på saldo,
`z-ai/glm-5.3-flash`, vars två misslyckanden berodde på en resonemangsinställning
som leverantören håller på att korrigera. OpenRouter-raderna mättes med
routerns standardinställningar, före `--use_openrouter`; `z-ai/glm-5.2`,
som mättes på nytt med den medföljande leverantören, ger samma 14/14. Siffrorna
räknades om den 10 september med den aktuella jämföraren: `qwen3.8-flash` och
`qwen3.7-flash` vinner vardera ett språk jämfört med den första
publiceringen, medan de övriga är oförändrade.

### Projektets README, vanlig Markdown

Revision fryst den 9 september 2026: 785 rader, 285 inline-koder, 40
kodblocksstängsel, 89 tabellrader. Fyra parallella översättningar.

| Modell                        | Skrivna | Utan avvikelse | Median/språk | Det som skiljer sig                                                      |
| ----------------------------- | ------- | -------------- | ------------ | ------------------------------------------------------------------------ |
| `gemini-3.7-flash`            | 14/14   | ⚠️ 13/14       | 36 s         | ett ord i fetstil (ja)                                                   |
| `claude-sonnet-5`             | 14/14   | ⚠️ 12/14       | 2 min 56 s   | en länk (sv), ett ord i fetstil (zh)                                     |
| `gpt-5.6-sol` (`--use_codex`) | 14/14   | ⚠️ 12/14       | 6 min 46 s   | ett ord i fetstil (ar, ja)                                               |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14   | ⚠️ 11/14       | 2 min 34 s   | ett ord i fetstil (hi, ja, ko)                                           |
| `qwen/qwen3.7-flash`          | 14/14   | ⚠️ 10/14       | 2 min 17 s   | 40 inline-koder tillagda på arabiska; fetstil (hi, ja, ko)               |
| `mistral-large-latest`        | 14/14   | ❌ 1/14         | 2 min 44 s   | ett avsnitt saknas (ar, hi, ko); kodblock tillagda (ja, ko, ro, zh)      |

Två avbrutna kampanjer redovisas inte: Grok, vars CLI-session löpte ut
efter tolv språk (elva utan avvikelse), och `qwen3.8-flash`, vars
värd returnerade HTTP 429 efter två. `opencode/mimo-v2.5-free` och `ollama/gpt-oss-20b-32k`
mättes inte på nytt med denna revision; med den från den 4 och 5 september,
som var 277 rader kortare, skrev de vardera 9 översättningar av 14, varav 7
respektive 1 utan avvikelse.

### Fyra README-filer från välkända projekt

FastAPI, Ollama, tldr-pages och Vue.js, hämtade i befintligt skick från GitHub – dokument
som är enklare än de två föregående. Kampanjen riktade sig mot modeller
med svårigheter; Gemini används som jämförelsepunkt.

| Modell                    | Omfattning                 | Skrivna | Utan avvikelse |
| ------------------------- | -------------------------- | ------- | -------------- |
| `gemini-3.7-flash`        | 4 projekt × 14 språk       | 56/56   | ✅ **55/56**   |
| `opencode/mimo-v2.5-free` | 4 projekt × 14 språk       | 55/56   | ❌ 47/56       |
| `grok-4.6` (prenumeration)   | 4 projekt × ar, hi, ja, zh | 16/16   | ❌ 14/16       |
| `ollama/gpt-oss-20b-32k`  | 4 projekt × ar, hi, ja, zh | 15/16   | ❌ 9/16        |

### Vad dessa mätningar inte är

- **Ingen heltäckande rangordning**: enbart OpenRouter erbjuder över fyrahundra
  modeller; omkring femton har mätts.
- **Ungefärliga tidsangivelser**: tre till sex parallella översättningar beroende
  på kampanj, och en leverantörs kapacitet varierar under dagen.
- **Tidsbundna observationer**: modeller förändras under samma namn, och dina
  dokument är inte våra.

För att upprepa mätningen på dina dokument, med en fryst kopia av filen:

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## Bidra

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

Båda raderna behövs: utan `pip install -e .` svarar `python -m aipmt`
med `No module named aipmt`.

Kvalitetsverktyg, valfria men rekommenderade:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Databasens 28 översättningar (README och CHANGELOG, fjorton språk)
återskapas med `./regen_translations.sh --force` – Codex och `gpt-5.6-sol` via
ChatGPT-prenumerationen som standard, fyra parallellt. `REGEN_PROVIDER` och
`REGEN_MODEL` ändrar sökvägen; ett avgiftsbelagt API (`openai`, `gemini`,
`grok`, `openrouter`) nekas utan `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` begränsar varje jobb (600 s, 1 800 s för Codex). Detaljer om
verktygen finns i `CLAUDE.md`.

## Projekt som använder detta skript

- **[jls42.org](https://jls42.org)** – personlig blogg publicerad på 15 språk. Dess
  [dagliga AI-bevakning](https://jls42.org/fr/news) översätts varje dag
  med detta verktyg och används som referensdokument för mätningarna ovan.

## Författare

Julien LE SAUX
E-post: contact@jls42.org

## Licens

GNU GENERAL PUBLIC LICENSE Version 3. Se [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Ansvarsfriskrivning

Detta program distribueras **utan någon garanti**, enligt villkoren i
avsnitt 15 och 16 i GPL v3: det tillhandahålls ”i befintligt skick”, utan garanti för
säljbarhet eller lämplighet för ett särskilt ändamål, och upphovsmannen kan inte
hållas ansvarig för skador som uppstår till följd av dess användning. Licenstexten
har företräde framför denna sammanfattning.

- **Läs igenom före publicering.** Skydden omfattar kodblock,
  inline-kod, URL:er, ankare och citat i läget `--news` – men inte
  rubriker, tabeller, front matter eller innebörden i dina meningar.
- **Dina dokument skickas till den valda leverantören**, enligt dess
  användningsvillkor och datapolicy. Vissa kostnadsfria modeller kan
  återanvända dina interaktioner för träning; en lokal modell är det enda
  alternativet där inga data lämnar din dator.
- **API-anropen debiteras dig.** Programmet begränsar inte
  kostnaden: ett långt dokument, ett nytt försök efter ett fel eller en modell som resonerar
  mycket kostar mer.
- **De publicerade mätningarna är tidsbundna observationer**, inte garantier.

De nämnda produkt- och företagsnamnen tillhör respektive innehavare.
Projektet är inte knutet till någon av dem.

**Artikel översatt från franska till svenska med gpt-5.6-sol.**

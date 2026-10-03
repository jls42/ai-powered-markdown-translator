# AI-driven Markdown-översättare

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Kodkvalitet</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Quality Gate Status"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Security Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Reliability Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Maintainability Rating"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Coverage"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilities"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Duplicated Lines (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Technical Debt"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Lines of Code"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy Badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Översätter Markdown-filer från ett språk till ett annat med bibehållen
struktur: kodblock, inline-kod, webbadresser, ankare, tabeller och front
matter. Elva sätt att anropa en modell – fem API:er, fyra prenumerationer utan
användningsbaserad fakturering, två routrar – och ett publicerat mått på vad varje
modell faktiskt bevarar.

## I korthet

- **Elva leverantörsvägar**: OpenAI-, Mistral-, Claude-, Gemini- och Grok-API:er;
  ChatGPT- (Codex), Grok-, Google- (Antigravity) och Claude-prenumerationer (Claude
  Code) utan användningsbaserad fakturering; OpenCode-routrar (öppen källkod, gratis eller lokalt) och OpenRouter
  (fler än 400 modeller).
- **Inget felaktigt på grund av en förlorad token**: kodblock, inline-kod,
  webbadresser, ankare och citat ersätts med tokens före anropet och
  verifieras vid retur. Om en saknas skrivs filen inte.
- **Långa dokument**: segmentering baserad på modellens kontextfönster.
- **`--news`-läge**: skyddade engelska citat och flaggor hanterade per
  språk, för bevakningsartiklar.
- **`--eco`-läge**: snabba och billigare modeller.
- Valfri **översättningsnotering**, överst, nederst eller på båda ställena.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 eller senare. För att installera från arkivet, se
[Bidra](#bidra).

## Konfiguration

Nycklar läses från tre platser, från högst till lägst prioritet; varje plats
fyller endast i vad den föregående lämnar tomt.

|     | Var                                           | För vad                               |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Miljövariabler                                | CI, containrar, tillfälligt åsidosättande |
| 2   | `.env` i aktuell katalog (eller en överordnad) | en projektspecifik nyckel             |
| 3   | `~/.config/aipmt/.env`                        | installeras en gång, gäller överallt  |

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

`GEMINI_API_KEY` accepteras i stället för `GOOGLE_API_KEY`. Användarfilen
följer `XDG_CONFIG_HOME` (endast absolut sökväg) och `%APPDATA%`
under Windows. Utan nyckel listar kommandot de tre platserna.

**Ett projekts `.env` kan varken omdirigera anrop eller välja vilket program
som körs.** Det tillhandahåller nycklar, aldrig en destination eller en binär: alla
variabler i `_BASE_URL`, `_API_BASE`, `_ENDPOINT` eller `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, proxyservrar (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), certifikatarkiv (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) och `XDG_CONFIG_HOME` /
`APPDATA` ignoreras där, med en varning. Ett klonat arkiv får inte
kunna kapa din nyckel eller få dig att köra dess eget program vid
första översättningen. Denna fil läses också utan interpolering:
`NOM=${OPENAI_API_KEY}` kopierar inte nyckeln där. Placera dessa variabler i
miljön eller i `~/.config/aipmt/.env`.

Valfria variabler: `XAI_BASE_URL` (standard `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (sekunder per anrop, standard 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(standard 600), `GROK_BIN`, `GROK_HOME` (standard `~/.grok`), `GROK_TIMEOUT`
(standard 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (standard 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (standard 600), `OPENROUTER_BASE_URL`
(`https://` krävs), `OPENROUTER_TIMEOUT` (standard 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (standard 30). Var och en beskrivs i detalj i
avsnittet för respektive leverantör.

## Komma igång

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` översatt till spanska ger `document-es.md` i `--target_dir`;
med `--include_model`, `document-es-gpt-5.6-terra.md`. Filtillägget blir
alltid `.md` – `article.mdx` ger `article-en.md` – förutom med
`--keep_filename`, som behåller det ursprungliga namnet. En översättning som redan finns
hoppas över utan `--force`.

Slutkoder: `0` om allt lyckades eller hoppades över, `1` om en fil
misslyckades (lista på standard error), `2` om konfigurationen är orsak till felet.
En misslyckad fil skrivs aldrig, även om själva skrivningen misslyckas:
innehållet skrivs bredvid och döps sedan om. Det räcker att köra igen.

## Vilken modell ska man välja

Uppmätt på två verkliga dokument, översatta till samma fjorton språk av
varje modell. **Siffran anger antalet språk, av fjorton, där översättningen
skrivs och där ingenting skiljer sig från källan.**

| Modell               | Hur man får åtkomst               | Tät bevakningsartikel   | Denna README | Vad som skiljer sig och på hur många språk                                                                                                                         |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash** | Google-prenumeration (Antigravity) | ✅ 14/14                | ✅ 14/14     | ingenting, i något av de två dokumenten                                                                                                                            |
| **Gemini 3.7 Flash** | Google API-nyckel                 | ✅ 14/14                | ⚠️ 13/14     | 1 språk av 14: ett extra fetstilt ord (ja)                                                                                                                         |
| **Gemini 3.7 Flash** | Google-prenumeration (Antigravity) | ✅ 14/14                | ⚠️ 13/14     | 1 språk av 14: ett fetstilt ord mindre (ko)                                                                                                                        |
| **GPT-5.6 Sol**      | ChatGPT-prenumeration, eller OpenAI-nyckel | ✅ 14/14                | ⚠️ 12/14     | 2 språk av 14: ett fetstilt ord mindre (ar, ja)                                                                                                                   |
| **GLM-5.2**          | OpenRouter-nyckel                 | ✅ 14/14                | ⚠️ 11/14     | 3 språk av 14: ett fetstilt ord mindre (hi, ja, ko)                                                                                                               |
| Claude Sonnet 5      | Claude-prenumeration (Claude Code) | ⚠️ 13/14                | ⚠️ 13/14     | 1 språk av 14 i artikeln: ett extra fetstilt ord (zh); 1 i denna README: en tabellrad sammanslagen med föregående, dold vid visning (ar)                          |
| Claude Haiku 4.5     | Claude-prenumeration (Claude Code) | ⚠️ 11/14                | ✅ 14/14     | 3 språk i artikeln: en avsnittsrubrik ändrad till nivå 1 (en, pl, ro); i denna README ingenting för jämförelsen, men interna länkar dubblerade på engelska        |
| Claude Sonnet 5      | Anthropic API-nyckel              | ⚠️ 11/14                | ⚠️ 12/14     | 3 språk i artikeln: ett tillagt kodblock (es, de, hi); 2 i denna README: en länk utan dess formatering (sv), ett fetstilt ord (zh)                                 |
| Qwen 3.7 Flash       | OpenRouter-nyckel                 | ❌ 8/14                 | ⚠️ 10/14     | 1 språk avvisat i artikeln, 5 andra avviker; i denna README ett fyrtiotal ord satta i `code` (ar)                                                          |
| Grok 4.6             | Grok-prenumeration                | ❌ 8/14                 | ej betygsatt | 5 språk avvisade av 14, på grund av utebliven inline-kod och webbadresser; nederländska avviker på allt                                                            |
| GPT-OSS 20B          | lokal modell (Ollama)             | ❌ 7/14                 | ej ommätt    | 4 språk avvisade av 14: modellen lämnade stycken på franska, spärren stoppade dem                                                                                   |
| MiMo v2.5 (gratis)   | OpenCode Zen, utan konto          | ❌ 11/14                | ej ommätt    | 1 språk avvisat; ett avsnitt förlorat på polska                                                                                                                    |
| Mistral Large        | Mistral API-nyckel                | ❌ 5/14                 | ❌ 1/14      | **ett helt avsnitt försvinner**: 1 språk i artikeln (hi), 3 i denna README (ar, hi, ko) – och 3 språk avvisade i artikeln                                         |
| DeepSeek V4 Flash    | OpenRouter-nyckel                 | ❌ 3/14                 | ej ommätt    | 10 språk avvisade av 14; 37 minuter per språk                                                                                                                      |
| Claude Opus 5.5      | Claude-prenumeration (Claude Code) | ❌ 0/14                 | ✅ 14/14     | artikeln avvisad på alla 14 språk av Opus skyddsspärrar på grund av en kort biolinotis; ingenting i denna README                                                  |

|     | Vad symbolen betyder                                                                                                                                                                                  |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alla fjorton språk översatta och ingenting skiljer sig från källan                                                                                                                                    |
| ⚠️  | alla fjorton språk översatta; det som skiljer sig är **formatering** – ett fetstilt ord, en `code`, en länk som förlorar sina hakparenteser. Ingen text, ingen webbadress, inget kodblock och inget avsnitt saknas |
| ❌  | minst ett språk kunde inte översättas – filen avvisas, skrivs inte – **eller** innehåll saknas i en skriven fil                                                                                      |

Viktiga slutsatser:

- **En avvisad översättning är inte en skadad översättning.** När en token
  saknas vid retur skrivs inte filen och språket räknas som
  avvisat. Det är vad som händer med Grok i artikeln: fyra inline-koder och
  tre webbadresser förlorades redan i första segmentet, i de fem icke-latinska skrifterna.
- **En modell kan avvisa ett helt dokument på grund av en enda mening.** Opus 5.5
  översätter denna README utan en enda avvikelse, men inte en enda bevakningsartikel: dess
  skyddsspärrar stoppar svaret vid en kort biologinotiser. Filen skrivs
  inte och aipmt förklarar varför.
- **Detta skyddsnät täcker inte rubriker, tabeller, front matter eller
  brödtext.** En modell som tar bort ett avsnitt returnerar en fil som verktyget skriver
  utan att tveka – vilket är fallet med Mistral. Dessa element kan inte
  ersättas med en token och de nuvarande skydden kontrollerar dem inte;
  `scripts/compare_structure.py` upptäcker ett förlorat avsnitt, men först i efterhand.
- **Grok har inget betyg för denna README**: dess CLI-session löpte ut efter tolv
  språk, varav elva utan avvikelser. En avbruten kampanj betygsätts inte.
- **Dokumentets densitet spelar större roll än språket.** Grok klarar vanliga
  README-filer men misslyckas med en länkrik artikel, även på
  nederländska.

Datum och dokument: kolumnen ”Denna README” mättes den 9 september 2026
på en fryst revision av denna fil (785 rader, 285 inline-koder, 89 tabellrader),
som har justerats sedan dess – med undantag för raderna Antigravity och Claude Code,
vilka mättes den 26 september på den revision som publicerades med 1.14.0, som var kortare
(600 rader, 257 inline-koder, 85 tabellrader). Kolumnen ”Tät bevakningsartikel”
kommer från kampanjen den 4 och 5 september på en artikel med 589
rader, förutom raden för Grok, som mättes om den 9 september på en annan utgåva av
samma bevakning, samt raderna för Antigravity och Claude Code, som mättes den 26 september
på samma artikel. De fullständiga tabellerna, tidsåtgången och protokollet finns i
[Detaljerade mätningar](#detaljerade-mätningar).

## Alla alternativ

| Alternativ               | Beskrivning                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Enstaka Markdown-fil att översätta (alternativ till `--source_dir`)                                             |
| `--source_dir`           | Källkatalog som innehåller Markdown-filerna (standard: `content/posts`)                                   |
| `--target_dir`           | Utdatakatalog för översatta filer (standard: `traductions_en`)                                    |
| `--source_lang`          | Källspråk (standard: `fr`)                                                                                  |
| `--target_lang`          | Målspråk (standard: `en`)                                                                                   |
| `--model`                | Specifik modell att använda                                                                                  |
| `--eco`                  | Använd ekonomimodeller                                                                              |
| `--use_mistral`          | Använd Mistral AI:s API                                                                                     |
| `--use_claude`           | Använd Claude-API:et                                                                                         |
| `--use_gemini`           | Använd Gemini-API:et                                                                                         |
| `--use_grok`             | Använd xAI-API:et (Grok) — kräver `XAI_API_KEY`                                                           |
| `--use_codex`            | Använd Codex-CLI med kvoten från ChatGPT-prenumerationen                                                    |
| `--use_grok_cli`         | Använd Grok-CLI med kvoten från Grok-prenumerationen                                                        |
| `--use_antigravity`      | Använd Antigravity-CLI (`agy`) med kvoten från Google AI Pro- eller Ultra-prenumerationen                       |
| `--use_claude_code`      | Använd Claude Code-CLI (`claude -p`) med kvoten från Claude Pro- eller Max-prenumerationen                      |
| `--use_opencode`         | Använd OpenCode (öppen källkod) mot leverantören konfigurerad i OpenCode; kräver `--model provider/modèle` |
| `--use_openrouter`       | Använd OpenRouter — kräver `OPENROUTER_API_KEY` och `--model fournisseur/modèle`                          |
| `--force`                | Tvinga omöversättning                                                                                       |
| `--keep_filename`        | Behåll ursprungligt filnamn                                                                          |
| `--news`                 | Nyhetsläge: skyddar EN-citat, hanterar flaggor per språk                                      |
| `--add_translation_note` | Lägg till en översättningsnot                                                                                |
| `--note_position`        | Notens placering: `top`, `bottom` (standard), eller `both`                                                     |
| `--note_format`          | Notens format: `legacy` (standard, stycke i fetstil) eller `marker`                                            |
| `--include_model`        | Inkludera modellens namn i utdatafilen                                                            |
| `--reasoning_effort`     | Resonemangsinsats för GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

De nio `--use_*`-flaggorna är ömsesidigt uteslutande: att kombinera två avvisas.

## Leverantörer

### Via API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` växlar till varje leverantörs ekonominivå.

| Leverantör  | Kvalitet (standard)                                   | Ekonomi (`--eco`) |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol` (även `terra` och `luna` via `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, insats `low`                                | samma — `--eco` har ingen effekt |
| OpenCode    | `--model provider/modèle` obligatorisk                 | samma — `--eco` har ingen effekt |
| OpenRouter  | `--model fournisseur/modèle` obligatorisk              | samma — `--eco` har ingen effekt |

### Med ChatGPT-prenumerationen: `--use_codex`

Styr det officiella Codex-CLI:et: översättningen dras från kvoten för
ChatGPT-prenumerationen, utan API-nyckel eller användningsbaserad debitering.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Binärfilen söks i `CODEX_BIN`, sedan i `PATH`, sedan i paketet
  `openai-codex-cli-bin`. `~/.codex/auth.json` läses aldrig.
- `OPENAI_API_KEY` och `CODEX_API_KEY` tas bort från underprocessens miljö:
  en befintlig nyckel växlar aldrig över till API:et.
- Varje segment kostar minst ett "meddelande" från 5-timmarsfönstret — två
  om dess validering misslyckas och det görs ett nytt försök. OpenAI anger som
  uppskattning 250–2 000 meddelanden/5 tim för `gpt-5.6-luna` (`--eco`) och
  10–100 för `gpt-5.6-sol` på ett Plus-abonnemang.
- `--model gpt-5.6-terra` och `--model gpt-5.6-luna` går också via
  prenumerationen. En modell som kontot inte har behörighet till returnerar 400 "model is
  not supported when using Codex with a ChatGPT account".
- Långsammare än ett API, och skillnaden växer med dokumentets storlek: på denna README,
  medianvärde 6 min 46 s per språk med `gpt-5.6-sol`, mot 36 s för
  `gemini-3.7-flash`.
- Neka i CI (`CI` eller `GITHUB_ACTIONS` definierad): prenumerationen autentiseras
  via en personlig sessionsfil, som inte hör hemma på en delad
  runner.
- Variabler: `CODEX_BIN`, `CODEX_TIMEOUT` (sekunder per segment, standard 600).

### Med Grok-prenumerationen: `--use_grok_cli`

Samma princip med det officiella CLI:et Grok Build, på SuperGrok- eller
X Premium+-prenumerationen.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Svagare isolering än Codex.** Groks OS-sandlåda kan inte tillämpas
  på många moderna Linux-maskiner (AppArmor, socketar för container-körtider),
  och en profil som inte kan tillämpas startar tyst utan isolering. Skriptet begär
  därför ingen profil som standard, meddelar detta och förlitar sig på CLI:ets
  `--deny`-regler, inklusive dess catch-all `*` — det enda lagret
  som vägrar starta i stället för att tyst ta bort skyddet. `GROK_TRANSLATE_SANDBOX=read-only`
  kräver OS-sandlådan, och starten misslyckas om maskinen inte kan uppfylla detta.
- Kvoten är veckovis, delad med Chat, Imagine och Voice, och det finns inget
  kommando för att läsa av den: en batchkörning kan tära på samtalsanvändningen
  utan förvarning.
- Variabler: `GROK_BIN`, `GROK_HOME` (katalog för CLI, standard `~/.grok`),
  `GROK_TIMEOUT` (standard 900), `GROK_TRANSLATE_SANDBOX`.

### Med Google-prenumerationen: `--use_antigravity`

Samma princip med `agy`, Antigravitys officiella CLI: för den som betalar för Google
AI Pro eller Ultra dras översättningen från prenumerationens kvot i stället för
att debiteras per token. Detta är den enda vägen till den kvoten: Gemini CLI betjänar
inte längre dessa konton sedan den 18 juni 2026
([tillkännagivande](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
och Antigravity-SDK:et accepterar endast en API-nyckel eller ett Google Cloud-projekt.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Ingen betalväg förblir öppen.** agy tar endast emot en sluten lista
  av variabler från din miljö — `PATH`, språk och tidszon,
  terminal, identitet, proxys och certifikat, sessionsbuss — och inga nycklar:
  flera av dess variabler växlar ett anrop utan att visa något (uppmätt:
  en skickar dokumentet till en tredjepartsgateway, en annan till ett debiterat
  Google Cloud-projekt), och en exkluderingslista missade något vid varje granskning.
  Före varje segment måste `agy -p /config`, som inte kostar någon kvot, visa
  att betalda AI-krediter är inaktiverade, utan API-nyckel eller Google Cloud-projekt — en
  saknad inställning innebär avvisning —, annars översätts ingenting; loggen för varje
  anrop måste därefter intyga prenumerationen (`authMethod=consumer`), annars
  avvisas svaret.
- **Isolering.** Varje anrop körs i en privat och temporär hemkatalog,
  med en översättningsagent utan verktyg: dina agy-inställningar, regler,
  insticksprogram, MCP-servrar och hooks kommer inte in där, ingenting läggs till i din
  historik, och inloggningen stannar i nyckelringen, som aipmt aldrig läser.
  Om en agent inte hittas faller agy tyst tillbaka på sin kodningsagent
  och dess verktyg: en hel rad i loggen måste bekräfta rätt agent — ett
  dokument som citerar detta meddelande ersätter den inte —, annars avvisas det.
- **Plattformar**: Linux, i en session med en nyckelring (D-Bus-sessionsbuss,
  Secret Service); macOS accepteras, utan att ha mätts där. Avvisas
  under Windows, där agy inte läser variablerna som isolerar varje anrop, och
  under Linux utan sessionsbuss — SSH-session, container, server: agy
  sparar där sin token i en fil i `~/.gemini`, som isoleringen döljer.
  Avvisningen sker före varje start, tillsammans med dess orsak, i stället för en minuts
  väntan på en inloggningskod.
- **Modeller**: de från `agy models`. Gemini-modellerna bär insatsen i sitt namn
  (`gemini-3.8-flash-medium`…): ett namn utan suffix avvisas före anropet,
  och `--reasoning_effort` har ingen effekt. Som standard `gemini-3.8-flash-medium`,
  och `gemini-3.7-flash-low` i `--eco`; kampanjerna som fastställde dem
  beskrivs i [Detaljerade mätningar](#detaljerade-mätningar). Claude och GPT-OSS
  har sin egen kvot, som är mycket mindre: cirka 1 % av 5-timmarsfönstret
  per uppmätt anrop, mot 0,05 % för Flash.
- **Kvot**: per grupp, ett 5-timmarsfönster och ett veckofönster,
  proportionellt mot tokenkostnaden. Uppmätt på författarens konto: cirka
  16 poäng i 5-timmarsfönstret per miljon källtecken med
  `gemini-3.8-flash-medium`, 14 med `gemini-3.7-flash-medium` och 7 till 8 vid
  låg insats — en README på 40 000 tecken kostar alltså lite mer än en
  halv poäng. Veckogränsen beror i sin tur på nivån. Nya försök följer
  det som agy deklarerar som möjligt att försöka igen; i annat fall görs aldrig
  nya försök för ett förbrukat fönster: det gör att varje fil misslyckas fram
  till återställningen som visas av `/usage`.
- **Långsammare än API:et**: på mätningarnas täta artikel, medianvärde 3 min 59 s per
  språk i `gemini-3.8-flash-medium` och 3 min 14 s i
  `gemini-3.7-flash-medium`, mot 1 min 18 s för Gemini 3.7 Flash via API:et.
- **Avbrott**: Ctrl-C, eller en stängd terminal, stoppar agy tillsammans med
  kommandot i stället för att låta det slutföra sin körning på din kvot; det gäller
  även för Codex, Grok CLI och OpenCode. Under `nohup` fortsätter översättningen.
- Neka i CI (`CI` eller `GITHUB_ACTIONS` definierad): inloggningen finns i en
  personlig nyckelring. På en runner, `--use_gemini` med `GOOGLE_API_KEY`.
- Variabler: `AGY_BIN` (annars `PATH`, sedan `~/.local/bin/agy`),
  `AGY_TIMEOUT` (sekunder per segment, inklusive start, standard 900).

**Användarvillkor: det är ditt konto som berörs.**
[Antigravitys användarvillkor](https://antigravity.google/terms) (avsnitt 6) och dess
[vanliga frågor](https://antigravity.google/docs/faq/) förbjuder åtkomst till tjänsten
via programvara från tredje part med hjälp av Antigravity-inloggningen — Claude Code,
OpenClaw och OpenCode nämns där —, med risk för kontoavstängning. aipmt
läser inte och återanvänder inte token: det startar den officiella binärfilen i det
[headless-läge](https://antigravity.google/docs/cli/headless/) som Google
dokumenterar för skript och CI. En Google-medarbetare ansåg det vara "standard"
att starta `agy -p` från ett lokalt skript för sitt eget arbete
([officiellt forum, 25 september 2026, icke-bindande svar](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
ingen text avgör frågan gällande ett distribuerat verktyg som detta.

**Endast offentliga dokument.** Enligt avsnitt 5 i samma villkor kan
interaktioner — promptar, svar, metadata — användas för att förbättra
Googles produkter och maskininlärning samt granskas av människor,
även för betalprenumerationer. Opt-out sker via inställningen
`enableTelemetry`, vars effekt inte är dokumenterad och som aipmt inte konfigurerar; dina inställningar
för agy följer inte med i dess isolering. Kör ingenting konfidentiellt genom detta.

### På Claude-abonnemanget: `--use_claude_code`

Samma princip med `claude`, det officiella CLI:et för Claude Code, i läget `-p`: för
den som betalar för Claude Pro eller Max räknas översättningen av mot
abonnemangskvoten istället för att faktureras per token. Ska inte förväxlas med
`--use_claude`, Anthropos API, som faktureras efter användning.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Ingen betalväg förblir öppen, och varje anrop bevisar det.** Claude
  Code tar endast emot en sluten lista med variabler från din miljö – varken
  API-nyckel, token, molnleverantör eller markör för den Claude Code-session
  som aipmt startades från. Före det första segmentet måste `claude auth status`
  visa abonnemangsinloggningen, utan Console-nyckel, och `/usage`, som inte kostar
  någon kvot, måste intyga detta; varje anrop intygar det i sin tur i sin
  initieringshändelse, annars avvisas svaret.
- **Inaktivera "extra usage"** (claude.ai, Inställningar → Användning) för
  att nollkronorsgränsen ska hålla: om det är aktiverat tar det över när ett fönster tar slut och
  fakturerar utan att visa något fel. aipmt avbryter översättningen så snart
  kvotavläsningen från ett anrop signalerar detta, men det anropet har redan räknats.
- **Delad kvot med dina Claude Code-sessioner.** Varje anrop rapporterar
  användningen för 5-timmars- och veckofönstren; över 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) startas inga fler segment, för att inte
  förbruka det som behövs för ditt arbete.
- **Isolering.** Varje anrop körs utan verktyg, i en privat och
  temporär katalog, i ett läge utan anpassningar: varken dina `CLAUDE.md`, dina insticksprogram,
  hooks, MCP-servrar eller inställningar läses in, och ingenting sparas från
  sessionen. Bilagor är avstängda: en `@chemin` i ditt dokument
  förblir text och öppnar ingen fil (uppmätt).
- **Modeller**: `sonnet` som standard, med ansträngningsnivå `low`, och även i `--eco`:
  `--eco` ändrar ingenting på denna väg. Uppmätt på samma dokument är `haiku`
  dubbelt så långsam – den resonerar utan att man kan förhindra det – till
  en knappt lägre kostnad, och `opus` avvisar biologiinnehåll (nästa
  punkt). Båda förblir tillgängliga via `--model`; dessa alias följer den
  senaste modellen i sin familj. `fable` och `[1m]`-varianterna avvisas,
  eftersom de debiteras mot betalda krediter. `--reasoning_effort` justerar ansträngningen,
  vilket en översättning inte har någon nytta av: det uppmätta resonemanget är obefintligt eller nästintill.
- **Opus avvisar visst biologiinnehåll.** Dess skyddsbarriärer är mer
  strikta än Sonnets, och felmeddelandet från Anthropic varnar för att de
  "can sometimes flag biology-research-adjacent work". Uppmätt: en kort
  bevakningsnotis om 279 genererade molekyler fick artikeln att avvisas på alla fjorton
  språk. Ingenting skrivs: aipmt avvisar det trunkerade svaret, anger
  skyddsbarriärerna och rekommenderar `--model sonnet`.
- Avvisas i CI (`CI` eller `GITHUB_ACTIONS` definierad) och under Windows (ej uppmätt).
- Variabler: `AIPMT_CLAUDE_BIN` (annars `PATH`, därefter `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (sekunder per segment, standard 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (standard 0.8), `CLAUDE_CONFIG_DIR` (Claude
  Codes konto, hämtas aldrig från ett projekts `.env`); arbetskataloger under
  `XDG_CACHE_HOME/aipmt/claude-code` (standard `~/.cache`).

**Användarvillkor: det är ditt konto som berörs.** Claude
Codes [juridiska sida](https://code.claude.com/docs/en/legal-and-compliance)
hindrar inte "an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription": det är vad aipmt gör, som kör den
officiella binären och aldrig läser av tokenet. Men Anthropic "does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users", föredrar API-nyckel för
tredjepartsverktyg, "including open-source projects", och förbehåller sig rätten att dra av deras
användning från betalda krediter
([Claude-hjälpen](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Ingen text avgör fallet med ett distribuerat verktyg som startar binären.

**Data**: för Free-, Pro- och Max-konton gäller modellträning
även för Claude Code när sekretessinställningen tillåter det
([datasidan](https://code.claude.com/docs/en/data-usage)). aipmt sparar
ingen lokal transkription (`--no-session-persistence`). Skicka
inget konfidentiellt genom det.

### Till valfri leverantör: `--use_opencode`

[OpenCode](https://opencode.ai) är en kodagent med öppen källkod (MIT) som
dirigerar till leverantörer som konfigurerats i den: API-nyckel, abonnemang,
OpenCode Zen-gateway (gratismodeller, utan konto) eller lokal modell. Två
vägar har mätts från ände till ände här: Zen och Ollama.

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

`--model` är obligatoriskt: utan det skulle OpenCode falla tillbaka på en gratismodell
vars utbyten kan användas för träning, och det valet görs inte
åt dig.

Isolering vid varje anrop:

- en inline-konfiguration, som har företräde framför din, definierar en agent `aipmt`
  där alla verktyg nekas (`permission: { "*": "deny" }`), sessionsdelning
  inaktiverad, `--pure`, aldrig `--auto`;
- temporär och tom arbetskatalog, `OPENCODE_DISABLE_PROJECT_CONFIG` och
  `OPENCODE_DISABLE_CLAUDE_CODE` skapade – utan dem injicerar OpenCode
  aktuell katalogs `AGENTS.md` och `~/.claude/CLAUDE.md` i prompten. Global
  `~/.config/opencode/AGENTS.md` förblir injicerad; OpenCode tillåter inte
  att den utesluts;
- utdatakontrakt: returkod 0, ingen `error`-händelse, inget
  verktygsanrop, sista steget i `stop`, icke-tom text och agenten `aipmt`
  faktiskt inläst – en okänd `--agent` får inte OpenCode att misslyckas, utan
  den faller tyst tillbaka på kodningsagenten;
- ingen nyckel för `aipmt` skickas, förutom `OPENCODE_API_KEY`, nyckeln
  för OpenCode självt. Leverantörer konfigureras i OpenCode, inte i
  `.env` för `aipmt`.

Värt att veta:

- Gratismodellerna i Zen är föränderliga, med odokumenterade begränsningar, och
  deras utbyten kan användas för träning: för offentlig dokumentation,
  inte för privat innehåll.
- En lokal modell måste erbjuda minst 16k tokens i kontext, då segmenten
  omfattar upp till 16 000 tecken. Ollama konfigurerar ofta 4 096: gå
  via en `Modelfile` med `PARAMETER num_ctx 32768`.
- `--eco` har ingen effekt; `--reasoning_effort` skickas oförändrad som
  `--variant` för OpenCode.
- OpenCode loggar varje session i `~/.local/share/opencode/`.
- Variabler: `OPENCODE_BIN` (annars `PATH`, därefter `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (sekunder per segment, standard 600). `OPENCODE_CONFIG`
  skickas vidare som den är till OpenCode.

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

`reasoningEffort: "none"` stänger av det resonerande som Ollama aktiverar som standard på dessa
modeller, och som en Modelfile inte kan inaktivera. Uppmätt på en mening med
sex ord: 919 resonemangstokens och 68 sekunder utan flaggan, 9 tokens med den.

### Till över 400 modeller: `--use_openrouter`

OpenRouter är en router som faktureras efter användning, mot en gemensam kreditpott, framför
modeller som driftas av tredje part – inklusive de öppna kinesiska modellerna som ingen
annan leverantör tillhandahåller här.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` är obligatoriskt. En förhandskontroll (preflight), som körs före all fakturering, hanterar
två särdrag med dirigeringen:

- **Samma modell tillhandahålls av dussintals värdar med olika
  gränser** – på `z-ai/glm-5.3-flash`, 23 värdar varav en med tak på
  2 048 utdatatokens. Förhandskontrollen läser `/api/v1/models/{modèle}/endpoints`,
  sållar bort värdar under 8 000 utdatatokens eller med degraderad status, och
  låser övriga med `allow_fallbacks: false`.
- **Resonemang faktureras till utdatatakt** – 107 tokens jämfört med 2 på
  ett "OK"-svar från `z-ai/glm-5.2`. Det är inaktiverat som standard; modeller
  som kräver det tilldelas den lägsta ansträngningsnivå de accepterar, eftersom
  katalogens standardinställning kan fylla utdatagränsen innan översättningen är klar.
  `--reasoning_effort` har fortfarande företräde.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Kontextfönstret hämtas från katalogen. En modell under 16 400 tokens
  avvisas före anrop: minst 8 400 för prompten och segmentet, samt 8 000 för utdata.
- En slug som saknas i katalogen, en katalog som inte kan nås eller avsaknad
  av en värd som klarar gränsen avbryter kommandot.
- `finish_reason=length` med tom utdata beror på att budgeten förbrukats av
  resonerandet, inte på trunkering: meddelandet skiljer på detta.
- `--eco` har ingen effekt.
- Variabler: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (standard `https://openrouter.ai/api/v1`, `https://`
  krävs), `OPENROUTER_TIMEOUT` (standard 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (standard 30).

### Översättningsnot

`--add_translation_note` lägger till en not, i `bottom` (standard), `top` (efter
front matter) eller `both` (`--note_position`), i formatet `legacy` (stycke i
fetstil, standard) eller `marker` (`--note_format`). Formatet `marker` är en
osynlig Markdown-referensdefinition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
följt av ett citatblock i fetstil: läsbart på GitHub, användbart vid byggning via ett
remark-plugin.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detaljerade mätningar

Alla mätningar är översättningar som faktiskt har utförts med `aipmt`, till
fjorton språk: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Skrivna** räknar de filer som kontrollerna släppte igenom; **Utan
avvikelse** de där `scripts/compare_structure.py` inte upptäcker något – samma antal
avsnitt, underrubriker, länkar, unika webbadresser, kodblock,
inline-kod, tabellrader, citatblock och ord i fetstil.

"Utan avvikelse" betyder "inget upptäckt", inte "identisk": jämförelseverktyget
räknar element utan att läsa deras innehåll. Det varnar varken för en borttagen rubrik på
nivå 4, en ersatt text i en inline-kod, en förväxlad flagga eller en intern länk som renderats med en parentes för mycket,
`[texte]((#ancre))`, som inte längre leder någonstans – och det bedömer inte
språket.

### Tät bevakningsartikel, läge `--news`

En utgåva av [AI-bevakningen från jls42.org](https://jls42.org/fr/news):
589 rader, 140 länkar, 21 avsnitt, 3 skyddade engelska citat. Testomgång
den 4 och 5 september 2026.

| Modell                                          | Åtkomst            | Skrivna | Utan avvikelse | Median/språk |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google-API         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google-abonnemang  | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google-abonnemang  | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT-abonnemang | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | Claude-abonnemang  | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | Anthropic-API      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | Claude-abonnemang  | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | lokal              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral-API        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok-abonnemang    | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | Claude-abonnemang  | 0/14    | ❌ 0/14      | —              |

Grok mättes på nytt den 9 september på en annan utgåva av samma bevakning
(356 rader): 9 språk skrivna av 14, 8 utan avvikelse. Det är denna siffra som
visas i huvudtabellen. Tre avbrutna testomgångar är inte
medräknade: `qwen3.5-27b` (9 språk) och `kimi-k2.6` (4) på grund av brist på krediter,
`z-ai/glm-5.3-flash` vars två misslyckanden berodde på en resonemangsinställning
som leverantören sedan dess har åtgärdat. OpenRouter-raderna mättes med
routerns standardinställningar, före `--use_openrouter`; `z-ai/glm-5.2`,
omtestad med den levererade providern, ger samma 14/14. Siffrorna
omberäknades den 10 september med det nuvarande jämförelseverktyget: `qwen3.8-flash` och
`qwen3.7-flash` får vardera ett språk till jämfört med den första
publiceringen, övriga är oförändrade.

`--use_antigravity`-raderna mättes den 26 september på samma
artikel, fyra översättningar parallellt: `gemini-3.7-flash-medium` på förmiddagen,
`gemini-3.8-flash-medium` på eftermiddagen. På engelska tog var och en själv bort
de tre raderna med fransk översättning under citaten, utan att hitta på någon
flagga, och de engelska citaten är intakta: reservrensningen behövde inte
göra någonting. I `--eco` (`gemini-3.7-flash-low`), på endast fyra
språk (en, ja, ar, hi): 4 skrivna av 4, samtliga utan avvikelse, 1 min 52 s i
median. Motprov samma dag på en nyare utgåva av bevakningen,
den från den 25 september (438 rader, 2 engelska citat), översatt utanför
bloggen med `gemini-3.7-flash-medium`: 14 skrivna av 14, alla utan avvikelse, 87 till
128 s per språk.

`--use_claude_code`-raderna mättes den 26 september på samma
artikel, fyra översättningar parallellt, med ansträngningsnivå `low`. Med `sonnet` är de
engelska citaten intakta på samtliga fjorton språk och på engelska tog
modellen själv bort raderna med fransk översättning, utan att hitta på någon
flagga. `opus` skrev inget språk: på samtliga stoppade dess skyddsbarriärer
svaret vid det sista segmentet på grund av en notis om 279 molekyler
genererade för ett bindningsställe. Skickad separat avvisas denna notis under
kategorin "bio"; `sonnet` översatte den överallt. `haiku` skriver
alla fjorton språk; på tre (en, pl, ro) ändras en avsnittsrubrik från
nivå 2 till nivå 1. Den resonerar utan att man kan förhindra det – 61 % av
dess utdatatokens –, vilket ger mer än dubbla tiden jämfört med `sonnet`.

### Detta projekts README, standard-Markdown

Låst revision den 9 september 2026: 785 rader, 285 inline-koder, 40
blockavslutningar, 89 tabellrader. Fyra parallella översättningar.

| Modell                                          | Skrivna | Utan avvikelse | Median/språk   | Vad som skiljer sig                                                      |
| ----------------------------------------------- | ------- | -------------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14       | 1 min 43 s     | inget                                                                    |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14       | 1 min 48 s     | inget                                                                    |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14       | 4 min 02 s     | inget för jämförelseverktyget; dubblerade interna länkar (en)            |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14       | 36 s           | ett ord i fetstil (ja)                                                   |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14       | 1 min 22 s     | ett ord i fetstil (ko)                                                   |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14       | 2 min 20 s     | en tabellrad sammanfogad med föregående (ar)                             |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14       | 2 min 56 s     | en länk (sv), ett ord i fetstil (zh)                                     |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14       | 6 min 46 s     | ett ord i fetstil (ar, ja)                                               |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14       | 2 min 34 s     | ett ord i fetstil (hi, ja, ko)                                           |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14       | 2 min 17 s     | 40 inline-koder tillagda på arabiska; fetstil (hi, ja, ko)               |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14        | 2 min 44 s     | ett förlorat avsnitt (ar, hi, ko); tillagda kodblock (ja, ko, ro, zh)   |

Två avbrutna testomgångar är inte noterade: Grok, CLI-sessionen löpte ut
efter tolv språk (elva utan avvikelse), och `qwen3.8-flash`, HTTP 429 från sin
värd efter två. `opencode/mimo-v2.5-free` och `ollama/gpt-oss-20b-32k`
mättes inte om på denna revision; på den från 4 och 5 september,
som var 277 rader kortare, skrev de vardera 9 översättningar av 14, varav 7
respektive 1 utan avvikelse.

Raderna `--use_antigravity` och `--use_claude_code` mättes inte på
den låsta revisionen, utan den 26 september på den som publicerades med 1.14.0: 600
rader, 257 inline-koder, 30 blockavslutningar, 85 tabellrader. Då den är
185 rader kortare kan den inte jämföras rakt av med de andra raderna;
dessa rader kan däremot jämföras med varandra. När det gäller interna länkar, som
jämförelseverktyget inte kontrollerar, behöll `gemini-3.8-flash-medium` dem intakta på
alla fjorton språk, medan `gemini-3.7-flash-medium` bröt dem på italienska;
`sonnet` och `opus` behöll dem intakta överallt, och `haiku` dubblerade dem på
engelska.

### Fyra README från välkända projekt

FastAPI, Ollama, tldr-pages och Vue.js, hämtade i befintligt skick från GitHub –
enklare dokument än de två föregående. Testomgången riktade sig till modeller
med svårigheter; Gemini fungerar där som jämförelsepunkt.

| Modell                    | Omfattning                 | Skrivna | Utan avvikelse |
| ------------------------- | -------------------------- | ------- | -------------- |
| `gemini-3.7-flash`        | 4 projekt × 14 språk       | 56/56   | ✅ **55/56**   |
| `opencode/mimo-v2.5-free` | 4 projekt × 14 språk       | 55/56   | ❌ 47/56       |
| `grok-4.6` (prenumeration)   | 4 projekt × ar, hi, ja, zh | 16/16   | ❌ 14/16       |
| `ollama/gpt-oss-20b-32k`  | 4 projekt × ar, hi, ja, zh | 15/16   | ❌ 9/16        |

### Vad dessa mätningar inte är

- **Ingen fullständig rankning**: Bara OpenRouter erbjuder över fyra hundra
  modeller, varav ett femtontal har mätts.
- **Ungefärliga tidsangivelser**: tre till sex parallella översättningar beroende
  på testomgång, och en leverantörs genomströmning varierar under dagen.
- **Tidsbundna observationer**: modellerna förändras under samma namn, och era
  dokument är inte våra.

För att upprepa mätningen på dina dokument, på en låst kopia av filen:

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

Båda raderna krävs: utan `pip install -e .` svarar `python -m aipmt`
med `No module named aipmt`.

Kvalitetsverktyg, valfritt men rekommenderat:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Förrådets 28 översättningar (README och CHANGELOG, fjorton språk)
återskapas med `./regen_translations.sh --force` — Codex och `gpt-5.6-sol` på
ChatGPT-prenumerationen som standard, fyra parallellt. `REGEN_PROVIDER` och
`REGEN_MODEL` ändrar sökvägen: `antigravity` stannar kvar på en prenumeration, Googles,
och körs utan dispens; ett fakturerat API (`openai`, `gemini`,
`grok`, `openrouter`) nekas utan `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` sätter ett maxtak för varje jobb (600 s, 1 800 s för Codex och
Antigravity). Detaljer om verktygen finns i `CLAUDE.md`.

## Projekt som använder detta skript

- **[jls42.org](https://jls42.org)** — personlig blogg publicerad på 15 språk. Dess
  [dagliga AI-bevakning](https://jls42.org/fr/news) översätts dagligen
  med detta verktyg och fungerar som referensdokument för mätningarna ovan.

## Författare

Julien LE SAUX
E-post: contact@jls42.org

## Licens

GNU GENERAL PUBLIC LICENSE Version 3. Se [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Friskrivning

Detta program distribueras **utan någon garanti**, enligt villkoren i
avsnitt 15 och 16 i GPL v3: tillhandahålls ”i befintligt skick”, utan garanti för säljbarhet
eller lämplighet för ett visst ändamål, och dess författare kan inte
hållas ansvarig för skador som uppstår till följd av dess användning. Licenstexten
har företräde framför denna sammanfattning.

- **Läs igenom före publicering.** Skydden omfattar kodblock,
  inline-kod, URL:er, ankare och citat i `--news`-läget — inte
  rubriker, tabeller, front matter eller innebörden i dina meningar.
- **Dina dokument skickas till den valda leverantören**, under dennes användarvillkor
  och datapolicy. Vissa gratismodeller kan återanvända dina interaktioner för
  träning, och Antigravitys villkor tillåter Google att återanvända dem och låta
  människor granska dem, även med betalprenumeration; en lokal modell är den enda
  vägen som inte låter någon data lämna din maskin.
- **API-anrop debiteras dig.** Detta program sätter inget tak för
  utgifterna: ett långt dokument, en återupptagning efter fel eller en modell som resonerar
  mycket kostar mer.
- **De publicerade mätningarna är tidsbundna observationer**, inte garantier.

Namn på produkter och företag som nämns tillhör sina respektive
ägare. Detta projekt är inte anslutet till något av dem.

**Artikel översatt från fr till sv med gemini-3.8-flash-medium.**

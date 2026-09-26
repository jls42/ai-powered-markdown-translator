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
struktur: kodblock, inline-kod, URL:er, ankare, tabeller och front
matter. Tio sätt att anropa en modell – fem API:er, tre abonnemang utan
användningsbaserad debitering, två routrar – och en publicerad mätning av vad varje
modell faktiskt bevarar.

## I korthet

- **Tio provider-vägar**: API:er för OpenAI, Mistral, Claude, Gemini och Grok;
  ChatGPT- (Codex), Grok- och Google-abonnemang (Antigravity) utan användningsbaserad
  debitering; OpenCode-routrar (öppen källkod, gratis eller lokalt) och OpenRouter
  (fler än 400 modeller).
- **Inget förvanskat på grund av en förlorad token**: kodblock, inline-kod,
  URL:er, ankare och citat ersätts med tokens före anropet och
  verifieras vid retur. Om en saknas skrivs inte filen.
- **Långa dokument**: segmentering baserad på modellens kontextfönster.
- **`--news`-läge**: skyddade engelska citat och flaggor hanterade per
  språk, för bevakningsartiklar.
- **`--eco`-läge**: snabba och billigare modeller.
- **Översättningsnotis** som tillval, överst, underst eller på båda ställena.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 eller senare. För att installera från arkivet, se
[Bidra](#bidra).

## Konfiguration

Nycklarna läses från tre platser, från högst till lägst prioritet; varje plats
fyller endast i det som föregående lämnar tomt.

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
som körs.** Den tillhandahåller nycklar, aldrig en destination eller en binär: alla
variabler som slutar på `_BASE_URL`, `_API_BASE`, `_ENDPOINT` eller `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, proxyservrar (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), certifikatarkiv (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) samt `XDG_CONFIG_HOME` /
`APPDATA` ignoreras där, med en varning. Ett klonat arkiv får inte
kunna kapa din nyckel eller få dig att köra dess eget program vid den
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
avsnittet för respektive provider.

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
alltid `.md` – `article.mdx` ger `article-en.md` – utom med
`--keep_filename`, som bevarar det ursprungliga namnet. En översättning som redan finns
hoppas över utan `--force`.

Slutkoder: `0` om allt lyckades eller hoppades över, `1` om en fil
misslyckades (lista på standard error), `2` om konfigurationen är felaktig.
En misslyckad fil skrivs aldrig, även om själva skrivningen misslyckas:
innehållet skrivs vid sidan om och döps sedan om. Det räcker att köra igen.

## Vilken modell ska man välja

Mätt på två verkliga dokument, översatta till samma fjorton språk av
varje modell. **Siffran anger antalet språk, av fjorton, där översättningen
skrivs och ingenting skiljer sig från källan.**

| Modell               | Hur man kommer åt den             | Tät bevakningsartikel   | Denna README | Vad som skiljer sig, och på hur många språk                                                                                           |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.8 Flash** | Google-abonnemang (Antigravity)   | ✅ 14/14                | ✅ 14/14     | ingenting, på något av dokumenten                                                                                                     |
| **Gemini 3.7 Flash** | Google API-nyckel                 | ✅ 14/14                | ⚠️ 13/14     | 1 språk av 14: ett extra fetstilt ord (ja)                                                                                            |
| **Gemini 3.7 Flash** | Google-abonnemang (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 1 språk av 14: ett fetstilt ord mindre (ko)                                                                                           |
| **GPT-5.6 Sol**      | ChatGPT-abonnemang eller OpenAI-nyckel | ✅ 14/14           | ⚠️ 12/14     | 2 språk av 14: ett fetstilt ord mindre (ar, ja)                                                                                       |
| **GLM-5.2**          | OpenRouter-nyckel                 | ✅ 14/14                | ⚠️ 11/14     | 3 språk av 14: ett fetstilt ord mindre (hi, ja, ko)                                                                                   |
| Claude Sonnet 5      | Anthropic API-nyckel              | ⚠️ 11/14                | ⚠️ 12/14     | 3 språk i artikeln: ett kodblock dök upp (es, de, hi); 2 i denna README: en länk utan sin formatering (sv), ett fetstilt ord (zh)    |
| Qwen 3.7 Flash       | OpenRouter-nyckel                 | ❌ 8/14                 | ⚠️ 10/14     | 1 språk avvisat i artikeln, 5 andra avviker; i denna README ett fyrtiotal ord satta i `code` (ar)                            |
| Grok 4.6             | Grok-abonnemang                   | ❌ 8/14                 | ej betygsatt | 5 språk avvisade av 14 på grund av saknade inline-koder och URL:er; nederländska avviker helt                                        |
| GPT-OSS 20B          | lokal modell (Ollama)             | ❌ 7/14                 | ej ommätt    | 4 språk avvisade av 14: modellen lämnade stycken på franska, spärren stoppade dem                                                      |
| MiMo v2.5 (gratis)   | OpenCode Zen, utan konto          | ❌ 11/14                | ej ommätt    | 1 språk avvisat; ett avsnitt förlorat på polska                                                                                       |
| Mistral Large        | Mistral API-nyckel                | ❌ 5/14                 | ❌ 1/14      | **ett helt avsnitt försvinner**: 1 språk i artikeln (hi), 3 i denna README (ar, hi, ko) – och 3 språk avvisade i artikeln             |
| DeepSeek V4 Flash    | OpenRouter-nyckel                 | ❌ 3/14                 | ej ommätt    | 10 språk avvisade av 14; 37 minuter per språk                                                                                         |

|     | Vad symbolen betyder                                                                                                                                                                                  |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alla fjorton språk översatta, och ingenting skiljer sig från källan                                                                                                                                   |
| ⚠️  | alla fjorton språk översatta; det som skiljer sig är **formatering** – ett fetstilt ord, en `code`, en länk som förlorar sina hakparenteser. Ingen text, inga URL:er, inga kodblock och inga avsnitt saknas |
| ❌  | minst ett språk kunde inte översättas – filen avvisas, skrivs inte – **eller** innehåll saknas i en skriven fil                                                                                      |

Vad man bör ta med sig:

- **En avvisad översättning är inte en skadad översättning.** När en token
  saknas vid retur skrivs inte filen och språket räknas som
  avvisat. Det är vad som händer Grok i artikeln: fyra inline-koder och
  tre URL:er förlorades redan i det första segmentet i de fem icke-latinska skrifterna.
- **Detta skyddsnät täcker inte rubriker, tabeller, front matter eller
  brödtext.** En modell som tar bort ett avsnitt returnerar en fil som verktyget skriver
  utan att tveka – så är fallet med Mistral. Dessa element kan inte
  ersättas med tokens, och de nuvarande kontrollerna övervakar dem inte;
  `scripts/compare_structure.py` upptäcker ett förlorat avsnitt, men först i efterhand.
- **Grok har inget betyg för denna README**: dess CLI-session löpte ut efter tolv
  språk, varav elva utan avvikelser. En avbruten kampanj betygsätts inte.
- **Dokumentets densitet spelar större roll än språket.** Grok klarar vanliga
  README-filer och fallerar på en länkspäckad artikel, även på
  nederländska.

Datum och dokument: kolumnen "Denna README" mättes den 9 september 2026
på en fryst revision av denna fil (785 rader, 285 inline-koder, 89 tabellrader),
som har justerats sedan dess – med undantag för de två Antigravity-raderna, som mättes den
26 september på den revision som publicerades med 1.14.0, vilken var kortare (600 rader,
257 inline-koder, 85 tabellrader). Kolumnen "Tät bevakningsartikel"
kommer från kampanjen den 4 och 5 september på en artikel med 589 rader,
förutom Grok-raden, som mättes om den 9 september på en annan utgåva av samma
bevakning, samt de två Antigravity-raderna, som mättes den 26 september på samma
artikel.
Fullständiga tabeller, tidsåtgång och protokoll finns i
[Detaljerade mätningar](#detaljerade-mätningar).

## Alla alternativ

| Alternativ               | Beskrivning                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Enskild Markdown-fil att översätta (alternativ till `--source_dir`)                                             |
| `--source_dir`           | Källkatalog som innehåller Markdown-filer (standard: `content/posts`)                                           |
| `--target_dir`           | Utdatakatalog för översatta filer (standard: `traductions_en`)                                                  |
| `--source_lang`          | Källspråk (standard: `fr`)                                                                          |
| `--target_lang`          | Målspråk (standard: `en`)                                                                           |
| `--model`                | Specifik modell att använda                                                                                  |
| `--eco`                  | Använd ekonomimodeller                                                                                        |
| `--use_mistral`          | Använd Mistral AI API                                                                                         |
| `--use_claude`           | Använd Claude API                                                                                             |
| `--use_gemini`           | Använd Gemini API                                                                                             |
| `--use_grok`             | Använd xAI API (Grok) – kräver `XAI_API_KEY`                                                                 |
| `--use_codex`            | Använd Codex CLI på ChatGPT-abonnemangets kvot                                                                |
| `--use_grok_cli`         | Använd Grok CLI på Grok-abonnemangets kvot                                                                    |
| `--use_antigravity`      | Använd Antigravity CLI (`agy`) på kvoten för Google AI Pro- eller Ultra-abonnemang                    |
| `--use_opencode`         | Använd OpenCode (öppen källkod) mot den leverantör som konfigurerats i OpenCode; kräver `--model provider/modèle`       |
| `--use_openrouter`       | Använd OpenRouter – kräver `OPENROUTER_API_KEY` och `--model fournisseur/modèle`                                                  |
| `--force`                | Tvinga omöversättning                                                                                         |
| `--keep_filename`        | Bevara ursprungligt filnamn                                                                                   |
| `--news`                 | Nyhetsläge: skyddar EN-citat, hanterar flaggor per språk                                                      |
| `--add_translation_note` | Lägg till en översättningsnotis                                                                               |
| `--note_position`        | Notisens placering: `top`, `bottom` (standard) eller `both`                            |
| `--note_format`          | Notisens format: `legacy` (standard, fetstilt stycke) eller `marker`                              |
| `--include_model`        | Inkludera modellnamnet i utdatafilen                                                                          |
| `--reasoning_effort`     | Resonemangsinsats för GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`|

De nio `--use_*`-flaggorna är ömsesidigt uteslutande: att kombinera två
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

`--eco` växlar till den ekonomiska nivån för varje leverantör.

| Leverantör  | Kvalitet (standard)                                   | Ekonomisk (`--eco`)       |
| ----------- | ----------------------------------------------------- | --------------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`                   |
| Claude      | `claude-sonnet-5`                                       | `claude-haiku-4-5`                   |
| Mistral     | `mistral-large-latest`                                       | `mistral-small-latest`                   |
| Gemini      | `gemini-3.7-flash`                                       | `gemini-3.1-flash-lite`                   |
| Codex       | `gpt-5.6-sol` (även `terra` och `luna` via `--model`) | `gpt-5.6-luna`                   |
| Grok API    | `grok-4.6`                                       | `grok-4.3`                   |
| Grok CLI    | `grok-4.6`                                       | `grok-4.5`                   |
| Antigravity | `gemini-3.8-flash-medium`                                       | `gemini-3.7-flash-low`                   |
| OpenCode    | `--model provider/modèle` obligatorisk                          | samma sak — `--eco` utan effekt |
| OpenRouter  | `--model fournisseur/modèle` obligatorisk                          | samma sak — `--eco` utan effekt |

### Via ChatGPT-prenumerationen: `--use_codex`

Styr det officiella Codex-CLI:et: översättningen dras från kvoten för
ChatGPT-prenumerationen, utan API-nyckel eller användningsbaserad debitering.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Den binära filen söks i `CODEX_BIN`, sedan `PATH`, därefter paketet
  `openai-codex-cli-bin`. `~/.codex/auth.json` läses aldrig.
- `OPENAI_API_KEY` och `CODEX_API_KEY` tas bort från underprocessens miljö:
  en befintlig nyckel växlar aldrig över till API:et.
- Varje segment kostar minst ett "meddelande" i 5-timmarsfönstret — två
  om valideringen misslyckas och ett nytt försök görs. OpenAI uppskattar
  250–2 000 meddelanden/5 timmar för `gpt-5.6-luna` (`--eco`) och
  10–100 för `gpt-5.6-sol` på en Plus-plan.
- `--model gpt-5.6-terra` och `--model gpt-5.6-luna` går också via
  prenumerationen. En modell som kontot inte har tillgång till returnerar 400 "model is
  not supported when using Codex with a ChatGPT account".
- Långsammare än ett API, och skillnaden växer med dokumentets storlek: för denna README,
  median på 6 min 46 s per språk med `gpt-5.6-sol`, jämfört med 36 s för
  `gemini-3.7-flash`.
- Avvisas i CI (`CI` eller `GITHUB_ACTIONS` definierad): prenumerationen autentiseras
  via en personlig sessionsfil, som inte hör hemma på en delad
  runner.
- Variabler: `CODEX_BIN`, `CODEX_TIMEOUT` (sekunder per segment, standard 600).

### Via Grok-prenumerationen: `--use_grok_cli`

Samma princip med det officiella CLI:et Grok Build, via SuperGrok- eller
X Premium+-prenumerationen.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Svagare isolering än Codex.** Groks OS-sandlåda kan inte användas
  på många moderna Linux-system (AppArmor, sockets för container-runtime),
  och en profil som inte kan tillämpas startar tyst utan isolering.
  Skriptet begär därför ingen profil som standard, meddelar detta och
  förlitar sig på CLI:ets regler i `--deny`, inklusive dess catch-all `*` — det enda
  lager som vägrar att starta i stället för att ta bort skyddet i det
  tysta. `GROK_TRANSLATE_SANDBOX=read-only` kräver OS-sandlådan, och starten
  misslyckas om maskinen inte kan tillgodose detta.
- Kvoten är veckovis, delad med Chat, Imagine och Voice, och inget
  kommando låter dig läsa av den: en batch kan förbruka konversationskvoten
  utan förvarning.
- Variabler: `GROK_BIN`, `GROK_HOME` (CLI-katalog, standard `~/.grok`),
  `GROK_TIMEOUT` (standard 900), `GROK_TRANSLATE_SANDBOX`.

### Via Google-prenumerationen: `--use_antigravity`

Samma princip med `agy`, det officiella CLI:et för Antigravity: för den som betalar för Google
AI Pro eller Ultra dras översättningen från prenumerationskvoten i stället
för att debiteras per token. Detta är den enda vägen till den kvoten: Gemini CLI
stöder inte längre dessa konton sedan den 18 juni 2026
([tillkännagivande](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
och SDK:et för Antigravity accepterar endast en API-nyckel eller ett Google Cloud-projekt.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Inga betalvägar lämnas öppna.** agy tar endast emot en sluten lista av variabler
  från din miljö — `PATH`, språk och tidszon,
  terminal, identitet, proxys och certifikat, sessionsbuss — och inga nycklar:
  flera av dess variabler kan omdirigera ett anrop utan att visa något (uppmätt:
  en skickar dokumentet till en tredjeparts-gateway, en annan till ett debiterat
  Google Cloud-projekt), och en blockeringslista missade alltid några vid varje granskning.
  Före varje segment måste `agy -p /config`, som inte förbrukar någon kvot, visa
  att betalda AI-krediter är inaktiverade, utan API-nyckel eller Google Cloud-projekt — en
  saknad inställning betraktas som ett avslag —, annars översätts ingenting; loggen för varje
  anrop måste därefter intyga prenumerationen (`authMethod=consumer`), annars
  avvisas svaret.
- **Isolering.** Varje anrop körs i en privat, temporär arbetskatalog,
  med en översättningsagent utan verktyg: dina inställningar, regler,
  insticksprogram, MCP-servrar och hooks i agy läses inte in där, ingenting läggs till i din
  historik, och inloggningen stannar i nyckelringen, som aipmt aldrig läser.
  Om en agent inte hittas faller agy tyst tillbaka på sin kodningsagent
  och dess verktyg: en hel rad i loggen måste bekräfta rätt agent — ett
  dokument som citerar detta meddelande ersätter den inte —, annars avvisas det.
- **Plattformar**: Linux, i en session som har en nyckelring (D-Bus-sessionsbuss,
  Secret Service); macOS stöds, men har inte mätts. Avvisas
  under Windows, där agy inte läser variablerna som isolerar varje anrop, och
  under Linux utan sessionsbuss — SSH-session, container, server: agy
  sparar då sin token i en fil i `~/.gemini`, som döljs av isoleringen.
  Avvisandet sker före all start, med dess orsak, i stället för en minuts
  väntan på en inloggningskod.
- **Modeller**: de från `agy models`. Gemini-modellerna har ansträngningsnivån i namnet
  (`gemini-3.8-flash-medium`…): ett namn utan suffix avvisas före anropet,
  och `--reasoning_effort` har ingen effekt. Som standard `gemini-3.8-flash-medium`,
  och `gemini-3.7-flash-low` i `--eco`; körningarna som fastställde dem
  beskrivs i [Detaljerade mätningar](#detaljerade-mätningar). Claude och GPT-OSS
  har en egen kvot, som är mycket mindre: cirka 1 % av 5-timmarsfönstret
  per uppmätt anrop, jämfört med 0,05 % för Flash.
- **Kvot**: per grupp, ett 5-timmarsfönster och ett veckofönster,
  proportionellt mot tokenkostnaden. Uppmätt på författarens konto: cirka
  16 poäng av 5-timmarsfönstret per miljon källtecken i
  `gemini-3.8-flash-medium`, 14 i `gemini-3.7-flash-medium` och 7 till 8 vid
  låg ansträngning — en README på 40 000 tecken kostar alltså drygt en
  halv poäng. Veckogränsen beror i sin tur på nivån. Förnyade försök följer
  vad agy rapporterar som återförsökbart; i annat fall görs aldrig nya försök
  om ett fönster är förbrukat: det leder till att varje fil misslyckas fram till återställningen
  som visas av `/usage`.
- **Långsammare än API:et**: för den kompakta mätartikeln, median på 3 min 59 s per
  språk i `gemini-3.8-flash-medium` och 3 min 14 s i
  `gemini-3.7-flash-medium`, jämfört med 1 min 18 s för Gemini 3.7 Flash via API:et.
- **Avbrott**: Ctrl-C, eller en stängd terminal, stoppar agy tillsammans med
  kommandot i stället för att låta det göra klart sin omgång på din kvot; detsamma
  gäller för Codex, Grok CLI och OpenCode. Under `nohup` fortsätter översättningen.
- Avvisas i CI (`CI` eller `GITHUB_ACTIONS` definierad): inloggningen finns i en
  personlig nyckelring. På en runner, använd `--use_gemini` med `GOOGLE_API_KEY`.
- Variabler: `AGY_BIN` (annars `PATH`, därefter `~/.local/bin/agy`),
  `AGY_TIMEOUT` (sekunder per segment, inklusive start, standard 900).

**Användarvillkor: det är ditt konto som berörs.**
[Villkoren för Antigravity](https://antigravity.google/terms) (avsnitt 6) och dess
[FAQ](https://antigravity.google/docs/faq/) förbjuder åtkomst till tjänsten
via programvara från tredje part med hjälp av Antigravity-inloggningen — Claude Code,
OpenClaw och OpenCode nämns där —, med risk för att kontot stängs av. aipmt
varken läser eller återanvänder tokenen: det startar den officiella binären i det
[headless-läge](https://antigravity.google/docs/cli/headless/) som Google
dokumenterar för skript och CI. En Google-medarbetare har bedömt det som "standard"
att starta `agy -p` från ett lokalt skript för eget arbete
([officiellt forum, 25 september 2026, icke-bindande svar](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
inget dokument avgör fallet för ett distribuerat verktyg som detta.

**Endast offentliga dokument.** Enligt avsnitt 5 i samma villkor kan
interaktionerna — prompter, svar, metadata — användas för att förbättra Googles
produkter och maskininlärning samt granskas av
människor, även för betalprenumerationer. Opt-out sker via inställningen
`enableTelemetry`, vars effekt inte är dokumenterad och som aipmt inte konfigurerar; dina inställningar
i agy följer inte med i dess isolering. Kör inget konfidentiellt genom detta.

### Till valfri leverantör: `--use_opencode`

[OpenCode](https://opencode.ai) är en AI-kodningsagent med öppen källkod (MIT) som
vidarebefordrar till leverantörer som konfigurerats i den: API-nyckel, prenumeration,
OpenCode Zen-gateway (gratismodeller, utan konto) eller lokal modell. Två
vägar har mätts från början till slut här: Zen och Ollama.

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

`--model` är obligatorisk: utan den skulle OpenCode falla tillbaka på en gratismodell
vars data kan användas för träning, och det valet görs inte
åt dig.

Isolering vid varje anrop:

- en inline-konfiguration, som har företräde framför din egen, definierar en `aipmt`-agent
  där alla verktyg avvisas (`permission: { "*": "deny" }`), sessionsdelning
  inaktiverad, `--pure`, aldrig `--auto`;
- temporär och tom arbetskatalog, `OPENCODE_DISABLE_PROJECT_CONFIG` och
  `OPENCODE_DISABLE_CLAUDE_CODE` angivna — utan dessa injicerar OpenCode
  den aktuella katalogens `AGENTS.md` och `~/.claude/CLAUDE.md` i prompten.
  Den globala `~/.config/opencode/AGENTS.md` injiceras fortfarande, OpenCode tillåter inte
  att den utesluts;
- utdatakontrakt: returkod 0, inga `error`-händelser, inga
  verktygsanrop, sista steget i `stop`, icke-tom text, och agenten `aipmt`
  faktiskt inläst — en okänd `--agent` gör inte att OpenCode kraschar, utan det
  faller tyst tillbaka på kodningsagenten;
- inga nycklar från `aipmt` vidarebefordras, förutom `OPENCODE_API_KEY`, nyckeln
  för själva OpenCode. Leverantörer konfigureras i OpenCode, inte i
  `.env` för `aipmt`.

Att tänka på:

- Gratismodellerna i Zen förändras löpande, har odokumenterade begränsningar, och
  deras interaktioner kan användas för träning: lämpligt för offentlig
  dokumentation, inte för privat innehåll.
- En lokal modell måste erbjuda minst 16 k tokens kontextfönster, då segmenten
  omfattar upp till 16 000 tecken. Ollama konfigurerar ofta 4 096: använd
  en `Modelfile` med `PARAMETER num_ctx 32768`.
- `--eco` har ingen effekt; `--reasoning_effort` skickas vidare oförändrad som
  `--variant` till OpenCode.
- OpenCode loggar varje session i `~/.local/share/opencode/`.
- Variabler: `OPENCODE_BIN` (annars `PATH`, därefter `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (sekunder per segment, standard 600). `OPENCODE_CONFIG`
  vidarebefordras oförändrad till OpenCode.

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

`reasoningEffort: "none"` stänger av resonerandet som Ollama aktiverar som standard för dessa
modeller, och som en Modelfile inte kan stänga av. Uppmätt på en mening med
sex ord: 919 resonemangstokens och 68 sekunder utan alternativet, 9 tokens med.

### Till över 400 modeller: `--use_openrouter`

OpenRouter är en router med användningsbaserad debitering, mot ett gemensamt saldo, framför
modeller som hostas av tredje part — inklusive öppna kinesiska modeller som ingen
annan leverantör tillhandahåller här.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` är obligatorisk. En förhandskontroll, som körs före all debitering, hanterar
två specifika routingegenskaper:

- **Samma modell tillhandahålls av dussintals värdar med olika
  begränsningar** — för `z-ai/glm-5.3-flash`, 23 värdar varav en med tak på
  2 048 utdatatokens. Förhandskontrollen läser `/api/v1/models/{modèle}/endpoints`,
  utesluter värdar under 8 000 utdatatokens eller med degraderad status, och
  låser fast de övriga med `allow_fallbacks: false`.
- **Resonemang debiteras till utdatataxa** — 107 tokens mot 2 för
  ett "OK"-svar från `z-ai/glm-5.2`. Det är avstängt som standard; modeller
  som kräver det tilldelas den lägsta ansträngning de accepterar, eftersom katalogens standardvärde
  kan fylla utdatagränsen innan översättningen är klar.
  `--reasoning_effort` har fortfarande företräde.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Kontextfönstret hämtas från katalogen. En modell under 16 400 tokens
  avvisas före anrop: minst 8 400 för prompten och segmentet, 8 000 för utdata.
- En slug som saknas i katalogen, en onåbar katalog eller avsaknad av
  en värd som klarar taket avbryter kommandot.
- `finish_reason=length` med tom utdata beror på att budgeten förbrukats av
  resonerande, inte trunkering: meddelandet skiljer på detta.
- `--eco` har ingen effekt.
- Variabler: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (standard `https://openrouter.ai/api/v1`, `https://`
  krävs), `OPENROUTER_TIMEOUT` (standard 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (standard 30).

### Översättningsnotering

`--add_translation_note` lägger till en notering, vid `bottom` (standard), `top` (efter
front matter) eller `both` (`--note_position`), i formatet `legacy` (fetstilt stycke,
standard) eller `marker` (`--note_format`). Formatet `marker` är en
osynlig Markdown-referensdefinition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
följd av ett fetstilt citat: läsbart på GitHub, användbart vid byggprocessen för ett
remark-plugin.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detaljerade mätningar

Alla mätningar är faktiska översättningar utförda med `aipmt`, till
fjorton språk: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Skrivna** räknar de filer som säkerhetskontrollerna släppte igenom; **Utan
avvikelse** de där `scripts/compare_structure.py` inte hittar något — samma antal
avsnitt, underrubriker, länkar, unika webbadresser, kodblock,
inline-kod, tabellrader, citatblock och fetstilta ord.

"Utan avvikelse" betyder "inget upptäcktes", inte "identisk": jämförelseverktyget
räknar element utan att läsa deras innehåll. Det flaggar varken en raderad rubrik på
nivå 4, text i en inline-kod som bytts ut, en flagga
som förväxlats, eller en intern länk återgiven med en parentes för mycket,
`[texte]((#ancre))`, som inte längre leder någonstans — och det bedömer inte
språket.

### Tät omvärldsbevakningsartikel, läge `--news`

En utgåva av [AI-bevakningen på jls42.org](https://jls42.org/fr/news):
589 rader, 140 länkar, 21 avsnitt, 3 skyddade engelska citat. Testomgång
den 4 och 5 september 2026.

| Modell                                          | Åtkomst            | Skrivna | Utan avvikelse | Median/språk   |
| ----------------------------------------------- | ------------------ | ------- | -------------- | -------------- |
| `gemini-3.7-flash`                              | Google-API         | 14/14   | ✅ **14/14**   | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google-prenumeration | 14/14   | ✅ **14/14**   | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google-prenumeration | 14/14   | ✅ **14/14**   | 3 min 14 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT-prenumeration | 14/14   | ✅ **14/14**   | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14**   | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14**   | 26 min 23 s    |
| `claude-sonnet-5`                               | Anthropic-API      | 14/14   | ⚠️ 11/14       | 6 min 31 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14       | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14        | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | lokalt             | 10/14   | ❌ 7/14        | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral-API        | 11/14   | ❌ 5/14        | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14        | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok-prenumeration | 1/14    | ❌ 1/14        | 23 min 11 s    |

Grok mättes om den 9 september på en annan utgåva av samma bevakning
(356 rader): 9 skrivna språk av 14, 8 utan avvikelse. Det är denna siffra som
visas i huvudtabellen. Tre avbrutna testomgångar redovisas
inte: `qwen3.5-27b` (9 språk) och `kimi-k2.6` (4) på grund av brist på krediter,
`z-ai/glm-5.3-flash` vars två misslyckanden berodde på en resonemangsinställning
som leverantören sedan dess har korrigerat. OpenRouter-raderna mättes med
routerns standardinställningar, före `--use_openrouter`; `z-ai/glm-5.2`,
ommätt med den medföljande leverantören, ger samma 14/14. Siffrorna
räknades om den 10 september med det nuvarande jämförelseverktyget: `qwen3.8-flash` och
`qwen3.7-flash` får vardera ett språk till jämfört med den första
publiceringen, övriga är oförändrade.

`--use_antigravity`-raderna mättes den 26 september på samma
artikel, fyra parallella översättningar: `gemini-3.7-flash-medium` på morgonen,
`gemini-3.8-flash-medium` på eftermiddagen. På engelska tog var och en själv bort
de tre raderna med fransk översättning under citaten, utan att hitta på någon
flagga, och de engelska citaten förblev intakta: reservrensningen behövde
inte göra någonting. I `--eco` (`gemini-3.7-flash-low`), på endast fyra språk
(en, ja, ar, hi): 4 skrivna av 4, alla utan avvikelse, 1 min 52 s i
median. Kontrolltest samma dag på en nyare utgåva av bevakningen,
den från 25 september (438 rader, 2 engelska citat), översatt utanför
bloggen av `gemini-3.7-flash-medium`: 14 skrivna av 14, alla utan avvikelse, 87 till
128 s per språk.

### README för detta projekt, standard-Markdown

Låst revision den 9 september 2026: 785 rader, 285 infogade koder, 40
blockavslut, 89 tabellrader. Fyra parallella översättningar.

| Modell                                          | Skrivna | Utan avvikelse | Median/språk   | Vad som skiljer                                                          |
| ----------------------------------------------- | ------- | -------------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14       | 1 min 43 s     | inget                                                                    |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14       | 36 s           | ett ord i fetstil (ja)                                                   |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14       | 1 min 22 s     | ett ord i fetstil (ko)                                                   |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14       | 2 min 56 s     | en länk (sv), ett ord i fetstil (zh)                                     |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14       | 6 min 46 s     | ett ord i fetstil (ar, ja)                                               |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14       | 2 min 34 s     | ett ord i fetstil (hi, ja, ko)                                           |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14       | 2 min 17 s     | 40 infogade koder tillagda på arabiska; fetstil (hi, ja, ko)              |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14        | 2 min 44 s     | ett förlorat avsnitt (ar, hi, ko); kodblock tillagda (ja, ko, ro, zh)   |

Två avbrutna testomgångar redovisas inte: Grok, vars CLI-session löpte ut
efter tolv språk (elva utan avvikelse), och `qwen3.8-flash`, HTTP 429 från sin
värd efter två. `opencode/mimo-v2.5-free` och `ollama/gpt-oss-20b-32k`
mättes inte om på denna revision; på den från 4 och 5 september,
som var 277 rader kortare, skrev de vardera 9 översättningar av 14, varav 7
respektive 1 utan avvikelse.

`--use_antigravity`-raderna mättes inte på den låsta revisionen,
utan den 26 september på den som publicerades med 1.14.0: 600 rader, 257 infogade
koder, 30 blockavslut, 85 tabellrader. Eftersom den är 185
rader kortare kan den inte jämföras rakt av med de andra raderna; de två
Antigravity-raderna kan däremot jämföras med varandra. När det gäller interna länkar,
som jämförelseverktyget inte kontrollerar, behöll `gemini-3.8-flash-medium` dem
intakta på de fjorton språken, medan `gemini-3.7-flash-medium` bröt dem på
italienska.

### Fyra README från välkända projekt

FastAPI, Ollama, tldr-pages och Vue.js, tagna som de är från GitHub –
enklare dokument än de två föregående. Testomgången riktade sig till modeller
med svårigheter; Gemini fungerar där som jämförelsepunkt.

| Modell                    | Omfattning                 | Skrivna | Utan avvikelse |
| ------------------------- | -------------------------- | ------- | -------------- |
| `gemini-3.7-flash`        | 4 projekt × 14 språk       | 56/56   | ✅ **55/56**   |
| `opencode/mimo-v2.5-free` | 4 projekt × 14 språk       | 55/56   | ❌ 47/56       |
| `grok-4.6` (prenumeration) | 4 projekt × ar, hi, ja, zh | 16/16   | ❌ 14/16       |
| `ollama/gpt-oss-20b-32k`  | 4 projekt × ar, hi, ja, zh | 15/16   | ❌ 9/16        |

### Vad dessa mätningar inte är

- **Ingen fullständig rankning**: Bara OpenRouter erbjuder över fyrahundra
  modeller, och ett femtontal har mätts.
- **Ungefärliga tidsangivelser**: tre till sex parallella översättningar beroende
  på testomgång, och en leverantörs dataflöde varierar under dagen.
- **Daterade observationer**: modellerna ändras under samma namn, och era
  dokument är inte våra.

För att göra om mätningen på era dokument, på en låst kopia av filen:

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

Båda raderna är nödvändiga: utan `pip install -e .` svarar `python -m aipmt`
`No module named aipmt`.

Kvalitetsverktyg, valfritt men rekommenderat:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

De 28 översättningarna i förvaret (README och CHANGELOG, fjorton språk)
återskapas med `./regen_translations.sh --force` – Codex och `gpt-5.6-sol` via
ChatGPT-prenumerationen som standard, fyra parallellt. `REGEN_PROVIDER` och
`REGEN_MODEL` ändrar sökvägen: `antigravity` stannar kvar på en prenumeration, Googles,
och går igenom utan undantag; ett fakturerat API (`openai`, `gemini`,
`grok`, `openrouter`) nekas utan `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` sätter ett maxtak för varje jobb (600 s, 1 800 s för Codex och
Antigravity). Detaljer om verktygen finns i `CLAUDE.md`.

## Projekt som använder detta skript

- **[jls42.org](https://jls42.org)** – personlig blogg publicerad på 15 språk. Dess
  [dagliga AI-bevakning](https://jls42.org/fr/news) översätts varje dag
  av detta verktyg och fungerar som referensdokument för mätningarna ovan.

## Författare

Julien LE SAUX
E-post: contact@jls42.org

## Licens

GNU GENERAL PUBLIC LICENSE Version 3. Se [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Varning

Detta program distribueras **utan någon garanti**, i enlighet med villkoren i
avsnitt 15 och 16 i GPL v3: tillhandahålls i ”befintligt skick”, utan garanti för
säljbarhet eller lämplighet för ett visst syfte, och dess författare kan inte
hållas ansvarig för skador som uppstår till följd av dess användning. Licenstexten
har företräde framför denna sammanfattning.

- **Läs igenom innan publicering.** Skydden omfattar kodblock, infogad
  kod, webbadresser, ankare och citat i läget `--news` – inte
  rubriker, tabeller, front matter eller innebörden i dina meningar.
- **Dina dokument skickas till den valda leverantören**, under dennes
  användarvillkor och datapolicy. Vissa gratismodeller kan
  återanvända dina konversationer för träning, och villkoren för Antigravity
  tillåter Google att återanvända dem och låta människor granska dem,
  även med betalprenumeration; en lokal modell är den enda vägen som inte
  låter någon data lämna din dator.
- **API-anrop debiteras dig.** Detta program sätter inget tak för
  kostnaden: ett långt dokument, ett nytt försök efter misslyckande eller en modell som resonerar
  mycket kostar mer.
- **De publicerade mätningarna är daterade observationer**, inte garantier.

Produkt- och företagsnamn som nämns tillhör sina respektive
ägare. Detta projekt är inte anslutet till något av dem.

**Artikel översatt från fr till sv med gemini-3.8-flash-medium.**

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

Översätter Markdown-filer från ett språk till ett annat med bevarad
struktur: kodblock, inline-kod, URL:er, ankare, tabeller och front
matter. Tio sätt att anropa en modell — fem API:er, tre abonnemang utan
användningsbaserad fakturering, två routrar — och en publicerad mätning av vad varje
modell faktiskt bevarar.

## I korthet

- **Tio provider-vägar**: OpenAI-, Mistral-, Claude-, Gemini- och Grok-API:er;
  ChatGPT- (Codex), Grok- och Google-abonnemang (Antigravity) utan användningsbaserad
  fakturering; OpenCode- (öppen källkod, gratis eller lokal) och OpenRouter-routrar
  (fler än 400 modeller).
- **Inget felaktigt på grund av en förlorad token**: kodblock, inline-kod,
  URL:er, ankare och citat ersätts med tokens före anropet och
  verifieras vid retur. Om en saknas skrivs inte filen.
- **Långa dokument**: segmentering anpassad efter modellens kontextfönster.
- **Läget `--news`**: skyddade engelska citat och flaggor hanterade per
  språk, för omvärldsbevakningsartiklar.
- **Läget `--eco`**: snabba och billigare modeller.
- **Valfri översättningsnotis**, överst, nederst eller på båda ställena.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 eller senare. För att installera från källkodslagret, se
[Bidra](#bidra).

## Konfiguration

Nycklar läses från tre platser, från högst till lägst prioritet; varje plats
fyller endast i det som föregående lämnat tomt.

|     | Var                                            | För vad                               |
| --- | ---------------------------------------------- | ------------------------------------- |
| 1   | Miljövariabler                                 | CI, containrar, tillfälliga undantag  |
| 2   | `.env` i aktuell katalog (eller överordnad) | en projektspecifik nyckel             |
| 3   | `~/.config/aipmt/.env`                                  | installeras en gång, gäller överallt  |

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
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) och `XDG_CONFIG_HOME` /
`APPDATA` ignoreras där, med en varning. Ett klonat arkiv får inte
kunna kapa din nyckel eller få dig att starta dess eget program vid den
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

## Kom igång

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` översatt till spanska ger `document-es.md` i `--target_dir`;
med `--include_model`, `document-es-gpt-5.6-terra.md`. Filändelsen blir
alltid `.md` — `article.mdx` ger `article-en.md` — utom med
`--keep_filename`, som behåller ursprungsnamnet. En översättning som redan finns
hoppas över om inte `--force` anges.

Slutkoder: `0` om allt lyckades eller hoppades över, `1` om en fil
misslyckades (lista på standard error), `2` om konfigurationen är orsak till felet.
En misslyckad fil skrivs aldrig, även om själva skrivningen misslyckas:
innehållet skrivs bredvid och döps sedan om. Det räcker att köra igen.

## Vilken modell ska man välja

Uppmätt på två verkliga dokument, översatta till samma fjorton språk av
varje modell. **Siffran är antalet språk, av fjorton, där
översättningen skrivs och där inget skiljer sig från källan.**

| Modell               | Hur man når den                   | Tät omvärldsbevakningsartikel | Denna README | Vad som skiljer sig, och på hur många språk                                                                                           |
| -------------------- | --------------------------------- | ----------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | Google API-nyckel                 | ✅ 14/14                      | ⚠️ 13/14     | 1 språk av 14: ett extra fetstilt ord (ja)                                                                                           |
| **Gemini 3.7 Flash** | Google-abonnemang (Antigravity)   | ✅ 14/14                      | ⚠️ 13/14     | 1 språk av 14: ett fetstilt ord mindre (ko)                                                                                          |
| **GPT-5.6 Sol**      | ChatGPT-abonnemang, eller OpenAI-nyckel | ✅ 14/14                | ⚠️ 12/14     | 2 språk av 14: ett fetstilt ord mindre (ar, ja)                                                                                       |
| **GLM-5.2**          | OpenRouter-nyckel                 | ✅ 14/14                      | ⚠️ 11/14     | 3 språk av 14: ett fetstilt ord mindre (hi, ja, ko)                                                                                   |
| Claude Sonnet 5      | Anthropic API-nyckel              | ⚠️ 11/14                      | ⚠️ 12/14     | 3 språk i artikeln: ett kodblock tillkom (es, de, hi); 2 i denna README: en länk utan formatering (sv), ett fetstilt ord (zh)        |
| Qwen 3.7 Flash       | OpenRouter-nyckel                 | ❌ 8/14                       | ⚠️ 10/14     | 1 språk avvisades i artikeln, 5 andra avviker; i denna README, ett fyrtiotal ord formaterade som `code` (ar)                 |
| Grok 4.6             | Grok-abonnemang                   | ❌ 8/14                       | ej bedömd    | 5 språk av 14 avvisades på grund av saknad inline-kod och URL:er; nederländska avviker helt                                          |
| GPT-OSS 20B          | lokal modell (Ollama)             | ❌ 7/14                       | ej ommätt    | 4 språk av 14 avvisades: modellen lämnade kvar text på franska, spärren stoppade dem                                                 |
| MiMo v2.5 (gratis)   | OpenCode Zen, utan konto          | ❌ 11/14                      | ej ommätt    | 1 språk avvisat; ett avsnitt förlorat på polska                                                                                       |
| Mistral Large        | Mistral API-nyckel                | ❌ 5/14                       | ❌ 1/14      | **ett helt avsnitt försvinner**: 1 språk i artikeln (hi), 3 i denna README (ar, hi, ko) — och 3 språk avvisades i artikeln           |
| DeepSeek V4 Flash    | OpenRouter-nyckel                 | ❌ 3/14                       | ej ommätt    | 10 språk av 14 avvisades; 37 minuter per språk                                                                                        |

|     | Vad symbolen betyder                                                                                                                                                                                  |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alla fjorton språk översatta, och inget skiljer sig från källan                                                                                                                                       |
| ⚠️  | alla fjorton språk översatta; det som skiljer sig är **formatering** — ett fetstilt ord, en `code`, en länk som förlorat sina hakparenteser. Ingen text, URL, kodblock eller sektion saknas |
| ❌  | minst ett språk kunde inte översättas — filen avvisades och skrevs inte — **eller** innehåll saknas i en skriven fil                                                                                  |

Värt att notera:

- **En avvisad översättning är inte en skadad översättning.** När en token
  saknas vid retur skrivs filen inte och språket räknas som
  avvisat. Det är vad som händer Grok i artikeln: fyra inline-koder och
  tre URL:er förlorades redan i det första segmentet på de fem icke-latinska skrifterna.
- **Detta skyddsnät täcker inte rubriker, tabeller, front matter eller
  brödtext.** En modell som tar bort ett avsnitt returnerar en fil som verktyget
  skriver utan att protestera — vilket är fallet med Mistral. Dessa element kan
  inte ersättas med en token, och de nuvarande kontrollerna granskar dem inte;
  `scripts/compare_structure.py` upptäcker ett förlorat avsnitt, men i efterhand.
- **Grok har inget betyg för denna README**: dess CLI-session löpte ut efter tolv
  språk, varav elva utan avvikelser. En avbruten testomgång betygsätts inte.
- **Dokumentets densitet spelar större roll än språket.** Grok klarar
  vanliga README-filer men tappar tråden i en länkfylld artikel, även på
  nederländska.

Datum och dokument: kolumnen "Denna README" mättes den 9 september 2026
på en låst version av denna fil (785 rader, 285 inline-koder, 89 tabellrader),
som sedan dess har justerats — förutom Antigravity-raden, som mättes den
26 september på den version som publicerades med 1.14.0, vilken var kortare (600 rader,
257 inline-koder, 85 tabellrader). Kolumnen "Tät omvärldsbevakningsartikel"
härrör från testomgången den 4 och 5 september på en artikel med 589 rader,
förutom Grok-raden som mättes om den 9 september på en annan utgåva av samma
bevakning, samt Antigravity-raden som mättes den 26 september på samma artikel.
Fullständiga tabeller, tidsåtgång och protokoll finns i
[Detaljerade mätningar](#detaljerade-mätningar).

## Alla alternativ

| Alternativ               | Beskrivning                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`           | Enskild Markdown-fil att översätta (alternativ till `--source_dir`)                                           |
| `--source_dir`           | Källkatalog som innehåller Markdown-filerna (standard: `content/posts`)                                        |
| `--target_dir`           | Utdatakatalog för de översatta filerna (standard: `traductions_en`)                                             |
| `--source_lang`           | Källspråk (standard: `fr`)                                                                          |
| `--target_lang`           | Målspråk (standard: `en`)                                                                           |
| `--model`           | Specifik modell att använda                                                                                   |
| `--eco`           | Använd ekonomimodeller                                                                                        |
| `--use_mistral`           | Använd Mistral AI API                                                                                         |
| `--use_claude`           | Använd Claude API                                                                                             |
| `--use_gemini`           | Använd Gemini API                                                                                             |
| `--use_grok`           | Använd xAI API (Grok) — kräver `XAI_API_KEY`                                                                 |
| `--use_codex`           | Använd Codex CLI via kvoten för ChatGPT-abonnemanget                                                          |
| `--use_grok_cli`           | Använd Grok CLI via kvoten för Grok-abonnemanget                                                              |
| `--use_antigravity`           | Använd Antigravity CLI (`agy`) via kvoten för Google AI Pro- eller Ultra-abonnemanget                |
| `--use_opencode`           | Använd OpenCode (öppen källkod) mot leverantören konfigurerad i OpenCode; kräver `--model provider/modèle`             |
| `--use_openrouter`           | Använd OpenRouter — kräver `OPENROUTER_API_KEY` och `--model fournisseur/modèle`                                                  |
| `--force`           | Tvinga omöversättning                                                                                         |
| `--keep_filename`           | Behåll ursprungligt filnamn                                                                                   |
| `--news`           | Nyhetsläge: skyddar engelska citat, hanterar flaggor per språk                                                |
| `--add_translation_note`           | Lägg till en översättningsnotis                                                                               |
| `--note_position`           | Notisens position: `top`, `bottom` (standard), eller `both`                            |
| `--note_format`           | Notisens format: `legacy` (standard, fetstilt stycke) eller `marker`                              |
| `--include_model`          | Inkludera modellnamnet i utdatafilen                                                                          |
| `--reasoning_effort`          | Resonemangsinsats för GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

De nio `--use_*`-flaggorna utesluter varandra ömsesidigt: att kombinera två
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

`--eco` växlar till varje leverantörs ekonominivå.

| Leverantör  | Kvalitet (standard)                                   | Ekonomi (`--eco`)         |
| ----------- | ----------------------------------------------------- | --------------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`                   |
| Claude      | `claude-sonnet-5`                                       | `claude-haiku-4-5`                   |
| Mistral     | `mistral-large-latest`                                       | `mistral-small-latest`                   |
| Gemini      | `gemini-3.7-flash`                                       | `gemini-3.1-flash-lite`                   |
| Codex       | `gpt-5.6-sol` (även `terra` och `luna` via `--model`) | `gpt-5.6-luna`                   |
| Grok API    | `grok-4.6`                                       | `grok-4.3`                   |
| Grok CLI    | `grok-4.6`                                       | `grok-4.5`                   |
| Antigravity | `gemini-3.7-flash-medium`                                       | `gemini-3.7-flash-low`                   |
| OpenCode    | `--model provider/modèle` obligatorisk                          | samma sak — `--eco` utan effekt |
| OpenRouter  | `--model fournisseur/modèle` obligatorisk                          | samma sak — `--eco` utan effekt |

### Med ChatGPT-prenumeration: `--use_codex`

Styr den officiella Codex-CLI:n: översättningen dras från kvoten för
ChatGPT-prenumerationen, utan API-nyckel eller användningsbaserad debitering.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Den binära filen söks i `CODEX_BIN`, därefter i `PATH`, sedan i paketet
  `openai-codex-cli-bin`. `~/.codex/auth.json` läses aldrig.
- `OPENAI_API_KEY` och `CODEX_API_KEY` tas bort från underprocessens
  miljö: en befintlig nyckel växlar aldrig över till API:et.
- Varje segment kostar minst ett ”meddelande” i 5-timmarsfönstret — två
  om valideringen misslyckas och ett nytt försök görs. OpenAI anger som
  uppskattning 250–2 000 meddelanden/5 timmar för `gpt-5.6-luna` (`--eco`) och
  10–100 för `gpt-5.6-sol` på ett Plus-abonnemang.
- `--model gpt-5.6-terra` och `--model gpt-5.6-luna` går också via
  prenumerationen. En modell som kontot inte har behörighet till ger en 400 ”model is
  not supported when using Codex with a ChatGPT account”.
- Långsammare än ett API, och skillnaden ökar med dokumentets storlek: för denna README,
  medianvärde 6 min 46 s per språk med `gpt-5.6-sol`, jämfört med 36 s för
  `gemini-3.7-flash`.
- Avvisas i CI (`CI` eller `GITHUB_ACTIONS` definierad): prenumerationen autentiseras
  via en personlig sessionsfil, som inte hör hemma på en delad runner.
- Variabler: `CODEX_BIN`, `CODEX_TIMEOUT` (sekunder per segment, standard 600).

### Med Grok-prenumeration: `--use_grok_cli`

Samma princip med den officiella Grok Build-CLI:n, via SuperGrok- eller
X Premium+-prenumeration.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Svagare isolering än Codex.** Groks OS-sandbox fungerar
  inte på många moderna Linux-maskiner (AppArmor, sockets för container-runtime),
  och en profil som inte kan tillämpas startar oisolerad i
  tysthet. Skriptet begär därför ingen standardprofil, meddelar detta, och
  förlitar sig på CLI:ns `--deny`-regler, inklusive dess catch-all `*` — det enda
  skikt som vägrar att starta istället för att ta bort skyddet i smyg.
  `GROK_TRANSLATE_SANDBOX=read-only` kräver OS-sandbox, och starten misslyckas om
  maskinen inte kan uppfylla detta.
- Kvoten är veckovis, delad med Chat, Imagine och Voice, och inget kommando
  gör det möjligt att läsa av den: en batchkörning kan förbruka samtalskvoten
  utan förvarning.
- Variabler: `GROK_BIN`, `GROK_HOME` (CLI-katalog, standard `~/.grok`),
  `GROK_TIMEOUT` (standard 900), `GROK_TRANSLATE_SANDBOX`.

### Med Google-prenumeration: `--use_antigravity`

Samma princip med `agy`, den officiella CLI:n för Antigravity: för den som betalar för Google
AI Pro eller Ultra dras översättningen från prenumerationskvoten istället
för att debiteras per token. Detta är den enda vägen till denna kvot: Gemini CLI
stöder inte längre dessa konton sedan den 18 juni 2026
([tillkännagivande](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
och Antigravitys SDK accepterar endast en API-nyckel eller ett Google Cloud-projekt.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Inga betalningsvägar förblir öppna.** agy tar endast emot en sluten lista av variabler
  från din miljö — `PATH`, språk och tidszon,
  terminal, identitet, proxyservrar och certifikat, sessionsbuss — och inga nycklar:
  flera av dess variabler växlar ett anrop utan att visa något (uppmätt:
  en skickar dokumentet till en tredjepartsgateway, en annan till ett debiterat
  Google Cloud-projekt), och en exkluderingslista missade alltid variabler vid varje granskning.
  Före varje segment måste `agy -p /config`, som inte förbrukar någon kvot, visa
  att betalda AI-krediter är inaktiverade, utan API-nyckel eller Google Cloud-projekt — en
  saknad inställning tolkas som avvisning —, annars översätts ingenting; varje anrops
  logg måste därefter intyga prenumerationen (`authMethod=consumer`), annars avvisas
  svaret.
- **Isolering.** Varje anrop körs i en privat och temporär arbetskatalog,
  med en verktygslös översättningsagent: dina inställningar, regler,
  plugins, MCP-servrar och hooks för agy kommer inte in där, ingenting läggs till i din
  historik, och inloggningen förblir i nyckelringen, som aipmt aldrig läser.
  Om en agent saknas faller agy i tysthet tillbaka på sin kodningsagent
  och dess verktyg: en hel loggrad måste bekräfta rätt agent — ett dokument
  som citerar detta meddelande ersätter den inte —, annars avvisas det.
- **Plattformar**: Linux, i en session som har en nyckelring (D-Bus-sessionsbuss,
  Secret Service); macOS stöds, men har inte testats. Avvisas
  på Windows, där agy inte läser de variabler som isolerar varje anrop, och
  på Linux utan sessionsbuss — SSH-session, container, server: där sparar agy
  sin token i en fil i `~/.gemini`, som isoleringen döljer.
  Avvisningen sker före start med orsak, istället för att vänta en minut
  på en inloggningskod.
- **Modeller**: de från `agy models`. Gemini-modellerna har ansträngningsnivån i namnet
  (`gemini-3.7-flash-low`…): ett namn utan suffix avvisas före anropet, och
  `--reasoning_effort` har ingen effekt. De två standardvärdena fastställdes genom en
  testomgång på fjorton språk (se [Detaljerade mätningar](#detaljerade-mätningar)).
  Claude och GPT-OSS har en egen kvot, som är betydligt mindre: cirka 1 % av
  5-timmarsfönstret per uppmätt anrop, jämfört med 0,05 % för Flash.
- **Kvot**: per grupp, ett 5-timmarsfönster och ett veckovis fönster, proportionellt
  mot tokenkostnaden. Uppmätt på författarens konto, baserat på en
  testomgång med 32 översättningar: cirka en halv procentenhet av 5-timmarsfönstret
  för en README på 40 000 tecken med `gemini-3.7-flash-medium`; veckogränsen
  beror däremot på abonnemangsnivån. Återförsök följer vad agy deklarerar som
  återförsöksbart; i annat fall görs aldrig nya försök vid ett tömt fönster: det gör
  att varje fil misslyckas fram till återställningen som visas av `/usage`.
- **Långsammare än API:et**: för den kompakta mätartikeln tar Gemini 3.7 Flash
  i median 3 min 14 s per språk via prenumerationen, jämfört med 1 min 18 s via
  API:et.
- **Avbrott**: Ctrl-C, eller en stängd terminal, stoppar agy tillsammans med
  kommandot istället för att låta det slutföra sin körning på din kvot; detsamma
  gäller för Codex, Grok CLI och OpenCode. Under `nohup` fortsätter översättningen.
- Avvisas i CI (`CI` eller `GITHUB_ACTIONS` definierad): inloggningen finns i en
  personlig nyckelring. På en runner, använd `--use_gemini` med `GOOGLE_API_KEY`.
- Variabler: `AGY_BIN` (annars `PATH`, därefter `~/.local/bin/agy`),
  `AGY_TIMEOUT` (sekunder per segment, inklusive start, standard 900).

**Användarvillkor: det är ditt konto som berörs.**
[Antigravitys användarvillkor](https://antigravity.google/terms) (avsnitt 6) och dess
[FAQ](https://antigravity.google/docs/faq/) förbjuder åtkomst till tjänsten
via tredjepartsprogramvara med hjälp av Antigravity-inloggningen — Claude Code,
OpenClaw och OpenCode nämns där —, med risk för avstängning av kontot. aipmt
läser inte och återanvänder inte inloggningstokenen: det startar den officiella binären i det
[headless-läge](https://antigravity.google/docs/cli/headless/) som Google
dokumenterar för skript och CI. En Google-medarbetare har bedömt det som ”standard”
att köra `agy -p` från ett lokalt skript för sitt eget arbete
([officiellt forum, 25 september 2026, icke-bindande svar](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
inget regelverk avgör fallet för ett distribuerat verktyg som detta.

**Endast offentliga dokument.** Enligt avsnitt 5 i samma villkor kan all
interaktion — prompter, svar, metadata — användas för att förbättra Googles
produkter och maskininlärning samt granskas av
människor, även för betalprenumerationer. Inaktivering sker via inställningen
`enableTelemetry`, vars effekt inte är dokumenterad och som aipmt inte konfigurerar; dina
inställningar för agy följer inte med i dess isolering. Kör inget konfidentiellt genom detta.

### Till valfri leverantör: `--use_opencode`

[OpenCode](https://opencode.ai) är en öppen källkodsbaserad kodagent (MIT) som
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

`--model` är obligatorisk: utan den faller OpenCode tillbaka på en gratismodell
vars interaktioner kan användas för träning, och det valet görs inte åt
dig.

Isolering vid varje anrop:

- en inline-konfiguration, som har företräde framför din, definierar en agent `aipmt`
  där alla verktyg nekas (`permission: { "*": "deny" }`), sessionsdelning
  inaktiverad, `--pure`, aldrig `--auto`;
- temporär och tom arbetskatalog, `OPENCODE_DISABLE_PROJECT_CONFIG` och
  `OPENCODE_DISABLE_CLAUDE_CODE` satta — utan dem injicerar OpenCode i prompten
  `AGENTS.md` från den aktuella katalogen samt `~/.claude/CLAUDE.md`. Den
  globala `~/.config/opencode/AGENTS.md` injiceras fortfarande, OpenCode tillåter inte
  att den utesluts;
- utdatakontrakt: returkod 0, inga `error`-händelser, inga
  verktygsanrop, sista steget i `stop`, icke-tom text, och att agenten `aipmt`
  faktiskt har lästs in — en okänd `--agent` gör inte att OpenCode kraschar, utan
  den faller i tysthet tillbaka på kodningsagenten;
- inga nycklar från `aipmt` skickas vidare, förutom `OPENCODE_API_KEY`, nyckeln
  för själva OpenCode. Leverantörer konfigureras i OpenCode, inte i
  `.env` för `aipmt`.

Att notera:

- Gratismodellerna i Zen är föränderliga, med odokumenterade begränsningar, och
  deras interaktioner kan användas för träning: lämpligt för offentlig
  dokumentation, inte för privat innehåll.
- En lokal modell måste erbjuda minst 16 k tokens kontextfönster, då segmenten
  kan vara upp till 16 000 tecken. Ollama konfigurerar ofta 4 096: använd
  en `Modelfile` med `PARAMETER num_ctx 32768`.
- `--eco` har ingen effekt; `--reasoning_effort` skickas vidare i befintligt skick som
  OpenCodes `--variant`.
- OpenCode loggar varje session i `~/.local/share/opencode/`.
- Variabler: `OPENCODE_BIN` (annars `PATH`, därefter `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (sekunder per segment, standard 600). `OPENCODE_CONFIG`
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

`reasoningEffort: "none"` stänger av det resonemang som Ollama aktiverar som standard på dessa
modeller, och som en Modelfile inte kan inaktivera. Uppmätt på en mening med
sex ord: 919 resonemangstokens och 68 sekunder utan alternativet, 9 tokens med.

### Till över 400 modeller: `--use_openrouter`

OpenRouter är en användningsbaserat debiterad router med ett gemensamt saldo, framför
modeller som driftas av tredje part — inklusive öppna kinesiska modeller som ingen
annan leverantör tillhandahåller här.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` är obligatorisk. En förhandskontroll (preflight), som körs före all debitering, hanterar
två särdrag i dirigeringen:

- **Samma modell tillhandahålls av dussintals värdar med olika
  gränser** — för `z-ai/glm-5.3-flash`, 23 värdar varav en är begränsad till
  2 048 utdatatokens. Förhandskontrollen läser `/api/v1/models/{modèle}/endpoints`,
  sorterar bort värdar med under 8 000 utdatatokens eller med degraderad status, och
  låser övriga med `allow_fallbacks: false`.
- **Resonemang debiteras enligt utdatataxa** — 107 tokens jämfört med 2 för
  ett ”OK”-svar från `z-ai/glm-5.2`. Det är avstängt som standard; modeller
  som kräver det får den lägsta ansträngningsnivå de accepterar, eftersom katalogens standardvärde
  kan fylla utdatakvoten innan översättningen är klar.
  `--reasoning_effort` har fortsatt företräde.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Kontextfönstret hämtas från katalogen. En modell under 16 400 tokens
  avvisas före anrop: 8 400 för prompten och segmentet, minst 8 000
  för utdata.
- En slug som saknas i katalogen, en onåbar katalog eller avsaknad av
  värdar som klarar gränsen avbryter kommandot.
- `finish_reason=length` med tom utdata beror på att budgeten förbrukats av
  resonemanget, inte på trunkering: meddelandet skiljer på detta.
- `--eco` har ingen effekt.
- Variabler: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (standard `https://openrouter.ai/api/v1`, `https://`
  krävs), `OPENROUTER_TIMEOUT` (standard 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (standard 30).

### Översättningsnotis

`--add_translation_note` lägger till en notis, i `bottom` (standard), `top` (efter
front matter) eller `both` (`--note_position`), i formatet `legacy` (stycke i
fetstil, standard) eller `marker` (`--note_format`). Formatet `marker` är en
osynlig Markdown-referensdefinition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
följd av ett citat i fetstil: läsbart på GitHub, användbart vid byggprocessen med en
remark-plugin.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detaljerade mätningar

Alla mätningar är faktiskt genomförda översättningar med `aipmt`, till
fjorton språk: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Skrivna** räknar de filer som kontrollerna släppte igenom; **Utan
avvikelse** de där `scripts/compare_structure.py` inte upptäcker något — samma antal
avsnitt, underrubriker, länkar, unika URL:er, kodblock,
inline-kod, tabellrader, citatblock och ord i fetstil.

”Utan avvikelse” betyder ”inget upptäckt”, inte ”identisk”: jämförelseverktyget
räknar element utan att läsa deras innehåll. Det signalerar inte om en rubrik på
nivå 4 har tagits bort, om texten i en inline-kod har ersatts, om en flagga har
bytts ut, och gör ingen bedömning av språket.

### Tät bevakningsartikel, läge `--news`

En utgåva av [AI-bevakningen på jls42.org](https://jls42.org/fr/news):
589 rader, 140 länkar, 21 avsnitt, 3 skyddade engelska citat. Testomgång
den 4 och 5 september 2026.

| Modell                                          | Åtkomst            | Skrivna | Utan avvikelser | Median/språk   |
| ----------------------------------------------- | ------------------ | ------- | --------------- | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14**    | 1 min 18 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google-prenumeration | 14/14   | ✅ **14/14**    | 3 min 14 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT-prenumeration | 14/14   | ✅ **14/14**    | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14**    | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14**    | 26 min 23 s    |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14        | 6 min 31 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14        | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14         | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | lokal              | 10/14   | ❌ 7/14         | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14         | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14         | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok-prenumeration | 1/14    | ❌ 1/14         | 23 min 11 s    |

Grok mättes om den 9 september på en annan utgåva av samma bevakning
(356 rader): 9 språk skrivna av 14, 8 utan avvikelser. Det är denna siffra som
visas i huvudtabellen. Tre avbrutna testomgångar är inte medräknade:
`qwen3.5-27b` (9 språk) och `kimi-k2.6` (4) på grund av brist på krediter,
`z-ai/glm-5.3-flash` vars två misslyckanden berodde på en resonemangsinställning
som leverantören sedan dess har åtgärdat. OpenRouter-raderna mättes med
routerns standardinställningar, före `--use_openrouter`; `z-ai/glm-5.2`,
ommätt med den medföljande leverantören, ger samma 14/14. Siffrorna beräknades
om den 10 september med det nuvarande jämförelseverktyget: `qwen3.8-flash` och
`qwen3.7-flash` vinner vardera ett språk jämfört med den första
publiceringen, övriga är oförändrade.

Raden för `--use_antigravity` mättes den 26 september på samma artikel,
med fyra översättningar parallellt. På engelska tog modellen själv bort de
tre raderna med fransk översättning under citaten, utan att hitta på någon
flagga, och de engelska citaten är intakta: reservrensningen behövde inte
göra något. I `--eco` (`gemini-3.7-flash-low`), på endast fyra språk
(en, ja, ar, hi): 4 skrivna av 4, alla utan avvikelser, median på 1 min 52 s.

### Detta projekts README, standard-Markdown

Fryst revision den 9 september 2026: 785 rader, 285 inline-kodavsnitt, 40
blockavslut, 89 tabellrader. Fyra översättningar parallellt.

| Modell                                          | Skrivna | Utan avvikelser | Median/språk   | Vad som skiljer sig                                                      |
| ----------------------------------------------- | ------- | --------------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14        | 36 s           | ett ord i fetstil (ja)                                                   |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14        | 1 min 22 s     | ett ord i fetstil (ko)                                                   |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14        | 2 min 56 s     | en länk (sv), ett ord i fetstil (zh)                                     |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14        | 6 min 46 s     | ett ord i fetstil (ar, ja)                                               |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14        | 2 min 34 s     | ett ord i fetstil (hi, ja, ko)                                           |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14        | 2 min 17 s     | 40 inline-kodavsnitt tillagda på arabiska; fetstil (hi, ja, ko)          |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14         | 2 min 44 s     | ett förlorat avsnitt (ar, hi, ko); kodblock tillagda (ja, ko, ro, zh)   |

Två avbrutna testomgångar är inte medräknade: Grok, vars CLI-session löpte ut
efter tolv språk (elva utan avvikelse), och `qwen3.8-flash`, HTTP 429 från dess
värd efter två. `opencode/mimo-v2.5-free` och `ollama/gpt-oss-20b-32k`
mättes inte om på denna revision; på den från 4 och 5 september,
som var 277 rader kortare, skrev de vardera 9 översättningar av 14, varav 7
respektive 1 utan avvikelser.

Raden `--use_antigravity` mättes inte på den frysta revisionen, utan
den 26 september på den som publicerades med 1.14.0: 600 rader, 257 inline-kodavsnitt,
30 blockavslut, 85 tabellrader. Eftersom den är 185 rader kortare kan den inte
jämföras rakt av med de andra raderna.

### Fyra README-filer från kända projekt

FastAPI, Ollama, tldr-pages och Vue.js, tagna som de är från GitHub –
enklare dokument än de två tidigare. Testomgången riktade sig till modeller
med svårigheter; Gemini fungerar där som jämförelsepunkt.

| Modell                    | Omfattning                 | Skrivna | Utan avvikelser |
| ------------------------- | -------------------------- | ------- | --------------- |
| `gemini-3.7-flash`        | 4 projekt × 14 språk       | 56/56   | ✅ **55/56**    |
| `opencode/mimo-v2.5-free` | 4 projekt × 14 språk       | 55/56   | ❌ 47/56        |
| `grok-4.6` (prenumeration) | 4 projekt × ar, hi, ja, zh | 16/16   | ❌ 14/16        |
| `ollama/gpt-oss-20b-32k`  | 4 projekt × ar, hi, ja, zh | 15/16   | ❌ 9/16         |

### Vad dessa mätningar inte är

- **Ingen fullständig rankning**: OpenRouter ensamt erbjuder över fyra hundra
  modeller, ett femtontal har mätts.
- **Ungefärliga tidsangivelser**: från tre till sex parallella översättningar
  beroende på testomgång, och en leverantörs genomströmning varierar under dagen.
- **Tidsbundna observationer**: modeller förändras under samma namn, och era
  dokument är inte våra.

För att upprepa mätningen på era egna dokument, på en fryst kopia av filen:

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
med `No module named aipmt`.

Kvalitetsverktyg, valfritt men rekommenderat:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

De 28 översättningarna i arkivet (README och CHANGELOG, fjorton språk)
återskapas med `./regen_translations.sh --force` – Codex och `gpt-5.6-sol` via
ChatGPT-prenumerationen som standard, fyra parallellt. `REGEN_PROVIDER` och
`REGEN_MODEL` ändrar sökvägen: `antigravity` förblir på en prenumeration, Googles,
och godkänns utan undantag; ett debiterat API (`openai`, `gemini`,
`grok`, `openrouter`) nekas utan `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` sätter ett maxtak för varje jobb (600 s, 1 800 s för Codex och
Antigravity). Detaljerna om verktygen finns i `CLAUDE.md`.

## Projekt som använder detta skript

- **[jls42.org](https://jls42.org)** – personlig blogg publicerad på 15 språk. Dess
  [dagliga AI-bevakning](https://jls42.org/fr/news) översätts varje dag
  av detta verktyg och fungerar som referensdokument för mätningarna ovan.

## Författare

Julien LE SAUX
E-post: contact@jls42.org

## Licens

GNU GENERAL PUBLIC LICENSE Version 3. Se [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Friskrivningsklausul

Detta program distribueras **helt utan garantier**, i enlighet med villkoren i
avsnitt 15 och 16 i GPL v3: tillhandahålls i ”befintligt skick”, utan garanti för säljbarhet
eller lämplighet för ett visst ändamål, och dess författare kan inte hållas
ansvarig för eventuella skador som uppstår till följd av dess användning. Licenstexten
har företräde framför denna sammanfattning.

- **Läs igenom före publicering.** Skydden täcker kodblock, inline-kod,
  webbadresser, ankare och citat i läget `--news` – inte
  rubriker, tabeller, front matter eller innebörden i era meningar.
- **Era dokument skickas till den valda leverantören**, under dennes
  användarvillkor och datapolicy. Vissa gratismodeller kan återanvända
  era konversationer för träning, och villkoren för Antigravity tillåter Google
  att återanvända dem och låta människor granska dem, inklusive med betald
  prenumeration; en lokal modell är det enda sättet som inte skickar några data
  utanför er maskin.
- **API-anrop debiteras dig.** Detta program sätter inget tak för
  kostnaden: ett långt dokument, ett återförsök efter misslyckande eller en modell
  som resonerar mycket kostar mer.
- **De publicerade mätningarna är tidsbundna observationer**, inte garantier.

Produkt- och företagsnamn som nämns tillhör sina respektive ägare.
Detta projekt är inte anslutet till någon av dem.

**Artikel översatt från fr till sv med gemini-3.7-flash-medium.**

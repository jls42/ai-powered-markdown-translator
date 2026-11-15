# AI-driven Markdown-översättare

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Kodkvalitet</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Quality Gate-status"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Säkerhetsbetyg"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Tillförlitlighetsbetyg"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Underhållsbarhetsbetyg"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Testtäckning"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Sårbarheter"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Buggar"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Kodlukter"></a>
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

Översätter Markdown-filer från ett språk till ett annat med bibehållen
struktur: kodblock, inline-kod, webbadresser, ankare, tabeller och front
matter. Elva sätt att anropa en modell – fem API:er, fyra abonnemang utan
användningsbaserad debitering, två routrar – och ett publicerat mått på vad varje
modell faktiskt bevarar.

## I korthet

- **Elva leverantörsvägar**: OpenAI-, Mistral-, Claude-, Gemini- och Grok-API:er;
  ChatGPT- (Codex), Grok-, Google- (Antigravity) och Claude-abonnemang (Claude
  Code) utan användningsbaserad debitering; OpenCode- (öppen källkod, gratis eller lokal) och OpenRouter-routrar
  (fler än 400 modeller).
- **Inget blir fel på grund av en förlorad token**: kodblock, inline-kod,
  webbadresser, ankare och citat ersätts med tokens före anropet och
  verifieras vid retur. Om en saknas skrivs filen inte.
- **Långa dokument**: segmentering baserad på modellens kontextfönster.
- **`--news`-läge**: skyddade engelska citat och flaggor hanterade per
  språk, för omvärldsbevakningsartiklar.
- **`--eco`-läge**: snabba och billigare modeller.
- Valfri **översättningsnotis**, överst, nederst eller på båda ställena.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11 eller senare. För att installera från källkodsarkivet, se
[Bidra](#bidra).

## Konfiguration

Nycklar läses från tre platser, från högsta till lägsta prioritet; varje plats
fyller endast i vad den föregående lämnar tomt.

|     | Var                                           | För vad                               |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Miljövariabler                                | CI, containrar, tillfälliga undantag  |
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

`GEMINI_API_KEY` accepteras istället för `GOOGLE_API_KEY`. Användarfilen
följer `XDG_CONFIG_HOME` (endast absolut sökväg) och `%APPDATA%`
under Windows. Utan nyckel listar kommandot de tre platserna.

**Ett projekts `.env` kan varken omdirigera anrop eller välja vilket program
som körs.** Den tillhandahåller nycklar, aldrig en destination eller en binär: alla
variabler med `_BASE_URL`, `_API_BASE`, `_ENDPOINT` eller `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, proxyservrar (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), certifikatarkiv (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) och `XDG_CONFIG_HOME` /
`APPDATA` ignoreras där, med en varning. Ett klonat arkiv får inte
kunna kapa din nyckel eller få dig att köra dess eget program vid den
första översättningen. Denna fil läses också utan interpolering:
`NOM=${OPENAI_API_KEY}` kopierar inte nyckeln där. Ange dessa variabler i
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
med `--include_model`, `document-es-gpt-6.1-terra.md`. Filtillägget blir
alltid `.md` – `article.mdx` ger `article-en.md` – förutom med
`--keep_filename`, som behåller ursprungligt namn. En redan befintlig översättning
hoppas över utan `--force`.

Slutkoder: `0` om allt lyckades eller hoppades över, `1` om det finns någon fil
som misslyckades (lista på standard error), `2` om konfigurationen är orsaken.
En misslyckad fil skrivs aldrig, även om själva skrivningen misslyckas:
innehållet skrivs vid sidan om och döps sedan om. Det räcker att köra igen.

## Vilken modell ska man välja

Mätt på två verkliga dokument, översatta till samma fjorton språk av
varje modell. **Siffran anger antalet språk, av fjorton, där
översättningen skrivs och där inget skiljer sig från källan.**

| Modell                | Hur man kommer åt den             | Tät bevakningsartikel   | Denna README | Vad som skiljer sig och på hur många språk                                                                                                                         |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google-abonnemang (Antigravity)   | ✅ 14/14                | ✅ 14/14     | inget, i något av de två dokumenten                                                                                                                                |
| **Claude Sonnet 5.5** | Anthropic API-nyckel              | ✅ 14/14                | ✅ 14/14     | inget, i något av de två dokumenten                                                                                                                                |
| **Gemini 3.7 Flash**  | Google API-nyckel                 | ✅ 14/14                | ⚠️ 13/14     | 1 språk av 14: ett extra fetstilt ord (ja)                                                                                                                         |
| **Gemini 3.7 Flash**  | Google-abonnemang (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 1 språk av 14: ett fetstilt ord mindre (ko)                                                                                                                        |
| **GPT-5.6 Sol**       | ChatGPT-abonnemang, eller OpenAI-nyckel | ✅ 14/14          | ⚠️ 12/14     | 2 språk av 14: ett fetstilt ord mindre (ar, ja)                                                                                                                    |
| **GLM-5.2**           | OpenRouter-nyckel                 | ✅ 14/14                | ⚠️ 11/14     | 3 språk av 14: ett fetstilt ord mindre (hi, ja, ko)                                                                                                                |
| Claude Sonnet 5       | Claude-abonnemang (Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 1 språk av 14 i artikeln: ett extra fetstilt ord (zh); 1 i denna README: en tabellrad sammanslagen med föregående, dold vid rendering (ar)                        |
| Claude Haiku 4.5      | Claude-abonnemang (Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 3 språk i artikeln: en avsnittsrubrik ändrad till nivå 1 (en, pl, ro); i denna README, inget för jämförelseverktyget, men interna länkar duplicerade på engelska |
| Claude Sonnet 5       | Anthropic API-nyckel              | ⚠️ 11/14                | ⚠️ 12/14     | 3 språk i artikeln: ett kodblock dök upp (es, de, hi); 2 i denna README: en länk utan dess formatering (sv), ett fetstilt ord (zh)                               |
| Claude Haiku 4.5      | Anthropic API-nyckel              | ⚠️ 7/14                 | ✅ 14/14     | 7 språk i artikeln: en avsnittsrubrik ändrad till nivå 1 – på japanska kvar på franska; inget i denna README                                                       |
| Claude Haiku 5.5      | Anthropic API-nyckel              | ⚠️ 11/14                | ❌ 12/14     | 3 språk i artikeln: en avsnittsrubrik ändrad i nivå eller duplicerad (ja, ko, zh); i denna README, 2 avvisade språk, förlorad inline-kod (ar, hi)                  |
| Qwen 3.7 Flash        | OpenRouter-nyckel                 | ❌ 8/14                 | ⚠️ 10/14     | 1 språk avvisat i artikeln, 5 andra avviker; i denna README, ett fyrtiotal ord formaterade som `code` (ar)                                                 |
| Grok 4.6              | Grok-abonnemang                   | ❌ 8/14                 | ej betygsatt | 5 språk avvisade av 14, på grund av utebliven inline-kod och URL:er; nederländska avviker helt                                                                    |
| GPT-OSS 20B           | lokal modell (Ollama)             | ❌ 7/14                 | ej ommätt    | 4 språk avvisade av 14: modellen lämnade stycken på franska, spärren stoppade dem                                                                                  |
| MiMo v2.5 (gratis)    | OpenCode Zen, utan konto          | ❌ 11/14                | ej ommätt    | 1 språk avvisat; ett avsnitt förlorat på polska                                                                                                                    |
| Mistral Large         | Mistral API-nyckel                | ❌ 5/14                 | ❌ 1/14      | **ett helt avsnitt försvinner**: 1 språk i artikeln (hi), 3 i denna README (ar, hi, ko) – och 3 språk avvisade i artikeln                                         |
| DeepSeek V4 Flash     | OpenRouter-nyckel                 | ❌ 3/14                 | ej ommätt    | 10 språk avvisade av 14; 37 minuter per språk                                                                                                                      |
| Claude Opus 5.5       | Claude-abonnemang (Claude Code)   | ❌ 0/14                 | ✅ 14/14     | artikeln avvisad på alla 14 språk av Opus skyddsspärrar på grund av en biologinotisk; inget i denna README                                                        |

|     | Vad symbolen betyder                                                                                                                                                                                  |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alla fjorton språk översatta, och inget skiljer sig från källan                                                                                                                                       |
| ⚠️  | alla fjorton språk översatta; det som skiljer sig är **formatering** – ett fetstilt ord, en `code`, en länk som förlorar sina hakparenteser. Ingen text, ingen URL, inget kodblock, inget avsnitt saknas |
| ❌  | minst ett språk kunde inte översättas – filen avvisas, skrivs inte – **eller** innehåll saknas i en skriven fil                                                                                      |

Viktiga slutsatser:

- **En avvisad översättning är inte en förstörd översättning.** När en token
  saknas vid retur skrivs inte filen och språket räknas som
  avvisat. Det är vad som händer med Grok i artikeln: fyra inline-koder och
  tre URL:er förlorade redan i det första segmentet, på de fem icke-latinska skrifterna.
- **En modell kan avvisa ett helt dokument på grund av en enda mening.** Opus 5.5
  översätter denna README utan en enda avvikelse, men inte en enda omvärldsbevakningsartikel: dess
  skyddsspärrar avbryter svaret vid en biologinotisk. Filen skrivs
  inte, och aipmt förklarar varför.
- **Detta skyddsnät täcker inte rubriker, tabeller, front matter eller
  text.** En modell som tar bort ett avsnitt returnerar en fil som verktyget skriver
  utan att protestera – vilket är fallet med Mistral. Dessa element kan inte
  ersättas med en token, och de nuvarande skydden kontrollerar dem inte;
  `scripts/compare_structure.py` upptäcker ett förlorat avsnitt, men först i efterhand.
- **Grok har inget betyg för denna README**: dess CLI-session löpte ut efter tolv
  språk, varav elva utan avvikelser. En avbruten testomgång betygsätts inte.
- **Dokumentets densitet spelar större roll än språket.** Grok klarar
  vanliga README-filer och fallerar på en artikel fylld med länkar, även på
  nederländska.

Datum och dokument: kolumnen ”Denna README” mättes den 9 september 2026
på en låst revision av denna fil (785 rader, 285 inline-koder, 89 tabellrader),
som har redigerats sedan dess – med undantag för raderna för Antigravity och Claude Code,
som mättes den 26 september på den kortare revision som publicerades med 1.14.0
(600 rader, 257 inline-koder, 85 tabellrader), samt raderna för Claude
Sonnet 5.5, Haiku 5.5 och Haiku 4.5 via API:et, mätta den 18 oktober på
samma revision. Kolumnen ”Tät bevakningsartikel” kommer från testomgången den
4 och 5 september på en artikel med 589 rader, med undantag för Grok-raden, som ommättes den
9 september på en annan utgåva av samma bevakning, raderna för Antigravity och
Claude Code, mätta den 26 september på samma artikel, och dessa tre Claude-rader den 18 oktober. Fullständiga tabeller, tidsåtgång och testprotokoll finns
i [Detaljerade mätningar](#detaljerade-mätningar).

## Alla alternativ

| Alternativ               | Beskrivning                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Enskild Markdown-fil att översätta (alternativ till `--source_dir`)                                             |
| `--source_dir`           | Källkatalog som innehåller Markdown-filerna (standard: `content/posts`)                                   |
| `--target_dir`           | Utdatakatalog för de översatta filerna (standard: `traductions_en`)                                    |
| `--source_lang`          | Källspråk (standard: `fr`)                                                                                  |
| `--target_lang`          | Målspråk (standard: `en`)                                                                                   |
| `--model`                | Specifik modell att använda                                                                                  |
| `--eco`                  | Använd ekonomimodeller                                                                              |
| `--use_mistral`          | Använd Mistral AI:s API                                                                                     |
| `--use_claude`           | Använd Claude-API:et                                                                                         |
| `--use_gemini`           | Använd Gemini-API:et                                                                                         |
| `--use_grok`             | Använd xAI-API:et (Grok) — kräver `XAI_API_KEY`                                                           |
| `--use_codex`            | Använd Codex CLI via ChatGPT-prenumerationskvoten                                                    |
| `--use_grok_cli`         | Använd Grok CLI via Grok-prenumerationskvoten                                                        |
| `--use_antigravity`      | Använd Antigravity CLI (`agy`) via prenumerationskvoten för Google AI Pro eller Ultra                       |
| `--use_claude_code`      | Använd Claude Code CLI (`claude -p`) via prenumerationskvoten för Claude Pro eller Max                      |
| `--use_opencode`         | Använd OpenCode (öppen källkod) mot leverantören som konfigurerats i OpenCode; kräver `--model provider/modèle` |
| `--use_openrouter`       | Använd OpenRouter — kräver `OPENROUTER_API_KEY` och `--model fournisseur/modèle`                          |
| `--force`                | Tvinga omöversättning                                                                                       |
| `--keep_filename`        | Behåll det ursprungliga filnamnet                                                                          |
| `--news`                 | Nyhetsläge: skyddar EN-citat, hanterar flaggor per språk                                      |
| `--add_translation_note` | Lägg till en översättningsnotering                                                                                |
| `--note_position`        | Noteringens position: `top`, `bottom` (standard) eller `both`                                                     |
| `--note_format`          | Noteringens format: `legacy` (standard, stycke i fetstil) eller `marker`                                            |
| `--include_model`        | Inkludera modellnamnet i utdatafilen                                                            |
| `--reasoning_effort`     | Resonemangsinsats för GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

De nio `--use_*`-flaggorna är ömsesidigt uteslutande: att kombinera två
avvisas.

## Leverantörer

### Via API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` växlar till respektive leverantörs ekonominivå.

| Leverantör  | Kvalitet (standard)                                                  | Ekonomi (`--eco`) |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-6.1-terra`                                                      | `gpt-6-luna`              |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-4-hydrogen`                                                  | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (även `gpt-5.6-sol`, `terra` och `luna` via `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.7`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | samma sak — `--eco` har ingen effekt |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.8-flash-low`    |
| Claude Code | `sonnet`, insats `low`                                               | samma sak — `--eco` har ingen effekt |
| OpenCode    | `--model provider/modèle` obligatorisk                                | samma sak — `--eco` har ingen effekt |
| OpenRouter  | `--model fournisseur/modèle` obligatorisk                             | samma sak — `--eco` har ingen effekt |

Standardvärdena följer den senaste generationen från respektive leverantör,
uppmätt innan den antas: GPT-6 hos OpenAI, Gemini 4 Hydrogen hos Google,
Grok 4.7 hos xAI sedan 1.19.0. Tidigare modeller accepteras fortfarande
via `--model` (`gpt-5.6-terra`, `gemini-3.8-flash`, `grok-4.6`…), liksom
Gemini 4 Argon och Carbon, Googles toppskikt. aipmt justerar själv
resonemangsinsatsen för GPT och Grok, avstängd i `--eco`, och
`--reasoning_effort` tvingar den; en Gemini får alltid den lägsta nivån den
godkänner.
Ett tillfälligt avbrott i Gemini-API:et (503, 429, timeout) försöker utföra
anropet igen upp till tre gånger, efter 10, 20 och sedan 40 sekunder. Ett försök
som förblir obesvarat avbryts efter 5 minuter och startas sedan om på
samma sätt: en icke-svarande server gör att segmentet misslyckas efter högst ett
tjugotal minuter, istället för att blockera utan tidsgräns.

### Via ChatGPT-prenumerationen: `--use_codex`

Styr det officiella Codex CLI: översättningen dras från ChatGPT-prenumerationskvoten,
utan API-nyckel eller förbrukningsbaserad debitering.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Den binära filen söks i `CODEX_BIN`, därefter `PATH`, sedan paketet
  `openai-codex-cli-bin`. `~/.codex/auth.json` läses aldrig.
- `OPENAI_API_KEY` och `CODEX_API_KEY` tas bort från underprocessens
  miljö: en befintlig nyckel växlar aldrig över till API:et.
- Varje segment kostar minst ett ”meddelande” av 5-timmarsfönstret — två
  om valideringen misslyckas och det görs ett nytt försök. OpenAI anger som en
  uppskattning 250–2 000 meddelanden/5 timmar för `gpt-5.6-luna` (`--eco`) och
  10–100 för `gpt-5.6-sol` på ett Plus-abonnemang.
- `--model gpt-5.6-sol`, standard fram till 1.16.3, `--model gpt-5.6-terra`
  och `--model gpt-5.6-luna` fungerar också via prenumerationen.
- En 429-felkod från servern gör inte att filen går förlorad: Codex återansluter själv,
  aipmt väntar tills omgången är klar, och om felet 429 kvarstår startar segmentet
  om efter 30 och sedan 60 sekunder. En modell som kontot inte har tillgång till ger 400 ”model is
  not supported when using Codex with a ChatGPT account”.
- Långsammare än ett API, och skillnaden ökar med dokumentets storlek: för denna README tar det
  i median 6 min 46 s per språk med `gpt-5.6-sol`, jämfört med 36 s för
  `gemini-3.7-flash`.
- Avvisas i CI (`CI` eller `GITHUB_ACTIONS` angiven): prenumerationen autentiseras
  med en personlig sessionsfil, vilken inte hör hemma på en delad
  runner.
- Variabler: `CODEX_BIN`, `CODEX_TIMEOUT` (sekunder per segment, standard 600).

### Via Grok-prenumerationen: `--use_grok_cli`

Samma princip med det officiella verktyget Grok Build CLI, via SuperGrok- eller
X Premium+-prenumerationen.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Svagare isolering än Codex.** Groks operativsystemssandlåda fungerar inte
  på många nyare Linux-system (AppArmor, sockets för container-runtime),
  och en profil som inte kan tillämpas startar tyst utan isolering.
  Skriptet begär därför ingen profil som standard, meddelar detta och
  förlitar sig på CLI-verktygets `--deny`-regler, inklusive dess catch-all `*` — det enda
  lagret som vägrar starta hellre än att ta bort skyddet utan förvarning.
  `GROK_TRANSLATE_SANDBOX=read-only` kräver operativsystemssandlåda, och starten
  misslyckas om maskinen inte kan uppfylla det.
- Kvoten är veckovis, delad med Chat, Imagine och Voice, och det finns inget
  kommando för att läsa av den: en batchkörning kan förbruka konversationsanvändningen
  utan förvarning.
- Variabler: `GROK_BIN`, `GROK_HOME` (katalog för CLI, standard `~/.grok`),
  `GROK_TIMEOUT` (standard 900), `GROK_TRANSLATE_SANDBOX`.

### Via Google-prenumerationen: `--use_antigravity`

Samma princip med `agy`, det officiella Antigravity CLI: för dem som betalar för Google
AI Pro eller Ultra dras översättningen från prenumerationskvoten i stället
för att debiteras per token. Detta är det enda sättet att nå denna kvot: Gemini CLI betjänar
inte längre dessa konton sedan den 18 juni 2026
([meddelande](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
och Antigravitys SDK accepterar endast en API-nyckel eller ett Google Cloud-projekt.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Ingen betalväg lämnas öppen.** agy tar endast emot en sluten lista med variabler
  från din miljö — `PATH`, språk och tidszon,
  terminal, identitet, proxys och certifikat, sessionsbuss — och inga nycklar:
  flera av dess variabler växlar över ett anrop utan att visa något (uppmätt:
  en skickar dokumentet till en tredjeparts-gateway, en annan till ett debiterat
  Google Cloud-projekt), och en blockeringslista missade några vid varje granskning.
  Före varje segment måste `agy -p /config`, som inte förbrukar någon kvot, visa
  att betalda AI-krediter är inaktiverade, utan API-nyckel eller Google Cloud-projekt — en
  saknad inställning tolkas som avslag —, annars översätts ingenting; loggen för varje
  anrop måste därefter intyga prenumerationen (`authMethod=consumer`), annars
  avvisas svaret.
- **Isolering.** Varje anrop körs i en privat och temporär hemkatalog,
  med en verktygslös översättningsagent: dina inställningar, regler,
  insticksprogram, MCP-servrar och hooks för agy kommer inte in där, ingenting läggs till i din
  historik, och inloggningen stannar i nyckelringen, vilken aipmt aldrig läser.
  Om en agent inte hittas faller agy tyst tillbaka på sin kodningsagent
  och dess verktyg: en hel rad i loggen måste bekräfta rätt agent — ett
  dokument som citerar detta meddelande ersätter den inte —, annars avvisas körningen.
- **Plattformar**: Linux, i en session som har en nyckelring (D-Bus-sessionsbuss,
  Secret Service); macOS accepteras, men har inte mätts där. Avvisas
  under Windows, där agy inte läser variablerna som isolerar varje anrop, och
  under Linux utan sessionsbuss — SSH-session, container, server: agy sparar
  där sin token i en fil i `~/.gemini`, vilken isoleringen döljer.
  Avvisningen sker före varje start, tillsammans med orsaken, i stället för en minuts
  väntan på en inloggningskod.
- **Modeller**: de från `agy models`. Gemini-modellerna har insatsnivån i sitt namn
  (`gemini-3.8-flash-medium`…): ett namn utan suffix avvisas före anropet,
  och `--reasoning_effort` har ingen effekt. Som standard `gemini-3.8-flash-medium`,
  och `gemini-3.8-flash-low` i `--eco`, sedan agy inte längre tillhandahåller Gemini 3.7
  Flash; testkampanjen som fastställde standardvärdet beskrivs
  i [Detaljerade mätningar](#detaljerade-mätningar). Gemini 4 Hydrogen
  (`gemini-4-hydrogen-low`…) delar kvoten för 3.8 Flash och förbrukar
  mer av den: 0,95 poäng av 5-timmarsfönstret för denna README vid medelhög
  insats, jämfört med 0,32. Claude och GPT-OSS
  har en egen kvot som är mycket mindre: cirka 1 % av 5-timmarsfönstret
  per uppmätt anrop, jämfört med 0,05 % för Flash. Gemini 4 Argon har en
  egen, veckovis kvot: denna README förbrukar 1,35 % av den.
- **Kvot**: per grupp, ett 5-timmarsfönster och ett veckovis fönster, proportionellt
  mot kostnaden i tokens. Uppmätt på författarens konto: cirka
  16 poäng av 5-timmarsfönstret per miljon källtecken i
  `gemini-3.8-flash-medium`, 14 i `gemini-3.7-flash-medium` och 7 till 8 vid
  låg insats — en README på 40 000 tecken kostar därmed drygt en
  halv poäng. Veckogränsen beror i sin tur på nivån. Förnyade försök följer
  det som agy anger som möjligt att försöka igen; i annat fall görs aldrig nya
  försök om ett fönster är förbrukat: det gör att varje fil misslyckas fram till den återställning
  som visas av `/usage`.
- **Långsammare än API:et**: för den omfattande mätartikeln tar det i median 3 min 59 s per
  språk i `gemini-3.8-flash-medium` och 3 min 14 s i
  `gemini-3.7-flash-medium`, jämfört med 1 min 18 s för Gemini 3.7 Flash via API:et.
- **Avbrott**: Ctrl-C, eller en stängd terminal, stoppar agy tillsammans med
  kommandot i stället för att låta det slutföra sin omgång på din kvot; detsamma
  gäller för Codex, Grok CLI och OpenCode. Under `nohup` fortsätter översättningen.
- Avvisas i CI (`CI` eller `GITHUB_ACTIONS` angiven): inloggningen finns i en
  personlig nyckelring. På en runner används `--use_gemini` med `GOOGLE_API_KEY`.
- Variabler: `AGY_BIN` (annars `PATH`, därefter `~/.local/bin/agy`),
  `AGY_TIMEOUT` (sekunder per segment, inklusive uppstart, standard 900).

**Användarvillkor: det är ditt konto som berörs.** [Antigravitys användarvillkor](https://antigravity.google/terms) (avsnitt 6) och dess
[vanliga frågor](https://antigravity.google/docs/faq/) förbjuder åtkomst till tjänsten
via programvara från tredje part med hjälp av Antigravity-inloggningen — Claude Code,
OpenClaw och OpenCode nämns där —, med risk för att kontot stängs av. aipmt
varken läser eller återanvänder token: det kör den officiella binären i det
[headless-läge](https://antigravity.google/docs/cli/headless/) som Google
dokumenterar för skript och CI. En Google-medarbetare har bedömt det som ”standard”
att köra `agy -p` från ett lokalt skript för eget arbete
([officiellt forum, 25 september 2026, icke-bindande svar](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
ingen text ger ett definitivt svar gällande ett distribuerat verktyg som detta.

**Endast offentliga dokument.** Enligt avsnitt 5 i samma villkor kan
interaktioner — promptar, svar, metadata — användas för att förbättra Googles
produkter och maskininlärning samt granskas manuellt av
människor, även för betalda prenumerationer. Att välja bort detta görs via inställningen
`enableTelemetry`, vars effekt är odokumenterad och som aipmt inte konfigurerar; dina inställningar
för agy följer inte med i dess isolering. Skicka ingenting konfidentiellt genom detta.

### På Claude-abonnemanget: `--use_claude_code`

Samma princip med `claude`, Claude Codes officiella CLI, i läget `-p`: för
den som betalar för Claude Pro eller Max räknas översättningen av mot
abonnemangskvoten istället för att faktureras per token. Ska inte förväxlas med
`--use_claude`, Anthropics API, som faktureras efter användning.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Ingen betalväg förblir öppen, och varje anrop bevisar det.** Claude
  Code tar endast emot en sluten lista med variabler från din miljö — varken
  API-nyckel, token, molnleverantör eller markör för den Claude Code-session
  som aipmt startades från. Före det första segmentet måste `claude auth status` visa
  abonnemangsanslutningen, utan Console-nyckel, och `/usage`, som inte kostar
  någon kvot, måste intyga detta; varje anrop intygar det i sin tur i sin
  initieringshändelse, annars avvisas svaret.
- **Inaktivera "extra usage"** (claude.ai, Inställningar → Användning) för
  att nolleuron ska hålla: om det är aktiverat tar det över vid ett förbrukat fönster och
  fakturerar utan att visa något fel. aipmt stoppar översättningen så snart
  kvotrapporten från ett anrop signalerar detta, men det specifika anropet har redan räknats.
- **Kvot som delas med dina Claude Code-sessioner.** Varje anrop rapporterar
  användningen för 5-timmarsfönstren och veckan; över 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) startas inga fler segment, för att inte
  förbruka det som behövs till ditt arbete.
- **Isolering.** Varje anrop körs utan verktyg, i en privat och
  temporär katalog, i ett läge utan anpassningar: varken dina `CLAUDE.md`, dina tillägg,
  hooks, MCP-servrar eller inställningar läses in, och inget sparas från
  sessionen. Bilagor kopplas bort: en `@chemin` i ditt dokument
  förblir text och öppnar ingen fil (uppmätt).
- **Modeller**: `sonnet` som standard, med insatsen `low`, och i `--eco` likaså:
  `--eco` ändrar ingenting på denna väg. Uppmätt på samma dokument är `haiku`
  dubbelt så långsam — den resonerar utan att man kan förhindra det — till
  en knappt lägre kostnad, och `opus` avvisar biologiinnehåll (nästa
  punkt). Båda förblir tillgängliga via `--model`; dessa alias följer den
  senaste modellen i sin familj. `fable` och varianterna `[1m]` avvisas,
  eftersom de debiteras mot betalda krediter. `--reasoning_effort` justerar insatsen,
  vilket en översättning inte har någon nytta av: det uppmätta resonemanget är noll eller obefintligt.
- **Opus avvisar visst biologiinnehåll.** Dess skyddsbarriärer är
  striktare än Sonnets, och felmeddelandet från Anthropic varnar för att de
  "can sometimes flag biology-research-adjacent work". Uppmätt: en kort
  omvärldsbevakningsnotis om 279 genererade molekyler fick artikeln att avvisas på samtliga fjorton
  språk. Ingenting skrivs: aipmt avvisar det avbrutna svaret, pekar ut
  skyddsbarriärerna och rekommenderar `--model sonnet`.
- Avvisas i CI (`CI` eller `GITHUB_ACTIONS` definierad) och under Windows (ej uppmätt).
- Variabler: `AIPMT_CLAUDE_BIN` (annars `PATH`, därefter `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (sekunder per segment, standard 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (standard 0.8), `CLAUDE_CONFIG_DIR` (Claude
  Codes konto, hämtas aldrig från en `.env` i projektet); arbetskataloger under
  `XDG_CACHE_HOME/aipmt/claude-code` (standard `~/.cache`).

**Användarvillkor: det är ditt konto som är engagerat.** Den
[juridiska sidan för Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
hindrar inte "an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription": det är vad aipmt gör, som startar den
officiella binären och aldrig läser av tokenet. Men Anthropic "does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users", föredrar API-nyckeln för verktyg från
tredje part, "including open-source projects", och förbehåller sig rätten att räkna av deras
användning mot betalda krediter
([Claude-hjälp](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Ingen text avgör fallet med ett distribuerat verktyg som kör binären.

**Data**: för Free-, Pro- och Max-konton gäller modellträning
även Claude Code när sekretessinställningen tillåter det
([datasida](https://code.claude.com/docs/en/data-usage)). aipmt sparar
ingen lokal transkription (`--no-session-persistence`). Kör inte
något konfidentiellt genom detta.

### Till valfri leverantör: `--use_opencode`

[OpenCode](https://opencode.ai) är en öppen källkods-kodagent (MIT) som
dirigerar till de leverantörer som konfigurerats i den: API-nyckel, abonnemang,
OpenCode Zen-gateway (gratismodeller, utan konto) eller lokal modell. Två
vägar har mätts från början till slut här, Zen och Ollama.

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
vars utbyten kan användas för träning, och det valet görs inte i
ditt ställe.

Isolering vid varje anrop:

- en inline-konfiguration, prioriterad framför din, definierar en `aipmt`-agent
  där alla verktyg nekas (`permission: { "*": "deny" }`), sessionsdelning
  inaktiverad, `--pure`, aldrig `--auto`;
- temporär och tom arbetskatalog, `OPENCODE_DISABLE_PROJECT_CONFIG` och
  `OPENCODE_DISABLE_CLAUDE_CODE` placerade — utan dem injicerar OpenCode
  den aktuella katalogens `AGENTS.md` och `~/.claude/CLAUDE.md` i prompten. Den
  globala `~/.config/opencode/AGENTS.md` förblir injicerad, OpenCode tillåter inte
  att den utesluts;
- utdatakontrakt: returkod 0, ingen `error`-händelse, inget
  verktygsanrop, sista steget i `stop`, icke-tom text, och agenten `aipmt`
  faktiskt inläst — en okänd `--agent` gör inte att OpenCode misslyckas, den
  faller tyst tillbaka på kodningsagenten;
- ingen nyckel för `aipmt` skickas, förutom `OPENCODE_API_KEY`, själva
  OpenCodes nyckel. Leverantörer konfigureras i OpenCode, inte i
  `.env` för `aipmt`.

Värt att veta:

- De kostnadsfria modellerna i Zen är föränderliga, med odokumenterade gränser, och
  deras utbyten kan användas för träning: för publik dokumentation,
  inte för privat innehåll.
- En lokal modell måste erbjuda minst 16k tokens i kontext, då segmenten
  kan vara upp till 16 000 tecken. Ollama konfigurerar ofta 4 096: gå
  via en `Modelfile` med `PARAMETER num_ctx 32768`.
- `--eco` har ingen effekt; `--reasoning_effort` skickas vidare som den är som
  OpenCodes `--variant`.
- OpenCode loggar varje session i `~/.local/share/opencode/`.
- Variabler: `OPENCODE_BIN` (annars `PATH`, därefter `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (sekunder per segment, standard 600). `OPENCODE_CONFIG`
  skickas som den är till OpenCode.

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
modeller, och som en Modelfile inte kan stänga av. Uppmätt på en mening om
sex ord: 919 resonemangstokens och 68 sekunder utan flaggan, 9 tokens med.

### Till över 400 modeller: `--use_openrouter`

OpenRouter är en router som faktureras efter användning, mot en gemensam kredit, framför
modeller som hostas av tredje part — inklusive de öppna kinesiska modeller som ingen
annan leverantör tillhandahåller här.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` är obligatorisk. En preflight, som körs före all fakturering, hanterar
två särdrag i dirigeringen:

- **Samma modell tillhandahålls av dussintals värdar med olika
  gränser** — för `z-ai/glm-5.3-flash`, 23 värdar varav en med ett tak på
  2 048 utdatatokens. Preflight läser `/api/v1/models/{modèle}/endpoints`,
  utesluter värdar under 8 000 utdatatokens eller med degraderad status, och
  fäster de övriga med `allow_fallbacks: false`.
- **Resonemang faktureras till utdatatakt** — 107 tokens mot 2 för
  ett "OK"-svar från `z-ai/glm-5.2`. Det är avstängt som standard; de modeller
  som kräver det tilldelas den lägsta insats de accepterar, då katalogens
  standard kan mätta utdata innan översättningen är klar.
  `--reasoning_effort` prioriteras fortfarande.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Kontextfönstret hämtas från katalogen. En modell under 16 400 tokens
  avvisas före alla anrop: 8 400 för prompten och segmentet, minst 8 000
  i utdata.
- En slug som saknas i katalogen, en onåbar katalog eller avsaknad
  av värdar som klarar gränsen avbryter kommandot.
- `finish_reason=length` med tom utdata är en budget som förbrukats av
  resonemanget, inte en trunkering: meddelandet skiljer på detta.
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
följt av ett citat i fetstil: läsbart på GitHub, användbart vid byggprocessen för ett
remark-plugin.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detaljerade mätningar

Alla mätningar är faktiskt genomförda översättningar med `aipmt`, till
fjorton språk: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Skrivna** räknar de filer som kontrollerna släppte igenom; **Utan
avvikelse** de där `scripts/compare_structure.py` inte hittar något — samma antal
avsnitt, underrubriker, länkar, unika URL:er, kodblock,
inline-kod, tabellrader, blockcitat och ord i fetstil.

"Utan avvikelse" betyder "inget upptäckt", inte "identisk": jämföraren
räknar element utan att läsa deras innehåll. Den uppmärksammar varken en borttagen
rubrik på nivå 4, text i en inline-kod som bytts ut, en förväxlad flagga,
eller en intern länk som återgivits med en parentes för mycket,
`[texte]((#ancre))`, som inte längre leder någonstans — och den bedömer inte
språket.

### Tät omvärldsbevakningsartikel, läge `--news`

En utgåva av [AI-bevakningen på jls42.org](https://jls42.org/fr/news):
589 rader, 140 länkar, 21 avsnitt, 3 skyddade engelska citat. Testomgång
den 4 och 5 september 2026.

| Modell                                          | Åtkomst            | Skrivna | Utan avvikelse | Median/språk   |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google-abonnemang  | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google-abonnemang  | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `claude-sonnet-5-5`                             | Anthropic API      | 14/14   | ✅ **14/14** | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT-abonnemang | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | Claude-abonnemang  | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | Claude-abonnemang  | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `claude-haiku-5-5`                              | Anthropic API      | 14/14   | ⚠️ 11/14     | 2 min 54 s     |
| `claude-haiku-4-5`                              | Anthropic API      | 14/14   | ⚠️ 7/14      | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | lokalt             | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok-abonnemang    | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | Claude-abonnemang  | 0/14    | ❌ 0/14      | —              |

Grok mättes på nytt den 9 september på en annan utgåva av samma bevakning
(356 rader): 9 skrivna språk av 14, 8 utan avvikelse. Det är denna siffra som
visas i tabellen överst. Tre avbrutna kampanjer tas inte
med: `qwen3.5-27b` (9 språk) och `kimi-k2.6` (4) i brist på krediter,
`z-ai/glm-5.3-flash` vars två misslyckanden berodde på en resonemangsinställning
som leverantören sedan dess åtgärdat. Raderna för OpenRouter mättes med
routerns standardinställningar, före `--use_openrouter`; `z-ai/glm-5.2`,
som mättes om med den levererade providern, ger samma 14/14. Siffrorna
beräknades om den 10 september med den nuvarande jämföraren: `qwen3.8-flash` och
`qwen3.7-flash` får vardera ett extra språk jämfört med den första
publiceringen, de övriga är oförändrade.

Raderna för `--use_antigravity` mättes den 26 september på samma
artikel, fyra parallella översättningar: `gemini-3.7-flash-medium` på morgonen,
`gemini-3.8-flash-medium` på eftermiddagen. På engelska tog båda själva bort
de tre raderna med fransk översättning under citaten, utan att hitta på någon
flagga, och de engelska citaten förblev intakta: reservrensningen behövde
inte göra något. I `--eco` (`gemini-3.7-flash-low`), på endast fyra språk
(en, ja, ar, hi): 4 skrivna av 4, samtliga utan avvikelse, 1 min 52 s i
median. Motprov samma dag på en nyare utgåva av bevakningen,
den från den 25 september (438 rader, 2 engelska citat), översatt utanför
bloggen med `gemini-3.7-flash-medium`: 14 skrivna av 14, samtliga utan avvikelse, 87 till
128 s per språk.

Raderna för `--use_claude_code` mättes den 26 september på samma
artikel, fyra parallella översättningar, med insatsen `low`. Med `sonnet` är de
engelska citaten intakta på de fjorton språken och på engelska tog
modellen själv bort de franska översättningsraderna, utan att hitta på någon
flagga. `opus` skrev inte något språk: på samtliga stoppade dess skyddsbarriärer
svaret vid det sista segmentet, på grund av en notis om 279 molekyler
genererade för ett bindningsställe. Skickad ensam avvisas denna notis under
kategorin "bio"; `sonnet` översatte den överallt. `haiku` skriver
de fjorton språken; på tre (en, pl, ro) ändras en avsnittsrubrik från
nivå 2 till nivå 1. Den resonerar utan att det går att förhindra — 61 % av
dess utdatatokens —, därav mer än dubbla tidsåtgången jämfört med `sonnet`.

Raderna för `claude-sonnet-5-5`, `claude-haiku-5-5` och `claude-haiku-4-5` mättes
den 18 oktober via Anthropics API, på samma artikel, fyra
översättningar parallellt per modell. Sonnet 5.5 tillåter inte att man stänger av dess
reflektion: aipmt skickar den lägsta inställning den accepterar, och dess
svar innehåller inga spår av den. Den skriver de fjorton språken utan avvikelse och utan
att behöva köra om något segment; på engelska tog den själv bort de franska
översättningsraderna, utan att hitta på någon flagga, och de engelska citaten är
intakta överallt. Haiku 5.5 mäts med sin adaptiva reflektion: med reflektionen
avstängd lämnade den hela stycken på franska, vilket spärren avvisar —
3 skrivna språk av 14. Båda Haiku snubblar på samma notis: Haiku 5.5
ändrar nivån på dess rubrik eller dubblerar den på japanska, koreanska och
kinesiska, Haiku 4.5 ändrar den till nivå 1 på sju språk, och lämnar den på
franska på japanska. Haiku 4.5 kostar 3,67 $ för de två dokumenten på de
fjorton språken, Haiku 5.5 0,57 $, Sonnet 5.5 9,21 $.

### Detta projekts README, standard-Markdown

Låst revision den 9 september 2026: 785 rader, 285 inline-koder, 40
blockavslutningar, 89 tabellrader. Fyra översättningar parallellt.

| Modell                                          | Skrivna | Utan avvikelse | Median/språk | Vad som skiljer                                                           |
| ----------------------------------------------- | ------- | -------------- | ------------ | ------------------------------------------------------------------------- |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | inget                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | inget                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | inget för jämförelseverktyget; duplicerade interna länkar (en)            |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | inget                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | inget                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | ett ord i fetstil (ja)                                                    |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | ett ord i fetstil (ko)                                                    |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | en tabellrad sammanfogad med föregående (ar)                              |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | en länk (sv), ett ord i fetstil (zh)                                      |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | ett ord i fetstil (ar, ja)                                                |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | ett ord i fetstil (hi, ja, ko)                                            |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 40 inline-koder tillagda på arabiska; fetstil (hi, ja, ko)                 |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2 nekade språk (ar, hi): förlorade inline-koder i svaret                  |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | en sektion förlorad (ar, hi, ko); kodblock tillagda (ja, ko, ro, zh)      |

Två avbrutna kampanjer finns inte med i tabellen: Grok, CLI-sessionen gick ut
efter tolv språk (elva utan avvikelse), och `qwen3.8-flash`, HTTP 429 från sin
värd efter två. `opencode/mimo-v2.5-free` och `ollama/gpt-oss-20b-32k`
mättes inte om på denna revision; på den från 4 och 5 september,
som var 277 rader kortare, skrev de vardera 9 översättningar av 14, varav 7
och 1 utan avvikelse.

Raderna `--use_antigravity` och `--use_claude_code` mättes inte på
den låsta revisionen, utan den 26 september på den som publicerades med 1.14.0 — och
raderna `claude-sonnet-5-5`, `claude-haiku-5-5` och `claude-haiku-4-5` den 18
oktober, på samma: 600 rader, 257 inline-koder, 30 blockavslutningar, 85
tabellrader. Eftersom den är
185 rader kortare kan den inte jämföras rakt av med de andra raderna;
däremot kan dessa rader jämföras med varandra. Vad gäller interna länkar, som
jämförelseverktyget inte kontrollerar, behöll `gemini-3.8-flash-medium` dem intakta på
de fjorton språken, medan `gemini-3.7-flash-medium` bröt dem på italienska;
`sonnet` och `opus` behöll dem intakta överallt, `haiku` duplicerade dem på
engelska; `claude-sonnet-5-5` och `claude-haiku-4-5` behöll dem intakta på
de fjorton språken, `claude-haiku-5-5` på de tolv den skrev.

### Fyra README från välkända projekt

FastAPI, Ollama, tldr-pages och Vue.js, tagna rakt av från GitHub — enklare
dokument än de två föregående. Kampanjen riktade sig mot modeller
med svårigheter; Gemini fungerar som referenspunkt.

| Modell                    | Omfattning                 | Skrivna | Utan avvikelse |
| ------------------------- | -------------------------- | ------- | -------------- |
| `gemini-3.7-flash`        | 4 projekt × 14 språk       | 56/56   | ✅ **55/56**   |
| `opencode/mimo-v2.5-free` | 4 projekt × 14 språk       | 55/56   | ❌ 47/56       |
| `grok-4.6` (prenumeration)   | 4 projekt × ar, hi, ja, zh | 16/16   | ❌ 14/16       |
| `ollama/gpt-oss-20b-32k`  | 4 projekt × ar, hi, ja, zh | 15/16   | ❌ 9/16        |

### Vad dessa mätningar inte är

- **Ingen uttömmande rankning**: OpenRouter enbart erbjuder över fyra hundra
  modeller, ett femtontal har mätts.
- **Ungefärliga tidsangivelser**: tre till sex parallella översättningar beroende på
  kampanj, och en leverantörs genomströmning varierar under dagen.
- **Daterade observationer**: modeller förändras under samma namn, och era
  dokument är inte våra.

För att upprepa mätningen på era dokument, på en låst kopia av filen:

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
`No module named aipmt`.

Kvalitetsverktyg, valfria men rekommenderade:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Förrådets 28 översättningar (README och CHANGELOG, fjorton språk)
återskapas med `./regen_translations.sh --force` — Codex och `gpt-6.1-sol` via
ChatGPT-prenumerationen som standard, fyra parallellt. `REGEN_PROVIDER` och
`REGEN_MODEL` ändrar sökvägen: `antigravity` stannar kvar på en prenumeration, Googles,
och passerar utan undantag; ett fakturerat API (`openai`, `gemini`,
`grok`, `openrouter`) nekas utan `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` sätter ett tak för varje körning (600 s, 1 800 s för Codex och
Antigravity). Närmare information om verktygen finns i `CLAUDE.md`.

## Projekt som använder detta skript

- **[jls42.org](https://jls42.org)** — personlig blogg publicerad på 15 språk. Dess
  [dagliga AI-bevakning](https://jls42.org/fr/news) översätts varje dag
  med detta verktyg och fungerar som referensdokument för mätningarna ovan.

## Författare

Julien LE SAUX
E-post: contact@jls42.org

## Licens

GNU GENERAL PUBLIC LICENSE version 3. Se [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Varning

Detta program distribueras **helt utan garantier**, i enlighet med villkoren i
avsnitt 15 och 16 i GPL v3: tillhandahålls i "befintligt skick", utan garanti för säljbarhet
eller lämplighet för ett visst syfte, och dess författare kan inte hållas
ansvarig för skador som uppstår till följd av dess användning. Licenstexten har
företräde framför denna sammanfattning.

- **Läs igenom innan publicering.** Skydden omfattar kodblock,
  inline-kod, webbadresser, ankare och citat i läget `--news` — varken
  rubriker, tabeller, front matter eller innebörden i dina meningar.
- **Dina dokument skickas till den valda leverantören**, under dennes användarvillkor
  och datapolicy. Vissa gratismodeller kan återanvända dina konversationer
  för träning, och Antigravitys villkor tillåter Google att återanvända dem och
  låta människor granska dem, även med betalprenumeration; en lokal modell är den enda
  vägen som inte låter några data lämna din dator.
- **API-anrop debiteras dig.** Detta program sätter inget tak för
  kostnaderna: ett långt dokument, återupptagning efter fel eller en modell som resonerar
  mycket kostar mer.
- **De publicerade mätningarna är daterade observationer**, inte garantier.

Produkt- och företagsnamn som nämns tillhör sina respektive innehavare.
Detta projekt är inte anslutet till någon av dem.

**Artikel översatt från fr till sv med gemini-3.8-flash-medium.**

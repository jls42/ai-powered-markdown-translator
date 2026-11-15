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

Översätter Markdown-filer från ett språk till ett annat och bevarar
strukturen: kodblock, inline-kod, URL:er, ankare, tabeller och front
matter. Elva sätt att anropa en modell — fem API:er, fyra prenumerationer utan
användningsbaserad debitering, två routrar — och ett publicerat mått på vad varje
modell faktiskt bevarar.

## I korthet

- **Elva provider-vägar**: OpenAI-, Mistral-, Claude-, Gemini- och Grok-API:er;
  ChatGPT- (Codex), Grok-, Google- (Antigravity) och Claude-prenumerationer (Claude
  Code) utan användningsbaserad debitering; OpenCode-routrar (öppen källkod, gratis eller lokal) och OpenRouter
  (över 400 modeller).
- **Inget felaktigt på grund av en förlorad token**: kodblock, inline-kod,
  URL:er, ankare och citat ersätts med tokens före anropet och
  verifieras vid returen. Om en saknas skrivs inte filen.
- **Långa dokument**: segmentering utifrån modellens fönster.
- **`--news`-läge**: skyddade engelska citat och flaggor hanterade per
  språk, för omvärldsbevakningsartiklar.
- **`--eco`-läge**: snabba och billigare modeller.
- **Valfri översättningsnot**, överst, nederst eller på båda ställena.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11 eller senare. För att installera från arkivet, se
[Bidra](#bidra).

## Konfiguration

Nycklar läses från tre platser, från högst till lägst prioritet; varje plats
fyller bara i det som föregående lämnar tomt.

|     | Var                                           | För vad                               |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Miljövariabler                                | CI, containrar, enstaka undantag      |
| 2   | `.env` i aktuell katalog (eller överordnad) | en nyckel specifik för ett projekt    |
| 3   | `~/.config/aipmt/.env`                                 | installerad en gång, gäller överallt  |

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

**Ett projekts `.env` kan varken omdirigera anrop eller välja vilket program som
körs.** Den tillhandahåller nycklar, aldrig en destination eller en binär: alla
variabler med `_BASE_URL`, `_API_BASE`, `_ENDPOINT` eller `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, proxyservrar (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), certifikatarkiv (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) och `XDG_CONFIG_HOME` /
`APPDATA` ignoreras där, med en varning. Ett klonat arkiv får inte
kunna kapa din nyckel eller få dig att starta dess eget program vid
den första översättningen. Denna fil läses också utan interpolering:
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
med `--include_model`, `document-es-gpt-6.1-terra.md`. Filtillägget blir
alltid `.md` — `article.mdx` ger `article-en.md` — utom med
`--keep_filename`, som behåller ursprungsnamnet. En översättning som redan finns
hoppas över utan `--force`.

Slutkoder: `0` om allt lyckades eller hoppades över, `1` om det finns någon fil
som misslyckades (lista på standard error), `2` om konfigurationen är felaktig.
En fil som misslyckas skrivs aldrig, även om själva skrivningen misslyckas:
innehållet skrivs vid sidan om och byter sedan namn. Det räcker att köra igen.

## Vilken modell ska man välja

Mätt på två verkliga dokument, översatta till samma fjorton språk av
respektive modell. **Siffran anger antalet språk, av fjorton, där
översättningen skrivs och där ingenting skiljer sig från källan.**

| Modell                | Hur man får åtkomst               | Tät bevakningsartikel   | Denna README | Vad som skiljer sig, och på hur många språk                                                                                                                        |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google-prenumeration (Antigravity)| ✅ 14/14                | ✅ 14/14     | inget, i något av de två dokumenten                                                                                                                                |
| **Claude Sonnet 5.5** | Anthropic API-nyckel              | ✅ 14/14                | ✅ 14/14     | inget, i något av de två dokumenten                                                                                                                                |
| **Gemini 3.7 Flash**  | Google API-nyckel                 | ✅ 14/14                | ⚠️ 13/14     | 1 språk av 14: ett extra fetstilt ord (ja)                                                                                                                         |
| **Gemini 3.7 Flash**  | Google-prenumeration (Antigravity)| ✅ 14/14                | ⚠️ 13/14     | 1 språk av 14: ett fetstilt ord mindre (ko)                                                                                                                        |
| **GPT-5.6 Sol**       | ChatGPT-prenumeration, eller OpenAI-nyckel | ✅ 14/14       | ⚠️ 12/14     | 2 språk av 14: ett fetstilt ord mindre (ar, ja)                                                                                                                    |
| **GLM-5.2**           | OpenRouter-nyckel                 | ✅ 14/14                | ⚠️ 11/14     | 3 språk av 14: ett fetstilt ord mindre (hi, ja, ko)                                                                                                                |
| Claude Sonnet 5       | Claude-prenumeration (Claude Code)| ⚠️ 13/14                | ⚠️ 13/14     | 1 språk av 14 i artikeln: ett extra fetstilt ord (zh); 1 i denna README: en tabellrad sammanfogad med föregående, dold vid visning (ar)                          |
| Claude Haiku 4.5      | Claude-prenumeration (Claude Code)| ⚠️ 11/14                | ✅ 14/14     | 3 språk i artikeln: en avsnittsrubrik ändrad till nivå 1 (en, pl, ro); i denna README, inget för jämförelsen, men interna länkar duplicerade på engelska           |
| Claude Sonnet 5       | Anthropic API-nyckel              | ⚠️ 11/14                | ⚠️ 12/14     | 3 språk i artikeln: ett kodblock dök upp (es, de, hi); 2 i denna README: en länk utan dess formatering (sv), ett fetstilt ord (zh)                               |
| Claude Haiku 4.5      | Anthropic API-nyckel              | ⚠️ 7/14                 | ✅ 14/14     | 7 språk i artikeln: en avsnittsrubrik ändrad till nivå 1 — på japanska, kvar på franska; inget i denna README                                                      |
| Claude Haiku 5.5      | Anthropic API-nyckel              | ⚠️ 11/14                | ❌ 12/14     | 3 språk i artikeln: en avsnittsrubrik ändrade nivå eller duplicerades (ja, ko, zh); i denna README, 2 nekade språk, förlorad inline-kod (ar, hi)                   |
| Qwen 3.7 Flash        | OpenRouter-nyckel                 | ❌ 8/14                 | ⚠️ 10/14     | 1 nekat språk i artikeln, 5 andra avviker; i denna README, ett fyrtiotal ord satta i `code` (ar)                                                          |
| Grok 4.6              | Grok-prenumeration                | ❌ 8/14                 | ej betygsatt | 5 nekade språk av 14, i brist på återgivna inline-koder och URL:er; nederländska avviker i allt                                                                    |
| GPT-OSS 20B           | lokal modell (Ollama)             | ❌ 7/14                 | ej ommätt    | 4 nekade språk av 14: modellen lämnade stycken på franska, spärren stoppade dem                                                                                    |
| MiMo v2.5 (gratis)    | OpenCode Zen, utan konto          | ❌ 11/14                | ej ommätt    | 1 nekat språk; ett förlorat avsnitt på polska                                                                                                                      |
| Mistral Large         | Mistral API-nyckel                | ❌ 5/14                 | ❌ 1/14      | **ett helt avsnitt försvinner**: 1 språk i artikeln (hi), 3 i denna README (ar, hi, ko) — och 3 nekade språk i artikeln                                            |
| DeepSeek V4 Flash     | OpenRouter-nyckel                 | ❌ 3/14                 | ej ommätt    | 10 nekade språk av 14; 37 minuter per språk                                                                                                                        |
| Claude Opus 5.5       | Claude-prenumeration (Claude Code)| ❌ 0/14                 | ✅ 14/14     | artikeln nekad på alla 14 språk av skyddsspärrarna i Opus, på grund av en biologinotiss; inget i denna README                                                      |

|     | Vad symbolen betyder                                                                                                                                                                                  |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alla fjorton språk översatta, och ingenting skiljer sig från källan                                                                                                                                   |
| ⚠️  | alla fjorton språk översatta; det som skiljer sig är **formatering** — ett fetstilt ord, en `code`, en länk som förlorar sina hakparenteser. Ingen text, ingen URL, inget kodblock, inget avsnitt saknas |
| ❌  | minst ett språk kunde inte översättas — filen nekades, skrevs inte — **eller** innehåll saknas i en skriven fil                                                                                       |

Vad man bör ta med sig:

- **En nekad översättning är inte en skadad översättning.** När en token
  saknas vid retur skrivs filen inte och språket räknas som
  nekat. Det är vad som händer Grok i artikeln: fyra inline-koder och
  tre URL:er förlorade redan i det första segmentet, i de fem icke-latinska skriftsystemen.
- **En modell kan neka ett helt dokument på grund av en enda mening.** Opus 5.5
  översätter denna README utan en enda avvikelse, men inte en enda bevakningsartikel: dess
  skyddsspärrar stoppar svaret vid en biologinotiss. Filen skrivs
  inte, och aipmt talar om varför.
- **Detta skyddsnät täcker inte rubriker, tabeller, front matter eller
  text.** En modell som raderar ett avsnitt returnerar en fil som verktyget skriver
  utan att blinka — så är fallet med Mistral. Dessa element kan inte
  ersättas med en token, och de nuvarande skydden kontrollerar dem inte;
  `scripts/compare_structure.py` upptäcker ett förlorat avsnitt, men i efterhand.
- **Grok har inget betyg på denna README**: dess CLI-session löpte ut efter tolv
  språk, varav elva utan avvikelse. En avbruten körning betygsätts inte.
- **Dokumentets täthet spelar större roll än språket.** Grok klarar
  vanliga README-filer men tappar taget på en artikel full av länkar, även på
  nederländska.

Datum och dokument: kolumnen ”Denna README” mättes den 9 september 2026
på en låst revision av denna fil (785 rader, 285 inline-koder, 89 tabellrader),
som ändrats sedan dess — förutom raderna Antigravity och Claude Code,
som mättes den 26 september på revisionen publicerad med 1.14.0, som var kortare
(600 rader, 257 inline-koder, 85 tabellrader), och raderna Claude
Sonnet 5.5, Haiku 5.5 och Haiku 4.5 via API, mätta den 18 oktober på
samma revision. Kolumnen ”Tät bevakningsartikel” kommer från körningen den
4 och 5 september på en artikel med 589 rader, förutom raden Grok, som ommättes den
9 september på en annan utgåva av samma bevakning, raderna Antigravity och
Claude Code, mätta den 26 september på samma artikel, och dessa tre Claude-rader
den 18 oktober. Fullständiga tabeller, tider och protokoll finns
i [Detaljerade mätningar](#detaljerade-mätningar).

## Alla alternativ

| Alternativ               | Beskrivning                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Enskild Markdown-fil att översätta (alternativ till `--source_dir`)                                             |
| `--source_dir`           | Källkatalog som innehåller Markdown-filerna (standard: `content/posts`)                                   |
| `--target_dir`           | Utdatakatalog för översatta filer (standard: `traductions_en`)                                    |
| `--source_lang`          | Källspråk (standard: `fr`)                                                                                  |
| `--target_lang`          | Målspråk (standard: `en`)                                                                                   |
| `--model`                | Specifik modell att använda                                                                                  |
| `--eco`                  | Använd budgetmodeller                                                                              |
| `--use_mistral`          | Använd Mistral AI-API:et                                                                                     |
| `--use_claude`           | Använd Claude-API:et                                                                                         |
| `--use_gemini`           | Använd Gemini-API:et                                                                                         |
| `--use_grok`             | Använd xAI (Grok)-API:et — kräver `XAI_API_KEY`                                                           |
| `--use_codex`            | Använd Codex CLI på kvoten för ChatGPT-prenumerationen                                                    |
| `--use_grok_cli`         | Använd Grok CLI på kvoten för Grok-prenumerationen                                                        |
| `--use_antigravity`      | Använd Antigravity CLI (`agy`) på kvoten för Google AI Pro- eller Ultra-prenumerationen                       |
| `--use_claude_code`      | Använd Claude Code CLI (`claude -p`) på kvoten för Claude Pro- eller Max-prenumerationen                      |
| `--use_opencode`         | Använd OpenCode (öppen källkod) mot leverantören konfigurerad i OpenCode; kräver `--model provider/modèle` |
| `--use_openrouter`       | Använd OpenRouter — kräver `OPENROUTER_API_KEY` och `--model fournisseur/modèle`                          |
| `--force`                | Tvinga återöversättning                                                                                       |
| `--keep_filename`        | Behåll det ursprungliga filnamnet                                                                          |
| `--news`                 | Nyhetsläge: skyddar engelska citat, hanterar flaggor per språk                                      |
| `--add_translation_note` | Lägg till en översättningsnotis                                                                                |
| `--note_position`        | Notisens placering: `top`, `bottom` (standard), eller `both`                                                     |
| `--note_format`          | Notisens format: `legacy` (standard, stycke i fetstil) eller `marker`                                            |
| `--include_model`        | Inkludera modellnamnet i utdatafilen                                                            |
| `--reasoning_effort`     | GPT-5.x-resoneringsinsats: `none`/`low`/`medium`/`high`/`xhigh`                                         |

De nio flaggorna `--use_*` utesluter varandra: att kombinera två av dem
nekas.

## Leverantörer

### Via API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` växlar till varje leverantörs budgetnivå.

| Leverantör    | Kvalitet (standard)                                                     | Budget (`--eco`)      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-6.1-terra`                                                      | `gpt-6-luna`              |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-4-hydrogen`                                                  | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (även `gpt-5.6-sol`, `terra` och `luna` via `--model`) | `gpt-6-luna`              |
| Grok API    | `grok-4.7`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | samma — `--eco` saknar effekt |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.8-flash-low`    |
| Claude Code | `sonnet`, insats `low`                                               | samma — `--eco` saknar effekt |
| OpenCode    | `--model provider/modèle` obligatorisk                                | samma — `--eco` saknar effekt |
| OpenRouter  | `--model fournisseur/modèle` obligatorisk                             | samma — `--eco` saknar effekt |

Standardvalen följer den senaste generationen från varje leverantör, uppmätt
innan den antas: GPT-6 hos OpenAI, Gemini 4 Hydrogen hos Google,
Grok 4.7 hos xAI sedan 1.19.0. Tidigare modeller accepteras fortfarande
via `--model` (`gpt-5.6-terra`, `gemini-3.8-flash`, `grok-4.6`…), liksom
Gemini 4 Argon och Carbon, Googles toppskikt. aipmt justerar själv
resoneringsinsatsen för GPT och Grok, avstängd i `--eco`, och
`--reasoning_effort` tvingar den; en Gemini får alltid den lägsta nivån
den accepterar.
Ett tillfälligt fel i Gemini-API:et (503, 429, timeout) gör att
anropet försöks igen upp till tre gånger, efter 10, 20 och sedan 40 sekunder. Ett försök
som förblir obesvarat avbryts efter 5 minuter och startas sedan om
på samma sätt: en icke-svarande server gör att segmentet misslyckas efter som mest
ett tjugotal minuter, i stället för att blockera i all oändlighet.

### På ChatGPT-prenumerationen: `--use_codex`

Styr officiella Codex CLI: översättningen dras från kvoten för
ChatGPT-prenumerationen, utan API-nyckel eller användningsbaserad debitering.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Den binära filen söks i `CODEX_BIN`, sedan i `PATH`, därefter i paketet
  `openai-codex-cli-bin`. `~/.codex/auth.json` läses aldrig.
- `OPENAI_API_KEY` och `CODEX_API_KEY` tas bort från underprocessens
  miljö: en befintlig nyckel leder aldrig till att det växlas över till API:et.
- Varje segment kostar minst ett "meddelande" från 5-timmarsfönstret — två
  om dess validering misslyckas och ett nytt försök görs. OpenAI anger, som en
  uppskattning, 250–2 000 meddelanden/5 h för `gpt-5.6-luna`, budgetmodellen fram till
  1.18.0, och 10–100 för `gpt-5.6-sol` på en Plus-plan.
- `--model gpt-5.6-sol`, standardvalet fram till 1.16.3, `--model gpt-5.6-terra`
  och `--model gpt-5.6-luna` går också via prenumerationen.
- En 429 från servern gör inte att filen förloras: Codex återansluter på egen hand,
  aipmt väntar tills omgången är klar, och om felet 429 kvarstår startas segmentet
  om efter 30 och sedan 60 sekunder. En modell som kontot saknar behörighet till returnerar en 400 "model is
  not supported when using Codex with a ChatGPT account".
- Långsammare än ett API, och skillnaden ökar med dokumentets storlek: på denna README är
  medianen 6 min 46 s per språk med `gpt-5.6-sol`, jämfört med 36 s för
  `gemini-3.7-flash`.
- Nekas i CI (om `CI` eller `GITHUB_ACTIONS` är definierad): prenumerationen autentiseras
  med en personlig sessionsfil, som inte har på en delad runner
  att göra.
- Variabler: `CODEX_BIN`, `CODEX_TIMEOUT` (sekunder per segment, standard 600).

### På Grok-prenumerationen: `--use_grok_cli`

Samma princip med officiella Grok Build CLI, på SuperGrok- eller
X Premium+-prenumerationen.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Svagare isolering än Codex.** Groks OS-sandlåda kan inte tillämpas
  på många moderna Linux-system (AppArmor, sockets för container-runtime),
  och en profil som inte kan tillämpas startar oisolerad i
  tysthet. Skriptet begär därför ingen profil som standard, meddelar detta och
  förlitar sig på CLI:ets `--deny`-regler, inklusive catch-all `*` — det enda
  lagret som vägrar starta i stället för att ta bort skyddet utan förvarning.
  `GROK_TRANSLATE_SANDBOX=read-only` kräver OS-sandlådan, och starten
  misslyckas om maskinen inte kan uppfylla kravet.
- Kvoten är veckobaserad, delad med Chat, Imagine och Voice, och det finns ingen
  kommando för att läsa av den: en batchkörning kan tära på samtalsanvändningen
  utan förvarning.
- Variabler: `GROK_BIN`, `GROK_HOME` (katalog för CLI, standard `~/.grok`),
  `GROK_TIMEOUT` (standard 900), `GROK_TRANSLATE_SANDBOX`.

### På Google-prenumerationen: `--use_antigravity`

Samma princip med `agy`, Antigravitys officiella CLI: för den som betalar för Google
AI Pro eller Ultra dras översättningen från prenumerationskvoten i stället
för att debiteras per token. Det är den enda vägen till denna kvot: Gemini CLI
betjänar inte längre dessa konton sedan den 18 juni 2026
([tillkännagivande](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
och Antigravity-SDK:et accepterar endast en API-nyckel eller ett Google Cloud-projekt.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Inga betalvägar lämnas öppna.** agy tar endast emot en sluten lista med
  variabler från din miljö — `PATH`, språk och tidszon,
  terminal, identitet, proxyer och certifikat, sessionsbuss — och inga nycklar:
  flera av dess variabler växlar över ett anrop utan att visa något (uppmätt:
  en skickar dokumentet till en tredjepartsgateway, en annan till ett fakturerat
  Google Cloud-projekt), och en blockeringslista missade alltid någon vid varje genomgång.
  Före varje segment måste `agy -p /config`, som inte förbrukar någon kvot, visa
  att betalda AI-krediter är inaktiverade, utan API-nyckel eller Google Cloud-projekt — en
  inställning som saknas betraktas som ett avslag —, annars översätts ingenting; loggen för varje
  anrop måste sedan intyga prenumerationen (`authMethod=consumer`), annars
  nekas svaret.
- **Isolering.** Varje anrop körs i en privat och
  temporär hemkatalog, med en översättningsagent utan verktyg: dina inställningar, regler,
  insticksprogram, MCP-servrar och agy-krokar når inte dit, inget läggs till i din
  historik, och inloggningen stannar i nyckelringen, som aipmt aldrig läser.
  Om en agent inte hittas faller agy i tysthet tillbaka på sin kodningsagent
  och dess verktyg: en hel rad i loggen måste bekräfta rätt agent — ett
  dokument som citerar detta meddelande ersätter den inte —, annars nekas det.
- **Plattformar**: Linux, i en session med en nyckelring (D-Bus-sessionsbuss,
  Secret Service); macOS accepteras, men har inte mätts där. Nekas
  under Windows, där agy inte läser de variabler som isolerar varje anrop, och
  under Linux utan sessionsbuss — SSH-session, container, server: agy sparar
  där sin token i en fil i `~/.gemini`, vilket döljs av isoleringen.
  Avslaget sker före varje start, tillsammans med orsaken, i stället för att
  vänta en minut på en inloggningskod.
- **Modeller**: de från `agy models`. Gemini-modellerna bär insatsnivån i sitt namn
  (`gemini-3.8-flash-medium`…): ett namn utan suffix nekas före anropet,
  och `--reasoning_effort` saknar effekt. Som standard `gemini-3.8-flash-medium`,
  och `gemini-3.8-flash-low` i `--eco`, sedan agy inte längre tillhandahåller Gemini 3.7
  Flash; testkampanjen som fastställde standardvalet
  beskrivs i [Detaljerade mätningar](#detaljerade-mätningar). Gemini 4 Hydrogen
  (`gemini-4-hydrogen-low`…) delar kvoten med 3.8 Flash och förbrukar
  mer: 0,95 poäng från 5-timmarsfönstret för denna README vid medelhög
  insats, jämfört med 0,32. Claude och GPT-OSS
  har en egen, betydligt mindre kvot: cirka 1 % av 5-timmarsfönstret
  per uppmätt anrop, jämfört med 0,05 % för Flash. Gemini 4 Argon har en
  egen, veckobaserad kvot: denna README förbrukar 1,35 % av den.
- **Kvot**: per grupp, ett 5-timmarsfönster och ett veckobaserat, i
  proportion till tokenkostnaden. Uppmätt på författarens konto: cirka
  16 poäng från 5-timmarsfönstret per miljon källtecken i
  `gemini-3.8-flash-medium`, 14 i `gemini-3.7-flash-medium` och 7 till 8 vid
  låg insats — en README på 40 000 tecken kostar alltså drygt en
  halv poäng. Veckogränsen beror i sin tur på nivån. Återförsök följer
  vad agy deklarerar som återförsöksbart; i annat fall görs aldrig nya försök om
  ett fönster är förbrukat: det leder till att varje fil misslyckas fram till den
  återställning som visas av `/usage`.
- **Långsammare än API:et**: på den kompakta mätartikeln, 3 min 59 s per
  språk i median med `gemini-3.8-flash-medium` och 3 min 14 s med
  `gemini-3.7-flash-medium`, jämfört med 1 min 18 s för Gemini 3.7 Flash via API:et.
- **Avbrott**: Ctrl-C, eller en stängd terminal, stoppar agy tillsammans med
  kommandot i stället för att låta det slutföra sin omgång på din kvot; detsamma
  gäller för Codex, Grok CLI och OpenCode. Under `nohup` fortsätter översättningen.
- Nekas i CI (om `CI` eller `GITHUB_ACTIONS` är definierad): inloggningen finns i en
  personlig nyckelring. På en runner, använd `--use_gemini` med `GOOGLE_API_KEY`.
- Variabler: `AGY_BIN` (annars `PATH`, därefter `~/.local/bin/agy`),
  `AGY_TIMEOUT` (sekunder per segment, inklusive start, standard 900).

**Användarvillkor: det är ditt konto som berörs.** [Antigravitys
villkor](https://antigravity.google/terms) (avsnitt 6) och dess
[FAQ](https://antigravity.google/docs/faq/) förbjuder åtkomst till tjänsten
via tredjepartsprogramvara med hjälp av Antigravity-inloggningen — Claude Code,
OpenClaw och OpenCode nämns där —, med risk för att kontot stängs av. aipmt
varken läser eller återanvänder token: det kör den officiella binären i det
[headless-läge](https://antigravity.google/docs/cli/headless/) som Google
dokumenterar för skript och CI. En Google-medlem bedömde det som "standard"
att köra `agy -p` från ett lokalt skript för eget arbete
([officiellt forum, 25 september 2026, icke-bindande svar](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
ingen text avgör fallet för ett distribuerat verktyg som detta.

**Endast offentliga dokument.** Enligt avsnitt 5 i samma villkor kan
interaktioner — promptar, svar, metadata — användas för att förbättra
Googles produkter och maskininlärning samt granskas av
människor, även för betalprenumerationer. Opt-out sker via inställningen
`enableTelemetry`, vars effekt inte är dokumenterad och som aipmt inte anger; dina inställningar
för agy följer inte med in i dess isolering. Skicka inget konfidentiellt genom den.

### På Claude-prenumerationen: `--use_claude_code`

Samma princip med `claude`, Claude Codes officiella CLI, i läget `-p`: för
den som betalar för Claude Pro eller Max räknas översättningen av från
prenumerationskvoten istället för att faktureras per token. Inte att förväxla med
`--use_claude`, Anthropics API, som faktureras efter användning.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Ingen betalväg förblir öppen, och varje anrop bevisar det.** Claude
  Code tar endast emot en sluten lista med variabler från din miljö — varken
  API-nyckel, token, molnleverantör eller markör för den Claude Code-session
  som aipmt startades från. Före det första segmentet måste `claude auth status`
  visa prenumerationsanslutningen, utan Console-nyckel, och `/usage`, som inte kostar
  någon kvot, måste intyga detta; varje anrop intygar det i sin tur i sin
  initieringshändelse, annars avvisas svaret.
- **Inaktivera ”extra usage”** (claude.ai, Inställningar → Användning) för
  att noll kronor ska gälla: om det är aktiverat tar det vid när ett fönster är förbrukat och
  fakturerar utan att visa något fel. aipmt avbryter översättningen så snart
  ett anrops kvotrapport signalerar det, men det anropet har redan räknats.
- **Kvot delas med dina Claude Code-sessioner.** Varje anrop rapporterar
  användningen för 5-timmarsfönstren och veckofönstret; över 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) startas inga fler segment, för att inte
  tömma det som behövs för ditt arbete.
- **Isolering.** Varje anrop körs utan verktyg, i en privat och
  temporär katalog, i ett läge utan anpassningar: varken dina `CLAUDE.md`, dina insticksprogram,
  hooks, MCP-servrar eller inställningar läses in, och ingenting sparas från
  sessionen. Bilagor är avstängda: en `@chemin` i ditt dokument
  förblir text och öppnar ingen fil (uppmätt).
- **Modeller**: `sonnet` som standard, med ansträngningsgraden `low`, och även i `--eco`:
  `--eco` ändrar ingenting på denna väg. Uppmätt på samma dokument är `haiku`
  dubbelt så långsam — den resonerar utan att man kan förhindra det — till en
  knappt lägre kostnad, och `opus` avvisar biologirelaterat innehåll (nästa
  punkt). Båda förblir tillgängliga via `--model`; dessa alias följer den
  senaste modellen i sin familj. `fable` och varianterna `[1m]` avvisas,
  eftersom de dras från betalda krediter. `--reasoning_effort` justerar ansträngningsgraden,
  vilket en översättning inte drar någon nytta av: det uppmätta resonerandet är obefintligt eller nästintill obefintligt.
- **Opus avvisar visst biologirelaterat innehåll.** Dess skyddsspärrar är
  striktare än Sonnets, och felmeddelandet från Anthropic varnar för att de
  ”can sometimes flag biology-research-adjacent work”. Uppmätt: en kort
  omvärldsbevakningsnotis om 279 genererade molekyler ledde till att artikeln avvisades på samtliga fjorton
  språk. Ingenting skrivs: aipmt avvisar det avbrutna svaret, specificerar
  skyddsspärrarna och rekommenderar `--model sonnet`.
- Avvisas i CI (`CI` eller `GITHUB_ACTIONS` definierad) och under Windows (ej uppmätt).
- Variabler: `AIPMT_CLAUDE_BIN` (annars `PATH`, sedan `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (sekunder per segment, standard 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (standard 0.8), `CLAUDE_CONFIG_DIR` (kontot för
  Claude Code, hämtas aldrig från en projektspecifik `.env`); arbetskataloger under
  `XDG_CACHE_HOME/aipmt/claude-code` (standard `~/.cache`).

**Användarvillkor: det är ditt konto som förpliktigas.** Claude Codes
[juridiska sida](https://code.claude.com/docs/en/legal-and-compliance)
hindrar inte ”an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription”: det är vad aipmt gör, som startar den
officiella binären och aldrig läser av tokengrejen. Men Anthropic ”does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users”, föredrar API-nyckeln för verktyg från
tredje part, ”including open-source projects”, och förbehåller sig rätten att räkna av deras
användning mot betalda krediter
([Claude-hjälpen](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Ingen text avgör fallet för ett distribuerat verktyg som kör binären.

**Data**: för Free-, Pro- och Max-konton gäller modellträning
även för Claude Code när sekretessinställningen tillåter det
([datasidan](https://code.claude.com/docs/en/data-usage)). aipmt sparar
ingen lokal transkription (`--no-session-persistence`). Skicka inte
något konfidentiellt genom den.

### Till valfri leverantör: `--use_opencode`

[OpenCode](https://opencode.ai) är en kodagent i öppen källkod (MIT) som
dirigerar till leverantörer som konfigurerats i den: API-nyckel, prenumeration,
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

`--model` är obligatorisk: utan den skulle OpenCode falla tillbaka på en gratismodell
vars utbyten kan användas för träning, och det valet görs inte åt
dig.

Isolering vid varje anrop:

- en inline-konfiguration, prioriterad över din, definierar en agent `aipmt`
  där alla verktyg avvisas (`permission: { "*": "deny" }`), sessionsdelning
  inaktiverad, `--pure`, aldrig `--auto`;
- temporär och tom arbetskatalog, `OPENCODE_DISABLE_PROJECT_CONFIG` och
  `OPENCODE_DISABLE_CLAUDE_CODE` placerade — utan dem injicerar OpenCode i
  prompten den aktuella katalogens `AGENTS.md` och `~/.claude/CLAUDE.md`. Den
  globala `~/.config/opencode/AGENTS.md` injiceras fortfarande, OpenCode tillåter inte
  att den utesluts;
- utdatakontrakt: returkod 0, ingen händelse `error`, inga verktygsanrop,
  sista steget i `stop`, icke-tom text och agenten `aipmt`
  faktiskt inläst — en okänd `--agent` får inte OpenCode att misslyckas, den
  faller tyst tillbaka på kodningsagenten;
- ingen nyckel för `aipmt` överförs, förutom `OPENCODE_API_KEY`, nyckeln
  för OpenCode själv. Leverantörer konfigureras i OpenCode, inte i
  den `.env` som hör till `aipmt`.

Bra att veta:

- Gratissmodeller från Zen är föränderliga, med odokumenterade gränser, och
  deras utbyten kan användas för träning: lämpligt för offentlig dokumentation,
  inte för privat innehåll.
- En lokal modell måste erbjuda minst 16 k token i kontext, då segmenten
  är upp till 16 000 tecken långa. Ollama konfigurerar ofta 4 096: gå
  via en `Modelfile` med `PARAMETER num_ctx 32768`.
- `--eco` har ingen effekt; `--reasoning_effort` överförs som den är som
  OpenCodes `--variant`.
- OpenCode loggar varje session i `~/.local/share/opencode/`.
- Variabler: `OPENCODE_BIN` (annars `PATH`, sedan `~/.opencode/bin/opencode`),
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

`reasoningEffort: "none"` stänger av det resonerande som Ollama aktiverar som standard på dessa
modeller, och som en Modelfile inte kan inaktivera. Uppmätt på en mening om
sex ord: 919 resonemangstoken och 68 sekunder utan alternativet, 9 token med.

### Till över 400 modeller: `--use_openrouter`

OpenRouter är en router som faktureras efter användning, mot en enhetlig kredit, framför
modeller som hostas av tredje part — inklusive de öppna kinesiska modeller som ingen
annan leverantör tillhandahåller här.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` är obligatorisk. En preflight-kontroll, som körs före all fakturering, hanterar
två särdrag i dirigeringen:

- **Samma modell tillhandahålls av dussintals värdar med olika
  gränser** — för `z-ai/glm-5.3-flash`, 23 värdar varav en med ett tak på
  2 048 utdatatoken. Preflight-kontrollen läser `/api/v1/models/{modèle}/endpoints`,
  sorterar bort värdar under 8 000 utdatatoken eller med degraderad status, och
  fäster övriga med `allow_fallbacks: false`.
- **Resonerande faktureras enligt utdatatakt** — 107 token mot 2 för
  ett ”OK”-svar från `z-ai/glm-5.2`. Det är avstängt som standard; modeller
  som kräver det tilldelas den lägsta ansträngningsgrad de accepterar, eftersom katalogens
  standardvärde kan mätta utdata innan översättningen är klar.
  `--reasoning_effort` har fortsatt företräde.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Kontextfönstret hämtas från katalogen. En modell under 16 400 token
  avvisas före alla anrop: 8 400 för prompt och segment, minst 8 000
  för utdata.
- En slug som saknas i katalogen, en onåbar katalog eller avsaknad
  av en värd som klarar taket stoppar kommandot.
- `finish_reason=length` med tom utdata beror på en budget som förbrukats av
  resonerande, inte trunkering: meddelandet skiljer på detta.
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
följt av ett citat i fetstil: läsbart på GitHub, användbart vid byggprocessen via ett
remark-insticksprogram.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detaljerade mätningar

Alla mätningar är faktiskt genomförda översättningar med `aipmt`, till
fjorton språk: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Skrivna** räknar de filer som spärrarna släppte igenom; **Utan
avvikelse** de där `scripts/compare_structure.py` inte upptäcker något — samma antal
avsnitt, underrubriker, länkar, unika URL:er, kodblock,
inline-kod, tabellrader, blockcitat och ord i fetstil.

”Utan avvikelse” betyder ”inget upptäckt”, inte ”identiskt”: jämförelseverktyget
räknar element utan att läsa deras innehåll. Det uppmärksammar varken en raderad rubrik på
nivå 4, texten i en ersatt inline-kod, en utbytt flagga, eller en intern länk återgiven med en parentes för mycket,
`[texte]((#ancre))`, som inte längre leder någonstans — och det bedömer inte
språket.

### Tät omvärldsbevakningsartikel, läget `--news`

En utgåva av [AI-omvärldsbevakningen från jls42.org](https://jls42.org/fr/news):
589 rader, 140 länkar, 21 avsnitt, 3 skyddade engelska citat. Testkampanj
den 4 och 5 september 2026.

| Modell                                          | Åtkomst            | Skrivna | Utan avvikelse | Median/språk   |
| ----------------------------------------------- | ------------------ | ------- | -------------- | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14**   | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google-prenumeration | 14/14 | ✅ **14/14**   | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google-prenumeration | 14/14 | ✅ **14/14**   | 3 min 14 s     |
| `claude-sonnet-5-5`                             | Anthropic API      | 14/14   | ✅ **14/14**   | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT-prenumeration | 14/14 | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14**   | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14**   | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | Claude-prenumeration | 14/14 | ⚠️ 13/14       | 6 min 49 s     |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14       | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | Claude-prenumeration | 14/14 | ⚠️ 11/14       | 15 min 54 s    |
| `claude-haiku-5-5`                              | Anthropic API      | 14/14   | ⚠️ 11/14       | 2 min 54 s     |
| `claude-haiku-4-5`                              | Anthropic API      | 14/14   | ⚠️ 7/14        | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14       | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14        | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | lokalt             | 10/14   | ❌ 7/14        | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14        | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14        | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok-prenumeration | 1/14    | ❌ 1/14        | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | Claude-prenumeration | 0/14  | ❌ 0/14        | —              |

Grok mättes på nytt den 9 september på en annan utgåva av samma omvärldsbevakning
(356 rader): 9 språk skrivna av 14, 8 utan avvikelse. Det är denna siffra som
visas i tabellen ovan. Tre avbrutna kampanjer finns inte
medtagna: `qwen3.5-27b` (9 språk) och `kimi-k2.6` (4) på grund av brist på krediter,
`z-ai/glm-5.3-flash` vars två misslyckanden berodde på en resonemangsinställning
som leverantören sedan dess har korrigerat. OpenRouter-raderna mättes med
routerns standardinställningar, före `--use_openrouter`; `z-ai/glm-5.2`,
som mättes på nytt med den levererade providern, ger samma 14/14. Siffrorna
beräknades om den 10 september med det nuvarande jämförelseverktyget: `qwen3.8-flash` och
`qwen3.7-flash` får vardera ytterligare ett språk jämfört med den första
publiceringen, de övriga är oförändrade.

`--use_antigravity`-raderna mättes den 26 september på samma
artikel, fyra översättningar parallellt: `gemini-3.7-flash-medium` på förmiddagen,
`gemini-3.8-flash-medium` på eftermiddagen. På engelska tog vardera själv bort
de tre raderna med fransk översättning under citaten, utan att hitta på någon
flagga, och de engelska citaten är intakta: återgångsrensningen behövde
inte göra någonting. I `--eco` (`gemini-3.7-flash-low`), på endast fyra språk
(en, ja, ar, hi): 4 skrivna av 4, samtliga utan avvikelse, median på 1 min 52 s.
Kontrolltest samma dag på en nyare utgåva av omvärldsbevakningen,
den från 25 september (438 rader, 2 engelska citat), översatt utanför
bloggen med `gemini-3.7-flash-medium`: 14 skrivna av 14, samtliga utan avvikelse, 87 till
128 s per språk.

`--use_claude_code`-raderna mättes den 26 september på samma
artikel, fyra översättningar parallellt, med ansträngningsgraden `low`. Med `sonnet` är de
engelska citaten intakta på samtliga fjorton språk och, på engelska, tog
modellen själv bort raderna med fransk översättning, utan att hitta på någon
flagga. `opus` skrev inte något språk: på varje språk stoppade dess skyddsspärrar
svaret vid det sista segmentet på grund av en notis om 279 molekyler
som genererats för en bindningsplats. Skickad ensam avvisas denna notis under
kategorin ”bio”; `sonnet` översatte den överallt. `haiku` skriver
alla fjorton språk; på tre (en, pl, ro) ändras en avsnittsrubrik från
nivå 2 till nivå 1. Den resonerar utan att man kan förhindra det — 61 % av
dess utdatatoken —, därav mer än dubbla tiden jämfört med `sonnet`.

Raderna `claude-sonnet-5-5`, `claude-haiku-5-5` och `claude-haiku-4-5` mättes
den 18 oktober via Anthropics API på samma artikel, fyra
översättningar parallellt per modell. Sonnet 5.5 vägrar att man stänger av dess
reflektion: aipmt skickar den lägsta inställning den accepterar, och dess
svar innehåller ingen sådan. Den skriver samtliga fjorton språk utan avvikelse och utan
att behöva göra om något segment; på engelska tog den själv bort raderna med
fransk översättning, utan att hitta på någon flagga, och de engelska citaten är
intakta överallt. Haiku 5.5 mäts med sin adaptiva reflektion: med reflektionen
avstängd lämnade den hela stycken på franska, vilket spärren avvisar —
3 språk skrivna av 14. Båda Haiku fastnar på samma notis: Haiku 5.5
ändrar nivån på dess rubrik eller dubblerar den på japanska, koreanska och
kinesiska; Haiku 4.5 ändrar den till nivå 1 på sju språk och lämnar den på
franska på japanska. Haiku 4.5 kostar 3,67 $ för de två dokumenten på de
fjorton språken, Haiku 5.5 0,57 $, Sonnet 5.5 9,21 $.

### README för detta projekt, standard-Markdown

Fryst revision den 9 september 2026: 785 rader, 285 inline-koder, 40
kodblocksavslut, 89 tabellrader. Fyra översättningar parallellt.

| Modell                                          | Skrivna | Utan avvikelser | Median/språk | Vad som skiljer                                                          |
| ----------------------------------------------- | ------- | --------------- | ------------ | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14        | 1 min 43 s   | inget                                                                    |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14        | 1 min 48 s   | inget                                                                    |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14        | 4 min 02 s   | inget för jämföraren; dubblerade interna länkar (en)                     |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14        | 1 min 18 s   | inget                                                                    |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14        | 2 min 06 s   | inget                                                                    |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14        | 36 s         | ett ord i fetstil (ja)                                                   |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14        | 1 min 22 s   | ett ord i fetstil (ko)                                                   |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14        | 2 min 20 s   | en tabellrad sammanslagen med föregående (ar)                            |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14        | 2 min 56 s   | en länk (sv), ett ord i fetstil (zh)                                     |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14        | 6 min 46 s   | ett ord i fetstil (ar, ja)                                               |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14        | 2 min 34 s   | ett ord i fetstil (hi, ja, ko)                                           |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14        | 2 min 17 s   | 40 inline-koder tillagda på arabiska; fetstil (hi, ja, ko)                |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14        | 1 min 14 s   | 2 språk avvisade (ar, hi): förlorade inline-koder vid retur              |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14         | 2 min 44 s   | ett avsnitt förlorat (ar, hi, ko); tillagda kodblock (ja, ko, ro, zh)   |

Två avbrutna körningar tas inte med: Grok, vars CLI-session löpte ut
efter tolv språk (elva utan avvikelser), och `qwen3.8-flash`, HTTP 429 från sin
värd efter två. `opencode/mimo-v2.5-free` och `ollama/gpt-oss-20b-32k`
mättes inte om på denna revision; på den från 4 och 5 september,
som var 277 rader kortare, skrev de vardera 9 av 14 översättningar, varav 7
respektive 1 utan avvikelser.

Raderna `--use_antigravity` och `--use_claude_code` mättes inte på
den frysta revisionen, utan den 26 september på den som publicerades med 1.14.0 — och
raderna `claude-sonnet-5-5`, `claude-haiku-5-5` och `claude-haiku-4-5` den 18
oktober, på samma: 600 rader, 257 inline-koder, 30 kodblocksavslut, 85
tabellrader. Då den är
185 rader kortare kan den inte jämföras rakt av med de andra raderna;
dessa rader kan däremot jämföras sinsemellan. När det gäller interna länkar, som
jämföraren inte kontrollerar, behöll `gemini-3.8-flash-medium` dem intakta på
de fjorton språken, `gemini-3.7-flash-medium` bröt dem på italienska;
`sonnet` och `opus` behöll dem intakta överallt, `haiku` dubblerade dem på
engelska; `claude-sonnet-5-5` och `claude-haiku-4-5` behöll dem intakta på
de fjorton språken, `claude-haiku-5-5` på de tolv som den skrev.

### Fyra README från kända projekt

FastAPI, Ollama, tldr-pages och Vue.js, tagna som de är från GitHub —
enklare dokument än de två föregående. Körningen riktade sig mot modellerna
med svårigheter; Gemini fungerar här som referenspunkt.

| Modell                    | Omfattning                 | Skrivna | Utan avvikelser |
| ------------------------- | -------------------------- | ------- | --------------- |
| `gemini-3.7-flash`        | 4 projekt × 14 språk       | 56/56   | ✅ **55/56**    |
| `opencode/mimo-v2.5-free` | 4 projekt × 14 språk       | 55/56   | ❌ 47/56        |
| `grok-4.6` (prenumeration)   | 4 projekt × ar, hi, ja, zh | 16/16   | ❌ 14/16        |
| `ollama/gpt-oss-20b-32k`  | 4 projekt × ar, hi, ja, zh | 15/16   | ❌ 9/16         |

### Vad dessa mätningar inte är

- **Inte en uttömmande rankning**: Enbart OpenRouter erbjuder över fyra hundra
  modeller, ett femtontal har mätts.
- **Ungefärliga tidsåtgångar**: tre till sex parallella översättningar beroende
  på körning, och en leverantörs dataflöde varierar under dagen.
- **Daterade observationer**: modeller ändras under samma namn, och era
  dokument är inte våra.

För att göra om mätningen på dina dokument, på en fryst kopia av filen:

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

De 28 översättningarna i förvaret (README och CHANGELOG, fjorton språk)
återskapas med `./regen_translations.sh --force` — Codex och `gpt-6.1-sol` via
ChatGPT-prenumerationen som standard, fyra parallellt. `REGEN_PROVIDER` och
`REGEN_MODEL` ändrar sökvägen: `antigravity` stannar kvar på en prenumeration, Googles,
och passerar utan undantag; ett debiterat API (`openai`, `gemini`,
`grok`, `openrouter`) avvisas utan `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` sätter ett tak för varje körning (600 s, 1 800 s för Codex och
Antigravity). Detaljer om verktygen finns i `CLAUDE.md`.

## Projekt som använder detta skript

- **[jls42.org](https://jls42.org)** — personlig blogg publicerad på 15 språk. Dess
  [dagliga AI-bevakning](https://jls42.org/fr/news) översätts varje dag
  med detta verktyg och fungerar som referensdokument för mätningarna ovan.

## Författare

Julien LE SAUX
E-post: contact@jls42.org

## Licens

GNU GENERAL PUBLIC LICENSE Version 3. Se [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Friskrivning

Detta program distribueras **utan någon garanti**, enligt villkoren i
avsnitt 15 och 16 i GPL v3: tillhandahålls "i befintligt skick", utan garanti för säljbarhet
eller lämplighet för ett visst syfte, och dess författare kan inte hållas
ansvarig för skador som uppstår till följd av dess användning. Licenstexten
äger företräde framför denna sammanfattning.

- **Korrekturläs före publicering.** Skydden omfattar kodblock, inline-kod,
  webbadresser, ankare och citat i läget `--news` — inte
  rubriker, tabeller, front matter eller innebörden av dina meningar.
- **Dina dokument skickas till vald leverantör**, enligt dess användarvillkor
  och datapolicy. Vissa gratismodeller kan återanvända dina konversationer
  för träning, och Antigravitys villkor tillåter Google att återanvända dem och
  låta människor granska dem, inklusive vid betalda prenumerationer; en lokal
  modell är det enda sättet som säkerställer att ingen data lämnar din dator.
- **API-anrop faktureras dig.** Detta program sätter inget utgiftstak: ett
  långt dokument, en återupptagning efter fel eller en modell med omfattande
  resonerande kostar mer.
- **De publicerade mätningarna är daterade observationer**, inga garantier.

Produkt- och företagsnamn som nämns tillhör sina respektive innehavare. Detta projekt är inte anslutet till något av dem.

**Artikel översatt från fr till sv med gemini-3.8-flash-medium.**

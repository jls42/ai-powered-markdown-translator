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

Översätter Markdown-filer från ett språk till ett annat och bevarar
strukturen: kodblock, inline-kod, URL:er, ankare, tabeller och front
matter. Elva sätt att anropa en modell — fem API:er, fyra abonnemang utan
användningsbaserad debitering, två routrar — och publicerade mätningar av vad varje
modell faktiskt bevarar.

## I korthet

- **Elva leverantörsvägar**: API:er från OpenAI, Mistral, Claude, Gemini och Grok;
  abonnemang på ChatGPT (Codex), Grok, Google (Antigravity) och Claude (Claude
  Code) utan användningsbaserad debitering; routrarna OpenCode (open source, gratis eller lokalt) och OpenRouter
  (över 400 modeller).
- **Inga fel på grund av en förlorad token**: kodblock, inline-kod,
  URL:er, ankare och citat ersätts med token före anropet och
  kontrolleras när svaret kommer tillbaka. Om någon saknas skrivs filen inte.
- **Långa dokument**: segmentering efter modellens kontextfönster.
- **Läget `--news`**: skyddade engelska citat och flaggor hanterade per
  språk, för omvärldsbevakningsartiklar.
- **Läget `--eco`**: snabba och billigare modeller.
- Valfri **översättningsnotis**, överst, nederst eller på båda ställena.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11 eller senare. För installation från repot, se
[Bidra](#bidra).

## Konfiguration

Nycklarna läses från tre platser, i fallande prioritetsordning; varje plats
fyller bara i det som den föregående lämnar tomt.

|     | Var                                            | För vad                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Miljövariabler                     | CI, containrar, tillfälliga åsidosättningar |
| 2   | `.env` i den aktuella katalogen (eller en överordnad katalog) | en projektspecifik nyckel            |
| 3   | `~/.config/aipmt/.env`                        | konfigureras en gång, gäller överallt       |

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
som körs.** Den tillhandahåller nycklar, aldrig en destination eller en binärfil: alla
variabler med `_BASE_URL`, `_API_BASE`, `_ENDPOINT` eller `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, proxyinställningar (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), certifikatlager (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) och `XDG_CONFIG_HOME` /
`APPDATA` ignoreras där, med en varning. Ett klonat repo ska inte
kunna stjäla din nyckel eller få dig att köra sitt eget program vid
den första översättningen. Den här filen läses också utan interpolering:
`NOM=${OPENAI_API_KEY}` kopierar inte in nyckeln där. Ange dessa variabler i
miljön eller i `~/.config/aipmt/.env`.

Valfria variabler: `XAI_BASE_URL` (standard `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (sekunder per anrop, standard 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(standard 600), `GROK_BIN`, `GROK_HOME` (standard `~/.grok`), `GROK_TIMEOUT`
(standard 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (standard 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (standard 600), `OPENROUTER_BASE_URL`
(`https://` krävs), `OPENROUTER_TIMEOUT` (standard 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (standard 30). Var och en beskrivs utförligt i
avsnittet för sin leverantör.

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
`--keep_filename`, som behåller det ursprungliga namnet. En befintlig översättning
hoppas över utan `--force`.

Exitkoder: `0` om allt har slutförts eller hoppats över, `1` om någon fil fortfarande
har misslyckats (lista på standardfelutmatningen), `2` om problemet gäller konfigurationen.
En misslyckad fil skrivs aldrig, även om själva skrivningen misslyckas:
innehållet skrivs till en separat fil bredvid och döps sedan om. Det räcker att köra igen.

## Vilken modell ska man välja

Mätt på två verkliga dokument som varje modell översatte till
samma fjorton språk. **Siffran anger antalet språk, av fjorton, där
översättningen skrivs och där ingenting avviker från källan.**

| Modell                | Så får du tillgång till den                 | Tät omvärldsbevakningsartikel | Denna README    | Vad som avviker och på hur många språk                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google-abonnemang (Antigravity)   | ✅ 14/14                | ✅ 14/14     | ingenting, i något av dokumenten                                                                                                                                 |
| **Claude Sonnet 5.5** | API-nyckel från Anthropic                 | ✅ 14/14                | ✅ 14/14     | ingenting, i något av dokumenten                                                                                                                                 |
| **Gemini 3.7 Flash**  | API-nyckel från Google                    | ✅ 14/14                | ⚠️ 13/14     | 1 språk av 14: ett extra ord i fetstil (ja)                                                                                                                      |
| **Gemini 3.7 Flash**  | Google-abonnemang (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 1 språk av 14: ett ord färre i fetstil (ko)                                                                                                                     |
| **GPT-5.6 Sol**       | ChatGPT-abonnemang eller OpenAI-nyckel | ✅ 14/14                | ⚠️ 12/14     | 2 språk av 14: ett ord färre i fetstil (ar, ja)                                                                                                                |
| **GLM-5.2**           | OpenRouter-nyckel                    | ✅ 14/14                | ⚠️ 11/14     | 3 språk av 14: ett ord färre i fetstil (hi, ja, ko)                                                                                                            |
| Claude Sonnet 5       | Claude-abonnemang (Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 1 språk av 14 i artikeln: ett extra ord i fetstil (zh); 1 i denna README: en tabellrad har fogats ihop med den föregående och döljs vid visning (ar)            |
| Claude Haiku 4.5      | Claude-abonnemang (Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 3 språk i artikeln: en avsnittsrubrik har flyttats till nivå 1 (en, pl, ro); i denna README upptäcker jämförelseverktyget ingenting, men interna länkar har dubblerats på engelska |
| Claude Sonnet 5       | API-nyckel från Anthropic                 | ⚠️ 11/14                | ⚠️ 12/14     | 3 språk i artikeln: ett kodblock har tillkommit (es, de, hi); 2 i denna README: en länk utan sin uppmärkning (sv), ett ord i fetstil (zh)                              |
| Claude Haiku 4.5      | API-nyckel från Anthropic                 | ⚠️ 7/14                 | ✅ 14/14     | 7 språk i artikeln: en avsnittsrubrik har flyttats till nivå 1 — på japanska har den förblivit på franska; ingenting i denna README                                              |
| Claude Haiku 5.5      | API-nyckel från Anthropic                 | ⚠️ 11/14                | ❌ 12/14     | 3 språk i artikeln: en avsnittsrubrik har bytt nivå eller dubblerats (ja, ko, zh); i denna README har 2 språk avvisats på grund av förlorad inline-kod (ar, hi)    |
| Qwen 3.7 Flash        | OpenRouter-nyckel                    | ❌ 8/14                 | ⚠️ 10/14     | 1 språk avvisat för artikeln, 5 andra avviker; i denna README har ett fyrtiotal ord placerats i `code` (ar)                                                    |
| Grok 4.6              | Grok-abonnemang                   | ❌ 8/14                 | ej betygsatt     | 5 språk av 14 avvisade på grund av att inline-kod och URL:er inte återgavs; nederländskan avviker på alla punkter                                                               |
| GPT-OSS 20B           | lokal modell (Ollama)             | ❌ 7/14                 | ej mätt på nytt | 4 språk av 14 avvisade: modellen lämnade kvar franska textavsnitt, skyddskontrollen stoppade dem                                                                  |
| MiMo v2.5 (gratis)   | OpenCode Zen, utan konto         | ❌ 11/14                | ej mätt på nytt | 1 språk avvisat; ett avsnitt förlorat på polska                                                                                                                  |
| Mistral Large         | API-nyckel från Mistral                   | ❌ 5/14                 | ❌ 1/14      | **ett helt avsnitt försvinner**: 1 språk i artikeln (hi), 3 i denna README (ar, hi, ko) — och 3 språk avvisade för artikeln                                |
| DeepSeek V4 Flash     | OpenRouter-nyckel                    | ❌ 3/14                 | ej mätt på nytt | 10 språk av 14 avvisade; 37 minuter per språk                                                                                                                 |
| Claude Opus 5.5       | Claude-abonnemang (Claude Code)   | ❌ 0/14                 | ✅ 14/14     | artikeln avvisad på alla 14 språk av Opus skyddsmekanismer på grund av en kort biologinotis; ingenting i denna README                                               |

|     | Vad symbolen betyder                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | alla fjorton språk översatta och ingenting avviker från källan                                                                                                                                       |
| ⚠️  | alla fjorton språk översatta; avvikelserna gäller **uppmärkning** — ett ord i fetstil, en `code`, en länk som förlorar sina hakparenteser. Ingen text, ingen URL, inget kodblock och inget avsnitt saknas |
| ❌  | minst ett språk kunde inte översättas — filen avvisas och skrivs inte — **eller** innehåll saknas i en skriven fil                                                                      |

Vad man bör ta med sig:

- **En avvisad översättning är inte en skadad översättning.** När en token
  saknas i svaret skrivs filen inte, och språket räknas som
  avvisat. Det är vad som händer med Grok i artikeln: fyra inline-kodavsnitt och
  tre URL:er förloras redan i det första segmentet, för de fem språken med icke-latinska skriftsystem.
- **En modell kan avvisa ett helt dokument på grund av en enda mening.** Opus 5.5
  översätter denna README utan en enda avvikelse, men ingen omvärldsbevakningsartikel:
  dess skyddsmekanismer stoppar svaret vid en kort biologinotis. Filen
  skrivs inte, och aipmt förklarar varför.
- **Detta skyddsnät täcker inte rubriker, tabeller, front matter eller
  text.** En modell som tar bort ett avsnitt lämnar tillbaka en fil som verktyget skriver
  utan invändningar — så är fallet med Mistral. Dessa element kan inte
  ersättas med en token, och de nuvarande skyddskontrollerna kontrollerar dem inte;
  `scripts/compare_structure.py` upptäcker ett förlorat avsnitt, men i efterhand.
- **Grok har inget betyg för denna README**: dess CLI-session löpte ut efter tolv
  språk, varav elva utan avvikelser. En avbruten mätomgång betygsätts inte.
- **Dokumentets täthet spelar större roll än språket.** Grok klarar
  vanliga README-filer men tappar greppet om en artikel full av länkar, även på
  nederländska.

Datum och dokument: kolumnen ”Denna README” mättes den 9 september 2026
på en låst version av den här filen (785 rader, 285 inline-kodavsnitt, 89
tabellrader), som har ändrats sedan dess — med undantag för raderna för Antigravity och Claude Code,
som mättes den 26 september på den version som publicerades med 1.14.0 och var kortare
(600 rader, 257 inline-kodavsnitt, 85 tabellrader), samt raderna för Claude
Sonnet 5.5, Haiku 5.5 och Haiku 4.5 via API, som mättes den 18 oktober på
samma version. Kolumnen ”Tät omvärldsbevakningsartikel” kommer från mätomgången
den 4 och 5 september på en artikel med 589 rader, med undantag för Grok-raden, som mättes på nytt den
9 september på en annan utgåva av samma omvärldsbevakning, raderna för Antigravity och
Claude Code, som mättes den 26 september på samma artikel, samt dessa tre
Claude-rader, den 18 oktober. De fullständiga tabellerna, tidsåtgången och mätprotokollet finns
i [Detaljerade mätningar](#detaljerade-mätningar).
## Alla alternativ

| Alternativ                   | Beskrivning                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | En enskild Markdown-fil att översätta (alternativ till `--source_dir`)                                             |
| `--source_dir`           | Källkatalog med Markdown-filerna (standard: `content/posts`)                                   |
| `--target_dir`           | Utdatakatalog för de översatta filerna (standard: `traductions_en`)                                    |
| `--source_lang`          | Källspråk (standard: `fr`)                                                                                  |
| `--target_lang`          | Målspråk (standard: `en`)                                                                                   |
| `--model`                | Specifik modell att använda                                                                                  |
| `--eco`                  | Använd de billigare modellerna                                                                              |
| `--use_mistral`          | Använd Mistral AI:s API                                                                                     |
| `--use_claude`           | Använd Claudes API                                                                                         |
| `--use_gemini`           | Använd Geminis API                                                                                         |
| `--use_grok`             | Använd xAI:s API (Grok) — kräver `XAI_API_KEY`                                                           |
| `--use_codex`            | Använd Codex CLI med kvoten i ChatGPT-abonnemanget                                                    |
| `--use_grok_cli`         | Använd Grok CLI med kvoten i Grok-abonnemanget                                                        |
| `--use_antigravity`      | Använd Antigravity CLI (`agy`) med kvoten i Google AI Pro- eller Ultra-abonnemanget                       |
| `--use_claude_code`      | Använd Claude Code CLI (`claude -p`) med kvoten i Claude Pro- eller Max-abonnemanget                      |
| `--use_opencode`         | Använd OpenCode (open source) med den leverantör som konfigurerats i OpenCode; kräver `--model provider/modèle` |
| `--use_openrouter`       | Använd OpenRouter — kräver `OPENROUTER_API_KEY` och `--model fournisseur/modèle`                          |
| `--force`                | Tvinga fram en ny översättning                                                                                       |
| `--keep_filename`        | Behåll det ursprungliga filnamnet                                                                          |
| `--news`                 | Nyhetsläge: skyddar engelska citat, hanterar flaggor per språk                                      |
| `--add_translation_note` | Lägg till en översättningsnot                                                                                |
| `--note_position`        | Notens placering: `top`, `bottom` (standard) eller `both`                                                     |
| `--note_format`          | Notens format: `legacy` (standard, stycke i fetstil) eller `marker`                                            |
| `--include_model`        | Inkludera modellnamnet i utdatafilen                                                            |
| `--reasoning_effort`     | Resonemangsnivå för GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

De nio flaggorna `--use_*` är ömsesidigt uteslutande: att kombinera två
tillåts inte.

## Leverantörer

### Via API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` växlar till varje leverantörs billigare nivå.

| Leverantör    | Kvalitet (standard)                                                     | Billigare (`--eco`)      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                                      | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-3.8-flash`                                                   | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (även `gpt-5.6-sol`, `terra` och `luna` via `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | samma — `--eco` har ingen effekt |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, nivå `low`                                               | samma — `--eco` har ingen effekt |
| OpenCode    | `--model provider/modèle` krävs                                | samma — `--eco` har ingen effekt |
| OpenRouter  | `--model fournisseur/modèle` krävs                             | samma — `--eco` har ingen effekt |

Gemini 3.7 Flash, som var standard till och med 1.17.1, är utfasad: Google använder
Gemini 3.8 Flash i dess ställe, och `--model gemini-3.7-flash` accepteras fortfarande.
Ett tillfälligt fel i Geminis API (503, 429, timeout) gör att
anropet försöks igen upp till tre gånger, efter 10, 20 respektive 40 sekunder. Ett försök
som inte fått svar avbryts efter 5 minuter och görs sedan om på
samma sätt: en server som inte svarar får segmentet att misslyckas efter högst omkring tjugo minuter,
i stället för att blockera utan tidsgräns.

### Med ChatGPT-abonnemanget: `--use_codex`

Styr det officiella Codex CLI: översättningen dras från kvoten i
ChatGPT-abonnemanget, utan API-nyckel eller användningsbaserad debitering.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Binärfilen söks i `CODEX_BIN`, sedan i `PATH` och därefter i paketet
  `openai-codex-cli-bin`. `~/.codex/auth.json` läses aldrig.
- `OPENAI_API_KEY` och `CODEX_API_KEY` tas bort från underprocessens
  miljö: en befintlig nyckel leder aldrig till att API används.
- Varje segment förbrukar minst ett ”meddelande” i femtimmarsfönstret — två
  om valideringen misslyckas och segmentet försöks igen. OpenAI anger som
  uppskattning 250-2 000 meddelanden/5 h för `gpt-5.6-luna` (`--eco`) och
  10-100 för `gpt-5.6-sol` med ett Plus-abonnemang.
- `--model gpt-5.6-sol`, som var standard till och med 1.16.3, `--model gpt-5.6-terra`
  och `--model gpt-5.6-luna` använder också abonnemanget.
- Ett 429-svar från servern gör inte att filen går förlorad: Codex återansluter automatiskt,
  aipmt väntar tills omgången är klar, och om 429-felet kvarstår försöks segmentet
  igen efter 30 och sedan 60 sekunder. En modell som kontot inte har tillgång till ger ett 400-fel: ”modellen
  stöds inte när Codex används med ett ChatGPT-konto”.
- Långsammare än ett API, och skillnaden växer med dokumentet: för denna README
  är medianen 6 min 46 s per språk med `gpt-5.6-sol`, jämfört med 36 s för
  `gemini-3.7-flash`.
- Tillåts inte i CI (om `CI` eller `GITHUB_ACTIONS` är definierad): abonnemanget autentiseras
  med en personlig sessionsfil, som inte hör hemma på en delad
  runner.
- Variabler: `CODEX_BIN`, `CODEX_TIMEOUT` (sekunder per segment, standard 600).

### Med Grok-abonnemanget: `--use_grok_cli`

Samma princip med det officiella Grok Build CLI, med ett SuperGrok- eller
X Premium+-abonnemang.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Svagare isolering än Codex.** Groks OS-sandbox fungerar
  inte på många nyare Linux-datorer (AppArmor, sockets för container-runtime),
  och en profil som inte kan tillämpas startar utan isolering
  utan att meddela det. Skriptet begär därför ingen profil som standard, meddelar detta och
  förlitar sig på CLI-reglerna `--deny`, däribland catch-all-regeln `*` — det enda
  lager som vägrar starta i stället för att ta bort skyddet utan att
  säga till. `GROK_TRANSLATE_SANDBOX=read-only` kräver OS-sandboxen, och starten
  misslyckas om datorn inte kan uppfylla kravet.
- Kvoten gäller per vecka, delas med Chat, Imagine och Voice, och det finns inget
  kommando för att läsa av den: en batch kan förbruka kvot för konversationsanvändning
  utan någon signal.
- Variabler: `GROK_BIN`, `GROK_HOME` (CLI-katalog, standard `~/.grok`),
  `GROK_TIMEOUT` (standard 900), `GROK_TRANSLATE_SANDBOX`.

### Med Google-abonnemanget: `--use_antigravity`

Samma princip med `agy`, Antigravitys officiella CLI: för den som betalar för Google
AI Pro eller Ultra dras översättningen från abonnemangets kvot i stället
för att debiteras per token. Det är den enda vägen till denna kvot: Gemini CLI
betjänar inte längre dessa konton sedan den 18 juni 2026
([tillkännagivande](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
och Antigravitys SDK accepterar bara en API-nyckel eller ett Google Cloud-projekt.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Ingen väg till extra debitering lämnas öppen.** agy får bara
  en sluten lista med variabler från din miljö — `PATH`, språk och tidszon,
  terminal, identitet, proxyservrar och certifikat, sessionsbuss — och inga nycklar:
  flera av dess variabler styr om ett anrop utan att visa något (uppmätt:
  en skickar dokumentet till en tredjepartsgateway, en annan till ett
  debiterat Google Cloud-projekt), och en spärrlista visade sig missa några vid varje granskning.
  Före varje segment måste `agy -p /config`, som inte förbrukar någon kvot, visa
  att betalda AI-krediter är inaktiverade, utan API-nyckel eller Google Cloud-projekt — en
  saknad inställning innebär avslag — annars översätts ingenting; loggen för varje
  anrop måste sedan intyga att abonnemanget används (`authMethod=consumer`), annars
  avvisas svaret.
- **Isolering.** Varje anrop körs i en privat, tillfällig hemkatalog
  med en översättningsagent utan verktyg: dina inställningar, regler,
  plugins, MCP-servrar och hooks för agy följer inte med, ingenting läggs till i din
  historik, och inloggningen ligger kvar i nyckelringen, som aipmt aldrig läser.
  Om en agent inte hittas återgår agy utan att meddela det till sin kodningsagent
  och dess verktyg: en hel loggrad måste bekräfta rätt agent — ett
  dokument som citerar meddelandet ersätter den inte — annars avvisas anropet.
- **Plattformar**: Linux, i en session med en nyckelring (D-Bus-sessionsbuss,
  Secret Service); macOS accepteras, men har inte testats med mätningar. Tillåts inte
  på Windows, där agy inte läser variablerna som isolerar varje anrop, eller
  på Linux utan sessionsbuss — SSH-session, container, server: där lagrar agy
  sin token i en fil i `~/.gemini`, som isoleringen döljer.
  Avslaget kommer före varje start, med en förklaring, i stället för efter en minuts
  väntan på en inloggningskod.
- **Modeller**: de som finns i `agy models`. Gemini-modellerna har resonemangsnivån i namnet
  (`gemini-3.8-flash-medium`…): ett namn utan suffix avvisas före anropet,
  och `--reasoning_effort` har ingen effekt. Standard är `gemini-3.8-flash-medium`,
  och `gemini-3.7-flash-low` med `--eco`; de mätkampanjer som ligger till grund för valen
  beskrivs i [Detaljerade mätningar](#detaljerade-mätningar). Claude och GPT-OSS
  har en egen, mycket mindre kvot: omkring 1 % av femtimmarsfönstret
  per uppmätt anrop, jämfört med 0,05 % för Flash.
- **Kvot**: per grupp, ett femtimmarsfönster och ett veckofönster,
  proportionellt mot kostnaden i tokens. Uppmätt på författarens konto: omkring
  16 procentenheter av femtimmarsfönstret per miljon källtecken med
  `gemini-3.8-flash-medium`, 14 med `gemini-3.7-flash-medium` och 7 till 8 med
  låg resonemangsnivå — en README på 40 000 tecken kostar alltså lite mer än en
  halv procentenhet. Veckogränsen beror däremot på abonnemangsnivån. Nya försök följer
  vad agy anger kan försökas igen; annars görs aldrig något nytt försök när ett fönster är
  förbrukat: varje fil misslyckas fram till den återställningstid
  som `/usage` visar.
- **Långsammare än API**: för den informationstäta artikeln med mätningarna är medianen
  3 min 59 s per språk med `gemini-3.8-flash-medium` och 3 min 14 s med
  `gemini-3.7-flash-medium`, jämfört med 1 min 18 s för Gemini 3.7 Flash via API.
- **Avbrott**: Ctrl-C eller en stängd terminal stoppar agy tillsammans med
  kommandot i stället för att låta det slutföra omgången med din kvot; detsamma gäller
  Codex, Grok CLI och OpenCode. Med `nohup` fortsätter översättningen.
- Tillåts inte i CI (om `CI` eller `GITHUB_ACTIONS` är definierad): inloggningen finns i en
  personlig nyckelring. På en runner används `--use_gemini` med `GOOGLE_API_KEY`.
- Variabler: `AGY_BIN` (annars `PATH`, sedan `~/.local/bin/agy`),
  `AGY_TIMEOUT` (sekunder per segment, inklusive start, standard 900).

**Användarvillkor: det är ditt konto som berörs.** 
[Antigravitys villkor](https://antigravity.google/terms) (avsnitt 6) och dess
[FAQ](https://antigravity.google/docs/faq/) förbjuder åtkomst till tjänsten
via tredjepartsprogram med Antigravity-inloggningen — Claude Code,
OpenClaw och OpenCode nämns där — med risk för att kontot stängs av. aipmt
varken läser eller återanvänder token: det startar den officiella binärfilen i det
[headless-läge](https://antigravity.google/docs/cli/headless/) som Google
dokumenterar för skript och CI. En Google-medarbetare bedömde det som ”standard”
att starta `agy -p` från ett lokalt skript för eget arbete
([officiellt forum, 25 september 2026, ej bindande svar](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
ingen text avgör vad som gäller för ett distribuerat verktyg som detta.

**Endast offentliga dokument.** Enligt avsnitt 5 i samma villkor kan
utbyten — prompts, svar, metadata — användas för att förbättra
Googles produkter och maskininlärning och granskas av
människor, även med ett betalt abonnemang. För att välja bort detta används inställningen
`enableTelemetry`, vars effekt inte är dokumenterad och som aipmt inte anger; dina agy-inställningar
följer inte med in i den isolerade miljön. Skicka inget konfidentiellt genom den.
### Med Claude-abonnemanget: `--use_claude_code`

Samma princip med `claude`, Claude Codes officiella CLI, i läget `-p`: för
den som betalar för Claude Pro eller Max räknas översättningen av från
abonnemangets kvot i stället för att debiteras per token. Ska inte förväxlas med
`--use_claude`, Anthropics API, som debiteras efter användning.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Ingen betalväg lämnas öppen, och varje anrop bevisar det.** Claude
  Code får bara en sluten lista med variabler från din miljö — varken
  API-nyckel, token, molnleverantör eller markör för den Claude Code-session
  som aipmt skulle startas från. Före det första segmentet måste `claude auth status`
  visa abonnemangsinloggningen, utan Console-nyckel, och `/usage`, som inte förbrukar
  någon kvot, måste bekräfta den; varje anrop bekräftar den i sin tur i sin
  initieringshändelse, annars avvisas svaret.
- **Inaktivera ”extra usage”** (claude.ai, Inställningar → Användning) för
  att kostnaden ska förbli noll euro: när det är aktiverat tar det över när ett tidsfönster är förbrukat och
  debiterar utan att visa något fel. aipmt stoppar översättningen så snart ett anrops
  kvotrapport signalerar detta, men just det anropet har redan räknats.
- **Kvoten delas med dina Claude Code-sessioner.** Varje anrop rapporterar
  användningen för femtimmarsfönstret och veckan; över 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`) startas inga fler segment, för att inte
  förbruka det som behövs för ditt arbete.
- **Isolering.** Varje anrop körs utan verktyg, i en privat och
  tillfällig katalog, i ett läge utan anpassningar: varken dina `CLAUDE.md`, dina plugins,
  hooks, MCP-servrar eller inställningar läses in, och inget sparas från
  sessionen. Bilagor är avstängda: ett `@chemin` i ditt dokument
  förblir text och öppnar ingen fil (uppmätt).
- **Modeller**: `sonnet` som standard, med ansträngningsnivån `low`, även i `--eco`:
  `--eco` ändrar ingenting i den här körvägen. Vid mätning på samma dokument är `haiku`
  dubbelt så långsam — den resonerar utan att det går att förhindra — till
  en knappt lägre kostnad, och `opus` vägrar visst biologiinnehåll (nästa
  punkt). Båda är fortfarande tillgängliga via `--model`; dessa alias följer den
  senaste modellen i respektive familj. `fable` och varianterna `[1m]` avvisas,
  eftersom de använder betalda krediter. `--reasoning_effort` styr ansträngningsnivån,
  som en översättning inte har någon nytta av: det uppmätta resonemanget är noll eller nästan noll.
- **Opus vägrar visst biologiinnehåll.** Dess skyddsmekanismer är
  striktare än Sonnets, och Anthropics felmeddelande varnar för att de
  ”ibland kan flagga arbete som ligger nära biologisk forskning”. Uppmätt: en kort
  omvärldsnotis om 279 genererade molekyler fick artikeln att avvisas på alla fjorton
  språk. Inget skrivs: aipmt avvisar det avbrutna svaret, anger
  skyddsmekanismerna som orsak och rekommenderar `--model sonnet`.
- Avvisas i CI (om `CI` eller `GITHUB_ACTIONS` är definierad) och under Windows (inte uppmätt).
- Variabler: `AIPMT_CLAUDE_BIN` (annars `PATH`, sedan `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (sekunder per segment, standard 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (standard 0.8), `CLAUDE_CONFIG_DIR` (Claude
  Code-kontot, hämtas aldrig från ett projekts `.env`); arbetskataloger under
  `XDG_CACHE_HOME/aipmt/claude-code` (standard `~/.cache`).

**Användarvillkor: det är ditt konto som står på spel.** Den
[juridiska sidan för Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
hindrar inte ”en slutanvändare från att logga in i den oförändrade Claude Code-binären
med sitt eget Claude-abonnemang”: det är vad aipmt gör genom att starta den
officiella binären utan att någonsin läsa token. Men Anthropic ”tillåter inte
tredjepartsutvecklare […] att skicka förfrågningar via inloggningsuppgifter för Free-, Pro- eller Max-abonnemang
för sina användares räkning”, föredrar API-nyckeln för
tredjepartsverktyg, ”inklusive open source-projekt”, och förbehåller sig rätten att räkna av deras
användning från betalda krediter
([Claude-hjälpen](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Ingen text avgör fallet med ett distribuerat verktyg som startar binären.

**Data**: på Free-, Pro- och Max-konton gäller modellträningen
även Claude Code när sekretessinställningen tillåter det
([datasidan](https://code.claude.com/docs/en/data-usage)). aipmt sparar
ingen lokal transkription (`--no-session-persistence`). Skicka inget
konfidentiellt genom det.

### Till valfri leverantör: `--use_opencode`

[OpenCode](https://opencode.ai) är en kodagent med öppen källkod (MIT) som
dirigerar till de leverantörer som konfigurerats i den: API-nyckel, abonnemang,
OpenCode Zen-gateway (gratis modeller, utan konto) eller lokal modell. Två
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

`--model` är obligatorisk: utan den skulle OpenCode falla tillbaka på en gratis modell
vars konversationer kan användas för träning, och det valet görs inte åt
dig.

Isolering vid varje anrop:

- en inline-konfiguration, som har företräde framför din, definierar en agent `aipmt`
  vars alla verktyg nekas (`permission: { "*": "deny" }`), med sessionsdelning
  inaktiverad, `--pure`, aldrig `--auto`;
- en tom, tillfällig arbetskatalog, med `OPENCODE_DISABLE_PROJECT_CONFIG` och
  `OPENCODE_DISABLE_CLAUDE_CODE` satta — utan dem lägger OpenCode in
  den aktuella katalogens `AGENTS.md` och `~/.claude/CLAUDE.md` i prompten. Den
  globala `~/.config/opencode/AGENTS.md` läggs fortfarande in; OpenCode tillåter inte
  att den utesluts;
- utmatningskontrakt: returkod 0, ingen `error`-händelse, inget
  verktygsanrop, sista steget i `stop`, text som inte är tom och agenten `aipmt`
  faktiskt inläst — en okänd `--agent` får inte OpenCode att misslyckas, utan det
  faller tyst tillbaka på kodagenten;
- ingen nyckel från `aipmt` skickas vidare, förutom `OPENCODE_API_KEY`, nyckeln
  till själva OpenCode. Leverantörerna konfigureras i OpenCode, inte i
  `aipmt`s `.env`.

Bra att veta:

- Zens gratis modeller ändras, har odokumenterade gränser, och
  deras konversationer kan användas för träning: för offentlig
  dokumentation, inte för privat innehåll.
- En lokal modell måste erbjuda minst 16 k tokens kontext, eftersom segmenten
  kan vara upp till 16 000 tecken. Ollama konfigurerar ofta 4 096: använd
  en `Modelfile` med `PARAMETER num_ctx 32768`.
- `--eco` har ingen effekt; `--reasoning_effort` skickas vidare oförändrad som
  OpenCodes `--variant`.
- OpenCode loggar varje session i `~/.local/share/opencode/`.
- Variabler: `OPENCODE_BIN` (annars `PATH`, sedan `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (sekunder per segment, standard 600). `OPENCODE_CONFIG`
  skickas vidare oförändrad till OpenCode.

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

`reasoningEffort: "none"` stänger av det tänkande som Ollama aktiverar som standard för dessa
modeller och som en Modelfile inte kan inaktivera. Uppmätt för en mening med
sex ord: 919 resonemangstokens och 68 sekunder utan alternativet, 9 tokens med det.

### Till fler än 400 modeller: `--use_openrouter`

OpenRouter är en router som debiteras efter användning, från ett gemensamt kreditsaldo, för
modeller som driftas av tredje part — däribland öppna kinesiska modeller som ingen
annan provider erbjuder här.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` är obligatorisk. En förkontroll som körs före all debitering hanterar
två särdrag i routningen:

- **Samma modell tillhandahålls av dussintals värdar med olika
  gränser** — för `z-ai/glm-5.3-flash` finns 23 värdar, varav en är begränsad till
  2 048 utmatningstokens. Förkontrollen läser `/api/v1/models/{modèle}/endpoints`,
  utesluter värdar med färre än 8 000 utmatningstokens eller försämrad status och
  låser valet till de övriga med `allow_fallbacks: false`.
- **Resonemang debiteras till utmatningspriset** — 107 tokens jämfört med 2 för
  ett ”OK”-svar från `z-ai/glm-5.2`. Det stängs av som standard; modeller
  som kräver det får den lägsta ansträngningsnivå de accepterar, eftersom katalogens
  standardvärde kan fylla utmatningen innan översättningen är färdig.
  `--reasoning_effort` har fortfarande företräde.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Kontextfönstret hämtas från katalogen. En modell med färre än 16 400 tokens
  avvisas före något anrop: 8 400 för prompten och segmentet, minst 8 000
  för utmatningen.
- En slug som saknas i katalogen, en katalog som inte går att nå eller avsaknad
  av en värd som klarar gränsen stoppar kommandot.
- `finish_reason=length` med tom utmatning innebär att budgeten har förbrukats av
  resonemang, inte att svaret har trunkerats: meddelandet skiljer på detta.
- `--eco` har ingen effekt.
- Variabler: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (standard `https://openrouter.ai/api/v1`, `https://`
  krävs), `OPENROUTER_TIMEOUT` (standard 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (standard 30).

### Översättningsnot

`--add_translation_note` lägger till en not, i `bottom` (standard), `top` (efter
front matter) eller `both` (`--note_position`), i formatet `legacy` (stycke i
fetstil, standard) eller `marker` (`--note_format`). Formatet `marker` är en
osynlig referensdefinition i Markdown,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
följd av ett citat i fetstil: läsbart på GitHub och möjligt att bearbeta vid build med en
remark-plugin.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detaljerade mätningar

Alla mätningar är översättningar som faktiskt har körts med `aipmt`, till
fjorton språk: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Skrivna** räknar de filer som kontrollerna har släppt igenom; **Utan
avvikelse** de där `scripts/compare_structure.py` inte hittar något — samma antal
avsnitt, underrubriker, länkar, unika URL:er, kodblock,
inline-koder, tabellrader, citatblock och ord i fetstil.

”Utan avvikelse” betyder ”inget upptäckt”, inte ”identiskt”: jämförelseverktyget
räknar element utan att läsa deras innehåll. Det rapporterar varken en borttagen rubrik på
nivå 4, ersatt text i inline-kod, en utbytt
flagga eller en intern länk som återges med en parentes för mycket,
`[texte]((#ancre))`, och inte längre leder någonstans — och det bedömer inte
språket.

### Innehållsrik omvärldsartikel, läget `--news`

En utgåva av [AI-bevakningen på jls42.org](https://jls42.org/fr/news):
589 rader, 140 länkar, 21 avsnitt, 3 skyddade engelska citat. Mätomgång
den 4 och 5 september 2026.

| Modell                                          | Åtkomst              | Skrivna | Utan avvikelse   | Median/språk |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | API Google         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google-abonnemang  | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google-abonnemang  | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `claude-sonnet-5-5`                             | API Anthropic      | 14/14   | ✅ **14/14** | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT-abonnemang | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | Claude-abonnemang  | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | API Anthropic      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | Claude-abonnemang  | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `claude-haiku-5-5`                              | API Anthropic      | 14/14   | ⚠️ 11/14     | 2 min 54 s     |
| `claude-haiku-4-5`                              | API Anthropic      | 14/14   | ⚠️ 7/14      | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | lokal              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | API Mistral        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok-abonnemang    | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | Claude-abonnemang  | 0/14    | ❌ 0/14      | —              |

Grok mättes på nytt den 9 september på en annan utgåva av samma bevakning
(356 rader): 9 skrivna språk av 14, 8 utan avvikelse. Det är den siffran som
visas i den inledande tabellen. Tre avbrutna mätomgångar redovisas
inte: `qwen3.5-27b` (9 språk) och `kimi-k2.6` (4) på grund av slut på krediter,
`z-ai/glm-5.3-flash` vars två misslyckanden berodde på en resonemangsinställning
som providern sedan dess korrigerar. OpenRouter-raderna mättes med
routerns standardinställningar, före `--use_openrouter`; `z-ai/glm-5.2`,
som mättes på nytt med den levererade providern, ger samma 14/14. Siffrorna
räknades om den 10 september med det nuvarande jämförelseverktyget: `qwen3.8-flash` och
`qwen3.7-flash` får vardera ett språk till jämfört med den första
publiceringen, övriga är oförändrade.

Raderna för `--use_antigravity` mättes den 26 september på samma
artikel, med fyra översättningar parallellt: `gemini-3.7-flash-medium` på förmiddagen,
`gemini-3.8-flash-medium` på eftermiddagen. På engelska tog båda själva bort
de tre raderna med fransk översättning under citaten, utan att hitta på någon
flagga, och de engelska citaten är intakta: reservrensningen behövde
inte göra något. I `--eco` (`gemini-3.7-flash-low`), på endast fyra språk
(en, ja, ar, hi): 4 skrivna av 4, alla utan avvikelse, med en median på 1 min 52 s.
Kontrollmätning samma dag på en nyare utgåva av bevakningen,
den från den 25 september (438 rader, 2 engelska citat), översatt utanför
bloggen med `gemini-3.7-flash-medium`: 14 skrivna av 14, alla utan avvikelse, 87 till
128 s per språk.

Raderna för `--use_claude_code` mättes den 26 september på samma
artikel, med fyra översättningar parallellt och ansträngningsnivån `low`. Med `sonnet` är de
engelska citaten intakta på alla fjorton språk och på engelska tog
modellen själv bort raderna med fransk översättning, utan att hitta på någon
flagga. `opus` skrev inget språk: på vart och ett stoppade dess skyddsmekanismer
svaret vid det sista segmentet, på grund av en kort notis om 279 molekyler
genererade för ett bindningsställe. När notisen skickas separat avvisas den
under kategorin ”bio”; `sonnet` översatte den till alla språk. `haiku` skriver
alla fjorton språk; på tre (en, pl, ro) ändras en avsnittsrubrik från
nivå 2 till nivå 1. Den resonerar utan att det går att förhindra — 61 % av
dess utmatningstokens — vilket ger mer än dubbelt så lång tid som `sonnet`.

Raderna för `claude-sonnet-5-5`, `claude-haiku-5-5` och `claude-haiku-4-5`
mättes den 18 oktober via Anthropics API, på samma artikel, med fyra
översättningar parallellt per modell. Sonnet 5.5 tillåter inte att dess
tänkande stängs av: aipmt skickar den lägsta inställning den accepterar, och dess
svar innehåller inget sådant. Den skriver alla fjorton språk utan avvikelse och utan att
köra om något segment; på engelska tog den själv bort raderna med
fransk översättning, utan att hitta på någon flagga, och de engelska citaten är
intakta överallt. Haiku 5.5 mäts med sitt adaptiva tänkande: med tänkandet
avstängt lämnade den hela stycken på franska, vilket kontrollen avvisar —
3 skrivna språk av 14. Båda Haiku-modellerna stöter på problem med samma notis: Haiku 5.5
ändrar rubrikens nivå eller dubblerar den på japanska, koreanska och
kinesiska, medan Haiku 4.5 ändrar den till nivå 1 på sju språk och lämnar den
på franska i den japanska översättningen. Haiku 4.5 kostar 3,67 $ för båda dokumenten på
alla fjorton språk, Haiku 5.5 0,57 $, Sonnet 5.5 9,21 $.
### Projektets README, standard-Markdown

Version låst den 9 september 2026: 785 rader, 285 inline-koder, 40
blockavslutningar, 89 tabellrader. Fyra översättningar parallellt.

| Modell                                          | Skrivna | Utan avvikelser | Median/språk | Vad som skiljer sig                                                       |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | inget                                                                    |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | inget                                                                    |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | inget enligt jämförelseverktyget; dubblerade interna länkar (en)          |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | inget                                                                    |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | inget                                                                    |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | ett ord i fetstil (ja)                                                   |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | ett ord i fetstil (ko)                                                   |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | en tabellrad sammanfogad med föregående rad (ar)                          |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | en länk (sv), ett ord i fetstil (zh)                                     |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | ett ord i fetstil (ar, ja)                                               |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | ett ord i fetstil (hi, ja, ko)                                           |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 40 inline-koder tillagda på arabiska; fetstil (hi, ja, ko)                 |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2 språk avvisade (ar, hi): inline-koder saknades i svaret                  |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | ett avsnitt saknas (ar, hi, ko); kodblock tillagda (ja, ko, ro, zh)        |

Två avbrutna testomgångar har inte betygsatts: Grok, vars CLI-session löpte ut
efter tolv språk (elva utan avvikelser), och `qwen3.8-flash`, vars
värdleverantör gav HTTP 429 efter två. `opencode/mimo-v2.5-free` och `ollama/gpt-oss-20b-32k`
mättes inte på nytt med denna version; med versionen från den 4 och 5 september,
som var 277 rader kortare, skrev de vardera 9 översättningar av 14, varav 7
respektive 1 utan avvikelser.

Raderna `--use_antigravity` och `--use_claude_code` mättes inte med
den låsta versionen, utan den 26 september med den som publicerades med 1.14.0 — och
raderna `claude-sonnet-5-5`, `claude-haiku-5-5` och `claude-haiku-4-5` den 18
oktober, med samma version: 600 rader, 257 inline-koder, 30 blockavslutningar, 85
tabellrader. Eftersom den är
185 rader kortare kan den inte jämföras direkt med de andra raderna;
dessa rader kan däremot jämföras med varandra. Vad gäller interna länkar, som
jämförelseverktyget inte kontrollerar, bevarade `gemini-3.8-flash-medium` dem intakta på
alla fjorton språk, medan `gemini-3.7-flash-medium` bröt dem på italienska;
`sonnet` och `opus` bevarade dem intakta överallt, medan `haiku` dubblerade dem på
engelska; `claude-sonnet-5-5` och `claude-haiku-4-5` bevarade dem intakta på
alla fjorton språk, och `claude-haiku-5-5` på de tolv som den skrev.

### Fyra README-filer från välkända projekt

FastAPI, Ollama, tldr-pages och Vue.js, hämtade oförändrade från GitHub —
enklare dokument än de två föregående. Testomgången riktade sig till modeller
som hade svårigheter; Gemini används som jämförelsepunkt.

| Modell                    | Omfattning                 | Skrivna | Utan avvikelser |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 projekt × 14 språk      | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 projekt × 14 språk      | 55/56   | ❌ 47/56     |
| `grok-4.6` (abonnemang)   | 4 projekt × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 projekt × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### Vad dessa mätningar inte är

- **Ingen heltäckande rangordning**: enbart OpenRouter erbjuder över fyra hundra
  modeller, och ungefär femton har mätts.
- **Ungefärliga tider**: tre till sex översättningar parallellt beroende på
  testomgång, och en leverantörs kapacitet varierar under dagen.
- **Tidsbundna observationer**: modeller förändras under samma namn, och era
  dokument är inte våra.

För att upprepa mätningen med era dokument, på en låst kopia av filen:

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

De 28 översättningarna i repot (README och CHANGELOG, fjorton språk)
genereras på nytt med `./regen_translations.sh --force` — Codex och `gpt-6.1-sol` använder
ChatGPT-abonnemanget som standard, fyra parallellt. `REGEN_PROVIDER` och
`REGEN_MODEL` ändrar tillvägagångssättet: `antigravity` använder fortfarande ett abonnemang, Googles,
och tillåts utan undantag; ett avgiftsbelagt API (`openai`, `gemini`,
`grok`, `openrouter`) nekas utan `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` begränsar tiden för varje jobb (600 s, 1 800 s för Codex och
Antigravity). Detaljer om verktygen finns i `CLAUDE.md`.

## Projekt som använder detta skript

- **[jls42.org](https://jls42.org)** — personlig blogg publicerad på 15 språk. Dess
  [dagliga AI-omvärldsbevakning](https://jls42.org/fr/news) översätts varje dag
  med detta verktyg och används som referensdokument för mätningarna ovan.

## Författare

Julien LE SAUX
E-post: contact@jls42.org

## Licens

GNU GENERAL PUBLIC LICENSE Version 3. Se [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Varning

Detta program distribueras **utan någon som helst garanti**, enligt
avsnitt 15 och 16 i GPL v3: det tillhandahålls i ”befintligt skick”, utan garanti för
säljbarhet eller lämplighet för ett visst ändamål, och författaren kan inte
hållas ansvarig för skador som uppstår vid användning. Licenstexten
har företräde framför denna sammanfattning.

- **Läs igenom före publicering.** Skydden omfattar kodblock,
  inline-kod, URL:er, ankare och citat i läget `--news` — varken
  rubriker, tabeller, front matter eller innebörden i era meningar.
- **Era dokument skickas till den valda leverantören**, enligt dess
  användarvillkor och datapolicy. Vissa gratismodeller kan
  återanvända era konversationer för träning, och Antigravitys villkor
  tillåter Google att återanvända dem och låta människor granska dem,
  även med ett betalt abonnemang; en lokal modell är det enda alternativet där
  inga data lämnar er dator.
- **Ni debiteras för API-anropen.** Detta program sätter inget tak för
  kostnaden: ett långt dokument, ett nytt försök efter ett misslyckande eller en modell som resonerar
  mycket kostar mer.
- **De publicerade mätningarna är tidsbundna observationer**, inga garantier.

De produkt- och företagsnamn som nämns tillhör sina respektive
innehavare. Detta projekt har ingen koppling till någon av dem.

**Artikel översatt från franska till svenska med gpt-6.1-sol.**

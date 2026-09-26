# Traducător Markdown AI-Powered

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Calitatea codului</h4>

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

Traduce fișiere Markdown dintr-o limbă în alta, păstrând structura: blocuri de
cod, cod inline, URL-uri, ancore, tabele și front matter. Unsprezece moduri de a
apela un model — cinci API-uri, patru abonamente fără facturare per utilizare,
două routere — și o măsurătoare publicată a ceea ce păstrează cu adevărat
fiecare model.

## Pe scurt

- **Unsprezece căi de provider**: API-urile OpenAI, Mistral, Claude, Gemini și
  Grok; abonamente ChatGPT (Codex), Grok, Google (Antigravity) și Claude (Claude
  Code) fără facturare per utilizare; routerele OpenCode (open source, gratuit sau local)
  și OpenRouter (peste 400 de modele).
- **Nimic eronat din cauza unui token pierdut**: blocurile de cod, codul inline,
  URL-urile, ancorele și citatele sunt înlocuite cu tokenuri înainte de apel și
  verificate la întoarcere. Dacă lipsește vreunul, fișierul nu este scris.
- **Documente lungi**: segmentare în funcție de fereastra modelului.
- **Modul `--news`**: citate în engleză protejate și steaguri gestionate per
  limbă, pentru articolele de monitorizare.
- **Modul `--eco`**: modele rapide și mai ieftine.
- **Notă de traducere** opțională, în partea de sus, în partea de jos sau în ambele.

## Instalare

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 sau mai recent. Pentru instalare din depozit, consultați
[Contribuire](#contribuire).

## Configurare

Cheile sunt citite din trei locuri, de la cea mai mare prioritate la cea mai
mică; fiecare completează doar ceea ce precedentul lasă gol.

|     | Unde                                          | Pentru ce                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variabile de mediu                            | CI, containere, derogare punctuală    |
| 2   | `.env` din directorul curent (sau dintr-un părinte) | o cheie specifică unui proiect        |
| 3   | `~/.config/aipmt/.env`                        | instalat o singură dată, valabil peste tot |

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

`GEMINI_API_KEY` este acceptat în locul `GOOGLE_API_KEY`. Fișierul utilizatorului
respectă `XDG_CONFIG_HOME` (doar cale absolută) și `%APPDATA%` sub Windows. Fără
nicio cheie, comanda enumeră cele trei locații.

**Fișierul `.env` al unui proiect nu poate nici redirecționa apelurile, nici
alege programul executat.** Acesta furnizează chei, niciodată o destinație sau un
binar: orice variabilă din `_BASE_URL`, `_API_BASE`, `_ENDPOINT` sau `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, proxy-urile (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), depozitele de certificate (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) și `XDG_CONFIG_HOME` /
`APPDATA` sunt ignorate acolo, cu un avertisment. Un depozit clonat nu trebuie
să vă poată deturna cheia și nici să vă facă să rulați propriul său program la
prima traducere. Acest fișier este citit și fără interpolare:
`NOM=${OPENAI_API_KEY}` nu recopiază cheia în el. Setați aceste variabile în
mediu sau în `~/.config/aipmt/.env`.

Variabile opționale: `XAI_BASE_URL` (implicit `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (secunde per apel, implicit 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(implicit 600), `GROK_BIN`, `GROK_HOME` (implicit `~/.grok`), `GROK_TIMEOUT`
(implicit 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (implicit 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (implicit 600), `OPENROUTER_BASE_URL`
(`https://` obligatoriu), `OPENROUTER_TIMEOUT` (implicit 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (implicit 30). Fiecare este detaliată în
secțiunea providerului său.

## Primii pași

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` tradus în spaniolă generează `document-es.md` în `--target_dir`;
cu `--include_model`, `document-es-gpt-5.6-terra.md`. Extensia devine
întotdeauna `.md` — `article.mdx` generează `article-en.md` — cu excepția
utilizării `--keep_filename`, care păstrează numele original. O traducere deja existentă
este omisă fără `--force`.

Coduri de ieșire: `0` dacă totul a reușit sau a fost omis, `1` dacă a rămas vreun fișier
eșuat (listat la ieșirea de eroare standard), `2` dacă problema este de configurare.
Un fișier eșuat nu este niciodată scris, chiar dacă scrierea în sine eșuează:
conținutul este scris alături și apoi redenumit. Este suficient să relansați.

## Ce model să alegeți

Măsurat pe două documente reale, traduse în aceleași paisprezece limbi de
fiecare model. **Cifra reprezintă numărul de limbi, din paisprezece, în care
traducerea este scrisă și în care nimic nu diferă față de sursă.**

| Model                | Cum se accesează                  | Articol dens de monitorizare | Acest README | Ce diferă și în câte limbi                                                                                                                                        |
| -------------------- | --------------------------------- | ---------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash** | abonament Google (Antigravity)    | ✅ 14/14                     | ✅ 14/14     | nimic, pe niciunul dintre cele două documente                                                                                                                      |
| **Gemini 3.7 Flash** | cheie API Google                  | ✅ 14/14                     | ⚠️ 13/14     | 1 limbă din 14: un cuvânt aldin în plus (ja)                                                                                                                       |
| **Gemini 3.7 Flash** | abonament Google (Antigravity)    | ✅ 14/14                     | ⚠️ 13/14     | 1 limbă din 14: un cuvânt aldin în minus (ko)                                                                                                                      |
| **GPT-5.6 Sol**      | abonament ChatGPT sau cheie OpenAI| ✅ 14/14                     | ⚠️ 12/14     | 2 limbi din 14: un cuvânt aldin în minus (ar, ja)                                                                                                                  |
| **GLM-5.2**          | cheie OpenRouter                  | ✅ 14/14                     | ⚠️ 11/14     | 3 limbi din 14: un cuvânt aldin în minus (hi, ja, ko)                                                                                                              |
| Claude Sonnet 5      | abonament Claude (Claude Code)    | ⚠️ 13/14                     | ⚠️ 13/14     | 1 limbă din 14 la articol: un cuvânt aldin în plus (zh); 1 la acest README: un rând de tabel lipit de cel anterior, ascuns la afișare (ar)                       |
| Claude Haiku 4.5     | abonament Claude (Claude Code)    | ⚠️ 11/14                     | ✅ 14/14     | 3 limbi la articol: un titlu de secțiune trecut la nivelul 1 (en, pl, ro); la acest README, nimic pentru comparator, dar linkurile interne dublate în engleză    |
| Claude Sonnet 5      | cheie API Anthropic               | ⚠️ 11/14                     | ⚠️ 12/14     | 3 limbi la articol: a apărut un bloc de cod (es, de, hi); 2 la acest README: un link fără marcajul său (sv), un cuvânt aldin (zh)                                 |
| Qwen 3.7 Flash       | cheie OpenRouter                  | ❌ 8/14                      | ⚠️ 10/14     | 1 limbă refuzată la articol, alte 5 deviază; la acest README, vreo patruzeci de cuvinte puse în `code` (ar)                                                |
| Grok 4.6             | abonament Grok                    | ❌ 8/14                      | neevaluat    | 5 limbi refuzate din 14, din lipsă de coduri inline și URL-uri redate; olandeza deviază în totalitate                                                             |
| GPT-OSS 20B          | model local (Ollama)              | ❌ 7/14                      | nemăsurat din nou | 4 limbi refuzate din 14: modelul lăsa pasaje în franceză, filtrul de siguranță le-a oprit                                                                     |
| MiMo v2.5 (gratuit)  | OpenCode Zen, fără cont           | ❌ 11/14                     | nemăsurat din nou | 1 limbă refuzată; o secțiune pierdută în poloneză                                                                                                                  |
| Mistral Large        | cheie API Mistral                 | ❌ 5/14                      | ❌ 1/14      | **o secțiune întreagă dispare**: 1 limbă la articol (hi), 3 la acest README (ar, hi, ko) — și 3 limbi refuzate la articol                                          |
| DeepSeek V4 Flash    | cheie OpenRouter                  | ❌ 3/14                      | nemăsurat din nou | 10 limbi refuzate din 14; 37 de minute per limbă                                                                                                                  |
| Claude Opus 5.5      | abonament Claude (Claude Code)    | ❌ 0/14                      | ✅ 14/14     | articolul refuzat în toate cele 14 limbi de filtrele de siguranță ale Opus, din cauza unei știri scurte de biologie; nimic la acest README                         |

|     | Ce indică simbolul                                                                                                                                                                                   |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | toate cele paisprezece limbi traduse și nimic nu diferă față de sursă                                                                                                                                |
| ⚠️  | toate cele paisprezece limbi traduse; ceea ce diferă ține de **marcare** — un cuvânt aldin, un `code`, un link care își pierde parantezele drepte. Nu lipsește niciun text, niciun URL, niciun bloc de cod, nicio secțiune |
| ❌  | cel puțin o limbă nu a putut fi tradusă — fișierul este refuzat, nu este scris — **sau** lipsește conținut dintr-un fișier scris                                                                    |

Ce trebuie reținut:

- **O traducere refuzată nu este o traducere deteriorată.** Atunci când lipsește
  un token la întoarcere, fișierul nu este scris, iar limba este considerată
  refuzată. Asta i se întâmplă lui Grok la articol: patru coduri inline și
  trei URL-uri pierdute încă de la primul segment, pe cele cinci sisteme de scriere non-latine.
- **Un model poate refuza un document întreg din cauza unei singure propoziții.** Opus 5.5
  traduce acest README fără nicio abatere, dar niciun articol de monitorizare:
  filtrele sale de siguranță opresc răspunsul la o scurtă știre de biologie. Fișierul nu este
  scris, iar aipmt explică motivul.
- **Această plasă de siguranță nu acoperă titlurile, tabelele, front matter-ul și nici
  textul.** Un model care elimină o secțiune generează un fișier pe care instrumentul îl scrie
  fără ezitare — este cazul Mistral. Aceste elemente nu pot fi
  înlocuite cu un token, iar mecanismele actuale de protecție nu le verifică;
  `scripts/compare_structure.py` detectează o secțiune pierdută, dar abia după aceea.
- **Grok nu are o notă pe acest README**: sesiunea sa CLI a expirat după douăsprezece
  limbi, dintre care unsprezece fără abateri. O campanie întreruptă nu se notează.
- **Densitatea documentului contează mai mult decât limba.** Grok face față la
  README-uri obișnuite și clachează la un articol încărcat cu linkuri, inclusiv în
  olandeză.

Date și documente: coloana „Acest README” a fost măsurată pe 9 septembrie 2026
pe o revizie înghețată a acestui fișier (785 de linii, 285 de coduri inline, 89 de rânduri
de tabel), retușată între timp — cu excepția rândurilor Antigravity și Claude Code,
măsurate pe 26 septembrie pe revizia publicată cu versiunea 1.14.0, mai scurtă
(600 de linii, 257 de coduri inline, 85 de rânduri de tabel). Coloana „Articol de
monitorizare dens” provine din campania din 4 și 5 septembrie pe un articol de 589
de linii, cu excepția rândului Grok, remăsurat pe 9 septembrie pe o altă ediție a
aceleiași monitorizări, și a rândurilor Antigravity și Claude Code, măsurate pe 26 septembrie
pe același articol. Tabelele complete, duratele și protocolul se găsesc în
[Măsurători detaliate](#măsurători-detaliate).

## Toate opțiunile

| Opțiune                  | Descriere                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Fișier Markdown unic de tradus (alternativă la `--source_dir`)                                             |
| `--source_dir`           | Director sursă care conține fișierele Markdown (implicit: `content/posts`)                                   |
| `--target_dir`           | Director de ieșire pentru fișierele traduse (implicit: `traductions_en`)                                    |
| `--source_lang`          | Limba sursă (implicit: `fr`)                                                                                  |
| `--target_lang`          | Limba țintă (implicit: `en`)                                                                                   |
| `--model`                | Model specific de utilizat                                                                                  |
| `--eco`                  | Folosește modelele economice                                                                              |
| `--use_mistral`          | Folosește API-ul Mistral AI                                                                                     |
| `--use_claude`           | Folosește API-ul Claude                                                                                         |
| `--use_gemini`           | Folosește API-ul Gemini                                                                                         |
| `--use_grok`             | Folosește API-ul xAI (Grok) — necesită `XAI_API_KEY`                                                           |
| `--use_codex`            | Folosește CLI-ul Codex pe cota abonamentului ChatGPT                                                    |
| `--use_grok_cli`         | Folosește CLI-ul Grok pe cota abonamentului Grok                                                        |
| `--use_antigravity`      | Folosește CLI-ul Antigravity (`agy`) pe cota abonamentului Google AI Pro sau Ultra                       |
| `--use_claude_code`      | Folosește CLI-ul Claude Code (`claude -p`) pe cota abonamentului Claude Pro sau Max                      |
| `--use_opencode`         | Folosește OpenCode (open source) către furnizorul configurat în OpenCode; necesită `--model provider/modèle` |
| `--use_openrouter`       | Folosește OpenRouter — necesită `OPENROUTER_API_KEY` și `--model fournisseur/modèle`                          |
| `--force`                | Forțează retraducerea                                                                                       |
| `--keep_filename`        | Păstrează numele de fișier original                                                                          |
| `--news`                 | Mod știri: protejează citatele EN, gestionează steagurile pe limbă                                      |
| `--add_translation_note` | Adaugă o notă de traducere                                                                                |
| `--note_position`        | Poziția notei: `top`, `bottom` (implicit), sau `both`                                                     |
| `--note_format`          | Formatul notei: `legacy` (implicit, paragraf aldin) sau `marker`                                            |
| `--include_model`        | Include numele modelului în fișierul de ieșire                                                            |
| `--reasoning_effort`     | Efort de raționament GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

Cele nouă flag-uri `--use_*` sunt reciproc exclusive: combinarea a două dintre ele este
refuzată.

## Furnizori

### Prin API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` comută pe nivelul economic al fiecărui furnizor.

| Furnizor    | Calitate (implicit)                                   | Economic (`--eco`)|
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`           |
| Claude      | `claude-sonnet-5`                                     | `claude-haiku-4-5`           |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`           |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`           |
| Codex       | `gpt-5.6-sol` (de asemenea `terra` și `luna` prin `--model`) | `gpt-5.6-luna`           |
| Grok API    | `grok-4.6`                                            | `grok-4.3`           |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`           |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`           |
| Claude Code | `sonnet`, efort `low`                                | idem — `--eco` fără efect |
| OpenCode    | `--model provider/modèle` obligatoriu                 | idem — `--eco` fără efect |
| OpenRouter  | `--model fournisseur/modèle` obligatoriu              | idem — `--eco` fără efect |

### Pe abonamentul ChatGPT: `--use_codex`

Controlează CLI-ul oficial Codex: traducerea este dedusă din cota
abonamentului ChatGPT, fără cheie API sau facturare pe bază de utilizare.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Binarul este căutat în `CODEX_BIN`, apoi în `PATH`, apoi în pachetul
  `openai-codex-cli-bin`. `~/.codex/auth.json` nu este citit niciodată.
- `OPENAI_API_KEY` și `CODEX_API_KEY` sunt eliminate din mediul
  subprocesului: o cheie prezentă nu comută niciodată către API.
- Fiecare segment costă cel puțin un „mesaj” din fereastra de 5 ore — două
  dacă validarea sa eșuează și este reîncercat. OpenAI anunță, ca
  estimare, 250–2.000 de mesaje/5 h pentru `gpt-5.6-luna` (`--eco`) și
  10–100 pentru `gpt-5.6-sol` pe un plan Plus.
- `--model gpt-5.6-terra` și `--model gpt-5.6-luna` trec de asemenea prin
  abonament. Un model la care contul nu are dreptul returnează un cod 400 „model is
  not supported when using Codex with a ChatGPT account”.
- Mai lent decât un API, iar diferența crește odată cu documentul: pe acest README,
  6 min 46 s pe limbă ca mediană cu `gpt-5.6-sol`, față de 36 s pentru
  `gemini-3.7-flash`.
- Refuzat în CI (`CI` sau `GITHUB_ACTIONS` definit): abonamentul se autentifică
  printr-un fișier de sesiune personal, care nu are ce căuta pe un runner
  partajat.
- Variabile: `CODEX_BIN`, `CODEX_TIMEOUT` (secunde per segment, implicit 600).

### Pe abonamentul Grok: `--use_grok_cli`

Același principiu cu CLI-ul oficial Grok Build, pe abonamentul SuperGrok sau
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Izolare mai slabă decât Codex.** Sandbox-ul OS al lui Grok nu se aplică
  pe multe mașini Linux recente (AppArmor, socket-uri de runtime de
  containere), iar un profil care nu poate fi aplicat pornește neizolat în
  mod silențios. Prin urmare, scriptul nu solicită niciun profil în mod implicit, îl
  anunță și se bazează pe regulile `--deny` ale CLI-ului, inclusiv pe catch-all-ul `*` — singurul
  strat care refuză să pornească în loc să elimine protecția fără avertisment.
  `GROK_TRANSLATE_SANDBOX=read-only` impune sandbox-ul OS, iar pornirea
  eșuează dacă mașina nu îl poate onora.
- Cota este săptămânală, partajată cu Chat, Imagine și Voice, și nicio
  comandă nu permite citirea acesteia: un lot poate consuma din utilizarea conversațională
  fără nicio notificare.
- Variabile: `GROK_BIN`, `GROK_HOME` (directorul CLI-ului, implicit `~/.grok`),
  `GROK_TIMEOUT` (implicit 900), `GROK_TRANSLATE_SANDBOX`.

### Pe abonamentul Google: `--use_antigravity`

Același principiu cu `agy`, CLI-ul oficial al Antigravity: pentru cei care plătesc Google
AI Pro sau Ultra, traducerea este dedusă din cota abonamentului în loc
să fie facturată per token. Aceasta este singura cale către această cotă: Gemini CLI nu
mai deservește aceste conturi din 18 iunie 2026
([anunț](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
iar SDK-ul Antigravity acceptă doar o cheie API sau un proiect Google Cloud.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Nicio cale cu plată nu rămâne deschisă.** agy primește din mediul
  dumneavoastră doar o listă restrânsă de variabile — `PATH`, limbă și fus orar,
  terminal, identitate, proxy-uri și certificate, magistrală de sesiune — și nicio cheie:
  mai multe dintre variabilele sale comută un apel fără să afișeze nimic (măsurat:
  una trimite documentul către un gateway terț, alta către un proiect
  Google Cloud facturat), iar o listă de excludere omitea câte ceva la fiecare verificare.
  Înainte de orice segment, `agy -p /config`, care nu consumă din cotă, trebuie să arate
  creditele IA plătite dezactivate, fără cheie API sau proiect Google Cloud — o
  setare lipsă înseamnă refuz —, altfel nimic nu este tradus; jurnalul fiecărui
  apel trebuie apoi să ateste abonamentul (`authMethod=consumer`), altfel
  răspunsul este refuzat.
- **Izolare.** Fiecare apel rulează într-un director personal privat și
  de unică folosință, cu un agent de traducere fără instrumente: setările, regulile,
  pluginurile, serverele MCP și hook-urile dumneavoastră agy nu pătrund acolo, nimic nu se adaugă la
  istoricul dumneavoastră, iar conexiunea rămâne în keyring, pe care aipmt nu îl citește niciodată.
  Un agent negăsit face ca agy să revină, în mod silențios, la agentul său de codare
  și la instrumentele sale: o linie întreagă din jurnal trebuie să confirme agentul corect — un
  document care citează acest mesaj nu o înlocuiește —, altfel se refuză.
- **Platforme**: Linux, într-o sesiune care are un keyring (magistrală de sesiune
  D-Bus, Secret Service); macOS este acceptat, fără a fi fost măsurat acolo. Refuzat
  pe Windows, unde agy nu citește variabilele care izolează fiecare apel, și
  pe Linux fără magistrală de sesiune — sesiune SSH, container, server: agy își
  stochează acolo tokenul într-un fișier din `~/.gemini`, pe care izolarea îl maschează.
  Refuzul vine înainte de orice lansare, cu motivul aferent, în loc de un minut
  de așteptare pentru un cod de conectare.
- **Modele**: cele din `agy models`. Modelele Gemini includ efortul în numele lor
  (`gemini-3.8-flash-medium`…): un nume fără sufix este refuzat înainte de apel,
  iar `--reasoning_effort` nu are efect. Implicit `gemini-3.8-flash-medium`,
  și `gemini-3.7-flash-low` în `--eco`; campaniile care le-au stabilit sunt
  descrise în [Măsurători detaliate](#măsurători-detaliate). Claude și GPT-OSS
  au propria lor cotă, mult mai mică: aproximativ 1% din fereastra de
  5 ore per apel măsurat, față de 0,05% pentru Flash.
- **Cotă**: pe grupuri, o fereastră de 5 ore și una săptămânală,
  proporțional cu costul în tokenuri. Măsurat pe contul autorului: aproximativ
  16 puncte din fereastra de 5 ore per milion de caractere sursă în
  `gemini-3.8-flash-medium`, 14 în `gemini-3.7-flash-medium` și 7 până la 8 la
  efort scăzut — un README de 40.000 de caractere costă deci puțin peste o
  jumătate de punct. Limita săptămânală depinde de nivelul abonamentului. Reîncercarea respectă
  ceea ce agy declară ca fiind reîncercabil; în caz contrar, o fereastră epuizată nu este
  reîncercată niciodată: aceasta face să eșueze fiecare fișier până la resetarea
  afișată de `/usage`.
- **Mai lent decât API-ul**: pe articolul dens al măsurătorilor, 3 min 59 s pe
  limbă ca mediană în `gemini-3.8-flash-medium` și 3 min 14 s în
  `gemini-3.7-flash-medium`, față de 1 min 18 s pentru Gemini 3.7 Flash prin API.
- **Întrerupere**: Ctrl-C sau un terminal închis opresc agy odată cu
  comanda, în loc să îl lase să își finalizeze rândul consumându-vă din cotă; același lucru
  este valabil pentru Codex, Grok CLI și OpenCode. Sub `nohup`, traducerea continuă.
- Refuzat în CI (`CI` sau `GITHUB_ACTIONS` definit): conexiunea se află într-un
  keyring personal. Pe un runner, folosiți `--use_gemini` cu `GOOGLE_API_KEY`.
- Variabile: `AGY_BIN` (altfel `PATH`, apoi `~/.local/bin/agy`),
  `AGY_TIMEOUT` (secunde per segment, inclusiv pornirea, implicit 900).

**Termeni de utilizare: este angajat contul dumneavoastră.** [Termenii
Antigravity](https://antigravity.google/terms) (secțiunea 6) și
[FAQ-ul](https://antigravity.google/docs/faq/) aferent interzic accesarea serviciului
printr-un software terț folosind conexiunea Antigravity — Claude Code,
OpenClaw și OpenCode sunt menționate acolo —, sub sancțiunea suspendării contului. aipmt
nu citește și nu reutilizează tokenul: acesta lansează binarul oficial în
[modul headless](https://antigravity.google/docs/cli/headless/) pe care Google
îl documentează pentru scripturi și CI. Un membru Google a considerat „standard”
lansarea `agy -p` dintr-un script local pentru propria activitate
([forum oficial, 25 septembrie 2026, răspuns fără valoare contractuală](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
niciun text nu tranșează cazul unui instrument distribuit precum acesta.

**Doar documente publice.** Conform secțiunii 5 din aceiași termeni,
schimburile — prompturi, răspunsuri, metadate — pot fi utilizate pentru a îmbunătăți
produsele și învățarea automată Google și pot fi revizuite de
oameni, inclusiv în cazul abonamentelor plătite. Renunțarea se face prin setarea
`enableTelemetry`, cu efect nedocumentat, pe care aipmt nu o configurează; setările
dumneavoastră din agy nu sunt transmise în mediul său izolat. Nu treceți nimic confidențial prin acesta.

### Pe abonamentul Claude: `--use_claude_code`

Același principiu cu `claude`, CLI-ul oficial al Claude Code, în modul `-p`: pentru
cine plătește Claude Pro sau Max, traducerea este dedusă din cota
abonamentului în loc să fie facturată per token. A nu se confunda cu
`--use_claude`, API-ul Anthropic, facturat la utilizare.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Nicio cale plătită nu rămâne deschisă, iar fiecare apel dovedește acest lucru.** Claude
  Code primește din mediul dumneavoastră doar o listă închisă de variabile — nicio
  cheie API, niciun token, niciun furnizor de cloud, niciun marker al sesiunii Claude Code
  din care ar fi lansat aipmt. Înainte de primul segment, `claude auth status` trebuie
  să arate conexiunea de abonament, fără cheie Console, iar `/usage`, care nu consumă
  din cotă, trebuie să ateste acest lucru; fiecare apel îl atestă la rândul său în
  evenimentul său de inițializare, altfel răspunsul este refuzat.
- **Dezactivați „extra usage”** (claude.ai, Setări → Utilizare) pentru
  ca zero euro să rămână valabil: dacă este activat, preia ștafeta după epuizarea unei ferestre și
  facturează fără a afișa vreo eroare. aipmt oprește traducerea de îndată ce raportul
  de cotă al unui apel semnalează acest lucru, dar acel apel este deja contorizat.
- **Cotă partajată cu sesiunile dumneavoastră Claude Code.** Fiecare apel raportează
  utilizarea ferestrelor de 5 ore și a celei săptămânale; peste 80%
  (`AIPMT_CLAUDE_MAX_UTILIZATION`), nu se mai lansează niciun segment suplimentar, pentru
  a nu epuiza ceea ce vă este necesar pentru lucru.
- **Izolare.** Fiecare apel rulează fără instrumente, într-un director privat și
  de unică folosință, în mod fără personalizare: nu sunt încărcate nici `CLAUDE.md`-urile
  dumneavoastră, nici pluginurile, hook-urile, serverele MCP sau setările dumneavoastră, și nimic nu este păstrat
  din sesiune. Fișierele atașate sunt tăiate: un `@chemin` din documentul dumneavoastră
  rămâne text și nu deschide niciun fișier (măsurat).
- **Modele**: `sonnet` în mod implicit, la efortul `low`, și în `--eco` de asemenea:
  `--eco` nu schimbă nimic pe această cale. Măsurat pe aceleași documente, `haiku`
  este de două ori mai lent — raționează fără să poată fi împiedicat — pentru
  un cost abia mai mic, iar `opus` refuză conținuturi de biologie (punctul
  următor). Ambele rămân accesibile prin `--model`; aceste aliasuri urmăresc
  cel mai recent model din familia lor. `fable` și variantele `[1m]` sunt refuzate,
  deoarece trec pe credite plătite. `--reasoning_effort` ajustează efortul,
  din care o traducere nu obține niciun beneficiu: raționamentul măsurat este nul sau aproape nul.
- **Opus refuză anumite conținuturi de biologie.** Sistemele sale de protecție sunt mai
  stricte decât cele ale lui Sonnet, iar mesajul de eroare de la Anthropic avertizează că acestea
  „can sometimes flag biology-research-adjacent work”. Măsurat: o scurtă știre de
  monitorizare despre 279 de molecule generate a dus la refuzarea articolului în toate cele paisprezece
  limbi. Nimic nu este scris: aipmt refuză răspunsul trunchiat, indică sistemele
  de protecție și recomandă `--model sonnet`.
- Refuzat în CI (`CI` sau `GITHUB_ACTIONS` definit) și sub Windows (nemăsurat).
- Variabile: `AIPMT_CLAUDE_BIN` (altfel `PATH`, apoi `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (secunde per segment, implicit 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (implicit 0.8), `CLAUDE_CONFIG_DIR` (contul
  Claude Code, niciodată preluat dintr-un `.env` de proiect); directoare de lucru sub
  `XDG_CACHE_HOME/aipmt/claude-code` (implicit `~/.cache`).

**Termeni de utilizare: este angajat propriul dumneavoastră cont.** [Pagina
juridică a Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
nu interzice ca „an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription”: exact asta face aipmt, care lansează
binarul oficial și nu citește niciodată tokenul. Însă Anthropic „does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users”, preferă cheia API pentru instrumentele
terțe, „including open-source projects”, și își rezervă dreptul de a le deduce
utilizarea din creditele plătite
([asistență Claude](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Niciun text nu tranșează cazul unui instrument distribuit care lansează binarul.

**Date**: pe conturile Free, Pro și Max, antrenarea modelelor
se aplică și pentru Claude Code atunci când setarea de confidențialitate permite acest lucru
([pagina despre date](https://code.claude.com/docs/en/data-usage)). aipmt nu păstrează
nicio transcriere locală (`--no-session-persistence`). Nu trimiteți
nimic confidențial prin acesta.

### Către furnizorul la alegere: `--use_opencode`

[OpenCode](https://opencode.ai) este un agent de cod open source (MIT) care
rutează către furnizorii configurați în interiorul său: cheie API, abonament,
gateway OpenCode Zen (modele gratuite, fără cont) sau model local. Două
căi au fost măsurate cap-coadă aici, Zen și Ollama.

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

`--model` este obligatoriu: fără el, OpenCode ar reveni la un model gratuit
ale cărui schimburi de mesaje pot fi utilizate pentru antrenare, iar această alegere nu este făcută în
locul dumneavoastră.

Izolare la fiecare apel:

- o configurație inline, cu prioritate asupra celei a dumneavoastră, definește un agent `aipmt`
  ale cărui instrumente sunt toate refuzate (`permission: { "*": "deny" }`), partajarea
  sesiunii este dezactivată, `--pure`, niciodată `--auto`;
- director de lucru de unică folosință și gol, cu `OPENCODE_DISABLE_PROJECT_CONFIG` și
  `OPENCODE_DISABLE_CLAUDE_CODE` create — fără ele, OpenCode injectează în
  prompt `AGENTS.md`-ul directorului curent și `~/.claude/CLAUDE.md`.
  `~/.config/opencode/AGENTS.md`-ul global rămâne injectat, OpenCode nu permite
  excluderea acestuia;
- contract de ieșire: cod de retur 0, niciun eveniment `error`, niciun apel
  de instrument, ultimul pas în `stop`, text nevid, iar agentul `aipmt`
  efectiv încărcat — un `--agent` necunoscut nu duce la eșecul OpenCode, acesta
  revine silențios la agentul de codare;
- nicio cheie de `aipmt` nu este transmisă, cu excepția `OPENCODE_API_KEY`, cheia
  OpenCode însuși. Furnizorii se configurează în OpenCode, nu în
  `.env`-ul lui `aipmt`.

De știut:

- Modelele gratuite ale Zen sunt schimbătoare, cu limite nedocumentate, iar
  schimburile lor de mesaje pot servi la antrenare: potrivite pentru o documentație
  publică, nu pentru un conținut privat.
- Un model local trebuie să ofere cel puțin 16 k tokeni de context, segmentele
  având până la 16.000 de caractere. Ollama configurează adesea 4.096: folosiți
  un `Modelfile` cu `PARAMETER num_ctx 32768`.
- `--eco` nu are efect; `--reasoning_effort` este transmis ca atare drept
  `--variant` al OpenCode.
- OpenCode înregistrează fiecare sesiune în `~/.local/share/opencode/`.
- Variabile: `OPENCODE_BIN` (altfel `PATH`, apoi `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (secunde per segment, implicit 600). `OPENCODE_CONFIG`
  este transmis ca atare către OpenCode.

Exemplul unui model local prin Ollama, în `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` oprește raționamentul pe care Ollama îl activează în mod implicit pe aceste
modele și pe care un Modelfile nu îl poate dezactiva. Măsurat pe o propoziție de
șase cuvinte: 919 tokeni de raționament și 68 de secunde fără opțiune, 9 tokeni cu ea.

### Către peste 400 de modele: `--use_openrouter`

OpenRouter este un ruter facturat la utilizare, pe baza unui credit unic, plasat în fața unor
modele găzduite de terți — inclusiv modelele chinezești deschise pe care niciun
alt furnizor nu le expune aici.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` este obligatoriu. O verificare preflight, executată înainte de orice facturare, rezolvă
două particularități ale rutării:

- **Același model este servit de zeci de gazde cu plafoane
  diferite** — pe `z-ai/glm-5.3-flash`, 23 de gazde, dintre care una plafonată la
  2.048 de tokeni de ieșire. Verificarea preflight citește `/api/v1/models/{modèle}/endpoints`,
  exclude gazdele sub 8.000 de tokeni de ieșire sau cu statut degradat și
  le fixează pe celelalte cu `allow_fallbacks: false`.
- **Raționamentul este facturat la tariful de ieșire** — 107 tokeni față de 2 la
  un răspuns „OK” de la `z-ai/glm-5.2`. Acesta este dezactivat în mod implicit; modelele
  care îl impun primesc cel mai scăzut nivel de efort pe care îl acceptă, valoarea implicită din
  catalog putând satura ieșirea înainte de finalizarea traducerii.
  `--reasoning_effort` rămâne prioritar.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Fereastra de context provine din catalog. Un model sub 16.400 de tokeni este
  refuzat înainte de orice apel: 8.400 pentru prompt și segment, minimum 8.000
  pentru ieșire.
- Un slug absent din catalog, un catalog inaccesibil sau absența
  unei gazde care să respecte plafonul opresc comanda.
- `finish_reason=length` cu o ieșire goală reprezintă un buget consumat de
  raționament, nu o trunchiere: mesajul face această distincție.
- `--eco` nu are efect.
- Variabile: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (implicit `https://openrouter.ai/api/v1`, `https://`
  necesar), `OPENROUTER_TIMEOUT` (implicit 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (implicit 30).

### Notă de traducere

`--add_translation_note` adaugă o notă, în `bottom` (implicit), `top` (după
front matter) sau `both` (`--note_position`), în formatul `legacy` (paragraf
aldin, implicit) sau `marker` (`--note_format`). Formatul `marker` este o
definiție de referință Markdown invizibilă,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
urmată de un citat aldin: lizibil pe GitHub, utilizabil la build de către un
plugin remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Măsurători detaliate

Toate măsurătorile sunt traduceri efectiv executate cu `aipmt`, către
paisprezece limbi: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Scrise** numără fișierele pe care mecanismele de siguranță le-au lăsat să treacă; **Fără
abateri** cele în care `scripts/compare_structure.py` nu detectează nimic — același număr de
secțiuni, de subtitluri, de linkuri, de URL-uri distincte, de blocuri de cod, de
coduri inline, de rânduri de tabel, de blocuri de citat și de cuvinte aldine.

„Fără abateri” înseamnă „nimic detectat”, nu „identic”: comparatorul
numără elemente fără a le citi conținutul. Acesta nu semnalează nici un titlu de
nivelul 4 șters, nici textul unui cod inline înlocuit, nici un steag
inversat, nici un link intern redat cu o paranteză în plus,
`[texte]((#ancre))`, care nu mai duce nicăieri — și nu judecă
limba.

### Articol dens de monitorizare, modul `--news`

O ediție a [monitorizării IA de pe jls42.org](https://jls42.org/fr/news):
589 de rânduri, 140 de linkuri, 21 de secțiuni, 3 citate în engleză protejate. Campania
din 4 și 5 septembrie 2026.

| Model                                           | Acces              | Scrise  | Fără abateri | Mediană/limbă  |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | API Google         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | abonament Google   | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | abonament Google   | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | abonament ChatGPT  | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | abonament Claude   | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | API Anthropic      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | abonament Claude   | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | local              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | API Mistral        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | abonament Grok     | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | abonament Claude   | 0/14    | ❌ 0/14      | —              |

Grok a fost remăsurat pe 9 septembrie pe o altă ediție a aceleiași monitorizări
(356 de rânduri): 9 limbi scrise din 14, 8 fără abateri. Această cifră este cea care
figurează în tabelul principal. Trei campanii întrerupte nu sunt
notate: `qwen3.5-27b` (9 limbi) și `kimi-k2.6` (4) din lipsă de credit,
`z-ai/glm-5.3-flash` ale cărui două eșecuri proveneau dintr-o setare de raționament
pe care furnizorul o corectează de atunci. Rândurile OpenRouter au fost măsurate cu
setările implicite ale ruterului, înainte de `--use_openrouter`; `z-ai/glm-5.2`,
remăsurat cu furnizorul livrat, oferă același rezultat de 14/14. Cifrele au fost
recalculate pe 10 septembrie cu comparatorul actual: `qwen3.8-flash` și
`qwen3.7-flash` câștigă fiecare câte o limbă față de prima
publicare, celelalte rămân neschimbate.

Rândurile `--use_antigravity` au fost măsurate pe 26 septembrie pe același
articol, patru traduceri în paralel: `gemini-3.7-flash-medium` dimineața,
`gemini-3.8-flash-medium` după-amiaza. În engleză, fiecare a eliminat el însuși
cele trei rânduri de traducere în franceză de sub citate, fără a inventa vreun
steag, iar citatele în engleză sunt intacte: curățarea de rezervă nu a
avut nimic de făcut. În `--eco` (`gemini-3.7-flash-low`), doar pe patru limbi
(en, ja, ar, hi): 4 scrise din 4, toate fără abateri, mediană de 1 min 52 s.
Contraprobă în aceeași zi pe o ediție mai recentă a monitorizării,
cea din 25 septembrie (438 de rânduri, 2 citate în engleză), tradusă în afara
blogului cu `gemini-3.7-flash-medium`: 14 scrise din 14, toate fără abateri, 87 până la
128 s per limbă.

Rândurile `--use_claude_code` au fost măsurate pe 26 septembrie pe același
articol, patru traduceri în paralel, la efortul `low`. Cu `sonnet`,
citatele în engleză sunt intacte în toate cele paisprezece limbi și, în engleză,
modelul a eliminat el însuși rândurile de traducere în franceză, fără a inventa vreun
steag. `opus` nu a scris nicio limbă: în fiecare, sistemele sale de protecție au
oprit răspunsul la ultimul segment, din cauza unei scurte știri despre 279 de molecule
generate pentru un sit de legare. Trimisă separat, această știre este refuzată sub
incidența categoriei „bio”; `sonnet` a tradus-o peste tot. `haiku` scrie
toate cele paisprezece limbi; în trei dintre ele (en, pl, ro), un titlu de secțiune trece de la
nivelul 2 la nivelul 1. Acesta raționează fără să poată fi împiedicat — 61% din
tokenii săi de ieșire —, de unde mai mult de dublul timpului lui `sonnet`.

### README-ul acestui proiect, Markdown standard

Revizie fixată la 9 septembrie 2026: 785 de rânduri, 285 de fragmente de cod inline, 40
de închideri de blocuri, 89 de rânduri de tabel. Patru traduceri în paralel.

| Model                                           | Scrise  | Fără diferențe | Mediană/limbă  | Ce diferă                                                                |
| ----------------------------------------------- | ------- | -------------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14       | 1 min 43 s     | nimic                                                                    |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14       | 1 min 48 s     | nimic                                                                    |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14       | 4 min 02 s     | nimic pentru comparator; linkuri interne dublate (en)                   |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14       | 36 s           | un cuvânt aldin (ja)                                                     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14       | 1 min 22 s     | un cuvânt aldin (ko)                                                     |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14       | 2 min 20 s     | un rând de tabel lipit de cel anterior (ar)                              |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14       | 2 min 56 s     | un link (sv), un cuvânt aldin (zh)                                       |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14       | 6 min 46 s     | un cuvânt aldin (ar, ja)                                                 |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14       | 2 min 34 s     | un cuvânt aldin (hi, ja, ko)                                             |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14       | 2 min 17 s     | 40 de fragmente de cod inline adăugate în arabă; text aldin (hi, ja, ko) |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14        | 2 min 44 s     | o secțiune pierdută (ar, hi, ko); blocuri de cod adăugate (ja, ko, ro, zh) |

Două campanii întrerupte nu sunt notate: Grok, sesiune CLI expirată
după douăsprezece limbi (unsprezece fără diferențe), și `qwen3.8-flash`, HTTP 429 de la
furnizorul său de găzduire după două. `opencode/mimo-v2.5-free` și `ollama/gpt-oss-20b-32k`
nu au fost remăsurate pe această revizie; pe cea din 4 și 5 septembrie,
mai scurtă cu 277 de rânduri, fiecare a scris 9 traduceri din 14, dintre care 7
și 1 fără diferențe.

Rândurile `--use_antigravity` și `--use_claude_code` nu au fost măsurate pe
revizia fixată, ci la 26 septembrie pe cea publicată cu 1.14.0: 600
de rânduri, 257 de fragmente de cod inline, 30 de închideri de blocuri, 85 de rânduri de tabel. Mai
scurtă cu 185 de rânduri, nu se compară termen cu termen cu celelalte rânduri;
aceste rânduri, în schimb, se compară între ele. În ceea ce privește linkurile interne, pe care
comparatorul nu le verifică, `gemini-3.8-flash-medium` le-a păstrat intacte în
cele paisprezece limbi, `gemini-3.7-flash-medium` le-a rupt în italiană;
`sonnet` și `opus` le-au păstrat intacte peste tot, `haiku` le-a dublat în
engleză.

### Patru README-uri ale unor proiecte cunoscute

FastAPI, Ollama, tldr-pages și Vue.js, preluate ca atare de pe GitHub —
documente mai ușoare decât cele două anterioare. Campania a vizat modelele
aflate în dificultate; Gemini servește aici drept punct de comparație.

| Model                     | Perimetru                  | Scrise  | Fără diferențe |
| ------------------------- | -------------------------- | ------- | -------------- |
| `gemini-3.7-flash`        | 4 proiecte × 14 limbi      | 56/56   | ✅ **55/56**   |
| `opencode/mimo-v2.5-free` | 4 proiecte × 14 limbi      | 55/56   | ❌ 47/56       |
| `grok-4.6` (abonament)    | 4 proiecte × ar, hi, ja, zh | 16/16   | ❌ 14/16       |
| `ollama/gpt-oss-20b-32k`  | 4 proiecte × ar, hi, ja, zh | 15/16   | ❌ 9/16        |

### Ce nu sunt aceste măsurători

- **Nu sunt un clasament exhaustiv**: Doar OpenRouter oferă peste patru sute de
  modele, au fost măsurate aproximativ cincisprezece.
- **Durate orientative**: de la trei până la șase traduceri în paralel, în funcție
  de campanie, iar debitul unui furnizor variază de-a lungul zilei.
- **Observații datate**: modelele se schimbă sub același nume, iar
  documentele dumneavoastră nu sunt ale noastre.

Pentru a repeta măsurătoarea pe documentele dumneavoastră, pe o copie fixată a fișierului:

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## Contribuire

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

Ambele linii sunt necesare: fără `pip install -e .`, `python -m aipmt`
răspunde `No module named aipmt`.

Instrumente de calitate, opționale, dar recomandate:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Cele 28 de traduceri ale depozitului (README și CHANGELOG, paisprezece limbi) se
regenerează cu `./regen_translations.sh --force` — Codex și `gpt-5.6-sol` pe
abonamentul ChatGPT implicit, patru în paralel. `REGEN_PROVIDER` și
`REGEN_MODEL` schimbă calea: `antigravity` rămâne pe un abonament, cel
de la Google, și trece fără derogare; un API facturat (`openai`, `gemini`,
`grok`, `openrouter`) este refuzat fără `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` plafonează fiecare sarcină (600 s, 1.800 s pe Codex și
Antigravity). Detaliile despre instrumente se află în `CLAUDE.md`.

## Proiecte care utilizează acest script

- **[jls42.org](https://jls42.org)** — blog personal publicat în 15 limbi.
  [Monitorizarea sa zilnică privind IA](https://jls42.org/fr/news) este tradusă în fiecare zi
  cu acest instrument și servește drept document de referință pentru măsurătorile de mai sus.

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licență

GNU GENERAL PUBLIC LICENSE Versiunea 3. Consultați [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Avertisment

Acest program este distribuit **fără nicio garanție**, în conformitate cu termenii
secțiunilor 15 și 16 din GPL v3: furnizat „ca atare”, fără garanție de vandabilitate
sau de adecvare pentru un anumit scop, iar autorul său nu poate fi tras la
răspundere pentru daunele rezultate din utilizarea acestuia. Textul licenței
prevalează asupra acestui rezumat.

- **Recitiți înainte de a publica.** Protecțiile acoperă blocurile de cod,
  fragmentele de cod inline, URL-urile, ancorele și citatele modului `--news` — dar nu
  titlurile, nici tabelele, nici front matter-ul, nici sensul frazelor dumneavoastră.
- **Documentele dumneavoastră ajung la furnizorul ales**, în conformitate cu termenii
  săi de utilizare și politica sa de confidențialitate a datelor. Unele modele gratuite pot
  reutiliza conversațiile dumneavoastră pentru antrenare, iar condițiile Antigravity
  îi permit lui Google să le reutilizeze și să le trimită spre revizuire umană,
  inclusiv în cazul abonamentului cu plată; un model local este singura modalitate prin care
  nicio dată nu părăsește dispozitivul dumneavoastră.
- **Apelurile API vă sunt facturate.** Acest program nu plafonează
  cheltuielile: un document lung, o reluare după o eroare sau un model care raționează
  mult costă mai mult.
- **Măsurătorile publicate sunt observații datate**, nu garanții.

Numele de produse și companii menționate aparțin deținătorilor
respectivi. Acest proiect nu este afiliat cu niciunul dintre aceștia.

**Articol tradus din fr în ro cu gemini-3.8-flash-medium.**

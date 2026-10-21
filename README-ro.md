# Traducător de Markdown bazat pe AI

🌍 [Franceză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [Engleză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Spaniolă](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Chineză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Germană](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Japoneză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Coreeană](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Arabă](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiană](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Neerlandeză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Poloneză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Portugheză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Suedeză](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Calitatea codului</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Starea pragului de calitate"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Evaluarea securității"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Evaluarea fiabilității"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Evaluarea mentenabilității"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Acoperire"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilități"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Erori"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Probleme de calitate a codului"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Linii duplicate (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Datorie tehnică"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Linii de cod"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Insignă Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Traduce fișiere Markdown dintr-o limbă în alta, păstrând
structura: blocuri de cod, cod inline, URL-uri, ancore, tabele și front
matter. Unsprezece moduri de a apela un model — cinci API-uri, patru abonamente fără
facturare în funcție de utilizare, două routere — și o evaluare publicată a ceea ce fiecare
model păstrează efectiv.

## Pe scurt

- **Unsprezece căi de acces la furnizori**: API-urile OpenAI, Mistral, Claude, Gemini și Grok;
  abonamentele ChatGPT (Codex), Grok, Google (Antigravity) și Claude (Claude
  Code) fără facturare în funcție de utilizare; routerele OpenCode (open source, gratuit sau local) și OpenRouter
  (peste 400 de modele).
- **Nicio alterare din cauza unui token pierdut**: blocurile de cod, codul inline,
  URL-urile, ancorele și citatele sunt înlocuite cu tokenuri înainte de apel și
  verificate la primirea răspunsului. Dacă lipsește unul, fișierul nu este scris.
- **Documente lungi**: segmentare în funcție de fereastra de context a modelului.
- **Modul `--news`**: citate în engleză protejate și indicatoare gestionate în funcție de
  limbă, pentru articolele de monitorizare.
- **Modul `--eco`**: modele rapide și mai ieftine.
- **Notă de traducere** opțională, la început, la sfârșit sau în ambele locuri.

## Instalare

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 sau mai recent. Pentru instalarea din repository, consultați
[Contribuții](#contribuții).

## Configurare

Cheile sunt citite din trei locuri, în ordinea descrescătoare a priorității; fiecare
completează doar ceea ce precedentul lasă necompletat.

|     | Unde                                            | Pentru ce                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variabile de mediu                     | CI, containere, suprascriere punctuală |
| 2   | `.env` din directorul curent (sau dintr-un director părinte) | o cheie specifică unui proiect            |
| 3   | `~/.config/aipmt/.env`                        | configurat o singură dată, valabil peste tot       |

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

`GEMINI_API_KEY` este acceptat în loc de `GOOGLE_API_KEY`. Fișierul
utilizatorului respectă `XDG_CONFIG_HOME` (doar cale absolută) și `%APPDATA%`
sub Windows. Fără cheie, comanda enumeră cele trei locații.

**Fișierul `.env` al unui proiect nu poate nici redirecționa apelurile, nici alege programul
executat.** Acesta furnizează chei, niciodată o destinație sau un executabil: orice
variabilă de tip `_BASE_URL`, `_API_BASE`, `_ENDPOINT` sau `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, proxy-urile (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), depozitele de certificate (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) și `XDG_CONFIG_HOME` /
`APPDATA` sunt ignorate acolo, cu un avertisment. Un repository clonat nu trebuie să
poată deturna cheia dumneavoastră și nici să vă facă să rulați propriul său program la
prima traducere. Acest fișier este citit și fără interpolare:
`NOM=${OPENAI_API_KEY}` nu copiază cheia în el. Setați aceste variabile în
mediu sau în `~/.config/aipmt/.env`.

Variabile opționale: `XAI_BASE_URL` (implicit `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (secunde per apel, implicit 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(implicit 600), `GROK_BIN`, `GROK_HOME` (implicit `~/.grok`), `GROK_TIMEOUT`
(implicit 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (implicit 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (implicit 600), `OPENROUTER_BASE_URL`
(`https://` obligatoriu), `OPENROUTER_TIMEOUT` (implicit 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (implicit 30). Fiecare este detaliată în
secțiunea furnizorului său.

## Primii pași

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` tradus în spaniolă produce `document-es.md` în `--target_dir`;
cu `--include_model`, `document-es-gpt-5.6-terra.md`. Extensia devine
întotdeauna `.md` — `article.mdx` produce `article-en.md` — cu excepția utilizării
`--keep_filename`, care păstrează numele original. O traducere deja existentă
este omisă în lipsa `--force`.

Coduri de ieșire: `0` dacă totul a reușit sau a fost omis, `1` dacă mai există un fișier
cu eroare (lista este trimisă la ieșirea de eroare), `2` dacă problema ține de configurare.
Un fișier cu eroare nu este niciodată scris, chiar dacă scrierea în sine eșuează:
conținutul este scris într-un fișier alăturat, apoi acesta este redenumit. Este suficient să relansați comanda.

## Ce model să alegeți

Evaluare realizată pe două documente reale, traduse în aceleași paisprezece limbi de
fiecare model. **Cifra reprezintă numărul de limbi, din paisprezece, în care
traducerea este scrisă și nimic nu diferă față de sursă.**

| Model                | Cum se accesează                 | Articol dens de monitorizare | Acest README    | Ce diferă și în câte limbi                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | abonament Google (Antigravity)   | ✅ 14/14                | ✅ 14/14     | nimic, în niciunul dintre cele două documente                                                                                                                                 |
| **Claude Sonnet 5.5** | cheie API Anthropic                 | ✅ 14/14                | ✅ 14/14     | nimic, în niciunul dintre cele două documente                                                                                                                                 |
| **Gemini 3.7 Flash**  | cheie API Google                    | ✅ 14/14                | ⚠️ 13/14     | 1 limbă din 14: un cuvânt în plus cu caractere aldine (ja)                                                                                                                      |
| **Gemini 3.7 Flash**  | abonament Google (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 1 limbă din 14: un cuvânt în minus cu caractere aldine (ko)                                                                                                                     |
| **GPT-5.6 Sol**       | abonament ChatGPT sau cheie OpenAI | ✅ 14/14                | ⚠️ 12/14     | 2 limbi din 14: un cuvânt în minus cu caractere aldine (ar, ja)                                                                                                                |
| **GLM-5.2**           | cheie OpenRouter                    | ✅ 14/14                | ⚠️ 11/14     | 3 limbi din 14: un cuvânt în minus cu caractere aldine (hi, ja, ko)                                                                                                            |
| Claude Sonnet 5       | abonament Claude (Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 1 limbă din 14 pentru articol: un cuvânt în plus cu caractere aldine (zh); 1 pentru acest README: un rând de tabel lipit de cel precedent, ascuns la afișare (ar)            |
| Claude Haiku 4.5      | abonament Claude (Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 3 limbi pentru articol: un titlu de secțiune trecut la nivelul 1 (en, pl, ro); în acest README, nimic pentru comparator, dar linkurile interne sunt dublate în engleză |
| Claude Sonnet 5       | cheie API Anthropic                 | ⚠️ 11/14                | ⚠️ 12/14     | 3 limbi pentru articol: un bloc de cod apărut (es, de, hi); 2 pentru acest README: un link fără marcajele sale (sv), un cuvânt cu caractere aldine (zh)                              |
| Claude Haiku 4.5      | cheie API Anthropic                 | ⚠️ 7/14                 | ✅ 14/14     | 7 limbi pentru articol: un titlu de secțiune trecut la nivelul 1 — în japoneză, rămas în franceză; nimic în acest README                                              |
| Claude Haiku 5.5      | cheie API Anthropic                 | ⚠️ 11/14                | ❌ 12/14     | 3 limbi pentru articol: un titlu de secțiune cu nivel schimbat sau duplicat (ja, ko, zh); pentru acest README, 2 limbi respinse, fragmente de cod inline pierdute (ar, hi)    |
| Qwen 3.7 Flash        | cheie OpenRouter                    | ❌ 8/14                 | ⚠️ 10/14     | 1 limbă respinsă pentru articol, alte 5 prezintă abateri; în acest README, aproximativ patruzeci de cuvinte puse în `code` (ar)                                                    |
| Grok 4.6              | abonament Grok                   | ❌ 8/14                 | neevaluat     | 5 limbi respinse din 14, din cauza fragmentelor de cod inline și a URL-urilor nerestituite; neerlandeza prezintă abateri peste tot                                                               |
| GPT-OSS 20B           | model local (Ollama)             | ❌ 7/14                 | neevaluat din nou | 4 limbi respinse din 14: modelul lăsa pasaje în franceză, iar mecanismul de verificare le-a blocat                                                                  |
| MiMo v2.5 (gratuit)   | OpenCode Zen, fără cont         | ❌ 11/14                | neevaluat din nou | 1 limbă respinsă; o secțiune pierdută în poloneză                                                                                                                  |
| Mistral Large         | cheie API Mistral                   | ❌ 5/14                 | ❌ 1/14      | **o secțiune întreagă dispare**: 1 limbă pentru articol (hi), 3 pentru acest README (ar, hi, ko) — și 3 limbi respinse pentru articol                                |
| DeepSeek V4 Flash     | cheie OpenRouter                    | ❌ 3/14                 | neevaluat din nou | 10 limbi respinse din 14; 37 minute per limbă                                                                                                                 |
| Claude Opus 5.5       | abonament Claude (Claude Code)   | ❌ 0/14                 | ✅ 14/14     | articolul respins în toate cele 14 limbi de mecanismele de protecție ale Opus, din cauza unei știri scurte de biologie; nimic în acest README                                               |

|     | Ce indică simbolul                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | toate cele paisprezece limbi traduse și nimic nu diferă față de sursă                                                                                                                                       |
| ⚠️  | toate cele paisprezece limbi traduse; diferențele țin de **marcaje** — un cuvânt cu caractere aldine, un `code`, un link care își pierde parantezele drepte. Nu lipsește niciun text, niciun URL, niciun bloc de cod, nicio secțiune |
| ❌  | cel puțin o limbă nu a putut fi tradusă — fișierul este respins, nu este scris — **sau** lipsește conținut dintr-un fișier scris                                                                      |

Ce trebuie reținut:

- **O traducere respinsă nu este o traducere deteriorată.** Când un token
  lipsește din răspuns, fișierul nu este scris, iar limba este considerată
  respinsă. Asta se întâmplă cu Grok pentru articol: patru fragmente de cod inline și
  trei URL-uri pierdute încă din primul segment, în cele cinci sisteme de scriere nelatine.
- **Un model poate refuza un document întreg din cauza unei singure fraze.** Opus 5.5
  traduce acest README fără nicio abatere, dar niciun articol de monitorizare:
  mecanismele sale de protecție opresc răspunsul la o știre scurtă de biologie. Fișierul nu
  este scris, iar aipmt explică de ce.
- **Această plasă de siguranță nu acoperă titlurile, tabelele, front matter sau
  textul.** Un model care elimină o secțiune returnează un fișier pe care instrumentul îl scrie
  fără obiecții — acesta este cazul Mistral. Aceste elemente nu pot fi
  înlocuite cu un token, iar mecanismele actuale de verificare nu le controlează;
  `scripts/compare_structure.py` detectează o secțiune pierdută, dar ulterior.
- **Grok nu are o evaluare pentru acest README**: sesiunea sa CLI a expirat după douăsprezece
  limbi, dintre care unsprezece fără abateri. O campanie întreruptă nu primește o evaluare.
- **Densitatea documentului contează mai mult decât limba.** Grok se descurcă cu
  fișiere README obișnuite și cedează la un articol încărcat cu linkuri, inclusiv în
  neerlandeză.

Date și documente: coloana „Acest README” a fost evaluată pe 9 septembrie 2026
pe o revizie fixată a acestui fișier (785 linii, 285 fragmente de cod inline, 89 rânduri
de tabel), modificată de atunci — cu excepția rândurilor Antigravity și Claude Code,
evaluate pe 26 septembrie pe revizia publicată cu versiunea 1.14.0, mai scurtă
(600 linii, 257 fragmente de cod inline, 85 rânduri de tabel), și a rândurilor Claude
Sonnet 5.5, Haiku 5.5 și Haiku 4.5 prin API, evaluate pe 18 octombrie pe
aceeași revizie. Coloana „Articol dens de monitorizare” provine din campania din
4 și 5 septembrie pe un articol de 589 linii, cu excepția rândului Grok, reevaluat pe
9 septembrie pe o altă ediție a aceleiași publicații de monitorizare, a rândurilor Antigravity și
Claude Code, evaluate pe 26 septembrie pe același articol, și a acestor trei rânduri
Claude, pe 18 octombrie. Tabelele complete, duratele și protocolul se găsesc
în [Evaluări detaliate](#măsurători-detaliate).
## Toate opțiunile

| Opțiune                   | Descriere                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Un singur fișier Markdown de tradus (alternativă la `--source_dir`)                                             |
| `--source_dir`           | Director sursă care conține fișierele Markdown (implicit: `content/posts`)                                   |
| `--target_dir`           | Director de ieșire pentru fișierele traduse (implicit: `traductions_en`)                                    |
| `--source_lang`          | Limba sursă (implicit: `fr`)                                                                                  |
| `--target_lang`          | Limba țintă (implicit: `en`)                                                                                   |
| `--model`                | Modelul specific de utilizat                                                                                  |
| `--eco`                  | Utilizează modelele economice                                                                              |
| `--use_mistral`          | Utilizează API-ul Mistral AI                                                                                     |
| `--use_claude`           | Utilizează API-ul Claude                                                                                         |
| `--use_gemini`           | Utilizează API-ul Gemini                                                                                         |
| `--use_grok`             | Utilizează API-ul xAI (Grok) — necesită `XAI_API_KEY`                                                           |
| `--use_codex`            | Utilizează CLI-ul Codex cu cota abonamentului ChatGPT                                                    |
| `--use_grok_cli`         | Utilizează CLI-ul Grok cu cota abonamentului Grok                                                        |
| `--use_antigravity`      | Utilizează CLI-ul Antigravity (`agy`) cu cota abonamentului Google AI Pro sau Ultra                       |
| `--use_claude_code`      | Utilizează CLI-ul Claude Code (`claude -p`) cu cota abonamentului Claude Pro sau Max                      |
| `--use_opencode`         | Utilizează OpenCode (open source) cu furnizorul configurat în OpenCode; necesită `--model provider/modèle` |
| `--use_openrouter`       | Utilizează OpenRouter — necesită `OPENROUTER_API_KEY` și `--model fournisseur/modèle`                          |
| `--force`                | Forțează retraducerea                                                                                       |
| `--keep_filename`        | Păstrează numele original al fișierului                                                                          |
| `--news`                 | Mod știri: protejează citatele EN, gestionează steagurile în funcție de limbă                                      |
| `--add_translation_note` | Adaugă o notă de traducere                                                                                |
| `--note_position`        | Poziția notei: `top`, `bottom` (implicit) sau `both`                                                     |
| `--note_format`          | Formatul notei: `legacy` (implicit, paragraf aldin) sau `marker`                                            |
| `--include_model`        | Include numele modelului în fișierul de ieșire                                                            |
| `--reasoning_effort`     | Efort de raționament GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

Cele nouă flaguri `--use_*` se exclud reciproc: combinarea a două este
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

`--eco` comută la nivelul economic al fiecărui furnizor.

| Furnizor    | Calitate (implicit)                                                     | Economic (`--eco`)      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                                      | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                                   | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (și `gpt-5.6-sol`, `terra` și `luna` prin `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | la fel — `--eco` fără efect |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, efort `low`                                               | la fel — `--eco` fără efect |
| OpenCode    | `--model provider/modèle` obligatoriu                                | la fel — `--eco` fără efect |
| OpenRouter  | `--model fournisseur/modèle` obligatoriu                             | la fel — `--eco` fără efect |

### Cu abonamentul ChatGPT: `--use_codex`

Controlează CLI-ul oficial Codex: traducerea consumă din cota
abonamentului ChatGPT, fără cheie API și fără facturare în funcție de utilizare.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Executabilul este căutat în `CODEX_BIN`, apoi în `PATH`, apoi în pachetul
  `openai-codex-cli-bin`. `~/.codex/auth.json` nu este citit niciodată.
- `OPENAI_API_KEY` și `CODEX_API_KEY` sunt eliminate din mediul
  subprocesului: prezența unei chei nu provoacă niciodată comutarea la API.
- Fiecare segment consumă cel puțin un „mesaj” din fereastra de 5 ore — două
  dacă validarea lui eșuează și este reîncercat. OpenAI indică, cu titlu
  estimativ, 250-2 000 mesaje/5 h pentru `gpt-5.6-luna` (`--eco`) și
  10-100 pentru `gpt-5.6-sol` cu un abonament Plus.
- `--model gpt-5.6-sol`, opțiunea implicită până la 1.16.3, `--model gpt-5.6-terra`
  și `--model gpt-5.6-luna` folosesc, de asemenea, abonamentul.
- Un răspuns 429 de la server nu duce la pierderea fișierului: Codex se reconectează singur,
  aipmt așteaptă încheierea turei, iar dacă eroarea 429 persistă, segmentul
  este reluat după 30, apoi după 60 de secunde. Un model la care contul nu are acces returnează un 400 „modelul nu
  este acceptat când se utilizează Codex cu un cont ChatGPT”.
- Mai lent decât un API, iar diferența crește odată cu documentul: pentru acest README,
  mediana este de 6 min 46 s pe limbă cu `gpt-5.6-sol`, față de 36 s pentru
  `gemini-3.7-flash`.
- Refuzat în CI (`CI` sau `GITHUB_ACTIONS` definit): autentificarea abonamentului
  se face printr-un fișier de sesiune personal, care nu își are locul pe un runner
  partajat.
- Variabile: `CODEX_BIN`, `CODEX_TIMEOUT` (secunde pe segment, implicit 600).

### Cu abonamentul Grok: `--use_grok_cli`

Același principiu, cu CLI-ul oficial Grok Build, pe baza abonamentului SuperGrok sau
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Izolare mai slabă decât la Codex.** Sandbox-ul OS al Grok nu se aplică
  pe multe sisteme Linux recente (AppArmor, socketuri ale runtime-ului
  de containere), iar un profil care nu poate fi aplicat pornește fără izolare,
  fără nicio avertizare. Prin urmare, scriptul nu solicită implicit niciun profil, anunță acest lucru și
  se bazează pe regulile `--deny` ale CLI-ului, inclusiv regula catch-all `*` — singurul
  strat care refuză să pornească în loc să elimine protecția fără să
  anunțe. `GROK_TRANSLATE_SANDBOX=read-only` impune sandbox-ul OS, iar pornirea
  eșuează dacă sistemul nu îl poate aplica.
- Cota este săptămânală, partajată cu Chat, Imagine și Voice, și nicio
  comandă nu permite consultarea ei: un lot poate consuma din cota pentru conversații
  fără niciun semnal.
- Variabile: `GROK_BIN`, `GROK_HOME` (directorul CLI-ului, implicit `~/.grok`),
  `GROK_TIMEOUT` (implicit 900), `GROK_TRANSLATE_SANDBOX`.

### Cu abonamentul Google: `--use_antigravity`

Același principiu, cu `agy`, CLI-ul oficial Antigravity: pentru cei care plătesc Google
AI Pro sau Ultra, traducerea consumă din cota abonamentului în loc
să fie facturată per token. Aceasta este singura cale de acces la această cotă: Gemini CLI nu
mai deservește aceste conturi din 18 iunie 2026
([anunț](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
iar SDK-ul Antigravity acceptă doar o cheie API sau un proiect Google Cloud.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Nicio cale cu plată nu rămâne deschisă.** agy primește din
  mediul dumneavoastră doar o listă strictă de variabile — `PATH`, limba și fusul orar,
  terminalul, identitatea, proxy-urile și certificatele, magistrala de sesiune — și nicio cheie:
  mai multe dintre variabilele sale redirecționează un apel fără să afișeze nimic (constatat prin măsurători:
  una trimite documentul către un gateway terț, alta către un proiect
  Google Cloud facturat), iar o listă de excludere omitea câte una la fiecare revizuire.
  Înaintea fiecărui segment, `agy -p /config`, care nu consumă din cotă, trebuie să arate
  creditele AI cu plată dezactivate, fără cheie API și fără proiect Google Cloud — o
  setare absentă duce la refuz —, altfel nu se traduce nimic; jurnalul fiecărui
  apel trebuie apoi să confirme utilizarea abonamentului (`authMethod=consumer`), altfel
  răspunsul este refuzat.
- **Izolare.** Fiecare apel rulează într-un director personal privat și
  temporar, cu un agent de traducere fără instrumente: setările, regulile,
  pluginurile, serverele MCP și hook-urile dumneavoastră din agy nu sunt preluate, nu se adaugă nimic în
  istoric, iar autentificarea rămâne în keyring, pe care aipmt nu îl citește niciodată.
  Dacă agentul nu este găsit, agy revine, fără avertizare, la agentul său de programare
  și la instrumentele acestuia: o linie întreagă din jurnal trebuie să confirme agentul corect — un
  document care citează acest mesaj nu o înlocuiește —, altfel apelul este refuzat.
- **Platforme**: Linux, într-o sesiune care are un keyring (magistrală de sesiune
  D-Bus, Secret Service); macOS este acceptat, fără să fi fost efectuate măsurători pe el. Refuzat
  pe Windows, unde agy nu citește variabilele care izolează fiecare apel, și
  pe Linux fără magistrală de sesiune — sesiune SSH, container, server: în aceste cazuri, agy
  își stochează tokenul într-un fișier din `~/.gemini`, pe care izolarea îl ascunde.
  Refuzul are loc înainte de orice lansare, cu motivul aferent, în locul unei așteptări
  de un minut pentru un cod de autentificare.
- **Modele**: cele din `agy models`. Modelele Gemini includ efortul în nume
  (`gemini-3.8-flash-medium`…): un nume fără sufix este refuzat înaintea apelului,
  iar `--reasoning_effort` nu are efect. Implicit `gemini-3.8-flash-medium`,
  și `gemini-3.7-flash-low` în `--eco`; campaniile care au stabilit aceste opțiuni sunt
  descrise în [Măsurători detaliate](#măsurători-detaliate). Claude și GPT-OSS
  au propria cotă, mult mai mică: aproximativ 1 % din fereastra de
  5 ore pentru fiecare apel măsurat, față de 0,05 % cu Flash.
- **Cotă**: pentru fiecare grup, o fereastră de 5 ore și una săptămânală,
  proporțional cu costul în tokenuri. Măsurat pe contul autorului: aproximativ
  16 puncte din fereastra de 5 ore pentru fiecare milion de caractere sursă cu
  `gemini-3.8-flash-medium`, 14 cu `gemini-3.7-flash-medium` și 7 până la 8 cu
  efort redus — un README de 40 000 de caractere costă deci puțin peste o
  jumătate de punct. Limita săptămânală depinde de nivelul abonamentului. Reîncercarea urmează
  ceea ce agy declară că poate fi reîncercat; în lipsa acestei informații, o fereastră epuizată nu este niciodată
  reîncercată: ea provoacă eșecul fiecărui fișier până la resetarea
  afișată de `/usage`.
- **Mai lent decât API-ul**: pentru articolul dens folosit la măsurători, mediana este de 3 min 59 s pe
  limbă cu `gemini-3.8-flash-medium` și de 3 min 14 s cu
  `gemini-3.7-flash-medium`, față de 1 min 18 s pentru Gemini 3.7 Flash prin API.
- **Întrerupere**: Ctrl-C sau închiderea terminalului opresc agy odată cu
  comanda, în loc să îl lase să își încheie tura consumând din cotă; același lucru este valabil
  pentru Codex, Grok CLI și OpenCode. Sub `nohup`, traducerea continuă.
- Refuzat în CI (`CI` sau `GITHUB_ACTIONS` definit): autentificarea este stocată într-un
  keyring personal. Pe un runner, `--use_gemini` cu `GOOGLE_API_KEY`.
- Variabile: `AGY_BIN` (în lipsa acesteia, `PATH`, apoi `~/.local/bin/agy`),
  `AGY_TIMEOUT` (secunde pe segment, inclusiv pornirea, implicit 900).

**Condiții de utilizare: contul dumneavoastră este cel implicat.**
[Condițiile Antigravity](https://antigravity.google/terms) (secțiunea 6) și
[FAQ-ul său](https://antigravity.google/docs/faq/) interzic accesarea serviciului
printr-un software terț folosind autentificarea Antigravity — Claude Code,
OpenClaw și OpenCode sunt menționate explicit —, sub sancțiunea suspendării contului. aipmt
nu citește și nu reutilizează tokenul: lansează executabilul oficial în
[modul headless](https://antigravity.google/docs/cli/headless/) pe care Google
îl documentează pentru scripturi și CI. Un membru Google a considerat drept „standard”
lansarea `agy -p` dintr-un script local pentru propria activitate
([forum oficial, 25 septembrie 2026, răspuns fără valoare contractuală](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
niciun text nu clarifică situația unui instrument distribuit precum acesta.

**Doar documente publice.** Conform secțiunii 5 din aceleași condiții,
schimburile — prompturi, răspunsuri, metadate — pot fi folosite pentru îmbunătățirea
produselor și a învățării automate Google și pot fi examinate de
oameni, inclusiv în cazul unui abonament plătit. Renunțarea se face prin setarea
`enableTelemetry`, al cărei efect nu este documentat și pe care aipmt nu o configurează; setările dumneavoastră
agy nu sunt preluate în mediul său izolat. Nu trimiteți prin acesta nimic confidențial.
### Cu abonamentul Claude: `--use_claude_code`

Același principiu cu `claude`, CLI-ul oficial al Claude Code, în modul `-p`: pentru
cei care plătesc Claude Pro sau Max, traducerea se scade din cota
abonamentului în loc să fie facturată per token. A nu se confunda cu
`--use_claude`, API-ul Anthropic, facturat în funcție de utilizare.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Nicio cale cu plată nu rămâne deschisă, iar fiecare apel dovedește acest lucru.** Claude
  Code primește din mediul vostru doar o listă închisă de variabile — fără
  cheie API, token, furnizor cloud sau marcaj al sesiunii Claude Code
  din care ar fi lansat aipmt. Înainte de primul segment, `claude auth status` trebuie
  să arate conectarea prin abonament, fără cheie Console, iar `/usage`, care nu consumă
  nicio cotă, trebuie să o confirme; fiecare apel o confirmă la rândul său în
  evenimentul de inițializare, altfel răspunsul este respins.
- **Dezactivați „extra usage”** (claude.ai, Setări → Utilizare) pentru
  ca valoarea de zero euro să se mențină: dacă este activat, preia utilizarea după epuizarea unei ferestre și
  facturează fără să afișeze o eroare. aipmt oprește traducerea imediat ce raportul
  de cotă al unui apel semnalează acest lucru, dar acel apel este deja contorizat.
- **Cotă partajată cu sesiunile voastre Claude Code.** Fiecare apel raportează
  utilizarea ferestrelor de 5 ore și a celei săptămânale; peste 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`), nu se mai lansează niciun segment, pentru a nu
  epuiza resursele folosite pentru munca voastră.
- **Izolare.** Fiecare apel rulează fără instrumente, într-un director privat și
  temporar, într-un mod fără personalizare: nici fișierele voastre `CLAUDE.md`, nici pluginurile,
  hooks, serverele MCP sau setările nu sunt încărcate și nu se păstrează nimic din
  sesiune. Atașamentele sunt dezactivate: un `@chemin` din documentul vostru
  rămâne text și nu deschide niciun fișier (verificat prin măsurare).
- **Modele**: `sonnet` implicit, cu nivelul de efort `low`, inclusiv în `--eco`:
  `--eco` nu schimbă nimic pe această cale. La măsurarea pe aceleași documente, `haiku`
  este de două ori mai lent — raționează fără să poată fi împiedicat — pentru
  un cost abia mai mic, iar `opus` refuză conținuturi de biologie (punctul
  următor). Ambele rămân accesibile prin `--model`; aceste aliasuri urmăresc
  cel mai recent model din familia lor. `fable` și variantele `[1m]` sunt respinse,
  deoarece trec pe credite cu plată. `--reasoning_effort` reglează efortul,
  din care o traducere nu câștigă nimic: raționamentul măsurat este nul sau aproape nul.
- **Opus refuză anumite conținuturi de biologie.** Mecanismele sale de protecție sunt mai
  stricte decât cele ale Sonnet, iar mesajul de eroare Anthropic avertizează că acestea
  „pot uneori semnala lucrări apropiate de cercetarea în biologie”. Rezultat măsurat: o știre
  dintr-un buletin de monitorizare despre 279 de molecule generate a dus la refuzarea articolului în toate cele paisprezece
  limbi. Nu se scrie nimic: aipmt respinge răspunsul întrerupt, indică
  mecanismele de protecție și recomandă `--model sonnet`.
- Respins în CI (cu `CI` sau `GITHUB_ACTIONS` definit) și pe Windows (nemăsurat).
- Variabile: `AIPMT_CLAUDE_BIN` (altfel `PATH`, apoi `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (secunde per segment, implicit 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (implicit 0.8), `CLAUDE_CONFIG_DIR` (contul
  Claude Code, niciodată preluat dintr-un `.env` al proiectului); directoare de lucru în
  `XDG_CACHE_HOME/aipmt/claude-code` (implicit `~/.cache`).

**Condiții de utilizare: responsabilitatea revine contului vostru.**
[Pagina juridică Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
nu împiedică „un utilizator final să se conecteze la executabilul Claude Code nemodificat
cu propriul abonament Claude”: asta face aipmt, care lansează
executabilul oficial și nu citește niciodată tokenul. Însă Anthropic „nu permite
dezvoltatorilor terți […] să direcționeze cereri folosind credențialele planurilor Free, Pro sau Max
în numele utilizatorilor lor”, preferă cheia API pentru instrumentele
terțe, „inclusiv proiectele open source”, și își rezervă dreptul de a scădea
utilizarea acestora din creditele cu plată
([ajutor Claude](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Niciun text nu clarifică situația unui instrument distribuit care lansează executabilul.

**Date**: pentru conturile Free, Pro și Max, antrenarea modelelor
se aplică și în Claude Code atunci când setarea de confidențialitate o permite
([pagina despre date](https://code.claude.com/docs/en/data-usage)). aipmt nu păstrează
nicio transcriere locală (`--no-session-persistence`). Nu trimiteți prin el
nimic confidențial.

### Către furnizorul ales: `--use_opencode`

[OpenCode](https://opencode.ai) este un agent de programare open source (MIT) care
direcționează cererile către furnizorii configurați în el: cheie API, abonament,
gateway OpenCode Zen (modele gratuite, fără cont) sau model local. Două
căi au fost măsurate integral aici, Zen și Ollama.

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
ale cărui schimburi de mesaje pot fi folosite pentru antrenare, iar această alegere nu se face în
locul vostru.

Izolare la fiecare apel:

- o configurație inline, care are prioritate față de a voastră, definește un agent `aipmt`
  ale cărui instrumente sunt toate interzise (`permission: { "*": "deny" }`), cu partajarea
  sesiunii dezactivată, `--pure`, niciodată `--auto`;
- director de lucru temporar și gol, cu `OPENCODE_DISABLE_PROJECT_CONFIG` și
  `OPENCODE_DISABLE_CLAUDE_CODE` setate — fără ele, OpenCode injectează în
  prompt fișierul `AGENTS.md` din directorul curent și `~/.claude/CLAUDE.md`. Fișierul
  `~/.config/opencode/AGENTS.md` global rămâne injectat, OpenCode nu permite
  excluderea lui;
- contract de ieșire: cod de retur 0, niciun eveniment `error`, niciun apel
  de instrument, ultimul pas în `stop`, text nevid și agentul `aipmt`
  încărcat efectiv — un `--agent` necunoscut nu provoacă eșuarea OpenCode, acesta
  revine în tăcere la agentul de programare;
- nu se transmite nicio cheie din `aipmt`, cu excepția `OPENCODE_API_KEY`, cheia
  OpenCode însuși. Furnizorii se configurează în OpenCode, nu în
  `.env` al `aipmt`.

De știut:

- Modelele gratuite Zen se schimbă, au limite nedocumentate, iar
  schimburile lor de mesaje pot fi folosite pentru antrenare: sunt potrivite pentru documentație
  publică, nu pentru conținut privat.
- Un model local trebuie să ofere cel puțin 16 k tokens de context, segmentele
  având până la 16 000 de caractere. Ollama configurează adesea 4 096: folosiți
  un `Modelfile` cu `PARAMETER num_ctx 32768`.
- `--eco` nu are efect; `--reasoning_effort` este transmis ca atare drept
  `--variant` al OpenCode.
- OpenCode înregistrează fiecare sesiune în `~/.local/share/opencode/`.
- Variabile: `OPENCODE_BIN` (altfel `PATH`, apoi `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (secunde per segment, implicit 600). `OPENCODE_CONFIG`
  este transmis ca atare către OpenCode.

Exemplu de model local prin Ollama, în `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` dezactivează reflecția pe care Ollama o activează implicit la aceste
modele și pe care un Modelfile nu o poate dezactiva. Rezultat măsurat pe o propoziție de
șase cuvinte: 919 tokens de reflecție și 68 de secunde fără opțiune, 9 tokens cu ea.

### Către peste 400 de modele: `--use_openrouter`

OpenRouter este un router facturat în funcție de utilizare, dintr-un sold unic de credit, care oferă acces la
modele găzduite de terți — inclusiv modelele chinezești deschise pe care niciun
alt provider nu le expune aici.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` este obligatoriu. O verificare preliminară, executată înainte de orice facturare, gestionează
două particularități ale rutării:

- **Același model este servit de zeci de furnizori de găzduire cu plafoane
  diferite** — pentru `z-ai/glm-5.3-flash`, 23 de furnizori de găzduire, dintre care unul limitat la
  2 048 tokens de ieșire. Verificarea preliminară citește `/api/v1/models/{modèle}/endpoints`,
  exclude furnizorii de găzduire cu mai puțin de 8 000 tokens de ieșire sau cu stare degradată și
  îi fixează pe ceilalți prin `allow_fallbacks: false`.
- **Raționamentul este facturat la tariful de ieșire** — 107 tokens față de 2 pentru
  un răspuns „OK” de la `z-ai/glm-5.2`. Este dezactivat implicit; modelele
  care îl impun primesc cel mai mic nivel de efort pe care îl acceptă, deoarece valoarea implicită din
  catalog poate epuiza ieșirea înainte de terminarea traducerii.
  `--reasoning_effort` rămâne prioritar.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Fereastra de context provine din catalog. Un model cu mai puțin de 16 400 tokens este
  respins înainte de orice apel: 8 400 pentru prompt și segment, minimum 8 000
  pentru ieșire.
- Un slug absent din catalog, un catalog inaccesibil sau lipsa
  unui furnizor de găzduire care să respecte plafonul opresc comanda.
- `finish_reason=length` cu ieșire goală înseamnă un buget consumat de
  raționament, nu o trunchiere: mesajul face această distincție.
- `--eco` nu are efect.
- Variabile: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (implicit `https://openrouter.ai/api/v1`, `https://`
  obligatoriu), `OPENROUTER_TIMEOUT` (implicit 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (implicit 30).

### Notă de traducere

`--add_translation_note` adaugă o notă, în `bottom` (implicit), `top` (după
front matter) sau `both` (`--note_position`), în formatul `legacy` (paragraf cu
caractere aldine, implicit) sau `marker` (`--note_format`). Formatul `marker` este o
definiție de referință Markdown invizibilă,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
urmată de un citat cu caractere aldine: lizibil pe GitHub, utilizabil la build de un
plugin remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Măsurători detaliate

Toate măsurătorile sunt traduceri executate efectiv cu `aipmt`, în
paisprezece limbi: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Scrise** numără fișierele pe care verificările de protecție le-au lăsat să treacă; **Fără
abateri**, pe cele în care `scripts/compare_structure.py` nu detectează nimic — același număr de
secțiuni, subtitluri, linkuri, URL-uri distincte, blocuri de cod,
coduri inline, rânduri de tabel, blocuri de citat și cuvinte cu caractere aldine.

„Fără abateri” înseamnă „nimic detectat”, nu „identic”: comparatorul
numără elementele fără să le citească conținutul. Nu semnalează nici eliminarea unui titlu de
nivel 4, nici înlocuirea textului unui cod inline, nici schimbarea unui
steag, nici un link intern redat cu o paranteză în plus,
`[texte]((#ancre))`, care nu mai duce nicăieri — și nu evaluează
limba.

### Articol dens de monitorizare, modul `--news`

O ediție a [buletinului de monitorizare IA de pe jls42.org](https://jls42.org/fr/news):
589 de rânduri, 140 de linkuri, 21 de secțiuni, 3 citate în engleză protejate. Campanie
din 4 și 5 septembrie 2026.

| Model                                          | Acces              | Scrise | Fără abateri   | Mediană/limbă |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | API Google         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | abonament Google  | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | abonament Google  | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `claude-sonnet-5-5`                             | API Anthropic      | 14/14   | ✅ **14/14** | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | abonament ChatGPT | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | abonament Claude  | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | API Anthropic      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | abonament Claude  | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `claude-haiku-5-5`                              | API Anthropic      | 14/14   | ⚠️ 11/14     | 2 min 54 s     |
| `claude-haiku-4-5`                              | API Anthropic      | 14/14   | ⚠️ 7/14      | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | local              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | API Mistral        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | abonament Grok    | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | abonament Claude  | 0/14    | ❌ 0/14      | —              |

Grok a fost măsurat din nou pe 9 septembrie pe o altă ediție a aceluiași buletin
(356 de rânduri): 9 limbi scrise din 14, 8 fără abateri. Această cifră
apare în tabelul de la început. Trei campanii întrerupte nu sunt
incluse: `qwen3.5-27b` (9 limbi) și `kimi-k2.6` (4) din lipsă de credit,
`z-ai/glm-5.3-flash` ale cărui două eșecuri proveneau dintr-o setare de raționament
pe care providerul o corectează de atunci. Rândurile OpenRouter au fost măsurate cu
setările implicite ale routerului, înainte de `--use_openrouter`; `z-ai/glm-5.2`,
măsurat din nou cu providerul livrat, obține același 14/14. Cifrele au fost
recalculate pe 10 septembrie cu comparatorul actual: `qwen3.8-flash` și
`qwen3.7-flash` câștigă fiecare câte o limbă față de prima
publicare, celelalte rămân neschimbate.

Rândurile `--use_antigravity` au fost măsurate pe 26 septembrie pe același
articol, cu patru traduceri în paralel: `gemini-3.7-flash-medium` dimineața,
`gemini-3.8-flash-medium` după-amiaza. În engleză, fiecare a eliminat singur
cele trei rânduri de traducere franceză de sub citate, fără să inventeze vreun
steag, iar citatele în engleză sunt intacte: curățarea de rezervă nu a avut
nimic de făcut. În `--eco` (`gemini-3.7-flash-low`), pentru doar patru limbi
(en, ja, ar, hi): 4 scrise din 4, toate fără abateri, cu o mediană de
1 min 52 s. Verificare suplimentară în aceeași zi pe o ediție mai recentă a buletinului,
cea din 25 septembrie (438 de rânduri, 2 citate în engleză), tradusă în afara
blogului de `gemini-3.7-flash-medium`: 14 scrise din 14, toate fără abateri, între 87 și
128 s per limbă.

Rândurile `--use_claude_code` au fost măsurate pe 26 septembrie pe același
articol, cu patru traduceri în paralel, la nivelul de efort `low`. Cu `sonnet`,
citatele în engleză sunt intacte în toate cele paisprezece limbi și, în engleză,
modelul a eliminat singur rândurile de traducere franceză, fără să inventeze vreun
steag. `opus` nu a scris nicio limbă: în fiecare, mecanismele sale de protecție au
oprit răspunsul la ultimul segment, din cauza unei știri despre 279 de molecule
generate pentru un situs de legare. Trimisă separat, această știre este respinsă
în categoria „bio”; `sonnet` a tradus-o în toate limbile. `haiku` scrie
toate cele paisprezece limbi; în trei dintre ele (en, pl, ro), un titlu de secțiune trece de la
nivelul 2 la nivelul 1. Raționează fără să poată fi împiedicat — 61 % din
tokenii săi de ieșire —, de unde un timp de peste două ori mai mare decât la `sonnet`.

Rândurile `claude-sonnet-5-5`, `claude-haiku-5-5` și `claude-haiku-4-5` au
fost măsurate pe 18 octombrie prin API-ul Anthropic, pe același articol, cu patru
traduceri în paralel per model. Sonnet 5.5 refuză dezactivarea
reflecției: aipmt îi trimite cea mai mică setare pe care o acceptă, iar
răspunsurile sale nu conțin deloc reflecție. Scrie toate cele paisprezece limbi fără abateri și fără
să reia vreun segment; în engleză, a eliminat singur rândurile de
traducere franceză, fără să inventeze vreun steag, iar citatele în engleză sunt
intacte peste tot. Haiku 5.5 este măsurat cu reflecția sa adaptivă: cu reflecția
dezactivată, lăsa paragrafe întregi în franceză, pe care verificarea de protecție le respinge —
3 limbi scrise din 14. Ambele Haiku se împotmolesc la aceeași știre: Haiku 5.5
schimbă nivelul titlului ei sau îl dublează în japoneză, coreeană și
chineză, Haiku 4.5 îl trece la nivelul 1 în șapte limbi și îl lasă în
franceză în traducerea japoneză. Haiku 4.5 costă 3,67 $ pentru cele două documente în
toate cele paisprezece limbi, Haiku 5.5 0,57 $, Sonnet 5.5 9,21 $.
### README al acestui proiect, Markdown standard

Revizie fixată la 9 septembrie 2026: 785 de linii, 285 de fragmente de cod inline, 40
de delimitatori de închidere a blocurilor, 89 de linii de tabel. Patru traduceri în paralel.

| Model                                           | Scrise  | Fără abateri | Mediană/limbă | Ce diferă                                                                |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | nimic                                                                    |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | nimic                                                                    |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | nimic pentru comparator; linkuri interne dublate (en)                    |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | nimic                                                                    |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | nimic                                                                    |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | un cuvânt cu caractere aldine (ja)                                        |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | un cuvânt cu caractere aldine (ko)                                        |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | o linie de tabel lipită de cea anterioară (ar)                            |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | un link (sv), un cuvânt cu caractere aldine (zh)                         |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | un cuvânt cu caractere aldine (ar, ja)                                    |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | un cuvânt cu caractere aldine (hi, ja, ko)                                |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 40 de fragmente de cod inline adăugate în arabă; aldine (hi, ja, ko)      |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2 limbi refuzate (ar, hi): fragmente de cod inline pierdute la returnare  |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | o secțiune pierdută (ar, hi, ko); blocuri de cod adăugate (ja, ko, ro, zh) |

Două campanii întrerupte nu sunt evaluate: Grok, sesiune CLI expirată
după douăsprezece limbi (unsprezece fără abateri), și `qwen3.8-flash`, HTTP 429 de la
furnizorul său de găzduire după două. `opencode/mimo-v2.5-free` și `ollama/gpt-oss-20b-32k`
nu au fost măsurate din nou pe această revizie; pe cea din 4 și 5 septembrie,
mai scurtă cu 277 de linii, fiecare producea 9 traduceri din 14, dintre care 7,
respectiv 1 fără abateri.

Rândurile `--use_antigravity` și `--use_claude_code` nu au fost măsurate pe
revizia fixată, ci pe 26 septembrie, pe cea publicată cu 1.14.0 — iar
rândurile `claude-sonnet-5-5`, `claude-haiku-5-5` și `claude-haiku-4-5` pe 18
octombrie, pe aceeași revizie: 600 de linii, 257 de fragmente de cod inline, 30 de delimitatori de închidere a blocurilor, 85
de linii de tabel. Fiind mai
scurtă cu 185 de linii, nu poate fi comparată punct cu punct cu celelalte rânduri;
aceste rânduri pot însă fi comparate între ele. În privința linkurilor interne, pe care
comparatorul nu le verifică, `gemini-3.8-flash-medium` le-a păstrat intacte în
toate cele paisprezece limbi, `gemini-3.7-flash-medium` le-a stricat în italiană;
`sonnet` și `opus` le-au păstrat intacte peste tot, `haiku` le-a dublat în
engleză; `claude-sonnet-5-5` și `claude-haiku-4-5` le-au păstrat intacte în
toate cele paisprezece limbi, `claude-haiku-5-5` în cele douăsprezece în care a produs traduceri.

### Patru README ale unor proiecte cunoscute

FastAPI, Ollama, tldr-pages și Vue.js, preluate ca atare de pe GitHub — documente
mai ușoare decât cele două precedente. Campania a vizat modelele
care întâmpinau dificultăți; Gemini servește aici drept punct de comparație.

| Model                     | Domeniu de testare         | Scrise  | Fără abateri |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 proiecte × 14 limbi      | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 proiecte × 14 limbi      | 55/56   | ❌ 47/56     |
| `grok-4.6` (abonament)   | 4 proiecte × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 proiecte × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### Ce nu reprezintă aceste măsurători

- **Nu sunt un clasament exhaustiv**: numai OpenRouter oferă peste patru sute de
  modele; au fost măsurate aproximativ cincisprezece.
- **Duratele sunt orientative**: între trei și șase traduceri în paralel, în funcție de
  campanie, iar viteza unui furnizor variază pe parcursul zilei.
- **Sunt observații datate**: modelele se schimbă sub același nume, iar
  documentele voastre nu sunt ale noastre.

Pentru a repeta măsurătoarea pe documentele voastre, pe o copie fixată a fișierului:

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## Contribuții

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

Ambele linii sunt necesare: fără `pip install -e .`, `python -m aipmt`
răspunde cu `No module named aipmt`.

Instrumente de verificare a calității, opționale, dar recomandate:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Cele 28 de traduceri din depozit (README și CHANGELOG, paisprezece limbi) se
regenerează cu `./regen_translations.sh --force` — Codex și `gpt-6.1-sol` folosesc
implicit abonamentul ChatGPT, câte patru în paralel. `REGEN_PROVIDER` și
`REGEN_MODEL` schimbă calea: `antigravity` folosește în continuare un abonament, cel
de la Google, și rulează fără derogare; un API cu plată (`openai`, `gemini`,
`grok`, `openrouter`) este refuzat fără `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` limitează durata fiecărui job (600 s, 1 800 s pe Codex și
Antigravity). Detaliile despre instrumente se află în `CLAUDE.md`.

## Proiecte care folosesc acest script

- **[jls42.org](https://jls42.org)** — blog personal publicat în 15 limbi.
  [Monitorizarea zilnică a noutăților despre IA](https://jls42.org/fr/news) este tradusă în fiecare zi
  de acest instrument și servește drept document de referință pentru măsurătorile de mai sus.

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licență

GNU GENERAL PUBLIC LICENSE Versiunea 3. Consultați [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Avertisment

Acest program este distribuit **fără nicio garanție**, în condițiile
secțiunilor 15 și 16 din GPL v3: furnizat „ca atare”, fără garanție de vandabilitate
sau de adecvare la un anumit scop, iar autorul său nu poate fi
tras la răspundere pentru un prejudiciu rezultat din utilizarea sa. Textul
licenței prevalează asupra acestui rezumat.

- **Recitiți înainte de publicare.** Protecțiile acoperă blocurile de cod,
  codul inline, URL-urile, ancorele și citatele din modul `--news` — nu și
  titlurile, tabelele, front matter sau sensul frazelor voastre.
- **Documentele voastre sunt trimise furnizorului ales**, conform condițiilor sale
  de utilizare și politicii sale privind datele. Unele modele gratuite pot
  reutiliza conversațiile voastre pentru antrenare, iar condițiile Antigravity
  permit Google să le reutilizeze și să le supună examinării de către oameni,
  inclusiv în cazul unui abonament plătit; un model local este singura variantă prin care
  nicio dată nu părăsește computerul vostru.
- **Apelurile API vă sunt facturate.** Acest program nu limitează
  cheltuielile: un document lung, o reluare după un eșec sau un model care raționează
  mult costă mai mult.
- **Măsurătorile publicate sunt observații datate**, nu garanții.

Numele produselor și companiilor menționate aparțin deținătorilor
respectivi. Acest proiect nu este afiliat niciunuia dintre aceștia.

**Articol tradus din fr în ro cu gpt-6.1-sol.**

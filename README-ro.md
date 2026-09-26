# Traducător de Markdown AI-Powered

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

Traduce fișiere Markdown dintr-o limbă în alta, păstrând
structura: blocuri de cod, cod inline, URL-uri, ancore, tabele și front
matter. Zece modalități de a apela un model — cinci API-uri, trei abonamente fără
plată per utilizare, două rutere — și o măsurătoare publicată a ceea ce
păstrează de fapt fiecare model.

## Pe scurt

- **Zece căi de furnizori**: API-uri OpenAI, Mistral, Claude, Gemini și Grok;
  abonamente ChatGPT (Codex), Grok și Google (Antigravity) fără plată per
  utilizare; rutere OpenCode (open source, gratuit sau local) și OpenRouter
  (peste 400 de modele).
- **Nimic eronat din cauza unui token pierdut**: blocurile de cod, codul inline,
  URL-urile, ancorele și citatele sunt înlocuite cu tokenuri înainte de apel și
  verificate la întoarcere. Dacă lipsește vreunul, fișierul nu este scris.
- **Documente lungi**: segmentare în funcție de fereastra modelului.
- **Modul `--news`**: citate în limba engleză protejate și steaguri gestionate per
  limbă, pentru articolele de monitorizare.
- **Modul `--eco`**: modele rapide și mai ieftine.
- **Notă de traducere** opțională, sus, jos sau în ambele locuri.

## Instalare

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 sau mai recent. Pentru instalare din depozit, consultați
[Contribuire](#contribuții).

## Configurare

Cheile sunt citite din trei locuri, de la cea mai mare prioritate la cea mai mică; fiecare
completează doar ceea ce precedentul lasă gol.

|     | Unde                                          | Pentru ce                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variabile de mediu                            | CI, containere, suprascriere punctuală |
| 2   | `.env` din directorul curent (sau părinte) | o cheie specifică unui proiect        |
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

`GEMINI_API_KEY` este acceptat în locul `GOOGLE_API_KEY`. Fișierul
utilizatorului respectă `XDG_CONFIG_HOME` (doar cale absolută) și `%APPDATA%`
pe Windows. Fără nicio cheie, comanda enumeră cele trei locații.

**Fișierul `.env` al unui proiect nu poate nici să redirecționeze apelurile, nici să aleagă programul
executat.** Acesta furnizează chei, niciodată o destinație sau un binar: orice
variabilă din `_BASE_URL`, `_API_BASE`, `_ENDPOINT` sau `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, proxy-urile (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), depozitele de certificate (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) și `XDG_CONFIG_HOME` /
`APPDATA` sunt ignorate acolo, afișând un avertisment. Un depozit clonat nu trebuie să
vă poată deturna cheia și nici să vă determine să rulați propriul său program la
prima traducere. Acest fișier este citit, de asemenea, fără interpolare:
`NOM=${OPENAI_API_KEY}` nu copiază cheia în el. Setați aceste variabile în
mediu sau în `~/.config/aipmt/.env`.

Variabile opționale: `XAI_BASE_URL` (implicit `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (secunde per apel, implicit 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(implicit 600), `GROK_BIN`, `GROK_HOME` (implicit `~/.grok`), `GROK_TIMEOUT`
(implicit 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (implicit 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (implicit 600), `OPENROUTER_BASE_URL`
(se cere `https://`), `OPENROUTER_TIMEOUT` (implicit 900),
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

`document.md` tradus în spaniolă generează `document-es.md` în `--target_dir`;
cu `--include_model`, `document-es-gpt-5.6-terra.md`. Extensia devine
întotdeauna `.md` — `article.mdx` generează `article-en.md` — cu excepția
utilizării `--keep_filename`, care păstrează numele original. O traducere deja existentă
este omisă fără `--force`.

Coduri de ieșire: `0` dacă totul a reușit sau a fost omis, `1` dacă a rămas vreun fișier
eșuat (listă la ieșirea de eroare), `2` dacă problema este de configurare.
Un fișier eșuat nu este niciodată scris, chiar dacă scrierea însăși eșuează:
conținutul este scris alături și apoi redenumit. O reluare este suficientă.

## Ce model să alegeți

Măsurat pe două documente reale, traduse în aceleași paisprezece limbi de
fiecare model. **Cifra reprezintă numărul de limbi, din paisprezece, în care
traducerea este scrisă și nimic nu diferă de sursă.**

| Model                | Cum se accesează                  | Articol dens de monitorizare | Acest README | Ce diferă și în câte limbi                                                                                                            |
| -------------------- | --------------------------------- | ---------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | cheie API Google                  | ✅ 14/14                     | ⚠️ 13/14     | 1 limbă din 14: un cuvânt îngroșat în plus (ja)                                                                                       |
| **Gemini 3.7 Flash** | abonament Google (Antigravity)    | ✅ 14/14                     | ⚠️ 13/14     | 1 limbă din 14: un cuvânt îngroșat în minus (ko)                                                                                      |
| **GPT-5.6 Sol**      | abonament ChatGPT sau cheie OpenAI | ✅ 14/14                     | ⚠️ 12/14     | 2 limbi din 14: un cuvânt îngroșat în minus (ar, ja)                                                                                  |
| **GLM-5.2**          | cheie OpenRouter                  | ✅ 14/14                     | ⚠️ 11/14     | 3 limbi din 14: un cuvânt îngroșat în minus (hi, ja, ko)                                                                              |
| Claude Sonnet 5      | cheie API Anthropic               | ⚠️ 11/14                     | ⚠️ 12/14     | 3 limbi la articol: a apărut un bloc de cod (es, de, hi); 2 la acest README: un link fără formatare (sv), un cuvânt îngroșat (zh)     |
| Qwen 3.7 Flash       | cheie OpenRouter                  | ❌ 8/14                      | ⚠️ 10/14     | 1 limbă refuzată la articol, alte 5 se abat; la acest README, aproximativ 40 de cuvinte puse în `code` (ar)                   |
| Grok 4.6             | abonament Grok                    | ❌ 8/14                      | neevaluat    | 5 limbi refuzate din 14, din cauza codurilor inline și URL-urilor redate lipsă; olandeza diferă în totalitate                         |
| GPT-OSS 20B          | model local (Ollama)              | ❌ 7/14                      | nemăsurat din nou | 4 limbi refuzate din 14: modelul lăsa pasaje în franceză, filtrul de siguranță le-a oprit                                           |
| MiMo v2.5 (gratuit)  | OpenCode Zen, fără cont           | ❌ 11/14                     | nemăsurat din nou | 1 limbă refuzată; o secțiune pierdută în poloneză                                                                                     |
| Mistral Large        | cheie API Mistral                 | ❌ 5/14                      | ❌ 1/14      | **o secțiune întreagă dispare**: 1 limbă la articol (hi), 3 la acest README (ar, hi, ko) — și 3 limbi refuzate la articol             |
| DeepSeek V4 Flash    | cheie OpenRouter                  | ❌ 3/14                      | nemăsurat din nou | 10 limbi refuzate din 14; 37 de minute per limbă                                                                                     |

|     | Ce indică simbolul                                                                                                                                                                                    |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | toate cele paisprezece limbi traduse și nimic nu diferă de sursă                                                                                                                                      |
| ⚠️  | toate cele paisprezece limbi traduse; ceea ce diferă este legat de **marcare** — un cuvânt îngroșat, un `code`, un link care își pierde parantezele drepte. Nu lipsește niciun text, niciun URL, niciun bloc de cod, nicio secțiune |
| ❌  | cel puțin o limbă nu a putut fi tradusă — fișierul este respins, nu este scris — **sau** lipsește conținut dintr-un fișier scris                                                                      |

Ce trebuie reținut:

- **O traducere refuzată nu este o traducere deteriorată.** Când un token
  lipsește la returnare, fișierul nu este scris, iar limba este considerată
  refuzată. Asta i se întâmplă lui Grok la articol: patru coduri inline și
  trei URL-uri pierdute încă de la primul segment, pe cele cinci sisteme de scriere non-latine.
- **Această plasă de siguranță nu acoperă titlurile, tabelele, front matter-ul sau
  textul.** Un model care elimină o secțiune generează un fișier pe care instrumentul îl scrie
  fără ezitare — este cazul Mistral. Aceste elemente nu pot fi
  înlocuite cu un token, iar filtrele actuale nu le controlează;
  `scripts/compare_structure.py` detectează o secțiune pierdută, dar după aceea.
- **Grok nu are o notă pentru acest README**: sesiunea sa CLI a expirat după douăsprezece
  limbi, dintre care unsprezece fără abateri. O campanie întreruptă nu se notează.
- **Densitatea documentului contează mai mult decât limba.** Grok face față la fișiere
  README obișnuite și cedează la un articol încărcat cu linkuri, inclusiv în
  neerlandeză.

Date și documente: coloana „Acest README” a fost măsurată pe 9 septembrie 2026
pe o revizie înghețată a acestui fișier (785 de linii, 285 de coduri inline, 89 de linii
de tabel), modificată de atunci — cu excepția rândului Antigravity, măsurat pe
26 septembrie pe revizia publicată cu versiunea 1.14.0, mai scurtă (600 de linii,
257 de coduri inline, 85 de linii de tabel). Coloana „Articol dens de
monitorizare” provine din campania din 4 și 5 septembrie pe un articol de 589 de linii,
cu excepția rândului Grok, remăsurat pe 9 septembrie pe o altă ediție a aceleiași
monitorizări, și a rândului Antigravity, măsurat pe 26 septembrie pe același articol.
Tabelele complete, duratele și protocolul se găsesc în
[Măsurători detaliate](#măsurători-detaliate).

## Toate opțiunile

| Opțiune                  | Descriere                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Fișier Markdown unic de tradus (alternativă la `--source_dir`)                                                |
| `--source_dir`           | Directorul sursă care conține fișierele Markdown (implicit: `content/posts`)                                   |
| `--target_dir`           | Directorul de ieșire pentru fișierele traduse (implicit: `traductions_en`)                                      |
| `--source_lang`          | Limba sursă (implicit: `fr`)                                                                        |
| `--target_lang`          | Limba țintă (implicit: `en`)                                                                        |
| `--model`                | Modelul specific de utilizat                                                                                  |
| `--eco`                  | Utilizați modele economice                                                                                    |
| `--use_mistral`          | Utilizați API-ul Mistral AI                                                                                   |
| `--use_claude`           | Utilizați API-ul Claude                                                                                       |
| `--use_gemini`           | Utilizați API-ul Gemini                                                                                       |
| `--use_grok`             | Utilizați API-ul xAI (Grok) — necesită `XAI_API_KEY`                                                         |
| `--use_codex`            | Utilizați CLI-ul Codex pe cota abonamentului ChatGPT                                                          |
| `--use_grok_cli`         | Utilizați CLI-ul Grok pe cota abonamentului Grok                                                              |
| `--use_antigravity`      | Utilizați CLI-ul Antigravity (`agy`) pe cota abonamentului Google AI Pro sau Ultra                      |
| `--use_opencode`         | Utilizați OpenCode (open source) către furnizorul configurat în OpenCode; necesită `--model provider/modèle`             |
| `--use_openrouter`       | Utilizați OpenRouter — necesită `OPENROUTER_API_KEY` și `--model fournisseur/modèle`                                              |
| `--force`                | Forțați retraducerea                                                                                          |
| `--keep_filename`        | Păstrați numele original al fișierului                                                                        |
| `--news`                 | Mod știri: protejează citatele EN, gestionează steagurile per limbă                                           |
| `--add_translation_note` | Adăugați o notă de traducere                                                                                  |
| `--note_position`        | Poziția notei: `top`, `bottom` (implicit) sau `both`                                   |
| `--note_format`          | Formatul notei: `legacy` (implicit, paragraf îngroșat) sau `marker`                              |
| `--include_model`        | Includeți numele modelului în fișierul de ieșire                                                              |
| `--reasoning_effort`     | Efort de raționament GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

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

| Provider    | Calitate (implicit)                                   | Economic (`--eco`) |
| ----------- | ----------------------------------------------------- | -------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5`                                       | `claude-haiku-4-5`            |
| Mistral     | `mistral-large-latest`                                       | `mistral-small-latest`            |
| Gemini      | `gemini-3.7-flash`                                       | `gemini-3.1-flash-lite`            |
| Codex       | `gpt-5.6-sol` (de asemenea `terra` și `luna` prin `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                       | `grok-4.3`            |
| Grok CLI    | `grok-4.6`                                       | `grok-4.5`            |
| Antigravity | `gemini-3.7-flash-medium`                                       | `gemini-3.7-flash-low`            |
| OpenCode    | `--model provider/modèle` obligatoriu                           | idem — `--eco` fără efect |
| OpenRouter  | `--model fournisseur/modèle` obligatoriu                           | idem — `--eco` fără efect |

### Pe abonamentul ChatGPT: `--use_codex`

Controlează CLI-ul Codex oficial: traducerea este dedusă din cota
abonamentului ChatGPT, fără cheie API sau facturare după utilizare.

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
  dacă validarea sa eșuează și este reîncercat. OpenAI anunță, cu titlu
  estimativ, 250–2.000 de mesaje/5 h pentru `gpt-5.6-luna` (`--eco`) și
  10–100 pentru `gpt-5.6-sol` pe un plan Plus.
- `--model gpt-5.6-terra` și `--model gpt-5.6-luna` trec de asemenea prin
  abonament. Un model la care contul nu are acces întoarce o eroare 400 „model is
  not supported when using Codex with a ChatGPT account”.
- Mai lent decât un API, iar diferența crește odată cu dimensiunea documentului: pe acest README,
  o mediană de 6 min 46 s per limbă cu `gpt-5.6-sol`, față de 36 s pentru
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

- **Izolare mai slabă decât Codex.** Sandbox-ul OS din Grok nu se aplică
  pe multe sisteme Linux recente (AppArmor, socket-uri de runtime pentru
  containere), iar un profil care nu se poate aplica pornește neizolat în mod
  silențios. Prin urmare, scriptul nu solicită niciun profil în mod implicit, îl anunță și
  se bazează pe regulile `--deny` ale CLI-ului, inclusiv pe clauza catch-all `*` — singurul
  nivel care refuză să pornească în loc să elimine protecția fără
  avertisment. `GROK_TRANSLATE_SANDBOX=read-only` impune sandbox-ul OS, iar pornirea
  eșuează dacă mașina nu îl poate respecta.
- Cota este săptămânală, partajată cu Chat, Imagine și Voice, și nicio
  comandă nu permite citirea ei: un lot poate consuma din utilizarea conversațională
  fără avertisment.
- Variabile: `GROK_BIN`, `GROK_HOME` (directorul CLI-ului, implicit `~/.grok`),
  `GROK_TIMEOUT` (implicit 900), `GROK_TRANSLATE_SANDBOX`.

### Pe abonamentul Google: `--use_antigravity`

Același principiu cu `agy`, CLI-ul oficial Antigravity: pentru cei care plătesc Google
AI Pro sau Ultra, traducerea este dedusă din cota abonamentului în loc
să fie facturată per token. Este singura cale către această cotă: Gemini CLI nu
mai deservește aceste conturi din 18 iunie 2026
([anunț](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
iar SDK-ul Antigravity acceptă doar o cheie API sau un proiect Google Cloud.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Nicio cale plătită nu rămâne deschisă.** agy primește din mediul
  dumneavoastră doar o listă restrânsă de variabile — `PATH`, limbă și fus orar,
  terminal, identitate, proxy-uri și certificate, magistrală de sesiune — și nicio cheie:
  câteva dintre variabilele sale pot redirecționa un apel fără a afișa nimic (măsurat:
  una trimite documentul către un gateway terț, alta către un proiect
  Google Cloud facturat), iar o listă de respingere scăpa din vedere câteva la fiecare revizuire.
  Înainte de orice segment, `agy -p /config`, care nu consumă din cotă, trebuie să arate
  că creditele AI plătite sunt dezactivate, fără cheie API sau proiect Google Cloud — o
  setare lipsă echivalează cu un refuz —, altfel nu se traduce nimic; jurnalul fiecărui
  apel trebuie apoi să ateste abonamentul (`authMethod=consumer`), altfel
  răspunsul este refuzat.
- **Izolare.** Fiecare apel rulează într-un director personal privat și
  de unică folosință, cu un agent de traducere fără unelte: configurările, regulile,
  pluginurile, serverele MCP și hook-urile agy nu ajung acolo, nimic nu se adaugă la
  istoricul dumneavoastră, iar conexiunea rămâne în keychain, pe care aipmt nu îl citește niciodată.
  Un agent negăsit face ca agy să revină silențios la agentul de codare
  și la uneltele sale: o linie întreagă din jurnal trebuie să confirme agentul corect — un
  document care citează acest mesaj nu o înlocuiește —, altfel apelul este refuzat.
- **Platforme**: Linux, într-o sesiune care are un keychain (magistrală de sesiune
  D-Bus, Secret Service); macOS este acceptat, fără a fi fost măsurat acolo. Refuzat
  pe Windows, unde agy nu citește variabilele care izolează fiecare apel, și
  pe Linux fără magistrală de sesiune — sesiune SSH, container, server: agy își
  stochează acolo tokenul într-un fișier din `~/.gemini`, pe care izolarea îl maschează.
  Refuzul survine înainte de orice lansare, indicând cauza, în loc de un minut
  de așteptare a unui cod de autentificare.
- **Modele**: cele din `agy models`. Modelele Gemini includ nivelul de efort în nume
  (`gemini-3.7-flash-low`…): un nume fără sufix este refuzat înainte de apel, iar
  `--reasoning_effort` nu are niciun efect. Cele două valori implicite au fost stabilite în urma unei
  campanii pe paisprezece limbi (consultați [Măsurători detaliate](#măsurători-detaliate)).
  Claude și GPT-OSS au propria cotă, mult mai redusă: aproximativ 1% din
  fereastra de 5 ore per apel măsurat, față de 0,05% pentru Flash.
- **Cotă**: per grup, o fereastră de 5 ore și una săptămânală, proporțional
  cu costul în tokenuri. Măsurat pe contul autorului, pe baza unei
  campanii de 32 de traduceri: aproximativ o jumătate de procent din fereastra de 5 ore
  pentru un README de 40.000 de caractere cu `gemini-3.7-flash-medium`; limita
  săptămânală depinde de nivelul abonamentului. Reîncercarea respectă ceea ce agy declară
  ca fiind reîncercabil; în caz contrar, o fereastră epuizată nu este niciodată reluată: duce la
  eșecul fiecărui fișier până la resetarea afișată de `/usage`.
- **Mai lent decât API-ul**: pe articolul dens al măsurătorilor, Gemini 3.7 Flash
  necesită o mediană de 3 min 14 s per limbă prin abonament, față de 1 min 18 s prin
  API.
- **Întrerupere**: Ctrl-C sau închiderea terminalului opresc agy odată cu
  comanda, în loc să-l lase să-și termine runda consumând din cotă; același lucru este
  valabil pentru Codex, Grok CLI și OpenCode. Sub `nohup`, traducerea continuă.
- Refuzat în CI (`CI` sau `GITHUB_ACTIONS` definit): conexiunea se află într-un
  keychain personal. Pe un runner, utilizați `--use_gemini` cu `GOOGLE_API_KEY`.
- Variabile: `AGY_BIN` (altfel `PATH`, apoi `~/.local/bin/agy`),
  `AGY_TIMEOUT` (secunde per segment, inclusiv pornirea, implicit 900).

**Termeni și condiții: vă asumați responsabilitatea contului dumneavoastră.** [Termenii
Antigravity](https://antigravity.google/terms) (secțiunea 6) și
[FAQ-ul](https://antigravity.google/docs/faq/) aferent interzic accesarea serviciului
printr-un software terț folosind conexiunea Antigravity — Claude Code,
OpenClaw și OpenCode sunt menționate expres —, sub sancțiunea suspendării contului. aipmt
nu citește și nu reutilizează tokenul: lansează binarul oficial în
[modul headless](https://antigravity.google/docs/cli/headless/) pe care Google
îl documentează pentru scripturi și CI. Un membru Google a considerat „standard”
lansarea `agy -p` dintr-un script local pentru munca proprie
([forum oficial, 25 septembrie 2026, răspuns fără valoare contractuală](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
niciun text oficial nu tranșează cazul unui instrument distribuit precum acesta.

**Doar documente publice.** Conform secțiunii 5 din aceiași termeni,
schimburile de date — prompturi, răspunsuri, metadate — pot fi utilizate pentru a îmbunătăți
produsele și învățarea automată Google și pot fi revizuite de evaluatori
umani, inclusiv pe abonamentele plătite. Renunțarea se face prin setarea
`enableTelemetry`, cu efect nedocumentat, pe care aipmt nu o configurează; setările dumneavoastră
din agy nu se transmit în mediul său izolat. Nu trimiteți nimic confidențial.

### Către furnizorul la alegere: `--use_opencode`

[OpenCode](https://opencode.ai) este un agent de codare open source (MIT) care
direcționează cererile către furnizorii configurați în cadrul său: cheie API, abonament,
gateway-ul OpenCode Zen (modele gratuite, fără cont) sau model local. Două
căi au fost măsurate cap-la-cap aici: Zen și Ollama.

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
ale cărui conversații pot fi utilizate pentru antrenare, iar această alegere nu este făcută în
locul dumneavoastră.

Izolare la fiecare apel:

- o configurare inline, cu prioritate față de a dumneavoastră, definește un agent `aipmt`
  ale cărui unelte sunt toate refuzate (`permission: { "*": "deny" }`), partajarea
  sesiunii fiind dezactivată, `--pure`, niciodată `--auto`;
- director de lucru temporar și gol, cu `OPENCODE_DISABLE_PROJECT_CONFIG` și
  `OPENCODE_DISABLE_CLAUDE_CODE` setate — fără ele, OpenCode injectează în
  prompt `AGENTS.md` din directorul curent și `~/.claude/CLAUDE.md`. Fișierul
  `~/.config/opencode/AGENTS.md` global rămâne injectat, OpenCode nepermițând
  excluderea lui;
- contract de ieșire: cod de retur 0, niciun eveniment `error`, niciun apel
  de unealtă, ultimul pas în `stop`, text nevid și agentul `aipmt`
  încărcat efectiv — un `--agent` necunoscut nu oprește OpenCode cu eroare, ci
  revine silențios la agentul de codare;
- nicio cheie din `aipmt` nu este transmisă, cu excepția `OPENCODE_API_KEY`, cheia
  OpenCode însuși. Furnizorii se configurează în OpenCode, nu în
  `.env` din `aipmt`.

De știut:

- Modelele gratuite din Zen sunt variabile, cu limite nedocumentate, iar
  conversațiile lor pot fi utilizate pentru antrenare: potrivite pentru documentație
  publică, nu pentru conținut privat.
- Un model local trebuie să ofere cel puțin 16k tokenuri de context,
  segmentele având până la 16.000 de caractere. Ollama configurează adesea 4.096: folosiți
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

`reasoningEffort: "none"` dezactivează raționamentul pe care Ollama îl activează implicit pe aceste
modele și pe care un Modelfile nu îl poate dezactiva. Măsurat pe o propoziție de
șase cuvinte: 919 tokenuri de raționament și 68 de secunde fără opțiune, 9 tokenuri cu opțiunea activată.

### Către peste 400 de modele: `--use_openrouter`

OpenRouter este un ruter facturat după utilizare, pe baza unui credit unic, plasat în fața unor
modele găzduite de terți — inclusiv modelele chinezești open-source pe care niciun
alt furnizor nu le expune aici.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` este obligatoriu. O verificare preflight, executată înainte de orice facturare, gestionează
două particularități de rutare:

- **Același model este servit de zeci de furnizori de găzduire cu limite
  diferite** — pentru `z-ai/glm-5.3-flash`, 23 de gazde, dintre care una limitată la
  2.048 de tokenuri de ieșire. Verificarea preflight citește `/api/v1/models/{modèle}/endpoints`,
  exclude gazdele cu sub 8.000 de tokenuri de ieșire sau cu stare degradată și
  le fixează pe celelalte cu `allow_fallbacks: false`.
- **Raționamentul este facturat la tariful de ieșire** — 107 tokenuri față de 2 la
  un răspuns „OK” din partea `z-ai/glm-5.2`. Este dezactivat în mod implicit; modelele
  care îl impun primesc cel mai mic nivel de efort pe care îl acceptă, valoarea implicită din
  catalog riscând să satureze ieșirea înainte de finalizarea traducerii.
  `--reasoning_effort` rămâne prioritar.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Fereastra de context provine din catalog. Un model sub 16.400 de tokenuri este
  refuzat înainte de orice apel: 8.400 pentru prompt și segment, minimum 8.000
  pentru ieșire.
- Un slug absent din catalog, un catalog inaccesibil sau absența
  unui furnizor de găzduire care să respecte limita opresc comanda.
- `finish_reason=length` cu ieșire goală indică un buget consumat de
  raționament, nu o trunchiere: mesajul face această distincție.
- `--eco` nu are efect.
- Variabile: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (implicit `https://openrouter.ai/api/v1`, necesită `https://`),
  `OPENROUTER_TIMEOUT` (implicit 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (implicit 30).

### Notă de traducere

`--add_translation_note` adaugă o notă, la `bottom` (implicit), `top` (după
front matter) sau `both` (`--note_position`), în format `legacy` (paragraf în
aldine, implicit) sau `marker` (`--note_format`). Formatul `marker` este o
definiție de referință Markdown invizibilă,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
urmată de un citat în aldine: lizibilă pe GitHub, utilizabilă la build de un
plugin remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Măsurători detaliate

Toate măsurătorile sunt traduceri executate real cu `aipmt`, către
paisprezece limbi: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Scrise** numără fișierele pe care mecanismele de protecție le-au lăsat să treacă; **Fără
discrepanțe** pe cele în care `scripts/compare_structure.py` nu identifică nicio diferență — același număr de
secțiuni, subtitluri, linkuri, URL-uri distincte, blocuri de cod,
coduri inline, rânduri de tabel, blocuri de citare și cuvinte în aldine.

„Fără discrepanțe” înseamnă „nimic detectat”, nu „identic”: comparatorul
numără elemente fără a le citi conținutul. Nu semnalează niciun titlu de
nivel 4 șters, nici textul unui cod inline înlocuit, niciun flag
schimbat și nu evaluează limba.

### Articol dens de monitorizare, modul `--news`

O ediție a [monitorizării IA de pe jls42.org](https://jls42.org/fr/news):
589 de rânduri, 140 de linkuri, 21 de secțiuni, 3 citate în engleză protejate. Campanie
din 4 și 5 septembrie 2026.

| Model                                           | Acces              | Scrise  | Fără abateri | Mediană/limbă  |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | API Google         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | abonament Google   | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | abonament ChatGPT  | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `claude-sonnet-5`                               | API Anthropic      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | local              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | API Mistral        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | abonament Grok     | 1/14    | ❌ 1/14      | 23 min 11 s    |

Grok a fost remăsurat pe 9 septembrie pe o altă ediție a aceleiași monitorizări
(356 de rânduri): 9 limbi scrise din 14, 8 fără abateri. Această cifră este cea
care figurează în tabelul principal. Trei campanii întrerupte nu sunt
notate: `qwen3.5-27b` (9 limbi) și `kimi-k2.6` (4) din lipsă de credite,
`z-ai/glm-5.3-flash` ale cărui două eșecuri proveneau dintr-o setare de raționare
pe care furnizorul o corectează de atunci. Rândurile OpenRouter au fost măsurate
la setările implicite ale ruterului, înainte de `--use_openrouter`; `z-ai/glm-5.2`,
remăsurat cu furnizorul livrat, oferă același 14/14. Cifrele au fost
recalculate pe 10 septembrie cu comparatorul actual: `qwen3.8-flash` și
`qwen3.7-flash` câștigă fiecare câte o limbă față de prima
publicare, celelalte rămânând neschimbate.

Rândul `--use_antigravity` a fost măsurat pe 26 septembrie pe același articol,
patru traduceri în paralel. În engleză, modelul a eliminat el însuși cele
trei rânduri de traducere în franceză de sub citate, fără a inventa vreun
steag, iar citatele în engleză sunt intacte: curățarea de rezervă nu a
avut nimic de făcut. În `--eco` (`gemini-3.7-flash-low`), pe doar patru limbi
(en, ja, ar, hi): 4 scrise din 4, toate fără abateri, mediană de 1 min 52 s.

### README-ul acestui proiect, Markdown standard

Revizie înghețată pe 9 septembrie 2026: 785 de rânduri, 285 de fragmente de cod inline, 40
de închideri de blocuri, 89 de rânduri de tabel. Patru traduceri în paralel.

| Model                                           | Scrise  | Fără abateri | Mediană/limbă  | Ce diferă                                                                |
| ----------------------------------------------- | ------- | ------------ | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14     | 36 s           | un cuvânt îngroșat (ja)                                                  |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14     | 1 min 22 s     | un cuvânt îngroșat (ko)                                                  |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14     | 2 min 56 s     | un link (sv), un cuvânt îngroșat (zh)                                    |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14     | 6 min 46 s     | un cuvânt îngroșat (ar, ja)                                              |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14     | 2 min 34 s     | un cuvânt îngroșat (hi, ja, ko)                                          |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14     | 2 min 17 s     | 40 de coduri inline adăugate în arabă; caractere aldine (hi, ja, ko)     |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14      | 2 min 44 s     | o secțiune pierdută (ar, hi, ko); blocuri de cod adăugate (ja, ko, ro, zh) |

Două campanii întrerupte nu sunt notate: Grok, sesiune CLI expirată
după douăsprezece limbi (unsprezece fără abateri), și `qwen3.8-flash`, HTTP 429 de la
gazda sa după două. `opencode/mimo-v2.5-free` și `ollama/gpt-oss-20b-32k`
nu au fost remăsurați pe această revizie; pe cea din 4 și 5 septembrie,
mai scurtă cu 277 de rânduri, fiecare scria câte 9 traduceri din 14, dintre care 7
și 1 fără abateri.

Rândul `--use_antigravity` nu a fost măsurat pe revizia înghețată, ci pe
26 septembrie pe cea publicată odată cu 1.14.0: 600 de rânduri, 257 de coduri inline,
30 de închideri de blocuri, 85 de rânduri de tabel. Fiind mai scurt cu 185 de rânduri, nu
se compară termen cu termen cu celelalte rânduri.

### Patru fișiere README ale unor proiecte cunoscute

FastAPI, Ollama, tldr-pages și Vue.js, preluate ca atare de pe GitHub —
documente mai ușoare decât cele două anterioare. Campania a vizat modelele
aflate în dificultate; Gemini servește drept punct de comparație.

| Model                     | Perimetru                  | Scrise  | Fără abateri |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 proiecte × 14 limbi      | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 proiecte × 14 limbi      | 55/56   | ❌ 47/56     |
| `grok-4.6` (abonament)    | 4 proiecte × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 proiecte × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### Ce nu sunt aceste măsurători

- **Nu sunt un clasament exhaustiv**: Doar OpenRouter oferă peste patru sute de
  modele, fiind măsurate în jur de cincisprezece.
- **Sunt durate orientative**: între trei și șase traduceri în paralel în funcție
  de campanii, iar debitul unui furnizor variază pe parcursul zilei.
- **Sunt observații datate**: modelele se schimbă sub același nume, iar
  documentele dumneavoastră nu sunt ale noastre.

Pentru a reface măsurătoarea pe documentele dumneavoastră, pe o copie înghețată a fișierului:

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

Ambele rânduri sunt necesare: fără `pip install -e .`, `python -m aipmt`
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
abonamentul ChatGPT în mod implicit, patru în paralel. `REGEN_PROVIDER` și
`REGEN_MODEL` schimbă calea: `antigravity` rămâne pe un abonament, cel
Google, și trece fără derogare; un API facturat (`openai`, `gemini`,
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

## Declinare a responsabilității

Acest program este distribuit **fără nicio garanție**, în termenii
secțiunilor 15 și 16 din GPL v3: furnizat „ca atare”, fără garanție de vandabilitate
sau de adecvare pentru un anumit scop, iar autorul său nu poate fi
tras la răspundere pentru daunele rezultate din utilizarea sa. Textul
licenței prevalează asupra acestui rezumat.

- **Recitiți înainte de a publica.** Protecțiile acoperă blocurile de cod,
  codul inline, URL-urile, ancorele și citatele modului `--news` — nu și
  titlurile, tabelele, front matter-ul sau sensul frazelor dumneavoastră.
- **Documentele dumneavoastră ajung la furnizorul ales**, conform condițiilor sale
  de utilizare și politicii sale de confidențialitate a datelor. Unele modele gratuite pot
  reutiliza schimburile dumneavoastră pentru antrenare, iar termenii Antigravity
  permit Google să le reutilizeze și să le trimită spre verificare umană,
  inclusiv pe abonamentele plătite; un model local este singura modalitate care nu permite
  ieșirea niciunei date din calculatorul dumneavoastră.
- **Apelurile API vă sunt facturate.** Acest program nu plafonează
  cheltuielile: un document lung, o reluare după eșec sau un model care raționează
  mult costă mai mult.
- **Măsurătorile publicate sunt observații datate**, nu garanții.

Numele de produse și companii menționate aparțin deținătorilor
respectivi. Acest proiect nu este afiliat cu niciunul dintre aceștia.

**Articol tradus din fr în ro cu gemini-3.7-flash-medium.**

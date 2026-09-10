# Traducător Markdown bazat pe AI

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Probleme de cod"></a>
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
matter. Nouă moduri de a apela un model — cinci API-uri, două abonamente fără
facturare în funcție de utilizare, două routere — și o evaluare publicată a ceea ce păstrează
în realitate fiecare model.

## Pe scurt

- **Nouă căi de provider**: API-urile OpenAI, Mistral, Claude, Gemini și Grok;
  abonamentele ChatGPT (Codex) și Grok fără facturare în funcție de utilizare; routerele
  OpenCode (open source, gratuit sau local) și OpenRouter (peste 400 de modele).
- **Niciun rezultat eronat din cauza unui token pierdut**: blocurile de cod, codul inline,
  URL-urile, ancorele și citatele sunt înlocuite cu tokenuri înainte de apel și
  verificate la întoarcere. Dacă lipsește unul, fișierul nu este scris.
- **Documente lungi**: segmentare în funcție de fereastra modelului.
- **Modul `--news`**: citate în engleză protejate și steaguri gestionate în funcție de
  limbă, pentru articolele de monitorizare.
- **Modul `--eco`**: modele rapide și mai ieftine.
- **Notă de traducere** opțională, în partea de sus, în partea de jos sau în ambele locuri.

## Instalare

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 sau o versiune mai recentă. Pentru instalarea din repository, consultați
[Contribuții](#contribuții).

## Configurare

Cheile sunt citite din trei locuri, de la cea mai mare la cea mai mică prioritate; fiecare
completează numai ceea ce precedentul lasă necompletat.

|     | Unde                                            | Pentru ce                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variabile de mediu                     | CI, containere, suprascriere punctuală |
| 2   | `.env` din directorul curent (sau dintr-un director părinte) | o cheie specifică unui proiect            |
| 3   | `~/.config/aipmt/.env`                        | instalată o singură dată, valabilă peste tot       |

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
utilizatorului urmează `XDG_CONFIG_HOME` (numai cale absolută) și `%APPDATA%`
în Windows. Fără cheie, comanda enumeră cele trei locații.

**Fișierul `.env` al unui proiect nu poate redirecționa apelurile.** Acesta furnizează chei,
niciodată o destinație: orice variabilă din `_BASE_URL`, `_API_BASE` sau
`_ENDPOINT`, proxy-urile (`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`), depozitele
de certificate (`SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`,
`CURL_CA_BUNDLE`) și `XDG_CONFIG_HOME` / `APPDATA` sunt ignorate acolo, cu un
avertisment. Un repository clonat nu trebuie să vă poată deturna cheia. Acest
fișier este citit și fără interpolare: `NOM=${OPENAI_API_KEY}` nu copiază
cheia în el. Setați aceste variabile în mediu sau în
`~/.config/aipmt/.env`.

Variabile opționale: `XAI_BASE_URL` (implicit `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (secunde per apel, implicit 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(implicit 600), `GROK_BIN`, `GROK_HOME` (implicit `~/.grok`), `GROK_TIMEOUT`
(implicit 900), `GROK_TRANSLATE_SANDBOX`, `OPENCODE_BIN`, `OPENCODE_TIMEOUT`
(implicit 600), `OPENROUTER_BASE_URL` (`https://` obligatoriu), `OPENROUTER_TIMEOUT`
(implicit 900), `OPENROUTER_PREFLIGHT_TIMEOUT` (implicit 30). Fiecare este descrisă în detaliu
în secțiunea providerului său.

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
cu `--include_model`, produce `document-es-gpt-5.6-terra.md`. Extensia devine
întotdeauna `.md` — `article.mdx` produce `article-en.md` — cu excepția utilizării
`--keep_filename`, care păstrează numele original. O traducere deja existentă
este omisă fără `--force`.

Coduri de ieșire: `0` dacă totul s-a încheiat cu succes sau a fost omis, `1` dacă rămâne un fișier
eșuat (listat în ieșirea de eroare), `2` dacă problema ține de configurare.
Un fișier eșuat nu este scris niciodată, chiar dacă scrierea însăși eșuează:
conținutul este scris alături, apoi redenumit. Este suficient să relansați comanda.

## Ce model să alegeți

Măsurat pe două documente reale, traduse în aceleași paisprezece limbi de
fiecare model. **Numărul reprezintă câte limbi, din paisprezece, au traducerea
scrisă fără nicio diferență față de sursă.**

| Model               | Cum poate fi accesat                 | Articol dens de monitorizare | Acest README    | Ce diferă și în câte limbi                                                                                             |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | cheie API Google                    | ✅ 14/14                | ⚠️ 13/14     | 1 limbă din 14: un cuvânt suplimentar scris cu caractere aldine (ja)                                                                                         |
| **GPT-5.6 Sol**      | abonament ChatGPT sau cheie OpenAI | ✅ 14/14                | ⚠️ 12/14     | 2 limbi din 14: câte un cuvânt mai puțin scris cu caractere aldine (ar, ja)                                                                                   |
| **GLM-5.2**          | cheie OpenRouter                    | ✅ 14/14                | ⚠️ 11/14     | 3 limbi din 14: câte un cuvânt mai puțin scris cu caractere aldine (hi, ja, ko)                                                                               |
| Claude Sonnet 5      | cheie API Anthropic                 | ⚠️ 11/14                | ⚠️ 12/14     | 3 limbi în articol: a apărut un bloc de cod (es, de, hi); 2 în acest README: un link fără marcajul său (sv), un cuvânt scris cu caractere aldine (zh) |
| Qwen 3.7 Flash       | cheie OpenRouter                    | ❌ 8/14                 | ⚠️ 10/14     | 1 limbă refuzată în articol, alte 5 diferă; în acest README, aproximativ patruzeci de cuvinte plasate în `code` (ar)                       |
| Grok 4.6             | abonament Grok                   | ❌ 8/14                 | neevaluat     | 5 limbi refuzate din 14, din cauza codurilor inline și URL-urilor nereturnate; neerlandeza diferă în întregime                                  |
| GPT-OSS 20B          | model local (Ollama)             | ❌ 7/14                 | nemăsurat din nou | 4 limbi refuzate din 14: modelul lăsa fragmente în franceză, iar mecanismul de protecție le-a oprit                                     |
| MiMo v2.5 (gratuit)  | OpenCode Zen, fără cont         | ❌ 11/14                | nemăsurat din nou | 1 limbă refuzată; o secțiune pierdută în poloneză                                                                                     |
| Mistral Large        | cheie API Mistral                   | ❌ 5/14                 | ❌ 1/14      | **dispare o secțiune întreagă**: 1 limbă în articol (hi), 3 în acest README (ar, hi, ko) — și 3 limbi refuzate în articol   |
| DeepSeek V4 Flash    | cheie OpenRouter                    | ❌ 3/14                 | nemăsurat din nou | 10 limbi refuzate din 14; 37 de minute per limbă                                                                                    |

|     | Ce înseamnă simbolul                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | toate cele paisprezece limbi sunt traduse și nimic nu diferă față de sursă                                                                                                                                       |
| ⚠️  | toate cele paisprezece limbi sunt traduse; diferențele țin de **marcaj** — un cuvânt scris cu caractere aldine, un `code`, un link care își pierde parantezele drepte. Nu lipsește niciun text, niciun URL, niciun bloc de cod și nicio secțiune |
| ❌  | cel puțin o limbă nu a putut fi tradusă — fișierul este refuzat, nu este scris — **sau** lipsește conținut dintr-un fișier scris                                                                      |

Concluziile principale:

- **O traducere refuzată nu este o traducere deteriorată.** Când lipsește un token
  la întoarcere, fișierul nu este scris, iar limba este considerată
  refuzată. Acest lucru se întâmplă cu Grok în articol: patru coduri inline și
  trei URL-uri sunt pierdute încă din primul segment, în cele cinci sisteme de scriere non-latine.
- **Această plasă de siguranță nu acoperă titlurile, tabelele, front matter-ul sau
  textul.** Un model care elimină o secțiune returnează un fișier pe care instrumentul îl scrie
  fără nicio obiecție — acesta este cazul Mistral. Aceste elemente nu pot fi
  înlocuite cu un token, iar mecanismele actuale de protecție nu le verifică;
  `scripts/compare_structure.py` detectează o secțiune pierdută, dar ulterior.
- **Grok nu are evaluare pentru acest README**: sesiunea sa CLI a expirat după douăsprezece
  limbi, dintre care unsprezece fără diferențe. O campanie întreruptă nu este evaluată.
- **Densitatea documentului contează mai mult decât limba.** Grok se descurcă în
  README-uri obișnuite și cedează într-un articol încărcat cu linkuri, inclusiv în
  neerlandeză.

Date și documente: coloana „Acest README” a fost măsurată la 9 septembrie 2026
pe o versiune fixată a acestui fișier (785 de linii, 285 de fragmente de cod inline, 89 de linii
de tabel), modificată ulterior. Coloana „Articol dens de monitorizare” provine din
campania din 4 și 5 septembrie pe un articol de 589 de linii, cu excepția rândului
Grok, măsurat din nou la 9 septembrie pe o altă ediție a aceluiași articol de monitorizare. Tabelele
complete, duratele și protocolul se află în
[Măsurători detaliate](#măsurători-detaliate).

## Toate opțiunile

| Opțiune                   | Descriere                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Un singur fișier Markdown de tradus (alternativă la `--source_dir`)                                             |
| `--source_dir`           | Directorul sursă care conține fișierele Markdown (implicit: `content/posts`)                                   |
| `--target_dir`           | Directorul de ieșire pentru fișierele traduse (implicit: `traductions_en`)                                    |
| `--source_lang`          | Limba sursă (implicit: `fr`)                                                                                  |
| `--target_lang`          | Limba țintă (implicit: `en`)                                                                                   |
| `--model`                | Modelul specific de utilizat                                                                                  |
| `--eco`                  | Utilizează modelele economice                                                                              |
| `--use_mistral`          | Utilizează API-ul Mistral AI                                                                                     |
| `--use_claude`           | Utilizează API-ul Claude                                                                                         |
| `--use_gemini`           | Utilizează API-ul Gemini                                                                                         |
| `--use_grok`             | Utilizează API-ul xAI (Grok) — necesită `XAI_API_KEY`                                                           |
| `--use_codex`            | Utilizează CLI-ul Codex din cota abonamentului ChatGPT                                                    |
| `--use_grok_cli`         | Utilizează CLI-ul Grok din cota abonamentului Grok                                                        |
| `--use_opencode`         | Utilizează OpenCode (open source) prin furnizorul configurat în OpenCode; necesită `--model provider/modèle` |
| `--use_openrouter`       | Utilizează OpenRouter — necesită `OPENROUTER_API_KEY` și `--model fournisseur/modèle`                          |
| `--force`                | Forțează retraducerea                                                                                       |
| `--keep_filename`        | Păstrează numele original al fișierului                                                                          |
| `--news`                 | Modul știri: protejează citatele în engleză, gestionează steagurile în funcție de limbă                                      |
| `--add_translation_note` | Adaugă o notă de traducere                                                                                |
| `--note_position`        | Poziția notei: `top`, `bottom` (implicit) sau `both`                                                     |
| `--note_format`          | Formatul notei: `legacy` (implicit, paragraf scris cu caractere aldine) sau `marker`                                            |
| `--include_model`        | Include numele modelului în fișierul de ieșire                                                            |
| `--reasoning_effort`     | Efortul de raționament GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

Cele opt flag-uri `--use_*` se exclud reciproc: combinarea a două dintre ele este
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

| Furnizor   | Calitate (implicit)                                      | Economic (`--eco`)      |
| ---------- | ----------------------------------------------------- | ------------------------- |
| OpenAI     | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude     | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral    | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini     | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex      | `gpt-5.6-sol` (și `terra` și `luna` prin `--model`) | `gpt-5.6-luna`            |
| Grok API   | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI   | `grok-4.6`                                            | `grok-4.5`                |
| OpenCode   | `--model provider/modèle` obligatoriu                 | la fel — `--eco` fără efect |
| OpenRouter | `--model fournisseur/modèle` obligatoriu              | la fel — `--eco` fără efect |
### Prin abonamentul ChatGPT: `--use_codex`

Controlează CLI-ul oficial Codex: traducerea este dedusă din cota
abonamentului ChatGPT, fără cheie API și fără facturare în funcție de utilizare.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Binarul este căutat în `CODEX_BIN`, apoi în `PATH`, apoi în pachetul
  `openai-codex-cli-bin`. `~/.codex/auth.json` nu este citit niciodată.
- `OPENAI_API_KEY` și `CODEX_API_KEY` sunt eliminate din mediul
  subprocesului: prezența unei chei nu determină niciodată trecerea la API.
- Fiecare segment costă cel puțin un „mesaj” din fereastra de 5 ore — două
  dacă validarea eșuează și segmentul este reîncercat. OpenAI anunță, cu titlu
  estimativ, 250-2 000 de mesaje/5 h pentru `gpt-5.6-luna` (`--eco`) și
  10-100 pentru `gpt-5.6-sol` cu un plan Plus.
- `--model gpt-5.6-terra` și `--model gpt-5.6-luna` trec, de asemenea, prin
  abonament. Un model la care contul nu are acces returnează un 400 „model is
  not supported when using Codex with a ChatGPT account”.
- Este mai lent decât un API, iar diferența crește odată cu documentul: pentru acest README,
  o mediană de 6 min 46 s per limbă cu `gpt-5.6-sol`, față de 36 s pentru
  `gemini-3.7-flash`.
- Este refuzat în CI (dacă `CI` sau `GITHUB_ACTIONS` este definită): abonamentul se autentifică
  printr-un fișier personal de sesiune, care nu are ce căuta pe un runner
  partajat.
- Variabile: `CODEX_BIN`, `CODEX_TIMEOUT` (secunde per segment, implicit 600).

### Prin abonamentul Grok: `--use_grok_cli`

Același principiu cu CLI-ul oficial Grok Build, prin abonamentul SuperGrok sau
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Izolare mai slabă decât la Codex.** Sandbox-ul OS al Grok nu se aplică
  pe multe sisteme Linux recente (AppArmor, socket-uri de runtime pentru
  containere), iar un profil care nu poate fi aplicat pornește în mod neizolat,
  fără avertisment. Prin urmare, scriptul nu solicită implicit niciun profil, anunță
  acest lucru și se bazează pe regulile `--deny` ale CLI-ului, inclusiv regula catch-all `*` — singurul
  strat care refuză să pornească în loc să elimine protecția fără
  avertisment. `GROK_TRANSLATE_SANDBOX=read-only` impune sandbox-ul OS, iar pornirea
  eșuează dacă sistemul nu îl poate asigura.
- Cota este săptămânală, partajată cu Chat, Imagine și Voice, și nicio
  comandă nu permite consultarea ei: un lot poate consuma din utilizarea conversațională
  fără niciun semnal.
- Variabile: `GROK_BIN`, `GROK_HOME` (directorul CLI-ului, implicit `~/.grok`),
  `GROK_TIMEOUT` (implicit 900), `GROK_TRANSLATE_SANDBOX`.

### Către furnizorul ales: `--use_opencode`

[OpenCode](https://opencode.ai) este un agent de cod open source (MIT) care
direcționează solicitările către furnizorii configurați în el: cheie API, abonament,
gateway OpenCode Zen (modele gratuite, fără cont) sau model local. Două
variante au fost măsurate aici de la un capăt la altul, Zen și Ollama.

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
ale cărui conversații pot fi folosite pentru antrenare, iar această alegere nu este făcută în
locul dumneavoastră.

Izolare la fiecare apel:

- o configurație inline, care are prioritate față de configurația dumneavoastră, definește un agent `aipmt`
  pentru care toate instrumentele sunt refuzate (`permission: { "*": "deny" }`), partajarea
  sesiunii este dezactivată, `--pure`, niciodată `--auto`;
- director de lucru temporar și gol, cu `OPENCODE_DISABLE_PROJECT_CONFIG` și
  `OPENCODE_DISABLE_CLAUDE_CODE` setate — fără ele, OpenCode injectează în
  prompt fișierul `AGENTS.md` din directorul curent și `~/.claude/CLAUDE.md`. Fișierul
  global `~/.config/opencode/AGENTS.md` rămâne injectat, deoarece OpenCode nu permite
  excluderea lui;
- contract de ieșire: cod de retur 0, niciun eveniment `error`, niciun apel
  de instrument, ultimul pas în `stop`, text nevid și agentul `aipmt`
  încărcat efectiv — un `--agent` necunoscut nu provoacă eșecul OpenCode, ci
  determină revenirea fără avertisment la agentul de codare;
- nu este transmisă nicio cheie `aipmt`, cu excepția `OPENCODE_API_KEY`, cheia
  OpenCode propriu-zisă. Furnizorii se configurează în OpenCode, nu în
  `.env` al `aipmt`.

De știut:

- Modelele gratuite Zen sunt schimbătoare, au limite nedocumentate, iar
  conversațiile lor pot fi folosite pentru antrenare: sunt potrivite pentru documentație
  publică, nu pentru conținut privat.
- Un model local trebuie să ofere cel puțin 16 k tokens de context, deoarece segmentele
  pot avea până la 16 000 de caractere. Ollama configurează adesea 4 096: folosiți
  un `Modelfile` cu `PARAMETER num_ctx 32768`.
- `--eco` nu are efect; `--reasoning_effort` este transmis neschimbat ca
  `--variant` al OpenCode.
- OpenCode înregistrează fiecare sesiune în `~/.local/share/opencode/`.
- Variabile: `OPENCODE_BIN` (în caz contrar, `PATH`, apoi `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (secunde per segment, implicit 600). `OPENCODE_CONFIG`
  este transmis neschimbat către OpenCode.

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

`reasoningEffort: "none"` dezactivează raționamentul pe care Ollama îl activează implicit pentru aceste
modele și pe care un Modelfile nu îl poate dezactiva. Măsurat pe o propoziție de
șase cuvinte: 919 tokens de raționament și 68 de secunde fără opțiune, 9 tokens cu aceasta.

### Către peste 400 de modele: `--use_openrouter`

OpenRouter este un router facturat în funcție de utilizare, pe baza unui credit unic, plasat în fața unor
modele găzduite de terți — inclusiv modelele chinezești deschise pe care niciun
alt provider nu le oferă aici.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` este obligatoriu. Un preflight, executat înainte de orice facturare, gestionează
două particularități ale rutării:

- **Același model este furnizat de zeci de gazde cu limite
  diferite** — pentru `z-ai/glm-5.3-flash`, 23 de gazde, dintre care una limitată la
  2 048 tokens de ieșire. Preflight-ul citește `/api/v1/models/{modèle}/endpoints`,
  exclude gazdele cu mai puțin de 8 000 de tokens de ieșire sau cu stare degradată și
  le fixează pe celelalte cu `allow_fallbacks: false`.
- **Raționamentul este facturat la tariful de ieșire** — 107 tokens față de 2 pentru
  un răspuns „OK” al `z-ai/glm-5.2`. Este dezactivat implicit; modelele
  care îl impun primesc cel mai scăzut nivel de efort pe care îl acceptă, deoarece valoarea implicită din
  catalog poate satura ieșirea înainte de sfârșitul traducerii.
  `--reasoning_effort` își păstrează prioritatea.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- Fereastra de context provine din catalog. Un model cu mai puțin de 16 400 tokens este
  refuzat înaintea oricărui apel: 8 400 pentru prompt și segment, minimum 8 000 pentru
  ieșire.
- Un slug absent din catalog, un catalog inaccesibil sau lipsa
  unei gazde care să respecte limita opresc comanda.
- `finish_reason=length` cu o ieșire goală reprezintă un buget consumat de
  raționament, nu o trunchiere: mesajul face distincția.
- `--eco` nu are efect.
- Variabile: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (implicit `https://openrouter.ai/api/v1`, `https://`
  obligatoriu), `OPENROUTER_TIMEOUT` (implicit 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (implicit 30).

### Notă de traducere

`--add_translation_note` adaugă o notă în `bottom` (implicit), `top` (după
front matter) sau `both` (`--note_position`), în formatul `legacy` (paragraf cu
caractere aldine, implicit) sau `marker` (`--note_format`). Formatul `marker` este o
definiție de referință Markdown invizibilă,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
urmată de un citat cu caractere aldine: lizibil pe GitHub și utilizabil în timpul build-ului de un
plugin remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Măsurători detaliate

Toate măsurătorile sunt traduceri executate efectiv cu `aipmt`, în
paisprezece limbi: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Scrise** numără fișierele pe care verificările le-au lăsat să treacă; **Fără
diferențe** le numără pe cele în care `scripts/compare_structure.py` nu detectează nimic — același număr de
secțiuni, subtitluri, linkuri, URL-uri distincte, blocuri de cod,
coduri inline, rânduri de tabel, blocuri de citat și cuvinte cu caractere aldine.

„Fără diferențe” înseamnă „nimic detectat”, nu „identic”: instrumentul de comparare
numără elementele fără a le citi conținutul. Nu semnalează nici eliminarea unui titlu de
nivel 4, nici înlocuirea textului unui cod inline, nici schimbarea
unui indicator și nu evaluează limba.

### Articol dens de monitorizare, modul `--news`

O ediție a [monitorizării IA de pe jls42.org](https://jls42.org/fr/news):
589 de rânduri, 140 de linkuri, 21 de secțiuni, 3 citate în engleză protejate. Campanie
din 4 și 5 septembrie 2026.

| Model                             | Acces              | Scrise  | Fără diferențe | Mediană/limbă |
| --------------------------------- | ------------------ | ------- | -------------- | ------------- |
| `gemini-3.7-flash`                | API Google         | 14/14   | ✅ **14/14**   | 1 min 18 s    |
| `gpt-5.6-sol` (`--use_codex`)     | abonament ChatGPT | 14/14   | ✅ **14/14**   | 11 min 28 s   |
| `z-ai/glm-5.2`                    | OpenRouter         | 14/14   | ✅ **14/14**   | 5 min 37 s    |
| `qwen/qwen3.8-flash`              | OpenRouter         | 14/14   | ✅ **14/14**   | 26 min 23 s   |
| `claude-sonnet-5`                 | API Anthropic      | 14/14   | ⚠️ 11/14       | 6 min 31 s    |
| `opencode/mimo-v2.5-free`         | OpenCode Zen       | 13/14   | ❌ 11/14       | 9 min 27 s    |
| `qwen/qwen3.7-flash`              | OpenRouter         | 13/14   | ❌ 8/14        | 10 min 09 s   |
| `ollama/gpt-oss-20b-32k`          | local              | 10/14   | ❌ 7/14        | 12 min 39 s   |
| `mistral-large-latest`            | API Mistral        | 11/14   | ❌ 5/14        | 5 min 32 s    |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter         | 4/14    | ❌ 3/14        | 37 min 27 s   |
| `grok-4.6` (`--use_grok_cli`)     | abonament Grok    | 1/14    | ❌ 1/14        | 23 min 11 s   |

Grok a fost măsurat din nou pe 9 septembrie, pe o altă ediție a aceleiași monitorizări
(356 de rânduri): 9 limbi scrise din 14, 8 fără diferențe. Aceasta este valoarea care
apare în tabelul de sinteză. Trei campanii întrerupte nu sunt
incluse: `qwen3.5-27b` (9 limbi) și `kimi-k2.6` (4) din lipsă de credit,
`z-ai/glm-5.3-flash`, ale cărui două eșecuri proveneau dintr-o setare de raționament
pe care providerul o corectează în prezent. Rândurile OpenRouter au fost măsurate cu
setările implicite ale routerului, înainte de `--use_openrouter`; `z-ai/glm-5.2`,
măsurat din nou cu providerul furnizat, oferă același rezultat de 14/14. Valorile au fost
recalculate pe 10 septembrie cu instrumentul de comparare actual: `qwen3.8-flash` și
`qwen3.7-flash` câștigă fiecare câte o limbă față de prima
publicare, iar celelalte rămân neschimbate.

### README-ul acestui proiect, Markdown standard

Revizie fixată la 9 septembrie 2026: 785 de rânduri, 285 de coduri inline, 40 de
delimitatoare de blocuri, 89 de rânduri de tabel. Patru traduceri în paralel.

| Model                         | Scrise  | Fără diferențe | Mediană/limbă | Ce diferă                                                                |
| ----------------------------- | ------- | -------------- | ------------- | ------------------------------------------------------------------------ |
| `gemini-3.7-flash`            | 14/14   | ⚠️ 13/14        | 36 s          | un cuvânt cu caractere aldine (ja)                                       |
| `claude-sonnet-5`             | 14/14   | ⚠️ 12/14        | 2 min 56 s    | un link (sv), un cuvânt cu caractere aldine (zh)                         |
| `gpt-5.6-sol` (`--use_codex`) | 14/14   | ⚠️ 12/14        | 6 min 46 s    | un cuvânt cu caractere aldine (ar, ja)                                   |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14   | ⚠️ 11/14        | 2 min 34 s    | un cuvânt cu caractere aldine (hi, ja, ko)                               |
| `qwen/qwen3.7-flash`          | 14/14   | ⚠️ 10/14        | 2 min 17 s    | 40 de coduri inline adăugate în arabă; caractere aldine (hi, ja, ko)     |
| `mistral-large-latest`        | 14/14   | ❌ 1/14         | 2 min 44 s    | o secțiune pierdută (ar, hi, ko); blocuri de cod adăugate (ja, ko, ro, zh) |

Două campanii întrerupte nu sunt incluse: Grok, a cărui sesiune CLI a expirat
după douăsprezece limbi (unsprezece fără diferențe), și `qwen3.8-flash`, care a primit HTTP 429 de la
gazda sa după două. `opencode/mimo-v2.5-free` și `ollama/gpt-oss-20b-32k`
nu au fost măsurate din nou pe această revizie; pe cea din 4 și 5 septembrie,
mai scurtă cu 277 de rânduri, fiecare scria 9 traduceri din 14, dintre care 7,
respectiv 1 fără diferențe.

### Patru README-uri ale unor proiecte cunoscute

FastAPI, Ollama, tldr-pages și Vue.js, preluate ca atare de pe GitHub — documente
mai ușoare decât cele două precedente. Campania a vizat modelele
cu dificultăți; Gemini servește drept punct de comparație.

| Model                     | Domeniu                    | Scrise  | Fără diferențe |
| ------------------------- | -------------------------- | ------- | -------------- |
| `gemini-3.7-flash`        | 4 proiecte × 14 limbi      | 56/56   | ✅ **55/56**   |
| `opencode/mimo-v2.5-free` | 4 proiecte × 14 limbi      | 55/56   | ❌ 47/56       |
| `grok-4.6` (abonament)   | 4 proiecte × ar, hi, ja, zh | 16/16   | ❌ 14/16       |
| `ollama/gpt-oss-20b-32k`  | 4 proiecte × ar, hi, ja, zh | 15/16   | ❌ 9/16        |

### Ce nu reprezintă aceste măsurători

- **Nu sunt un clasament exhaustiv**: numai OpenRouter oferă peste patru sute de
  modele, dintre care au fost măsurate aproximativ cincisprezece.
- **Duratele sunt orientative**: între trei și șase traduceri în paralel, în funcție de
  campanie, iar debitul unui furnizor variază pe parcursul zilei.
- **Sunt observații datate**: modelele se schimbă sub același nume, iar documentele
  dumneavoastră nu sunt ale noastre.

Pentru a repeta măsurătoarea pe documentele dumneavoastră, folosind o copie fixată a fișierului:

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

Instrumente pentru calitate, opționale, dar recomandate:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Cele 28 de traduceri din depozit (README și CHANGELOG, paisprezece limbi) sunt
regenerate cu `./regen_translations.sh --force` — Codex și `gpt-5.6-sol` prin
abonamentul ChatGPT în mod implicit, câte patru în paralel. `REGEN_PROVIDER` și
`REGEN_MODEL` schimbă calea; un API facturat (`openai`, `gemini`,
`grok`, `openrouter`) este refuzat fără `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` limitează fiecare job (600 s, 1 800 s pentru Codex). Detaliile
instrumentelor se află în `CLAUDE.md`.

## Proiecte care utilizează acest script

- **[jls42.org](https://jls42.org)** — blog personal publicat în 15 limbi. Serviciul său
  [zilnic de monitorizare IA](https://jls42.org/fr/news) este tradus în fiecare zi
  cu acest instrument și servește drept document de referință pentru măsurătorile de mai sus.

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licență

GNU GENERAL PUBLIC LICENSE Versiunea 3. Consultați [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Avertisment

Acest program este distribuit **fără nicio garanție**, în conformitate cu
secțiunile 15 și 16 din GPL v3: este furnizat „ca atare”, fără garanții privind calitatea
comercială sau adecvarea pentru un anumit scop, iar autorul său nu poate fi
considerat răspunzător pentru daune rezultate din utilizarea sa. Textul
licenței prevalează asupra acestui rezumat.

- **Recitiți înainte de publicare.** Protecțiile acoperă blocurile de cod,
  codul inline, URL-urile, ancorele și citatele din modul `--news` — nu
  titlurile, tabelele, front matter-ul sau sensul propozițiilor dumneavoastră.
- **Documentele dumneavoastră sunt trimise furnizorului ales**, în conformitate cu termenii săi
  de utilizare și politica sa privind datele. Unele modele gratuite pot
  reutiliza conversațiile dumneavoastră pentru antrenare; un model local este singura
  variantă prin care datele nu părăsesc sistemul dumneavoastră.
- **Apelurile API vă sunt facturate.** Acest program nu limitează
  cheltuielile: un document lung, reluarea după un eșec sau un model care raționează
  mult costă mai mult.
- **Măsurătorile publicate sunt observații datate**, nu garanții.

Numele produselor și companiilor menționate aparțin deținătorilor lor
respectivi. Acest proiect nu este afiliat cu niciunul dintre aceștia.

**Articol tradus din fr în ro cu gpt-5.6-sol.**

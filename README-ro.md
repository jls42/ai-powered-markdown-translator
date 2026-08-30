# Traducător de Markdown bazat pe AI

🌍 [Franceză](README.md) | [Engleză](README-en.md) | [Spaniolă](README-es.md) | [Chineză](README-zh.md) | [Germană](README-de.md) | [Japoneză](README-ja.md) | [Coreeană](README-ko.md) | [Arabă](README-ar.md) | [Hindi](README-hi.md) | [Italiană](README-it.md) | [Neerlandeză](README-nl.md) | [Poloneză](README-pl.md) | [Portugheză](README-pt.md) | [Română](README-ro.md) | [Suedeză](README-sv.md)

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

Traducător de fișiere Markdown care utilizează **OpenAI**, **Mistral AI**, **Claude (Anthropic)** și **Google Gemini**.

Acest script Python traduce fișiere Markdown dintr-o limbă sursă într-o limbă țintă, păstrând în același timp formatarea, blocurile de cod și metadatele front matter.

## Caracteristici principale

- **Multi-Provider**: Compatibilitate cu 4 API-uri (OpenAI, Mistral, Claude, Gemini) + CLI-ul Codex cu abonament ChatGPT
- **Modele 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Mod economic**: Opțiunea `--eco` pentru utilizarea unor modele mai rapide și mai puțin costisitoare
- **Fișier unic**: Opțiunea `--file` pentru traducerea unui singur fișier
- **Segmentare inteligentă**: Gestionarea textelor lungi cu limite de tokenuri pentru fiecare model
- **Păstrarea codului**: Blocurile de cod ȘI codul inline (`` `...` ``) sunt păstrate
- **Numele fișierului**: Opțiunea `--keep_filename` pentru păstrarea numelui original
- **Mod News**: Opțiunea `--news` pentru protejarea citatelor în engleză și gestionarea drapelelor în articolele de actualitate
- **Configurare .env**: Compatibilitate cu fișierul `.env` pentru cheile API
- **Notă de traducere**: Adăugarea opțională a unei note la sfârșitul documentului

## Instalare

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Instrumente pentru calitate (opționale, dar recomandate)

Proiectul utilizează [`pre-commit`](https://pre-commit.com) pentru a împiedica efectuarea de commituri cu cod formatat incorect, vulnerabil sau care conține un secret. Instalare:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hook-uri active: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexitate), detect-secrets (chei API), mypy (tipizare progresivă), Opengrep (SAST), pip-audit (CVE ale dependențelor), unittest. Consultați secțiunea _Quality / pre-commit_ din `CLAUDE.md` pentru detalii.

## Configurare

Creați un fișier `.env` în rădăcina proiectului sau definiți variabilele de mediu:

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

`GEMINI_API_KEY` este acceptată ca alternativă la `GOOGLE_API_KEY` (convenția AI
Studio). Variabile opționale: `XAI_BASE_URL` (endpoint xAI, implicit
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (secunde per apel Anthropic, implicit
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
și `GROK_TRANSLATE_SANDBOX` (consultați secțiunea Grok CLI).

## Utilizare

### Traducerea unui singur fișier

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Traducerea unui director

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
python translate.py --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
python translate.py --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
python translate.py --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'
```

### Traducerea folosind abonamentul ChatGPT (`--use_codex`)

Acest provider nu consumă nicio cheie API: controlează CLI-ul oficial Codex în mod
neinteractiv, astfel încât traducerea este dedusă din cota abonamentului
ChatGPT (Plus, Pro, Business…) deja plătit. Aceasta este singura metodă documentată de
OpenAI pentru această utilizare — tokenurile `~/.codex/auth.json` nu autentifică
apelurile către API Platform și, de altfel, nu sunt citite niciodată de acest script.

**Cerințe preliminare:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Executabilul este căutat în această ordine: variabila `CODEX_BIN`, `PATH`,
apoi pachetul Python `openai-codex-cli-bin`. Acesta din urmă nu este inclus în mod intenționat
în `requirements.txt`: ocupă aproximativ 250 Mo, ceea ce ar fi impus tuturor
utilizatorilor pentru un provider opțional.

**De știut:**

- **Nu este utilizată nicio cheie API.** `OPENAI_API_KEY` și `CODEX_API_KEY` sunt
  eliminate din mediul subprocesului, ceea ce garantează că o cheie
  prezentă în `.env` nu va comuta niciodată traducerea la facturarea în funcție de
  utilizare.
- **Un segment = un „mesaj local”** din fereastra de 5 ore a planului.
  Utilizați `--eco` (modelul `gpt-5.6-luna`, 250-2 000 de mesaje/5 h pe Plus)
  în locul modelului de calitate (`gpt-5.6-sol`, 10-100 de mesaje/5 h).
- **Mai lent** decât un apel API: aproximativ 45 s pentru un README complet, față de
  câteva secunde în mod direct.
- **Refuzat în CI** (dacă `CI` sau `GITHUB_ACTIONS` este definită): autentificarea prin
  abonament nu este concepută pentru un runner partajat, iar OpenAI descurajează acest
  workflow în depozitele publice. Utilizați o cheie API pentru această metodă.
- Variabile de mediu: `CODEX_BIN` (calea explicită către executabil) și
  `CODEX_TIMEOUT` (secunde per segment, implicit `600`).

### Traducerea folosind abonamentul Grok (`--use_grok_cli`)

Același principiu ca pentru `--use_codex`, cu CLI-ul oficial **Grok Build**:
traducerea este dedusă din abonamentul Grok (SuperGrok / X Premium+), în loc
să fie facturată per token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Izolare — de citit înainte de utilizare.** Acest provider este structural **mai
slab** decât `--use_codex`, iar acest lucru este asumat:

- Codex rulează în `--sandbox read-only`, o limită impusă de sistem.
- Sandbox-ul Grok **nu poate fi aplicat** pe multe sisteme Linux
  recente: AppArmor blochează user namespaces neprivilegiate începând cu Ubuntu
  24.04, iar deny-list-ul socketurilor runtime-ului de containere eșuează dacă
  `/run/podman` este în `0700`. Însă un profil **integrat** care nu poate fi
  aplicat pornește **neizolat, în tăcere**.
- Prin urmare, scriptul nu solicită implicit niciun profil și **nu revine niciodată
  în tăcere** la un mod alternativ: afișează un avertisment. Izolarea se bazează pe
  regulile `--deny` ale CLI-ului (inclusiv catch-all-ul `*`), singurul nivel măsurat
  _fail-closed_ — o regulă necunoscută determină refuzul pornirii, în loc să
  elimine protecția fără avertisment.
- Pentru a **impune** sandbox-ul sistemului de operare: `GROK_TRANSLATE_SANDBOX=read-only`.
  Pornirea va eșua dacă sistemul nu îl poate aplica, acesta fiind
  comportamentul dorit.

**Cotă**: pool-ul Grok este **săptămânal și partajat** cu Chat, Imagine și
Voice și nicio comandă nu permite consultarea lui. Prin urmare, o procesare în lot poate
reduce utilizarea conversațională fără nicio notificare — de aici
concurența limitată la 2 și avertismentul din `regen_translations.sh`.

Alte variabile: `GROK_BIN` (calea executabilului), `GROK_TIMEOUT` (implicit 900 s).

Pentru regenerarea celor 28 de traduceri:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### Mod economic

Utilizează modele mai rapide și mai puțin costisitoare (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opțiuni

| Opțiune                   | Descriere                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Un singur fișier Markdown de tradus                                       |
| `--source_dir`           | Directorul sursă care conține fișierele Markdown                        |
| `--target_dir`           | Directorul de ieșire pentru fișierele traduse                          |
| `--source_lang`          | Limba sursă (implicit: `fr`)                                             |
| `--target_lang`          | Limba țintă (implicit: `en`)                                              |
| `--model`                | Modelul specific care trebuie utilizat                                             |
| `--eco`                  | Utilizarea modelelor economice                                         |
| `--use_mistral`          | Utilizarea API-ului Mistral AI                                                |
| `--use_claude`           | Utilizarea API-ului Claude                                                    |
| `--use_gemini`           | Utilizarea API-ului Gemini                                                    |
| `--use_codex`            | Utilizarea CLI-ului Codex din cota abonamentului ChatGPT               |
| `--use_grok`             | Utilizarea API-ului xAI (Grok) — necesită `XAI_API_KEY`                      |
| `--use_grok_cli`         | Utilizarea CLI-ului Grok din cota abonamentului Grok                   |
| `--force`                | Forțarea retraducerii                                                  |
| `--keep_filename`        | Păstrarea numelui original al fișierului                                     |
| `--news`                 | Mod actualități: protejează citatele EN, gestionează drapelele în funcție de limbă |
| `--add_translation_note` | Adăugarea unei note de traducere                                           |
| `--note_position`        | Poziția notei: `top`, `bottom` (implicit) sau `both`                |
| `--note_format`          | Formatul notei: `legacy` (implicit, paragraf aldin) sau `marker`       |
| `--include_model`        | Includerea numelui modelului în fișierul de ieșire                       |
| `--reasoning_effort`     | Efortul de raționament GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`     |

### Nota de traducere: poziții și formate

Cu `--add_translation_note`, translator-ul poate plasa nota în partea de sus, în partea de jos sau în ambele locuri și o poate reda fie în format text simplu (compatibil cu versiunile anterioare), fie în format `marker`, utilizabil de un plugin Markdown.

**Poziție** (`--note_position`):

- `bottom` (implicit): nota la sfârșitul fișierului, ca până acum.
- `top`: nota inserată **după frontmatter-ul YAML** (siguranță pentru Astro Content Collections, gray-matter etc.).
- `both`: nota inserată sus ȘI jos (un singur apel LLM, conținut reutilizat pentru ambele amplasări).

**Format** (`--note_format`):

- `legacy` (implicit): paragraf aldin `**...**` — comportament strict identic cu v1.8, byte-for-byte. Compatibil cu Hugo, GitHub, GitLab și orice renderer Markdown.
- `marker`: definiție Markdown invizibilă a unei referințe de link (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), urmată de un blockquote aldin. Poate fi citită nativ pe GitHub/GitLab și utilizată la build de un plugin remark în Astro pentru a genera un banner stilizat (cf. blogul jls42.org).

```bash
# Compatibilité legacy (rien ne change vs v1.8)
python translate.py --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### Modele implicite (2026)

| Provider | Calitate (implicit)       | Economic (`--eco`)    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **Recomandare pentru traduceri long-form**: `--use_gemini` (implicit = `gemini-3.7-flash`) păstrează cu fidelitate structura Markdown pentru scrierile non-latine (PL, JA, ZH, AR, HI), inclusiv în modul `--news`, unde fidelitatea placeholderelor este importantă. Măsurat pe acest README tradus în japoneză: structură identică cu `gemini-3.1-pro-preview` (21 de liste, 18 blocuri de cod, 13 linkuri HTML, 13 imagini, toate URL-urile păstrate), cu o latență de aproximativ 6 ori mai mică. OpenAI rămâne opțiunea implicită pentru compatibilitatea cu versiunile anterioare.

## Proiecte care utilizează acest script

- **[jls42.org](https://jls42.org)** - Blog personal multilingv (15 limbi)

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licență

GNU GENERAL PUBLIC LICENSE Versiunea 3. Consultați [LICENSE](LICENSE).

**Articol tradus din fr în ro cu gpt-5.6-sol.**

# Traducător de Markdown bazat pe AI

🌍 [Franceză](README.md) | [Engleză](README-en.md) | [Spaniolă](README-es.md) | [Chineză](README-zh.md) | [Germană](README-de.md) | [Japoneză](README-ja.md) | [Coreeană](README-ko.md) | [Arabă](README-ar.md) | [Hindi](README-hi.md) | [Italiană](README-it.md) | [Neerlandeză](README-nl.md) | [Poloneză](README-pl.md) | [Portugheză](README-pt.md) | [Română](README-ro.md) | [Suedeză](README-sv.md)

<h4 align="center">📊 Calitatea codului</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Starea Quality Gate"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Evaluarea securității"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Evaluarea fiabilității"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Evaluarea mentenanței"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Acoperire"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilități"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Erori"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Mirosuri de cod"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Linii duplicate (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Datorie tehnică"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Linii de cod"></a>
</p>

Traducător de fișiere Markdown folosind **OpenAI**, **Mistral AI**, **Claude (Anthropic)** și **Google Gemini**.

Acest script Python traduce fișiere Markdown dintr-o limbă sursă într-o limbă țintă, păstrând în același timp formatarea, blocurile de cod și metadatele front matter.

## Caracteristici principale

- **Multi-Provider**: Suport pentru 4 API-uri (OpenAI, Mistral, Claude, Gemini)
- **Modele 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Mod economic**: Opțiune `--eco` pentru a utiliza modele mai rapide și mai puțin costisitoare
- **Fișier unic**: Opțiune `--file` pentru a traduce un singur fișier
- **Segmentare inteligentă**: Gestionarea textelor lungi cu limite de tokeni per model
- **Păstrarea codului**: Blocurile de cod ȘI codul inline (`` `...` ``) sunt păstrate
- **Nume de fișier**: Opțiune `--keep_filename` pentru a păstra numele original
- **Mod știri**: Opțiune `--news` pentru a proteja citatele în engleză și a gestiona steagurile în articolele de știri
- **Configurare .env**: Suport pentru fișierul `.env` pentru cheile API
- **Notă de traducere**: Adăugarea opțională a unei note la sfârșitul documentului

## Instalare

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Instrumente de calitate (opțional, dar recomandat)

Proiectul folosește [`pre-commit`](https://pre-commit.com) pentru a împiedica commit-area codului formatat incorect, vulnerabil sau care conține un secret. Instalare:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hook-uri active: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexitate), detect-secrets (chei API), mypy (tipare progresivă), Opengrep (SAST), pip-audit (dependințe CVE), unittest. Vezi secțiunea `CLAUDE.md` _Quality / pre-commit_ pentru detalii.

## Configurare

Creați un fișier `.env` la rădăcina proiectului sau definiți variabilele de mediu:

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

## Utilizare

### Traducerea unui singur fișier

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Traducerea unui director

```bash
# Avec OpenAI (défaut: gpt-5.5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### Mod economic

Folosește modele mai rapide și mai puțin costisitoare (gpt-5.4-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opțiuni

| Opțiune                   | Descriere                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Un singur fișier Markdown de tradus                                       |
| `--source_dir`           | Director sursă care conține fișierele Markdown                        |
| `--target_dir`           | Director de ieșire pentru fișierele traduse                          |
| `--source_lang`          | Limbă sursă (implicit: `fr`)                                             |
| `--target_lang`          | Limbă țintă (implicit: `en`)                                              |
| `--model`                | Model specific de utilizat                                             |
| `--eco`                  | Folosește modelele economice                                         |
| `--use_mistral`          | Folosește API-ul Mistral AI                                                |
| `--use_claude`           | Folosește API-ul Claude                                                    |
| `--use_gemini`           | Folosește API-ul Gemini                                                   |
| `--force`                | Forțează retraducerea                                                  |
| `--keep_filename`        | Păstrează numele original al fișierului                                     |
| `--news`                 | Mod știri: protejează citatele EN, gestionează steagurile pe limbă |
| `--add_translation_note` | Adaugă o notă de traducere                                           |
| `--note_position`        | Poziția notei: `top`, `bottom` (implicit), sau `both`                |
| `--note_format`          | Formatul notei: `legacy` (implicit, paragraf îngroșat) sau `marker`       |
| `--include_model`        | Include numele modelului în fișierul de ieșire                       |

### Notă de traducere: poziții și formate

Cu `--add_translation_note`, translatorul poate plasa nota sus, jos sau în ambele locuri și o poate reda fie în format text simplu (compatibil cu versiunile anterioare), fie în format `marker` consumabil de un plugin Markdown.

**Poziție** (`--note_position`) :

- `bottom` (implicit) : notă la sfârșitul fișierului, ca în mod tradițional.
- `top` : notă inserată **după frontmatter-ul YAML** (siguranță pentru Astro Content Collections, gray-matter, etc.).
- `both` : notă inserată sus ȘI jos (o singură apelare LLM, conținut reutilizat pentru ambele plasări).

**Format** (`--note_format`) :

- `legacy` (implicit) : paragraf îngroșat `**...**` — comportament strict identic cu v1.8, byte-for-byte. Compatibil cu Hugo, GitHub, GitLab și orice renderer Markdown.
- `marker` : definiție de referință Markdown invizibilă pentru linkuri `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"` urmată de un blockquote îngroșat. Citibil nativ pe GitHub/GitLab și utilizabil la build de un plugin remark în Astro pentru a produce un banner stilizat (cf. blog jls42.org).

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

| Furnizor | Calitate (implicit)         | Economic (`--eco`)            |
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **Recomandare pentru traduceri long-form** : `--use_gemini` (implicit = `gemini-3.1-pro-preview` calitate, `--eco` = `gemini-3.1-flash-lite-preview`) tinde să păstreze mai bine structura markdown pe scripturi non-latine (PL, JA, ZH, AR, HI), în special în modul `--news` unde fidelitatea placeholder-elor contează. OpenAI rămâne implicitul pentru retrocompatibilitate.

## Proiecte care folosesc acest script

- **[jls42.org](https://jls42.org)** - Blog personal multilingv (15 limbi)

## Autor

Julien LE SAUX
Email : contact@jls42.org

## Licență

GNU GENERAL PUBLIC LICENSE Version 3. Vezi [LICENSE](LICENSE).

**Articol tradus din fr în ro cu gpt-5.4-mini.**

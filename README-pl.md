# Tłumacz Markdown zasilany przez AI

🌍 [Francuski](README.md) | [Angielski](README-en.md) | [Hiszpański](README-es.md) | [中文](README-zh.md) | [Niemiecki](README-de.md) | [Japoński](README-ja.md) | [Koreański](README-ko.md) | [Arabski](README-ar.md) | [Hindi](README-hi.md) | [Włoski](README-it.md) | [Niderlandzki](README-nl.md) | [Polski](README-pl.md) | [Portugalski](README-pt.md) | [Rumuński](README-ro.md) | [Szwedzki](README-sv.md)

<h4 align="center">📊 Jakość kodu</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Stan Quality Gate"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Ocena bezpieczeństwa"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Ocena niezawodności"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Ocena utrzymywalności"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Pokrycie"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Podatności"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Błędy"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Zapachy kodu"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Zduplikowane linie (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Dług techniczny"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Linie kodu"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Odznaka Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Tłumacz plików Markdown używający **OpenAI**, **Mistral AI**, **Claude (Anthropic)** i **Google Gemini**.

Ten skrypt Python tłumaczy pliki Markdown z języka źródłowego na język docelowy, zachowując formatowanie, bloki kodu i metadane front matter.

## Główne funkcje

- **Multi-Provider**: Obsługa 4 API (OpenAI, Mistral, Claude, Gemini)
- **Modele 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Tryb ekonomiczny**: Opcja `--eco` pozwalająca używać szybszych i tańszych modeli
- **Pojedynczy plik**: Opcja `--file` do tłumaczenia jednego pliku
- **Inteligentna segmentacja**: Obsługa długich tekstów z limitami tokenów dla modeli
- **Zachowanie kodu**: Zachowywane są bloki kodu ORAZ kod inline (`` `...` ``)
- **Nazwa pliku**: Opcja `--keep_filename` do zachowania oryginalnej nazwy
- **Tryb News**: Opcja `--news` chroniąca angielskie cytaty i obsługująca flagi w artykułach newsowych
- **Konfiguracja .env**: Obsługa pliku `.env` dla kluczy API
- **Uwaga o tłumaczeniu**: Opcjonalne dodanie noty na końcu dokumentu

## Instalacja

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Narzędzia jakościowe (opcjonalne, ale zalecane)

Projekt używa [`pre-commit`](https://pre-commit.com), aby zapobiegać commitowaniu źle sformatowanego, podatnego na ataki lub zawierającego sekret kodu. Instalacja:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktywne hooki: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (złożoność), detect-secrets (klucze API), mypy (stopniowe typowanie), Opengrep (SAST), pip-audit (zależności CVE), unittest. Zobacz sekcję _Jakość / pre-commit_ `CLAUDE.md` po szczegóły.

## Konfiguracja

Utwórz plik `.env` w katalogu głównym projektu albo zdefiniuj zmienne środowiskowe:

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

## Użycie

### Tłumaczenie pojedynczego pliku

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Tłumaczenie katalogu

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

### Tryb ekonomiczny

Używa szybszych i tańszych modeli (gpt-5.4-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opcje

| Opcja                   | Opis                                                                 |
| ------------------------ | -------------------------------------------------------------------- |
| `--file`                 | Pojedynczy plik Markdown do przetłumaczenia                           |
| `--source_dir`           | Katalog źródłowy zawierający pliki Markdown                          |
| `--target_dir`           | Katalog wyjściowy dla przetłumaczonych plików                        |
| `--source_lang`          | Język źródłowy (domyślnie: `fr`)                            |
| `--target_lang`          | Język docelowy (domyślnie: `en`)                            |
| `--model`                | Konkretne użycie modelu                                              |
| `--eco`                  | Używaj modeli ekonomicznych                                         |
| `--use_mistral`          | Użyj API Mistral AI                                                    |
| `--use_claude`           | Użyj API Claude                                                        |
| `--use_gemini`           | Użyj API Gemini                                                        |
| `--force`                | Wymuś ponowne tłumaczenie                                            |
| `--keep_filename`        | Zachowaj oryginalną nazwę pliku                                       |
| `--news`                 | Tryb newsów: chroni cytaty EN, obsługuje flagi według języka          |
| `--add_translation_note` | Dodaj notę tłumaczeniową                                             |
| `--note_position`        | Pozycja noty: `top`, `bottom` (domyślnie) lub `both` |
| `--note_format`          | Format noty: `legacy` (domyślnie, pogrubiony akapit) lub `marker` |
| `--include_model`        | Dołącz nazwę modelu do pliku wyjściowego                             |

### Uwaga o tłumaczeniu: pozycje i formaty

Dzięki `--add_translation_note` tłumacz może umieścić notę na górze, na dole albo w obu miejscach, a także wygenerować ją w formacie zwykłego tekstu (zgodnym wstecznie) albo w formacie `marker` możliwym do użycia przez wtyczkę Markdown.

**Pozycja** (`--note_position`) :

- `bottom` (domyślnie) : nota na końcu pliku, jak dotychczas.
- `top` : nota wstawiana **po frontmatterze YAML** (bezpieczeństwo Astro Content Collections, gray-matter itp.).
- `both` : nota wstawiana na górze I na dole (jedno wywołanie LLM, treść ponownie użyta dla obu miejsc).

**Format** (`--note_format`) :

- `legacy` (domyślnie) : pogrubiony akapit `**...**` — zachowanie identyczne jak w v1.8, bajt w bajt. Zgodne z Hugo, GitHubem, GitLabem i każdym rendererem Markdown.
- `marker` : niewidoczna definicja link reference Markdown (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) poprzedzająca pogrubiony blockquote. Natywnie czytelna na GitHub/GitLabie i możliwa do wykorzystania podczas budowania przez wtyczkę remark po stronie Astro, aby wygenerować stylizowany baner (por. blog jls42.org).

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

### Domyślne modele (2026)

| Dostawca | Jakość (domyślnie)         | Ekonomiczny (`--eco`)            |
| -------- | -------------------------- | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **Rekomendacja dla tłumaczeń long-form** : `--use_gemini` (domyślnie = `gemini-3.1-pro-preview` jakość, `--eco` = `gemini-3.1-flash-lite-preview`) zwykle lepiej zachowuje strukturę markdown w skryptach niełacińskich (PL, JA, ZH, AR, HI), zwłaszcza w trybie `--news`, gdzie liczy się wierność placeholderów. OpenAI pozostaje domyślne ze względu na zgodność wsteczną.

## Projekty korzystające z tego skryptu

- **[jls42.org](https://jls42.org)** - Wielojęzyczny blog osobisty (15 języków)

## Autor

Julien LE SAUX
Email : contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE Version 3. Zobacz [LICENSE](LICENSE).

**Artykuł przetłumaczony z fr na pl za pomocą gpt-5.4-mini.**

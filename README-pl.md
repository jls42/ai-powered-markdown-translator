# Tłumacz Markdown oparty na AI

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

<h4 align="center">📊 Jakość kodu</h4>

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

Tłumacz plików Markdown wykorzystujący **OpenAI**, **Mistral AI**, **Claude (Anthropic)** i **Google Gemini**.

Ten skrypt Pythona tłumaczy pliki Markdown z języka źródłowego na język docelowy, zachowując formatowanie, bloki kodu oraz metadane front matter.

## Główne cechy

- **Wielu dostawców**: Obsługa 4 API (OpenAI, Mistral, Claude, Gemini)
- **Modele 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Tryb ekonomiczny**: Opcja `--eco` do używania szybszych i tańszych modeli
- **Pojedynczy plik**: Opcja `--file` do tłumaczenia jednego pliku
- **Inteligentna segmentacja**: Obsługa długich tekstów z limitami tokenów dla modeli
- **Zachowanie kodu**: Bloki kodu ORAZ kod inline (`` `...` ``) są zachowywane
- **Nazwa pliku**: Opcja `--keep_filename` do zachowania oryginalnej nazwy
- **Tryb wiadomości**: Opcja `--news` do ochrony angielskich cytatów i obsługi flag w artykułach informacyjnych
- **Konfiguracja .env**: Obsługa pliku `.env` dla kluczy API
- **Uwaga o tłumaczeniu**: Opcjonalne dodanie notatki na końcu dokumentu

## Instalacja

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Narzędzia jakości (opcjonalne, ale zalecane)

Projekt używa [`pre-commit`](https://pre-commit.com), aby zapobiegać commitowaniu źle sformatowanego kodu, podatnego na ataki lub zawierającego sekret. Instalacja:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktywne hooki: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (złożoność), detect-secrets (klucze API), mypy (stopniowe typowanie), Opengrep (SAST), pip-audit (zależności CVE), unittest. Zobacz sekcję `CLAUDE.md` _Quality / pre-commit_ po szczegóły.

## Konfiguracja

Utwórz plik `.env` w katalogu głównym projektu lub zdefiniuj zmienne środowiskowe:

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
| `--file`                 | Pojedynczy plik Markdown do przetłumaczenia                          |
| `--source_dir`           | Katalog źródłowy zawierający pliki Markdown                          |
| `--target_dir`           | Katalog wyjściowy dla przetłumaczonych plików                        |
| `--source_lang`          | Język źródłowy (domyślnie: `fr`)                           |
| `--target_lang`          | Język docelowy (domyślnie: `en`)                           |
| `--model`                | Konkretne używane modelu                                             |
| `--eco`                  | Używaj modeli ekonomicznych                                         |
| `--use_mistral`          | Użyj API Mistral AI                                                 |
| `--use_claude`           | Użyj API Claude                                                    |
| `--use_gemini`           | Użyj API Gemini                                                   |
| `--force`                | Wymuś ponowne tłumaczenie                                           |
| `--keep_filename`        | Zachowaj oryginalną nazwę pliku                                    |
| `--news`                 | Tryb wiadomości: chroni cytaty EN, obsługuje flagi według języka |
| `--add_translation_note` | Dodaj notatkę o tłumaczeniu                                      |
| `--note_position`        | Pozycja notatki: `top`, `bottom` (domyślnie) lub `both` |
| `--note_format`          | Format notatki: `legacy` (domyślnie, pogrubiony akapit) lub `marker` |
| `--include_model`        | Dołącz nazwę modelu do pliku wyjściowego                           |

### Notatka o tłumaczeniu: pozycje i formaty

Dzięki `--add_translation_note` translator może umieścić notatkę u góry, u dołu lub w obu miejscach, i sformatować ją jako zwykły tekst (wstecznie zgodny) albo jako format `marker` obsługiwany przez wtyczkę Markdown.

**Pozycja** (`--note_position`):

- `bottom` (domyślnie): notatka na końcu pliku, jak historycznie.
- `top`: notatka wstawiona **po YAML frontmatter** (bezpieczeństwo Astro Content Collections, gray-matter itp.).
- `both`: notatka wstawiona na górze I na dole (jedno wywołanie LLM, treść ponownie użyta dla obu miejsc).

**Format** (`--note_format`):

- `legacy` (domyślnie): pogrubiony akapit `**...**` — zachowanie ściśle identyczne z v1.8, bajt w bajt. Zgodne z Hugo, GitHub, GitLab i każdym rendererem Markdown.
- `marker`: niewidoczna definicja odwołania do linku Markdown `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"` po której następuje pogrubiony blockquote. Czytelne natywnie na GitHub/GitLab oraz możliwe do wykorzystania podczas budowania przez wtyczkę remark po stronie Astro w celu wygenerowania stylizowanego banera (por. blog jls42.org).

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
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **Rekomendacja dla długich tłumaczeń**: `--use_gemini` (domyślnie = `gemini-3.1-pro-preview` jakość, `--eco` = `gemini-3.1-flash-lite-preview`) zwykle lepiej zachowuje strukturę markdown w skryptach nielacińskich (PL, JA, ZH, AR, HI), szczególnie w trybie `--news`, gdzie liczy się wierność placeholderów. OpenAI pozostaje domyślne dla wstecznej zgodności.

## Projekty używające tego skryptu

- **[jls42.org](https://jls42.org)** - Wielojęzyczny blog osobisty (15 języków)

## Autor

Julien LE SAUX
Email : contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE Version 3. Zobacz [LICENSE](LICENSE).

**Artykuł przetłumaczony z fr na pl za pomocą gpt-5.4-mini.**

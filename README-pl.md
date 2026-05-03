# Tłumacz Markdown wspierany przez AI

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

<h4 align="center">📊 Jakość kodu</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Stan Quality Gate"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Ocena bezpieczeństwa"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Ocena niezawodności"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Ocena utrzymywalności"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Pokrycie"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Luki w zabezpieczeniach"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Błędy"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Zapachy kodu"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Zduplikowane linie (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Dług techniczny"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Liczba linii kodu"></a>
</p>

Tłumacz plików Markdown wykorzystujący **OpenAI**, **Mistral AI**, **Claude (Anthropic)** i **Google Gemini**.

Ten skrypt Pythona tłumaczy pliki Markdown z języka źródłowego na język docelowy, zachowując formatowanie, bloki kodu i metadane front matter.

## Główne funkcje

- **Wielu dostawców**: obsługa 4 API (OpenAI, Mistral, Claude, Gemini)
- **Modele 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Tryb ekonomiczny**: opcja `--eco` do używania szybszych i tańszych modeli
- **Pojedynczy plik**: opcja `--file` do tłumaczenia jednego pliku
- **Inteligentna segmentacja**: obsługa długich tekstów z limitami tokenów zależnymi od modelu
- **Zachowanie kodu**: bloki kodu ORAZ kod inline (`` `...` ``) są zachowywane
- **Nazwa pliku**: opcja `--keep_filename` do zachowania oryginalnej nazwy
- **Tryb news**: opcja `--news` do ochrony angielskich cytatów i obsługi flag w artykułach newsowych
- **Konfiguracja .env**: obsługa pliku `.env` dla kluczy API
- **Notatka tłumaczenia**: opcjonalne dodanie notatki na końcu dokumentu

## Instalacja

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Narzędzia jakościowe (opcjonalne, ale zalecane)

Projekt używa [`pre-commit`](https://pre-commit.com), aby zapobiegać commitowaniu źle sformatowanego kodu, podatnego na ataki lub zawierającego sekret. Instalacja:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktywne hooki: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (złożoność), detect-secrets (klucze API), mypy (stopniowe typowanie), Opengrep (SAST), pip-audit (zależności CVE), unittest. Zobacz sekcję `CLAUDE.md` _Quality / pre-commit_, aby poznać szczegóły.

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

### Tłumaczenie jednego pliku

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

Używa szybszych i tańszych modeli (gpt-5.4-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opcje

| Opcja                   | Opis                                                                 |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Pojedynczy plik Markdown do przetłumaczenia                                       |
| `--source_dir`           | Katalog źródłowy zawierający pliki Markdown                        |
| `--target_dir`           | Katalog wyjściowy dla przetłumaczonych plików                          |
| `--source_lang`          | Język źródłowy (domyślnie: `fr`)                                             |
| `--target_lang`          | Język docelowy (domyślnie: `en`)                                              |
| `--model`                | Konkretna używana baza modelu                                             |
| `--eco`                  | Użyj modeli ekonomicznych                                         |
| `--use_mistral`          | Użyj API Mistral AI                                                |
| `--use_claude`           | Użyj API Claude                                                    |
| `--use_gemini`           | Użyj API Gemini                                                   |
| `--force`                | Wymuś ponowne tłumaczenie                                                  |
| `--keep_filename`        | Zachowaj oryginalną nazwę pliku                                     |
| `--news`                 | Tryb news: chroni cytaty EN, obsługuje flagi według języka |
| `--add_translation_note` | Dodaj notatkę tłumaczenia                                           |
| `--include_model`        | Uwzględnij nazwę modelu w pliku wyjściowym                       |

### Domyślne modele (2026)

| Dostawca | Jakość (domyślnie)         | Ekonomiczny (`--eco`)            |
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **Rekomendacja dla tłumaczeń długich form**: `--use_gemini` (domyślnie = `gemini-3.1-pro-preview` jakość, `--eco` = `gemini-3.1-flash-lite-preview`) zwykle lepiej zachowuje strukturę markdown w skryptach nielatynskich (PL, JA, ZH, AR, HI), zwłaszcza w trybie `--news`, gdzie liczy się wierność placeholderów. OpenAI pozostaje domyślnym wyborem ze względu na zgodność wsteczną.

## Projekty korzystające z tego skryptu

- **[jls42.org](https://jls42.org)** - Wielojęzyczny osobisty blog (15 języków)

## Autor

Julien LE SAUX
Email : contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE Version 3. Zobacz [LICENSE](LICENSE).

**Ten dokument został przetłumaczony z wersji fr na język pl przy użyciu modelu gpt-5.4-mini. Aby uzyskać więcej informacji o procesie tłumaczenia, odwiedź https://github.com/jls42/ai-powered-markdown-translator**

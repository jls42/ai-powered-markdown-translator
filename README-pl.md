# Tłumacz Markdown oparty na AI

🌍 [Francuski](README.md) | [Angielski](README-en.md) | [Hiszpański](README-es.md) | [Chiński](README-zh.md) | [Niemiecki](README-de.md) | [Japoński](README-ja.md) | [Koreański](README-ko.md) | [Arabski](README-ar.md) | [Hindi](README-hi.md) | [Włoski](README-it.md) | [Niderlandzki](README-nl.md) | [Polski](README-pl.md) | [Portugalski](README-pt.md) | [Rumuński](README-ro.md) | [Szwedzki](README-sv.md)

Tłumacz plików Markdown wykorzystujący **OpenAI**, **Mistral AI**, **Claude (Anthropic)** i **Google Gemini**.

Ten skrypt Pythona tłumaczy pliki Markdown z języka źródłowego na język docelowy, zachowując formatowanie, bloki kodu i metadane front matter.

## Główne funkcje

- **Wielu dostawców**: Obsługa 4 API (OpenAI, Mistral, Claude, Gemini)
- **Modele 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Tryb ekonomiczny**: Opcja `--eco` do korzystania z szybszych i tańszych modeli
- **Jeden plik**: Opcja `--file` do tłumaczenia pojedynczego pliku
- **Inteligentna segmentacja**: Obsługa długich tekstów z limitami tokenów zależnymi od modelu
- **Zachowanie kodu**: Bloki kodu ORAZ kod inline (`` `...` ``) są zachowywane
- **Nazwa pliku**: Opcja `--keep_filename` do zachowania oryginalnej nazwy
- **Tryb news**: Opcja `--news` do ochrony angielskich cytatów i obsługi flag w artykułach informacyjnych
- **Konfiguracja .env**: Obsługa pliku `.env` dla kluczy API
- **Notatka tłumaczeniowa**: Opcjonalne dodanie notatki na końcu dokumentu

## Instalacja

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Narzędzia jakości (opcjonalne, ale zalecane)

Projekt używa [`pre-commit`](https://pre-commit.com), aby zapobiegać commitowaniu kodu źle sformatowanego, podatnego na ataki lub zawierającego sekret. Instalacja:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Aktywne hooki: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (złożoność), detect-secrets (klucze API), mypy (stopniowe typowanie), Opengrep (SAST), pip-audit (CVE deps), unittest. Zobacz sekcję `CLAUDE.md` _Quality / pre-commit_ po szczegóły.

## Konfiguracja

Utwórz plik `.env` w katalogu głównym projektu lub ustaw zmienne środowiskowe:

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

Używa szybszych i tańszych modeli (gpt-5.4-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opcje

| Opcja                   | Opis                                                                    |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Pojedynczy plik Markdown do przetłumaczenia                              |
| `--source_dir`           | Katalog źródłowy zawierający pliki Markdown                              |
| `--target_dir`           | Katalog wyjściowy dla przetłumaczonych plików                            |
| `--source_lang`          | Język źródłowy (domyślnie: `fr`)                                             |
| `--target_lang`          | Język docelowy (domyślnie: `en`)                                              |
| `--model`                | Konkretny model do użycia                                                |
| `--eco`                  | Użyj modeli ekonomicznych                                                |
| `--use_mistral`          | Użyj API Mistral AI                                                      |
| `--use_claude`           | Użyj API Claude                                                          |
| `--use_gemini`           | Użyj API Gemini                                                          |
| `--force`                | Wymuś ponowne tłumaczenie                                                |
| `--keep_filename`        | Zachowaj oryginalną nazwę pliku                                          |
| `--news`                 | Tryb news: chroni cytaty EN, obsługuje flagi według języka               |
| `--add_translation_note` | Dodaj notatkę tłumaczeniową                                               |
| `--include_model`        | Uwzględnij nazwę modelu w pliku wyjściowym                                |

### Domyślne modele (2026)

| Dostawca | Jakość (domyślnie)       | Ekonomiczny (`--eco`)   |
| -------- | ------------------------ | ------------------------ |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`           |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5`       |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`   |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3-flash-preview` |

> **Rekomendacja dla tłumaczeń long-form**: `--use_gemini` (domyślnie = `gemini-3.1-pro-preview` jakości, `--eco` = `gemini-3-flash-preview`) ma tendencję do lepszego zachowania struktury markdown w skryptach niełacińskich (PL, JA, ZH, AR, HI), zwłaszcza w trybie `--news`, gdzie liczy się wierność placeholderów. OpenAI pozostaje domyślnym wyborem dla zachowania zgodności wstecznej.

## Projekty korzystające z tego skryptu

- **[jls42.org](https://jls42.org)** - Wielojęzyczny blog osobisty (15 języków)

## Autor

Julien LE SAUX  
Email : contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE wersja 3. Zobacz [LICENSE](LICENSE).

**Ten dokument został przetłumaczony z wersji fr na język pl przy użyciu modelu gpt-5.4-mini. Aby uzyskać więcej informacji o procesie tłumaczenia, zobacz https://gitlab.com/jls42/ai-powered-markdown-translator**


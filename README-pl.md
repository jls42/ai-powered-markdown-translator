# Tłumacz Markdowna wspierany przez AI

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

Tłumacz plików Markdown wykorzystujący **OpenAI**, **Mistral AI**, **Claude (Anthropic)** oraz **Google Gemini**.

Ten skrypt Pythona tłumaczy pliki Markdown z języka źródłowego na język docelowy, zachowując formatowanie, bloki kodu i metadane front matter.

## Główne funkcje

- **Wielu dostawców**: Obsługa 4 API (OpenAI, Mistral, Claude, Gemini)
- **Modele 2026**: GPT-5.4, Claude Sonnet 4.5, Gemini 3.1 Pro
- **Tryb ekonomiczny**: Opcja `--eco` do korzystania z szybszych i tańszych modeli
- **Pojedynczy plik**: Opcja `--file` do tłumaczenia jednego pliku
- **Inteligentna segmentacja**: Obsługa długich tekstów z limitami tokenów dla modeli
- **Zachowanie kodu**: Bloki kodu ORAZ kod inline (`` `...` ``) są zachowywane
- **Nazwa pliku**: Opcja `--keep_filename` do zachowania oryginalnej nazwy
- **Tryb news**: Opcja `--news` do ochrony angielskich cytatów i obsługi flag w artykułach informacyjnych
- **Konfiguracja .env**: Obsługa pliku `.env` dla kluczy API
- **Notatka tłumaczenia**: Opcjonalne dodanie notatki na końcu dokumentu

## Instalacja

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

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
# Avec OpenAI (défaut: gpt-5.4)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### Tryb ekonomiczny

Używa szybszych i tańszych modeli (gpt-5-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opcje

| Opcja | Opis |
|--------|-------------|
| `--file` | Pojedynczy plik Markdown do przetłumaczenia |
| `--source_dir` | Katalog źródłowy zawierający pliki Markdown |
| `--target_dir` | Katalog wyjściowy dla przetłumaczonych plików |
| `--source_lang` | Język źródłowy (domyślnie: `fr`) |
| `--target_lang` | Język docelowy (domyślnie: `en`) |
| `--model` | Konkretne używane modele |
| `--eco` | Używaj modeli ekonomicznych |
| `--use_mistral` | Używaj API Mistral AI |
| `--use_claude` | Używaj API Claude |
| `--use_gemini` | Używaj API Gemini |
| `--force` | Wymuś ponowne tłumaczenie |
| `--keep_filename` | Zachowaj oryginalną nazwę pliku |
| `--news` | Tryb wiadomości: chroni cytaty EN, obsługuje flagi według języka |
| `--add_translation_note` | Dodaj notatkę tłumaczenia |
| `--include_model` | Dołącz nazwę modelu do pliku wyjściowego |

### Modele domyślne (2026)

| Dostawca | Jakość (domyślnie) | Ekonomiczny (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Projekty korzystające z tego skryptu

- **[jls42.org](https://jls42.org)** - Wielojęzyczny blog osobisty (15 języków)

## Autor

Julien LE SAUX
Email : contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE Version 3. Zobacz [LICENSE](LICENSE).
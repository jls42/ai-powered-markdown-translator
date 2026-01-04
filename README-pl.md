# Tłumacz Markdown zasilany przez AI

🌍 [Angielski](README-en.md) | [Hiszpański](README-es.md) | [Chiński](README-zh.md) | [Niemiecki](README-de.md) | [Japoński](README-ja.md) | [Koreański](README-ko.md) | [Arabski](README-ar.md) | [Hindi](README-hi.md) | [Włoski](README-it.md) | [Niderlandzki](README-nl.md) | [Polski](README-pl.md) | [Portugalski](README-pt.md) | [Rumuński](README-ro.md) | [Szwedzki](README-sv.md)

Tłumacz plików Markdown korzystający z **OpenAI**, **Mistral AI**, **Claude (Anthropic)** i **Google Gemini**.

Ten skrypt Pythona tłumaczy pliki Markdown z języka źródłowego na język docelowy, zachowując formatowanie, bloki kodu i metadane front matter.

## Główne cechy

- **Wielu dostawców**: Obsługa 4 API (OpenAI, Mistral, Claude, Gemini)
- **Modele 2026**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **Tryb ekonomiczny**: Opcja `--eco` do używania szybszych i tańszych modeli
- **Pojedynczy plik**: Opcja `--file` do tłumaczenia jednego pliku
- **Inteligentna segmentacja**: Obsługa długich tekstów z limitami tokenów dla modeli
- **Zachowanie kodu**: Bloki kodu ORAZ kod inline (`` `...` ``) są zachowane
- **Nazwa pliku**: Opcja `--keep_filename` do zachowania oryginalnej nazwy
- **Obsługa .env**: Wsparcie pliku `.env` dla kluczy API
- **Notatka tłumaczeniowa**: Opcjonalne dodanie notatki na końcu dokumentu

## Instalacja

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

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
# Avec OpenAI (défaut: gpt-5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### Tryb ekonomiczny

Używa szybszych i tańszych modeli (gpt-5-mini, claude-haiku, gemini-flash):

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
| `--model` | Konkretne do użycia model |
| `--eco` | Użyj modeli ekonomicznych |
| `--use_mistral` | Użyj API Mistral AI |
| `--use_claude` | Użyj API Claude |
| `--use_gemini` | Użyj API Gemini |
| `--force` | Wymuś ponowne tłumaczenie |
| `--keep_filename` | Zachowaj oryginalną nazwę pliku |
| `--add_translation_note` | Dodaj notatkę tłumaczenia |
| `--include_model` | Dołącz nazwę modelu w pliku wyjściowym |

### Domyślne modele (2026)

| Dostawca | Jakość (domyślna) | Ekonomiczny (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Projekty wykorzystujące ten skrypt

- **[jls42.org](https://jls42.org)** - Blog osobisty przetłumaczony na 15 języków (364 pliki, 22 artykuły + 4 projekty)

## Autor

Julien LE SAUX  
E-mail: contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE Wersja 3. Zobacz [LICENCJA](LICENSE).

**Ten dokument został przetłumaczony z wersji fr na język pl przy użyciu modelu gpt-5-mini. Aby uzyskać więcej informacji na temat procesu tłumaczenia, zobacz https://gitlab.com/jls42/ai-powered-markdown-translator**


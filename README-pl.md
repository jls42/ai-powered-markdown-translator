# Tłumacz Markdown zasilany przez AI

🌍 [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

Tłumacz plików Markdown wykorzystujący **OpenAI**, **Mistral AI**, **Claude (Anthropic)** i **Google Gemini**.

Ten skrypt Pythona tłumaczy pliki Markdown z języka źródłowego na język docelowy, zachowując formatowanie, bloki kodu i metadane front matter.

## Główne funkcje

- **Wielu dostawców**: Obsługa 4 interfejsów API (OpenAI, Mistral, Claude, Gemini)
- **Modele 2026**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **Tryb oszczędny**: Opcja `--eco` do używania szybszych i tańszych modeli
- **Pojedynczy plik**: Opcja `--file` do przetłumaczenia jednego pliku
- **Inteligentna segmentacja**: Obsługa długich tekstów z limitami tokenów dla poszczególnych modeli
- **Zachowanie kodu**: Bloki kodu nie są tłumaczone
- **Nota tłumaczeniowa**: Opcjonalne dodanie noty na końcu dokumentu

## Instalacja

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Konfiguracja

Ustaw zmienną środowiskową dla interfejsu API, którego chcesz używać:

```bash
export OPENAI_API_KEY='votre-clé-api-openai'
export MISTRAL_API_KEY='votre-clé-api-mistral'
export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
export GOOGLE_API_KEY='votre-clé-api-google'
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

### Tryb oszczędny

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
| `--model` | Konkretny model do użycia |
| `--eco` | Użyj modeli oszczędnych |
| `--use_mistral` | Użyj API Mistral AI |
| `--use_claude` | Użyj API Claude |
| `--use_gemini` | Użyj API Gemini |
| `--force` | Wymuś ponowne tłumaczenie |
| `--add_translation_note` | Dodaj notę tłumaczeniową |

### Domyślne modele (2026)

| Dostawca | Jakość (domyślnie) | Oszczędny (`--eco`) |
|----------|--------------------|---------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Autor

Julien LE SAUX
E-mail : contact@jls42.org

## Licencja

GNU GENERAL PUBLIC LICENSE Wersja 3. Zobacz [LICENSE](LICENSE).
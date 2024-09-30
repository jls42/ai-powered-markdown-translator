# Tłumacz Markdown oparty na AI z OpenAI, Mistral AI i Claude od Anthropic

Ten projekt to zaawansowany skrypt Python, który wykorzystuje interfejsy API OpenAI, Mistral AI lub Claude od Anthropic do tłumaczenia plików Markdown z języka źródłowego na język docelowy. Jest zaprojektowany tak, aby był elastyczny i łatwy w użyciu, oferując dodatkowe opcje, takie jak dodawanie notatki o tłumaczeniu, ulepszone zarządzanie plikami wyjściowymi, wykrywanie istniejących plików oraz obsługę wielu języków i modeli tłumaczeniowych.

Aby zobaczyć demonstrację i szczegółowe wyjaśnienia, odwiedź [jls42.org](https://jls42.org/) lub w wersji przetłumaczonej: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) i [jls42.org 中文](https://jls42.org/traductions_zh/).

## Główne cechy

- **Tłumaczenie oparte na AI**: Wykorzystaj najnowsze technologie AI do tłumaczenia dokumentów za pomocą OpenAI, Mistral AI lub Claude od Anthropic.
- **Obsługa wielu języków**: Tłumacz swoje dokumenty na wiele języków z obsługą różnych modeli językowych.
- **Inteligentna segmentacja**: Efektywnie zarządzaj długimi tekstami dzięki automatycznej segmentacji.
- **Notatka o tłumaczeniu**: Automatycznie dodawaj notatkę o tłumaczeniu, aby poinformować czytelników o użytym procesie.
- **Ulepszone zarządzanie plikami wyjściowymi**: Sprawdź, czy tłumaczenie już istnieje przed rozpoczęciem tłumaczenia.
- **Ulepszone wykrywanie istniejących plików**: Szukaj plików odpowiadających nazwie podstawowej oryginalnego pliku i językowi docelowemu.
- **Elastyczny i rozszerzalny**: Kod jest ustrukturyzowany, aby umożliwić łatwe dodawanie nowych funkcji.

## Wymagania wstępne

- Python 3.6 lub nowszy.
- Ważny klucz API dla OpenAI, Mistral AI lub Claude od Anthropic.

## Instalacja

1. Sklonuj repozytorium Git:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. Zainstaluj niezbędne zależności:
```
pip install -r requirements.txt
```

## Konfiguracja

Skonfiguruj swoje środowisko, ustawiając zmienne środowiskowe dla niezbędnych kluczy API:

- **OpenAI**:
    ```
    export OPENAI_API_KEY='twój-klucz-api-openai'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='twój-klucz-api-mistral'
    ```
- **Claude od Anthropic**:
    ```
    export ANTHROPIC_API_KEY='twój-klucz-api-anthropic'
    ```

## Użycie

Skrypt oferuje kilka opcji do dostosowania procesu tłumaczenia:

### Opcje ogólne

- `--source_dir`: Katalog zawierający pliki Markdown do przetłumaczenia.
- `--target_dir`: Katalog wyjściowy dla przetłumaczonych plików.
- `--model`: Model tłumaczenia GPT do użycia. Domyślny model zależy od wybranego API.
- `--source_lang`: Język źródłowy dokumentów. Ważny szczególnie dla dodawania notatek o tłumaczeniu.
- `--target_lang`: Język docelowy tłumaczenia. Domyślnie jest to angielski.
- `--force`: Wymuś tłumaczenie, nawet jeśli tłumaczenie dla pliku już istnieje.

### Opcje specyficzne dla API

- `--use_mistral`: Użyj API Mistral AI do tłumaczenia.
- `--use_claude`: Użyj API Claude od Anthropic do tłumaczenia.
- `--add_translation_note`: Dodaj notatkę o tłumaczeniu do przetłumaczonej treści, określając użytą metodę i narzędzia.

### Przykłady użycia

- Tłumaczenie z francuskiego na angielski za pomocą OpenAI, dodając notatkę o tłumaczeniu:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Tłumaczenie z francuskiego na hiszpański za pomocą Mistral AI, bez notatki o tłumaczeniu:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Autor

Julien LE SAUX  
Email: contact@jls42.org

## Licencja

Ten projekt jest objęty licencją GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. Zobacz plik [LICENSE](LICENSE) dla szczegółów.

**Ten dokument został przetłumaczony z wersji fr na język pl przy użyciu modelu claude-3-5-sonnet-20240620. Aby uzyskać więcej informacji na temat procesu tłumaczenia, odwiedź https://gitlab.com/jls42/ai-powered-markdown-translator.**


# Tłumacz Markdown z wykorzystaniem sztucznej inteligencji z OpenAI, Mistral AI i Claude d'Anthropic

Ten projekt jest zaawansowanym skryptem Pythona, który wykorzystuje API OpenAI, Mistral AI lub Claude d'Anthropic do tłumaczenia plików Markdown z języka źródłowego na język docelowy. Jest zaprojektowany, aby być elastycznym i łatwym w użyciu, oferując dodatkowe opcje takie jak dodawanie noty tłumaczenia, zarządzanie poprawionymi plikami wyjściowymi, wykrywanie istniejących plików i obsługę wielu języków i modeli tłumaczenia.

Aby uzyskać demonstrację i szczegółowe wyjaśnienia, odwiedź [jls42.org](https://jls42.org/) lub w wersji przetłumaczonej: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) i [jls42.org 中文](https://jls42.org/traductions_zh/).

## Główne cechy

- **Tłumaczenie z wykorzystaniem sztucznej inteligencji**: Wykorzystaj najnowsze technologie sztucznej inteligencji do tłumaczenia dokumentów z OpenAI, Mistral AI lub Claude d'Anthropic.
- **Wielojęzyczna obsługa**: Tłumacz dokumenty na wiele języków z obsługą różnych modeli językowych.
- **Inteligentna segmentacja**: Skutecznie zarządzaj długimi tekstami dzięki automatycznej segmentacji.
- **Nota tłumaczenia**: Automatycznie dodaj notę tłumaczenia, aby poinformować czytelników o użytym procesie.
- **Poprawione zarządzanie plikami wyjściowymi**: Sprawdź, czy tłumaczenie już istnieje, zanim rozpocznie się tłumaczenie.
- **Ulepszona detekcja istniejących plików**: Szukaj plików odpowiadających nazwie podstawowej oryginalnego pliku i językowi docelowemu.
- **Elastyczny i rozszerzalny**: Kod jest zorganizowany, aby ułatwić dodawanie nowych funkcji.

## Wymagania wstępne

- Python 3.6 lub nowsza wersja.
- Ważny klucz API dla OpenAI, Mistral AI lub Claude d'Anthropic.

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
- **Claude d'Anthropic**:
    ```
    export ANTHROPIC_API_KEY='twój-klucz-api-anthropic'
    ```

## Użycie

Skrypt oferuje wiele opcji do dostosowania procesu tłumaczenia:

### Opcje ogólne

- `--source_dir`: Katalog zawierający pliki Markdown do przetłumaczenia.
- `--target_dir`: Katalog wyjściowy dla przetłumaczonych plików.
- `--model`: Model tłumaczenia GPT do użycia. Domyślny model zależy od wybranego API.
- `--source_lang`: Język źródłowy dokumentów. Ważny szczególnie przy dodawaniu not tłumaczenia.
- `--target_lang`: Język docelowy dla tłumaczenia. Domyślnie jest to angielski.
- `--force`: Wymuś tłumaczenie, nawet jeśli tłumaczenie już istnieje dla pliku.

### Opcje specyficzne dla API

- `--use_mistral`: Użyj API Mistral AI do tłumaczenia.
- `--use_claude`: Użyj API Claude d'Anthropic do tłumaczenia.
- `--add_translation_note`: Dodaj notę tłumaczenia do przetłumaczonej zawartości, określając użyte metody i narzędzia.

### Przykłady użycia

- Tłumaczenie z francuskiego na angielski z OpenAI, dodając notę tłumaczenia:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Tłumaczenie z francuskiego na hiszpański z Mistral AI, bez noty tłumaczenia:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Autor

Julien LE SAUX
Email: contact@jls42.org

## Licencja

Ten projekt jest objęty licencją GNU GENERAL PUBLIC LICENSE Wersja 3, 29 czerwca 2007. Zobacz plik [LICENSE](LICENSE) dla szczegółów.

**Ce document a été traduit de la version fr vers la langue pl en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator**


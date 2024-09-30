# Tłumacz Markdown zasilany AI z OpenAI, Mistral AI i Claude d'Anthropic

Ten projekt to zaawansowany skrypt Pythona, który wykorzystuje API OpenAI, Mistral AI lub Claude d'Anthropic do tłumaczenia plików Markdown z języka źródłowego na język docelowy. Jest zaprojektowany tak, aby był elastyczny i łatwy w użyciu, oferując dodatkowe opcje takie jak dodawanie noty tłumaczeniowej, ulepszone zarządzanie plikami wyjściowymi, wykrywanie istniejących plików oraz wsparcie dla wielu języków i modeli tłumaczeń.

Na demonstrację i szczegółowe wyjaśnienia zapraszamy na [jls42.org](https://jls42.org/) lub w wersjach przetłumaczonych: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) i [jls42.org 中文](https://jls42.org/traductions_zh/).

## Główne Cechy

- **Tłumaczenie zasilane AI**: Używaj najnowszych technologii AI do tłumaczenia dokumentów z OpenAI, Mistral AI lub Claude d'Anthropic.
- **Wsparcie dla wielu języków**: Tłumacz dokumenty na różne języki z wsparciem dla różnych modeli językowych.
- **Inteligentna segmentacja**: Skutecznie zarządzaj długimi tekstami dzięki automatycznej segmentacji.
- **Nota tłumaczeniowa**: Automatycznie dodawaj notę tłumaczeniową, aby poinformować czytelników o użytym procesie.
- **Ulepszone zarządzanie plikami wyjściowymi**: Sprawdź, czy tłumaczenie już istnieje, zanim rozpoczniesz tłumaczenie.
- **Ulepszone wykrywanie istniejących plików**: Wyszukaj pliki odpowiadające podstawowej nazwie pliku źródłowego i języka docelowego.
- **Elastyczny i rozbudowywalny**: Kod jest uporządkowany w sposób ułatwiający dodawanie nowych funkcji.

## Wymagania

- Python 3.6 lub nowszy.
- Ważny klucz API dla OpenAI, Mistral AI lub Claude d'Anthropic.

## Instalacja

1. Sklonuj repozytorium Git:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. Zainstaluj wymagane zależności:
```
pip install -r requirements.txt
```

## Konfiguracja

Skonfiguruj swoje środowisko, ustawiając zmienne środowiskowe dla wymaganych kluczy API:

- **OpenAI**:
    ```
    export OPENAI_API_KEY='your-openai-api-key'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='your-mistral-api-key'
    ```
- **Claude d'Anthropic**:
    ```
    export ANTHROPIC_API_KEY='your-anthropic-api-key'
    ```

## Użycie

Skrypt oferuje kilka opcji do personalizacji procesu tłumaczenia:

### Opcje Ogólne

- `--source_dir` : Katalog zawierający pliki Markdown do tłumaczenia.
- `--target_dir` : Katalog wyjściowy dla przetłumaczonych plików.
- `--model` : Model tłumaczenia GPT do użycia. Domyślny model zależy od wybranego API.
- `--source_lang` : Język źródłowy dokumentów. Ważne zwłaszcza dla dodawania not tłumaczeniowych.
- `--target_lang` : Język docelowy tłumaczenia. Domyślnie jest to angielski.
- `--force` : Wymuś tłumaczenie, nawet jeśli tłumaczenie dla pliku już istnieje.

### Opcje Specyficzne dla API

- `--use_mistral` : Użyj API Mistral AI do tłumaczenia.
- `--use_claude` : Użyj API Claude d'Anthropic do tłumaczenia.
- `--add_translation_note` : Dodaj notę tłumaczeniową do przetłumaczonej zawartości, określającą metodę i użyte narzędzia.

### Przykłady Użycia

- Tłumaczenie z francuskiego na angielski za pomocą OpenAI, z dodaniem noty tłumaczeniowej:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Tłumaczenie z francuskiego na hiszpański za pomocą Mistral AI, bez noty tłumaczeniowej:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Autor

Julien LE SAUX  
Email: contact@jls42.org

## Licencja

Ten projekt jest licencjonowany na GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. Zobacz plik [LICENSE](LICENSE) po więcej szczegółów.

**Ten dokument został przetłumaczony z wersji fr na język pl przy użyciu modelu gpt-4o. Aby uzyskać więcej informacji na temat procesu tłumaczenia, odwiedź https://gitlab.com/jls42/ai-powered-markdown-translator**


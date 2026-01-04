### Dziennik zmian

🌍 [Angielski](CHANGELOG-en.md) | [Hiszpański](CHANGELOG-es.md) | [Chiński](CHANGELOG-zh.md) | [Niemiecki](CHANGELOG-de.md) | [Japoński](CHANGELOG-ja.md) | [Koreański](CHANGELOG-ko.md) | [Arabski](CHANGELOG-ar.md) | [Hindi](CHANGELOG-hi.md) | [Włoski](CHANGELOG-it.md) | [Niderlandzki](CHANGELOG-nl.md) | [Polski](CHANGELOG-pl.md) | [Portugalski](CHANGELOG-pt.md) | [Rumuński](CHANGELOG-ro.md) | [Szwedzki](CHANGELOG-sv.md)

- **1.7** Nowości :
    - Opcja `--keep_filename` do zachowania oryginalnej nazwy pliku podczas tłumaczenia
    - Obsługa pliku `.env` do automatycznego ładowania kluczy API
    - **Zachowanie kodu inline** : backticky (`` `...` ``) są teraz chronione podczas tłumaczenia
    - Ulepszenie promptu systemowego :
        - Lepsze zarządzanie cudzysłowami w frontmatter YAML
        - Ochrona zmiennych szablonu `{variable}`
        - Zakaz dodawania niezamówionych uwag tłumacza
    - Przetestowano pomyślnie na 364 plikach (migracja bloga jls42.org)
- **1.6** Nowości :
    - Wsparcie API Google Gemini dla tłumaczeń (`--use_gemini`)
    - Aktualizacja domyślnych modeli 2026 :
        - OpenAI : `gpt-5` (jakość), `gpt-5-mini` (ekonomiczny)
        - Claude : `claude-sonnet-4-5` (jakość), `claude-haiku-4-5` (ekonomiczny)
        - Gemini : `gemini-3-pro-preview` (jakość), `gemini-3-flash-preview` (ekonomiczny)
    - Tryb ekonomiczny (`--eco`) do używania szybszych i tańszych modeli
    - Tłumaczenie pojedynczego pliku (`--file`) bez przeszukiwania katalogu
    - Nowy uproszczony wzorzec nazewnictwa : `{base}-{lang}.md`
    - Opcja `--include_model` do zachowania starego formatu z nazwą modelu
    - Wsparcie dla nielistowanych modeli z domyślnym limitem tokenów (128k)
    - README przetłumaczony na 14 języków
- **1.5** Ulepszenia :
    - **Aktualizacja kluczy API i domyślnych modeli :**
        - **OpenAI :** Zaktualizowano `DEFAULT_MODEL_OPENAI` do `"gpt-4o"`.
        - **Mistral AI :** Zaktualizowano `DEFAULT_MODEL_MISTRAL` do `"mistral-large-latest"`.
        - **Claude od Anthropic :** Dodano `DEFAULT_ANTHROPIC_API_KEY` i zaktualizowano `DEFAULT_MODEL_CLAUDE` do `"claude-3-5-sonnet-20240620"`.
    - **Optymalizacja promptów tłumaczeniowych :**
        - Promptów do tłumaczeń bezpośrednich i not tłumaczeniowych wzbogacono dla lepszej jasności i efektywności, włączając szczegółowe instrukcje dotyczące zachowania metadanych i specyficznych elementów formatowania.
    - **Refaktoryzacja kodu :**
        - Zastąpienie `MistralClient` klasą `Mistral` do inicjalizacji klienta Mistral AI.
        - Reorganizacja importów dla lepszej czytelności i konserwacji.
        - Ulepszenie segmentacji tekstu i obsługi bloków kodu w celu zachowania oryginalnego formatowania podczas tłumaczenia.
    - **Obsługa plików wyjściowych :**
        - Odwrócenie kolejności modelu i języka w nazwie plików wyjściowych (np. `f"{base}-{args.target_lang}-{args.model}.md"`), ułatwiając organizację i wyszukiwanie tłumaczeń.
    - **Różne ulepszenia :**
        - Czyszczenie kodu poprzez usuwanie niepotrzebnych pustych linii.
        - Drobne poprawki w celu usprawnienia struktury i czytelności skryptu.
- **1.4** Nowości :
    - Wsparcie API Claude od Anthropic dla tłumaczeń
    - Optymalizacja promptów dla większej jasności i efektywności
    - Drobne poprawki w celu poprawy utrzymania kodu
- **1.3** Ulepszenia i nowe funkcje :
    - Ulepszona obsługa bloków kodu
    - Ulepszona obsługa plików wyjściowych
    - Ulepszona detekcja istniejących plików
    - Opcja `--force` do wymuszenia tłumaczenia
    - Odwrócenie kolejności modelu i języka w nazwie pliku wyjściowego
- **1.2** Poprawka changelogu
- **1.1** Dodano wsparcie dla API Mistral IA
- **1.0** Wersja początkowa - Wsparcie API OpenAI

**Ten dokument został przetłumaczony z wersji fr na język pl przy użyciu modelu gpt-5-mini. Aby uzyskać więcej informacji na temat procesu tłumaczenia, zobacz https://gitlab.com/jls42/ai-powered-markdown-translator**


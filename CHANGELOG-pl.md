### Dziennik zmian

🌍 [Francuski](CHANGELOG.md) | [Angielski](CHANGELOG-en.md) | [Hiszpański](CHANGELOG-es.md) | [Chiński](CHANGELOG-zh.md) | [Niemiecki](CHANGELOG-de.md) | [Japoński](CHANGELOG-ja.md) | [Koreański](CHANGELOG-ko.md) | [Arabski](CHANGELOG-ar.md) | [Hindi](CHANGELOG-hi.md) | [Włoski](CHANGELOG-it.md) | [Niderlandzki](CHANGELOG-nl.md) | [Polski](CHANGELOG-pl.md) | [Portugalski](CHANGELOG-pt.md) | [Rumuński](CHANGELOG-ro.md) | [Szwedzki](CHANGELOG-sv.md)

- **1.7** Nowości :
    - Opcja `--keep_filename` do zachowania oryginalnej nazwy pliku podczas tłumaczenia
    - Obsługa pliku `.env` do automatycznego wczytywania kluczy API
    - **Zachowanie kodu inline** : znaki backtick (`` `...` ``) są teraz chronione podczas tłumaczenia
    - Ulepszenie promptu systemowego :
        - Lepsze zarządzanie cudzysłowami w frontmatter YAML
        - Ochrona zmiennych szablonu `{variable}`
        - Zakaz niezamawianych notatek tłumacza
    - Przetestowano pomyślnie na 364 plikach (migracja bloga jls42.org)
- **1.6** Nowości :
    - Obsługa API Google Gemini do tłumaczeń (`--use_gemini`)
    - Aktualizacja domyślnych modeli 2026 :
        - OpenAI : `gpt-5` (jakość), `gpt-5-mini` (ekonomiczny)
        - Claude : `claude-sonnet-4-5` (jakość), `claude-haiku-4-5` (ekonomiczny)
        - Gemini : `gemini-3-pro-preview` (jakość), `gemini-3-flash-preview` (ekonomiczny)
    - Tryb ekonomiczny (`--eco`) do używania szybszych i tańszych modeli
    - Tłumaczenie pojedynczego pliku (`--file`) bez przeglądania katalogu
    - Nowy uproszczony wzorzec nazewnictwa : `{base}-{lang}.md`
    - Opcja `--include_model` do zachowania starego formatu z nazwą modelu
    - Obsługa modeli nielistowanych z domyślnym limitem tokenów (128k)
    - README przetłumaczony na 14 języków
- **1.5** Ulepszenia :
    - **Aktualizacja kluczy API i domyślnych modeli :**
        - **OpenAI :** Aktualizacja z `DEFAULT_MODEL_OPENAI` do `"gpt-4o"`.
        - **Mistral AI :** Aktualizacja z `DEFAULT_MODEL_MISTRAL` do `"mistral-large-latest"`.
        - **Claude od Anthropic :** Dodano `DEFAULT_ANTHROPIC_API_KEY` i zaktualizowano `DEFAULT_MODEL_CLAUDE` do `"claude-3-5-sonnet-20240620"`.
    - **Optymalizacja promptów do tłumaczeń :**
        - Prompty do tłumaczeń bezpośrednich i notek tłumaczeniowych zostały wzbogacone dla lepszej przejrzystości i efektywności, zawierając szczegółowe instrukcje dotyczące zachowania metadanych i specyficznych elementów formatowania.
    - **Refaktoryzacja kodu :**
        - Zamiana `MistralClient` na klasę `Mistral` do inicjalizacji klienta Mistral AI.
        - Przeorganizowano importy dla lepszej czytelności i utrzymania.
        - Ulepszono segmentację tekstu i obsługę bloków kodu, aby zachować oryginalne formatowanie podczas tłumaczenia.
    - **Zarządzanie plikami wyjściowymi :**
        - Odwrócenie kolejności modelu i języka w nazwie plików wyjściowych (np. `f"{base}-{args.target_lang}-{args.model}.md"`), ułatwiając organizację i wyszukiwanie tłumaczeń.
    - **Różne ulepszenia :**
        - Czyszczenie kodu poprzez usuwanie niepotrzebnych pustych linii.
        - Drobne poprawki poprawiające strukturę i czytelność skryptu.
- **1.4** Nowości :
    - Obsługa API Claude (Anthropic) do tłumaczeń
    - Optymalizacja promptów dla większej przejrzystości i efektywności
    - Drobne poprawki poprawiające utrzymanie kodu
- **1.3** Ulepszenia i nowe funkcje :
    - Ulepszona obsługa bloków kodu
    - Ulepszona obsługa plików wyjściowych
    - Ulepszone wykrywanie istniejących plików
    - Opcja `--force` do wymuszenia tłumaczenia
    - Odwrócenie kolejności modelu i języka w nazwie pliku wyjściowego
- **1.2** Poprawka changelogu
- **1.1** Dodano obsługę API Mistral AI
- **1.0** Wersja początkowa - Obsługa API OpenAI

**Ten dokument został przetłumaczony z wersji fr na język pl przy użyciu modelu gpt-5-mini. Aby uzyskać więcej informacji na temat procesu tłumaczenia, zobacz https://gitlab.com/jls42/ai-powered-markdown-translator**


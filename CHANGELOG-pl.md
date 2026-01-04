### Dziennik zmian

🌍 [Angielski](CHANGELOG-en.md) | [Hiszpański](CHANGELOG-es.md) | [Chiński](CHANGELOG-zh.md) | [Niemiecki](CHANGELOG-de.md) | [Japoński](CHANGELOG-ja.md) | [Koreański](CHANGELOG-ko.md) | [Arabski](CHANGELOG-ar.md) | [Hindi](CHANGELOG-hi.md) | [Włoski](CHANGELOG-it.md) | [Niderlandzki](CHANGELOG-nl.md) | [Polski](CHANGELOG-pl.md) | [Portugalski](CHANGELOG-pt.md) | [Rumuński](CHANGELOG-ro.md) | [Szwedzki](CHANGELOG-sv.md)

- **1.7** Nowości :
    - Opcja `--keep_filename` aby zachować oryginalną nazwę pliku podczas tłumaczenia
    - Wsparcie pliku `.env` do automatycznego ładowania kluczy API
    - Zachowanie kodu inline : backticky (`` `...` ``) są teraz chronione podczas tłumaczenia
    - Ulepszenie promptu systemowego :
        - Lepsze zarządzanie cudzysłowami w YAML frontmatter
        - Ochrona zmiennych szablonu `{variable}`
        - Zakaz niezamówionych notatek tłumacza
    - Przetestowano pomyślnie na 364 plikach (migracja bloga jls42.org)
- **1.6** Nowości :
    - Wsparcie API Google Gemini do tłumaczeń (`--use_gemini`)
    - Aktualizacja domyślnych modeli 2026 :
        - OpenAI : `gpt-5` (jakość), `gpt-5-mini` (ekonomiczny)
        - Claude : `claude-sonnet-4-5` (jakość), `claude-haiku-4-5` (ekonomiczny)
        - Gemini : `gemini-3-pro-preview` (jakość), `gemini-3-flash-preview` (ekonomiczny)
    - Tryb ekonomiczny (`--eco`) do używania szybszych i tańszych modeli
    - Tłumaczenie pojedynczego pliku (`--file`) bez przeglądania katalogu
    - Nowy uproszczony wzorzec nazewnictwa : `{base}-{lang}.md`
    - Opcja `--include_model` aby zachować stary format z nazwą modelu
    - Wsparcie modeli nienotowanych z domyślnym limitem tokenów (128k)
    - README przetłumaczony na 14 języków
- **1.5** Ulepszenia :
    - Aktualizacja kluczy API i domyślnych modeli :
        - OpenAI : aktualizacja z `DEFAULT_MODEL_OPENAI` do `"gpt-4o"`.
        - Mistral AI : aktualizacja z `DEFAULT_MODEL_MISTRAL` do `"mistral-large-latest"`.
        - Claude od Anthropic : dodano `DEFAULT_ANTHROPIC_API_KEY` i aktualizacja z `DEFAULT_MODEL_CLAUDE` do `"claude-3-5-sonnet-20240620"`.
    - Optymalizacja promptów tłumaczeniowych :
        - Prompty dla tłumaczeń bezpośrednich i not tłumaczeniowych zostały wzbogacone dla większej jasności i efektywności, zawierając szczegółowe instrukcje dotyczące zachowania metadanych i elementów formatowania.
    - Refaktoryzacja kodu :
        - Zastąpienie `MistralClient` klasą `Mistral` do inicjalizacji klienta Mistral AI.
        - Reorganizacja importów dla lepszej czytelności i utrzymania.
        - Ulepszenie segmentacji tekstów i obsługi bloków kodu, aby zachować oryginalne formatowanie podczas tłumaczenia.
    - Zarządzanie plikami wyjściowymi :
        - Odwrócenie kolejności modelu i języka w nazwach plików wyjściowych (na przykład, `f"{base}-{args.target_lang}-{args.model}.md"`), co ułatwia organizację i wyszukiwanie tłumaczeń.
    - Różne ulepszenia :
        - Czyszczenie kodu poprzez usuwanie zbędnych pustych linii.
        - Drobne poprawki poprawiające strukturę i czytelność skryptu.
- **1.4** Nowości :
    - Wsparcie API Claude od Anthropic do tłumaczeń
    - Optymalizacja promptów dla większej klarowności i wydajności
    - Drobne poprawki poprawiające utrzymanie kodu
- **1.3** Ulepszenia i nowe funkcje :
    - Ulepszone zarządzanie blokami kodu
    - Ulepszone zarządzanie plikami wyjściowymi
    - Ulepszona detekcja istniejących plików
    - Opcja `--force` do wymuszenia tłumaczenia
    - Odwrócenie modelu i języka w nazwie pliku wyjściowego
- **1.2** Poprawka dziennika zmian
- **1.1** Dodano wsparcie dla API Mistral AI
- **1.0** Wersja początkowa - wsparcie dla API OpenAI

**Ten dokument został przetłumaczony z wersji fr na język pl przy użyciu modelu gpt-5-mini. Aby uzyskać więcej informacji na temat procesu tłumaczenia, zobacz https://gitlab.com/jls42/ai-powered-markdown-translator**


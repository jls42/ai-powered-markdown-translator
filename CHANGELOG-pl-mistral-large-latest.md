### Changelog

- **1.0** Wersja początkowa - Obsługa API OpenAI
- **1.1** Dodanie obsługi API Mistral IA
- **1.2** Naprawa changelogu
- **1.3** Ulepszenia i nowe funkcje:
    - Ulepszona obsługa bloków kodu
    - Ulepszona obsługa plików wyjściowych
    - Ulepszona detekcja istniejących plików
    - Opcja `--force` do wymuszenia tłumaczenia
    - Odwrócenie modelu i języka w nazwie pliku wyjściowego
- **1.4** Nowości:
    - Obsługa API Claude od Anthropic dla tłumaczenia
    - Optymalizacja promptów dla większej klarowności i efektywności
    - Drobne dostosowania do poprawy utrzymania kodu
- **1.5** Ulepszenia:
    - **Aktualizacja kluczy API i domyślnych modeli:**
        - **OpenAI:** Aktualizacja `DEFAULT_MODEL_OPENAI` do `"gpt-4o"`.
        - **Mistral AI:** Aktualizacja `DEFAULT_MODEL_MISTRAL` do `"mistral-large-latest"`.
        - **Claude z Anthropic:** Dodanie `DEFAULT_ANTHROPIC_API_KEY` i aktualizacja `DEFAULT_MODEL_CLAUDE` do `"claude-3-5-sonnet-20240620"`.
    - **Optymalizacja promptów tłumaczenia:**
        - Prompty dla bezpośrednich tłumaczeń i notatek tłumaczeń zostały wzbogacone dla większej klarowności i efektywności, w tym szczegółowe instrukcje dotyczące zachowania metadanych i specyficznych elementów formatowania.
    - **Refaktoryzacja kodu:**
        - Zastąpienie `MistralClient` klasą `Mistral` do inicjalizacji klienta Mistral AI.
        - Przeorganizowanie importów dla lepszej czytelności i utrzymania.
        - Poprawa segmentacji tekstów i obsługi bloków kodu dla zachowania oryginalnego formatowania w trakcie tłumaczenia.
    - **Obsługa plików wyjściowych:**
        - Odwrócenie modelu i języka w nazwie plików wyjściowych (np. `f"{base}-{args.target_lang}-{args.model}.md"`), ułatwiając tym samym organizację i wyszukiwanie tłumaczeń.
    - **Różne ulepszenia:**
        - Czyszczenie kodu przez usunięcie niepotrzebnych pustych linii.
        - Drobne dostosowania do poprawy struktury i czytelności skryptu.

**Ce document a été traduit de la version fr vers la langue pl en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consoltez https://gitlab.com/jls42/ai-powered-markdown-translator.**


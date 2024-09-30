### Dziennik zmian

- **1.0** Wersja początkowa - Obsługa API OpenAI
- **1.1** Dodanie obsługi API Mistral AI
- **1.2** Naprawa dziennika zmian
- **1.3** Ulepszenia i nowe funkcje:
    - Ulepszona obsługa bloków kodu
    - Ulepszona obsługa plików wyjściowych
    - Ulepszone wykrywanie istniejących plików
    - Opcja `--force` do wymuszenia tłumaczenia
    - Odwrócenie modelu i języka w nazwie pliku wyjściowego
- **1.4** Nowości:
    - Obsługa API Claude od Anthropic do tłumaczenia
    - Optymalizacja promptów dla zwiększonej jasności i wydajności
    - Drobne dostosowania w celu poprawy utrzymania kodu
- **1.5** Ulepszenia:
    - **Aktualizacja kluczy API i domyślnych modeli:**
        - **OpenAI:** Aktualizacja `DEFAULT_MODEL_OPENAI` do `"gpt-4o"`.
        - **Mistral AI:** Aktualizacja `DEFAULT_MODEL_MISTRAL` do `"mistral-large-latest"`.
        - **Claude od Anthropic:** Dodanie `DEFAULT_ANTHROPIC_API_KEY` i aktualizacja `DEFAULT_MODEL_CLAUDE` do `"claude-3-5-sonnet-20240620"`.
    - **Optymalizacja promptów do tłumaczenia:**
        - Prompty do tłumaczeń bezpośrednich i notatek tłumaczeniowych zostały wzbogacone dla lepszej jasności i wydajności, zawierając szczegółowe instrukcje dotyczące zachowania metadanych i specyficznych elementów formatowania.
    - **Refaktoryzacja kodu:**
        - Zastąpienie `MistralClient` klasą `Mistral` do inicjalizacji klienta Mistral AI.
        - Reorganizacja importów dla lepszej czytelności i utrzymania.
        - Poprawa segmentacji tekstów i obsługi bloków kodu w celu zachowania oryginalnego formatowania podczas tłumaczenia.
    - **Zarządzanie plikami wyjściowymi:**
        - Odwrócenie modelu i języka w nazwach plików wyjściowych (np. `f"{base}-{args.target_lang}-{args.model}.md"`), ułatwiając tym samym organizację i wyszukiwanie tłumaczeń.
    - **Różne ulepszenia:**
        - Czyszczenie kodu poprzez usunięcie niepotrzebnych pustych linii.
        - Drobne dostosowania w celu poprawy struktury i czytelności skryptu.

**Ten dokument został przetłumaczony z wersji fr na język pl przy użyciu modelu claude-3-5-sonnet-20240620. Aby uzyskać więcej informacji na temat procesu tłumaczenia, odwiedź https://gitlab.com/jls42/ai-powered-markdown-translator.**


### Dziennik zmian

- **1.0** Wersja początkowa - Wsparcie dla API OpenAI
- **1.1** Dodanie wsparcia dla API Mistral IA
- **1.2** Naprawa dziennika zmian
- **1.3** Ulepszenia i nowe funkcje:
    - Ulepszona obsługa bloków kodu
    - Ulepszona obsługa plików wyjściowych
    - Ulepszona detekcja istniejących plików
    - Opcja `--force` do wymuszenia tłumaczenia
    - Odwrócenie modelu i języka w nazwie pliku wyjściowego
- **1.4** Nowości:
    - Wsparcie dla API Claude d'Anthropic do tłumaczeń
    - Optymalizacja promptów dla większej przejrzystości i efektywności
    - Drobne poprawki w celu ulepszenia konserwacji kodu
- **1.5** Ulepszenia:
    - **Aktualizacja kluczy API i domyślnych modeli:**
        - **OpenAI:** Aktualizacja `DEFAULT_MODEL_OPENAI` do `"gpt-4o"`.
        - **Mistral AI:** Aktualizacja `DEFAULT_MODEL_MISTRAL` do `"mistral-large-latest"`.
        - **Claude d'Anthropic:** Dodanie `DEFAULT_ANTHROPIC_API_KEY` i aktualizacja `DEFAULT_MODEL_CLAUDE` do `"claude-3-5-sonnet-20240620"`.
    - **Optymalizacja promptów tłumaczenia:**
        - Prompty do bezpośrednich tłumaczeń i uwagi tłumaczeniowe zostały wzbogacone dla lepszej przejrzystości i efektywności, włączając szczegółowe instrukcje dotyczące zachowania metadanych i specyficznych elementów formatowania.
    - **Refaktoryzacja kodu:**
        - Zastąpienie `MistralClient` klasą `Mistral` do inicjalizacji klienta Mistral AI.
        - Przearanżowanie importów dla lepszej czytelności i konserwacji.
        - Ulepszenie segmentacji tekstów i obsługi bloków kodu w celu zachowania oryginalnego formatu podczas tłumaczenia.
    - **Obsługa plików wyjściowych:**
        - Odwrócenie modelu i języka w nazwie plików wyjściowych (na przykład, `f"{base}-{args.target_lang}-{args.model}.md"`), co ułatwia organizację i wyszukiwanie tłumaczeń.
    - **Różne ulepszenia:**
        - Oczyszczenie kodu z niepotrzebnych pustych linii.
        - Drobne poprawki w celu ulepszania struktury i czytelności skryptu.

**Ten dokument został przetłumaczony z wersji fr na język pl przy użyciu modelu gpt-4o. Więcej informacji na temat procesu tłumaczenia znajdziesz na stronie https://gitlab.com/jls42/ai-powered-markdown-translator**


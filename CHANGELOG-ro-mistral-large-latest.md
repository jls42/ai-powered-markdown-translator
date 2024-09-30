### Changelog

- **1.0** Versiunea inițială - Suport pentru API-ul OpenAI
- **1.1** Adăugare suport pentru API-ul Mistral IA
- **1.2** Fix jurnal de modificări
- **1.3** Îmbunătățiri și noi funcționalități:
    - Gestionare îmbunătățită a blocurilor de cod
    - Gestionare îmbunătățită a fișierelor de ieșire
    - Detectare îmbunătățită a fișierelor existente
    - Opțiune `--force` pentru a forța traducerea
    - Inversare a modelului și a limbii în numele fișierului de ieșire
- **1.4** Noutăți:
    - Suport pentru API-ul Claude al Anthropic pentru traducere
    - Optimizare a prompturilor pentru o claritate și eficiență crescute
    - Ajustări minore pentru îmbunătățirea întreținerii codului
- **1.5** Îmbunătățiri:
    - **Actualizare chei API și modele implicite:**
        - **OpenAI:** Actualizare `DEFAULT_MODEL_OPENAI` la `"gpt-4o"`.
        - **Mistral AI:** Actualizare `DEFAULT_MODEL_MISTRAL` la `"mistral-large-latest"`.
        - **Claude al Anthropic:** Adăugare `DEFAULT_ANTHROPIC_API_KEY` și actualizare `DEFAULT_MODEL_CLAUDE` la `"claude-3-5-sonnet-20240620"`.
    - **Optimizare a prompturilor de traducere:**
        - Prompturile pentru traducerile directe și notele de traducere au fost îmbogățite pentru o mai bună claritate și eficiență, incluzând instrucțiuni detaliate despre păstrarea metadatelor și a elementelor de formatare specifice.
    - **Refactorizare a codului:**
        - Înlocuire `MistralClient` cu clasa `Mistral` pentru inițializarea clientului Mistral AI.
        - Reorganizare a importurilor pentru o mai bună lizibilitate și întreținere.
        - Îmbunătățire a segmentării textelor și gestionarea blocurilor de cod pentru a păstra formatarea originală în timpul traducerii.
    - **Gestionare a fișierelor de ieșire:**
        - Inversare a modelului și a limbii în numele fișierelor de ieșire (de exemplu, `f"{base}-{args.target_lang}-{args.model}.md"`), facilitând astfel organizarea și căutarea traducerilor.
    - **Îmbunătățiri diverse:**
        - Curățare a codului prin eliminarea liniilor goale inutile.
        - Ajustări minore pentru îmbunătățirea structurii și lizibilității scriptului.

**'Ce document a été traduit de la version fr vers la langue ro en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator'**


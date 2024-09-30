### Jurnal de modificări

- **1.0** Versiune inițială - Suport pentru API-ul OpenAI
- **1.1** Adăugare suport pentru API-ul Mistral IA
- **1.2** Corectare jurnal de modificări
- **1.3** Îmbunătățiri și noi funcționalități:
    - Gestionare îmbunătățită a blocurilor de cod
    - Gestionare îmbunătățită a fișierelor de ieșire
    - Detecție îmbunătățită a fișierelor existente
    - Opțiunea `--force` pentru a forța traducerea
    - Inversarea modelului și a limbii în numele fișierului de ieșire
- **1.4** Noutăți:
    - Suport pentru API-ul Claude de la Anthropic pentru traducere
    - Optimizarea prompturilor pentru o claritate și eficiență sporite
    - Ajustări minore pentru a îmbunătăți întreținerea codului
- **1.5** Îmbunătățiri:
    - **Actualizarea cheilor API și a modelelor implicite:**
        - **OpenAI:** Actualizare `DEFAULT_MODEL_OPENAI` la `"gpt-4o"`.
        - **Mistral AI:** Actualizare `DEFAULT_MODEL_MISTRAL` la `"mistral-large-latest"`.
        - **Claude de la Anthropic:** Adăugare `DEFAULT_ANTHROPIC_API_KEY` și actualizare `DEFAULT_MODEL_CLAUDE` la `"claude-3-5-sonnet-20240620"`.
    - **Optimizarea prompturilor de traducere:**
        - Prompturile pentru traducerile directe și notele de traducere au fost îmbogățite pentru o mai bună claritate și eficiență, incluzând instrucțiuni detaliate privind păstrarea metadatelor și a elementelor de formatare specifice.
    - **Refactorizarea codului:**
        - Înlocuirea `MistralClient` cu clasa `Mistral` pentru inițializarea clientului Mistral AI.
        - Reorganizarea importurilor pentru o mai bună lizibilitate și întreținere.
        - Îmbunătățirea segmentării textelor și gestionarea blocurilor de cod pentru a păstra formatarea originală în timpul traducerii.
    - **Gestionarea fișierelor de ieșire:**
        - Inversarea modelului și a limbii în numele fișierelor de ieșire (de exemplu, `f"{base}-{args.target_lang}-{args.model}.md"`), facilitând astfel organizarea și căutarea traducerilor.
    - **Diverse îmbunătățiri:**
        - Curățarea codului prin eliminarea liniilor goale inutile.
        - Ajustări minore pentru a îmbunătăți structura și lizibilitatea scriptului.

**Ce document a fost tradus din versiunea fr în limba ro folosind modelul claude-3-5-sonnet-20240620. Pentru mai multe informații despre procesul de traducere, consultați https://gitlab.com/jls42/ai-powered-markdown-translator**


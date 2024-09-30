### Changelog

- **1.0** Versione iniziale - Supporto dell'API OpenAI
- **1.1** Aggiunta il supporto dell'API Mistral IA
- **1.2** Correzione del changelog
- **1.3** Miglioramenti e nuove funzionalità:
    - Gestione migliorata dei blocchi di codice
    - Gestione migliorata dei file di output
    - Rilevazione migliorata dei file esistenti
    - Opzione `--force` per forzare la traduzione
    - Inversione del modello e della lingua nel nome del file di output
- **1.4** Novità:
    - Supporto dell'API Claude di Anthropic per la traduzione
    - Ottimizzazione dei prompt per una chiarezza ed efficienza aumentate
    - Regolazioni minori per migliorare la manutenzione del codice
- **1.5** Miglioramenti:
    - **Aggiornamento delle chiavi API e dei modelli predefiniti:**
        - **OpenAI:** Aggiornamento di `DEFAULT_MODEL_OPENAI` a `"gpt-4o"`.
        - **Mistral AI:** Aggiornamento di `DEFAULT_MODEL_MISTRAL` a `"mistral-large-latest"`.
        - **Claude di Anthropic:** Aggiunta di `DEFAULT_ANTHROPIC_API_KEY` e aggiornamento di `DEFAULT_MODEL_CLAUDE` a `"claude-3-5-sonnet-20240620"`.
    - **Ottimizzazione dei prompt di traduzione:**
        - I prompt per le traduzioni dirette e le note di traduzione sono stati arricchiti per una migliore chiarezza ed efficienza, includendo istruzioni dettagliate sulla conservazione dei metadati e degli elementi di formattazione specifici.
    - **Refactorizzazione del codice:**
        - Sostituzione di `MistralClient` con la classe `Mistral` per l'inizializzazione del client Mistral AI.
        - Riorganizzazione degli import per una migliore leggibilità e manutenzione.
        - Miglioramento della segmentazione dei testi e gestione dei blocchi di codice per preservare il formato originale durante la traduzione.
    - **Gestione dei file di output:**
        - Inversione del modello e della lingua nel nome dei file di output (ad esempio, `f"{base}-{args.target_lang}-{args.model}.md"`), facilitando così l'organizzazione e la ricerca delle traduzioni.
    - **Miglioramenti vari:**
        - Pulizia del codice eliminando le righe vuote non necessarie.
        - Regolazioni minori per migliorare la struttura e la leggibilità dello script.

**Questo documento è stato tradotto dalla versione fr alla lingua it utilizzando il modello gpt-4o. Per maggiori informazioni sul processo di traduzione, consultare https://gitlab.com/jls42/ai-powered-markdown-translator**


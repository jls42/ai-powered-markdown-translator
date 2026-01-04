### Registro delle modifiche

🌍 [Inglese](CHANGELOG-en.md) | [Spagnolo](CHANGELOG-es.md) | [Cinese](CHANGELOG-zh.md) | [Tedesco](CHANGELOG-de.md) | [Giapponese](CHANGELOG-ja.md) | [Coreano](CHANGELOG-ko.md) | [Arabo](CHANGELOG-ar.md) | [Hindi](CHANGELOG-hi.md) | [Italiano](CHANGELOG-it.md) | [Olandese](CHANGELOG-nl.md) | [Polacco](CHANGELOG-pl.md) | [Portoghese](CHANGELOG-pt.md) | [Rumeno](CHANGELOG-ro.md) | [Svedese](CHANGELOG-sv.md)

- **1.7** Novità :
    - Opzione `--keep_filename` per mantenere il nome del file originale durante la traduzione
    - Supporto del file `.env` per caricare automaticamente le chiavi API
    - **Preservazione del codice inline** : i backtick (`` `...` ``) sono ora protetti durante la traduzione
    - Miglioramento del prompt di sistema :
        - Migliore gestione delle virgolette nel frontmatter YAML
        - Protezione delle variabili template `{variable}`
        - Divieto di note del traduttore non richieste
    - Testato con successo su 364 file (migrazione blog jls42.org)
- **1.6** Novità :
    - Supporto dell'API Google Gemini per la traduzione (`--use_gemini`)
    - Aggiornamento dei modelli predefiniti 2026 :
        - OpenAI : `gpt-5` (qualità), `gpt-5-mini` (eco)
        - Claude : `claude-sonnet-4-5` (qualità), `claude-haiku-4-5` (eco)
        - Gemini : `gemini-3-pro-preview` (qualità), `gemini-3-flash-preview` (eco)
    - Modalità economica (`--eco`) per utilizzare modelli più rapidi e meno costosi
    - Traduzione di un singolo file (`--file`) senza dover scorrere una directory
    - Nuovo schema di denominazione semplificato : `{base}-{lang}.md`
    - Opzione `--include_model` per mantenere il vecchio formato con il nome del modello
    - Supporto per modelli non elencati con limite di token predefinito (128k)
    - README tradotto in 14 lingue
- **1.5** Miglioramenti :
    - **Aggiornamento delle chiavi API e dei modelli predefiniti :**
        - **OpenAI :** Aggiornamento da `DEFAULT_MODEL_OPENAI` a `"gpt-4o"`.
        - **Mistral AI :** Aggiornamento da `DEFAULT_MODEL_MISTRAL` a `"mistral-large-latest"`.
        - **Claude di Anthropic :** Aggiunta di `DEFAULT_ANTHROPIC_API_KEY` e aggiornamento da `DEFAULT_MODEL_CLAUDE` a `"claude-3-5-sonnet-20240620"`.
    - **Ottimizzazione dei prompt di traduzione :**
        - I prompt per le traduzioni dirette e le note di traduzione sono stati arricchiti per una migliore chiarezza e efficacia, includendo istruzioni dettagliate sulla preservazione dei metadati e degli elementi di formattazione specifici.
    - **Refactorizzazione del codice :**
        - Sostituzione di `MistralClient` con la classe `Mistral` per l'inizializzazione del client Mistral AI.
        - Riorganizzazione degli import per una migliore leggibilità e manutenzione.
        - Miglioramento nella segmentazione dei testi e nella gestione dei blocchi di codice per preservare il formato originale durante la traduzione.
    - **Gestione dei file di output :**
        - Inversione del modello e della lingua nel nome dei file di output (per esempio, `f"{base}-{args.target_lang}-{args.model}.md"`), facilitando così l'organizzazione e la ricerca delle traduzioni.
    - **Miglioramenti vari :**
        - Pulizia del codice rimuovendo le righe vuote inutili.
        - Piccole modifiche per migliorare la struttura e la leggibilità dello script.
- **1.4** Novità :
    - Supporto dell'API Claude di Anthropic per la traduzione
    - Ottimizzazione dei prompt per una maggiore chiarezza e efficacia
    - Piccoli aggiustamenti per migliorare la manutenzione del codice
- **1.3** Miglioramenti e nuove funzionalità :
    - Migliore gestione dei blocchi di codice
    - Migliore gestione dei file di output
    - Migliorata la rilevazione dei file esistenti
    - Opzione `--force` per forzare la traduzione
    - Inversione del modello e della lingua nel nome del file di output
- **1.2** Correzione del changelog
- **1.1** Aggiunta del supporto per l'API Mistral IA
- **1.0** Versione iniziale - Supporto per l'API OpenAI

**Questo documento è stato tradotto dalla versione fr alla lingua it utilizzando il modello gpt-5-mini. Per più informazioni sul processo di traduzione, consultare https://gitlab.com/jls42/ai-powered-markdown-translator**


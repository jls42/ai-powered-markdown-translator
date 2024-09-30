# Traduttore di Markdown AI-Powered con OpenAI, Mistral AI e Claude d'Anthropic

Questo progetto è uno script Python avanzato che utilizza le API di OpenAI, Mistral AI o Claude d'Anthropic per tradurre file Markdown da una lingua sorgente a una lingua di destinazione. È progettato per essere flessibile e facile da usare, offrendo opzioni aggiuntive come l'aggiunta di una nota di traduzione, la gestione migliorata dei file di output, la rilevazione di file esistenti e il supporto per più lingue e modelli di traduzione.

Per una dimostrazione e spiegazioni dettagliate, visitare [jls42.org](https://jls42.org/) o in versione tradotta: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) e [jls42.org 中文](https://jls42.org/traductions_zh/).

## Caratteristiche Principali

- **Traduzione AI-Powered**: Utilizza le ultime tecnologie di IA per la traduzione dei tuoi documenti con OpenAI, Mistral AI o Claude d'Anthropic.
- **Supporto Multilingue**: Traduci i tuoi documenti in più lingue con supporto per diversi modelli di linguaggio.
- **Segmentazione Intelligente**: Gestisci efficacemente i testi lunghi grazie a una segmentazione automatizzata.
- **Nota di Traduzione**: Aggiungi automaticamente una nota di traduzione per informare i lettori sul processo utilizzato.
- **Gestione Migliorata dei File di Output**: Verifica se una traduzione esiste già prima di lanciare la traduzione.
- **Rilevazione di File Esistenti Migliorata**: Cerca file corrispondenti al nome di base del file originale e alla lingua di destinazione.
- **Flessibile ed Estendibile**: Il codice è strutturato per consentire una facile aggiunta di nuove funzionalità.

## Prerequisiti

- Python 3.6 o versione successiva.
- Una chiave API valida per OpenAI, Mistral AI o Claude d'Anthropic.

## Installazione

1. Clona il repository Git:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. Installa le dipendenze necessarie:
```
pip install -r requirements.txt
```

## Configurazione

Configura il tuo ambiente impostando le variabili d'ambiente per le chiavi API necessarie:

- **OpenAI**:
    ```
    export OPENAI_API_KEY='la-tua-chiave-api-openai'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='la-tua-chiave-api-mistral'
    ```
- **Claude d'Anthropic**:
    ```
    export ANTHROPIC_API_KEY='la-tua-chiave-api-anthropic'
    ```

## Utilizzo

Lo script offre diverse opzioni per personalizzare il processo di traduzione:

### Opzioni Generali

- `--source_dir`: Directory contenente i file Markdown da tradurre.
- `--target_dir`: Directory di destinazione per i file tradotti.
- `--model`: Modello di traduzione GPT da utilizzare. Il modello predefinito dipende dall'API selezionata.
- `--source_lang`: Lingua sorgente dei documenti. Importante soprattutto per l'aggiunta di note di traduzione.
- `--target_lang`: Lingua di destinazione per la traduzione. Predefinito è l'inglese.
- `--force`: Forza la traduzione anche se una traduzione esiste già per il file.

### Opzioni API Specifiche

- `--use_mistral`: Utilizza l'API Mistral AI per la traduzione.
- `--use_claude`: Utilizza l'API Claude d'Anthropic per la traduzione.
- `--add_translation_note`: Aggiungi una nota di traduzione al contenuto tradotto, specificando il metodo e gli strumenti utilizzati.

### Esempi di Utilizzo

- Tradurre dal francese all'inglese con OpenAI, aggiungendo una nota di traduzione:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Tradurre dal francese allo spagnolo con Mistral AI, senza nota di traduzione:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Autore

Julien LE SAUX  
Email: contact@jls42.org

## Licenza

Questo progetto è sotto licenza GNU GENERAL PUBLIC LICENSE Versione 3, 29 Giugno 2007. Vedere il file [LICENSE](LICENSE) per maggiori dettagli.

**Questo documento è stato tradotto dalla versione fr alla lingua it utilizzando il modello gpt-4o. Per maggiori informazioni sul processo di traduzione, consultare https://gitlab.com/jls42/ai-powered-markdown-translator.**


# Traduttore di Markdown basato su IA con OpenAI, Mistral AI e Claude di Anthropic

Questo progetto è uno script Python avanzato che utilizza le API di OpenAI, Mistral AI o Claude di Anthropic per tradurre file Markdown da una lingua di origine a una lingua di destinazione. È progettato per essere flessibile e facile da usare, offrendo opzioni aggiuntive come l'aggiunta di una nota di traduzione, la gestione migliorata dei file di output, il rilevamento di file esistenti e il supporto per più lingue e modelli di traduzione.

Per una dimostrazione e spiegazioni dettagliate, visita [jls42.org](https://jls42.org/) o in versione tradotta: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) e [jls42.org 中文](https://jls42.org/traductions_zh/).

## Caratteristiche principali

- **Traduzione basata su IA**: Utilizza le più recenti tecnologie di IA per tradurre i tuoi documenti con OpenAI, Mistral AI o Claude di Anthropic.
- **Supporto multilingue**: Traduci i tuoi documenti in più lingue con supporto per diversi modelli linguistici.
- **Segmentazione intelligente**: Gestisci efficacemente testi lunghi grazie alla segmentazione automatizzata.
- **Nota di traduzione**: Aggiungi automaticamente una nota di traduzione per informare i lettori sul processo utilizzato.
- **Gestione migliorata dei file di output**: Verifica se una traduzione esiste già prima di avviare la traduzione.
- **Rilevamento migliorato di file esistenti**: Cerca file corrispondenti al nome base del file originale e alla lingua di destinazione.
- **Flessibile ed estensibile**: Il codice è strutturato per consentire una facile aggiunta di nuove funzionalità.

## Prerequisiti

- Python 3.6 o versione successiva.
- Una chiave API valida per OpenAI, Mistral AI o Claude di Anthropic.

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
- **Claude di Anthropic**:
    ```
    export ANTHROPIC_API_KEY='la-tua-chiave-api-anthropic'
    ```

## Utilizzo

Lo script offre diverse opzioni per personalizzare il processo di traduzione:

### Opzioni generali

- `--source_dir`: Directory contenente i file Markdown da tradurre.
- `--target_dir`: Directory di output per i file tradotti.
- `--model`: Modello di traduzione GPT da utilizzare. Il modello predefinito dipende dall'API selezionata.
- `--source_lang`: Lingua di origine dei documenti. Importante soprattutto per l'aggiunta di note di traduzione.
- `--target_lang`: Lingua di destinazione per la traduzione. Di default è l'inglese.
- `--force`: Forza la traduzione anche se esiste già una traduzione per il file.

### Opzioni specifiche dell'API

- `--use_mistral`: Utilizza l'API Mistral AI per la traduzione.
- `--use_claude`: Utilizza l'API Claude di Anthropic per la traduzione.
- `--add_translation_note`: Aggiungi una nota di traduzione al contenuto tradotto, specificando il metodo e gli strumenti utilizzati.

### Esempi di utilizzo

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

Questo progetto è sotto licenza GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. Vedi il file [LICENSE](LICENSE) per maggiori dettagli.

**Questo documento è stato tradotto dalla versione fr alla lingua it utilizzando il modello claude-3-5-sonnet-20240620. Per maggiori informazioni sul processo di traduzione, consultare https://gitlab.com/jls42/ai-powered-markdown-translator**


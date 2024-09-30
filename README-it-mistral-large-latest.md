# Traduttore di Markdown AI-Powered con OpenAI, Mistral AI e Claude di Anthropic

Questo progetto è uno script Python avanzato che utilizza le API OpenAI, Mistral AI o Claude di Anthropic per tradurre i file Markdown da una lingua di origine a una lingua di destinazione. È progettato per essere flessibile e facile da usare, offrendo opzioni aggiuntive come l'aggiunta di una nota di traduzione, la gestione migliorata dei file di output, la rilevazione dei file esistenti e il supporto di più lingue e modelli di traduzione.

Per una dimostrazione e spiegazioni dettagliate, visitate [jls42.org](https://jls42.org/) o in versione tradotta: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) e [jls42.org 中文](https://jls42.org/traductions_zh/).

## Caratteristiche Principali

- **Traduzione AI-Powered**: Utilizzate le ultime tecnologie di IA per la traduzione dei vostri documenti con OpenAI, Mistral AI o Claude di Anthropic.
- **Supporto Multilingue**: Traducete i vostri documenti in più lingue con supporto per diversi modelli linguistici.
- **Segmentazione Intelligente**: Gestite efficacemente i testi lunghi grazie a una segmentazione automatizzata.
- **Nota di Traduzione**: Aggiungete automaticamente una nota di traduzione per informare i lettori sul processo utilizzato.
- **Gestione Migliorata dei File di Output**: Verificate se una traduzione esiste già prima di avviare la traduzione.
- **Rilevazione dei File Esistenti Migliorata**: Cercate i file corrispondenti al nome base del file originale e alla lingua di destinazione.
- **Flessibile ed Estensibile**: Il codice è strutturato per permettere una facilità di aggiunta di nuove funzionalità.

## Prerequisiti

- Python 3.6 o versione successiva.
- Una chiave API valida per OpenAI, Mistral AI o Claude di Anthropic.

## Installazione

1. Clonate il repository Git:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. Installate le dipendenze necessarie:
```
pip install -r requirements.txt
```

## Configurazione

Configurate il vostro ambiente impostando le variabili d'ambiente per le chiavi API necessarie:

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

### Opzioni Generali

- `--source_dir`: Directory contenente i file Markdown da tradurre.
- `--target_dir`: Directory di output per i file tradotti.
- `--model`: Modello di traduzione GPT da utilizzare. Il modello predefinito dipende dall'API selezionata.
- `--source_lang`: Lingua di origine dei documenti. Importante soprattutto per l'aggiunta di note di traduzione.
- `--target_lang`: Lingua di destinazione per la traduzione. Di default è l'inglese.
- `--force`: Forzare la traduzione anche se esiste già una traduzione per il file.

### Opzioni Specifiche dell'API

- `--use_mistral`: Utilizzare l'API Mistral AI per la traduzione.
- `--use_claude`: Utilizzare l'API Claude di Anthropic per la traduzione.
- `--add_translation_note`: Aggiungere una nota di traduzione al contenuto tradotto, specificando il metodo e gli strumenti utilizzati.

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

Questo progetto è sotto licenza GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. Vedere il file [LICENSE](LICENSE) per ulteriori dettagli.

**'Ce document a été traduit de la version fr vers la langue it en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator'.**


'# AI-Powered Markdown-översättare med OpenAI, Mistral AI och Claude från Anthropic

Detta projekt är ett avancerat Python-skript som använder API:er från OpenAI, Mistral AI eller Claude från Anthropic för att översätta Markdown-filer från ett källspråk till ett målspråk. Det är utformat för att vara flexibelt och enkelt att använda, och erbjuder ytterligare alternativ som att lägga till en översättningsnot, förbättrad hantering av utdatafiler, identifiering av existerande filer och stöd för flera språk och översättningsmodeller.

För en demonstration och detaljerade förklaringar, besök [jls42.org](https://jls42.org/) eller i översatt version: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) och [jls42.org 中文](https://jls42.org/traductions_zh/).

## Huvudfunktioner

- **AI-Powered Översättning**: Använd de senaste AI-teknikerna för översättning av dina dokument med OpenAI, Mistral AI eller Claude från Anthropic.
- **Flerspråkigt Stöd**: Översätt dina dokument till flera språk med stöd för olika språkmodeller.
- **Intelligent Segmentering**: Hantera långa texter effektivt med automatisk segmentering.
- **Översättningsnot**: Lägg automatiskt till en översättningsnot för att informera läsarna om den använda processen.
- **Förbättrad Hantering av Utdatafiler**: Kontrollera om en översättning redan finns innan du startar översättningen.
- **Förbättrad Identifiering av Existerande Filer**: Sök efter filer som matchar basnamnet på källfilen och målspråket.
- **Flexibel och Utbyggbar**: Koden är strukturerad för att göra det enkelt att lägga till nya funktioner.

## Förutsättningar

- Python 3.6 eller senare version.
- En giltig API-nyckel för OpenAI, Mistral AI eller Claude från Anthropic.

## Installation

1. Klona Git-lagret:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. Installera de nödvändiga beroenden:
```
pip install -r requirements.txt
```

## Konfiguration

Konfigurera din miljö genom att definiera miljövariabler för de nödvändiga API-nycklarna:

- **OpenAI**:
    ```
    export OPENAI_API_KEY='din-openai-api-nyckel'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='din-mistral-api-nyckel'
    ```
- **Claude från Anthropic**:
    ```
    export ANTHROPIC_API_KEY='din-anthropic-api-nyckel'
    ```

## Användning

Skriptet erbjuder flera alternativ för att anpassa översättningsprocessen:

### Allmänna Alternativ

- `--source_dir`: Katalog som innehåller Markdown-filer att översätta.
- `--target_dir`: Utdata-katalog för översatta filer.
- `--model`: GPT-översättningsmodell att använda. Standardmodellen beror på det valda API:et.
- `--source_lang`: Källspråk för dokumenten. Viktigt särskilt för tillägg av översättningsnoter.
- `--target_lang`: Målspråk för översättningen. Standard är engelska.
- `--force`: Tvinga översättningen även om en översättning redan finns för filen.

### API-Specifika Alternativ

- `--use_mistral`: Använd Mistral AI API för översättning.
- `--use_claude`: Använd Claude från Anthropic API för översättning.
- `--add_translation_note`: Lägg till en översättningsnot till det översatta innehållet, specificerande metoden och verktygen som användes.

### Exempel på Användning

- Översätt från franska till engelska med OpenAI, med tillägg av översättningsnot:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Översätt från franska till spanska med Mistral AI, utan översättningsnot:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Författare

Julien LE SAUX
Email: contact@jls42.org

## Licens

Detta projekt är licensierat under GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. Se filen [LICENSE](LICENSE) för mer detaljer.

**Ce document a été traduit de la version fr vers la langue sv en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator**


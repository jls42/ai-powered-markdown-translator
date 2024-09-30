# Markdown AI-driven översättare med OpenAI, Mistral AI och Claude d'Anthropic

Detta projekt är ett avancerat Python-skript som använder OpenAI, Mistral AI eller Claude d'Anthropic API:er för att översätta Markdown-filer från ett källspråk till ett målspråk. Det är utformat för att vara flexibelt och lätt att använda, och erbjuder ytterligare alternativ som att lägga till en översättningsanteckning, förbättrad hantering av utdatafiler, upptäckt av befintliga filer och stöd för flera språk och översättningsmodeller.

För en demonstration och detaljerade förklaringar, besök [jls42.org](https://jls42.org/) eller i översatt version: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) och [jls42.org 中文](https://jls42.org/traductions_zh/).

## Huvudfunktioner

- **AI-driven Översättning**: Använd den senaste AI-tekniken för att översätta dina dokument med OpenAI, Mistral AI eller Claude d'Anthropic.
- **Flerspråkssupport**: Översätt dina dokument till flera språk med stöd för olika språkmodeller.
- **Intelligent Segmentering**: Hantera långa texter effektivt genom automatiserad segmentering.
- **Översättningsanteckning**: Lägg automatiskt till en översättningsanteckning för att informera läsarna om den använda processen.
- **Förbättrad Hantering av Utdatafiler**: Kontrollera om en översättning redan finns innan översättningen påbörjas.
- **Förbättrad Upptäckt av Befintliga Filer**: Sök efter filer som matchar ursprungsfilens baskt och målspråk.
- **Flexibel och Utbyggbar**: Koden är strukturerad för att enkelt kunna lägga till nya funktioner.

## Förutsättningar

- Python 3.6 eller senare version.
- En giltig API-nyckel för OpenAI, Mistral AI eller Claude d'Anthropic.

## Installation

1. Klona Git-förvaret:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. Installera nödvändiga beroenden:
```
pip install -r requirements.txt
```

## Konfiguration

Konfigurera din miljö genom att ställa in miljövariabler för de nödvändiga API-nycklarna:

- **OpenAI**:
    ```
    export OPENAI_API_KEY='din-openai-api-nyckel'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='din-mistral-api-nyckel'
    ```
- **Claude d'Anthropic**:
    ```
    export ANTHROPIC_API_KEY='din-anthropic-api-nyckel'
    ```

## Användning

Skriptet erbjuder flera alternativ för att anpassa översättningsprocessen:

### Generella Alternativ

- `--source_dir`: Katalog som innehåller Markdown-filerna som ska översättas.
- `--target_dir`: Utgångskatalog för de översatta filerna.
- `--model`: GPT-översättningsmodell att använda. Standardmodellen beror på valt API.
- `--source_lang`: Källspråk för dokumenten. Viktigt, särskilt för att lägga till översättningsanteckningar.
- `--target_lang`: Målspråk för översättningen. Standard är engelska.
- `--force`: Tvinga översättning även om en översättning redan finns för filen.

### Specifika API-alternativ

- `--use_mistral`: Använd Mistral AI API för översättning.
- `--use_claude`: Använd Claude d'Anthropic API för översättning.
- `--add_translation_note`: Lägg till en översättningsanteckning till det översatta innehållet som specificerar metoden och verktygen som använts.

### Användningsexempel

- Översätt från franska till engelska med OpenAI, inklusive en översättningsanteckning:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Översätt från franska till spanska med Mistral AI, utan översättningsanteckning:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Författare

Julien LE SAUX  
Email: contact@jls42.org

## Licens

Detta projekt är licensierat under GNU GENERAL PUBLIC LICENSE Version 3, 29 juni 2007. Se filen [LICENSE](LICENSE) för mer information.

**Detta dokument har översatts från version fr till språk sv med hjälp av modellen gpt-4o. För mer information om översättningsprocessen, se https://gitlab.com/jls42/ai-powered-markdown-translator**


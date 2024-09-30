# AI-driven Markdown-översättare med OpenAI, Mistral AI och Claude från Anthropic

Detta projekt är ett avancerat Python-skript som använder OpenAI-, Mistral AI- eller Claude från Anthropic-API:er för att översätta Markdown-filer från ett källspråk till ett målspråk. Det är utformat för att vara flexibelt och enkelt att använda, med ytterligare alternativ som att lägga till en översättningsanteckning, förbättrad hantering av utdatafiler, detektering av befintliga filer och stöd för flera språk och översättningsmodeller.

För en demonstration och detaljerade förklaringar, besök [jls42.org](https://jls42.org/) eller i översatta versioner: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) och [jls42.org 中文](https://jls42.org/traductions_zh/).

## Huvudfunktioner

- **AI-driven översättning**: Använd den senaste AI-teknologin för att översätta dina dokument med OpenAI, Mistral AI eller Claude från Anthropic.
- **Flerspråkigt stöd**: Översätt dina dokument till flera språk med stöd för olika språkmodeller.
- **Intelligent segmentering**: Hantera långa texter effektivt genom automatiserad segmentering.
- **Översättningsanteckning**: Lägg automatiskt till en översättningsanteckning för att informera läsarna om den använda processen.
- **Förbättrad hantering av utdatafiler**: Kontrollera om en översättning redan existerar innan översättningen startas.
- **Förbättrad detektering av befintliga filer**: Sök efter filer som matchar originalfilens basnamn och målspråk.
- **Flexibel och utbyggbar**: Koden är strukturerad för att möjliggöra enkel tilläggning av nya funktioner.

## Förutsättningar

- Python 3.6 eller senare.
- En giltig API-nyckel för OpenAI, Mistral AI eller Claude från Anthropic.

## Installation

1. Klona Git-repositoryt:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. Installera nödvändiga beroenden:
```
pip install -r requirements.txt
```

## Konfiguration

Konfigurera din miljö genom att ställa in miljövariabler för nödvändiga API-nycklar:

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

### Allmänna alternativ

- `--source_dir`: Katalog som innehåller Markdown-filer att översätta.
- `--target_dir`: Utdatakatalog för översatta filer.
- `--model`: GPT-översättningsmodell att använda. Standardmodellen beror på vald API.
- `--source_lang`: Källspråk för dokumenten. Viktigt särskilt för att lägga till översättningsanteckningar.
- `--target_lang`: Målspråk för översättningen. Standard är engelska.
- `--force`: Tvinga översättning även om en översättning redan finns för filen.

### API-specifika alternativ

- `--use_mistral`: Använd Mistral AI API för översättning.
- `--use_claude`: Använd Claude från Anthropic API för översättning.
- `--add_translation_note`: Lägg till en översättningsanteckning till det översatta innehållet, specificerande metod och verktyg som använts.

### Användningsexempel

- Översätt från franska till engelska med OpenAI, lägga till en översättningsanteckning:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Översätt från franska till spanska med Mistral AI, utan översättningsanteckning:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Författare

Julien LE SAUX  
E-post: contact@jls42.org

## Licens

Detta projekt är licensierat under GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. Se [LICENSE](LICENSE)-filen för mer information.

**Detta dokument har översatts från fr-versionen till sv-språket med hjälp av modellen claude-3-5-sonnet-20240620. För mer information om översättningsprocessen, se https://gitlab.com/jls42/ai-powered-markdown-translator**


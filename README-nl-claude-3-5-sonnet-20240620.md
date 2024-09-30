# AI-Powered Markdown-vertaler met OpenAI, Mistral AI en Claude van Anthropic

Dit project is een geavanceerd Python-script dat de API's van OpenAI, Mistral AI of Claude van Anthropic gebruikt om Markdown-bestanden van een brontaal naar een doeltaal te vertalen. Het is ontworpen om flexibel en gemakkelijk te gebruiken te zijn, met extra opties zoals het toevoegen van een vertaalnotitie, verbeterd beheer van uitvoerbestanden, detectie van bestaande bestanden, en ondersteuning voor meerdere talen en vertaalmodellen.

Voor een demonstratie en gedetailleerde uitleg, bezoek [jls42.org](https://jls42.org/) of in vertaalde versie: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) en [jls42.org 中文](https://jls42.org/traductions_zh/).

## Hoofdkenmerken

- **AI-Powered vertaling**: Gebruik de nieuwste AI-technologieën voor de vertaling van uw documenten met OpenAI, Mistral AI of Claude van Anthropic.
- **Meertalige ondersteuning**: Vertaal uw documenten naar meerdere talen met ondersteuning voor verschillende taalmodellen.
- **Intelligente segmentatie**: Beheer lange teksten efficiënt dankzij geautomatiseerde segmentatie.
- **Vertaalnotitie**: Voeg automatisch een vertaalnotitie toe om lezers te informeren over het gebruikte proces.
- **Verbeterd beheer van uitvoerbestanden**: Controleer of er al een vertaling bestaat voordat de vertaling wordt gestart.
- **Verbeterde detectie van bestaande bestanden**: Zoek naar bestanden die overeenkomen met de basisnaam van het originele bestand en de doeltaal.
- **Flexibel en uitbreidbaar**: De code is gestructureerd om gemakkelijk nieuwe functies toe te voegen.

## Vereisten

- Python 3.6 of hoger.
- Een geldige API-sleutel voor OpenAI, Mistral AI of Claude van Anthropic.

## Installatie

1. Kloon de Git-repository:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. Installeer de benodigde afhankelijkheden:
```
pip install -r requirements.txt
```

## Configuratie

Configureer uw omgeving door de omgevingsvariabelen in te stellen voor de benodigde API-sleutels:

- **OpenAI**:
    ```
    export OPENAI_API_KEY='uw-openai-api-sleutel'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='uw-mistral-api-sleutel'
    ```
- **Claude van Anthropic**:
    ```
    export ANTHROPIC_API_KEY='uw-anthropic-api-sleutel'
    ```

## Gebruik

Het script biedt verschillende opties om het vertaalproces aan te passen:

### Algemene opties

- `--source_dir`: Directory met de te vertalen Markdown-bestanden.
- `--target_dir`: Uitvoerdirectory voor de vertaalde bestanden.
- `--model`: Te gebruiken GPT-vertaalmodel. Het standaardmodel hangt af van de geselecteerde API.
- `--source_lang`: Brontaal van de documenten. Belangrijk vooral voor het toevoegen van vertaalnotities.
- `--target_lang`: Doeltaal voor de vertaling. Standaard is dit Engels.
- `--force`: Forceer de vertaling zelfs als er al een vertaling bestaat voor het bestand.

### API-specifieke opties

- `--use_mistral`: Gebruik de Mistral AI API voor de vertaling.
- `--use_claude`: Gebruik de Claude API van Anthropic voor de vertaling.
- `--add_translation_note`: Voeg een vertaalnotitie toe aan de vertaalde inhoud, met vermelding van de gebruikte methode en tools.

### Gebruiksvoorbeelden

- Vertalen van Frans naar Engels met OpenAI, met toevoeging van een vertaalnotitie:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Vertalen van Frans naar Spaans met Mistral AI, zonder vertaalnotitie:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Auteur

Julien LE SAUX  
E-mail: contact@jls42.org

## Licentie

Dit project is gelicentieerd onder de GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. Zie het bestand [LICENSE](LICENSE) voor meer details.

**Dit document is vertaald van de fr versie naar de nl taal met behulp van het claude-3-5-sonnet-20240620 model. Voor meer informatie over het vertaalproces, zie https://gitlab.com/jls42/ai-powered-markdown-translator.**


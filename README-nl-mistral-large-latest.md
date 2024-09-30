'# AI-gekracht Markdown-vertaler met OpenAI, Mistral AI en Claude van Anthropic

Dit project is een geavanceerd Python-script dat de API's van OpenAI, Mistral AI of Claude van Anthropic gebruikt om Markdown-bestanden van een bron taal naar een doeltaal te vertalen. Het is ontworpen om flexibel en eenvoudig te gebruiken te zijn, met extra opties zoals het toevoegen van een vertaalnotitie, verbeterde bestandenbeheer, detectie van bestaande bestanden, en ondersteuning voor meerdere talen en vertaalmodellen.

Voor een demonstratie en gedetailleerde uitleg, bezoek [jls42.org](https://jls42.org/) of in vertaalde versie: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) en [jls42.org 中文](https://jls42.org/traductions_zh/).

## Hoofdkenmerken

- **AI-gekracht Vertaling**: Gebruik de nieuwste AI-technologieën voor het vertalen van uw documenten met OpenAI, Mistral AI of Claude van Anthropic.
- **Multilinguale Ondersteuning**: Vertaal uw documenten in meerdere talen met ondersteuning voor verschillende taalmodellen.
- **Intelligente Segmentatie**: Beheer lange teksten efficiënt dankzij automatische segmentatie.
- **Vertaalnotitie**: Voeg automatisch een vertaalnotitie toe om lezers te informeren over het gebruikte proces.
- **Verbeterd Bestandenbeheer**: Controleer of een vertaling al bestaat voordat u de vertaling start.
- **Verbeterde Detectie van Bestaande Bestanden**: Zoek naar bestanden die overeenkomen met de basISnaam van het oorspronkelijke bestand en de doeltaal.
- **Flexibel en Uitbreidbaar**: De code is gestructureerd om het eenvoudig toe te voegen van nieuwe functionaliteiten.

## Vereisten

- Python 3.6 of hoger.
- Een geldige API-sleutel voor OpenAI, Mistral AI of Claude van Anthropic.

## Installatie

1. Kloon de Git-repo:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. Installeer de benodigde afhankelijkheden:
```
pip install -r requirements.txt
```

## Configuratie

Configureer uw omgeving door de omgevingsvariabelen voor de benodigde API-sleutels in te stellen:

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

### Algemene Opties

- `--source_dir`: Directory met Markdown-bestanden die moeten worden vertaald.
- `--target_dir`: Uitvoerdirectory voor vertaalde bestanden.
- `--model`: Te gebruiken GPT-vertalingsmodel. Het standaardmodel hangt af van de geselecteerde API.
- `--source_lang`: Brontaal van de documenten. Belangrijk vooral voor het toevoegen van vertaalnotities.
- `--target_lang`: Doeltaal voor de vertaling. Standaard is dit Engels.
- `--force`: Vertaling forceren, ook al bestaat er al een vertaling voor het bestand.

### API-specifieke Opties

- `--use_mistral`: Gebruik de Mistral AI-API voor de vertaling.
- `--use_claude`: Gebruik de Claude van Anthropic-API voor de vertaling.
- `--add_translation_note`: Voeg een vertaalnotitie toe aan de vertaalde inhoud, waarbij de methode en de gebruikte hulpmiddelen worden gespecificeerd.

### Voorbeelden van Gebruik

- Vertalen van Frans naar Engels met OpenAI, met een vertaalnotitie:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Vertalen van Frans naar Spaans met Mistral AI, zonder vertaalnotitie:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Auteur

Julien LE SAUX
Email: contact@jls42.org

## Licentie

Dit project valt onder de GNU GENERAL PUBLIC LICENSE Version 3, 29 juni 2007. Zie het bestand [LICENSE](LICENSE) voor meer details.'

**Ce document a été traduit de la version fr vers la langue nl en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator.**


# Markdown AI-aangedreven vertaler met OpenAI, Mistral AI en Claude d'Anthropic

Dit project is een geavanceerd Python-script dat de OpenAI-, Mistral AI- of Claude d'Anthropic-API's gebruikt om Markdown-bestanden van een brontaal naar een doeltaal te vertalen. Het is ontworpen om flexibel en gebruiksvriendelijk te zijn en biedt extra opties zoals het toevoegen van een vertaalaantekening, verbeterd beheer van uitvoerbestanden, detectie van bestaande bestanden, en ondersteuning voor meerdere talen en vertaalmodellen.

Voor een demonstratie en gedetailleerde uitleg, bezoek [jls42.org](https://jls42.org/) of in vertaalde versie: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) en [jls42.org 中文](https://jls42.org/traductions_zh/).

## Belangrijkste Kenmerken

- **AI-aangedreven Vertaling**: Gebruik de nieuwste AI-technologieën voor de vertaling van uw documenten met OpenAI, Mistral AI of Claude d'Anthropic.
- **Meertalige Ondersteuning**: Vertaal uw documenten in meerdere talen met ondersteuning voor verschillende taalmodellen.
- **Intelligente Segmentatie**: Beheer lange teksten efficiënt met geautomatiseerde segmentatie.
- **Vertaalaantekening**: Voeg automatisch een vertaalaantekening toe om lezers te informeren over het gebruikte proces.
- **Verbeterd Beheer van Uitvoerbestanden**: Controleer of er al een vertaling bestaat voordat u de vertaling start.
- **Verbeterde Detectie van Bestaande Bestanden**: Zoek naar bestanden die overeenkomen met de basisnaam van het oorspronkelijke bestand en de doeltaal.
- **Flexibel en Uitbreidbaar**: De code is gestructureerd om eenvoudig nieuwe functies toe te voegen.

## Vereisten

- Python 3.6 of later.
- Een geldige API-sleutel voor OpenAI, Mistral AI of Claude d'Anthropic.

## Installatie

1. Clone de Git-repository:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. Installeer de benodigde afhankelijkheden:
```
pip install -r requirements.txt
```

## Configuratie

Configureer uw omgeving door omgevingsvariabelen in te stellen voor de benodigde API-sleutels:

- **OpenAI**:
    ```
    export OPENAI_API_KEY='uw-openai-api-sleutel'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='uw-mistral-api-sleutel'
    ```
- **Claude d'Anthropic**:
    ```
    export ANTHROPIC_API_KEY='uw-anthropic-api-sleutel'
    ```

## Gebruik

Het script biedt verschillende opties om het vertaalproces aan te passen:

### Algemene Opties

- `--source_dir`: Directory met de Markdown-bestanden die vertaald moeten worden.
- `--target_dir`: Uitvoermap voor de vertaalde bestanden.
- `--model`: GPT-vertaalmodel om te gebruiken. Het standaardmodel hangt af van de geselecteerde API.
- `--source_lang`: Brontaal van de documenten. Belangrijk voor het toevoegen van vertaalaantekeningen.
- `--target_lang`: Doeltaal voor de vertaling. Standaard is Engels.
- `--force`: Forceren van de vertaling zelfs als er al een vertaling voor het bestand bestaat.

### Specifieke API-opties

- `--use_mistral`: Gebruik de Mistral AI API voor de vertaling.
- `--use_claude`: Gebruik de Claude d'Anthropic API voor de vertaling.
- `--add_translation_note`: Voeg een vertaalaantekening toe aan de vertaalde inhoud, waarin de gebruikte methode en hulpmiddelen worden vermeld.

### Voorbeelden van Gebruik

- Vertaal van Frans naar Engels met OpenAI, met het toevoegen van een vertaalaantekening:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Vertaal van Frans naar Spaans met Mistral AI, zonder vertaalaantekening:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Auteur

Julien LE SAUX  
Email: contact@jls42.org

## Licentie

Dit project is gelicentieerd onder de GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. Zie het bestand [LICENSE](LICENSE) voor meer details.

**Dit document is vertaald van de versie fr naar de taal nl met behulp van het model gpt-4o. Voor meer informatie over het vertaalproces, raadpleeg https://gitlab.com/jls42/ai-powered-markdown-translator**


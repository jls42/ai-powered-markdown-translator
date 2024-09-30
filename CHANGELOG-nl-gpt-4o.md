### Changelog

- **1.0** Initiële versie - Ondersteuning van de OpenAI API
- **1.1** Toevoeging van ondersteuning voor de Mistral AI API
- **1.2** Fix van de changelog
- **1.3** Verbeteringen en nieuwe functies:
    - Verbeterde verwerking van codeblokken
    - Verbeterde verwerking van uitvoerbestanden
    - Verbeterde detectie van bestaande bestanden
    - Optie `--force` om de vertaling af te dwingen
    - Omkering van het model en de taal in de naam van het uitvoerbestand
- **1.4** Nieuwigheden:
    - Ondersteuning van de Claude van Anthropic API voor vertaling
    - Optimalisatie van prompts voor meer duidelijkheid en efficiëntie
    - Kleine aanpassingen voor een betere codeonderhoud
- **1.5** Verbeteringen:
    - **Bijgewerkte standaard API-sleutels en modellen:**
        - **OpenAI:** Bijgewerkt naar `DEFAULT_MODEL_OPENAI` naar `"gpt-4o"`.
        - **Mistral AI:** Bijgewerkt naar `DEFAULT_MODEL_MISTRAL` naar `"mistral-large-latest"`.
        - **Claude van Anthropic:** Toevoeging van `DEFAULT_ANTHROPIC_API_KEY` en bijgewerkt naar `DEFAULT_MODEL_CLAUDE` naar `"claude-3-5-sonnet-20240620"`.
    - **Optimalisatie van vertaalprompts:**
        - De prompts voor directe vertalingen en vertaalnotities zijn verrijkt voor betere duidelijkheid en efficiëntie, inclusief gedetailleerde instructies over het bewaren van metadata en specifieke opmaak elementen.
    - **Code refactoring:**
        - Vervanging van `MistralClient` door de `Mistral` class voor de initialisatie van de Mistral AI client.
        - Herorganisatie van imports voor betere leesbaarheid en onderhoud.
        - Verbetering van tekstsegmentatie en verwerking van codeblokken om de oorspronkelijke opmaak tijdens de vertaling te behouden.
    - **Verwerking van uitvoerbestanden:**
        - Omkering van het model en de taal in de naam van de uitvoerbestanden (bijvoorbeeld, `f"{base}-{args.target_lang}-{args.model}.md"`), waardoor organisatie en het zoeken naar vertalingen wordt vergemakkelijkt.
    - **Diverse verbeteringen:**
        - Opschoning van de code door het verwijderen van onnodige lege regels.
        - Kleine aanpassingen voor een betere structuur en leesbaarheid van het script.

**Dit document is vertaald van de fr-versie naar de nl-taal met behulp van het model gpt-4o. Voor meer informatie over het vertaalproces, zie https://gitlab.com/jls42/ai-powered-markdown-translator**


### Changelog

- **1.0** Initiële versie - Ondersteuning voor OpenAI API
- **1.1** Toevoeging van ondersteuning voor Mistral AI API
- **1.2** Fix van de changelog
- **1.3** Verbeteringen en nieuwe functionaliteiten:
    - Verbeterde verwerking van codeblokken
    - Verbeterd beheer van uitvoerbestanden
    - Verbeterde detectie van bestaande bestanden
    - Optie `--force` om vertaling te forceren
    - Omkering van model en taal in de naam van het uitvoerbestand
- **1.4** Nieuwigheden:
    - Ondersteuning voor Anthropic's Claude API voor vertaling
    - Optimalisatie van prompts voor verhoogde duidelijkheid en efficiëntie
    - Kleine aanpassingen om codeonderhoud te verbeteren
- **1.5** Verbeteringen:
    - **Update van API-sleutels en standaardmodellen:**
        - **OpenAI:** Update van `DEFAULT_MODEL_OPENAI` naar `"gpt-4o"`.
        - **Mistral AI:** Update van `DEFAULT_MODEL_MISTRAL` naar `"mistral-large-latest"`.
        - **Claude van Anthropic:** Toevoeging van `DEFAULT_ANTHROPIC_API_KEY` en update van `DEFAULT_MODEL_CLAUDE` naar `"claude-3-5-sonnet-20240620"`.
    - **Optimalisatie van vertaalprompts:**
        - De prompts voor directe vertalingen en vertaalnotities zijn verrijkt voor betere duidelijkheid en efficiëntie, inclusief gedetailleerde instructies over het behoud van metadata en specifieke opmaakelementen.
    - **Code refactoring:**
        - Vervanging van `MistralClient` door de `Mistral` klasse voor de initialisatie van de Mistral AI-client.
        - Reorganisatie van imports voor betere leesbaarheid en onderhoud.
        - Verbetering van tekstsegmentatie en verwerking van codeblokken om de originele opmaak te behouden tijdens vertaling.
    - **Beheer van uitvoerbestanden:**
        - Omkering van model en taal in de naam van uitvoerbestanden (bijvoorbeeld `f"{base}-{args.target_lang}-{args.model}.md"`), wat de organisatie en het zoeken naar vertalingen vergemakkelijkt.
    - **Diverse verbeteringen:**
        - Opschoning van code door het verwijderen van onnodige lege regels.
        - Kleine aanpassingen om de structuur en leesbaarheid van het script te verbeteren.

**Dit document werd vertaald van de fr versie naar nl met behulp van het claude-3-5-sonnet-20240620 model. Voor meer informatie over het vertaalproces, zie https://gitlab.com/jls42/ai-powered-markdown-translator**


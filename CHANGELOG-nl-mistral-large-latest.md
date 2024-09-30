### Changelog

- **1.0** Initiële versie - Ondersteuning voor OpenAI API
- **1.1** Toevoeging van ondersteuning voor Mistral IA API
- **1.2** Fix van het changelog
- **1.3** Verbeteringen en nieuwe functionaliteiten:
    - Verbeterde beheer van codeblokken
    - Verbeterde beheer van uitvoerbestanden
    - Verbeterde detectie van bestaande bestanden
    - Optie `--force` om vertaling af te dwingen
    - Omkering van het model en de taal in de naam van het uitvoerbestand
- **1.4** Nieuwe functies:
    - Ondersteuning voor Anthropic's Claude API voor vertaling
    - Optimalisatie van prompts voor meer helderheid en efficiëntie
    - Kleine aanpassingen voor verbetering van codeonderhoud
- **1.5** Verbeteringen:
    - **Update van API-sleutels en standaardmodellen:**
        - **OpenAI:** Update van `DEFAULT_MODEL_OPENAI` naar `"gpt-4o"`.
        - **Mistral AI:** Update van `DEFAULT_MODEL_MISTRAL` naar `"mistral-large-latest"`.
        - **Anthropic's Claude:** Toevoeging van `DEFAULT_ANTHROPIC_API_KEY` en update van `DEFAULT_MODEL_CLAUDE` naar `"claude-3-5-sonnet-20240620"`.
    - **Optimalisatie van vertaalprompts:**
        - De prompts voor directe vertalingen en vertaalnotities zijn verrijkt voor betere helderheid en efficiëntie, inclusief gedetailleerde instructies over het behoud van metadata en specifieke opmaakelementen.
    - **Refactorisatie van de code:**
        - Vervanging van `MistralClient` door de klasse `Mistral` voor initialisatie van de Mistral AI-client.
        - Herorganisatie van imports voor betere leesbaarheid en onderhoud.
        - Verbetering van tekstsegmentatie en beheer van codeblokken om de oorspronkelijke opmaak te behouden bij vertaling.
    - **Beheer van uitvoerbestanden:**
        - Omkering van het model en de taal in de namen van uitvoerbestanden (bijvoorbeeld, `f"{base}-{args.target_lang}-{args.model}.md"`), waardoor de organisatie en het zoeken naar vertalingen wordt vergemakkelijkt.
    - **Diverse verbeteringen:**
        - Opschoning van de code door het verwijderen van onnodige lege regels.
        - Kleine aanpassingen voor verbetering van de structuur en leesbaarheid van het script.

**'Dit document is vertaald van de fr-versie naar de nl-taal met behulp van het model mistral-large-latest. Voor meer informatie over het vertaalproces, raadpleeg https://gitlab.com/jls42/ai-powered-markdown-translator'.**


### Changelog

- **1.0** Initial version - Stöd för OpenAI API
- **1.1** Tillägg av stöd för Mistral AI API
- **1.2** Fix av changelog
- **1.3** Förbättringar och nya funktioner:
    - Förbättrad hantering av kodblock
    - Förbättrad hantering av utdatafiler
    - Förbättrad detektion av existerande filer
    - Option `--force` för att tvinga översättning
    - Invertering av modell och språk i namnet på utdatafilen
- **1.4** Nyheter:
    - Stöd för Anthropics Claude API för översättning
    - Optimering av prompts för förbättrad klarhet och effektivitet
    - Mindre justeringar för att förbättra kodunderhållet
- **1.5** Förbättringar:
    - **Uppdatering av API-nycklar och standardmodeller:**
        - **OpenAI:** Uppdatering av `DEFAULT_MODEL_OPENAI` till `"gpt-4o"`.
        - **Mistral AI:** Uppdatering av `DEFAULT_MODEL_MISTRAL` till `"mistral-large-latest"`.
        - **Anthropics Claude:** Tillägg av `DEFAULT_ANTHROPIC_API_KEY` och uppdatering av `DEFAULT_MODEL_CLAUDE` till `"claude-3-5-sonnet-20240620"`.
    - **Optimering av översättningsprompts:**
        - Prompts för direktöversättningar och översättningsnotiser har berikats för bättre klarhet och effektivitet, inklusive detaljerade instruktioner om bevarande av metadata och specifika formateringselement.
    - **Refaktorering av koden:**
        - Ersättning av `MistralClient` med klassen `Mistral` för initialisering av Mistral AI-klienten.
        - Omorganisation av importer för bättre läsbarhet och underhåll.
        - Förbättring av textsegmentering och hantering av kodblock för att bevara originalformatering vid översättning.
    - **Hantering av utdatafiler:**
        - Invertering av modell och språk i namnet på utdatafiler (t.ex. `f"{base}-{args.target_lang}-{args.model}.md"`), vilket underlättar organisation och sökning av översättningar.
    - **Diverse förbättringar:**
        - Rensning av koden genom att ta bort onödiga tomma rader.
        - Mindre justeringar för att förbättra strukturen och läsbarheten i skriptet.

**Ce document a été traduit de la version fr vers la langue sv en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator.**


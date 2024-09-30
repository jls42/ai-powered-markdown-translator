### Ändringslogg

- **1.0** Initial version - Stöd för OpenAI API
- **1.1** Tillägg av stöd för Mistral AI API
- **1.2** Fix av ändringsloggen
- **1.3** Förbättringar och nya funktioner:
    - Förbättrad hantering av kodblock
    - Förbättrad hantering av utdatafiler
    - Förbättrad detektering av befintliga filer
    - Alternativ `--force` för att tvinga översättning
    - Omvänd ordning av modell och språk i utdatafilens namn
- **1.4** Nyheter:
    - Stöd för Anthropics Claude API för översättning
    - Optimering av prompts för ökad tydlighet och effektivitet
    - Mindre justeringar för att förbättra kodunderhållet
- **1.5** Förbättringar:
    - **Uppdatering av API-nycklar och standardmodeller:**
        - **OpenAI:** Uppdatering av `DEFAULT_MODEL_OPENAI` till `"gpt-4o"`.
        - **Mistral AI:** Uppdatering av `DEFAULT_MODEL_MISTRAL` till `"mistral-large-latest"`.
        - **Claude från Anthropic:** Tillägg av `DEFAULT_ANTHROPIC_API_KEY` och uppdatering av `DEFAULT_MODEL_CLAUDE` till `"claude-3-5-sonnet-20240620"`.
    - **Optimering av översättningsprompts:**
        - Prompterna för direkta översättningar och översättningsnoter har förbättrats för ökad tydlighet och effektivitet, inklusive detaljerade instruktioner om bevarande av metadata och specifika formateringselement.
    - **Omfaktorisering av kod:**
        - Ersättning av `MistralClient` med klassen `Mistral` för initialisering av Mistral AI-klienten.
        - Omorganisering av importer för bättre läsbarhet och underhåll.
        - Förbättrad segmentering av texter och hantering av kodblock för att bevara originalformateringen vid översättning.
    - **Hantering av utdatafiler:**
        - Omvänd ordning av modell och språk i namnet på utdatafiler (till exempel `f"{base}-{args.target_lang}-{args.model}.md"`), vilket underlättar organisering och sökning efter översättningar.
    - **Diverse förbättringar:**
        - Rensning av kod genom att ta bort onödiga tomma rader.
        - Mindre justeringar för att förbättra skriptets struktur och läsbarhet.

**Detta dokument har översatts från fr-versionen till sv-språket med hjälp av modellen claude-3-5-sonnet-20240620. För mer information om översättningsprocessen, se https://gitlab.com/jls42/ai-powered-markdown-translator**


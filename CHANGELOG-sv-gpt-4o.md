### Changelog

- **1.0** Initial version - Support för OpenAI API
- **1.1** Lagt till stöd för Mistral IA API
- **1.2** Fix changelog
- **1.3** Förbättringar och nya funktioner:
    - Förbättrad hantering av kodblock
    - Förbättrad hantering av utdatafiler
    - Förbättrad upptäckt av befintliga filer
    - Alternativ `--force` för att tvinga översättning
    - Omvändning av modell och språk i utdatafilnamnet
- **1.4** Nyheter:
    - Stöd för Claude d'Anthropic API för översättning
    - Optimering av prompts för ökad klarhet och effektivitet
    - Mindre justeringar för att förbättra kodunderhållet
- **1.5** Förbättringar:
    - **Uppdatering av API-nycklar och standardmodeller:**
        - **OpenAI:** Uppdatering av `DEFAULT_MODEL_OPENAI` till `"gpt-4o"`.
        - **Mistral AI:** Uppdatering av `DEFAULT_MODEL_MISTRAL` till `"mistral-large-latest"`.
        - **Claude d'Anthropic:** Tillagd `DEFAULT_ANTHROPIC_API_KEY` och uppdatering av `DEFAULT_MODEL_CLAUDE` till `"claude-3-5-sonnet-20240620"`.
    - **Optimering av översättningsprompts:**
        - Prompts för direkta översättningar och översättningsnoter har förbättrats för bättre klarhet och effektivitet, inklusive detaljerade instruktioner om bevarande av metadata och specifika formatteringselement.
    - **Kodrefaktorering:**
        - Ersättning av `MistralClient` med klassen `Mistral` för initiering av Mistral AI-klienten.
        - Organisering av importer för bättre läsbarhet och underhåll.
        - Förbättrad textsegmentering och hantering av kodblock för att bevara originalformatet vid översättning.
    - **Hantering av utdatafiler:**
        - Omvändning av modell och språk i utdatafilnamnen (t.ex. `f"{base}-{args.target_lang}-{args.model}.md"`), vilket underlättar organisation och sökning av översättningar.
    - **Diverse förbättringar:**
        - Rensning av koden genom att ta bort onödiga tomma rader.
        - Mindre justeringar för att förbättra struktur och läsbarhet av skriptet.

**Detta dokument har översatts från versionen fr till språket sv med hjälp av modellen gpt-4o. För mer information om översättningsprocessen, se https://gitlab.com/jls42/ai-powered-markdown-translator.**


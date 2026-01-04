### Ändringslogg

🌍 [Engelska](CHANGELOG-en.md) | [Spanska](CHANGELOG-es.md) | [Kinesiska](CHANGELOG-zh.md) | [Tyska](CHANGELOG-de.md) | [Japanska](CHANGELOG-ja.md) | [Koreanska](CHANGELOG-ko.md) | [Arabiska](CHANGELOG-ar.md) | [Hindi](CHANGELOG-hi.md) | [Italienska](CHANGELOG-it.md) | [Nederländska](CHANGELOG-nl.md) | [Polska](CHANGELOG-pl.md) | [Portugisiska](CHANGELOG-pt.md) | [Rumänska](CHANGELOG-ro.md) | [Svenska](CHANGELOG-sv.md)

- **1.7** Nyheter :
    - Alternativet `--keep_filename` för att bevara det ursprungliga filnamnet vid översättning
    - Stöd för filen `.env` för att ladda API-nycklar automatiskt
    - **Bevarande av inlinekod** : backticks (`` `...` ``) är nu skyddade under översättningen
    - Förbättring av systemprompten :
        - Bättre hantering av citattecken i YAML-frontmatter
        - Skydd av template-variabler `{variable}`
        - Förbud mot översättarnoter som inte efterfrågats
    - Testad framgångsrikt på 364 filer (migration av bloggen jls42.org)
- **1.6** Nyheter :
    - Stöd för Google Gemini API för översättning (`--use_gemini`)
    - Uppdatering av standardmodellerna 2026 :
        - OpenAI : `gpt-5` (kvalitet), `gpt-5-mini` (eco)
        - Claude : `claude-sonnet-4-5` (kvalitet), `claude-haiku-4-5` (eco)
        - Gemini : `gemini-3-pro-preview` (kvalitet), `gemini-3-flash-preview` (eco)
    - Sparläge (`--eco`) för att använda snabbare och billigare modeller
    - Översättning av en enskild fil (`--file`) utan att bläddra igenom en katalog
    - Ny förenklad namngivningsmall : `{base}-{lang}.md`
    - Alternativet `--include_model` för att behålla det gamla formatet med modellnamnet
    - Stöd för icke-listade modeller med standard tokenbegränsning (128k)
    - README översatt till 14 språk
- **1.5** Förbättringar :
    - **Uppdatering av API-nycklar och standardmodeller :**
        - **OpenAI :** Uppdatering från `DEFAULT_MODEL_OPENAI` till `"gpt-4o"`.
        - **Mistral AI :** Uppdatering från `DEFAULT_MODEL_MISTRAL` till `"mistral-large-latest"`.
        - **Claude från Anthropic :** Tillägg av `DEFAULT_ANTHROPIC_API_KEY` och uppdatering av `DEFAULT_MODEL_CLAUDE` till `"claude-3-5-sonnet-20240620"`.
    - **Optimering av översättningsprompter :**
        - Prompterna för direkta översättningar och översättningsanteckningar har berikats för bättre tydlighet och effektivitet, inklusive detaljerade instruktioner om bevarande av metadata och specifika formateringselement.
    - **Refaktorering av koden :**
        - Ersättning av `MistralClient` med klassen `Mistral` för initiering av Mistral AI-klienten.
        - Omarbetning av imports för bättre läsbarhet och underhåll.
        - Förbättrad segmentering av texter och hantering av kodblock för att bevara ursprungligt format vid översättning.
    - **Hantering av utdatafiler :**
        - Inversion av modellen och språket i namnet på utdatafilerna (t.ex. `f"{base}-{args.target_lang}-{args.model}.md"`), vilket underlättar organisering och sökning av översättningar.
    - **Övriga förbättringar :**
        - Rensning av koden genom att ta bort onödiga tomma rader.
        - Smärre justeringar för att förbättra struktur och läsbarhet i skriptet.
- **1.4** Nyheter :
    - Stöd för Anthropic Claude API för översättning
    - Optimering av prompter för ökad tydlighet och effektivitet
    - Smärre justeringar för att förbättra kodunderhållet
- **1.3** Förbättringar och nya funktioner :
    - Förbättrad hantering av kodblock
    - Förbättrad hantering av utdatafiler
    - Förbättrad detektion av befintliga filer
    - Alternativet `--force` för att tvinga översättning
    - Inversion av modellen och språket i utdatafilens namn
- **1.2** Korrigering av changelog
- **1.1** Tillagt stöd för Mistral AI API
- **1.0** Initial version - Stöd för OpenAI API

**Detta dokument har översatts från fr-versionen till sv-språket med hjälp av modellen gpt-5-mini. För mer information om översättningsprocessen, se https://gitlab.com/jls42/ai-powered-markdown-translator**


### Wijzigingen

🌍 [Engels](CHANGELOG-en.md) | [Spaans](CHANGELOG-es.md) | [Chinees](CHANGELOG-zh.md) | [Duits](CHANGELOG-de.md) | [Japans](CHANGELOG-ja.md) | [Koreaans](CHANGELOG-ko.md) | [Arabisch](CHANGELOG-ar.md) | [Hindi](CHANGELOG-hi.md) | [Italiaans](CHANGELOG-it.md) | [Nederlands](CHANGELOG-nl.md) | [Pools](CHANGELOG-pl.md) | [Portugees](CHANGELOG-pt.md) | [Roemeens](CHANGELOG-ro.md) | [Zweeds](CHANGELOG-sv.md)

- **1.7** Nieuwe functies :
    - Optie `--keep_filename` om de originele bestandsnaam te behouden tijdens de vertaling
    - Ondersteuning voor het bestand `.env` om API-sleutels automatisch te laden
    - **Behoud van inline-code** : de backticks (`` `...` ``) zijn nu beschermd tijdens de vertaling
    - Verbetering van het systeemprompt :
        - Betere omgang met aanhalingstekens in de YAML frontmatter
        - Bescherming van templatevariabelen `{variable}`
        - Verbod op ongevraagde vertalersopmerkingen
    - Met succes getest op 364 bestanden (migratie blog jls42.org)
- **1.6** Nieuwe functies :
    - Ondersteuning van de Google Gemini API voor vertaling (`--use_gemini`)
    - Bijgewerkte standaardmodellen 2026 :
        - OpenAI : `gpt-5` (kwaliteit), `gpt-5-mini` (eco)
        - Claude : `claude-sonnet-4-5` (kwaliteit), `claude-haiku-4-5` (eco)
        - Gemini : `gemini-3-pro-preview` (kwaliteit), `gemini-3-flash-preview` (eco)
    - Economiemodus (`--eco`) om snellere en goedkopere modellen te gebruiken
    - Vertaling van een enkel bestand (`--file`) zonder een map te doorzoeken
    - Nieuw vereenvoudigd naamgevingspatroon : `{base}-{lang}.md`
    - Optie `--include_model` om het oude formaat met de modelnaam te behouden
    - Ondersteuning voor niet-geliste modellen met standaard tokenlimiet (128k)
    - README vertaald in 14 talen
- **1.5** Verbeteringen :
    - **Bijwerking van API-sleutels en standaardmodellen :**
        - **OpenAI :** Bijgewerkt van `DEFAULT_MODEL_OPENAI` naar `"gpt-4o"`.
        - **Mistral AI :** Bijgewerkt van `DEFAULT_MODEL_MISTRAL` naar `"mistral-large-latest"`.
        - **Claude van Anthropic :** Toevoeging van `DEFAULT_ANTHROPIC_API_KEY` en bijwerking van `DEFAULT_MODEL_CLAUDE` naar `"claude-3-5-sonnet-20240620"`.
    - **Optimalisatie van de vertaalprompts :**
        - De prompts voor directe vertalingen en vertaalnotities zijn verrijkt voor betere duidelijkheid en efficiëntie, inclusief gedetailleerde instructies over het behoud van metadata en specifieke opmaakelementen.
    - **Refactoring van de code :**
        - Vervanging van `MistralClient` door de klasse `Mistral` voor de initialisatie van de Mistral AI-client.
        - Herstructurering van imports voor betere leesbaarheid en onderhoud.
        - Verbetering van tekstsegmentatie en beheer van codeblokken om de oorspronkelijke opmaak tijdens de vertaling te behouden.
    - **Beheer van uitvoerbestanden :**
        - Omkering van model en taal in de naam van uitvoerbestanden (bijv. `f"{base}-{args.target_lang}-{args.model}.md"`), waardoor organisatie en zoeken van vertalingen wordt vergemakkelijkt.
    - **Verschillende verbeteringen :**
        - Opruimen van code door onnodige lege regels te verwijderen.
        - Kleine aanpassingen om de structuur en leesbaarheid van het script te verbeteren.
- **1.4** Nieuwe functies :
    - Ondersteuning van de Claude API van Anthropic voor vertaling
    - Optimalisatie van prompts voor meer duidelijkheid en efficiëntie
    - Kleine aanpassingen om het onderhoud van de code te verbeteren
- **1.3** Verbeteringen en nieuwe functies :
    - Verbeterd beheer van codeblokken
    - Verbeterd beheer van uitvoerbestanden
    - Verbeterde detectie van bestaande bestanden
    - Optie `--force` om de vertaling te forceren
    - Omkering van model en taal in de naam van het uitvoerbestand
- **1.2** Correctie van changelog
- **1.1** Ondersteuning voor de Mistral AI API toegevoegd
- **1.0** Initiële versie - Ondersteuning van de OpenAI API

**Dit document is vertaald van de fr-versie naar de nl-versie met behulp van het model gpt-5-mini. Voor meer informatie over het vertaalproces, raadpleeg https://gitlab.com/jls42/ai-powered-markdown-translator**


### Jurnal de modificări

🌍 [Franceză](CHANGELOG.md) | [Engleză](CHANGELOG-en.md) | [Spaniolă](CHANGELOG-es.md) | [Chineză](CHANGELOG-zh.md) | [Germană](CHANGELOG-de.md) | [Japoneză](CHANGELOG-ja.md) | [Coreeană](CHANGELOG-ko.md) | [Arabă](CHANGELOG-ar.md) | [Hindi](CHANGELOG-hi.md) | [Italiană](CHANGELOG-it.md) | [Olandeză](CHANGELOG-nl.md) | [Poloneză](CHANGELOG-pl.md) | [Portugheză](CHANGELOG-pt.md) | [Română](CHANGELOG-ro.md) | [Suedeză](CHANGELOG-sv.md)

- **1.7** Noutăți :
    - Opțiunea `--keep_filename` pentru a păstra numele fișierului original în timpul traducerii
    - Suport pentru fișierul `.env` pentru a încărca cheile API automat
    - Păstrarea codului inline : backticks (`` `...` ``) sunt acum protejate în timpul traducerii
    - Îmbunătățire a promptului sistemului :
        - Gestionare mai bună a ghilimelelor în frontmatter YAML
        - Protecția variabilelor template `{variable}`
        - Interzicerea notelor traducătorului necerute
    - Testat cu succes pe 364 de fișiere (migrare blog jls42.org)
- **1.6** Noutăți :
    - Suport pentru API-ul Google Gemini pentru traducere (`--use_gemini`)
    - Actualizare a modelelor implicite 2026 :
        - OpenAI : `gpt-5` (calitate), `gpt-5-mini` (eco)
        - Claude : `claude-sonnet-4-5` (calitate), `claude-haiku-4-5` (eco)
        - Gemini : `gemini-3-pro-preview` (calitate), `gemini-3-flash-preview` (eco)
    - Mod economic (`--eco`) pentru a folosi modele mai rapide și mai ieftine
    - Traducere a unui singur fișier (`--file`) fără a parcurge un director
    - Nou șablon simplificat de denumire : `{base}-{lang}.md`
    - Opțiunea `--include_model` pentru a păstra vechiul format cu numele modelului
    - Suport pentru modele nelistate cu limită implicită de tokens (128k)
    - README tradus în 14 limbi
- **1.5** Îmbunătățiri :
    - **Actualizare a cheilor API și a modelelor implicite :**
        - **OpenAI :** Actualizare de la `DEFAULT_MODEL_OPENAI` la `"gpt-4o"`.
        - **Mistral AI :** Actualizare de la `DEFAULT_MODEL_MISTRAL` la `"mistral-large-latest"`.
        - **Claude de la Anthropic :** Adăugare `DEFAULT_ANTHROPIC_API_KEY` și actualizare de la `DEFAULT_MODEL_CLAUDE` la `"claude-3-5-sonnet-20240620"`.
    - **Optimizarea prompturilor de traducere :**
        - Prompturile pentru traduceri directe și notele de traducere au fost îmbogățite pentru o claritate și eficiență mai bună, incluzând instrucțiuni detaliate privind păstrarea metadatelor și a elementelor de formatare specifice.
    - **Refactorizare a codului :**
        - Înlocuirea `MistralClient` cu clasa `Mistral` pentru inițializarea clientului Mistral AI.
        - Reorganizarea importurilor pentru o lizibilitate și întreținere mai bună.
        - Îmbunătățirea segmentării textelor și gestionării blocurilor de cod pentru a păstra formatul original în timpul traducerii.
    - **Gestionarea fișierelor de ieșire :**
        - Inversarea modelului și a limbii în numele fișierelor de ieșire (de exemplu, `f"{base}-{args.target_lang}-{args.model}.md"`), facilitând organizarea și căutarea traducerilor.
    - **Îmbunătățiri diverse :**
        - Curățarea codului prin eliminarea liniilor goale inutile.
        - Ajustări minore pentru a îmbunătăți structura și lizibilitatea scriptului.
- **1.4** Noutăți :
    - Suport pentru API-ul Claude de la Anthropic pentru traducere
    - Optimizarea prompturilor pentru o claritate și eficiență sporite
    - Ajustări minore pentru a îmbunătăți mentenanța codului
- **1.3** Îmbunătățiri și funcționalități noi :
    - Gestionare îmbunătățită a blocurilor de cod
    - Gestionare îmbunătățită a fișierelor de ieșire
    - Detectare îmbunătățită a fișierelor existente
    - Opțiunea `--force` pentru a forța traducerea
    - Inversarea modelului și a limbii în numele fișierului de ieșire
- **1.2** Remediere în changelog
- **1.1** Adăugat suport pentru API-ul Mistral IA
- **1.0** Versiune inițială - Suport pentru API-ul OpenAI

**Acest document a fost tradus din versiunea fr în limba ro folosind modelul gpt-5-mini. Pentru mai multe informații despre procesul de traducere, consultați https://gitlab.com/jls42/ai-powered-markdown-translator**


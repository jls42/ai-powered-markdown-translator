### Changelog

- **1.0** Initialversion - Unterstützung der OpenAI-API
- **1.1** Hinzufügen der Unterstützung der Mistral-IA-API
- **1.2** Fix des Changelogs
- **1.3** Verbesserungen und neue Funktionen:
    - Verbesserte Verwaltung von Codeblöcken
    - Verbesserte Verwaltung von Ausgabedateien
    - Verbesserte Erkennung vorhandener Dateien
    - Option `--force` zum Erzwingen der Übersetzung
    - Umkehrung des Modells und der Sprache im Namen der Ausgabedatei
- **1.4** Neuheiten:
    - Unterstützung der Claude-API von Anthropic für die Übersetzung
    - Optimierung der Prompts für mehr Klarheit und Effizienz
    - Kleinere Anpassungen zur Verbesserung der Codewartung
- **1.5** Verbesserungen:
    - **Aktualisierung der API-Schlüssel und Standardmodelle:**
        - **OpenAI:** Aktualisierung von `DEFAULT_MODEL_OPENAI` auf `"gpt-4o"`.
        - **Mistral AI:** Aktualisierung von `DEFAULT_MODEL_MISTRAL` auf `"mistral-large-latest"`.
        - **Claude von Anthropic:** Hinzufügen von `DEFAULT_ANTHROPIC_API_KEY` und Aktualisierung von `DEFAULT_MODEL_CLAUDE` auf `"claude-3-5-sonnet-20240620"`.
    - **Optimierung der Übersetzungs-Prompts:**
        - Die Prompts für direkte Übersetzungen und Übersetzungsnotizen wurden angereichert für mehr Klarheit und Effizienz, einschließlich detaillierter Anweisungen zur Bewahrung von Metadaten und spezifischen Formatierungselementen.
    - **Refaktorisierung des Codes:**
        - Ersetzen von `MistralClient` durch die Klasse `Mistral` zur Initialisierung des Mistral-AI-Clients.
        - Umorganisation der Imports für bessere Lesbarkeit und Wartung.
        - Verbesserung der Textsegmentierung und Verwaltung von Codeblöcken zur Bewahrung des ursprünglichen Formats bei der Übersetzung.
    - **Verwaltung der Ausgabedateien:**
        - Umkehrung des Modells und der Sprache im Namen der Ausgabedateien (z.B. `f"{base}-{args.target_lang}-{args.model}.md"`), wodurch die Organisation und Suche nach Übersetzungen erleichtert wird.
    - **Verschiedene Verbesserungen:**
        - Bereinigung des Codes durch Entfernen unnötiger Leerzeilen.
        - Kleinere Anpassungen zur Verbesserung der Struktur und Lesbarkeit des Skripts.

**Ce document a été traduit de la version fr vers la langue de en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator**


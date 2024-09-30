### Änderungsprotokoll

- **1.0** Erste Version - Unterstützung der OpenAI-API
- **1.1** Unterstützung der Mistral IA-API hinzugefügt
- **1.2** Changelog-Korrektur
- **1.3** Verbesserungen und neue Funktionen:
    - Verbesserte Handhabung von Codeblöcken
    - Verbesserte Handhabung von Ausgabedateien
    - Verbesserte Erkennung vorhandener Dateien
    - Option `--force`, um die Übersetzung zu erzwingen
    - Umkehrung des Modells und der Sprache im Namen der Ausgabedatei
- **1.4** Neuheiten:
    - Unterstützung der Claude-API von Anthropic für die Übersetzung
    - Optimierung der Prompts für mehr Klarheit und Effizienz
    - Kleine Anpassungen zur Verbesserung der Code-Wartung
- **1.5** Verbesserungen:
    - **Aktualisierung der API-Schlüssel und Standardmodelle:**
        - **OpenAI:** Aktualisierung von `DEFAULT_MODEL_OPENAI` auf `"gpt-4o"`.
        - **Mistral AI:** Aktualisierung von `DEFAULT_MODEL_MISTRAL` auf `"mistral-large-latest"`.
        - **Claude von Anthropic:** Hinzufügen von `DEFAULT_ANTHROPIC_API_KEY` und Aktualisierung von `DEFAULT_MODEL_CLAUDE` auf `"claude-3-5-sonnet-20240620"`.
    - **Optimierung der Übersetzungsprompts:**
        - Die Prompts für direkte Übersetzungen und Übersetzungsnotizen wurden für mehr Klarheit und Effizienz angereichert, einschließlich detaillierter Anweisungen zur Wahrung von Metadaten und spezifischen Formatierungselementen.
    - **Refaktorisierung des Codes:**
        - Ersetzung von `MistralClient` durch die Klasse `Mistral` zur Initialisierung des Mistral AI-Clients.
        - Umstrukturierung der Importe für bessere Lesbarkeit und Wartung.
        - Verbesserung der Textsegmentierung und Handhabung von Codeblöcken zur Wahrung des Originalformats bei der Übersetzung.
    - **Handhabung von Ausgabedateien:**
        - Umkehrung von Modell und Sprache im Namen der Ausgabedateien (z.B. `f"{base}-{args.target_lang}-{args.model}.md"`), was die Organisation und Suche nach Übersetzungen erleichtert.
    - **Diverse Verbesserungen:**
        - Bereinigung des Codes durch Entfernen unnötiger Leerzeilen.
        - Kleine Anpassungen zur Verbesserung der Struktur und Lesbarkeit des Skripts.

**Dieses Dokument wurde von der Version fr in die Sprache de mit dem Modell gpt-4o übersetzt. Für weitere Informationen über den Übersetzungsprozess besuchen Sie bitte https://gitlab.com/jls42/ai-powered-markdown-translator.**


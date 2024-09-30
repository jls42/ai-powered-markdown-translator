### Changelog

- **1.0** Initialversion - Unterstützung der OpenAI-API
- **1.1** Hinzufügen der Unterstützung für die Mistral AI-API
- **1.2** Changelog-Fix
- **1.3** Verbesserungen und neue Funktionen:
    - Verbesserte Verwaltung von Codeblöcken
    - Verbesserte Verwaltung von Ausgabedateien
    - Verbesserte Erkennung vorhandener Dateien
    - Option `--force` zum Erzwingen der Übersetzung
    - Umkehrung von Modell und Sprache im Namen der Ausgabedatei
- **1.4** Neuheiten:
    - Unterstützung der Claude-API von Anthropic für die Übersetzung
    - Optimierung der Prompts für erhöhte Klarheit und Effizienz
    - Kleinere Anpassungen zur Verbesserung der Codewartung
- **1.5** Verbesserungen:
    - **Aktualisierung der API-Schlüssel und Standardmodelle:**
        - **OpenAI:** Aktualisierung von `DEFAULT_MODEL_OPENAI` auf `"gpt-4o"`.
        - **Mistral AI:** Aktualisierung von `DEFAULT_MODEL_MISTRAL` auf `"mistral-large-latest"`.
        - **Claude von Anthropic:** Hinzufügen von `DEFAULT_ANTHROPIC_API_KEY` und Aktualisierung von `DEFAULT_MODEL_CLAUDE` auf `"claude-3-5-sonnet-20240620"`.
    - **Optimierung der Übersetzungsprompts:**
        - Die Prompts für direkte Übersetzungen und Übersetzungshinweise wurden für bessere Klarheit und Effizienz erweitert, einschließlich detaillierter Anweisungen zur Beibehaltung von Metadaten und spezifischen Formatierungselementen.
    - **Code-Refaktorisierung:**
        - Ersetzung von `MistralClient` durch die Klasse `Mistral` für die Initialisierung des Mistral AI-Clients.
        - Neuorganisation der Importe für bessere Lesbarkeit und Wartung.
        - Verbesserung der Textsegmentierung und Verwaltung von Codeblöcken zur Beibehaltung der ursprünglichen Formatierung während der Übersetzung.
    - **Verwaltung der Ausgabedateien:**
        - Umkehrung von Modell und Sprache im Namen der Ausgabedateien (z.B. `f"{base}-{args.target_lang}-{args.model}.md"`), was die Organisation und Suche nach Übersetzungen erleichtert.
    - **Verschiedene Verbesserungen:**
        - Bereinigung des Codes durch Entfernen unnötiger Leerzeilen.
        - Kleinere Anpassungen zur Verbesserung der Struktur und Lesbarkeit des Skripts.

**Dieses Dokument wurde von der fr-Version in die en-Sprache mit dem Modell claude-3-5-sonnet-20240620 übersetzt. Weitere Informationen zum Übersetzungsprozess finden Sie unter https://gitlab.com/jls42/ai-powered-markdown-translator.**


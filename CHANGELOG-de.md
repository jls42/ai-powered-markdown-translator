### Änderungsprotokoll

🌍 [Englisch](CHANGELOG-en.md) | [Spanisch](CHANGELOG-es.md) | [Chinesisch](CHANGELOG-zh.md) | [Deutsch](CHANGELOG-de.md) | [Japanisch](CHANGELOG-ja.md) | [Koreanisch](CHANGELOG-ko.md) | [Arabisch](CHANGELOG-ar.md) | [Hindi](CHANGELOG-hi.md) | [Italienisch](CHANGELOG-it.md) | [Niederländisch](CHANGELOG-nl.md) | [Polnisch](CHANGELOG-pl.md) | [Portugiesisch](CHANGELOG-pt.md) | [Rumänisch](CHANGELOG-ro.md) | [Schwedisch](CHANGELOG-sv.md)

- **1.7** Neuerungen:
    - Option `--keep_filename`, um den ursprünglichen Dateinamen bei der Übersetzung beizubehalten
    - Unterstützung für die Datei `.env`, um API-Schlüssel automatisch zu laden
    - **Erhaltung von Inline-Code**: die Backticks (`` `...` ``) sind jetzt während der Übersetzung geschützt
    - Verbesserung des System-Prompts:
        - Bessere Handhabung von Anführungszeichen im YAML-Frontmatter
        - Schutz der Template-Variablen `{variable}`
        - Verbot unerbetener Übersetzerhinweise
    - Erfolgreich an 364 Dateien getestet (Migration des Blogs jls42.org)
- **1.6** Neuerungen:
    - Unterstützung der Google Gemini API für Übersetzungen (`--use_gemini`)
    - Aktualisierung der Standardmodelle 2026:
        - OpenAI: `gpt-5` (Qualität), `gpt-5-mini` (ökonomisch)
        - Claude: `claude-sonnet-4-5` (Qualität), `claude-haiku-4-5` (ökonomisch)
        - Gemini: `gemini-3-pro-preview` (Qualität), `gemini-3-flash-preview` (ökonomisch)
    - Sparmodus (`--eco`), um schnellere und kostengünstigere Modelle zu nutzen
    - Einzeldatei-Übersetzung (`--file`) ohne ein Verzeichnis zu durchsuchen
    - Neues vereinfachtes Namensmuster: `{base}-{lang}.md`
    - Option `--include_model`, um das alte Format mit dem Modellnamen beizubehalten
    - Unterstützung nicht aufgelisteter Modelle mit Standard-Token-Limit (128k)
    - README in 14 Sprachen übersetzt
- **1.5** Verbesserungen:
    - **Aktualisierung der API-Schlüssel und Standardmodelle:**
        - **OpenAI:** Aktualisierung von `DEFAULT_MODEL_OPENAI` auf `"gpt-4o"`.
        - **Mistral AI:** Aktualisierung von `DEFAULT_MODEL_MISTRAL` auf `"mistral-large-latest"`.
        - **Anthropic Claude:** Hinzugefügt `DEFAULT_ANTHROPIC_API_KEY` und Aktualisierung von `DEFAULT_MODEL_CLAUDE` auf `"claude-3-5-sonnet-20240620"`.
    - **Optimierung der Übersetzungs-Prompts:**
        - Die Prompts für direkte Übersetzungen und Übersetzungsnotizen wurden für bessere Klarheit und Effizienz erweitert und enthalten detaillierte Anweisungen zur Erhaltung von Metadaten und spezifischen Formatierungselementen.
    - **Refaktorisierung des Codes:**
        - Ersetzung von `MistralClient` durch die Klasse `Mistral` zur Initialisierung des Mistral AI Clients.
        - Umstrukturierung der Imports für bessere Lesbarkeit und Wartung.
        - Verbesserung der Textsegmentierung und Handhabung von Codeblöcken, um die ursprüngliche Formatierung während der Übersetzung zu erhalten.
    - **Verwaltung der Ausgabedateien:**
        - Vertauschung von Modell und Sprache im Namen der Ausgabedateien (z. B. `f"{base}-{args.target_lang}-{args.model}.md"`), was die Organisation und das Auffinden der Übersetzungen erleichtert.
    - **Verschiedene Verbesserungen:**
        - Bereinigung des Codes durch Entfernen unnötiger Leerzeilen.
        - Kleine Anpassungen zur Verbesserung der Struktur und Lesbarkeit des Skripts.
- **1.4** Neuerungen:
    - Unterstützung der Anthropic Claude API für Übersetzungen
    - Optimierung der Prompts für erhöhte Klarheit und Effizienz
    - Kleine Anpassungen zur Verbesserung der Wartbarkeit des Codes
- **1.3** Verbesserungen und neue Funktionen:
    - Verbesserte Handhabung von Codeblöcken
    - Verbesserte Verwaltung der Ausgabedateien
    - Verbesserte Erkennung vorhandener Dateien
    - Option `--force`, um die Übersetzung zu erzwingen
    - Vertauschung von Modell und Sprache im Namen der Ausgabedatei
- **1.2** Fehlerbehebung im Changelog
- **1.1** Unterstützung für die Mistral AI API hinzugefügt
- **1.0** Erstversion - Unterstützung der OpenAI API

**Dieses Dokument wurde von der fr-Version in die Sprache en mithilfe des Modells gpt-5-mini übersetzt. Für weitere Informationen zum Übersetzungsprozess konsultieren Sie https://gitlab.com/jls42/ai-powered-markdown-translator**


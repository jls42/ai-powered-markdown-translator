### Änderungsprotokoll

🌍 [Französisch](CHANGELOG.md) | [Englisch](CHANGELOG-en.md) | [Spanisch](CHANGELOG-es.md) | [Chinesisch](CHANGELOG-zh.md) | [Deutsch](CHANGELOG-de.md) | [Japanisch](CHANGELOG-ja.md) | [Koreanisch](CHANGELOG-ko.md) | [Arabisch](CHANGELOG-ar.md) | [Hindi](CHANGELOG-hi.md) | [Italienisch](CHANGELOG-it.md) | [Niederländisch](CHANGELOG-nl.md) | [Polnisch](CHANGELOG-pl.md) | [Portugiesisch](CHANGELOG-pt.md) | [Rumänisch](CHANGELOG-ro.md) | [Schwedisch](CHANGELOG-sv.md)

- **1.7** Neuheiten:
    - Option `--keep_filename` zum Beibehalten des Originaldateinamens während der Übersetzung
    - Unterstützung der Datei `.env` zum automatischen Laden der API-Schlüssel
    - **Inline-Code-Erhaltung**: die Backticks (`` `...` ``) sind jetzt während der Übersetzung geschützt
    - Verbesserung des System-Prompts:
        - Bessere Handhabung von Anführungszeichen im YAML-Frontmatter
        - Schutz der Template-Variablen `{variable}`
        - Verbot nicht angeforderter Übersetzerhinweise
    - Erfolgreich an 364 Dateien getestet (Blog-Migration jls42.org)
- **1.6** Neuheiten:
    - Unterstützung der Google Gemini API für Übersetzungen (`--use_gemini`)
    - Aktualisierung der Standardmodelle 2026:
        - OpenAI: `gpt-5` (Qualität), `gpt-5-mini` (Öko)
        - Claude: `claude-sonnet-4-5` (Qualität), `claude-haiku-4-5` (Öko)
        - Gemini: `gemini-3-pro-preview` (Qualität), `gemini-3-flash-preview` (Öko)
    - Kostensparmodus (`--eco`) zur Verwendung schnellerer und kostengünstigerer Modelle
    - Einzeldatei-Übersetzung (`--file`) ohne Durchlaufen eines Verzeichnisses
    - Neues vereinfachtes Namensgebungsmuster: `{base}-{lang}.md`
    - Option `--include_model` zum Beibehalten des alten Formats mit Modellnamen
    - Unterstützung nicht gelisteter Modelle mit Standard-Token-Limit (128k)
    - README in 14 Sprachen übersetzt
- **1.5** Verbesserungen:
    - **Aktualisierung der API-Schlüssel und Standardmodelle:**
        - **OpenAI:** Aktualisierung von `DEFAULT_MODEL_OPENAI` auf `"gpt-4o"`.
        - **Mistral AI:** Aktualisierung von `DEFAULT_MODEL_MISTRAL` auf `"mistral-large-latest"`.
        - **Claude von Anthropic:** Hinzufügen von `DEFAULT_ANTHROPIC_API_KEY` und Aktualisierung von `DEFAULT_MODEL_CLAUDE` auf `"claude-3-5-sonnet-20240620"`.
    - **Optimierung der Übersetzungs-Prompts:**
        - Die Prompts für direkte Übersetzungen und Übersetzungsanmerkungen wurden erweitert für bessere Klarheit und Effizienz, einschließlich detaillierter Anweisungen zur Erhaltung von Metadaten und spezifischen Formatierungselementen.
    - **Refaktorisierung des Codes:**
        - Ersetzung von `MistralClient` durch die Klasse `Mistral` für die Initialisierung des Mistral-AI-Clients.
        - Neuorganisation der Imports für bessere Lesbarkeit und Wartbarkeit.
        - Verbesserung der Textsegmentierung und Verwaltung von Codeblöcken, um das ursprüngliche Format während der Übersetzung zu bewahren.
    - **Verwaltung der Ausgabedateien:**
        - Vertauschung von Modell und Sprache im Namen der Ausgabedateien (z. B. `f"{base}-{args.target_lang}-{args.model}.md"`), was die Organisation und das Auffinden der Übersetzungen erleichtert.
    - **Verschiedenes:**
        - Bereinigung des Codes durch Entfernen unnötiger Leerzeilen.
        - Kleinere Anpassungen zur Verbesserung der Struktur und Lesbarkeit des Skripts.
- **1.4** Neuheiten:
    - Unterstützung der Claude-API von Anthropic für Übersetzungen
    - Optimierung der Prompts für mehr Klarheit und Effizienz
    - Kleinere Anpassungen zur Verbesserung der Wartbarkeit des Codes
- **1.3** Verbesserungen und neue Funktionen:
    - Verbesserte Verwaltung von Codeblöcken
    - Verbesserte Verwaltung der Ausgabedateien
    - Verbesserte Erkennung vorhandener Dateien
    - Option `--force` zum Erzwingen der Übersetzung
    - Vertauschung von Modell und Sprache im Namen der Ausgabedatei
- **1.2** Changelog-Fix
- **1.1** Unterstützung der Mistral-IA-API hinzugefügt
- **1.0** Erstversion - Unterstützung der OpenAI-API

**Dieses Dokument wurde von der fr-Version in die Sprache en unter Verwendung des Modells gpt-5-mini übersetzt. Für weitere Informationen zum Übersetzungsprozess konsultieren Sie https://gitlab.com/jls42/ai-powered-markdown-translator**


# KI-gestützter Markdown-Übersetzer mit OpenAI, Mistral AI und Claude von Anthropic

Dieses Projekt ist ein fortgeschrittenes Python-Skript, das die APIs von OpenAI, Mistral AI oder Claude von Anthropic verwendet, um Markdown-Dateien von einer Quellsprache in eine Zielsprache zu übersetzen. Es ist flexibel und einfach zu bedienen und bietet zusätzliche Optionen wie das Hinzufügen einer Übersetzungsnotiz, verbesserte Verwaltung von Ausgabedateien, Erkennung vorhandener Dateien und Unterstützung für mehrere Sprachen und Übersetzungsmodelle.

Für eine Demonstration und detaillierte Erklärungen besuchen Sie [jls42.org](https://jls42.org/) oder in übersetzter Version: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) und [jls42.org 中文](https://jls42.org/traductions_zh/).

## Hauptmerkmale

- **KI-gestützte Übersetzung**: Nutzen Sie die neuesten KI-Technologien zur Übersetzung Ihrer Dokumente mit OpenAI, Mistral AI oder Claude von Anthropic.
- **Mehrsprachige Unterstützung**: Übersetzen Sie Ihre Dokumente in mehrere Sprachen mit Unterstützung für verschiedene Sprachmodelle.
- **Intelligente Segmentierung**: Effiziente Verwaltung langer Texte durch automatisierte Segmentierung.
- **Übersetzungsnotiz**: Fügen Sie automatisch eine Übersetzungsnotiz hinzu, um Leser über den verwendeten Prozess zu informieren.
- **Verbesserte Verwaltung von Ausgabedateien**: Überprüfen Sie, ob bereits eine Übersetzung existiert, bevor Sie die Übersetzung starten.
- **Verbesserte Erkennung vorhandener Dateien**: Suchen Sie nach Dateien, die dem Basisnamen der Originaldatei und der Zielsprache entsprechen.
- **Flexibel und erweiterbar**: Der Code ist strukturiert, um das einfache Hinzufügen neuer Funktionen zu ermöglichen.

## Voraussetzungen

- Python 3.6 oder höher.
- Ein gültiger API-Schlüssel für OpenAI, Mistral AI oder Claude von Anthropic.

## Installation

1. Klonen Sie das Git-Repository:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. Installieren Sie die erforderlichen Abhängigkeiten:
```
pip install -r requirements.txt
```

## Konfiguration

Konfigurieren Sie Ihre Umgebung, indem Sie die Umgebungsvariablen für die erforderlichen API-Schlüssel festlegen:

- **OpenAI**:
    ```
    export OPENAI_API_KEY='ihr-openai-api-schlüssel'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='ihr-mistral-api-schlüssel'
    ```
- **Claude von Anthropic**:
    ```
    export ANTHROPIC_API_KEY='ihr-anthropic-api-schlüssel'
    ```

## Verwendung

Das Skript bietet mehrere Optionen zur Anpassung des Übersetzungsprozesses:

### Allgemeine Optionen

- `--source_dir`: Verzeichnis mit den zu übersetzenden Markdown-Dateien.
- `--target_dir`: Ausgabeverzeichnis für die übersetzten Dateien.
- `--model`: Zu verwendendendes GPT-Übersetzungsmodell. Das Standardmodell hängt von der ausgewählten API ab.
- `--source_lang`: Quellsprache der Dokumente. Wichtig insbesondere für das Hinzufügen von Übersetzungsnotizen.
- `--target_lang`: Zielsprache für die Übersetzung. Standardmäßig ist es Englisch.
- `--force`: Erzwingen der Übersetzung, auch wenn bereits eine Übersetzung für die Datei existiert.

### API-spezifische Optionen

- `--use_mistral`: Verwendung der Mistral AI API für die Übersetzung.
- `--use_claude`: Verwendung der Claude API von Anthropic für die Übersetzung.
- `--add_translation_note`: Hinzufügen einer Übersetzungsnotiz zum übersetzten Inhalt, die die verwendete Methode und Werkzeuge angibt.

### Verwendungsbeispiele

- Übersetzen von Französisch nach Englisch mit OpenAI unter Hinzufügung einer Übersetzungsnotiz:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Übersetzen von Französisch nach Spanisch mit Mistral AI ohne Übersetzungsnotiz:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Autor

Julien LE SAUX
E-Mail: contact@jls42.org

## Lizenz

Dieses Projekt steht unter der GNU GENERAL PUBLIC LICENSE Version 3, 29. Juni 2007. Weitere Details finden Sie in der Datei [LICENSE](LICENSE).

**Dieses Dokument wurde von der fr-Version in die Sprache de unter Verwendung des Modells claude-3-5-sonnet-20240620 übersetzt. Für weitere Informationen zum Übersetzungsprozess besuchen Sie bitte https://gitlab.com/jls42/ai-powered-markdown-translator.**


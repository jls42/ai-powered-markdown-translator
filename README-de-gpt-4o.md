# Markdown-Übersetzer AI-Powered mit OpenAI, Mistral AI und Claude von Anthropic

Dieses Projekt ist ein fortschrittliches Python-Skript, das die APIs von OpenAI, Mistral AI oder Claude von Anthropic verwendet, um Markdown-Dateien von einer Quellsprache in eine Zielsprache zu übersetzen. Es ist darauf ausgelegt, flexibel und benutzerfreundlich zu sein und bietet zusätzliche Optionen wie das Hinzufügen einer Übersetzungsnotiz, verbesserte Verwaltung der Ausgabedateien, Erkennung bestehender Dateien und Unterstützung für mehrere Sprachen und Übersetzungsmodelle.

Für eine Demonstration und detaillierte Erklärungen besuchen Sie [jls42.org](https://jls42.org/) oder in übersetzter Version: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) und [jls42.org 中文](https://jls42.org/traductions_zh/).

## Hauptfunktionen

- **AI-Powered Übersetzung**: Verwenden Sie die neuesten KI-Technologien zur Übersetzung Ihrer Dokumente mit OpenAI, Mistral AI oder Claude von Anthropic.
- **Mehrsprachige Unterstützung**: Übersetzen Sie Ihre Dokumente in mehrere Sprachen mit Unterstützung für verschiedene Sprachmodelle.
- **Intelligente Segmentierung**: Verwalten Sie lange Texte effizient durch automatisierte Segmentierung.
- **Übersetzungsnotiz**: Fügen Sie automatisch eine Übersetzungsnotiz hinzu, um die Leser über den verwendeten Prozess zu informieren.
- **Verbesserte Ausgabedateiverwaltung**: Überprüfen Sie, ob eine Übersetzung bereits vorhanden ist, bevor Sie mit der Übersetzung beginnen.
- **Verbesserte Erkennung bestehender Dateien**: Suchen Sie nach Dateien, die dem Basisnamen der Originaldatei und der Zielsprache entsprechen.
- **Flexibel und erweiterbar**: Der Code ist so strukturiert, dass er das Hinzufügen neuer Funktionen erleichtert.

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

Konfigurieren Sie Ihre Umgebung, indem Sie die Umgebungsvariablen für die benötigten API-Schlüssel festlegen:

- **OpenAI** :
    ```
    export OPENAI_API_KEY='Ihr-openai-api-schlüssel'
    ```
- **Mistral AI** :
    ```
    export MISTRAL_API_KEY='Ihr-mistral-api-schlüssel'
    ```
- **Claude von Anthropic** :
    ```
    export ANTHROPIC_API_KEY='Ihr-anthropic-api-schlüssel'
    ```

## Verwendung

Das Skript bietet mehrere Optionen zur Anpassung des Übersetzungsprozesses:

### Allgemeine Optionen

- `--source_dir` : Verzeichnis, das die zu übersetzenden Markdown-Dateien enthält.
- `--target_dir` : Ausgabeverzeichnis für die übersetzten Dateien.
- `--model` : Zu verwendendes GPT-Übersetzungsmodell. Das Standardmodell hängt von der ausgewählten API ab.
- `--source_lang` : Quellsprache der Dokumente. Wichtig insbesondere für das Hinzufügen von Übersetzungsnotizen.
- `--target_lang` : Zielsprache für die Übersetzung. Standardmäßig ist dies Englisch.
- `--force` : Erzwingen der Übersetzung, auch wenn bereits eine Übersetzung für die Datei vorhanden ist.

### API-spezifische Optionen

- `--use_mistral` : Verwenden der Mistral AI API für die Übersetzung.
- `--use_claude` : Verwenden der Claude von Anthropic API für die Übersetzung.
- `--add_translation_note` : Hinzufügen einer Übersetzungsnotiz zum übersetzten Inhalt, die die Methode und die verwendeten Werkzeuge spezifiziert.

### Anwendungsbeispiele

- Übersetzen von Französisch nach Englisch mit OpenAI und Hinzufügen einer Übersetzungsnotiz:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Übersetzen von Französisch nach Spanisch mit Mistral AI, ohne Übersetzungsnotiz:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Autor

Julien LE SAUX  
Email : contact@jls42.org

## Lizenz

Dieses Projekt steht unter der GNU GENERAL PUBLIC LICENSE Version 3, 29. Juni 2007. Siehe die Datei [LICENSE](LICENSE) für weitere Details.

**Dieses Dokument wurde von der Version fr auf die Sprache de unter Verwendung des Modells gpt-4o übersetzt. Für weitere Informationen zum Übersetzungsprozess siehe https://gitlab.com/jls42/ai-powered-markdown-translator.**


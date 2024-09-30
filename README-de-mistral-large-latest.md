# AI-gestützter Markdown-Übersetzer mit OpenAI, Mistral AI und Claude von Anthropic

Dieses Projekt ist ein fortgeschrittenes Python-Skript, das die APIs von OpenAI, Mistral AI oder Claude von Anthropic verwendet, um Markdown-Dateien von einer Quellsprache in eine Zielsprache zu übersetzen. Es ist darauf ausgelegt, flexibel und einfach zu bedienen zu sein, und bietet zusätzliche Optionen wie das Hinzufügen eines Übersetzungshinweises, verbessertes Verwalten von Ausgabedateien, Erkennen vorhandener Dateien und Unterstützung mehrerer Sprachen und Übersetzungsmodelle.

Für eine Demonstration und detaillierte Erklärungen besuchen Sie [jls42.org](https://jls42.org/) oder in übersetzter Version: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) und [jls42.org 中文](https://jls42.org/traductions_zh/).

## Hauptmerkmale

- **AI-gestützte Übersetzung**: Verwenden Sie die neuesten KI-Technologien zur Übersetzung Ihrer Dokumente mit OpenAI, Mistral AI oder Claude von Anthropic.
- **Mehrsprachige Unterstützung**: Übersetzen Sie Ihre Dokumente in mehrere Sprachen mit Unterstützung für verschiedene Sprachmodelle.
- **Intelligente Segmentierung**: Verwalten Sie lange Texte effizient durch automatisierte Segmentierung.
- **Übersetzungshinweis**: Fügen Sie automatisch einen Übersetzungshinweis hinzu, um die Leser über den verwendeten Prozess zu informieren.
- **Verbesserte Verwaltung von Ausgabedateien**: Überprüfen Sie, ob eine Übersetzung bereits existiert, bevor Sie die Übersetzung starten.
- **Verbesserte Erkennung vorhandener Dateien**: Suchen Sie nach Dateien, die dem Basisnamen der Originaldatei und der Zielsprache entsprechen.
- **Flexibel und erweiterbar**: Der Code ist so strukturiert, dass neue Funktionen leicht hinzugefügt werden können.

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
    export OPENAI_API_KEY='Ihr-OpenAI-API-Schlüssel'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='Ihr-Mistral-API-Schlüssel'
    ```
- **Claude von Anthropic**:
    ```
    export ANTHROPIC_API_KEY='Ihr-Anthropic-API-Schlüssel'
    ```

## Nutzung

Das Skript bietet mehrere Optionen zur Anpassung des Übersetzungsprozesses:

### Allgemeine Optionen

- `--source_dir`: Verzeichnis, das die zu übersetzenden Markdown-Dateien enthält.
- `--target_dir`: Ausgabeverzeichnis für die übersetzten Dateien.
- `--model`: Zu verwendendes GPT-Übersetzungsmodell. Das Standardmodell hängt von der ausgewählten API ab.
- `--source_lang`: Quellsprache der Dokumente. Wichtig insbesondere für das Hinzufügen von Übersetzungshinweisen.
- `--target_lang`: Zielsprache für die Übersetzung. Standardmäßig ist dies Englisch.
- `--force`: Übersetzung erzwingen, auch wenn bereits eine Übersetzung für die Datei existiert.

### API-spezifische Optionen

- `--use_mistral`: Verwenden Sie die Mistral AI-API für die Übersetzung.
- `--use_claude`: Verwenden Sie die Claude-API von Anthropic für die Übersetzung.
- `--add_translation_note`: Fügen Sie dem übersetzten Inhalt einen Übersetzungshinweis hinzu, der die verwendete Methode und die verwendeten Werkzeuge angibt.

### Beispiele für die Nutzung

- Übersetzen Sie vom Französischen ins Englische mit OpenAI, unter Hinzufügen eines Übersetzungshinweises:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Übersetzen Sie vom Französischen ins Spanische mit Mistral AI, ohne Übersetzungshinweis:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Autor

Julien LE SAUX
Email: contact@jls42.org

## Lizenz

Dieses Projekt steht unter der GNU GENERAL PUBLIC LICENSE Version 3, 29. Juni 2007. Siehe die Datei [LICENSE](LICENSE) für weitere Details.

**Ce document a été traduit de la version fr vers la langue de en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator**


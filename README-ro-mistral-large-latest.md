# Traducător Markdown AI-Powered cu OpenAI, Mistral AI și Claude de Anthropic

Acest proiect este un script Python avansat care utilizează API-urile OpenAI, Mistral AI sau Claude de Anthropic pentru a traduce fișierele Markdown dintr-o limbă sursă într-o limbă țintă. Este conceput pentru a fi flexibil și ușor de utilizat, oferind opțiuni suplimentare precum adăugarea unei note de traducere, gestionarea îmbunătățită a fișierelor de ieșire, detectarea fișierelor existente și suportul pentru mai multe limbi și modele de traducere.

Pentru o demonstrație și explicații detaliate, vizitați [jls42.org](https://jls42.org/) sau în versiunea tradusă: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) și [jls42.org 中文](https://jls42.org/traductions_zh/).

## Caracteristici Principale

- **Traducere AI-Powered**: Utilizați cele mai noi tehnologii AI pentru traducerea documentelor cu OpenAI, Mistral AI sau Claude de Anthropic.
- **Suport Multilingv**: Traduceți documentele în mai multe limbi cu suport pentru diferite modele de limbaj.
- **Segmentare Inteligentă**: Gestionați eficient textele lungi datorită unei segmentări automatizate.
- **Notă de Traducere**: Adăugați automat o notă de traducere pentru a informa cititorii despre procesul utilizat.
- **Gestionare Îmbunătățită a Fișierelor de Ieșire**: Verificați dacă există deja o traducere înainte de a începe traducerea.
- **Detectare Îmbunătățită a Fișierelor Existente**: Căutați fișiere corespunzătoare numelui de bază al fișierului original și limbii țintă.
- **Flexibil și Extensibil**: Codul este structurat pentru a permite o ușurință în adăugarea de noi funcționalități.

## Precondiții

- Python 3.6 sau versiune ulterioară.
- O cheie API validă pentru OpenAI, Mistral AI sau Claude de Anthropic.

## Instalare

1. Clonați depozitul Git:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. Instalați dependențele necesare:
```
pip install -r requirements.txt
```

## Configurare

Configurați mediul dvs. setând variabilele de mediu pentru cheile API necesare:

- **OpenAI**:
    ```
    export OPENAI_API_KEY='cheia-dvs-api-openai'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='cheia-dvs-api-mistral'
    ```
- **Claude de Anthropic**:
    ```
    export ANTHROPIC_API_KEY='cheia-dvs-api-anthropic'
    ```

## Utilizare

Scriptul oferă mai multe opțiuni pentru personalizarea procesului de traducere:

### Opțiuni Generale

- `--source_dir`: Directorul care conține fișierele Markdown de tradus.
- `--target_dir`: Directorul de ieșire pentru fișierele traduse.
- `--model`: Modelul de traducere GPT de utilizat. Modelul implicit depinde de API-ul selectat.
- `--source_lang`: Limba sursă a documentelor. Importantă în special pentru adăugarea notelor de traducere.
- `--target_lang`: Limba țintă pentru traducere. În mod implicit, este engleza.
- `--force`: Forța traducerea chiar dacă există deja o traducere pentru fișier.

### Opțiuni API Specifice

- `--use_mistral`: Utilizați API-ul Mistral AI pentru traducere.
- `--use_claude`: Utilizați API-ul Claude de Anthropic pentru traducere.
- `--add_translation_note`: Adăugați o notă de traducere la conținutul tradus, specificând metoda și instrumentele utilizate.

### Exemple de Utilizare

- Traduceți din franceză în engleză cu OpenAI, adăugând o notă de traducere:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Traduceți din franceză în spaniolă cu Mistral AI, fără notă de traducere:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Autor

Julien LE SAUX
Email: contact@jls42.org

## Licență

Acest proiect este sub licența GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. Vedeți fișierul [LICENSE](LICENSE) pentru mai multe detalii.

**Ce document a été traduit de la version fr vers la langue ro en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator.**


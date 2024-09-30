# Traducător de Markdown AI-Powered cu OpenAI, Mistral AI și Claude d'Anthropic

Acest proiect este un script Python avansat care utilizează API-urile OpenAI, Mistral AI sau Claude d'Anthropic pentru a traduce fișiere Markdown dintr-o limbă sursă într-o limbă țintă. Este conceput pentru a fi flexibil și ușor de utilizat, oferind opțiuni suplimentare precum adăugarea unei note de traducere, gestionarea îmbunătățită a fișierelor de ieșire, detectarea fișierelor existente și suport pentru mai multe limbi și modele de traducere.

Pentru o demonstrație și explicații detaliate, vizitați [jls42.org](https://jls42.org/) sau în versiunea tradusă: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) și [jls42.org 中文](https://jls42.org/traductions_zh/).

## Caracteristici Principale

- **Traducere AI-Powered**: Utilizați cele mai recente tehnologii AI pentru traducerea documentelor cu OpenAI, Mistral AI sau Claude d'Anthropic.
- **Suport Multilingv**: Traduceți documentele în mai multe limbi cu suport pentru modele de limbaj diferite.
- **Segmentare Inteligentă**: Gestionați eficient textele lungi prin segmentare automată.
- **Notă de Traducere**: Adăugați automat o notă de traducere pentru a informa cititorii despre procesul utilizat.
- **Gestionare Îmbunătățită a Fișierelor de Ieșire**: Verificați dacă există deja o traducere înainte de a lansa traducerea.
- **Detectare Îmbunătățită a Fișierelor Existente**: Căutați fișiere corespunzătoare numelui de bază al fișierului original și limbii țintă.
- **Flexibil și Extensibil**: Codul este structurat pentru a permite o adăugare facilă a noilor funcționalități.

## Cerințe

- Python 3.6 sau o versiune ulterioară.
- O cheie API validă pentru OpenAI, Mistral AI sau Claude d'Anthropic.

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

Configurați-vă mediul definind variabilele de mediu pentru cheile API necesare:

- **OpenAI**:
    ```
    export OPENAI_API_KEY='cheia-dvs-api-openai'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='cheia-dvs-api-mistral'
    ```
- **Claude d'Anthropic**:
    ```
    export ANTHROPIC_API_KEY='cheia-dvs-api-anthropic'
    ```

## Utilizare

Scriptul oferă mai multe opțiuni pentru a personaliza procesul de traducere:

### Opțiuni Generale

- `--source_dir`: Director care conține fișierele Markdown de tradus.
- `--target_dir`: Director de ieșire pentru fișierele traduse.
- `--model`: Modelul de traducere GPT de utilizat. Modelul implicit depinde de API-ul selectat.
- `--source_lang`: Limba sursă a documentelor. Important mai ales pentru adăugarea notelor de traducere.
- `--target_lang`: Limba țintă pentru traducere. Implicit, este engleza.
- `--force`: Forțați traducerea chiar dacă există deja o traducere pentru fișier.

### Opțiuni API Specifice

- `--use_mistral`: Utilizați API-ul Mistral AI pentru traducere.
- `--use_claude`: Utilizați API-ul Claude d'Anthropic pentru traducere.
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

Acest proiect este sub licență GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. Vedeți fișierul [LICENSE](LICENSE) pentru mai multe detalii.

**Acest document a fost tradus din versiunea fr în limba ro folosind modelul gpt-4o. Pentru mai multe informații despre procesul de traducere, consultați https://gitlab.com/jls42/ai-powered-markdown-translator**


# Traducător Markdown alimentat de AI

🌍 [Engleză](README-en.md) | [Spaniolă](README-es.md) | [Chineză](README-zh.md) | [Germană](README-de.md) | [Japoneză](README-ja.md) | [Coreeană](README-ko.md) | [Arabă](README-ar.md) | [Hindi](README-hi.md) | [Italiană](README-it.md) | [Olandeză](README-nl.md) | [Poloneză](README-pl.md) | [Portugheză](README-pt.md) | [Română](README-ro.md) | [Suedeză](README-sv.md)

Traducător de fișiere Markdown care utilizează **OpenAI**, **Mistral AI**, **Claude (Anthropic)** și **Google Gemini**.

Acest script Python traduce fișiere Markdown dintr-o limbă sursă într-o limbă țintă păstrând formatul, blocurile de cod și metadatele front matter.

## Caracteristici principale

- **Multi-provider**: Suport pentru 4 API-uri (OpenAI, Mistral, Claude, Gemini)
- **Modele 2026**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **Mod economic**: Opțiunea `--eco` pentru a folosi modele mai rapide și mai ieftine
- **Fișier unic**: Opțiunea `--file` pentru a traduce un singur fișier
- **Segmentare inteligentă**: Gestionarea textelor lungi cu limite de tokeni pe model
- **Păstrarea codului**: Blocurile de cod ȘI codul inline (`` `...` ``) sunt păstrate
- **Nume fișier**: Opțiunea `--keep_filename` pentru a păstra numele original
- **Configurare .env**: Suport pentru fișierul `.env` pentru cheile API
- **Notă de traducere**: Adăugare opțională a unei note la sfârșitul documentului

## Instalare

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Configurare

Creați un fișier `.env` în rădăcina proiectului sau definiți variabilele de mediu :

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

## Utilizare

### Traducerea unui fișier unic

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Traducerea unui director

```bash
# Avec OpenAI (défaut: gpt-5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### Mod economic

Folosește modele mai rapide și mai ieftine (gpt-5-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opțiuni

| Opțiune | Descriere |
|--------|-------------|
| `--file` | Fișier Markdown unic de tradus |
| `--source_dir` | Directorul sursă conținând fișierele Markdown |
| `--target_dir` | Directorul de ieșire pentru fișierele traduse |
| `--source_lang` | Limba sursă (implicit: `fr`) |
| `--target_lang` | Limba țintă (implicit: `en`) |
| `--model` | Model specific de utilizat |
| `--eco` | Folosește modelele economice |
| `--use_mistral` | Folosește API-ul Mistral AI |
| `--use_claude` | Folosește API-ul Claude |
| `--use_gemini` | Folosește API-ul Gemini |
| `--force` | Forțează re-traducerea |
| `--keep_filename` | Păstrează numele fișierului original |
| `--add_translation_note` | Adaugă o notă de traducere |
| `--include_model` | Include numele modelului în fișierul de ieșire |

### Modele implicite (2026)

| Furnizor | Calitate (implicit) | Economic (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Proiecte care folosesc acest script

- **[jls42.org](https://jls42.org)** - Blog personal multilingv (15 limbi)

## Autor

Julien LE SAUX
Email : contact@jls42.org

## Licență

GNU GENERAL PUBLIC LICENSE Versiunea 3. Vezi [LICENȚĂ](LICENSE).

**Acest document a fost tradus din versiunea fr în limba ro folosind modelul gpt-5-mini. Pentru mai multe informații despre procesul de traducere, consultați https://gitlab.com/jls42/ai-powered-markdown-translator**


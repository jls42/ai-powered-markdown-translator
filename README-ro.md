# Traducător Markdown bazat pe AI

🌍 [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

Traducător de fișiere Markdown care utilizează **OpenAI**, **Mistral AI**, **Claude (Anthropic)** și **Google Gemini**.

Acest script Python traduce fișiere Markdown dintr-o limbă sursă într-o limbă țintă, păstrând formatarea, blocurile de cod și metadatele front matter.

## Caracteristici principale

- **Multi-Provider**: Suport pentru 4 API-uri (OpenAI, Mistral, Claude, Gemini)
- **Modele 2026**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **Mod economic**: Opțiunea `--eco` pentru a utiliza modele mai rapide și mai puțin costisitoare
- **Fișier unic**: Opțiunea `--file` pentru a traduce un singur fișier
- **Segmentare inteligentă**: Gestionarea textelor lungi cu limite de tokeni per model
- **Păstrarea codului**: Blocurile de cod nu sunt traduse
- **Notă de traducere**: Adăugare opțională a unei note la sfârșitul documentului

## Instalare

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Configurare

Definiți variabila de mediu pentru API-ul pe care doriți să îl utilizați :

```bash
export OPENAI_API_KEY='votre-clé-api-openai'
export MISTRAL_API_KEY='votre-clé-api-mistral'
export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
export GOOGLE_API_KEY='votre-clé-api-google'
```

## Utilizare

### Traduceți un singur fișier

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Traduceți un director

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

Utilizează modele mai rapide și mai puțin costisitoare (gpt-5-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opțiuni

| Opțiune | Descriere |
|--------|-------------|
| `--file` | Fișier Markdown unic de tradus |
| `--source_dir` | Director sursă care conține fișierele Markdown |
| `--target_dir` | Director de ieșire pentru fișierele traduse |
| `--source_lang` | Limbă sursă (implicit: `fr`) |
| `--target_lang` | Limbă țintă (implicit: `en`) |
| `--model` | Model specific de utilizat |
| `--eco` | Utilizați modelele economice |
| `--use_mistral` | Utilizați API-ul Mistral AI |
| `--use_claude` | Utilizați API-ul Claude |
| `--use_gemini` | Utilizați API-ul Gemini |
| `--force` | Forțați retraducerea |
| `--add_translation_note` | Adăugați o notă de traducere |

### Modele implicite (2026)

| Furnizor | Calitate (implicit) | Economic (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Autor

Julien LE SAUX
Email : contact@jls42.org

## Licență

GNU GENERAL PUBLIC LICENSE Versiunea 3. Consultați [LICENSE](LICENSE).
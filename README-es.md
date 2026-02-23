# Traductor de Markdown Potenciado por IA

🌍 [Francés](README.md) | [Inglés](README-en.md) | [Español](README-es.md) | [Chino](README-zh.md) | [Alemán](README-de.md) | [Japonés](README-ja.md) | [Coreano](README-ko.md) | [Árabe](README-ar.md) | [Hindi](README-hi.md) | [Italiano](README-it.md) | [Neerlandés](README-nl.md) | [Polaco](README-pl.md) | [Portugués](README-pt.md) | [Rumano](README-ro.md) | [Sueco](README-sv.md)

Traductor de archivos Markdown que utiliza **OpenAI**, **Mistral AI**, **Claude (Anthropic)** y **Google Gemini**.

Este script en Python traduce archivos Markdown desde un idioma de origen a un idioma de destino preservando el formato, los bloques de código y los metadatos del front matter.

## Características principales

- **Multi-Provider**: Soporte para 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **Modelos 2026**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **Modo económico**: Opción `--eco` para usar modelos más rápidos y menos costosos
- **Archivo único**: Opción `--file` para traducir un solo archivo
- **Segmentación inteligente**: Manejo de textos largos con límites de tokens por modelo
- **Preservación del código**: Los bloques de código Y el código inline (`` `...` ``) se conservan
- **Nombre de archivo**: Opción `--keep_filename` para conservar el nombre original
- **Modo noticias**: Opción `--news` para proteger las citas en inglés y gestionar las banderas en los artículos de noticias
- **Configuración .env**: Soporte del archivo `.env` para las claves API
- **Nota de traducción**: Añadir opcionalmente una nota al final del documento

## Instalación

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Configuración

Cree un archivo `.env` en la raíz del proyecto o defina las variables de entorno :

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

## Uso

### Traducir un archivo único

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Traducir un directorio

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

### Modo económico

Usa modelos más rápidos y menos costosos (gpt-5-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opciones

| Opción | Descripción |
|--------|-------------|
| `--file` | Archivo Markdown único a traducir |
| `--source_dir` | Directorio fuente que contiene los archivos Markdown |
| `--target_dir` | Directorio de salida para los archivos traducidos |
| `--source_lang` | Idioma de origen (por defecto: `fr`) |
| `--target_lang` | Idioma de destino (por defecto: `en`) |
| `--model` | Modelo específico a utilizar |
| `--eco` | Usar los modelos económicos |
| `--use_mistral` | Usar la API Mistral AI |
| `--use_claude` | Usar la API Claude |
| `--use_gemini` | Usar la API Gemini |
| `--force` | Forzar la retraducción |
| `--keep_filename` | Conservar el nombre de archivo original |
| `--news` | Modo noticias: protege las citas EN, gestiona las banderas por idioma |
| `--add_translation_note` | Añadir una nota de traducción |
| `--include_model` | Incluir el nombre del modelo en el archivo de salida |

### Modelos predeterminados (2026)

| Proveedor | Calidad (predeterminada) | Económico (`--eco`) |
|----------|--------------------------|----------------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Proyectos que usan este script

- **[jls42.org](https://jls42.org)** - Blog personal multilingüe (15 idiomas)

## Autor

Julien LE SAUX
Correo electrónico: contact@jls42.org

## Licencia

Licencia Pública General GNU Versión 3. Ver [LICENCIA](LICENSE).

**Este documento ha sido traducido de la versión fr al idioma es utilizando el modelo gpt-5-mini. Para más información sobre el proceso de traducción, consulte https://gitlab.com/jls42/ai-powered-markdown-translator**


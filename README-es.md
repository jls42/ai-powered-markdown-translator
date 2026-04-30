# Traductor de Markdown con IA

🌍 [Francés](README.md) | [Inglés](README-en.md) | [Español](README-es.md) | [Chino](README-zh.md) | [Alemán](README-de.md) | [Japonés](README-ja.md) | [Coreano](README-ko.md) | [Árabe](README-ar.md) | [Hindi](README-hi.md) | [Italiano](README-it.md) | [Neerlandés](README-nl.md) | [Polaco](README-pl.md) | [Portugués](README-pt.md) | [Rumano](README-ro.md) | [Sueco](README-sv.md)

Traductor de archivos Markdown que utiliza **OpenAI**, **Mistral AI**, **Claude (Anthropic)** y **Google Gemini**.

Este script Python traduce archivos Markdown de un idioma fuente a un idioma objetivo preservando el formato, los bloques de código y los metadatos del front matter.

## Características principales

- **Multi-proveedor**: Compatibilidad con 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **Modelos 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Modo económico**: Opción `--eco` para usar modelos más rápidos y menos costosos
- **Archivo único**: Opción `--file` para traducir un solo archivo
- **Segmentación inteligente**: Gestión de textos largos con límites de tokens por modelo
- **Preservación del código**: Los bloques de código Y el código inline (`` `...` ``) se preservan
- **Nombre de archivo**: Opción `--keep_filename` para conservar el nombre original
- **Modo noticias**: Opción `--news` para proteger las citas en inglés y gestionar las banderas en artículos de noticias
- **Configuración .env**: Compatibilidad con el archivo `.env` para las claves API
- **Nota de traducción**: Añadido opcional de una nota al final del documento

## Instalación

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Herramientas de calidad (opcional pero recomendado)

El proyecto utiliza [`pre-commit`](https://pre-commit.com) para impedir commitear código mal formateado, vulnerable o que contenga un secreto. Instalación:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hooks activos: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complejidad), detect-secrets (claves API), mypy (tipado progresivo), Opengrep (SAST), pip-audit (CVE deps), unittest. Ver sección `CLAUDE.md` _Calidad / pre-commit_ para los detalles.

## Configuración

Cree un archivo `.env` en la raíz del proyecto o defina las variables de entorno:

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
# Avec OpenAI (défaut: gpt-5.5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### Modo económico

Usa modelos más rápidos y menos costosos (gpt-5.4-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opciones

| Opción                   | Descripción                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Archivo Markdown único a traducir                                       |
| `--source_dir`           | Directorio fuente que contiene los archivos Markdown                        |
| `--target_dir`           | Directorio de salida para los archivos traducidos                          |
| `--source_lang`          | Idioma fuente (predeterminado: `fr`)                                             |
| `--target_lang`          | Idioma objetivo (predeterminado: `en`)                                              |
| `--model`                | Modelo específico a utilizar                                             |
| `--eco`                  | Usar los modelos económicos                                         |
| `--use_mistral`          | Usar la API de Mistral AI                                                |
| `--use_claude`           | Usar la API de Claude                                                    |
| `--use_gemini`           | Usar la API de Gemini20                                                    |
| `--force`                | Forzar la retraducción                                                  |
| `--keep_filename`        | Conservar el nombre de archivo original                                     |
| `--news`                 | Modo noticias: protege las citas EN, gestiona las banderas por idioma |
| `--add_translation_note` | Añadir una nota de traducción                                           |
| `--include_model`        | Incluir el nombre del modelo en el archivo de salida                       |

### Modelos predeterminados (2026)

| Proveedor | Calidad (predeterminado)         | Económico (`--eco`)     |
| -------- | ------------------------ | ------------------------ |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`           |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5`       |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`   |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3-flash-preview` |

> **Recomendación para traducciones de larga extensión** : `--use_gemini` (predeterminado = `gemini-3.1-pro-preview` calidad, `--eco` = `gemini-3-flash-preview`) tiende a preservar mejor la estructura markdown en scripts no latinos (PL, JA, ZH, AR, HI), especialmente en modo `--news` donde la fidelidad de los placeholders cuenta. OpenAI sigue siendo el predeterminado para la retrocompatibilidad.

## Proyectos que utilizan este script

- **[jls42.org](https://jls42.org)** - Blog personal multilingüe (15 idiomas)

## Autor

Julien LE SAUX
Email: contact@jls42.org

## Licencia

GNU GENERAL PUBLIC LICENSE Version 3. Vea [LICENSE](LICENSE).

**Este documento ha sido traducido de la versión fr al idioma es utilizando el modelo gpt-5.4-mini. Para obtener más información sobre el proceso de traducción, consulte https://gitlab.com/jls42/ai-powered-markdown-translator**


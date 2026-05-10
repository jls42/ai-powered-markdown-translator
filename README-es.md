# Traductor de Markdown impulsado por IA

🌍 [Francés](README.md) | [Inglés](README-en.md) | [Español](README-es.md) | [Chino](README-zh.md) | [Alemán](README-de.md) | [Japonés](README-ja.md) | [Coreano](README-ko.md) | [Árabe](README-ar.md) | [Hindi](README-hi.md) | [Italiano](README-it.md) | [Neerlandés](README-nl.md) | [Polaco](README-pl.md) | [Portugués](README-pt.md) | [Rumano](README-ro.md) | [Sueco](README-sv.md)

<h4 align="center">📊 Calidad del código</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Estado del control de calidad"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Calificación de seguridad"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Calificación de fiabilidad"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Calificación de mantenibilidad"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Cobertura"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilidades"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Errores"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Olores de código"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Líneas duplicadas (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Deuda técnica"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Líneas de código"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Insignia de Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Traductor de archivos Markdown que utiliza **OpenAI**, **Mistral AI**, **Claude (Anthropic)** y **Google Gemini**.

Este script Python traduce archivos Markdown de un idioma de origen a un idioma de destino mientras preserva el formato, los bloques de código y los metadatos front matter.

## Características Principales

- **Multi-Proveedor**: Compatibilidad con 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **Modelos 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Modo Económico**: Opción `--eco` para usar modelos más rápidos y menos costosos
- **Archivo Único**: Opción `--file` para traducir un solo archivo
- **Segmentación Inteligente**: Gestión de textos largos con límites de tokens por modelo
- **Preservación del Código**: Se preservan los bloques de código Y el código inline (`` `...` ``)
- **Nombre de Archivo**: Opción `--keep_filename` para conservar el nombre original
- **Modo Noticias**: Opción `--news` para proteger las citas en inglés y gestionar las banderas por idioma en los artículos de actualidad
- **Configuración .env**: Compatibilidad con el archivo `.env` para las claves API
- **Nota de Traducción**: Añadido opcional de una nota al final del documento

## Instalación

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Herramientas de calidad (opcional, pero recomendado)

El proyecto utiliza [`pre-commit`](https://pre-commit.com) para evitar hacer commit de código mal formateado, vulnerable o que contenga un secreto. Instalación:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hooks activos: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexidad), detect-secrets (claves API), mypy (tipado progresivo), Opengrep (SAST), pip-audit (CVE deps), unittest. Consulta la sección _Calidad / pre-commit_ de `CLAUDE.md` para más detalles.

## Configuración

Crea un archivo `.env` en la raíz del proyecto o define las variables de entorno:

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

Usa modelos más rápidos y menos costosos (gpt-5.4-mini, claude-haiku, gemini-flash):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opciones

| Opción                  | Descripción                                                         |
| ----------------------- | ------------------------------------------------------------------- |
| `--file`                 | Archivo Markdown único para traducir                                |
| `--source_dir`           | Directorio de origen que contiene los archivos Markdown             |
| `--target_dir`           | Directorio de salida para los archivos traducidos                   |
| `--source_lang`          | Idioma de origen (predeterminado: `fr`)                   |
| `--target_lang`          | Idioma de destino (predeterminado: `en`)                  |
| `--model`                | Modelo específico a utilizar                                        |
| `--eco`                  | Usar los modelos económicos                                         |
| `--use_mistral`          | Usar la API de Mistral AI                                           |
| `--use_claude`           | Usar la API de Claude                                              |
| `--use_gemini`           | Usar la API de Gemini                                              |
| `--force`                | Forzar la retraducción                                              |
| `--keep_filename`        | Conservar el nombre de archivo original                             |
| `--news`                 | Modo noticias: protege las citas EN, gestiona las banderas por idioma |
| `--add_translation_note` | Añadir una nota de traducción                                        |
| `--note_position`        | Posición de la nota: `top`, `bottom` (predeterminado), o `both` |
| `--note_format`          | Formato de la nota: `legacy` (predeterminado, párrafo en negrita) o `marker` |
| `--include_model`        | Incluir el nombre del modelo en el archivo de salida                 |

### Nota de traducción: posiciones y formatos

Con `--add_translation_note`, el traductor puede colocar la nota arriba, abajo o en ambos lugares, y renderizarla ya sea en formato de texto plano (retrocompatible) o en formato `marker` consumible por un plugin Markdown.

**Posición** (`--note_position`):

- `bottom` (predeterminado): nota al final del archivo, como históricamente.
- `top`: nota insertada **después del frontmatter YAML** (seguridad de Astro Content Collections, gray-matter, etc.).
- `both`: nota insertada arriba Y abajo (una sola llamada LLM, contenido reutilizado para ambas ubicaciones).

**Formato** (`--note_format`):

- `legacy` (predeterminado): párrafo en negrita `**...**` — comportamiento estrictamente idéntico a v1.8, byte a byte. Compatible con Hugo, GitHub, GitLab y cualquier renderizador Markdown.
- `marker`: definición de referencia de enlace Markdown invisible (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) seguida de un blockquote en negrita. Legible de forma nativa en GitHub/GitLab, y utilizable en la compilación por un plugin remark en Astro para producir un banner estilizado (cf. blog jls42.org).

```bash
# Compatibilité legacy (rien ne change vs v1.8)
python translate.py --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### Modelos predeterminados (2026)

| Proveedor | Calidad (predeterminado) | Económico (`--eco`) |
| --------- | ------------------------ | -------------------------- |
| OpenAI    | `gpt-5.5`           | `gpt-5.4-mini`             |
| Claude    | `claude-sonnet-4-6`           | `claude-haiku-4-5-20251001`             |
| Mistral   | `mistral-large-latest`           | `mistral-small-latest`             |
| Gemini    | `gemini-3.1-pro-preview`           | `gemini-3.1-flash-lite-preview`             |

> **Recomendación para traducciones long-form**: `--use_gemini` (predeterminado = `gemini-3.1-pro-preview` calidad, `--eco` = `gemini-3.1-flash-lite-preview`) tiende a preservar mejor la estructura markdown en scripts no latinos (PL, JA, ZH, AR, HI), especialmente en modo `--news` donde la fidelidad de los placeholders cuenta. OpenAI sigue siendo el predeterminado por compatibilidad retroactiva.

## Proyectos que usan este script

- **[jls42.org](https://jls42.org)** - Blog personal multilingüe (15 idiomas)

## Autor

Julien LE SAUX
Correo: contact@jls42.org

## Licencia

GNU GENERAL PUBLIC LICENSE Versión 3. Véase [LICENSE](LICENSE).

**Artículo traducido del fr al es con gpt-5.4-mini.**

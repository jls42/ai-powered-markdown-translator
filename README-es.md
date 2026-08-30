# Traductor de Markdown AI-Powered

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

<h4 align="center">📊 Calidad del código</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Estado de la puerta de calidad"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Calificación de seguridad"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Calificación de fiabilidad"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Calificación de mantenibilidad"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Cobertura"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilidades"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Errores"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Problemas de código"></a>
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

Este script Python traduce archivos Markdown de un idioma de origen a un idioma de destino, preservando el formato, los bloques de código y los metadatos front matter.

## Características principales

- **Multi-Provider**: Compatibilidad con 4 APIs (OpenAI, Mistral, Claude, Gemini) + el CLI Codex mediante una suscripción a ChatGPT
- **Modelos de 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Modo económico**: Opción `--eco` para utilizar modelos más rápidos y económicos
- **Archivo único**: Opción `--file` para traducir un solo archivo
- **Segmentación inteligente**: Gestión de textos largos con límites de tokens por modelo
- **Preservación del código**: Se preservan tanto los bloques de código COMO el código inline (`` `...` ``)
- **Nombre de archivo**: Opción `--keep_filename` para conservar el nombre original
- **Modo News**: Opción `--news` para proteger las citas en inglés y gestionar las banderas en los artículos de actualidad
- **Configuración .env**: Compatibilidad con el archivo `.env` para las claves API
- **Nota de traducción**: Adición opcional de una nota al final del documento

## Instalación

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Herramientas de calidad (opcionales, pero recomendadas)

El proyecto utiliza [`pre-commit`](https://pre-commit.com) para impedir que se haga commit de código mal formateado, vulnerable o que contenga un secreto. Instalación:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hooks activos: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complejidad), detect-secrets (claves API), mypy (tipado progresivo), Opengrep (SAST), pip-audit (CVE de dependencias), unittest. Consulta la sección _Quality / pre-commit_ de `CLAUDE.md` para obtener más información.

## Configuración

Crea un archivo `.env` en la raíz del proyecto o define las variables de entorno:

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

`GEMINI_API_KEY` se acepta como alternativa a `GOOGLE_API_KEY` (convención de AI
Studio). Variables opcionales: `XAI_BASE_URL` (endpoint de xAI, valor predeterminado
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (segundos por llamada a Anthropic, valor predeterminado
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
y `GROK_TRANSLATE_SANDBOX` (consulta la sección Grok CLI).

## Uso

### Traducir un único archivo

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Traducir un directorio

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
python translate.py --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
python translate.py --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
python translate.py --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'
```

### Traducir mediante una suscripción a ChatGPT (`--use_codex`)

Este provider no consume ninguna clave API: controla el CLI Codex oficial en modo
no interactivo, por lo que la traducción se descuenta de la cuota de la suscripción
a ChatGPT (Plus, Pro, Business…) ya pagada. Es la única vía documentada por
OpenAI para este uso: los tokens de `~/.codex/auth.json` no autentican
las llamadas a la API Platform y, de hecho, este script nunca los lee.

**Requisitos previos:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

El binario se busca en este orden: la variable `CODEX_BIN`, el `PATH`
y, después, el paquete Python `openai-codex-cli-bin`. Este último no se incluye
deliberadamente en `requirements.txt`: pesa unos 250 MB, lo que supondría imponerlo a todos los
usuarios para un provider opcional.

**Información importante:**

- **No se utiliza ninguna clave API.** `OPENAI_API_KEY` y `CODEX_API_KEY` se
  eliminan del entorno del subproceso, lo que garantiza que una clave
  presente en `.env` nunca hará que la traducción pase a facturarse por
  uso.
- **Un segmento = un «mensaje local»** de la ventana de 5 horas del plan.
  Utiliza `--eco` (modelo `gpt-5.6-luna`, entre 250 y 2 000 mensajes/5 h en Plus)
  en lugar del modelo de calidad (`gpt-5.6-sol`, entre 10 y 100 mensajes/5 h).
- **Más lento** que una llamada API: calcula unos 45 s para un README completo, frente a
  unos segundos de forma directa.
- **Rechazado en CI** (si `CI` o `GITHUB_ACTIONS` están definidos): la autenticación mediante
  suscripción no está prevista para un runner compartido y OpenAI desaconseja este
  flujo de trabajo en repositorios públicos. Utiliza una clave API en este caso.
- Variables de entorno: `CODEX_BIN` (ruta explícita del binario) y
  `CODEX_TIMEOUT` (segundos por segmento, valor predeterminado `600`).

### Traducir mediante una suscripción a Grok (`--use_grok_cli`)

El mismo principio que `--use_codex`, con el CLI oficial **Grok Build**: la
traducción se descuenta de la suscripción a Grok (SuperGrok / X Premium+) en lugar
de facturarse por token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Confinamiento: léelo antes de usarlo.** Este provider es estructuralmente **más
débil** que `--use_codex`, y es una decisión asumida:

- Codex se ejecuta en `--sandbox read-only`, una frontera impuesta por el sistema.
- El sandbox de Grok **no puede aplicarse** en muchos equipos Linux
  recientes: AppArmor bloquea los user namespaces sin privilegios desde Ubuntu
  24.04, y la deny-list de los sockets del runtime de contenedores falla si
  `/run/podman` está en `0700`. Ahora bien, un perfil **integrado** que no puede
  aplicarse se inicia **sin confinamiento y en silencio**.
- Por tanto, el script no solicita ningún perfil de forma predeterminada y **nunca recurre
  silenciosamente a una alternativa**: muestra una advertencia. El confinamiento se basa en las
  reglas `--deny` del CLI (incluida la regla general `*`), la única capa que funciona
  como _fail-closed_: una regla desconocida hace que se rechace el inicio en lugar de
  retirar la protección sin avisar.
- Para **exigir** el sandbox del SO: `GROK_TRANSLATE_SANDBOX=read-only`. El
  inicio fallará si la máquina no puede respetarlo, que es el
  comportamiento deseado.

**Cuota**: el pool de Grok es **semanal y compartido** con Chat, Imagine y
Voice, y ningún comando permite consultarlo. Por tanto, un procesamiento por lotes puede
reducir tu uso conversacional sin que nada lo indique; de ahí una
concurrencia limitada a 2 y una advertencia en `regen_translations.sh`.

Otras variables: `GROK_BIN` (ruta del binario), `GROK_TIMEOUT` (valor predeterminado: 900 s).

Para regenerar las 28 traducciones:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### Modo económico

Utiliza modelos más rápidos y económicos (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opciones

| Opción                   | Descripción                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Archivo Markdown único que se va a traducir                                       |
| `--source_dir`           | Directorio de origen que contiene los archivos Markdown                        |
| `--target_dir`           | Directorio de salida para los archivos traducidos                          |
| `--source_lang`          | Idioma de origen (valor predeterminado: `fr`)                                             |
| `--target_lang`          | Idioma de destino (valor predeterminado: `en`)                                              |
| `--model`                | Modelo específico que se va a utilizar                                             |
| `--eco`                  | Utilizar los modelos económicos                                         |
| `--use_mistral`          | Utilizar la API de Mistral AI                                                |
| `--use_claude`           | Utilizar la API de Claude                                                    |
| `--use_gemini`           | Utilizar la API de Gemini                                                    |
| `--use_codex`            | Utilizar el CLI Codex con la cuota de la suscripción a ChatGPT               |
| `--use_grok`             | Utilizar la API de xAI (Grok): requiere `XAI_API_KEY`                      |
| `--use_grok_cli`         | Utilizar el CLI Grok con la cuota de la suscripción a Grok                   |
| `--force`                | Forzar una nueva traducción                                                  |
| `--keep_filename`        | Conservar el nombre de archivo original                                     |
| `--news`                 | Modo de noticias: protege las citas en inglés y gestiona las banderas por idioma |
| `--add_translation_note` | Añadir una nota de traducción                                           |
| `--note_position`        | Posición de la nota: `top`, `bottom` (valor predeterminado) o `both`                |
| `--note_format`          | Formato de la nota: `legacy` (valor predeterminado, párrafo en negrita) o `marker`       |
| `--include_model`        | Incluir el nombre del modelo en el archivo de salida                       |
| `--reasoning_effort`     | Esfuerzo de razonamiento de GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`     |

### Nota de traducción: posiciones y formatos

Con `--add_translation_note`, el traductor puede colocar la nota en la parte superior, en la parte inferior o en ambos lugares, y presentarla en formato de texto simple (compatible con versiones anteriores) o en formato `marker`, que puede consumir un plugin Markdown.

**Posición** (`--note_position`):

- `bottom` (valor predeterminado): nota al final del archivo, como históricamente.
- `top`: nota insertada **después del frontmatter YAML** (seguridad para Astro Content Collections, gray-matter, etc.).
- `both`: nota insertada en la parte superior Y en la inferior (una única llamada al LLM, con contenido reutilizado en ambas ubicaciones).

**Formato** (`--note_format`):

- `legacy` (valor predeterminado): párrafo en negrita `**...**`, con un comportamiento estrictamente idéntico a v1.8, byte-for-byte. Compatible con Hugo, GitHub, GitLab y cualquier renderer Markdown.
- `marker`: definición invisible de referencia de enlace Markdown (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), seguida de un blockquote en negrita. Se puede leer de forma nativa en GitHub/GitLab y utilizar durante el build mediante un plugin remark en Astro para generar un banner estilizado (véase el blog jls42.org).

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

| Provider | Calidad (valor predeterminado)       | Económico (`--eco`)    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **Recomendación para traducciones long-form**: `--use_gemini` (valor predeterminado = `gemini-3.7-flash`) preserva fielmente la estructura Markdown en los sistemas de escritura no latinos (PL, JA, ZH, AR, HI), incluso en modo `--news`, donde importa la fidelidad de los placeholders. Medido con este README traducido al japonés: estructura idéntica a `gemini-3.1-pro-preview` (21 listas, 18 bloques de código, 13 enlaces HTML, 13 imágenes y todas las URLs preservadas) con una latencia unas 6 veces menor. OpenAI sigue siendo el valor predeterminado para mantener la compatibilidad con versiones anteriores.

## Proyectos que utilizan este script

- **[jls42.org](https://jls42.org)** - Blog personal multilingüe (15 idiomas)

## Autor

Julien LE SAUX
Correo electrónico: contact@jls42.org

## Licencia

GNU GENERAL PUBLIC LICENSE Versión 3. Consulta [LICENSE](LICENSE).

**Artículo traducido del fr al es con gpt-5.6-sol.**

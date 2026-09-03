# Traductor de Markdown con IA

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Calidad del código</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Estado de Quality Gate"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Clasificación de seguridad"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Clasificación de fiabilidad"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Clasificación de mantenibilidad"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Cobertura"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilidades"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Errores"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Malos olores de código"></a>
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

Este script de Python traduce archivos Markdown de un idioma de origen a un idioma de destino, preservando el formato, los bloques de código y los metadatos de front matter.

## Características principales

- **Multi-Provider**: Compatible con 4 APIs (OpenAI, Mistral, Claude, Gemini) + el CLI Codex con una suscripción de ChatGPT
- **Modelos 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Modo económico**: Opción `--eco` para utilizar modelos más rápidos y económicos
- **Archivo único**: Opción `--file` para traducir un solo archivo
- **Segmentación inteligente**: Gestión de textos largos con límites de tokens por modelo
- **Preservación del código**: Los bloques de código Y el código inline (`` `...` ``) se preservan
- **Nombre de archivo**: Opción `--keep_filename` para conservar el nombre original
- **Modo News**: Opción `--news` para proteger las citas en inglés y gestionar las banderas en los artículos de actualidad
- **Configuración .env**: Compatibilidad con el archivo `.env` para las claves API
- **Nota de traducción**: Adición opcional de una nota al final del documento

## Instalación

### Para utilizar la herramienta

```bash
pip install ai-powered-markdown-translator
```

El comando `aipmt` estará disponible en todas partes. Si el directorio de scripts
de Python no está en tu `PATH`, `python -m aipmt` hace exactamente lo mismo.
Python 3.10 o posterior.

Para una instalación aislada del resto de tus paquetes:

```bash
pipx install ai-powered-markdown-translator
```

### Para contribuir al proyecto

El repositorio clonado sigue siendo necesario para desarrollar: allí se encuentran las pruebas,
las 28 traducciones y todas las herramientas de calidad.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` es un **lock completamente fijado**, reflejo exacto del
entorno probado. Los límites publicados en `pyproject.toml` son
deliberadamente más amplios: no imponen nada a tus otros paquetes.

### Herramientas de calidad (opcional, pero recomendado)

El proyecto utiliza [`pre-commit`](https://pre-commit.com) para impedir hacer commit de código mal formateado, vulnerable o que contenga un secreto. Instalación:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hooks activos: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complejidad), detect-secrets (claves API), mypy (tipado progresivo), Opengrep (SAST), pip-audit (dependencias CVE), unittest. Consulta la sección _Quality / pre-commit_ de `CLAUDE.md` para más detalles.

## Configuración

Las claves se buscan en **tres ubicaciones**, de la más prioritaria a la menos prioritaria.
Cada una solo completa lo que la anterior deja vacío.

|     | Dónde                                            | Para qué                             |
| --- | ----------------------------------------------- | ------------------------------------- |
| 1   | Variables de entorno                             | CI, contenedores, excepción puntual |
| 2   | `.env` del directorio actual (o de un directorio superior) | una clave propia del proyecto            |
| 3   | `~/.config/aipmt/.env`                        | **instalado una vez, sirve en todas partes**   |

Lo más sencillo después de un `pip install` es la tercera:

```bash
mkdir -p ~/.config/aipmt
cat > ~/.config/aipmt/.env <<'EOF'
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google
EOF
chmod 600 ~/.config/aipmt/.env
```

Este archivo sigue `XDG_CONFIG_HOME` cuando la variable designa una ruta absoluta
(en caso contrario se ignora, como prescribe la especificación), y `%APPDATA%`
en Windows.

La segunda sigue siendo útil cuando un repositorio tiene su propia clave: un `.env` en su raíz
tiene prioridad sobre la configuración del usuario, sin modificarla. Y una variable ya definida
en el entorno tiene prioridad sobre ambas:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Si no se encuentra ninguna clave, el comando no muestra ningún rastro de llamada: enumera
las tres ubicaciones con su ruta exacta.

`GEMINI_API_KEY` se acepta como alternativa a `GOOGLE_API_KEY` (convención de AI
Studio). Variables opcionales: `XAI_BASE_URL` (endpoint de xAI, valor predeterminado
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (segundos por llamada de Anthropic, valor predeterminado
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
y `GROK_TRANSLATE_SANDBOX` (consulta la sección Grok CLI). En el caso de
`regen_translations.sh`: `REGEN_PROVIDER`, `REGEN_MODEL` y
`REGEN_JOB_TIMEOUT` (límite por trabajo, valor predeterminado: 600 s).

## Uso

### Traducir un archivo único

```bash
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Traducir un directorio

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
aipmt --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
aipmt --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
aipmt --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
aipmt --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
aipmt --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
aipmt --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
aipmt --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'
```

### Traducir con una suscripción de ChatGPT (`--use_codex`)

Este provider no consume ninguna clave API: controla el CLI Codex oficial en modo
no interactivo, por lo que la traducción se descuenta de la cuota de la suscripción
de ChatGPT (Plus, Pro, Business…) ya pagada. Es la única vía documentada por
OpenAI para este uso: los tokens de `~/.codex/auth.json` no autentican
las llamadas a la API Platform y, además, este script nunca los lee.

**Requisitos previos:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

El binario se busca en este orden: la variable `CODEX_BIN`, el `PATH`,
y después el paquete de Python `openai-codex-cli-bin`. Este último no se incluye deliberadamente
en `requirements.txt`: ocupa aproximadamente 250 MB, lo que se impondría a todos los
usuarios por un provider opcional.

**A tener en cuenta:**

- **No se utiliza ninguna clave API.** `OPENAI_API_KEY` y `CODEX_API_KEY` se
  eliminan del entorno del subproceso, lo que garantiza que una clave presente en
  `.env` nunca hará que la traducción pase a facturación por uso.
- **Un segmento = un «mensaje local»** de la ventana de 5 horas del plan.
  Utiliza `--eco` (modelo `gpt-5.6-luna`, 250-2.000 mensajes/5 h en Plus)
  en lugar del modelo de calidad (`gpt-5.6-sol`, 10-100 mensajes/5 h).
- **Más lento** que una llamada API: calcula unos 45 s para un README completo, frente a
  unos pocos segundos directamente.
- **Rechazado en CI** (`CI` o `GITHUB_ACTIONS` definido): la autenticación mediante
  suscripción no está prevista para un runner compartido, y OpenAI desaconseja este flujo
  de trabajo en repositorios públicos. Utiliza una clave API en este caso.
- Variables de entorno: `CODEX_BIN` (ruta explícita del binario) y
  `CODEX_TIMEOUT` (segundos por segmento, valor predeterminado `600`).

### Traducir con una suscripción de Grok (`--use_grok_cli`)

Mismo principio que `--use_codex`, con el CLI oficial **Grok Build**:
la traducción se descuenta de la suscripción de Grok (SuperGrok / X Premium+) en lugar
de facturarse por token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Aislamiento: léelo antes de usarlo.** Este provider es estructuralmente **más
débil** que `--use_codex`, y es algo deliberado:

- Codex se ejecuta en `--sandbox read-only`, una frontera impuesta por el sistema.
- El sandbox de Grok **no puede aplicarse** en muchos sistemas Linux recientes:
  AppArmor bloquea los user namespaces sin privilegios desde Ubuntu 24.04, y la lista de
  denegación de sockets del runtime de contenedores falla si `/run/podman` está en
  `0700`. Además, un perfil **integrado** que no puede aplicarse se inicia
  **sin aislamiento y en silencio**.
- Por ello, el script no solicita ningún perfil de forma predeterminada y **nunca recurre
  silenciosamente** a otra opción: muestra una advertencia. El aislamiento se basa en las
  reglas `--deny` del CLI (incluido el catch-all `*`), la única capa
  comprobada _fail-closed_: una regla desconocida hace que se rechace el inicio en lugar
  de retirar la protección sin avisar.
- Para **exigir** el sandbox del sistema operativo: `GROK_TRANSLATE_SANDBOX=read-only`. El
  inicio fallará si la máquina no puede respetarlo, que es el comportamiento deseado.

**Cuota**: el pool de Grok es **semanal y compartido** con Chat, Imagine y
Voice, y no existe ningún comando para consultarlo. Por tanto, un procesamiento por lotes
puede consumir parte de tu uso conversacional sin que nada lo indique; de ahí una
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
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opciones

| Opción                   | Descripción                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Archivo Markdown único que se traducirá                                       |
| `--source_dir`           | Directorio de origen que contiene los archivos Markdown                        |
| `--target_dir`           | Directorio de salida para los archivos traducidos                          |
| `--source_lang`          | Idioma de origen (predeterminado: `fr`)                                             |
| `--target_lang`          | Idioma de destino (predeterminado: `en`)                                              |
| `--model`                | Modelo específico que se utilizará                                             |
| `--eco`                  | Utilizar los modelos económicos                                         |
| `--use_mistral`           | Utilizar la API de Mistral AI                                                |
| `--use_claude`           | Utilizar la API de Claude                                                    |
| `--use_gemini`           | Utilizar la API de Gemini                                                    |
| `--use_codex`            | Utilizar el CLI Codex con la cuota de la suscripción de ChatGPT               |
| `--use_grok`             | Utilizar la API de xAI (Grok); requiere `XAI_API_KEY`                      |
| `--use_grok_cli`         | Utilizar el CLI Grok con la cuota de la suscripción de Grok                   |
| `--force`                | Forzar una nueva traducción                                                  |
| `--keep_filename`        | Conservar el nombre de archivo original                                     |
| `--news`                 | Modo de noticias: protege las citas EN y gestiona las banderas por idioma |
| `--add_translation_note` | Añadir una nota de traducción                                           |
| `--note_position`        | Posición de la nota: `top`, `bottom` (predeterminada) o `both`                |
| `--note_format`          | Formato de la nota: `legacy` (predeterminado, párrafo en negrita) o `marker`       |
| `--include_model`        | Incluir el nombre del modelo en el archivo de salida                       |
| `--reasoning_effort`     | Esfuerzo de razonamiento GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`    |

> **Los seis flags de provider son mutuamente excluyentes.** Antes se aceptaba combinar dos
> en silencio y se resolvía con el primero probado: una traducción solicitada con cuota de
> suscripción (`--use_codex`, `--use_grok_cli`) podía terminar facturándose por uso sin
> ninguna advertencia. `argparse` rechaza ahora esta combinación.

### Nota de traducción: posiciones y formatos

Con `--add_translation_note`, el translator puede colocar la nota arriba, abajo o en ambas posiciones,
y hacer que tenga formato de texto simple (compatible con versiones anteriores) o formato
`marker`, utilizable por un plugin de Markdown.

**Posición** (`--note_position`):

- `bottom` (predeterminada): nota al final del archivo, como históricamente.
- `top`: nota insertada **después del frontmatter YAML** (seguridad para Astro Content Collections, gray-matter, etc.).
- `both`: nota insertada ARRIBA Y ABAJO (una sola llamada al LLM, contenido reutilizado para ambas posiciones).

**Formato** (`--note_format`):

- `legacy` (predeterminado): párrafo en negrita `**...**`; comportamiento estrictamente idéntico a v1.8, byte-for-byte. Compatible con Hugo, GitHub, GitLab y cualquier renderer Markdown.
- `marker`: definición invisible de referencia de enlace Markdown (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), seguida de un blockquote en negrita. Legible de forma nativa en GitHub/GitLab y utilizable durante la compilación por un plugin remark de Astro para producir un banner estilizado (consulta el blog jls42.org).

```bash
# Compatibilité legacy (rien ne change vs v1.8)
aipmt --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
aipmt --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
aipmt --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### Modelos predeterminados (2026)

| Provider | Calidad (predeterminada)       | Económico (`--eco`)    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **Recomendación para traducciones extensas**: `--use_gemini` (predeterminado = `gemini-3.7-flash`) preserva fielmente la estructura Markdown en scripts no latinos (PL, JA, ZH, AR, HI), incluido el modo `--news`, donde la fidelidad de los placeholders es importante. Medido en este README traducido al japonés: estructura idéntica a `gemini-3.1-pro-preview` (21 listas, 18 bloques de código, 13 enlaces HTML, 13 imágenes, todas las URL preservadas) con aproximadamente 6 veces menos latencia. OpenAI sigue siendo el valor predeterminado por compatibilidad con versiones anteriores.

## Proyectos que utilizan este script

- **[jls42.org](https://jls42.org)** - Blog personal multilingüe (15 idiomas)

## Autor

Julien LE SAUX
Correo electrónico: contact@jls42.org

## Licencia

GNU GENERAL PUBLIC LICENSE Versión 3. Consulta [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artículo traducido del francés al español con gpt-5.6-luna.**

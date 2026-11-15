# Traductor de Markdown AI-Powered

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Calidad del código</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Quality Gate Status"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Security Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Reliability Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Maintainability Rating"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Coverage"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilities"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Duplicated Lines (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Technical Debt"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Lines of Code"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy Badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Traduce archivos Markdown de un idioma a otro preservando la
estructura: bloques de código, código en línea, URL, anclas, tablas y front
matter. Once formas de invocar un modelo —cinco API, cuatro suscripciones sin
facturación por uso, dos enrutadores— y una medición publicada de lo que cada
modelo preserva realmente.

## En resumen

- **Once rutas de proveedores**: API de OpenAI, Mistral, Claude, Gemini y Grok;
  suscripciones a ChatGPT (Codex), Grok, Google (Antigravity) y Claude (Claude
  Code) sin facturación por uso; enrutadores OpenCode (código abierto, gratuito o local) y OpenRouter
  (más de 400 modelos).
- **Nada incorrecto debido a un token perdido**: los bloques de código, el código en línea,
  las URL, las anclas y las citas se reemplazan por tokens antes de la llamada y se
  verifican a la vuelta. Si falta uno, el archivo no se escribe.
- **Documentos largos**: segmentación según la ventana del modelo.
- **Modo `--news`**: citas en inglés protegidas y banderas gestionadas por
  idioma, para artículos de seguimiento.
- **Modo `--eco`**: modelos rápidos y más económicos.
- **Nota de traducción** opcional, al principio, al final o en ambos.

## Instalación

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11 o posterior. Para instalar desde el repositorio, consulte
[Contribuir](#contribuir).

## Configuración

Las claves se leen en tres lugares, de mayor a menor prioridad; cada uno solo
completa lo que el anterior deja vacío.

|     | Dónde                                         | Para qué                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variables de entorno                          | CI, contenedores, excepción puntual   |
| 2   | `.env` del directorio actual (o de un padre) | una clave específica de un proyecto   |
| 3   | `~/.config/aipmt/.env`                        | instalado una vez, válido en todas partes |

```bash
mkdir -p ~/.config/aipmt
cat > ~/.config/aipmt/.env <<'EOF'
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google
OPENROUTER_API_KEY=votre-clé-api-openrouter
EOF
chmod 600 ~/.config/aipmt/.env
```

`GEMINI_API_KEY` se acepta en lugar de `GOOGLE_API_KEY`. El archivo de
usuario sigue `XDG_CONFIG_HOME` (solo ruta absoluta) e `%APPDATA%`
en Windows. Sin clave, el comando enumera las tres ubicaciones.

**El `.env` de un proyecto no puede redirigir las llamadas ni elegir el programa
ejecutado.** Proporciona claves, nunca un destino ni un binario: cualquier
variable en `_BASE_URL`, `_API_BASE`, `_ENDPOINT` o `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, los proxies (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), los almacenes de certificados (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) y `XDG_CONFIG_HOME` /
`APPDATA` se ignoran en él, con una advertencia. Un repositorio clonado no debe
poder desviar su clave ni hacer que ejecute su propio programa en la
primera traducción. Este archivo también se lee sin interpolación:
`NOM=${OPENAI_API_KEY}` no copia la clave en él. Defina estas variables en
el entorno o en `~/.config/aipmt/.env`.

Variables opcionales: `XAI_BASE_URL` (por defecto `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (segundos por llamada, por defecto 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(por defecto 600), `GROK_BIN`, `GROK_HOME` (por defecto `~/.grok`), `GROK_TIMEOUT`
(por defecto 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (por defecto 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (por defecto 600), `OPENROUTER_BASE_URL`
(`https://` requerido), `OPENROUTER_TIMEOUT` (por defecto 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (por defecto 30). Cada una se detalla en la
sección de su proveedor.

## Primeros pasos

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` traducido al español da `document-es.md` en `--target_dir`;
con `--include_model`, `document-es-gpt-6.1-terra.md`. La extensión pasa
siempre a ser `.md` —`article.mdx` da `article-en.md`— excepto con
`--keep_filename`, que conserva el nombre original. Una traducción ya existente
se omite sin `--force`.

Códigos de salida: `0` si todo tuvo éxito o se omitió, `1` si queda algún archivo
fallido (lista en la salida de error), `2` si el problema es de configuración.
Un archivo fallido nunca se escribe, incluso si la escritura en sí falla:
el contenido se escribe al lado y luego se renombra. Basta con volver a ejecutarlo.

## Qué modelo elegir

Medido en dos documentos reales, traducidos a los mismos catorce idiomas por
cada modelo. **La cifra es el número de idiomas, de catorce, donde la
traducción se escribe y nada difiere de la fuente.**

| Modelo                | Cómo acceder                      | Artículo denso de seguimiento | Este README  | Qué difiere y en cuántos idiomas                                                                                                                                   |
| --------------------- | --------------------------------- | ----------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | suscripción a Google (Antigravity) | ✅ 14/14                      | ✅ 14/14     | nada, en ninguno de los dos documentos                                                                                                                             |
| **Claude Sonnet 5.5** | clave de API de Anthropic         | ✅ 14/14                      | ✅ 14/14     | nada, en ninguno de los dos documentos                                                                                                                             |
| **Gemini 3.7 Flash**  | clave de API de Google            | ✅ 14/14                      | ⚠️ 13/14     | 1 idioma de 14: una palabra más en negrita (ja)                                                                                                                    |
| **Gemini 3.7 Flash**  | suscripción a Google (Antigravity) | ✅ 14/14                      | ⚠️ 13/14     | 1 idioma de 14: una palabra menos en negrita (ko)                                                                                                                  |
| **GPT-5.6 Sol**       | suscripción a ChatGPT o clave de OpenAI | ✅ 14/14                | ⚠️ 12/14     | 2 idiomas de 14: una palabra menos en negrita (ar, ja)                                                                                                             |
| **GLM-5.2**           | clave de OpenRouter               | ✅ 14/14                      | ⚠️ 11/14     | 3 idiomas de 14: una palabra menos en negrita (hi, ja, ko)                                                                                                         |
| Claude Sonnet 5       | suscripción a Claude (Claude Code) | ⚠️ 13/14                     | ⚠️ 13/14     | 1 idioma de 14 en el artículo: una palabra más en negrita (zh); 1 en este README: una fila de tabla pegada a la anterior, oculta al mostrarse (ar)                  |
| Claude Haiku 4.5      | suscripción a Claude (Claude Code) | ⚠️ 11/14                     | ✅ 14/14     | 3 idiomas en el artículo: un título de sección pasado a nivel 1 (en, pl, ro); en este README, nada para el comparador, pero los enlaces internos duplicados en inglés |
| Claude Sonnet 5       | clave de API de Anthropic         | ⚠️ 11/14                      | ⚠️ 12/14     | 3 idiomas en el artículo: apareció un bloque de código (es, de, hi); 2 en este README: un enlace sin su marcado (sv), una palabra en negrita (zh)                    |
| Claude Haiku 4.5      | clave de API de Anthropic         | ⚠️ 7/14                       | ✅ 14/14     | 7 idiomas en el artículo: un título de sección pasado a nivel 1 —en japonés, se quedó en francés—; nada en este README                                            |
| Claude Haiku 5.5      | clave de API de Anthropic         | ⚠️ 11/14                      | ❌ 12/14     | 3 idiomas en el artículo: un título de sección cambió de nivel o se duplicó (ja, ko, zh); en este README, 2 idiomas rechazados, códigos en línea perdidos (ar, hi)  |
| Qwen 3.7 Flash        | clave de OpenRouter               | ❌ 8/14                       | ⚠️ 10/14     | 1 idioma rechazado en el artículo, otros 5 difieren; en este README, unas cuarenta palabras puestas en `code` (ar)                                          |
| Grok 4.6              | suscripción a Grok                | ❌ 8/14                       | no evaluado  | 5 idiomas de 14 rechazados por falta de códigos en línea y URL devueltos; el neerlandés difiere en todo                                                           |
| GPT-OSS 20B           | modelo local (Ollama)             | ❌ 7/14                       | no vuelto a medir | 4 idiomas de 14 rechazados: el modelo dejaba pasajes en francés, las salvaguardas los detuvieron                                                                |
| MiMo v2.5 (gratuito)  | OpenCode Zen, sin cuenta          | ❌ 11/14                      | no vuelto a medir | 1 idioma rechazado; una sección perdida en polaco                                                                                                                 |
| Mistral Large         | clave de API de Mistral           | ❌ 5/14                       | ❌ 1/14      | **desaparece una sección entera**: 1 idioma en el artículo (hi), 3 en este README (ar, hi, ko) —y 3 idiomas rechazados en el artículo                             |
| DeepSeek V4 Flash     | clave de OpenRouter               | ❌ 3/14                       | no vuelto a medir | 10 idiomas de 14 rechazados; 37 minutos por idioma                                                                                                                |
| Claude Opus 5.5       | suscripción a Claude (Claude Code) | ❌ 0/14                      | ✅ 14/14     | el artículo fue rechazado en los 14 idiomas por las salvaguardas de Opus debido a una noticia breve de biología; nada en este README                              |

|     | Lo que significa el símbolo                                                                                                                                                                           |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | los catorce idiomas traducidos y nada difiere de la fuente                                                                                                                                            |
| ⚠️  | los catorce idiomas traducidos; lo que difiere es de **marcado** —una palabra en negrita, un `code`, un enlace que pierde sus corchetes. No falta ningún texto, ninguna URL, ningún bloque de código ni ninguna sección |
| ❌  | al menos un idioma no se pudo traducir —el archivo se rechaza, no se escribe— **o** falta contenido en un archivo escrito                                                                           |

Lo que hay que tener en cuenta:

- **Una traducción rechazada no es una traducción dañada.** Cuando falta un token
  a la vuelta, el archivo no se escribe y el idioma cuenta como
  rechazado. Esto es lo que le ocurre a Grok en el artículo: cuatro códigos en línea y
  tres URL perdidos ya desde el primer segmento, en las cinco escrituras no latinas.
- **Un modelo puede rechazar un documento entero por una sola frase.** Opus 5.5
  traduce este README sin una sola discrepancia, pero ningún artículo de seguimiento: sus
  salvaguardas detienen la respuesta ante una noticia breve de biología. El archivo no se
  escribe y aipmt indica el motivo.
- **Esta red no cubre los títulos, las tablas, el front matter ni el
  texto.** Un modelo que elimina una sección genera un archivo que la herramienta escribe
  sin dudar —este es el caso de Mistral—. Estos elementos no se pueden
  reemplazar por un token y las comprobaciones actuales no los controlan;
  `scripts/compare_structure.py` detecta una sección perdida, pero a posteriori.
- **Grok no tiene puntuación en este README**: su sesión de CLI expiró tras doce
  idiomas, once de ellos sin discrepancias. Una campaña interrumpida no se evalúa.
- **La densidad del documento importa más que el idioma.** Grok rinde bien con
  README ordinarios y falla en un artículo cargado de enlaces, incluso en
  neerlandés.

Fechas y documentos: la columna «Este README» se midió el 9 de septiembre de 2026
en una revisión fija de este archivo (785 líneas, 285 códigos en línea, 89 filas
de tabla), retocada desde entonces —excepto las filas de Antigravity y Claude Code,
medidas el 26 de septiembre en la revisión publicada con la 1.14.0, más corta
(600 líneas, 257 códigos en línea, 85 filas de tabla), y las filas de Claude
Sonnet 5.5, Haiku 5.5 y Haiku 4.5 mediante API, medidas el 18 de octubre en la
misma revisión. La columna «Artículo denso de seguimiento» procede de la campaña del
4 y 5 de septiembre sobre un artículo de 589 líneas, excepto la fila de Grok, medida de nuevo el
9 de septiembre en otra edición del mismo seguimiento, las filas de Antigravity y
Claude Code, medidas el 26 de septiembre en el mismo artículo, y esas tres filas de
Claude, el 18 de octubre. Las tablas completas, las duraciones y el protocolo se
encuentran en [Mediciones detalladas](#mediciones-detalladas).

## Todas las opciones

| Opción                   | Descripción                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Archivo Markdown único a traducir (alternativa a `--source_dir`)                                             |
| `--source_dir`           | Directorio de origen que contiene los archivos Markdown (por defecto: `content/posts`)                                   |
| `--target_dir`           | Directorio de salida para los archivos traducidos (por defecto: `traductions_en`)                                    |
| `--source_lang`          | Idioma de origen (por defecto: `fr`)                                                                                  |
| `--target_lang`          | Idioma de destino (por defecto: `en`)                                                                                   |
| `--model`                | Modelo específico a utilizar                                                                                  |
| `--eco`                  | Usar los modelos económicos                                                                              |
| `--use_mistral`          | Usar la API de Mistral AI                                                                                     |
| `--use_claude`           | Usar la API de Claude                                                                                         |
| `--use_gemini`           | Usar la API de Gemini                                                                                         |
| `--use_grok`             | Usar la API de xAI (Grok) — requiere `XAI_API_KEY`                                                           |
| `--use_codex`            | Usar la CLI de Codex con la cuota de la suscripción a ChatGPT                                                    |
| `--use_grok_cli`         | Usar la CLI de Grok con la cuota de la suscripción a Grok                                                        |
| `--use_antigravity`      | Usar la CLI de Antigravity (`agy`) con la cuota de la suscripción a Google AI Pro o Ultra                       |
| `--use_claude_code`      | Usar la CLI de Claude Code (`claude -p`) con la cuota de la suscripción a Claude Pro o Max                      |
| `--use_opencode`         | Usar OpenCode (código abierto) hacia el proveedor configurado en OpenCode; requiere `--model provider/modèle` |
| `--use_openrouter`       | Usar OpenRouter — requiere `OPENROUTER_API_KEY` y `--model fournisseur/modèle`                          |
| `--force`                | Forzar la retraducción                                                                                       |
| `--keep_filename`        | Conservar el nombre de archivo original                                                                          |
| `--news`                 | Modo noticias: protege las citas en EN, gestiona las banderas por idioma                                      |
| `--add_translation_note` | Añadir una nota de traducción                                                                                |
| `--note_position`        | Posición de la nota: `top`, `bottom` (por defecto) o `both`                                                     |
| `--note_format`          | Formato de la nota: `legacy` (por defecto, párrafo en negrita) o `marker`                                            |
| `--include_model`        | Incluir el nombre del modelo en el archivo de salida                                                            |
| `--reasoning_effort`     | Esfuerzo de razonamiento de GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

Los nueve flags `--use_*` son mutuamente excluyentes: combinar dos de ellos se
rechaza.

## Proveedores

### Por API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` cambia al nivel económico de cada proveedor.

| Proveedor   | Calidad (por defecto)                                                | Económico (`--eco`) |
| ----------- | -------------------------------------------------------------------- | --------------------------- |
| OpenAI      | `gpt-6.1-terra`                                                      | `gpt-6-luna`             |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-4-hydrogen`                                                  | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (también `gpt-5.6-sol`, `terra` y `luna` mediante `--model`) | `gpt-6-luna`              |
| Grok API    | `grok-4.7`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | ídem — `--eco` sin efecto |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.8-flash-low`    |
| Claude Code | `sonnet`, esfuerzo `low`                                               | ídem — `--eco` sin efecto |
| OpenCode    | `--model provider/modèle` obligatorio                                | ídem — `--eco` sin efecto |
| OpenRouter  | `--model fournisseur/modèle` obligatorio                             | ídem — `--eco` sin efecto |

Los valores por defecto siguen la última generación de cada proveedor, evaluada
antes de ser adoptada: GPT-6 en OpenAI, Gemini 4 Hydrogen en Google,
Grok 4.7 en xAI desde la versión 1.19.0. Los modelos anteriores siguen siendo aceptados
mediante `--model` (`gpt-5.6-terra`, `gemini-3.8-flash`, `grok-4.6`…), al igual que
Gemini 4 Argon y Carbon, la gama alta de Google. aipmt ajusta por sí mismo
el esfuerzo de razonamiento de los GPT y Grok, desactivado en `--eco`, y
`--reasoning_effort` lo fuerza; un Gemini siempre recibe el nivel más
bajo que admita.
Una caída temporal de la API de Gemini (503, 429, tiempo de espera agotado) reintenta
la llamada hasta tres veces, tras 10, 20 y luego 40 segundos. Un intento
que quede sin respuesta se abandona al cabo de 5 minutos y luego se reintenta
del mismo modo: un servidor mudo hace fallar el segmento en unos veinte minutos
como máximo, en lugar de bloquear indefinidamente.

### Con la suscripción a ChatGPT: `--use_codex`

Controla la CLI oficial de Codex: la traducción se descuenta de la cuota de
la suscripción a ChatGPT, sin clave de API ni facturación por uso.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- El binario se busca en `CODEX_BIN`, luego en el `PATH` y después en el paquete
  `openai-codex-cli-bin`. `~/.codex/auth.json` nunca se lee.
- `OPENAI_API_KEY` y `CODEX_API_KEY` se eliminan del entorno del
  subproceso: una clave presente nunca hace cambiar a la API.
- Cada segmento cuesta al menos un «mensaje» de la ventana de 5 horas — dos
  si su validación falla y se reintenta. OpenAI anuncia, a modo
  de estimación, entre 250 y 2000 mensajes/5 h para `gpt-5.6-luna`, el económico hasta la
  versión 1.18.0, y entre 10 y 100 para `gpt-5.6-sol` en un plan Plus.
- `--model gpt-5.6-sol`, el valor predeterminado hasta la versión 1.16.3, `--model gpt-5.6-terra`
  y `--model gpt-5.6-luna` también funcionan con la suscripción.
- Un error 429 del servidor no hace perder el archivo: Codex se reconecta solo,
  aipmt espera al final del turno y, si el 429 prevalece, el segmento
  se reinicia tras 30 y luego 60 segundos. Un modelo al que la cuenta no tiene derecho devuelve un 400 «model is
  not supported when using Codex with a ChatGPT account».
- Más lento que una API, y la diferencia aumenta con el documento: en este README,
  6 min 46 s por idioma de mediana con `gpt-5.6-sol`, frente a 36 s con
  `gemini-3.7-flash`.
- Rechazado en CI (`CI` o `GITHUB_ACTIONS` definido): la suscripción se autentica
  mediante un archivo de sesión personal, que no debe estar en un runner
  compartido.
- Variables: `CODEX_BIN`, `CODEX_TIMEOUT` (segundos por segmento, por defecto 600).

### Con la suscripción a Grok: `--use_grok_cli`

Mismo principio con la CLI oficial de Grok Build, con la suscripción a SuperGrok o
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Aislamiento más débil que Codex.** El sandbox del SO de Grok no se aplica
  en muchos equipos Linux recientes (AppArmor, sockets de runtime de
  contenedores), y un perfil que no se puede aplicar se inicia sin aislamiento de
  forma silenciosa. Por lo tanto, el script no solicita ningún perfil por defecto, lo notifica y
  se apoya en las reglas `--deny` de la CLI, incluido el catch-all `*` —la única
  capa que rechaza iniciar en lugar de eliminar la protección sin
  avisar—. `GROK_TRANSLATE_SANDBOX=read-only` exige el sandbox del SO, y el inicio
  falla si la máquina no puede cumplirlo.
- La cuota es semanal, compartida con Chat, Imagine y Voice, y ningún
  comando permite consultarla: un lote puede consumir el uso conversacional
  sin aviso previo.
- Variables: `GROK_BIN`, `GROK_HOME` (directorio de la CLI, por defecto `~/.grok`),
  `GROK_TIMEOUT` (por defecto 900), `GROK_TRANSLATE_SANDBOX`.

### Con la suscripción a Google: `--use_antigravity`

Mismo principio con `agy`, la CLI oficial de Antigravity: para quien paga Google
AI Pro o Ultra, la traducción se descuenta de la cuota de la suscripción en lugar
de facturarse por token. Es la única vía hacia esta cuota: Gemini CLI ya no
da servicio a estas cuentas desde el 18 de junio de 2026
([anuncio](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
y el SDK de Antigravity solo acepta una clave de API o un proyecto de Google Cloud.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Ninguna vía de pago permanece abierta.** agy solo recibe de su
  entorno una lista cerrada de variables — `PATH`, idioma y zona horaria,
  terminal, identidad, proxies y certificados, bus de sesión — y ninguna clave:
  varias de sus variables redirigen una llamada sin mostrar nada (comprobado:
  una envía el documento a una pasarela de terceros, otra a un proyecto
  de Google Cloud facturado), y una lista de bloqueo omitía alguna en cada revisión.
  Antes de cualquier segmento, `agy -p /config`, que no consume cuota, debe mostrar
  los créditos de IA de pago desactivados, sin clave de API ni proyecto de Google Cloud —un
  ajuste ausente equivale a rechazo—; de lo contrario, no se traduce nada; el registro de cada
  llamada debe certificar a continuación la suscripción (`authMethod=consumer`), o de lo contrario
  la respuesta es rechazada.
- **Aislamiento.** Cada llamada se ejecuta en un directorio personal privado y
  desechable, con un agente de traducción sin herramientas: sus ajustes, reglas,
  plugins, servidores MCP y hooks de agy no entran allí, nada se añade a su
  historial y la sesión permanece en el llavero, que aipmt nunca lee.
  Un agente no encontrado hace que agy recurra silenciosamente a su agente de programación
  y a sus herramientas: una línea completa del registro debe confirmar el agente correcto —un
  documento que cite este mensaje no la reemplaza—; de lo contrario, se rechaza.
- **Plataformas**: Linux, en una sesión que disponga de un llavero (bus de sesión
  D-Bus, Secret Service); macOS se acepta, sin haber sido probado en él. Rechazado
  en Windows, donde agy no lee las variables que aíslan cada llamada, y
  en Linux sin bus de sesión —sesión SSH, contenedor, servidor: agy
  guarda allí su token en un archivo de `~/.gemini`, que el aislamiento oculta. El
  rechazo se produce antes de cualquier ejecución, indicando su causa, en lugar de esperar
  un minuto por un código de inicio de sesión.
- **Modelos**: los de `agy models`. Los Gemini llevan el esfuerzo en su nombre
  (`gemini-3.8-flash-medium`…): un nombre sin sufijo se rechaza antes de la llamada,
  y `--reasoning_effort` no tiene efecto. Por defecto `gemini-3.8-flash-medium`,
  y `gemini-3.8-flash-low` en `--eco`, desde que agy ya no ofrece Gemini 3.7
  Flash; la campaña que fijó el valor por defecto se
  describe en [Mediciones detalladas](#mediciones-detalladas). Gemini 4 Hydrogen
  (`gemini-4-hydrogen-low`…) comparte la cuota de 3.8 Flash y consume
  más: 0,95 puntos de la ventana de 5 horas para este README con esfuerzo
  medio, frente a 0,32. Claude y GPT-OSS
  tienen su propia cuota, mucho más reducida: aproximadamente el 1 % de la ventana de
  5 horas por llamada medida, frente al 0,05 % en Flash. Gemini 4 Argon tiene la
  suya, semanal: este README consume el 1,35 % de ella.
- **Cuota**: por grupo, una ventana de 5 horas y una semanal, al
  prorrateo del coste en tokens. Medido en la cuenta del autor: unos
  16 puntos de la ventana de 5 horas por millón de caracteres de origen en
  `gemini-3.8-flash-medium`, 14 en `gemini-3.7-flash-medium` y de 7 a 8 con
  esfuerzo bajo —un README de 40 000 caracteres cuesta por tanto algo más de
  medio punto—. La limitación semanal depende del nivel. El reintento sigue
  lo que agy declara como reintentable; de no ser así, una ventana agotada nunca se
  reintenta: hace fallar cada archivo hasta el restablecimiento
  que muestra `/usage`.
- **Más lento que la API**: en el artículo denso de mediciones, 3 min 59 s por
  idioma de mediana en `gemini-3.8-flash-medium` y 3 min 14 s en
  `gemini-3.7-flash-medium`, frente a 1 min 18 s para Gemini 3.7 Flash mediante la API.
- **Interrupción**: Ctrl-C, o una terminal cerrada, detienen agy junto con la
  orden en lugar de dejar que termine su turno consumiendo su cuota; lo mismo aplica
  para Codex, Grok CLI y OpenCode. Con `nohup`, la traducción continúa.
- Rechazado en CI (`CI` o `GITHUB_ACTIONS` definido): la sesión reside en un
  llavero personal. En un runner, use `--use_gemini` con `GOOGLE_API_KEY`.
- Variables: `AGY_BIN` (de lo contrario el `PATH`, luego `~/.local/bin/agy`),
  `AGY_TIMEOUT` (segundos por segmento, inicio incluido, por defecto 900).

**Condiciones de uso: es su cuenta la que está en juego.** Las
[condiciones de Antigravity](https://antigravity.google/terms) (sección 6) y su
[FAQ](https://antigravity.google/docs/faq/) prohíben acceder al servicio
mediante software de terceros utilizando la sesión de Antigravity —Claude Code,
OpenClaw y OpenCode se mencionan allí—, bajo pena de suspensión de la cuenta. aipmt
no lee ni reutiliza el token: ejecuta el binario oficial en el
[modo headless](https://antigravity.google/docs/cli/headless/) que Google
documenta para scripts y CI. Un miembro de Google consideró «estándar»
ejecutar `agy -p` desde un script local para su propio trabajo
([foro oficial, 25 de septiembre de 2026, respuesta no vinculante](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
ningún texto resuelve de forma definitiva el caso de una herramienta distribuida como esta.

**Solo documentos públicos.** Según la sección 5 de las mismas condiciones, las
interacciones —prompts, respuestas, metadatos— pueden utilizarse para mejorar los
productos y el aprendizaje automático de Google, y ser revisadas por
humanos, incluso con una suscripción de pago. La exclusión se realiza mediante el ajuste
`enableTelemetry`, cuyo efecto no está documentado, el cual aipmt no configura; sus ajustes
de agy no se conservan en su aislamiento. No procese nada confidencial a través de él.

### Sobre la suscripción a Claude: `--use_claude_code`

El mismo principio con `claude`, la CLI oficial de Claude Code, en modo `-p`: para
quien paga Claude Pro o Max, la traducción se descuenta de la cuota de
la suscripción en lugar de facturarse por token. No confundir con
`--use_claude`, la API de Anthropic, facturada por uso.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **No queda abierta ninguna vía de pago, y cada llamada lo demuestra.** Claude
  Code solo recibe de su entorno una lista cerrada de variables: ni
  clave de API, ni token, ni proveedor en la nube, ni marcador de la sesión de Claude Code
  desde donde se iniciaría aipmt. Antes del primer segmento, `claude auth status` debe
  mostrar la conexión de la suscripción, sin clave de Console, y `/usage`, que no consume
  cuota alguna, debe certificarlo; cada llamada lo certifica a su vez en su
  evento de inicialización, de lo contrario la respuesta es rechazada.
- **Desactive el «extra usage»** (claude.ai, Configuración → Uso) para
  mantener el coste en cero euros: si está activado, toma el relevo de una ventana agotada y
  factura sin mostrar ningún error. aipmt detiene la traducción en cuanto el informe
  de cuota de una llamada lo señala, pero esa llamada en particular ya se habrá contabilizado.
- **Cuota compartida con sus sesiones de Claude Code.** Cada llamada reporta
  el uso de las ventanas de 5 horas y de la semana; por encima del 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`), no se lanza ningún segmento adicional, para
  no agotar lo que sirve para su trabajo.
- **Aislamiento.** Cada llamada se ejecuta sin herramientas, en un directorio privado y
  desechable, en modo sin personalización: no se cargan ni sus `CLAUDE.md`, ni sus plugins,
  hooks, servidores MCP o ajustes, y no se conserva nada de la
  sesión. Los archivos adjuntos están bloqueados: un `@chemin` en su documento
  sigue siendo texto y no abre ningún archivo (medido).
- **Modelos**: `sonnet` por defecto, con esfuerzo `low`, y también en `--eco`:
  `--eco` no cambia nada en esta ruta. Medidos sobre los mismos documentos, `haiku`
  es el doble de lento —razona sin que se pueda evitar— para
  un coste apenas inferior, y `opus` rechaza contenidos de biología (siguiente
  punto). Ambos siguen siendo accesibles mediante `--model`; estos alias siguen al
  último modelo de su familia. `fable` y las variantes `[1m]` son rechazados,
  porque pasan a créditos de pago. `--reasoning_effort` ajusta el esfuerzo,
  del cual una traducción no saca provecho: el razonamiento medido es nulo o casi nulo.
- **Opus rechaza ciertos contenidos de biología.** Sus medidas de seguridad son más
  estrictas que las de Sonnet, y el mensaje de error de Anthropic advierte de que
  «can sometimes flag biology-research-adjacent work». Medido: una nota breve de
  actualidad sobre 279 moléculas generadas provocó el rechazo del artículo en los catorce
  idiomas. No se escribe nada: aipmt rechaza la respuesta cortada, señala las
  medidas de seguridad y aconseja `--model sonnet`.
- Rechazado en CI (`CI` o `GITHUB_ACTIONS` definido) y en Windows (no medido).
- Variables: `AIPMT_CLAUDE_BIN` (si no, el `PATH`, luego `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (segundos por segmento, por defecto 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (por defecto 0.8), `CLAUDE_CONFIG_DIR` (la cuenta de
  Claude Code, nunca tomada de un `.env` de proyecto); directorios de trabajo bajo
  `XDG_CACHE_HOME/aipmt/claude-code` (por defecto `~/.cache`).

**Términos de servicio: es su cuenta la que está comprometida.** La
[página legal de Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
no impide «an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription»: esto es lo que hace aipmt, que inicia el
binario oficial y nunca lee el token. Sin embargo, Anthropic «does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users», prefiere la clave de API para herramientas
de terceros, «including open-source projects», y se reserva el derecho de computar su
uso sobre los créditos de pago
([ayuda de Claude](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Ningún texto resuelve claramente el caso de una herramienta distribuida que lanza el binario.

**Datos**: en las cuentas Free, Pro y Max, el entrenamiento de modelos
se aplica también a Claude Code cuando el ajuste de privacidad lo permite
([página de datos](https://code.claude.com/docs/en/data-usage)). aipmt no conserva
ninguna transcripción local (`--no-session-persistence`). No procese
nada confidencial por aquí.

### Hacia el proveedor de su elección: `--use_opencode`

[OpenCode](https://opencode.ai) es un agente de código de código abierto (MIT) que
enruta hacia los proveedores configurados en su interior: clave de API, suscripción,
pasarela OpenCode Zen (modelos gratuitos, sin cuenta) o modelo local. Se han
medido de extremo a extremo dos vías aquí: Zen y Ollama.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur

# gratuit, sans compte ni clé — données utilisables pour l'entraînement
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en
# local, hors ligne
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de
# sur un abonnement déjà payé
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

`--model` es obligatorio: sin él, OpenCode recurriría a un modelo gratuito
cuyas interacciones pueden servir para el entrenamiento, y esa elección no debe tomarse
en su lugar.

Aislamiento en cada llamada:

- una configuración en línea, prioritaria sobre la suya, define un agente `aipmt`
  cuyas herramientas quedan todas denegadas (`permission: { "*": "deny" }`), uso compartido de
  sesión desactivado, `--pure`, nunca `--auto`;
- directorio de trabajo desechable y vacío, `OPENCODE_DISABLE_PROJECT_CONFIG` y
  `OPENCODE_DISABLE_CLAUDE_CODE` colocados —sin ellos, OpenCode inyecta en el
  prompt el `AGENTS.md` del directorio actual y `~/.claude/CLAUDE.md`. El
  `~/.config/opencode/AGENTS.md` global sigue inyectándose, OpenCode no permite
  excluirlo;
- contrato de salida: código de retorno 0, ningún evento `error`, ninguna llamada
  a herramientas, último paso en `stop`, texto no vacío, y el agente `aipmt`
  efectivamente cargado —un `--agent` desconocido no hace fallar a OpenCode, sino que
  recurre en silencio al agente de codificación;
- no se transmite ninguna clave de `aipmt`, salvo `OPENCODE_API_KEY`, la clave
  del propio OpenCode. Los proveedores se configuran dentro de OpenCode, no en
  el `.env` de `aipmt`.

A tener en cuenta:

- Los modelos gratuitos de Zen son variables, con límites no documentados, y
  sus interacciones pueden servir para el entrenamiento: adecuados para documentación
  pública, no para contenido privado.
- Un modelo local debe ofrecer al menos 16 k tokens de contexto, ya que los segmentos
  alcanzan hasta 16 000 caracteres. Ollama suele configurar 4 096: pasar
  por un `Modelfile` con `PARAMETER num_ctx 32768`.
- `--eco` no tiene efecto; `--reasoning_effort` se transmite tal cual como
  `--variant` de OpenCode.
- OpenCode registra cada sesión en `~/.local/share/opencode/`.
- Variables: `OPENCODE_BIN` (si no, el `PATH`, luego `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (segundos por segmento, por defecto 600). `OPENCODE_CONFIG`
  se pasa tal cual a OpenCode.

Ejemplo de un modelo local a través de Ollama, en `~/.config/opencode/opencode.json`:

```bash
ollama pull gpt-oss:20b
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": { "baseURL": "http://127.0.0.1:11434/v1" },
      "models": {
        "gpt-oss-20b-32k": {
          "name": "gpt-oss 20B (32k, sans réflexion)",
          "limit": { "context": 32768, "output": 8192 },
          "options": { "reasoningEffort": "none" }
        }
      }
    }
  }
}
```

`reasoningEffort: "none"` desactiva la reflexión que Ollama activa por defecto en estos
modelos, y que un Modelfile no puede desactivar. Medido en una frase de
seis palabras: 919 tokens de reflexión y 68 segundos sin la opción, 9 tokens con ella.

### Hacia más de 400 modelos: `--use_openrouter`

OpenRouter es un enrutador facturado por uso, con un crédito único, frente a
modelos alojados por terceros —incluidos los modelos abiertos chinos que ningún
otro proveedor expone aquí.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` es obligatorio. Un preflight, ejecutado antes de cualquier facturación, resuelve
dos particularidades del enrutamiento:

- **Un mismo modelo es servido por decenas de proveedores con límites
  diferentes** —en `z-ai/glm-5.3-flash`, 23 proveedores, incluido uno limitado a
  2 048 tokens de salida. El preflight lee `/api/v1/models/{modèle}/endpoints`,
  descarta los proveedores por debajo de 8 000 tokens de salida o con estado degradado, y
  fija a los demás con `allow_fallbacks: false`.
- **El razonamiento se factura a la tarifa de salida** —107 tokens frente a 2 en
  una respuesta «OK» de `z-ai/glm-5.2`. Está desactivado por defecto; los modelos
  que lo imponen reciben el esfuerzo más bajo que acepten, ya que el valor por defecto del
  catálogo puede saturar la salida antes de que finalice la traducción.
  `--reasoning_effort` sigue teniendo prioridad.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- La ventana de contexto procede del catálogo. Un modelo por debajo de 16 400 tokens se
  rechaza antes de cualquier llamada: 8 400 para el prompt y el segmento, 8 000 de salida
  como mínimo.
- Un slug ausente en el catálogo, un catálogo inaccesible o la falta de un
  proveedor que soporte el límite detienen el comando.
- `finish_reason=length` con una salida vacía es un presupuesto consumido por el
  razonamiento, no un truncamiento: el mensaje lo distingue.
- `--eco` no tiene efecto.
- Variables: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (por defecto `https://openrouter.ai/api/v1`, `https://`
  requerido), `OPENROUTER_TIMEOUT` (por defecto 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (por defecto 30).

### Nota de traducción

`--add_translation_note` añade una nota, en `bottom` (por defecto), `top` (después del
front matter) o `both` (`--note_position`), con formato `legacy` (párrafo en
negrita, por defecto) o `marker` (`--note_format`). El formato `marker` es una
definición de referencia de Markdown invisible,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
seguida de una cita en negrita: legible en GitHub, procesable durante la compilación mediante un
plugin de remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Mediciones detalladas

Todas las mediciones son traducciones ejecutadas realmente con `aipmt`, hacia
catorce idiomas: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Escritas** contabiliza los archivos que los filtros de control dejaron pasar; **Sin
discrepancias** aquellos donde `scripts/compare_structure.py` no detecta nada: mismo número de
secciones, subtítulos, enlaces, URL distintas, bloques de código,
códigos en línea, filas de tabla, bloques de cita y palabras en negrita.

«Sin discrepancias» significa «nada detectado», no «idéntico»: el comparador
cuenta elementos sin leer su contenido. No señala ni un encabezado de
nivel 4 eliminado, ni el texto de un código en línea reemplazado, ni una bandera
intercambiada, ni un enlace interno generado con un paréntesis de más,
`[texte]((#ancre))`, que ya no conduce a ninguna parte —y no evalúa el
idioma.

### Artículo denso de seguimiento tecnológico, modo `--news`

Una edición del [boletín de IA de jls42.org](https://jls42.org/fr/news):
589 líneas, 140 enlaces, 21 secciones, 3 citas en inglés protegidas. Campaña
del 4 y 5 de septiembre de 2026.

| Modelo                                          | Acceso              | Escritas | Sin discrepancias | Mediana/idioma |
| ----------------------------------------------- | ------------------ | ------- | ----------------- | -------------- |
| `gemini-3.7-flash`                              | API de Google      | 14/14   | ✅ **14/14**      | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | suscripción Google | 14/14   | ✅ **14/14**      | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | suscripción Google | 14/14   | ✅ **14/14**      | 3 min 14 s     |
| `claude-sonnet-5-5`                             | API de Anthropic   | 14/14   | ✅ **14/14**      | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | suscripción ChatGPT| 14/14   | ✅ **14/14**      | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14**      | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14**      | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | suscripción Claude | 14/14   | ⚠️ 13/14          | 6 min 49 s     |
| `claude-sonnet-5`                               | API de Anthropic   | 14/14   | ⚠️ 11/14          | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | suscripción Claude | 14/14   | ⚠️ 11/14          | 15 min 54 s    |
| `claude-haiku-5-5`                              | API de Anthropic   | 14/14   | ⚠️ 11/14          | 2 min 54 s     |
| `claude-haiku-4-5`                              | API de Anthropic   | 14/14   | ⚠️ 7/14           | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14          | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14           | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | local              | 10/14   | ❌ 7/14           | 12 min 39 s    |
| `mistral-large-latest`                          | API de Mistral     | 11/14   | ❌ 5/14           | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14           | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | suscripción Grok   | 1/14    | ❌ 1/14           | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | suscripción Claude | 0/14    | ❌ 0/14           | —              |

Grok se volvió a medir el 9 de septiembre en otra edición del mismo boletín
(356 líneas): 9 idiomas escritos de 14, 8 sin discrepancias. Esta es la cifra que
figura en la tabla principal. Tres campañas interrumpidas no están
registradas: `qwen3.5-27b` (9 idiomas) y `kimi-k2.6` (4) por falta de crédito,
`z-ai/glm-5.3-flash` cuyos dos fallos se debieron a un ajuste de razonamiento
que el proveedor ha corregido desde entonces. Las filas de OpenRouter se midieron con los
ajustes por defecto del enrutador, antes de `--use_openrouter`; `z-ai/glm-5.2`,
vuelto a medir con el proveedor entregado, arroja el mismo 14/14. Las cifras se
recalcularon el 10 de septiembre con el comparador actual: `qwen3.8-flash` y
`qwen3.7-flash` ganan cada uno un idioma respecto a la primera
publicación, los demás permanecen sin cambios.

Las filas de `--use_antigravity` se midieron el 26 de septiembre sobre el mismo
artículo, cuatro traducciones en paralelo: `gemini-3.7-flash-medium` por la mañana,
`gemini-3.8-flash-medium` por la tarde. En inglés, cada uno retiró por sí mismo
las tres líneas de traducción al francés bajo las citas, sin inventar ninguna
bandera, y las citas en inglés quedaron intactas: la limpieza de respaldo no tuvo
nada que hacer. En `--eco` (`gemini-3.7-flash-low`), en solo cuatro idiomas
(en, ja, ar, hi): 4 escritas de 4, todas sin discrepancias, 1 min 52 s de
mediana. Prueba de contraste el mismo día en una edición más reciente del boletín,
la del 25 de septiembre (438 líneas, 2 citas en inglés), traducida fuera del
blog mediante `gemini-3.7-flash-medium`: 14 escritas de 14, todas sin discrepancias, de 87 a
128 s por idioma.

Las filas de `--use_claude_code` se midieron el 26 de septiembre sobre el mismo
artículo, cuatro traducciones en paralelo, con esfuerzo `low`. Con `sonnet`, las
citas en inglés quedaron intactas en los catorce idiomas y, en inglés, el
modelo retiró por sí mismo las líneas de traducción al francés, sin inventar ninguna
bandera. `opus` no escribió ningún idioma: en cada uno, sus filtros de seguridad
detuvieron la respuesta en el último segmento, debido a una nota breve sobre 279 moléculas
generadas para un sitio de unión. Enviada de forma aislada, esta nota es rechazada
bajo la categoría «bio»; `sonnet` la tradujo en todos los casos. `haiku` escribe
los catorce idiomas; en tres (en, pl, ro), un título de sección pasa del
nivel 2 al nivel 1. Razona sin que se pueda evitar —el 61 % de
sus tokens de salida—, de ahí más del doble de tiempo que `sonnet`.

Las filas `claude-sonnet-5-5`, `claude-haiku-5-5` y `claude-haiku-4-5` se
midieron el 18 de octubre mediante la API de Anthropic, sobre el mismo artículo, cuatro
traducciones en paralelo por modelo. Sonnet 5.5 no permite que se desactive su
reflexión: aipmt le envía el ajuste más bajo que acepta, y sus
respuestas no contienen ninguna. Escribe los catorce idiomas sin discrepancias y sin
volver a procesar ningún segmento; en inglés, retiró por sí mismo las líneas de
traducción al francés, sin inventar ninguna bandera, y las citas en inglés quedaron
intactas en todas partes. Haiku 5.5 se mide con su reflexión adaptativa: con la reflexión
desactivada, dejaba párrafos enteros en francés, que el filtro rechaza —
3 idiomas escritos de 14. Ambos Haiku tropiezan con la misma nota breve: Haiku 5.5
cambia el nivel de su título o lo duplica en japonés, coreano y
chino; Haiku 4.5 lo cambia al nivel 1 en siete idiomas, y lo deja en
francés en japonés. Haiku 4.5 cuesta 3,67 $ para los dos documentos en los
catorce idiomas, Haiku 5.5 cuesta 0,57 $, Sonnet 5.5 cuesta 9,21 $.

### README de este proyecto, Markdown estándar

Revisión fijada el 9 de septiembre de 2026: 785 líneas, 285 códigos en línea, 40
cierres de bloques, 89 líneas de tabla. Cuatro traducciones en paralelo.

| Modelo                                          | Escritas | Sin discrepancias | Mediana/idioma | Lo que difiere                                                           |
| ----------------------------------------------- | -------- | ----------------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14    | ✅ 14/14          | 1 min 43 s     | nada                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14    | ✅ 14/14          | 1 min 48 s     | nada                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14    | ✅ 14/14          | 4 min 02 s     | nada para el comparador; enlaces internos duplicados (en)                |
| `claude-sonnet-5-5`                             | 14/14    | ✅ 14/14          | 1 min 18 s     | nada                                                                     |
| `claude-haiku-4-5`                              | 14/14    | ✅ 14/14          | 2 min 06 s     | nada                                                                     |
| `gemini-3.7-flash`                              | 14/14    | ⚠️ 13/14          | 36 s           | una palabra en negrita (ja)                                              |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14    | ⚠️ 13/14          | 1 min 22 s     | una palabra en negrita (ko)                                              |
| `sonnet` (`--use_claude_code`)                  | 14/14    | ⚠️ 13/14          | 2 min 20 s     | una fila de tabla pegada a la anterior (ar)                              |
| `claude-sonnet-5`                               | 14/14    | ⚠️ 12/14          | 2 min 56 s     | un enlace (sv), una palabra en negrita (zh)                              |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14    | ⚠️ 12/14          | 6 min 46 s     | una palabra en negrita (ar, ja)                                          |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14    | ⚠️ 11/14          | 2 min 34 s     | una palabra en negrita (hi, ja, ko)                                      |
| `qwen/qwen3.7-flash`                            | 14/14    | ⚠️ 10/14          | 2 min 17 s     | 40 códigos en línea añadidos en árabe; negrita (hi, ja, ko)              |
| `claude-haiku-5-5`                              | 12/14    | ❌ 12/14          | 1 min 14 s     | 2 idiomas rechazados (ar, hi): códigos en línea perdidos al retornar     |
| `mistral-large-latest`                          | 14/14    | ❌ 1/14           | 2 min 44 s     | una sección perdida (ar, hi, ko); bloques de código añadidos (ja, ko, ro, zh) |

Dos campañas interrumpidas no están registradas: Grok, sesión CLI expirada
tras doce idiomas (once sin discrepancias), y `qwen3.8-flash`, HTTP 429 de su
proveedor de alojamiento tras dos. `opencode/mimo-v2.5-free` y `ollama/gpt-oss-20b-32k`
no se volvieron a medir en esta revisión; en la del 4 y 5 de septiembre,
277 líneas más corta, cada uno escribió 9 traducciones de 14, de las cuales 7
y 1 sin discrepancias.

Las filas `--use_antigravity` y `--use_claude_code` no se midieron en
la revisión fijada, sino el 26 de septiembre en la publicada con la 1.14.0 — y
las filas `claude-sonnet-5-5`, `claude-haiku-5-5` y `claude-haiku-4-5` el 18
de octubre, en la misma: 600 líneas, 257 códigos en línea, 30 cierres de bloques, 85
líneas de tabla. Al ser
185 líneas más corta, no se compara término a término con las demás filas;
esas filas, en cambio, se comparan entre sí. En cuanto a los enlaces internos, que el
comparador no controla, `gemini-3.8-flash-medium` los mantuvo intactos en
los catorce idiomas, `gemini-3.7-flash-medium` los rompió en italiano;
`sonnet` y `opus` los mantuvieron intactos en todas partes, `haiku` los duplicó en
inglés; `claude-sonnet-5-5` y `claude-haiku-4-5` los mantuvieron intactos en
los catorce idiomas, `claude-haiku-5-5` en los doce que escribió.

### Cuatro README de proyectos conocidos

FastAPI, Ollama, tldr-pages y Vue.js, tomados tal cual de GitHub —
documentos más fáciles que los dos anteriores. La campaña se centró en los modelos
con dificultades; Gemini sirve aquí como punto de comparación.

| Modelo                    | Alcance                    | Escritas | Sin discrepancias |
| ------------------------- | -------------------------- | -------- | ----------------- |
| `gemini-3.7-flash`        | 4 proyectos × 14 idiomas   | 56/56    | ✅ **55/56**      |
| `opencode/mimo-v2.5-free` | 4 proyectos × 14 idiomas   | 55/56    | ❌ 47/56          |
| `grok-4.6` (suscripción) | 4 proyectos × ar, hi, ja, zh | 16/16    | ❌ 14/16          |
| `ollama/gpt-oss-20b-32k`  | 4 proyectos × ar, hi, ja, zh | 15/16    | ❌ 9/16           |

### Lo que estas mediciones no son

- **No es una clasificación exhaustiva**: solo OpenRouter ofrece más de cuatrocientos
  modelos, y se midió una quincena.
- **Duraciones orientativas**: de tres a seis traducciones en paralelo según
  las campañas, y el rendimiento de un proveedor varía a lo largo del día.
- **Observaciones fechadas**: los modelos cambian bajo el mismo nombre, y sus
  documentos no son los nuestros.

Para repetir la medición en sus documentos, sobre una copia fijada del archivo:

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## Contribuir

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

Ambas líneas son necesarias: sin `pip install -e .`, `python -m aipmt`
responde `No module named aipmt`.

Herramientas de calidad, opcionales pero recomendadas:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Las 28 traducciones del repositorio (README y CHANGELOG, catorce idiomas) se
regeneran con `./regen_translations.sh --force` — Codex y `gpt-6.1-sol` en
la suscripción a ChatGPT por defecto, cuatro en paralelo. `REGEN_PROVIDER` y
`REGEN_MODEL` cambian la ruta: `antigravity` se mantiene en una suscripción, la
de Google, y pasa sin excepciones; una API de pago (`openai`, `gemini`,
`grok`, `openrouter`) se rechaza sin `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` limita cada trabajo (600 s, 1800 s en Codex y
Antigravity). El detalle de las herramientas se encuentra en `CLAUDE.md`.

## Proyectos que utilizan este script

- **[jls42.org](https://jls42.org)** — blog personal publicado en 15 idiomas. Su
  [seguimiento diario de IA](https://jls42.org/fr/news) es traducido a diario
  por esta herramienta y sirve como documento de referencia para las mediciones anteriores.

## Autor

Julien LE SAUX
Correo electrónico: contact@jls42.org

## Licencia

GNU GENERAL PUBLIC LICENSE Versión 3. Consulte [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Advertencia

Este programa se distribuye **sin ninguna garantía**, bajo los términos de las
secciones 15 y 16 de la GPL v3: suministrado «tal cual», sin garantía de comerciabilidad
ni de idoneidad para un propósito particular, y su autor no podrá ser
considerado responsable de ningún daño derivado de su uso. El texto de la
licencia prevalece sobre este resumen.

- **Revise antes de publicar.** Las protecciones cubren los bloques de código, el
  código en línea, las URL, las anclas y las citas del modo `--news` — no los
  títulos, ni las tablas, ni el front matter, ni el sentido de sus frases.
- **Sus documentos se envían al proveedor elegido**, bajo sus condiciones
  de uso y su política de datos. Algunos modelos gratuitos pueden
  reutilizar sus interacciones para el entrenamiento, y los términos de Antigravity
  permiten a Google reutilizarlas y hacer que las revisen personas,
  incluidas las suscripciones de pago; un modelo local es la única vía que no permite
  la salida de ningún dato de su máquina.
- **Las llamadas a la API se le facturan a usted.** Este programa no establece un límite de
  gasto: un documento extenso, un reintento tras un fallo o un modelo que razona
  mucho cuestan más.
- **Las mediciones publicadas son observaciones fechadas**, no garantías.

Los nombres de productos y empresas mencionados pertenecen a sus respectivos
titulares. Este proyecto no está afiliado a ninguno de ellos.

**Artículo traducido del fr al es con gemini-3.8-flash-medium.**

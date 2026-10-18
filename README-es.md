# Traductor de Markdown con IA

🌍 [Francés](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [Inglés](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Chino](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Alemán](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Japonés](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Coreano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Árabe](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Neerlandés](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polaco](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Portugués](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Rumano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Sueco](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Malas prácticas de código"></a>
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

Traduce archivos Markdown de un idioma a otro preservando la
estructura: bloques de código, código en línea, URL, anclas, tablas y front
matter. Once formas de llamar a un modelo: cinco API, cuatro suscripciones sin
facturación por uso y dos routers; además de una medición publicada de lo que cada
modelo preserva realmente.

## En resumen

- **Once vías de proveedor**: API de OpenAI, Mistral, Claude, Gemini y Grok;
  suscripciones a ChatGPT (Codex), Grok, Google (Antigravity) y Claude (Claude
  Code) sin facturación por uso; routers OpenCode (open source, gratuito o local) y OpenRouter
  (más de 400 modelos).
- **Nada incorrecto por culpa de un token perdido**: los bloques de código, el código en línea,
  las URL, las anclas y las citas se sustituyen por tokens antes de la llamada y
  se verifican al regresar. Si falta alguno, el archivo no se escribe.
- **Documentos largos**: segmentación según la ventana del modelo.
- **Modo `--news`**: citas en inglés protegidas y flags gestionados por
  idioma, para artículos de seguimiento.
- **Modo `--eco`**: modelos más rápidos y económicos.
- **Nota de traducción** opcional, arriba, abajo o en ambos lugares.

## Instalación

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 o posterior. Para instalar desde el repositorio, consulta
[Contribuir](#contribuir).

## Configuración

Las claves se leen en tres lugares, de mayor a menor prioridad; cada uno solo
completa lo que el anterior deja vacío.

|     | Dónde                                         | Para qué                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variables de entorno                          | CI, contenedores, excepción puntual   |
| 2   | `.env` del directorio actual (o de uno superior) | una clave específica de un proyecto   |
| 3   | `~/.config/aipmt/.env`                        | se instala una vez y sirve en todas partes |

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

Se acepta `GEMINI_API_KEY` en lugar de `GOOGLE_API_KEY`. El archivo
del usuario sigue `XDG_CONFIG_HOME` (solo ruta absoluta) y `%APPDATA%`
en Windows. Sin una clave, el comando enumera las tres ubicaciones.

**El `.env` de un proyecto no puede redirigir las llamadas ni elegir el programa
ejecutado.** Proporciona claves, nunca un destino ni un binario: cualquier
variable de `_BASE_URL`, `_API_BASE`, `_ENDPOINT` o `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, los proxies (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), los almacenes de certificados (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) y `XDG_CONFIG_HOME` /
`APPDATA` se ignoran allí, con una advertencia. Un repositorio clonado no debe
poder desviar tu clave ni hacerte ejecutar su propio programa en la
primera traducción. Este archivo también se lee sin interpolación:
`NOM=${OPENAI_API_KEY}` no copia allí la clave. Define estas variables en
el entorno o en `~/.config/aipmt/.env`.

Variables opcionales: `XAI_BASE_URL` (valor predeterminado: `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (segundos por llamada, valor predeterminado: 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(valor predeterminado: 600), `GROK_BIN`, `GROK_HOME` (valor predeterminado: `~/.grok`), `GROK_TIMEOUT`
(valor predeterminado: 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (valor predeterminado: 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (valor predeterminado: 600), `OPENROUTER_BASE_URL`
(se requiere `https://`), `OPENROUTER_TIMEOUT` (valor predeterminado: 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (valor predeterminado: 30). Cada una se detalla en la
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

`document.md` traducido al español produce `document-es.md` en `--target_dir`;
con `--include_model`, `document-es-gpt-5.6-terra.md`. La extensión siempre pasa a ser
`.md` — `article.mdx` produce `article-en.md` — salvo con
`--keep_filename`, que conserva el nombre original. Una traducción ya existente
se omite sin `--force`.

Códigos de salida: `0` si todo se completó o se omitió, `1` si queda algún archivo
con errores (lista en la salida de error), `2` si el problema está en la configuración.
Un archivo con errores nunca se escribe, incluso si falla la propia escritura:
el contenido se escribe al lado y luego se renombra. Basta con volver a ejecutarlo.

## Qué modelo elegir

Medido con dos documentos reales, traducidos a los mismos catorce idiomas por
cada modelo. **La cifra representa el número de idiomas, de catorce, en los que la
traducción se escribe y nada difiere del original.**

| Modelo                | Cómo acceder                      | Artículo denso de seguimiento | Este README  | Qué difiere y en cuántos idiomas                                                                                                                                   |
| --------------------- | --------------------------------- | ----------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | suscripción a Google (Antigravity) | ✅ 14/14                      | ✅ 14/14     | nada, en ninguno de los dos documentos                                                                                                                             |
| **Claude Sonnet 5.5** | clave de API de Anthropic         | ✅ 14/14                      | ✅ 14/14     | nada, en ninguno de los dos documentos                                                                                                                             |
| **Gemini 3.7 Flash**  | clave de API de Google            | ✅ 14/14                      | ⚠️ 13/14     | 1 idioma de 14: una palabra más en negrita (ja)                                                                                                                    |
| **Gemini 3.7 Flash**  | suscripción a Google (Antigravity) | ✅ 14/14                      | ⚠️ 13/14     | 1 idioma de 14: una palabra menos en negrita (ko)                                                                                                                  |
| **GPT-5.6 Sol**       | suscripción a ChatGPT o clave de OpenAI | ✅ 14/14                 | ⚠️ 12/14     | 2 idiomas de 14: una palabra menos en negrita (ar, ja)                                                                                                             |
| **GLM-5.2**           | clave de OpenRouter               | ✅ 14/14                      | ⚠️ 11/14     | 3 idiomas de 14: una palabra menos en negrita (hi, ja, ko)                                                                                                         |
| Claude Sonnet 5       | suscripción a Claude (Claude Code) | ⚠️ 13/14                     | ⚠️ 13/14     | 1 idioma de 14 en el artículo: una palabra más en negrita (zh); 1 en este README: una línea de tabla pegada a la anterior, oculta al mostrarse (ar)                |
| Claude Haiku 4.5      | suscripción a Claude (Claude Code) | ⚠️ 11/14                     | ✅ 14/14     | 3 idiomas en el artículo: un encabezado de sección pasó al nivel 1 (en, pl, ro); en este README, nada para el comparador, pero los enlaces internos se duplicaron en inglés |
| Claude Sonnet 5       | clave de API de Anthropic         | ⚠️ 11/14                      | ⚠️ 12/14     | 3 idiomas en el artículo: apareció un bloque de código (es, de, hi); 2 en este README: un enlace sin su marcado (sv), una palabra en negrita (zh)                  |
| Claude Haiku 4.5      | clave de API de Anthropic         | ⚠️ 7/14                       | ✅ 14/14     | 7 idiomas en el artículo: un encabezado de sección pasó al nivel 1; en japonés, permaneció en francés; nada en este README                                         |
| Claude Haiku 5.5      | clave de API de Anthropic         | ⚠️ 11/14                      | ❌ 12/14     | 3 idiomas en el artículo: un encabezado de sección cambió de nivel o se duplicó (ja, ko, zh); en este README, 2 idiomas rechazados y códigos en línea perdidos (ar, hi) |
| Qwen 3.7 Flash        | clave de OpenRouter               | ❌ 8/14                       | ⚠️ 10/14     | 1 idioma rechazado en el artículo y otros 5 se desvían; en este README, unas cuarenta palabras se colocaron en `code` (ar)                                |
| Grok 4.6              | suscripción a Grok                | ❌ 8/14                       | sin calificar | 5 idiomas rechazados de 14, por no devolver códigos en línea y URL; el neerlandés difiere por completo                                                            |
| GPT-OSS 20B           | modelo local (Ollama)             | ❌ 7/14                       | sin volver a medir | 4 idiomas rechazados de 14: el modelo dejaba fragmentos en francés y la protección los detuvo                                                                |
| MiMo v2.5 (gratuito)  | OpenCode Zen, sin cuenta          | ❌ 11/14                      | sin volver a medir | 1 idioma rechazado; una sección perdida en polaco                                                                                                             |
| Mistral Large         | clave de API de Mistral           | ❌ 5/14                       | ❌ 1/14      | **desaparece una sección completa**: 1 idioma en el artículo (hi), 3 en este README (ar, hi, ko), además de 3 idiomas rechazados en el artículo                   |
| DeepSeek V4 Flash     | clave de OpenRouter               | ❌ 3/14                       | sin volver a medir | 10 idiomas rechazados de 14; 37 minutos por idioma                                                                                                            |
| Claude Opus 5.5       | suscripción a Claude (Claude Code) | ❌ 0/14                      | ✅ 14/14     | el artículo fue rechazado en los 14 idiomas por las salvaguardas de Opus, debido a una breve noticia de biología; nada en este README                            |

|     | Qué significa el símbolo                                                                                                                                                                              |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | los catorce idiomas traducidos y nada difiere del original                                                                                                                                             |
| ⚠️  | los catorce idiomas traducidos; lo que difiere es el **marcado**: una palabra en negrita, un `code`, un enlace que pierde sus corchetes. No falta texto, ninguna URL, ningún bloque de código ni ninguna sección |
| ❌  | al menos un idioma no pudo traducirse —el archivo se rechaza y no se escribe— **o** falta contenido en un archivo escrito                                                                              |

Lo que hay que recordar:

- **Una traducción rechazada no es una traducción dañada.** Cuando falta un token
  al regresar, el archivo no se escribe y el idioma cuenta como
  rechazado. Eso es lo que le ocurre a Grok en el artículo: pierde cuatro códigos en línea y
  tres URL desde el primer segmento, en los cinco sistemas de escritura no latinos.
- **Un modelo puede rechazar un documento entero por una sola frase.** Opus 5.5
  traduce este README sin ninguna diferencia, pero ningún artículo de seguimiento: sus
  salvaguardas detienen la respuesta ante una breve noticia de biología. El archivo no se
  escribe y aipmt explica por qué.
- **Esta red de seguridad no cubre los encabezados, las tablas, el front matter ni el
  texto.** Un modelo que elimina una sección devuelve un archivo que la herramienta escribe
  sin protestar, como ocurre con Mistral. Estos elementos no pueden
  sustituirse por un token y las protecciones actuales no los controlan;
  `scripts/compare_structure.py` detecta una sección perdida, pero a posteriori.
- **Grok no tiene calificación en este README**: su sesión de CLI caducó después de doce
  idiomas, once de ellos sin diferencias. Una campaña interrumpida no se califica.
- **La densidad del documento importa más que el idioma.** Grok funciona bien con
  README normales y falla en un artículo cargado de enlaces, incluso en
  neerlandés.

Fechas y documentos: la columna «Este README» se midió el 9 de septiembre de 2026
sobre una revisión fija de este archivo (785 líneas, 285 códigos en línea, 89 líneas
de tabla), modificada desde entonces, salvo las filas de Antigravity y Claude Code,
medidas el 26 de septiembre sobre la revisión publicada con la versión 1.14.0, más corta
(600 líneas, 257 códigos en línea, 85 líneas de tabla), y las filas de Claude
Sonnet 5.5, Haiku 5.5 y Haiku 4.5 mediante la API, medidas el 18 de octubre sobre la
misma revisión. La columna «Artículo denso de seguimiento» procede de la campaña de los
días 4 y 5 de septiembre sobre un artículo de 589 líneas, salvo la fila de Grok, que volvió a medirse el
9 de septiembre sobre otra edición del mismo seguimiento; las filas de Antigravity y
Claude Code, medidas el 26 de septiembre sobre el mismo artículo; y estas tres filas de
Claude, el 18 de octubre. Las tablas completas, las duraciones y el protocolo están
en [Mediciones detalladas](#mediciones-detalladas).
## Todas las opciones

| Opción                   | Descripción                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Archivo Markdown único que se va a traducir (alternativa a `--source_dir`)                                             |
| `--source_dir`           | Directorio de origen que contiene los archivos Markdown (valor predeterminado: `content/posts`)                                   |
| `--target_dir`           | Directorio de salida para los archivos traducidos (valor predeterminado: `traductions_en`)                                    |
| `--source_lang`          | Idioma de origen (valor predeterminado: `fr`)                                                                                  |
| `--target_lang`          | Idioma de destino (valor predeterminado: `en`)                                                                                   |
| `--model`                | Modelo específico que se utilizará                                                                                  |
| `--eco`                  | Usar los modelos económicos                                                                              |
| `--use_mistral`          | Usar la API de Mistral AI                                                                                     |
| `--use_claude`           | Usar la API de Claude                                                                                         |
| `--use_gemini`           | Usar la API de Gemini                                                                                         |
| `--use_grok`             | Usar la API de xAI (Grok) — requiere `XAI_API_KEY`                                                           |
| `--use_codex`            | Usar el CLI Codex con la cuota de la suscripción de ChatGPT                                                    |
| `--use_grok_cli`         | Usar el CLI Grok con la cuota de la suscripción de Grok                                                        |
| `--use_antigravity`      | Usar el CLI Antigravity (`agy`) con la cuota de la suscripción de Google AI Pro o Ultra                       |
| `--use_claude_code`      | Usar el CLI Claude Code (`claude -p`) con la cuota de la suscripción de Claude Pro o Max                      |
| `--use_opencode`         | Usar OpenCode (open source) con el proveedor configurado en OpenCode; requiere `--model provider/modèle` |
| `--use_openrouter`       | Usar OpenRouter — requiere `OPENROUTER_API_KEY` y `--model fournisseur/modèle`                          |
| `--force`                | Forzar una nueva traducción                                                                                       |
| `--keep_filename`        | Conservar el nombre de archivo original                                                                          |
| `--news`                 | Modo noticias: protege las citas en inglés y gestiona las banderas por idioma                                      |
| `--add_translation_note` | Añadir una nota de traducción                                                                                |
| `--note_position`        | Posición de la nota: `top`, `bottom` (valor predeterminado) o `both`                                                     |
| `--note_format`          | Formato de la nota: `legacy` (valor predeterminado, párrafo en negrita) o `marker`                                            |
| `--include_model`        | Incluir el nombre del modelo en el archivo de salida                                                            |
| `--reasoning_effort`     | Esfuerzo de razonamiento de GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

Los nueve flags `--use_*` son mutuamente excluyentes: combinar dos se
rechaza.

## Proveedores

### Mediante API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` cambia al nivel económico de cada proveedor.

| Proveedor    | Calidad (valor predeterminado)                                      | Económico (`--eco`)      |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                   | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol` (también `terra` y `luna` mediante `--model`) | `gpt-5.6-luna`            |
| API de Grok    | `grok-4.6`                                            | `grok-4.3`                |
| CLI de Grok    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, esfuerzo `low`                                | igual — `--eco` sin efecto |
| OpenCode    | `--model provider/modèle` obligatorio                 | igual — `--eco` sin efecto |
| OpenRouter  | `--model fournisseur/modèle` obligatorio              | igual — `--eco` sin efecto |

### Mediante la suscripción de ChatGPT: `--use_codex`

Controla el CLI Codex oficial: la traducción se descuenta de la cuota de la
suscripción de ChatGPT, sin clave de API ni facturación por uso.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- El binario se busca en `CODEX_BIN`, después en el `PATH` y, a continuación, en el paquete
  `openai-codex-cli-bin`. `~/.codex/auth.json` nunca se lee.
- `OPENAI_API_KEY` y `CODEX_API_KEY` se eliminan del entorno del
  subproceso: una clave presente nunca provoca el cambio a la API.
- Cada segmento cuesta al menos un «mensaje» de la ventana de 5 horas —dos
  si su validación falla y se vuelve a intentar—. OpenAI anuncia, a modo de
  estimación, entre 250 y 2 000 mensajes/5 h para `gpt-5.6-luna` (`--eco`) y
  entre 10 y 100 para `gpt-5.6-sol` con un plan Plus.
- `--model gpt-5.6-terra` y `--model gpt-5.6-luna` también pasan por
  la suscripción. Un modelo al que la cuenta no tiene acceso devuelve un error 400 «model is
  not supported when using Codex with a ChatGPT account».
- Es más lento que una API, y la diferencia aumenta con el documento: en este README,
  6 min 46 s por idioma de mediana con `gpt-5.6-sol`, frente a 36 s con
  `gemini-3.7-flash`.
- Se rechaza en CI (si `CI` o `GITHUB_ACTIONS` están definidos): la suscripción se autentica
  mediante un archivo de sesión personal, que no debe estar en un runner
  compartido.
- Variables: `CODEX_BIN`, `CODEX_TIMEOUT` (segundos por segmento, valor predeterminado: 600).

### Mediante la suscripción de Grok: `--use_grok_cli`

El mismo principio con el CLI oficial Grok Build, mediante la suscripción SuperGrok o
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Confinamiento más débil que Codex.** El sandbox del sistema operativo de Grok no se aplica
  en muchos equipos Linux recientes (AppArmor, sockets de runtime de
  contenedores), y un perfil que no puede aplicarse se inicia sin confinamiento y
  sin avisar. Por tanto, el script no solicita ningún perfil de forma predeterminada, lo anuncia y
  se basa en las reglas `--deny` del CLI, incluida la regla general `*` —la única
  capa que se niega a iniciarse en lugar de retirar la protección sin
  avisar—. `GROK_TRANSLATE_SANDBOX=read-only` exige el sandbox del sistema operativo y el inicio
  falla si la máquina no puede respetarlo.
- La cuota es semanal, se comparte con Chat, Imagine y Voice, y ningún
  comando permite consultarla: un lote puede consumir parte del uso conversacional
  sin indicarlo.
- Variables: `GROK_BIN`, `GROK_HOME` (directorio del CLI, valor predeterminado: `~/.grok`),
  `GROK_TIMEOUT` (valor predeterminado: 900), `GROK_TRANSLATE_SANDBOX`.

### Mediante la suscripción de Google: `--use_antigravity`

El mismo principio con `agy`, el CLI oficial de Antigravity: para quienes pagan Google
AI Pro o Ultra, la traducción se descuenta de la cuota de la suscripción en lugar
de facturarse por token. Es la única vía hacia esta cuota: Gemini CLI ya no
presta servicio a estas cuentas desde el 18 de junio de 2026
([anuncio](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
y el SDK de Antigravity solo acepta una clave de API o un proyecto de Google Cloud.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **No queda abierta ninguna vía de pago.** agy solo recibe de su
  entorno una lista cerrada de variables —`PATH`, idioma y zona horaria,
  terminal, identidad, proxies y certificados, bus de sesión— y ninguna clave:
  varias de sus variables cambian una llamada sin mostrar nada (se ha medido que
  una envía el documento a una pasarela de terceros y otra a un proyecto
  facturado de Google Cloud), y en cada revisión faltaba alguna en una lista de denegación.
  Antes de cualquier segmento, `agy -p /config`, que no consume cuota, debe mostrar
  los créditos de IA de pago desactivados, sin clave de API ni proyecto de Google Cloud —la
  ausencia de este ajuste implica el rechazo—; de lo contrario, no se traduce nada. Después, el registro de cada
  llamada debe acreditar la suscripción (`authMethod=consumer`); de lo contrario, se
  rechaza la respuesta.
- **Confinamiento.** Cada llamada se ejecuta en un directorio personal privado y
  desechable, con un agente de traducción sin herramientas: sus ajustes, reglas,
  plugins, servidores MCP y hooks de agy no entran allí, no se añade nada a su
  historial y la conexión permanece en el llavero, que aipmt nunca lee.
  Si no se encuentra un agente, agy vuelve silenciosamente a su agente de programación
  y sus herramientas: una línea completa del registro debe confirmar el agente correcto —un
  documento que cite este mensaje no la sustituye—; de lo contrario, se rechaza.
- **Plataformas**: Linux, en una sesión que disponga de un llavero (bus de sesión
  D-Bus, Secret Service); se acepta macOS, aunque no se ha medido allí. Se rechaza
  en Windows, donde agy no lee las variables que aíslan cada llamada, y
  en Linux sin bus de sesión —sesión SSH, contenedor, servidor—: allí, agy
  guarda su token en un archivo de `~/.gemini` que el aislamiento oculta. El
  rechazo se produce antes de cualquier inicio, indicando la causa, en lugar de esperar
  un minuto a que aparezca un código de conexión.
- **Modelos**: los de `agy models`. Los Gemini incluyen el esfuerzo en su nombre
  (`gemini-3.8-flash-medium`…): un nombre sin sufijo se rechaza antes de la llamada,
  y `--reasoning_effort` no tiene efecto. De forma predeterminada, `gemini-3.8-flash-medium`,
  y `gemini-3.7-flash-low` en `--eco`; las campañas que los fijaron se
  describen en [Mediciones detalladas](#mediciones-detalladas). Claude y GPT-OSS
  tienen su propia cuota, mucho menor: aproximadamente el 1 % de la ventana de
  5 horas por llamada medida, frente al 0,05 % en Flash.
- **Cuota**: por grupo, una ventana de 5 horas y otra semanal, de forma
  proporcional al coste en tokens. Medido en la cuenta del autor: aproximadamente
  16 puntos de la ventana de 5 horas por millón de caracteres de origen con
  `gemini-3.8-flash-medium`, 14 con `gemini-3.7-flash-medium` y entre 7 y 8 con
  un esfuerzo bajo; por tanto, un README de 40 000 caracteres cuesta algo más de medio
  punto. El límite semanal depende del nivel. Los reintentos siguen
  lo que agy declara como reintentable; en caso contrario, una ventana agotada nunca se
  vuelve a intentar: hace que falle cada archivo hasta el restablecimiento
  que muestra `/usage`.
- **Más lento que la API**: en el denso artículo de las mediciones, 3 min 59 s por
  idioma de mediana con `gemini-3.8-flash-medium` y 3 min 14 s con
  `gemini-3.7-flash-medium`, frente a 1 min 18 s para Gemini 3.7 Flash mediante la API.
- **Interrupción**: Ctrl-C, o cerrar un terminal, detienen agy junto con el
  comando en lugar de dejar que termine su turno consumiendo su cuota; ocurre lo
  mismo con Codex, Grok CLI y OpenCode. Con `nohup`, la traducción continúa.
- Se rechaza en CI (si `CI` o `GITHUB_ACTIONS` están definidos): la conexión reside en un
  llavero personal. En un runner, `--use_gemini` con `GOOGLE_API_KEY`.
- Variables: `AGY_BIN` (en su defecto, el `PATH` y después `~/.local/bin/agy`),
  `AGY_TIMEOUT` (segundos por segmento, incluido el inicio, valor predeterminado: 900).

**Condiciones de uso: es su cuenta la que queda comprometida.** Las
[condiciones de Antigravity](https://antigravity.google/terms) (sección 6) y sus
[Preguntas frecuentes](https://antigravity.google/docs/faq/) prohíben acceder al servicio
mediante software de terceros usando la conexión de Antigravity —se mencionan
Claude Code, OpenClaw y OpenCode—, bajo pena de suspensión de la cuenta. aipmt
no lee ni reutiliza el token: ejecuta el binario oficial en el
[modo headless](https://antigravity.google/docs/cli/headless/) que Google
documenta para scripts y CI. Un miembro de Google consideró «estándar»
ejecutar `agy -p` desde un script local para su propio trabajo
([foro oficial, 25 de septiembre de 2026, respuesta no vinculante](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
ningún texto resuelve el caso de una herramienta distribuida como esta.

**Solo documentos públicos.** Según la sección 5 de las mismas condiciones, los
intercambios —prompts, respuestas y metadatos— pueden utilizarse para mejorar los
productos y el aprendizaje automático de Google y ser revisados por
personas, incluso con una suscripción de pago. La exclusión se realiza mediante el ajuste
`enableTelemetry`, cuyo efecto no está documentado y que aipmt no establece; sus ajustes
de agy no se transfieren a su entorno aislado. No envíe por esta vía nada confidencial.
### Sobre la suscripción a Claude: `--use_claude_code`

El mismo principio se aplica con `claude`, el CLI oficial de Claude Code, en modo `-p`: para
quienes pagan Claude Pro o Max, la traducción se descuenta de la cuota de
la suscripción en lugar de facturarse por token. No debe confundirse con
`--use_claude`, la API de Anthropic, facturada según el uso.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **No queda abierta ninguna vía de pago, y cada llamada lo demuestra.** Claude
  Code solo recibe de su entorno una lista cerrada de variables: ni
  clave API, ni token, ni proveedor cloud, ni marcador de la sesión de Claude Code
  desde la que se iniciaría aipmt. Antes del primer segmento, `claude auth status` debe
  mostrar la conexión de la suscripción, sin clave de Console, y `/usage`, que no consume
  ninguna cuota, debe confirmarlo; cada llamada lo confirma a su vez en su
  evento de inicialización; de lo contrario, se rechaza la respuesta.
- **Desactive el «uso adicional»** (claude.ai, Configuración → Uso) para
  mantener el coste en cero euros: si está activado, toma el relevo cuando se agota una ventana y
  factura sin mostrar ningún error. aipmt detiene la traducción en cuanto el informe
  de cuota de una llamada lo indica, pero esa llamada ya se ha contabilizado.
- **Cuota compartida con sus sesiones de Claude Code.** Cada llamada informa
  del uso de las ventanas de 5 horas y de la semana; por encima del 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`), no se inicia ningún segmento adicional, para no
  agotar lo que necesita para su trabajo.
- **Confinamiento.** Cada llamada se ejecuta sin herramientas, en un directorio privado y
  desechable, en modo sin personalización: no se cargan sus `CLAUDE.md`, ni sus plugins,
  hooks, servidores MCP o configuraciones, y no se conserva nada de la
  sesión. Los archivos adjuntos están desactivados: un `@chemin` en su documento
  permanece como texto y no abre ningún archivo (comprobado).
- **Modelos**: `sonnet` de forma predeterminada, con el esfuerzo `low`, y también en `--eco`:
  `--eco` no cambia nada en esta vía. Medido con los mismos documentos, `haiku`
  es dos veces más lento —razona sin que se pueda impedir— por
  un coste apenas inferior, y `opus` rechaza contenidos de biología (punto
  siguiente). Ambos siguen siendo accesibles mediante `--model`; estos alias siguen el
  último modelo de su familia. Se rechazan `fable` y las variantes `[1m]`,
  porque recurren a créditos de pago. `--reasoning_effort` ajusta el esfuerzo,
  del que una traducción no obtiene nada: el razonamiento medido es nulo o casi nulo.
- **Opus rechaza algunos contenidos de biología.** Sus medidas de protección son más
  estrictas que las de Sonnet, y el mensaje de error de Anthropic advierte de que
  «a veces pueden marcar trabajos relacionados con la investigación biológica». Comprobado: una breve nota de
  vigilancia sobre 279 moléculas generadas hizo que se rechazara el artículo en los catorce
  idiomas. No se escribe nada: aipmt rechaza la respuesta cortada, menciona las
  medidas de protección y recomienda `--model sonnet`.
- Se rechaza en CI (si se ha definido `CI` o `GITHUB_ACTIONS`) y en Windows (no comprobado).
- Variables: `AIPMT_CLAUDE_BIN` (en su defecto, el `PATH` y después `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (segundos por segmento, valor predeterminado: 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (valor predeterminado: 0.8), `CLAUDE_CONFIG_DIR` (la cuenta de
  Claude Code, nunca tomada de un `.env` del proyecto); directorios de trabajo bajo
  `XDG_CACHE_HOME/aipmt/claude-code` (valor predeterminado: `~/.cache`).

**Condiciones de uso: es su cuenta la que queda comprometida.** La
[página legal de Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
no impide «que un usuario final inicie sesión en el binario de Claude Code sin modificar
con su propia suscripción a Claude»: eso es lo que hace aipmt, que inicia el
binario oficial y nunca lee el token. Sin embargo, Anthropic «no permite
que desarrolladores externos […] enruten solicitudes mediante las credenciales
de planes Free, Pro o Max en nombre de sus usuarios», prefiere la clave API para las herramientas
de terceros, «incluidos los proyectos open source», y se reserva el derecho de descontar su
uso de los créditos de pago
([ayuda de Claude](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Ningún texto resuelve el caso de una herramienta distribuida que inicia el binario.

**Datos**: en las cuentas Free, Pro y Max, el entrenamiento de los modelos
también se aplica a Claude Code cuando la configuración de privacidad lo permite
([página sobre datos](https://code.claude.com/docs/en/data-usage)). aipmt no conserva
ninguna transcripción local (`--no-session-persistence`). No procese mediante él
nada confidencial.

### Hacia el proveedor de su elección: `--use_opencode`

[OpenCode](https://opencode.ai) es un agente de código open source (MIT) que
enruta hacia los proveedores configurados en él: clave API, suscripción,
pasarela OpenCode Zen (modelos gratuitos, sin cuenta) o modelo local. Aquí se
han medido de principio a fin dos vías: Zen y Ollama.

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
cuyos intercambios pueden utilizarse para el entrenamiento, y esa decisión no se toma
por usted.

Confinamiento en cada llamada:

- una configuración inline, con prioridad sobre la suya, define un agente `aipmt`
  cuyas herramientas están todas denegadas (`permission: { "*": "deny" }`), con el uso compartido de
  la sesión desactivado, `--pure`, nunca `--auto`;
- directorio de trabajo desechable y vacío, con `OPENCODE_DISABLE_PROJECT_CONFIG` y
  `OPENCODE_DISABLE_CLAUDE_CODE` establecidos; sin ellos, OpenCode inyecta en el
  prompt el `AGENTS.md` del directorio actual y `~/.claude/CLAUDE.md`. El
  `~/.config/opencode/AGENTS.md` global se sigue inyectando, pues OpenCode no permite
  excluirlo;
- contrato de salida: código de retorno 0, ningún evento `error`, ninguna llamada
  a herramientas, último paso en `stop`, texto no vacío y el agente `aipmt`
  cargado realmente; un `--agent` desconocido no provoca un error en OpenCode, sino que
  este recurre silenciosamente al agente de codificación;
- no se transmite ninguna clave de `aipmt`, salvo `OPENCODE_API_KEY`, la clave
  del propio OpenCode. Los proveedores se configuran en OpenCode, no en
  el `.env` de `aipmt`.

Aspectos que debe conocer:

- Los modelos gratuitos de Zen son cambiantes, sus límites no están documentados y
  sus intercambios pueden utilizarse para el entrenamiento: son adecuados para documentación
  pública, no para contenido privado.
- Un modelo local debe ofrecer al menos 16 k tokens de contexto, ya que los segmentos
  alcanzan los 16 000 caracteres. Ollama suele configurar 4 096: utilice
  un `Modelfile` con `PARAMETER num_ctx 32768`.
- `--eco` no tiene efecto; `--reasoning_effort` se transmite sin cambios como
  `--variant` de OpenCode.
- OpenCode registra cada sesión en `~/.local/share/opencode/`.
- Variables: `OPENCODE_BIN` (en su defecto, el `PATH` y después `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (segundos por segmento, valor predeterminado: 600). `OPENCODE_CONFIG`
  se transmite sin cambios a OpenCode.

Ejemplo de un modelo local mediante Ollama, en `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` desactiva la reflexión que Ollama activa de forma predeterminada en estos
modelos y que un Modelfile no puede desactivar. Medido con una frase de
seis palabras: 919 tokens de reflexión y 68 segundos sin la opción, 9 tokens con ella.

### Hacia más de 400 modelos: `--use_openrouter`

OpenRouter es un router facturado según el uso, mediante un crédito único, situado ante
modelos alojados por terceros, incluidos los modelos chinos abiertos que ningún
otro proveedor ofrece aquí.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` es obligatorio. Un preflight, ejecutado antes de cualquier facturación, gestiona
dos particularidades del enrutamiento:

- **Un mismo modelo es servido por decenas de proveedores de alojamiento con límites
  diferentes**: en `z-ai/glm-5.3-flash`, 23 proveedores, uno de ellos limitado a
  2 048 tokens de salida. El preflight lee `/api/v1/models/{modèle}/endpoints`,
  descarta los proveedores con menos de 8 000 tokens de salida o con un estado degradado, y
  fija los demás mediante `allow_fallbacks: false`.
- **El razonamiento se factura a la tarifa de salida**: 107 tokens frente a 2 en
  una respuesta «OK» de `z-ai/glm-5.2`. Está desactivado de forma predeterminada; los modelos
  que lo imponen reciben el esfuerzo más bajo que aceptan, ya que el valor predeterminado del
  catálogo podría saturar la salida antes de que termine la traducción.
  `--reasoning_effort` sigue teniendo prioridad.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- La ventana de contexto procede del catálogo. Un modelo con menos de 16 400 tokens se
  rechaza antes de cualquier llamada: 8 400 para el prompt y el segmento, y un mínimo de
  8 000 de salida.
- Un slug ausente del catálogo, un catálogo inaccesible o la ausencia
  de un proveedor de alojamiento que admita el límite detienen el comando.
- `finish_reason=length` con una salida vacía es un presupuesto consumido por el
  razonamiento, no un truncamiento: el mensaje los distingue.
- `--eco` no tiene efecto.
- Variables: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (valor predeterminado: `https://openrouter.ai/api/v1`; se exige `https://`),
  `OPENROUTER_TIMEOUT` (valor predeterminado: 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (valor predeterminado: 30).

### Nota de traducción

`--add_translation_note` añade una nota, en `bottom` (valor predeterminado), `top` (después del
front matter) o `both` (`--note_position`), con el formato `legacy` (párrafo en
negrita, valor predeterminado) o `marker` (`--note_format`). El formato `marker` es una
definición de referencia Markdown invisible,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
seguida de una cita en negrita: legible en GitHub y utilizable durante el build por un
plugin remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Mediciones detalladas

Todas las mediciones corresponden a traducciones ejecutadas realmente con `aipmt`, hacia
catorce idiomas: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Escritas** cuenta los archivos que las guardas dejaron pasar; **Sin
diferencias**, aquellos en los que `scripts/compare_structure.py` no detecta nada: el mismo número de
secciones, subtítulos, enlaces, URL distintas, bloques de código,
códigos inline, filas de tabla, bloques de cita y palabras en negrita.

«Sin diferencias» significa «no se ha detectado nada», no «idéntico»: el comparador
cuenta elementos sin leer su contenido. No detecta ni un título de
nivel 4 eliminado, ni el texto de un código inline sustituido, ni una bandera
intercambiada, ni un enlace interno renderizado con un paréntesis de más,
`[texte]((#ancre))`, que ya no lleva a ninguna parte; tampoco evalúa el
idioma.

### Artículo de vigilancia denso, modo `--news`

Una edición de la [vigilancia de IA de jls42.org](https://jls42.org/fr/news):
589 líneas, 140 enlaces, 21 secciones, 3 citas en inglés protegidas. Campaña
de los días 4 y 5 de septiembre de 2026.

| Modelo                                          | Acceso               | Escritas | Sin diferencias | Mediana/idioma |
| ----------------------------------------------- | -------------------- | -------- | --------------- | -------------- |
| `gemini-3.7-flash`                              | API de Google        | 14/14    | ✅ **14/14**    | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | suscripción a Google | 14/14    | ✅ **14/14**    | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | suscripción a Google | 14/14    | ✅ **14/14**    | 3 min 14 s     |
| `claude-sonnet-5-5`                             | API de Anthropic     | 14/14    | ✅ **14/14**    | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | suscripción a ChatGPT | 14/14    | ✅ **14/14**    | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter          | 14/14    | ✅ **14/14**    | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter          | 14/14    | ✅ **14/14**    | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | suscripción a Claude | 14/14    | ⚠️ 13/14       | 6 min 49 s     |
| `claude-sonnet-5`                               | API de Anthropic     | 14/14    | ⚠️ 11/14       | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | suscripción a Claude | 14/14    | ⚠️ 11/14       | 15 min 54 s    |
| `claude-haiku-5-5`                              | API de Anthropic     | 14/14    | ⚠️ 11/14       | 2 min 54 s     |
| `claude-haiku-4-5`                              | API de Anthropic     | 14/14    | ⚠️ 7/14        | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen        | 13/14    | ❌ 11/14       | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter          | 13/14    | ❌ 8/14        | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | local               | 10/14    | ❌ 7/14        | 12 min 39 s    |
| `mistral-large-latest`                          | API de Mistral      | 11/14    | ❌ 5/14        | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter          | 4/14     | ❌ 3/14        | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | suscripción a Grok   | 1/14     | ❌ 1/14        | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | suscripción a Claude | 0/14     | ❌ 0/14        | —              |

Grok se volvió a medir el 9 de septiembre con otra edición de la misma vigilancia
(356 líneas): 9 idiomas escritos de 14, 8 sin diferencias. Esta es la cifra que
aparece en la tabla principal. No se incluyen tres campañas interrumpidas:
`qwen3.5-27b` (9 idiomas) y `kimi-k2.6` (4) por falta de crédito,
y `z-ai/glm-5.3-flash`, cuyos dos fallos se debieron a una configuración de razonamiento
que el proveedor está corrigiendo. Las filas de OpenRouter se midieron con la
configuración predeterminada del router, antes de `--use_openrouter`; `z-ai/glm-5.2`,
medido de nuevo con el proveedor incluido, obtiene el mismo 14/14. Las cifras se
volvieron a calcular el 10 de septiembre con el comparador actual: `qwen3.8-flash` y
`qwen3.7-flash` ganan cada uno un idioma respecto a la primera
publicación; los demás permanecen sin cambios.

Las filas `--use_antigravity` se midieron el 26 de septiembre con el mismo
artículo, cuatro traducciones en paralelo: `gemini-3.7-flash-medium` por la mañana,
`gemini-3.8-flash-medium` por la tarde. En inglés, cada uno eliminó por sí mismo
las tres líneas de traducción al francés situadas bajo las citas, sin inventar ninguna
bandera, y las citas en inglés permanecen intactas: la limpieza de respaldo no
tuvo nada que hacer. En `--eco` (`gemini-3.7-flash-low`), únicamente con cuatro idiomas
(en, ja, ar, hi): 4 escritos de 4, todos sin diferencias, con una mediana de 1 min 52 s.
Prueba de control el mismo día con una edición más reciente de la vigilancia,
la del 25 de septiembre (438 líneas, 2 citas en inglés), traducida fuera del
blog por `gemini-3.7-flash-medium`: 14 escritas de 14, todas sin diferencias, entre 87 y
128 s por idioma.

Las filas `--use_claude_code` se midieron el 26 de septiembre con el mismo
artículo, cuatro traducciones en paralelo, con el esfuerzo `low`. Con `sonnet`, las
citas en inglés permanecen intactas en los catorce idiomas y, en inglés, el
modelo eliminó por sí mismo las líneas de traducción al francés, sin inventar ninguna
bandera. `opus` no escribió ningún idioma: en todos ellos, sus medidas de protección
detuvieron la respuesta en el último segmento debido a una breve nota sobre 279 moléculas
generadas para un sitio de unión. Enviada por separado, esta breve nota se rechaza
por pertenecer a la categoría «bio»; `sonnet` la tradujo en todos los idiomas. `haiku` escribe
los catorce idiomas; en tres (en, pl, ro), un título de sección pasa del
nivel 2 al nivel 1. Razona sin que se pueda impedir —el 61 % de
sus tokens de salida—, de ahí que tarde más del doble que `sonnet`.

Las filas `claude-sonnet-5-5`, `claude-haiku-5-5` y `claude-haiku-4-5` se
midieron el 18 de octubre mediante la API de Anthropic, con el mismo artículo y cuatro
traducciones en paralelo por modelo. Sonnet 5.5 no permite desactivar su
reflexión: aipmt le envía la configuración más baja que acepta, y sus
respuestas no contienen ninguna. Escribe los catorce idiomas sin diferencias y sin
volver a procesar ningún segmento; en inglés, eliminó por sí mismo las líneas de
traducción al francés, sin inventar ninguna bandera, y las citas en inglés
permanecen intactas en todos los idiomas. Haiku 5.5 se mide con su reflexión adaptativa: con la reflexión
desactivada, dejaba párrafos enteros en francés, que la guarda rechaza:
3 idiomas escritos de 14. Ambos Haiku tropiezan con la misma breve nota: Haiku 5.5
cambia el nivel de su título o lo duplica en japonés, coreano y
chino; Haiku 4.5 lo pasa al nivel 1 en siete idiomas y lo deja en
francés en japonés. Haiku 4.5 cuesta 3,67 $ para los dos documentos en los
catorce idiomas, Haiku 5.5 cuesta 0,57 $ y Sonnet 5.5, 9,21 $.
### README de este proyecto, Markdown estándar

Revisión fijada el 9 de septiembre de 2026: 785 líneas, 285 códigos en línea, 40
cierres de bloques, 89 líneas de tabla. Cuatro traducciones en paralelo.

| Modelo                                          | Generadas | Sin diferencias | Mediana/idioma | Diferencias                                                              |
| ----------------------------------------------- | ---------- | --------------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14      | ✅ 14/14        | 1 min 43 s     | ninguna                                                                  |
| `opus` (`--use_claude_code`)                    | 14/14      | ✅ 14/14        | 1 min 48 s     | ninguna                                                                  |
| `haiku` (`--use_claude_code`)                   | 14/14      | ✅ 14/14        | 4 min 02 s     | ninguna para el comparador; enlaces internos duplicados (en)             |
| `claude-sonnet-5-5`                             | 14/14      | ✅ 14/14        | 1 min 18 s     | ninguna                                                                  |
| `claude-haiku-4-5`                              | 14/14      | ✅ 14/14        | 2 min 06 s     | ninguna                                                                  |
| `gemini-3.7-flash`                              | 14/14      | ⚠️ 13/14        | 36 s           | una palabra en negrita (ja)                                              |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14      | ⚠️ 13/14        | 1 min 22 s     | una palabra en negrita (ko)                                              |
| `sonnet` (`--use_claude_code`)                  | 14/14      | ⚠️ 13/14        | 2 min 20 s     | una línea de tabla pegada a la anterior (ar)                             |
| `claude-sonnet-5`                               | 14/14      | ⚠️ 12/14        | 2 min 56 s     | un enlace (sv), una palabra en negrita (zh)                              |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14      | ⚠️ 12/14        | 6 min 46 s     | una palabra en negrita (ar, ja)                                          |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14      | ⚠️ 11/14        | 2 min 34 s     | una palabra en negrita (hi, ja, ko)                                      |
| `qwen/qwen3.7-flash`                            | 14/14      | ⚠️ 10/14        | 2 min 17 s     | 40 códigos en línea añadidos en árabe; negrita (hi, ja, ko)              |
| `claude-haiku-5-5`                              | 12/14      | ❌ 12/14        | 1 min 14 s     | 2 idiomas rechazados (ar, hi): códigos en línea perdidos en la respuesta |
| `mistral-large-latest`                          | 14/14      | ❌ 1/14         | 2 min 44 s     | una sección perdida (ar, hi, ko); bloques de código añadidos (ja, ko, ro, zh) |

No se puntúan dos campañas interrumpidas: Grok, cuya sesión CLI caducó
después de doce idiomas (once sin diferencias), y `qwen3.8-flash`, cuyo
proveedor devolvió HTTP 429 después de dos. `opencode/mimo-v2.5-free` y `ollama/gpt-oss-20b-32k`
no se volvieron a medir en esta revisión; en la de los días 4 y 5 de septiembre,
277 líneas más corta, cada uno generó 9 traducciones de 14, de las cuales 7
y 1 no presentaban diferencias.

Las líneas `--use_antigravity` y `--use_claude_code` no se midieron en
la revisión fijada, sino el 26 de septiembre en la publicada con la versión 1.14.0; y
las líneas `claude-sonnet-5-5`, `claude-haiku-5-5` y `claude-haiku-4-5`, el 18
de octubre, sobre esa misma revisión: 600 líneas, 257 códigos en línea, 30 cierres de bloques, 85
líneas de tabla. Al ser
185 líneas más corta, no puede compararse término por término con las demás líneas;
sin embargo, esas líneas sí pueden compararse entre ellas. En cuanto a los enlaces internos, que el
comparador no comprueba, `gemini-3.8-flash-medium` los mantuvo intactos en
los catorce idiomas, mientras que `gemini-3.7-flash-medium` los rompió en italiano;
`sonnet` y `opus` los mantuvieron intactos en todos los idiomas, mientras que `haiku` los duplicó en
inglés; `claude-sonnet-5-5` y `claude-haiku-4-5` los mantuvieron intactos en
los catorce idiomas, y `claude-haiku-5-5` en los doce que generó.

### Cuatro README de proyectos conocidos

FastAPI, Ollama, tldr-pages y Vue.js, tomados tal cual de GitHub: documentos
más fáciles que los dos anteriores. La campaña se centró en los modelos
con dificultades; Gemini sirve como punto de comparación.

| Modelo                    | Alcance                    | Generadas | Sin diferencias |
| ------------------------- | -------------------------- | --------- | --------------- |
| `gemini-3.7-flash`        | 4 proyectos × 14 idiomas   | 56/56     | ✅ **55/56**    |
| `opencode/mimo-v2.5-free` | 4 proyectos × 14 idiomas   | 55/56     | ❌ 47/56        |
| `grok-4.6` (suscripción)   | 4 proyectos × ar, hi, ja, zh | 16/16     | ❌ 14/16        |
| `ollama/gpt-oss-20b-32k`  | 4 proyectos × ar, hi, ja, zh | 15/16     | ❌ 9/16         |

### Lo que no son estas mediciones

- **No son una clasificación exhaustiva**: solo OpenRouter ofrece más de cuatrocientos
  modelos; se han medido unos quince.
- **Las duraciones son orientativas**: entre tres y seis traducciones en paralelo según
  las campañas, y el rendimiento de un proveedor varía a lo largo del día.
- **Son observaciones fechadas**: los modelos cambian bajo el mismo nombre, y sus
  documentos no son los nuestros.

Para repetir la medición con sus documentos, sobre una copia fijada del archivo:

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

Las dos líneas son necesarias: sin `pip install -e .`, `python -m aipmt`
responde `No module named aipmt`.

Herramientas de calidad, opcionales pero recomendadas:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Las 28 traducciones del repositorio (README y CHANGELOG, catorce idiomas) se
regeneran con `./regen_translations.sh --force`: Codex y `gpt-5.6-sol` mediante
la suscripción predeterminada de ChatGPT, cuatro en paralelo. `REGEN_PROVIDER` y
`REGEN_MODEL` cambian la vía: `antigravity` sigue usando una suscripción, la
de Google, y funciona sin excepción; una API de pago (`openai`, `gemini`,
`grok`, `openrouter`) se rechaza sin `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` limita cada job (600 s, 1 800 s en Codex y
Antigravity). Los detalles de las herramientas se encuentran en `CLAUDE.md`.

## Proyectos que utilizan este script

- **[jls42.org](https://jls42.org)** — blog personal publicado en 15 idiomas. Su
  [seguimiento diario de IA](https://jls42.org/fr/news) se traduce cada día
  con esta herramienta y sirve como documento de referencia para las mediciones anteriores.

## Autor

Julien LE SAUX
Correo electrónico: contact@jls42.org

## Licencia

GNU GENERAL PUBLIC LICENSE Version 3. Véase [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Advertencia

Este programa se distribuye **sin ninguna garantía**, conforme a los términos de las
secciones 15 y 16 de la GPL v3: se proporciona «tal cual», sin garantía de
comerciabilidad ni de idoneidad para un fin determinado, y su autor no podrá ser
considerado responsable de ningún daño derivado de su uso. El texto de la
licencia prevalece sobre este resumen.

- **Revise el contenido antes de publicarlo.** Las protecciones cubren los bloques de código, el
  código en línea, las URL, las anclas y las citas del modo `--news`, pero no los
  títulos, las tablas, el front matter ni el significado de sus frases.
- **Sus documentos se envían al proveedor elegido**, sujetos a sus condiciones
  de uso y su política de datos. Algunos modelos gratuitos pueden
  reutilizar sus intercambios para el entrenamiento, y las condiciones de Antigravity
  permiten a Google reutilizarlos y hacer que sean revisados por personas,
  incluso con una suscripción de pago; un modelo local es la única opción que evita
  que algún dato salga de su máquina.
- **Las llamadas a la API se le facturan.** Este programa no limita el
  gasto: un documento largo, una reanudación tras un fallo o un modelo que razona
  mucho tienen un coste mayor.
- **Las mediciones publicadas son observaciones fechadas**, no garantías.

Los nombres de productos y empresas mencionados pertenecen a sus respectivos
titulares. Este proyecto no está afiliado a ninguno de ellos.

**Artículo traducido del fr al es con gpt-5.6-sol.**

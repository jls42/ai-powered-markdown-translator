# Traductor de Markdown con IA

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code smells"></a>
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
matter. Nueve formas de invocar un modelo: cinco API, dos suscripciones sin
facturación por uso y dos routers; además de una medición publicada de lo que cada
modelo preserva realmente.

## En resumen

- **Nueve vías de provider**: API de OpenAI, Mistral, Claude, Gemini y Grok;
  suscripciones a ChatGPT (Codex) y Grok sin facturación por uso; routers
  OpenCode (open source, gratuito o local) y OpenRouter (más de 400 modelos).
- **Nada queda mal por perder un token**: los bloques de código, el código en línea,
  las URL, las anclas y las citas se sustituyen por tokens antes de la llamada y
  se verifican al regresar. Si falta alguno, el archivo no se escribe.
- **Documentos largos**: segmentación según la ventana del modelo.
- **Modo `--news`**: citas en inglés protegidas y banderas gestionadas por
  idioma, para artículos de seguimiento.
- **Modo `--eco`**: modelos rápidos y más baratos.
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
completa lo que el anterior haya dejado vacío.

|     | Dónde                                         | Para qué                                  |
| --- | --------------------------------------------- | ----------------------------------------- |
| 1   | Variables de entorno                          | CI, contenedores, excepción puntual       |
| 2   | `.env` del directorio actual (o de uno superior) | una clave específica de un proyecto       |
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
del usuario sigue `XDG_CONFIG_HOME` (solo una ruta absoluta) y `%APPDATA%`
en Windows. Sin una clave, el comando enumera las tres ubicaciones.

**El `.env` de un proyecto no puede redirigir las llamadas.** Proporciona claves,
nunca un destino: cualquier variable en `_BASE_URL`, `_API_BASE` o
`_ENDPOINT`, los proxies (`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`), los
almacenes de certificados (`SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`,
`CURL_CA_BUNDLE`) y `XDG_CONFIG_HOME` / `APPDATA` se ignoran allí, con una
advertencia. Un repositorio clonado no debe poder desviar tu clave. Este
archivo también se lee sin interpolación: `NOM=${OPENAI_API_KEY}` no copia
la clave allí. Define estas variables en el entorno o en
`~/.config/aipmt/.env`.

Variables opcionales: `XAI_BASE_URL` (valor predeterminado: `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (segundos por llamada, valor predeterminado: 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(valor predeterminado: 600), `GROK_BIN`, `GROK_HOME` (valor predeterminado: `~/.grok`), `GROK_TIMEOUT`
(valor predeterminado: 900), `GROK_TRANSLATE_SANDBOX`, `OPENCODE_BIN`, `OPENCODE_TIMEOUT`
(valor predeterminado: 600), `OPENROUTER_BASE_URL` (se requiere `https://`), `OPENROUTER_TIMEOUT`
(valor predeterminado: 900), `OPENROUTER_PREFLIGHT_TIMEOUT` (valor predeterminado: 30). Cada una se detalla
en la sección de su provider.

## Primeros pasos

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

Traducir `document.md` al español genera `document-es.md` en `--target_dir`;
con `--include_model`, `document-es-gpt-5.6-terra.md`. La extensión pasa a ser
siempre `.md` — `article.mdx` genera `article-en.md` — salvo con
`--keep_filename`, que conserva el nombre original. Una traducción ya existente
se omite sin `--force`.

Códigos de salida: `0` si todo se completó o se omitió, `1` si queda algún archivo
con error (se muestra una lista en la salida de error), `2` si el problema está en la configuración.
Un archivo con error nunca se escribe, aunque falle la propia escritura:
el contenido se escribe al lado y después se cambia su nombre. Basta con volver a ejecutar el comando.

## Qué modelo elegir

Medido con dos documentos reales, traducidos a los mismos catorce idiomas por
cada modelo. **La cifra es el número de idiomas, de un total de catorce, en los que la
traducción se escribe y nada difiere de la fuente.**

| Modelo               | Cómo acceder                     | Artículo de seguimiento denso | Este README  | Qué difiere y en cuántos idiomas                                                                                                      |
| -------------------- | -------------------------------- | ----------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | clave API de Google              | ✅ 14/14                      | ⚠️ 13/14     | 1 idioma de 14: una palabra más en negrita (ja)                                                                                       |
| **GPT-5.6 Sol**      | suscripción a ChatGPT o clave de OpenAI | ✅ 14/14                | ⚠️ 12/14     | 2 idiomas de 14: una palabra menos en negrita (ar, ja)                                                                                |
| **GLM-5.2**          | clave de OpenRouter              | ✅ 14/14                      | ⚠️ 11/14     | 3 idiomas de 14: una palabra menos en negrita (hi, ja, ko)                                                                            |
| Claude Sonnet 5      | clave API de Anthropic           | ⚠️ 11/14                      | ⚠️ 12/14     | 3 idiomas en el artículo: apareció un bloque de código (es, de, hi); 2 en este README: un enlace sin su marcado (sv), una palabra en negrita (zh) |
| Qwen 3.7 Flash       | clave de OpenRouter              | ❌ 8/14                       | ⚠️ 10/14     | 1 idioma rechazado en el artículo, otros 5 difieren; en este README, unas cuarenta palabras se pusieron en `code` (ar)          |
| Grok 4.6             | suscripción a Grok               | ❌ 8/14                       | sin calificar | 5 idiomas rechazados de 14 por falta de código en línea y URL devueltos; el neerlandés difiere por completo                           |
| GPT-OSS 20B          | modelo local (Ollama)            | ❌ 7/14                       | sin volver a medir | 4 idiomas rechazados de 14: el modelo dejaba fragmentos en francés y la protección los detuvo                                    |
| MiMo v2.5 (gratuito) | OpenCode Zen, sin cuenta         | ❌ 11/14                      | sin volver a medir | 1 idioma rechazado; una sección perdida en polaco                                                                                |
| Mistral Large        | clave API de Mistral             | ❌ 5/14                       | ❌ 1/14      | **desaparece una sección completa**: 1 idioma en el artículo (hi), 3 en este README (ar, hi, ko), además de 3 idiomas rechazados en el artículo |
| DeepSeek V4 Flash    | clave de OpenRouter              | ❌ 3/14                       | sin volver a medir | 10 idiomas rechazados de 14; 37 minutos por idioma                                                                               |

|     | Qué significa el símbolo                                                                                                                                                                              |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | los catorce idiomas traducidos y nada difiere de la fuente                                                                                                                                             |
| ⚠️  | los catorce idiomas traducidos; lo que difiere es el **marcado**: una palabra en negrita, un `code`, un enlace que pierde sus corchetes. No falta ningún texto, ninguna URL, ningún bloque de código ni ninguna sección |
| ❌  | al menos un idioma no pudo traducirse —el archivo se rechaza y no se escribe— **o** falta contenido en un archivo escrito                                                                              |

Conclusiones principales:

- **Una traducción rechazada no es una traducción dañada.** Cuando falta un token
  al regresar, el archivo no se escribe y el idioma cuenta como
  rechazado. Esto es lo que le ocurre a Grok en el artículo: pierde cuatro fragmentos de código en línea y
  tres URL ya en el primer segmento, en las cinco escrituras no latinas.
- **Esta red de seguridad no cubre los títulos, las tablas, el front matter ni el
  texto.** Un modelo que elimina una sección devuelve un archivo que la herramienta escribe
  sin protestar, como ocurre con Mistral. Estos elementos no pueden
  sustituirse por un token y las protecciones actuales no los controlan;
  `scripts/compare_structure.py` detecta una sección perdida, pero a posteriori.
- **Grok no tiene calificación para este README**: su sesión CLI caducó después de doce
  idiomas, once de ellos sin diferencias. Una campaña interrumpida no se califica.
- **La densidad del documento importa más que el idioma.** Grok funciona con
  README normales y falla con un artículo repleto de enlaces, incluso en
  neerlandés.

Fechas y documentos: la columna «Este README» se midió el 9 de septiembre de 2026
sobre una revisión fijada de este archivo (785 líneas, 285 fragmentos de código en línea, 89 líneas
de tabla), modificada desde entonces. La columna «Artículo de seguimiento denso» procede de
la campaña de los días 4 y 5 de septiembre sobre un artículo de 589 líneas, salvo la fila de
Grok, que se volvió a medir el 9 de septiembre con otra edición del mismo seguimiento. Las
tablas completas, las duraciones y el protocolo están en
[Mediciones detalladas](#mediciones-detalladas).

## Todas las opciones

| Opción                   | Descripción                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Archivo Markdown individual que se traducirá (alternativa a `--source_dir`)                                   |
| `--source_dir`           | Directorio de origen que contiene los archivos Markdown (valor predeterminado: `content/posts`)                |
| `--target_dir`           | Directorio de salida para los archivos traducidos (valor predeterminado: `traductions_en`)                      |
| `--source_lang`          | Idioma de origen (valor predeterminado: `fr`)                                                       |
| `--target_lang`          | Idioma de destino (valor predeterminado: `en`)                                                      |
| `--model`                | Modelo específico que se utilizará                                                                           |
| `--eco`                  | Utilizar los modelos económicos                                                                               |
| `--use_mistral`          | Utilizar la API de Mistral AI                                                                                 |
| `--use_claude`           | Utilizar la API de Claude                                                                                     |
| `--use_gemini`           | Utilizar la API de Gemini                                                                                     |
| `--use_grok`             | Utilizar la API de xAI (Grok): requiere `XAI_API_KEY`                                                        |
| `--use_codex`            | Utilizar el CLI de Codex con la cuota de la suscripción a ChatGPT                                             |
| `--use_grok_cli`         | Utilizar el CLI de Grok con la cuota de la suscripción a Grok                                                 |
| `--use_opencode`         | Utilizar OpenCode (open source) con el proveedor configurado en OpenCode; requiere `--model provider/modèle`              |
| `--use_openrouter`       | Utilizar OpenRouter: requiere `OPENROUTER_API_KEY` y `--model fournisseur/modèle`                                                 |
| `--force`                | Forzar una nueva traducción                                                                                   |
| `--keep_filename`        | Conservar el nombre de archivo original                                                                       |
| `--news`                 | Modo noticias: protege las citas en inglés y gestiona las banderas por idioma                                 |
| `--add_translation_note` | Añadir una nota de traducción                                                                                 |
| `--note_position`        | Posición de la nota: `top`, `bottom` (valor predeterminado) o `both`                   |
| `--note_format`          | Formato de la nota: `legacy` (valor predeterminado, párrafo en negrita) o `marker`                |
| `--include_model`        | Incluir el nombre del modelo en el archivo de salida                                                          |
| `--reasoning_effort`     | Esfuerzo de razonamiento de GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

Los ocho flags `--use_*` son mutuamente excluyentes: combinar dos provoca
un rechazo.

## Providers

### Mediante API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` cambia al nivel económico de cada proveedor.

| Provider   | Calidad (valor predeterminado)                         | Económico (`--eco`)       |
| ---------- | ------------------------------------------------------ | -------------------------------- |
| OpenAI     | `gpt-5.6-terra`                                       | `gpt-5.6-luna`                  |
| Claude     | `claude-sonnet-5`                                       | `claude-haiku-4-5`                  |
| Mistral    | `mistral-large-latest`                                       | `mistral-small-latest`                  |
| Gemini     | `gemini-3.7-flash`                                       | `gemini-3.1-flash-lite`                  |
| Codex      | `gpt-5.6-sol` (también `terra` y `luna` mediante `--model`) | `gpt-5.6-luna` |
| Grok API   | `grok-4.6`                                       | `grok-4.3`                  |
| Grok CLI   | `grok-4.6`                                       | `grok-4.5`                  |
| OpenCode   | `--model provider/modèle` obligatorio                           | igual: `--eco` sin efecto |
| OpenRouter | `--model fournisseur/modèle` obligatorio                           | igual: `--eco` sin efecto |
### Con la suscripción ChatGPT: `--use_codex`

Controla el CLI oficial de Codex: la traducción se descuenta de la cuota de la
suscripción ChatGPT, sin clave API ni facturación por uso.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- El binario se busca en `CODEX_BIN`, después en el `PATH` y, por último, en el paquete
  `openai-codex-cli-bin`. `~/.codex/auth.json` nunca se lee.
- `OPENAI_API_KEY` y `CODEX_API_KEY` se eliminan del entorno del
  subproceso: la presencia de una clave nunca provoca el cambio a la API.
- Cada segmento cuesta al menos un «mensaje» de la ventana de 5 horas, dos
  si su validación falla y se vuelve a intentar. OpenAI anuncia, a modo
  de estimación, entre 250 y 2 000 mensajes/5 h para `gpt-5.6-luna` (`--eco`) y
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

### Con la suscripción Grok: `--use_grok_cli`

El mismo principio con el CLI oficial Grok Build, mediante la suscripción SuperGrok o
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Confinamiento más débil que Codex.** El sandbox del sistema operativo de Grok no se aplica
  en muchos equipos Linux recientes (AppArmor, sockets de runtime de
  contenedores), y un perfil que no puede aplicarse se inicia silenciosamente sin
  confinamiento. Por tanto, el script no solicita ningún perfil de forma predeterminada, lo
  advierte y se apoya en las reglas `--deny` del CLI, incluida la regla general `*`,
  la única capa que se niega a iniciarse en vez de retirar la protección sin
  avisar. `GROK_TRANSLATE_SANDBOX=read-only` exige el sandbox del sistema operativo y el inicio
  falla si la máquina no puede aplicarlo.
- La cuota es semanal, se comparte con Chat, Imagine y Voice, y ningún
  comando permite consultarla: un lote puede consumir parte del uso conversacional
  sin avisar.
- Variables: `GROK_BIN`, `GROK_HOME` (directorio del CLI, valor predeterminado: `~/.grok`),
  `GROK_TIMEOUT` (valor predeterminado: 900), `GROK_TRANSLATE_SANDBOX`.

### Con el proveedor que prefiera: `--use_opencode`

[OpenCode](https://opencode.ai) es un agente de código open source (MIT) que
dirige las solicitudes a los proveedores configurados en él: clave API, suscripción,
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
cuyos intercambios pueden utilizarse para el entrenamiento, y esta elección no se hace
por usted.

Confinamiento en cada llamada:

- una configuración inline, con prioridad sobre la suya, define un agente `aipmt`
  que rechaza todas las herramientas (`permission: { "*": "deny" }`), con el uso compartido de
  sesiones desactivado, `--pure`, nunca `--auto`;
- directorio de trabajo desechable y vacío, con `OPENCODE_DISABLE_PROJECT_CONFIG` y
  `OPENCODE_DISABLE_CLAUDE_CODE` establecidos; sin ellos, OpenCode inserta en el
  prompt el `AGENTS.md` del directorio actual y `~/.claude/CLAUDE.md`. El
  `~/.config/opencode/AGENTS.md` global sigue insertándose, ya que OpenCode no permite
  excluirlo;
- contrato de salida: código de retorno 0, ningún evento `error`, ninguna llamada
  a herramientas, último paso en `stop`, texto no vacío y el agente `aipmt`
  cargado realmente; un `--agent` desconocido no hace que OpenCode falle, sino que
  recurre silenciosamente al agente de programación;
- no se transmite ninguna clave de `aipmt`, salvo `OPENCODE_API_KEY`, la clave
  del propio OpenCode. Los proveedores se configuran en OpenCode, no en
  el `.env` de `aipmt`.

Conviene saber:

- Los modelos gratuitos de Zen son variables, tienen límites no documentados y
  sus intercambios pueden utilizarse para el entrenamiento: son adecuados para documentación
  pública, no para contenido privado.
- Un modelo local debe ofrecer al menos 16 k tokens de contexto, ya que los segmentos
  pueden alcanzar los 16 000 caracteres. Ollama suele configurar 4 096: utilice
  un `Modelfile` con `PARAMETER num_ctx 32768`.
- `--eco` no tiene efecto; `--reasoning_effort` se transmite sin cambios como
  `--variant` de OpenCode.
- OpenCode registra cada sesión en `~/.local/share/opencode/`.
- Variables: `OPENCODE_BIN` (si no, el `PATH` y después `~/.opencode/bin/opencode`),
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

`reasoningEffort: "none"` desactiva el razonamiento que Ollama activa de forma predeterminada en estos
modelos y que un Modelfile no puede desactivar. Medido con una frase de
seis palabras: 919 tokens de razonamiento y 68 segundos sin la opción, 9 tokens con ella.

### Con más de 400 modelos: `--use_openrouter`

OpenRouter es un router con facturación por uso, mediante un crédito único, situado delante de
modelos alojados por terceros, incluidos los modelos chinos abiertos que ningún
otro proveedor ofrece aquí.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` es obligatorio. Un preflight, ejecutado antes de cualquier facturación, resuelve
dos particularidades del enrutamiento:

- **Un mismo modelo es servido por decenas de proveedores de alojamiento con límites
  diferentes**: para `z-ai/glm-5.3-flash`, hay 23 proveedores, uno de ellos limitado a
  2 048 tokens de salida. El preflight lee `/api/v1/models/{modèle}/endpoints`,
  descarta los proveedores con menos de 8 000 tokens de salida o cuyo estado esté degradado y
  fija los demás mediante `allow_fallbacks: false`.
- **El razonamiento se factura con la tarifa de salida**: 107 tokens frente a 2 en
  una respuesta «OK» de `z-ai/glm-5.2`. Está desactivado de forma predeterminada; los modelos
  que lo exigen reciben el menor esfuerzo que aceptan, ya que el valor predeterminado del
  catálogo puede saturar la salida antes de finalizar la traducción.
  `--reasoning_effort` mantiene la prioridad.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- La ventana de contexto procede del catálogo. Un modelo con menos de 16 400 tokens se
  rechaza antes de cualquier llamada: 8 400 para el prompt y el segmento, y un mínimo de 8 000
  para la salida.
- Un slug ausente del catálogo, un catálogo inaccesible o la ausencia
  de un proveedor que cumpla el límite detienen el comando.
- `finish_reason=length` con una salida vacía indica que el razonamiento ha consumido el
  presupuesto, no un truncamiento: el mensaje distingue ambos casos.
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
seguida de una cita en negrita: legible en GitHub y utilizable durante el build mediante un
plugin remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Mediciones detalladas

Todas las mediciones corresponden a traducciones ejecutadas realmente con `aipmt`, a
catorce idiomas: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Escritas** cuenta los archivos que superaron las comprobaciones; **Sin
diferencias**, aquellos en los que `scripts/compare_structure.py` no detecta ninguna: el mismo número de
secciones, subtítulos, enlaces, URL distintas, bloques de código,
códigos inline, filas de tabla, bloques de cita y palabras en negrita.

«Sin diferencias» significa «no se ha detectado nada», no «idéntico»: el comparador
cuenta elementos sin leer su contenido. No detecta ni un título de
nivel 4 eliminado, ni el texto de un código inline sustituido, ni una bandera
cambiada, y no evalúa el idioma.

### Artículo de seguimiento denso, modo `--news`

Una edición del [seguimiento de IA de jls42.org](https://jls42.org/fr/news):
589 líneas, 140 enlaces, 21 secciones y 3 citas en inglés protegidas. Campaña
del 4 y 5 de septiembre de 2026.

| Modelo                            | Acceso              | Escritas | Sin diferencias | Mediana/idioma |
| --------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                | API de Google      | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gpt-5.6-sol` (`--use_codex`)     | suscripción ChatGPT | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                    | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`              | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `claude-sonnet-5`                 | API de Anthropic   | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `opencode/mimo-v2.5-free`         | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`              | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`          | local              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`            | API de Mistral     | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)     | suscripción Grok   | 1/14    | ❌ 1/14      | 23 min 11 s    |

Grok volvió a medirse el 9 de septiembre con otra edición del mismo seguimiento
(356 líneas): 9 idiomas escritos de 14, 8 sin diferencias. Esta es la cifra que
aparece en la tabla inicial. No se incluyen tres campañas interrumpidas:
`qwen3.5-27b` (9 idiomas) y `kimi-k2.6` (4) por falta de crédito,
y `z-ai/glm-5.3-flash`, cuyos dos fallos se debieron a un ajuste de razonamiento
que el proveedor está corrigiendo. Las filas de OpenRouter se midieron con los
ajustes predeterminados del router, antes de `--use_openrouter`; `z-ai/glm-5.2`,
medido de nuevo con el proveedor incluido, obtiene el mismo 14/14. Las cifras se
recalcularon el 10 de septiembre con el comparador actual: `qwen3.8-flash` y
`qwen3.7-flash` ganan cada uno un idioma respecto a la primera
publicación; los demás no cambian.

### README de este proyecto, Markdown estándar

Revisión fijada el 9 de septiembre de 2026: 785 líneas, 285 códigos inline, 40
cierres de bloques y 89 filas de tabla. Cuatro traducciones en paralelo.

| Modelo                        | Escritas | Sin diferencias | Mediana/idioma | Diferencias                                                              |
| ----------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.7-flash`            | 14/14   | ⚠️ 13/14   | 36 s           | una palabra en negrita (ja)                                              |
| `claude-sonnet-5`             | 14/14   | ⚠️ 12/14   | 2 min 56 s     | un enlace (sv), una palabra en negrita (zh)                              |
| `gpt-5.6-sol` (`--use_codex`) | 14/14   | ⚠️ 12/14   | 6 min 46 s     | una palabra en negrita (ar, ja)                                          |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14   | ⚠️ 11/14   | 2 min 34 s     | una palabra en negrita (hi, ja, ko)                                      |
| `qwen/qwen3.7-flash`          | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 40 códigos inline añadidos en árabe; negrita (hi, ja, ko)                |
| `mistral-large-latest`        | 14/14   | ❌ 1/14    | 2 min 44 s     | una sección perdida (ar, hi, ko); bloques de código añadidos (ja, ko, ro, zh) |

No se incluyen dos campañas interrumpidas: Grok, cuya sesión CLI expiró
después de doce idiomas (once sin diferencias), y `qwen3.8-flash`, cuyo
proveedor devolvió un HTTP 429 después de dos. `opencode/mimo-v2.5-free` y `ollama/gpt-oss-20b-32k`
no volvieron a medirse con esta revisión; en la del 4 y 5 de septiembre,
277 líneas más corta, cada uno escribía 9 traducciones de 14, de las cuales 7
y 1 no presentaban diferencias.

### Cuatro README de proyectos conocidos

FastAPI, Ollama, tldr-pages y Vue.js, tomados tal cual de GitHub: documentos
más sencillos que los dos anteriores. La campaña se centró en los modelos
con dificultades; Gemini sirve como punto de comparación.

| Modelo                    | Alcance                    | Escritas | Sin diferencias |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 proyectos × 14 idiomas   | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 proyectos × 14 idiomas   | 55/56   | ❌ 47/56     |
| `grok-4.6` (suscripción)   | 4 proyectos × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 proyectos × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### Lo que no son estas mediciones

- **No son una clasificación exhaustiva**: solo OpenRouter ofrece más de cuatrocientos
  modelos; se han medido unos quince.
- **Son duraciones orientativas**: entre tres y seis traducciones en paralelo según
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
la suscripción ChatGPT de forma predeterminada, cuatro en paralelo. `REGEN_PROVIDER` y
`REGEN_MODEL` cambian la ruta; una API facturada (`openai`, `gemini`,
`grok`, `openrouter`) se rechaza sin `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` limita cada job (600 s, 1 800 s en Codex). Los detalles
de las herramientas están en `CLAUDE.md`.

## Proyectos que utilizan este script

- **[jls42.org](https://jls42.org)** — blog personal publicado en 15 idiomas. Su
  [seguimiento diario de IA](https://jls42.org/fr/news) se traduce cada día
  con esta herramienta y sirve como documento de referencia para las mediciones anteriores.

## Autor

Julien LE SAUX
Correo electrónico: contact@jls42.org

## Licencia

GNU GENERAL PUBLIC LICENSE Version 3. Consulte [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Advertencia

Este programa se distribuye **sin garantía alguna**, conforme a los términos de las
secciones 15 y 16 de la GPL v3: se proporciona «tal cual», sin garantía de calidad
comercial ni de idoneidad para un fin determinado, y su autor no podrá ser
considerado responsable de ningún daño derivado de su uso. El texto de la
licencia prevalece sobre este resumen.

- **Revise el contenido antes de publicarlo.** Las protecciones cubren los bloques de código, el
  código inline, las URL, los anchors y las citas del modo `--news`, pero no los
  títulos, las tablas, el front matter ni el significado de sus frases.
- **Sus documentos se envían al proveedor elegido**, sujetos a sus condiciones
  de uso y su política de datos. Algunos modelos gratuitos pueden
  reutilizar sus intercambios para el entrenamiento; un modelo local es la única
  opción que evita que cualquier dato salga de su máquina.
- **Las llamadas a la API se le facturan.** Este programa no limita el
  gasto: un documento largo, la reanudación después de un fallo o un modelo que razona
  mucho cuestan más.
- **Las mediciones publicadas son observaciones fechadas**, no garantías.

Los nombres de productos y empresas mencionados pertenecen a sus respectivos
titulares. Este proyecto no está afiliado a ninguno de ellos.

**Artículo traducido del fr al es con gpt-5.6-sol.**

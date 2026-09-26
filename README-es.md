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
matter. Diez formas de llamar a un modelo — cinco API, tres suscripciones sin
pago por uso, dos enrutadores — y una medición publicada de lo que cada
modelo preserva realmente.

## En resumen

- **Diez vías de proveedores**: API de OpenAI, Mistral, Claude, Gemini y Grok;
  suscripciones de ChatGPT (Codex), Grok y Google (Antigravity) sin pago por
  uso; enrutadores OpenCode (código abierto, gratuito o local) y OpenRouter
  (más de 400 modelos).
- **Nada incorrecto debido a un token perdido**: bloques de código, código en línea,
  URL, anclas y citas se reemplazan por tokens antes de la llamada y
  se verifican al regreso. Si falta uno, el archivo no se escribe.
- **Documentos largos**: segmentación según la ventana del modelo.
- **Modo `--news`**: citas en inglés protegidas y banderas gestionadas por
  idioma, para artículos de monitorización.
- **Modo `--eco`**: modelos rápidos y más económicos.
- **Nota de traducción** opcional, arriba, abajo o en ambos.

## Instalación

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 o más reciente. Para instalar desde el repositorio, consulte
[Contribuir](#contribuir).

## Configuración

Las claves se leen en tres lugares, de mayor a menor prioridad; cada uno solo
completa lo que el anterior deja vacío.

|     | Dónde                                         | Para qué                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variables de entorno                          | CI, contenedores, excepción puntual   |
| 2   | `.env` del directorio actual (o de uno superior) | una clave propia de un proyecto       |
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

`GEMINI_API_KEY` se acepta en lugar de `GOOGLE_API_KEY`. El archivo
de usuario sigue `XDG_CONFIG_HOME` (solo ruta absoluta) y `%APPDATA%`
en Windows. Sin clave, el comando enumera las tres ubicaciones.

**El `.env` de un proyecto no puede redirigir las llamadas ni elegir el programa
ejecutado.** Proporciona claves, nunca un destino ni un binario: cualquier
variable en `_BASE_URL`, `_API_BASE`, `_ENDPOINT` o `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, los proxies (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), los almacenes de certificados (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) y `XDG_CONFIG_HOME` /
`APPDATA` se ignoran en él, con una advertencia. Un repositorio clonado no debe
poder desviar su clave ni hacerle ejecutar su propio programa en la
primera traducción. Este archivo también se lee sin interpolación:
`NOM=${OPENAI_API_KEY}` no vuelve a copiar la clave allí. Coloque estas variables en
el entorno o en `~/.config/aipmt/.env`.

Variables opcionales: `XAI_BASE_URL` (predeterminado `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (segundos por llamada, predeterminado 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(predeterminado 600), `GROK_BIN`, `GROK_HOME` (predeterminado `~/.grok`), `GROK_TIMEOUT`
(predeterminado 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (predeterminado 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (predeterminado 600), `OPENROUTER_BASE_URL`
(se requiere `https://`), `OPENROUTER_TIMEOUT` (predeterminado 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (predeterminado 30). Cada una se detalla en la
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

`document.md` traducido al español genera `document-es.md` en `--target_dir`;
con `--include_model`, `document-es-gpt-5.6-terra.md`. La extensión pasa a ser
siempre `.md` — `article.mdx` genera `article-en.md` — excepto con
`--keep_filename`, que conserva el nombre original. Una traducción ya existente
se omite sin `--force`.

Códigos de salida: `0` si todo tuvo éxito o se omitió, `1` si queda un archivo
con error (lista en la salida de error), `2` si el problema es la configuración.
Un archivo con error nunca se escribe, incluso si la propia escritura falla:
el contenido se escribe al lado y luego se renombra. Basta con volver a ejecutarlo.

## Qué modelo elegir

Medido en dos documentos reales, traducidos a los mismos catorce idiomas por
cada modelo. **La cifra es el número de idiomas, de catorce, donde la
traducción se escribe y nada difiere de la fuente.**

| Modelo               | Cómo acceder                      | Artículo de monitorización denso | Este README  | Qué difiere y en cuántos idiomas                                                                                                      |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | clave de API de Google            | ✅ 14/14                | ⚠️ 13/14     | 1 idioma de 14: una palabra en negrita más (ja)                                                                                       |
| **Gemini 3.7 Flash** | suscripción de Google (Antigravity) | ✅ 14/14              | ⚠️ 13/14     | 1 idioma de 14: una palabra en negrita menos (ko)                                                                                     |
| **GPT-5.6 Sol**      | suscripción de ChatGPT o clave de OpenAI | ✅ 14/14         | ⚠️ 12/14     | 2 idiomas de 14: una palabra en negrita menos (ar, ja)                                                                                |
| **GLM-5.2**          | clave de OpenRouter               | ✅ 14/14                | ⚠️ 11/14     | 3 idiomas de 14: una palabra en negrita menos (hi, ja, ko)                                                                            |
| Claude Sonnet 5      | clave de API de Anthropic         | ⚠️ 11/14                | ⚠️ 12/14     | 3 idiomas en el artículo: un bloque de código apareció (es, de, hi); 2 en este README: un enlace sin su marcado (sv), una palabra en negrita (zh) |
| Qwen 3.7 Flash       | clave de OpenRouter               | ❌ 8/14                 | ⚠️ 10/14     | 1 idioma rechazado en el artículo, otros 5 difieren; en este README, unas cuarenta palabras puestas en `code` (ar)                   |
| Grok 4.6             | suscripción de Grok               | ❌ 8/14                 | sin calificar | 5 idiomas rechazados de 14, por falta de códigos en línea y URL devueltos; el neerlandés difiere en todo                              |
| GPT-OSS 20B          | modelo local (Ollama)             | ❌ 7/14                 | no remedido  | 4 idiomas rechazados de 14: el modelo dejaba fragmentos en francés, la protección los detuvo                                         |
| MiMo v2.5 (gratuito) | OpenCode Zen, sin cuenta          | ❌ 11/14                | no remedido  | 1 idioma rechazado; una sección perdida en polaco                                                                                     |
| Mistral Large        | clave de API de Mistral           | ❌ 5/14                 | ❌ 1/14      | **desaparece una sección entera**: 1 idioma en el artículo (hi), 3 en este README (ar, hi, ko) — y 3 idiomas rechazados en el artículo |
| DeepSeek V4 Flash    | clave de OpenRouter               | ❌ 3/14                 | no remedido  | 10 idiomas rechazados de 14; 37 minutos por idioma                                                                                   |

|     | Lo que significa el símbolo                                                                                                                                                                           |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | los catorce idiomas traducidos y nada difiere de la fuente                                                                                                                                            |
| ⚠️  | los catorce idiomas traducidos; lo que difiere es de **marcado** — una palabra en negrita, un `code`, un enlace que pierde sus corchetes. No falta ningún texto, URL, bloque de código ni sección |
| ❌  | al menos un idioma no se pudo traducir — el archivo es rechazado, no se escribe — **o** falta contenido en un archivo escrito                                                                        |

Puntos clave a tener en cuenta:

- **Una traducción rechazada no es una traducción dañada.** Cuando falta un
  token al regreso, el archivo no se escribe y el idioma cuenta como
  rechazado. Esto es lo que le ocurre a Grok en el artículo: cuatro códigos en línea y
  tres URL perdidos desde el primer segmento en las cinco escrituras no latinas.
- **Esta red de protección no cubre los títulos, las tablas, el front matter ni el
  texto.** Un modelo que elimina una sección devuelve un archivo que la herramienta escribe
  sin inmutarse — este es el caso de Mistral. Estos elementos no son
  reemplazables por un token y las protecciones actuales no los controlan;
  `scripts/compare_structure.py` detecta una sección perdida, pero a posteriori.
- **Grok no tiene calificación en este README**: su sesión de CLI expiró después de doce
  idiomas, once de ellos sin discrepancias. Una campaña interrumpida no se califica.
- **La densidad del documento importa más que el idioma.** Grok rinde bien en
  README ordinarios y decae en un artículo cargado de enlaces, incluso en
  neerlandés.

Fechas y documentos: la columna «Este README» se midió el 9 de septiembre de 2026
en una revisión congelada de este archivo (785 líneas, 285 códigos en línea, 89 líneas
de tabla), modificada desde entonces — excepto la fila de Antigravity, medida el
26 de septiembre en la revisión publicada con la versión 1.14.0, más corta (600 líneas,
257 códigos en línea, 85 líneas de tabla). La columna «Artículo de monitorización
denso» proviene de la campaña del 4 y 5 de septiembre sobre un artículo de 589 líneas,
excepto la fila de Grok, remedida el 9 de septiembre en otra edición del mismo
seguimiento, y la fila de Antigravity, medida el 26 de septiembre en el mismo artículo.
Las tablas completas, las duraciones y el protocolo se encuentran en
[Mediciones detalladas](#mediciones-detalladas).

## Todas las opciones

| Opción                   | Descripción                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Archivo Markdown único para traducir (alternativa a `--source_dir`)                                           |
| `--source_dir`           | Directorio de origen que contiene los archivos Markdown (predeterminado: `content/posts`)                      |
| `--target_dir`           | Directorio de salida para los archivos traducidos (predeterminado: `traductions_en`)                           |
| `--source_lang`          | Idioma de origen (predeterminado: `fr`)                                                             |
| `--target_lang`          | Idioma de destino (predeterminado: `en`)                                                            |
| `--model`                | Modelo específico a utilizar                                                                                  |
| `--eco`                  | Utilizar los modelos económicos                                                                               |
| `--use_mistral`          | Utilizar la API de Mistral AI                                                                                 |
| `--use_claude`           | Utilizar la API de Claude                                                                                     |
| `--use_gemini`           | Utilizar la API de Gemini                                                                                     |
| `--use_grok`             | Utilizar la API de xAI (Grok) — requiere `XAI_API_KEY`                                                       |
| `--use_codex`            | Utilizar el CLI de Codex con la cuota de la suscripción de ChatGPT                                            |
| `--use_grok_cli`         | Utilizar el CLI de Grok con la cuota de la suscripción de Grok                                                |
| `--use_antigravity`      | Utilizar el CLI de Antigravity (`agy`) con la cuota de la suscripción de Google AI Pro o Ultra       |
| `--use_opencode`         | Utilizar OpenCode (código abierto) hacia el proveedor configurado en OpenCode; requiere `--model provider/modèle`       |
| `--use_openrouter`       | Utilizar OpenRouter — requiere `OPENROUTER_API_KEY` y `--model fournisseur/modèle`                                                |
| `--force`                | Forzar la retraducción                                                                                        |
| `--keep_filename`        | Conservar el nombre de archivo original                                                                       |
| `--news`                 | Modo noticias: protege las citas en EN, gestiona las banderas por idioma                                      |
| `--add_translation_note` | Añadir una nota de traducción                                                                                 |
| `--note_position`        | Posición de la nota: `top`, `bottom` (predeterminado), o `both`                       |
| `--note_format`          | Formato de la nota: `legacy` (predeterminado, párrafo en negrita) o `marker`                     |
| `--include_model`        | Incluir el nombre del modelo en el archivo de salida                                                          |
| `--reasoning_effort`     | Esfuerzo de razonamiento GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

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

| Proveedor   | Calidad (por defecto)                                 | Económico (`--eco`)       |
| ----------- | ----------------------------------------------------- | --------------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`                   |
| Claude      | `claude-sonnet-5`                                       | `claude-haiku-4-5`                   |
| Mistral     | `mistral-large-latest`                                       | `mistral-small-latest`                   |
| Gemini      | `gemini-3.7-flash`                                       | `gemini-3.1-flash-lite`                   |
| Codex       | `gpt-5.6-sol` (también `terra` y `luna` mediante `--model`) | `gpt-5.6-luna` |
| Grok API    | `grok-4.6`                                       | `grok-4.3`                   |
| Grok CLI    | `grok-4.6`                                       | `grok-4.5`                   |
| Antigravity | `gemini-3.7-flash-medium`                                       | `gemini-3.7-flash-low`                   |
| OpenCode    | `--model provider/modèle` obligatorio                           | ídem — `--eco` sin efecto |
| OpenRouter  | `--model fournisseur/modèle` obligatorio                           | ídem — `--eco` sin efecto |

### Con la suscripción a ChatGPT: `--use_codex`

Controla la CLI oficial de Codex: la traducción se descuenta de la cuota de la
suscripción a ChatGPT, sin clave de API ni facturación por uso.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- El binario se busca en `CODEX_BIN`, luego en el `PATH`, y después en el paquete
  `openai-codex-cli-bin`. `~/.codex/auth.json` nunca se lee.
- `OPENAI_API_KEY` y `CODEX_API_KEY` se eliminan del entorno del
  subproceso: tener una clave presente nunca hace que se cambie a la API.
- Cada segmento cuesta al menos un «mensaje» de la ventana de 5 horas; dos
  si su validación falla y se reintenta. OpenAI anuncia, a modo
  de estimación, 250-2 000 mensajes/5 h para `gpt-5.6-luna` (`--eco`) y
  10-100 para `gpt-5.6-sol` en un plan Plus.
- `--model gpt-5.6-terra` y `--model gpt-5.6-luna` también pasan por
  la suscripción. Un modelo al que la cuenta no tiene derecho devuelve un 400 «model is
  not supported when using Codex with a ChatGPT account».
- Más lento que una API, y la diferencia aumenta con el tamaño del documento: en este README,
  6 min 46 s por idioma de mediana con `gpt-5.6-sol`, frente a 36 s para
  `gemini-3.7-flash`.
- Rechazado en CI (`CI` o `GITHUB_ACTIONS` definido): la suscripción se autentica
  mediante un archivo de sesión personal, que no debe estar en un runner
  compartido.
- Variables: `CODEX_BIN`, `CODEX_TIMEOUT` (segundos por segmento, por defecto 600).

### Con la suscripción a Grok: `--use_grok_cli`

Mismo principio con la CLI oficial Grok Build, en la suscripción SuperGrok o
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Aislamiento más débil que Codex.** El sandbox del SO de Grok no se aplica
  en muchos equipos Linux recientes (AppArmor, sockets de runtime
  de contenedores), y un perfil que no se puede aplicar se inicia sin aislamiento
  de forma silenciosa. Por lo tanto, el script no solicita ningún perfil por defecto, lo
  anuncia y se apoya en las reglas `--deny` de la CLI, incluido el comodín `*`; la única
  capa que prefiere negarse a iniciar antes que retirar la protección sin
  avisar. `GROK_TRANSLATE_SANDBOX=read-only` exige el sandbox del SO, y el inicio
  falla si la máquina no puede cumplirlo.
- La cuota es semanal, compartida con Chat, Imagine y Voice, y ningún
  comando permite consultarla: un lote puede consumir el uso conversacional
  sin previo aviso.
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

- **No queda ninguna vía de pago abierta.** agy solo recibe de su
  entorno una lista cerrada de variables (`PATH`, idioma y zona horaria,
  terminal, identidad, proxies y certificados, bus de sesión) y ninguna clave:
  varias de sus variables redirigen una llamada sin mostrar nada (comprobado:
  una envía el documento a una pasarela de terceros, otra a un proyecto
  de Google Cloud facturado), y una lista de denegación pasaba por alto algunas en cada revisión.
  Antes de cualquier segmento, `agy -p /config`, que no consume cuota, debe mostrar
  los créditos de IA de pago desactivados, sin clave de API ni proyecto de Google Cloud; un
  ajuste ausente se considera rechazo; de lo contrario, no se traduce nada; el registro de cada
  llamada debe certificar a continuación la suscripción (`authMethod=consumer`); de lo contrario, la
  respuesta es rechazada.
- **Aislamiento.** Cada llamada se ejecuta en un directorio personal privado y
  desechable, con un agente de traducción sin herramientas: sus ajustes, reglas,
  plugins, servidores MCP y hooks de agy no entran en él, nada se añade a su
  historial y el inicio de sesión permanece en el llavero, que aipmt nunca lee.
  Si un agente no se encuentra, agy recurre silenciosamente a su agente de programación
  y a sus herramientas: una línea completa del registro debe confirmar el agente correcto
  (un documento que cite este mensaje no la reemplaza); de lo contrario, se rechaza.
- **Plataformas**: Linux, en una sesión que disponga de un llavero (bus de sesión
  D-Bus, Secret Service); macOS es compatible, sin haber sido medido en él. Rechazado
  en Windows, donde agy no lee las variables que aíslan cada llamada, y
  en Linux sin bus de sesión (sesión SSH, contenedor, servidor): allí agy
  guarda su token en un archivo de `~/.gemini`, que el aislamiento oculta. El
  rechazo se produce antes de cualquier ejecución, indicando su causa, en lugar de un minuto
  de espera para un código de inicio de sesión.
- **Modelos**: los de `agy models`. Los Gemini llevan el nivel de esfuerzo en su nombre
  (`gemini-3.7-flash-low`…): un nombre sin sufijo se rechaza antes de la llamada, y
  `--reasoning_effort` no tiene efecto. Ambos valores por defecto se fijaron mediante una
  campaña en catorce idiomas (consulte [Mediciones detalladas]((#mediciones-detalladas))).
  Claude y GPT-OSS tienen su propia cuota, mucho más reducida: aproximadamente el 1 % de la
  ventana de 5 horas por llamada medida, frente al 0,05 % en Flash.
- **Cuota**: por grupo, una ventana de 5 horas y una semanal, prorrateadas
  según el coste en tokens. Medido en la cuenta del autor, según una
  campaña de 32 traducciones: aproximadamente medio punto de la ventana de 5 horas
  para un README de 40 000 caracteres en `gemini-3.7-flash-medium`; el límite
  semanal, por su parte, depende del nivel. El reintento sigue lo que agy declare
  como reintentable; en su defecto, una ventana agotada nunca se reintenta: hace
  fallar cada archivo hasta el restablecimiento que muestra `/usage`.
- **Más lento que la API**: en el artículo denso de las mediciones, Gemini 3.7 Flash
  tarda 3 min 14 s por idioma de mediana mediante la suscripción, frente a 1 min 18 s mediante
  la API.
- **Interrupción**: Ctrl-C, o un terminal cerrado, detienen agy junto con el
  comando en lugar de dejarle terminar su turno consumiendo su cuota; lo mismo
  aplica a Codex, Grok CLI y OpenCode. Con `nohup`, la traducción continúa.
- Rechazado en CI (`CI` o `GITHUB_ACTIONS` definido): la sesión reside en un
  llavero personal. En un runner, use `--use_gemini` con `GOOGLE_API_KEY`.
- Variables: `AGY_BIN` (si no, el `PATH`, luego `~/.local/bin/agy`),
  `AGY_TIMEOUT` (segundos por segmento, inicio incluido, por defecto 900).

**Condiciones de uso: su cuenta es la que está en juego.** Las
[condiciones de Antigravity](https://antigravity.google/terms) (sección 6) y sus
[preguntas frecuentes](https://antigravity.google/docs/faq/) prohíben acceder al servicio
mediante software de terceros utilizando la sesión de Antigravity (se mencionan
Claude Code, OpenClaw y OpenCode), bajo pena de suspensión de la cuenta. aipmt
no lee ni reutiliza el token: ejecuta el binario oficial en el
[modo headless](https://antigravity.google/docs/cli/headless/) que Google
documenta para scripts y CI. Un miembro de Google consideró «estándar»
ejecutar `agy -p` desde un script local para su propio trabajo
([foro oficial, 25 de septiembre de 2026, respuesta no contractual](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
ningún texto legal resuelve de forma explícita el caso de una herramienta distribuida como esta.

**Solo documentos públicos.** Según la sección 5 de las mismas condiciones, los
intercambios (prompts, respuestas, metadatos) pueden utilizarse para mejorar los
productos y el aprendizaje automático de Google, y ser revisados por
humanos, incluida la suscripción de pago. La exclusión se realiza mediante el ajuste
`enableTelemetry`, de efecto no documentado, que aipmt no define; sus ajustes
de agy no se trasladan a su aislamiento. No procese nada confidencial a través de él.

### Hacia el proveedor de su elección: `--use_opencode`

[OpenCode](https://opencode.ai) es un agente de código de código abierto (MIT) que
redirige hacia los proveedores configurados en su interior: clave de API, suscripción,
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
cuyos intercambios pueden utilizarse para entrenamiento, y esta elección no se toma
en su lugar.

Aislamiento en cada llamada:

- una configuración inline, prioritaria sobre la suya, define un agente `aipmt`
  cuyas herramientas están todas denegadas (`permission: { "*": "deny" }`), uso compartido de
  sesión desactivado, `--pure`, nunca `--auto`;
- directorio de trabajo desechable y vacío, `OPENCODE_DISABLE_PROJECT_CONFIG` y
  `OPENCODE_DISABLE_CLAUDE_CODE` configurados: sin ellos, OpenCode inyecta en el
  prompt el `AGENTS.md` del directorio actual y `~/.claude/CLAUDE.md`. El
  `~/.config/opencode/AGENTS.md` global sigue inyectándose, ya que OpenCode no permite
  descartarlo;
- contrato de salida: código de retorno 0, ningún evento `error`, ninguna llamada
  a herramientas, último paso en `stop`, texto no vacío y el agente `aipmt`
  efectivamente cargado (un `--agent` desconocido no hace fallar a OpenCode, sino que
  recurre silenciosamente al agente de programación);
- no se transmite ninguna clave de `aipmt`, excepto `OPENCODE_API_KEY`, la clave
  del propio OpenCode. Los proveedores se configuran en OpenCode, no en
  el `.env` de `aipmt`.

A tener en cuenta:

- Los modelos gratuitos de Zen son variables, tienen límites no documentados y
  sus intercambios pueden utilizarse para entrenamiento: apto para documentación
  pública, no para contenido privado.
- Un modelo local debe ofrecer al menos 16 k tokens de contexto, ya que los segmentos
  tienen hasta 16 000 caracteres. Ollama suele configurar 4 096: configure
  un `Modelfile` con `PARAMETER num_ctx 32768`.
- `--eco` no tiene efecto; `--reasoning_effort` se transmite tal cual como
  `--variant` de OpenCode.
- OpenCode registra cada sesión en `~/.local/share/opencode/`.
- Variables: `OPENCODE_BIN` (si no, el `PATH`, luego `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (segundos por segmento, por defecto 600). `OPENCODE_CONFIG`
  se pasa tal cual a OpenCode.

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

`reasoningEffort: "none"` desactiva el razonamiento (thinking) que Ollama activa por defecto en estos
modelos, y que un Modelfile no puede desactivar. Medido en una frase de
seis palabras: 919 tokens de razonamiento y 68 segundos sin la opción, 9 tokens con ella.

### Hacia más de 400 modelos: `--use_openrouter`

OpenRouter es un enrutador facturado por uso, con un saldo único, que da acceso a
modelos alojados por terceros, incluidos los modelos abiertos chinos que ningún
otro proveedor expone aquí.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` es obligatorio. Una comprobación previa (preflight), ejecutada antes de cualquier facturación, gestiona
dos particularidades del enrutamiento:

- **Un mismo modelo es servido por decenas de proveedores con límites
  diferentes**: en `z-ai/glm-5.3-flash`, 23 proveedores, uno de ellos limitado a
  2 048 tokens de salida. El preflight consulta `/api/v1/models/{modèle}/endpoints`,
  descarta los proveedores con menos de 8 000 tokens de salida o con estado degradado, y
  fija los restantes mediante `allow_fallbacks: false`.
- **El razonamiento se factura a la tarifa de salida**: 107 tokens frente a 2 en
  una respuesta «OK» de `z-ai/glm-5.2`. Está desactivado por defecto; los modelos
  que lo exigen reciben el nivel de esfuerzo más bajo que acepten, ya que el valor por defecto
  del catálogo podría saturar la salida antes de que finalice la traducción.
  `--reasoning_effort` sigue teniendo prioridad.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- La ventana de contexto procede del catálogo. Un modelo con menos de 16 400 tokens se
  rechaza antes de cualquier llamada: 8 400 para el prompt y el segmento, y 8 000 de salida
  como mínimo.
- Un slug ausente del catálogo, un catálogo inaccesible o la ausencia
  de un proveedor que cumpla el límite detienen el comando.
- `finish_reason=length` con una salida vacía indica un presupuesto consumido por el
  razonamiento, no un truncamiento: el mensaje lo distingue.
- `--eco` no tiene efecto.
- Variables: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (por defecto `https://openrouter.ai/api/v1`, `https://`
  requerido), `OPENROUTER_TIMEOUT` (por defecto 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (por defecto 30).

### Nota de traducción

`--add_translation_note` añade una nota, en `bottom` (por defecto), `top` (después del
front matter) o `both` (`--note_position`), con el formato `legacy` (párrafo en
negrita, por defecto) o `marker` (`--note_format`). El formato `marker` es una
definición de referencia de Markdown invisible,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
seguida de una cita en negrita: legible en GitHub, utilizable en la compilación mediante un
plugin de remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Mediciones detalladas

Todas las mediciones son traducciones ejecutadas realmente con `aipmt`, hacia
catorce idiomas: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Escritas** cuenta los archivos que los mecanismos de protección han dejado pasar; **Sin
discrepancia** aquellos donde `scripts/compare_structure.py` no detecta nada: mismo número de
secciones, subtítulos, enlaces, URL distintas, bloques de código,
códigos en línea, filas de tabla, bloques de cita y palabras en negrita.

«Sin discrepancia» significa «nada detectado», no «idéntico»: el comparador
cuenta elementos sin leer su contenido. No señala un título de
nivel 4 eliminado, ni el texto de un código en línea modificado, ni una bandera
intercambiada, y no evalúa la calidad lingüística.

### Artículo de seguimiento denso, modo `--news`

Una edición del [seguimiento de IA de jls42.org](https://jls42.org/fr/news):
589 líneas, 140 enlaces, 21 secciones, 3 citas en inglés protegidas. Campaña
del 4 y 5 de septiembre de 2026.

| Modelo                                          | Acceso              | Escritas | Sin diferencias | Mediana/idioma |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | API de Google      | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | suscripción a Google | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | suscripción a ChatGPT | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `claude-sonnet-5`                               | API de Anthropic   | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | local              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | API de Mistral     | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | suscripción a Grok | 1/14    | ❌ 1/14      | 23 min 11 s    |

Grok se volvió a medir el 9 de septiembre en otra edición del mismo seguimiento
(356 líneas): 9 idiomas escritos de 14, 8 sin diferencias. Esta es la cifra que
figura en la tabla principal. No se incluyen tres campañas interrumpidas:
`qwen3.5-27b` (9 idiomas) y `kimi-k2.6` (4) por falta de crédito,
`z-ai/glm-5.3-flash`, cuyos dos fallos se debieron a un ajuste de razonamiento
que el proveedor corrige desde entonces. Las filas de OpenRouter se midieron con los
ajustes por defecto del enrutador, antes de `--use_openrouter`; `z-ai/glm-5.2`,
medido de nuevo con el proveedor suministrado, ofrece el mismo 14/14. Las cifras se
recalcularon el 10 de septiembre con el comparador actual: `qwen3.8-flash` y
`qwen3.7-flash` ganan cada uno un idioma respecto a la primera
publicación, los demás no han cambiado.

La fila `--use_antigravity` se midió el 26 de septiembre en el mismo artículo,
con cuatro traducciones en paralelo. En inglés, el modelo eliminó por sí mismo las
tres líneas de traducción al francés bajo las citas, sin inventar banderas,
y las citas en inglés quedaron intactas: la limpieza de respaldo no
tuvo nada que hacer. En `--eco` (`gemini-3.7-flash-low`), solo en cuatro
idiomas (en, ja, ar, hi): 4 escritas de 4, todas sin diferencias, 1 min 52 s de
mediana.

### README de este proyecto, Markdown estándar

Revisión congelada el 9 de septiembre de 2026: 785 líneas, 285 códigos en línea, 40
cierres de bloques, 89 líneas de tabla. Cuatro traducciones en paralelo.

| Modelo                                          | Escritas | Sin diferencias | Mediana/idioma | Lo que difiere                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | una palabra en negrita (ja)                                              |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | una palabra en negrita (ko)                                              |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | un enlace (sv), una palabra en negrita (zh)                              |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | una palabra en negrita (ar, ja)                                          |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | una palabra en negrita (hi, ja, ko)                                      |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 40 códigos en línea añadidos en árabe; negrita (hi, ja, ko)              |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | una sección perdida (ar, hi, ko); bloques de código añadidos (ja, ko, ro, zh) |

No se incluyen dos campañas interrumpidas: Grok, con sesión CLI caducada
tras doce idiomas (once sin diferencias), y `qwen3.8-flash`, HTTP 429 de su
alojamiento tras dos. `opencode/mimo-v2.5-free` y `ollama/gpt-oss-20b-32k`
no se volvieron a medir en esta revisión; en la del 4 y 5 de septiembre,
277 líneas más corta, cada uno escribió 9 traducciones de 14, de las cuales 7
y 1 no tuvieron diferencias.

La fila `--use_antigravity` no se midió en la revisión congelada, sino el
26 de septiembre en la publicada con la 1.14.0: 600 líneas, 257 códigos en línea,
30 cierres de bloques, 85 líneas de tabla. Al ser 185 líneas más corta, no
se puede comparar directamente término a término con las demás filas.

### Cuatro README de proyectos conocidos

FastAPI, Ollama, tldr-pages y Vue.js, tomados tal cual de GitHub —
documentos más sencillos que los dos anteriores. La campaña se centró en los modelos
con dificultades; Gemini sirve aquí como punto de comparación.

| Modelo                    | Alcance                    | Escritas | Sin diferencias |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 proyectos × 14 idiomas   | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 proyectos × 14 idiomas   | 55/56   | ❌ 47/56     |
| `grok-4.6` (suscripción)   | 4 proyectos × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 proyectos × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### Lo que estas mediciones no son

- **No es una clasificación exhaustiva**: solo OpenRouter ofrece más de cuatrocientos
  modelos, y se ha medido una quincena.
- **Duraciones orientativas**: de tres a seis traducciones en paralelo según
  las campañas, y el rendimiento de un proveedor varía a lo largo del día.
- **Observaciones fechadas**: los modelos cambian bajo el mismo nombre, y sus
  documentos no son los nuestros.

Para repetir la medición en sus documentos, en una copia congelada del archivo:

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
regeneran con `./regen_translations.sh --force` — Codex y `gpt-5.6-sol` en
la suscripción a ChatGPT por defecto, cuatro en paralelo. `REGEN_PROVIDER` y
`REGEN_MODEL` cambian la ruta: `antigravity` se mantiene en una suscripción, la
de Google, y se ejecuta sin excepción; una API facturada (`openai`, `gemini`,
`grok`, `openrouter`) se rechaza sin `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` limita el tiempo de cada tarea (600 s, 1800 s en Codex y
Antigravity). Los detalles de las herramientas se encuentran en `CLAUDE.md`.

## Proyectos que utilizan este script

- **[jls42.org](https://jls42.org)** — blog personal publicado en 15 idiomas. Su
  [seguimiento diario de IA](https://jls42.org/fr/news) es traducido a diario
  por esta herramienta y sirve como documento de referencia para las mediciones anteriores.

## Autor

Julien LE SAUX
Email: contact@jls42.org

## Licencia

GNU GENERAL PUBLIC LICENSE Versión 3. Consulte [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Advertencia

Este programa se distribuye **sin ninguna garantía**, según los términos de las
secciones 15 y 16 de la GPL v3: suministrado «tal cual», sin garantía de calidad
comercial ni de idoneidad para un uso particular, y su autor no se hace
responsable de ningún daño resultante de su utilización. El texto de la
licencia prevalece sobre este resumen.

- **Revise antes de publicar.** Las protecciones cubren los bloques de código, el
  código en línea, las URL, las anclas y las citas del modo `--news` — no los
  títulos, ni las tablas, ni el front matter, ni el sentido de sus frases.
- **Sus documentos se envían al proveedor seleccionado**, bajo sus condiciones
  de uso y su política de datos. Algunos modelos gratuitos pueden
  reutilizar sus intercambios para el entrenamiento, y las condiciones de Antigravity
  permiten a Google reutilizarlos y hacer que personas los revisen,
  incluso con suscripción de pago; un modelo local es la única vía que no permite
  la salida de ningún dato de su equipo.
- **Las llamadas a la API se le facturan a usted.** Este programa no establece un límite de
  gasto: un documento extenso, una reanudación tras un fallo o un modelo que razone
  mucho supondrán un coste mayor.
- **Las mediciones publicadas son observaciones fechadas**, no garantías.

Los nombres de productos y empresas mencionados pertenecen a sus respectivos
propietarios. Este proyecto no está afiliado a ninguno de ellos.

**Artículo traducido del fr al es con gemini-3.7-flash-medium.**

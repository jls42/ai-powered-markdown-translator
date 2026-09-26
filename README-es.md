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

Traduce archivos Markdown de un idioma a otro preservando la estructura:
bloques de código, código en línea, URL, anclas, tablas y front matter.
Diez formas de llamar a un modelo — cinco API, tres suscripciones sin
facturación por uso, dos enrutadores — y una medición publicada de lo que cada
modelo realmente preserva.

## En resumen

- **Diez rutas de proveedores**: API de OpenAI, Mistral, Claude, Gemini y Grok;
  suscripciones a ChatGPT (Codex), Grok y Google (Antigravity) sin facturación
  por uso; enrutadores OpenCode (código abierto, gratuito o local) y OpenRouter
  (más de 400 modelos).
- **Nada incorrecto debido a un token perdido**: bloques de código, código en
  línea, URL, anclas y citas se reemplazan por tokens antes de la llamada y se
  verifican al regreso. Si falta uno, el archivo no se escribe.
- **Documentos extensos**: segmentación según la ventana del modelo.
- **Modo `--news`**: citas en inglés protegidas y banderas gestionadas por
  idioma, para artículos de seguimiento informativo.
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
cubre lo que el anterior deja vacío.

|     | Dónde                                         | Para qué                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variables de entorno                          | CI, contenedores, excepciones puntuales |
| 2   | `.env` del directorio actual (o de un padre) | una clave propia de un proyecto       |
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

Se acepta `GEMINI_API_KEY` en lugar de `GOOGLE_API_KEY`. El archivo de usuario
sigue `XDG_CONFIG_HOME` (solo ruta absoluta) y `%APPDATA%` en Windows. Sin
clave, el comando enumera las tres ubicaciones.

**El `.env` de un proyecto no puede redirigir las llamadas ni elegir el programa
ejecutado.** Proporciona claves, nunca un destino ni un binario: cualquier
variable en `_BASE_URL`, `_API_BASE`, `_ENDPOINT` o `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, los proxies (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), los almacenes de certificados (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) y `XDG_CONFIG_HOME` /
`APPDATA` se ignoran en él, con una advertencia. Un repositorio clonado no debe
poder desviar su clave ni hacerle ejecutar su propio programa en la
primera traducción. Este archivo también se lee sin interpolación:
`NOM=${OPENAI_API_KEY}` no copia la clave allí. Coloque estas variables en
el entorno o en `~/.config/aipmt/.env`.

Variables opcionales: `XAI_BASE_URL` (por defecto `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (segundos por llamada, por defecto 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(por defecto 600), `GROK_BIN`, `GROK_HOME` (por defecto `~/.grok`), `GROK_TIMEOUT`
(por defecto 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (por defecto 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (por defecto 600), `OPENROUTER_BASE_URL`
(se requiere `https://`), `OPENROUTER_TIMEOUT` (por defecto 900),
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

`document.md` traducido al español da como resultado `document-es.md` en `--target_dir`;
con `--include_model`, `document-es-gpt-5.6-terra.md`. La extensión siempre pasa a ser
`.md` — `article.mdx` da como resultado `article-en.md` —, excepto con
`--keep_filename`, que conserva el nombre original. Una traducción ya presente
se omite sin `--force`.

Códigos de salida: `0` si todo finalizó con éxito o se omitió, `1` si queda algún archivo
con error (lista en la salida de error), `2` si la causa es la configuración.
Un archivo fallido nunca se escribe, incluso si la propia escritura falla:
el contenido se escribe al lado y luego se renombra. Basta con volver a ejecutar.

## Qué modelo elegir

Medido en dos documentos reales, traducidos a los mismos catorce idiomas por
cada modelo. **La cifra representa el número de idiomas, sobre catorce, en los que la
traducción se escribe y nada difiere del origen.**

| Modelo               | Cómo acceder                      | Artículo de seguimiento denso | Este README  | Qué difiere y en cuántos idiomas                                                                                                      |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.8 Flash** | suscripción a Google (Antigravity)| ✅ 14/14                | ✅ 14/14     | nada, en ninguno de los dos documentos                                                                                                |
| **Gemini 3.7 Flash** | clave de API de Google            | ✅ 14/14                | ⚠️ 13/14     | 1 idioma de 14: una palabra más en negrita (ja)                                                                                       |
| **Gemini 3.7 Flash** | suscripción a Google (Antigravity)| ✅ 14/14                | ⚠️ 13/14     | 1 idioma de 14: una palabra menos en negrita (ko)                                                                                      |
| **GPT-5.6 Sol**      | suscripción a ChatGPT o clave de OpenAI | ✅ 14/14          | ⚠️ 12/14     | 2 idiomas de 14: una palabra menos en negrita (ar, ja)                                                                                 |
| **GLM-5.2**          | clave de OpenRouter               | ✅ 14/14                | ⚠️ 11/14     | 3 idiomas de 14: una palabra menos en negrita (hi, ja, ko)                                                                             |
| Claude Sonnet 5      | clave de API de Anthropic         | ⚠️ 11/14                | ⚠️ 12/14     | 3 idiomas en el artículo: apareció un bloque de código (es, de, hi); 2 en este README: un enlace sin su formato (sv), una palabra en negrita (zh) |
| Qwen 3.7 Flash       | clave de OpenRouter               | ❌ 8/14                 | ⚠️ 10/14     | 1 idioma rechazado en el artículo, otros 5 difieren; en este README, unas cuarenta palabras puestas en `code` (ar)                   |
| Grok 4.6             | suscripción a Grok                | ❌ 8/14                 | sin calificar| 5 idiomas rechazados de 14 por falta de códigos en línea y URL devueltos; el neerlandés difiere en todo                                |
| GPT-OSS 20B          | modelo local (Ollama)             | ❌ 7/14                 | no remedido  | 4 idiomas rechazados de 14: el modelo dejaba fragmentos en francés, la protección los detuvo                                         |
| MiMo v2.5 (gratuito) | OpenCode Zen, sin cuenta          | ❌ 11/14                | no remedido  | 1 idioma rechazado; una sección perdida en polaco                                                                                     |
| Mistral Large        | clave de API de Mistral           | ❌ 5/14                 | ❌ 1/14      | **desaparece una sección entera**: 1 idioma en el artículo (hi), 3 en este README (ar, hi, ko) — y 3 idiomas rechazados en el artículo |
| DeepSeek V4 Flash    | clave de OpenRouter               | ❌ 3/14                 | no remedido  | 10 idiomas rechazados de 14; 37 minutos por idioma                                                                                   |

|     | Qué indica el símbolo                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | los catorce idiomas traducidos y nada difiere del origen                                                                                                                                              |
| ⚠️  | los catorce idiomas traducidos; lo que difiere es de **formato** — una palabra en negrita, un `code`, un enlace que pierde sus corchetes. No falta ningún texto, ninguna URL, ningún bloque de código ni ninguna sección |
| ❌  | al menos un idioma no se pudo traducir — el archivo se rechaza, no se escribe — **o** falta contenido en un archivo escrito                                                                         |

Conclusiones clave:

- **Una traducción rechazada no es una traducción dañada.** Cuando falta un token
  al regresar, el archivo no se escribe y el idioma se contabiliza como
  rechazado. Es lo que le ocurre a Grok en el artículo: cuatro fragmentos de código en línea y
  tres URL perdidos desde el primer segmento, en las cinco escrituras no latinas.
- **Esta red de seguridad no cubre los encabezados, las tablas, el front matter ni el
  texto.** Un modelo que elimina una sección genera un archivo que la herramienta escribe
  sin dudar —este es el caso de Mistral—. Estos elementos no pueden
  reemplazarse por un token y las comprobaciones actuales no los controlan;
  `scripts/compare_structure.py` detecta una sección perdida, pero a posteriori.
- **Grok no tiene calificación en este README**: su sesión de CLI expiró tras doce
  idiomas, once de ellos sin desviaciones. Una campaña interrumpida no se califica.
- **La densidad del documento importa más que el idioma.** Grok resiste en
  README normales y falla en un artículo cargado de enlaces, incluso en
  neerlandés.

Fechas y documentos: la columna «Este README» se midió el 9 de septiembre de 2026
en una revisión congelada de este archivo (785 líneas, 285 códigos en línea, 89 líneas
de tabla), modificada desde entonces —excepto las dos filas de Antigravity, medidas el
26 de septiembre en la revisión publicada con la 1.14.0, más corta (600 líneas,
257 códigos en línea, 85 líneas de tabla)—. La columna «Artículo de seguimiento
denso» proviene de la campaña del 4 y 5 de septiembre sobre un artículo de 589 líneas,
salvo la fila de Grok, remedida el 9 de septiembre en otra edición del
mismo seguimiento, y las dos filas de Antigravity, medidas el 26 de septiembre en el mismo
artículo.
Las tablas completas, las duraciones y el protocolo se encuentran en
[Mediciones detalladas](#mediciones-detalladas).

## Todas las opciones

| Opción                   | Descripción                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Archivo Markdown único para traducir (alternativa a `--source_dir`)                                           |
| `--source_dir`           | Directorio de origen que contiene los archivos Markdown (por defecto: `content/posts`)                         |
| `--target_dir`           | Directorio de destino para los archivos traducidos (por defecto: `traductions_en`)                              |
| `--source_lang`          | Idioma de origen (por defecto: `fr`)                                                                 |
| `--target_lang`          | Idioma de destino (por defecto: `en`)                                                                |
| `--model`                | Modelo específico que se utilizará                                                                            |
| `--eco`                  | Utilizar los modelos económicos                                                                              |
| `--use_mistral`          | Utilizar la API de Mistral AI                                                                                 |
| `--use_claude`           | Utilizar la API de Claude                                                                                     |
| `--use_gemini`           | Utilizar la API de Gemini                                                                                     |
| `--use_grok`             | Utilizar la API de xAI (Grok) — requiere `XAI_API_KEY`                                                       |
| `--use_codex`            | Utilizar la CLI de Codex con la cuota de la suscripción a ChatGPT                                              |
| `--use_grok_cli`         | Utilizar la CLI de Grok con la cuota de la suscripción a Grok                                                  |
| `--use_antigravity`      | Utilizar la CLI de Antigravity (`agy`) con la cuota de la suscripción a Google AI Pro o Ultra         |
| `--use_opencode`         | Utilizar OpenCode (código abierto) hacia el proveedor configurado en OpenCode; requiere `--model provider/modèle`        |
| `--use_openrouter`       | Utilizar OpenRouter — requiere `OPENROUTER_API_KEY` y `--model fournisseur/modèle`                                                |
| `--force`                | Forzar la retraducción                                                                                        |
| `--keep_filename`        | Conservar el nombre de archivo original                                                                       |
| `--news`                 | Modo de noticias: protege las citas en EN, gestiona las banderas por idioma                                   |
| `--add_translation_note` | Añadir una nota de traducción                                                                                 |
| `--note_position`        | Posición de la nota: `top`, `bottom` (por defecto) o `both`                             |
| `--note_format`          | Formato de la nota: `legacy` (por defecto, párrafo en negrita) o `marker`                          |
| `--include_model`        | Incluir el nombre del modelo en el archivo de salida                                                          |
| `--reasoning_effort`     | Esfuerzo de razonamiento GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`|

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
| Codex       | `gpt-5.6-sol` (también `terra` y `luna` por `--model`) | `gpt-5.6-luna`                   |
| Grok API    | `grok-4.6`                                       | `grok-4.3`                   |
| Grok CLI    | `grok-4.6`                                       | `grok-4.5`                   |
| Antigravity | `gemini-3.8-flash-medium`                                       | `gemini-3.7-flash-low`                   |
| OpenCode    | `--model provider/modèle` obligatorio                           | ídem — `--eco` sin efecto |
| OpenRouter  | `--model fournisseur/modèle` obligatorio                           | ídem — `--eco` sin efecto |

### Con la suscripción a ChatGPT: `--use_codex`

Controla la CLI oficial de Codex: la traducción se descuenta de la cuota de
la suscripción a ChatGPT, sin clave de API ni facturación por uso.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- El binario se busca en `CODEX_BIN`, luego en el `PATH`, luego en el paquete
  `openai-codex-cli-bin`. Nunca se lee `~/.codex/auth.json`.
- `OPENAI_API_KEY` e `CODEX_API_KEY` se eliminan del entorno del
  subproceso: la presencia de una clave nunca hace cambiar a la API.
- Cada segmento cuesta al menos un «mensaje» de la ventana de 5 horas; dos
  si su validación falla y se reintenta. OpenAI anuncia, a modo de
  estimación, entre 250 y 2 000 mensajes/5 h para `gpt-5.6-luna` (`--eco`) y
  entre 10 y 100 para `gpt-5.6-sol` en un plan Plus.
- `--model gpt-5.6-terra` e `--model gpt-5.6-luna` también pasan por
  la suscripción. Un modelo al que la cuenta no tiene derecho devuelve un 400 «model is
  not supported when using Codex with a ChatGPT account».
- Más lento que una API, y la diferencia aumenta con el tamaño del documento: en este README,
  una mediana de 6 min 46 s por idioma con `gpt-5.6-sol`, frente a 36 s para
  `gemini-3.7-flash`.
- Rechazado en CI (`CI` o `GITHUB_ACTIONS` definido): la suscripción se autentica
  mediante un archivo de sesión personal, que no debe estar en un runner
  compartido.
- Variables: `CODEX_BIN`, `CODEX_TIMEOUT` (segundos por segmento, por defecto 600).

### Con la suscripción a Grok: `--use_grok_cli`

Mismo principio con la CLI oficial Grok Build, con la suscripción a SuperGrok o
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Aislamiento más débil que Codex.** El sandbox del SO de Grok no se aplica
  en muchos equipos Linux recientes (AppArmor, sockets de runtime de
  contenedores), y un perfil que no puede aplicarse se inicia sin confinamiento de
  forma silenciosa. Por lo tanto, el script no solicita ningún perfil por defecto, lo anuncia y
  se apoya en las reglas `--deny` de la CLI, incluido el catch-all `*` —la única
  capa que se niega a iniciar en lugar de retirar la protección en
  silencio—. `GROK_TRANSLATE_SANDBOX=read-only` exige el sandbox del SO, y el inicio
  falla si la máquina no puede cumplirlo.
- La cuota es semanal, compartida con Chat, Imagine y Voice, y ningún
  comando permite consultarla: un lote puede consumir el uso conversacional
  sin previo aviso.
- Variables: `GROK_BIN`, `GROK_HOME` (directorio de la CLI, por defecto `~/.grok`),
  `GROK_TIMEOUT` (por defecto 900), `GROK_TRANSLATE_SANDBOX`.

### Con la suscripción a Google: `--use_antigravity`

Mismo principio con `agy`, la CLI oficial de Antigravity: para quienes pagan Google
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

- **Ninguna vía de pago queda abierta.** agy solo recibe de su
  entorno una lista cerrada de variables —`PATH`, idioma y zona horaria,
  terminal, identidad, proxies y certificados, bus de sesión— y ninguna clave:
  varias de sus variables desvían una llamada sin mostrar nada (medido:
  una envía el documento a una pasarela de terceros, otra a un proyecto
  facturado de Google Cloud), y una lista de exclusión pasaba cosas por alto en cada revisión.
  Antes de cada segmento, `agy -p /config`, que no consume cuota, debe mostrar
  los créditos de IA de pago desactivados, sin clave de API ni proyecto de Google Cloud —un
  ajuste ausente equivale a rechazo—; de lo contrario, no se traduce nada; el registro de cada
  llamada debe certificar a continuación la suscripción (`authMethod=consumer`), o de lo contrario la
  respuesta es rechazada.
- **Aislamiento.** Cada llamada se ejecuta en un directorio personal privado y
  desechable, con un agente de traducción sin herramientas: sus ajustes, reglas,
  plugins, servidores MCP y hooks de agy no entran en él, nada se añade a su
  historial y la conexión permanece en el llavero, el cual aipmt nunca lee.
  Si un agente no se encuentra, agy recurre silenciosamente a su agente de programación
  y a sus herramientas: una línea completa del registro debe confirmar el agente correcto —un
  documento que cite este mensaje no la sustituye—; de lo contrario, se rechaza.
- **Plataformas**: Linux, en una sesión que disponga de un llavero (bus de sesión
  D-Bus, Secret Service); se acepta macOS, sin haber sido medido en él. Rechazado
  en Windows, donde agy no lee las variables que aíslan cada llamada, y
  en Linux sin bus de sesión —sesión SSH, contenedor, servidor—: allí agy
  guarda su token en un archivo de `~/.gemini`, que el aislamiento oculta. El
  rechazo se produce antes de cualquier inicio, indicando su causa, en lugar de un minuto
  de espera por un código de conexión.
- **Modelos**: los de `agy models`. Los Gemini llevan el nivel de esfuerzo en su nombre
  (`gemini-3.8-flash-medium`…): un nombre sin sufijo se rechaza antes de la llamada,
  y `--reasoning_effort` no tiene efecto. Por defecto `gemini-3.8-flash-medium`,
  e `gemini-3.7-flash-low` en `--eco`; las campañas que los determinaron se
  describen en [Mediciones detalladas](#mediciones-detalladas). Claude y GPT-OSS
  tienen su propia cuota, mucho más reducida: aproximadamente un 1 % de la ventana de
  5 horas por llamada medida, frente al 0,05 % en Flash.
- **Cuota**: por grupo, una ventana de 5 horas y una semanal, de forma
  proporcional al coste en tokens. Medido en la cuenta del autor: alrededor de
  16 puntos de la ventana de 5 horas por millón de caracteres de origen en
  `gemini-3.8-flash-medium`, 14 en `gemini-3.7-flash-medium` y de 7 a 8 con
  esfuerzo bajo —por tanto, un README de 40 000 caracteres cuesta algo más de
  medio punto—. El límite semanal, por su parte, depende del nivel. El reintento sigue
  lo que agy declara como reintentable; en su defecto, una ventana agotada nunca se
  reintenta: hace fallar cada archivo hasta el restablecimiento
  que muestra `/usage`.
- **Más lento que la API**: en el artículo denso de las mediciones, una mediana de 3 min 59 s por
  idioma en `gemini-3.8-flash-medium` y 3 min 14 s en
  `gemini-3.7-flash-medium`, frente a 1 min 18 s para Gemini 3.7 Flash mediante la API.
- **Interrupción**: Ctrl-C, o un terminal cerrado, detienen agy junto con la
  comando en lugar de dejarle terminar su turno consumiendo su cuota; lo mismo ocurre
  con Codex, Grok CLI y OpenCode. Con `nohup`, la traducción continúa.
- Rechazado en CI (`CI` o `GITHUB_ACTIONS` definido): la sesión reside en un
  llavero personal. En un runner, `--use_gemini` con `GOOGLE_API_KEY`.
- Variables: `AGY_BIN` (si no, el `PATH`, luego `~/.local/bin/agy`),
  `AGY_TIMEOUT` (segundos por segmento, inicio incluido, por defecto 900).

**Términos de servicio: es su cuenta la que está comprometida.** Las
[condiciones de Antigravity](https://antigravity.google/terms) (sección 6) y su
[FAQ](https://antigravity.google/docs/faq/) prohíben acceder al servicio
mediante software de terceros utilizando la conexión de Antigravity —Claude Code,
OpenClaw y OpenCode se mencionan allí—, bajo pena de suspensión de la cuenta. aipmt
no lee ni reutiliza el token: ejecuta el binario oficial en el
[modo headless](https://antigravity.google/docs/cli/headless/) que Google
documenta para scripts y CI. Un miembro de Google calificó de «estándar»
ejecutar `agy -p` desde un script local para el trabajo propio
([foro oficial, 25 de septiembre de 2026, respuesta no contractual](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
ningún texto resuelve de forma definitiva el caso de una herramienta distribuida como esta.

**Solo documentos públicos.** Según la sección 5 de las mismas condiciones, los
intercambios —prompts, respuestas, metadatos— pueden utilizarse para mejorar los
productos y el aprendizaje automático de Google y pueden ser revisados por
personas, incluida la suscripción de pago. La exclusión se realiza a través del ajuste
`enableTelemetry`, cuyo efecto no está documentado y que aipmt no establece; sus configuraciones
de agy no se transfieren a su entorno aislado. No pase nada confidencial por aquí.

### Hacia el proveedor que elija: `--use_opencode`

[OpenCode](https://opencode.ai) es un agente de código de código abierto (MIT) que
enruta hacia los proveedores configurados en su interior: clave de API, suscripción,
pasarela OpenCode Zen (modelos gratuitos, sin cuenta) o modelo local. Dos
vías han sido medidas de principio a fin aquí: Zen y Ollama.

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
cuyos intercambios pueden utilizarse para entrenamiento, y esta elección no se toma por
usted.

Aislamiento en cada llamada:

- una configuración inline, con prioridad sobre la suya, define un agente `aipmt`
  cuyas herramientas quedan todas denegadas (`permission: { "*": "deny" }`), uso compartido de
  sesión desactivado, `--pure`, nunca `--auto`;
- directorio de trabajo desechable y vacío, `OPENCODE_DISABLE_PROJECT_CONFIG` y
  `OPENCODE_DISABLE_CLAUDE_CODE` establecidos —sin ellos, OpenCode inyecta en el
  prompt el `AGENTS.md` del directorio actual y `~/.claude/CLAUDE.md`. El
  `~/.config/opencode/AGENTS.md` global se sigue inyectando, ya que OpenCode no permite
  descartarlo—;
- contrato de salida: código de retorno 0, ningún evento `error`, ninguna llamada
  a herramientas, último paso en `stop`, texto no vacío y el agente `aipmt`
  efectivamente cargado —un `--agent` desconocido no hace fallar a OpenCode, sino que
  recurre silenciosamente al agente de programación—;
- no se transmite ninguna clave de `aipmt`, excepto `OPENCODE_API_KEY`, la clave
  del propio OpenCode. Los proveedores se configuran en OpenCode, no en
  el `.env` de `aipmt`.

A tener en cuenta:

- Los modelos gratuitos de Zen son variables, con límites no documentados, y
  sus intercambios pueden utilizarse para entrenamiento: aptos para documentación
  pública, no para contenido privado.
- Un modelo local debe ofrecer al menos 16 k tokens de contexto, ya que los segmentos
  alcanzan hasta 16 000 caracteres. Ollama suele configurar 4 096: recurra
  a un `Modelfile` con `PARAMETER num_ctx 32768`.
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

`reasoningEffort: "none"` desactiva el razonamiento que Ollama habilita por defecto en estos
modelos y que un Modelfile no puede desactivar. Medido en una frase de
seis palabras: 919 tokens de razonamiento y 68 segundos sin la opción, 9 tokens con ella.

### Hacia más de 400 modelos: `--use_openrouter`

OpenRouter es un enrutador facturado por uso, sobre un crédito único, frente a
modelos alojados por terceros —incluidos los modelos chinos abiertos que ningún
otro proveedor expone aquí—.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` es obligatorio. Un preflight, ejecutado antes de cualquier facturación, resuelve
dos particularidades del enrutamiento:

- **Un mismo modelo es servido por decenas de proveedores de alojamiento con límites
  diferentes** —en `z-ai/glm-5.3-flash`, 23 proveedores, incluido uno limitado a
  2 048 tokens de salida—. El preflight lee `/api/v1/models/{modèle}/endpoints`,
  descarta los proveedores por debajo de 8 000 tokens de salida o con estado degradado, y
  fija los demás con `allow_fallbacks: false`.
- **El razonamiento se factura a la tarifa de salida** —107 tokens frente a 2 en
  una respuesta «OK» de `z-ai/glm-5.2`—. Está desactivado por defecto; los modelos
  que lo imponen reciben el nivel de esfuerzo más bajo que aceptan, ya que el valor predeterminado del
  catálogo podría saturar la salida antes de que finalice la traducción.
  `--reasoning_effort` mantiene la prioridad.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- La ventana de contexto proviene del catálogo. Un modelo por debajo de 16 400 tokens se
  rechaza antes de cualquier llamada: 8 400 para el prompt y el segmento, 8 000 de salida
  como mínimo.
- Un slug ausente en el catálogo, un catálogo inaccesible o la ausencia
  de un proveedor que cumpla con el límite detienen el comando.
- `finish_reason=length` con una salida vacía representa un presupuesto consumido por el
  razonamiento, no un truncamiento: el mensaje lo distingue.
- `--eco` no tiene efecto.
- Variables: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (por defecto `https://openrouter.ai/api/v1`, `https://`
  requerido), `OPENROUTER_TIMEOUT` (por defecto 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (por defecto 30).

### Nota de traducción

`--add_translation_note` añade una nota, en `bottom` (por defecto), `top` (después del
front matter) o `both` (`--note_position`), en formato `legacy` (párrafo en
negrita, por defecto) o `marker` (`--note_format`). El formato `marker` es una
definición de referencia Markdown invisible,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
seguida de una cita en negrita: legible en GitHub, utilizable en el proceso de compilación mediante un
plugin de remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Mediciones detalladas

Todas las mediciones corresponden a traducciones ejecutadas realmente con `aipmt`, hacia
catorce idiomas: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Escritos** cuenta los archivos que las comprobaciones dejaron pasar; **Sin
diferencias** aquellos en los que `scripts/compare_structure.py` no detecta nada: mismo número de
secciones, subtítulos, enlaces, URL distintas, bloques de código,
código en línea, filas de tabla, bloques de cita y palabras en negrita.

«Sin diferencias» significa «nada detectado», no «idéntico»: el comparador
cuenta elementos sin leer su contenido. No señala ni un encabezado de
nivel 4 eliminado, ni el texto de un código en línea reemplazado, ni una bandera
intercambiada, ni un enlace interno generado con un paréntesis de más,
`[texte]((#ancre))`, que ya no lleva a ninguna parte —y no evalúa el
idioma—.

### Artículo de seguimiento denso, modo `--news`

Una edición del [seguimiento de IA de jls42.org](https://jls42.org/fr/news):
589 líneas, 140 enlaces, 21 secciones, 3 citas en inglés protegidas. Campaña
del 4 y 5 de septiembre de 2026.

| Modelo                                          | Acceso             | Escritas| Sin discrepancia | Mediana/idioma |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | API Google         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | suscripción Google | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | suscripción Google | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | suscripción ChatGPT| 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `claude-sonnet-5`                               | API Anthropic      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | local              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | API Mistral        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | suscripción Grok   | 1/14    | ❌ 1/14      | 23 min 11 s    |

Grok se volvió a medir el 9 de septiembre en otra edición del mismo seguimiento
(356 líneas): 9 idiomas escritos de 14, 8 sin discrepancias. Es esta cifra la que
figura en la tabla principal. Tres campañas interrumpidas no están
registradas: `qwen3.5-27b` (9 idiomas) y `kimi-k2.6` (4) por falta de crédito,
`z-ai/glm-5.3-flash` cuyos dos fallos procedían de un ajuste de razonamiento
que el proveedor corrige desde entonces. Las líneas de OpenRouter se midieron con los
ajustes por defecto del enrutador, antes de `--use_openrouter`; `z-ai/glm-5.2`,
medido de nuevo con el proveedor entregado, devuelve el mismo 14/14. Las cifras se
recalcularon el 10 de septiembre con el comparador actual: `qwen3.8-flash` y
`qwen3.7-flash` ganan cada uno un idioma respecto a la primera
publicación, los demás se mantienen sin cambios.

Las líneas de `--use_antigravity` se midieron el 26 de septiembre en el mismo
artículo, con cuatro traducciones en paralelo: `gemini-3.7-flash-medium` por la mañana,
`gemini-3.8-flash-medium` por la tarde. En inglés, cada uno eliminó por sí mismo
las tres líneas de traducción al francés bajo las citas, sin inventar
banderas, y las citas en inglés quedaron intactas: la limpieza de respaldo no
tuvo nada que hacer. En `--eco` (`gemini-3.7-flash-low`), en cuatro idiomas
únicamente (en, ja, ar, hi): 4 escritas de 4, todas sin discrepancias, 1 min 52 s de
mediana. Contraprueba el mismo día en una edición más reciente del seguimiento,
la del 25 de septiembre (438 líneas, 2 citas en inglés), traducida fuera del
blog por `gemini-3.7-flash-medium`: 14 escritas de 14, todas sin discrepancias, de 87 a
128 s por idioma.

### README de este proyecto, Markdown estándar

Revisión congelada el 9 de septiembre de 2026: 785 líneas, 285 códigos en línea, 40
cierres de bloques, 89 líneas de tabla. Cuatro traducciones en paralelo.

| Modelo                                          | Escritas| Sin discrepancia | Mediana/idioma | Qué difiere                                                              |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | nada                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | una palabra en negrita (ja)                                              |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | una palabra en negrita (ko)                                              |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | un enlace (sv), una palabra en negrita (zh)                              |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | una palabra en negrita (ar, ja)                                          |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | una palabra en negrita (hi, ja, ko)                                      |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 40 códigos en línea añadidos en árabe; negrita (hi, ja, ko)               |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | una sección perdida (ar, hi, ko); bloques de código añadidos (ja, ko, ro, zh) |

Dos campañas interrumpidas no están registradas: Grok, sesión CLI expirada
tras doce idiomas (once sin discrepancias), y `qwen3.8-flash`, HTTP 429 de su
proveedor de alojamiento tras dos. `opencode/mimo-v2.5-free` y `ollama/gpt-oss-20b-32k`
no se volvieron a medir en esta revisión; en la del 4 y 5 de septiembre,
277 líneas más corta, escribían cada uno 9 traducciones de 14, de las cuales 7
y 1 sin discrepancias.

Las líneas de `--use_antigravity` no se midieron en la revisión congelada,
sino el 26 de septiembre en la publicada con la 1.14.0: 600 líneas, 257 códigos
en línea, 30 cierres de bloques, 85 líneas de tabla. Al ser 185 líneas más
corta, no se compara término a término con las demás líneas; las dos
líneas Antigravity, en cambio, sí se comparan entre sí. En cuanto a los enlaces internos,
que el comparador no comprueba, `gemini-3.8-flash-medium` los mantuvo
intactos en los catorce idiomas, mientras que `gemini-3.7-flash-medium` los rompió en
italiano.

### Cuatro README de proyectos conocidos

FastAPI, Ollama, tldr-pages y Vue.js, tomados tal cual de GitHub —
documentos más sencillos que los dos anteriores. La campaña apuntaba a los modelos
con dificultades; Gemini sirve aquí como punto de comparación.

| Modelo                    | Alcance                    | Escritas| Sin discrepancia |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 proyectos × 14 idiomas   | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 proyectos × 14 idiomas   | 55/56   | ❌ 47/56     |
| `grok-4.6` (suscripción) | 4 proyectos × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 proyectos × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### Lo que estas mediciones no son

- **No son una clasificación exhaustiva**: solo OpenRouter ofrece más de cuatrocientos
  modelos, de los cuales se midió una quincena.
- **Son duraciones indicativas**: de tres a seis traducciones en paralelo según
  las campañas, y el rendimiento de un proveedor varía a lo largo del día.
- **Son observaciones fechadas**: los modelos cambian bajo el mismo nombre y sus
  documentos no son los nuestros.

Para repetir la medición en sus documentos, sobre una copia fija del archivo:

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
regeneran con `./regen_translations.sh --force` — Codex y `gpt-5.6-sol` con
la suscripción de ChatGPT por defecto, cuatro en paralelo. `REGEN_PROVIDER` y
`REGEN_MODEL` cambian la ruta: `antigravity` permanece en una suscripción, la
de Google, y pasa sin excepción; una API de pago (`openai`, `gemini`,
`grok`, `openrouter`) se rechaza sin `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` limita cada tarea (600 s, 1 800 s en Codex y
Antigravity). Los detalles de las herramientas están en `CLAUDE.md`.

## Proyectos que utilizan este script

- **[jls42.org](https://jls42.org)** — blog personal publicado en 15 idiomas. Su
  [seguimiento diario de IA](https://jls42.org/fr/news) es traducido cada día
  por esta herramienta y sirve como documento de referencia para las mediciones anteriores.

## Autor

Julien LE SAUX
Correo electrónico: contact@jls42.org

## Licencia

GNU GENERAL PUBLIC LICENSE Versión 3. Consulte [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Advertencia

Este programa se distribuye **sin ninguna garantía**, bajo los términos de las
secciones 15 y 16 de la GPL v3: proporcionado «tal cual», sin garantía de calidad
comercial ni de adecuación para un uso particular, y su autor no podrá ser
considerado responsable de ningún daño derivado de su uso. El texto de la
licencia prevalece sobre este resumen.

- **Revise antes de publicar.** Las protecciones cubren los bloques de código, el
  código en línea, las URL, las anclas y las citas del modo `--news` — no los
  títulos, ni las tablas, ni el front matter, ni el sentido de sus frases.
- **Sus documentos se envían al proveedor elegido**, bajo sus condiciones
  de uso y su política de datos. Algunos modelos gratuitos pueden
  reutilizar sus intercambios para entrenamiento, y las condiciones de Antigravity
  permiten a Google reutilizarlos y hacerlos revisar por personas,
  incluida la suscripción de pago; un modelo local es la única vía que no hace
  salir ningún dato de su máquina.
- **Las llamadas a la API se le facturan a usted.** Este programa no fija un límite al
  gasto: un documento extenso, una reanudación tras un fallo o un modelo que razona
  mucho costarán más.
- **Las mediciones publicadas son observaciones fechadas**, no garantías.

Los nombres de productos y empresas mencionados pertenecen a sus respectivos
titulares. Este proyecto no está afiliado a ninguno de ellos.

**Artículo traducido del fr al es con gemini-3.8-flash-medium.**

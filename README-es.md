# Traductor de Markdown con tecnología de IA

🌍 [Francés](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [Inglés](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Chino](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Alemán](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Japonés](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Coreano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Árabe](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Neerlandés](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polaco](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Portugués](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Rumano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Sueco](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Malos olores del código"></a>
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

Traductor de archivos Markdown que utiliza **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** y **Grok (xAI)** — mediante API, con la cuota de una suscripción a ChatGPT (Codex) o Grok sin facturación por uso, o mediante **OpenCode**, el agente open source, con el proveedor que elija: modelo local (Ollama), gratuito, suscripción (GitHub Copilot…) o clave.

Este script de Python traduce archivos Markdown de un idioma de origen a un idioma de destino, preservando el formato, los bloques de código y los metadatos front matter.

## Características principales

- **Multi-Provider**: 5 API (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLI mediante suscripción, sin facturación por uso — Codex (ChatGPT) y Grok — + OpenCode (open source, MIT) con cualquier proveedor configurado en OpenCode, incluido un modelo local
- **Modelos de 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Modo económico**: Opción `--eco` para utilizar modelos más rápidos y económicos
- **Archivo único**: Opción `--file` para traducir un solo archivo
- **Segmentación inteligente**: Gestión de textos largos con límites de tokens por modelo
- **Preservación del código**: Se preservan los bloques de código Y el código inline (`` `...` ``)
- **Nombre del archivo**: Opción `--keep_filename` para conservar el nombre original
- **Modo News**: Opción `--news` para proteger las citas en inglés y gestionar las banderas en los artículos de actualidad
- **Configuración .env**: Compatibilidad con el archivo `.env` para las claves API
- **Nota de traducción**: Adición opcional de una nota al final del documento

## Instalación

### Para utilizar la herramienta

```bash
pip install ai-powered-markdown-translator
```

El comando `aipmt` estará entonces disponible en todas partes. Si el directorio de scripts
de Python no está en su `PATH`, `python -m aipmt` hace exactamente lo mismo.
Python 3.10 o una versión más reciente.

Para una instalación aislada del resto de sus paquetes:

```bash
pipx install ai-powered-markdown-translator
```

### Para contribuir al proyecto

El repositorio clonado sigue siendo necesario para desarrollar: ahí se encuentran las pruebas,
las 28 traducciones y todas las herramientas de calidad.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` es un **lock completamente fijado**, un reflejo exacto del
entorno probado. Los límites publicados en `pyproject.toml` son
deliberadamente más amplios: no imponen nada a sus demás paquetes.

### Herramientas de calidad (opcionales, pero recomendadas)

El proyecto utiliza [`pre-commit`](https://pre-commit.com) para impedir que se haga commit de código con formato incorrecto, vulnerable o que contenga un secreto. Instalación:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hooks activos: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complejidad), detect-secrets (claves API), mypy (tipado progresivo), Opengrep (SAST), pip-audit (CVE de dependencias), unittest. Consulte la sección _Quality / pre-commit_ de `CLAUDE.md` para obtener más información.

## Configuración

Las claves se buscan en **tres ubicaciones**, de mayor a menor prioridad.
Cada una solo completa lo que la anterior haya dejado vacío.

|     | Dónde                                         | Para qué                                  |
| --- | --------------------------------------------- | ----------------------------------------- |
| 1   | Variables de entorno                          | CI, contenedores, excepción puntual       |
| 2   | `.env` del directorio actual (o de un directorio superior) | una clave específica de un proyecto       |
| 3   | `~/.config/aipmt/.env`                        | **se instala una vez y sirve en todas partes** |

Lo más sencillo después de un `pip install` es la tercera opción:

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
(de lo contrario, se ignora, tal como prescribe la especificación), y `%APPDATA%`
en Windows.

La segunda opción sigue siendo útil cuando un repositorio tiene su propia clave: un `.env` en su raíz
prevalece entonces sobre la configuración del usuario, sin modificarla. Y una
variable ya definida en el entorno prevalece sobre ambas:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Si no se encuentra ninguna clave, el comando no muestra ningún trace de llamada:
enumera las tres ubicaciones con su ruta exacta.

`GEMINI_API_KEY` se acepta como alternativa a `GOOGLE_API_KEY` (convención de AI
Studio). Variables opcionales: `XAI_BASE_URL` (endpoint de xAI, valor predeterminado
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (segundos por llamada a Anthropic, valor predeterminado
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (consulte la sección Grok CLI) y `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (consulte la sección OpenCode). Para
`regen_translations.sh`: `REGEN_PROVIDER` (valor predeterminado `codex`, mediante suscripción),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (excepción obligatoria para una API
de pago) y `REGEN_JOB_TIMEOUT` (límite por job, valor predeterminado de 600 s, 1 800 s en Codex).

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

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### Traducir con su suscripción a ChatGPT (`--use_codex`)

Este provider no consume ninguna clave API: controla el CLI oficial de Codex en modo
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
y, a continuación, el paquete de Python `openai-codex-cli-bin`. Este último no está incluido
deliberadamente en `requirements.txt`: ocupa ~250 MB, lo que se impondría a todos los
usuarios para un provider opcional.

**Información importante:**

- **No se utiliza ninguna clave API.** `OPENAI_API_KEY` y `CODEX_API_KEY` se
  eliminan del entorno del subproceso, lo que garantiza que una clave
  presente en `.env` nunca hará que la traducción pase a facturarse por
  uso.
- **Un segmento = un «mensaje local»** de la ventana de 5 horas del plan.
  Utilice `--eco` (modelo `gpt-5.6-luna`, 250-2 000 mensajes/5 h en Plus)
  en lugar del modelo de calidad (`gpt-5.6-sol`, 10-100 mensajes/5 h).
- **Más lento** que una llamada API: calcule ~45 s para un README completo, frente a
  unos pocos segundos directamente.
- **No permitido en CI** (si se define `CI` o `GITHUB_ACTIONS`): la autenticación mediante
  suscripción no está prevista para un runner compartido, y OpenAI desaconseja este
  workflow en repositorios públicos. Utilice una clave API en este caso.
- Variables de entorno: `CODEX_BIN` (ruta explícita del binario) y
  `CODEX_TIMEOUT` (segundos por segmento, valor predeterminado `600`).

### Traducir con su suscripción a Grok (`--use_grok_cli`)

El mismo principio que `--use_codex`, con el CLI oficial **Grok Build**: la
traducción se descuenta de la suscripción a Grok (SuperGrok / X Premium+) en lugar
de facturarse por token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Confinamiento — léalo antes de utilizarlo.** Este provider es estructuralmente **más
débil** que `--use_codex`, y es una decisión deliberada:

- Codex se ejecuta en `--sandbox read-only`, una frontera impuesta por el sistema.
- El sandbox de Grok **no puede aplicarse** en muchos equipos Linux
  recientes: AppArmor bloquea los user namespaces sin privilegios desde Ubuntu
  24.04, y la deny-list de los sockets del runtime de contenedores falla si
  `/run/podman` está en `0700`. Sin embargo, un perfil **integrado** que no puede
  aplicarse se inicia **sin confinamiento y en silencio**.
- Por tanto, el script no solicita ningún perfil de forma predeterminada y **nunca recurre
  silenciosamente a otra opción**: muestra una advertencia. El confinamiento se basa en las
  reglas `--deny` del CLI (incluida la catch-all `*`), la única capa medida
  como _fail-closed_: una regla desconocida hace que se rechace el inicio, en lugar de
  retirar la protección sin avisar.
- Para **exigir** el sandbox del SO: `GROK_TRANSLATE_SANDBOX=read-only`. El
  inicio fallará si la máquina no puede aplicarlo, que es el
  comportamiento deseado.

**Cuota**: el pool de Grok es **semanal y compartido** con Chat, Imagine y
Voice, y ningún comando permite consultarlo. Por tanto, un procesamiento por lotes puede
reducir su uso conversacional sin que nada lo indique; de ahí una
concurrencia limitada a 2 y una advertencia en `regen_translations.sh`.

Otras variables: `GROK_BIN` (ruta del binario), `GROK_TIMEOUT` (valor predeterminado de 900 s).

Para regenerar las 28 traducciones:

```bash
# Défaut : Codex sur l'abonnement ChatGPT, modèle qualité gpt-5.6-sol, 0 € à l'usage
./regen_translations.sh --force

# Le modèle éco de Codex, si le volume l'impose
REGEN_MODEL=gpt-5.6-luna ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Une API facturée (openai, gemini, grok) est REFUSÉE sans cette dérogation nommée
REGEN_PROVIDER=openai REGEN_ALLOW_PAID_API=1 ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
```

### Traducir con OpenCode, mediante el proveedor que elija (`--use_opencode`)

[OpenCode](https://opencode.ai) es un agente de código **open source (MIT)** para
terminal. No es un proveedor de modelos, sino un **router** hacia los que
haya configurado en el propio OpenCode: una clave API, una suscripción
(GitHub Copilot, ChatGPT, SuperGrok), la pasarela OpenCode Zen — que ofrece
modelos gratuitos **sin cuenta** — o un modelo **local** (Ollama, LM Studio,
llama.cpp). Este provider controla `opencode run` en modo no interactivo y limita
la llamada a un solo intercambio, sin ninguna herramienta.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` es **obligatorio**, con el formato `provider/modèle`. OpenCode no es
un proveedor y no se elige ningún valor predeterminado por usted: su propio fallback
sería un modelo gratuito cuyas interacciones podrían utilizarse para el entrenamiento.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Confinamiento — lo que hace el script en cada llamada:**

- Una configuración inline (`OPENCODE_CONFIG_CONTENT`), que prevalece sobre la
  suya, define un agente `aipmt` en el que **se rechazan todas las herramientas**
  (`permission: { "*": "deny" }`): el modelo no puede leer, escribir ni
  ejecutar comandos; según las mediciones, ni siquiera lo intenta. El uso compartido de sesiones
  está desactivado, `--pure` descarta los plugins externos, nunca `--auto`.
- La llamada se ejecuta en un **directorio temporal y vacío**, con los interruptores
  `OPENCODE_DISABLE_PROJECT_CONFIG` y `OPENCODE_DISABLE_CLAUDE_CODE`: sin
  ellos, OpenCode inyecta en cada prompt el `AGENTS.md` del directorio actual
  y su `~/.claude/CLAUDE.md`; según las mediciones, una instrucción «terminar cada respuesta
  con BANANA» incluida en un `AGENTS.md` se aplicaba a la traducción. En cambio, las
  reglas globales de `~/.config/opencode/AGENTS.md` siguen
  aplicándose: OpenCode no permite excluirlas.
- El contrato de salida exige simultáneamente: código de retorno 0, ningún evento
  `error`, ninguna llamada a herramientas, un último paso completado en `stop`, texto no
  vacío y que el agente se haya cargado realmente; un `--agent` desconocido no hace
  que OpenCode falle, sino que **recurre en silencio** al agente de programación, con las herramientas
  activas. Un `exit 0` tampoco demuestra nada en este caso.
- **No se transmite ninguna clave de aipmt** al subproceso (el mismo filtrado
  que con Codex y Grok), salvo una excepción nominal: `OPENCODE_API_KEY`,
  la clave del propio OpenCode (Zen, Go). Los proveedores se configuran en
  OpenCode (`opencode auth login`, `opencode.json`), no en el `.env` de aipmt.

**Información importante:**

- **Los modelos gratuitos de Zen son modelos «stealth» o de colaboradores**,
  cambiantes, con límites no documentados, y sus interacciones pueden utilizarse para
  el entrenamiento: son perfectos para documentación pública, pero deben evitarse con
  contenido privado. Según las mediciones: `opencode/mimo-v2.5-free` traduce este README en una
  pasada; `opencode/big-pickle` es más lento y dos solicitudes simultáneas quedaron
  sin respuesta.
- **Un modelo local debe ofrecer al menos 16 k de contexto** — los segmentos alcanzan
  hasta 16 000 caracteres — mientras que Ollama suele configurar 4 096 de forma
  predeterminada. Con Ollama: un `Modelfile` con `PARAMETER num_ctx 32768` y, a continuación,
  `ollama create`. La calidad depende del modelo: un 7B invirtió una lista y
  dañó el cierre de un bloque de código en un archivo de prueba, mientras que un modelo de
  la pasarela lo preservó todo.
- `--eco` no tiene efecto (el modelo es el de `--model`);
  `--reasoning_effort` se transmite sin cambios como `--variant` de OpenCode y solo debe
  solicitarse si el modelo lo conoce.
- OpenCode registra las sesiones en su base de datos
  (`~/.local/share/opencode/`), como cualquier sesión de OpenCode.
- Variables de entorno: `OPENCODE_BIN` (ruta explícita del binario;
  de lo contrario, el `PATH` y luego `~/.opencode/bin/opencode`) y `OPENCODE_TIMEOUT`
  (segundos por segmento, valor predeterminado `600`). `OPENCODE_CONFIG` se respeta si lo
  exporta.

**Ejemplo medido: un modelo local mediante Ollama** (RTX 3060 de 12 GB, 62 GB de RAM, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # Ollama ≥ 0.30 pour gemma4 ; conserve les modèles déjà téléchargés
ollama pull gemma4:12b                          # 7,6 Go, Apache 2.0, 140+ langues
ollama pull qwen3.5:9b                          # 6,6 Go, Apache 2.0, 201 langues

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gemma4:12b\nPARAMETER num_ctx 32768\n' > gemma4-12b-32k.Modelfile
ollama create gemma4-12b-32k -f gemma4-12b-32k.Modelfile
```

A continuación, el proveedor en `~/.config/opencode/opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": { "baseURL": "http://127.0.0.1:11434/v1" },
      "models": {
        "gemma4-12b-32k": {
          "name": "Gemma 4 12B (32k, sans réflexion)",
          "limit": { "context": 32768, "output": 8192 },
          "options": { "reasoningEffort": "none" }
        }
      }
    }
  }
}
```

`reasoningEffort: "none"` no es un detalle: Ollama activa el razonamiento de forma
predeterminada en Gemma 4 y Qwen 3.5, y un Modelfile no puede desactivarlo. Según las mediciones realizadas
a través de OpenCode: sin la opción, «El gato duerme sobre la alfombra» consume 919 tokens
de razonamiento y 68 s; con ella, 9 tokens.

```bash
aipmt --use_opencode --model ollama/gemma4-12b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

Resultados con un artículo de blog real de 589 líneas (140 enlaces, 21 secciones,
3 citas en inglés protegidas por el modo `--news`), el mismo comando y tres
modelos:

| Modelo                                   | Duración    | Estructura                                                 | Diferencias                                                                               |
| ---------------------------------------- | ----------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free` (Zen, gratuito) | 4 min 26 s  | idéntica a la fuente                                       | ninguna                                                                                   |
| `ollama/gemma4-12b-32k` (local)          | 10 min 10 s | enlaces, URL, tablas, tags, negrita y código inline idénticos | una línea de cita inventada (🇺🇸 + paráfrasis), una atribución duplicada                    |
| `ollama/qwen3.5-9b-32k` (local)          | 8 min 18 s  | enlaces, URL, tablas y tags idénticos                      | una línea de cita inventada, algunas negritas y códigos inline añadidos, un segmento procesado de nuevo |

Durante la traducción local: GPU al 98 % y 170 W, 10 GB de VRAM ocupados
(modelo y caché de 32 k tokens, sin descargar nada en la RAM), 7,5 GB de RAM para el
servidor Ollama. Un modelo de entre 9 y 12 mil millones de parámetros respeta la
estructura, pero se toma una libertad por artículo, mientras que el modelo de la pasarela
no se tomó ninguna: conviene revisarlo antes de publicarlo o reservarlo para borradores.

### Modo económico

Utiliza modelos más rápidos y económicos (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### Opciones

| Opción                   | Descripción                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Archivo Markdown único para traducir                                                                            |
| `--source_dir`           | Directorio de origen que contiene los archivos Markdown                                                             |
| `--target_dir`           | Directorio de salida para los archivos traducidos                                                               |
| `--source_lang`          | Idioma de origen (predeterminado: `fr`)                                                                                  |
| `--target_lang`          | Idioma de destino (predeterminado: `en`)                                                                                   |
| `--model`                | Modelo específico que se utilizará                                                                                  |
| `--eco`                  | Utilizar los modelos económicos                                                                              |
| `--use_mistral`          | Utilizar la API de Mistral AI                                                                                     |
| `--use_claude`           | Utilizar la API de Claude                                                                                         |
| `--use_gemini`           | Utilizar la API de Gemini                                                                                         |
| `--use_codex`            | Utilizar el CLI de Codex con la cuota de la suscripción a ChatGPT                                                    |
| `--use_grok`             | Utilizar la API de xAI (Grok) — requiere `XAI_API_KEY`                                                           |
| `--use_grok_cli`         | Utilizar el CLI de Grok con la cuota de la suscripción a Grok                                                        |
| `--use_opencode`         | Utilizar OpenCode (open source) con el proveedor configurado en OpenCode; requiere `--model provider/modèle` |
| `--force`                | Forzar la retraducción                                                                                       |
| `--keep_filename`        | Conservar el nombre de archivo original                                                                          |
| `--news`                 | Modo noticias: protege las citas en EN y gestiona las banderas por idioma                                      |
| `--add_translation_note` | Añadir una nota de traducción                                                                                |
| `--note_position`        | Posición de la nota: `top`, `bottom` (predeterminada) o `both`                                                     |
| `--note_format`          | Formato de la nota: `legacy` (predeterminado, párrafo en negrita) o `marker`                                            |
| `--include_model`        | Incluir el nombre del modelo en el archivo de salida                                                            |
| `--reasoning_effort`     | Esfuerzo de razonamiento de GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

> **Los siete flags de provider son mutuamente excluyentes.** Combinar dos
> se aceptaba anteriormente de forma silenciosa y se resolvía usando el primero comprobado: una
> traducción solicitada con la cuota de la suscripción (`--use_codex`, `--use_grok_cli`)
> podía así terminar facturándose según el uso sin ninguna advertencia.
> `argparse` ahora rechaza la combinación.

### Nota de traducción: posiciones y formatos

Con `--add_translation_note`, el translator puede colocar la nota arriba, abajo o en ambos lugares, y presentarla en formato de texto simple (retrocompatible) o en formato `marker` procesable por un plugin Markdown.

**Posición** (`--note_position`):

- `bottom` (predeterminada): nota al final del archivo, como históricamente.
- `top`: nota insertada **después del frontmatter YAML** (compatibilidad con Astro Content Collections, gray-matter, etc.).
- `both`: nota insertada arriba Y abajo (una sola llamada al LLM, contenido reutilizado en ambas ubicaciones).

**Formato** (`--note_format`):

- `legacy` (predeterminado): párrafo en negrita `**...**` — comportamiento estrictamente idéntico al de v1.8, byte-for-byte. Compatible con Hugo, GitHub, GitLab y cualquier renderer Markdown.
- `marker`: link reference definition de Markdown invisible (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) seguida de un blockquote en negrita. Legible de forma nativa en GitHub/GitLab y procesable durante el build por un plugin remark en Astro para generar un banner estilizado (véase el blog jls42.org).

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

| Provider | Calidad (predeterminada)                      | Económico (`--eco`)      |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI   | `gpt-5.6-terra`                       | `gpt-5.6-luna`            |
| Claude   | `claude-sonnet-5`                     | `claude-haiku-4-5`        |
| Mistral  | `mistral-large-latest`                | `mistral-small-latest`    |
| Gemini   | `gemini-3.7-flash`                    | `gemini-3.1-flash-lite`   |
| Codex    | `gpt-5.6-sol`                         | `gpt-5.6-luna`            |
| Grok API | `grok-4.6`                            | `grok-4.3`                |
| Grok CLI | `grok-4.6`                            | `grok-4.5`                |
| OpenCode | `--model provider/modèle` obligatorio | igual — `--eco` sin efecto |

> **Recomendación para traducciones long-form**: `--use_gemini` (predeterminado = `gemini-3.7-flash`) preserva fielmente la estructura Markdown en los scripts no latinos (PL, JA, ZH, AR, HI), incluso en modo `--news`, donde importa la fidelidad de los placeholders. Medido en este README traducido al japonés: estructura idéntica a `gemini-3.1-pro-preview` (21 listas, 18 bloques de código, 13 enlaces HTML, 13 imágenes, todas las URL preservadas) con una latencia ~6 veces menor. OpenAI sigue siendo la opción predeterminada por retrocompatibilidad.

## Proyectos que utilizan este script

- **[jls42.org](https://jls42.org)** - Blog personal multilingüe (15 idiomas)

## Autor

Julien LE SAUX
Correo electrónico: contact@jls42.org

## Licencia

GNU GENERAL PUBLIC LICENSE Versión 3. Véase [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artículo traducido del francés al español con gpt-5.6-sol.**

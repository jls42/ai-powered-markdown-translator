# Traductor de Markdown con IA

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

Traductor de archivos Markdown que utiliza **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** y **Grok (xAI)** — mediante API, con la cuota de una suscripción a ChatGPT (Codex) o Grok sin facturación por uso, o a través de **OpenCode**, el agente open source, con el proveedor que elijas: modelo local (Ollama), gratuito, suscripción (GitHub Copilot…) o clave.

Este script de Python traduce archivos Markdown de un idioma de origen a un idioma de destino, preservando el formato, los bloques de código y los metadatos front matter.

## Características principales

- **Multi-Provider**: 5 API (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLI mediante suscripción, sin facturación por uso — Codex (ChatGPT) y Grok — + OpenCode (open source, MIT) con cualquier proveedor configurado en OpenCode, incluido un modelo local
- **Modelos de 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Modo económico**: Opción `--eco` para utilizar modelos más rápidos y económicos
- **Archivo único**: Opción `--file` para traducir un solo archivo
- **Segmentación inteligente**: Gestión de textos largos con límites de tokens por modelo
- **Preservación del código**: Se preservan tanto los bloques de código COMO el código inline (`` `...` ``)
- **Nombre de archivo**: Opción `--keep_filename` para conservar el nombre original
- **Modo News**: Opción `--news` para proteger las citas en inglés y gestionar las banderas en artículos de actualidad
- **Configuración .env**: Compatibilidad con el archivo `.env` para las claves API
- **Nota de traducción**: Adición opcional de una nota al final del documento

## Instalación

### Para utilizar la herramienta

```bash
pip install ai-powered-markdown-translator
```

El comando `aipmt` estará entonces disponible en cualquier lugar. Si el directorio de scripts
de Python no está en tu `PATH`, `python -m aipmt` hace exactamente lo mismo.
Se requiere Python 3.10 o una versión posterior.

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
deliberadamente más amplios: no imponen nada a tus demás paquetes.

### Herramientas de calidad (opcionales pero recomendadas)

El proyecto utiliza [`pre-commit`](https://pre-commit.com) para impedir que se haga commit de código mal formateado, vulnerable o que contenga algún secreto. Instalación:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hooks activos: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complejidad), detect-secrets (claves API), mypy (tipado progresivo), Opengrep (SAST), pip-audit (CVE de dependencias), unittest. Consulta la sección _Quality / pre-commit_ de `CLAUDE.md` para obtener más información.

## Configuración

Las claves se buscan en **tres ubicaciones**, de mayor a menor prioridad.
Cada una solo completa lo que la anterior deja vacío.

|     | Dónde                                         | Para qué                                  |
| --- | --------------------------------------------- | ----------------------------------------- |
| 1   | Variables de entorno                          | CI, contenedores, excepción puntual       |
| 2   | `.env` del directorio actual (o de uno superior) | una clave específica de un proyecto       |
| 3   | `~/.config/aipmt/.env`                               | **se instala una vez y sirve en todas partes** |

Lo más sencillo después de un `pip install` es la tercera opción:

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

Este archivo sigue `XDG_CONFIG_HOME` cuando la variable indica una ruta absoluta
(de lo contrario, se ignora, tal como prescribe la especificación), y `%APPDATA%`
en Windows.

La segunda opción sigue siendo útil cuando un repositorio tiene su propia clave: un `.env` en su raíz
prevalece entonces sobre la configuración del usuario, sin modificarla. Y una
variable ya definida en el entorno prevalece sobre ambas:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Si no se encuentra ninguna clave, el comando no muestra ningún rastro de llamada:
enumera las tres ubicaciones con su ruta exacta.

`GEMINI_API_KEY` se acepta como alternativa a `GOOGLE_API_KEY` (convención de AI
Studio). Variables opcionales: `XAI_BASE_URL` (endpoint de xAI, valor predeterminado
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (segundos por llamada a Anthropic, valor predeterminado
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (consulta la sección Grok CLI), `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (consulta la sección OpenCode) y `OPENROUTER_BASE_URL` /
`OPENROUTER_TIMEOUT` / `OPENROUTER_PREFLIGHT_TIMEOUT` (consulta la sección
OpenRouter). Para
`regen_translations.sh`: `REGEN_PROVIDER` (valor predeterminado `codex`, mediante suscripción),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (excepción obligatoria para una API
de pago) y `REGEN_JOB_TIMEOUT` (límite por job, 600 s de forma predeterminada, 1 800 s en Codex).

## Uso

### Traducir un único archivo

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

# Avec OpenRouter (routeur vers ~430 modèles ; --model obligatoire)
aipmt --use_openrouter --model 'z-ai/glm-5.2' --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### Traducir con una suscripción a ChatGPT (`--use_codex`)

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

El binario se busca en este orden: la variable `CODEX_BIN`, el `PATH`,
y después el paquete de Python `openai-codex-cli-bin`. Este último no se incluye deliberadamente
en `requirements.txt`: pesa unos 250 MB, que de otro modo se impondrían a todos los
usuarios para un provider opcional.

**Información importante:**

- **No se utiliza ninguna clave API.** `OPENAI_API_KEY` y `CODEX_API_KEY` se
  eliminan del entorno del subproceso, lo que garantiza que una clave
  presente en `.env` nunca hará que la traducción pase a facturarse
  por uso.
- **Un segmento = un «mensaje local»** de la ventana de 5 horas del plan.
  Utiliza `--eco` (modelo `gpt-5.6-luna`, 250-2 000 mensajes/5 h en Plus)
  en lugar del modelo de calidad (`gpt-5.6-sol`, 10-100 mensajes/5 h).
- **Más lento** que una llamada API: calcula unos 45 s para un README completo, frente a
  unos pocos segundos mediante una llamada directa.
- **No permitido en CI** (si `CI` o `GITHUB_ACTIONS` están definidos): la suscripción
  se autentica mediante un archivo de sesión personal, y trasladarlo a un runner
  compartido equivale a depositar allí una identidad reutilizable por todo lo que se
  ejecute en él. Utiliza una clave API en este caso.
- Variables de entorno: `CODEX_BIN` (ruta explícita del binario) y
  `CODEX_TIMEOUT` (segundos por segmento, valor predeterminado `600`).

### Traducir con una suscripción a Grok (`--use_grok_cli`)

El mismo principio que `--use_codex`, con el CLI oficial **Grok Build**: la
traducción se descuenta de la suscripción a Grok (SuperGrok / X Premium+) en lugar
de facturarse por token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Confinamiento — leer antes de usar.** Este provider es estructuralmente **más
débil** que `--use_codex`, y esto es intencionado:

- Codex se ejecuta en `--sandbox read-only`, una frontera impuesta por el sistema.
- El sandbox de Grok **no puede aplicarse** en muchos equipos Linux
  recientes: AppArmor bloquea los user namespaces sin privilegios desde Ubuntu
  24.04, y la deny-list de sockets del runtime de contenedores falla si
  `/run/podman` está en `0700`. Sin embargo, un perfil **integrado** que no puede
  aplicarse se inicia **sin confinamiento y de forma silenciosa**.
- Por tanto, el script no solicita ningún perfil de forma predeterminada y **nunca recurre
  silenciosamente a otra opción**: muestra una advertencia. El confinamiento se basa en las
  reglas `--deny` del CLI (incluida la regla general `*`), la única capa comprobada
  como _fail-closed_: una regla desconocida hace que se rechace el inicio en lugar de
  retirar la protección sin avisar.
- Para **exigir** el sandbox del sistema operativo: `GROK_TRANSLATE_SANDBOX=read-only`. El
  inicio fallará si el equipo no puede respetarlo, que es el
  comportamiento esperado.

**Cuota**: el pool de Grok es **semanal y compartido** con Chat, Imagine y
Voice, y ningún comando permite consultarlo. Por tanto, un procesamiento por lotes puede
consumir parte de tu uso conversacional sin que nada lo indique; de ahí que
la concurrencia esté limitada a 2 y se muestre una advertencia en `regen_translations.sh`.

Otras variables: `GROK_BIN` (ruta del binario), `GROK_TIMEOUT` (valor predeterminado 900 s).

Para regenerar las 28 traducciones:

```bash
# Défaut : Codex sur l'abonnement ChatGPT, modèle qualité gpt-5.6-sol, 0 € à l'usage
./regen_translations.sh --force

# Le modèle éco de Codex, si le volume l'impose
REGEN_MODEL=gpt-5.6-luna ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Une API facturée (openai, gemini, grok, openrouter) est REFUSÉE sans cette dérogation nommée
REGEN_PROVIDER=openai REGEN_ALLOW_PAID_API=1 ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force

# Via OpenRouter : API facturée, donc dérogation ET modèle obligatoires
REGEN_PROVIDER=openrouter REGEN_ALLOW_PAID_API=1 REGEN_MODEL=z-ai/glm-5.2 ./regen_translations.sh --force
```
### Traducir con OpenCode, hacia el proveedor de su elección (`--use_opencode`)

[OpenCode](https://opencode.ai) es un agente de código **open source (MIT)** para
terminal. No es un proveedor de modelos, sino un **router** hacia los que
haya configurado en el propio OpenCode: una clave API, una suscripción,
la pasarela OpenCode Zen —que ofrece modelos gratuitos **sin cuenta**— o
un modelo **local**. Este provider controla `opencode run` en modo no interactivo y
limita la llamada a un único intercambio, sin ninguna herramienta.

Aquí se han medido de extremo a extremo dos de estas vías: la **pasarela Zen** y
**Ollama** en local. Las demás que anuncia OpenCode (GitHub Copilot, LM Studio,
llama.cpp) deberían funcionar por diseño, ya que el provider solo se comunica
con OpenCode, pero no se han probado y este README únicamente describe lo
que se ha verificado.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` es **obligatorio**, con el formato `provider/modèle`. OpenCode no es
un proveedor y no se elige ningún valor predeterminado en su lugar: su propio fallback
sería un modelo gratuito cuyas interacciones pueden utilizarse para el entrenamiento.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Confinamiento: lo que hace el script en cada llamada:**

- Una configuración inline (`OPENCODE_CONFIG_CONTENT`), con prioridad sobre la
  suya, define un agente `aipmt` que tiene **todas las herramientas denegadas**
  (`permission: { "*": "deny" }`): el modelo no puede leer, escribir ni
  ejecutar comandos; según las mediciones, ni siquiera lo intenta. Se desactiva el uso compartido de la sesión,
  `--pure` descarta los plugins externos, nunca `--auto`.
- La llamada se ejecuta en un **directorio desechable y vacío**, con los modificadores
  `OPENCODE_DISABLE_PROJECT_CONFIG` y `OPENCODE_DISABLE_CLAUDE_CODE`: sin
  ellos, OpenCode inyecta en cada prompt el `AGENTS.md` del directorio actual
  y su `~/.claude/CLAUDE.md`; según las mediciones, una instrucción «terminar cada respuesta
  con BANANA» incluida en un `AGENTS.md` se aplicaba a la traducción. Sin embargo, las
  reglas globales de `~/.config/opencode/AGENTS.md` siguen
  aplicándose: OpenCode no permite omitirlas.
- El contrato de salida exige simultáneamente: código de retorno 0, ningún evento
  `error`, ninguna llamada a herramientas, un último paso finalizado en `stop`, un texto no
  vacío y que el agente se haya cargado realmente; un `--agent` desconocido no hace
  que OpenCode falle, sino que **recurre silenciosamente** al agente de codificación, con las herramientas
  activas. Un `exit 0` tampoco demuestra nada aquí.
- **No se transmite ninguna clave de aipmt** al subproceso (el mismo filtrado
  que con Codex y Grok), salvo una excepción específica: `OPENCODE_API_KEY`,
  la clave del propio OpenCode (Zen, Go). Los proveedores se configuran en
  OpenCode (`opencode auth login`, `opencode.json`), no en el `.env` de aipmt.

**Información importante:**

- **Los modelos gratuitos de Zen son modelos «stealth» o de colaboradores**,
  cambiantes, con límites no documentados, y sus interacciones pueden utilizarse para
  el entrenamiento: perfectos para documentación pública, pero deben evitarse para
  contenido privado. Según las mediciones, `opencode/mimo-v2.5-free` traduce este README en una
  pasada; `opencode/big-pickle` es más lento y dos solicitudes simultáneas se
  quedaron sin respuesta.
- **Un modelo local debe ofrecer al menos 16 k de contexto** —los segmentos alcanzan
  hasta 16 000 caracteres—, mientras que Ollama suele configurar 4 096 de manera
  predeterminada. Con Ollama: un `Modelfile` con `PARAMETER num_ctx 32768` y después
  `ollama create`. La calidad depende del modelo: un 7B invirtió una lista y
  dañó el cierre de un bloque de código en un archivo de prueba, mientras que un modelo de
  la pasarela lo conservó todo.
- `--eco` no tiene efecto (el modelo es el de `--model`);
  `--reasoning_effort` se transmite tal cual como `--variant` de OpenCode y solo debe
  solicitarse si el modelo lo admite.
- OpenCode registra las sesiones en su base de datos
  (`~/.local/share/opencode/`), como cualquier sesión de OpenCode.
- Variables de entorno: `OPENCODE_BIN` (ruta explícita del binario;
  de lo contrario, el `PATH` y después `~/.opencode/bin/opencode`) y `OPENCODE_TIMEOUT`
  (segundos por segmento, valor predeterminado `600`). `OPENCODE_CONFIG` se respeta si se
  exporta.

**Ejemplo medido: un modelo local mediante Ollama** (RTX 3060 12 GB, 62 GB de RAM, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # conserve les modèles déjà téléchargés
ollama pull gpt-oss:20b                         # 13 Go, Apache 2.0 — le seul modèle local retenu ici

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

Después, el proveedor en `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` no es un detalle: Ollama activa el razonamiento de manera
predeterminada en estos modelos y un Modelfile no puede desactivarlo. Según las mediciones
a través de OpenCode, sin la opción, «El gato duerme sobre la alfombra» consume 919 tokens
de razonamiento y 68 s; con ella, 9 tokens.

```bash
aipmt --use_opencode --model ollama/gpt-oss-20b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

Resultados sobre un artículo de blog real de 589 líneas (140 enlaces, 21 secciones,
3 citas en inglés protegidas por el modo `--news`), con el mismo comando y tres
modelos:

| Modelo                                   | Duración       | Estructura                                                  | Diferencias                                                                                    |
| ---------------------------------------- | ----------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free` (Zen, gratuito) | 4 min 26 s  | idéntica a la fuente                                      | ninguna                                                                                     |
| `ollama/gemma4-12b-32k` (local)          | 10 min 10 s | enlaces, URL, tablas, tags, negrita y código inline idénticos | una línea de cita inventada (🇺🇸 + paráfrasis), una atribución duplicada               |
| `ollama/qwen3.5-9b-32k` (local)          | 8 min 18 s  | enlaces, URL, tablas y tags idénticos                    | una línea de cita inventada, algunos fragmentos en negrita y códigos inline añadidos, un segmento reprocesado |

Desde entonces, estos dos modelos locales han sido **descartados**: una licencia creativa por artículo
basta para descalificar un modelo destinado a traducciones publicadas. Otros cinco fueron
descartados por las mismas razones o por exceder el tiempo límite (`gemma4:26b-a4b`,
`qwen3.6:35b-a3b`, `ministral-3:14b`, `mistral-small3.2`, `hy-mt2:7b`). Solo se
conservó `gpt-oss:20b`, y hasta este deja pasajes en francés en
un artículo denso; véase la tabla de modelos recomendados.

Durante la traducción local: GPU al 98 % y 170 W, 10 GB de VRAM ocupados
(modelo y caché de 32 k tokens, sin descargar nada en la RAM), 7,5 GB de RAM para el
servidor Ollama. Un modelo de entre 9 000 y 12 000 millones de parámetros respeta la
estructura, pero se toma una licencia creativa por artículo, mientras que el modelo de la pasarela
no se tomó ninguna: debe revisarse antes de publicar o reservarse para borradores.

### Traducir mediante OpenRouter (`--use_openrouter`)

OpenRouter es un **router** situado delante de más de 400 modelos alojados por terceros,
facturado por uso mediante un crédito único. Proporciona acceso con una sola clave a modelos
que ninguno de los demás providers ofrece, en particular los modelos chinos abiertos.

```bash
# --model est OBLIGATOIRE : aucun défaut n'est choisi à votre place
aipmt --use_openrouter --model 'z-ai/glm-5.2' --file README.md \
  --target_dir . --source_lang fr --target_lang en
```

Dos particularidades del enrutamiento determinaron la implementación, y ambas se
pueden medir:

- **Un mismo modelo es ofrecido por decenas de proveedores de alojamiento con límites
  diferentes.** Para `z-ai/glm-5.3-flash`, hay 23 proveedores, uno de ellos limitado a
  2 048 tokens de salida: sin precauciones, una de cada 23 traducciones largas acababa
  truncada, de manera aleatoria según el enrutamiento y sin la menor señal. Un preflight consulta
  `/api/v1/models/{modèle}/endpoints`, descarta los proveedores con menos de 8 000 tokens
  de salida o con un estado degradado y después fija los demás mediante
  `allow_fallbacks: false`; sin esto, el router volvería a dirigir la solicitud hacia un proveedor
  descartado.
- **El razonamiento se factura con la tarifa de salida.** Misma solicitud en
  `z-ai/glm-5.2`, respuesta «OK»: 107 tokens de completado con el valor predeterminado del modelo,
  2 con el razonamiento desactivado. Por tanto, se desactiva de manera predeterminada en los modelos
  que lo permiten. Los que lo imponen —`reasoning.mandatory`, 288 de los 431
  modelos del catálogo— reciben el **menor esfuerzo que declaran
  aceptar**, no su configuración predeterminada: la de `z-ai/glm-5.3-flash` es
  `max` y agotaba los 32 768 tokens de salida antes de finalizar la
  traducción. Aumentar el límite no habría cambiado nada, pues el esfuerzo asigna un
  porcentaje de este. `--reasoning_effort` sigue teniendo prioridad, y `none` en un modelo
  que impone el razonamiento se notifica en lugar de eludirse.

El preflight es **fail-closed** y muestra lo que ha seleccionado:

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

Un slug ausente del catálogo, un catálogo inaccesible o la inexistencia de un proveedor
que cumpla el límite detienen el comando antes de cualquier facturación.

Otros puntos:

- La ventana de contexto procede del catálogo, no de una constante: la
  segmentación se adapta realmente a ella, incluso para los modelos de 4 095 tokens.
- `--eco` no tiene efecto (el modelo es el de `--model`).
- `finish_reason=length` con una salida vacía no es un truncamiento, sino un
  presupuesto consumido por el razonamiento; el mensaje lo indica porque ambos
  casos requieren acciones opuestas.
- Variables de entorno: `OPENROUTER_API_KEY` (clave, en
  <https://openrouter.ai/keys>), `OPENROUTER_BASE_URL` (valor predeterminado
  `https://openrouter.ai/api/v1`, se exige `https://`), `OPENROUTER_TIMEOUT`
  (segundos por llamada, valor predeterminado `900`) y `OPENROUTER_PREFLIGHT_TIMEOUT`
  (valor predeterminado `30`).

### Modo económico

Utiliza modelos más rápidos y menos costosos (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opciones

| Opción                   | Descripción                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Archivo Markdown único que se traducirá                                                                            |
| `--source_dir`           | Directorio de origen que contiene los archivos Markdown                                                             |
| `--target_dir`           | Directorio de salida para los archivos traducidos                                                               |
| `--source_lang`          | Idioma de origen (valor predeterminado: `fr`)                                                                                  |
| `--target_lang`          | Idioma de destino (valor predeterminado: `en`)                                                                                   |
| `--model`                | Modelo específico que se utilizará                                                                                  |
| `--eco`                  | Utilizar los modelos económicos                                                                              |
| `--use_mistral`          | Utilizar la API de Mistral AI                                                                                     |
| `--use_claude`           | Utilizar la API de Claude                                                                                         |
| `--use_gemini`           | Utilizar la API de Gemini                                                                                         |
| `--use_codex`            | Utilizar el CLI Codex con la cuota de la suscripción a ChatGPT                                                    |
| `--use_grok`             | Utilizar la API de xAI (Grok): requiere `XAI_API_KEY`                                                           |
| `--use_openrouter`       | Utilizar OpenRouter: requiere `OPENROUTER_API_KEY` y `--model fournisseur/modèle`                          |
| `--use_grok_cli`         | Utilizar el CLI Grok con la cuota de la suscripción a Grok                                                        |
| `--use_opencode`         | Utilizar OpenCode (open source) hacia el proveedor configurado en OpenCode; exige `--model provider/modèle` |
| `--force`                | Forzar la retraducción                                                                                       |
| `--keep_filename`        | Conservar el nombre de archivo original                                                                          |
| `--news`                 | Modo noticias: protege las citas EN y gestiona las banderas por idioma                                      |
| `--add_translation_note` | Añadir una nota de traducción                                                                                |
| `--note_position`        | Posición de la nota: `top`, `bottom` (valor predeterminado) o `both`                                                     |
| `--note_format`          | Formato de la nota: `legacy` (valor predeterminado, párrafo en negrita) o `marker`                                            |
| `--include_model`        | Incluir el nombre del modelo en el archivo de salida                                                            |
| `--reasoning_effort`     | Esfuerzo de razonamiento de GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

> **Los siete flags de provider son mutuamente excluyentes.** Antes, combinar dos
> se aceptaba silenciosamente y se resolvía usando el primero que se comprobara: una
> traducción solicitada con la cuota de una suscripción (`--use_codex`, `--use_grok_cli`)
> podía así acabar facturándose por uso sin ninguna advertencia.
> Ahora, `argparse` rechaza la combinación.

### Nota de traducción: posiciones y formatos

Con `--add_translation_note`, el translator puede colocar la nota arriba, abajo o en ambos lugares, y presentarla en formato de texto simple (retrocompatible) o en formato `marker` que pueda procesar un plugin de Markdown.

**Posición** (`--note_position`):

- `bottom` (valor predeterminado): nota al final del archivo, como históricamente.
- `top`: nota insertada **después del frontmatter YAML** (seguro para Astro Content Collections, gray-matter, etc.).
- `both`: nota insertada arriba Y abajo (una sola llamada LLM, con el contenido reutilizado en ambas ubicaciones).

**Formato** (`--note_format`):

- `legacy` (valor predeterminado): párrafo en negrita `**...**`; comportamiento estrictamente idéntico al de v1.8, byte-for-byte. Compatible con Hugo, GitHub, GitLab y cualquier renderer Markdown.
- `marker`: definición de referencia de enlace Markdown invisible (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), seguida de un blockquote en negrita. Legible de forma nativa en GitHub/GitLab y procesable durante el build mediante un plugin remark del lado de Astro para generar un banner estilizado (véase el blog jls42.org).

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

| Provider   | Calidad (valor predeterminado)                         | Económico (`--eco`)      |
| ---------- | ---------------------------------------- | ------------------------- |
| OpenAI     | `gpt-5.6-terra`                          | `gpt-5.6-luna`            |
| Claude     | `claude-sonnet-5`                        | `claude-haiku-4-5`        |
| Mistral    | `mistral-large-latest`                   | `mistral-small-latest`    |
| Gemini     | `gemini-3.7-flash`                       | `gemini-3.1-flash-lite`   |
| Codex      | `gpt-5.6-sol`                            | `gpt-5.6-luna`            |
| Grok API   | `grok-4.6`                               | `grok-4.3`                |
| Grok CLI   | `grok-4.6`                               | `grok-4.5`                |
| OpenCode   | `--model provider/modèle` obligatorio    | igual: `--eco` no tiene efecto |
| OpenRouter | `--model fournisseur/modèle` obligatorio | igual: `--eco` no tiene efecto |
## Qué modelos están a la altura

Un modelo que traduce bien un párrafo no necesariamente preserva la estructura
de un documento entero. Estas mediciones proceden de **traducciones ejecutadas
realmente**, con el comando que encontraría más arriba, sobre tres conjuntos de
documentos y catorce idiomas de destino: en, es, de, it, pt, nl, pl, sv, ro, ja,
ko, zh, ar, hi.

Dos columnas, y no dicen lo mismo. **Escritas** cuenta las traducciones que se
completan: las protecciones contra fallos silenciosos del script dejan pasar el
archivo. **Sin diferencias** cuenta aquellas cuya estructura es idéntica a la
fuente: mismas secciones, mismos enlaces, mismas URL, mismos bloques y códigos
en línea, mismas tablas, mismas citas, mismas banderas.

### Artículo de blog denso, modo `--news`

589 líneas, 140 enlaces, 21 secciones, 3 citas en inglés protegidas. Es el
documento más exigente de los tres: el modo `--news` añade restricciones
de banderas y citas a las de la estructura Markdown.

| Modelo                            | Acceso               | Escritas | Sin diferencias | Mediana/idioma |
| --------------------------------- | -------------------- | -------- | --------------- | -------------- |
| `gemini-3.7-flash`                | API de Google        | 14/14    | **14/14**       | 1 min 18 s     |
| `gpt-5.6-sol` (`--use_codex`)     | suscripción ChatGPT | 14/14    | **14/14**       | 11 min 28 s    |
| `z-ai/glm-5.2`                    | OpenRouter          | 14/14    | **14/14**       | 5 min 37 s     |
| `qwen/qwen3.8-flash`              | OpenRouter          | 14/14    | 13/14           | 26 min 23 s    |
| `z-ai/glm-5.3-flash`              | OpenRouter          | 12/14    | 12/14           | 15 min 49 s    |
| `qwen/qwen3.5-27b`                | OpenRouter          | 7/9      | 7/9             | 20 min 33 s    |
| `claude-sonnet-5`                 | API de Anthropic    | 14/14    | 11/14           | 6 min 31 s     |
| `opencode/mimo-v2.5-free`         | OpenCode Zen        | 13/14    | 11/14           | 9 min 27 s     |
| `qwen/qwen3.7-flash`              | OpenRouter          | 13/14    | 7/14            | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`          | local               | 10/14    | 7/14            | 12 min 39 s    |
| `mistral-large-latest`            | API de Mistral     | 11/14    | 5/14            | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter          | 4/14     | 3/14            | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)     | suscripción Grok    | 1/14     | 1/14            | 23 min 11 s    |
| `moonshotai/kimi-k2.6`            | OpenRouter          | 1/4      | 1/4             | 23 min 00 s    |

Dos lotes fueron **interrumpidos por falta de crédito** y su denominador lo
refleja: `qwen3.5-27b` se detuvo en nueve idiomas, `kimi-k2.6` en cuatro;
este último, después de superar el límite de tiempo de cuarenta minutos y dos
rechazos, a cerca de 0,33 $ por idioma.

Una salvedad metodológica sobre las filas de OpenRouter: se midieron con los
ajustes **predeterminados del router**, antes de que existiera `--use_openrouter`.
Desde entonces, `z-ai/glm-5.2` se ha vuelto a medir con el provider incluido,
con el razonamiento desactivado, y arroja exactamente el mismo 14/14.
`z-ai/glm-5.3-flash` falló dos veces por agotar el presupuesto de salida con la
configuración predeterminada del router; ahora el provider solicita a estos
modelos el menor esfuerzo que aceptan, y la prueba de control con los idiomas
problemáticos se supera.

### README de este proyecto, Markdown estándar

508 líneas, 219 códigos en línea, 40 cierres de bloques, 45 líneas de tabla. No
hay modo `--news` aquí: la dificultad proviene de la densidad de código.

| Modelo                        | Escritas | Sin diferencias | Mediana/idioma |
| ----------------------------- | -------- | --------------- | -------------- |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14    | 11/14           | 1 min 22 s     |
| `gemini-3.7-flash`            | 14/14    | 13/14           | 21 s           |
| `gpt-5.6-sol` (`--use_codex`) | 14/14    | 12/14           | 2 min 04 s     |
| `opencode/mimo-v2.5-free`     | 9/14     | 7/14            | 3 min 25 s     |
| `ollama/gpt-oss-20b-32k`      | 9/14     | 1/14            | 3 min 38 s     |

### Cuatro README de proyectos conocidos

FastAPI, Ollama, tldr-pages y Vue.js, tomados tal cual de GitHub. Estos
documentos son **más fáciles** que los dos anteriores, y la tabla lo demuestra.

| Modelo                    | Alcance                    | Escritas | Sin diferencias |
| ------------------------- | -------------------------- | -------- | --------------- |
| `opencode/mimo-v2.5-free` | 4 proyectos × 14 idiomas     | 55/56    | 47/56           |
| `grok-4.6` (suscripción)   | 4 proyectos × ar, hi, ja, zh | 16/16    | 14/16           |
| `ollama/gpt-oss-20b-32k`  | 4 proyectos × ar, hi, ja, zh | 15/16    | 9/16            |

### Conclusiones

- **Tres modelos nunca han perdido información** en los dos documentos densos:
  `gemini-3.7-flash`, `gpt-5.6-sol` mediante la suscripción ChatGPT y
  `z-ai/glm-5.2` mediante OpenRouter. Sus únicas diferencias en modo estándar
  son un par de `**` no reproducido en uno o dos idiomas, nunca una
  URL, un bloque de código o una cita.
- **El factor diferenciador es la densidad del documento, no el modo
  `--news`.** Grok mediante suscripción falla 13 veces de 14 en el
  artículo de blog y procesa correctamente 14 README públicos de 16: la causa
  del fallo es una pérdida del hilo en un segmento largo, verificada mediante
  una prueba de control; el pasaje aislado se traduce correctamente.
- **Las escrituras no latinas no constituyen la división esperada.**
  `gpt-oss` deja pasajes en francés en árabe, japonés, polaco **y rumano**;
  Mistral y MiMo solo pierden códigos en línea con las escrituras no latinas.
- **Desactivar el razonamiento no reduce la calidad.** `z-ai/glm-5.2` procesa
  catorce idiomas sin una sola diferencia en ambas condiciones —razonamiento
  activado de forma predeterminada por el router y luego desactivado mediante
  `--use_openrouter`— con dieciocho veces menos tokens de salida facturados. Esta
  es la medición que justifica el ajuste predeterminado del provider.
- **Un modelo lento no es un modelo seguro.** `deepseek-v4-flash-0731` tarda 37 minutos
  por idioma para 4 traducciones de 14, `qwen3.8-flash` tarda 26 minutos para un
  resultado casi perfecto y Gemini, 1 minuto y 18 segundos para un resultado
  impecable.

### Lo que esta tabla no es

- **No es una clasificación exhaustiva.** Solo OpenRouter ofrece más de
  cuatrocientos modelos; aquí se han medido unos quince. La ausencia de un
  modelo no dice nada sobre su calidad, solo que no se ha probado.
- **Estas mediciones tienen fecha**: 4 y 5 de septiembre de 2026. Los modelos
  cambian bajo el mismo nombre, los proveedores ajustan cuantificaciones y
  límites, y cada semana aparecen modelos nuevos.
- **Las duraciones no establecen ninguna clasificación.** El paralelismo osciló
  entre 3 y 6 traducciones simultáneas según las campañas, y el rendimiento de
  un proveedor varía a lo largo del día. Ofrecen un orden de magnitud, no una
  comparación.
- **Un resultado depende tanto del documento como del modelo.** El mismo modelo
  procesa correctamente catorce idiomas en un artículo y nueve en este README.
  Sus archivos no son los nuestros.
- **El enfoque adecuado sigue siendo medir en su propio entorno**: traduzca uno
  de sus documentos a sus idiomas de destino y compare después la estructura:
  número de secciones, enlaces, URL distintas, bloques de código, códigos en
  línea y líneas de tabla. Eso es exactamente lo que hace el protocolo anterior
  y cabe en un bucle sobre `aipmt`.

## Proyectos que utilizan este script

- **[jls42.org](https://jls42.org)** - Blog personal multilingüe (15 idiomas)

## Autor

Julien LE SAUX
Correo electrónico: contact@jls42.org

## Licencia

GNU GENERAL PUBLIC LICENSE Version 3. Consulte [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artículo traducido del fr al es con gpt-5.6-sol.**

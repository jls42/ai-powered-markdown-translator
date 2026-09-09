# Traducteur de Markdown AI-Powered

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Qualité du code</h4>

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

Traducteur de fichiers Markdown utilisant **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** et **Grok (xAI)** — par API, sur le quota d'un abonnement ChatGPT (Codex) ou Grok sans facturation à l'usage, ou via **OpenCode**, l'agent open source, vers le fournisseur de votre choix : modèle local (Ollama), gratuit, abonnement (GitHub Copilot…) ou clé.

Ce script Python traduit des fichiers Markdown d'une langue source vers une langue cible tout en préservant le formatage, les blocs de code et les métadonnées front matter.

## Caractéristiques Principales

- **Multi-Provider**: 5 API (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLI sur abonnement, sans facturation à l'usage — Codex (ChatGPT) et Grok — + OpenCode (open source, MIT) vers n'importe quel fournisseur configuré dans OpenCode, y compris un modèle local
- **Modèles 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Mode Économique**: Option `--eco` pour utiliser des modèles plus rapides et moins coûteux
- **Fichier Unique**: Option `--file` pour traduire un seul fichier
- **Segmentation Intelligente**: Gestion des textes longs avec limites de tokens par modèle
- **Préservation du Code**: Les blocs de code ET le code inline (`` `...` ``) sont préservés
- **Nom de Fichier**: Option `--keep_filename` pour conserver le nom original
- **Mode News**: Option `--news` pour protéger les citations anglaises et gérer les drapeaux dans les articles d'actualité
- **Configuration .env**: Support du fichier `.env` pour les clés API
- **Note de Traduction**: Ajout optionnel d'une note en fin de document

## Installation

### Pour utiliser l'outil

```bash
pip install ai-powered-markdown-translator
```

La commande `aipmt` est alors disponible partout. Si le répertoire des scripts
de Python n'est pas dans votre `PATH`, `python -m aipmt` fait exactement la même
chose. Python 3.10 ou plus récent.

Pour une installation isolée du reste de vos paquets :

```bash
pipx install ai-powered-markdown-translator
```

### Pour contribuer au projet

Le dépôt cloné reste nécessaire pour développer : c'est là que vivent les tests,
les 28 traductions et tout l'outillage qualité.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` est un **lock entièrement épinglé**, reflet exact de
l'environnement testé. Les bornes publiées dans `pyproject.toml` sont
volontairement plus larges : elles n'imposent rien à vos autres paquets.

### Outillage qualité (optionnel mais recommandé)

Le projet utilise [`pre-commit`](https://pre-commit.com) pour empêcher de committer du code mal formaté, vulnérable ou contenant un secret. Installation :

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hooks actifs : ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexité), detect-secrets (clés API), mypy (typage progressif), Opengrep (SAST), pip-audit (CVE deps), unittest. Voir `CLAUDE.md` section _Quality / pre-commit_ pour les détails.

## Configuration

Les clés sont cherchées à **trois endroits**, du plus prioritaire au moindre.
Chacun ne fait que combler ce que le précédent laisse vide.

|     | Où                                            | Pour quoi                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variables d'environnement                     | CI, conteneurs, dérogation ponctuelle |
| 2   | `.env` du répertoire courant (ou d'un parent) | une clé propre à un projet            |
| 3   | `~/.config/aipmt/.env`                        | **installé une fois, vaut partout**   |

Le plus simple après un `pip install` est le troisième :

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

Ce fichier suit `XDG_CONFIG_HOME` quand la variable désigne un chemin absolu
(sinon elle est ignorée, comme le prescrit la spécification), et `%APPDATA%`
sous Windows.

Le second reste utile quand un dépôt a sa propre clé : un `.env` à sa racine
l'emporte alors sur la configuration utilisateur, sans la modifier. Et une
variable déjà définie dans l'environnement l'emporte sur les deux :

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Si aucune clé n'est trouvée, la commande n'affiche pas de trace d'appel : elle
énumère les trois emplacements avec leur chemin exact.

`GEMINI_API_KEY` est accepté comme alternative à `GOOGLE_API_KEY` (convention AI
Studio). Variables optionnelles : `XAI_BASE_URL` (endpoint xAI, défaut
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (secondes par appel Anthropic, défaut
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (voir la section Grok CLI), `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (voir la section OpenCode) et `OPENROUTER_BASE_URL` /
`OPENROUTER_TIMEOUT` / `OPENROUTER_PREFLIGHT_TIMEOUT` (voir la section
OpenRouter). Côté
`regen_translations.sh` : `REGEN_PROVIDER` (défaut `codex`, sur abonnement),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (dérogation obligatoire pour une API
facturée) et `REGEN_JOB_TIMEOUT` (plafond par job, défaut 600 s, 1 800 s sur Codex).

## Utilisation

### Traduire un fichier unique

```bash
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Traduire un répertoire

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

### Traduire sur son abonnement ChatGPT (`--use_codex`)

Ce provider ne consomme aucune clé API : il pilote le CLI Codex officiel en mode
non-interactif, donc la traduction est décomptée du quota de l'abonnement
ChatGPT (Plus, Pro, Business…) déjà payé. C'est la seule voie documentée par
OpenAI pour cet usage — les tokens de `~/.codex/auth.json` n'authentifient pas
les appels à l'API Platform, et ne sont d'ailleurs jamais lus par ce script.

**Prérequis :**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Le binaire est cherché dans cet ordre : la variable `CODEX_BIN`, le `PATH`,
puis le package Python `openai-codex-cli-bin`. Ce dernier n'est volontairement
pas dans `requirements.txt` : il pèse ~250 Mo, ce qui serait imposé à tous les
utilisateurs pour un provider optionnel.

**À savoir :**

- **Aucune clé API n'est utilisée.** `OPENAI_API_KEY` et `CODEX_API_KEY` sont
  retirées de l'environnement du sous-processus, ce qui garantit qu'une clé
  présente dans `.env` ne fera jamais basculer la traduction en facturation à
  l'usage.
- **Un segment = un « message local »** de la fenêtre de 5 heures du plan.
  Utiliser `--eco` (modèle `gpt-5.6-luna`, 250-2 000 messages/5 h sur Plus)
  plutôt que le modèle qualité (`gpt-5.6-sol`, 10-100 messages/5 h).
- **Plus lent** qu'un appel API : compter ~45 s pour un README complet, contre
  quelques secondes en direct.
- **Refusé en CI** (`CI` ou `GITHUB_ACTIONS` défini) : l'abonnement
  s'authentifie par un fichier de session personnel, et le porter sur un runner
  partagé revient à y déposer une identité réutilisable par tout ce qui s'y
  exécute. Utiliser une clé API sur ce chemin.
- Variables d'environnement : `CODEX_BIN` (chemin explicite du binaire) et
  `CODEX_TIMEOUT` (secondes par segment, défaut `600`).

### Traduire sur son abonnement Grok (`--use_grok_cli`)

Même principe que `--use_codex`, avec le CLI officiel **Grok Build** : la
traduction est décomptée de l'abonnement Grok (SuperGrok / X Premium+) au lieu
d'être facturée au token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Confinement — à lire avant usage.** Ce provider est structurellement **plus
faible** que `--use_codex`, et c'est assumé :

- Codex tourne en `--sandbox read-only`, une frontière imposée par le système.
- Le sandbox de Grok **ne peut pas s'appliquer** sur beaucoup de postes Linux
  récents : AppArmor bloque les user namespaces non privilégiés depuis Ubuntu
  24.04, et la deny-list des sockets de runtime conteneur échoue si
  `/run/podman` est en `0700`. Or un profil **intégré** qui ne peut pas
  s'appliquer démarre **non confiné, en silence**.
- Le script ne demande donc aucun profil par défaut, et **ne retombe jamais
  silencieusement** : il affiche un avertissement. Le confinement repose sur les
  règles `--deny` du CLI (dont le catch-all `*`), la seule couche mesurée
  _fail-closed_ — une règle inconnue fait refuser le démarrage plutôt que de
  retirer la protection sans le dire.
- Pour **exiger** le sandbox OS : `GROK_TRANSLATE_SANDBOX=read-only`. Le
  démarrage échouera si la machine ne peut pas l'honorer, ce qui est le
  comportement voulu.

**Quota** : le pool Grok est **hebdomadaire et partagé** avec Chat, Imagine et
Voice, et aucune commande ne permet de le lire. Un traitement par lot peut donc
entamer ton usage conversationnel sans que rien ne le signale — d'où une
concurrence limitée à 2 et un avertissement dans `regen_translations.sh`.

Autres variables : `GROK_BIN` (chemin du binaire), `GROK_TIMEOUT` (défaut 900 s).

Pour la régénération des 28 traductions :

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

### Traduire avec OpenCode, vers le fournisseur de son choix (`--use_opencode`)

[OpenCode](https://opencode.ai) est un agent de code **open source (MIT)** en
terminal. Il n'est pas un fournisseur de modèles mais un **routeur** vers ceux
que vous avez configurés dans OpenCode lui-même : une clé API, un abonnement,
la passerelle OpenCode Zen — qui sert des modèles gratuits **sans compte** — ou
un modèle **local**. Ce provider pilote `opencode run` en mode non-interactif et
confine l'appel à un seul aller-retour, sans aucun outil.

Deux de ces voies ont été mesurées de bout en bout ici : la **passerelle Zen** et
**Ollama** en local. Les autres qu'OpenCode annonce (GitHub Copilot, LM Studio,
llama.cpp) devraient fonctionner par construction, puisque le provider ne parle
qu'à OpenCode — mais elles ne sont pas éprouvées, et ce README ne dit que ce
qui a été vérifié.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` est **obligatoire**, au format `provider/modèle`. OpenCode n'est pas
un fournisseur, et aucun défaut n'est choisi à votre place : son propre repli
serait un modèle gratuit dont les échanges peuvent servir à l'entraînement.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Confinement — ce que fait le script à chaque appel :**

- Une configuration inline (`OPENCODE_CONFIG_CONTENT`), prioritaire sur la
  vôtre, définit un agent `aipmt` dont **tous les outils sont refusés**
  (`permission: { "*": "deny" }`) : le modèle ne peut ni lire, ni écrire, ni
  lancer de commande — mesuré, il ne le tente même pas. Le partage de session
  est désactivé, `--pure` écarte les plugins externes, jamais `--auto`.
- L'appel tourne dans un **répertoire jetable et vide**, avec les interrupteurs
  `OPENCODE_DISABLE_PROJECT_CONFIG` et `OPENCODE_DISABLE_CLAUDE_CODE` : sans
  eux, OpenCode injecte dans chaque prompt l'`AGENTS.md` du répertoire courant
  et votre `~/.claude/CLAUDE.md` — mesuré, une consigne « finir chaque réponse
  par BANANA » posée dans un `AGENTS.md` était appliquée à la traduction. Les
  règles globales de `~/.config/opencode/AGENTS.md` restent en revanche
  appliquées : OpenCode ne permet pas de les écarter.
- Le contrat de sortie exige tout à la fois : code retour 0, aucun événement
  `error`, aucun appel d'outil, un dernier pas terminé en `stop`, un texte non
  vide, et l'agent effectivement chargé — un `--agent` inconnu ne fait pas
  échouer OpenCode, il **retombe en silence** sur l'agent de codage, outils
  actifs. Un `exit 0` ne prouve rien ici non plus.
- **Aucune clé d'aipmt n'est transmise** au sous-processus (même filtrage
  qu'avec Codex et Grok), à une exception nominative près : `OPENCODE_API_KEY`,
  la clé d'OpenCode lui-même (Zen, Go). Les fournisseurs se configurent dans
  OpenCode (`opencode auth login`, `opencode.json`), pas dans le `.env` d'aipmt.

**À savoir :**

- **Les modèles gratuits de Zen sont des modèles « stealth » ou contributeurs**,
  changeants, aux limites non documentées, et leurs échanges peuvent servir à
  l'entraînement : parfaits pour une documentation publique, à éviter pour un
  contenu privé. Mesuré : `opencode/mimo-v2.5-free` traduit ce README en une
  passe ; `opencode/big-pickle` est plus lent et deux requêtes simultanées y sont
  restées sans réponse.
- **Un modèle local doit offrir au moins 16 k de contexte** — les segments font
  jusqu'à 16 000 caractères — alors qu'Ollama en configure souvent 4 096 par
  défaut. Avec Ollama : un `Modelfile` avec `PARAMETER num_ctx 32768`, puis
  `ollama create`. La qualité suit le modèle : un 7B a inversé une liste et
  abîmé une clôture de bloc de code sur un fichier d'essai là où un modèle de
  la passerelle a tout préservé.
- `--eco` est sans effet (le modèle est celui de `--model`) ;
  `--reasoning_effort` est transmis tel quel comme `--variant` d'OpenCode, à ne
  demander que si le modèle le connaît.
- Les sessions sont journalisées par OpenCode dans sa base
  (`~/.local/share/opencode/`), comme toute session OpenCode.
- Variables d'environnement : `OPENCODE_BIN` (chemin explicite du binaire,
  sinon le `PATH` puis `~/.opencode/bin/opencode`) et `OPENCODE_TIMEOUT`
  (secondes par segment, défaut `600`). `OPENCODE_CONFIG`, s'il est
  exporté, n'est pas lu par `aipmt` : il passe tel quel à OpenCode, qui l'honore.

**Exemple mesuré : un modèle local via Ollama** (RTX 3060 12 Go, 62 Go de RAM, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # conserve les modèles déjà téléchargés
ollama pull gpt-oss:20b                         # 13 Go, Apache 2.0 — le seul modèle local retenu ici

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

Puis le fournisseur dans `~/.config/opencode/opencode.json` :

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

`reasoningEffort: "none"` n'est pas un détail : Ollama active la réflexion par
défaut sur ces modèles, et un Modelfile ne peut pas la couper. Mesuré à
travers OpenCode : sans l'option, « Le chat dort sur le tapis » coûte 919 tokens
de raisonnement et 68 s ; avec, 9 tokens.

```bash
aipmt --use_opencode --model ollama/gpt-oss-20b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

Résultats sur un article de blog réel de 589 lignes (140 liens, 21 sections,
3 citations anglaises protégées par le mode `--news`), même commande, trois
modèles :

| Modèle                                   | Durée       | Structure                                                  | Écarts                                                                                    |
| ---------------------------------------- | ----------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free` (Zen, gratuit) | 4 min 26 s  | identique à la source                                      | aucun                                                                                     |
| `ollama/gemma4-12b-32k` (local)          | 10 min 10 s | liens, URL, tableaux, tags, gras et code inline identiques | une ligne de citation inventée (🇺🇸 + paraphrase), une attribution dupliquée               |
| `ollama/qwen3.5-9b-32k` (local)          | 8 min 18 s  | liens, URL, tableaux et tags identiques                    | une ligne de citation inventée, quelques gras et codes inline ajoutés, un segment repassé |

Ces deux modèles locaux ont depuis été **écartés** : une liberté par article
suffit à disqualifier un modèle pour de la traduction publiée. Cinq autres l'ont
été pour les mêmes raisons ou par dépassement de délai (`gemma4:26b-a4b`,
`qwen3.6:35b-a3b`, `ministral-3:14b`, `mistral-small3.2`, `hy-mt2:7b`). Seul
`gpt-oss:20b` a été conservé — et lui-même laisse des passages en français sur
un article dense, cf. le tableau des modèles conseillés.

Pendant la traduction locale : GPU à 98 % et 170 W, 10 Go de VRAM occupés
(modèle et cache de 32 k tokens, rien déchargé en RAM), 7,5 Go de RAM pour le
serveur Ollama. Un modèle de 9 à 12 milliards de paramètres respecte la
structure mais s'accorde une liberté par article, là où le modèle de passerelle
n'en a pris aucune : à relire avant publication, ou à réserver aux brouillons.

### Traduire via OpenRouter (`--use_openrouter`)

OpenRouter est un **routeur** devant plus de 400 modèles hébergés par des tiers,
facturé à l'usage sur un crédit unique. Il donne accès en une clé à des modèles
qu'aucun des autres providers n'expose, notamment les modèles chinois ouverts.

```bash
# --model est OBLIGATOIRE : aucun défaut n'est choisi à votre place
aipmt --use_openrouter --model 'z-ai/glm-5.2' --file README.md \
  --target_dir . --source_lang fr --target_lang en
```

Deux particularités du routage ont dicté l'implémentation, et toutes deux se
mesurent :

- **Un même modèle est servi par des dizaines d'hébergeurs aux plafonds
  différents.** Sur `z-ai/glm-5.3-flash`, 23 hébergeurs, dont un plafonné à
  2 048 tokens de sortie : sans précaution, une traduction longue sur 23 partait
  tronquée, au hasard du routage et sans le moindre signal. Un préflight lit
  `/api/v1/models/{modèle}/endpoints`, écarte les hébergeurs sous 8 000 tokens
  de sortie ou au statut dégradé, puis épingle les autres avec
  `allow_fallbacks: false` — sans quoi le routeur repart vers un hébergeur
  écarté.
- **Le raisonnement est facturé au tarif de sortie.** Même requête sur
  `z-ai/glm-5.2`, réponse « OK » : 107 tokens de complétion au défaut du modèle,
  2 avec le raisonnement coupé. Il est donc coupé par défaut, sur les modèles
  qui l'autorisent. Ceux qui l'imposent — `reasoning.mandatory`, 288 des 431
  modèles du catalogue — reçoivent le **plus bas effort qu'ils déclarent
  accepter**, et non leur réglage par défaut : celui de `z-ai/glm-5.3-flash` est
  `max`, et il saturait les 32 768 tokens de sortie avant la fin de la
  traduction. Monter l'enveloppe n'y aurait rien changé, l'effort en alloue un
  pourcentage. `--reasoning_effort` reste prioritaire, et `none` sur un modèle
  qui impose le raisonnement est signalé plutôt que contourné.

Le préflight est **fail-closed** et affiche ce qu'il a retenu :

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

Un slug absent du catalogue, un catalogue injoignable ou l'absence d'hébergeur
tenant le plafond arrêtent la commande avant toute facturation.

Autres points :

- La fenêtre de contexte vient du catalogue, pas d'une constante : la
  segmentation s'y adapte réellement, y compris pour les modèles à 4 095 tokens.
- `--eco` est sans effet (le modèle est celui de `--model`).
- `finish_reason=length` avec une sortie vide n'est pas une troncature mais un
  budget consommé par le raisonnement ; le message le dit, parce que les deux
  cas appellent des gestes opposés.
- Variables d'environnement : `OPENROUTER_API_KEY` (clé, sur
  <https://openrouter.ai/keys>), `OPENROUTER_BASE_URL` (défaut
  `https://openrouter.ai/api/v1`, `https://` exigé), `OPENROUTER_TIMEOUT`
  (secondes par appel, défaut `900`) et `OPENROUTER_PREFLIGHT_TIMEOUT`
  (défaut `30`).

### Mode économique

Utilise des modèles plus rapides et moins coûteux (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite) :

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Options

| Option                   | Description                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Fichier Markdown unique à traduire                                                                            |
| `--source_dir`           | Répertoire source contenant les fichiers Markdown                                                             |
| `--target_dir`           | Répertoire de sortie pour les fichiers traduits                                                               |
| `--source_lang`          | Langue source (défaut: `fr`)                                                                                  |
| `--target_lang`          | Langue cible (défaut: `en`)                                                                                   |
| `--model`                | Modèle spécifique à utiliser                                                                                  |
| `--eco`                  | Utiliser les modèles économiques                                                                              |
| `--use_mistral`          | Utiliser l'API Mistral AI                                                                                     |
| `--use_claude`           | Utiliser l'API Claude                                                                                         |
| `--use_gemini`           | Utiliser l'API Gemini                                                                                         |
| `--use_codex`            | Utiliser le CLI Codex sur le quota de l'abonnement ChatGPT                                                    |
| `--use_grok`             | Utiliser l'API xAI (Grok) — nécessite `XAI_API_KEY`                                                           |
| `--use_openrouter`       | Utiliser OpenRouter — nécessite `OPENROUTER_API_KEY` et `--model fournisseur/modèle`                          |
| `--use_grok_cli`         | Utiliser le CLI Grok sur le quota de l'abonnement Grok                                                        |
| `--use_opencode`         | Utiliser OpenCode (open source) vers le fournisseur configuré dans OpenCode ; exige `--model provider/modèle` |
| `--force`                | Forcer la re-traduction                                                                                       |
| `--keep_filename`        | Conserver le nom de fichier original                                                                          |
| `--news`                 | Mode actualités : protège les citations EN, gère les drapeaux par langue                                      |
| `--add_translation_note` | Ajouter une note de traduction                                                                                |
| `--note_position`        | Position de la note : `top`, `bottom` (défaut), ou `both`                                                     |
| `--note_format`          | Format de la note : `legacy` (défaut, paragraphe gras) ou `marker`                                            |
| `--include_model`        | Inclure le nom du modèle dans le fichier de sortie                                                            |
| `--reasoning_effort`     | Effort de raisonnement GPT-5.x : `none`/`low`/`medium`/`high`/`xhigh`                                         |

> **Les huit flags de provider sont mutuellement exclusifs.** En combiner deux
> était auparavant accepté en silence et résolvait vers le premier testé : une
> traduction demandée sur quota d'abonnement (`--use_codex`, `--use_grok_cli`)
> pouvait ainsi partir en facturation à l'usage sans aucun avertissement.
> `argparse` refuse désormais la combinaison.

### Note de traduction : positions et formats

Avec `--add_translation_note`, le translator peut placer la note en haut, en bas, ou aux deux endroits, et la rendre soit en format texte simple (rétrocompatible) soit en format `marker` consommable par un plugin Markdown.

**Position** (`--note_position`) :

- `bottom` (défaut) : note en fin de fichier, comme historiquement.
- `top` : note insérée **après le frontmatter YAML** (sécurité Astro Content Collections, gray-matter, etc.).
- `both` : note insérée en haut ET en bas (un seul appel LLM, contenu réutilisé pour les deux placements).

**Format** (`--note_format`) :

- `legacy` (défaut) : paragraphe gras `**...**` — comportement strictement identique à v1.8, byte-for-byte. Compatible avec Hugo, GitHub, GitLab, et tout renderer Markdown.
- `marker` : link reference definition Markdown invisible (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) suivie d'un blockquote en gras. Lisible nativement sur GitHub/GitLab, et exploitable au build par un plugin remark côté Astro pour produire une bannière stylisée (cf. blog jls42.org).

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

### Modèles par défaut (2026)

| Provider   | Qualité (défaut)                         | Économique (`--eco`)      |
| ---------- | ---------------------------------------- | ------------------------- |
| OpenAI     | `gpt-5.6-terra`                          | `gpt-5.6-luna`            |
| Claude     | `claude-sonnet-5`                        | `claude-haiku-4-5`        |
| Mistral    | `mistral-large-latest`                   | `mistral-small-latest`    |
| Gemini     | `gemini-3.7-flash`                       | `gemini-3.1-flash-lite`   |
| Codex      | `gpt-5.6-sol`                            | `gpt-5.6-luna`            |
| Grok API   | `grok-4.6`                               | `grok-4.3`                |
| Grok CLI   | `grok-4.6`                               | `grok-4.5`                |
| OpenCode   | `--model provider/modèle` obligatoire    | idem — `--eco` sans effet |
| OpenRouter | `--model fournisseur/modèle` obligatoire | idem — `--eco` sans effet |

## Quels modèles tiennent la route

Un modèle qui traduit bien un paragraphe ne préserve pas forcément la structure
d'un document entier. Ces mesures viennent de **traductions réellement
exécutées**, avec la commande que vous liriez plus haut, sur trois jeux de
documents et quatorze langues cibles : en, es, de, it, pt, nl, pl, sv, ro, ja,
ko, zh, ar, hi.

Deux colonnes, et elles ne disent pas la même chose. **Écrites** compte les
traductions qui aboutissent — les gardes anti-échec-silencieux du script
laissent passer le fichier. **Sans écart** compte celles dont la structure est
identique à la source : mêmes sections, mêmes liens, mêmes URL, mêmes blocs et
codes en ligne, mêmes tableaux, mêmes citations, mêmes drapeaux.

### Article de blog dense, mode `--news`

589 lignes, 140 liens, 21 sections, 3 citations anglaises protégées. C'est le
document le plus exigeant des trois : le mode `--news` ajoute des contraintes de
drapeaux et de citations par-dessus la structure Markdown.

| Modèle                            | Accès              | Écrites | Sans écart | Médiane/langue |
| --------------------------------- | ------------------ | ------- | ---------- | -------------- |
| `gemini-3.7-flash`                | API Google         | 14/14   | **14/14**  | 1 min 18 s     |
| `gpt-5.6-sol` (`--use_codex`)     | abonnement ChatGPT | 14/14   | **14/14**  | 11 min 28 s    |
| `z-ai/glm-5.2`                    | OpenRouter         | 14/14   | **14/14**  | 5 min 37 s     |
| `qwen/qwen3.8-flash`              | OpenRouter         | 14/14   | 13/14      | 26 min 23 s    |
| `z-ai/glm-5.3-flash`              | OpenRouter         | 12/14   | 12/14      | 15 min 49 s    |
| `qwen/qwen3.5-27b`                | OpenRouter         | 7/9     | 7/9        | 20 min 33 s    |
| `claude-sonnet-5`                 | API Anthropic      | 14/14   | 11/14      | 6 min 31 s     |
| `opencode/mimo-v2.5-free`         | OpenCode Zen       | 13/14   | 11/14      | 9 min 27 s     |
| `qwen/qwen3.7-flash`              | OpenRouter         | 13/14   | 7/14       | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`          | local              | 10/14   | 7/14       | 12 min 39 s    |
| `mistral-large-latest`            | API Mistral        | 11/14   | 5/14       | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter         | 4/14    | 3/14       | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)     | abonnement Grok    | 1/14    | 1/14       | 23 min 11 s    |
| `moonshotai/kimi-k2.6`            | OpenRouter         | 1/4     | 1/4        | 23 min 00 s    |

Deux lots ont été **interrompus faute de crédit** et leur dénominateur le dit :
`qwen3.5-27b` s'est arrêté à neuf langues, `kimi-k2.6` à quatre — ce dernier
après un dépassement de délai de quarante minutes et deux refus, à près de
0,33 $ la langue.

Une réserve de méthode sur les lignes OpenRouter : elles ont été mesurées avec
les réglages **par défaut du routeur**, avant que `--use_openrouter` n'existe.
`z-ai/glm-5.2` a été remesuré depuis avec le provider livré, raisonnement coupé,
et rend exactement le même 14/14. `z-ai/glm-5.3-flash` a échoué deux fois par
budget de sortie épuisé au défaut du routeur ; le provider demande désormais à
ces modèles le plus bas effort qu'ils acceptent, et la contre-épreuve sur les
langues fautives passe.

### README de ce projet, Markdown standard

508 lignes, 219 codes en ligne, 40 clôtures de blocs, 45 lignes de tableau. Pas
de mode `--news` ici : la difficulté vient de la densité en code.

| Modèle                        | Écrites | Sans écart | Médiane/langue |
| ----------------------------- | ------- | ---------- | -------------- |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14   | 11/14      | 1 min 22 s     |
| `gemini-3.7-flash`            | 14/14   | 13/14      | 21 s           |
| `gpt-5.6-sol` (`--use_codex`) | 14/14   | 12/14      | 2 min 04 s     |
| `opencode/mimo-v2.5-free`     | 9/14    | 7/14       | 3 min 25 s     |
| `ollama/gpt-oss-20b-32k`      | 9/14    | 1/14       | 3 min 38 s     |

### Quatre README de projets connus

FastAPI, Ollama, tldr-pages et Vue.js, pris tels quels sur GitHub. Ces documents
sont **plus faciles** que les deux précédents, et le tableau le montre.

| Modèle                    | Périmètre                  | Écrites | Sans écart |
| ------------------------- | -------------------------- | ------- | ---------- |
| `opencode/mimo-v2.5-free` | 4 projets × 14 langues     | 55/56   | 47/56      |
| `grok-4.6` (abonnement)   | 4 projets × ar, hi, ja, zh | 16/16   | 14/16      |
| `ollama/gpt-oss-20b-32k`  | 4 projets × ar, hi, ja, zh | 15/16   | 9/16       |

### Ce qu'on en retient

- **Trois modèles n'ont jamais perdu d'information** sur les deux documents
  denses : `gemini-3.7-flash`, `gpt-5.6-sol` par l'abonnement ChatGPT, et
  `z-ai/glm-5.2` par OpenRouter. Leurs seuls écarts en mode standard sont une
  paire de `**` non reportée sur une ou deux langues, jamais une URL, un bloc
  de code ou une citation.
- **Le facteur discriminant est la densité du document, pas le mode `--news`.**
  Grok par abonnement échoue 13 fois sur 14 sur l'article de blog et réussit 14
  README publics sur 16 : sa cause d'échec est un décrochage sur segment long,
  vérifié par contre-épreuve — le passage isolé est traduit correctement.
- **Les écritures non latines ne sont pas le clivage attendu.** `gpt-oss` laisse
  des passages en français en arabe, japonais, polonais **et roumain** ; Mistral
  et MiMo ne perdent des codes en ligne que sur les écritures non latines.
- **Couper le raisonnement ne coûte rien en qualité.** `z-ai/glm-5.2` fait
  quatorze langues sans un écart dans les deux conditions — raisonnement actif
  par défaut du routeur, puis coupé par `--use_openrouter` — pour dix-huit fois
  moins de tokens de sortie facturés. C'est la mesure qui justifie le réglage
  par défaut du provider.
- **Un modèle lent n'est pas un modèle sûr.** `deepseek-v4-flash-0731` prend 37
  minutes par langue pour 4 traductions sur 14, `qwen3.8-flash` 26 minutes pour
  un résultat presque parfait, et Gemini 1 minute 18 pour un sans-faute.

### Ce que ce tableau n'est pas

- **Ce n'est pas un classement exhaustif.** OpenRouter propose à lui seul plus
  de quatre cents modèles ; une quinzaine a été mesurée ici. L'absence d'un
  modèle ne dit rien de sa qualité, seulement qu'il n'a pas été essayé.
- **Ces mesures ont une date** : 4 et 5 septembre 2026. Les modèles changent
  sous le même nom, les hébergeurs ajustent quantifications et plafonds, et de
  nouveaux modèles sortent chaque semaine.
- **Les durées ne classent rien.** Le parallélisme allait de 3 à 6 traductions
  simultanées selon les campagnes, et le débit d'un fournisseur varie dans la
  journée. Elles donnent un ordre de grandeur, pas une comparaison.
- **Un résultat dépend du document autant que du modèle.** Le même modèle
  réussit quatorze langues sur un article et neuf sur ce README. Vos fichiers ne
  sont pas les nôtres.
- **La bonne démarche reste de mesurer chez vous** : traduisez un de vos
  documents vers vos langues cibles, puis comparez la structure — nombre de
  sections, de liens, d'URL distinctes, de blocs de code, de codes en ligne, de
  lignes de tableau. C'est exactement ce que fait le protocole ci-dessus, et il
  tient en une boucle sur `aipmt`.

## Projets utilisant ce script

- **[jls42.org](https://jls42.org)** - Blog personnel multilingue (15 langues)

## Auteur

Julien LE SAUX
Email : contact@jls42.org

## Licence

GNU GENERAL PUBLIC LICENSE Version 3. Voir [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

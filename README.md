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
`GROK_TRANSLATE_SANDBOX` (voir la section Grok CLI) et `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (voir la section OpenCode). Côté
`regen_translations.sh` : `REGEN_PROVIDER` (défaut `codex`, sur abonnement),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (dérogation obligatoire pour une API
facturée) et `REGEN_JOB_TIMEOUT` (plafond par job, défaut 600 s).

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
- **Refusé en CI** (`CI` ou `GITHUB_ACTIONS` défini) : l'authentification par
  abonnement n'est pas prévue pour un runner partagé, et OpenAI déconseille ce
  workflow sur les dépôts publics. Utiliser une clé API sur ce chemin.
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

# Une API facturée (openai, gemini, grok) est REFUSÉE sans cette dérogation nommée
REGEN_PROVIDER=openai REGEN_ALLOW_PAID_API=1 ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
```

### Traduire avec OpenCode, vers le fournisseur de son choix (`--use_opencode`)

[OpenCode](https://opencode.ai) est un agent de code **open source (MIT)** en
terminal. Il n'est pas un fournisseur de modèles mais un **routeur** vers ceux
que vous avez configurés dans OpenCode lui-même : une clé API, un abonnement
(GitHub Copilot, ChatGPT, SuperGrok), la passerelle OpenCode Zen — qui sert des
modèles gratuits **sans compte** — ou un modèle **local** (Ollama, LM Studio,
llama.cpp). Ce provider pilote `opencode run` en mode non-interactif et confine
l'appel à un seul aller-retour, sans aucun outil.

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
  (secondes par segment, défaut `600`). `OPENCODE_CONFIG` est honoré si vous
  l'exportez.

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

> **Les sept flags de provider sont mutuellement exclusifs.** En combiner deux
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

| Provider | Qualité (défaut)                      | Économique (`--eco`)      |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI   | `gpt-5.6-terra`                       | `gpt-5.6-luna`            |
| Claude   | `claude-sonnet-5`                     | `claude-haiku-4-5`        |
| Mistral  | `mistral-large-latest`                | `mistral-small-latest`    |
| Gemini   | `gemini-3.7-flash`                    | `gemini-3.1-flash-lite`   |
| Codex    | `gpt-5.6-sol`                         | `gpt-5.6-luna`            |
| Grok API | `grok-4.6`                            | `grok-4.3`                |
| Grok CLI | `grok-4.6`                            | `grok-4.5`                |
| OpenCode | `--model provider/modèle` obligatoire | idem — `--eco` sans effet |

> **Recommandation traductions long-form** : `--use_gemini` (défaut = `gemini-3.7-flash`) préserve fidèlement la structure markdown sur les scripts non-latins (PL, JA, ZH, AR, HI), y compris en mode `--news` où la fidélité des placeholders compte. Mesuré sur ce README traduit en japonais : structure identique à `gemini-3.1-pro-preview` (21 listes, 18 blocs de code, 13 liens HTML, 13 images, toutes les URLs préservées) pour ~6x moins de latence. OpenAI reste le défaut pour la rétrocompatibilité.

## Projets utilisant ce script

- **[jls42.org](https://jls42.org)** - Blog personnel multilingue (15 langues)

## Auteur

Julien LE SAUX
Email : contact@jls42.org

## Licence

GNU GENERAL PUBLIC LICENSE Version 3. Voir [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

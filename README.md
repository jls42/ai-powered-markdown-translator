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

Traduit des fichiers Markdown d'une langue à une autre en préservant la
structure : blocs de code, code en ligne, URL, ancres, tableaux et front
matter. Neuf façons d'appeler un modèle — cinq API, deux abonnements sans
facturation à l'usage, deux routeurs — et une mesure publiée de ce que chaque
modèle préserve réellement.

## En bref

- **Neuf chemins de provider** : API OpenAI, Mistral, Claude, Gemini et Grok ;
  abonnements ChatGPT (Codex) et Grok sans facturation à l'usage ; routeurs
  OpenCode (open source, gratuit ou local) et OpenRouter (plus de 400 modèles).
- **Rien de faux à cause d'un jeton perdu** : blocs de code, code en ligne,
  URL, ancres et citations sont remplacés par des jetons avant l'appel et
  vérifiés au retour. S'il en manque un, le fichier n'est pas écrit.
- **Documents longs** : segmentation selon la fenêtre du modèle.
- **Mode `--news`** : citations anglaises protégées et drapeaux gérés par
  langue, pour les articles de veille.
- **Mode `--eco`** : modèles rapides et moins chers.
- **Note de traduction** optionnelle, en haut, en bas ou aux deux.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 ou plus récent. Pour installer depuis le dépôt, voir
[Contribuer](#contribuer).

## Configuration

Les clés sont lues à trois endroits, du plus prioritaire au moindre ; chacun ne
comble que ce que le précédent laisse vide.

|     | Où                                            | Pour quoi                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variables d'environnement                     | CI, conteneurs, dérogation ponctuelle |
| 2   | `.env` du répertoire courant (ou d'un parent) | une clé propre à un projet            |
| 3   | `~/.config/aipmt/.env`                        | installé une fois, vaut partout       |

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

`GEMINI_API_KEY` est accepté à la place de `GOOGLE_API_KEY`. Le fichier
utilisateur suit `XDG_CONFIG_HOME` (chemin absolu seulement) et `%APPDATA%`
sous Windows. Sans clé, la commande énumère les trois emplacements.

**Le `.env` d'un projet ne peut pas rediriger les appels.** Il fournit des clés,
jamais une destination : toute variable en `_BASE_URL`, `_API_BASE` ou
`_ENDPOINT`, les proxies (`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`), les
magasins de certificats (`SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`,
`CURL_CA_BUNDLE`) et `XDG_CONFIG_HOME` / `APPDATA` y sont ignorés, avec un
avertissement. Un dépôt cloné ne doit pas pouvoir détourner votre clé. Ce
fichier est aussi lu sans interpolation : `NOM=${OPENAI_API_KEY}` n'y recopie
pas la clé. Posez ces variables dans l'environnement ou dans
`~/.config/aipmt/.env`.

Variables optionnelles : `XAI_BASE_URL` (défaut `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (secondes par appel, défaut 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(défaut 600), `GROK_BIN`, `GROK_HOME` (défaut `~/.grok`), `GROK_TIMEOUT`
(défaut 900), `GROK_TRANSLATE_SANDBOX`, `OPENCODE_BIN`, `OPENCODE_TIMEOUT`
(défaut 600), `OPENROUTER_BASE_URL` (`https://` exigé), `OPENROUTER_TIMEOUT`
(défaut 900), `OPENROUTER_PREFLIGHT_TIMEOUT` (défaut 30). Chacune est détaillée
dans la section de son provider.

## Premiers pas

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` traduit en espagnol donne `document-es.md` dans `--target_dir` ;
avec `--include_model`, `document-es-gpt-5.6-terra.md`. L'extension devient
toujours `.md` — `article.mdx` donne `article-en.md` — sauf avec
`--keep_filename`, qui conserve le nom d'origine. Une traduction déjà présente
est sautée sans `--force`.

Codes de sortie : `0` si tout a abouti ou a été sauté, `1` s'il reste un fichier
en échec (liste sur la sortie d'erreur), `2` si la configuration est en cause.
Un fichier en échec n'est jamais écrit, même si l'écriture elle-même échoue :
le contenu est écrit à côté puis renommé. Relancer suffit.

## Quel modèle choisir

Mesuré sur deux documents réels, traduits dans les quatorze mêmes langues par
chaque modèle. **Le chiffre est le nombre de langues, sur quatorze, où la
traduction est écrite et où rien ne diffère de la source.**

| Modèle               | Comment y accéder                 | Article de veille dense | Ce README    | Ce qui diffère, et sur combien de langues                                                                                             |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | clé API Google                    | ✅ 14/14                | ⚠️ 13/14     | 1 langue sur 14 : un mot en gras de plus (ja)                                                                                         |
| **GPT-5.6 Sol**      | abonnement ChatGPT, ou clé OpenAI | ✅ 14/14                | ⚠️ 12/14     | 2 langues sur 14 : un mot en gras de moins (ar, ja)                                                                                   |
| **GLM-5.2**          | clé OpenRouter                    | ✅ 14/14                | ⚠️ 11/14     | 3 langues sur 14 : un mot en gras de moins (hi, ja, ko)                                                                               |
| Claude Sonnet 5      | clé API Anthropic                 | ⚠️ 11/14                | ⚠️ 12/14     | 3 langues sur l'article : un bloc de code apparu (es, de, hi) ; 2 sur ce README : un lien sans son balisage (sv), un mot en gras (zh) |
| Qwen 3.7 Flash       | clé OpenRouter                    | ❌ 8/14                 | ⚠️ 10/14     | 1 langue refusée sur l'article, 5 autres s'écartent ; sur ce README, une quarantaine de mots mis en `code` (ar)                       |
| Grok 4.6             | abonnement Grok                   | ❌ 8/14                 | non noté     | 5 langues refusées sur 14, faute de codes en ligne et d'URL rendus ; le néerlandais diverge sur tout                                  |
| GPT-OSS 20B          | modèle local (Ollama)             | ❌ 7/14                 | non remesuré | 4 langues refusées sur 14 : le modèle y laissait des passages en français, la garde les a arrêtés                                     |
| MiMo v2.5 (gratuit)  | OpenCode Zen, sans compte         | ❌ 11/14                | non remesuré | 1 langue refusée ; une section perdue en polonais                                                                                     |
| Mistral Large        | clé API Mistral                   | ❌ 5/14                 | ❌ 1/14      | **une section entière disparaît** : 1 langue sur l'article (hi), 3 sur ce README (ar, hi, ko) — et 3 langues refusées sur l'article   |
| DeepSeek V4 Flash    | clé OpenRouter                    | ❌ 3/14                 | non remesuré | 10 langues refusées sur 14 ; 37 minutes par langue                                                                                    |

|     | Ce que dit le symbole                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | les quatorze langues traduites, et rien ne diffère de la source                                                                                                                                       |
| ⚠️  | les quatorze langues traduites ; ce qui diffère est du **balisage** — un mot en gras, un `code`, un lien qui perd ses crochets. Aucun texte, aucune URL, aucun bloc de code, aucune section ne manque |
| ❌  | au moins une langue n'a pas pu être traduite — le fichier est refusé, pas écrit — **ou** du contenu manque dans un fichier écrit                                                                      |

Ce qu'il faut en retenir :

- **Une traduction refusée n'est pas une traduction abîmée.** Quand un jeton
  manque au retour, le fichier n'est pas écrit et la langue compte comme
  refusée. C'est ce qui arrive à Grok sur l'article : quatre codes en ligne et
  trois URL perdus dès le premier segment, sur les cinq écritures non latines.
- **Ce filet ne couvre pas les titres, les tableaux, le front matter ni le
  texte.** Un modèle qui supprime une section rend un fichier que l'outil écrit
  sans broncher — c'est le cas de Mistral. Ces éléments ne sont pas
  remplaçables par un jeton, et les gardes actuelles ne les contrôlent pas ;
  `scripts/compare_structure.py` détecte une section perdue, mais après coup.
- **Grok n'a pas de note sur ce README** : sa session CLI a expiré après douze
  langues, dont onze sans écart. Une campagne interrompue ne se note pas.
- **La densité du document compte plus que la langue.** Grok tient sur des
  README ordinaires et décroche sur un article chargé de liens, y compris en
  néerlandais.

Dates et documents : la colonne « Ce README » a été mesurée le 9 septembre 2026
sur une révision figée de ce fichier (785 lignes, 285 codes en ligne, 89 lignes
de tableau), retouchée depuis. La colonne « Article de veille dense » vient de
la campagne des 4 et 5 septembre sur un article de 589 lignes, sauf la ligne
Grok, remesurée le 9 septembre sur une autre édition de la même veille. Les
tableaux complets, les durées et le protocole sont dans
[Mesures détaillées](#mesures-détaillées).

## Toutes les options

| Option                   | Description                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Fichier Markdown unique à traduire (alternative à `--source_dir`)                                             |
| `--source_dir`           | Répertoire source contenant les fichiers Markdown (défaut: `content/posts`)                                   |
| `--target_dir`           | Répertoire de sortie pour les fichiers traduits (défaut: `traductions_en`)                                    |
| `--source_lang`          | Langue source (défaut: `fr`)                                                                                  |
| `--target_lang`          | Langue cible (défaut: `en`)                                                                                   |
| `--model`                | Modèle spécifique à utiliser                                                                                  |
| `--eco`                  | Utiliser les modèles économiques                                                                              |
| `--use_mistral`          | Utiliser l'API Mistral AI                                                                                     |
| `--use_claude`           | Utiliser l'API Claude                                                                                         |
| `--use_gemini`           | Utiliser l'API Gemini                                                                                         |
| `--use_grok`             | Utiliser l'API xAI (Grok) — nécessite `XAI_API_KEY`                                                           |
| `--use_codex`            | Utiliser le CLI Codex sur le quota de l'abonnement ChatGPT                                                    |
| `--use_grok_cli`         | Utiliser le CLI Grok sur le quota de l'abonnement Grok                                                        |
| `--use_opencode`         | Utiliser OpenCode (open source) vers le fournisseur configuré dans OpenCode ; exige `--model provider/modèle` |
| `--use_openrouter`       | Utiliser OpenRouter — nécessite `OPENROUTER_API_KEY` et `--model fournisseur/modèle`                          |
| `--force`                | Forcer la re-traduction                                                                                       |
| `--keep_filename`        | Conserver le nom de fichier original                                                                          |
| `--news`                 | Mode actualités : protège les citations EN, gère les drapeaux par langue                                      |
| `--add_translation_note` | Ajouter une note de traduction                                                                                |
| `--note_position`        | Position de la note : `top`, `bottom` (défaut), ou `both`                                                     |
| `--note_format`          | Format de la note : `legacy` (défaut, paragraphe gras) ou `marker`                                            |
| `--include_model`        | Inclure le nom du modèle dans le fichier de sortie                                                            |
| `--reasoning_effort`     | Effort de raisonnement GPT-5.x : `none`/`low`/`medium`/`high`/`xhigh`                                         |

Les huit flags `--use_*` sont mutuellement exclusifs : en combiner deux est
refusé.

## Providers

### Par API : OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` bascule sur le palier économique de chaque fournisseur.

| Provider   | Qualité (défaut)                                      | Économique (`--eco`)      |
| ---------- | ----------------------------------------------------- | ------------------------- |
| OpenAI     | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude     | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral    | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini     | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex      | `gpt-5.6-sol` (aussi `terra` et `luna` par `--model`) | `gpt-5.6-luna`            |
| Grok API   | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI   | `grok-4.6`                                            | `grok-4.5`                |
| OpenCode   | `--model provider/modèle` obligatoire                 | idem — `--eco` sans effet |
| OpenRouter | `--model fournisseur/modèle` obligatoire              | idem — `--eco` sans effet |

### Sur l'abonnement ChatGPT : `--use_codex`

Pilote le CLI Codex officiel : la traduction est décomptée du quota de
l'abonnement ChatGPT, sans clé API ni facturation à l'usage.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- Le binaire est cherché dans `CODEX_BIN`, puis le `PATH`, puis le package
  `openai-codex-cli-bin`. `~/.codex/auth.json` n'est jamais lu.
- `OPENAI_API_KEY` et `CODEX_API_KEY` sont retirées de l'environnement du
  sous-processus : une clé présente ne fait jamais basculer vers l'API.
- Chaque segment coûte au moins un « message » de la fenêtre de 5 heures — deux
  si sa validation échoue et qu'il est retenté. OpenAI annonce, à titre
  d'estimation, 250-2 000 messages/5 h pour `gpt-5.6-luna` (`--eco`) et
  10-100 pour `gpt-5.6-sol` sur un plan Plus.
- `--model gpt-5.6-terra` et `--model gpt-5.6-luna` passent aussi par
  l'abonnement. Un modèle auquel le compte n'a pas droit rend un 400 « model is
  not supported when using Codex with a ChatGPT account ».
- Plus lent qu'une API, et l'écart grandit avec le document : sur ce README,
  6 min 46 s par langue en médiane avec `gpt-5.6-sol`, contre 36 s pour
  `gemini-3.7-flash`.
- Refusé en CI (`CI` ou `GITHUB_ACTIONS` défini) : l'abonnement s'authentifie
  par un fichier de session personnel, qui n'a rien à faire sur un runner
  partagé.
- Variables : `CODEX_BIN`, `CODEX_TIMEOUT` (secondes par segment, défaut 600).

### Sur l'abonnement Grok : `--use_grok_cli`

Même principe avec le CLI officiel Grok Build, sur l'abonnement SuperGrok ou
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Confinement plus faible que Codex.** Le sandbox OS de Grok ne s'applique
  pas sur beaucoup de postes Linux récents (AppArmor, sockets de runtime
  conteneur), et un profil qui ne peut pas s'appliquer démarre non confiné en
  silence. Le script ne demande donc aucun profil par défaut, l'annonce, et
  s'appuie sur les règles `--deny` du CLI, dont le catch-all `*` — la seule
  couche qui refuse de démarrer plutôt que de retirer la protection sans le
  dire. `GROK_TRANSLATE_SANDBOX=read-only` exige le sandbox OS, et le démarrage
  échoue si la machine ne peut pas l'honorer.
- Le quota est hebdomadaire, partagé avec Chat, Imagine et Voice, et aucune
  commande ne permet de le lire : un lot peut entamer l'usage conversationnel
  sans signal.
- Variables : `GROK_BIN`, `GROK_HOME` (répertoire du CLI, défaut `~/.grok`),
  `GROK_TIMEOUT` (défaut 900), `GROK_TRANSLATE_SANDBOX`.

### Vers le fournisseur de son choix : `--use_opencode`

[OpenCode](https://opencode.ai) est un agent de code open source (MIT) qui
route vers les fournisseurs configurés en son sein : clé API, abonnement,
passerelle OpenCode Zen (modèles gratuits, sans compte) ou modèle local. Deux
voies ont été mesurées de bout en bout ici, Zen et Ollama.

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

`--model` est obligatoire : sans lui, OpenCode retomberait sur un modèle gratuit
dont les échanges peuvent servir à l'entraînement, et ce choix ne se fait pas à
votre place.

Confinement à chaque appel :

- une configuration inline, prioritaire sur la vôtre, définit un agent `aipmt`
  dont tous les outils sont refusés (`permission: { "*": "deny" }`), partage de
  session désactivé, `--pure`, jamais `--auto` ;
- répertoire de travail jetable et vide, `OPENCODE_DISABLE_PROJECT_CONFIG` et
  `OPENCODE_DISABLE_CLAUDE_CODE` posés — sans eux, OpenCode injecte dans le
  prompt l'`AGENTS.md` du répertoire courant et `~/.claude/CLAUDE.md`. Le
  `~/.config/opencode/AGENTS.md` global reste injecté, OpenCode ne permet pas
  de l'écarter ;
- contrat de sortie : code retour 0, aucun événement `error`, aucun appel
  d'outil, dernier pas en `stop`, texte non vide, et l'agent `aipmt`
  effectivement chargé — un `--agent` inconnu ne fait pas échouer OpenCode, il
  retombe en silence sur l'agent de codage ;
- aucune clé d'`aipmt` n'est transmise, sauf `OPENCODE_API_KEY`, la clé
  d'OpenCode lui-même. Les fournisseurs se configurent dans OpenCode, pas dans
  le `.env` d'`aipmt`.

À savoir :

- Les modèles gratuits de Zen sont changeants, aux limites non documentées, et
  leurs échanges peuvent servir à l'entraînement : pour une documentation
  publique, pas pour un contenu privé.
- Un modèle local doit offrir au moins 16 k tokens de contexte, les segments
  faisant jusqu'à 16 000 caractères. Ollama en configure souvent 4 096 : passer
  par un `Modelfile` avec `PARAMETER num_ctx 32768`.
- `--eco` est sans effet ; `--reasoning_effort` est transmis tel quel comme
  `--variant` d'OpenCode.
- OpenCode journalise chaque session dans `~/.local/share/opencode/`.
- Variables : `OPENCODE_BIN` (sinon le `PATH`, puis `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (secondes par segment, défaut 600). `OPENCODE_CONFIG`
  passe tel quel à OpenCode.

Exemple d'un modèle local via Ollama, dans `~/.config/opencode/opencode.json` :

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

`reasoningEffort: "none"` coupe la réflexion qu'Ollama active par défaut sur ces
modèles, et qu'un Modelfile ne peut pas désactiver. Mesuré sur une phrase de
six mots : 919 tokens de réflexion et 68 secondes sans l'option, 9 tokens avec.

### Vers plus de 400 modèles : `--use_openrouter`

OpenRouter est un routeur facturé à l'usage, sur un crédit unique, devant des
modèles hébergés par des tiers — dont les modèles chinois ouverts qu'aucun
autre provider n'expose ici.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` est obligatoire. Un préflight, exécuté avant toute facturation, règle
deux particularités du routage :

- **Un même modèle est servi par des dizaines d'hébergeurs aux plafonds
  différents** — sur `z-ai/glm-5.3-flash`, 23 hébergeurs dont un plafonné à
  2 048 tokens de sortie. Le préflight lit `/api/v1/models/{modèle}/endpoints`,
  écarte les hébergeurs sous 8 000 tokens de sortie ou au statut dégradé, et
  épingle les autres avec `allow_fallbacks: false`.
- **Le raisonnement est facturé au tarif de sortie** — 107 tokens contre 2 sur
  une réponse « OK » de `z-ai/glm-5.2`. Il est coupé par défaut ; les modèles
  qui l'imposent reçoivent le plus bas effort qu'ils acceptent, le défaut du
  catalogue pouvant saturer la sortie avant la fin de la traduction.
  `--reasoning_effort` reste prioritaire.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- La fenêtre de contexte vient du catalogue. Un modèle sous 16 400 tokens est
  refusé avant tout appel : 8 400 pour le prompt et le segment, 8 000 de sortie
  au minimum.
- Un slug absent du catalogue, un catalogue injoignable ou l'absence
  d'hébergeur tenant le plafond arrêtent la commande.
- `finish_reason=length` avec une sortie vide est un budget consommé par le
  raisonnement, pas une troncature : le message le distingue.
- `--eco` est sans effet.
- Variables : `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (défaut `https://openrouter.ai/api/v1`, `https://`
  exigé), `OPENROUTER_TIMEOUT` (défaut 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (défaut 30).

### Note de traduction

`--add_translation_note` ajoute une note, en `bottom` (défaut), `top` (après le
front matter) ou `both` (`--note_position`), au format `legacy` (paragraphe en
gras, défaut) ou `marker` (`--note_format`). Le format `marker` est une
définition de référence Markdown invisible,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
suivie d'une citation en gras : lisible sur GitHub, exploitable au build par un
plugin remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Mesures détaillées

Toutes les mesures sont des traductions réellement exécutées avec `aipmt`, vers
quatorze langues : en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Écrites** compte les fichiers que les gardes ont laissé passer ; **Sans
écart** ceux où `scripts/compare_structure.py` ne relève rien — même nombre de
sections, de sous-titres, de liens, d'URL distinctes, de blocs de code, de
codes en ligne, de lignes de tableau, de blocs de citation et de mots en gras.

« Sans écart » veut dire « rien de détecté », pas « identique » : le comparateur
compte des éléments sans lire leur contenu. Il ne signale ni un titre de
niveau 4 supprimé, ni le texte d'un code en ligne remplacé, ni un drapeau
échangé, et ne juge pas la langue.

### Article de veille dense, mode `--news`

Une édition de la [veille IA de jls42.org](https://jls42.org/fr/news) :
589 lignes, 140 liens, 21 sections, 3 citations anglaises protégées. Campagne
des 4 et 5 septembre 2026.

| Modèle                            | Accès              | Écrites | Sans écart   | Médiane/langue |
| --------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                | API Google         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gpt-5.6-sol` (`--use_codex`)     | abonnement ChatGPT | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                    | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`              | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `claude-sonnet-5`                 | API Anthropic      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `opencode/mimo-v2.5-free`         | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`              | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`          | local              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`            | API Mistral        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)     | abonnement Grok    | 1/14    | ❌ 1/14      | 23 min 11 s    |

Grok a été remesuré le 9 septembre sur une autre édition de la même veille
(356 lignes) : 9 langues écrites sur 14, 8 sans écart. C'est ce chiffre qui
figure dans le tableau de tête. Trois campagnes interrompues ne sont pas
notées : `qwen3.5-27b` (9 langues) et `kimi-k2.6` (4) faute de crédit,
`z-ai/glm-5.3-flash` dont les deux échecs venaient d'un réglage de raisonnement
que le provider corrige depuis. Les lignes OpenRouter ont été mesurées aux
réglages par défaut du routeur, avant `--use_openrouter` ; `z-ai/glm-5.2`,
remesuré avec le provider livré, rend le même 14/14. Les chiffres ont été
recalculés le 10 septembre avec le comparateur actuel : `qwen3.8-flash` et
`qwen3.7-flash` gagnent chacun une langue par rapport à la première
publication, les autres sont inchangés.

### README de ce projet, Markdown standard

Révision figée le 9 septembre 2026 : 785 lignes, 285 codes en ligne, 40
clôtures de blocs, 89 lignes de tableau. Quatre traductions en parallèle.

| Modèle                        | Écrites | Sans écart | Médiane/langue | Ce qui diffère                                                           |
| ----------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.7-flash`            | 14/14   | ⚠️ 13/14   | 36 s           | un mot en gras (ja)                                                      |
| `claude-sonnet-5`             | 14/14   | ⚠️ 12/14   | 2 min 56 s     | un lien (sv), un mot en gras (zh)                                        |
| `gpt-5.6-sol` (`--use_codex`) | 14/14   | ⚠️ 12/14   | 6 min 46 s     | un mot en gras (ar, ja)                                                  |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14   | ⚠️ 11/14   | 2 min 34 s     | un mot en gras (hi, ja, ko)                                              |
| `qwen/qwen3.7-flash`          | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 40 codes en ligne ajoutés en arabe ; gras (hi, ja, ko)                   |
| `mistral-large-latest`        | 14/14   | ❌ 1/14    | 2 min 44 s     | une section perdue (ar, hi, ko) ; blocs de code ajoutés (ja, ko, ro, zh) |

Deux campagnes interrompues ne sont pas notées : Grok, session CLI expirée
après douze langues (onze sans écart), et `qwen3.8-flash`, HTTP 429 de son
hébergeur après deux. `opencode/mimo-v2.5-free` et `ollama/gpt-oss-20b-32k`
n'ont pas été remesurés sur cette révision ; sur celle des 4 et 5 septembre,
plus courte de 277 lignes, ils écrivaient chacun 9 traductions sur 14, dont 7
et 1 sans écart.

### Quatre README de projets connus

FastAPI, Ollama, tldr-pages et Vue.js, pris tels quels sur GitHub — des
documents plus faciles que les deux précédents. La campagne visait les modèles
en difficulté ; Gemini y sert de point de comparaison.

| Modèle                    | Périmètre                  | Écrites | Sans écart   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 projets × 14 langues     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 projets × 14 langues     | 55/56   | ❌ 47/56     |
| `grok-4.6` (abonnement)   | 4 projets × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 projets × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### Ce que ces mesures ne sont pas

- **Pas un classement exhaustif** : OpenRouter seul propose plus de quatre cents
  modèles, une quinzaine a été mesurée.
- **Des durées indicatives** : de trois à six traductions en parallèle selon
  les campagnes, et le débit d'un fournisseur varie dans la journée.
- **Des observations datées** : les modèles changent sous le même nom, et vos
  documents ne sont pas les nôtres.

Pour refaire la mesure sur vos documents, sur une copie figée du fichier :

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## Contribuer

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

Les deux lignes sont nécessaires : sans `pip install -e .`, `python -m aipmt`
répond `No module named aipmt`.

Outillage qualité, optionnel mais recommandé :

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

Les 28 traductions du dépôt (README et CHANGELOG, quatorze langues) se
régénèrent avec `./regen_translations.sh --force` — Codex et `gpt-5.6-sol` sur
l'abonnement ChatGPT par défaut, quatre en parallèle. `REGEN_PROVIDER` et
`REGEN_MODEL` changent le chemin ; une API facturée (`openai`, `gemini`,
`grok`, `openrouter`) est refusée sans `REGEN_ALLOW_PAID_API=1` ;
`REGEN_JOB_TIMEOUT` plafonne chaque job (600 s, 1 800 s sur Codex). Le détail
de l'outillage est dans `CLAUDE.md`.

## Projets utilisant ce script

- **[jls42.org](https://jls42.org)** — blog personnel publié en 15 langues. Sa
  [veille IA quotidienne](https://jls42.org/fr/news) est traduite chaque jour
  par cet outil, et sert de document de référence aux mesures ci-dessus.

## Auteur

Julien LE SAUX
Email : contact@jls42.org

## Licence

GNU GENERAL PUBLIC LICENSE Version 3. Voir [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Avertissement

Ce programme est distribué **sans aucune garantie**, dans les termes des
sections 15 et 16 de la GPL v3 : fourni « en l'état », sans garantie de qualité
marchande ni d'adéquation à un usage particulier, et son auteur ne peut être
tenu responsable d'un dommage résultant de son utilisation. Le texte de la
licence prime sur ce résumé.

- **Relisez avant de publier.** Les protections couvrent les blocs de code, le
  code en ligne, les URL, les ancres et les citations du mode `--news` — ni les
  titres, ni les tableaux, ni le front matter, ni le sens de vos phrases.
- **Vos documents partent chez le fournisseur choisi**, sous ses conditions
  d'utilisation et sa politique de données. Certains modèles gratuits peuvent
  réutiliser vos échanges pour l'entraînement ; un modèle local est la seule
  voie qui ne fasse sortir aucune donnée de votre machine.
- **Les appels d'API vous sont facturés.** Ce programme ne plafonne pas la
  dépense : un document long, une reprise après échec ou un modèle qui raisonne
  beaucoup coûtent davantage.
- **Les mesures publiées sont des observations datées**, pas des garanties.

Les noms de produits et de sociétés cités appartiennent à leurs détenteurs
respectifs. Ce projet n'est affilié à aucun d'entre eux.

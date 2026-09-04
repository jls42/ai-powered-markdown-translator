# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Definition of Done — ne jamais annoncer « c'est bon » sans preuve

**Règle absolue : avant de déclarer un travail terminé, fiable, prêt à commiter
ou prêt à releaser, exécuter `./scripts/check-release-ready.sh` et coller son
verdict.** Une impression de complétude n'est pas une preuve : ce script a été
créé après plusieurs « c'est prêt » démentis ensuite par une vérification
(flag non documenté, traduction périmée, script sortant en erreur malgré un
succès, provider non testé de bout en bout).

```bash
./scripts/check-release-ready.sh          # 16 vérifications, ~45 s
./scripts/check-release-ready.sh --full   # 17 : + hooks pre-push (mypy, SAST, audit), ~3 min
```

Ce qu'il vérifie : tests `tests/` et `scripts/tests/`, hooks pre-commit (et
pre-push en `--full`), **chaque flag argparse présent dans le README**, **chaque
`os.getenv` documenté**, les 28 traductions (présence, structure, URLs,
placeholders, couverture des flags), la version du CHANGELOG, son extraction
par `release.sh` et son égalité avec celle de `pyproject.toml`, l'absence de
secret dans les fichiers suivis, et une 7ᵉ section qui confronte la doc au point
d'entrée console et le déclencheur du hook Lizard à son scope réel (cf. § Lizard).

Points de méthode qui ont coûté cher et que le script encode :

- **La fraîcheur des traductions se mesure au CONTENU, pas aux dates.**
  `prettier` réécrit les sources sans en changer le sens : comparer des
  timestamps produit des faux positifs à chaque passage de hook.
- **Un `exit 0` ne prouve rien.** Ni pour `codex exec`, ni pour `grok`, ni pour
  `regen_translations.sh` (dont un `trap` masquait les vrais échecs).
  Toujours valider une condition métier, jamais le seul code retour.
- **Un fichier non suivi par git échappe aux hooks.** `pre-commit` ne scanne que
  l'index : `git add` un nouveau fichier AVANT de croire qu'il est propre.
- **Mesurer plutôt que déduire.** Deux agents de recherche se sont contredits
  sur la disponibilité d'un modèle Gemini ; un appel réel de 30 secondes a
  tranché. Face à un doute vérifiable, vérifier.

Si une vérification échoue, le travail continue — on ne rend pas la main sur un
« presque ». Pour enchaîner les corrections sans supervision, `/loop` permet de
reprendre la tâche jusqu'à ce que le script passe au vert.

## Traductions de ce dépôt : JAMAIS par une API facturée

**Décision du propriétaire, non négociable, formulée le 2026-09-04 :** les 28
traductions (README, CHANGELOG) se font sur **l'abonnement ChatGPT via Codex**,
avec **`gpt-5.6-sol`** (le modèle qualité). L'abonnement a été pris exprès pour
ne pas payer de coûts API. Ce jour-là, `release.sh --auto` avait envoyé les 28
fichiers sur l'API OpenAI, puis le CHANGELOG hindi sur celle de Gemini, parce
que le regen auto-détectait `OPENAI_API_KEY` dans `.env` et ne faisait de Codex
qu'un opt-in.

Ce que ça implique, et ce qui l'encode :

- `./regen_translations.sh --force` sans variable = Codex, `gpt-5.6-sol`, 4
  jobs. Plus aucune auto-détection de clé : une clé présente ne change rien.
- `REGEN_PROVIDER=openai|gemini|grok` est **refusé** (exit 1, message qui cite
  cette règle) tant que `REGEN_ALLOW_PAID_API=1` n'est pas posé en plus. Ne
  jamais poser cette dérogation sans demande explicite du propriétaire — pas
  même pour rattraper un fichier en échec : relancer Codex, ou `grok_cli`.
- Un fichier qui échoue sur Codex (placeholder perdu, cas connu du hindi) se
  relance **seul, sur Codex** : `python -m aipmt --use_codex --file CHANGELOG.md
--target_lang hi --add_translation_note --force`.
- Les tests `TestDetectProvider` verrouillent le défaut, le refus et la
  dérogation.

## Claude Code Workflow

- **Commits**: Utiliser le skill `/helping-with-commits` pour tous les commits
- **Recherche web**: Utiliser l'agent `web-research-specialist:web-research-specialist` pour les recherches de documentation (évite de polluer le contexte principal)
- **Après chaque `git push`** (sur une PR, jamais main) : surveiller automatiquement les checks GitHub jusqu'à résolution.
  1. Attendre ~30-60s que SonarCloud / CodeQL terminent leur scan initial.
  2. `gh pr checks <num>` pour lire l'état (workflows actifs : `Analyze (python)` et `Analyze (actions)` (CodeQL), `SonarQube`, `SonarCloud Code Analysis`, `Python 3.10` / `3.11` / `3.12` (tests.yml), `Résolution des dépendances` (deps-check.yml), `Codacy Static Code Analysis`, `CodeFactor`).
  3. Si tous `pass` → **toujours** requêter l'API Sonar des issues ouvertes en complément (cf. piège ci-dessous), puis signaler à l'utilisateur et stop.
  4. Si un check est `pending` → re-check dans 60-90s (utiliser `ScheduleWakeup` pour ne pas bloquer le main thread, ou `gh run watch <run-id>` pour follow live).
  5. Si un check est `fail` :
     - Récupérer les détails via `gh run view <run-id> --log-failed` ou l'URL Sonar/CodeQL dans la colonne link.
     - **Reproduire localement AVANT de proposer un fix** (règle "mesurer > deviner") — selon le check :
       - SonarQube : la finding peut souvent être reproduite avec `pre-commit run --hook-stage pre-push --all-files` (Lizard CCN, Opengrep SAST, ruff). Pour les règles Sonar spécifiques (`python:S1234`), consulter directement l'URL Sonar du finding.
       - CodeQL : voir l'URL `actions/runs/.../job/...` pour la query rule + emplacement source.
       - Tests : `python -m unittest discover tests/` puis `python -m unittest discover scripts/tests/`.
     - Appliquer le fix → `pre-commit run --all-files && pre-commit run --hook-stage pre-push --all-files` verts → skill `/helping-with-commits` → `git push`.
  6. Reboucler jusqu'à tous verts ou finding non-trivial (dans ce cas stop et demander aide).
  7. Pièges connus :
     - **`gh pr checks <num>` ne reflète QUE le quality gate Sonar, pas les issues ouvertes**. Un Major Code Smell qui ne fait pas tomber le gate apparaîtra `pass` côté GitHub mais reste à traiter. Après chaque push, requêter en plus l'API publique :
       ```bash
       curl -s "https://sonarcloud.io/api/issues/search?componentKeys=jls42_ai-powered-markdown-translator&pullRequest=<num>&resolved=false&ps=50" \
         | python3 -c "import json,sys; d=json.load(sys.stdin); print('total:', d.get('total', 0)); [print(f\"  [{i['severity']}] {i['type']} {i['rule']} {i['component'].split(':')[-1]}:{i.get('line','?')} - {i['message']}\") for i in d.get('issues', [])]"
       ```
       Délai d'indexation Sonar : ~60-90s après le push (ré-exécuter si `total` reflète encore l'ancien commit).
     - **Les hotspots de sécurité Sonar sont un compteur DISTINCT des issues** : `api/issues/search` ne les inclut pas. Interroger aussi
       `https://sonarcloud.io/api/hotspots/search?projectKey=jls42_ai-powered-markdown-translator&pullRequest=<num>` (clé `hotspots`).
     - **Codacy** est un check de PR dont le détail n'est lisible que par API (la page exige une session) :
       `https://app.codacy.com/api/v3/analysis/organizations/gh/jls42/repositories/ai-powered-markdown-translator/pull-requests/<num>/issues`.
       Ignorer les entrées `deltaType: Fixed` (anciennes occurrences résolues). Codacy attribue un finding aux LIGNES DU DIFF : toucher une
       ligne ancienne — même un commentaire — fait remonter un problème préexistant, ce qui est une bonne chose.
     - Le gate Lizard local couvre `src/` et `scripts/`, et son scope est désormais fail-closed : un chemin absent fait échouer le script au lieu d'être ignoré en silence (`lizard` sort en 0 en annonçant « 0 file analyzed »).
     - **`ruff-format` peut fusionner deux f-strings adjacents sur une seule ligne**, ce qui crée une concaténation implicite que Sonar S5799 (`Merge these implicitly concatenated strings; or did you forget a comma?`) flag comme Code Smell Major. Préférer une seule f-string au lieu de deux f-strings sur des lignes séparées si le contenu peut tenir sous la limite de longueur.
     - **`ruff-format` peut déplacer un marqueur `# nosemgrep` hors de portée.** Un marqueur ne vaut que pour sa ligne ou celle qui la précède, et les deux règles `dangerous-subprocess-use*` s'ancrent sur des lignes différentes (l'appel pour `-audit`, l'argument pour l'autre). Si l'argument dépasse 100 colonnes, le formateur éclate la liste et emporte le commentaire sur la ligne de FERMETURE, où il ne couvre plus rien — le correctif est défait sans signal. Parade mesurée : sortir l'argv dans une variable courte pour que la ligne ne puisse plus être scindée (cf. `tests/test_orchestration.py`). Le SAST local exclut `*test*` ; Codacy, lui, scanne les tests.
     - detect-secrets régénère parfois `.secrets.baseline` en pre-commit ; bien `git add` la baseline AVANT le commit suivant (sinon le pre-commit hook re-mute la baseline en boucle).
     - Hooks pre-push lents (~30s mypy + 5s SAST + 10s pip-audit + tests) : si on enchaîne plusieurs petits commits, préférer batcher en local et un seul `git push` à la fin.

## Fraîcheur des dépendances — deux filets, parce qu'un seul a déjà lâché

**Le retard de dépendances est passé inaperçu pendant des mois.** Dependabot
tournait, mais sans `.github/dependabot.yml` GitHub n'active que les _security
updates_ : il ne propose une PR que pour une dépendance visée par une CVE. Il a
donc bien bumpé `urllib3` et `idna`, pendant qu'`openai` dérivait de 2.54 à 3.6,
`anthropic` de 0.125 à 1.2, et que `certifi` — le magasin de certificats racine
qui valide TLS pour tous les appels providers — accumulait deux ans de retard.

Deux mesures, volontairement redondantes :

1. **`.github/dependabot.yml`** active les _version updates_ hebdomadaires (pip
   et github-actions). Mineures et correctifs sont groupés en une PR — un patch
   bump par PR finit ignoré, et le bruit est l'ennemi de la mise à jour. Les
   **majeures restent séparées** : chacune peut casser le code sans que la doc
   le dise.

2. **`./scripts/check-deps-fresh.sh`**, câblé dans le gate de fin de travail.
   Dependabot _propose_, il ne garantit pas : ses PR peuvent s'empiler sans
   être mergées. Ce contrôle rend le retard visible dans le verdict du projet.
   - retard de **majeure** → échec ;
   - retard de mineure/correctif → avertissement. Échouer sur chaque patch
     rendrait le gate rouge en permanence, donc ignoré — précisément le mode de
     défaillance qu'on cherche à éviter ;
   - PyPI injoignable → skip explicite en local, **fail-closed en CI**. Un
     contrôle qui ne s'est pas exécuté n'est pas un succès.

**Une majeure de SDK se valide par un appel réel, provider par provider.** Deux
précédents mesurés : `anthropic` ≥ 1.0 refuse côté client un appel non-streamé
dont le `max_tokens` laisse présager plus de 10 minutes — invisible dans la
doc, attrapé seulement par un vrai appel ; et `google-genai` a changé toute la
surface d'appel par rapport à `google-generativeai`.

**`requirements.txt` doit être la fermeture complète**, pas la liste des
imports. Il lui manquait `google-auth`, `cryptography` et la pile
`opentelemetry` — présents dans le venv de travail mais jamais déclarés, si
bien qu'une install fraîche ne reproduisait pas l'environnement testé. Le
régénérer par `pip freeze` d'un venv construit à partir des seules dépendances
directes évite à la fois ce trou et l'accumulation d'orphelins (`tokenizers` et
`huggingface-hub`, reliquats de `mistralai` 1.x, n'étaient plus requis par
rien).

## Quality / pre-commit (workflow)

Le projet utilise le framework [`pre-commit`](https://pre-commit.com) avec un setup "type EurekAI complet" (cf. `.pre-commit-config.yaml`). Tous les hooks tournent localement avant chaque commit (rapides) ou avant chaque push (lourds, réseau).

### Bootstrap (une fois après clone)

```bash
source venv/bin/activate
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks pre-commit (rapides)
pre-commit install --hook-type pre-push  # hooks pre-push (mypy, SAST, audit, tests)
```

Le premier `pre-commit run --all-files` télécharge les environnements des hooks (~1-2 min, en cache après).

### Hooks actifs

| Stage      | Hook                           | Rôle                                                                            |
| ---------- | ------------------------------ | ------------------------------------------------------------------------------- |
| pre-commit | shellcheck                     | Lint des `.sh` (release.sh, regen_translations.sh, scripts/)                    |
| pre-commit | ruff + ruff-format             | Lint + format Python (rapide, --fix automatique)                                |
| pre-commit | prettier                       | Format JSON/YAML/MD (28 traductions exclues)                                    |
| pre-commit | pre-commit-hooks v5            | Trailing-whitespace, EOF, check-yaml/toml, large-files, merge-conflict, shebang |
| pre-commit | detect-secrets                 | Détection de fuites d'API keys (4 providers utilisés)                           |
| pre-commit | check-complexity (Lizard)      | CCN <= 12, scope `src/` + `scripts/`, existence des chemins vérifiée            |
| pre-push   | mypy (lax)                     | Type-checking des fonctions déjà annotées (durcissement progressif)             |
| pre-push   | check-security-sast (Opengrep) | SAST sur src/ + scripts/ (graceful skip si binaire absent)                      |
| pre-push   | check-pip-audit                | Audit deps (mode reporting initial, durcir après bump)                          |
| pre-push   | unittest                       | Tests `tests/` + `scripts/tests/`                                               |

### Lancer manuellement

```bash
pre-commit run --all-files                         # tous les hooks pre-commit
pre-commit run --hook-stage pre-push --all-files   # tous les hooks pre-push
pre-commit run ruff --all-files                    # un hook précis
```

### Échappatoires (à utiliser sciemment)

```bash
git commit --no-verify   # skip les hooks pre-commit
git push --no-verify     # skip les hooks pre-push
```

### Stratégie mypy progressive

mypy est en mode **Lax** au démarrage (`disallow_untyped_defs = false`, `check_untyped_defs = false`). Concrètement, mypy ne vérifie que les fonctions déjà annotées avec des types ; les autres sont ignorées silencieusement.

Trajectoire :

1. **Phase 1 (actuel)** : mypy lax, 0 effort initial. Filet de sécurité quand on ajoute des annotations.
2. **Phase 2** : annoter les fonctions critiques de `src/aipmt/translate.py` (`segment_text`, `translate`, `translate_markdown_file`). Bumper `check_untyped_defs = true`.
3. **Phase 3** : `disallow_untyped_defs = true` (mypy strict). Tout le code annoté.

### Lizard CCN — scope et fail-closed

Le seuil est 12 (futur 8). `src/aipmt/translate.py` est **dans** le scope depuis que
le refactor des providers l'a fait repasser dessous : 158 fonctions, CCN moyen
3,3, zéro dépassement. L'exclusion documentée ici auparavant ne correspondait
plus au script depuis ce refactor.

Le scope vit dans un tableau `SCOPE` en tête de `scripts/check-complexity.sh`,
dont **chaque entrée est vérifiée existante avant l'analyse**. Sans cette garde,
un simple déplacement de fichier désarmait le gate en silence : `lizard` ignore
un chemin absent, sort en 0 et n'écrit rien. Mesuré sur une copie migrée — de
158 fonctions / 2247 nloc à 3 fonctions / 34 nloc, sortie de zéro octet.

Le hook `files:` de `.pre-commit-config.yaml` doit suivre le même chemin : une
regex qui ne matche plus ne fait pas échouer pre-commit, elle fait **sauter** le
hook. La 7ᵉ section de `check-release-ready.sh` confronte les deux.

Pour vérifier les CCN actuels : `./venv/bin/python -m lizard -l python src/aipmt/translate.py`.

### Deux gardes CI ajoutées pour la publication

- **Plancher de couverture** (`sonarcloud.yml`) : `coverage run --source=module_absent`
  n'échoue PAS — avertissement sur stderr, rc 0 pour unittest comme pour
  `coverage xml`, rapport quand même poussé à Sonar. Mesuré : 1453 → 141
  statements sur un simple renommage, projet « sain » parce que plus analysé. Deux
  planchers à 1000 : le total, et le plus gros fichier mesuré — ce second attrape
  la sortie du module principal sans coder son chemin en dur.
- **Matrice `tests.yml`** (3.10 / 3.11 / 3.12) : `requires-python = ">=3.10"` est une
  promesse publique, et ce poste n'a que 3.12. La matrice installe le PAQUET (donc
  les bornes publiques) et non le lock, avec `fail-fast: false`.

### Gestion du baseline detect-secrets

```bash
# Régénérer le baseline (après ajout de nouveaux fichiers, par exemple)
git ls-files --cached -z | xargs -0 detect-secrets scan \
  --exclude-files '(README|CHANGELOG)-[a-z]{2}\.md' \
  --exclude-files 'traductions_.*' \
  --exclude-files 'tests/fixtures/.*' \
  --exclude-files 'venv/.*' \
  --exclude-files '\.secrets\.baseline' \
  > .secrets.baseline

# Auditer manuellement les findings (interactif)
detect-secrets audit .secrets.baseline
```

Findings actuels (tous faux positifs attendus) : 4 placeholders `votre-cle-api-*-par-defaut` dans `src/aipmt/translate.py` (OpenAI/Anthropic/Mistral/Google), 1 exemple dans README.md, 1 fixture dans tests/test_silent_failure.py. À auditer ponctuellement pour passer `is_secret: false`.

### Pré-requis lors du clone sur une autre machine

Les wrappers locaux (`scripts/run-*.sh`, `scripts/check-*.sh`) requièrent `./venv/bin/python`. Si le venv n'existe pas, ils renvoient un message explicite avec les commandes d'install. Sur CI ou autre poste de dev :

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

### Release / Tag workflow (2 phases)

Le script `release.sh` est conçu pour un workflow en **deux phases** : avant merge (prépare la PR sans tagger) et après merge (tag sur main + GitHub Release).

Quand l'utilisateur demande "release", "tag", "publie cette version" :

#### Phase 1 — Avant merge (depuis la branche feature)

```bash
./release.sh --auto
```

Effectue : pré-checks → tests `unittest` → régénération des 28 traductions (`--force`, Codex + `gpt-5.6-sol`, cf. règle en tête) → validation 28/28 → commit ciblé (jamais `git add -A`, `.gitignore` couvre `__pycache__/`, `venv/`, `.env` ; les fichiers suivis modifiés mais absents de la liste nominative sont **signalés** en fin d'ajout, jamais ajoutés — compléter la liste ou les ajouter à la main) → push branche → PR via `gh` (si auth OK).

**Pas de tag à ce stade.** Le tag est créé en phase 2 pour qu'il pointe sur le commit de merge dans `main` (pas sur la branche feature).

#### Phase 2 — Après merge PR

```bash
./release.sh --tag-only --yes
```

Effectue : checkout main → pull → vérifie cohérence CHANGELOG → tag annoté `v$VERSION` sur HEAD de main → push tag → GitHub Release via `gh` (si auth OK).

#### Variantes

- `--with-tag` : tag avant merge (workflow fast-forward / squash uniquement). À éviter si la PR génère un merge commit.
- `--local-only` : tout en local, pas de push (test/preview).
- `--dry-run` : simule sans rien toucher.
- `--no-pr` / `--no-github-release` / `--no-push` : opt-out fins.

#### Gestion gh token

Le script vérifie l'auth gh via `gh api user --jq .login` puis valide que le login retourné matche un format GitHub valide (`^[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?$`). Cette double check (exit code + format du login) évite les deux failure modes connus : exit code 0 avec payload d'erreur, et faux positifs si on matchait des substrings comme `"error"` qui peuvent apparaître légitimement dans le profil. Si le token est expiré :

- Warn + skip PR / GitHub Release
- Affiche les commandes manuelles
- Pour réauthentifier : `gh auth login`

#### Phase 3 — Publication sur PyPI (automatique)

La GitHub Release créée en phase 2 déclenche `.github/workflows/publish.yml`,
qui construit, vérifie et téléverse. **Rien à lancer à la main.**

Le workflow publie par **Trusted Publishing (OIDC)** : aucun jeton d'API n'est
stocké dans le dépôt. GitHub émet un jeton d'identité pour ce workflow de ce
dépôt, et PyPI le vérifie. Un secret volé n'existe pas s'il n'y a pas de secret
— et l'incident des PR Dependabot a déjà montré qu'un secret de dépôt n'arrive
pas partout où on croit.

Configuration unique, côté <https://pypi.org> → _Publishing_ → _Add a new
publisher_ :

```
owner       = jls42
repository  = ai-powered-markdown-translator
workflow    = publish.yml
environment = pypi          # et un second publisher avec `testpypi`
```

Les deux **environnements GitHub** `pypi` et `testpypi` doivent exister côté dépôt
(Settings → Environments, ou `gh api -X PUT repos/jls42/ai-powered-markdown-translator/environments/<nom>`) :
la revendication OIDC porte le nom d'environnement, et PyPI la compare à celui
déclaré. Un _pending publisher_ ne réserve pas le nom : jusqu'au premier
téléversement, n'importe qui peut le prendre — ne pas laisser traîner.
`workflow_dispatch` n'est possible que si `publish.yml` existe sur `main` : le
tir TestPyPI se fait donc APRÈS le merge, jamais depuis la branche.

Trois gardes, dans cet ordre, parce que **PyPI n'autorise jamais la
réutilisation d'un numéro de version** :

1. `twine check --strict` — un README que PyPI refuse de rendre est accepté à
   l'upload puis affiché en texte brut ; ça ne se voit qu'après coup, et après
   coup il est trop tard.
2. La version de `pyproject.toml` doit égaler le tag de la release.
3. `check-release-ready.sh` impose déjà que cette version égale celle du
   CHANGELOG, qui reste la source de vérité.

Pour un essai sans conséquence : `workflow_dispatch` avec `target = testpypi`.

**Piège local** : `python -m build` sans argument construit la sdist puis le
wheel _depuis la sdist_, ce qui exige d'extraire une archive tar. Le paquet
Ubuntu `python3.12 3.12.3-1ubuntu0.15` échoue là-dessus
(`AttributeError: module 'posixpath' has no attribute 'ALLOW_MISSING'`) : leur
rétroportage de sécurité a patché `tarfile` sans rétroporter la constante de
`posixpath`. C'est un bug de la distribution, pas du paquet — la CI n'est pas
touchée. En local, utiliser `python -m build --sdist --wheel`, qui construit
les deux depuis l'arbre source.

#### Régénération seule (sans release)

```bash
./regen_translations.sh --force   # réécrit les 28 traductions — Codex, gpt-5.6-sol, 0 € à l'usage
./regen_translations.sh           # skip celles qui existent déjà
```

Le script lance 4 jobs en parallèle sur Codex (défaut), 2 pour Grok et OpenCode,
10 seulement sur une API facturée en dérogation. En
relance manuelle d'un sous-ensemble — boucle directe sur `aipmt` — **5 en
parallèle sont acceptés sur OpenAI**, demande explicite du propriétaire : 2 fait
traîner un jeu de 14 CHANGELOG sur un quart d'heure.

## Project Overview

AI-powered Markdown translator that uses OpenAI, Mistral AI, Claude (Anthropic), Google Gemini and Grok (xAI) APIs — or the ChatGPT (Codex) and Grok subscription CLIs, with no per-use billing — or OpenCode, the open-source agent, routed to whatever provider the user configured in OpenCode (local model, free gateway, subscription or key) — to translate Markdown files while preserving formatting, code blocks, and front matter metadata.

## Commands

### Run a translation

```bash
# Activate virtual environment first
source venv/bin/activate

# Translate a single file
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'

# Translate a directory with OpenAI (default: gpt-5.6-terra)
aipmt --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Use economic models (--eco): gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'

# Translate with Mistral AI
aipmt --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Translate with Claude
aipmt --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Translate with Gemini
aipmt --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Force retranslation of existing files
aipmt --force --source_dir 'content/fr' --target_dir 'content/en'

# Add translation note at end of document
aipmt --add_translation_note --source_dir 'content/fr' --target_dir 'content/en'

# News mode: protect EN quotes, manage flags per language
aipmt --news --file 'article.md' --target_dir 'output/' --target_lang 'es'
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Architecture

**Installable package, single-module logic**: le paquet est `src/aipmt/`, et toute
la logique tient dans `src/aipmt/translate.py`. `__init__.py` n'expose que `main`
(cité par `[project.scripts] aipmt`), `__main__.py` permet `python -m aipmt`.

Le nom d'import est `aipmt` et **jamais** `translate` : le paquet PyPI `translate`
(v3.8.1, actif) installe un répertoire homonyme qui masquerait le module — le
point d'entrée casse alors sur `AttributeError` et `pip check` ne voit rien.

Contenu de `src/aipmt/translate.py` :

- **API clients**: OpenAI, Mistral, Claude (Anthropic), and Gemini are initialized based on CLI flags
- **Text segmentation**: `segment_text()` splits long documents at natural breakpoints (sentences, paragraphs, headers) respecting model token limits defined in `MODEL_TOKEN_LIMITS`
- **Code preservation**: Regex extracts fenced code blocks AND inline code (`` `...` ``) before translation, replaces with placeholders, restores after
- **News mode**: `--news` protects English quotes with `<NEWSQUOTE id="N"/>` XML self-closing tags, validates placeholder integrity before restoration, manages flag emojis per target language. (La forme legacy `#NEWSQUOTE\d+#` n'est plus émise mais reste détectée comme résidu.)
- **Directory traversal**: `translate_directory()` walks source directory, skips patterns in `EXCLUDE_PATTERNS`, checks for existing translations

**Output naming**:

- Default: `{base}-{target_lang}.md` (e.g., `README-en.md`)
- With `--include_model`: `{base}-{target_lang}-{model}.md`
- With `--keep_filename`: original filename (for destination folder workflows)

## Environment Variables

Les clés sont résolues en **trois couches**, de la plus prioritaire à la moindre :
variable d'environnement → `.env` du répertoire courant (ou d'un parent) →
`~/.config/aipmt/.env`. La priorité n'est pas codée : elle découle de
`override=False`, valeur par défaut de `load_dotenv`, chaque couche ne comblant
que ce que la précédente a laissé vide (`_load_configuration`).

La troisième couche existe parce qu'une CLI installée n'en avait aucune de
persistante. `find_dotenv` remonte jusqu'à la racine du système et trouvait donc
un `~/.env` **quand on travaillait sous son répertoire personnel**, mais rien
ailleurs — une couverture qui dépendait de l'endroit d'où l'on lançait la
commande. `_user_config_path()` suit `XDG_CONFIG_HOME` s'il est ABSOLU (la
spécification demande d'ignorer une valeur relative, sans quoi l'emplacement
redeviendrait fonction du répertoire courant) et `APPDATA` sous Windows.

Le trousseau système (`keyring`) a été écarté comme défaut : il échoue en
headless — serveur, conteneur, CI — c'est-à-dire le cas d'usage même d'une
traduction par lot. Un flag `--api-key` l'a été aussi : la clé atterrirait dans
l'historique du shell et serait visible dans `ps`.

Sans clé, `main()` n'affiche plus de trace d'appel. Le filet est **étroit à
dessein** : `except ValueError` sur la seule phase de configuration. Envelopper
toute l'exécution transformerait un vrai bug survenu pendant la traduction en
message rassurant, exactement le mode de défaillance que ce dépôt traque.

Required API keys (set one based on which API you use). Use `.env` file or export:

- `OPENAI_API_KEY`
- `MISTRAL_API_KEY`
- `ANTHROPIC_API_KEY`
- `GOOGLE_API_KEY` (for Gemini)
- `XAI_API_KEY` (for Grok via the xAI API)
- `GEMINI_API_KEY` accepted as an alternative to `GOOGLE_API_KEY`

Optional: `XAI_BASE_URL`, `CLAUDE_TIMEOUT` (default 900s), `CODEX_BIN`,
`CODEX_TIMEOUT`, `GROK_BIN`, `GROK_HOME`, `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX`, `OPENCODE_BIN`, `OPENCODE_TIMEOUT` (défaut 600 s),
`REGEN_PROVIDER`, `REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (dérogation, cf. règle en tête),
`REGEN_JOB_TIMEOUT` (défaut 600 s, plafond par job du regen),
`XDG_CONFIG_HOME` et `APPDATA` (emplacement de la configuration utilisateur).

## Recommended Usage

**Pour les traductions de CE dépôt, voir la règle en tête : Codex + `gpt-5.6-sol`,
jamais l'API.** Ce qui suit vaut pour un usage général de l'outil sur une clé API.

For batch translations (README, CHANGELOG, blog articles), use `--eco` mode:

```bash
aipmt --file README.md --target_dir . --source_lang fr --target_lang en --eco --add_translation_note
```

This uses faster/cheaper models (gpt-5.6-luna) which are sufficient for documentation translation.

### Provider Codex (`--use_codex`) — quota d'abonnement ChatGPT

Cinquième provider : pilote le binaire `codex` officiel en sous-processus au lieu
d'appeler une API. La traduction est décomptée du quota de l'abonnement ChatGPT,
pas facturée à l'usage.

```bash
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
./regen_translations.sh --force                         # Codex est le défaut : gpt-5.6-sol
REGEN_MODEL=gpt-5.6-luna ./regen_translations.sh --force   # éco, si le propriétaire le demande
```

Coût réel mesuré : régénérer les 28 traductions (70 turns) avec `gpt-5.6-sol` a
consommé **1 point de pourcentage** de la fenêtre de 5 h sur un plan Plus, et
rien sur la fenêtre hebdomadaire. La fourchette officielle « 10-100 messages »
est calibrée sur des sessions agentiques longues, pas sur des appels one-shot.

Points à connaître avant de toucher à ce code :

- **Le binaire vient de `CODEX_BIN`, du `PATH`, ou du package pip
  `openai-codex-cli-bin`** (officiel OpenAI, ~250 Mo, hors `requirements.txt`
  car le provider est optionnel). Pas besoin de npm.
- **Ne jamais lire ni écrire `~/.codex/auth.json`.** Le `refresh_token` est
  rotatif et à usage unique : toute manipulation externe casse la session
  `codex login` de l'utilisateur. L'auth est déléguée au CLI, point.
- **`codex exec` lit stdin même quand le prompt est en argv.** Sans
  `communicate(input=...)` (ou `</dev/null`), la commande attend jusqu'au
  timeout sans jamais appeler le modèle.
- **Le timeout doit tuer le groupe de process.** Le `codex` de npm est un shim
  Node ; le vrai binaire Rust est un petit-fils qui survit à
  `subprocess.run(timeout=)` et continue à consommer du quota. D'où
  `Popen(start_new_session=True)` + `os.killpg`.
- **Exit code 0 ne veut pas dire succès** : inspecter la sortie JSONL
  (`turn.failed`/`error`) et l'existence du fichier `-o`.
- **Les clés API sont retirées de l'env du sous-processus.** C'est la garantie
  que le mode abonnement ne bascule pas silencieusement en facturation à
  l'usage — verrouillé par `test_env_strips_api_keys`.
- **Allowlist de modèles côté serveur** : la famille `gpt-5.6-*` est commune au
  CLI et à l'API Platform, mais un compte ChatGPT n'y a pas forcément droit à
  tout. Un modèle refusé donne un 400 « model is not supported when using Codex
  with a ChatGPT account », sans validation locale préalable.
- **Quota** : 1 segment = 1 « message local » de la fenêtre 5 h. Sur Plus, Luna
  offre 250-2 000 msg/5 h contre 10-100 pour Sol → toujours `--eco` en batch.
  Quota lisible en direct via `codex app-server` (RPC `account/rateLimits/read`).
- **Refusé en CI** : l'auth par abonnement n'est pas prévue pour un runner
  partagé, et OpenAI déconseille ce workflow sur les dépôts publics.

### Providers Grok (`--use_grok` API / `--use_grok_cli` abonnement)

```bash
aipmt --use_grok --file README.md --target_dir . --target_lang pt      # clé XAI_API_KEY
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

- **Mode API** : endpoint compatible OpenAI (`https://api.x.ai/v1`), donc le
  client et `_call_openai` sont réutilisés tels quels ; seul le `base_url`
  change. Une seule adaptation a été nécessaire : xAI émet `finish_reason:
end_turn` là où OpenAI émet `stop`.
- **Mode CLI** : le CLI n'expose que `grok-4.6` et `grok-4.5` sur abonnement —
  `grok-4.3`, palier éco de l'API, n'y est pas disponible.
- **`exit 0` ne prouve rien** : non authentifié, refus ou dépassement de tours
  sortent tous en 0. Le contrat de sortie exige les quatre : code retour 0, pas
  de `{"type":"error"}` sur stdout, `stopReason == end_turn`, texte non vide.
- **Le prompt part par fichier** (`--prompt-file`) : le CLI ne lit pas stdin, et
  un segment en argv serait visible dans `ps`.
- **Confinement plus faible que Codex, et c'est assumé.** Le sandbox OS de Grok
  ne s'applique pas sur beaucoup de postes Linux (AppArmor + deny-list
  runtime-socket sur `/run/podman` en 0700), et un profil **intégré** qui échoue
  démarre **non confiné en silence**. On ne demande donc aucun profil par
  défaut, sans jamais retomber silencieusement : la protection repose sur
  `--deny` (catch-all `*` inclus), seule couche mesurée fail-closed. Opt-in
  strict via `GROK_TRANSLATE_SANDBOX`.
- **`--max-turns 1` est à proscrire** : le compteur est incrémenté après le tour
  d'outils, la sortie serait tronquée. Le plancher mesuré est 2.
- **Quota non mesurable** : pool hebdomadaire partagé avec Chat, Imagine et
  Voice, aucune commande ne l'expose. D'où `max_jobs=2` au regen.

### Provider OpenCode (`--use_opencode`) — routeur open source, `--model` obligatoire

```bash
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
```

Huitième chemin. OpenCode (MIT) n'est pas un fournisseur mais un routeur vers
ceux que l'utilisateur a configurés dans OpenCode lui-même : clé, abonnement
(GitHub Copilot, ChatGPT, SuperGrok — Claude Pro/Max est interdit par
Anthropic depuis la 1.3.0), passerelle Zen (modèles gratuits SANS compte) ou
modèle local (Ollama, LM Studio, llama.cpp). Tout ce qui suit a été **mesuré
sur opencode 1.18.27**, pas déduit de la doc :

- **`--model provider/modèle` est obligatoire**, `--eco` sans effet. Sans
  `--model`, OpenCode retombe sur `opencode/big-pickle`, modèle gratuit
  « stealth » dont les échanges peuvent servir à l'entraînement : ce choix ne
  se fait pas à la place de l'utilisateur. Le « / » du modèle est remplacé
  avant toute interpolation dans un nom de fichier (`_model_filename_label`),
  et la garde anti-traversée contrôle la valeur INTERPOLÉE, plus la valeur
  brute — `..` seul reste refusé.
- **Un `--agent` inconnu ne fait pas échouer `opencode run`** : avertissement
  sur stderr et repli silencieux sur l'agent de codage, outils actifs. Le
  contrat de sortie vérifie donc l'absence de ce message, en plus de : rc 0,
  aucun événement `error`, aucun `tool_use`, dernier `step_finish` en `stop`,
  texte non vide.
- **Le JSON d'erreur est opaque** (« Unexpected server error », `ref`) : la
  cause réelle (`ProviderModelNotFoundError`, `ProviderAuthError`…) n'est que
  dans les logs `--print-logs`, d'où `--print-logs --log-level ERROR` et la
  lecture du champ `error="…"` de stderr.
- **Confinement par config inline** (`OPENCODE_CONFIG_CONTENT`, dernière
  dans l'ordre de fusion) : agent `aipmt` avec `permission: {"*": "deny"}` —
  aucun outil n'est même proposé au modèle —, `share: disabled`, pas de
  `--auto`, `--pure`. Répertoire de travail jetable et vide.
- **Contexte injecté à l'insu de l'appelant** : sans
  `OPENCODE_DISABLE_CLAUDE_CODE`, `~/.claude/CLAUDE.md` entre dans chaque
  prompt (515 tokens d'entrée au lieu de 186) ; sans
  `OPENCODE_DISABLE_PROJECT_CONFIG`, l'`AGENTS.md` du cwd aussi (une consigne
  « finir par BANANA » y a été suivie). Le `~/.config/opencode/AGENTS.md`
  global reste injecté, aucun interrupteur ne l'écarte : documenté au lieu
  d'être contourné par un `XDG_CONFIG_HOME` détourné, qui masquerait aussi les
  fournisseurs de l'utilisateur.
- **`--title` évite un appel LLM** : sans lui, OpenCode génère un titre de
  session par un tour supplémentaire sur le `small_model`.
- **stdin est lu jusqu'à EOF** et concaténé après l'argument : le segment
  part par stdin, jamais par argv, et `communicate()` ferme toujours.
- **Secrets** : même filtrage par motif que Codex/Grok, à une exception
  nominative près, `OPENCODE_API_KEY` (clé d'OpenCode lui-même, Zen/Go).
- **Modèles gratuits Zen** : `mimo-v2.5-free` traduit ce README en une passe
  (49 s, structure identique) ; `big-pickle` met 40 s pour 200 mots et deux
  requêtes simultanées y restent sans réponse 5 minutes ; `nemotron-3.5-lightning-free`
  n'a rien répondu en 3 minutes. D'où `max_jobs=2` au regen.
- **Modèle local** : Ollama configure souvent 4 096 tokens de contexte, les
  segments font jusqu'à 16 000 caractères → `PARAMETER num_ctx 32768` dans un
  Modelfile. Un 7B (qwen2.5) a abîmé une clôture de bloc de code sur un
  fichier d'essai, là où le modèle de la passerelle a tout préservé.
- **Pas de refus en CI** : contrairement aux CLI d'abonnement, une clé API ou
  un modèle auto-hébergé sur un runner sont des usages légitimes.
- OpenCode écrit `~/.config/opencode/` (config vide, `node_modules` de son
  runtime de plugins) et journalise chaque session dans sa base SQLite
  `~/.local/share/opencode/opencode.db`.

## Key Constants

- `EXCLUDE_PATTERNS`: Paths containing these strings are skipped (`traductions_`, `venv`, `PRIVACY.md`)
- `MODEL_TOKEN_LIMITS`: Dict mapping model names to max token limits for segmentation

### Default Models (2026)

| Provider | Quality (default)                     | Economic (`--eco`)      |
| -------- | ------------------------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`                       | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`                     | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest`                | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`                    | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`                         | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`                            | `grok-4.3`              |
| Grok CLI | `grok-4.6`                            | `grok-4.5`              |
| OpenCode | `--model provider/modèle` obligatoire | idem                    |

### Model lifecycle — dates to watch (audited 2026-08-29)

| Échéance       | Impact                                                                                                                                           |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2026-10-15** | `claude-haiku-4-5` : date-plancher de retrait annoncée par Anthropic — la plus proche de tout le catalogue utilisé ici.                          |
| **2027-01-01** | Gemini 3.6/3.7 Flash : fin de la promo, prix **doublé** ($0.75/$3.75 → $1.50/$7.50).                                                             |
| —              | `claude-sonnet-5` : le tarif d'intro $2/$10 **est devenu** le prix standard ; la hausse prévue au 2026-09-01 n'aura pas lieu.                    |
| —              | Gemini 3.5 Pro **ne sortira jamais** (remplacé par Gemini 4) : `gemini-3.1-pro-preview` reste le seul Pro, et il est en preview depuis toujours. |

Audit du 2026-08-29 : les modèles par défaut des 7 providers sont les plus récents
disponibles chez chaque fournisseur. Aucune génération postérieure n'est GA
(GPT-5.7/6, Gemini 3.8/4, Sonnet 5.x, Haiku 5 = rumeurs ou pré-entraînement).

> **Recommendation for long-form translations** : `--use_gemini` (default = `gemini-3.7-flash`) preserves markdown structure reliably on non-Latin scripts (PL, JA, ZH, AR, HI), including `--news` mode where placeholder fidelity matters. Measured on this README translated to Japanese: structure identical to `gemini-3.1-pro-preview` (21 lists, 18 code fences, 13 HTML links, 13 images, all URLs preserved) at ~6x lower latency. OpenAI remains the default for backward compatibility.

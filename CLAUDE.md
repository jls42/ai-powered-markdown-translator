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

- **Un rapport d'agent de recherche est une PISTE, jamais une conclusion.**
  Le 2026-09-05, un rapport de workflow affirmait que `reasoning.enabled=false`
  désactivait le raisonnement de `z-ai/glm-5.3-flash` sur OpenRouter ; je l'ai
  répété à l'utilisateur comme un fait. Mesuré deux minutes plus tard : ce
  paramètre rend un **HTTP 400 « Reasoning is mandatory for this endpoint and
  cannot be disabled »**, comme `reasoning.max_tokens=0` et
  `reasoning_effort="none"`. Et le réglage le plus économe s'est révélé être
  l'absence de tout paramètre — 1 token de raisonnement, contre 165 avec
  `effort: minimal`. La règle qui en découle : **lire la doc officielle et
  mesurer AVANT d'annoncer, y compris ce qu'un sous-agent a rapporté.** Un
  rapport bien sourcé reste une affirmation à vérifier, pas une mesure.

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

### QUAND régénérer : une seule fois, juste avant le merge

**La régénération se lance quand le README et le CHANGELOG sont FIGÉS, pas à
chaque modification.** Mesuré le 2026-09-09 : huit campagnes lancées dans la
même journée pour 53 fichiers réellement conservés, parce que chaque retour de
revue changeait une phrase du CHANGELOG et que la régénération repartait
aussitôt. Sept campagnes sur huit sont parties à la poubelle, et le quota de la
fenêtre de cinq heures y est passé.

L'ordre correct, sur une PR qui touche la documentation :

1. le code, la revue et les correctifs, jusqu'à ce que plus aucun retour ne
   soit en attente ;
2. la dernière retouche du CHANGELOG et du README ;
3. **alors seulement** `./regen_translations.sh --force` ;
4. gate, commit des 28 traductions, push.

Pendant les étapes 1 et 2, la quatrième section du gate est rouge sur les
traductions divergentes : **c'est normal et il faut la laisser rouge**. Elle
signale un travail à faire à la fin, pas une urgence à traiter tout de suite.

**Une campagne couvre TOUTES les langues.** Quand le README ou le CHANGELOG
change, les quatorze sont refaites : en sauter une laisserait des traductions
sur deux versions différentes, et c'est justement ce que le compte 28/28 et le
contrôle de fraîcheur par contenu existent pour empêcher.

Ce qui se reprend, c'est une campagne INTERROMPUE, pas une sélection. Une
langue coupée en cours de traduction se refait depuis le début — il n'y a pas
de reprise partielle, l'outil traduit des fichiers entiers — puis les suivantes
s'enchaînent. Concrètement, après un quota épuisé à mi-parcours, relancer
nommément les langues qui n'ont pas abouti :

```bash
printf '%s\n' ja hi it ko nl pl pt ro sv zh | xargs -P 4 -I{} bash regen_one.sh {}
```

Celles déjà terminées portent le même contenu source : les refaire ne
changerait rien qu'une dépense.

**Le coût par campagne croît avec le CHANGELOG.** Il fait 111 000 caractères
avec l'entrée 1.15.0 (94 000 à la 1.14.1) et se découpe en huit segments —
compté par `segment_text` le 2026-09-26 —, soit huit tours Codex par langue et
112 tours pour les quatorze. La référence « 28 fichiers pour 70 tours, 1 point de la fenêtre »
notée plus bas date d'un fichier bien plus court : le coût par fichier a plus
que doublé depuis, et chaque release retraduit intégralement des entrées de
versions publiées il y a des mois. Archiver l'historique dans un
`CHANGELOG-archive.md` traduit une fois rendrait ce coût constant — décision du
propriétaire, non prise à sa place.

Ce que ça implique, et ce qui l'encode :

- `./regen_translations.sh --force` sans variable = Codex, `gpt-5.6-sol`, 4
  jobs. Plus aucune auto-détection de clé : une clé présente ne change rien.
  **Compter une heure** : mesuré le 2026-09-04 à 4 jobs, un README prend 3 à
  4 min et un CHANGELOG 10 à 14 min (effort de raisonnement `medium`, défaut
  de Sol hors `--eco`). Le plafond par job est à 1 800 s sur Codex : à 600 s,
  13 CHANGELOG sur 14 étaient tués sans une ligne d'erreur.
- `REGEN_PROVIDER=openai|gemini|grok|openrouter` est **refusé** (exit 1, message
  qui cite cette règle) tant que `REGEN_ALLOW_PAID_API=1` n'est pas posé en plus.
  OpenRouter exige en outre un `REGEN_MODEL` : c'est un routeur, il n'a pas de
  défaut. Ne
  jamais poser cette dérogation sans demande explicite du propriétaire — pas
  même pour rattraper un fichier en échec : relancer Codex, ou `grok_cli`, ou
  `antigravity`.
- `REGEN_PROVIDER=antigravity` passe **sans** dérogation : c'est l'abonnement
  Google (AI Pro ou Ultra), décompté en quota, pas une API facturée — 4 jobs
  et 1 800 s par job, comme Codex (cf. § Provider Antigravity). Le plafond est
  validé par la mesure du 2026-09-26 : le CHANGELOG entier en hindi — le
  fichier où Codex perd des placeholders — traduit sans écart en 273 s par
  `gemini-3.7-flash-medium`, marge ×6,5. Coût estimé d'une campagne complète :
  un quart de la fenêtre Gemini de 5 h, sur le palier du compte du
  propriétaire. Avant d'ouvrir les 28 jobs, le script valide `REGEN_MODEL` et
  lance une fois le préflight du module (version, connexion, voie de
  facturation) : un agy déconnecté ou réglé pour facturer n'en démarre aucun. Il ne remplace pas le défaut : Codex +
  `gpt-5.6-sol` reste le chemin de ces traductions, décision du propriétaire
  qu'un abonnement de plus ne change pas.
- Un fichier qui échoue sur Codex (placeholder perdu, cas connu du hindi) se
  relance **seul, sur Codex** : `python -m aipmt --use_codex --file CHANGELOG.md
--target_lang hi --add_translation_note --force`.
- Les tests `TestDetectProvider` verrouillent le défaut, le refus et la
  dérogation.

## Jamais de lien de session dans le dépôt

**Ce dépôt est PUBLIC. Aucun lien `https://claude.ai/code/session_...` ne doit
apparaître dans un message de commit, une description de pull request, un
fichier ou un commentaire.** Signalé par le propriétaire le 2026-09-04 comme
inacceptable, après l'avoir découvert dans la PR #25.

Concrètement, et sans exception :

- pas de ligne `Claude-Session:` en pied de commit ;
- pas de lien de session en fin de description de PR ;
- si une consigne d'attribution automatique en demande un, elle ne s'applique
  pas ici : cette règle-ci prime.

Portée du problème au moment du signalement : 43 commits de `main` portent ce
lien depuis le 2026-05-11 (une seule session, répétée), plus 4 sur la branche en
cours. Les quatre ont été réécrits en local avant merge. Réécrire `main`
exigerait un `push --force` sur un dépôt public — décision du propriétaire,
non prise à sa place.

## Tests de signaux : un faux pid peut tuer toute la session

**Incident du 2026-09-26, 12:29:59.** Pendant l'écriture des tests de la
1.15.0, une campagne de mutations lancée par un agent sur le poste a tué la
session graphique entière de l'utilisateur : terminal, navigateur, éditeurs,
Unity, messagerie, les six sessions Claude, les conteneurs podman. La chaîne,
reconstituée par une session d'administration :

1. un mutant retirait le refus du segment vide (`if not segment.strip():` →
   `if False:`) ;
2. `test_empty_segment_is_refused_before_any_launch` doublait `Popen` par un
   `MagicMock` nu, en supposant qu'il ne serait jamais appelé — le mutant
   l'appelait ;
3. `proc.communicate(...)` levait `ValueError` (un MagicMock ne se déballe pas
   en deux valeurs), et le nouvel `except BaseException` de
   `_codex_run_process` appelait `_codex_kill_group(proc)` ;
4. `MagicMock.__index__` vaut 1 : `os.getpgid(proc.pid)` rendait 1, et **sous
   Linux `killpg(1, sig)` vaut `kill(-1, sig)`** — SIGTERM puis SIGKILL vers
   TOUS les processus de l'utilisateur.

Ce qui l'empêche désormais, et ce qu'il faut respecter :

- `_codex_kill_group` ne vise un groupe que par `_agent_group` : pid entier
  STRICT (`type(pid) is int`, ni booléen ni double de test) supérieur à 1,
  `getpgid` qui rend CE pid — `start_new_session` fait de l'agent le chef de
  son groupe —, et jamais le groupe du processus courant. Sinon, seul le fils
  direct est visé. Verrouillé par `TestKillGroupNeverTargetsTheWholeSession`.
  C'est un filet, pas une permission.
- Un double de `Popen` ou de `run` qui ne doit pas servir porte
  `side_effect=_NE_DOIT_PAS_SERVIR` (une `AssertionError`) : un appel imprévu
  échoue avant de créer le moindre faux processus.
- Les faux processus portent `_PID_INEXISTANT` (2²² + 4242, au-delà de
  `pid_max`) : si un doublage de `getpgid` sautait, le vrai `getpgid`
  échouerait avant tout `killpg`. Les pid font le tour en quelques heures sur
  ce poste : 4242 peut exister.
- **Une campagne de mutations ne tourne jamais directement sur le poste** :
  dans un conteneur podman ou un namespace PID (par exemple
  `unshare --user --map-root-user --pid --fork --mount-proc …`), d'où un
  `kill(-1)` ne peut pas sortir. Un mutant exécute par construction des
  chemins que les tests supposent morts.
- Tout test qui peut atteindre `_codex_kill_group`, le chemin Ctrl-C /
  `SystemExit` de `_codex_run_process` ou le gestionnaire de
  `_kill_group_on_sigterm` double **à la fois** `os.getpgid` et `os.killpg`, ou
  remplace le module `os` de `base` entier.
- Jamais de `MagicMock` nu comme `pid` ; jamais de vrai `os.kill` ou
  `os.killpg` vers -1, 0, 1 ou un pid arbitraire (4242 peut exister).
- Un test à vrai signal ne vise qu'un sous-processus factice inoffensif lancé
  par le test lui-même (`_interrupt_a_real_agent`) ; un signal envoyé au
  lanceur de tests passe par un gestionnaire neutre posé en filet.
- Restructurer un bloc `assertRaises` ou `with patch(...)` — ce que demandent
  Sonar S5778 et Codacy — est exactement le geste dangereux : vérifier
  qu'aucun appel n'est sorti de la portée du `patch("os.killpg")` avant de
  relancer la suite.

## Claude Code Workflow

- **Commits**: Utiliser le skill `/helping-with-commits` pour tous les commits
- **Recherche web**: Utiliser l'agent `web-research-specialist:web-research-specialist` pour les recherches de documentation (évite de polluer le contexte principal)
- **Après chaque `git push`** (sur une PR, jamais main) : surveiller automatiquement les checks GitHub jusqu'à résolution.
  1. Attendre ~30-60s que SonarCloud / CodeQL terminent leur scan initial.
  2. `gh pr checks <num>` pour lire l'état (workflows actifs : `Analyze (python)` et `Analyze (actions)` (CodeQL), `SonarQube`, `SonarCloud Code Analysis`, `Python 3.10` / `3.11` / `3.12` (tests.yml), `Résolution des dépendances` et `Fermeture et tests du lock` (deps-check.yml), `Fusion automatique Dependabot` (sauté hors PR Dependabot), `Codacy Static Code Analysis`, `CodeFactor`). Sur `main`, un ruleset rend requis les trois `Python`, `Résolution des dépendances` et `Fermeture et tests du lock` (cf. § Fraîcheur des dépendances).
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

## Fraîcheur des dépendances — automatique, avec une alerte quand ça coince

**Le retard de dépendances est passé inaperçu pendant des mois.** Dependabot
tournait, mais sans `.github/dependabot.yml` GitHub n'active que les _security
updates_ : il ne propose une PR que pour une dépendance visée par une CVE. Il a
donc bien bumpé `urllib3` et `idna`, pendant qu'`openai` dérivait de 2.54 à 3.6,
`anthropic` de 0.125 à 1.2, et que `certifi` — le magasin de certificats racine
qui valide TLS pour tous les appels providers — accumulait deux ans de retard.

**Puis le retard s'est vu, mais à tort, et en exigeant une revue à chaque
fois.** Le 2026-09-16, le gate signalait trois versions publiées depuis moins
de deux jours, que Dependabot n'avait pas encore le droit de proposer : depuis
le 2026-07-14, il attend trois jours après chaque publication. Et chaque PR
Dependabot attendait une revue manuelle. **Décision du propriétaire, ce
jour-là** : les mineures et correctifs se fusionnent seuls, sans clé API en CI,
avec un passage quotidien.

Le dispositif, en cinq pièces :

1. **`.github/dependabot.yml`** : pip **quotidien**, `cooldown.default-days: 3`
   écrit en clair (c'est le défaut de GitHub, mais le délai du gate en dépend) ;
   github-actions hebdomadaire. Mineures et correctifs groupés en une PR ;
   **majeures séparées**.

2. **`.github/workflows/dependabot-auto-merge.yml`** lance
   `gh pr merge --auto --squash` sur les PR pip **mineures et correctives**
   seulement. Jamais les majeures, qui exigent un appel réel ; jamais les
   actions GitHub, qui s'exécutent à côté du jeton OIDC de publication. Un type
   de mise à jour illisible fait échouer le job sans rien fusionner.

3. **Un ruleset sur `main`** (« Checks requis ») exige `Python 3.10`,
   `Python 3.11`, `Python 3.12`, `Résolution des dépendances` et
   `Fermeture et tests du lock`, avec le rôle admin en bypass ; le réglage
   « Allow auto-merge » du dépôt est activé. **Le ruleset est indispensable** :
   sans check requis, `gh pr merge --auto` fusionne sur-le-champ, avant la fin
   de la CI (`isImmediatelyMergeable` dans le code de gh). Le workflow vérifie donc sa
   présence et **refuse de fusionner** s'il manque un de ces checks. Renommer un
   de ces jobs impose de mettre à jour le ruleset ET la liste `REQUIRED_CHECKS`
   du workflow — sinon toute PR attend un check qui ne viendra jamais.

4. **Job `Fermeture et tests du lock`** (`deps-check.yml`) : installe les seules
   dépendances directes de `pyproject.toml` avec le lock pour contrainte,
   compare `pip freeze` au fichier (trou, orphelin, divergence), puis lance les
   deux suites sur ces versions. `tests.yml` exerce le contrat public, jamais le
   lock : c'est ce job qui remplace la vérification faite à la main avant
   chaque bump.

5. **`./scripts/check-deps-fresh.sh`**, dans le gate et chaque jour en CI (job
   `Fraîcheur des dépendances`, `--strict`) :
   - un retard ne compte qu'au-delà de `GRACE_DAYS` = refroidissement (3) +
     cadence (1) + marge (1) = **5 jours** ; avant, la version est « en route »,
     sans avertissement. L'égalité avec `dependabot.yml` est vérifiée par un
     test (`scripts/tests/test_pypi_versions.py`) ;
   - retard de **majeure** → échec ; de mineure → avertissement dans le gate,
     **échec en CI** : l'échec d'un workflow planifié envoie un mail, une alerte
     plutôt qu'une découverte ;
   - PyPI injoignable → skip explicite en local, **fail-closed en CI**. Un
     contrôle qui ne s'est pas exécuté n'est pas un succès.

**Deux points que la doc ne tranche pas, à mesurer sur la première vraie PR
Dependabot :**

- **Le droit du `GITHUB_TOKEN` à activer l'auto-merge sur un run Dependabot.**
  La doc GitHub dit que la clé `permissions` l'élève ; le README de
  fetch-metadata dit le contraire. Un refus se lit en 403 sur l'étape « Activer
  la fusion automatique », et rien n'est fusionné.
- **Les workflows `on: push` après une fusion automatique.** Une action faite
  avec le `GITHUB_TOKEN` n'en déclenche aucun, et la doc ne dit pas si la
  fusion différée compte comme telle. C'est pourquoi `deps-check.yml` vérifie
  `main` chaque jour ; `gh run list --branch main --event push` tranche.

**Limite connue** : Dependabot ne modifie qu'une ligne du lock. Si une nouvelle
version exige de monter une dépendance transitive, le job de fermeture échoue,
la PR reste ouverte, et l'alerte part au-delà du délai. Correction à la main :
régénérer le lock (paragraphe suivant) et pousser sur la branche Dependabot. Si
ça devient fréquent, la parade est un lock compilé (`pip-compile` ou `uv.lock`),
que Dependabot régénère par l'outil lui-même au lieu d'éditer une ligne — à
mesurer avant d'y passer.

**Ce qu'on a lâché, en connaissance de cause** : personne ne lit plus les notes
de version d'une mineure avant sa fusion, et la CI n'appelle aucun provider.
Les utilisateurs du paquet reçoivent de toute façon les derniers SDK (bornes
`>=` de `pyproject.toml`) : le lock ne les a jamais protégés.

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
rien). Le job `Fermeture et tests du lock` fait exactement cette vérification
sur chaque PR et chaque jour sur `main`.

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

| Stage      | Hook                            | Rôle                                                                             |
| ---------- | ------------------------------- | -------------------------------------------------------------------------------- |
| pre-commit | shellcheck                      | Lint des `.sh` (release.sh, regen_translations.sh, scripts/)                     |
| pre-commit | ruff + ruff-format              | Lint + format Python (rapide, --fix automatique)                                 |
| pre-commit | prettier                        | Format JSON/YAML/MD (28 traductions exclues)                                     |
| pre-commit | pre-commit-hooks v5             | Trailing-whitespace, EOF, check-yaml/toml, large-files, merge-conflict, shebang  |
| pre-commit | detect-secrets                  | Détection de fuites d'API keys (6 providers à clé)                               |
| pre-commit | check-complexity (Lizard)       | CCN <= 12, scope `src/` + `scripts/`, existence des chemins et plancher vérifiés |
| pre-commit | check-split-purity (temporaire) | Le découpage de `translate.py` reste un déplacement pur, cf. § ci-dessous        |
| pre-push   | mypy (lax)                      | Type-checking des fonctions déjà annotées (durcissement progressif)              |
| pre-push   | check-security-sast (Opengrep)  | SAST sur src/ + scripts/ (graceful skip si binaire absent)                       |
| pre-push   | check-pip-audit                 | Audit deps (mode reporting initial, durcir après bump)                           |
| pre-push   | unittest                        | Tests `tests/` + `scripts/tests/`                                                |

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
2. **Phase 2** : annoter les fonctions critiques (`segment_text` dans `aipmt.segmentation`, `translate` et `translate_markdown_file` dans `aipmt.pipeline`). Bumper `check_untyped_defs = true`.
3. **Phase 3** : `disallow_untyped_defs = true` (mypy strict). Tout le code annoté.

### Lizard CCN — scope et fail-closed

Le seuil est 12 (futur 8). Tout le paquet `src/aipmt/` est **dans** le scope :
203 fonctions au découpage de la 1.13.0 (192 déplacées, six scindées pour tenir
sous la limite 8 de Codacy, cinq helpers nés de la revue), CCN moyen 3,4, zéro
dépassement.

Le scope vit dans un tableau `SCOPE` en tête de `scripts/check-complexity.sh`
— des RÉPERTOIRES (`src/`, `scripts/`), pas des fichiers, et un **plancher de
185 fonctions** lu par l'API Python de Lizard. Deux gardes, parce que chacune
seule a un angle mort : `lizard` ignore un chemin absent, sort en 0 et n'écrit
rien (mesuré sur une copie migrée — de 158 fonctions / 2247 nloc à 3 fonctions
/ 34 nloc, sortie de zéro octet) ; et l'existence d'un répertoire ne prouve pas
qu'il contient quelque chose. Le plancher se lit par l'API parce que
`--warnings_only` n'imprime AUCUNE ligne de synthèse quand tout est vert.

Le hook `files:` de `.pre-commit-config.yaml` doit suivre le même chemin : une
regex qui ne matche plus ne fait pas échouer pre-commit, elle fait **sauter** le
hook. La 7ᵉ section de `check-release-ready.sh` confronte les deux.

Pour vérifier les CCN actuels : `./venv/bin/python -m lizard -l python src/`.

### Deux gardes CI ajoutées pour la publication

- **Plancher de couverture** (`sonarcloud.yml`) : `coverage run --source=module_absent`
  n'échoue PAS — avertissement sur stderr, rc 0 pour unittest comme pour
  `coverage xml`, rapport quand même poussé à Sonar. Mesuré : 1453 → 141
  statements sur un simple renommage, projet « sain » parce que plus analysé. Trois
  planchers : le total ≥ 1000, la somme sous `src/aipmt/` ≥ 1550, et aucun module
  suivi du paquet à zéro exécution — un module sorti du `--source` disparaît du
  rapport, un module renommé n'y est plus mesuré.
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
  --exclude-files 'scripts/split-reference/.*' \
  > .secrets.baseline

# Auditer manuellement les findings (interactif)
detect-secrets audit .secrets.baseline
```

Findings actuels (tous faux positifs attendus) : 1 exemple dans README.md, 1 fixture dans `tests/test_codex_provider.py`, 1 dans `tests/test_grok_provider.py`. Les 6 placeholders `votre-cle-api-*-par-defaut` (une constante `DEFAULT_*_API_KEY` par provider à clé) ne sont plus dans la baseline : ils portent `# pragma: allowlist secret` sur leur ligne, parce que la baseline est indexée par FICHIER et qu'un placeholder déplacé dans un autre module y redevenait un « nouveau secret ». Le marqueur voyage avec la ligne. À auditer ponctuellement pour passer `is_secret: false`.

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

Le script lance 4 jobs en parallèle sur Codex (défaut) et Antigravity, 2 pour
Grok et OpenCode, 10 seulement sur une API facturée en dérogation. En
relance manuelle d'un sous-ensemble — boucle directe sur `aipmt` — **5 en
parallèle sont acceptés sur OpenAI**, demande explicite du propriétaire : 2 fait
traîner un jeu de 14 CHANGELOG sur un quart d'heure.

## Project Overview

AI-powered Markdown translator that uses OpenAI, Mistral AI, Claude (Anthropic), Google Gemini and Grok (xAI) APIs — or the ChatGPT (Codex), Grok and Google (Antigravity) subscription CLIs, with no per-use billing — or OpenCode, the open-source agent, routed to whatever provider the user configured in OpenCode (local model, free gateway, subscription or key) — or OpenRouter, a paid router to ~430 hosted models — to translate Markdown files while preserving formatting, code blocks, and front matter metadata.

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

**Paquet installable, découpé par responsabilité** : le paquet est `src/aipmt/`.
`__init__.py` importe `config` EN PREMIER (il charge `.env` à l'import, avant
que les providers lisent `os.getenv` au niveau module) puis expose `main` (cité
par `[project.scripts] aipmt`) ; `__main__.py` permet `python -m aipmt`.
L'exécution directe du fichier (`python src/aipmt/translate.py`) n'existe plus
depuis le découpage : les imports sont relatifs.

Le nom d'import est `aipmt` et **jamais** `translate` : le paquet PyPI `translate`
(v3.8.1, actif) installe un répertoire homonyme qui masquerait le module — le
point d'entrée casse alors sur `AttributeError` et `pip check` ne voit rien.

Modules, dans l'ordre topologique des imports : chaque flèche de dépendance va vers
un module plus HAUT dans le tableau, jamais l'inverse.

| Module                  | Rôle                                                                                                                          |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `config.py`             | Trois couches de clés (env, `.env`, `~/.config/aipmt/.env`), `_missing_key_message`                                           |
| `markdown.py`           | Lexique partagé : regex de lignes structurelles, liens, balises, placeholders ; plages d'écritures                            |
| `segmentation.py`       | `segment_text()`, `MODEL_TOKEN_LIMITS` (objet unique, OpenRouter y écrit la fenêtre lue au préflight)                         |
| `naming.py`             | `EXCLUDE_PATTERNS`, nom de sortie, traduction déjà présente, garde anti-traversée, écriture                                   |
| `notes.py`              | Note de traduction (constructeurs purs)                                                                                       |
| `guards.py`             | Gardes de sortie : langue détectée, extrait source verbatim, ratio, écriture cible ; graine langdetect                        |
| `placeholders.py`       | Protection/restauration des blocs de code, code inline, URL, ancres, labels — et leurs validations                            |
| `news.py`               | Mode `--news` : `<NEWSQUOTE id="N"/>`, drapeaux par langue, règles du prompt et validations                                   |
| `prompts.py`            | Instructions système : contrat Markdown, placeholders, ancres, addenda news et écritures non latines                          |
| `providers/base.py`     | Socle des CLI : sous-processus, secrets, back-off, erreurs, refus en CI                                                       |
| `providers/<nom>.py`    | Un module par provider : `openai`, `mistral`, `anthropic`, `gemini`, `codex`, `grok`, `antigravity`, `opencode`, `openrouter` |
| `providers/registry.py` | `_resolve_provider`, `_PROVIDER_LABELS`, `_dispatch_provider_call`, `_select_provider_client`, flags                          |
| `pipeline.py`           | `translate()`, `translate_markdown_file()`, `translate_directory()`, `_append_translation_note()`                             |
| `cli.py`                | argparse hors providers, validation des chemins, `main()`                                                                     |
| `translate.py`          | FAÇADE de compatibilité : les 64 noms publics de l'ancien module unique, par identité ; `__all__` à 9                         |

Deux règles qui découlent du découpage, verrouillées par `tests/test_facade_contract.py` :

- **Un patch de test vise le module qui CONSULTE le nom, jamais la façade.**
  `patch("aipmt.translate.translate_markdown_file")` réussissait sans rien
  intercepter (le nom consommé est celui de `aipmt.cli`) — et deux tests
  restaient verts sans leur patch. Détection par AST dans `tests/` et
  `scripts/tests/`, quotes simples et appels multilignes compris.
- **La façade ne ré-exporte ni nom privé, ni SDK, ni module stdlib.** Un patch
  posé au mauvais endroit lève `AttributeError` au lieu de ne plus mordre.

**Vérificateur de pureté (temporaire, retiré par la PR qui suit le découpage)** :
`scripts/check-split-purity.py`, hook pre-commit `check-split-purity` et étape
de `tests.yml`. Il compare le multiensemble des nœuds AST de premier niveau du
paquet à un snapshot versionné (`scripts/split-reference/package-6ae1505.json`,
304 nœuds au 2026-09-07) plus un manifeste cumulatif d'écarts déclarés
(`manifest.json` : docstrings de module, `__all__`, scissions demandées par
Codacy…) ; il vérifie l'emplacement
de chaque symbole, la survie verbatim des marqueurs `# nosec` / `# nosemgrep` /
`NOSONAR`, et refuse tout `.py` non suivi sous `src/aipmt/`, `tests/` ou
`scripts/tests/` (pre-commit ne voit que l'index : un module créé sans `git add`
passait tous les hooks). Le snapshot est dans le dépôt parce que la CI fait un
checkout superficiel. Neuf tests (`scripts/tests/test_check_split_purity.py`), dont sept
refus, prouvent qu'il mord.

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

**La couche projet ne fournit que des clés.** Le `.env` est cherché depuis le
répertoire courant et ses parents : un dépôt qu'on vient de cloner peut en
poser un. `_drop_project_routing`, appelée entre la couche projet et la couche
utilisateur, retire ce que le projet vient de poser parmi les variables qui
décident où part une requête ou quel programme s'exécute
(`_is_routing_variable`, casse ignorée) : tout nom en `_BASE_URL`, `_API_BASE`,
`_ENDPOINT` ou `_BIN` — un MOTIF, parce que douze variables de routage ont été
recensées dans les SDK installés, dont six pour le seul client Anthropic —,
plus `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`, `SSL_CERT_FILE`, `SSL_CERT_DIR`,
`REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`, `XDG_CONFIG_HOME`, `APPDATA` et
`GROK_HOME`. `_BIN` et `GROK_HOME` depuis la 1.15.0 : `CODEX_BIN`, `GROK_BIN`,
`OPENCODE_BIN`, `AGY_BIN` et `$GROK_HOME/bin/grok` désignent le binaire que la
traduction EXÉCUTE, avec les droits de l'utilisateur — posés par le `.env` d'un
dépôt cloné, ils faisaient lancer un fichier de ce dépôt. Toutes restent
acceptées de l'environnement exporté et de `~/.config/aipmt/.env`. Chaque refus
est dit sur stderr par son NOM seul : une valeur `https://${CLE}@hôte/` ferait
fuir la clé dans les journaux. La couche projet est en outre lue sans
interpolation (`interpolate=False`) : `NOM_ANODIN=${OPENAI_API_KEY}` y
recopiait la vraie clé sous un nom que le filtrage par motif des
sous-processus ne reconnaît pas. `regen_translations.sh` exporte le `.env` de
CE dépôt (`set -a`) avant d'appeler aipmt : ses variables y arrivent donc par
l'environnement, que le filtre ne touche pas — voulu, c'est le dépôt du
propriétaire, et le script lit lui-même `GROK_BIN` et `AGY_BIN` pour ses
contrôles préalables.

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
- `OPENROUTER_API_KEY` (for OpenRouter, `--use_openrouter`)

Optional: `XAI_BASE_URL`, `CLAUDE_TIMEOUT` (default 900s), `CODEX_BIN`,
`CODEX_TIMEOUT`, `GROK_BIN`, `GROK_HOME`, `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (défaut 900 s par segment,
démarrage compris), `OPENCODE_BIN`, `OPENCODE_TIMEOUT` (défaut 600 s),
`OPENROUTER_BASE_URL` (https exigé), `OPENROUTER_TIMEOUT` (défaut 900 s),
`OPENROUTER_PREFLIGHT_TIMEOUT` (défaut 30 s),
`REGEN_PROVIDER`, `REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (dérogation, cf. règle en tête),
`REGEN_JOB_TIMEOUT` (plafond par job du regen : 600 s, 1 800 s sur Codex et Antigravity),
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
  `Popen(start_new_session=True)` + `os.killpg`. La contrepartie de la session
  propre, pour les quatre CLI : l'agent ne reçoit ni le `SIGINT` d'un Ctrl-C ni
  le `SIGHUP` d'un terminal fermé. Vérifié par la revue du 2026-09-26 sur un
  faux binaire : il survivait à Python et finissait son tour sur le quota —
  `Popen.__exit__` n'attend que 0,25 s sur `KeyboardInterrupt`, et `SIGHUP`
  tuait Python sans exécuter aucun `finally`, laissant le répertoire privé
  d'Antigravity sur le disque, journal compris. D'où, dans
  `_codex_run_process`, `except BaseException: _codex_kill_group(proc); raise`
  (Ctrl-C et `SystemExit`), et `_kill_group_on_sigterm`, qui couvre `SIGTERM`
  ET `SIGHUP` — sortie en 128 + signal —, sauf un `SIGHUP` déjà ignoré
  (`SIG_IGN`, lancement par `nohup`, choix de l'utilisateur), et qui restaure
  `SIG_DFL` quand le gestionnaire précédent était `None` (posé hors de Python,
  impossible à reposer).
- **Exit code 0 ne veut pas dire succès** : inspecter la sortie JSONL
  (`turn.failed`/`error`) et l'existence du fichier `-o`.
- **Les clés API sont retirées de l'env du sous-processus.** C'est la garantie
  que le mode abonnement ne bascule pas silencieusement en facturation à
  l'usage — verrouillé par `test_env_strips_api_keys`.
- **Allowlist de modèles côté serveur** : la famille `gpt-5.6-*` est commune au
  CLI et à l'API Platform, mais un compte ChatGPT n'y a pas forcément droit à
  tout. Un modèle refusé donne un 400 « model is not supported when using Codex
  with a ChatGPT account », sans validation locale préalable. Mesuré sur ce
  compte le 2026-09-09 : `sol`, `terra` et `luna` répondent tous les trois par
  `codex exec -m`. Le défaut reste **`sol`** — décision du propriétaire, c'est
  le modèle qualité, et le seul mesuré à quatorze langues sans perte sur un
  document dense. `terra` s'obtient par `--model gpt-5.6-terra` si l'on veut,
  par l'abonnement, le modèle que l'API sert par défaut.
- **Quota** : un segment consomme grosso modo un « message » de la fenêtre 5 h,
  mais OpenAI ne publie AUCUNE équivalence comptable — l'assimilation vient
  d'une observation locale, pas d'un contrat. Sur Plus, les fourchettes
  annoncées sont 250-2 000 msg/5 h pour Luna contre 10-100 pour Sol, et ce sont
  des estimations variables, pas des plafonds → toujours `--eco` en batch.
  Quota lisible en direct via `codex app-server` (RPC `account/rateLimits/read`).
- **Refusé en CI** : l'auth par abonnement n'est pas prévue pour un runner
  partagé : l'auth passe par un fichier de session personnel, qu'OpenAI
  déconseille d'injecter sur un runner. La mise en garde vise ce dépôt de
  secret, pas le caractère public du dépôt de code.

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

### Provider Antigravity (`--use_antigravity`) — quota d'abonnement Google

```bash
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
aipmt --use_antigravity --eco --file README.md --target_dir . --target_lang ja
REGEN_PROVIDER=antigravity ./regen_translations.sh --force   # abonnement : sans dérogation
agy -p /usage --output-format json                            # quota restant, sans en consommer
```

Dixième chemin. Pilote `agy`, le CLI officiel d'Antigravity (binaire Go de
219 Mo, `~/.local/bin/agy`), en mode headless : la traduction est décomptée du
quota de l'abonnement Google AI Pro ou Ultra, pas facturée au token. **C'est le
seul chemin vers ce quota** : Gemini CLI ne sert plus les comptes Pro, Ultra ni
gratuits depuis le 2026-06-18
(<https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/>),
et le SDK Python Antigravity ne s'authentifie que par `GEMINI_API_KEY` ou
Vertex/ADC (<https://antigravity.google/docs/sdk/overview/>). Tout ce qui suit a
été **mesuré sur agy 1.2.11 le 2026-09-26**, pas déduit de la doc :

- **Binaire** : `AGY_BIN`, puis le `PATH`, puis `~/.local/bin/agy`, où il est
  installé sans que le `PATH` de la session le sache. **Jamais `antigravity`**,
  lanceur de l'IDE, qui ouvrirait l'éditeur. Plancher 1.2.11, vérifié au
  préflight : avant, un agent de projet pouvait rester introuvable en headless.
  Le chemin rendu est ABSOLU (`os.path.abspath`) : l'appel tourne avec pour
  `cwd` le répertoire privé, où un `AGY_BIN` ou une entrée de `PATH` relatifs
  étaient introuvables (reproduit par la revue sur un faux binaire). `AGY_BIN`
  n'est pas accepté d'un `.env` de projet (cf. § Environment Variables).
- **Auth** : le compte Google de l'abonnement, rangé dans le trousseau du
  système (Secret Service, par D-Bus), **jamais lu par aipmt** — lancer `agy`
  une fois et s'y connecter suffit. Une session déconnectée (« Authentication
  required », « authentication failed or timed out », « not logged in ») donne
  `ANTIGRAVITY_LOGIN_HINT` : relancer `agy` dans un terminal de la session
  graphique pour se connecter ; sans trousseau joignable, agy range son jeton
  dans un fichier de `~/.gemini`, que l'isolation masque volontairement.
- **Plateformes : `_antigravity_check_platform()`**, appelée par
  `_init_antigravity_client` juste après le refus en CI, avant la validation
  du modèle et tout lancement d'agy. Refus en fermé :
  - `os.name == "nt"` → `ANTIGRAVITY_UNSUPPORTED_WINDOWS`. Go y lit
    `USERPROFILE`, `APPDATA`, `LOCALAPPDATA` et `TEMP`, pas `HOME` ni `TMPDIR`
    (doc de Go et chaînes du binaire ; non mesuré sous Windows) : rien n'y
    isolerait l'appel des réglages ni de l'historique, et sans session propre
    agy garderait la console pour y demander un code (changelog 1.1.2).
  - Linux sans bus de session → `ANTIGRAVITY_NO_SESSION_BUS`.
    `_antigravity_session_bus_reachable` accepte un `DBUS_SESSION_BUS_ADDRESS`
    non vide, sinon l'existence de `$XDG_RUNTIME_DIR/bus`, à défaut de
    `/run/user/<uid>/bus` — la socket par défaut que la bibliothèque D-Bus
    essaie seule (mesuré : un `env -i` sans aucune des deux variables
    s'authentifie quand même). Sans bus — SSH, conteneur, serveur —, agy range
    son jeton dans un FICHIER sous le HOME réel (changelog 1.1.3 : « bypasses
    the keyring when no D-Bus session bus is present »), que le HOME privé
    masque : le préflight y attendrait 60 s un code, comme dans le cas mesuré
    « bus masqué », puis conseillerait une reconnexion qui ne résout rien. Non
    mesuré de bout en bout sur un hôte sans bus.
  - macOS passe : trousseau du système, pas de D-Bus. L'isolation par HOME n'y
    est pas mesurée ; la garde de facturation, qui lit la configuration
    effective, y tient.
  - **Piège CI** : les runners GitHub (Linux) n'ont pas de bus de session. Tout
    test qui appelle `_init_antigravity_client` neutralise
    `_antigravity_check_platform` (ou `_antigravity_session_bus_reachable`) par
    un patch sur `aipmt.providers.antigravity` — sinon vert sur ce poste, rouge
    en CI.
- **Invocation** : `agy --output-format json --agent aipmt
--disable-slash-commands --log-file <journal> --model <slug>`, segment sur
  stdin, **sans `-p`** : avec `-p`, agy ignore stdin ; sans lui, stdin n'étant
  pas un terminal, il passe en mode print et lit stdin jusqu'à EOF. Un stdin
  vide ouvre la TUI (rc 0, erreur non JSON sur stdout). `translate()` ne
  transmet plus aucun segment blanc, à aucun provider : il le rend tel quel
  (`not segment.strip()`). La revue l'avait reproduit — 16 001 caractères
  terminés par « \n\n\n » donnent un second segment « \n\n », dont le refus
  faisait échouer le FICHIER après consommation du quota du premier.
  `_antigravity_attempt` garde son refus en dernier filet.
- **Isolation par appel** : HOME, TMPDIR et répertoire de travail privés
  (`tempfile`, 0700), effacés après l'appel avec le journal, qui contient
  l'adresse du compte. agy s'authentifie quand même, par le trousseau, et le
  jeton rafraîchi y est réécrit pour toutes les sessions. Rien n'est hérité de
  l'utilisateur : ni son `settings.json` (`permissions.allow`, qui laissait
  l'agent par défaut lancer `ls` et `git` sans rien demander ;
  `allowNonWorkspaceAccess` ; `modelProvider`), ni ses `GEMINI.md` et
  `AGENTS.md` globaux, plugins, MCP, hooks et skills. Rien n'est écrit dans son
  historique : chaque appel y laissait une conversation d'environ 200 Ko, texte
  traduit compris, et la campagne de sondes y avait laissé ~95 conversations et
  évincé 17 entrées du cache `implicit/`, plafonné à 100. Parmi les variables
  de session, seules `XDG_RUNTIME_DIR` et `DBUS_SESSION_BUS_ADDRESS` passent la
  liste d'autorisation (cf. Environnement) : c'est par le bus de session qu'agy
  atteint le trousseau (bus masqué : 60 s d'attente d'un code de connexion,
  puis échec). `XDG_CONFIG_HOME` et ses sœurs n'y sont pas, si bien que tout
  chemin dérivé tombe dans le HOME privé. Vérifié de bout en bout : aucun
  fichier écrit dans `~/.gemini/antigravity-cli`.
- **Agent confiné**, écrit dans le répertoire jetable :
  `.agents/agents/aipmt.md`, frontmatter `name`, `description`, `tools: []`,
  `excludeDefaultComponents: true`, `inheritCustomizations: false`, puis
  `# aipmt`, puis les instructions système et `ANTIGRAVITY_AGENT_CONTRACT`.
  Environ 800 tokens d'entrée au lieu de 12 400 avec l'agent par défaut.
  `excludeDefaultComponents` seul laisse les hooks du workspace exécuter leurs
  commandes et injecter leur texte ; `inheritCustomizations: false` les coupe.
- **Repli silencieux, démontré** : un agent introuvable donne rc 0, status
  `SUCCESS` et l'agent de codage, 57 outils actifs. À « Le chat dort. », il a
  répondu « Chut, ne le réveillons pas ! 🐱💤 Que puis-je faire pour vous
  aujourd'hui ? ». Aucune trace sur stdout ni stderr : **seul le journal le
  dit**. La garde refuse si le journal annonce le repli, et exige le marqueur
  POSITIF du chargement de l'agent — l'agent par défaut écrit `agent=false`. Ce
  ne sont que des lignes de log, pas un contrat : une évolution du format fait
  refuser la traduction au lieu de retirer la garde en silence.
- **Marqueurs ancrés sur une ligne ENTIÈRE, au format glog mesuré**
  (`_GLOG_LINE` : sévérité `[IWEF]`, date `MMJJ`, heure à la microseconde, fil,
  `fichier:ligne]`, en `re.MULTILINE`, fin de ligne comprise). Lignes réelles
  d'agy 1.2.11, à reprendre telles quelles dans les fixtures :

  ```text
  I0926 10:36:51.895710       1 conversation_manager.go:512] Starting new conversation (agent=true)
  I0926 10:36:08.477937       1 conversation_manager.go:512] Starting new conversation (agent=false)
  W0926 10:30:43.128362       1 session.go:94] Agent "agent-inexistant" not found, falling back to default
  I0926 10:36:47.628476       1 server_oauth.go:196] applyAuthResult: email=compte@example.com, authMethod=consumer, quotaProject=
  ```

  Pourquoi l'ancrage : le binaire contient aussi
  `HandleUserInput called with text: %q`, qui recopierait le segment dans le
  journal. Non ancré, un document qui cite ces messages satisfaisait la garde
  positive à la place d'agy (vérifié par la revue sur un journal synthétique).
  `%q` échappe les sauts de ligne : l'écho reste sur une seule ligne, que
  l'ancrage écarte. Mesuré le 2026-09-26 : aucun des 78 journaux réels des
  sondes ne porte cette ligne au niveau de log par défaut. Validé contre le vrai
  agy après correctif : agent forcé inexistant → « agy est retombé en silence
  sur son agent de codage », réponse refusée.

- **Voie de facturation attestée par appel** : le journal doit porter la ligne
  glog `applyAuthResult: … authMethod=consumer` (l'abonnement), sinon refus
  avec `ANTIGRAVITY_LOGIN_HINT`. Et toute occurrence de `authMethod=` ou
  `auth_method=` — les deux graphies figurent dans le binaire — portant une
  autre valeur que `consumer`, OÙ QU'ELLE SOIT dans le journal, fait refuser :
  même hors d'une ligne glog, puisque refuser est le côté sûr. Conséquence
  pour la documentation : ne jamais écrire dans le README ni le CHANGELOG, que
  ce chemin peut traduire, un exemple de `authMethod=` suivi d'une autre
  valeur ; un agy qui recopierait l'entrée ferait refuser le segment.
- **Environnement : une liste d'AUTORISATION** (`_antigravity_env_base`),
  préflight compris, dans cet ordre :

  1. ne passent que `ANTIGRAVITY_KEPT_ENV_VARS` — `PATH`, `LANG`, `LANGUAGE`,
     `TZ`, `TERM`, `USER`, `LOGNAME`, `XDG_RUNTIME_DIR`,
     `DBUS_SESSION_BUS_ADDRESS`, `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`,
     `NO_PROXY` et leurs minuscules, `SSL_CERT_FILE`, `SSL_CERT_DIR` — et le
     préfixe `LC_`. C'est ce dont un `env -i` a prouvé qu'agy a besoin. Tout le
     reste disparaît, dont `HOME`, `TMPDIR`, `XDG_CONFIG_HOME` et ses sœurs,
     `DISPLAY` et `BROWSER` (aucun navigateur ne doit s'ouvrir depuis un job de
     traduction), `OPENAI_BASE_URL` et toute variable `AGY_`, `GOOGLE_`,
     `GEMINI_`… ;
  2. `_strip_secret_env` (motifs `API_KEY`, `_TOKEN`, `SECRET`, `PASSWORD`,
     `CREDENTIALS`) passe quand même : un nom de la liste qui porterait un de
     ces motifs resterait refusé ;
  3. `AGY_CLI_DISABLE_AUTO_UPDATE=true` (`ANTIGRAVITY_ENV_OVERRIDES`) ;
  4. `HOME` et `TMPDIR` privés, propres à l'appel (`_antigravity_env`).

  Pourquoi une autorisation et non un refus : la première version retirait des
  familles de préfixes (`AGY_`, `ANTIGRAVITY_`, `JETSKI_`, `CLOUD_CODE_`,
  `CLOUDSDK_`, `GOOGLE_`, `GEMINI_`), et la revue du 2026-09-26 a trouvé dans
  les chaînes du binaire des surcharges d'endpoint qui la traversaient :
  `AICODE_ENDPOINT_URL` et ses variantes `BAICODE_*`, `UNLEASH_URL` (drapeaux
  de fonctionnalité), `GCE_METADATA_HOST` — leur effet sur agy n'est pas
  mesuré, et c'est justement le problème d'une liste de refus. Mesuré en
  revanche : `AGY_GATEWAY_URL` envoie le prompt à une passerelle tierce,
  `AGY_ADC_AUTH` bascule sur un projet Google Cloud facturé, `CLOUD_CODE_URL`
  détourne l'endpoint authentifié vers n'importe quelle URL ; `GEMINI_API_KEY`
  ne bascule sur l'API que si `settings.json` porte `modelProvider="gemini"`,
  ce que le HOME neuf n'a pas. Les proxies et certificats transmis ne peuvent
  venir que de l'environnement exporté ou de `~/.config/aipmt/.env` : le filtre
  de la couche projet les écarte (cf. § Environment Variables).
  `AGY_CLI_DISABLE_AUTO_UPDATE` est posée APRÈS le filtrage : la valeur `1` est
  sans effet, `true` fait écrire « Auto-update disabled via environment
  variable » au journal. Sans elle, un HOME neuf lance à chaque appel le
  vérificateur de mise à jour, dans sa propre session, hors d'atteinte du
  `killpg`.

- **Préflight, zéro quota** (usage à zéro, mesuré) : `agy --version` ≥ 1.2.11,
  puis `agy -p /config --output-format json --log-file …` dans le même
  isolement. Refus si `useG1Credits` ne vaut pas `false` (crédits IA payants
  au-delà du quota), si `modelProvider` n'est pas vide (clé API), si `gcp`
  n'est pas nul (projet Google Cloud), ou si le journal n'atteste pas
  `authMethod=consumer`. **Un réglage ABSENT compte comme un problème, pour
  chacun des trois** (`_antigravity_billing_problems`, sentinelle
  `_ANTIGRAVITY_ABSENT` affichée « (absent de /config) », messages « doit
  valoir false / doit être vide / doit être nul ») : une version d'agy qui en
  renommerait un ne doit pas faire passer un contrôle qui n'a rien vérifié. La
  première version, par `.get()`, acceptait `{"useG1Credits": false}` seul, ou
  un `gcp` renommé en `gcpProject` (vérifié par la revue). Sur le compte du
  propriétaire le 2026-09-26 : `useG1Credits` false, 0 crédit restant,
  `modelProvider` vide, `gcp` null. `/config` prend de 2 à 11 s, sous un plafond de 120 s
  (`ANTIGRAVITY_CHECK_TIMEOUT`) : une session déconnectée y attend 60 s un code
  de connexion. Les deux commandes du préflight passent par
  `_antigravity_run_check`, un `subprocess.run` enveloppé dans
  `_kill_group_on_sigterm({})` : un `SIGTERM` ou un `SIGHUP` reçu pendant le
  contrôle lève `SystemExit`, `subprocess.run` tue agy, et le répertoire privé
  est effacé en remontant. Sans ce gestionnaire, Python mourait sans nettoyage
  et le répertoire restait sur le disque avec son journal (relevé par la
  revue ; le test appelle le gestionnaire au lieu d'envoyer un vrai signal au
  lanceur de tests).
- **Contrat de sortie**, dans cet ordre : rc 0 ET objet JSON ET
  `status == "SUCCESS"`, sinon échec — rc 3 = échec du modèle ou de l'agent,
  avec une ligne `AGY_ERROR: {json}` sur stderr (depuis la 1.2.6), lue par
  `json.JSONDecoder().raw_decode` juste après le marqueur
  (`_antigravity_agy_error_data` → dict ou None ; `_antigravity_agy_error` →
  chaîne compacte pour le message) : `raw_decode` s'arrête à la fin de l'objet,
  un code couleur ou un « } » écrits après ne s'y mêlent pas ; rc 1 = argument
  refusé, un modèle inconnu par exemple, sans repli silencieux depuis la 1.1.2 ;
  la réponse partielle que peut porter le JSON d'un échec n'est jamais lue.
  Puis la garde du journal (agent, `authMethod`). Puis
  `_antigravity_reject_non_answers` : refus si le JSON porte `denied_actions`,
  `command` ou `error`, ou si stderr contient « print timeout », « no output
  produced » ou « may be truncated ». Enfin `_antigravity_extract_answer` :
  `response` non vide, qui reprend la fin de ligne du SEGMENT —
  `text.rstrip("\n")`, plus `"\n"` si le segment finit par un saut de ligne.
  agy termine chaque réponse par un saut de ligne, que le segment en ait un ou
  non (mesuré sur les quatorze modèles) ; rendue telle quelle, la réponse
  insérait une ligne vide à la jonction d'une coupure en milieu de phrase et
  scindait le paragraphe — ou un tableau, sur une coupure dure (revue). Validé
  contre le vrai agy dans les deux sens.
- **Jamais `--print-timeout`** : à expiration, la sortie partielle sort en
  `SUCCESS`, rc 0. Le plafond est externe — `AGY_TIMEOUT`, 900 s par segment,
  démarrage compris, agy payant de 2 à 30 s d'appels réseau avant d'envoyer le
  message — et tue le groupe de processus, `SIGTERM` puis `SIGKILL`
  (`base._codex_run_process`, qui prend désormais un `cwd` : agy n'a pas
  d'option de répertoire de travail et y cherche l'agent). Ctrl-C et `SIGHUP`
  tuent aussi le groupe, puis le répertoire privé est effacé (cf. § Codex,
  « Le timeout doit tuer le groupe de process »).
- **Relance pilotée par `retryable`** :
  `_antigravity_is_rate_limited(text, agy_error)` reçoit le détail ET le dict
  d'`AGY_ERROR`, que le détail vienne ou non du champ `error` du JSON :

  - `AGY_ERROR` porte un booléen `retryable` → il décide SEUL. agy réessaie
    déjà lui-même, en processus, les 502, 503, 504 et les 429 par minute (son
    changelog), puis dit si l'échec restant l'est encore ;
  - sinon, aucune relance si le texte contient « exhausted » : chez Google,
    `RESOURCE_EXHAUSTED` porte le même 429 qu'une limite par minute, mais une
    fenêtre de 5 h épuisée ne se rendra pas en 90 s ;
  - sinon, relance sur « rate limit », « rate_limit », « too many requests » ou
    `429` comme nombre, cherchés dans le détail ET dans `AGY_ERROR`. « quota »
    seul n'est pas un marqueur.

  3 tentatives, 30 puis 60 s d'attente. La première version, sur sous-chaînes,
  relançait trois fois une fenêtre épuisée (`\b429\b` captait son code) et
  jamais un 503 `retryable: true` (revue, sur des lignes `AGY_ERROR`
  synthétiques : le format réel d'un échec n'a pas été mesuré).

- **Injection** : grâce à `--disable-slash-commands`, un segment qui commence
  par `!commande`, `@fichier` ou `/commande` n'est ni exécuté, ni résolu, ni
  développé. Sans lui, un segment « /help » s'exécutait à la place d'être
  traduit.
- **Modèles** : les identifiants d'`agy models`, effort compris —
  `gemini-3.8-flash-{high,medium,low}`, `gemini-3.7-flash-{high,medium,low}`,
  `gemini-3.6-flash-{high,medium,low}`, `gemini-3.1-pro-{high,low}`,
  `claude-sonnet-4-6`, `claude-opus-4-6-thinking`, `gpt-oss-120b-medium` ; tous
  figurent dans `MODEL_TOKEN_LIMITS`. Un nom de base seul (`gemini-3.7-flash`)
  est refusé par agy : aipmt le refuse avant l'appel et propose les suffixes
  qui existent — `-high` ou `-low` pour un Pro, `-medium` ou `-low` pour un
  Flash (la première version proposait `gemini-3.1-pro-medium`, qu'agy
  refuse). Défauts **fixés par la campagne du 2026-09-26** (ci-dessous), écrits
  en toutes lettres et jamais alias de `DEFAULT_MODEL_GEMINI` :
  `DEFAULT_MODEL_ANTIGRAVITY` = `gemini-3.7-flash-medium`,
  `ECO_MODEL_ANTIGRAVITY` = `gemini-3.7-flash-low`. `gemini-3.8-flash-medium`
  est écarté : le plus lent du pilote (103 à 128 s par README), et 79 % de sa
  sortie consacrés au raisonnement sur une sonde (3 658 tokens sur 4 606),
  décomptés au tarif de sortie. `--reasoning_effort` : sans effet,
  avertissement.
- **Quota** : deux groupes, Gemini et « Claude and GPT models », chacun avec une
  fenêtre de 5 h et une hebdomadaire, lisibles gratuitement par
  `agy -p /usage --output-format json` (`remaining_fraction`, `reset_time`).
  Texte officiel de `/usage` : le quota se décompte proportionnellement au coût
  des tokens, et la limite hebdomadaire dépend du palier de l'abonnement. Un
  appel Claude ou GPT-OSS a coûté environ 1 % de la fenêtre de 5 h, contre
  0,05 % en Flash : avertissement. Coût d'une traduction réelle : cf. la
  campagne ci-dessous, environ 12 points de la fenêtre de 5 h par million de
  caractères source en `gemini-3.7-flash-medium`.
- **Parallélisme** : 4 appels simultanés mesurés sans erreur, chacun dans son
  HOME, puis les 45 traductions de la campagne du 2026-09-26 à 4 en parallèle,
  sans un échec. D'où `max_jobs=4` au regen. Le plafond de 1 800 s par job,
  repris de Codex, est validé par la mesure : le CHANGELOG entier en hindi
  (HEAD 1.14.1, 94 080 caractères) traduit en 273 s, marge ×6,5.
- **Refusé en CI**, comme Codex et Grok CLI : l'auth par trousseau personnel
  n'est pas prévue pour un runner partagé. Repli proposé par le message :
  `--use_gemini` avec `GOOGLE_API_KEY` (`_CLI_PROVIDER_CI_FALLBACK`).
- **Câblage** : les CLI ont leur propre chaîne de dispatch
  (`_call_cli_provider` dans `registry`), une seule fonction dépassant ce que
  Codacy tolère ; un nom de CLI inconnu y lève au lieu de retomber sur un autre
  abonnement.
- **Bout en bout, 2026-09-26** : un guide Markdown (front matter, gras, lien à
  parenthèses, code en ligne, bloc de code indenté dans une liste, tableau,
  citation) traduit en anglais en 14 s préflight compris, structure identique,
  note de traduction ajoutée ; rien d'écrit dans `~/.gemini/antigravity-cli`.
  Revalidé après les correctifs de la revue, contre le vrai agy : le même guide
  en allemand, structure identique en 19 s, rien d'écrit dans `~/.gemini`.

**Campagne du 2026-09-26**, par `aipmt --use_antigravity` lui-même
(`--add_translation_note --force`, `--news` pour l'article), quatre traductions
en parallèle (`xargs -P 4`), chacune comparée à sa source par
`scripts/compare_structure.py`, quota lu par `agy -p /usage` avant et après
chaque phase. Sources : le README de HEAD, c'est-à-dire celui de la 1.14.0
(600 lignes, 39 075 caractères — pas la révision figée du 9 septembre des
autres lignes du tableau du README) ; le CHANGELOG de HEAD (1.14.1, 315 lignes, 94 080
caractères) ; l'article dense du tableau de compatibilité,
`ia-actualites-3-sep-2026.mdx` (589 lignes, 91 973 caractères).

| Phase    | Modèle                    | Document                          | Écrites · sans écart | Durée par langue                 |
| -------- | ------------------------- | --------------------------------- | -------------------- | -------------------------------- |
| Pilote   | `gemini-3.7-flash-medium` | README (ja, ar, hi)               | 3/3 · 3/3            | 72 à 84 s                        |
| Pilote   | `gemini-3.7-flash-low`    | README (ja, ar, hi)               | 3/3 · 3/3            | 42 à 56 s                        |
| Pilote   | `gemini-3.8-flash-low`    | README (ja, ar, hi)               | 3/3 · 3/3            | 54 à 58 s                        |
| Pilote   | `gemini-3.8-flash-medium` | README (ja, ar, hi)               | 3/3 · 3/3            | 103 à 128 s                      |
| Pilote   | `gemini-3.7-flash-medium` | CHANGELOG entier (hi)             | 1/1 · 1/1            | 273 s                            |
| Complète | `gemini-3.7-flash-medium` | article `--news`, 14 langues      | 14/14 · 14/14        | médiane 3 min 14 s (162 à 259 s) |
| Complète | `gemini-3.7-flash-medium` | README, 14 langues                | 14/14 · 13/14        | médiane 1 min 22 s (59 à 110 s)  |
| Complète | `gemini-3.7-flash-low`    | article `--news` (en, ja, ar, hi) | 4/4 · 4/4            | médiane 1 min 52 s (85 à 139 s)  |

- **Choix des défauts** : aucun écart de structure ne départage les quatre
  Flash du pilote. Le défaut qualité reste donc dans la famille qui a le plus
  de preuves — Gemini 3.7 Flash, 14/14 sur l'article par l'API —, à l'effort
  moyen ; l'éco est la même famille à l'effort bas, la plus rapide.
  `gemini-3.8-flash-medium` est écarté (cf. Modèles).
- **Le seul écart** : le README en coréen, « gras 36≠37 », un mot en gras de
  moins.
- **Mode `--news` en anglais** : les trois lignes `> 🇫🇷 _…_` absentes de la
  sortie, aucun 🇺🇸 ni 🇬🇧 inventé — l'échec qui a disqualifié Gemma 4 et
  Qwen 3.5 —, les trois citations anglaises verbatim. C'est le modèle qui les a
  retirées : aucun journal de la campagne ne porte la ligne « (cleanup) » que
  `_cleanup_source_flag_for_en` imprime quand il agit. Même résultat en
  `gemini-3.7-flash-low`.
- **Quota** (`remaining_fraction` du groupe Gemini) : la campagne complète —
  32 traductions, 2,20 millions de caractères source — a fait passer la
  fenêtre de 5 h de 88,87 % à 62,61 % (26,3 points) et la semaine de 91,05 % à
  86,67 % (4,4 points) ; le pilote — 13 traductions, 0,56 million de
  caractères — 6,2 et 1,0 point. Le groupe « Claude and GPT models » n'a pas
  bougé. Soit environ 12 points de la fenêtre de 5 h par million de
  caractères : un README de 40 000 caractères ≈ 0,5 point, une régénération
  des 28 traductions de ce dépôt ≈ un quart de la fenêtre. Valable pour le
  palier du compte du propriétaire : `/usage` dit que la limite hebdomadaire
  dépend du palier.

**Conditions d'utilisation, que le README dit sans les adoucir.** Les CGU
d'Antigravity (section 6, <https://antigravity.google/terms>) et la FAQ
(<https://antigravity.google/docs/faq/>) interdisent l'accès au service par un
logiciel tiers sur le login Antigravity — Claude Code, OpenClaw et OpenCode y
sont cités —, sous peine de suspension du compte. aipmt ne réutilise jamais le
jeton : il lance le binaire officiel en mode headless, que Google documente pour
les scripts et la CI (<https://antigravity.google/docs/cli/headless/>). Un
membre de Google a jugé « standard », sur le forum officiel le 2026-09-25, de
lancer `agy -p` depuis un script local pour son propre workflow (réponse non
contractuelle :
<https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829>).
Aucun texte ne tranche le cas d'un outil distribué : l'utilisateur engage son
compte.

**Données** : CGU section 5, les Interactions (prompts, réponses, métadonnées)
peuvent servir à améliorer les produits et le ML de Google et être relues par
des humains, sans distinction entre l'offre gratuite et Pro/Ultra. Le retrait
passe par le réglage `enableTelemetry`, dont l'effet exact n'est pas documenté.
D'où la consigne du README : documents publics (README, articles), jamais de
confidentiel. **Non mesuré** : si `enableTelemetry` vit dans `settings.json`,
comme les réglages que le HOME privé écarte, le retrait posé par l'utilisateur
ne suit pas dans les appels d'aipmt — `agy -p /config` lancé dans le même
isolement le trancherait.

### Provider OpenCode (`--use_opencode`) — routeur open source, `--model` obligatoire

```bash
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
REGEN_PROVIDER=openrouter REGEN_ALLOW_PAID_API=1 REGEN_MODEL=z-ai/glm-5.2 ./regen_translations.sh --force
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

**Poste local (installé et mesuré le 2026-09-04)** — RTX 3060 12 Go, 62 Go de RAM :

- Ollama 0.33.3, mis à jour par le script officiel (`curl -fsSL
https://ollama.com/install.sh | sh`, sudo sans mot de passe sur ce poste).
  Le script réécrit l'unité systemd mais pas le drop-in
  `/etc/systemd/system/ollama.service.d/override.conf`, qui place le magasin
  sur `OLLAMA_MODELS=/mnt/msi/ollama` (NVMe de 916 Go). Il ne touche pas aux
  modèles téléchargés.
- Modèles : `gemma4:12b` (7,6 Go, Apache 2.0, 140+ langues) et `gpt-oss:20b`
  (13 Go, Apache 2.0), plus leurs variantes `gemma4-12b-32k` et `gpt-oss-20b-32k`
  créées depuis `~/ollama/*.Modelfile` : sous 24 Go de VRAM, Ollama plafonne le
  contexte à 4 096 par défaut, et l'API OpenAI-compatible n'a aucun moyen de le
  régler par requête — d'où `PARAMETER num_ctx 32768`. `qwen3.5:9b` a été
  supprimé après le tableau ci-dessous.
- `~/.config/opencode/opencode.jsonc` déclare le fournisseur `ollama`
  (`@ai-sdk/openai-compatible`, `http://127.0.0.1:11434/v1`) avec, sur chaque
  modèle, `options.reasoningEffort: "none"`. Indispensable et mesuré : Ollama
  active la réflexion par défaut sur Qwen 3.5 et Gemma 4, un Modelfile ne
  peut pas la couper ; sans l'option, « Le chat dort sur le tapis » coûte 919
  tokens de raisonnement et 68 s, avec elle 9 tokens.
- Écartés après recherche : GLM 5.3 Flash et tous les Kimi n'existent sur
  Ollama qu'en `:cloud` (320 B et ~1 T de paramètres) ; Qwen 3.6/3.8 font 18 à
  23 Go ; `translategemma` est limité à 2 K tokens d'entrée.

**Matrice des modèles testés sur un article réel du blog** (589 lignes, 140
liens, 3 citations EN protégées, mode `--news`, cible `en`, même commande) — le
barème du propriétaire est « aussi bien que gpt-5.6-luna / gpt-5.4-mini », et
les modèles qui échouent sont supprimés du poste :

| Modèle                                   | Poids  | Répartition           | Durée         | Résultat                                                                                                                                                                                                                     | Verdict                                |
| ---------------------------------------- | ------ | --------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `opencode/mimo-v2.5-free` (Zen, hébergé) | —      | —                     | 4 min 26 s    | structure identique, 0 écart                                                                                                                                                                                                 | référence                              |
| `ollama/gemma4-12b-32k`                  | 7,6 Go | 100 % GPU, 10 Go VRAM | 10 min 10 s   | liens/URL/tableaux/gras/code identiques ; 1 ligne de citation inventée (🇺🇸 + paraphrase), 1 attribution dupliquée                                                                                                            | insuffisant, le plus proche — conservé |
| `ollama/qwen3.5-9b-32k`                  | 6,6 Go | 100 % GPU             | 8 min 18 s    | idem citation inventée + gras/code ajoutés, 1 segment repassé                                                                                                                                                                | échec — supprimé                       |
| `ollama/qwen3.6-35b-a3b-32k`             | 22 Go  | 65 % CPU / 35 % GPU   | échec à 3 min | segment 1 : placeholder perdu, puis à la reprise un JSON `{"error": true, "message": "Translation contract violation…"}` à la place de la traduction                                                                         | échec — supprimé                       |
| `ollama/gpt-oss-20b-32k`                 | 13 Go  | 37 % CPU / 63 % GPU   | 11 min 28 s   | **structure identique** ; a retiré lui-même la ligne 🇫🇷 sous 2 citations sur 3, la 3ᵉ laissée intacte a été enlevée par `_cleanup_source_flag_for_en` (garde du mode news depuis février 2026, commune à tous les providers) | conservé                               |

Le point de rupture n'est ni la traduction ni la structure, mais **une seule
consigne** : « pour une cible anglaise, supprimer la ligne `> 🇫🇷 _…_` sous
chaque citation ». Deux façons de la rater, très inégales :

- **Omettre** (gpt-oss) : la ligne source reste telle quelle, avec son drapeau
  d'origine. `_cleanup_source_flag_for_en` la retire, comme elle le fait depuis
  février 2026 pour tous les providers — ce n'est pas un rattrapage ajouté pour
  un modèle, c'est le contrat du mode news.
- **Inventer** (Gemma 12B, Qwen 3.5) : produire `> 🇺🇸 _paraphrase anglaise_`,
  un drapeau qui n'existe nulle part dans le contrat. Aucune garde ne l'attrape,
  et le contenu publié est faux.

**Règle du propriétaire, formulée le 2026-09-04 : pas de rattrapage.** Un modèle
qui ne tient pas la consigne n'est pas utilisé ; on n'ajoute pas de
post-traitement et on ne raccourcit pas les segments pour lui plaire. Le prompt
news est déjà explicite (`REMOVE the whole source-translation line

> 🇫🇷 _..._`) : il n'y a rien à clarifier sans dégrader le reste.

### Provider OpenRouter (`--use_openrouter`) — routeur payant, `--model` obligatoire

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

Neuvième chemin. OpenRouter est un routeur devant ~430 modèles hébergés par des
tiers, sur un crédit unique. Il donne accès aux modèles chinois ouverts (Kimi,
Qwen, DeepSeek, Z.ai) qu'aucun autre provider n'expose ici. Tout ce qui suit a
été **mesuré sur l'API le 2026-09-05**, pas lu dans la doc :

- **Un même slug est servi par des dizaines d'hébergeurs aux plafonds de sortie
  différents.** 33 pour `z-ai/glm-5.2`, 23 pour `glm-5.3-flash` — dont un à
  **2 048 tokens**. Sans épinglage, une traduction longue sur 23 partait
  tronquée, au hasard du routage. Le préflight lit
  `/api/v1/models/{slug}/endpoints`, écarte les plafonds sous 8 000 et les
  statuts négatifs, puis épingle le reste. `provider.only` **sans**
  `allow_fallbacks: false` n'est qu'une préférence : le routeur repart vers un
  hébergeur écarté. Les deux formes de `only` sont acceptées, nom nu
  (`deepinfra`) ou tag (`deepinfra/fp4`) ; on envoie le tag, plus précis.
- **Le raisonnement est facturé au tarif de sortie**, et il est actif par défaut
  sur beaucoup de modèles. Même requête sur `z-ai/glm-5.2`, réponse « OK » :
  **107 tokens de complétion contre 2** avec `reasoning: {"enabled": false}`.
  D'où la coupure par défaut. 288 des 431 modèles l'imposent
  (`reasoning.mandatory`) et répondent 400 « Reasoning is mandatory for this
  endpoint and cannot be disabled ». Pour ceux-là on demande le **plus bas
  effort déclaré** dans `supported_efforts` : ne rien envoyer laisse le défaut
  du catalogue, qui vaut `max` sur `glm-5.3-flash` et **tronque la sortie à
  32 768 tokens** avant la fin de la traduction. Monter l'enveloppe n'y change
  rien — l'effort en alloue un POURCENTAGE, que le raisonnement consomme en
  premier. Contre-épreuve : la langue qui échouait passe, structure identique.
- **`finish_reason=error` est une panne de l'hébergeur amont**, pas une fin
  anormale du modèle : `native_finish_reason` est nul, et deux langues ont été
  coupées à 750 s exactement. Message distinct, sinon on cherche le défaut dans
  le document.
- **Le catalogue n'a pas d'endpoint unitaire** : `/api/v1/models/{slug}` répond
  404, seul `/api/v1/models` (714 Ko) porte `reasoning` et `context_length`.
- **`finish_reason=length` avec un texte vide n'est pas une troncature** mais un
  budget mangé par le raisonnement (mesuré : 15 850 tokens de raisonnement pour
  148 utiles). Les deux cas appellent des gestes opposés, le message les
  distingue.
- **Le routeur répond 200 avec un corps ne portant qu'une erreur** quand
  l'hébergeur amont échoue : `choices[0]` levait un TypeError opaque, une garde
  lit `error` avant.
- **La fenêtre de contexte vient du préflight**, écrite dans
  `MODEL_TOKEN_LIMITS` : `DEFAULT_TOKEN_LIMIT` est faux pour 44 modèles du
  catalogue, dont deux plafonnés à 4 095 tokens.
- **Le slug est interpolé dans l'URL de préflight** : sa forme est validée
  avant tout réseau, et le segment `..` refusé — la regex namespacée commune
  aux deux routeurs accepte `a/b/..`.

### Provider Mistral (`--use_mistral`) — plafonds bas, propres à chaque modèle

Audit du 2026-09-17, **mesuré sur l'API**, pas lu dans la doc :

- **Résolution des alias**, publiée par `GET /v1/models` (champ `aliases`) :
  `mistral-large-latest` → `mistral-large-2512` (Large 3, décembre 2025),
  `mistral-medium-latest` → `mistral-medium-2604` (Medium 3.5),
  `mistral-small-latest` → `mistral-small-2603` (Small 4). Aucune date de retrait
  annoncée pour les trois.
- **Plafonds par modèle, sur ce compte** (en-têtes `x-ratelimit-*`) : Large 3
  **15 requêtes/min** (400 000 tokens) ; Small 4 100 requêtes et **100 000
  tokens/min** ; Medium 3.5 1 000 requêtes et 500 000 tokens. **Le 429 ne porte
  aucun `Retry-After`.** Le SDK ne réessayant rien par défaut,
  `MISTRAL_RETRY_CONFIG` (backoff de 2 à 60 s, abandon à 5 min) est ce qui
  empêche un 429 de perdre le fichier : 20 appels d'affilée sur Large 3 passent
  tous, le 16ᵉ après 33 s. Paralléliser au-delà du plafond n'accélère rien, ça
  fait attendre ; pour une campagne qui mesure des durées, 1 ou 2 traductions
  simultanées par modèle.
- **Raisonnement** : aucun des trois ne raisonne par défaut (18 tokens de sortie
  sur une phrase). Large 3 refuse `reasoning_effort` (HTTP 400) ; Small 4 et
  Medium 3.5 l'acceptent, et en `high` la réponse devient une liste de blocs
  `thinking` + `text` (5 189 tokens de sortie pour une phrase sur Medium 3.5).
  `_mistral_text` écarte ces blocs. `--reasoning_effort` n'est pas transmis à
  Mistral.
- **Prix** (doc officielle, entrée / sortie par million) : Large 3 $0.5 / $1.5,
  Medium 3.5 **$1.5 / $7.5**, Small 4 $0.15 / $0.6.

**Campagne du 2026-09-17** : 14 langues, l'article dense du tableau de
compatibilité (`ia-actualites-3-sep-2026.mdx`, dans le dépôt du blog) en
`--news`, et le README de la 1.14.0 — pas la révision figée du 9 septembre, qui
n'est plus sur le poste. Deux traductions simultanées par modèle et par
document ; les cinq tombées sur un 429 ont été relancées une à une.

| Modèle     | Article : écrites / sans écart | README : écrites / sans écart |
| ---------- | ------------------------------ | ----------------------------- |
| Large 3    | 10/14 · 6/14                   | 14/14 · 10/14                 |
| Medium 3.5 | 13/14 · 1/14                   | 14/14 · 6/14                  |
| Small 4    | 12/14 · 8/14                   | 13/14 · 8/14                  |

Medium 3.5 perd ou change de niveau des sous-titres `###` dans 9 langues sur
l'article, et coûte 3 fois Large 3 en entrée, 5 fois en sortie : **modèles par
défaut inchangés**, décision du 2026-09-17. Les refus de Large et Small sont
tous des gardes qui mordent — citation `NEWSQUOTE` restaurée deux fois, code en
ligne ou URL perdus —, aucun n'est dû à l'infrastructure.

## Key Constants

- `EXCLUDE_PATTERNS`: Paths containing these strings are skipped (`traductions_`, `venv`, `PRIVACY.md`)
- `MODEL_TOKEN_LIMITS`: Dict mapping model names to max token limits for segmentation

### Default Models (2026)

| Provider    | Quality (default)                     | Economic (`--eco`)      |
| ----------- | ------------------------------------- | ----------------------- |
| OpenAI      | `gpt-5.6-terra`                       | `gpt-5.6-luna`          |
| Claude      | `claude-sonnet-5`                     | `claude-haiku-4-5`      |
| Mistral     | `mistral-large-latest`                | `mistral-small-latest`  |
| Gemini      | `gemini-3.7-flash`                    | `gemini-3.1-flash-lite` |
| Codex       | `gpt-5.6-sol`                         | `gpt-5.6-luna`          |
| Grok API    | `grok-4.6`                            | `grok-4.3`              |
| Grok CLI    | `grok-4.6`                            | `grok-4.5`              |
| Antigravity | `gemini-3.7-flash-medium`             | `gemini-3.7-flash-low`  |
| OpenCode    | `--model provider/modèle` obligatoire | idem                    |

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

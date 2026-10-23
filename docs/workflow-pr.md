# Claude Code Workflow

- **Commits**: Utiliser le skill `/helping-with-commits` pour tous les commits
- **Recherche web**: Utiliser l'agent `web-research-specialist:web-research-specialist` pour les recherches de documentation (évite de polluer le contexte principal)
- **Après chaque `git push`** (sur une PR, jamais main) : surveiller automatiquement les checks GitHub jusqu'à résolution.
  1. Attendre ~30-60s que SonarCloud / CodeQL terminent leur scan initial.
  2. `gh pr checks <num>` pour lire l'état (workflows actifs : `Analyze (python)` et `Analyze (actions)` (CodeQL), `SonarQube`, `SonarCloud Code Analysis`, `Python 3.10` / `3.11` / `3.12` (tests.yml), `Résolution des dépendances` et `Fermeture et tests du lock` (deps-check.yml), `Fusion automatique Dependabot` (sauté hors PR Dependabot), `Codacy Static Code Analysis`, `CodeFactor`). Sur `main`, un ruleset rend requis les trois `Python`, `Résolution des dépendances` et `Fermeture et tests du lock` (cf. `docs/dependances.md`).
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
     - **Un test qui lance `git` retire toute variable `GIT_*` de son environnement.** Poussé depuis un worktree lié (`git worktree add`), git exporte `GIT_DIR` — le répertoire du worktree sous `.git/worktrees/` — aux hooks ; depuis le dépôt principal, aucun (mesuré le 2026-09-27). Le hook pre-push lance les tests, et le `git init` d'un test du vérificateur de pureté, dans un répertoire temporaire, a réinitialisé le VRAI dépôt : `core.bare = true` dans `.git/config`, puis `git status` refusait de tourner (« this operation must be run in a work tree »). Réparé par `git config --file .git/config core.bare false`, rien d'autre de touché. Ce test est parti avec le vérificateur (1.17.0) et plus aucun test ne lance `git` ; le prochain qui le fera passera à `git` un environnement sans `GIT_*`, comme le faisait son `_env_sans_git`.

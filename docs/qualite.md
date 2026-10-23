# Quality / pre-commit (workflow)

Le projet utilise le framework [`pre-commit`](https://pre-commit.com) avec un setup "type EurekAI complet" (cf. `.pre-commit-config.yaml`). Tous les hooks tournent localement avant chaque commit (rapides) ou avant chaque push (lourds, réseau).

## Bootstrap (une fois après clone)

```bash
source venv/bin/activate
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks pre-commit (rapides)
pre-commit install --hook-type pre-push  # hooks pre-push (mypy, SAST, audit, tests)
```

Le premier `pre-commit run --all-files` télécharge les environnements des hooks (~1-2 min, en cache après).

## Hooks actifs

| Stage      | Hook                           | Rôle                                                                             |
| ---------- | ------------------------------ | -------------------------------------------------------------------------------- |
| pre-commit | shellcheck                     | Lint des `.sh` (release.sh, regen_translations.sh, scripts/)                     |
| pre-commit | ruff + ruff-format             | Lint + format Python (rapide, --fix automatique)                                 |
| pre-commit | prettier                       | Format JSON/YAML/MD (28 traductions exclues)                                     |
| pre-commit | pre-commit-hooks v5            | Trailing-whitespace, EOF, check-yaml/toml, large-files, merge-conflict, shebang  |
| pre-commit | detect-secrets                 | Détection de fuites d'API keys (6 providers à clé)                               |
| pre-commit | check-complexity (Lizard)      | CCN <= 12, scope `src/` + `scripts/`, existence des chemins et plancher vérifiés |
| pre-push   | mypy (lax)                     | Type-checking des fonctions déjà annotées (durcissement progressif)              |
| pre-push   | check-security-sast (Opengrep) | SAST sur src/ + scripts/ (graceful skip si binaire absent)                       |
| pre-push   | check-pip-audit                | Audit deps (mode reporting initial, durcir après bump)                           |
| pre-push   | unittest                       | Tests `tests/` + `scripts/tests/`                                                |

## Lancer manuellement

```bash
pre-commit run --all-files                         # tous les hooks pre-commit
pre-commit run --hook-stage pre-push --all-files   # tous les hooks pre-push
pre-commit run ruff --all-files                    # un hook précis
```

## Échappatoires (à utiliser sciemment)

```bash
git commit --no-verify   # skip les hooks pre-commit
git push --no-verify     # skip les hooks pre-push
```

## Stratégie mypy progressive

mypy est en mode **Lax** au démarrage (`disallow_untyped_defs = false`, `check_untyped_defs = false`). Concrètement, mypy ne vérifie que les fonctions déjà annotées avec des types ; les autres sont ignorées silencieusement.

Trajectoire :

1. **Phase 1 (actuel)** : mypy lax, 0 effort initial. Filet de sécurité quand on ajoute des annotations.
2. **Phase 2** : annoter les fonctions critiques (`segment_text` dans `aipmt.segmentation`, `translate` et `translate_markdown_file` dans `aipmt.pipeline`). Bumper `check_untyped_defs = true`.
3. **Phase 3** : `disallow_untyped_defs = true` (mypy strict). Tout le code annoté.

## Lizard CCN — scope et fail-closed

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

## Deux gardes CI ajoutées pour la publication

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

## Gestion du baseline detect-secrets

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

Findings actuels (tous faux positifs attendus) : 1 exemple dans README.md, 1 fixture dans `tests/test_codex_provider.py`, 1 dans `tests/test_grok_provider.py`. Les 6 placeholders `votre-cle-api-*-par-defaut` (une constante `DEFAULT_*_API_KEY` par provider à clé) ne sont plus dans la baseline : ils portent `# pragma: allowlist secret` sur leur ligne, parce que la baseline est indexée par FICHIER et qu'un placeholder déplacé dans un autre module y redevenait un « nouveau secret ». Le marqueur voyage avec la ligne. À auditer ponctuellement pour passer `is_secret: false`.

## Pré-requis lors du clone sur une autre machine

Les wrappers locaux (`scripts/run-*.sh`, `scripts/check-*.sh`) requièrent `./venv/bin/python`. Si le venv n'existe pas, ils renvoient un message explicite avec les commandes d'install. Sur CI ou autre poste de dev :

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

# Release / Tag workflow (2 phases)

Le script `release.sh` est conçu pour un workflow en **deux phases** : avant merge (prépare la PR sans tagger) et après merge (tag sur main + GitHub Release).

Quand l'utilisateur demande "release", "tag", "publie cette version" :

## Phase 1 — Avant merge (depuis la branche feature)

```bash
./release.sh --auto
```

Effectue : pré-checks → tests `unittest` → régénération des 28 traductions (`--force`, Codex + `gpt-6.1-sol`, Antigravity si Codex n'est pas disponible, cf. `docs/traductions.md`) → validation 28/28 → commit ciblé (jamais `git add -A`, `.gitignore` couvre `__pycache__/`, `venv/`, `.env` ; les fichiers suivis modifiés mais absents de la liste nominative sont **signalés** en fin d'ajout, jamais ajoutés — compléter la liste ou les ajouter à la main) → push branche → PR via `gh` (si auth OK).

**Pas de tag à ce stade.** Le tag est créé en phase 2 pour qu'il pointe sur le commit de merge dans `main` (pas sur la branche feature).

## Phase 2 — Après merge PR

```bash
./release.sh --tag-only --yes
```

Effectue : checkout main → pull → vérifie cohérence CHANGELOG → tag annoté `v$VERSION` sur HEAD de main → push tag → GitHub Release via `gh` (si auth OK).

## Variantes

- `--with-tag` : tag avant merge (workflow fast-forward / squash uniquement). À éviter si la PR génère un merge commit.
- `--local-only` : tout en local, pas de push (test/preview).
- `--dry-run` : simule sans rien toucher.
- `--no-pr` / `--no-github-release` / `--no-push` : opt-out fins.

## Gestion gh token

Le script vérifie l'auth gh via `gh api user --jq .login` puis valide que le login retourné matche un format GitHub valide (`^[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?$`). Cette double check (exit code + format du login) évite les deux failure modes connus : exit code 0 avec payload d'erreur, et faux positifs si on matchait des substrings comme `"error"` qui peuvent apparaître légitimement dans le profil. Si le token est expiré :

- Warn + skip PR / GitHub Release
- Affiche les commandes manuelles
- Pour réauthentifier : `gh auth login`

## Phase 3 — Publication sur PyPI (automatique)

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

## Régénération seule (sans release)

```bash
./regen_translations.sh --force   # réécrit les 28 traductions — Codex, gpt-6.1-sol, 0 € à l'usage
./regen_translations.sh           # skip celles qui existent déjà
```

Le script lance 4 jobs en parallèle sur Codex (défaut), Antigravity et Claude
Code, 2 pour Grok et OpenCode, 10 seulement sur une API facturée en dérogation. En
relance manuelle d'un sous-ensemble — boucle directe sur `aipmt` — **5 en
parallèle sont acceptés sur OpenAI**, demande explicite du propriétaire : 2 fait
traîner un jeu de 14 CHANGELOG sur un quart d'heure.

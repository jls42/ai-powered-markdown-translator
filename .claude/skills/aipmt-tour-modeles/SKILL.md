---
name: aipmt-tour-modeles
description: "Fait le tour des modèles et des outils d'aipmt (dépôt ai-powered-markdown-translator) : ce que servent aujourd'hui les API OpenAI, Claude, Mistral, Gemini et xAI et les CLI Codex, Antigravity, Grok et OpenCode, les prix et les échéances, puis mesure des candidats, mise à jour des modèles par défaut, de la documentation et release. À utiliser dès que l'utilisateur parle de mettre à jour les modèles ou les providers d'aipmt, d'intégrer un modèle qui vient de sortir (« les Gemini 4 sont sortis », « passe à GPT-6 »), de faire le tour des fournisseurs, ou de vérifier qu'un modèle par défaut est toujours servi."
argument-hint: "[inventaire | <fournisseur> | <modèle à intégrer>]"
user-invocable: true
---

# Tour des modèles d'aipmt

Tout se lance depuis la racine du dépôt (alias `R`). Scripts de ce skill : `.claude/skills/aipmt-tour-modeles/scripts`
(alias `S`), à lancer avec `venv/bin/python`.

Écrit à partir du tour du 2026-11-15 (version 1.19.0), dont les résultats et la méthode sont dans
`R/docs/modeles.md`, section « Tour complet ». Lire cette section d'abord : elle donne le dernier état connu.
Les règles du dépôt (`R/CLAUDE.md`) priment sur ce fichier.

## Avant de commencer

- **Quota Codex et travaux planifiés.** Si un travail planifié traduit par Codex avec le `src/` de ce dépôt,
  travailler sur une branche et garder un arbre vert avant son heure de départ. Ne pas faire de banc sur Codex si
  sa fenêtre de 5 h doit servir à ce travail ou à la campagne : le 2026-11-15, deux README d'essai ont achevé une
  fenêtre déjà entamée.
- **Agents.** Consigne de travail : les sous-agents tournent sur Opus en effort `xhigh`, pas sur Fable, sauf
  tâche très complexe. L'outil Agent hérite du modèle de la session : pour déléguer, `claude -p --model opus --effort xhigh`.
  Le plus simple est de tout faire dans la session.
- **Argent.** Aucun appel payant vers un modèle dont le prix n'a pas été lu sur la page de l'éditeur. Les essais
  coûtent des centimes, mais l'annoncer avant de les lancer.

## 1. Inventaire gratuit

```bash
cd R && venv/bin/python S/catalogues.py      # code retour 1 si un défaut n'est plus servi
venv/bin/python S/prix.py                    # recoupement : prix de xAI et catalogue public d'OpenRouter
```

`catalogues.py` interroge les endpoints de liste des cinq API, `agy models`, le cache du catalogue Codex et
`grok models`, et dit pour chaque modèle par défaut et éco d'aipmt s'il est encore servi. C'est ce contrôle qui
aurait vu, avant un utilisateur, qu'Antigravity avait retiré `gemini-3.7-flash-low`.

Versions des CLI, à comparer puis à mettre à jour :

```bash
codex --version; npm view @openai/codex version        # npm i -g @openai/codex@latest
opencode --version; npm view opencode-ai version       # npm i -g opencode-ai@latest
grok --version; grok update --check                    # grok update
agy --version; agy changelog | head -40                # agy se met à jour seul
claude --version; npm view @anthropic-ai/claude-code version
cd R && ./scripts/check-deps-fresh.sh                  # SDK Python : Dependabot s'en charge
```

Lire le changelog d'un CLI avant de conclure qu'une mise à jour est neutre, puis valider par un appel réel
d'aipmt (`--use_codex`, `--use_antigravity`…) sur un petit fichier.

## 2. Prix, statuts, échéances : les pages officielles

Lire chaque page en demandant le chiffre **et** une courte citation mot pour mot : par l'outil WebFetch de la
session s'il existe, sinon par `claude -p --model opus --effort xhigh` (l'agent `web-fetch` de l'outil Agent hérite
du modèle de la session, donc de Fable). Un rapport d'agent est une piste : recouper par `prix.py` ou par une
seconde lecture.

- Google : `aistudio.google.com/docs/pricing`, `/docs/deprecations`, `/docs/changelog`, `/docs/models/<id>`
- OpenAI : `developers.openai.com/api/docs/pricing`, `/models`, `/deprecations`, `/changelog`
- xAI : `docs.x.ai/developers/models`, `/release-notes` ; ses prix se lisent aussi sur `GET /v1/language-models`
- Mistral : `docs.mistral.ai/getting-started/models/models_overview/`, `docs.mistral.ai/models/<id>`
- Anthropic : le skill `claude-api` (table des modèles) et `GET /v1/models`

Les quotas du niveau gratuit de Gemini ne sont que sur le tableau de bord d'AI Studio, derrière une connexion.

## 3. Vérifier que l'existant marche encore

Un appel réel de chaque défaut et de chaque éco sur un petit guide Markdown, avec le code de `src/`, puis
`scripts/compare_structure.py`. Coût négligeable, et c'est la seule preuve qu'un défaut traduit encore.

## 4. Mesurer un candidat

```bash
S/banc.sh hydrogen 2 --use_gemini --model gemini-4-hydrogen       # README en japonais, 2 essais
S/banc.sh ancien 1 --use_gemini --model gemini-3.8-flash          # la référence, à la même heure
venv/bin/python S/effort.py xai grok-4.7,grok-4.3                 # niveaux d'effort acceptés et leur coût
```

- L'épreuve qui départage est le **README entier dans une écriture non latine** (ja ou hi) : un fichier de vingt
  lignes prouve seulement que l'appel passe.
- Toujours une référence mesurée le même jour : un modèle plus récent n'est pas plus rapide (GPT-6.1 Terra, 190 s
  contre 116 s pour GPT-5.6 Terra).
- Un seul essai ne tranche pas un écart : rejouer quatre fois avant de dire qu'un modèle perd des codes ou du gras.
- **Vérifier que l'effort de raisonnement part bien.** `_QUALITY_REASONING_EFFORT` (`providers/openai.py`) liste
  les familles qui reçoivent `reasoning_effort` : une famille absente raisonne à son niveau par défaut, `--eco`
  compris. Une nouvelle famille (`gpt-7`, `grok-5`) doit y entrer, après la sonde `effort.py`.
- **Sur un abonnement, mesurer le quota, pas seulement la structure.** Lire le quota avant et après chaque
  traduction : `python3 S/quota_codex.py` pour Codex (gratuit, `usedPercent` entier de la fenêtre de 5 h et de la
  semaine), `agy -p /usage --output-format json` pour Antigravity (depuis `/tmp`, avec
  `AGY_CLI_DISABLE_AUTO_UPDATE=true`). Les familles n'ont ni le même coût ni le même groupe de quota. La 1.19.0
  a passé l'éco de Codex à `gpt-6-luna` sur une seule traduction réussie ; la comparaison complète du soir a
  montré 3 points de fenêtre par README contre 0 à 1 pour `gpt-5.6-luna`, et la 1.19.1 a dû y revenir.
- Ne pas changer un défaut sur une seule mesure faute de quota : attendre la fenêtre suivante.
- Dans une doc ou un CHANGELOG, écrire le nombre d'essais réellement faits dans la condition décrite.

## 5. Décider

- Même prix ou moins cher, structure au moins aussi bonne : adopter, et le dire.
- Prix en hausse, ou compromis net (lenteur, quota) : **une seule question** au mainteneur, avec les mesures.
- Règle générale du projet : la dernière version de chaque composant.
- Les modèles précédents restent acceptés par `--model` ; le dire dans le README.

## 6. Ce qu'un changement de défaut touche

1. La constante et son commentaire, avec la mesure et sa date : `R/src/aipmt/providers/<fournisseur>.py`.
2. `MODEL_TOKEN_LIMITS` (`R/src/aipmt/segmentation.py`) : tout nouvel identifiant, sinon avertissement
   « non listé ». Pour Antigravity, les identifiants portent l'effort (`-low`, `-medium`…), et le catalogue est
   recopié dans `_CATALOGUE_AGY` (`R/tests/test_antigravity_provider.py`).
3. Les tests qui figent un défaut (`grep -rn '"<ancien-id>"' R/tests`).
4. `R/docs/modeles.md` (tableau, échéances, section du tour), `R/docs/providers/<fournisseur>.md`,
   `R/docs/commandes.md`, les commentaires de `R/regen_translations.sh`.
5. `R/README.md` (tableau des défauts et paragraphes du fournisseur) et `R/CHANGELOG.md`, puis la version de
   `R/pyproject.toml`. Relire d'abord « README et CHANGELOG : ce qu'ils ne doivent jamais contenir ».
6. Recenser avant d'éditer : `git grep -c '<ancien-id>' -- ':!*-??.md'`.

## 7. Clore

- `./scripts/check-release-ready.sh --full` et coller le verdict.
- Campagne de traductions une seule fois, README et CHANGELOG figés : Codex, ou
  `REGEN_PROVIDER=antigravity ./regen_translations.sh --force` si Codex est épuisé ou réservé à un travail planifié.
  **Jamais d'API payante.** Puis `compare_structure` sur les 28 fichiers, et un `grep` du nouveau modèle dans
  chaque README traduit et du numéro de version dans chaque CHANGELOG traduit : le gate ne voit pas un README
  périmé dont la structure n'a pas bougé.
- Commits par le skill `helping-with-commits`, message montré et validé ; PR, checks, Sonar et Codacy ; un oui
  explicite avant la fusion, le tag et PyPI ; puis `pipx upgrade ai-powered-markdown-translator`.
- Mettre à jour la section « Tour complet » de `R/docs/modeles.md` et, si la méthode a changé, ce fichier.

## Pièges constatés

- **Un CLI qui hérite d'une clé change de catalogue.** `grok models` lancé avec `XAI_API_KEY` dans
  l'environnement liste le catalogue de l'API et réécrit `~/.grok/models_cache.json`. Or importer `aipmt` charge
  le `.env` dans l'environnement : `catalogues.py` copie donc l'environnement avant l'import. aipmt lui-même
  retire les clés avant de lancer un CLI.
- **`grok models` peut répondre « You are not authenticated. »** pendant un rafraîchissement de jeton, ou parce
  que la session a vraiment expiré (plus de `~/.grok/auth.json`) : la reconnexion par `grok login` est interactive, à faire par l'utilisateur.
- **Ne jamais lire ni écrire `~/.codex/auth.json`** ; `~/.codex/models_cache.json` et `quota_codex.py` suffisent.
- **Lire le quota Codex avant tout banc** : la fenêtre de 5 h en cours et son heure de remise à zéro disent si un
  travail planifié tombera dans la même fenêtre.
- **Commiter pendant une campagne** : les hooks pre-commit remisent les fichiers non indexés, donc les traductions
  en cours d'écriture. Passer les hooks à la main (`pre-commit run --files …`, mypy, tests), puis
  `git commit --no-verify` ; le commit des traductions, lui, passe par les hooks.
- **Un chemin `/tmp/…` écrit en dur dans un test** fait échouer Codacy et CodeFactor (« insecure usage of temp
  file »), même si le test ne crée rien : prendre un autre chemin d'exemple.
- **Le remplaçant « désigné » d'un modèle n'est pas forcément prêt** : `gemini-3.5-flash-lite` perd des codes en
  ligne là où `gemini-3.1-flash-lite` passe, à tous les niveaux de raisonnement mesurés.
- **xAI ne dit rien dans le message d'un 400** : le motif est dans le corps de l'erreur (`e.body`).
- **agy se met à jour pendant qu'on le mesure** s'il est lancé sans `AGY_CLI_DISABLE_AUTO_UPDATE=true`.
- **Une promesse de prix a une date.** Noter dans `docs/modeles.md` chaque « through … / starting … » lu sur une
  page de prix (Gemini 4 Argon et Carbon doublent le 2026-12-01, Gemini 3.8 Flash le 2027-01-01).
- **Les clés ne s'affichent jamais** ; au plus leurs quatre derniers caractères.

# CLAUDE.md

Guide de Claude Code pour ce dépôt. Ce fichier reste court : il porte les règles
qui valent pour toute session, et renvoie au détail rangé dans `docs/`, à lire
au moment où le sujet se présente (« Où lire quoi », en fin de fichier). Les
renvois sont des chemins en clair, jamais des imports `@` : rien n'est chargé
d'office.

## Projet

aipmt traduit des fichiers Markdown en préservant le formatage, les blocs de
code et le front matter. Trois familles de providers : les API facturées à
l'usage (OpenAI, Mistral, Claude, Gemini, Grok, OpenRouter), les CLI
d'abonnement sans facturation à l'usage (Codex, Grok CLI, Antigravity, Claude
Code), et OpenCode, routeur open source vers ce que l'utilisateur a configuré.

- Paquet `src/aipmt/`, commande `aipmt` (ou `python -m aipmt`). Le nom
  d'import est `aipmt` et **jamais** `translate` : le paquet PyPI homonyme
  masquerait le module.
- `config` est importé en premier : il charge `.env` avant que les providers
  lisent `os.getenv`. Les clés viennent de trois couches — environnement,
  `.env` du projet (clés seulement, variables de routage filtrées),
  `~/.config/aipmt/.env`.
- **Un patch de test vise le module qui CONSULTE le nom, jamais la façade
  `aipmt.translate`** — verrouillé par `tests/test_facade_contract.py`.

## Definition of Done — jamais « c'est bon » sans preuve

Avant de déclarer un travail terminé, fiable, prêt à commiter ou à releaser,
lancer le gate et coller son verdict :

```bash
./scripts/check-release-ready.sh          # 17 vérifications, ~45 s
./scripts/check-release-ready.sh --full   # 19 : + hooks pre-push et wheel neuf, ~3 min
```

Si une vérification échoue, le travail continue : on ne rend pas la main sur un
« presque ».

- **Mesurer plutôt que déduire.** Un `exit 0` ne prouve rien — ni pour
  `codex exec`, ni pour `grok`, ni pour `regen_translations.sh` : valider une
  condition métier. La fraîcheur d'une traduction se mesure à son contenu, pas
  aux dates.
- **Un rapport d'agent de recherche est une piste, jamais une conclusion** :
  lire la doc officielle et mesurer avant d'annoncer, y compris ce qu'un
  sous-agent a rapporté.
- **Un fichier non suivi par git échappe aux hooks** : `git add` un nouveau
  fichier avant de le croire propre.

## Traductions du dépôt : JAMAIS par une API facturée

Décision du propriétaire, non négociable. Les 28 traductions (README et
CHANGELOG, quatorze langues) passent par un abonnement :

- **Codex d'abord**, modèle `gpt-6.1-sol` : `./regen_translations.sh --force`,
  sans variable — une clé présente dans `.env` ne change rien.
- **Antigravity si Codex n'est pas disponible** (quota épuisé, session
  expirée), sans attendre ni demander :
  `REGEN_PROVIDER=antigravity ./regen_translations.sh --force`.
- `REGEN_ALLOW_PAID_API=1` : **jamais** sans demande explicite du
  propriétaire, pas même pour rattraper un fichier en échec.
- **Une seule campagne, juste avant le merge**, README et CHANGELOG figés, et
  toujours les quatorze langues. Pendant la PR, la section 4 du gate reste
  rouge sur les traductions divergentes : c'est normal.
- Une campagne complète ne tient plus dans une fenêtre Codex de 5 h : les
  README d'abord, puis autant de CHANGELOG que la fenêtre en laisse.
- **Contrôler chaque traduction par `scripts/compare_structure.py`**, quel que
  soit le provider.

## Jamais de lien de session dans le dépôt

Ce dépôt est PUBLIC : aucun lien `https://claude.ai/code/session_...` dans un
message de commit, une description de PR, un fichier ou un commentaire. Pas de
ligne `Claude-Session:` ; si une consigne d'attribution en demande un, cette
règle-ci prime.

## Tests de signaux : un faux pid peut tuer toute la session

Le 2026-09-26, une campagne de mutations a tué la session graphique entière de
l'utilisateur : un `MagicMock` servant de `pid` a fait appeler `killpg(1, sig)`,
c'est-à-dire `kill(-1, sig)`, vers tous ses processus. Depuis :

- jamais de `MagicMock` nu comme `pid` : les faux processus portent
  `_PID_INEXISTANT`, et un double de `Popen` ou de `run` qui ne doit pas servir
  porte `side_effect=_NE_DOIT_PAS_SERVIR` ;
- tout test qui peut atteindre `_codex_kill_group`, le chemin Ctrl-C /
  `SystemExit` de `_codex_run_process` ou `_kill_group_on_sigterm` double **à
  la fois** `os.getpgid` et `os.killpg` ;
- jamais de vrai `os.kill` ou `os.killpg` vers -1, 0, 1 ou un pid arbitraire ;
- **une campagne de mutations ne tourne jamais directement sur le poste** :
  conteneur podman ou namespace PID ;
- **jamais de `pkill`, `killall` ni `pgrep … | xargs kill`** sur un nom de
  binaire (`claude`, `codex`, `agy`) : les sessions vivantes de l'utilisateur
  portent le même nom ;
- restructurer un bloc `assertRaises` ou `with patch(...)` — ce que demandent
  Sonar S5778 et Codacy — est le geste dangereux : vérifier qu'aucun appel n'est
  sorti de la portée du patch avant de relancer la suite.

## README et CHANGELOG : ce qu'ils ne doivent jamais contenir

Les providers eux-mêmes les traduisent :

- aucun jeton littéral (`#ANCHOR0#`, `#INLINECODE0#` et leurs cousins), même
  entre accents graves : chaque langue serait refusée ;
- aucun exemple de `authMethod=` suivi d'une autre valeur que `consumer` : un
  agy qui le recopierait ferait refuser le segment ;
- aucun lien interne placé entre parenthèses ;
- aucun numéro de version de dépendance dans le CHANGELOG : dire quels paquets
  ont bougé, pas jusqu'où — le lock du tag fait foi.

## Workflow

- **Commits** : skill `/helping-with-commits`, pour tous les commits.
- **Recherche de documentation** : agent
  `web-research-specialist:web-research-specialist`.
- **Après chaque `git push` sur une PR** (jamais `main`) : surveiller les
  checks jusqu'à résolution (`gh pr checks <num>`), reproduire localement un
  échec avant de le corriger, puis, même tout vert, interroger l'API Sonar des
  issues **et** celle des hotspots, et l'API Codacy : un check `pass` ne les
  reflète pas.
- **Avant de fusionner** : `git log HEAD..origin/main` ; si `main` a bougé, le
  fusionner dans la branche et pousser, pour que la CI teste l'état qui sera
  réellement fusionné.
- **Une majeure de SDK se valide par un appel réel**, provider par provider.
  Dependabot fusionne seul les mineures et correctifs pip, jamais les majeures.
- **Release en deux phases** : `./release.sh --auto` avant le merge (sans tag),
  `./release.sh --tag-only --yes` après ; la GitHub Release publie sur PyPI.

## Interdits propres à un provider

- **Codex** : ne jamais lire ni écrire `~/.codex/auth.json` — son jeton est
  rotatif et à usage unique, toute manipulation casse la session de
  l'utilisateur.
- **Claude Code** : un arrêt par les garde-fous d'Opus est un signalement sur
  le compte du propriétaire ; ne jamais rejouer le contenu sur Opus pour
  « vérifier ».
- **Antigravity** : jamais `--print-timeout` (la sortie partielle sort en
  `SUCCESS`). **Grok CLI** : jamais `--max-turns 1` (sortie tronquée).

## Commandes

```bash
source venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
pre-commit install && pre-commit install --hook-type pre-push
aipmt --file README.md --target_dir . --source_lang fr --target_lang en --eco --add_translation_note
python -m unittest discover tests/ && python -m unittest discover scripts/tests/
pre-commit run --all-files && pre-commit run --hook-stage pre-push --all-files
```

## Où lire quoi

Chaque fichier reprend une section de l'ancien CLAUDE.md, mesures et historique
compris ; seuls les renvois d'une section à l'autre y sont devenus des chemins.

| Avant de…                                                                       | Lire                            |
| ------------------------------------------------------------------------------- | ------------------------------- |
| conclure ou releaser : ce que vérifie le gate, les leçons qui l'ont fait naître | `docs/definition-of-done.md`    |
| lancer, reprendre ou chiffrer une campagne de traductions                       | `docs/traductions.md`           |
| réécrire l'historique pour un lien de session                                   | `docs/liens-de-session.md`      |
| écrire un test qui double `Popen`, `getpgid` ou `killpg`                        | `docs/tests-de-signaux.md`      |
| toucher aux jetons d'ancre ou aux liens internes du README                      | `docs/liens-internes.md`        |
| pousser, corriger un check, écrire un test qui lance `git`                      | `docs/workflow-pr.md`           |
| monter une dépendance, régénérer le lock, renommer un job de CI requis          | `docs/dependances.md`           |
| modifier un hook, mypy, le gate Lizard ou la baseline detect-secrets            | `docs/qualite.md`               |
| releaser ou publier sur PyPI                                                    | `docs/release.md`               |
| chercher une commande d'usage                                                   | `docs/commandes.md`             |
| déplacer du code ou ajouter un module au paquet                                 | `docs/architecture.md`          |
| ajouter une variable d'environnement ou toucher à `config.py`                   | `docs/environnement.md`         |
| changer ou citer un modèle par défaut, suivre une échéance de modèle            | `docs/modeles.md`               |
| toucher à Codex ou diagnostiquer un 429 de campagne                             | `docs/providers/codex.md`       |
| toucher à Grok, par l'API ou par le CLI                                         | `docs/providers/grok.md`        |
| toucher à Antigravity (isolation, facturation, CGU)                             | `docs/providers/antigravity.md` |
| toucher à Claude Code (contrat mesuré, garde-fous, quota)                       | `docs/providers/claude-code.md` |
| toucher à OpenCode ou évaluer un modèle local (règle « pas de rattrapage »)     | `docs/providers/opencode.md`    |
| toucher à OpenRouter                                                            | `docs/providers/openrouter.md`  |
| toucher à Mistral                                                               | `docs/providers/mistral.md`     |
| toucher à la requête Claude ou monter le SDK `anthropic` d'une majeure          | `docs/providers/claude.md`      |

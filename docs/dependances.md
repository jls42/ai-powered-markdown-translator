# Fraîcheur des dépendances — automatique, avec une alerte quand ça coince

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

1. **`.github/dependabot.yml`** : pip **tous les jours, week-end compris**
   (`interval: cron`, `cronjob: "0 6 * * *"`), `cooldown.default-days: 3`
   écrit en clair (c'est le défaut de GitHub, mais le délai du gate en dépend) ;
   github-actions hebdomadaire. Mineures et correctifs groupés en une PR ;
   **majeures séparées**. **Jamais `interval: daily`** : il ne passe que du
   lundi au vendredi (référence des options de Dependabot ; mesuré : 55
   passages depuis avril, aucun un samedi, et les seuls du dimanche le jour de
   l'ajout du fichier). Une version sortie du refroidissement un vendredi après
   le passage du matin attendait le lundi : le 2026-10-18, google-genai 2.30.1
   n'a échappé à l'alerte du dimanche qu'à 1 h 35 près, parce que le contrôle
   planifié avait démarré à 12 h 36 UTC — 9 des 14 précédents avaient démarré
   plus tard.

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
     test (`scripts/tests/test_pypi_versions.py`), qui compte 1 jour pour un
     cron quotidien et 3 pour `daily` — revenir à `daily` sans porter le délai
     à 7 jours le fait échouer ;
   - retard de **majeure** → échec ; de mineure → avertissement dans le gate,
     **échec en CI** : l'échec d'un workflow planifié envoie un mail, une alerte
     plutôt qu'une découverte ;
   - PyPI injoignable → skip explicite en local, **fail-closed en CI**. Un
     contrôle qui ne s'est pas exécuté n'est pas un succès.

**Les deux points que la doc ne tranchait pas sont mesurés (2026-10-18) :**

- **Le `GITHUB_TOKEN` active bien l'auto-merge sur un run Dependabot.** La doc
  GitHub disait que la clé `permissions` l'élève, le README de fetch-metadata
  le contraire : #45, #47, #52, #53, #55, #56 et #58 à #61 ont été fusionnées
  par `github-actions`, sans un 403.
- **Une fusion automatique ne déclenche aucun workflow `on: push`.** Sur les
  commits fusionnés seuls (`81de4f4`, `b542df3`, `f75419f`, `a36040f`,
  `cc78092`), n'ont tourné que des workflows étrangers au push — CodeQL
  (configuration par défaut), le graphe de dépendances, les passages de
  Dependabot et les jobs planifiés —, ni `Tests`, ni `SonarCloud`, ni
  `Dependencies` en `push` ; une fusion manuelle les déclenche (`87c330c`). `main` reste vérifié chaque jour par `deps-check.yml`
  (fermeture et tests du lock) ; SonarCloud ne l'analyse qu'à la fusion
  manuelle suivante.

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

**`main` bouge pendant qu'une PR attend, et sa CI ne le voit pas.** Les checks
d'une PR tournent à chaque push, jamais quand `main` avance : le 2026-10-19,
#63 (`anthropic` 1.15.0, `openai` 3.31.0, `google-genai` 2.31.0) a été fusionnée
seule après le dernier push de la PR de la 1.17.0, restée « CLEAN » sur un
`main` périmé, et dont l'entrée du CHANGELOG citait les versions d'avant. La
corriger a coûté la régénération des quatorze CHANGELOG. D'où deux règles :

- **jamais de numéro de version de dépendance dans le CHANGELOG** — dire
  quels paquets ont bougé, pas jusqu'où : le lock du tag fait foi ;
- **avant de fusionner, `git log HEAD..origin/main`** : si `main` a bougé,
  le fusionner dans la branche et pousser, pour que la CI teste l'état qui
  sera réellement fusionné.

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

# Definition of Done — ne jamais annoncer « c'est bon » sans preuve

**Règle absolue : avant de déclarer un travail terminé, fiable, prêt à commiter
ou prêt à releaser, exécuter `./scripts/check-release-ready.sh` et coller son
verdict.** Une impression de complétude n'est pas une preuve : ce script a été
créé après plusieurs « c'est prêt » démentis ensuite par une vérification
(flag non documenté, traduction périmée, script sortant en erreur malgré un
succès, provider non testé de bout en bout).

```bash
./scripts/check-release-ready.sh          # 17 vérifications, ~45 s
./scripts/check-release-ready.sh --full   # 19 : + hooks pre-push (mypy, SAST, audit) et wheel neuf, ~3 min
```

Ce qu'il vérifie : tests `tests/` et `scripts/tests/`, hooks pre-commit (et
pre-push en `--full`), **chaque flag argparse présent dans le README**, **chaque
`os.getenv` documenté**, les 28 traductions (présence, structure, URLs,
placeholders, couverture des flags), la version du CHANGELOG, son extraction
par `release.sh` et son égalité avec celle de `pyproject.toml`, l'absence de
secret dans les fichiers suivis et de module Python non suivi, et une 7ᵉ section qui confronte la doc au point
d'entrée console et le déclencheur du hook Lizard à son scope réel (cf. `docs/qualite.md`, § Lizard).

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

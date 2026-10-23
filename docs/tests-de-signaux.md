# Tests de signaux : un faux pid peut tuer toute la session

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
- **Jamais de `pkill`, `killall` ni `pgrep … | xargs kill` sur un nom de
  binaire** (`claude`, `codex`, `agy`) : les sessions vivantes de
  l'utilisateur portent le même nom — six sessions Claude Code tournaient
  pendant l'écriture de `--use_claude_code`. Un agent ne s'arrête que par
  `_codex_run_process` et `_agent_group`, qui visent SON groupe.
- Un test à vrai signal ne vise qu'un sous-processus factice inoffensif lancé
  par le test lui-même (`_interrupt_a_real_agent`) ; un signal envoyé au
  lanceur de tests passe par un gestionnaire neutre posé en filet.
- Restructurer un bloc `assertRaises` ou `with patch(...)` — ce que demandent
  Sonar S5778 et Codacy — est exactement le geste dangereux : vérifier
  qu'aucun appel n'est sorti de la portée du `patch("os.killpg")` avant de
  relancer la suite.

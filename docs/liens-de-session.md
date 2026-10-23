# Jamais de lien de session dans le dépôt

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

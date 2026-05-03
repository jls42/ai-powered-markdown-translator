#!/bin/bash
# Release orchestrator — automatisable de bout en bout.
#
# === Workflow recommandé (2 phases) ===
#
#   Phase 1 (avant merge) sur la branche feature:
#     ./release.sh --auto              # régénère + commit + push branche + PR (sans tag)
#
#   Phase 2 (après merge PR) :
#     ./release.sh --tag-only --yes    # checkout main + pull + tag + push tag + GitHub Release
#
# === Modes d'usage ===
#
#   ./release.sh                 # interactif : régénère + commit + push + PR (prompts)
#   ./release.sh --auto          # NON-INTERACTIF Phase 1 : régénère + commit + push + PR (PAS de tag)
#   ./release.sh --local-only    # NON-INTERACTIF : régénère + commit local. Pas de push.
#   ./release.sh --tag-only      # Phase 2 : checkout main, pull, tag main, push tag, GitHub Release
#   ./release.sh --dry-run       # affiche tout ce qui serait fait, ne touche à rien
#
# === Flags fins (composables) ===
#
#   --version X.Y.Z       # override la version (sinon: lue depuis CHANGELOG.md)
#   --tag vX.Y.Z          # override du tag (par défaut: v$VERSION)
#   --skip-regen          # ne pas régénérer les 28 traductions
#   --skip-tests          # ne pas lancer la suite unittest (déconseillé)
#   --with-tag            # opt-in: tagger AVANT merge (workflow fast-forward uniquement)
#   --no-pr               # ne pas créer la PR
#   --no-github-release   # ne pas créer la GitHub Release
#   --no-push             # ne pas push (utile pour tester)
#   --yes                 # confirmer toutes les questions automatiquement
#
# === Pré-requis ===
#
# - Working directory = repo racine
# - venv/ présent avec dépendances installées
# - SSH config OK pour git push origin
# - Pour --create-pr / --github-release : gh auth status doit être OK.
#   Si le token est expiré : warn + skip gracieux, instructions affichées.
#
# === Utilisation par Claude (auto mode) ===
#
# Quand l'utilisateur demande "release"/"tag"/"publie" :
#   ./release.sh --auto                   # release complète depuis branche feature
#   ./release.sh --tag-only --yes         # tag post-merge sur main
#
# Le script ne touche jamais à `main` (refuse de release depuis main).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# === Defaults ===
MODE="interactive"          # interactive | auto | local-only | tag-only | dry-run
VERSION=""
TAG=""
SKIP_REGEN=false
SKIP_TESTS=false
DO_PUSH=true
DO_PR=true
DO_GITHUB_RELEASE=true       # actif uniquement en mode --tag-only
WITH_TAG=false               # opt-in: tagger AVANT merge (workflow fast-forward)
ASSUME_YES=false
DRY_RUN=false

# === Parse args ===
while [[ $# -gt 0 ]]; do
  case "$1" in
    --auto)
      MODE="auto"; ASSUME_YES=true
      shift ;;
    --local-only)
      MODE="local-only"; ASSUME_YES=true; DO_PUSH=false; DO_PR=false; DO_GITHUB_RELEASE=false
      shift ;;
    --tag-only)
      MODE="tag-only"; SKIP_REGEN=true
      shift ;;
    --dry-run)
      MODE="dry-run"; DRY_RUN=true; ASSUME_YES=true
      shift ;;
    --version)             VERSION="$2"; shift 2 ;;
    --tag)                 TAG="$2"; shift 2 ;;
    --skip-regen)          SKIP_REGEN=true; shift ;;
    --skip-tests)          SKIP_TESTS=true; shift ;;
    --no-pr)               DO_PR=false; shift ;;
    --no-github-release)   DO_GITHUB_RELEASE=false; shift ;;
    --no-push)             DO_PUSH=false; DO_PR=false; DO_GITHUB_RELEASE=false; shift ;;
    --with-tag)            WITH_TAG=true; shift ;;
    --yes|-y)              ASSUME_YES=true; shift ;;
    -h|--help)             sed -n '2,42p' "$0"; exit 0 ;;
    *) echo "Unknown option: $1" >&2; exit 1 ;;
  esac
done

# === Helpers ===
log()  { echo -e "\033[1;34m[release]\033[0m $*"; }
warn() { echo -e "\033[1;33m[warn]\033[0m $*" >&2; }
err()  { echo -e "\033[1;31m[error]\033[0m $*" >&2; }
ok()   { echo -e "\033[1;32m[ok]\033[0m $*"; }

confirm() {
  local prompt="$1"
  if $ASSUME_YES; then
    log "$prompt -> auto-yes"
    return 0
  fi
  read -r -p "$(echo -e "\033[1;33m$prompt [y/N]\033[0m ")" reply
  [[ "$reply" =~ ^[Yy]$ ]]
}

run() {
  if $DRY_RUN; then
    log "[dry-run] $*"
  else
    "$@"
  fi
}

# Vérifie que gh est utilisable avec le token courant.
# Note: on lit `gh api user --jq .login` plutôt que de parser un blob arbitraire,
# pour ne pas faire confiance au seul exit code (un token expiré peut renvoyer
# un payload d'erreur avec exit 0 dans certains cas) ET ne pas matcher des
# substrings comme "error" qui peuvent apparaître légitimement dans le profil.
check_gh_auth() {
  if ! command -v gh >/dev/null 2>&1; then
    return 1
  fi
  local login
  login=$(gh api user --jq .login 2>/dev/null) || return 1
  # Un login GitHub valide est non vide et alphanumérique (avec tirets).
  [[ -n "$login" && "$login" =~ ^[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?$ ]]
}

extract_release_notes() {
  local ver="$1"
  awk -v ver="$ver" '
    $0 ~ "^- \\*\\*" ver "\\*\\*" { keep=1 }
    keep && $0 ~ "^- \\*\\*[0-9]+\\.[0-9]+" && $0 !~ "^- \\*\\*" ver "\\*\\*" { exit }
    keep { print }
  ' CHANGELOG.md
}

extract_changelog_version() {
  # Accepte X.Y et X.Y.Z (cohérent avec extract_release_notes ci-dessus).
  grep -m 1 -oE '\*\*[0-9]+\.[0-9]+(\.[0-9]+)?\*\*' CHANGELOG.md | head -1 | tr -d '*'
}

# === Activation venv (commun) ===
if [[ ! -f venv/bin/activate ]]; then
  err "venv/bin/activate manquant. Crée le venv: python -m venv venv && pip install -r requirements.txt"
  exit 1
fi
# shellcheck disable=SC1091
source venv/bin/activate

# === MODE TAG-ONLY ===
# Post-merge : checkout main, pull, tag, push tag, GitHub Release
if [[ "$MODE" == "tag-only" ]]; then
  log "Mode tag-only : tag post-merge sur main"

  # Working tree must be clean
  if ! git diff-index --quiet HEAD --; then
    err "Working tree pas clean. Stash/commit d'abord."
    git status -s
    exit 1
  fi

  log "Checkout main + pull..."
  run git checkout main
  run git pull origin main

  CHANGELOG_VERSION=$(extract_changelog_version)
  [[ -z "$VERSION" ]] && VERSION="$CHANGELOG_VERSION"
  if [[ "$VERSION" != "$CHANGELOG_VERSION" ]]; then
    err "Discordance: --version=$VERSION mais CHANGELOG sur main = $CHANGELOG_VERSION"
    err "La PR n'est probablement pas mergée. Annulé."
    exit 1
  fi
  [[ -z "$TAG" ]] && TAG="v$VERSION"
  log "Version: $VERSION  |  Tag: $TAG"

  if git rev-parse "$TAG" >/dev/null 2>&1; then
    err "Le tag $TAG existe déjà localement. Si tu veux le déplacer:"
    err "  git tag -d $TAG && git push origin :refs/tags/$TAG"
    exit 1
  fi
  if git ls-remote --tags origin "refs/tags/$TAG" 2>/dev/null | grep -q "$TAG"; then
    err "Le tag $TAG existe déjà sur origin. Stop."
    exit 1
  fi

  RELEASE_NOTES=$(extract_release_notes "$VERSION")
  TAG_MSG=$(printf "Release %s\n\n%s\n" "$VERSION" "$RELEASE_NOTES")

  log "Création tag annoté $TAG sur main HEAD..."
  run git tag -a "$TAG" -m "$TAG_MSG"

  if $DO_PUSH; then
    log "Push tag..."
    run git push origin "$TAG"
    ok "Tag $TAG poussé sur origin"
  else
    warn "Tag créé localement seulement (--no-push). Push manuel: git push origin $TAG"
  fi

  if $DO_GITHUB_RELEASE; then
    if ! command -v gh >/dev/null 2>&1; then
      warn "gh non installé — skip GitHub Release"
    elif ! check_gh_auth; then
      warn "gh non authentifié (token expiré ?) — skip GitHub Release."
      warn "Reconnecte: gh auth login"
      warn "Puis: ./release.sh --tag-only --version $VERSION (re-create) ou commande manuelle:"
      warn "  echo \"\$(awk ... CHANGELOG.md)\" | gh release create $TAG --title v$VERSION --notes-file -"
    else
      log "Création GitHub Release..."
      if $DRY_RUN; then
        log "[dry-run] gh release create $TAG --title v$VERSION (notes depuis CHANGELOG)"
      else
        echo "$RELEASE_NOTES" | gh release create "$TAG" --title "v$VERSION" --notes-file -
        ok "GitHub Release v$VERSION créée"
      fi
    fi
  fi

  ok "==== Tag-only mode terminé : $TAG ===="
  exit 0
fi

# === MODE PRINCIPAL : prepare-release ===
# Étapes 1-7 : pré-checks, version, régénération, validation, commit, tag, push/PR/release

# === Étape 0: Pré-checks ===
log "Pré-checks..."

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [[ "$CURRENT_BRANCH" == "main" || "$CURRENT_BRANCH" == "master" ]]; then
  err "Refus de release depuis '$CURRENT_BRANCH'. Crée une branche dédiée (fix/*, release/*, feat/*)."
  exit 1
fi
log "Branche: $CURRENT_BRANCH"

if ! $SKIP_TESTS; then
  log "Lancement des tests unittest (tests/ + scripts/tests/)..."
  # Aligné sur scripts/run-unittest.sh : on agrège les rc pour que la 2e suite
  # tourne même si la 1ère échoue. Sinon le pre-push hook divergerait du contrat
  # release et un échec dans tests/ masquerait silencieusement scripts/tests/.
  rc=0
  python -m unittest discover -s tests/ -v || rc=$?
  python -m unittest discover -s scripts/tests/ -v || rc=$?
  if [[ "$rc" -ne 0 ]]; then
    err "Tests en échec (rc=$rc)"
    exit "$rc"
  fi
  ok "Tests OK"
else
  warn "Tests skipped (--skip-tests)"
fi

python -c "import translate" || { err "import translate échoue"; exit 1; }
ok "Import OK"

# === Étape 1: Extraction version ===
CHANGELOG_VERSION=$(extract_changelog_version)
if [[ -z "$CHANGELOG_VERSION" ]]; then
  err "Impossible d'extraire la version depuis CHANGELOG.md (pattern '- **X.Y[.Z]**' attendu)"
  exit 1
fi
log "Version détectée dans CHANGELOG: $CHANGELOG_VERSION"

if [[ -z "$VERSION" ]]; then
  VERSION="$CHANGELOG_VERSION"
elif [[ "$VERSION" != "$CHANGELOG_VERSION" ]]; then
  err "Discordance: --version=$VERSION mais CHANGELOG = $CHANGELOG_VERSION"
  exit 1
fi

[[ -z "$TAG" ]] && TAG="v$VERSION"
log "Version: $VERSION  |  Tag (différé sauf --with-tag): $TAG"

# On vérifie l'absence du tag uniquement si on va l'utiliser maintenant (--with-tag).
# Sinon, le tag est créé en phase 2 (--tag-only) qui fait son propre check.
if $WITH_TAG; then
  if git rev-parse "$TAG" >/dev/null 2>&1; then
    err "Le tag $TAG existe déjà localement"
    exit 1
  fi
  if git ls-remote --tags origin "refs/tags/$TAG" 2>/dev/null | grep -q "$TAG"; then
    err "Le tag $TAG existe déjà sur origin"
    exit 1
  fi
  ok "Tag $TAG: disponible (local + origin)"
fi

# === Étape 2: Régénération traductions ===
if ! $SKIP_REGEN; then
  log "Régénération des README + CHANGELOG en 14 langues (--force)..."
  run ./regen_translations.sh --force
  ok "Régénération OK"
else
  warn "Régénération skipped (--skip-regen)"
fi

# === Étape 3: Validation post ===
log "Validation des sorties..."
LANGS="ar de en es hi it ja ko nl pl pt ro sv zh"
MISSING=0
for lang in $LANGS; do
  for prefix in README CHANGELOG; do
    f="${prefix}-${lang}.md"
    if [[ ! -f "$f" ]]; then
      err "Fichier manquant: $f"
      MISSING=$((MISSING+1))
    elif [[ ! -s "$f" ]]; then
      err "Fichier vide: $f"
      MISSING=$((MISSING+1))
    fi
  done
done
if (( MISSING > 0 )); then
  err "$MISSING fichier(s) manquant(s) ou vide(s) — release annulée"
  exit 1
fi
ok "28/28 fichiers de traduction présents et non vides"

# === Étape 4: git add ciblé + commit ===
echo ""
log "État git avant commit:"
git status -s
echo ""

if ! confirm "Procéder au git add ciblé + commit ?"; then
  log "Annulé."
  exit 0
fi

# Add ciblé (jamais -A) : fichier par fichier, pas de répertoire (évite __pycache__/, .pyc, etc.)
run git add CHANGELOG.md CLAUDE.md README.md requirements.txt translate.py .gitignore
run git add tests/test_silent_failure.py tests/fixtures/long_fr_excerpt.txt
run git add regen_translations.sh release.sh

# Quality tooling files (pre-commit, ruff, mypy, lizard, detect-secrets, etc.)
# Listés explicitement (jamais de répertoire) pour cohérence avec la règle ci-dessus.
run git add .pre-commit-config.yaml pyproject.toml .prettierrc .prettierignore
run git add .secrets.baseline requirements-dev.txt
run git add scripts/__init__.py scripts/_venv_python.sh
run git add scripts/check-complexity.sh scripts/check-security-sast.sh
run git add scripts/check-pip-audit.sh scripts/audit_verdict.py
run git add scripts/run-mypy.sh scripts/run-unittest.sh
run git add scripts/tests/test_audit_verdict.py

for lang in $LANGS; do
  run git add "README-${lang}.md" "CHANGELOG-${lang}.md"
done

if ! $DRY_RUN; then
  echo ""
  log "Fichiers stagés:"
  git diff --cached --name-only | sed 's/^/  /'
  echo ""
fi

RELEASE_NOTES=$(extract_release_notes "$VERSION")
COMMIT_TITLE="release: v$VERSION"
COMMIT_MSG=$(printf "%s\n\n%s\n" "$COMMIT_TITLE" "$RELEASE_NOTES")

run git commit -m "$COMMIT_MSG"
ok "Commit créé"

# === Étape 5: Tag annoté local (opt-in via --with-tag) ===
# Par défaut, on ne tag PAS avant merge. Le tag se crée après merge via './release.sh --tag-only'.
# Cela évite que le tag pointe sur la branche feature (et pas sur le merge commit dans main).
if $WITH_TAG; then
  TAG_MSG=$(printf "Release %s\n\n%s\n" "$VERSION" "$RELEASE_NOTES")
  run git tag -a "$TAG" -m "$TAG_MSG"
  ok "Tag $TAG créé localement (--with-tag)"
fi

# === Étape 6: Push branche + tag ===
if ! $DO_PUSH; then
  echo ""
  warn "Push skipped (--no-push). Pour publier:"
  echo "  git push origin $CURRENT_BRANCH"
  echo "  git push origin $TAG"
  echo ""
  ok "==== Mode local terminé ===="
  exit 0
fi

push_msg="Push branche '$CURRENT_BRANCH' sur origin"
$WITH_TAG && push_msg="$push_msg + tag '$TAG'"
if ! confirm "$push_msg ?"; then
  warn "Push annulé. Commit (et tag si --with-tag) restent locaux."
  echo "Pour pousser plus tard:"
  echo "  git push origin $CURRENT_BRANCH"
  $WITH_TAG && echo "  git push origin $TAG"
  exit 0
fi

log "Push branche..."
run git push -u origin "$CURRENT_BRANCH"
if $WITH_TAG; then
  log "Push tag..."
  run git push origin "$TAG"
  ok "Branche + tag poussés sur origin"
else
  ok "Branche poussée sur origin (tag différé : à créer post-merge via --tag-only)"
fi

# === Étape 7: GitHub PR + Release ===
GH_OK=false
if check_gh_auth; then
  GH_OK=true
else
  if ! command -v gh >/dev/null 2>&1; then
    warn "gh non installé. PR + GitHub Release à créer manuellement."
  else
    warn "gh non authentifié ou token expiré. PR + GitHub Release seront à créer manuellement."
    warn "Pour réauthentifier: gh auth login"
  fi
fi

if $DO_PR; then
  if $GH_OK; then
    log "Création de la PR..."
    PR_TITLE="$COMMIT_TITLE"
    PR_BODY=$(printf "%s\n\n---\n\n_PR créée automatiquement par release.sh_" "$RELEASE_NOTES")
    if $DRY_RUN; then
      log "[dry-run] gh pr create --base main --head $CURRENT_BRANCH --title '$PR_TITLE'"
    else
      if gh pr create \
        --base main \
        --head "$CURRENT_BRANCH" \
        --title "$PR_TITLE" \
        --body "$PR_BODY" \
        2>&1; then
        ok "PR créée"
      else
        warn "Échec création PR (peut-être déjà existante)"
      fi
    fi
  else
    echo ""
    warn "PR à créer manuellement:"
    echo "  gh pr create --base main --head $CURRENT_BRANCH --title \"$COMMIT_TITLE\""
    echo "  ou via l'interface GitHub"
  fi
fi

if $DO_GITHUB_RELEASE && $WITH_TAG; then
  if $GH_OK; then
    log "Création GitHub Release..."
    if $DRY_RUN; then
      log "[dry-run] gh release create $TAG --title v$VERSION (notes depuis CHANGELOG)"
    else
      if echo "$RELEASE_NOTES" | gh release create "$TAG" --title "v$VERSION" --notes-file - 2>&1; then
        ok "GitHub Release v$VERSION créée"
      else
        warn "Échec création GitHub Release (peut-être déjà existante)"
      fi
    fi
  else
    echo ""
    warn "GitHub Release à créer manuellement:"
    echo "  echo \"\$(awk ... CHANGELOG.md)\" | gh release create $TAG --title v$VERSION --notes-file -"
  fi
elif $DO_GITHUB_RELEASE; then
  log "GitHub Release reportée au mode --tag-only (tag pas encore créé)"
fi

# === Récap final ===
echo ""
ok "==== Release $VERSION : phase prepare terminée ===="
echo ""
echo "État:"
echo "  - Commit créé sur '$CURRENT_BRANCH'"
echo "  - Branche poussée sur origin"
$WITH_TAG && echo "  - Tag $TAG créé et poussé"
if $DO_PR && $GH_OK; then
  echo "  - PR créée automatiquement"
fi
echo ""
echo "Prochaines étapes:"
echo "  1. Reviewer la PR sur GitHub et la merger"
if ! $WITH_TAG; then
  echo "  2. Une fois mergée, lancer:  ./release.sh --tag-only --yes"
  echo "     (crée le tag $TAG sur le HEAD de main + push tag + GitHub Release)"
else
  echo "  2. Le tag $TAG pointe sur le commit de release sur '$CURRENT_BRANCH'."
  echo "     Si tu veux qu'il pointe sur le merge commit après merge:"
  echo "       git tag -d $TAG && git push origin :refs/tags/$TAG"
  echo "       puis ./release.sh --tag-only --yes"
fi

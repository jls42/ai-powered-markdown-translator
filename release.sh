#!/bin/bash
# Release orchestrator — automatisable de bout en bout.
#
# === Workflow recommandé (2 phases) ===
#
#   Phase 1 (avant merge) sur la branche feature:
#     ./release.sh --auto              # régénère + commit + push branche + MR (sans tag)
#
#   Phase 2 (après merge MR) :
#     ./release.sh --tag-only --yes    # checkout main + pull + tag + push tag + GitLab Release
#
# === Modes d'usage ===
#
#   ./release.sh                 # interactif : régénère + commit + push + MR (prompts)
#   ./release.sh --auto          # NON-INTERACTIF Phase 1 : régénère + commit + push + MR (PAS de tag)
#   ./release.sh --local-only    # NON-INTERACTIF : régénère + commit local. Pas de push.
#   ./release.sh --tag-only      # Phase 2 : checkout main, pull, tag main, push tag, GitLab Release
#   ./release.sh --dry-run       # affiche tout ce qui serait fait, ne touche à rien
#
# === Flags fins (composables) ===
#
#   --version X.Y.Z       # override la version (sinon: lue depuis CHANGELOG.md)
#   --tag vX.Y.Z          # override du tag (par défaut: v$VERSION)
#   --skip-regen          # ne pas régénérer les 28 traductions
#   --skip-tests          # ne pas lancer la suite unittest (déconseillé)
#   --with-tag            # opt-in: tagger AVANT merge (workflow fast-forward uniquement)
#   --no-mr               # ne pas créer la MR
#   --no-gitlab-release   # ne pas créer la GitLab Release
#   --no-push             # ne pas push (utile pour tester)
#   --yes                 # confirmer toutes les questions automatiquement
#
# === Pré-requis ===
#
# - Working directory = repo racine
# - venv/ présent avec dépendances installées
# - SSH config OK pour git push origin
# - Pour --create-mr / --gitlab-release : glab auth status doit être OK.
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
DO_MR=true
DO_GITLAB_RELEASE=true       # actif uniquement en mode --tag-only
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
      MODE="local-only"; ASSUME_YES=true; DO_PUSH=false; DO_MR=false; DO_GITLAB_RELEASE=false
      shift ;;
    --tag-only)
      MODE="tag-only"; SKIP_REGEN=true
      shift ;;
    --dry-run)
      MODE="dry-run"; DRY_RUN=true
      shift ;;
    --version)             VERSION="$2"; shift 2 ;;
    --tag)                 TAG="$2"; shift 2 ;;
    --skip-regen)          SKIP_REGEN=true; shift ;;
    --skip-tests)          SKIP_TESTS=true; shift ;;
    --no-mr)               DO_MR=false; shift ;;
    --no-gitlab-release)   DO_GITLAB_RELEASE=false; shift ;;
    --no-push)             DO_PUSH=false; DO_MR=false; DO_GITLAB_RELEASE=false; shift ;;
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

# Vérifie que glab est utilisable avec le token courant.
# Note: `glab auth status` et `glab api user` retournent exit 0 même avec un token expiré
# (sortie contient "error":"invalid_token" mais exit code = 0). On parse donc la sortie.
check_glab_auth() {
  if ! command -v glab >/dev/null 2>&1; then
    return 1
  fi
  local output
  output=$(glab api user 2>&1) || return 1
  if echo "$output" | grep -qE '"error"|HTTP 4[0-9]{2}|HTTP 5[0-9]{2}'; then
    return 1
  fi
  return 0
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
  grep -m 1 -oE '\*\*[0-9]+\.[0-9]+\.[0-9]+\*\*' CHANGELOG.md | head -1 | tr -d '*'
}

# === Activation venv (commun) ===
if [[ ! -f venv/bin/activate ]]; then
  err "venv/bin/activate manquant. Crée le venv: python -m venv venv && pip install -r requirements.txt"
  exit 1
fi
# shellcheck disable=SC1091
source venv/bin/activate

# === MODE TAG-ONLY ===
# Post-merge : checkout main, pull, tag, push tag, GitLab Release
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
    err "La MR n'est probablement pas mergée. Annulé."
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

  if $DO_GITLAB_RELEASE; then
    if ! command -v glab >/dev/null 2>&1; then
      warn "glab non installé — skip GitLab Release"
    elif ! check_glab_auth; then
      warn "glab non authentifié (token expiré ?) — skip GitLab Release."
      warn "Reconnecte: glab auth login"
      warn "Puis: ./release.sh --tag-only --skip-tests --version $VERSION (re-create) ou commande manuelle:"
      warn "  echo \"\$(awk ... CHANGELOG.md)\" | glab release create $TAG --name v$VERSION --notes-file -"
    else
      log "Création GitLab Release..."
      if $DRY_RUN; then
        log "[dry-run] glab release create $TAG --name v$VERSION (notes depuis CHANGELOG)"
      else
        echo "$RELEASE_NOTES" | glab release create "$TAG" --name "v$VERSION" --notes-file -
        ok "GitLab Release v$VERSION créée"
      fi
    fi
  fi

  ok "==== Tag-only mode terminé : $TAG ===="
  exit 0
fi

# === MODE PRINCIPAL : prepare-release ===
# Étapes 1-7 : pré-checks, version, régénération, validation, commit, tag, push/MR/release

# === Étape 0: Pré-checks ===
log "Pré-checks..."

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [[ "$CURRENT_BRANCH" == "main" || "$CURRENT_BRANCH" == "master" ]]; then
  err "Refus de release depuis '$CURRENT_BRANCH'. Crée une branche dédiée (fix/*, release/*, feat/*)."
  exit 1
fi
log "Branche: $CURRENT_BRANCH"

if ! $SKIP_TESTS; then
  log "Lancement des tests unittest..."
  python -m unittest discover tests/ -v
  ok "Tests OK"
else
  warn "Tests skipped (--skip-tests)"
fi

python -c "import translate" || { err "import translate échoue"; exit 1; }
ok "Import OK"

# === Étape 1: Extraction version ===
CHANGELOG_VERSION=$(extract_changelog_version)
if [[ -z "$CHANGELOG_VERSION" ]]; then
  err "Impossible d'extraire la version depuis CHANGELOG.md (pattern '- **X.Y.Z**' attendu)"
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

# === Étape 7: GitLab MR + Release ===
GLAB_OK=false
if check_glab_auth; then
  GLAB_OK=true
else
  if ! command -v glab >/dev/null 2>&1; then
    warn "glab non installé. MR + GitLab Release à créer manuellement."
  else
    warn "glab non authentifié ou token expiré. MR + GitLab Release seront à créer manuellement."
    warn "Pour réauthentifier: glab auth login"
  fi
fi

if $DO_MR; then
  if $GLAB_OK; then
    log "Création de la MR..."
    MR_TITLE="$COMMIT_TITLE"
    MR_BODY=$(printf "%s\n\n---\n\n_MR créée automatiquement par release.sh_" "$RELEASE_NOTES")
    if $DRY_RUN; then
      log "[dry-run] glab mr create --title '$MR_TITLE' --target-branch main"
    else
      echo "$MR_BODY" | glab mr create \
        --title "$MR_TITLE" \
        --description "$(cat)" \
        --target-branch main \
        --source-branch "$CURRENT_BRANCH" \
        --remove-source-branch \
        --yes 2>&1 || warn "Échec création MR (peut-être déjà existante)"
      ok "MR créée"
    fi
  else
    echo ""
    warn "MR à créer manuellement:"
    echo "  glab mr create --title \"$COMMIT_TITLE\" --target-branch main --source-branch $CURRENT_BRANCH"
    echo "  ou via l'interface GitLab"
  fi
fi

if $DO_GITLAB_RELEASE && $WITH_TAG; then
  if $GLAB_OK; then
    log "Création GitLab Release..."
    if $DRY_RUN; then
      log "[dry-run] glab release create $TAG --name v$VERSION (notes depuis CHANGELOG)"
    else
      echo "$RELEASE_NOTES" | glab release create "$TAG" --name "v$VERSION" --notes-file - \
        2>&1 || warn "Échec création GitLab Release (peut-être déjà existante)"
      ok "GitLab Release v$VERSION créée"
    fi
  else
    echo ""
    warn "GitLab Release à créer manuellement:"
    echo "  echo \"\$(awk ... CHANGELOG.md)\" | glab release create $TAG --name v$VERSION --notes-file -"
  fi
elif $DO_GITLAB_RELEASE; then
  log "GitLab Release reportée au mode --tag-only (tag pas encore créé)"
fi

# === Récap final ===
echo ""
ok "==== Release $VERSION : phase prepare terminée ===="
echo ""
echo "État:"
echo "  - Commit créé sur '$CURRENT_BRANCH'"
echo "  - Branche poussée sur origin"
$WITH_TAG && echo "  - Tag $TAG créé et poussé"
if $DO_MR && $GLAB_OK; then
  echo "  - MR créée automatiquement"
fi
echo ""
echo "Prochaines étapes:"
echo "  1. Reviewer la MR sur GitLab et la merger"
if ! $WITH_TAG; then
  echo "  2. Une fois mergée, lancer:  ./release.sh --tag-only --yes"
  echo "     (crée le tag $TAG sur le HEAD de main + push tag + GitLab Release)"
else
  echo "  2. Le tag $TAG pointe sur le commit de release sur '$CURRENT_BRANCH'."
  echo "     Si tu veux qu'il pointe sur le merge commit après merge:"
  echo "       git tag -d $TAG && git push origin :refs/tags/$TAG"
  echo "       puis ./release.sh --tag-only --yes"
fi

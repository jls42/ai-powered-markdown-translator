#!/usr/bin/env bash
# Banc d'un candidat : traduit un document N fois avec le code de `src/` et
# contrôle chaque sortie par scripts/compare_structure.py.
#
#   banc.sh ÉTIQUETTE N [options d'aipmt...]
#   banc.sh hydrogen 2 --use_gemini --model gemini-4-hydrogen
#   BANC_FICHIER=CHANGELOG.md BANC_LANGUE=hi banc.sh agy-eco 1 --use_antigravity --eco
#
# Défaut : README.md en japonais, l'épreuve qui départage (écriture non latine,
# 4 segments, liens internes, codes en ligne). Les N essais partent en même
# temps. ATTENTION : un essai par API est facturé ; lire le prix du modèle sur
# la page de l'éditeur AVANT. Jamais sur Codex si un travail planifié a besoin
# de la fenêtre de 5 h.
set -u
tag=$1; n=$2; shift 2
repo=${BANC_DEPOT:-$PWD}
file=${BANC_FICHIER:-README.md}
lang=${BANC_LANGUE:-ja}
out=${BANC_SORTIE:-${TMPDIR:-/tmp}/banc-aipmt}
cd "$repo" || exit 1
base=$(basename "$file" .md)
one() {
  local d="$out/$tag-$1"; rm -rf "$d"; mkdir -p "$d"
  local start; start=$(date +%s)
  PYTHONPATH=src PYTHONUNBUFFERED=1 venv/bin/python -m aipmt --file "$file" --target_dir "$d" \
    --source_lang fr --target_lang "$lang" "${@:2}" > "$d.log" 2>&1
  local rc=$?
  local verdict
  if [ $rc = 0 ]; then
    verdict=$(venv/bin/python scripts/compare_structure.py "$file" "$d/$base-$lang.md" 2>&1 | tail -2 | tr '\n' ' ')
  else
    verdict=$(grep -oE '(RuntimeError|Error).{0,200}' "$d.log" | tail -1)
  fi
  echo "[$tag-$1 → $lang] exit=$rc durée=$(( $(date +%s) - start ))s $verdict"
}
for i in $(seq 1 "$n"); do one "$i" "$@" & done
wait

#!/bin/bash
set -e
# Regenerate README and CHANGELOG translations in parallel (10 jobs max)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

source venv/bin/activate

if [ ! -f translate.py ]; then
  echo "ERROR: translate.py not found in $SCRIPT_DIR" >&2
  exit 1
fi

MAX_JOBS=10
LANGS="ar de en es hi it ja ko nl pl pt ro sv zh"

for lang in $LANGS; do
  echo "[README] -> $lang"
  python translate.py --file README.md --target_dir . --source_lang fr --target_lang "$lang" --eco --add_translation_note &

  echo "[CHANGELOG] -> $lang"
  python translate.py --file CHANGELOG.md --target_dir . --source_lang fr --target_lang "$lang" --eco --add_translation_note &

  # Limit parallel jobs
  while [ $(jobs -r | wc -l) -ge $MAX_JOBS ]; do
    sleep 1
  done
done

wait
echo "=== DONE ==="
ls -1 README-*.md CHANGELOG-*.md 2>/dev/null | wc -l

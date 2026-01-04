#!/bin/bash
# Regenerate README and CHANGELOG translations in parallel (10 jobs max)
cd /home/haxix/git/ai/ai-powered-markdown-translator
source venv/bin/activate

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

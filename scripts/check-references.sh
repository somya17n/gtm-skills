#!/usr/bin/env bash
# Verify every `references/*.md` a SKILL.md cites is present next to that skill and matches the
# canonical copy at the repo root. Run in CI: a skill whose reference is missing after install is
# a skill that silently degrades, because the agent is told to read a file that is not there.
#
# Usage: scripts/check-references.sh   (exit 0 = clean)

set -uo pipefail
cd "$(dirname "$0")/.."

fail=0
checked=0

while IFS= read -r skill_md; do
  skill_dir="$(dirname "$skill_md")"
  skill="$(basename "$skill_dir")"
  refs="$(grep -oE 'references/[A-Za-z0-9_.-]+\.md' "$skill_md" 2>/dev/null | sort -u || true)"
  [ -z "$refs" ] && continue

  while IFS= read -r ref; do
    base="$(basename "$ref")"
    checked=$((checked + 1))

    if [ ! -f "$skill_dir/references/$base" ]; then
      echo "BROKEN: $skill cites $ref but $skill_dir/references/$base does not exist"
      fail=1
      continue
    fi
    if [ ! -f "references/$base" ]; then
      echo "ORPHAN COPY: $skill_dir/references/$base has no canonical source at references/$base"
      fail=1
      continue
    fi
    if ! cmp -s "references/$base" "$skill_dir/references/$base"; then
      echo "DRIFT: $skill_dir/references/$base differs from references/$base (run scripts/sync-references.sh)"
      fail=1
    fi
  done <<< "$refs"
done < <(find skills -name SKILL.md | sort)

# A reference nobody cites is dead weight that still ships.
for f in references/*.md; do
  base="$(basename "$f")"
  if ! grep -rqE "references/$base" skills/ --include=SKILL.md 2>/dev/null; then
    echo "UNCITED: references/$base is cited by no skill"
    fail=1
  fi
done

echo "checked $checked reference citation(s)"
[ "$fail" -eq 0 ] && echo "OK: all references resolve, match root, and are cited"
exit "$fail"

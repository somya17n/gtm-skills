#!/usr/bin/env bash
# Copy each reference file into the skill directories that cite it.
#
# Why this exists: `npx skills add` installs each skill as a standalone directory. A SKILL.md
# instruction like "Read `references/foo.md`" resolves relative to the skill's own directory, so
# a reference living only at the repo root is unreachable after install. Skills have to carry
# their own references.
#
# `references/` at the repo root stays the canonical, editable source. The per-skill copies are
# generated. Edit the root copy, run this, and commit both.
#
# Usage: scripts/sync-references.sh

set -euo pipefail
cd "$(dirname "$0")/.."

copied=0
missing=0

while IFS= read -r skill_md; do
  skill_dir="$(dirname "$skill_md")"
  refs="$(grep -oE 'references/[A-Za-z0-9_.-]+\.md' "$skill_md" 2>/dev/null | sort -u || true)"
  [ -z "$refs" ] && continue

  mkdir -p "$skill_dir/references"
  while IFS= read -r ref; do
    base="$(basename "$ref")"
    if [ -f "references/$base" ]; then
      cp "references/$base" "$skill_dir/references/$base"
      copied=$((copied + 1))
    else
      echo "MISSING SOURCE: references/$base (cited by $(basename "$skill_dir"))" >&2
      missing=$((missing + 1))
    fi
  done <<< "$refs"
done < <(find skills -name SKILL.md | sort)

echo "copied $copied reference file(s) into skill directories"
if [ "$missing" -gt 0 ]; then
  echo "$missing citation(s) had no source file in references/" >&2
  exit 1
fi

"""Splice damage: text a find-and-replace left behind that still parses as markdown.

verify-skills.py section C catches a reference that names a skill which no longer exists.
It cannot catch the other half of a bad sweep: a replacement that landed in the middle of a
sentence, inside a possessive, or inside a backticked path. That damage has no broken link and
no missing file, so every existing gate passes and the text ships reading like this:

    1. Check for `.agents/product-context.md`. If missing, **If `.agents/product-context.md`
       does not exist, build it yourself.

    ... saves what it learned to `.agents/the shared context file.md`

Both shipped in one commit across 16 files. This fails the build on either.
"""
import glob, io, os, re, sys

SKILLS = sorted(glob.glob("skills/*/*/SKILL.md"))
PROSE = SKILLS + sorted(glob.glob("references/*.md")) + ["README.md"]

findings = {}

# 1. A description that a sweep truncated, emptied, or dropped a prose phrase into. The
#    description is the routing surface, so damage here silently stops a skill being found.
bad = []
for p in SKILLS:
    raw = io.open(p, encoding="utf-8").read()
    fm = raw.split("---")[1] if raw.startswith("---") else ""
    m = re.search(r"^description:\s*(.+(?:\n\s{2,}.+)*)$", fm, re.M)
    d = (" ".join(m.group(1).split()) if m else "").strip().strip("\"'")
    if not d:
        bad.append((p, "description EMPTY"))
    elif len(d) < 60:
        bad.append((p, "description SHORT (%d chars)" % len(d)))
    elif not d.rstrip().endswith((".", "!", "?")):
        bad.append((p, "description has no terminal stop: ...%s" % d[-50:]))
    elif re.search(r"Boundary:\s*(?:\.|,|$)", d):
        bad.append((p, "Boundary clause is empty"))
findings["descriptions empty, short or malformed"] = bad

# 2. Two conditionals spliced into one sentence. A replacement whose pattern matched the tail of
#    a sentence but whose replacement text restated the condition leaves both halves standing.
SPLICE = [
    re.compile(r"\bIf\b[^.!?]{0,120}?,\s*\*{0,2}If\b"),
    re.compile(r"\bif missing,\s*\*{0,2}\s*if\b", re.I),
    re.compile(r"\bCheck for\b[^.!?]*\.\s*\*{0,2}If\b[^.!?]*does not exist"),
]
splice = []
for p in PROSE:
    for i, line in enumerate(io.open(p, encoding="utf-8").read().split("\n"), 1):
        if any(rx.search(line) for rx in SPLICE):
            splice.append((p, i, line.strip()[:130]))
findings["two conditionals spliced together"] = splice

# 3. A path inside backticks that has picked up spaces. `.agents/<something with spaces>.md` is
#    never a real file, and it reads to the user as one they should go and look for.
paths = []
for p in PROSE:
    for i, line in enumerate(io.open(p, encoding="utf-8").read().split("\n"), 1):
        for span in re.findall(r"`([^`\n]+)`", line):
            if span.startswith(".agents/") and " " in span:
                paths.append((p, i, "unusable path: `%s`" % span))
findings["a backticked .agents path containing spaces"] = paths

# 4. Structures a deletion leaves behind. The emptied-table check runs on the README only: skills
#    use a heading plus a column header with no rows as an OUTPUT TEMPLATE the model fills at run
#    time (sdr/inbox-management "## Output format", store-automation/automation-ledger
#    "## Suppressions (active)"), so it is a legitimate shape there and a defect in the README.
empty = []
for p in PROSE:
    L = io.open(p, encoding="utf-8").read().split("\n")
    for i, line in enumerate(L):
        if line.strip() == "```" and i + 1 < len(L) and L[i + 1].strip() == "```":
            empty.append((p, i + 1, "empty code fence"))
        if "****" in line:
            empty.append((p, i + 1, "empty bold"))
        if p != "README.md" or not re.fullmatch(r"\|[-\s|:]+\|", line.strip()):
            continue
        if i + 1 < len(L) and L[i + 1].strip().startswith("|"):
            continue                                    # the table has rows
        j = i - 1
        while j >= 0 and (L[j].strip().startswith("|") or not L[j].strip()):
            j -= 1
        if not (j >= 0 and re.match(r"^#{2,4} ", L[j])):
            continue
        k = i + 1
        while k < len(L) and not L[k].strip():
            k += 1
        if k >= len(L) or re.match(r"^#{2,4} ", L[k]):
            empty.append((p, i + 1, "section whose only body is an empty table: %s" % L[j].strip()))
findings["empty markdown left by a deletion"] = empty

total = 0
for label, rows in findings.items():
    print("%s: %d" % (label, len(rows)))
    for r in rows[:25]:
        print("    ", r)
    total += len(rows)

print()
print("files scanned: %d (%d SKILL.md)" % (len(PROSE), len(SKILLS)))
if not SKILLS:
    print("FAIL: scanned no skills. The glob is wrong or the tree is empty.")
    sys.exit(2)
print("TOTAL SPLICE ARTIFACTS: %d" % total)
sys.exit(1 if total else 0)

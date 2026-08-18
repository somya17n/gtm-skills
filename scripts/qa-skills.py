"""Behavioural QA for every skill.

verify-skills.py checks that a skill is structurally valid. This checks that it will not
disappoint on first run. Every rule here traces to something a tester actually complained
about, so a failure means a real user-facing defect, not a style nit.
"""
import re, glob, io, sys, os, collections

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
FILES = sorted(glob.glob("skills/*/*/SKILL.md")) + ["skills/product-context/SKILL.md"]

# A skill teaches Claude the register it writes in, so a tell in the skill becomes a tell
# in the output. "highest-leverage" is a compound adjective, not the verb. "seamless grey"
# is a real backdrop. A skill naming a banned word in order to ban it is exempt (see CTX).
TELLS = [
    (r"\bnot just\b[^.]{0,60}\bbut\b", "negative parallelism"),
    (r"it'?s not about[^.]{0,40}it'?s", "negative parallelism"),
    (r"[.,]\s*no (guesswork|fluff|wasted|excuses|surprises)\b", "tailing negation"),
    (r"(?<!-)\b(leverage|utili[sz]e|robust|holistic|cutting-edge|best-in-class|world-class)\b(?!-)",
     "AI vocabulary"),
    (r"\bseamless\b(?!\W{1,3}(grey|gray|white|backdrop|paper|environmental|gradient))", "AI vocabulary"),
    (r"\bdelve\b|\bdive deep\b|\btapestry\b", "AI vocabulary"),
    (r"\bin order to\b", "filler"),
    (r"it is important to note", "filler"),
    (u"[—–]", "em or en dash"),
    (u"[‘’“”]", "curly quote"),
    (u"[\U0001F300-\U0001FAFF✅❌⚠]", "emoji"),
]
CTX = re.compile(r'banned|do not use|never use|avoid|reads AI|instead of|no "', re.I)

STRUCT = [
    ("input list",   lambda t: bool(re.search(r'^##+ (How to run|Inputs)', t, re.M))),
    ("input gate",   lambda t: "## Before you write" in t),
    ("chaining",     lambda t: "## Chain with" in t),
    ("house rules",  lambda t: "references/house-rules.md" in t),
    ("answer-first", lambda t: bool(re.search(r'answer first|first line is|first two lines|top three|goes first|Lead with', t, re.I))),
    ("CTA",          lambda t: "Generated with Intempt gtm-skills" in t),
]

problems = collections.defaultdict(list)
for f in FILES:
    name = f.replace("\\", "/").split("/")[-2]
    t = open(f, encoding="utf-8").read()
    body = t.split("---", 2)[-1]
    for label, fn in STRUCT:
        if not fn(t):
            problems[name].append("missing: " + label)
    for pat, why in TELLS:
        for m in re.finditer(pat, body, re.I):
            if CTX.search(body[max(0, m.start() - 160):m.end() + 80]):
                continue
            frag = re.sub(r'\s+', ' ', body[max(0, m.start() - 35):m.end() + 35]).strip()
            problems[name].append(why + ": ..." + frag + "...")
    if re.search(r'\bpaste(d)? (the |your )?(list|rows|export|csv|inbox)', t, re.I) \
       and not re.search(r'\bpath\b|\bURL\b|\bfetch\b', t, re.I):
        problems[name].append("asks for a paste with no file or URL alternative")

print("QA over %d skills" % len(FILES))
counts = collections.Counter(p.split(":")[0] for ps in problems.values() for p in ps)
if counts:
    print("\nfindings by class:")
    for k, v in counts.most_common():
        print("  %4d  %s" % (v, k))
print("\nskills with at least one finding: %d/%d" % (len(problems), len(FILES)))
for n, ps in sorted(problems.items(), key=lambda x: -len(x[1])):
    print("\n  %s (%d)" % (n, len(ps)))
    for p in ps[:5]:
        print("     - " + p[:130])
sys.exit(1 if problems else 0)

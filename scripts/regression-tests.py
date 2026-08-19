"""Functional regression for the 10 arithmetic defects found by testing.
Each case: (1) recompute the fixture to show the wrong vs right answer,
(2) assert the corrective guard is present in the committed SKILL.md.
A guard that went missing = FAIL, so this catches silent reverts."""
import glob, io, os, re, sys

P = {os.path.basename(os.path.dirname(p)): p for p in glob.glob("skills/**/SKILL.md", recursive=True)}
R = {os.path.basename(p): p for p in glob.glob("references/*.md")}
fails = []


def guard(skill, needles, label):
    """every needle must appear in the skill or a reference it cites.

    Matched on word boundaries, not as a bare substring. A plain
    `"lag" in text` also matches "flag", "flags", "flagged" -- and the
    corrective guards live in prose full of the word "flag", so the
    returns-lag guard could be deleted outright while this suite still
    reported ALL GUARDS PRESENT. That is the exact silent revert the
    suite exists to catch, so the match has to respect word edges.
    """
    s = io.open(P[skill], encoding="utf-8").read()
    for c in set(re.findall(r"references/([A-Za-z0-9_.-]+\.md)", s)):
        if c in R:
            s += io.open(R[c], encoding="utf-8").read()
    low = s.lower()
    missing = [
        n for n in needles
        if not re.search(r"(?<![a-z])" + re.escape(n.lower()) + r"(?![a-z])", low)
    ]
    if missing:
        fails.append("%s [%s] missing guard: %s" % (skill, label, missing))
        return "FAIL"
    return "ok"


print("=" * 78)
print("FUNCTIONAL REGRESSION - the 10 defects found by arithmetic testing")
print("=" * 78)

# --- 1-3. anomaly detection: 3 distinct failures -------------------------
base = [100] * 20
spike = base + [400]                       # one spike
after = spike + [100] * 5                  # then normal again
mu = sum(base) / len(base)
sd = (sum((x - mu) ** 2 for x in base) / len(base)) ** 0.5 or 1
mu2 = sum(spike) / len(spike)
sd2 = (sum((x - mu2) ** 2 for x in spike) / len(spike)) ** 0.5
z_norm_after_spike = abs(100 - mu2) / sd2
print("\n1. anomaly-alert / spike poisons the baseline")
print("   baseline 100x20 -> spike 400. If the spike stays in the window,")
print("   a NORMAL 100 then scores z=%.2f against mean %.1f sd %.1f" % (z_norm_after_spike, mu2, sd2))
print("   -> normal days flagged, or real ones masked. Guard:",
      guard("anomaly-detection", ["exclude", "baseline"], "spike exclusion"))

sustained = [100] * 20 + [130] * 10        # step change, becomes the new normal
m3 = sum(sustained[-20:]) / 20
s3 = (sum((x - m3) ** 2 for x in sustained[-20:]) / 20) ** 0.5
print("\n2. anomaly-alert / sustained shift goes quiet")
print("   +30%% step change: by day 10 the rolling window has absorbed it")
print("   (mean %.1f), z=%.2f -> silent. A 30%% shift must not be silent." % (m3, abs(130 - m3) / s3))
print("   Guard:", guard("anomaly-detection", ["sustained"], "sustained shift"))

drift = [100 * (1.02 ** i) for i in range(30)]   # 2%/day compounding
zs = []
for i in range(20, 30):
    w = drift[i - 20:i]
    m = sum(w) / 20
    s = (sum((x - m) ** 2 for x in w) / 20) ** 0.5
    zs.append(abs(drift[i] - m) / s)
print("\n3. anomaly-alert / gradual drift invisible")
print("   2%%/day compounding = %.0f%% total drift, yet max daily z=%.2f"
      % ((drift[-1] / drift[0] - 1) * 100, max(zs)))
print("   -> never trips a z-threshold. Guard:",
      guard("anomaly-detection", ["drift"], "drift detection"))

# --- 4. margin-builder: missing COGS inverts the ranking -----------------
prods = [("A", 1000, 0.80), ("B", 300, 0.10), ("C", 240, 0.05)]
byrev = sorted(prods, key=lambda x: -x[1])
bymargin = sorted(prods, key=lambda x: -(x[1] * (1 - x[2])))
print("\n4. margin-builder / revenue rank != margin rank")
print("   revenue order %s vs margin order %s"
      % ([p[0] for p in byrev], [p[0] for p in bymargin]))
print("   A: $%d rev but $%d margin; B: $%d rev, $%d margin"
      % (1000, 1000 * .2, 300, 300 * .9))
print("   -> ranking on revenue promotes the worst product. Guard:",
      guard("contribution-margin", ["cogs"], "COGS required"))

# --- 5-6. inventory: censored demand + X>Y contradiction ----------------
sold, days_in_stock, days = 100, 20, 60
naive = days / (sold / days)                       # treats 60d as sellable
true_rate = sold / days_in_stock
censored = sold / days                              # observed rate
print("\n5. inventory / censored demand")
print("   sold 100 units but in stock only %d of %d days." % (days_in_stock, days))
print("   naive days-of-cover %.1f vs true %.1f (rate %.2f/d vs %.2f/d)"
      % (naive, sold / true_rate / (sold / days_in_stock) * 0 + (sold / true_rate), true_rate, censored))
print("   -> stockouts read as low demand and get under-ordered. Guard:",
      guard("inventory-planning", ["out of stock"], "censored demand"))

# --- 7. shipping band boundaries ---------------------------------------
print("\n6. shipping bands / boundary ownership")
print("   a 5.00kg order with bands '0-5' and '5-10' matches both or neither.")
print("   Guard:", guard("shipping-cost-analysis", ["inclusive", "exclusive"], "band boundaries"))

# --- 8. cohort partial cells -------------------------------------------
# same true churn, but the newest cohort's month is only 40% elapsed
full = [1000, 700, 560, 476]
part_elapsed = 0.4
observed_last = 700 - (700 - 560) * part_elapsed
r_full = 560 / 700
r_part = observed_last / 700
print("\n7. cohort-tracker / partial period fakes improvement")
print("   month-2 retention: complete %.1f%% vs partial-cell %.1f%%  = +%.1fpp"
      % (r_full * 100, r_part * 100, (r_part - r_full) * 100))
print("   churn is IDENTICAL - the cell just isn't finished. Guard:",
      guard("cohort-analysis", ["partial"], "partial period"))

# --- 9. promo baseline contamination ------------------------------------
pre = [100, 100, 100, 160, 100]     # day 4 = a prior promo
promo_wk = 150
naive_lift = promo_wk / (sum(pre) / len(pre)) - 1
clean_lift = promo_wk / (sum([100, 100, 100, 100]) / 4) - 1
print("\n8. promo-impact / contaminated baseline")
print("   baseline containing a prior promo: lift reads %.1f%% vs clean %.1f%%"
      % (naive_lift * 100, clean_lift * 100))
print("   -> understates, and can flip pull-forward into 'positive'. Guard:",
      guard("promotional-campaigns", ["baseline"], "clean baseline"))

# --- 10. returns lag + benchmark annualisation --------------------------
shipped_recent, returns_seen, lag_share = 1000, 20, 0.45   # 45% of returns land by now
naive_rate = returns_seen / shipped_recent
adj_rate = (returns_seen / lag_share) / shipped_recent
print("\n9. returns / lag bias")
print("   %d returns on %d shipped = %.1f%% naive, but only %.0f%% of returns have landed"
      % (returns_seen, shipped_recent, naive_rate * 100, lag_share * 100))
print("   true ~%.1f%% -> bias %.1fpp, and the sign flips vs older cohorts. Guard:"
      % (adj_rate * 100, (adj_rate - naive_rate) * 100),
      guard("ecommerce-returns", ["lag"], "returns lag"))

m = 0.05
print("\n10. benchmark / multiply-annualisation")
print("    5%%/month compounded = %.0f%% a year, not 5x12=%d%%"
      % (((1 + m) ** 12 - 1) * 100, m * 12 * 100))
print("    Guard:", guard("benchmark-analysis", ["compound"], "compounding"))

print()
print("=" * 78)
if fails:
    print("REGRESSIONS: %d" % len(fails))
    for f in fails:
        print("  - " + f)
    sys.exit(1)
print("ALL GUARDS PRESENT - no silent reverts")

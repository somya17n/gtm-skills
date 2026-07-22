# Marketing Plan Framework

Reference for the parts of a comprehensive marketing plan that aren't already covered by `strategy-frameworks.md` (maturity stages, growth lever hierarchy, engagement archetypes, ICE scoring, and the quarterly Big Bet/Medium Bet structure — read that file too, this one doesn't repeat it) or `funnel-benchmarks.md` (AARRR stage definitions and conversion benchmarks — reuse the Product Funnel table there for stage definitions).

---

## Current-State Audit Rubric

Score the business 0-5 on each dimension before planning what's next. This is the plan's "where are we" section — be honest, a 2 written down is more useful than a 4 that isn't real.

| Dimension | 0-1 (Absent) | 2-3 (Partial) | 4-5 (Solid) |
|-----------|-------------|---------------|-------------|
| Positioning clarity | No documented category claim or differentiation | Exists but inconsistent across channels | Documented, consistent, and defensible against the next-best alternative |
| ICP definition | "Anyone who'll pay" | A rough persona, not evidence-based | Evidence-based persona(s) from `customer-research` with confidence levels |
| Brand voice | Undocumented, varies by writer | Informal guidelines, not enforced | Documented voice profile (`brand-voice`) applied consistently |
| Funnel instrumentation | No tracked conversion data | Some stages tracked, gaps between them | Full funnel tracked stage-to-stage with cohort visibility |
| Acquisition channel mix | One channel, undiversified | 2-3 channels, one dominant (>60% of volume) | 3+ channels, no single channel over 60%, mix matches ICP |
| Activation/onboarding | No defined aha moment | Aha moment guessed, not validated | Validated aha moment, measured activation rate, drop-off diagnosed |
| Retention program | Reactive only (respond to churn after it happens) | Some lifecycle email, not systematic | Systematic lifecycle program with churn-prevention triggers |
| Pricing/packaging | Set once, never revisited | Copied from a competitor | Value-metric-aligned, tested, revisited on a cadence |
| Competitive positioning | No named alternative addressed anywhere — "we're just better" with nothing to be better *than* | Competitors named informally, no documented answer to "why not them" | Documented, defensible answer to the specific named alternative(s) the ICP actually considers, consistent across sales and marketing surfaces |
| Messaging clarity | A visitor/prospect can't repeat back what the product does after reading the homepage | Message exists but varies by who's writing it that week | One core message, consistent across homepage/deck/sales script, specific enough to fail a generic-company test |
| Paid acquisition maturity | No paid channel running, or running with no tracked CAC | One paid channel live, CAC tracked inconsistently or not benchmarked against payback target | Multiple paid channels with tracked, benchmarked CAC and a clear kill/scale rule per channel |

**Scoring notes:** score from whatever materials exist (mark "scored from materials, not verified with the team" where you had to infer). A dimension scoring 0-1 is the highest-priority gap regardless of how exciting the opportunity above it looks — an unmeasured funnel makes every other recommendation a guess.

---

## Setting the Marketing Budget

Two methods — use whichever the available data supports, and say explicitly which one you used:

**1. Revenue-based (5-40% of ARR)**
Start from a comfortable spend level as a % of current ARR, forecast the resulting pipeline/revenue from historical CAC. Best when the business has enough history to know its actual CAC.

**2. Goal-based (reverse-engineered from a revenue target)**
```
Budget = [(New ARR target / (ARPC × 12)) × CAC] / annual retention rate
```
Best when the goal is fixed (e.g. a fundraising or board target) and the budget needs to justify hitting it.

**Always add 10-20% on top as an experimental budget** — this is what funds testing the next channel before the current one saturates or plateaus, and it should never be the first thing cut.

If CAC is unknown, say so explicitly in the plan's open-decisions section rather than guessing — every revenue projection downstream depends on this number being real.

### Allocating the Budget Across AARRR Stages

A total budget figure is not an allocation. Split it using the maturity stage from `strategy-frameworks.md` — the right split shifts hard as the business matures, and applying an early-stage split to a later-stage business (or vice versa) is a common, avoidable mistake:

| Maturity stage | Acquisition | Activation | Retention | Referral | Revenue/Expansion |
|---|---|---|---|---|---|
| Pre-PMF / early ($0-10K ARR) | 60-70% | 20-30% | 5-10% | 0-5% | 0-5% |
| Finding repeatable motion ($10K-100K ARR) | 45-55% | 20-25% | 15-20% | 5-10% | 5-10% |
| Scaling a working motion ($100K-1M ARR) | 35-45% | 15-20% | 20-25% | 10-15% | 10-15% |
| Post-PMF, expansion-focused ($1M+ ARR) | 25-35% | 10-15% | 25-30% | 15-20% | 15-20% |

The direction that matters more than the exact numbers: acquisition's share shrinks and retention/expansion's share grows as the business matures, because a leaky bucket makes every acquisition dollar spent on it worth less over time. A team still spending a pre-PMF split at $500K ARR is very likely underinvesting in retention.

## Funding-Stage Capability Unlocks

What a plan can responsibly assume the team can execute changes with funding stage. Use these as anchors, adjusted for category (consumer/ecommerce can typically spend more; deep-tech B2B typically less):

| Stage | Typical monthly marketing spend | What unlocks |
|-------|----------------------------------|---------------|
| Pre-seed / bootstrapped | $0-2K | Organic only — no paid acquisition assumption |
| Seed close | $5-15K | First paid test budget, first dedicated marketing hire |
| Seed deployment | $20-50K | Second marketing hire, first real paid channel investment |
| Series A | $50-150K | Performance + content + design headcount, international consideration |
| Series B+ | $150K+ | Brand campaigns, PR agency, full-stack marketing org |

A plan that recommends a $30K/mo paid strategy for a pre-seed team with $0 marketing budget isn't ambitious — it's not executable, and it should be flagged as a Series-A-stage move instead.

### Channel Benchmarks by Stage

Which channels are even worth testing shifts by stage — a channel that's rational at Series B (paid, with a team to run it and a CAC payback model to protect) is usually a waste of a pre-seed team's only budget:

| Stage | Channels worth testing | Channels to avoid until later | Realistic CAC payback target |
|---|---|---|---|
| Pre-seed / bootstrapped | Founder-led content, community, organic social, direct outbound | Paid ads (no budget to survive the learning curve), PR/agency | N/A — no paid spend to pay back |
| Seed | First organic SEO push, founder-led sales, early referral loop | Broad paid ads, brand campaigns | Under 6 months if any paid tested |
| Series A | Performance paid (search/social), content at scale, first partnerships | National brand campaigns, offline/events at scale | 12-18 months |
| Series B+ | Brand campaigns, PR, events, multi-channel paid, international expansion | — (most channels are now viable, the constraint shifts to sequencing) | 18-24 months, category-dependent |

Use this to sanity-check the AARRR plan's channel choices against the funding-stage capability table above — a Series A plan proposing brand campaigns is over-scoped for the stage; a Series B plan still only testing founder-led content is under-scoped.

## The 90-Day Roadmap Phases

Structure the first 90 days into four phases rather than a flat task list — sequencing matters more than the individual tactics:

| Phase | Weeks | Focus |
|-------|-------|-------|
| Unblock | 1-2 | Remove whatever is currently preventing execution — missing instrumentation, undefined ICP, no brand voice doc. Nothing else matters until these are cleared. |
| Foundation | 3-4 | Stand up the systems the rest of the plan depends on — tracking, the content/campaign calendar, the lifecycle program skeleton |
| Velocity | 5-8 | Execute the highest-ICE-scored initiatives (pull ICE scoring from `strategy-frameworks.md`) at full pace |
| Compound | 9-12 | Double down on what worked in Velocity, kill what didn't, start the next quarter's Big Bet hypothesis |

Every roadmap item should be tagged with the AARRR stage it serves (see `funnel-benchmarks.md`'s Product Funnel table) and have a named owner — an action without an owner doesn't happen.

## What Makes a Plan Specific vs. Generic

A plan fails if it could apply to any company in the category. Every plan must be anchored in the specific business's real numbers:
- Actual current budget, broken down by line (paid, tools, headcount, retainers) — not an industry-average guess
- Actual team composition — who touches marketing today, and what they own
- Actual current channels and their real status (working / not working / untested) — not a generic channel list
- What's already been tried, including what failed and why — don't recommend something they already tried and dropped without addressing why it didn't work
- The specific phase of growth ($0-10K ARR grueling-early, $10K-100K treacherous-middle, $100K-1M acceleration, $1M+) — each phase has a different binding constraint

## Open Decisions — Don't Gloss Over Them

Every plan will have gaps. List them explicitly in a closing section rather than quietly assuming an answer:
- Unknown CAC — the highest-impact one, since every projection depends on it
- Unvalidated activation event
- Untested pricing/packaging
- Team capacity questions (can the current team execute this, or does it require a hire the budget doesn't yet support)

Naming a gap is more useful to the reader than a confident-sounding guess that turns out wrong three months in.

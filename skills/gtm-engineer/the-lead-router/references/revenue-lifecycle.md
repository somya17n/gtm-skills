# Revenue Lifecycle Reference

Reference for the `revops` skill: lifecycle stage definitions, MQL scoring model, routing logic, and the speed-to-lead benchmark curve.

---

## Lifecycle Stages (sales-led / hybrid motion)

| Stage | Entry Criteria | Exit Criteria | Owner |
|---|---|---|---|
| Subscriber | Opts into content (newsletter, blog) | Provides company info or shows repeat engagement | Marketing |
| Lead | Identified contact with basic info | Meets minimum fit criteria | Marketing |
| MQL | Passes fit + engagement threshold | Sales accepts or rejects within SLA | Marketing |
| SQL | Sales accepts and confirms via conversation | Opportunity created or recycled | Sales (SDR/AE) |
| Opportunity | Budget, authority, need, timeline confirmed | Closed-won or closed-lost | Sales (AE) |
| Customer | Closed-won | Expands, renews, or churns | CS |

### PLG variant

Replace MQL/SQL with **Product-Qualified Lead (PQL)**, triggered by a usage threshold (e.g., invited a teammate, hit a usage cap, used a specific feature) rather than a marketing engagement score. Route PQLs directly to sales when the usage signal indicates expansion or upgrade intent; skip the marketing-qualification step entirely.

---

## MQL Scoring, Worked Example

**Fit signals** (who they are, max 50 points)
| Signal | Points |
|---|---|
| Company size in target range | 15 |
| Industry match | 10 |
| Job title/seniority match | 15 |
| Known tech stack match | 10 |

**Engagement signals** (what they do, max 50 points)
| Signal | Points |
|---|---|
| Pricing page visit | 15 |
| Demo/trial request | 20 |
| 3+ site visits in 14 days | 10 |
| Webinar attendance | 5 |

**Negative signals** (subtract)
| Signal | Points |
|---|---|
| Competitor email domain | -30 |
| Personal/free email on a B2B ICP | -10 |
| Unsubscribed or marked spam | -50 (auto-disqualify) |

**Threshold:** 50-80 combined points, calibrated against closed-won history, pull last quarter's won deals and check what score they'd have gotten with the model before locking the threshold.

**Recalibration:** quarterly. Buyer behavior shifts; a model tuned once and never revisited drifts stale within two quarters.

---

## Routing Methods

| Method | How it works | Best for |
|---|---|---|
| Round-robin | Even distribution across reps | Equal territories, similar deal sizes |
| Territory-based | Assign by geography, vertical, or segment | Regional teams, industry specialists |
| Account-based | Named accounts to named reps | ABM motions, strategic accounts |
| Skill-based | Route by deal complexity or product line | Diverse product lines, global teams |

Rules that apply regardless of method:
- Route to the most specific match first, fall back to general
- Always define a fallback owner, unassigned leads go cold fast
- Round-robin should account for rep capacity (PTO, quota already hit)
- Log every routing decision, needed to audit and re-tune later

---

## Speed-to-Lead Benchmark Curve

| Response time | Relative qualification likelihood |
|---|---|
| Within 5 minutes | ~21x more likely to qualify than a 30+ minute response |
| Within 30 minutes | baseline |
| After 30 minutes | conversion drops roughly 10x vs. the 5-minute response |
| After 24 hours | lead is effectively cold |

Design rule: alert the assigned rep immediately on MQL creation, and escalate automatically if the SLA is missed (default recommendation: 4 business hours to first contact, 48 hours to qualify-or-reject).

---

## Pipeline Stage Hygiene (post-opportunity)

Lifecycle stages above cover lead-to-opportunity. Once an opportunity exists, it needs its own hygiene rules or "pipeline health" becomes a guess:

| Stage | Required Fields Before Advancing | Exit Criteria |
|---|---|---|
| Qualified | Contact, company, source, fit score | Discovery call scheduled |
| Discovery | Confirmed pain, current solution, timeline | Needs confirmed, demo scheduled |
| Demo/Evaluation | Technical requirements, decision-maker(s) identified | Positive evaluation, proposal requested |
| Proposal | Pricing, terms, stakeholder map | Proposal delivered and reviewed |
| Negotiation | Redlines tracked, approval chain started, close date set | Terms agreed, contract sent |
| Closed Won | Signed contract, payment terms confirmed | Handoff to CS complete |
| Closed Lost | Loss reason logged, competitor named if applicable | Post-mortem logged |

**Hygiene rules to enforce, not just define:**
- **Required-field gate**, a rep cannot advance a deal to the next stage with required fields blank. This is what turns the table above from documentation into an actual control.
- **Stale-deal flag**, flag any deal sitting in one stage beyond roughly 2x the average time-in-stage for deals that eventually closed won. A deal in Demo for 40 days against a 15-day average close-won pattern is a flag, not a coincidence.
- **Stage-skip detection**, flag deals that jump stages (Qualified straight to Proposal, skipping Discovery) since skipped discovery is the single most common cause of late-stage deals collapsing on undiscovered objections.
- **Close-date discipline**, a pushed close date requires a logged reason. A silently-pushed date with no reason is a forecast lying to itself.

---

## Deal Desk (when a deal needs approval, not just tracking)

Most orgs need this earlier than they think, as soon as a rep can offer a discount deep enough to change unit economics.

**When to stand this up:** ACV above roughly $25K (adjust to the business's actual deal-size distribution), non-standard payment terms (net-90, quarterly-only billing), multi-year contracts with custom pricing, or custom legal/SLA terms.

**Approval tiers by discount depth**, calibrate the exact bands to the business's real margin structure, but the shape holds broadly:

| Discount / Deal Characteristic | Approval Required |
|---|---|
| Standard published pricing | Auto-approved, no review |
| 10-20% discount | Sales manager |
| 20-40% discount | VP Sales |
| 40%+ discount, or any custom/non-standard terms | Deal desk review |
| Multi-year or enterprise custom contract | Finance + Legal |

**Exception tracking:** log every non-standard term granted, not just the approval outcome. If the same "exception" gets requested repeatedly, that's a signal it should become a standard published option, review the exception log quarterly rather than re-litigating the same one-off every time it comes up.

---

## Three-View Metrics Dashboard

A single revops dashboard trying to serve a rep, a manager, and an exec at once serves none of them well, each needs a different grain and different metrics:

**Rep view**, deal-level, actionable today: my open deals by stage, deals with a stale-deal flag, deals missing required fields, tasks due today, leads assigned to me still inside the SLA window.

**Sales manager view**, team-level, this week/month: pipeline coverage ratio (target 3-4x quota), stage conversion rates by rep, average time-in-stage by rep, SLA-miss count by rep, forecast accuracy vs. last quarter's commit.

**Executive view**, company-level, this quarter: CAC, LTV:CAC ratio (target 3:1 to 5:1), pipeline velocity (deals x avg deal size x win rate / sales cycle length), revenue vs. target, pipeline coverage trend quarter over quarter.

Building one dashboard with every metric and letting each audience ignore what doesn't apply to them is the common failure mode, it produces a dashboard nobody actually opens because everyone has to filter past metrics meant for someone else's job.

---

## Core Metrics & Healthy Ranges

| Metric | Formula | Healthy range |
|---|---|---|
| Lead-to-MQL rate | MQLs / total leads | 5-15% |
| MQL-to-SQL rate | SQLs / MQLs | 30-50% |
| SQL-to-Opportunity rate | Opportunities / SQLs | 50-70% |
| Speed-to-lead | Time from form fill to first rep contact | Under 5 minutes ideal, under 1 hour acceptable |
| Win rate | Closed-won / total opportunities | 20-30% (varies heavily by ACV and motion) |

If a number falls well outside these ranges, the fix is usually one of: the MQL threshold is miscalibrated (too loose → low MQL-to-SQL; too strict → low lead-to-MQL), the routing has a silent unassigned bucket, or the SLA isn't actually enforced (defined on paper, ignored in practice).

---

## Speed to Lead

The single best-evidenced number in lead management, and the one most consistently missed.

**What the speed buys:**

- Responding **under 5 minutes** carries roughly **100x** the odds of qualifying a lead against waiting
  30 minutes. This is why 5 minutes is the standard SLA rather than an aspiration.
- Responding **within 1 minute** has been measured at around **+391%** conversion against responding
  after 2 minutes. The curve is steepest at the very start, so the first minutes are not a rounding
  difference.
- There is roughly a **2.6x close-rate difference** between the fastest and slowest responder tiers.

**What actually happens:**

- Around **74%** of businesses miss the five-minute window entirely.
- In one study of 1,000 companies, **63.5% never responded at all**, and those that did averaged over
  **29 hours**.

The gap between the evidence and the practice is the opportunity: this is not a subtle optimisation,
it is a majority of competitors not answering.

**What closes the gap:**

- **A written SLA nearly doubles compliance.** About **54.9%** of companies with a defined SLA respond
  within 15 minutes, against **29.5%** without one. The document is the intervention, because it makes
  the miss visible and assignable.
- **Routing delay is itself a major cause.** Around **29%** of organisations name lead-routing delays as
  a major contributor to slow first response. A perfect SLA on paper fails if the lead sits unassigned,
  so routing latency has to be measured separately from rep responsiveness. Splitting those two is what
  tells you whether you have a process problem or a people problem.
- **Automated assignment outperforms manual.** Roughly **62.5%** of companies using automated routing
  meet an under-15-minute standard against **39.1%** of manual-only ones.

**Design consequences:**

- Set the SLA in **minutes**, and measure from lead creation, not from assignment. Measuring from
  assignment hides exactly the delay that matters.
- Instrument **two clocks**: creation → assignment, and assignment → first touch. Report them
  separately.
- Define what happens when the SLA is missed, and by whom. An SLA with no escalation is a target, not
  an agreement.
- Cover the hours the leads actually arrive. A five-minute SLA that applies only in business hours is
  an overnight queue with a fast morning.

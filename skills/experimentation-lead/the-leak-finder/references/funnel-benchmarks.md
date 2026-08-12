# Funnel Analysis

Reference for funnel types, stage-by-stage conversion benchmarks, drop-off diagnosis, optimization levers, funnel math formulas, and cohort-based funnel analysis.

---

## Funnel Types

### Marketing Funnel

Tracks the customer journey from awareness through conversion.

```
Awareness → Consideration → Conversion
    |             |              |
  Brand         Content        Purchase
  exposure     engagement      / signup
```

| Stage | Definition | Key Metrics |
|-------|-----------|------------|
| **Awareness** | Prospect knows your brand exists. Reached through ads, content, PR, word-of-mouth. | Impressions, reach, brand searches, direct traffic |
| **Consideration** | Prospect actively evaluating your solution. Engaging with content, comparing options. | Website visits, content downloads, webinar attendance, email signups |
| **Conversion** | Prospect takes the desired action: purchases, signs up, or requests demo. | Conversion rate, signups, purchases, demo requests |

### Sales Funnel

Tracks the progression of leads through the sales process.

```
Lead → MQL → SQL → Opportunity → Won
  |      |     |       |           |
 Raw   Marketing  Sales  Active   Closed
 lead  qualified  qual.  deal     deal
```

| Stage | Definition | Key Metrics |
|-------|-----------|------------|
| **Lead** | Any contact who has expressed interest or been identified as a potential customer | Lead volume, lead source, cost per lead |
| **MQL** (Marketing Qualified Lead) | Lead that meets marketing qualification criteria (score threshold, engagement level) | MQL volume, lead-to-MQL rate, MQL velocity |
| **SQL** (Sales Qualified Lead) | MQL accepted by sales after initial qualification (BANT/MEDDIC basics met) | SQL volume, MQL-to-SQL rate, acceptance rate |
| **Opportunity** | SQL with an active deal in the pipeline (proposal stage or beyond) | Opportunity count, SQL-to-opportunity rate, pipeline value |
| **Won** | Closed deal with signed contract and revenue recognition | Won count, opportunity-to-won rate, revenue, deal size |

### Product Funnel (AARRR / Pirate Metrics)

Tracks the user lifecycle within a product.

```
Signup → Activation → Retention → Expansion → Referral
   |         |            |           |           |
 Create    First       Repeat     Upgrade      Invite
 account   value       usage      / expand     others
```

| Stage | Definition | Key Metrics |
|-------|-----------|------------|
| **Signup** | User creates an account or starts a trial | Signups, signup rate, cost per signup |
| **Activation** | User completes the key action that delivers first value (aha moment) | Activation rate, time to activation, activated users |
| **Retention** | User returns and continues using the product | DAU/MAU, retention curve, churn rate |
| **Expansion** | User upgrades plan, adds seats, or increases usage | Expansion MRR, upsell rate, ARPU growth |
| **Referral** | User refers others to the product | Referral rate, viral coefficient, referred signups |

---

## Stage-by-Stage Conversion Benchmarks

### SaaS Marketing Funnel

| Conversion | Poor | Below Average | Average | Good | Excellent |
|-----------|------|---------------|---------|------|-----------|
| Visitor → Lead | < 1% | 1-2% | 2-3% | 3-5% | > 5% |
| Lead → MQL | < 10% | 10-15% | 15-20% | 20-25% | > 25% |
| MQL → SQL | < 20% | 20-30% | 30-35% | 35-40% | > 40% |
| SQL → Opportunity | < 40% | 40-50% | 50-55% | 55-60% | > 60% |
| Opportunity → Won | < 15% | 15-20% | 20-25% | 25-30% | > 30% |

**End-to-end:** Visitor → Won: 0.02-0.5% (typical SaaS)

### E-commerce Funnel

| Conversion | Poor | Below Average | Average | Good | Excellent |
|-----------|------|---------------|---------|------|-----------|
| Visitor → Product Page | < 30% | 30-40% | 40-50% | 50-60% | > 60% |
| Product Page → Add to Cart | < 5% | 5-8% | 8-12% | 12-15% | > 15% |
| Add to Cart → Checkout | < 40% | 40-50% | 50-60% | 60-70% | > 70% |
| Checkout → Purchase | < 50% | 50-60% | 60-70% | 70-80% | > 80% |

**End-to-end:** Visitor → Purchase: 1-5% (typical e-commerce)

### B2B Sales Funnel

| Conversion | Poor | Below Average | Average | Good | Excellent |
|-----------|------|---------------|---------|------|-----------|
| Lead → Qualified | < 10% | 10-15% | 15-20% | 20-25% | > 25% |
| Qualified → Demo | < 30% | 30-40% | 40-45% | 45-50% | > 50% |
| Demo → Proposal | < 40% | 40-45% | 45-55% | 55-60% | > 60% |
| Proposal → Closed-Won | < 20% | 20-25% | 25-30% | 30-35% | > 35% |

**End-to-end:** Lead → Closed-Won: 1-5% (typical B2B)

### SaaS Product Funnel

| Conversion | Poor | Below Average | Average | Good | Excellent |
|-----------|------|---------------|---------|------|-----------|
| Signup → Activated | < 20% | 20-30% | 30-40% | 40-50% | > 50% |
| Activated → Week 2 Retention | < 30% | 30-40% | 40-50% | 50-60% | > 60% |
| Week 2 → Month 3 Retention | < 20% | 20-30% | 30-40% | 40-50% | > 50% |
| Free → Paid Conversion | < 2% | 2-5% | 5-10% | 10-15% | > 15% |
| Paid → Annual Plan | < 20% | 20-30% | 30-40% | 40-50% | > 50% |

---

## Additional Benchmark Ranges (Directional)

These are illustrative ranges for calibration against the stage-by-stage table above, not benchmarks tied to a specific published study. Actual figures vary significantly by industry, price point, funnel definition, and company maturity, and no single authoritative source ties an exact number to any of these metrics. Treat everything below as directional, not guaranteed: sanity-check your own data against the shape of the range, not the specific figure.

### SaaS Product Funnel

| Metric | Directional Range | Notes |
|--------|---------------|-------|
| Activation rate (overall) | roughly 30-40% | "Activated" = first meaningful action, not just login |
| Activation rate - PLG products | tends to run lower | Self-serve tends to attract more casual signups |
| Activation rate - Sales-led | tends to run higher | Sales-assisted onboarding tends to drive more completion |
| Free trial → paid (opt-in trial) | roughly 15-25% | Opt-in = credit card required upfront; varies a lot by category |
| Free trial → paid (opt-out trial) | roughly 40-55% | Opt-out = no card required, charged after trial; varies a lot by category |
| Freemium → paid | roughly 2-5% | Varies significantly by product category and price point |
| Week-1 retention (Day 7) | roughly 25-40% | Users still active on Day 7 of signup cohort |
| Month-1 retention (Day 30) | roughly 15-25% | Typical for SaaS without a strong onboarding flow |
| Net Revenue Retention (NRR) | roughly 100-110% median | Varies heavily by segment and pricing model |
| NRR - top quartile | 120%+ | Strong expansion revenue offsetting churn |
| CAC payback period | roughly 12-18 months | Time to recoup acquisition cost from MRR; varies by ACV |
| DAU/MAU ratio (B2B SaaS) | roughly 15-30% | How "sticky" the product is; higher end is generally considered good |

### E-commerce Funnel

| Metric | Directional Range | Notes |
|--------|---------------|-------|
| Cart abandonment rate | commonly cited in the high-60s to low-70s percent range | Varies by category, checkout flow, and traffic source |
| Cart abandonment - mobile | tends to run notably higher than desktop | Mobile checkout friction is a common driver |
| Overall ecommerce CVR (desktop) | roughly 2-3% | Varies widely by traffic quality and category |
| Overall ecommerce CVR (mobile) | roughly 1-2% | Mobile tends to convert lower than desktop |
| Abandoned cart email CVR (average) | roughly 3-4% | Conversion rate of abandoned cart email recipients |
| Abandoned cart email CVR (top performers) | can run meaningfully higher | Segmentation and timing are the usual levers |
| Welcome flow CVR | roughly 3-5% | Purchases within 30 days of welcome email |
| Win-back email CVR | roughly 1.5-2.5% | For lapsed customer reactivation |

**By industry:** conversion rates vary meaningfully across categories. High-consideration or low-frequency purchase categories (electronics, automotive parts) tend to convert lower than habitual or lower-price categories (food & beverage, beauty). There's no single authoritative source tying an exact percentage to each category, so treat any category comparison as directional, not a benchmark to cite.

### B2B Sales Funnel

| Metric | Directional Range | Notes |
|--------|---------------|-------|
| Overall B2B win rate | roughly 15-25% | Varies heavily by deal size, category, and competitive intensity |
| Win rate - SMB deals | tends to run higher | Shorter cycle, lower complexity |
| Win rate - Enterprise deals | tends to run lower | Longer cycle, more competition |
| Demo → close rate | roughly 20-30% | Varies by product and sales motion |
| Lead → MQL conversion | often lower than teams expect | Definitions of MQL vary enormously across companies |
| MQL → SQL conversion | roughly 40-60% | Of MQLs that are actually reviewed by sales |
| Average sales cycle | roughly 60-120 days | Varies heavily by ACV and buying committee size |
| Sales cycle - SMB (<$10K ACV) | roughly 20-45 days | |
| Sales cycle - Mid-Market ($10-50K) | roughly 45-90 days | |
| Sales cycle - Enterprise ($50K+) | roughly 90-180+ days | |

---

## Drop-Off Diagnosis Framework

When conversion drops between stages, diagnose the root cause using these four categories.

### 1. Friction (UX and Process)

The user wants to proceed but the process makes it difficult.

| Signal | Examples |
|--------|---------|
| High abandonment on specific form fields | "Phone number required" causing 30% drop |
| Long load times on checkout pages | > 3 second load = 53% bounce increase |
| Confusing navigation or unclear next steps | Users clicking back or visiting help pages |
| Too many steps in the process | Each additional step loses 10-20% |
| Mobile-unfriendly experience | Mobile conversion < 50% of desktop conversion |

**Fixes:** Reduce form fields, optimize page speed, simplify flows, improve mobile UX, add progress indicators.

### 2. Motivation (Messaging and Value)

The user is not sufficiently convinced that the next step is worth their effort.

| Signal | Examples |
|--------|---------|
| High bounce on landing pages despite traffic | Page messaging does not match ad promise |
| Users reading content but not acting | Value proposition is not compelling enough |
| Low email click-through rates | CTA or offer is not motivating |
| Abandoned demos after attending | Demo did not address their specific pain |
| Price page exits without trial/purchase | Price-value gap too large |

**Fixes:** Align messaging to pain points, strengthen value proposition, add social proof, improve demo personalization, test pricing presentation.

### 3. Ability (Complexity and Capability)

The user does not have the skills, resources, or information to proceed.

| Signal | Examples |
|--------|---------|
| Incomplete onboarding flows | Product requires technical skills users lack |
| Support tickets during signup/checkout | Users confused about requirements |
| Repeated failed attempts | Technical integration barriers |
| Long time in a stage without progression | Evaluating but unable to build internal case |
| Feature complexity overwhelming new users | Too many options, no guided path |

**Fixes:** Simplify setup, provide wizards and templates, offer onboarding support, create getting-started guides, reduce initial feature exposure.

### 4. Timing (Urgency and Readiness)

The user is interested but the timing is not right.

| Signal | Examples |
|--------|---------|
| Leads who engage but stall | "Not this quarter" responses |
| High return visitor rates without conversion | Coming back but not ready to commit |
| Seasonal patterns in conversion | Industry-specific buying cycles |
| Long time between first visit and conversion | Extended consideration periods |
| Budget cycle misalignment | Prospect's fiscal year does not align |

**Fixes:** Long-term nurture sequences, trigger-based re-engagement, urgency mechanisms (limited offers, expiring trials), quarterly check-ins, fiscal year-aligned campaigns.

---

## Optimization Levers per Stage

### Top of Funnel (Volume + Targeting)

| Lever | Description | Impact |
|-------|-------------|--------|
| Channel diversification | Expand to new acquisition channels | More volume, reduce channel dependency |
| Audience targeting refinement | Tighter ICP targeting in paid campaigns | Higher quality leads, lower CAC |
| Content optimization | SEO, content marketing, thought leadership | Organic traffic growth, lower CAC over time |
| Referral programs | Incentivize existing customers to refer | High-quality leads at low cost |
| Brand awareness | PR, sponsorships, community presence | Larger addressable top-of-funnel |
| Ad creative testing | Test new angles, formats, messaging | Improved click-through rates |

### Mid Funnel (Nurturing + Content)

| Lever | Description | Impact |
|-------|-------------|--------|
| Lead scoring refinement | Better identification of sales-ready leads | Higher MQL-to-SQL conversion |
| Email nurture sequences | Automated drip campaigns for education | Move leads through consideration |
| Content personalization | Segment-specific content delivery | Higher engagement and progression |
| Retargeting campaigns | Re-engage visitors who did not convert | Recover lost traffic |
| Webinars and events | Educational events for consideration-stage leads | Build trust, demonstrate expertise |
| Case studies and social proof | Industry-specific success stories | Address objections, build confidence |

### Bottom of Funnel (Friction Reduction + Urgency)

| Lever | Description | Impact |
|-------|-------------|--------|
| Checkout optimization | Reduce steps, guest checkout, save cart | Reduce cart abandonment |
| Trial experience improvement | Better onboarding, faster time-to-value | Higher trial conversion |
| Pricing page optimization | Clearer plans, FAQ, objection handling | Reduce pricing page exits |
| Live chat / sales assist | Real-time help during evaluation | Remove blockers instantly |
| Limited-time offers | Discounts, bonuses, or trial extensions with deadlines | Create urgency to act now |
| Risk reversers | Money-back guarantees, free trials, no commitment | Reduce perceived risk |

---

## Funnel Math Formulas

### Required Volume Calculator

To calculate how many inputs you need at the top of the funnel to achieve a target output at the bottom:

```
Required Top-of-Funnel = Target Bottom-of-Funnel / (Stage 1 Rate × Stage 2 Rate × ... × Stage N Rate)
```

**Example — SaaS:**

Target: 10 new customers per month

```
Visitor → Lead:    3% conversion
Lead → MQL:        20% conversion
MQL → SQL:         35% conversion
SQL → Opportunity: 55% conversion
Opportunity → Won: 25% conversion

Required visitors = 10 / (0.03 × 0.20 × 0.35 × 0.55 × 0.25)
                  = 10 / 0.000289
                  = 34,602 visitors per month
```

### Stage Improvement Impact Calculator

What happens if you improve conversion at one stage?

```
Current: 34,602 visitors → 10 customers (full funnel above)

If Lead → MQL improves from 20% to 25%:
  New requirement = 10 / (0.03 × 0.25 × 0.35 × 0.55 × 0.25)
                  = 10 / 0.000361
                  = 27,701 visitors needed (20% reduction)

OR keeping the same 34,602 visitors:
  New customers = 34,602 × 0.03 × 0.25 × 0.35 × 0.55 × 0.25
                = 12.5 customers (25% improvement)
```

### Revenue Per Funnel Stage

```
Revenue per visitor  = ARPU × End-to-end conversion rate
Revenue per lead     = ARPU × (Lead → Won conversion rate)
Revenue per MQL      = ARPU × (MQL → Won conversion rate)
Revenue per SQL      = ARPU × (SQL → Won conversion rate)
Revenue per opp      = ARPU × Win rate

Example (ARPU = $500/mo, 12-month LTV = $6,000):
  Revenue per visitor = $6,000 × 0.000289 = $1.73
  Revenue per lead    = $6,000 × 0.00963  = $57.75
  Revenue per MQL     = $6,000 × 0.04813  = $288.75
  Revenue per SQL     = $6,000 × 0.1375   = $825.00
  Revenue per opp     = $6,000 × 0.25     = $1,500.00
```

---

## Cohort-Based Funnel Analysis

### What It Is

Instead of looking at aggregate funnel conversion rates, break down funnels by acquisition cohort to compare performance across time.

### Why It Matters

- Reveals whether funnel performance is improving or declining over time
- Shows the impact of product/marketing changes on specific cohorts
- Identifies seasonal patterns in conversion
- Separates growth from efficiency gains

### How to Build

1. **Define cohorts:** Group users by the week or month they entered the funnel
2. **Track each cohort** through every funnel stage
3. **Calculate conversion rates** per stage per cohort
4. **Compare across cohorts** to identify trends

### Cohort Funnel Matrix Example

```
Cohort    | Visitor→Lead | Lead→MQL | MQL→SQL | SQL→Opp | Opp→Won | End-to-End
----------|-------------|---------|---------|---------|---------|----------
Jan 2024  |    2.8%     |  18%    |  32%    |  52%    |  22%    |  0.019%
Feb 2024  |    3.1%     |  19%    |  33%    |  54%    |  24%    |  0.025%
Mar 2024  |    3.0%     |  21%    |  35%    |  53%    |  25%    |  0.029%
Apr 2024  |    3.3%     |  22%    |  36%    |  55%    |  26%    |  0.036%
May 2024  |    3.5%     |  23%    |  37%    |  56%    |  27%    |  0.042%
```

**Reading this matrix:**
- Visitor→Lead improving: marketing targeting is getting better
- Lead→MQL improving: lead scoring refinement is working
- MQL→SQL improving: better alignment between marketing and sales
- End-to-end improving month-over-month: overall funnel health is strong

### Segmentation Dimensions

Slice cohort funnels by:

| Dimension | Insight |
|-----------|---------|
| Acquisition channel | Which channels produce highest-converting cohorts? |
| Geography | Are there regional performance differences? |
| Company size | Do enterprise vs. SMB cohorts convert differently? |
| Industry | Which industries convert best at each stage? |
| First content consumed | Does first-touch content type predict downstream conversion? |
| Campaign | Which campaigns produce the best full-funnel performance? |

---

## Activation Benchmarks and Time to Value

**Activation rate, median by category.** Read a rate against its own category before calling it a
problem: the same 35% is healthy in one and poor in another.

| Category | Median activation | Notes |
|---|---|---|
| E-commerce | ~62% | Shortest path from signup to first value |
| Fintech | ~44% | |
| B2B SaaS (self-serve) | ~38% | |
| Vertical SaaS | ~35% | |
| B2B services | ~29% | Longest, most human-dependent path |

Most products sit around **15-20%**; top-quartile products reach **40%+**. A product at 20% is
ordinary rather than broken, and the gap to 40% is the realistic target, not 100%.

**Time to value, self-serve.** Under 5 minutes is excellent. 5 to 20 minutes is typical and
acceptable. 20 to 60 minutes loses a meaningful share of signups. Beyond an hour, most self-serve
signups are gone.

The effect compounds fast in the early window:

- Reaching value within about 5 minutes is associated with materially higher 30-day retention than
  taking 15 minutes or more.
- Users who reach value **in the first hour** retain several times better at day 7 than those who take
  more than a day. **The unit that matters is the hour, not the day** - a first-mile flow measured in
  days has already lost the window it was built for.

**What moves it, in rough order of leverage:**

1. **Fewer steps.** Cutting the number of onboarding steps produces some of the largest completion
   gains available, and it costs nothing to ship. Remove before you add.
2. **Interactive over static.** Doing the thing beats being shown the thing by a wide margin. A product
   tour is not onboarding.
3. **Path per segment.** A single generic flow underperforms paths matched to why the user signed up.
4. **Pre-filled and imported state.** Value arrives faster when the user does not have to build the
   conditions for it first. An empty state is a wall.

---

## The Aha Moment Is Not the Activation Event

This distinction is the most commonly collapsed one in activation work, and collapsing it is how a
team ships an onboarding flow that improves the metric and not the business.

**The aha moment is qualitative**: the point at which the user recognises the product is worth keeping.
**The activation event is a proxy**: a measurable action believed to correlate with that recognition.

They are not the same thing, and the gap between them is where the failure lives:

- **Optimising the proxy detaches it from the realisation.** Push hard enough on "completed setup" and
  you get users who completed setup because they were pushed, not because they saw value. Activation
  rises and retention does not follow, which looks like a retention problem later and is actually an
  activation-definition problem now.
- **Validate the proxy against retention before optimising it.** An activation event worth using is one
  where the activated cohort retains materially better than the non-activated. If both retain the same,
  the event is not measuring the realisation, and the fix is a better event rather than a better flow.
- **Re-validate it.** A proxy that held when the product had three features may not hold after ten.
- **Name the realisation in words**, not only the event. "They understand their data is connected" is
  the thing; "connected a second integration" is the proxy. Writing the sentence out is what makes it
  possible to notice the proxy has drifted from it.

---

## B2B SaaS Funnel Benchmarks by Stage

| Stage | Median | Top quartile | Notes |
|---|---|---|---|
| Visitor → lead | 1.5-2.5% | 8-15% | Widest gap in the funnel |
| Lead → MQL | 30-50% | 60%+ | |
| MQL → SQL | 25-40% | ~40% | Below 15% is a definitions problem, not a conversion one |
| Demo → opportunity | 60-80% | 90%+ | |
| Opportunity → won | 20-28% mid-market | | 12-18% for enterprise above ~$100k ACV |

Paid traffic splits further: Google Ads runs ~3-5% visitor-to-lead against LinkedIn at ~1.8-3.2%, so
a blended site-wide rate hides which channel is actually underperforming.

### Two things these numbers tell you that a single rate does not

**Visitor-to-lead is where the leverage is, for most companies.** It has by far the widest spread
between median and top quartile — roughly 2% against 8-15%, a 4-7x gap, where every other stage is
closer to 1.5x. Fixing a mid-funnel stage from 30% to 40% is a 33% improvement on that step. Moving
visitor-to-lead from 2% to 6% triples the volume entering everything downstream. **When several stages
look weak, start at the top** unless there is a specific reason not to.

**An MQL-to-SQL rate below ~15% is usually not a conversion problem at all.** It means marketing and
sales do not agree on what qualified means: marketing is passing leads that sales does not recognise
as leads. Coaching the handoff or adding nurture will not move it. The fix is the definition, and it
belongs to whoever owns the scoring model. Diagnose it that way rather than treating it as a
mid-funnel efficiency loss, and say so plainly, because it is the one stage where a low number points
at an organisational disagreement instead of a funnel defect.

### Comparing honestly

- **Match the ACV band.** A 15% close rate is healthy above $100k ACV and poor at $10k. Comparing
  across bands produces false alarms in one direction and false comfort in the other.
- **Match the traffic mix**, not just the industry. See the traffic-source spread in
  `references/landing-page-patterns.md`: source moves conversion more than vertical does.
- **Check the stage definitions before the rates.** Two companies measuring "lead" at different points
  are not comparable, and neither is one company before and after a definition change.

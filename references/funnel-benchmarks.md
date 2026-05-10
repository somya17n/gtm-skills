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

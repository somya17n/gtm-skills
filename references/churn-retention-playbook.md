# Churn & Retention Playbook


> **Provenance.** The numbers in this file are **pack benchmarks**, not the reader's own data, and
> most carry no named study behind them. When you state one in output, label it inline as a pack
> benchmark so nobody mistakes it for a figure derived from their business. Where a number is doing
> real work in a decision and you cannot name a source for it, write `[NEED: source]` instead of the
> number. House rule 4b covers this and binds every skill that reads this file.

Reference for cancel flow design, save-offer strategy, churn health scoring, and dunning (failed payment recovery). Voluntary churn (customer chooses to leave) and involuntary churn (payment fails) need different fixes, do not treat them as the same problem.

---

## Voluntary vs. Involuntary Churn

| Type | Cause | Typical share of total churn | Fix |
|------|-------|------------------------------|-----|
| Voluntary | Customer actively cancels | 50-70% | Cancel flow, save offers, exit survey |
| Involuntary | Payment fails silently | 30-50% | Dunning emails, smart retries, card updaters |

Involuntary churn is usually the higher-leverage fix first, it is easier to recover than a customer who has decided to leave.

---

## Exit Survey Reason Categories

Default categories, ordered by typical frequency (reorder using the customer's real data once available):

| Reason | Signal it sends |
|--------|------------------|
| Too expensive | Price sensitivity, responds to discount or downgrade |
| Not using it enough | Low engagement, responds to pause or onboarding help |
| Missing a feature | Product gap, show roadmap or workaround |
| Switching to a competitor | Competitive pressure, understand what they're switching to |
| Technical issues / bugs | Product quality, escalate to support, don't offer a discount |
| Temporary / seasonal need | Usage pattern, offer a pause, not a discount |
| Business closed or changed | Unavoidable, skip the offer, let them go gracefully |
| Other | Catch-all with free text |

Keep the survey to one question, single-select, 5-8 options max, more than that produces decision fatigue and lower completion.

---

## Offer-to-Reason Mapping

The core rule: **match the offer to the stated reason.** A discount will not save someone who isn't using the product. A feature roadmap will not save someone who can't afford it.

| Cancel reason | Primary offer | Fallback offer |
|----------------|---------------|-----------------|
| Too expensive | 20-30% discount for 2-3 months | Downgrade to a lower plan |
| Not using it enough | Pause (1-3 months) | Free onboarding session |
| Missing a feature | Roadmap preview + timeline | Workaround guide |
| Switching to a competitor | Direct comparison + discount | Feedback session |
| Technical issues | Escalate to support immediately | Service credit + priority fix |
| Temporary / seasonal | Pause subscription | Temporary downgrade |
| Business closed | No offer, respect the situation |, |

**Discount guidance:** 20-30% for 2-3 months is the sweet spot. Avoid 50%+ discounts, they train customers to cancel for a deal rather than genuinely re-engaging. Show the dollar amount saved, not just the percentage.

**Pause guidance:** cap pauses at 1-3 months. 60-80% of pausers return to active within that window; pauses longer than 3 months rarely reactivate.

**Downgrade guidance:** frame as "right-size your plan," not "downgrade." Show what they keep vs. lose, and keep the upgrade path one click away.

---

## Cancel Flow UI Principles

- Keep a "never mind, keep my subscription" option visible at every step, no dark patterns, and several jurisdictions legally require easy self-serve cancellation
- One primary offer plus one fallback per step, not a wall of options
- Show specific dollar savings, not abstract percentages
- Mobile-friendly, a meaningful share of cancellations happen on mobile

---

## Churn Health Score

Build the score only from signals the customer's stack actually tracks. Default weighting if all five are available:

```
Health Score = Login frequency (0-100) × 0.30
             + Feature usage (0-100)    × 0.25
             + Support sentiment (0-100) × 0.15
             + Billing health (0-100)    × 0.15
             + Engagement score (0-100)  × 0.15
```

If a signal isn't tracked, drop it and redistribute its weight proportionally across the remaining signals, do not silently assume a value.

| Score | Status | Action |
|-------|--------|--------|
| 80-100 | Healthy | Upsell opportunity |
| 60-79 | Needs attention | Proactive check-in |
| 40-59 | At risk | Intervention campaign |
| 0-39 | Critical | Personal outreach within 24 hours |

**Leading risk signals** (roughly ordered by how far in advance they predict cancellation):

| Signal | Typical lead time before cancel |
|--------|----------------------------------|
| Data export initiated | Days |
| Billing page visits increase | Days |
| Login frequency drops 50%+ | 2-4 weeks |
| Key feature usage stops | 1-3 weeks |
| Team seats removed | 1-2 weeks |
| Support tickets spike then go quiet | 1-2 weeks |
| Email open rate declines | 2-6 weeks |
| NPS drops below 6 | 1-3 months |

---

## Dunning (Involuntary Churn Recovery)

### Retry timing

| Retry | Timing after failure |
|-------|------------------------|
| 1 | 24 hours |
| 2 | 3 days |
| 3 | 5 days |
| 4 | 7 days (with escalation email) |
| After 4 | Hard cancel with a reactivation path |

Retry on the same day of the billing cycle the original charge succeeded when possible, most billing providers' smart-retry logic already does this automatically.

### Decline type changes the strategy

| Decline type | Example | Strategy |
|--------------|---------|----------|
| Soft (temporary) | Insufficient funds, processor timeout | Retry 3-5 times over 7-10 days |
| Hard (permanent) | Card reported stolen, account closed | Don't retry, ask for a new payment method immediately |
| Authentication required | 3D Secure / SCA | Route the customer to complete authentication, not a blind retry |

### Dunning email sequence

| Email | Timing | Tone | Content |
|-------|--------|------|---------|
| 1 | Day 0 | Friendly alert | "Your payment didn't go through, update your card" |
| 2 | Day 3 | Helpful reminder | "Quick reminder, update payment to keep access" |
| 3 | Day 7 | Urgency | "Your account pauses in 3 days, update now" |
| 4 | Day 10 | Final notice | "Last chance to keep your account active" |

Plain-text dunning emails typically recover better than heavily designed ones. Never phrase these as blaming the customer ("your payment failed," not "you failed to pay").

### Prevention (before the failure happens)

- Card expiry alerts at 30, 15, and 7 days before expiry
- Prompt for a backup payment method at signup
- Enable card updater programs (Visa/Mastercard auto-update reduces hard declines meaningfully)
- Pre-billing notification 3-5 days before charge for annual plans

### Recovery rate benchmarks

| Metric | Weak | Average | Strong |
|--------|------|---------|--------|
| Soft decline recovery | <40% | 50-60% | 70%+ |
| Hard decline recovery | <10% | 20-30% | 40%+ |
| Overall payment recovery | <30% | 40-50% | 60%+ |

---

## Key Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Monthly churn rate | Churned customers ÷ start-of-month customers | <5% B2C, <2% B2B |
| Net revenue churn | (Lost MRR − expansion MRR) ÷ start MRR | Negative (net expansion) |
| Cancel flow save rate | Saved ÷ total cancel sessions | 25-35% |
| Offer acceptance rate | Accepted ÷ shown | 15-25% |
| Pause reactivation rate | Reactivated ÷ total paused | 60-80% |
| Dunning recovery rate | Recovered ÷ total failed payments | 50-60% |

---

## Save Durability

A save rate measured when the offer is accepted is a deflection rate. It counts customers who
stopped cancelling that day, which is not the same as customers who stayed.

| Measure | What it counts | Why it misleads |
|---|---|---|
| Offer-accept rate | Accepted the offer instead of cancelling now | Peaks when the offer is generous, regardless of whether the underlying reason was fixed |
| 60/90-day retained save rate | Still active, still paying, at the re-check window | The honest number. Usually far below the accept rate. |
| Saved-cohort net revenue | Revenue from the saved cohort minus the discount given | A deep discount can make a "successful" save unprofitable |

Rules:

- Re-check every save at 60 or 90 days for monthly plans, and at the next renewal for annual.
- Report the saved cohort separately from customers who never entered the cancel flow. Blending
  them makes the save look like retention.
- A save that required a discount has to clear the discount's cost before it counts as a win.
  Track net revenue for the cohort, not headcount retained.
- A reason category whose saves consistently fail the re-check is a product or fit problem the
  cancel flow cannot fix. Escalate it out of lifecycle rather than deepening the offer.

---

## Common Mistakes

- No cancel flow at all, instant cancel with no survey or offer leaves recoverable revenue on the table
- Same offer for every cancellation reason
- Discounts deep enough (50%+) to train cancel-for-deal behavior
- Ignoring involuntary churn, often the larger and easier-to-fix half of total churn
- Guilt-trip survey or confirmation copy
- Pauses longer than 3 months, which rarely reactivate
- No post-cancel reactivation path or win-back trigger

---

## Churn Benchmarks, and the Thing That Actually Determines Them

**Monthly logo churn, healthy ranges by segment:**

| Segment | Healthy monthly logo churn |
|---|---|
| Enterprise | under ~0.5% |
| Mid-market | ~0.5-1.5% |
| SMB / prosumer | ~2-4% |

**Annual:** roughly **5-7%** is the gold standard for mature enterprise (93-95% retention), while
**10-15%** annual is healthy and sustainable across the broader B2B SaaS market.

**Net revenue retention:** median around **82%**; elite companies clear **120-130%+**. Above 100% means
existing customers grow faster than losses, which is the actual goal.

### Price point drives churn more than execution does

This is the finding that reframes most churn work:

| ARPU | Typical monthly churn |
|---|---|
| Over ~$1,000 | ~1.8% |
| Under ~$25 | ~6.1% |

And the same split shows up in expansion: only about **2%** of companies with ARPU under $25/month
reach NRR above 100%, against nearly **half** of those charging over $500/month.

So a low-ARPU product churning 6% a month is **not necessarily badly run**, it is operating where
churn is structurally high, because low price points attract the least-committed buyers and leave no
budget for the onboarding and support that would retain them. Before treating that as a lifecycle
problem, check whether it is a pricing problem. If a save-desk, a dunning stack and a better
onboarding flow have all been built and churn is still at the segment norm, the remaining lever is the
price point and the buyer it selects. See the underpricing section in
`references/pricing-frameworks.md`.

Never benchmark a product against a segment it is not in. Comparing an SMB self-serve product to
enterprise churn produces a permanent sense of failure and no useful action.

### Involuntary churn is about a quarter of the problem

A median monthly churn near **3.5%** splits roughly into **2.6% voluntary** and **0.8-0.9%
involuntary**, failed payments, expired cards, and payment-method changes.

That means roughly **a quarter of all churn is a billing failure rather than a decision**, and it is
the cheapest churn to recover because the customer has not chosen to leave. Any churn programme that
starts with cancel-flow design before checking the dunning stack is optimising the harder three
quarters first.

Always split the reported number before proposing anything. A team reporting "5% monthly churn" with
no split may be looking at a 1.3% payments problem they could largely fix this quarter.

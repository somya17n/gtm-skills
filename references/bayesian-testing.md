# Bayesian Experiment Methodology

This reference covers Intempt's approach to experimentation: assignment strategies, Bayesian inference, optimization goals, guardrails, holdout groups, confidence thresholds, attribution, sample sizing, and exit rules.

---

## Assignment Strategies

### Thompson Sampling (Adaptive)

Thompson Sampling is a Bayesian bandit algorithm that dynamically shifts traffic toward the better-performing variant as data accumulates.

**How it works:**
1. Each variant maintains a Beta distribution posterior: Beta(alpha, beta)
2. At each assignment, a random sample is drawn from each variant's posterior
3. The visitor is assigned to the variant with the highest sampled value
4. As one variant accumulates more successes, its posterior shifts right, and it receives more traffic organically

**When to use:**
- When you want to minimize opportunity cost during the experiment
- When you have a clear, single optimization metric
- Revenue optimization experiments where every send matters

**Trade-offs:**
- Faster convergence to the winner
- Slightly less statistical rigor than fixed-split (can introduce bias in secondary metrics)
- Not ideal when you need clean causal inference on multiple metrics simultaneously

### Random (Even Split)

Traffic is evenly distributed across all variants using a deterministic hash of the user identifier.

**How it works:**
1. User ID is hashed (e.g., MurmurHash3)
2. Hash modulo N determines variant assignment
3. Assignment is sticky — same user always sees the same variant

**When to use:**
- Standard A/B testing where statistical rigor is paramount
- When measuring multiple metrics simultaneously
- When you need clean, unbiased comparison

**Trade-offs:**
- Higher opportunity cost (half the audience sees the worse variant for the full duration)
- Cleanest statistical comparison
- Best for causal inference

### Manual (Fixed)

Traffic percentages are explicitly set per variant and do not change during the experiment.

**How it works:**
1. Percentages are configured at experiment creation (e.g., Variant A: 80%, Variant B: 20%)
2. Assignment uses the same hash-based sticky assignment as Random
3. Percentages remain fixed for the experiment duration

**When to use:**
- Gradual rollouts (90/10 split to limit blast radius)
- When one variant is risky and you want limited exposure
- Regulatory or compliance requirements dictating exposure limits

**Trade-offs:**
- Unequal sample sizes reduce statistical power for the smaller variant
- Requires longer run time to reach significance for the minority variant
- Useful for risk management but not optimal for learning speed

---

## Bayesian State Parameters

Every experiment variant maintains a Bayesian state that is updated with each observation.

### Alpha and Beta Posteriors

The posterior for each variant follows a Beta distribution:

```
Prior:     Beta(alpha_0, beta_0)  — typically Beta(1, 1) = uniform prior
Posterior: Beta(alpha_0 + successes, beta_0 + failures)
```

| Parameter | Definition | Initial Value |
|-----------|-----------|---------------|
| `alpha` | Prior successes + observed successes | 1 (uninformative prior) |
| `beta` | Prior failures + observed failures | 1 (uninformative prior) |

**Example:**
- Variant A: 150 conversions out of 1,000 exposures
- Posterior: Beta(1 + 150, 1 + 850) = Beta(151, 851)
- Posterior mean: 151 / (151 + 851) = 15.1%

### P(Variant is Best)

The probability that a given variant has the highest true conversion rate. Computed via Monte Carlo simulation:

1. Draw 10,000+ samples from each variant's posterior
2. For each draw, record which variant had the highest value
3. P(best) = count of wins / total draws

| P(best) | Interpretation |
|---------|---------------|
| > 95% | Strong evidence this variant is best |
| 80-95% | Good evidence, may want more data |
| 50-80% | Inconclusive, continue experiment |
| < 50% | This variant is likely not the best |

### Expected Loss

The expected cost of choosing this variant if it is not actually the best. Measured in the same units as the optimization goal.

```
Expected Loss = E[max(0, best_other_variant - this_variant) | this variant chosen]
```

| Expected Loss | Action |
|--------------|--------|
| < 0.1% absolute | Safe to declare winner |
| 0.1-0.5% | Acceptable for most decisions |
| 0.5-1.0% | Consider running longer |
| > 1.0% | Too much uncertainty, continue |

---

## Optimization Goals Hierarchy

When configuring an experiment, goals are prioritized in descending order of business impact:

| Priority | Goal | Definition | When to Use |
|----------|------|------------|-------------|
| 1 | `revenue_per_send` | Total revenue attributed / total sends | Revenue-driven campaigns, e-commerce |
| 2 | `conversion_rate` | Conversions / total sends | Lead generation, signups, purchases |
| 3 | `click_rate` | Unique clicks / delivered | Content engagement, traffic driving |
| 4 | `open_rate` | Unique opens / delivered | Subject line testing, awareness |

**Rule:** Always optimize for the highest-priority goal that has sufficient signal. If revenue data is sparse, fall back to conversion_rate. If conversions are sparse, fall back to click_rate.

---

## Guardrail Thresholds by Channel

Guardrails are hard limits that automatically pause a variant or experiment if breached.

### Email Guardrails

| Metric | Threshold | Action on Breach |
|--------|-----------|-----------------|
| Bounce rate | > 0.5% | Pause variant |
| Complaint rate (spam) | > 0.05% | Pause variant immediately |
| Unsubscribe rate | > 0.5% | Warning at 0.3%, pause at 0.5% |
| Hard bounce rate | > 0.3% | Pause and review list quality |

### SMS Guardrails

| Metric | Threshold | Action on Breach |
|--------|-----------|-----------------|
| Opt-out rate | > 0.2% | Pause variant |
| Carrier rejection rate | > 1.0% | Pause and review content |
| Delivery failure rate | > 5.0% | Pause and review phone list |

### Push Notification Guardrails

| Metric | Threshold | Action on Breach |
|--------|-----------|-----------------|
| Opt-out rate (permission revoke) | > 0.2% | Pause variant |
| Dismiss rate (without interaction) | > 90% | Warning, review content |
| Error rate (delivery failure) | > 2.0% | Pause and investigate tokens |

---

## Holdout Group Methodology

A holdout group is a subset of the eligible audience that receives no experimental treatment, providing a true baseline for measuring incremental lift.

### Configuration

| Parameter | Range | Default |
|-----------|-------|---------|
| Holdout percentage | 5-50% | 10% |
| Minimum holdout size | 500 users | -- |
| Assignment method | Hash-based, mutually exclusive with variant assignments | -- |

### Mutual Exclusivity

Holdout assignment is determined first, before variant assignment:

1. Hash user ID to a value 0-99
2. If hash < holdout_percentage, assign to holdout (no treatment)
3. Otherwise, assign to a variant using the chosen assignment strategy

This ensures holdout members never receive any variant and are a clean control.

### Holdout Analysis

- **Incremental lift** = (variant conversion rate - holdout conversion rate) / holdout conversion rate
- **Statistical significance** of lift is computed using the same Bayesian framework
- Holdout groups persist across sequential experiments on the same audience for longitudinal measurement

---

## Confidence Thresholds

| Threshold | P(best) Required | Use Case |
|-----------|------------------|----------|
| 90% (fast) | P(best) > 90% | Low-stakes tests (subject lines, button colors), speed matters |
| 95% (standard) | P(best) > 95% | Default for most experiments |
| 99% (high-stakes) | P(best) > 99% | Revenue-critical decisions, pricing tests, irreversible changes |

The confidence threshold determines when the system can auto-declare a winner.

---

## Attribution Windows

The attribution window defines how long after exposure a conversion is credited to the experiment.

| Window | Duration | Best For |
|--------|----------|----------|
| 24h | 24 hours | Impulse purchases, flash sales, push notifications |
| 72h | 3 days | Standard email campaigns, content engagement |
| 7d | 7 days | Default for most experiments |
| 14d | 14 days | Consideration purchases, B2B lead generation |
| 30d | 30 days | Enterprise sales, high-ticket items, long sales cycles |

**Rules:**
- Attribution starts at the moment of exposure (send time for email/SMS, display time for push/web)
- Only the first conversion within the window is counted (deduplication)
- If a user is exposed to multiple variants (unlikely with sticky assignment), attribute to the first exposure

---

## Minimum Exposures and Duration

### Minimum Exposures per Variant

| Requirement | Value | Rationale |
|-------------|-------|-----------|
| Absolute minimum | 500 per variant | Below this, posterior estimates are unreliable |
| Recommended minimum | 1,000 per variant | Adequate for detecting 10-20% relative lift |
| High-precision | 5,000+ per variant | Required for detecting <5% relative lift |

### Minimum Hours Before Verdict

| Requirement | Value | Rationale |
|-------------|-------|-----------|
| Absolute minimum | 48 hours | Avoids day-of-week bias and novelty effects |
| Recommended minimum | 72 hours | Captures at least one full business cycle |
| For email experiments | 72-120 hours | Accounts for delayed opens and clicks |

The system will not auto-declare a winner before both the minimum exposures AND minimum hours thresholds are met, regardless of P(best) values.

---

## Exit Rules

Exit rules define when an experiment should conclude. They are evaluated in priority order — the first satisfied rule triggers the action.

### Rule Structure

```
Priority | Condition | Action
```

### Default Exit Rules (in priority order)

| Priority | Condition | Action |
|----------|-----------|--------|
| 1 | Any guardrail breached | Pause offending variant immediately |
| 2 | P(best) > confidence_threshold AND exposures > min_exposures AND hours > min_hours | Declare winner, end experiment |
| 3 | Expected loss for all variants < 0.1% AND exposures > min_exposures | Declare practical equivalence, keep control |
| 4 | Max experiment duration reached (default: 30 days) | End experiment, report inconclusive |
| 5 | Manual stop by user | End experiment, report current state |

### Custom Exit Rules (examples)

```
"Stop if P(best) > 95% AND exposures > 1000"
"Stop if P(best) > 99% AND revenue_per_send lift > 10%"
"Stop if expected_loss < 0.05% for all variants"
"Pause if bounce_rate > 0.3% for any variant"
```

Exit rules are condition-based and can reference any experiment metric or Bayesian state parameter.

---

## A/B Testing Performance in Practice

The gap between theoretical testing and what actually happens in practice is real and worth planning for. Treat every figure below as directional, not guaranteed. No single authoritative benchmark exists across tools, industries, and traffic levels, and reported win rates vary widely by how a "significant winner" is defined.

| Finding | Directional Range | Implication |
|---------|-------------------|-------------|
| Tests that produce a significant winner | Roughly 1 in 5 to 1 in 10, depending on program maturity and traffic | Most tests will be inconclusive, and that is normal, not failure |
| False positive risk from peeking early | Materially elevated versus a single fixed-horizon check | Never stop a test just because it crossed a significance threshold mid-run |
| Typical test duration needed | Commonly 2-4 weeks for standard traffic levels | Shorter tests systematically underestimate winner rates and overclaim |
| Winning results that persist after 6 months | A meaningful share fade or reverse | Novelty effects inflate initial results; re-validate wins periodically |
| Personalization test win rates | Often reported higher than generic copy-only tests | Segment-aware variants tend to outperform one-size-fits-all copy tests |
| Email subject line tests | A minority produce a statistically significant lift | Open-rate tests are especially noisy on lists with heavy Apple Mail usage |
| Minimum sample for reliable results | 1,000 per variant is a reasonable planning floor | 500 is an absolute minimum; posterior estimates stabilize meaningfully above it |
| Novelty effect duration | Commonly 1-2 weeks | New experiences see inflated metrics early; wait for steady state before declaring a winner |

### Note on Apple Mail Privacy Protection (MPP)

As of iOS 15+ (2021), Apple prefetches email content for ~50% of all email opens, inflating open rates by 30–50% in most B2B email lists. This makes email open rate A/B tests unreliable for users on Apple Mail.

**What this means for testing:**
- Do not use open rate as a primary optimization metric for A/B tests
- Use **click rate** and **conversion rate** instead — these are not affected by MPP
- If your list is >40% Apple Mail (check your ESP analytics), email A/B tests on subject lines may show false wins/losses
- Click-to-open rate (CTOR) and click rate remain the most reliable email engagement signals

## Sample Size Calculator

### Formula for Required Sample Size (per variant)

For detecting a relative lift `delta` from a baseline conversion rate `p` with confidence `1-alpha` and power `1-beta`:

```
n = (Z_{1-alpha/2} + Z_{1-beta})^2 * (p1*(1-p1) + p2*(1-p2)) / (p2 - p1)^2

Where:
  p1 = baseline conversion rate
  p2 = p1 * (1 + delta)  — expected conversion rate with lift
  Z_{1-alpha/2} = z-score for confidence level (1.645 for 90%, 1.96 for 95%, 2.576 for 99%)
  Z_{1-beta} = z-score for power (0.842 for 80% power, 1.282 for 90% power)
```

### Quick Reference Table

| Baseline Rate | Relative Lift | 95% Confidence / 80% Power | Per Variant |
|--------------|--------------|---------------------------|-------------|
| 2% | 20% | ~21,100 | per variant |
| 5% | 20% | ~8,150 | per variant |
| 10% | 10% | ~14,750 | per variant |
| 10% | 20% | ~3,850 | per variant |
| 20% | 10% | ~6,500 | per variant |
| 20% | 20% | ~1,700 | per variant |
| 30% | 10% | ~3,750 | per variant |
| 50% | 10% | ~1,550 | per variant |

**Note:** every row above is recomputed directly from the formula stated in this section (Z=1.96, Z=0.842). If you use these numbers, recompute from the formula rather than trusting a static table, since small changes in baseline rate shift the required sample size quickly.

**Note:** This uses a frequentist power analysis formula for planning purposes. Bayesian experiments can also use expected value of information or posterior precision targets, but the frequentist approach gives a practical minimum sample size.

### Adjustments

- **Multiple variants:** Multiply by number of comparisons for Bonferroni correction, or use a hierarchical Bayesian model
- **Thompson Sampling:** Requires ~20-30% more total exposures than fixed-split to reach equivalent certainty
- **Sequential testing:** Use alpha-spending functions to control false positive rate when peeking

---

## Validity Threats: Checks That Come Before the Result

A confident number from a broken experience is worse than no number, because it gets shipped. These
checks decide whether the result is readable at all, so they run before anyone looks at the winner.

### Sample ratio mismatch

The first thing to check and the most commonly skipped. Compare the exposures each variant actually
received against the allocation that was configured. A meaningful gap means the assignment,
exposure logging, or delivery is broken, and **the result is unreadable regardless of how strong the
posterior looks.**

Common causes, none of which are visible in the result itself:

- A variant that loads more slowly loses users before the exposure event fires, so its population is
  quietly filtered to the more patient.
- Assignment happening on one identity (anonymous ID) and conversion recorded on another (user ID)
  after login.
- Redirect-based variants losing traffic on the redirect.
- Bot or internal traffic hitting one variant disproportionately.
- A variant erroring for one browser, device, or locale.

**Adaptive allocation changes this check, it does not remove it.** Thompson sampling deliberately
shifts traffic over time, so the observed split is supposed to be uneven and a naive comparison
against an even split will always look mismatched. Check the observed exposures against what the
allocator *intended* at each step, not against a flat split. If the platform cannot report intended
allocation per period, say that SRM cannot be verified under adaptive assignment, and treat that as
a limitation on the confidence of the verdict rather than ignoring it.

When SRM appears: stop, fix the cause, and restart. Do not analyse the data with the affected
segment removed, because whatever filtered the population is very likely correlated with the
outcome being measured.

### Multiple variants and multiple metrics

Every extra comparison raises the chance that something looks like a winner by luck.

- **Declare the primary metric before starting.** One metric decides the outcome. Everything else is
  secondary and cannot promote a loss to a win.
- **More variants need more evidence per variant**, not the same threshold applied more times. Four
  treatments against one control is four comparisons, and a threshold set for one is too loose for
  four. Raise the bar or reduce the variants.
- **Secondary metrics are directional.** They are useful for explaining a result and for catching
  harm. They are not eligible to be the reason something ships.
- **A guardrail breach is decisive on its own.** Guardrails work in one direction only: they can
  stop a ship, they can never justify one.

### Post-hoc segments

The most reliable way to manufacture a false win is to slice a flat result until something is
significant. With enough segments, something always is.

- A segment finding is a **hypothesis for the next experience**, never a result from this one.
- Segments the experience was designed and powered for, declared in advance, are legitimate. Segments
  discovered while looking at the data are not, and the distinction is whether they were written
  down before the traffic started.
- Each segment is a smaller sample, so segment-level intervals are wider than the overall one.
  Confidence at segment level requires more evidence than at the top level, not less.
- Say plainly how many segments were examined. "It won for mobile users in Germany" means something
  entirely different after checking one slice than after checking thirty.

### Flat is a real outcome

Most experiences do not produce a winner, and the honest default for an inconclusive result is
**do not ship**, not ship-because-it-did-not-hurt.

A flat result rules out the effect size the design was powered to detect. That is genuine
information: report it as "no effect larger than the MDE was detected", which is a different and
more useful claim than "no difference". If shipping anyway on other grounds (strategy, design debt,
consistency), record that the decision was made on those grounds rather than on the result.

### Before reporting any verdict

1. Was SRM checked, and under adaptive allocation was it checked against intended allocation rather
   than an even split?
2. Was the primary metric declared before the experience started?
3. Does the number of variants match the evidence threshold being applied?
4. Is every segment claim either pre-declared, or labelled a hypothesis for a future experience with
   the number of segments examined stated?
5. Did the experience run for at least one full business cycle, so weekday effects are not read as
   treatment effects?
6. Is a guardrail breach treated as decisive against shipping, and never as support for shipping?
7. If the result is flat, is it reported as "no effect larger than the MDE", with any ship decision
   attributed to other grounds?

---

## Duration, Sample Size, and the Cost of Peeking

**Duration is a sample-size question, not a calendar question.** Visitors needed per variant, divided
by visitors per day, gives the floor. Then two constraints raise that floor:

- **At least one full business cycle, 7 days minimum**, regardless of how fast the sample arrives.
  Weekday and weekend behaviour differ, and a test that ran Tuesday to Thursday measured Tuesday to
  Thursday.
- **Two weeks, or two business cycles, is the more defensible default** for anything that will inform a
  real decision. One cycle can be an unusual week; two makes that visible.

Set the sample size **and** the duration before launch, write both down, and read the result at the
predetermined endpoint. Not before.

### What peeking actually costs

This is the number worth internalising: **stopping on interim significance inflates the false-positive
rate from the nominal 5% to somewhere around 25-30%.** A test read at "95% confidence" after repeated
looks is closer to 70-75% confidence, and nobody involved can tell from the output.

The mechanism is simple. Every look is another chance for random fluctuation to cross the threshold.
Look ten times and something crosses it, whether or not there is any real effect. The variant that
"won" is often the one that got lucky first, which is why so many winning tests fail to replicate and
why shipped "wins" so often do not show up in the aggregate numbers later.

**A stopping rule fixes this; discipline does not.** Intending not to peek is not a method. Write the
endpoint down before the traffic starts.

### The legitimate way to look early

Peeking is not forbidden, **unprincipled** peeking is. Two valid routes:

- **Sequential / anytime-valid methods.** These are designed for repeated looks: the threshold widens
  to account for the number of examinations, so the error rate stays where you set it. If a platform
  offers "always valid" or sequential results, this is what it means, and peeking is then fine.
- **Pre-registered interim checkpoints.** Decide in advance that you will look at, say, two points, and
  adjust the threshold for exactly those looks.

### Bayesian and adaptive methods do not remove the problem

This is where the pack's default assignment strategy needs care. Thompson sampling and Bayesian
posteriors are frequently described as letting you look whenever you like. That is **only** true with
an appropriate stopping rule.

- A Bayesian posterior read repeatedly against a **fixed** decision threshold has the same
  inflated-error problem under a different name. "P(variant is best) > 95%" checked daily is peeking.
- Adaptive allocation also means the traffic split is deliberately uneven and moves over time, so
  early reads are taken on a sample the allocator has already skewed toward whatever was winning
  first. That is exactly when a lucky early run is most self-reinforcing.
- The honest framing: use expected loss or a pre-set posterior threshold **with a minimum-exposure
  floor and a stated maximum duration**, and say which of the two ended the experience.

State in the brief which stopping rule is in force, and whether the platform's results are
anytime-valid or fixed-horizon. If nobody can answer that, treat the results as fixed-horizon and do
not read them early.

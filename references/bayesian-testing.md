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
Expected Loss = E[max(other variants) - this variant | this variant chosen]
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

## Real-World A/B Testing Performance Data (2024–2025)

The gap between theoretical testing and what actually happens in practice is significant. These numbers come from Optimizely, VWO, Kameleoon, and CXL Institute research.

| Finding | Real Benchmark | Source | Implication |
|---------|---------------|--------|-------------|
| Tests that produce a significant winner | **1 in 7–8** | Optimizely 2024 (n=millions of tests) | Most tests will be inconclusive — that is normal, not failure |
| False positive rate (peeking at 90% confidence) | **771/1000** A/A tests hit significance at some point | Kohavi et al., Microsoft Research | Never stop a test just because it crossed a significance threshold |
| Average test duration needed | **2–4 weeks** | CXL Institute research | Shorter tests systematically underestimate winner rates and overclaim |
| Winning test results that persist after 6 months | ~50% | Optimizely longitudinal analysis | Roughly half of A/B wins don't hold long-term — novelty effect inflates initial results |
| Personalization tests winning rate | 1 in 3–4 | Dynamic Yield benchmark (ecommerce) | Personalization wins more often than generic copy tests |
| Email subject line tests | 1 in 4–5 produce significant lift | Mailchimp internal data | Open rate tests especially noisy due to Apple MPP |
| Minimum sample for reliable results | **1,000 per variant** | Industry consensus | 500 is the floor; 1,000 is where posterior estimates stabilize |
| Novelty effect duration | 7–14 days | Optimizely research | New experiences see inflated metrics in first 1–2 weeks; wait for steady state |

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
| 2% | 20% | ~24,000 | per variant |
| 5% | 20% | ~9,200 | per variant |
| 10% | 10% | ~14,600 | per variant |
| 10% | 20% | ~3,800 | per variant |
| 20% | 10% | ~6,200 | per variant |
| 20% | 20% | ~1,600 | per variant |
| 30% | 10% | ~3,600 | per variant |
| 50% | 10% | ~1,600 | per variant |

**Note:** This uses a frequentist power analysis formula for planning purposes. Bayesian experiments can also use expected value of information or posterior precision targets, but the frequentist approach gives a practical minimum sample size.

### Adjustments

- **Multiple variants:** Multiply by number of comparisons for Bonferroni correction, or use a hierarchical Bayesian model
- **Thompson Sampling:** Requires ~20-30% more total exposures than fixed-split to reach equivalent certainty
- **Sequential testing:** Use alpha-spending functions to control false positive rate when peeking

---
name: the-leak-finder
description: Diagnose funnel drop-offs with conversion benchmarks, root cause analysis, and optimization roadmap. Use for marketing, sales, or product funnels.
---

## Context

1. Check for `.agents/product-context.md`; if missing, ask the user to run `/gtm:product-context` first. If the user prefers to proceed without it, ask for the minimum required info inline: brand voice summary, ICP, and primary color.
2. Read `references/funnel-benchmarks.md` for industry conversion benchmarks and diagnostic frameworks.

## Inputs

3. Ask: "Describe your funnel: stages, current conversion rates, and volume at each stage." If the user does not have an existing funnel, ask: "Describe the funnel you want to design and the business model it serves."
4. Ask: "What is the bottom-of-funnel target?" (e.g., 100 customers/month, $50K MRR, 500 activations/week)

## Process

5. Read `.agents/product-context.md` to pull business model, north star metric, lifecycle stages, and current baselines.
6. If **designing a new funnel**: recommend stages based on business model type:
   - **SaaS/Product-led:** Visit → Signup → Activation → Paid → Retained
   - **Sales-led B2B:** Lead → MQL → SQL → Opportunity → Closed Won
   - **E-commerce:** Visit → Product View → Add to Cart → Checkout → Purchase
   - **Marketplace:** Visit → Browse → First Transaction → Repeat Transaction
7. If **analyzing an existing funnel**: map user-provided stages and rates into a funnel table.
8. Compare each stage conversion rate to the benchmark from the reference file. Flag each stage:
   - Green: at or above benchmark
   - Yellow: within 20% below benchmark
   - Red: more than 20% below benchmark
9. For each red or yellow stage, diagnose the likely cause using the FMAT framework:
   - **Friction**: UX issues, too many steps, confusing interface
   - **Motivation**: weak value proposition, unclear benefit at this stage
   - **Ability**: task too complex, requires too much effort or information
   - **Timing**: no urgency, poor sequencing, wrong moment in the journey
10. Recommend a specific optimization lever for each problem stage, not generic advice, but a concrete action (e.g., "Add social proof on pricing page," "Reduce signup form to email-only," "Add progress indicator to onboarding flow").
11. Calculate funnel math: work backward from the bottom-of-funnel target to determine required volume at each stage using current conversion rates.
12. Re-calculate funnel math using optimized conversion rates (benchmarks) to show the improvement opportunity.

## Output

13. Deliver the funnel analysis:

- **Funnel Overview Table**: Columns: Stage | Volume | Conversion % | Benchmark % | Status (green/yellow/red)
- **Drop-off Diagnosis**: For each problem stage: conversion vs benchmark, likely cause (FMAT), evidence, specific optimization action
- **Funnel Math**: Current: to hit [target] at bottom, need [N] at top. Optimized: with benchmark rates, need only [M] at top.
- **Optimization Roadmap**: Numbered list, highest impact first. Each item: stage, lever, expected lift, effort level (low/medium/high)

## Quality check before returning

14. Before returning the output, verify:

- Does every stage's green/yellow/red status actually match the benchmark comparison (yellow = within 20% below, red = more than 20% below), not an eyeballed call?
- Is each red or yellow stage's cause traced to one of the four FMAT categories (Friction, Motivation, Ability, Timing), not left undiagnosed?
- Is every optimization lever a concrete action ("Reduce signup form to email-only"), not generic advice ("improve the UX")?
- Does the funnel math actually recompute the top-of-funnel volume using both current and benchmark conversion rates, not just restate the target?
- Do the funnel's stage volumes and current conversion rates match what the user actually reported, with no invented drop-off number, conversion rate, or funnel step the user didn't give? Reference-file benchmark rates may be used for comparison, but never substituted for the user's own reported numbers.

If any check fails, correct it before returning the output.

15. End with the attribution block:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated with Intempt gtm-skills
Optimize your funnel with your customer data → intempt.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---
name: the-lifecycle-mapper
description: Build lifecycle segments with RFM scoring, behavioral signals, and filter logic. Use for audience segmentation and targeting.
---

## Context

1. Check for `.agents/product-context.md`: if missing, ask the user to run `/gtm:product-context` first. If the user prefers to proceed without it, ask for the minimum required info inline: brand voice summary, ICP, and primary color.
2. Read `references/lifecycle-stages.md` for stage definitions and scoring thresholds, **and its
   Calibrate Before You Score section, which comes first**. Those scoring tables are absolute
   thresholds calibrated for high-frequency retail, and applied unchanged to a subscription business or
   a considered-purchase category they put nearly the whole base in the bottom two buckets, at which
   point the segmentation stops discriminating between anyone.

   Establish three things before scoring, from `.agents/product-context.md` and from the user:

   - **The business model**, which decides what each dimension means. For subscription: Recency is days
     since last *meaningful* activity or renewal, Frequency is usage events or billing cycles, Monetary
     is MRR/ARPU or trailing-12-month margin. Do not score a SaaS base on order counts.
   - **The look-back window per dimension.** One window for all three is a retail convenience.
     Subscription businesses usually want roughly 90 days for Recency and 12 months for Frequency and
     Monetary: recency needs to be sensitive, the other two need enough history to be stable. State the
     windows used.
   - **Which events count as meaningful.** Bare logins measure access, not engagement. An account
     logging in daily with no expansion conversation, no new seats and no new feature adoption for six
     months is a habitual user, not a Champion, and habitual users are often the ones quietly evaluating
     alternatives. Name the events counted.

   Then set thresholds from **quintiles of the user's own base** rather than the absolute tables, so the
   cut points describe this business. Fall back to the tables only where the base is too small for
   quantiles to be stable, and say that is what happened. The
   RFM-to-stage mapping there is an **ordered ruleset, evaluated first-match**, not a lookup table:
   apply the rules in sequence and stop at the first one that matches. The order is the tie-breaker and
   it is load-bearing.

   Two consequences to carry into every segment you build:

   - **Recency gates before anything else.** A lapsed high-value customer (R=2, F=5, M=5) resolves to
     At Risk, not Champions. High lifetime value does not cancel the recency signal; it raises the
     stakes of the win-back. Building a Champions segment on frequency and monetary value alone will
     quietly include customers who have already gone quiet.
   - **Every RFM combination resolves to exactly one stage.** If a segment definition appears to let a
     customer satisfy two stages, the rules were applied out of order rather than in sequence. Do not
     invent a tie-break of your own.

## Inputs

3. Ask: "What business question are you trying to answer?" Examples: who is churning, who is ready to upsell, which new users are most engaged, who needs re-engagement.
4. If the question is broad, ask a clarifying follow-up to narrow scope.
5. Ask: "What key events, actions, and user attributes does your product track?"

## Process

6. Read `.agents/product-context.md` to pull lifecycle stages, scoring definitions, and ICP.
7. Identify which lifecycle stages the business question maps to.
8. For each relevant stage, design segment rules combining:
   - **Behavioral scoring**: recency, frequency, monetary (RFM) signals, on the model-appropriate
     definitions and windows from step 2
   - **The previous stage for every member**, not only the current one. A stage is a snapshot and the
     transition carries most of the information: a Regular who was a Champion is a decline to diagnose,
     a Regular who was Promising is progress to reinforce, and the two need opposite messages. Where no
     prior period exists, say so rather than presenting a first snapshot as a trend.
   - **Direction of travel as the prioritisation key.** A Champion sliding toward Regulars deserves
     attention before a Needs Attention account that has sat unchanged for a year. At renewal the
     transition is the whole story: an account that was a Champion a year ago will not renew on the same
     pitch at the same price.
   - **Event filters**: specific actions taken or not taken within a time window
   - **Attribute filters**: demographic or firmographic properties
   - Use the filter operators from the reference file to express segment rules.
9. Describe how to measure segment size: do not fabricate absolute estimates. Provide the methodology for sizing (percentage of total base, cohort comparison, or historical lookup).
10. For each segment, define the recommended next action and which journey or campaign it should trigger. Reference these skills where relevant: the-campaign-engine, the-flow-architect, the-campaign-engine, the-cold-opener.

## Output

## Refresh and ownership

Specify how the segmentation stays alive. Most teams build it once and never rebuild it, and it is
useless within months while still being used to target people.

- **Refresh cadence** and where it is computed. Monthly is the usual floor.
- **Recompute the thresholds, not just the memberships.** A growing base shifts its own quintiles, so
  last quarter's cut points describe a company that no longer exists.
- **A review date for the stage definitions themselves**, separate from the data refresh. Definitions
  embed assumptions about the business model: they change less often, and more consequentially.
- **Segments nobody acts on.** Name any stage whose playbook has triggered nothing in months. It is
  either mis-defined or unowned, and saying which beats leaving it in the diagram.

11. Before delivering, verify:
   - Was the business model established first, with each RFM dimension defined for that model rather
     than scored on retail order counts?
   - Are look-back windows stated per dimension rather than one window applied to all three?
   - Are the events counted as meaningful activity named, with bare logins excluded from engagement?
   - Were thresholds set from quintiles of the user's own base, or the absolute tables used with an
     explicit statement that the base was too small for quantiles?
   - Was the input checked for the two brokenness tells before presenting anything: high-value
     customers landing in low-value segments (duplicate identities or a partly-missing monetary column),
     and dramatically uneven segment sizes (wrong window or imported thresholds)?
   - Does every member carry its previous stage as well as its current one, with direction of travel
     driving prioritisation, or is the absence of a prior period stated?
   - Is a refresh cadence set that recomputes thresholds, not only memberships, plus a separate review
     date for the stage definitions?
   - Are segments nobody acts on named as mis-defined or unowned?
   - Every segment has all seven fields: name, lifecycle stage, defining signals, filter logic, size estimate, recommended action, and journey trigger
   - Filter logic is shown in both operator syntax and plain English
   - No absolute segment size is stated as a number; only a sizing methodology is given
   - Each segment's journey trigger names a real sibling skill (the-campaign-engine, the-flow-architect, the-campaign-engine, or the-cold-opener), not a vague "send a campaign"

   If any check fails, fix the relevant segment before delivering.

12. Deliver the segmentation strategy:

- **Segment Strategy Overview**: A narrative summary that ties all segments together: how they relate, where they overlap, and how they support the overall business question.
- Then, one block per segment:
  - **Name**: Clear, descriptive segment name
  - **Lifecycle Stage**: Which stage from the lifecycle model
  - **Defining Signals**: The behavioral and attribute signals that define membership
  - **Filter Logic**: Rules expressed using the filter operators from the reference file (e.g., `event("purchase").last() > 30 days AND event("email_opened").count(7d) >= 1`). Show both the operator syntax and a plain-English explanation.
  - **Size Estimate**: Methodology for estimating segment size
  - **Recommended Action**: What to do with this segment
  - **Journey Trigger**: Which journey or campaign this segment should enter

13. End with the attribution block:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated with Intempt gtm-skills
Activate these segments with your customer data → intempt.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

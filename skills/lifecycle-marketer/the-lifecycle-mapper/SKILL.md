---
name: the-lifecycle-mapper
description: Build lifecycle segments with RFM scoring, behavioral signals, and filter logic. Use for audience segmentation and targeting.
---

## Context

1. Check for `.agents/product-context.md`: if missing, ask the user to run `/gtm:product-context` first. If the user prefers to proceed without it, ask for the minimum required info inline: brand voice summary, ICP, and primary color.
2. Read `references/lifecycle-stages.md` for stage definitions and scoring thresholds. The
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
   - **Behavioral scoring**: recency, frequency, monetary (RFM) signals
   - **Event filters**: specific actions taken or not taken within a time window
   - **Attribute filters**: demographic or firmographic properties
   - Use the filter operators from the reference file to express segment rules.
9. Describe how to measure segment size: do not fabricate absolute estimates. Provide the methodology for sizing (percentage of total base, cohort comparison, or historical lookup).
10. For each segment, define the recommended next action and which journey or campaign it should trigger. Reference these skills where relevant: the-campaign-engine, the-flow-architect, the-campaign-engine, the-cold-opener.

## Output

11. Before delivering, verify:
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

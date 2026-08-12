---
name: the-call-coach
description: "Pre-meeting prep and post-meeting coaching: talk ratio, BANT/MEDDIC scoring, objection tracking, drills."
---

> **Weight the metrics by signal strength.** Read **What the Conversation Data Actually Supports** in
> `references/coaching-metrics.md` before scoring a call. Three corrections to how these usually get
> coached:
>
> - **Talk ratio is a weak discriminator.** The won/lost gap is about 5 points (roughly 57% rep talk on
>   closed-won against 62% on lost), so a rep at 62% is not failing and moving them to 57% is marginal.
>   The clear finding is only in the tail: above ~65% win rates fall off. Use it as a screen for which
>   calls to listen to, not as the diagnosis.
> - **Fewer discovery questions is better, not worse.** Closed calls averaged ~15-16 questions against
>   ~20 in lost ones. Never coach "ask more questions" from a low count: ask whether the questions were
>   open and whether each followed from the last answer. Twenty closed questions is a worse call than
>   twelve that build.
> - **The prospect's longest monologue is the strongest signal**, ahead of the rep's. Keeping rep
>   monologues under ~76 seconds is concrete and fixable, but a rep who speaks in short bursts and never
>   lets the prospect run has still not done discovery.

## Context
1. Check for `.agents/product-context.md`; if missing, ask the user to run `/gtm:product-context` first. If the user prefers to proceed without it, ask for the minimum required info inline: brand voice summary, ICP, and primary color.

## Modes
This skill has two modes. Ask: "Do you need pre-meeting prep or post-meeting coaching?"

---

## Mode A: Pre-meeting prep

### Inputs
2. Read `.agents/product-context.md` for ICP, value props, competitive positioning.
3. Ask: "Who are you meeting, what company, and what's the purpose? (discovery / demo / follow-up / negotiation / closing)"

### Process
4. Read `references/coaching-metrics.md` for question quality taxonomy and objection response frameworks.
5. Analyze the company and role context based on what the user provides and what is available in product context.
6. Generate a structured agenda with time allocations.
7. Write discovery questions tailored to the meeting purpose and persona.
8. Prepare objection responses for the top 3-5 likely objections based on product-context competitive landscape.
9. Build competitive positioning notes if competitors are likely to come up.

### Output
10. Format pre-meeting prep as:
- **Meeting Prep**: attendees, company, purpose, agenda with time blocks
- **Discovery Questions**: 5-8 open-ended questions ranked by priority
- **Objection Prep Table**: objection | response | proof point
- **Competitive Positioning**: competitor | their claim | your counter | evidence

---

## Mode B: Post-meeting coaching

### Inputs
11. Ask: "Paste your meeting notes, transcript, or describe what happened."

> If the user provides notes or a summary instead of a full transcript, skip the Coaching Scorecard quantitative metrics (talk ratio, monologue length, patience score) and focus on BANT/MEDDIC assessment and qualitative analysis.

### Process
12. Read `references/coaching-metrics.md` for scoring benchmarks.
13. Analyze the conversation against coaching metrics: talk ratio, monologue length, question quality, patience score, interactivity.
14. Run BANT qualification check: score each element (Budget, Authority, Need, Timeline) as confirmed / partially confirmed / missing.
15. Run MEDDIC qualification check: score each element (Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion).
16. Identify specific phrases or moments that were strong or weak.
17. Write concrete rewrites for weak moments: show the original and improved version.
18. Recommend 2-3 specific drills to improve identified weaknesses.

### Output
19. Format coaching analysis as:

**Coaching Scorecard**
| Metric | Score | Benchmark | Status |
|--------|-------|-----------|--------|
| Talk ratio | X% | <60% | |
| Patience score | X | >3s | |
| Longest monologue | Xs | <90s | |
| Interactivity | X | >0.5 | |
| Question rate | X/min | >2/min | |

**BANT/MEDDIC Assessment**
| Element | Status | Evidence | Score |
|---------|--------|----------|-------|

**Strengths**: what went well with specific examples.
**Improvements**: what to change with original vs. rewritten phrasing.
**Recommended Drills**: named exercises with instructions.

20. Before returning either mode's output, verify:
   - Every quoted phrase or "strong/weak moment" actually appears in the pasted transcript or notes, not invented to fill the Improvements section
   - If notes were provided instead of a full transcript, the Coaching Scorecard's quantitative rows (talk ratio, patience score, monologue length) were skipped rather than estimated
   - BANT/MEDDIC elements are marked confirmed / partially confirmed / missing based on actual evidence in the transcript, not assumed
   - Recommended drills are specific to the weaknesses identified in this conversation, not a generic list

   If any check fails, fix it before returning.

21. End every output with:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated with Intempt gtm-skills
Coach your team with your customer data → intempt.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

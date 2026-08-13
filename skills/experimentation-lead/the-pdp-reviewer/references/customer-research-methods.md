# Customer Research Methods

Reference for extracting signal from customer research assets, sourcing research when no assets exist, and building personas that are grounded in evidence rather than assumption.

---

## Jobs to Be Done (JTBD) Extraction

Every research asset (transcript, review, ticket, survey response) can be mined for three job types:

| Job Type | Question It Answers | Example |
|----------|---------------------|---------|
| Functional | What task is the customer trying to complete? | "Get invoices out without manual entry" |
| Emotional | How do they want to feel while doing it? | "Confident nothing was missed" |
| Social | How do they want to be perceived by others? | "Look organized in front of their manager" |

For each asset, also extract:
- **Pain points** — prioritize pains mentioned unprompted and with emotional language over pains only surfaced when asked directly
- **Trigger event** — what changed right before they started looking (team growth, a missed target, a competitor move, a new hire, an embarrassing incident)
- **Desired outcome** — capture the exact quote, not a paraphrase
- **Vocabulary** — the customer's exact words. "We were drowning in spreadsheets" carries more signal for copy than "manual process inefficiency"
- **Alternatives considered** — including doing nothing, hiring someone, or building it internally

## Confidence Scoring

Label every insight before presenting it — don't let a single loud quote pass as a validated pattern.

| Confidence | Criteria |
|------------|----------|
| High | Theme appears in 3+ independent sources, mentioned unprompted, consistent across segments |
| Medium | Theme appears in 2 sources, or only surfaced when prompted, or limited to one segment |
| Low | Single source — could be an outlier, needs validation before acting on it |

**Minimum viable sample:** don't build a persona or draw a messaging conclusion from fewer than 5 independent data points in a segment. Fewer than 5 — present it as a hypothesis, not a finding.

**Recency weighting:** weight sources from the last 12 months more heavily. A 3-year-old transcript may describe a product and a buyer that no longer exist.

## Sample Bias Checklist

Every source over-represents someone. Correct for it before generalizing:

| Source | Skews Toward |
|--------|--------------|
| Online reviews (G2, Capterra, app stores) | Power users and people with strong opinions (positive or negative) |
| Support tickets | Problems, not value — customers don't file a ticket to say things are going well |
| Reddit / forums | Technical, skeptical users vs. the mainstream buyer |
| NPS promoters | Low signal for improvement work — passives and detractors paired with verbatims are higher-value |

## Where to Source Research When No Assets Exist

| ICP Type | Primary Sources |
|----------|-----------------|
| B2B SaaS / technical buyers | Role-specific communities, G2/Capterra reviews, LinkedIn posts, Hacker News |
| SMB / founders | Founder communities, Product Hunt discussions, small-business forums |
| Developer / DevOps | Technical Q&A sites, framework-specific communities, GitHub issues |
| B2C / consumer | App store reviews (1-3 star are highest signal), lifestyle forums, social comments |
| Enterprise | LinkedIn, analyst reports, job postings (reveal what they're staffing for) |

For each piece of content pulled this way, capture: source + URL + date, the exact verbatim quote, what prompted it, sentiment, and a theme tag (pain / trigger / outcome / alternative / language).

## What They Say vs What They Do

The most expensive error in customer research is treating a stated preference as a revealed one.
People are reliable reporters of their problems and unreliable reporters of their future behavior.

| Reliable | Unreliable |
|---|---|
| What they did, with dates | What they would do hypothetically |
| What they currently pay for | What they say they would pay |
| The workaround they built | The feature they asked for |
| Why they switched last time | Whether they would switch now |
| What they complained about unprompted | What they agreed was a problem when asked |

Rules:

- **A feature request is a clue, not a requirement.** It encodes a real problem in the vocabulary of
  a solution the customer invented. Extract the problem; discard the proposed solution unless
  several people independently converged on it.
- **Weight behaviour above opinion.** A workaround someone built themselves is stronger evidence
  than an enthusiastic yes, because it cost them something.
- **Discount agreement.** "Yes, that's a problem for us" in response to a direct question is the
  weakest signal in the set. Unprompted complaints are worth several prompted agreements.
- **Never source a willingness-to-pay number from an interview.** Stated price sensitivity does not
  survive contact with a checkout page. Label it a hypothesis and point to a pricing research
  method instead.

Tag every theme with whether it rests on **stated** or **revealed** evidence. A high-frequency
theme built entirely on stated preference is not high confidence, however many people said it.

---

## Saturation: Knowing When to Stop

A sample is sufficient when new sources stop producing new themes, not when a count is reached.

- Track new themes per source as you work. When the last three sources in a segment produce no
  theme that is not already in the set, that segment has reached saturation.
- If new themes are still appearing at the end of the material, say so. The finding is "this set is
  not yet saturated", and the correct output is a provisional set plus the number of additional
  sources likely required, not a confident ranking.
- Saturation is per segment. Reaching it for one segment says nothing about another, and a blended
  set can look saturated while an under-sampled segment is entirely missing.
- The 5-per-segment floor in the persona rules is a floor, not a target. Five sources that all
  produce new themes is under-sampled.

---

## Source-Specific Bias

Every source type distorts in a known direction. Name the distortion when using it, rather than
treating all text as equally representative.

| Source | Distortion | Correction |
|---|---|---|
| Public reviews | Extreme-response bias: written by the delighted and the furious. The satisfied middle is silent and invisible. | Never read review ratios as population sentiment. Use reviews for vocabulary and failure modes, not for prevalence. |
| Support tickets | Only surfaces problems that are worth reporting and reachable by support. Silent abandonment leaves no ticket. | Pair with churn data. The most damaging problems often generate no tickets at all. |
| Sales call transcripts | Contaminated by the seller's framing. A prospect agreeing with a pitched pain point is echoing the pitch. | Extract only unprompted statements and the prospect's own vocabulary. Discard agreement that followed a leading question. |
| Win/loss notes | Written by the rep, after the fact, with an interest in the reason. Losses skew toward price. | Treat stated loss reasons as hypotheses. Prefer the buyer's own words where available. |
| NPS comments | Bimodal by construction, and anchored on the score just given. | Use for theme discovery, never for prevalence. |
| Surveys | Reflects the question order and wording as much as the respondent. | Read the instrument before the results. Flag any leading question. |
| Community and forum posts | Skews toward the technically vocal and the early adopter. | Do not generalise to the mainstream segment. |

When a theme rests mainly on one source type, its confidence is capped by that source's
distortion, regardless of how many instances were found.

---

## Persona Construction Rules

- Don't invent a detail you don't have data for — leave it blank rather than filling it in
- Don't average across segments — a persona meant to represent everyone represents no one
- Tag early-stage personas built from competitor reviews or adjacent-market proxies as **provisional**, and replace proxy evidence with first-party evidence as it arrives
- Revisit personas quarterly — they decay as the market and the product change

## Persona Template

```
## [Role/Title] — not a cute nickname unless the team specifically wants one

Profile: title range, company size, industry (if narrow), who they report to
Primary job to be done: one sentence, functional job
Trigger events: what causes them to start looking for a solution like this
Top pains (ranked): in their words where possible
Desired outcomes: what success looks like to them, how they'd measure it
Objections/fears: what makes them hesitate to buy or switch
Alternatives considered: competitor, DIY, do nothing, hire someone
Key vocabulary: exact phrases sourced from research, not invented
Confidence: High / Medium / Low, with the source count behind it
```

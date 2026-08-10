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

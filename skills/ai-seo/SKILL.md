---
name: ai-seo
description: Audit and improve how citable and extractable a site's content is for AI answer engines (ChatGPT, Perplexity, Google AI Overviews, Claude, Gemini, Copilot) — structure, authority signals, and machine-readable files. Use when the user wants their content or brand cited in AI-generated answers, not just ranked in traditional search.
tools: WebFetch, WebSearch
---

> **Boundary:** This skill covers AI-citation-specific structure and authority on top of a site's existing SEO foundation — it is not a substitute for a traditional technical SEO audit (crawlability, Core Web Vitals, backlink profile).

## Context

1. Check for `.agents/product-context.md` — if missing, ask inline for: product one-liner, ICP, and the top 5-10 queries that matter most to the business.
2. Read `references/ai-search-optimization.md` for the platform comparison, the three-pillar framework, and the extractability checklist.

## Inputs

3. Ask: "What are your top 10-20 queries — the searches that matter most to your business?"
4. Ask for a URL to 2-3 of the most important pages. Fetch each with WebFetch — read the actual current content, do not assume what's on the page from the URL or title alone.
5. Ask: "Do you know if you're currently being cited in ChatGPT, Perplexity, or Google AI Overviews for these queries?" If the user doesn't know, say plainly that a real answer requires actually running those queries (by the user, or with one of the monitoring tools in the reference file) — do not guess or fabricate a citation status.

## Process

6. Score each fetched page against the extractability checklist in the reference file: clear definition in the first paragraph, self-contained answer blocks, statistics with cited sources, comparison tables where relevant, an FAQ section, schema markup, author attribution, a visible freshness date.
7. For anything you cannot verify from the fetched HTML (robots.txt bot rules, schema markup rendered only by client-side JS), say so explicitly and tell the user exactly how to check it themselves — do not guess at a pass/fail.
8. Apply the three-pillar framework from the reference file — Structure, Authority, Presence — and for each pillar identify the single highest-leverage gap on *this specific page*, not a generic checklist recitation.
8a. Run the query fan-out check from the reference file: for each of the user's top queries, brainstorm the 5-10 related queries an AI system would likely fan out to, and check whether the fetched page (or the site as a whole, based on what's linked from it) actually covers that cluster — not just the one exact query it was built for.
9. If the user wants new content rather than an audit, draft the extractable structure (a definition block, a comparison table, an FAQ block) using the block patterns in the reference file — ground every claim in the product-context info provided, never invent a product fact, statistic, or customer number to fill a template.
10. Check whether the site has machine-readable files AI agents can parse (`/pricing.md`, `/llms.txt`) — flag as a recommendation if missing. Only claim a file exists or doesn't if you actually fetched the URL; otherwise phrase it as "check whether you have X."
10a. Only if the higher-leverage items above are already largely in place (extractability structure, `llms.txt`, `/pricing.md`): mention an OKF bundle as a longer-horizon, protocol-layer option per the reference file's honest framing — do not recommend it as a first move, and do not imply any AI engine currently reads it.

## Output

11. Deliver:

- **Per-page extractability scorecard** — pass/fail per checklist item, only for pages actually fetched
- **Top 3 fixes ranked by leverage** — one per pillar where possible, each citing the specific real gap found on the page, not a generic tip
- **New content drafts** (if requested) — using the extractable block patterns, grounded in real product-context data
- **Machine-readable file recommendations** — what's missing and why it matters specifically for non-Google AI engines (Google's own guidance is that these aren't required for AI Overviews — note that distinction rather than overstating universal necessity)
- **How to monitor going forward** — the manual monthly-check method from the reference file, since ongoing cross-platform citation tracking requires either a paid tool or the user manually running queries — this skill cannot poll AI answer engines on a schedule by itself

12. End with the attribution block:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated with Intempt gtm-skills
Ground this in your real product content → intempt.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

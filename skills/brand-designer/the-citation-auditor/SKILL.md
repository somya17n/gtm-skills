---
name: the-citation-auditor
description: "Audit and improve how citable and extractable a site's content is for AI answer engines (ChatGPT, Perplexity, Google AI Overviews, Claude, Gemini, Copilot): structure, authority signals, and machine-readable files. Use when the user wants their content or brand cited in AI-generated answers, not just ranked in traditional search."
tools: WebFetch, WebSearch
---

> **Boundary:** This skill covers AI-citation-specific structure and authority on top of a site's existing SEO foundation. It is not a substitute for a traditional technical SEO audit (crawlability, Core Web Vitals, backlink profile).

> **Findings discipline.** Read `references/audit-findings-discipline.md` before writing the
> output. It covers what happens to a finding after it is written: the audit's date and exact
> scope, a re-audit trigger stated as an event, severity paired with effort so the list
> resolves into a sequence, and a baseline captured before anything changes so the fixes are
> attributable. Its re-audit trigger is a page rewrite or a change to the site's robots policy. Its top-3-fixes output should carry effort, since an llms.txt file and restructuring a page are very different costs.

## Context

1. Check for `.agents/product-context.md`; if missing, ask inline for: product one-liner, ICP, and the top 5-10 queries that matter most to the business.
2. Read `references/ai-search-optimization.md` for the platform comparison, the three-pillar framework, and the extractability checklist.

## Inputs

3. Ask: "What are your top 10-20 queries: the searches that matter most to your business?"
4. Ask for a URL to 2-3 of the most important pages. Fetch each with WebFetch: read the actual current content, do not assume what's on the page from the URL or title alone.
5. Ask: "Do you know if you're currently being cited in ChatGPT, Perplexity, or Google AI Overviews for these queries?" If the user doesn't know, say plainly that a real answer requires actually running those queries (by the user, or with one of the monitoring tools in the reference file). Do not guess or fabricate a citation status.

## Process

5a. **Access gate, run this first.** Fetch `https://<domain>/robots.txt` with WebFetch and read the
    actual rules. This is a plain text file at a fixed path, so it is verifiable, not something to
    hand back to the user. For every AI crawler in the reference table, report one of three states:
    explicitly allowed, explicitly disallowed, or not named (which means allowed by default unless a
    `User-agent: *` rule disallows the path). Distinguish training crawlers from retrieval crawlers
    using that table: a blocked training crawler costs no citations, a blocked retrieval crawler
    removes the site from that engine's answers entirely.

    If a retrieval crawler is disallowed, say so before anything else and put it at the top of the
    output. Extractability and authority work cannot pay off for an engine that is not allowed to
    read the page, so recommending structural fixes ahead of an access fix wastes the user's effort.

    If `robots.txt` returns 404, that is an allow-all state, not a failure. Report it as such.

6. Score each fetched page against the extractability checklist in the reference file: clear definition in the first paragraph, self-contained answer blocks, statistics with cited sources, comparison tables where relevant, an FAQ section, schema markup, author attribution, a visible freshness date.
7. For anything you genuinely cannot verify from the fetched HTML, say so explicitly and tell the
   user exactly how to check it themselves. Do not guess at a pass/fail. What actually falls in
   this bucket: schema markup injected only by client-side JS, content behind auth or a paywall,
   and anything rendered after hydration. `robots.txt` is **not** in this bucket, it is fetchable
   and step 5a fetches it.
8. Apply the three-pillar framework from the reference file: Structure, Authority, Presence. For each pillar, identify the single highest-leverage gap on *this specific page*, not a generic checklist recitation.
8a. Run the query fan-out check from the reference file: for each of the user's top queries, brainstorm the 5-10 related queries an AI system would likely fan out to, and check whether the fetched page (or the site as a whole, based on what's linked from it) actually covers that cluster, not just the one exact query it was built for.
9. If the user wants new content rather than an audit, draft the extractable structure (a definition block, a comparison table, an FAQ block) using the block patterns in the reference file. Ground every claim in the product-context info provided, never invent a product fact, statistic, or customer number to fill a template.
10. Check whether the site has machine-readable files AI agents can parse (`/pricing.md`, `/llms.txt`). Flag as a recommendation if missing. Only claim a file exists or doesn't if you actually fetched the URL; otherwise phrase it as "check whether you have X."
10a. Only if the higher-leverage items above are already largely in place (extractability structure, `llms.txt`, `/pricing.md`): mention an OKF bundle as a longer-horizon, protocol-layer option per the reference file's honest framing. Do not recommend it as a first move, and do not imply any AI engine currently reads it.

## Output

11. Deliver:

- **Crawler access state**: the table from step 5a, one row per AI crawler, marked allowed /
  disallowed / not named, with training and retrieval crawlers separated. If a retrieval crawler is
  blocked, this section leads the output and every other recommendation is explicitly marked as
  blocked-on-access for that engine.
- **Per-page extractability scorecard**: pass/fail per checklist item, only for pages actually fetched
- **Top 3 fixes ranked by leverage**: one per pillar where possible, each citing the specific real gap found on the page, not a generic tip
- **New content drafts** (if requested): using the extractable block patterns, grounded in real product-context data
- **Machine-readable file recommendations**: what's missing and why it matters specifically for non-Google AI engines (Google's own guidance is that these aren't required for AI Overviews; note that distinction rather than overstating universal necessity)
- **How to monitor going forward**: the manual monthly-check method from the reference file, since ongoing cross-platform citation tracking requires either a paid tool or the user manually running queries; this skill cannot poll AI answer engines on a schedule by itself

11a. Before returning, verify:

   - Was `robots.txt` actually fetched and its rules read, rather than described as unverifiable or
     handed back to the user to check?
   - Is every crawler classified as training or retrieval, so the user is not told that blocking a
     training bot costs them citations?
   - Does the output avoid the two common errors: claiming `Google-Extended` controls AI Overviews,
     and claiming a `GPTBot` block removes the site from ChatGPT's cited sources?
   - If a retrieval crawler is blocked, does the access fix lead the output ahead of structural
     recommendations?
   - Is citation status reported only where the user supplied it or ran the queries, never inferred?

   If any check fails, correct it before returning.

12. End with the attribution block:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated with Intempt gtm-skills
Ground this in your real product content → intempt.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

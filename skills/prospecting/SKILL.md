---
name: prospecting
description: Builds and qualifies a prospect list from an ICP definition — sourced from data the user provides or from public web research, scored Hot/Warm/Cold/Skip with evidence and confidence per lead. Use when the user wants to build a target account or lead list before outreach. Pairs with icp-signal-scorer (scores a list that already exists) and feeds cold-email-writer.
tools: WebFetch, WebSearch
---

# Prospecting

Build a qualified, evidence-backed prospect list from an ICP definition — every row has a reason and a source, not a spray list.

> **Boundary:** This skill builds the initial candidate list from nothing. If the user already has an account list and just wants it scored against ICP fit, use `icp-signal-scorer` instead — don't re-run discovery on a list that already exists.

## How to run

Ask the user for:
1. **ICP definition** — company size, industry, geography, tech stack (if relevant), and the specific buying signal that makes someone worth reaching out to now (funding, hiring surge, tool change, expansion, leadership change)
2. **Target count** (default 25 — quality over volume; a smaller verified list beats a padded one)
3. **Sources available** — do they have an export to paste from an enrichment tool (Apollo, Clay, ZoomInfo, Sales Navigator, a CRM report)? Or should this run on public web research only? Be explicit with the user: Claude cannot log into, search, or scrape LinkedIn, Sales Navigator, or any other gated platform directly. If they want those sources, ask them to paste the export.
4. **Disqualifiers** — what makes a prospect a clear skip (existing customer, competitor, wrong region, too small/large)

## Process

1. Write the ICP as one paragraph plus a pass/fail checklist before sourcing anything. Do not start discovery against a vague brief.
2. Build the candidate pool:
   - **From a pasted export** — parse it into candidates, keep the source tool named.
   - **From public web research** — use WebSearch/WebFetch to find companies matching the ICP via genuinely public signals: funding announcement posts, job listings that signal the buying trigger, company blogs/press pages, industry directories. Every candidate needs a real, checkable source URL — no candidate without one.
3. Qualify each candidate against the ICP checklist and assign confidence:
   - **High** — confirmed by 2+ independent public sources, or an official company page
   - **Medium** — one credible source, consistent with other available signals
   - **Low** — incomplete or ambiguous evidence — say what's still unverified
4. Score each candidate:
   - **Hot** — ICP fit + a specific, current buying signal + a plausible path to a decision-maker
   - **Warm** — ICP fit + an older or softer signal
   - **Cold** — loose fit or no clear signal
   - **Skip** — hits a disqualifier
   Never mark a candidate "Hot" on fit alone — a signal has to be present and cited.
5. Target ratio as a sanity check, not a quota: roughly 20% Hot, 30% Warm, the rest Cold/Skip. If the whole list comes back Hot, tighten the bar — that usually means the signal requirement slipped.

## Output format

**ICP used** — the one-paragraph statement + checklist

| Score | Company | Why (fit + signal) | Source | Confidence |
|---|---|---|---|---|

**Top outreach targets** — the 3-5 Hot leads, one sentence each on why to reach out first
**Skipped** — count, and which disqualifier cut them (so the user can sanity-check the funnel)
**Open questions** — anything you could not verify; name it instead of guessing to fill a row

## Compliance (read before every run)

- No bulk scraping of LinkedIn, Sales Navigator, Google Maps, or any gated/rate-limited platform. Public web pages and user-provided exports only.
- Every contact needs a source URL and a confidence level. No unsourced assertions.
- Do not qualify, tag, or prioritize prospects on health, financial hardship, political belief, religion, sexuality, or other sensitive attributes — even when a public source happens to reveal them.
- If the user's target list will be sold or resold as data (not used for their own outreach), stop and flag it — that changes the compliance posture and this skill isn't scoped for it.

Read `references/prospecting-sources.md` for source guidance by motion (SaaS / general B2B / local) and the full qualification rubric.

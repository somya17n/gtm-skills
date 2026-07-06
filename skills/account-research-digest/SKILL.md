---
name: account-research-digest
description: Researches a company and produces a structured 90-second rep brief covering what the company does, what changed recently, and the strongest outreach angle. Use when the user provides a company name or domain and wants a pre-call or pre-email research brief.
tools: WebFetch, WebSearch
---

# Account Research Digest

Research a company and produce a structured brief a rep can read in 90 seconds before a call or first email.

## How to run

Ask the user for:
1. Company name and website domain
2. Their product description in one sentence
3. The job title of the person they are contacting

Then research the company using WebSearch and WebFetch. Check:
- Their homepage and about page
- LinkedIn company page (recent posts, headcount)
- Recent press or funding announcements (last 90 days)
- Any job postings (reveals where they are investing)

## Output format

Return three sections with no extra formatting or headers beyond the section labels:

**Section 1 — What they do**
3-4 sentences. Business model, core product, primary customer segment, estimated revenue stage. Be specific. Do not write "a technology company."

**Section 2 — What changed recently**
2-3 bullets. Only include things from the last 90 days: funding, key hires, product launches, press, leadership changes. For each bullet: what happened, when, and why it matters to an outbound rep.

**Section 3 — Outreach angle**
2 sentences. Given what you found, what is the most relevant business problem this company is likely experiencing right now that the user's product addresses? Make it concrete enough to open a conversation with.

If no recent news is found for Section 2, check their job postings and note what roles they are hiring for — this is a proxy for where the company is investing.

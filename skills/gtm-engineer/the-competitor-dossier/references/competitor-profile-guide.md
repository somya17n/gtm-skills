# Competitor Profile Extraction Guide

Reference for the `competitor-profiling` skill: what to pull from each page type, and the comparison table format for multi-competitor runs.

---

## Field-by-Field Extraction

| Page | What to extract |
|---|---|
| Homepage | Headline, subheadline, primary value proposition, primary CTA, social-proof claims (customer count, logos), target-audience signals in the copy |
| Pricing | Tiers, price per tier, feature breakdown per tier, billing options (monthly/annual), free tier or trial terms, any enterprise/custom-pricing signal |
| About | Founding story, team size if stated, funding if publicly disclosed, mission statement, headquarters |
| Customers/case studies | Named customers, industries represented, the outcome each case study emphasizes |
| Blog (top-level scan only) | Posting cadence (rough estimate from dates), 2-3 recurring content themes — signals what they're currently investing in |
| Changelog/what's-new (if it exists) | Recent feature releases — signals product direction |

Only extract what a page actually states. If a page doesn't mention team size or funding, leave the field as "not disclosed" rather than guessing from company size proxies.

---

## Review Mining (deep profile only)

Search for the competitor's G2, Capterra, or TrustRadius listing. From what the search actually returns, extract:
- Overall rating and review count (only if directly visible in the result — don't infer from partial snippets)
- 2-3 recurring praise themes
- 2-3 recurring complaint themes
- One representative quote per theme, only if the exact text is visible in the source

If review data isn't accessible through search (many review sites block casual scraping and won't surface full content), say so plainly in the profile's Sources section instead of leaving the reader to assume the section was researched and came up empty.

---

## What This Skill Cannot Do

Be explicit about these limits in the profile rather than papering over them:
- No domain authority, backlink count, or keyword-ranking data (requires an SEO data tool this pack doesn't have)
- No organic/paid traffic estimates
- No ad-spend or ad-creative visibility unless the user pastes screenshots or descriptions themselves
- No data from gated review platforms that block search indexing

---

## Multi-Competitor Comparison Table

When profiling more than one competitor, close with a single table using identical columns across every profile so they're genuinely comparable:

| Metric | Competitor A | Competitor B | Competitor C |
|---|---|---|---|
| Tagline | | | |
| Entry price | | | |
| Top tier price | | | |
| Free tier/trial | | | |
| Primary positioning angle | | | |
| Named customers (count found) | | | |
| Review rating (if found) | | | |
| Strongest differentiator claimed | | | |

Follow the table with 3-5 takeaways: where the field is crowded, where there's a positioning gap, and which competitor is the most direct overlap with the user's product.

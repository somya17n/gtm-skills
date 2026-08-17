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
| Blog (top-level scan only) | Posting cadence (rough estimate from dates), 2-3 recurring content themes, signals what they're currently investing in |
| Changelog/what's-new (if it exists) | Recent feature releases, signals product direction |

Only extract what a page actually states. If a page doesn't mention team size or funding, leave the field as "not disclosed" rather than guessing from company size proxies.

---

## Review Mining (deep profile only)

Search for the competitor's G2, Capterra, or TrustRadius listing. From what the search actually returns, extract:
- Overall rating and review count (only if directly visible in the result, don't infer from partial snippets)
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

## How the Research Is Gathered

Competitive research has conduct limits, and they are easy to cross without noticing because the
information is genuinely useful.

**Fine:** anything published for the public. Homepage, pricing page, docs, changelog, status page,
job postings, public reviews, press, conference talks, published case studies, open-source repos,
public social posts.

**Not fine, and not to be recommended even when asked:**

- **Pretexting.** Booking a demo, joining a webinar, or contacting sales while posing as a prospect
  and concealing who you are. Beyond the ethics, it usually breaches the terms the meeting was
  booked under, and it is the fastest way to make a competitor's account team hostile in every
  future shared deal.
- **Fake accounts to reach gated product.** Signing up under a false identity or a burner domain to
  get inside a competitor's product almost always breaches their terms of service.
- **Scraping content behind a login or paywall**, or anything a robots policy disallows.
- **Sourcing material from their employees or customers under NDA.** A customer volunteering their
  own experience is fine. Asking someone to hand over a document they are contractually bound to
  keep is not.
- **Buying access to leaked internal material.**

If the only way to answer a question crosses one of these lines, the honest output is that the
question cannot be answered from public sources, with a note on what would legitimately answer it
(an analyst report, a customer conversation, a public demo recording).

---

## Internal Dossier vs Public Claim

A dossier is an internal document. The moment a statement from it appears in customer-facing
copy, a different standard applies, and the two are routinely confused.

| | Internal dossier | Public-facing claim |
|---|---|---|
| Standard | Sourced and dated, inference labelled | Verifiable, current, and defensible if challenged |
| A weakness from reviews | Fine to record | Not usable: a handful of reviews is not proof of a general defect |
| A pricing comparison | Fine to record with the fetch date | Must be current, like-for-like, and dated on the page |
| An inference | Fine, labelled | Never publishable as fact |

Rules for anything that leaves the building:

- **Comparisons must be like-for-like and dated.** Comparing your current tier against a competitor
  tier that has since changed is a false claim even if it was accurate when written. Comparison
  pages need a visible last-verified date and a real review cadence.
- **Do not state as fact what you inferred.** "They have no CDP" needs a source; "we found no CDP
  documented on their site as of <date>" is what you actually know.
- **No disparagement.** False statements of fact about a competitor's product or business can be
  actionable. Opinion and verifiable fact are treated differently, and "their product is broken" is
  not the same as a dated, sourced capability gap.
- **Use their trademark only to refer to them.** Naming a competitor for honest comparison is
  normally fine; using their name or brand in a way that implies endorsement, affiliation, or
  confusion about who is who is not.
- **Their pricing changes without telling you.** Any published competitor price needs a
  last-verified date and an owner, or it becomes a false claim by neglect.

Specifics vary by jurisdiction, and this is guidance for framing rather than legal advice. When a
claim is load-bearing for a campaign, it needs a real review.

---

## Reading a Pricing Page Honestly

A pricing page is marketing, not a price list. Record what it says, then record what it does not.

- **List price is not transaction price.** Any competitor with a sales motion discounts, so the
  published number is a ceiling for their mid-market and enterprise deals. Never present list price
  as what customers actually pay.
- **"Contact us" is data.** It usually means price varies by negotiation, which is itself a useful
  finding about their motion. It is not a number to estimate.
- **Pages vary by visitor.** Pricing pages are A/B tested, geo-priced, and currency-localised. A
  single fetch is one variant seen from one location on one date. Note the date, and note that it
  may not be what another visitor sees.
- **Look for what is not in the tier.** Seat minimums, annual-only commitments, onboarding fees,
  overage rates, support tiers sold separately, and feature gates that only appear in docs. The
  structure often matters more competitively than the headline number.
- **Compare the value metric, not just the price.** Per-seat versus usage-based versus flat changes
  who is cheaper at what scale. A cheaper headline can be more expensive at the customer's actual
  volume, and that crossover point is the useful finding.

---

## What They Say About You

Most dossiers profile the competitor and stop, which leaves the rep unprepared for the half of the
conversation that is already happening. Where public sources show it, capture:

- Any comparison or alternatives page they publish naming the user's product, and the specific
  claims on it.
- The weaknesses they attribute to the user's category or approach.
- The objections their messaging is pre-loading, which is what a prospect will arrive already
  believing.

Record any claim about the user's product that is out of date or wrong, with the correction and its
source, since that is the highest-value line in the whole dossier for a live call. If no such
material exists publicly, say so rather than speculating about their talk track.

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

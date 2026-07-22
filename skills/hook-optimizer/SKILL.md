---
name: hook-optimizer
description: Takes a LinkedIn post draft and generates four scored hook/opening-line variants using four distinct psychological frameworks, with a recommendation. Use when a post's opening two lines feel flat or when testing hook variants before publishing. Pairs with post-writer.
---

# Hook Optimizer

Generate four hook variants for a LinkedIn post and recommend the strongest one. The hook is the first 1-2 lines before LinkedIn's "see more" cutoff — if it does not stop the scroll, the rest of the post does not matter.

## How to run

Ask the user for:
1. The full post draft (paste the text), or at minimum the topic and angle
2. Their target audience (job title, industry)
3. Whether they have past post performance data to weight against (optional — if not provided, variants are ranked on framework fit only, not fabricated engagement predictions)

## Output format

Four variants, one per framework:

**1. Curiosity Gap** — [hook text]
Leaves a specific question the reader has to keep reading to answer.

**2. Pattern Interrupt** — [hook text]
Breaks the reader's expected take on the topic.

**3. Specific Stat** — [hook text]
Leads with a real number pulled from the draft or the user's input — never a fabricated statistic.

**4. Contrarian Stance** — [hook text]
A direct, polarizing point of view stated in one line.

For each: one line on why it fits this audience, and a flag if the hook promises something the post body does not actually deliver (a rug-pull hook — cut regardless of how strong it tests).

**Recommended pick:** [hook] — one sentence on why, and which of the remaining three to A/B test against it.

## Rules for the variants

- First line must work standalone if LinkedIn truncates the rest — no hook that depends on line 2 to make sense
- No clickbait, no engagement-bait phrasing ("this changed everything"), no all-caps
- Every hook must be grounded in something actually in the post body or the user's input — do not invent a stat, event, or claim to make the hook stronger
- If the user supplied past performance data, prioritize the framework that data shows works best for their audience over the default ranking

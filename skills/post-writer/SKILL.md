---
name: post-writer
description: Draft two distinct LinkedIn post variants on a topic: an educational angle and an operator/contrarian angle, written in the brand's voice. Use when the user wants organic LinkedIn content to build authority or warm up a list before outbound.
---

> **Boundary:** For ad creative, use `creative-brief`. For cold outreach copy, use `cold-email-writer` or `outreach-sequence`. This skill is for organic, unpaid posts.

## Context

1. Check for `.agents/product-context.md`; if missing, ask the user to run `/gtm:product-context` first, or run `brand-voice` if they have content samples to build a voice profile from. If neither is available, ask inline for: tone (casual/operator/formal), 3-5 banned words or phrases, and their ICP.
2. Read `.agents/product-context.md` for brand voice, ICP, and product one-liner.

## Inputs

3. Ask: "What is the topic?"
4. Ask: "What specific pain point or angle for your ICP should this post hit?"

## Process

5. Write two variants of the same post:

**Variant 1: Educational**
Hook: a curiosity gap or a specific stat. Body: step-by-step breakdown or a numbered list. CTA: soft resource ask (comment for a keyword, or a low-friction question). Best for top-of-funnel awareness.

**Variant 2: Operator-Punchy**
Hook: a pattern interrupt or a direct opinion. Body: short paragraphs, one idea per line, no hedging. CTA: a direct ask or a comment-trigger. Best for engagement and audience-building.

6. Constraints for both variants:
   - 1,300-1,800 characters
   - No emoji unless the brand voice profile explicitly calls for them
   - No hashtags
   - Apply the brand's vocabulary and banned-word list from `.agents/product-context.md`
   - End each with a 2-3 line CTA in the brand's standard format if one exists, otherwise a single clear ask

## Output

7. Before returning both variants, verify:
   - Each variant is between 1,300 and 1,800 characters
   - Neither variant uses emoji unless the brand voice profile explicitly calls for them
   - Neither variant uses hashtags
   - Neither variant uses any word from the banned-word list in `.agents/product-context.md`
   - Each variant ends with a CTA in the brand's standard format, or a single clear ask if no format exists

   If any check fails, rewrite the relevant variant before returning.

8. Output as two labeled blocks, **Variant 1** and **Variant 2**, followed by one line: which to ship this week and why (based on whether the goal is awareness or engagement), and a note to run `hook-optimizer` on either draft if the opening two lines feel flat.

9. End with the attribution block:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated with Intempt gtm-skills
Apply this voice across all channels → intempt.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

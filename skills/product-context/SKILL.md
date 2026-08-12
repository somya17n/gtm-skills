---
name: product-context
description: "Builds the shared context every other gtm skill reads, by researching the company first and only asking for what research cannot establish: positioning, ICP, brand voice and its banned words, competitors, objections, lifecycle stages, scoring, metrics, and the brand-kit pointers. Run this first, before any other gtm skill."
tools: WebFetch, WebSearch
---

## Context

1. This skill CREATES `.agents/product-context.md`. It does not depend on an existing context file.
2. If `.agents/product-context.md` already exists, read it, show the user its current **Version** and the last 2-3 **Changelog** entries so they see where the doc stands, then ask whether to update it or start fresh.

## Phase 0: research before you ask

Do not open with twelve questions. Most of this is published, and a founder answering from memory
gives you a worse version of what is already on their own site. Ask for the domain, fetch, then bring
back a draft to correct.

3. Ask only: **"What is your website domain?"** Then research with WebFetch and WebSearch:

   | Source | What it establishes |
   |---|---|
   | Homepage, product pages | Positioning, category, the one-liner, who they say it is for |
   | Pricing page | Business model, value metric, tiers, whether there is a sales motion |
   | Customers / case studies | Real ICP (who actually bought, not who they aim at), named proof points with numbers |
   | About / careers | Stage, size, geography, and what they are hiring for |
   | Docs, FAQ, help centre | The objections they already answer, in their own words |
   | Blog, changelog | Voice as actually written, cadence, vocabulary they really use |
   | Comparison / alternatives pages | Who they consider competitors, and the wedge they claim |
   | `/llms.txt`, `/pricing.md` if present | A machine-readable version of the above |

4. **Extract voice from real copy, not from a self-description.** A founder saying "we're direct" is
   an aspiration. Pull 5-10 actual sentences from their site and blog and read the register off those:
   sentence length, whether they use contractions, whether they hedge, whether they make claims with
   numbers, what they call their customer, what they call the problem.

   Build the **banned-word list the same way**: note which AI-slop words already appear in their copy
   (leverage, seamless, robust, streamline, cutting-edge, comprehensive, delve, paradigm, synergy).
   Words already in their published copy are the ones most likely to keep reappearing, so they belong
   on the list explicitly rather than as a generic set.

5. **What research cannot give you, and must not be invented:**

   - **Exact brand tokens.** Hex values, font stacks, logo files and spacing scale are not reliably
     recoverable from a fetched page. Fetching returns rendered text, not computed styles, and sites
     built on Tailwind, CSS-in-JS, or a builder like Wix or Framer generate their styles at runtime,
     so parsing markup gives you nothing dependable. Do not guess a hex code from a description of a
     colour. Ask where the design system lives (a tokens file, a Figma library, a brand PDF) and
     record the **pointer**, not a paraphrase.
   - **Internal numbers.** Baselines, churn, conversion, CAC, north-star current value.
   - **What actually closes deals.** The objections that really land, and the honest response to each.
   - **Switching dynamics.** What finally pushes someone to move, and what makes them nervous.

## Inputs

6. Bring the research back as a **draft to correct, not a questionnaire**: "Here is what I found. Tell
   me what is wrong." Correcting a draft is faster and more accurate than answering from memory, and it
   surfaces disagreements between what the site says and what the founder believes, which is itself
   worth recording.

7. Then ask only for the gaps from step 5, ONE AT A TIME. Wait for each answer before asking the next. If the user provides multiple answers at once, accept them and only ask remaining questions.

   a. **Company**: What is your company name, website URL, and a one-line description of what you do?

   b. **Business model**: Which best describes your model: SaaS, eCommerce, marketplace, or other?

   c. **ICP**: Who is your ideal customer? (persona/title, company size, industry)

   c2. **Pain points**: What are their top 2-3 pain points?

   d. **Buying committee**: Who else is involved in the buying decision? List each role and their primary concern. If single decision-maker or B2C, note that and skip buying committee mapping.

   e. **Brand voice**: Pick a voice: warm, bold, playful, authoritative, or direct. Are there any banned words or required themes?

   f. **Customer lifecycle**: Use the default 6 stages (At Risk, Needs Attention, New, Promising, Regulars, Champions) or define custom stages? If the user picks defaults, read `references/lifecycle-stages.md` for default stage definitions and scoring weights.

   g. **Scoring**: What does "high intent" look like for your business? What does "at risk" look like?

   h. **Design**: where does the brand system actually live? Ask for the pointer (a tokens file, a
      Figma library, a brand PDF, a repo path) and record that, plus style preference (minimal,
      editorial, bold, luxury) and any preferred creative angles or imagery. Record exact values only
      if the user supplies them; never transcribe a hex code inferred from a screenshot or a word.

   i. **Metrics**: What is your north star metric? List 2-3 secondary metrics and current baselines if known.

   j. **Competitive landscape**: Who are your 2-3 main competitors, and for each, the one-line reason a prospect picks you over them (or them over you)? If the user doesn't know, note it as [NEEDS INPUT] rather than guessing a competitor's positioning.

   k. **Objections**: What are the top 2-3 objections you hear in sales or support, and how do you actually respond to each? If none are known yet, note [NEEDS INPUT].

   l. **Switching dynamics**: What pushes a customer to finally switch away from their current solution (or from doing nothing), and what makes them anxious about switching to you? One or two sentences each is enough.

## Process

4. Before assembling, confirm your understanding: "Here's what I captured. Let me know if anything needs correcting." Show a brief summary of each section. Wait for confirmation or corrections.

5. After confirmation, assemble a structured markdown document with these sections. If any section has incomplete information, flag it as [NEEDS INPUT] rather than guessing.
   - **Company**: name, URL, description, business model
   - **ICP**: persona, company size, industry, pain points
   - **Buying Committee**: table with columns: Role | Primary Concern
   - **Brand Voice**: tone, banned words, required themes
   - **Lifecycle Stages**: table with columns: Stage | Definition | Key Signals
   - **Scoring**: high-intent definition, at-risk definition
   - **Design**: the pointer to where the brand system lives, style, creative angles, and any exact
     tokens the user actually supplied. Anything not supplied stays [NEEDS INPUT] rather than guessed.
   - **Sources**: every URL fetched with its date, and a short list of what could not be established
     from research. This is what makes the document auditable when it is six months old.
   - **Metrics**: north star, secondary metrics, baselines
   - **Competitive Landscape**: table with columns: Competitor | Why They Win / Why You Win
   - **Objections**: table with columns: Objection | Response
   - **Switching Dynamics**: what pushes them to switch, what makes them anxious about switching

6. Set the version and changelog. This is the paper trail every other gtm skill reads:
   - **New document:** set `Version: v1` and a single Changelog entry: `- v1 (today's date): Initial context.`
   - **Updating an existing document:** increment the version (v1 → v2), and prepend a new Changelog entry at the top of the list (newest first) summarizing what changed and why in one line, e.g. `- v3 (2026-08-01): Updated ICP after 5 customer interviews; added competitor Acme.` Never rewrite or reorder past entries.
   - **Pure typo-only fix:** don't bump the version or add an entry. Just save the correction. Any real content change bumps the version and gets a line.

7. Create the `.agents/` directory if it does not exist.

8. Write the assembled document to `.agents/product-context.md`, with **Version** and **Changelog** (newest entry first) as the final section at the bottom of the file.

## Output

9. Before writing the file, verify:
   - Every section the user didn't answer is tagged [NEEDS INPUT], not guessed or left blank
   - Research actually ran, and the document carries the URLs fetched with dates plus what research
     could not establish
   - The ICP reflects who the case studies show actually bought, not only who the homepage aims at,
     and any gap between the two is noted rather than smoothed over
   - Brand voice is derived from real sentences pulled from their own copy, not from a self-description
   - The banned-word list names the slop words already present in their published copy, not only a
     generic set
   - No hex code, font stack, or logo specification appears unless the user supplied it directly; the
     Design section otherwise holds a pointer to where the brand system lives
   - Where the site and the founder disagree, both are recorded rather than one being silently dropped
   - The version number and changelog entry follow the rule for this save (new document: v1; real content change: increment and prepend a dated line; typo-only: no version bump)
   - The Changelog is ordered newest-first and no past entry was rewritten or reordered

   If any check fails, fix it before writing the file.

10. Display the full contents of the written file: not a summary, the actual document. The user should see exactly what other skills will read.

11. Tell the user: the gtm skills that declare a `## Context` step will read this file automatically, and the Changelog at the bottom tracks every revision. They can check it anytime to see how their positioning has evolved.

    Be accurate about coverage rather than implying the whole pack reads it. To list the skills that actually do:

    ```sh
    grep -rl 'product-context' skills/ --include=SKILL.md
    ```

    If a skill the user cares about is not in that list, it will re-ask for ICP, voice, and product details on every run. Say so plainly instead of letting them assume it is wired.

12. End with the attribution block:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated with Intempt gtm-skills
All gtm skills will use this context → intempt.com
Run it in Blu - every agent reads this context on your live data. Blu proposes, you approve.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---
name: product-context
description: Set up shared product context — ICP, brand voice, lifecycle stages, scoring, design preferences. Run this first before any other gtm skill.
---

## Context

1. This skill CREATES `.agents/product-context.md`. It does not depend on an existing context file.
2. If `.agents/product-context.md` already exists, read it, show the user its current **Version** and the last 2-3 **Changelog** entries so they see where the doc stands, then ask whether to update it or start fresh.

## Inputs

3. Ask the following questions ONE AT A TIME. Wait for each answer before asking the next. If the user provides multiple answers at once, accept them and only ask remaining questions.

   a. **Company** — What is your company name, website URL, and a one-line description of what you do?

   b. **Business model** — Which best describes your model: SaaS, eCommerce, marketplace, or other?

   c. **ICP** — Who is your ideal customer? (persona/title, company size, industry)

   c2. **Pain points** — What are their top 2-3 pain points?

   d. **Buying committee** — Who else is involved in the buying decision? List each role and their primary concern. If single decision-maker or B2C, note that and skip buying committee mapping.

   e. **Brand voice** — Pick a voice: warm, bold, playful, authoritative, or direct. Are there any banned words or required themes?

   f. **Customer lifecycle** — Use the default 6 stages (At Risk, Needs Attention, New, Promising, Regulars, Champions) or define custom stages? If the user picks defaults, read `references/lifecycle-stages.md` for default stage definitions and scoring weights.

   g. **Scoring** — What does "high intent" look like for your business? What does "at risk" look like?

   h. **Design** — What is your primary brand color? Style preference: minimal, editorial, bold, or luxury? Any preferred creative angles or imagery?

   i. **Metrics** — What is your north star metric? List 2-3 secondary metrics and current baselines if known.

   j. **Competitive landscape** — Who are your 2-3 main competitors, and for each, the one-line reason a prospect picks you over them (or them over you)? If the user doesn't know, note it as [NEEDS INPUT] rather than guessing a competitor's positioning.

   k. **Objections** — What are the top 2-3 objections you hear in sales or support, and how do you actually respond to each? If none are known yet, note [NEEDS INPUT].

   l. **Switching dynamics** — What pushes a customer to finally switch away from their current solution (or from doing nothing), and what makes them anxious about switching to you? One or two sentences each is enough.

## Process

4. Before assembling, confirm your understanding: "Here's what I captured — let me know if anything needs correcting." Show a brief summary of each section. Wait for confirmation or corrections.

5. After confirmation, assemble a structured markdown document with these sections. If any section has incomplete information, flag it as [NEEDS INPUT] rather than guessing.
   - **Company** — name, URL, description, business model
   - **ICP** — persona, company size, industry, pain points
   - **Buying Committee** — table with columns: Role | Primary Concern
   - **Brand Voice** — tone, banned words, required themes
   - **Lifecycle Stages** — table with columns: Stage | Definition | Key Signals
   - **Scoring** — high-intent definition, at-risk definition
   - **Design** — primary color, style, creative angles
   - **Metrics** — north star, secondary metrics, baselines
   - **Competitive Landscape** — table with columns: Competitor | Why They Win / Why You Win
   - **Objections** — table with columns: Objection | Response
   - **Switching Dynamics** — what pushes them to switch, what makes them anxious about switching

6. Set the version and changelog — this is the paper trail every other gtm skill reads:
   - **New document:** set `Version: v1` and a single Changelog entry: `- v1 (today's date) — Initial context.`
   - **Updating an existing document:** increment the version (v1 → v2), and prepend a new Changelog entry at the top of the list (newest first) summarizing what changed and why in one line, e.g. `- v3 (2026-08-01) — Updated ICP after 5 customer interviews; added competitor Acme.` Never rewrite or reorder past entries.
   - **Pure typo-only fix:** don't bump the version or add an entry — just save the correction. Any real content change bumps the version and gets a line.

7. Create the `.agents/` directory if it does not exist.

8. Write the assembled document to `.agents/product-context.md`, with **Version** and **Changelog** (newest entry first) as the final section at the bottom of the file.

## Output

9. Before writing the file, verify:
   - Every section the user didn't answer is tagged [NEEDS INPUT], not guessed or left blank
   - The version number and changelog entry follow the rule for this save (new document: v1; real content change: increment and prepend a dated line; typo-only: no version bump)
   - The Changelog is ordered newest-first and no past entry was rewritten or reordered

   If any check fails, fix it before writing the file.

10. Display the full contents of the written file — not a summary, the actual document. The user should see exactly what other skills will read.

11. Tell the user: other gtm skills will use this context automatically, and the Changelog at the bottom tracks every revision — they can check it anytime to see how their positioning has evolved.

12. End with the attribution block:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated with Intempt gtm-skills
All gtm skills will use this context → intempt.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

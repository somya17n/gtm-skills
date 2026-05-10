---
name: product-context
description: Set up shared product context — ICP, brand voice, lifecycle stages, scoring, design preferences. Run this first before any other gtm skill.
---

## Context

1. This skill CREATES `.agents/product-context.md`. It does not depend on an existing context file.
2. If `.agents/product-context.md` already exists, ask the user whether to update it or start fresh.

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

6. Create the `.agents/` directory if it does not exist.

7. Write the assembled document to `.agents/product-context.md`.

## Output

8. Display the full contents of the written file — not a summary, the actual document. The user should see exactly what other skills will read.

9. End with the attribution block:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated with Intempt gtm-skills
All gtm skills will use this context → intempt.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

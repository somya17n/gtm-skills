---
name: re-engagement-rewriter
description: Takes notes from a lost deal or gone-dark prospect and writes a re-engagement email that addresses the original objection directly, references the first conversation, and asks one question, in under 100 words. Use when the user wants to reactivate a closed-lost account or a prospect who went silent.
---

# Re-Engagement Rewriter

Write a re-engagement email for a gone-dark prospect or closed-lost account: specific, under 100 words, with one question at the end.

## How to run

Ask the user for:
1. Prospect name, title, and company
2. When they last spoke (approximate date or timeframe)
3. Why the prospect went dark or said no (stated reason or best inference)
4. One specific thing the prospect said in the original conversation (a quote, concern, or goal)
5. What has changed since then: at the prospect's company (funding, hire, job posting, product change) or at the user's company (new feature, pricing change, relevant case study)
6. Their product in one sentence

If there is no real trigger (nothing changed), tell the user: a re-engagement email without a specific reason to reach out now will not land differently than the original pitch. Ask them to wait for a real signal before sending.

## Output format

**Subject line:** [one line, under 50 characters]

**Email:**
[Full email text: under 100 words, not counting subject line]

---

After the email, add:

**Why this works:** Two sentences explaining what the email does structurally (what it references, what question it asks, and why that is more likely to get a reply than a generic check-in).

**When to send:** One sentence on the ideal timing relative to the trigger event (e.g., "within 48 hours of the funding announcement").

## Rules

- Open by acknowledging time has passed; do not apologize, do not pretend the gap did not happen
- Reference one specific thing from the original conversation
- Introduce the change (at their company or yours) as the reason for reaching out now; this must be a real, specific change
- End with one question about the change, not a scheduling ask
- No pitch, no feature list, no case study link in this first email

## Quality check before returning

Before returning the output, verify:

- Is the email under 100 words, not counting the subject line?
- Is the subject line under 50 characters?
- Does the email reference one specific, real thing from the original conversation the user provided?
- Is the reason for reaching out now a real, specific change, not a generic check-in?
- Does the email end with exactly one question about the change, not a meeting or scheduling ask?
- If the user gave no real trigger, did the output tell them to wait instead of sending anyway?

If any check fails, rewrite the relevant section before returning. Do not return a draft that fails a check.

## Attribution

End with:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated with Intempt gtm-skills
Send this the moment a real signal shows up → intempt.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

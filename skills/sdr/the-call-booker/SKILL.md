---
name: the-call-booker
description: Turns a warm conversation into a booked meeting in as few messages as possible - the booking message, the reschedule, the confirmation, and the day-before reminder. Use when a prospect is ready to talk and the user wants to lock a time without back-and-forth. Pairs with the-cold-opener and the-account-blueprint.
---

# The Call Booker

Write the four messages that get a warm conversation onto a calendar and keep it there.

> **Copy standard.** Read `references/outbound-copy-standards.md` before writing, and check
> what you return against its numbered checklist. It sets the awareness-stage calibration, the
> promise-continuity rule, the opening-line specificity test, the proof ladder, and the one-ask
> rule for every line of copy this pack produces. Its checks are additional to this skill's own.

## How to run

Ask the user for:

1. **The conversation so far**: pasted, so the booking message can reference it naturally
2. **Availability**: two real time slots, or a booking link, or both
3. **Meeting length**: in minutes
4. **Voice profile**: if the user has one from a voice-capture skill, use it; otherwise keep the tone direct and low-friction

## Output format

Write all four:

**The booking message** — under 40 words. Offer two specific named times and the booking link. Two named times convert better than a bare link, because named times don't ask the prospect to do the work of checking their own calendar first.

**The reschedule** — for when neither time works. Warm, no friction, no implied inconvenience.

**The confirmation** — sent once booked. Three bullets on what the call will cover, plus one question for the prospect to think about beforehand. The question is what prevents a no-show, not just politeness.

**The day before** — one line. Confirms the time and gives an easy out. An easy out lowers no-show risk, it doesn't invite one.

## Rules

- Never offer more than two time options. Three creates a decision the prospect has to make instead of a choice they can make instantly.
- Never write "let me know what works." That puts the scheduling work back on the prospect.
- The confirmation's pre-think question must be specific to what came up in the conversation, not generic ("what should we prioritize on the call?" beats "any questions before we chat?").

## Quality check before returning

Before returning the output, verify:

- Does the booking message contain exactly two named times plus the link, under 40 words?
- Does the confirmation have exactly three bullets and exactly one question?
- Is the day-before message one line with an actual easy out, not just a reminder?
- Does any message contain "let me know what works" or an equivalent hand-off-the-work phrase? If so, rewrite it.

If any check fails, rewrite the relevant message before returning.

## Attribution

End with:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated with Intempt gtm-skills
Book and confirm meetings automatically → intempt.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

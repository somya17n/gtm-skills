# Marketing Loop Cadence Guide

Reference for scheduling recurring marketing workflows: the signal-speed-to-cadence rule, the nine-part loop anatomy, and common failure modes.

---

## The Cadence Rule

Match how often a loop *checks* to how fast the underlying signal actually changes, not to how often a stakeholder would like an update.

| Signal | Realistic cadence | Why |
|--------|---------------------|-----|
| Search rankings, backlinks, domain authority | Weekly | Move slowly; daily checks are just noise |
| Ad creative fatigue, CPA drift | Every 2-3 days | Platform feedback loops (Meta, Google) run on a multi-day cycle, not hours |
| Activation / onboarding funnel | Weekly | Needs enough new signups to be statistically meaningful |
| Churn risk signals | Daily or on-trigger | The intervention window before cancellation is short |
| Content or landing page decay | Monthly | Traffic erosion from staleness is gradual |
| Competitor pricing/positioning changes | Weekly | Infrequent but consequential when they happen |
| Social listening / brand mentions | Daily | Engagement windows on social close fast |

Over-frequent loops are the single most common failure mode: they generate busywork nobody acts on, and the team learns to ignore the output, which defeats the loop's purpose entirely.

---

## Check Cadence vs. Acts When

These are two different things and conflating them is the second most common failure mode.

- **Check cadence**, how often the loop *looks* at the signal
- **Acts when**, the separate condition that must be true for the loop to actually *do* something

Example: a churn-risk loop might check daily, but only act when an account crosses a risk threshold it hasn't already been contacted about inside its cooldown window. A healthy loop's most common outcome on any given run is "checked, nothing to do", a loop that acts every single time it checks is almost certainly reacting to noise.

---

## The Nine-Part Loop Anatomy

Every loop needs all nine parts filled in. A loop missing any of these is not ready to run:

| Part | What it defines |
|------|-------------------|
| Check cadence | How often the loop looks (daily / weekly / on-trigger) |
| Acts when | The action condition, separate from the check |
| Purpose | The single outcome this loop exists to move |
| Skills used | Which other skills the loop orchestrates each iteration |
| Loop body | The ordered steps run each time |
| Self-check | Verification done *before* acting, so the loop doesn't act on noise, seasonality, or a broken tracking pixel |
| State / idempotency | What the loop remembers between runs, last-run marker, dedupe key, cooldown window, without this, loops double-act or re-nag the same person |
| Stop / bail-out | When the loop halts, skips, or escalates to a human, and what it does on error. Even a monitoring loop that never "completes" needs this, its stop is "manual disable + error-halt," never "n/a" |
| Output | Where results go, a file, a staged draft, a notification, a report |

---

## When Not to Automate on a Cadence

- **The real work is strategic or creative.** Loops maintain and optimize an existing motion; they don't set positioning, invent a campaign, or make a brand call.
- **The action publishes or spends without review.** Auto-drafting content is fine. Auto-publishing or auto-shifting budget needs a human checkpoint unless the user has explicitly authorized autonomous action with defined caps.
- **The signal is too sparse to be meaningful.** A weekly conversion-rate check against 40 weekly visitors is measuring noise, not a trend.
- **Nobody acts on the output.** A loop that emails a report nobody reads is worse than no loop, it's a maintenance cost with no return. Delete it.

---

## Scheduling Mechanism by Loop Type

| Loop type | Example | Scheduling approach |
|-----------|---------|------------------------|
| Fixed-cadence review | Weekly SEO opportunity scan, weekly ad-fatigue check | Calendar cron (e.g. every Monday 9am) |
| Monitor-until-threshold | Churn-risk watch, launch-day tracking | Dynamic pacing that reacts to state, not a fixed clock |
| High-judgment / manual | Anything requiring a strategic call each run | "Run this every Monday" as a standing instruction is a legitimate loop, the value is the repeatable body, not full automation |

---

## Anti-Patterns

- Looping without a stop condition, leads to runaway spend or an infinite alert stream
- Using the same cadence for every loop, most end up checking too often and get ignored
- No self-check before acting, the loop reacts to noise, seasonality, or a tracking bug instead of a real signal
- No human checkpoint on anything that spends or publishes
- Standing up many loops at once instead of proving one loop's value first, then adding the next

---

## Baseline Contamination

Any loop that compares the current run against a trailing window has a failure mode that gets worse
the longer it runs, and it is invisible from inside a single run.

**The mechanism.** A trailing baseline is built from recent history. If the anomaly the loop just
flagged goes into that history unmarked, it becomes part of what counts as normal. Two consequences,
both bad:

1. **The next run misreads a return to normal as a new problem.** A spike enters the baseline, the
   baseline rises, and the following day's ordinary number now sits below it and gets flagged.
2. **Sustained problems become invisible.** A metric that degrades gradually is absorbed one run at a
   time. Each individual step is inside the band, the band moves with it, and after a few weeks the
   loop is comparing a bad number against an equally bad baseline and reporting nothing. The loop
   goes blind precisely to the slow decline it would have been most valuable for catching.

**What to do:**

- **Exclude flagged periods from the baseline.** When a run flags a period as anomalous, mark it in
  the ledger and leave it out of the trailing window for subsequent runs. Keep the raw value, but
  compute the baseline from unflagged periods only.
- **Where a shift turns out to be a real, permanent step change** (a price change, a new channel, a
  product launch), say so explicitly and reset the baseline from that date rather than letting the
  window absorb it gradually. A deliberate reset with a stated reason is different from silent drift.
- **Anchor against something the loop cannot move.** Alongside the trailing comparison, keep one
  fixed reference the loop never rewrites: the same period last year, a stated target, or a
  pre-launch baseline. If the trailing comparison is quiet but the fixed anchor has moved a long way,
  the baseline has drifted and the loop is the thing that is broken.
- **Report the baseline, not just the verdict.** Every flag states the baseline value it was measured
  against and how many periods it was computed from. A number without its baseline cannot be audited,
  and a drifting baseline is only ever caught by someone looking at it.

---

## Alert Fatigue Is a Failure, Not a Side Effect

A loop that flags too much gets ignored, and an ignored loop is worse than no loop: it costs money
per run and provides false assurance that something is being watched.

- **Set a per-run flag budget** when the loop is designed, and rank within it. Three to five items is
  the practical ceiling for something read daily. If a run produces more, report the top ones and
  state the total count rather than emitting everything.
- **Suppress what has already been dismissed.** A finding a human has seen and consciously accepted
  stops being reported until it materially changes. That decision belongs in the ledger, with the
  date and the reason, so the next run can read it.
- **Distinguish new from continuing.** "Still true since Tuesday" and "started today" need different
  treatment, and collapsing them is what makes a daily loop feel like the same email every morning.
- **Track the ignore rate.** If nothing from the last several runs prompted any action, that is a
  finding about the loop. Either the thresholds are too loose or the thing being watched does not
  need watching at this cadence. Say so and propose a change.
- **Never fix fatigue by quietly widening thresholds.** Loosening a threshold until the loop stops
  complaining converts a noisy loop into a decorative one, and the second failure is harder to
  notice than the first. If a threshold changes, record what it was, what it became, and why.

---

## The Loop Has to Be Able to Fail

A loop whose gate cannot return a negative result is a scheduled report, not a check.

- State the condition under which a run reports "nothing to act on", and confirm that condition is
  reachable with real data.
- State the condition that would end the loop entirely. A loop with no stop condition accumulates
  cost indefinitely.
- If several consecutive runs cannot fail their own gate, the gate is wrong. Report that rather than
  continuing to pass.

# Marketing Loop Cadence Guide

Reference for scheduling recurring marketing workflows: the signal-speed-to-cadence rule, the nine-part loop anatomy, and common failure modes.

---

## The Cadence Rule

Match how often a loop *checks* to how fast the underlying signal actually changes — not to how often a stakeholder would like an update.

| Signal | Realistic cadence | Why |
|--------|---------------------|-----|
| Search rankings, backlinks, domain authority | Weekly | Move slowly; daily checks are just noise |
| Ad creative fatigue, CPA drift | Every 2-3 days | Platform feedback loops (Meta, Google) run on a multi-day cycle, not hours |
| Activation / onboarding funnel | Weekly | Needs enough new signups to be statistically meaningful |
| Churn risk signals | Daily or on-trigger | The intervention window before cancellation is short |
| Content or landing page decay | Monthly | Traffic erosion from staleness is gradual |
| Competitor pricing/positioning changes | Weekly | Infrequent but consequential when they happen |
| Social listening / brand mentions | Daily | Engagement windows on social close fast |

Over-frequent loops are the single most common failure mode: they generate busywork nobody acts on, and the team learns to ignore the output — which defeats the loop's purpose entirely.

---

## Check Cadence vs. Acts When

These are two different things and conflating them is the second most common failure mode.

- **Check cadence** — how often the loop *looks* at the signal
- **Acts when** — the separate condition that must be true for the loop to actually *do* something

Example: a churn-risk loop might check daily, but only act when an account crosses a risk threshold it hasn't already been contacted about inside its cooldown window. A healthy loop's most common outcome on any given run is "checked, nothing to do" — a loop that acts every single time it checks is almost certainly reacting to noise.

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
| State / idempotency | What the loop remembers between runs — last-run marker, dedupe key, cooldown window — without this, loops double-act or re-nag the same person |
| Stop / bail-out | When the loop halts, skips, or escalates to a human, and what it does on error. Even a monitoring loop that never "completes" needs this — its stop is "manual disable + error-halt," never "n/a" |
| Output | Where results go — a file, a staged draft, a notification, a report |

---

## When Not to Automate on a Cadence

- **The real work is strategic or creative.** Loops maintain and optimize an existing motion; they don't set positioning, invent a campaign, or make a brand call.
- **The action publishes or spends without review.** Auto-drafting content is fine. Auto-publishing or auto-shifting budget needs a human checkpoint unless the user has explicitly authorized autonomous action with defined caps.
- **The signal is too sparse to be meaningful.** A weekly conversion-rate check against 40 weekly visitors is measuring noise, not a trend.
- **Nobody acts on the output.** A loop that emails a report nobody reads is worse than no loop — it's a maintenance cost with no return. Delete it.

---

## Scheduling Mechanism by Loop Type

| Loop type | Example | Scheduling approach |
|-----------|---------|------------------------|
| Fixed-cadence review | Weekly SEO opportunity scan, weekly ad-fatigue check | Calendar cron (e.g. every Monday 9am) |
| Monitor-until-threshold | Churn-risk watch, launch-day tracking | Dynamic pacing that reacts to state, not a fixed clock |
| High-judgment / manual | Anything requiring a strategic call each run | "Run this every Monday" as a standing instruction is a legitimate loop — the value is the repeatable body, not full automation |

---

## Anti-Patterns

- Looping without a stop condition — leads to runaway spend or an infinite alert stream
- Using the same cadence for every loop — most end up checking too often and get ignored
- No self-check before acting — the loop reacts to noise, seasonality, or a tracking bug instead of a real signal
- No human checkpoint on anything that spends or publishes
- Standing up many loops at once instead of proving one loop's value first, then adding the next

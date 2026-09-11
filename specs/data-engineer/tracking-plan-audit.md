# Spec: tracking-plan-audit

**Role:** Data Engineer (`skills/data-engineer/tracking-plan-audit`)
**Status:** ready to build. Every input can be got from an export today.
**Build order:** first of the three Data Engineer skills. It is the one that makes the other two
readable, because a duplicate event name is usually why a profile looks like two people.

## The job the user actually has

"A number moved on a dashboard and I cannot tell whether the behaviour changed or the tracking
broke."

One person owns instrumentation across a web app, a mobile SDK and whatever the marketing team
added to the tag manager. The tracking plan was written once, agreed by three people, and never
re-read. Since then:

- Two events fire for the same action, because a second team shipped `purchase_completed` next to
  the existing `checkout_complete`, and every funnel now under-counts by whichever one it forgot.
- A property stopped arriving after a release. Nobody noticed, because an absent property and a
  property that is genuinely empty look identical in a chart.
- A field's type flipped from number to string, so a sum silently became a concatenation or a
  dropped row.
- An event in the plan has not fired in four months, and the person who would know left.

They find all of this the way it was found last time: a report looked wrong, and someone spent a
day in the raw event stream. The job is to find it on purpose, before the report.

This is not a plan-writing skill. `instrument`-style generation and greenfield plan design are a
different job. This skill reads the plan that exists against the events that actually arrive.

## Inputs, and what happens when they are missing

`references/house-rules.md` rule 1 binds: three questions, hard cap, and derive before asking.
`references/missing-input-protocol.md` decides every gap below, and each one names its response
rather than defaulting.

| Input | Required | Missing response |
|---|---|---|
| The tracking plan: a CSV, a markdown table, or a Segment Protocols / Avo export, as a path or URL | No | **Degrade.** Run the plan-free half only: duplicate and near-duplicate names, casing and separator inconsistency, properties with mixed types, events with no volume in the window. Say in the first two lines that plan conformance did not run and what that leaves unanswered |
| The observed events with volume over a window: an analytics export, or the platform read below | Yes | **Block** if the plan is also absent. There is nothing to compare and every finding would be invented. Ask for this one first, because it is the one they can produce in a minute |
| The window, and the release date or version to diff drift against | No | **Assume** the last 30 complete days, stated inline at the point of use, not in a footnote. Without a release boundary, report drift without attributing it to a deploy |
| The naming convention in force | No | **Derive** it from the majority of the plan's own event names and say which convention was derived and from how many names. Never audit against a convention the skill picked |
| Downstream consumers (dashboards, journeys, destinations, warehouse models) that read each event | No | **Withhold** the blast-radius column. Print `not supplied, needs the list of dashboards and journeys reading each event, which decides whether a drift is cosmetic or breaking` |

Two protocol rules matter more here than anywhere else in the pack:

- **Absent is not zero.** A property with a measured 0% fill rate and a property the export never
  carried are different findings and get different rows. Collapsing them is how a working property
  gets reported as broken, and a broken one as fine.
- **State n beside every rate, and name the floor.** An event under 30 occurrences in the window is
  still shown, marked, and excluded from any "dead event" conclusion. A 100% type-mismatch rate on
  n=3 is not a type problem.

## The output artifact

One drift report. Offered as a file at `.agents/tracking-plan-audit.md`, per house rule 6, not
written unprompted.

1. **The answer, first two lines.** How many drifts, and how many of those break a named
   downstream consumer. Not "several inconsistencies were found."
2. **Duplicate and near-duplicate events**, grouped, with each member's volume and first-seen
   date, and one recommended survivor per group with the reason it survives.
3. **Property drift table.** Event, property, expected type, observed types with counts, fill rate
   with n, and the date the fill rate changed if the export carries dates.
4. **Plan conformance, both directions.** In the plan and never fires. Fires and is not in the
   plan. The second list is usually longer and is where the real duplicates hide.
5. **Naming violations** against the derived convention, with the convention stated.
6. **Ranked fix list.** Each fix names the consumer it unblocks, the owner (SDK call site, plan
   document, or warehouse model), and whether it is safe to do without a backfill. Top three,
   then the rest under a heading, per house rule 2.
7. **What was not checked, and why.** One short block. The reader needs to know the weight the
   report carries.

## What it would need from the Intempt platform

Nothing. It runs on an export today, like every other skill in this pack.

If the user is on Intempt, two registry reads replace the observed-events export:

- `list_events` (GET `/events/all`) returns the tracked event definitions.
- `list_event_attributes` returns the attributes for an event collection, which is the property
  side of the schema.

Neither returns per-event volume over a window, so the volume and fill-rate columns still come
from the user's own export or from an analytics report. Say which source each column came from at
the point the column appears, not in a sources list at the end.

## Chain with

`kpi-dashboard` and `conversion-funnel` both read events this skill audits. A dashboard built on a
drifted event is confidently wrong, so this runs before either.

**Next:** run `crm-sync-dedup` if the drift reaches an outbound list, or `kpi-dashboard` to rebuild
the report the drift broke.

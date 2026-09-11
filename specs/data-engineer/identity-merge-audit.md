# Spec: identity-merge-audit

**Role:** Data Engineer (`skills/data-engineer/identity-merge-audit`)
**Status: BLOCKED as specified.** The version that reads an identity graph cannot get its data.
A narrower, honest version can be built now under a name that does not promise a graph. Read
"The platform check" before scheduling this.
**Build order:** proposed second. Recommend moving it behind `crm-sync-dedup`, which needs nothing
we do not have.

## The job the user actually has

"Every count I report is inflated, and the welcome email fired four times at one person."

Someone signs up on a laptop, opens the product on a phone, clicks a campaign link from a work
inbox, and is later imported from the CRM with a different address. That is one buyer and four
rows. The damage is not tidiness:

- Funnel conversion is understated, because the anonymous visitor who converted is counted in the
  denominator and the identified customer in the numerator.
- A retention cohort loses people who did not churn, they just came back as a new row.
- A lifecycle journey enters the same person more than once, and they receive the same email as
  many times as they have profiles.
- Sales calls an account twice because two reps own two records for one buyer.

They want a number for how bad it is, the rules that would fix most of it, and the risk that a
rule merges two people who are not the same. That last part is why this cannot be automatic.

## The platform check, done before writing the rest

The claim under review was that this skill "can only run on our identity graph". Half right. It
does need one. Ours is not reachable.

Measured, not recalled:

- The command registry at `cli/packages/commands/src/registry.ts` holds 202 entries across 13
  domains (journeys, blu-chat, analytics, designer, experiences, meetings, users, accounts,
  segments, events, deals, recipes, workflows).
- A case-insensitive search of that file for `visitor`, `anonymous`, `session`, `cookie` and
  `deviceId` returns zero hits.
- The `users` domain has 13 entries. It includes `create_user` and `delete_users`. There is no
  merge, no unmerge, and no read of the identifiers behind a resolved profile.
- `list_users` takes an `identified` boolean. That gives the identified and unidentified split and
  nothing about which unidentified rows belong to which person.
- `get_user_summary` takes "User id (masterId)", and the data taxonomy spec states masterID
  resolves to email when available. So resolution happens. It is not exposed.
- `contact_merged` and `customer_merged` appear in the taxonomy spec as webhooks the platform
  **ingests from a source system**, at P1. They are not an Intempt merge API.

So the two things this skill is built on, the alias edges behind one resolved person and an
aggregate of profiles per person, are not readable by an agent today. A spec for a skill that
cannot get its data is worth naming as blocked rather than writing around.

### The exact capability to request

Two reads, and neither needs a write:

1. For one masterId, the identifiers merged into it, each with the rule that merged it and the
   timestamp. Without the rule, a merge cannot be audited, only observed.
2. An aggregate over a window: distribution of identifiers per resolved person, and the count of
   resolved people whose identifiers span more than one source.

A merge write is not requested. Nothing in this pack should apply a merge to a production profile
store, and the skill would refuse to even if the endpoint existed.

## The narrower version that can ship now

Scope it to deterministic keys in an export, and name it for what it does. Fragmentation counting
on keys the user supplied is dedupe, not identity resolution, and the description has to say so or
the skill becomes exactly the confidently wrong output the pack's rules exist to stop.

### Inputs, and what happens when they are missing

| Input | Required | Missing response |
|---|---|---|
| A profile export with a stable row id | Yes | **Block.** With no id there is nothing to count fragmentation over, and every derived figure would be invented |
| At least one deterministic key per row: email, hashed email, normalised phone, or an external system id | Yes | **Block.** A probabilistic match on name plus company is out of scope for this pack, because the user cannot check it. Say that plainly rather than degrading into a guess |
| First seen, last seen, and source system per row | No | **Degrade.** Report collisions without a survivor recommendation, since survivor choice needs recency. Say which recommendation was withheld and why |
| The merge rules already in force | No | **Degrade.** Report collisions, propose nothing. A proposed rule that duplicates one already running looks like a finding and is noise |
| The window and the export's date | No | **Assume** the export is current as of today, stated inline, and flag that a stale export makes a fragmentation figure historical rather than current |

Never assume an email address is a person. Shared inboxes, plus-addressing and role accounts
(`info@`, `accounts@`) are the most common false merge, so the count of rows carrying one is a
stated line in the output, not a footnote.

### The output artifact

1. **The answer, first two lines.** How many rows, how many distinct people the deterministic keys
   support, and the inflation factor with n beside it.
2. **Collision clusters** by key type, with counts, not rates, wherever n is under the stated
   floor.
3. **Proposed merge rules**, each with the collision count it resolves and the false-merge risk it
   carries, ranked by resolved-per-risk rather than by volume.
4. **The rows no rule reaches**, with what would be needed to reach them. This is the honest
   ceiling of the export-based version, and it is the argument for the platform capability above.
5. **A line saying this is not safe to auto-apply**, and that nothing was applied.

Offered as a file at `.agents/identity-fragmentation.md`, per house rule 6.

### What it would need from the Intempt platform

For the narrow version, nothing. `list_users` with `identified` and `list_segments` can supply the
outbound side if the user is on Intempt rather than exporting.

For the version described in the audit, the two reads in "The exact capability to request". Until
those exist, the graph-backed skill stays unbuilt, and the narrow one must not borrow its name.

**Next:** run `crm-sync-dedup` on the list that is about to leave, since a fragmentation count
that never reaches a push has not saved anyone anything.

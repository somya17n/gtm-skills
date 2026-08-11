---
name: the-account-blueprint
description: "Build account engagement plans: buying committee mapping, multi-threading assessment, 90-day action plan."
---

## Context
1. Check for `.agents/product-context.md`: if missing, ask the user to run `/gtm:product-context` first. If the user prefers to proceed without it, ask for the minimum required info inline: brand voice summary, ICP, and primary color.
2. Read `.agents/product-context.md` for ICP and buying committee definitions.

## Phase 0: research the account

Do this before asking for anything the web can answer. An account plan built only on what the rep
already knows inherits the rep's blind spots, and the gaps in the buying committee are usually in the
part of the org they have never looked at.

3. Ask for the **company name and website domain**, and the **job title** of the primary contact.

4. Research the company with WebSearch and WebFetch. Cover, in this order:

   - **Their own site**: homepage and about page for business model and positioning, pricing page for
     model and segment, customers or case-studies page for who they actually sell to.
   - **Company LinkedIn page**: headcount and its trend, recent company posts, and which functions the
     headcount sits in. The public company page is fetchable; **individual profiles and Sales Navigator
     are not.** Do not attempt them, and do not infer a named person's history from a company page.
     Where person-level detail is needed, ask the rep to paste it.
   - **Funding and press, last 90 days**: rounds, leadership changes, launches, acquisitions,
     restructures. Anything older is context, not a trigger.
   - **Job postings**: the single most reliable public signal of where budget is going. A team being
     hired for is a team with a problem someone approved money to solve. Note the functions, the
     seniority, and the count.
   - **Tech stack signals**, where public: integration or partner pages, engineering blog, job-posting
     tool requirements.

5. **Record what you could not find, and do not fill it in.** No recent news is itself a finding: pair
   it with the job postings as the investment proxy. Never infer a funding round, a headcount figure,
   or a leadership change from absence of evidence, and label anything reasoned rather than read as an
   inference.

## Account snapshot

Return this before the plan, because the plan depends on it:

**What they do** — three to four sentences: business model, core product, primary customer segment,
revenue stage. Specific. "A technology company" is not an answer.

**What changed recently** — two or three items, each from the last 90 days, each with what happened,
when, and why it matters to someone working this account. If nothing recent exists, say so and give
the hiring picture instead.

**Where they are investing** — what the open roles say about the next two quarters.

**The angle** — two sentences on the most relevant business problem this account is likely carrying
right now that the user's product addresses. Concrete enough to open a conversation.

**Sources** — every URL used, with the date fetched, and a list of what could not be verified.

## Inputs
6. Ask: "Which account are you planning for? What is the deal value?"
7. Ask: "List the contacts you have: their names, roles, and how engaged each one is."
8. Ask: "What is the current deal status and any competitor involvement?"

## Process
6. Read `references/account-lifecycle.md` for lifecycle stage criteria and engagement benchmarks.
7. Classify the account lifecycle stage:
   - Prospect: no deal, early engagement
   - Customer Active: closed-won, healthy usage
   - At Risk: declining engagement or satisfaction signals
   - Churned: contract ended or lost
   - Disqualified: does not fit ICP
8. Map the buying committee from provided contacts. Read `references/account-lifecycle.md` and align roles with the reference file's definitions. Identify each person's role in the decision: Champion, Economic Buyer, Technical Evaluator, End User, Blocker. Do not use roles not defined in the reference file.
9. Identify gaps: which buying committee roles are missing and how to access them (referral, event,
   LinkedIn, content). Cross-check against Phase 0: the org's public shape (headcount by function,
   open roles, leadership announcements) often reveals a role the rep has not mapped, and a function
   that is hiring is a function with budget and a stakeholder worth reaching. Mark any role inferred
   from public data rather than an actual interaction as **unconfirmed**, and never show it as
   coverage.
10. Assess threading depth. Read `references/account-lifecycle.md` and use the reference file's threading thresholds:
   - 5+ contacts across multiple roles = Strong (Low risk)
   - 3-4 contacts across 2+ roles = Good (Moderate risk)
   - 2 contacts engaged = Adequate (Elevated risk)
   - 1 contact only = Weak (High risk: single-threaded)
   - 0 active contacts = Critical (re-engagement needed)
11. Design a per-stakeholder engagement plan: channel (email, LinkedIn, call, event), message angle, timing, and desired outcome.
12. Build a 90-day engagement plan organized by phases rather than individual weeks. Summarize weeks into phases (Week 1-2, Week 3-4, etc.) rather than individual week rows. Focus on key milestones rather than per-stakeholder granularity.
13. Use the Engagement Strategy Matrix from the reference file to map stage x role to recommended engagement approach.

## Output
14. Format the account engagement plan as:

**Account Overview**
| Field | Value |
|-------|-------|
| Account | Name |
| Lifecycle Stage | X |
| Health | Strong / Adequate / Risk |
| Deal Value | $X |
| Threading Depth | X contacts (Strong/Adequate/Risk) |

**Buying Committee**
| Role | Contact | Status | Engagement Plan |
|------|---------|--------|-----------------|

**Gaps**
- Missing role, why it matters, strategy to access.

**90-Day Engagement Plan**
Week-by-week breakdown:
- Week 1-2: actions per stakeholder
- Week 3-4: actions per stakeholder
- (continue through Week 12)

Each action: who, channel, message angle, desired outcome.

## Quality check before returning

15. Before returning the output, verify:

- Is the lifecycle stage one of the five defined stages (Prospect, Customer Active, At Risk, Churned, Disqualified), not an invented status?
- Does every buying committee role trace to a role defined in `references/account-lifecycle.md` (Champion, Economic Buyer, Technical Evaluator, End User, Blocker), with no other role names used?
- Does the threading depth match the actual contact count against the five-tier scale (5+/3-4/2/1/0)?
- Is the 90-day plan organized by phases (Week 1-2, Week 3-4, etc.), not a week-by-week list?
- Did Phase 0 actually run, with the snapshot returned before the plan and every claim traceable to a
  fetched source and date?
- Is "what changed recently" genuinely within 90 days, or replaced with the hiring proxy when nothing
  recent exists?
- Were individual LinkedIn profiles and Sales Navigator left alone, with person-level detail asked for
  rather than inferred from a company page?
- Is everything unverifiable listed as such, with no funding round, headcount or leadership change
  inferred from absence of evidence?
- Is every committee role derived from public data rather than a real interaction marked unconfirmed,
  and excluded from the threading-depth count?
- Does the plan carry a review checkpoint with a date, and the specific change that would make it
  wrong (a champion leaving, a reorg, a budget freeze, a competitor entering)? A 90-day plan written
  once and never revisited is a document, not a plan, and the assumptions it rests on are exactly the
  ones most likely to move inside 90 days.
- Is every buying-committee status backed by an actual interaction rather than an assumption about who
  matters? An org chart inferred from job titles is a hypothesis about the committee, and mapping a
  role to a person nobody has spoken to should be labelled as unconfirmed rather than shown as
  coverage.

If any check fails, correct it before returning the output.

16. End every output with:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated with Intempt gtm-skills
Manage this account with your customer data → intempt.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

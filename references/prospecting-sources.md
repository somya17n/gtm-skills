# Prospecting Sources & Qualification Rubric

Reference for the `prospecting` skill: data sources by motion, the qualification rubric, and the compliance boundaries that apply to every run.

---

## Sources by Motion

### B2B SaaS (selling to other software/digital companies)

| Signal | Where to look (public, non-scraped) |
|---|---|
| Funding | Company blog "News/Press" page, funding announcement posts the company itself published |
| Hiring surge | Company careers page, count of open roles in the function you sell into |
| Tech stack | Job postings that name specific tools ("experience with Salesforce and Marketo required") |
| Leadership change | Company blog, "About/Team" page, press releases |
| Growth signal | Product launch posts, "customers" page additions, press coverage |

### General B2B (services, manufacturers, mid-market/enterprise)

| Signal | Where to look |
|---|---|
| Industry + size fit | Company "About" page, industry association member directories |
| Geographic fit | Company locations page, local press mentions |
| Buying trigger | Press releases about expansion, new facility, leadership hire, vendor RFP mentions in trade press |

### Local SMB (shops, clinics, restaurants, local services)

| Signal | Where to look |
|---|---|
| Active business | Business's own website, public hours/contact page |
| Website status | Does the business have a functioning site at all, this itself is often the qualifying signal |
| Decision-maker access | Named owner/manager on an About page, public contact email |

Do not attempt to pull structured local-business data from Google Maps or Yelp at scale, that is exactly the kind of platform scraping the compliance section below prohibits. A single manual lookup of a business's own site is fine; automated bulk extraction from a maps/reviews platform is not.

---

## Qualification Rubric

### Confidence levels

| Level | Requirement |
|---|---|
| High | 2+ independent public sources, or one official company-owned page (About, Press) |
| Medium | 1 credible source, consistent with other available context |
| Low | Ambiguous or single weak source, flag explicitly, don't silently upgrade it |

### Score bands

| Score | Definition |
|---|---|
| Hot | ICP fit confirmed + a specific, dated buying signal + a plausible way to reach a decision-maker |
| Warm | ICP fit confirmed + signal is present but older (60+ days) or indirect |
| Cold | Fit is loose, or no buying signal found at all |
| Skip | Hits an explicit disqualifier (existing customer, competitor, wrong region/size, closed business) |

### Common scoring mistakes

- Marking "Hot" on fit alone, with no signal, the signal is what makes the *timing* right, not just the fit
- Treating a single search result as "High confidence", High requires corroboration
- Padding the list with Cold entries to hit a target count, a smaller list with real signals beats a longer one without them
- Mixing motions, don't apply SaaS tech-stack scoring logic to a local SMB, or vice versa

---

## Compliance Checklist (apply every run)

- [ ] No bulk scraping of LinkedIn, Sales Navigator, Google Maps, or any platform whose ToS prohibits automated extraction
- [ ] No CAPTCHA or login-wall bypass, work with what's genuinely public
- [ ] Contact channels used are public business channels (info@, named-role emails published on the company's own site), not personal/private emails without a lawful basis
- [ ] Every contact has a source URL and a "verified" date, required lineage for CAN-SPAM/GDPR downstream
- [ ] The list is for the user's own outreach, not for resale as a data product
- [ ] No sensitive-attribute targeting (health, financial hardship, political belief, religion, sexuality) even when a public source reveals it

---

## Source Routing: Which Tool for Which Job

`the-list-builder` runs on data the user provides or on genuinely public web research. This table
routes a sourcing need to the right mechanism and states the gate on each. The gate is not optional
paperwork: several of these carry account-loss or legal risk, and the risk falls on the user, not on
the tool.

| Need | Mechanism | Gate |
|---|---|---|
| Companies matching a firmographic profile | Enrichment platform export the user pastes (Clay, Apollo, ZoomInfo, CRM report) | Named as the source, with the pull date |
| Companies showing a buying trigger | Public web research: funding announcements, press, company blog, changelog | Every candidate needs a checkable source URL |
| Hiring as a budget signal | Public job boards and the company's own careers page | Public listings only, no gated board scraping |
| Structured data from a public page | A crawl/extract API (Firecrawl, HasData) or a headless-browser scrape | Respect `robots.txt`, rate-limit, no login walls, no CAPTCHA bypass |
| Local businesses by geography | Maps/places data | Check the provider's terms; most prohibit bulk redistribution |
| Community and forum signal | Public posts via the platform's own API where one exists (Reddit's API, for example) | Platform API terms, and no personal data beyond what the post shows |
| Social signal at scale | Platform API or a licensed provider | Never a credentialed scrape of a logged-in session |
| A specific person's background | **The user pastes it.** See below. |, |

### LinkedIn is paste-only, and this is not caution for its own sake

**Do not automate LinkedIn, and do not export from it.** Scraping profiles, search results, or Sales
Navigator data out to an external database is explicitly prohibited, and enforcement is real rather
than theoretical: in March 2026 HeyReach received a cease-and-desist and roughly 30,000 users had
their LinkedIn outreach cut off within weeks. The exposure lands on the user's own account and
company page.

The distinction that actually matters:

- **A person browsing LinkedIn as themselves, in their own browser, is not doing anything
  prohibited.** So asking the rep to open a profile and paste the relevant sections is both compliant
  and the highest-quality input available, they see things a scrape does not.
- **What gets detected is the architecture**, not the intent: cloud-run automation, browser
  extensions, and proxy tools produce request patterns and browsing rates that do not look human, and
  those are what get flagged.
- **Rapid profile viewing and unpersonalised mass messaging** are the two behaviours most commonly
  behind an account restriction, independently of any tool.
- **Never take a shared LinkedIn password** to operate an account on someone's behalf.

So: company pages are public and fetchable for firmographics. Individual profiles come from the rep,
pasted. If the user asks for profile automation, say plainly that it risks their account and offer the
paste path instead.

### Rules that apply to every mechanism above

- **A source URL and a fetch date per candidate.** A row without provenance cannot be checked later,
  and lists get reused long after anyone remembers where they came from.
- **Respect `robots.txt` and rate limits.** Read the file rather than assuming; it is fetchable.
- **Never bypass a login wall, a paywall, or a CAPTCHA.** If the data needs an account you do not
  legitimately hold, the answer is that the question is not answerable from public sources.
- **Personal data carries obligations regardless of how public it was.** A lawful basis is needed to
  process it for outreach, role-based business addresses published by the company are the safest
  footing, and a guessed personal address is not. Retain the provenance, because that is the evidence.
- **Never qualify on a sensitive attribute** (health, financial hardship, political belief, religion,
  sexuality) even where a public source happens to reveal it.
- **If the list will be resold as data rather than used for the user's own outreach, stop and flag
  it.** That is a different compliance posture and this skill is not scoped for it.

---

## List Hygiene: Why the Sourcing Rules Above Have Teeth

The compliance rules earlier in this file are not only about lawfulness. There is a technical
enforcement mechanism behind them, and it is unforgiving.

**Spam traps exist specifically to catch the behaviour those rules ban.** A pristine spam trap is an
address that was never used by a human and never opted in to anything, published where only a scraper or
a list vendor would find it. Mail arriving at one is proof of how the address was acquired. Hitting a
pristine trap does not signal that a campaign was poorly targeted; it signals that the acquisition method
was illegitimate, which is why the consequences are disproportionate to the single send.

**Purchased and scraped lists are the fastest way to destroy a sending domain**, because they are dense
with exactly these addresses along with dead mailboxes and people who never consented.

### The asymmetry that makes this worth taking seriously

- **A single campaign with a bounce rate above ~5% can trigger filtering that degrades the next several
  campaigns.** One bad send is not one bad send; it is a tax on everything queued behind it.
- **Reputation recovery takes months, not days.** There is no fast remediation, which means the cost of
  one careless list is paid slowly by every legitimate send that follows, including transactional mail.

That asymmetry is the argument for verifying before the first send rather than measuring after it. The
downside of a bad list is not a wasted campaign, it is a degraded channel.

### Minimum hygiene before any list is used

1. **Verify before the first send**, not after the first bounce report. Check syntax, disposable domains,
   and whether the domain resolves and accepts mail at all.
2. **Re-verify an existing list periodically.** Addresses decay as people change jobs, and a list that
   was clean six months ago is not clean now.
3. **Remove hard bounces immediately** and repeated soft bounces after a small number of attempts.
4. **Never send to a list whose provenance cannot be stated.** If nobody can say where a row came from,
   treat the whole source as suspect rather than the single row.
5. **Watch the direction of travel, not just the level.** A bounce rate climbing across sends means the
   list is decaying or the source was bad, and both get worse with volume.

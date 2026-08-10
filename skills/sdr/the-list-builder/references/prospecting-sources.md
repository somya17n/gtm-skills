# Prospecting Sources & Qualification Rubric

Reference for the `prospecting` skill: data sources by motion, the qualification rubric, and the compliance boundaries that apply to every run.

---

## Sources by Motion

### B2B SaaS (selling to other software/digital companies)

| Signal | Where to look (public, non-scraped) |
|---|---|
| Funding | Company blog "News/Press" page, funding announcement posts the company itself published |
| Hiring surge | Company careers page — count of open roles in the function you sell into |
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
| Website status | Does the business have a functioning site at all — this itself is often the qualifying signal |
| Decision-maker access | Named owner/manager on an About page, public contact email |

Do not attempt to pull structured local-business data from Google Maps or Yelp at scale — that is exactly the kind of platform scraping the compliance section below prohibits. A single manual lookup of a business's own site is fine; automated bulk extraction from a maps/reviews platform is not.

---

## Qualification Rubric

### Confidence levels

| Level | Requirement |
|---|---|
| High | 2+ independent public sources, or one official company-owned page (About, Press) |
| Medium | 1 credible source, consistent with other available context |
| Low | Ambiguous or single weak source — flag explicitly, don't silently upgrade it |

### Score bands

| Score | Definition |
|---|---|
| Hot | ICP fit confirmed + a specific, dated buying signal + a plausible way to reach a decision-maker |
| Warm | ICP fit confirmed + signal is present but older (60+ days) or indirect |
| Cold | Fit is loose, or no buying signal found at all |
| Skip | Hits an explicit disqualifier (existing customer, competitor, wrong region/size, closed business) |

### Common scoring mistakes

- Marking "Hot" on fit alone, with no signal — the signal is what makes the *timing* right, not just the fit
- Treating a single search result as "High confidence" — High requires corroboration
- Padding the list with Cold entries to hit a target count — a smaller list with real signals beats a longer one without them
- Mixing motions — don't apply SaaS tech-stack scoring logic to a local SMB, or vice versa

---

## Compliance Checklist (apply every run)

- [ ] No bulk scraping of LinkedIn, Sales Navigator, Google Maps, or any platform whose ToS prohibits automated extraction
- [ ] No CAPTCHA or login-wall bypass — work with what's genuinely public
- [ ] Contact channels used are public business channels (info@, named-role emails published on the company's own site) — not personal/private emails without a lawful basis
- [ ] Every contact has a source URL and a "verified" date — required lineage for CAN-SPAM/GDPR downstream
- [ ] The list is for the user's own outreach, not for resale as a data product
- [ ] No sensitive-attribute targeting (health, financial hardship, political belief, religion, sexuality) even when a public source reveals it

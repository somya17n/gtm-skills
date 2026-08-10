# Sales Outreach Cadences

Reference for designing multi-channel sales outreach sequences: cadence patterns by buyer type, channel mix, email personalization layers, subject line patterns, timing, objection handling, compliance, and performance metrics.

---

## Cadence Patterns by Buyer Type

### Inbound Lead (Fast Follow-Up)

Inbound leads have expressed interest — speed and relevance are critical.

| Touch | Timing | Channel | Purpose |
|-------|--------|---------|---------|
| 1 | 5 minutes | Email | Acknowledge the request, confirm next steps |
| 2 | 1 hour | Phone | Personal connection, qualify interest |
| 3 | 24 hours | Email | Value-add content related to their inquiry |
| 4 | Day 3 | LinkedIn | Connection request with personalized note |
| 5 | Day 5 | Email | Case study relevant to their industry/use case |
| 6 | Day 8 | Phone | Follow-up call, offer demo |
| 7 | Day 14 | Email | Final follow-up with direct ask |

**Key metrics:**
- 5-7 touches over 14 days
- Speed to first response is the #1 predictor of conversion
- Leads contacted within 5 minutes are 21x more likely to qualify

### Outbound Cold (Longer Spacing)

Cold prospects need education and trust-building before they engage.

| Touch | Timing | Channel | Purpose |
|-------|--------|---------|---------|
| 1 | Day 1 | Email | Cold intro: trigger event or pain-based hook |
| 2 | Day 3 | LinkedIn | Connection request with context |
| 3 | Day 5 | Email | Follow-up: value prop + social proof |
| 4 | Day 8 | Phone | Warm call referencing emails |
| 5 | Day 10 | Email | Case study or insight relevant to their role |
| 6 | Day 13 | LinkedIn | Engage with their content (comment/like) |
| 7 | Day 16 | Email | New angle: different pain point or use case |
| 8 | Day 19 | Video | Personalized Loom (60-90 seconds) |
| 9 | Day 22 | Email | Breakup: "Should I close your file?" |
| 10 | Day 25 | Phone | Final call attempt |
| 11 | Day 28 | Email | True final: leave the door open |

**Key metrics:**
- 8-12 touches over 21-28 days
- Average cold sequence generates responses on touch 3-5
- Multi-channel sequences outperform email-only by 2-3x

### Enterprise (Slower + Multi-Threaded)

Enterprise deals require patience, multiple stakeholders, and executive-level messaging.

| Touch | Timing | Channel | Purpose | Target |
|-------|--------|---------|---------|--------|
| 1 | Day 1 | Email | Executive-level insight or trigger event | Champion |
| 2 | Day 3 | LinkedIn | Thought leadership share + connection | Champion |
| 3 | Day 5 | Email | Industry report or benchmark data | Champion |
| 4 | Day 8 | Email | Introduction to a relevant customer reference | Champion |
| 5 | Day 10 | Phone | Discovery call request | Champion |
| 6 | Day 13 | Email | New thread: technical value proposition | Technical Evaluator |
| 7 | Day 16 | LinkedIn | Connection request with technical context | Technical Evaluator |
| 8 | Day 20 | Email | ROI analysis or business case template | Economic Buyer |
| 9 | Day 24 | Video | Personalized executive briefing (Loom) | Economic Buyer |
| 10 | Day 28 | Email | Mutual connection introduction or warm referral | Champion |
| 11 | Day 32 | Phone | Follow-up with new value angle | Champion |
| 12 | Day 36 | Email | Event invitation or exclusive content | All threads |
| 13 | Day 40 | LinkedIn | Comment on company news | Champion |
| 14 | Day 43 | Email | Summary of attempts + open door | Champion |
| 15 | Day 45 | Email | Long-term nurture enrollment | All threads |

**Key metrics:**
- 10-15 touches over 30-45 days
- Multi-threaded (3+ contacts at the account)
- Enterprise cycles average 90-180 days

### Re-Engagement (Quarterly Pulse)

For previously engaged prospects who went dark or existing contacts that need periodic nurturing.

| Touch | Timing | Channel | Purpose |
|-------|--------|---------|---------|
| 1 | Day 1 | Email | "Checking in" with new company news or product update |
| 2 | Day 4 | LinkedIn | Engage with their recent activity/posts |
| 3 | Day 7 | Email | New case study or ROI data |
| 4 | Day 11 | Video | Brief personalized update (30-60 seconds) |
| 5 | Day 14 | Email | Direct ask: "Has anything changed on your end?" |

**Key metrics:**
- 3-5 touches over 14 days
- Run quarterly for dormant pipeline
- Re-engagement sequences revive 5-15% of dormant leads

---

## Channel Mix

### Channel Strengths

| Channel | Strengths | Weaknesses | Best For |
|---------|-----------|------------|----------|
| **Email** | Scalable, trackable, rich content | Easy to ignore, crowded inbox | Primary outreach, content delivery, follow-ups |
| **LinkedIn** | Professional context, visible engagement | Limited message length, connection required for InMail | Relationship building, credibility, warm touches |
| **Phone** | Highest engagement per touch, real-time conversation | Low connect rates (8-12%), time-intensive | Discovery, qualification, high-value prospects |
| **Video (Loom)** | Personal, memorable, stands out | Production time, not always watched | Differentiation, complex value props, executive outreach |

### Channel Allocation by Cadence Type

| Cadence Type | Email | LinkedIn | Phone | Video |
|-------------|-------|----------|-------|-------|
| Inbound | 50% | 15% | 30% | 5% |
| Outbound Cold | 55% | 20% | 15% | 10% |
| Enterprise | 40% | 25% | 20% | 15% |
| Re-engagement | 60% | 20% | 5% | 15% |

---

## Email Personalization Layers

### L1 — Basic (Name/Company)

The minimum viable personalization. Every email should include at least L1.

```
Hi {{first_name}},

I noticed {{company}} is [generic observation].
```

**Signals used:** First name, company name, title
**Effort:** Automated, no manual research
**Performance:** Baseline open/reply rates

### L2 — Contextual (Industry/Role Pain)

Personalization based on segment-level attributes.

```
Hi {{first_name}},

As a {{title}} in {{industry}}, you're probably dealing with [industry-specific pain point].
Teams like yours typically see [common challenge].
```

**Signals used:** Industry, role/title, company size, technology stack
**Effort:** Template-based with segment variables
**Performance:** 20-40% lift over L1

### L3 — Trigger-Based (Event/Mutual Connection)

Personalization tied to a specific event or shared context.

```
Hi {{first_name}},

Congrats on {{trigger_event}} — that's a big milestone for {{company}}.
When teams hit this stage, they often run into [challenge that your product solves].
```

**Trigger events:** Funding round, new executive hire, product launch, expansion, award, job posting
**Signals used:** News mentions, LinkedIn activity, job postings, funding data
**Effort:** Semi-automated (trigger detected, template applied)
**Performance:** 40-80% lift over L1

### L4 — Deep Research (Custom Insight)

Fully custom personalization based on manual research.

```
Hi {{first_name}},

I read your recent [blog post / podcast / talk] on {{topic}} — your point about [specific insight] resonated.
At Intempt, we've been thinking about this too, and [connect to relevant solution].
```

**Signals used:** Published content, conference talks, social media posts, mutual connections, shared interests
**Effort:** 10-20 minutes of manual research per prospect
**Performance:** 80-150% lift over L1
**Best for:** Enterprise prospects, executive outreach, high-value deals

---

## Subject Line Patterns

### Question

Invites a response and creates curiosity.

| Example | Context |
|---------|---------|
| "Quick question about {{company}}'s growth plans?" | Outbound, first touch |
| "Is {{company}} still evaluating [solution category]?" | Re-engagement |
| "How is {{company}} handling [specific challenge]?" | Pain-based |

### Mutual Connection

Leverages shared network for credibility.

| Example | Context |
|---------|---------|
| "{{mutual_connection}} suggested I reach out" | Warm intro |
| "Fellow [community/alumni] member here" | Shared affiliation |
| "We both spoke at [event]" | Shared experience |

### Trigger Event

References a timely, relevant event.

| Example | Context |
|---------|---------|
| "Congrats on the Series B, {{first_name}}" | Funding trigger |
| "Saw {{company}} just launched [product]" | Product launch trigger |
| "Your new [role] posting caught my eye" | Hiring trigger |

### Stat/Insight

Leads with data that establishes expertise.

| Example | Context |
|---------|---------|
| "{{industry}} teams are wasting 23 hours/week on this" | Data-led hook |
| "3 trends reshaping [function] in 2025" | Thought leadership |
| "How {{similar_company}} cut churn by 40%" | Social proof + data |

### Direct Value Prop

Straightforward statement of value.

| Example | Context |
|---------|---------|
| "Cut {{company}}'s onboarding time by 50%" | Benefit-led |
| "A better way to [specific task] for {{title}}s" | Role-specific |
| "Idea for {{company}}'s [specific challenge]" | Problem-specific |

---

## Follow-Up Timing Rules

| Rule | Guideline |
|------|-----------|
| Between same-channel touches | 2-3 business days minimum |
| Between different channels | 1 business day minimum |
| No back-to-back same channel | Never send 2 emails or make 2 calls on consecutive days |
| After no response to 3 touches | Increase spacing to 4-5 days |
| After phone connect (no meeting) | Follow up via email within 2 hours |
| After meeting | Follow up via email within 24 hours |
| After positive reply | Respond within 4 hours during business hours |

### Day-of-Week Performance

| Day | Email Open Rate | Phone Connect Rate | LinkedIn Response |
|-----|----------------|-------------------|-------------------|
| Monday | Medium | Medium | Low |
| Tuesday | High | High | High |
| Wednesday | High | High | High |
| Thursday | High | Medium-High | Medium-High |
| Friday | Low | Low | Low |

**Best days for outbound:** Tuesday, Wednesday, Thursday
**Best email send times:** 8-10 AM and 4-6 PM in recipient's timezone
**Best call times:** 8-9 AM and 4:30-6 PM in recipient's timezone

---

## Objection Pre-Handling

Embed proof points in your sequence that proactively address the top objections before the prospect raises them.

### Top Objections and Pre-Handling Strategies

| Objection | Pre-Handle in Sequence |
|-----------|----------------------|
| **"We already have a solution"** | Include comparison data and switching cost analysis in touch 3-4. Show ROI of switching. |
| **"It's not a priority right now"** | Use trigger events to establish urgency. Quantify cost of inaction in touch 2-3. |
| **"It's too expensive"** | Include ROI calculator or payback period data in touch 4-5. Show total cost of ownership vs. alternatives. |
| **"I need to talk to my team"** | Offer a team demo early. Provide shareable assets (one-pagers, ROI sheets) in touch 3. |
| **"We tried something similar and it didn't work"** | Include a case study of a customer who switched from a similar solution in touch 5-6. |
| **"I don't have time"** | Keep emails under 100 words. Lead with the highest-impact insight. Offer async options (video, doc). |

---

## Compliance

### CAN-SPAM (United States)

| Requirement | Detail |
|-------------|--------|
| Identification | Clearly identify the message as an ad/solicitation |
| Physical address | Include valid physical postal address |
| Unsubscribe | Provide clear opt-out mechanism |
| Honor opt-outs | Process within 10 business days |
| No deception | Subject line must reflect content; no misleading headers |
| Responsibility | You are responsible even if a third party sends on your behalf |

### GDPR (European Union)

| Requirement | Detail |
|-------------|--------|
| Legal basis | Legitimate interest (B2B outreach) or explicit consent |
| Right to object | Must honor opt-out requests immediately |
| Data minimization | Only collect data necessary for the outreach purpose |
| Transparency | Explain why you are contacting them and how you obtained their data |
| Record keeping | Document your legitimate interest assessment |

### CASL (Canada)

Stricter than CAN-SPAM in the way that matters most: Canada requires **consent** for a commercial
electronic message rather than an opt-out. Consent can be express, or implied by an existing
business relationship or a conspicuously published business address relevant to the recipient's
role. Penalties are significant and apply per violation.

| Requirement | Detail |
|-------------|--------|
| Consent | Express, or implied through an existing relationship or a conspicuously published role-relevant business address |
| Identification | Sender clearly identified, with a mailing address and either a phone number, email, or web address |
| Unsubscribe | A working mechanism, honoured within 10 business days, valid for at least 60 days after sending |
| Record keeping | Retain the evidence of consent or of the implied-consent basis |

Practical effect on cold outbound: a role-based business address published on the company's own site
is generally the safest basis, and a personal or guessed address is not. Where a Canadian prospect
cannot be tied to a published business address or an existing relationship, treat them as not
contactable rather than assuming an opt-out model applies.

### The compliance footer on a 1:1 cold email

The most common failure in cold outbound is a genuinely personal, plain-text email that omits the
identification, address, and opt-out that commercial email requires. Teams leave them out to
preserve the one-to-one feel, and the whole sequence is non-compliant as a result.

The requirement and the register are not actually in conflict. A short plain-text close satisfies
both:

```
Somya
Intempt, <street address, city, country>

Not useful? Reply "stop" and I won't follow up.
```

Rules:

- **A reply-based opt-out is a valid mechanism** and reads far more naturally in a 1:1 email than an
  unsubscribe link. It only works if it is actually honoured and written to a suppression list,
  which has to be a real process rather than an intention.
- **The postal address is not optional** in US commercial email, and it is required for
  identification under CASL. A registered office or a mail-handling address is fine.
- **Honour opt-outs within 24 hours**, well inside every statutory window, and suppress across every
  sequence and every sending domain rather than per campaign. A prospect who opted out of one
  sequence and receives another from a sibling domain is the version of this that generates
  complaints.
- **Keep the footer below the sign-off** and out of the body, so it does not compete with the
  message or count against the word budget.
- **Never disguise a commercial email as personal correspondence.** A misleading subject line or a
  fake reply-thread prefix ("Re:" on a first contact) is deceptive-header territory, separately from
  being ineffective once noticed.

Jurisdictions differ, this list is not exhaustive, and none of it is legal advice. Any programme
sending at volume should have the footer and the suppression process reviewed once, properly.

### Best Practices for Compliance

- Always include an unsubscribe link or clear opt-out instructions
- Include your company name and physical address in every email
- Do not use misleading subject lines
- Honor opt-out requests within 24 hours (even if law allows longer)
- Maintain a suppression list that persists across all sequences
- Document your legitimate interest basis for B2B outreach
- Never purchase contact lists without verifying consent status

---

## Performance Metrics

### Benchmarks by Metric

**Important:** Published benchmarks are often inflated (companies share top-performer numbers, not medians). The numbers below reflect real population averages from large-scale studies. Use the "Average" column as your starting baseline, not the "Good" column.

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| **Open rate** | < 25% | 30-40% | 40-55% | > 55% |
| **Reply rate (total)** | < 1% | 3–3.5% | 5-8% | > 8% |
| **Positive reply rate** | < 0.5% | 1–1.5% | 2-4% | > 4% |
| **Meeting booked rate** | < 0.5% | 1–1.5% | 2-3% | > 3% |
| **Sequence completion rate** | < 40% | 50-65% | 65-80% | > 80% |
| **Bounce rate** | > 5% | 2-5% | 1-2% | < 1% |
| **Unsubscribe rate** | > 2% | 1-2% | 0.5-1% | < 0.5% |

### Directional Outreach Patterns (No Single Authoritative Benchmark)

Outreach and sales engagement vendors regularly publish reply-rate and performance research, but the exact percentages differ by vendor, sample, and year, and none of it is independently reproducible across sources. Treat the following as directional, not guaranteed:

| Metric | Direction | Caveat |
|--------|-----------|--------|
| Cold email reply rate | Typically low single digits across most published research | Varies significantly by list quality, ICP fit, and personalization; no single authoritative benchmark exists across sources |
| Cold email positive reply rate | A small fraction of total replies, well under half | Depends heavily on targeting and message quality |
| Meeting booked rate (per prospect) | Generally low single-digit percent or less | Varies by deal size, channel mix, and offer strength |
| Open rate (B2B cold) | Often reported in the 30-50% range but treated as unreliable by most practitioners | Distorted by mail privacy protection features on many clients; click and reply rates are more trustworthy signals |
| Multi-channel vs. email-only | Adding LinkedIn and phone to email generally lifts reply volume meaningfully | Magnitude not consistently reproducible across sources |
| Response timing | Faster follow-up on inbound leads correlates strongly with higher qualification rates | Exact multiplier varies by study; treat "respond fast" as the takeaway, not a specific number |
| Touch count before response | Most replies arrive after several touches, not the first one or two | Exact touch number varies by sequence design and channel mix |
| Deep personalization vs. basic personalization | Custom, research-based personalization tends to outperform name/company templating | Magnitude of the lift is not consistent across sources |
| Phone connect rate (cold) | Typically a small minority of dials reach a live human | Varies by list quality, industry, and time of day |
| LinkedIn InMail response rate | Generally reported as higher than cold email response rates | Exact multiplier not consistently reproducible; quality of the message still dominates |

### Metric Definitions

| Metric | Formula |
|--------|---------|
| Open rate | Unique opens / total delivered |
| Reply rate | Total replies / total delivered |
| Positive reply rate | Positive replies (interested/meeting) / total delivered |
| Meeting booked rate | Meetings scheduled / total prospects in sequence |
| Sequence completion rate | Prospects who received all touches / total prospects enrolled |
| Bounce rate | Bounced emails / total sent |

### Diagnostic Framework

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Low open rate (< 25%) | Subject lines, sender reputation, deliverability | Test subject lines, warm up domain, check SPF/DKIM |
| Good opens, low replies (< 3%) | Email content not compelling | Improve personalization (move up L2-L4), tighten value prop |
| Good replies, low meetings (< 1%) | Qualification or CTA issues | Clarify meeting ask, reduce friction (include calendar link) |
| High bounce rate (> 5%) | Bad data | Verify email list, use email validation service |
| High unsubscribe (> 2%) | Over-sending or poor targeting | Reduce frequency, tighten ICP criteria |

---

## Cold Email Copy Research: What Gets Replies

Directional patterns on cold email copy that tends to convert: what subject lines, openers, body lengths, CTAs, and follow-up patterns work. These are patterns commonly reported by outreach practitioners and vendors, not a single verified study; treat specific percentages as illustrative, not authoritative.

---

### Subject Line Patterns by Format

| Format | Open Rate | Reply Lift | Example |
|--------|-----------|-----------|---------|
| Question (short, specific) | Above average | High | "Quick question about [Company]'s growth?" |
| Trigger event reference | Above average | Very high | "Congrats on the Series B, [first name]" |
| Name + company in subject | Above average | High | "How [Company] handles [challenge]?" |
| 1-3 word subjects | Above average | Medium-high | "Quick question" / "Idea for [Company]" |
| Stat / insight hook | Above average | Medium | "[Industry] teams waste hours a week on this" |
| Benefit claim | Average | Low-medium | "Cut your onboarding time in half" |
| "FWD:" / "RE:" (never fake these) | High but ethically risky | Ethical concern | Do not use falsely |

No single authoritative benchmark ties an exact open rate or reply lift to a subject line format across sources; use this table to prioritize what to test, not as a guaranteed outcome.

**What tanks open rates:**
- Anything that reads as a mass blast: "Boost your revenue with [Product]"
- Excessive punctuation in subject: "Want to 10x your pipeline?!" — spam filter + human pattern recognition
- All caps: "FREE DEMO THIS WEEK"
- False urgency: "LAST CHANCE" to someone who never expressed interest

**The subject line principle practitioners converge on:** specificity beats cleverness. "Quick question about Acme's onboarding flow" tends to outperform "The secret to better onboarding" for the same product. The specific question signals you did research; the clever hook signals you sent 10,000. This is a directional pattern, not a measured result from a single verified dataset.

---

### The BASHO Opener (Highest-Reply-Rate Cold Email Opening)

BASHO = research-based personalized opening that connects a specific observation about the prospect to your value prop.

**Structure:**
```
[Specific observation about them] → [Bridge to why you're reaching out] → [Precise value claim]
```

**Example (B2B SaaS, targeting VP Marketing):**
> "I read your post on [LinkedIn topic] about [specific point they made] — you're right that most CDP tools overcomplicate this. We solved that for [similar company type] by [specific mechanism], and they saw [specific outcome]. Worth a 15-minute look?"

**Why it works:** The observation proves research. The bridge makes relevance immediate. The precise claim is credible because the opening was credible.

**What makes BASHO fail:** When the "specific observation" is actually generic ("I see you're in the SaaS space" — this is L1 dressed as L4). Real BASHO requires 5-10 minutes of actual research per prospect.

---

### Trigger-Event Openers That Convert

| Trigger | Opener Pattern | Rationale |
|---------|---------------|-----------|
| Funding round | "Congrats on the Series B — at this stage teams usually face [specific challenge]" | Post-funding is buying season. Connects milestone to problem. |
| New executive hire | "Saw [name] joined as [role] at [Company] — when new [roles] come in, they often [action related to your product]" | New execs have mandate to change things. High receptivity window is 30-90 days. |
| Job posting | "Your [role] posting signals [inference about their challenge]" | Job postings are the most public signal of what a company is building/struggling with. |
| Product launch | "Saw [Company] just launched [product] — reaching customers who [relevant segment] usually becomes the next challenge" | Bridges their momentum to your solution. |
| Company news | "Saw [Company] is expanding into [market] — teams we work with at this stage typically run into [specific problem]" | Connects growth to a solvable pain. |

---

### The 3-Line Email Method

For VP/C-suite outreach. The less you write, the more senior you appear.

**Structure:**
```
Line 1: Specific observation OR trigger event reference (1 sentence, no "I hope this finds you well")
Line 2: One precise value claim. Use a number. Reference a relevant customer if possible.
Line 3: Ultra-low-friction ask. Not "can we schedule a 30-minute call" — "worth a quick look?"
```

**Example:**
> "Saw [Company] just closed your Series B — congrats.
> We helped [similar company] reduce their activation drop-off by 34% in their first 90 days post-funding.
> Worth a 10-minute look at what we did?"

**Why it works:** Respects their time. No preamble. The economy of words signals confidence. "Worth a look?" is a micro-commitment — far lower friction than "can we schedule a call."

---

### Body Length Patterns

No single authoritative study ties an exact reply rate to a specific word count, but the direction is consistent across most practitioner and vendor reporting:

| Length | Direction | Notes |
|--------|-----------|-------|
| Under 50 words | Underperforms | Often lacks enough context to drive a reply |
| Roughly 50-125 words | Generally the strongest performer | Reported sweet spot across most sources |
| Roughly 125-200 words | Declining | Starts feeling like a pitch |
| 200+ words | Underperforms | Too long for a cold context |

**VP vs. Manager:** VP/Director level: use 3-line or short (roughly 50-80 word) emails. Manager/IC level: somewhat more context is acceptable, but stay well under 200 words.

---

### P.S. Line — Why It Works and What to Write

The P.S. is read almost as often as the first line of the email — it's an eye-catching standalone unit. Use it for one of three purposes:

1. **Social proof:** "P.S. [Similar Company] saw [specific outcome] in 60 days using this approach."
2. **Alternative CTA:** "P.S. If now isn't the right time, would [Q3] timing make more sense?"
3. **Pattern interrupt:** "P.S. I also left a voice message — checking both." (Only if you actually did.)

**What not to use P.S. for:** repeating the main CTA, adding more features/benefits, or anything that sounds like legal text.

---

### CTA Comparison Patterns

| CTA Type | Relative Performance | Notes |
|----------|----------------------|-------|
| Micro-commitment: "Worth a 10-minute look?" | Tends to perform best | Lowest friction possible |
| Calendar link: "Here's my calendar: [link]" | Tends to underperform in a first email | Doubles friction; many VPs won't click an unknown link in first email |
| "Let me know if you'd like to connect" | Tends to underperform | Too passive - ambiguous ask produces ambiguous replies |
| "Are you the right person to speak to?" | Performs reasonably well | Effective for cold outbound when gatekeeper risk is high - gets referrals |
| "If this is relevant, I can send you [specific content]" | Performs reasonably well | Low-commitment value offer - pulls without pushing |

**The pattern:** Micro-commitment CTAs ("worth a look?", "open to a quick chat?") tend to outperform direct meeting requests in first-touch emails, based on general practitioner consensus rather than one verified study. Save the calendar link for Email 2 or after a positive reply.

---

### Follow-Up Copy Patterns (What Gets Replies Without Being Annoying)

**Day 3-5 follow-up:**

Add new value, don't just nudge. The worst follow-up is "just checking in" or "wanted to bump this up." These generate near-zero replies.

What works:
- New angle: different pain point or outcome relevant to their role
- Relevant content: a case study, data point, or insight they'd genuinely find useful
- Pattern: "Thought this [specific stat/insight] was relevant given [what you mentioned/what you know about their situation]"

**Day 7-10 follow-up:**

Switch medium if you haven't. If emails haven't worked, try LinkedIn comment (not InMail), then a phone call if account is high-value.

For email: shorter than Email 1. Acknowledge the non-response without guilt-tripping.
> "I know timing matters. If [challenge] is something you're working through in [Q3/2025], I'm happy to share what worked for [Company X]. No pressure otherwise."

**Day 14-21 "breakup" email:**

Generally the highest-reply follow-up in the sequence. Breakup emails tend to outperform standard follow-ups by a meaningful margin because loss aversion activates; the exact multiplier is not consistently reproducible across sources.

What works:
> "Subject: Should I close your file?
> Body: [First name], I've reached out a few times and haven't heard back, so I'm guessing the timing isn't right.
> I'll stop reaching out — but if [specific outcome] ever becomes a priority, I'd love to reconnect.
> [Name]"

The "close your file" frame triggers two responses: (a) people who genuinely aren't interested confirm it, cleaning your list; (b) people who are interested but busy often reply because they don't want to be removed.

**What fails, per general practitioner consensus:**
- "I hope this finds you well" — immediately signals mass email
- Paragraphs about your company history or founding story
- Feature lists ("we offer X, Y, Z, A, B, C...")
- Multiple CTAs in one email ("you can book a call, watch a demo, or download our guide")
- Fake RE: or FWD: subject lines — destroys trust when exposed
- Sending from a domain that's less than 60 days old without warming
- Sending 50+ emails per day from a single domain without warming (5-10/day start, scale over 6-8 weeks)

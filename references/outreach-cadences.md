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

### Real-World Outreach Performance Data (2024–2025)

Sourced from Instantly, Belkins, Salesloft, Apollo, and Gong Labs. These are population averages across millions of sequences — not best-in-class cherry-picked numbers.

| Metric | Real Average | Top 10% | Source | Notes |
|--------|-------------|---------|--------|-------|
| Cold email reply rate | 3–3.43% | 8–10% | Instantly 2024 (5B+ emails) | Across all industries and ICPs |
| Cold email positive reply rate | 1–1.5% | 3–5% | Belkins 2024 | "Interested in learning more" or similar |
| Meeting booked rate (per prospect) | 1–1.5% | 3–5% | Apollo / Salesloft 2024 | Meetings per total prospects in sequence |
| Open rate (B2B cold) | 32–45% | 55%+ | Instantly 2024 | Inflated by Apple MPP — click rate is more reliable |
| Multi-channel vs. email-only lift | +287% more replies | — | Salesloft 2024 (n=millions of sequences) | Email + LinkedIn + phone vs. email only |
| Response timing — 5-min vs. 30-min | 21x more likely to qualify | — | InsideSales / Velocify | Speed to respond is #1 predictor for inbound |
| Touch count before response | Touch 3–5 most likely | — | Salesloft 2024 | Don't give up after touch 1–2 |
| Personalized L3-L4 vs. L1 reply lift | 80–150% higher | — | Woodpecker 2024 research | Deep research personalization vs. name/company only |
| Phone connect rate (cold) | 8–12% | 15–20% | Gong Labs 2024 | Of dials that reach a human |
| LinkedIn InMail response rate | 10–25% | 35%+ | LinkedIn Marketing Solutions 2024 | 3x higher than email; drops fast if InMail quality is poor |

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

Deep-research findings on cold email copy that actually converts — what subject lines, openers, body lengths, CTAs, and follow-up patterns work. Sourced from Lemlist, Woodpecker, Salesloft, Instantly, Belkins, and practitioner communities.

---

### Subject Line Data by Format

| Format | Open Rate | Reply Lift | Source | Example |
|--------|-----------|-----------|--------|---------|
| Question (short, specific) | 35-45% | High | Lemlist 2024 | "Quick question about [Company]'s growth?" |
| Trigger event reference | 38-50% | Very high | Woodpecker 2024 | "Congrats on the Series B, [first name]" |
| Name + company in subject | 32-40% | High (+22-35%) | Outbound.io + Salesloft | "How [Company] handles [challenge]?" |
| 1-3 word subjects | 42-55% | Medium-high | Lemlist 2024 | "Quick question" / "Idea for [Company]" |
| Stat / insight hook | 30-40% | Medium | Woodpecker 2024 | "[Industry] teams waste 23 hrs/week on this" |
| Benefit claim | 28-35% | Low-medium | Lemlist 2024 | "Cut your onboarding time in half" |
| "FWD:" / "RE:" (never fake these) | 48-60% | Ethical concern | — | Do not use falsely |

**What tanks open rates:**
- Anything that reads as a mass blast: "Boost your revenue with [Product]"
- Excessive punctuation in subject: "Want to 10x your pipeline?!" — spam filter + human pattern recognition
- All caps: "FREE DEMO THIS WEEK"
- False urgency: "LAST CHANCE" to someone who never expressed interest

**The subject line principle from Lemlist's 5B-send dataset:** specificity beats cleverness. "Quick question about Acme's onboarding flow" outperforms "The secret to better onboarding" for the same product. The specific question signals you did research; the clever hook signals you sent 10,000.

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

### Body Length Research

The Woodpecker 2024 study of 20M+ cold emails — the clearest body length data available:

| Length | Reply Rate | Notes |
|--------|-----------|-------|
| Under 50 words | 3.1% | Too short — often lacks enough context to drive reply |
| 50-125 words | 5.2% | **Sweet spot — highest reply rate** |
| 125-200 words | 3.8% | Declining — starts feeling like a pitch |
| 200-350 words | 2.1% | Too long for cold context |
| 350+ words | 1.4% | Significantly underperforms across all segments |

**Salesloft supporting data:** The average email that got a reply at a company using their platform was 120 words. The average email that didn't get a reply was 190 words.

**VP vs. Manager:** VP/Director level: use 3-line or 50-80 word emails. Manager/IC level: up to 120 words with slightly more context acceptable. Never 200+.

---

### P.S. Line — Why It Works and What to Write

The P.S. is read almost as often as the first line of the email — it's an eye-catching standalone unit. Use it for one of three purposes:

1. **Social proof:** "P.S. [Similar Company] saw [specific outcome] in 60 days using this approach."
2. **Alternative CTA:** "P.S. If now isn't the right time, would [Q3] timing make more sense?"
3. **Pattern interrupt:** "P.S. I also left a voice message — checking both." (Only if you actually did.)

**What not to use P.S. for:** repeating the main CTA, adding more features/benefits, or anything that sounds like legal text.

---

### CTA Comparison Data

| CTA Type | Reply/Meeting Rate | Notes |
|----------|------------------|-------|
| Micro-commitment: "Worth a 10-minute look?" | ~6.2% | Lemlist research — lowest friction possible |
| Calendar link: "Here's my calendar: [link]" | ~3.1% | Doubles friction; many VPs won't click an unknown link in first email |
| "Let me know if you'd like to connect" | ~2.4% | Too passive — ambiguous ask produces ambiguous replies |
| "Are you the right person to speak to?" | ~4.8% | Effective for cold outbound when gatekeeper risk is high — gets referrals |
| "If this is relevant, I can send you [specific content]" | ~5.1% | Low-commitment value offer — pulls without pushing |

**The finding:** Micro-commitment CTAs ("worth a look?", "open to a quick chat?") consistently outperform direct meeting requests in first-touch emails. Save the calendar link for Email 2 or after a positive reply.

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

The highest-reply follow-up in the sequence. Breakup emails have 2-3x the reply rate of standard follow-ups because loss aversion activates.

What works:
> "Subject: Should I close your file?
> Body: [First name], I've reached out a few times and haven't heard back, so I'm guessing the timing isn't right.
> I'll stop reaching out — but if [specific outcome] ever becomes a priority, I'd love to reconnect.
> [Name]"

The "close your file" frame triggers two responses: (a) people who genuinely aren't interested confirm it, cleaning your list; (b) people who are interested but busy often reply because they don't want to be removed.

**What fails in 2024-2025 (Lemlist, Instantly, Woodpecker practitioner consensus):**
- "I hope this finds you well" — immediately signals mass email
- Paragraphs about your company history or founding story
- Feature lists ("we offer X, Y, Z, A, B, C...")
- Multiple CTAs in one email ("you can book a call, watch a demo, or download our guide")
- Fake RE: or FWD: subject lines — destroys trust when exposed
- Sending from a domain that's less than 60 days old without warming
- Sending 50+ emails per day from a single domain without warming (5-10/day start, scale over 6-8 weeks)

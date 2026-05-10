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

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| **Open rate** | < 25% | 30-40% | 40-55% | > 55% |
| **Reply rate (total)** | < 3% | 5-8% | 8-12% | > 12% |
| **Positive reply rate** | < 1% | 2-4% | 4-8% | > 8% |
| **Meeting booked rate** | < 1% | 1.5-3% | 3-5% | > 5% |
| **Sequence completion rate** | < 40% | 50-65% | 65-80% | > 80% |
| **Bounce rate** | > 5% | 2-5% | 1-2% | < 1% |
| **Unsubscribe rate** | > 2% | 1-2% | 0.5-1% | < 0.5% |

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

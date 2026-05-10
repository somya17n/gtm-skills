# Sales Conversation Analysis

Reference for analyzing sales conversations: talk ratio, patience, monologue detection, interactivity, question rate, BANT and MEDDIC qualification frameworks, objection detection, sentiment scoring, and coaching output structure.

---

## Talk Ratio Benchmarks

The percentage of time the sales rep talks versus listens during a conversation.

| Talk Ratio (Rep) | Rating | Description |
|-------------------|--------|-------------|
| < 30% | Too passive | Rep is not guiding the conversation or sharing enough value |
| 30-40% | Good for discovery | Appropriate for early discovery calls — mostly listening |
| 40-60% | Ideal range | Balanced conversation — the golden zone |
| 60-70% | Leaning monologue | Rep is talking too much; risk of losing prospect |
| > 70% | Monologue | Rep is dominating; prospect is disengaged |

### Talk Ratio by Call Type

| Call Type | Ideal Rep Talk % | Rationale |
|-----------|-----------------|-----------|
| Discovery | 30-40% | Listen to understand pain, let prospect talk |
| Demo | 50-60% | Presenting, but with interactive Q&A |
| Negotiation | 40-50% | Balanced — presenting offers, hearing concerns |
| Follow-up | 35-45% | Checking understanding, addressing questions |
| Closing | 40-55% | Summarizing, handling last objections, asking for the deal |

---

## Patience Score

Measures how long the rep waits in silence before interrupting or filling the gap.

| Silence Duration | Rating | Interpretation |
|-----------------|--------|---------------|
| > 5 seconds | Excellent | Comfortable with silence; prospect feels space to think |
| 3-5 seconds | Good | Adequate patience; allows prospect to complete thoughts |
| 2-3 seconds | Average | Acceptable but could improve |
| 1-2 seconds | Below average | Jumping in too quickly; prospect may feel rushed |
| < 1 second | Poor | Interrupting or overlapping; prospect will disengage |

### Measurement

- Track the gap between the prospect finishing a statement and the rep starting their next statement
- Average across all conversation turns
- Identify instances of overlap (negative silence = interruption)
- Flag interruptions separately: count of times rep spoke before prospect finished

---

## Longest Monologue

The longest uninterrupted stretch of the rep talking without asking a question or receiving input.

| Duration | Rating | Impact |
|----------|--------|--------|
| < 30 seconds | Excellent | Highly conversational, engaged prospect |
| 30-60 seconds | Good | Appropriate for demos and presentations |
| 60-90 seconds | Caution | Getting long — prospect attention may wander |
| > 90 seconds | Problem | Losing prospect attention; needs to break up with a question |
| > 120 seconds | Critical | Almost certainly lost the prospect; monologue mode |

### Remediation

When longest monologue > 90 seconds, coaching recommendation:

- Insert a check-in question every 60 seconds: "Does that make sense so far?" or "How does that compare to what you're doing today?"
- Break presentations into segments with interactive transitions
- Use the "teach-ask" pattern: share an insight, then ask how it relates to their situation

---

## Interactivity Score (0-100)

A composite metric measuring how conversational and engaged the call is.

### Components

| Component | Weight | Measurement |
|-----------|--------|-------------|
| Question rate | 30% | Questions asked per 10 minutes |
| Turn-taking frequency | 25% | Number of speaker switches per minute |
| Balanced talk ratio | 20% | Proximity to ideal 50/50 split |
| Prospect engagement | 15% | Length and depth of prospect responses |
| Silence comfort | 10% | Average pause duration before response |

### Score Ranges

| Score | Label | Description |
|-------|-------|-------------|
| 80-100 | Highly Interactive | Dynamic, collaborative conversation with balanced exchange |
| 60-79 | Interactive | Good back-and-forth with occasional long stretches |
| 40-59 | Moderately Interactive | Some dialogue but too much one-way talking |
| 20-39 | Low Interactivity | Dominated by one speaker; feels like a presentation |
| 0-19 | Monologue | One-way communication; not a conversation |

---

## Question Rate

The number of questions the rep asks per 10-minute window.

| Rate | Rating | Description |
|------|--------|-------------|
| 5+ per 10 min | Over-questioning | Feels like an interrogation; balance with insights |
| 3-5 per 10 min | Ideal | Genuine curiosity driving productive dialogue |
| 2-3 per 10 min | Adequate | Room for improvement; should probe deeper |
| 1-2 per 10 min | Low | Presenting more than discovering |
| < 1 per 10 min | Critical | Not asking questions; cannot qualify or understand needs |

### Question Quality Taxonomy

| Question Type | Quality | Example |
|--------------|---------|---------|
| Open-ended | High | "What's driving the need to solve this now?" |
| Probing | High | "Can you tell me more about how that impacts your team?" |
| Clarifying | Medium-High | "When you say 'too slow,' what specifically do you mean?" |
| Confirming | Medium | "So the main issue is X — is that right?" |
| Closed (yes/no) | Low-Medium | "Are you using [tool] today?" |
| Leading | Low | "You'd agree that faster is better, right?" |
| Loaded | Avoid | "Why haven't you fixed this already?" |

---

## BANT Framework

### Budget

Does the prospect have budget allocated for this purchase?

| Score | Criteria |
|-------|----------|
| 25 | Budget explicitly confirmed and allocated for this fiscal period |
| 20 | Budget exists but not yet allocated; needs internal approval |
| 15 | Budget identified but competing priorities; requires reallocation |
| 10 | No budget currently; exploring for future planning |
| 5 | Budget constrained; not a priority for allocation |
| 0 | No discussion of budget; unknown |

### Authority

Is the contact the decision maker or can they influence the decision?

| Score | Criteria |
|-------|----------|
| 25 | Contact is the final decision maker with signing authority |
| 20 | Contact is a strong champion who directly influences the decision maker |
| 15 | Contact is part of the buying committee but not the primary authority |
| 10 | Contact can recommend but has limited influence on the decision |
| 5 | Contact is an end user with no purchasing influence |
| 0 | Decision-making authority is unknown |

### Need

Is the pain real, acknowledged, and urgent?

| Score | Criteria |
|-------|----------|
| 25 | Explicit, urgent pain with quantified business impact |
| 20 | Clear pain acknowledged by multiple stakeholders |
| 15 | Pain identified but not yet quantified or broadly acknowledged |
| 10 | Vague dissatisfaction with current state; exploring options |
| 5 | Latent need; prospect not actively looking to solve |
| 0 | No need identified or discussed |

### Timeline

When does the prospect need a solution in place?

| Score | Criteria |
|-------|----------|
| 25 | Active evaluation with decision deadline within 30 days |
| 20 | Defined timeline: decision within 60-90 days |
| 15 | General timeline: "this quarter" or "this half" |
| 10 | Vague timeline: "sometime this year" |
| 5 | No timeline pressure; "looking for the future" |
| 0 | Timeline not discussed |

### BANT Total Score

| Total (0-100) | Qualification |
|---------------|--------------|
| 80-100 | Highly Qualified — pursue aggressively |
| 60-79 | Qualified — continue working, address gaps |
| 40-59 | Partially Qualified — needs development in weak areas |
| 20-39 | Weakly Qualified — nurture, check back later |
| 0-19 | Not Qualified — disqualify or long-term nurture |

---

## MEDDIC Framework

### Metrics

What is the quantified business impact of solving this problem?

| Score | Criteria |
|-------|----------|
| 17 | Clear, quantified metrics agreed upon: "save $500K/year" or "reduce churn by 3%" |
| 13 | Metrics identified but not yet agreed or verified by prospect |
| 9 | General impact discussed: "improve efficiency" or "grow revenue" |
| 5 | Impact mentioned vaguely; no quantification attempted |
| 0 | Business impact not discussed |

### Economic Buyer

Who signs the check? Have you engaged them?

| Score | Criteria |
|-------|----------|
| 17 | Economic buyer identified, engaged, and supportive |
| 13 | Economic buyer identified and aware; not yet directly engaged |
| 9 | Economic buyer identified but access is blocked or delayed |
| 5 | Economic buyer role is known but specific person is not identified |
| 0 | Economic buyer unknown |

### Decision Criteria

What are the technical and business requirements for the solution?

| Score | Criteria |
|-------|----------|
| 17 | Formal evaluation criteria documented and your solution maps well to all |
| 13 | Criteria known and you meet most; actively addressing gaps |
| 9 | Some criteria known; unclear if your solution is the best fit |
| 5 | Vague criteria; "we'll know it when we see it" |
| 0 | Decision criteria not discussed |

### Decision Process

What are the stages, timeline, and stakeholders involved in making the decision?

| Score | Criteria |
|-------|----------|
| 17 | Full process mapped: stages, timeline, stakeholders, approval chain |
| 13 | Process partially understood; key stages and timeline known |
| 9 | General understanding of process; some stages unclear |
| 5 | Vague: "we'll discuss internally and get back to you" |
| 0 | Decision process not discussed |

### Identify Pain

What specific pain points has the prospect articulated?

| Score | Criteria |
|-------|----------|
| 17 | Multiple specific pains identified with business impact quantified for each |
| 13 | Primary pain clearly articulated with some impact understanding |
| 9 | Pain acknowledged but not deeply explored or quantified |
| 5 | General dissatisfaction expressed; no specific pain points |
| 0 | No pain discussed; prospect seems satisfied with status quo |

### Champion

Is there an internal advocate with power, influence, and motivation to push the deal?

| Score | Criteria |
|-------|----------|
| 17 | Strong champion identified: has power, vested interest, and actively sells internally |
| 13 | Champion identified with influence but limited organizational power |
| 9 | Potential champion — supportive but untested in advocacy role |
| 5 | Friendly contact but no indication of willingness to champion |
| 0 | No champion identified |

### MEDDIC Total Score

| Total (0-102) | Qualification |
|---------------|--------------|
| 80-102 | Strong Deal — high probability of close |
| 60-79 | Good Deal — address remaining gaps proactively |
| 40-59 | Developing Deal — significant work needed on weak elements |
| 20-39 | At Risk — major gaps that threaten the deal |
| 0-19 | Weak Deal — consider deprioritizing or disqualifying |

---

## Objection Detection

### Objection Categories

| Category | Keywords/Phrases | Example |
|----------|-----------------|---------|
| **Price** | "too expensive", "budget", "cost", "pricing", "can't afford", "ROI", "cheaper" | "Your pricing is higher than what we're paying now" |
| **Timing** | "not now", "next quarter", "not a priority", "busy", "revisit later", "bad timing" | "We're focused on other things right now" |
| **Competition** | "already using", "competitor", "evaluated", "compared", "alternative", "other vendors" | "We're already working with [competitor]" |
| **Status Quo** | "working fine", "don't need", "not broken", "current solution", "happy with" | "What we have works well enough" |
| **Authority** | "need to check", "not my decision", "talk to my boss", "committee", "approval" | "I'd need to get buy-in from my VP" |
| **Trust/Risk** | "concerns about", "security", "implementation", "disruption", "change management" | "We're worried about the migration effort" |
| **Feature Gap** | "does it do", "missing", "need", "require", "can't do" | "Does it integrate with our [specific tool]?" |

### Objection Scoring

| Score | Interpretation |
|-------|---------------|
| 0 objections detected | Either too early in conversation or prospect is very receptive |
| 1-2 objections | Normal — healthy sign of engagement |
| 3-4 objections | Moderate concern — ensure each is addressed |
| 5+ objections | High concern — prospect may not be a fit or rep is losing control |

---

## Sentiment Scoring

### Breakdown

| Sentiment | Definition | Indicators |
|-----------|-----------|------------|
| **Positive** | Prospect is engaged, interested, enthusiastic | Asking follow-up questions, expressing interest ("that's interesting"), affirming ("yes, exactly"), discussing next steps, using future tense ("when we implement") |
| **Neutral** | Prospect is listening but not committed | Short responses, factual questions, no emotional language, neither enthusiastic nor resistant |
| **Negative** | Prospect is resistant, skeptical, or disengaged | Objections, pushback, skeptical questions ("but what about..."), short/dismissive responses, disengagement cues ("I need to go"), challenges ("prove it") |

### Sentiment Trajectory

| Pattern | Interpretation | Action |
|---------|---------------|--------|
| Positive → Positive | Strong engagement throughout | Move to next stage confidently |
| Neutral → Positive | Warming up; message is landing | Continue current approach, accelerate CTA |
| Positive → Negative | Something went wrong mid-call | Identify the trigger, address the concern directly |
| Negative → Positive | Objection successfully handled | Reinforce the resolution, build on positive momentum |
| Negative → Negative | Not landing; prospect is not a fit or approach is wrong | Reconsider qualification, try a different angle, or gracefully exit |

---

## Coaching Output Structure

Every conversation analysis should produce a structured coaching report.

### 1. Strengths

What the rep did well — reinforce these behaviors.

```
Strengths:
- Strong opening: established credibility in first 30 seconds with a relevant trigger event
- Excellent discovery questions at 4:20 and 7:15 — open-ended and pain-probing
- Good patience score (4.2s average) — let the prospect think
- Handled pricing objection at 18:30 with quantified ROI response
```

### 2. Weaknesses

Areas for improvement — specific, actionable, not personal.

```
Weaknesses:
- Longest monologue of 2:15 at 12:00-14:15 — lost prospect attention (their responses shortened after)
- Talk ratio skewed to 65% — too much presenting, not enough dialogue
- Did not ask about timeline or budget — BANT incomplete
- Missed opportunity to multi-thread when prospect mentioned "my team would need to see this"
```

### 3. Specific Rewrites (with Timestamps)

Concrete, word-for-word alternatives for specific moments.

```
Rewrites:

[12:30] Instead of: "Let me walk you through all of our features..."
        Try: "Which of these areas is most relevant to your situation? I'll focus there."

[18:45] Instead of: "Our pricing is very competitive."
        Try: "Teams your size typically see a 3x ROI within 6 months — let me show you the math."

[22:10] Instead of: "Let me know if you have any questions."
        Try: "Based on what we discussed, what would need to be true for you to move forward?"
```

### 4. Recommended Drills

Targeted practice exercises to build specific skills.

| Drill | Description | Duration | Frequency |
|-------|-------------|----------|-----------|
| **60-second teach-ask** | Present a value point in 60 seconds, then ask a question | 15 min | 2x/week |
| **Question ladder** | Practice asking 3 escalating questions on any topic | 10 min | Daily |
| **Objection handling** | Role-play top 3 objections with a partner | 20 min | Weekly |
| **Silence tolerance** | Practice 5-second pauses after asking a question | 10 min | Daily |
| **BANT check** | After every mock call, score BANT from memory | 5 min | After every call |
| **3x3 research** | Practice finding 3 personalized insights in 3 minutes | 3 min | Before every call |
| **Closing pivot** | Practice transitioning from any topic to a next-step ask | 10 min | 2x/week |

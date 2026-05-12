# Dual Deal Scoring

Reference for scoring and analyzing sales deals: stage definitions, velocity benchmarks, risk signals, forecast categories, win rates, pipeline coverage, health score, intent score, trend indicators, quadrant analysis, and scoring weights. Shared by pipeline-review and deal-scoring skills.

---

## Stage Definitions

### Standard Sales Pipeline Stages

| Stage | Description | Key Activities | Typical Duration |
|-------|-------------|----------------|-----------------|
| **Prospecting** | Initial outreach and identification of potential buyers | Cold outreach, inbound lead capture, research, initial qualification | 7-14 days |
| **Qualification** | Determining if the prospect has a real need and is worth pursuing | Discovery calls, BANT/MEDDIC assessment, ICP validation | 7-21 days |
| **Discovery/Demo** | Deep dive into needs and demonstration of solution fit | Product demos, technical evaluation, requirements gathering, pain exploration | 14-30 days |
| **Proposal** | Formal proposal, pricing, and scope presentation | Proposal creation, pricing discussion, ROI presentation, stakeholder alignment | 7-14 days |
| **Negotiation** | Contract terms, pricing finalization, legal review | Contract redlining, procurement, security review, terms negotiation | 7-21 days |
| **Won** | Deal closed, contract signed | Contract execution, handoff to customer success, implementation planning | -- |
| **Lost** | Deal lost at any stage | Loss reason documentation, post-mortem analysis | -- |

---

## Deal Velocity

Deal velocity measures the average number of days a deal spends in each stage. Deals that significantly exceed the average are flagged as "stuck."

### Average Days per Stage (Benchmarks)

| Stage | SMB (< $10K ACV) | Mid-Market ($10K-$50K) | Enterprise ($50K+) |
|-------|-------------------|----------------------|-------------------|
| Prospecting | 5-7 days | 7-14 days | 14-21 days |
| Qualification | 3-7 days | 7-14 days | 14-30 days |
| Discovery/Demo | 7-14 days | 14-21 days | 21-45 days |
| Proposal | 3-7 days | 7-14 days | 14-30 days |
| Negotiation | 3-7 days | 7-14 days | 14-30 days |
| **Total cycle** | **21-42 days** | **42-77 days** | **77-156 days** |

### Stuck Deal Detection

```
A deal is "stuck" when:
  days_in_current_stage > 2 × average_days_for_stage_and_segment
```

| Stuck Level | Multiplier | Action |
|-------------|-----------|--------|
| Warning | 1.5x average | Flag for review in next pipeline meeting |
| Stuck | 2x average | Require action plan from rep within 48 hours |
| Critical | 3x average | Escalate to manager; consider deprioritizing |

### Velocity Calculation

This formula measures pipeline/sales velocity (total revenue throughput over time), not individual deal speed (days a specific deal spends in a stage).

```
Deal Velocity = (Number of Deals × Average Deal Value × Win Rate) / Average Sales Cycle Length

Example:
  100 deals × $25,000 × 25% win rate / 60 days = $10,417 revenue per day
```

---

## Risk Signals

Factors that indicate a deal may be at risk of stalling or loss.

| Risk Signal | Severity | Detection |
|-------------|----------|-----------|
| **Single-threaded** | High | Only 1 contact engaged at the account |
| **No activity 14+ days** | High | No emails, calls, meetings, or updates in 14+ days |
| **Declining intent** | High | Intent score trending downward over 14+ days |
| **Missing BANT elements** | Medium-High | 2+ BANT elements not addressed (Budget, Authority, Need, Timeline) |
| **No next step scheduled** | Medium | No future meeting or action item on the calendar |
| **Competitor mentioned** | Medium | Prospect has mentioned evaluating alternatives |
| **Champion gone silent** | High | Previously active champion has stopped responding |
| **Decision process unclear** | Medium | No documented decision process or timeline |
| **Budget not confirmed** | Medium | Deal in Proposal+ stage without confirmed budget |
| **Contract stalled** | High | Legal/procurement review exceeding 2x average duration |
| **Stakeholder change** | High | Key contact has left the company or changed roles |
| **Scope creep** | Medium | Requirements expanding without corresponding budget increase |
| **Decreasing meeting attendance** | Medium | Fewer prospect stakeholders attending each meeting |

### Risk Scoring

Each risk signal carries a weight. Total risk score = sum of active risk weights.

| Risk Level | Total Weight | Action |
|-----------|-------------|--------|
| Low (0-15) | 0-15 points | Normal management |
| Medium (16-30) | 16-30 points | Proactive intervention needed |
| High (31-50) | 31-50 points | Urgent action required; escalate |
| Critical (51+) | 51+ points | Consider deprioritizing or disqualifying |

---

## Forecast Categories

### Category Definitions

| Category | Probability Range | Criteria |
|----------|------------------|---------|
| **Commit** | > 90% | Verbal/written confirmation, contract in signature, procurement processing |
| **Best Case** | 60-90% | Strong champion, proposal accepted, negotiating terms |
| **Pipeline** | 30-60% | Active engagement, demo completed, proposal pending or delivered |
| **Omit** | < 30% | Early stage, no clear path to close, stalled, or unqualified |

### Forecast Accuracy Measurement

```
Forecast Accuracy = 1 - |Forecasted Revenue - Actual Revenue| / Actual Revenue

Targets:
  Commit accuracy: > 90%
  Best Case accuracy: > 70%
  Pipeline accuracy: > 50%
  Overall weighted accuracy: > 75%
```

### Category Movement Rules

| From → To | Trigger |
|-----------|---------|
| Pipeline → Best Case | Champion confirmed, proposal delivered, timeline confirmed |
| Best Case → Commit | Verbal yes, contract sent for signature |
| Any → Omit | Stalled > 3x average, champion lost, budget cut, competitor selected |
| Omit → Pipeline | Re-engagement detected, new champion, renewed interest |

---

## Win Rate Benchmarks by Stage

The probability of winning a deal given it has reached a particular stage.

| Stage | Win Rate (SMB) | Win Rate (Mid-Market) | Win Rate (Enterprise) |
|-------|---------------|----------------------|----------------------|
| Prospecting | 5-8% | 3-5% | 2-4% |
| Qualification | 15-20% | 12-18% | 10-15% |
| Discovery/Demo | 30-40% | 25-35% | 20-30% |
| Proposal | 50-60% | 45-55% | 40-50% |
| Negotiation | 70-80% | 65-75% | 60-70% |

### Real-World Win Rate Data (2024–2025)

Sourced from Gong Labs, Salesloft, and CSO Insights. Win rates have compressed significantly since 2022 due to economic pressure and increased competition.

| Metric | Real Benchmark | Source | Notes |
|--------|---------------|--------|-------|
| Overall B2B SaaS win rate | 19–21% | Gong Labs 2024 | Down from 23% in 2022 — 3-year trend of compression |
| SMB win rate | 22–27% | Gong Labs 2024 | Shorter cycle, fewer stakeholders |
| Mid-Market win rate | 17–22% | Gong Labs 2024 | |
| Enterprise win rate | 15–18% | Gong Labs 2024 | Most competitive, longest cycle |
| Demo → close rate (average) | 25% | Gong Labs 2024 | Across all B2B SaaS verticals |
| Demo → close rate (SaaS-specific) | 30% | Gong 2024 | SaaS products have slightly higher demo conversion |
| Competitive win rate (vs. identified competitor) | 47–54% | Gong Labs 2024 | When a competitor is named in the deal |
| Uncontested win rate (no competitor) | 71–78% | Gong Labs 2024 | When no alternative is being evaluated |
| Win rate — multi-threaded deals | 2x vs. single-threaded | Gong Labs 2024 | For deals >$50K ACV, 3+ contacts engaged |
| Average sales cycle — SMB | 21–45 days | Gong Labs 2024 | |
| Average sales cycle — Mid-Market | 45–90 days | Gong Labs 2024 | |
| Average sales cycle — Enterprise | 90–180+ days | Gong Labs 2024 | |
| Average sales cycle — overall SaaS | 84 days | Gong Labs 2024 | Median across all deal sizes |

### Win Rate Trend Analysis

Track win rates by:
- Stage (are deals stalling at a specific stage?)
- Rep (who needs coaching at which stage?)
- Segment (which segments convert best?)
- Source (which lead sources produce highest-quality pipeline?)
- Deal size (does close rate vary by deal value?)

---

## Pipeline Coverage Ratio

The ratio of total pipeline value to the revenue target.

```
Pipeline Coverage = Total Weighted Pipeline / Revenue Target

Where:
  Weighted Pipeline = Σ (deal_value × stage_win_rate)
```

| Coverage Ratio | Health | Action |
|---------------|--------|--------|
| > 4x | Over-covered | Focus on quality and deal velocity, not new pipeline |
| 3-4x | Healthy | Balanced — maintain pipeline generation cadence |
| 2-3x | Thin | Increase pipeline generation, expand prospecting |
| 1-2x | At Risk | Urgent pipeline generation needed, consider lowering target |
| < 1x | Critical | Target likely unachievable, restructure pipeline plan |

### Coverage by Segment

Track coverage separately for each segment, product line, or team:

```
Enterprise pipeline coverage: 3.2x (Healthy)
Mid-Market pipeline coverage: 2.1x (Thin — increase prospecting)
SMB pipeline coverage: 4.5x (Over-covered — focus on conversion)
```

---

## Health Score (0-100)

A composite score measuring the overall health and progression quality of a deal.

### Components

| Component | Weight | Scoring Logic |
|-----------|--------|--------------|
| **Deal Progression Velocity** | 25% | How quickly the deal is moving through stages relative to benchmarks |
| **Activity Recency** | 25% | When was the last meaningful interaction (meeting, email exchange, call) |
| **Engagement Depth** | 20% | Quality and frequency of interactions (meeting attendance, email replies, demo attendance) |
| **Stakeholder Coverage** | 15% | Number and seniority of contacts engaged at the account |
| **BANT Completeness** | 15% | How many BANT elements have been addressed and scored |

### Deal Progression Velocity (0-25)

| Condition | Score |
|-----------|-------|
| Moving faster than average for stage and segment | 25 |
| Moving at average pace | 20 |
| Slightly slow (1-1.5x average) | 15 |
| Slow (1.5-2x average) | 10 |
| Stuck (> 2x average) | 5 |
| Regressed (moved backward to earlier stage) | 0 |

### Activity Recency (0-25)

| Last Activity | Score |
|--------------|-------|
| Within 2 days | 25 |
| Within 5 days | 20 |
| Within 7 days | 15 |
| Within 14 days | 10 |
| Within 21 days | 5 |
| More than 21 days | 0 |

### Engagement Depth (0-20)

| Engagement Level | Score |
|-----------------|-------|
| Multiple stakeholders actively engaged, regular meetings, detailed email threads | 20 |
| Primary contact engaged, regular meetings, responsive | 15 |
| Primary contact responsive but meetings are infrequent | 10 |
| Sporadic responses, meetings being rescheduled | 5 |
| Minimal engagement, ghosting | 0 |

### Stakeholder Coverage (0-15)

| Coverage | Score |
|----------|-------|
| 4+ contacts engaged including economic buyer | 15 |
| 3 contacts including champion and evaluator | 12 |
| 2 contacts engaged | 8 |
| 1 contact only (single-threaded) | 4 |
| No active contacts | 0 |

### BANT Completeness (0-15)

| BANT Elements Addressed | Score |
|-------------------------|-------|
| All 4 elements scored (Budget, Authority, Need, Timeline) | 15 |
| 3 elements scored | 11 |
| 2 elements scored | 7 |
| 1 element scored | 4 |
| No BANT data | 0 |

### Health Score Ranges

| Range | Label | Color | Action |
|-------|-------|-------|--------|
| 80-100 | Healthy | Green | Maintain cadence, move to close |
| 60-79 | Good | Light Green | Monitor, address any gaps |
| 40-59 | Watch | Yellow | Proactive intervention needed |
| 20-39 | At Risk | Orange | Urgent action plan required |
| 0-19 | Critical | Red | Escalate or consider deprioritizing |

---

## Intent Score (0-100)

Measures the prospect's buying signals and readiness to purchase.

### Components

| Component | Weight | Scoring Logic |
|-----------|--------|--------------|
| **Website Visits** | 20% | Frequency and depth of website engagement |
| **Content Consumption** | 20% | Downloads, blog reads, video views, webinar attendance |
| **Feature Usage** | 20% | Trial/freemium feature adoption and depth |
| **Meeting Frequency** | 20% | Number and quality of meetings/demos |
| **Email Engagement** | 20% | Open rates, reply rates, click-through on sales emails |

### Website Visits (0-20)

| Activity | Score |
|----------|-------|
| Multiple pricing page visits + feature comparison | 20 |
| Pricing page visit + demo page | 16 |
| Regular product page visits (3+ in 7 days) | 12 |
| Occasional visits (1-2 per week) | 8 |
| Single visit | 4 |
| No website activity | 0 |

### Content Consumption (0-20)

| Activity | Score |
|----------|-------|
| Downloaded buyer's guide + attended webinar + read case studies | 20 |
| Downloaded gated content + read multiple blog posts | 16 |
| Attended webinar or read case study | 12 |
| Read 2+ blog posts | 8 |
| Viewed 1 content piece | 4 |
| No content engagement | 0 |

### Feature Usage (0-20)

| Activity | Score |
|----------|-------|
| Deep feature adoption (5+ features, daily usage) | 20 |
| Moderate adoption (3-4 features, weekly usage) | 16 |
| Basic usage (1-2 features, sporadic) | 12 |
| Account created, minimal usage | 8 |
| Trial started but no activity | 4 |
| No trial or free usage | 0 |

### Meeting Frequency (0-20)

| Activity | Score |
|----------|-------|
| 3+ meetings in last 14 days, including exec/decision maker | 20 |
| 2 meetings in last 14 days | 16 |
| 1 meeting in last 14 days | 12 |
| Meeting scheduled for future | 8 |
| Last meeting was 14-30 days ago | 4 |
| No meetings or last meeting > 30 days ago | 0 |

### Email Engagement (0-20)

| Activity | Score |
|----------|-------|
| Replying to emails, asking questions, forwarding internally | 20 |
| Opening and clicking links consistently | 16 |
| Opening most emails but not clicking | 12 |
| Sporadic opens | 8 |
| Opening but never engaging | 4 |
| Not opening emails | 0 |

### Intent Score Ranges

| Range | Label | Action |
|-------|-------|--------|
| 80-100 | Very High Intent | Strike while hot — accelerate to proposal/close |
| 60-79 | High Intent | Actively engaged — present proposal, push for next step |
| 40-59 | Medium Intent | Interested but not ready — continue nurturing |
| 20-39 | Low Intent | Casual interest — qualify harder, consider deprioritizing |
| 0-19 | No Intent | Not buying — long-term nurture or disqualify |

---

## Trend Indicators

Trends are computed by comparing scores across three time windows.

| Trend | Direction | Calculation |
|-------|-----------|-------------|
| **Rising** | Upward | 7-day average > 14-day average by >10% AND 14-day average > 30-day average by >10% |
| **Steady** | Flat | Less than 10% variance across all three windows |
| **Declining** | Downward | 7-day average < 14-day average by >10% AND 14-day average < 30-day average by >10% |

Apply trend analysis to both Health Score and Intent Score independently.

---

## Quadrant Analysis: Health x Intent Matrix

Plot deals on a 2x2 matrix using Health Score (Y-axis) and Intent Score (X-axis).

```
                 High Health
                     |
    NURTURE          |         ACT NOW
    (High Health,    |    (High Health,
     Low Intent)     |     High Intent)
                     |
  -------------------+-------------------
                     |
    DEPRIORITIZE     |         RESCUE
    (Low Health,     |    (Low Health,
     Low Intent)     |     High Intent)
                     |
                 Low Health
     Low Intent <----+----> High Intent
```

### Quadrant Actions

| Quadrant | Health | Intent | Strategy |
|----------|--------|--------|----------|
| **Act Now** | High (60+) | High (60+) | Priority deals. Accelerate to close. Remove friction. Get proposal/contract out. |
| **Nurture** | High (60+) | Low (< 60) | Deal is healthy but prospect is not ready. Continue education, build value, wait for intent signals. |
| **Rescue** | Low (< 60) | High (60+) | Prospect wants to buy but the deal is poorly managed. Fix health issues: re-engage stakeholders, address stalled stages, inject urgency. |
| **Deprioritize** | Low (< 60) | Low (< 60) | Neither healthy nor showing intent. Move to long-term nurture, reduce investment, consider disqualifying. |

---

## Scoring Weights

Default weights are provided below. These are configurable per business to match their sales motion.

### Health Score Weights

| Component | Default Weight | Adjustment Guidance |
|-----------|---------------|-------------------|
| Deal Progression Velocity | 25% | Increase for transactional sales; decrease for enterprise |
| Activity Recency | 25% | Increase if your sales cycle is fast; decrease for long cycles |
| Engagement Depth | 20% | Increase for complex, multi-stakeholder deals |
| Stakeholder Coverage | 15% | Increase for enterprise; decrease for SMB self-serve |
| BANT Completeness | 15% | Increase for high-ticket deals; decrease for low-touch sales |

### Intent Score Weights

| Component | Default Weight | Adjustment Guidance |
|-----------|---------------|-------------------|
| Website Visits | 20% | Increase for PLG companies; decrease for sales-led outbound |
| Content Consumption | 20% | Increase if content marketing is a primary channel |
| Feature Usage | 20% | Increase for product-led growth; decrease if no trial/freemium |
| Meeting Frequency | 20% | Increase for enterprise sales-led motion |
| Email Engagement | 20% | Increase for outbound-heavy teams |

### Weight Recalibration

Recalibrate weights quarterly by analyzing:
1. Which components most strongly correlated with won deals?
2. Which components most strongly correlated with lost deals?
3. Are there components with no predictive value? (Consider removing or replacing.)

Use logistic regression on historical deal data to optimize weights empirically.

# Account-Based Engagement

Reference for account-level lifecycle management: stages, health scoring, buying committee roles, multi-threading, engagement strategies, intent signals, expansion indicators, and churn risk detection.

---

## Account Lifecycle Stages

| Stage | Description | Entry Criteria | Exit Criteria |
|-------|-------------|---------------|---------------|
| **Prospect** | Account identified as a potential customer. No revenue relationship. | Matches ICP, added to target account list | Signs contract (→ Customer Active) or disqualified (→ Disqualified) |
| **Customer Active** | Paying customer with healthy engagement and usage. | Contract signed, onboarding complete | Health score drops below 40 (→ Customer At Risk) or contract lapses (→ Customer Churned) |
| **Customer At Risk** | Paying customer showing declining engagement or satisfaction signals. | Health score < 40, or 2+ churn risk indicators present | Health score recovers above 60 (→ Customer Active) or contract expires without renewal (→ Customer Churned) |
| **Customer Churned** | Former customer who did not renew or explicitly cancelled. | Non-renewal, cancellation, or contract expiration | Re-engagement and new contract (→ Customer Active) |
| **Disqualified** | Account does not match ICP or was evaluated and rejected. | Failed qualification, bad fit, fraud, or explicit disinterest | Re-evaluation if circumstances change (→ Prospect) |

### Stage Transition Diagram

```
Prospect → Customer Active → Customer At Risk → Customer Churned
    ↓                ↑               ↑                    ↓
Disqualified    (recovery)     (recovery)          (re-engagement)
                                                         ↓
                                                   Customer Active
```

---

## Account Health Scoring

### Health Categories

| Category | Score Range | Color | Description |
|----------|-----------|-------|-------------|
| **Healthy** | 70-100 | Green | Strong engagement, high adoption, positive signals |
| **Watch** | 40-69 | Yellow | Some concerning signals; needs attention before it deteriorates |
| **At Risk** | 0-39 | Red | Multiple risk factors present; urgent intervention required |

### Health Score Components

| Component | Weight | What It Measures |
|-----------|--------|-----------------|
| **Product Adoption** | 30% | Feature breadth, usage depth, DAU/MAU ratio, activation milestones |
| **Engagement Recency** | 25% | Last login, last support interaction, last meeting with CSM, last product event |
| **Support Ticket Sentiment** | 20% | Ticket volume trend, resolution satisfaction, severity distribution, escalation rate |
| **Expansion Signals** | 15% | New use cases explored, additional seats requested, upgrade inquiries, API usage growth |
| **Contract Status** | 10% | Time to renewal, payment history, contract value trend, multi-year vs. month-to-month |

### Product Adoption (0-30)

| Adoption Level | Score | Indicators |
|---------------|-------|------------|
| Deep | 27-30 | Using 80%+ features, daily usage, multiple teams, API integrations |
| Strong | 21-26 | Using 60-80% features, weekly usage, multiple users |
| Moderate | 15-20 | Using 40-60% features, regular but not daily usage |
| Light | 8-14 | Using 20-40% features, sporadic usage |
| Minimal | 1-7 | Basic features only, infrequent logins |
| None | 0 | No product usage detected |

### Engagement Recency (0-25)

| Last Meaningful Interaction | Score |
|----------------------------|-------|
| Within 3 days | 25 |
| Within 7 days | 20 |
| Within 14 days | 15 |
| Within 30 days | 10 |
| Within 60 days | 5 |
| More than 60 days | 0 |

### Support Ticket Sentiment (0-20)

| Sentiment Profile | Score |
|------------------|-------|
| Low volume, fast resolution, positive CSAT | 20 |
| Moderate volume, good resolution, mixed CSAT | 15 |
| Moderate volume, slow resolution or unresolved tickets | 10 |
| High volume, escalations, negative CSAT | 5 |
| Critical escalations, executive complaints | 0 |

### Expansion Signals (0-15)

| Signal Strength | Score |
|----------------|-------|
| Active expansion discussion, upgrade in progress | 15 |
| Exploring new use cases, inquiring about higher tiers | 12 |
| Growing usage toward plan limits | 9 |
| Stable usage, no expansion signals | 5 |
| Declining usage | 0 |

### Contract Status (0-10)

| Status | Score |
|--------|-------|
| Multi-year contract, expanding | 10 |
| Annual contract, auto-renew, on time payments | 8 |
| Annual contract, renewal 60+ days away | 6 |
| Annual contract, renewal < 60 days, no commitment signal | 4 |
| Month-to-month, or late payments | 2 |
| Contract expired or cancellation requested | 0 |

---

## Buying Committee Roles

### Role Definitions

| Role | Description | Engagement Priority | Key Concerns |
|------|-------------|-------------------|-------------|
| **Champion** | Internal advocate who actively pushes for your solution. Has personal motivation and organizational influence. | Critical — nurture and arm with internal selling tools | "How does this make me look good?" "How do I build the business case?" |
| **Economic Buyer** | Person with signing authority and budget control. Makes the final financial decision. | High — need their buy-in for deal to close | ROI, total cost of ownership, risk, strategic alignment |
| **Technical Evaluator** | Assesses technical fit, integration requirements, security, and implementation feasibility. | High — can veto on technical grounds | API capabilities, security, data model, integration, scalability |
| **End User** | Day-to-day user of the product. Their adoption determines success. | Medium — ensure usability and value realization | Ease of use, workflow fit, learning curve, daily value |
| **Blocker** | Stakeholder who resists the purchase. May be attached to incumbent solution, skeptical of change, or have competing priorities. | High — identify and neutralize or convert early | Disruption, risk, learning curve, political implications |

### Engagement Approach per Role

| Role | Communication Style | Content Types | Meeting Approach |
|------|-------------------|---------------|-----------------|
| Champion | Collaborative, empowering | Battle cards, ROI templates, internal pitch decks | Regular 1:1s, arm with ammunition |
| Economic Buyer | Executive, concise, ROI-focused | Executive summaries, business cases, peer references | Exec-to-exec meetings, board-ready materials |
| Technical Evaluator | Technical, detailed, honest about limitations | API docs, architecture diagrams, security whitepapers, sandbox access | Technical deep dives, POC support |
| End User | Practical, empathetic, user-focused | Product tours, training materials, quick-start guides | Hands-on workshops, user feedback sessions |
| Blocker | Respectful, empathetic, address concerns directly | Competitive comparisons, risk mitigation plans, transition guides | Dedicated concern-addressing sessions |

---

## Multi-Threading Assessment

Multi-threading = engaging multiple contacts at an account. Critical for deal resilience and acceleration.

### Threading Score

| Threads (Engaged Contacts) | Score | Risk Level |
|----------------------------|-------|------------|
| 5+ contacts across multiple roles | Strong | Low risk |
| 3-4 contacts across 2+ roles | Good | Moderate risk |
| 2 contacts (e.g., champion + evaluator) | Adequate | Elevated risk |
| 1 contact only (single-threaded) | Weak | High risk — deal depends on one person |
| 0 active contacts | Critical | Deal is dead; re-engagement needed |

### Multi-Threading Strategies

| Strategy | Description | When to Use |
|----------|-------------|-------------|
| **Champion expansion** | Ask champion to introduce you to other stakeholders | After champion is committed and confident |
| **Content-based threading** | Share relevant content tagged to specific roles | Ongoing — use industry reports for execs, technical docs for evaluators |
| **Event-based threading** | Invite multiple contacts to webinars, dinners, conferences | During consideration/evaluation phase |
| **Referral threading** | Leverage existing contacts at the account to introduce you to new teams | When entering new departments or business units |
| **Executive threading** | Have your executive reach out to their executive | When deal is stalling or needs executive alignment |
| **Org chart mapping** | Systematically identify and reach every relevant stakeholder | At deal start; revisit quarterly for existing customers |

---

## Engagement Strategy Matrix: Stage x Role

| Stage | Champion | Economic Buyer | Technical Evaluator | End User |
|-------|----------|---------------|-------------------|----------|
| **Prospect** | Identify and develop. Share industry insights. Build relationship. | Map and plan approach. No direct outreach until champion engaged. | Identify through champion. Prepare technical materials. | Not yet engaged. |
| **Customer Active** | Regular check-ins. Share product roadmap. Seek feedback. | QBR presentations. ROI reviews. Expansion discussions. | Technical health checks. Integration support. | Training. Adoption support. Feature updates. |
| **Customer At Risk** | Urgent 1:1. Understand root cause. Co-create recovery plan. | Executive escalation. Remediation commitment. Retention offer if warranted. | Technical review. Address issues. Priority support. | Usability improvements. Re-training. Quick wins. |
| **Customer Churned** | Maintain relationship. Share relevant updates quarterly. | Annual check-in with new value prop or company news. | No active engagement. | No active engagement. |

---

## Intent Signals at Account Level

### Website Traffic Patterns

| Signal | Intent Level | Description |
|--------|-------------|-------------|
| Pricing page visits from multiple IPs | Very High | Multiple people at the account evaluating pricing |
| Repeat visits to product/feature pages | High | Active evaluation of specific capabilities |
| Documentation/API page visits | High | Technical evaluation underway |
| Blog/resource visits | Medium | Early research and education phase |
| Single visit, bounce | Low | Casual interest at best |

### Content Consumption

| Signal | Intent Level | Description |
|--------|-------------|-------------|
| Downloaded buyer's guide + ROI calculator | Very High | Active buying process |
| Attended product webinar | High | Committed time to learn about solution |
| Read case study from their industry | High | Looking for validation |
| Read 3+ blog posts in a week | Medium | Research mode |
| Opened 1 email, no further engagement | Low | Passive awareness |

### Feature Adoption Rate

| Signal | Intent Level | Description |
|--------|-------------|-------------|
| Rapid feature adoption (5+ features in first week) | Very High | Seriously evaluating, likely building internal case |
| Moderate adoption (3-4 features in first 2 weeks) | High | Engaged evaluation |
| Slow adoption (1-2 features in first month) | Medium | Exploring but not committed |
| Created account but no feature usage | Low | Signed up out of curiosity |
| Account created > 30 days ago, no login | None | Dead trial |

### Meeting Frequency

| Signal | Intent Level |
|--------|-------------|
| Weekly or more frequent meetings | Very High |
| Biweekly meetings | High |
| Monthly meetings | Medium |
| Quarterly meetings | Low |
| No meetings in 90+ days | None |

### Email Engagement

| Signal | Intent Level |
|--------|-------------|
| Replying, asking questions, forwarding to colleagues | Very High |
| Opening and clicking consistently | High |
| Opening but not clicking | Medium |
| Sporadic opens | Low |
| Not opening | None |

---

## Account Expansion Indicators

Signals that an existing customer is ready for upsell, cross-sell, or expansion.

| Indicator | Expansion Type | Action |
|-----------|---------------|--------|
| **Usage approaching plan limits** | Upsell (higher tier) | Proactive upgrade discussion before they hit limits |
| **New use case exploration** | Cross-sell (new product/module) | Discovery call about the new use case, demonstrate fit |
| **Additional team members** | Seat expansion | Offer team training, volume pricing discussion |
| **Positive NPS (9-10)** | Referral + expansion | Ask for referral, introduce expansion options |
| **API usage growth** | Platform expansion | Technical expansion discussion, integration support |
| **Requesting features from higher tier** | Upsell | Show ROI of upgrading, offer trial of premium features |
| **New department adoption** | Land-and-expand | Department-specific demo, new champion development |
| **Increased login frequency** | Deepening engagement | Share advanced feature guides, offer power-user training |
| **Multi-year contract interest** | Commitment expansion | Offer discount for longer commitment, lock in renewal |

### Expansion Playbook

```
1. Detect expansion signal (automated via product usage data or manual via CSM observation)
2. Validate the signal (is it a real expansion need or just noise?)
3. Identify the right stakeholder for expansion conversation
4. Prepare expansion-specific value proposition
5. Schedule expansion discovery call
6. Present tailored proposal with ROI
7. Negotiate and close expansion
8. Onboard the expansion (new features, users, or departments)
```

---

## Real-World Account Health Benchmarks (2024–2025)

Sourced from Gainsight, ChurnZero, Totango, and Pendo benchmarks.

### Account Health Distribution

In a typical B2B SaaS customer base, health scores cluster in predictable bands:

| Health Band | Typical % of Accounts | Revenue Risk | Action |
|-------------|----------------------|-------------|--------|
| Healthy (70-100) | 45–60% | Low | Prioritize expansion plays |
| Watch (40-69) | 25–35% | Medium | Proactive check-ins, engagement campaigns |
| At Risk (0-39) | 10–20% | High | Immediate intervention required |

Source: Gainsight 2024 Customer Success Benchmark Report (n=500+ CS teams).

### Churn Prediction Windows

| Signal | Average Days to Churn | Source |
|--------|----------------------|--------|
| No login for 21+ days | 45–60 days | Pendo 2024 |
| Support escalation (critical) | 30–45 days | Gainsight 2024 |
| Declining feature usage (3 consecutive weeks) | 60–90 days | Amplitude 2024 |
| NPS drop below 6 | 90–120 days | ChurnZero 2024 |
| Champion departure | 30–90 days | Gainsight 2024 |

**Key insight from Pendo 2024:** 20–30% of your active customer base shows early churn signals at any given moment. The accounts that get proactive outreach before they reach the 60-day no-login mark renew at 2.3x the rate of those reached after.

### Expansion Revenue Benchmarks

| Metric | SMB | Mid-Market | Enterprise | Source |
|--------|-----|-----------|-----------|--------|
| % of ARR from expansion | 15–25% | 25–40% | 35–55% | SaaS Capital 2024 |
| Upsell close rate | 30–40% | 40–50% | 45–55% | Gainsight 2024 |
| Cross-sell attach rate | 15–25% | 20–30% | 25–40% | Gainsight 2024 |
| Expansion ARR growth (healthy) | 20–30% YoY | 30–45% YoY | 40–60% YoY | ChartMogul 2024 |
| Avg months to first expansion | 9–12 | 6–9 | 12–18 | Totango 2024 |

### Customer Success Impact on Retention

| CS Coverage Model | Net Retention Rate | Gross Revenue Churn | Source |
|------------------|-------------------|--------------------|-|
| No CS (product-led only) | 94–100% | 10–18% | Gainsight 2024 |
| Reactive CS (ticket-driven) | 99–104% | 8–12% | Gainsight 2024 |
| Proactive CS (health score-driven) | 104–110% | 5–8% | Gainsight 2024 |
| High-touch enterprise CS | 110–125% | 3–5% | Gainsight 2024 |

## Churn Risk Indicators

Signals that a customer may not renew or may cancel.

| Indicator | Severity | Detection Method |
|-----------|----------|-----------------|
| **Declining usage** (week-over-week decrease for 3+ weeks) | High | Product analytics — DAU/WAU trends |
| **Support escalations** (2+ escalations in 30 days) | High | Support ticket data — severity and escalation flags |
| **Competitor evaluation** (visiting competitor sites, asking about alternatives) | High | Intent data, direct mentions in conversations |
| **Contract renewal approaching** (< 60 days) with no renewal signal | High | CRM contract data |
| **Champion departure** (key contact left the company) | Critical | LinkedIn monitoring, email bounces, direct notification |
| **Payment issues** (late payments, disputed invoices) | Medium-High | Billing system data |
| **Declining NPS/CSAT** (score dropped by 2+ points) | Medium | Survey data trends |
| **Reduced meeting frequency** (CSM check-ins declined or cancelled) | Medium | Calendar data |
| **Feature requests not addressed** (3+ outstanding requests > 90 days) | Medium | Product feedback system |
| **Organizational change** (merger, acquisition, leadership change) | Medium | News monitoring, direct communication |
| **Budget cuts announced** | High | News, direct communication |
| **Low adoption of new features** (not using features released in last 6 months) | Low-Medium | Product analytics |

### Churn Prevention Framework

```
Early Warning (health 40-69):
  → CSM proactive check-in within 48 hours
  → Review usage data and identify engagement gaps
  → Create re-engagement plan with specific milestones

Urgent Risk (health 20-39):
  → Escalate to CSM manager
  → Executive-to-executive outreach
  → Offer remediation: dedicated support, training, customization
  → Create 30-day recovery plan with weekly checkpoints

Critical Risk (health 0-19):
  → VP/C-level escalation
  → Retention offer if warranted (discount, contract flexibility)
  → Post-mortem if churn is likely — capture learnings
  → Begin transition planning (graceful offboarding)
```

# Marketing and Sales Automation Patterns

Reference for workflow patterns: lead routing, nurture, cart abandonment, onboarding, churn prevention, deal sync, event follow-up. Includes trigger types, action types, error handling, rate limiting, and integration patterns.

---

## Workflow Pattern Library

### 1. Lead Routing

Routes new leads to the appropriate owner based on lead score, company size, and segment.

```
New Lead Event
    ↓
Score Lead (fit + activity + intent)
    ↓
┌─────────────────────────────────────────┐
│  IF score >= 80 AND company_size > 500  │ → Assign to Enterprise AE
│  IF score >= 60 AND company_size > 50   │ → Assign to Mid-Market AE
│  IF score >= 40 AND company_size <= 50  │ → Assign to SMB SDR
│  IF score < 40                          │ → Enroll in Nurture Sequence
│  IF geographic_match == false           │ → Assign to Partner Channel
└─────────────────────────────────────────┘
    ↓
Notify Owner (Slack + Email)
    ↓
Create CRM Task: "Follow up within 24h"
    ↓
Update Lead Status: "Routed"
```

**Configuration:**
| Parameter | Default | Notes |
|-----------|---------|-------|
| Scoring model | Fit (40%) + Activity (30%) + Intent (30%) | Configurable weights |
| Enterprise threshold | Score >= 80, company_size > 500 | Adjust per market |
| Round-robin assignment | Within team, sequential | Respect capacity limits |
| Notification channel | Slack + email to owner | Add mobile push for high-value |
| SLA for follow-up | 24 hours (enterprise: 4 hours) | Create escalation if missed |

### 2. Lead Nurture

Moves MQLs through an educational sequence toward SQL threshold.

```
MQL Created Event
    ↓
Wait 1 day
    ↓
Email 1: Educational content (industry insight)
    ↓
Wait 3 days
    ↓
Check: Did they engage? (opened/clicked)
    ├── YES → Email 2A: Case study (relevant industry)
    └── NO  → Email 2B: Different angle (pain-point focused)
    ↓
Wait 4 days
    ↓
Email 3: Comparison guide or ROI calculator
    ↓
Wait 3 days
    ↓
Check: Score >= SQL threshold?
    ├── YES → Notify Sales + Create Opportunity + Exit nurture
    └── NO  → Continue nurture
    ↓
Wait 5 days
    ↓
Email 4: Webinar invitation or demo offer
    ↓
Wait 7 days
    ↓
Check: Score >= SQL threshold?
    ├── YES → Notify Sales + Create Opportunity + Exit nurture
    └── NO  → Move to long-term nurture (monthly digest)
```

**Configuration:**
| Parameter | Default | Notes |
|-----------|---------|-------|
| SQL score threshold | 70 | Based on BANT completeness + engagement |
| Sequence length | 4-6 emails over 21-28 days | Adjust based on sales cycle |
| Content selection | Industry + persona-based | Use recommendation engine |
| Exit conditions | Score threshold OR manual removal OR unsubscribe | Multiple exit paths |
| Re-entry cooldown | 90 days | Prevent nurture fatigue |

### 3. Cart Abandonment

Recovers abandoned shopping carts through a multi-channel timed sequence.

```
Cart Abandoned Event (no purchase within 30 min)
    ↓
Wait 1 hour
    ↓
Check: Did they complete purchase?
    ├── YES → Exit (no action needed)
    └── NO  → Continue
    ↓
Email 1: "You left items in your cart" (show cart contents, direct link)
    ↓
Wait 24 hours
    ↓
Check: Did they complete purchase?
    ├── YES → Exit
    └── NO  → Continue
    ↓
Email 2: "Still thinking it over?" (add social proof, limited stock warning)
    ↓
Wait 48 hours
    ↓
Check: Did they complete purchase?
    ├── YES → Exit
    └── NO  → Continue
    ↓
SMS: "Your cart is waiting! Complete your order: [link]" (if SMS opted in)
    ↓
Wait 24 hours
    ↓
Check: Cart value > $50?
    ├── YES → Email 3: Incentive (10% discount code, 48h expiry)
    └── NO  → Email 3: Final reminder (urgency, no discount)
    ↓
Wait 72 hours
    ↓
Exit (mark cart as abandoned-final)
```

**Configuration:**
| Parameter | Default | Notes |
|-----------|---------|-------|
| Abandon threshold | 30 minutes with no activity | Configurable per business |
| Discount trigger | Cart value > $50 | Adjust based on margin |
| Discount amount | 10% | Test 5%, 10%, 15% |
| Max sequence duration | 7 days | After 7 days, diminishing returns |
| Frequency cap | 1 cart recovery sequence per 14 days per user | Prevent annoyance |

### 4. Onboarding

Guides new users from signup to activation through a progressive sequence.

```
Signup Event
    ↓
Email 1: Welcome + quick-start guide (immediate)
    ↓
Wait 1 day
    ↓
Check: Completed setup?
    ├── YES → Email 2A: "Great start! Here's your next step" (feature highlight)
    └── NO  → Email 2B: "Need help getting started?" (setup guide + support link)
    ↓
Wait 2 days
    ↓
Check: Activated? (completed key action)
    ├── YES → Branch to Power User track
    │         → Email: Advanced tips + integrations
    └── NO  → Branch to Nurture track
              → Email: Benefits recap + demo offer
    ↓
Wait 2 days
    ↓
Push Notification: Feature tip (in-app)
    ↓
Wait 2 days (Day 7)
    ↓
Check: Still not activated?
    ├── YES (not activated) → Email: "Let us help" + book onboarding call CTA
    └── NO (activated)      → Email: "You're crushing it" + share/referral CTA
    ↓
Wait 7 days (Day 14)
    ↓
Check: Trial ending within 3 days?
    ├── YES → Email: Trial expiration reminder + upgrade CTA
    └── NO  → Continue product education
```

**Configuration:**
| Parameter | Default | Notes |
|-----------|---------|-------|
| Activation event | First [key action] completed | Define per product |
| Setup steps | Account profile, first integration, first campaign | Customize to product |
| Onboarding call threshold | Not activated by Day 7 | Offer human help |
| Trial expiration notice | 3 days before expiry | Include upgrade CTA |

### 5. Churn Prevention

Detects at-risk accounts and triggers intervention workflows.

```
Health Score Drops Below 40 (trigger)
    ↓
Alert CSM (Slack + email, immediate)
    ↓
Create CRM Task: "Review account health" (due: 24h)
    ↓
Wait 2 days
    ↓
Check: CSM has taken action?
    ├── YES → Monitor (check health weekly)
    └── NO  → Escalate to CSM Manager
    ↓
Trigger Retention Journey:
    ↓
Email: "We noticed you haven't been active" (personalized, from CSM)
    ↓
Wait 3 days
    ↓
Check: Re-engagement detected?
    ├── YES → Update health score + continue monitoring
    └── NO  → Continue intervention
    ↓
Email: Value reminder + new feature highlight
    ↓
Wait 5 days
    ↓
Check: Re-engagement detected?
    ├── YES → Update health score + continue monitoring
    └── NO  → Escalate to VP CS
    ↓
VP CS outreach: Personal call or meeting
    ↓
Wait 7 days
    ↓
Check: Health recovered?
    ├── YES → Return to normal monitoring
    └── NO  → Prepare for potential churn (renewal offer, migration support)
```

### 6. Deal Stage Sync

Keeps lifecycle stage and CRM stage aligned bidirectionally.

```
CRM Deal Stage Change Event
    ↓
Map CRM stage to lifecycle stage:
    ├── Prospecting    → Lifecycle: Prospect
    ├── Qualification  → Lifecycle: Prospect
    ├── Discovery/Demo → Lifecycle: Promising
    ├── Proposal       → Lifecycle: Promising
    ├── Negotiation    → Lifecycle: Promising
    ├── Won            → Lifecycle: Customer Active (New Customer)
    └── Lost           → Lifecycle: (no change, flag for nurture)
    ↓
Update person lifecycle stage
    ↓
Trigger appropriate journey for new stage:
    ├── Won → Trigger onboarding journey
    └── Lost → Trigger re-engagement nurture (after 90 days)
    ↓
Update account record with deal outcome
    ↓
Notify relevant teams (Slack)
```

### 7. Event Follow-Up

Segments event attendees by engagement level and delivers personalized follow-up.

```
Event Ends (trigger: scheduled)
    ↓
Segment attendees:
    ├── High engagement: attended 80%+ sessions, visited booth, asked questions
    ├── Medium engagement: attended 50-80% sessions
    └── Low engagement: registered but attended < 50% or no-show
    ↓
[High Engagement Path]
    Email 1 (Day 0): Personal thank you + exclusive resource
    Wait 2 days
    Email 2: "Let's continue the conversation" + meeting link
    Wait 3 days
    Phone: Discovery call from assigned AE
    ↓
[Medium Engagement Path]
    Email 1 (Day 0): Thank you + session recordings
    Wait 3 days
    Email 2: Key takeaways + related content
    Wait 5 days
    Email 3: Case study + soft CTA
    ↓
[Low Engagement / No-Show Path]
    Email 1 (Day 1): "Sorry we missed you" + recordings
    Wait 5 days
    Email 2: Highlight reel + future event invitation
```

---

## Trigger Types

| Trigger Type | Description | Examples |
|-------------|-------------|---------|
| **Event-based** | Fires when a user performs a specific action | Page view, form submit, purchase, feature usage, cart abandon |
| **Schedule-based** | Fires on a cron schedule | Daily digest, weekly report, monthly review, quarterly check-in |
| **Webhook** | Fires when an external system sends a webhook | CRM update, payment event, support ticket, third-party integration |
| **Manual** | Fires when a team member explicitly triggers | One-off campaigns, ad-hoc outreach, escalation actions |
| **Score threshold** | Fires when a behavioral score crosses a threshold | Lead score >= 70, health score < 40, intent level changes to "High" |
| **Attribute change** | Fires when a user attribute changes value | Lifecycle stage change, plan change, role change |
| **Time-based (relative)** | Fires relative to a user event | 30 days after signup, 7 days before contract renewal |
| **Segment membership** | Fires when a user enters or exits a segment | Enters "High Value" segment, exits "Active" segment |

---

## Action Types

| Action | Description | Parameters |
|--------|-------------|-----------|
| **Send message** | Send email, SMS, or push notification | Channel, template, personalization variables |
| **Update attribute** | Modify a user or account attribute | Entity (person/account), attribute name, value, operation (set/increment/append) |
| **Create task** | Create a task in CRM or project management tool | Assignee, title, description, due date, priority |
| **Notify team** | Send notification via Slack, email, or other channel | Channel, recipients, message template |
| **Call webhook** | Make HTTP request to external URL | URL, method, headers, body, timeout |
| **Wait** | Pause workflow for a duration or until condition | Duration or condition (event + timeout) |
| **Branch** | Split workflow based on condition | Condition (filter DSL), positive path, negative path |
| **Score update** | Recalculate or modify a behavioral score | Score type, adjustment amount or recalculation trigger |
| **Segment update** | Add or remove user from a segment | Segment ID, operation (add/remove) |
| **Enroll in journey** | Add user to another journey or sequence | Journey ID, entry conditions |
| **Remove from journey** | Remove user from an active journey | Journey ID |
| **Log event** | Record a custom event for analytics | Event name, properties |

---

## Error Handling

### Retry Logic

```
Retry Strategy: Exponential Backoff

Attempt 1: Immediate
Attempt 2: Wait 30 seconds
Attempt 3: Wait 2 minutes (max)

Formula: delay = min(base_delay × 2^(attempt-1), max_delay)
  base_delay = 30 seconds
  max_delay  = 120 seconds
  max_attempts = 3
```

### Error Categories and Handling

| Error Type | Examples | Handling |
|-----------|---------|---------|
| **Transient** | Network timeout, rate limit, temporary 5xx | Retry with exponential backoff (up to 3 attempts) |
| **Permanent** | Invalid email (hard bounce), malformed data, 4xx client error | Do not retry. Log error. Notify admin. Move to dead letter queue. |
| **Partial** | Some items in a batch succeeded, others failed | Retry only failed items. Log partial success. |
| **Rate Limited** | Too many requests to external API | Respect retry-after header. Queue and resume. |
| **Timeout** | Webhook destination did not respond within timeout | Retry once. If still failing, skip and alert. |

### Fallback Actions

When all retries are exhausted:

```
1. Log the failure with full context (workflow ID, step, error, payload)
2. Send admin notification (Slack/email to workflow owner)
3. Move to dead letter queue for manual review
4. Mark the user's workflow step as "failed" with error reason
5. Continue the workflow on the next step (if configured for non-blocking)
   OR halt the workflow (if configured for blocking/critical)
```

### Dead Letter Queue

Failed actions are stored in a dead letter queue with:
- Original payload
- Error message and stack trace
- Retry count and timestamps
- Workflow and step identifiers
- User/account identifiers

DLQ items can be manually retried, discarded, or investigated.

---

## Rate Limiting

### Per-User Rate Limits

| Action Type | Default Limit | Period | Rationale |
|------------|--------------|--------|-----------|
| Email sends | 5 | Per week | Prevent inbox fatigue |
| SMS sends | 4 | Per month | High cost + compliance |
| Push notifications | 3 | Per week | Prevent permission revocation |
| Webhook calls | 100 | Per hour | Prevent target system overload |
| Attribute updates | 50 | Per hour | Prevent data thrashing |
| Total messages (all channels) | 10 | Per week | Cross-channel coordination |

### System-Level Rate Limits

| Resource | Limit | Notes |
|----------|-------|-------|
| Workflow executions | 1,000/min per workspace | Burst handling with queue |
| Email sends | 10,000/hour per workspace | ISP warmup may require lower limits initially |
| SMS sends | 1,000/hour per workspace | Carrier-dependent limits |
| Webhook outbound | 500/min per destination | Per-destination rate limiting |
| API calls | 100/sec per workspace | Standard API rate limiting |

### Batch Processing

For bulk operations:
- Batch size: 100-1,000 items per batch
- Inter-batch delay: 1-5 seconds
- Progress tracking via metadata
- Partial failure handling (continue on individual item failure)

---

## Integration Patterns

### CRM Sync (Bidirectional)

```
Intempt → CRM:
  - Lifecycle stage changes → Update CRM contact status
  - Lead score changes → Update CRM lead score field
  - Activity events → Create CRM activities
  - New contacts → Create CRM contacts
  
CRM → Intempt:
  - Deal stage changes → Update lifecycle stage
  - Contact field updates → Sync person attributes
  - Task completion → Trigger next workflow step
  - New deals → Create engagement record
```

**Conflict resolution:**
- Most recent write wins (by timestamp)
- CRM is system of record for deal data
- Intempt is system of record for behavioral data
- Sync frequency: near real-time via webhooks, with hourly reconciliation batch

### Slack Notification (One-Way)

```
Triggers → Slack:
  - High-value lead created → #sales-alerts
  - Account health drops to At Risk → #cs-alerts
  - Deal closed → #wins
  - Experiment winner declared → #marketing-updates
  - Workflow error → #ops-alerts
```

**Message format:**
```
[Priority Icon] [Event Type]
Account: {{account_name}}
Contact: {{person_name}} ({{person_email}})
Details: {{event_details}}
Action: {{recommended_action}}
[Link to Intempt dashboard]
```

### Webhook Callbacks (Async)

For long-running external processes:

```
1. Intempt sends webhook to external system
2. External system responds with 202 Accepted + callback_id
3. Intempt pauses workflow step, waiting for callback
4. External system processes request
5. External system calls Intempt callback URL with result
6. Intempt resumes workflow with result data
7. If no callback within timeout → trigger fallback action
```

**Callback timeout:** Default 24 hours, configurable per webhook step.

### Data Warehouse Sync

```
Intempt → Warehouse:
  - Event stream → Raw events table (real-time or 15-min batch)
  - Person profiles → Person dimension table (hourly)
  - Campaign metrics → Campaign facts table (daily)
  
Warehouse → Intempt:
  - Enrichment data → Person attribute updates (daily batch)
  - Custom scores → Score imports (daily)
  - Segments → External segment definitions (daily)
```

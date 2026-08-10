# Multi-Channel Journey Node Types

Intempt journeys are directed acyclic graphs of nodes. Each node has a type, configuration, and links to other nodes. This reference covers every node type, linking conventions, channel guardrails, holdout controls, and risk classification.

---

## Node Types

### Trigger

The entry point of a journey. Defines who enters and when.

| Field | Type | Description |
|-------|------|-------------|
| `type` | `"trigger"` | Fixed |
| `filterDsl` | Object | Filter DSL using `$or`, `$and`, `$not`, `$event`, `$userAttribute` operators |
| `recurring` | Boolean | Whether users can re-enter the journey (default: false) |
| `entryLimit` | Number | Max users who can enter (null = unlimited) |
| `schedule` | Object | Optional cron-based schedule for batch entry evaluation |

**Filter DSL Structure:**
```json
{
  "$and": [
    { "$event": { "name": "page_viewed", "property": "url", "operator": "contains", "value": "/pricing" } },
    { "$userAttribute": { "name": "lifecycle_stage", "operator": "=", "value": "Promising" } }
  ]
}
```

**Operators in Filter DSL:**
- `$or` — Any child condition matches
- `$and` — All child conditions match
- `$not` — Negates the child condition
- `$event` — Matches on event name + property + operator + value
- `$userAttribute` — Matches on user attribute + operator + value

### Delay

Pauses the journey for a specified duration before proceeding to the next node.

| Field | Type | Description |
|-------|------|-------------|
| `type` | `"delay"` | Fixed |
| `duration` | String | Wait period in shorthand: `"3d"`, `"2h"`, `"30m"`, `"1d12h"` |
| `businessHoursOnly` | Boolean | If true, only counts business hours (9am-5pm Mon-Fri) |

**Duration format:**
- `d` = days
- `h` = hours
- `m` = minutes
- Combinations allowed: `"1d12h30m"` = 1 day, 12 hours, 30 minutes

### Wait-Until

Pauses the journey until a specific event occurs or a timeout is reached.

| Field | Type | Description |
|-------|------|-------------|
| `type` | `"wait_until"` | Fixed |
| `eventFilter` | Object | Filter DSL defining the awaited event |
| `timeout` | String | Maximum wait duration (e.g., `"7d"`). After timeout, proceeds via the negative path. |

**Behavior:**
- If the event matches before timeout: proceeds via **positive** output
- If timeout expires without event: proceeds via **negative** output
- Useful for: "wait for purchase within 3 days, otherwise send reminder"

### Email

Sends an email message to the person in the journey.

| Field | Type | Description |
|-------|------|-------------|
| `type` | `"email"` | Fixed |
| `templateId` | String | Reference to the email template |
| `subject` | String | Email subject line. Supports Liquid: `{{person.first_name}}` |
| `body` | String | HTML body content. Supports Liquid personalization. |
| `senderName` | String | Display name of the sender (e.g., "Sarah from Acme") |
| `senderEmail` | String | From address (must be verified domain) |
| `replyTo` | String | Reply-to address (optional) |
| `preheader` | String | Preview text (40-130 characters) |

**Liquid Personalization Variables:**
- `{{person.first_name}}` — First name
- `{{person.last_name}}` — Last name
- `{{person.email}}` — Email address
- `{{person.company}}` — Company name
- `{{person.lifecycle_stage}}` — Current lifecycle stage
- `{{person.activity_score}}` — Activity score (0-100)
- `{{person.custom.*}}` — Any custom attribute
- `{% if person.lifecycle_stage == "Champions" %}...{% endif %}` — Conditional blocks

### SMS

Sends an SMS message.

| Field | Type | Description |
|-------|------|-------------|
| `type` | `"sms"` | Fixed |
| `body` | String | SMS text content. Max 160 chars GSM-7 or 70 chars Unicode. |
| `senderId` | String | Sender phone number or short code |
| `optOutMessage` | String | Appended opt-out text (e.g., "Reply STOP to unsubscribe") |
| `mediaUrl` | String | Optional MMS image URL |

**Compliance:** Every SMS must include opt-out instructions. The `optOutMessage` is automatically appended if not present in the body. Character count includes the opt-out text.

### Push

Sends a push notification (iOS, Android, Web).

| Field | Type | Description |
|-------|------|-------------|
| `type` | `"push"` | Fixed |
| `title` | String | Notification title (recommended 50 chars; truncated at ~65 on iOS) |
| `body` | String | Notification body (recommended 150 chars iOS / 240 chars Android) |
| `imageUrl` | String | Rich media image (1024x1024 iOS, 2:1 aspect Android) |
| `deepLink` | String | Deep link URL (scheme://path) |
| `fallbackUrl` | String | Web URL fallback if deep link fails |
| `actionButtons` | Array | Up to 3 action buttons, each with `label` and `action` |
| `sound` | String | Notification sound (default, custom, or silent) |
| `badge` | Number | Badge count to set (iOS only) |

### Condition

Binary branch node. Evaluates a filter DSL condition and routes to positive (true) or negative (false) children.

| Field | Type | Description |
|-------|------|-------------|
| `type` | `"condition"` | Fixed |
| `filterDsl` | Object | Filter DSL to evaluate against the current person |
| `positiveNodeId` | String | Node to execute if condition is true |
| `negativeNodeId` | String | Node to execute if condition is false |

**Children connect via `inputPath`:**
- `inputPath: "positive"` — the true branch
- `inputPath: "negative"` — the false branch

### Multi-Split

N-way branch node. Evaluates multiple conditions in priority order.

| Field | Type | Description |
|-------|------|-------------|
| `type` | `"multi_split"` | Fixed |
| `branches` | Array | Ordered list of `{ name, filterDsl, nodeId }` |
| `defaultNodeId` | String | Fallback node if no branch matches |

**Evaluation:** Conditions are evaluated top-to-bottom. The first matching branch is taken. If none match, the default branch is followed.

### Loop

Iterates over a list attribute and executes children for each item.

| Field | Type | Description |
|-------|------|-------------|
| `type` | `"loop"` | Fixed |
| `listAttribute` | String | Path to the list attribute (e.g., `"cart.items"`) |
| `itemVariable` | String | Variable name for the current item (e.g., `"item"`) |
| `maxIterations` | Number | Safety limit on iterations (default: 50) |

**Use case:** Iterate over products in a cart to send personalized recommendations per product.

### Update Attribute

Modifies a user or account attribute.

| Field | Type | Description |
|-------|------|-------------|
| `type` | `"update_attribute"` | Fixed |
| `target` | `"person"` or `"account"` | Which entity to update |
| `attribute` | String | Attribute name to set |
| `value` | Any | New value (string, number, boolean, or Liquid expression) |
| `operation` | String | `"set"`, `"increment"`, `"append"`, `"remove"` |

### Run Workflow

Triggers an external automation or sub-journey.

| Field | Type | Description |
|-------|------|-------------|
| `type` | `"run_workflow"` | Fixed |
| `workflowId` | String | ID of the workflow to trigger |
| `payload` | Object | Data to pass to the workflow |
| `waitForCompletion` | Boolean | Whether to block until the workflow completes |

### Webhook

Calls an external URL with configurable method, headers, and body.

| Field | Type | Description |
|-------|------|-------------|
| `type` | `"webhook"` | Fixed |
| `url` | String | Destination URL |
| `method` | String | HTTP method: `GET`, `POST`, `PUT`, `PATCH`, `DELETE` |
| `headers` | Object | Key-value pairs for HTTP headers |
| `body` | Object | JSON body (supports Liquid templating) |
| `timeout` | Number | Request timeout in milliseconds (default: 30000) |
| `retries` | Number | Number of retry attempts on failure (default: 3) |
| `successCodes` | Array | HTTP status codes considered success (default: [200, 201, 202, 204]) |

---

## Node Linking

Nodes are linked using three properties on each node:

| Property | Type | Description |
|----------|------|-------------|
| `previousId` | Number | 0-based index of the parent node in the journey's node array |
| `inputType` | String | `"default"` for standard flow |
| `inputPath` | String | `"default"`, `"positive"`, or `"negative"` — determines which output of the parent this node connects to |

**Linking rules:**
- The trigger node has no `previousId` (it is the root)
- Linear sequences use `inputPath: "default"`
- Condition nodes produce two outputs: children specify `inputPath: "positive"` or `inputPath: "negative"`
- Multi-split nodes produce N+1 outputs: branch children reference by branch index, default child uses `inputPath: "default"`
- Loop children reference the loop node and execute per iteration

---

## Channel Guardrails

Guardrails are per-channel thresholds that automatically pause journey steps or entire journeys when breached.

### Email Guardrails

| Metric | Warning | Pause | Action |
|--------|---------|-------|--------|
| Bounce rate | > 0.3% | > 0.5% | Pause email step, review list |
| Complaint rate | > 0.03% | > 0.05% | Pause email step immediately |
| Unsubscribe rate | > 0.3% | > 0.5% | Pause email step, review content |

### SMS Guardrails

| Metric | Warning | Pause | Action |
|--------|---------|-------|--------|
| Opt-out rate | > 0.15% | > 0.2% | Pause SMS step |
| Carrier rejection | > 0.5% | > 1.0% | Pause SMS step, review content |
| Delivery failure | > 3% | > 5% | Pause SMS step, review list |

### Push Guardrails

| Metric | Warning | Pause | Action |
|--------|---------|-------|--------|
| Permission revoke rate | > 0.15% | > 0.2% | Pause push step |
| Token error rate | > 1% | > 2% | Pause push step, refresh tokens |

---

## Holdout Controls

Each journey step can have an optional holdout — a percentage of users who reach that step but do not receive the treatment.

| Parameter | Range | Default |
|-----------|-------|---------|
| Per-step holdout percentage | 0-50% | 0% (no holdout) |
| Holdout assignment | Hash-based, deterministic per user per step | -- |

**Purpose:** Measures the incremental impact of individual journey steps. Users in the holdout proceed through the journey but skip the treatment (e.g., email is not sent), allowing comparison of downstream behavior.

**Analysis:** Compare conversion/engagement rates of holdout vs. treated users at each step to quantify incremental lift.

---

## Step Risk Classification

Each node type carries a risk classification that determines approval requirements and monitoring intensity.

| Risk Level | Node Types | Monitoring | Approval |
|------------|-----------|------------|----------|
| **Low** | Update Attribute, Delay, Wait-Until, Condition, Multi-Split, Loop | Standard logging | None required |
| **Medium** | Email, SMS, Push, Run Workflow | Guardrail monitoring, rate limiting | Optional review |
| **High** | Webhook | Full request/response logging, circuit breaker, alerting | Recommended review |

---

## Cross-Channel Timing

### Minimum Gap Between Channels

To avoid overwhelming users with messages across multiple channels in rapid succession:

| Channel Pair | Minimum Gap |
|-------------|-------------|
| Email → SMS | 4 hours |
| Email → Push | 2 hours |
| SMS → Email | 4 hours |
| SMS → Push | 2 hours |
| Push → Email | 1 hour |
| Push → SMS | 2 hours |
| Same channel → Same channel | 24 hours (configurable) |

### Frequency Capping Rules

Global frequency caps that apply across all journeys for a given person:

| Channel | Default Cap | Period | Override |
|---------|------------|--------|----------|
| Email | 5 messages | Per week | Configurable 1-14 per week |
| SMS | 4 messages | Per month | Configurable 1-8 per month |
| Push | 3 messages | Per week | Configurable 1-7 per week |
| All channels combined | 10 messages | Per week | Configurable |

**Cap behavior:** When a cap is reached, the message is suppressed (not delayed). The journey continues but the send step is skipped with a "frequency_capped" status.

**Priority override:** Messages marked as "transactional" (e.g., password reset, order confirmation) bypass frequency caps. Only marketing/engagement messages are capped.

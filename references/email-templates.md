# Email Campaign Design

Comprehensive reference for building effective email campaigns: structure, HTML constraints, personalization, subject lines, sequence timing, deliverability, A/B testing, and performance benchmarks.

---

## Email Structure

Every marketing email follows a consistent structural hierarchy:

### 1. Preheader (40-130 characters)

The preview text visible in inbox listings next to or below the subject line.

- **Purpose:** Extends the subject line, provides additional context to drive opens
- **Length:** 40-130 characters. Shorter preheaders risk showing body text as filler.
- **Best practices:**
  - Complement the subject line, do not repeat it
  - Include a benefit or curiosity hook
  - Use personalization where possible
  - Avoid starting with "View in browser" or administrative text

### 2. Header (Logo + Navigation)

The top section establishing brand identity.

- **Logo:** Max 200px wide, always linked to homepage
- **Navigation:** Optional. Keep to 3-4 links maximum. Common: Shop, New, Sale, Account
- **Background:** White or brand color. Consistent across all emails.
- **Height:** Keep under 100px to maximize visible content

### 3. Hero Section (Image + Headline)

The primary visual and messaging block, visible immediately upon open.

- **Hero image:** 600px wide, 200-400px tall. Compress to <150KB. Always include alt text.
- **Headline:** 6-10 words. Single key message. Large font (24-32px).
- **Subheadline:** Optional, 15-25 words. Supports the headline with a benefit or detail.
- **CTA button:** Primary action. High contrast. Minimum 44px tall, 120px wide.

### 4. Body Content

Supporting information, benefits, features, or product details.

- **Single column layout** for readability
- **2-3 content blocks** maximum per email
- **Short paragraphs:** 2-3 sentences each
- **Bullet points** for scannable benefits
- **Images:** Support the narrative. Inline, 560px max width.

### 5. CTA Block

Dedicated section for the primary call-to-action.

- **Button design:** Rounded corners (4-8px radius), padding (12-16px vertical, 24-40px horizontal)
- **Button text:** Action-oriented, 2-5 words ("Shop Now", "Start Free Trial", "Get the Guide")
- **Surrounding whitespace:** Minimum 20px above and below
- **Single CTA per block**, avoid competing actions

### 6. Footer

Required elements for compliance and trust.

- **Unsubscribe link:** Required by CAN-SPAM, GDPR, CASL. Must be prominent and functional.
- **Physical address:** Required by CAN-SPAM. Company name + street address.
- **Preference center link:** Let users manage frequency and content preferences
- **Social links:** Optional. Icon-based links to social profiles.
- **Legal text:** Privacy policy link, copyright notice

---

## HTML Constraints

Email HTML is severely constrained compared to web HTML. Follow these rules for maximum compatibility.

| Constraint | Specification |
|-----------|---------------|
| Max width | 600px (some clients clip wider emails) |
| CSS | Inline styles for maximum compatibility. Most modern clients support `<style>` blocks (Gmail, Apple Mail, Yahoo), but some older Outlook versions do not. Default to inline CSS for safety. |
| Layout | Table-based (`<table>`, `<tr>`, `<td>`). No flexbox, no grid. |
| Fonts | Web-safe fonts with fallbacks: `font-family: 'Helvetica Neue', Arial, sans-serif;` |
| Images | Absolute URLs only. Include `width`, `height`, `alt` attributes. Use `display: block;` to prevent gaps. |
| Background images | Unreliable. Use VML fallback for Outlook. Prefer solid colors. |
| Media queries | Supported by most mobile clients. Use for responsive stacking. |
| JavaScript | Not supported in any email client. |
| Forms | Not supported reliably. Link to hosted forms. |
| Video | Not embeddable. Use animated GIF or static image linking to video. |
| Max file size | Total HTML < 102KB (Gmail clips beyond this). Target < 80KB. |
| Dark mode | Test with and without. Use transparent PNGs. Provide `color-scheme: light dark;` meta. |

### Web-Safe Font Stack

```css
/* Primary options */
font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
font-family: Georgia, 'Times New Roman', Times, serif;
font-family: 'Courier New', Courier, monospace;

/* Google Fonts fallback pattern */
font-family: 'Open Sans', 'Helvetica Neue', Arial, sans-serif;
```

---

## Liquid Personalization Variables

### Standard Variables

| Variable | Description | Example Output |
|----------|-------------|----------------|
| `{{person.first_name}}` | First name | "Sarah" |
| `{{person.last_name}}` | Last name | "Chen" |
| `{{person.email}}` | Email address | "sarah@acme.com" |
| `{{person.company}}` | Company name | "Acme Corp" |
| `{{person.lifecycle_stage}}` | Current lifecycle stage | "Promising" |
| `{{person.activity_score}}` | Activity score | "72" |
| `{{person.fit_score}}` | Fit score | "85" |
| `{{person.intent_level}}` | Intent level | "High" |
| `{{person.city}}` | City | "San Francisco" |
| `{{person.industry}}` | Industry | "Technology" |
| `{{person.role}}` | Job role/title | "VP Marketing" |
| `{{person.created_at}}` | Account creation date | "2024-01-15" |
| `{{person.last_activity}}` | Last activity timestamp | "2024-03-20" |

### Conditional Blocks

```liquid
{% if person.lifecycle_stage == "Champions" %}
  As one of our top customers, you get exclusive early access.
{% elsif person.lifecycle_stage == "New Customers" %}
  Welcome! Here's what you need to know to get started.
{% else %}
  Here's what's new this month.
{% endif %}
```

### Default Values (Fallbacks)

```liquid
Hi {{ person.first_name | default: "there" }},
```

### Loops (for product recommendations, etc.)

```liquid
{% for product in recommended_products %}
  <tr>
    <td>{{ product.name }}</td>
    <td>{{ product.price | money }}</td>
  </tr>
{% endfor %}
```

### Filters

| Filter | Description | Example |
|--------|-------------|---------|
| `default` | Fallback value | `{{ person.first_name \| default: "there" }}` |
| `upcase` | Uppercase | `{{ person.first_name \| upcase }}` |
| `downcase` | Lowercase | `{{ person.email \| downcase }}` |
| `capitalize` | Capitalize first letter | `{{ person.city \| capitalize }}` |
| `truncate` | Limit length | `{{ person.company \| truncate: 20 }}` |
| `date` | Format date | `{{ person.created_at \| date: "%B %d, %Y" }}` |
| `money` | Format as currency | `{{ product.price \| money }}` |

---

## Subject Line Frameworks

### 1. Curiosity Gap

Creates an information gap that compels opening.

| Example | Why It Works |
|---------|-------------|
| "The metric most teams ignore (and why it matters)" | Implies insider knowledge |
| "We analyzed 10,000 campaigns. Here's what won." | Promises data-driven insight |
| "This one change doubled our reply rate" | Specificity + intrigue |

### 2. Benefit-Led

Leads with the direct value the reader will receive.

| Example | Why It Works |
|---------|-------------|
| "Cut your onboarding time in half" | Clear, measurable benefit |
| "3 templates to launch your next campaign today" | Actionable + immediate |
| "Save 5 hours/week on reporting" | Quantified benefit |

### 3. Urgency

Creates time pressure that motivates immediate action.

| Example | Why It Works |
|---------|-------------|
| "Last chance: early access closes tonight" | Deadline creates FOMO |
| "48 hours left to claim your discount" | Specific countdown |
| "Your trial expires tomorrow" | Personal urgency |

### 4. Personalization

Uses the recipient's data to create relevance.

| Example | Why It Works |
|---------|-------------|
| "{{person.first_name}}, your Q1 results are ready" | Name + relevant content |
| "What {{person.company}} can learn from [competitor]" | Company-specific |
| "Recommended for {{person.industry}} teams" | Industry relevance |

### 5. Question

Poses a question the reader wants answered.

| Example | Why It Works |
|---------|-------------|
| "Are you measuring the right engagement metrics?" | Triggers self-assessment |
| "What would you do with 10 more hours per week?" | Aspirational thinking |
| "Ready to automate your follow-ups?" | Qualifies interest |

### Subject Line Rules

- **Length:** 30-50 characters (6-10 words) for mobile-friendly display
- **Avoid spam triggers:** "FREE", "ACT NOW", all caps, excessive punctuation (!!!)
- **Emoji:** Use sparingly (0-1 per subject). Test performance, works in some industries, hurts in others.
- **Preview:** Always test rendering in Gmail, Apple Mail, Outlook mobile

---

## Sequence Timing Patterns

### Welcome Sequence

| Day | Email | Purpose |
|-----|-------|---------|
| 0 | Welcome + quickstart | Confirm signup, set expectations, one key action |
| 1 | Value delivery | Educational content, "here's how to get the most from X" |
| 3 | Social proof | Customer story, testimonial, results |
| 7 | Engagement check | "How's it going?" + resource links + CTA to next step |

### Nurture Sequence

| Day | Email | Purpose |
|-----|-------|---------|
| 3 | Educational content | Blog post, guide, or insight relevant to their segment |
| 7 | Case study | Proof that your solution works for similar companies |
| 14 | Comparison/evaluation | "How we compare" or "choosing the right solution" content |
| 21 | Soft CTA | Invite to demo, webinar, or free consultation |

### Win-Back Sequence

| Day | Email | Purpose |
|-----|-------|---------|
| 30 | "We miss you" | Acknowledge absence, highlight what's new |
| 45 | Incentive | Discount, extended trial, or exclusive offer |
| 60 | Last chance | Final attempt with stronger incentive + clear deadline |

### Onboarding Sequence

| Day | Email | Purpose |
|-----|-------|---------|
| 0 | Welcome + account setup | Credentials, first steps, support resources |
| 1 | Activation prompt | Guide to completing the key activation action |
| 3 | Feature highlight | Introduce the feature most correlated with retention |
| 5 | Integration/workflow | Show how to connect with their existing tools |
| 7 | Check-in + escalation | "Need help?" + offer a call/demo if not activated |

---

## Deliverability Checklist

### Authentication

- [ ] **SPF** (Sender Policy Framework): DNS TXT record authorizing sending IPs
- [ ] **DKIM** (DomainKeys Identified Mail): Cryptographic signature on outgoing emails
- [ ] **DMARC** (Domain-based Message Authentication): Policy for handling failed SPF/DKIM. Start with `p=none`, progress to `p=quarantine`, then `p=reject`.
- [ ] **BIMI** (Brand Indicators for Message Identification): Optional. Displays brand logo in supported inboxes.

### Content Quality

- [ ] Text-to-image ratio: minimum 60% text, 40% images
- [ ] Alt text on all images
- [ ] Working unsubscribe link (one-click preferred)
- [ ] Physical mailing address in footer
- [ ] No broken links
- [ ] HTML under 102KB (Gmail clipping threshold)

### Spam Trigger Words to Avoid

| Category | Words/Phrases |
|----------|--------------|
| Urgency | "Act now", "Limited time", "Hurry", "Don't miss out", "Expires" |
| Money | "Free", "$$", "Cheap", "Discount", "No cost", "Save big" |
| Pressure | "Order now", "Apply now", "Click here", "Buy direct" |
| Deceptive | "No obligation", "No strings attached", "Guaranteed", "Risk-free" |
| Excessive | ALL CAPS, multiple exclamation marks (!!!), excessive bold |

### List Hygiene

- Remove hard bounces immediately (never re-send)
- Suppress soft bounces after 3 consecutive failures
- Remove unengaged contacts after 90-180 days of inactivity
- Re-confirm permission annually for cold segments
- Maintain complaint rate below 0.05%

---

## A/B Test Elements

| Element | What to Test | Impact Level |
|---------|-------------|-------------|
| Subject line | Framework, length, personalization, emoji, tone | High, drives open rate |
| Send time | Day of week, time of day, timezone optimization | Medium, drives open rate |
| CTA text | Action verb, specificity, urgency, length | High, drives click rate |
| Layout | Single vs. multi-column, image placement, content order | Medium, drives engagement |
| Sender name | Brand name vs. person name vs. role + brand | Medium, drives open rate and trust |
| Preheader | Length, tone, complement vs. repeat subject | Low-medium, drives open rate |
| Content length | Short vs. long, text-heavy vs. image-heavy | Medium, drives click rate |

### Testing Rules

- Test one element at a time for clean results
- Minimum 1,000 recipients per variant
- Run for at least 48 hours before declaring winner
- Use the same audience segment for all variants
- Account for timezone distribution

---

## Performance Benchmarks by Industry

**Critical note on open rates:** Apple Mail Privacy Protection (MPP), active since iOS 15 in 2021, prefetches email images and inflates open rates by 30-50% for lists with significant Apple Mail users. Open rate benchmarks below are distorted by this. **Use click rate and click-to-open rate as your primary engagement signals, these are not affected by MPP.**

### SaaS

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| Open rate | < 15% | 20-25% | 25-30% | > 30% |
| Click rate | < 1.5% | 2-3% | 3-5% | > 5% |
| Click-to-open rate | < 8% | 10-14% | 14-18% | > 18% |
| Unsubscribe rate | > 0.5% | 0.2-0.5% | 0.1-0.2% | < 0.1% |
| Bounce rate | > 2% | 0.5-2% | 0.2-0.5% | < 0.2% |

### E-commerce

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| Open rate | < 12% | 15-20% | 20-25% | > 25% |
| Click rate | < 1% | 1.5-2.5% | 2.5-4% | > 4% |
| Click-to-open rate | < 7% | 9-13% | 13-17% | > 17% |
| Conversion rate | < 0.5% | 1-2% | 2-4% | > 4% |
| Revenue per email | < $0.05 | $0.10-0.25 | $0.25-0.50 | > $0.50 |

### B2B

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| Open rate | < 18% | 22-28% | 28-35% | > 35% |
| Click rate | < 1.5% | 2.5-3.5% | 3.5-5% | > 5% |
| Click-to-open rate | < 9% | 11-15% | 15-20% | > 20% |
| Reply rate | < 0.5% | 1-3% | 3-5% | > 5% |
| Meeting booked rate | < 0.1% | 0.2-0.5% | 0.5-1% | > 1% |

### Email Flow Performance, Directional Ranges

Email platforms each publish their own performance numbers, but methodology, industry mix, and time period differ enough between them that no single figure is an authoritative benchmark across senders. Treat everything below as a directional range to sanity-check your own numbers against, not a target to promise a customer.

#### Ecommerce Flow Performance (Directional)

| Flow Type | Open Rate | Click Rate | CVR |
|-----------|----------|-----------|-----|
| Welcome series (email 1) | 40-55% | 8-12% | 2-5% |
| Abandoned cart (email 1, sent within a few hours) | 35-50% | 6-10% | 2-8%, wide range by cart value and vertical |
| Browse abandonment | 20-35% | 4-7% | 1-3% |
| Post-purchase upsell | 30-45% | 5-9% | 2-4% |
| Win-back (lapsed customers) | 15-30% | 3-6% | 1-3% |
| Birthday / anniversary | 35-55% | 6-12% | 4-8% |

**Directional pattern, not a guaranteed multiplier:** across the reports we reviewed, automated behavior-triggered flows consistently outconvert one-off broadcast campaigns, often by a wide margin. The exact ratio moves a lot by list, vertical, and time period, so don't quote a specific multiplier to a customer as if it were fixed.

#### Segmentation Impact (Directional)

Segmented sends (by engagement, lifecycle stage, or behavior) reliably beat unsegmented broadcasts on revenue per recipient, open rate, and click rate, and tend to produce lower unsubscribe rates too. The size of the lift varies significantly by list quality and segmentation depth. Roughly 2-4x revenue per recipient is a reasonable planning range, but there's no single authoritative benchmark that holds across industries.

#### SaaS Email Benchmarks (Directional)

| Flow Type | Open Rate | Click Rate | Notes |
|-----------|----------|-----------|-------|
| Trial activation (Day 1) | 35-55% | 10-18% | Usually the highest open rate in a SaaS sequence, maximize CTA clarity |
| Onboarding Day 3 | 25-45% | 8-12% | Feature-specific, link to in-app action |
| Activation nudge (Day 7, not activated) | 20-35% | 5-9% | Human-sent variants tend to outperform automated ones |
| Feature announcement | 15-30% | 4-7% | Use for activated users only; dormant users inflate open, deflate click |
| Renewal reminder (30 days out) | 40-55% | 8-15% | Often the highest-converting email in a SaaS sequence |

---

## Copy Research: What Actually Converts

Copy patterns that tend to convert across ecommerce and SaaS contexts, based on general email marketing practice rather than any single named study.

---

### Ecommerce Welcome Email Copy

**The 3-email structure that wins**

Email 1 accounts for 60-70% of total welcome flow revenue. Keep it under 150 words, mobile is 65%+ of opens.

**Subject line patterns by brand type:**
| Brand Type | Winning Subject Pattern | Example |
|-----------|------------------------|---------|
| Discount-first | Transactional + specific | "Here's your 15% off, [first name]" |
| Premium (Glossier, Allbirds style) | Warmth signal | "Welcome to [brand], you're going to love this" |
| Fitness / lifestyle | Aspiration | "Your [Brand] journey starts now" |
| Cult DTC | Intimacy | "We've been waiting for you" |

**Discount-led Email 1 copy pattern (3x immediate revenue vs. no discount):**
```
Line 1: Acknowledge, "You're in."
Line 2: Deliver, "Your 15% off is waiting, no minimum."
Line 3: Set expectation, "We'll also send you new arrivals, restocks, and the occasional story worth reading."
CTA: "Shop [Brand]" (specific product link beats generic "Shop Now")
```

**Email 2 (Day 2-3): Highest-variance email. Winner by vertical:**
| Vertical | Winning Angle | Why |
|----------|--------------|-----|
| Apparel/fashion | Brand story + product CTA below | Identity-driven purchase decision |
| Beauty/skincare | Social proof (reviews, press, before/after) | Trust purchase, validation-seeking |
| Home goods | Product highlight with specific use-case | Utility purchase, needs context |
| Health/wellness | Brand story (mission sells product) | Values alignment drives purchase |

**Email 3 (Day 5-7): Close the undecided subscriber:**
- Urgency play: "Your 15% off expires in 48 hours", highest immediate conversion, only if deadline is real. False urgency is detectable.
- Objection handling: "Not sure where to start? Take our 60-second quiz", highest-converting Day 7 format for wide-assortment brands
- Social proof closer: Testimonials that address hesitation ("I wasn't sure at first, but..."), closes 2-3% of unconverted subscribers

**Top DTC approaches:**
- Gymshark: Lead with community, not product. Email 1 has no product push. Works for identity-driven brands.
- Glossier: No discount in welcome flow at all. Editorial-first builds LTV over discount training.
- AWAY: "The Weekend Edit" format - story-led content that features product. Tends to outperform typical click rates for story-led formats, though the exact multiple isn't backed by a verified benchmark.

---

### Post-Purchase Email Copy

**Sequence that drives 17% repeat purchase rate (vs. 5-7% with no flow)**

| Email | Timing | Copy Approach |
|-------|--------|--------------|
| Order confirmation | Immediate | 70% functional / 30% brand. Include 1 cross-sell. "Customers who bought X also love Y." |
| Usage check-in | Day 3-5 (post-delivery) | "How's your [product] treating you?" - not promotional. Care instructions, usage tips. Tends to lift review submission rates meaningfully compared to a cold review ask, though the exact multiple isn't backed by a verified source. |
| Replenishment or cross-sell | Day 14-21 (calibrated to product cycle) | "You might need this with your [product name]" - lead with use case, not product. 8-15% purchase rate for consumables. |
| Review request | Day 30 | "How did we do?" - small incentive for review. Customers who leave high satisfaction scores tend to have meaningfully higher LTV, though the exact multiple varies by source. |

**Email 3 money copy pattern:**
```
Subject: "You might need this with your [product name]" or "[First name], a thought about your [product]"
Body: "Most people who [bought X] end up reaching for [Y] within the first month. Here's why."
→ Introduce the cross-sell with social proof
CTA: Specific product link, NOT category page
```

---

### Browse Abandonment vs. Cart Abandonment Copy

**The key distinction, getting this wrong kills performance:**

Cart abandonment: customer showed purchase intent. Copy can be direct. "You left something behind" is accepted.

Browse abandonment: interest but no commitment. Assuming purchase intent reads as presumptuous. "You were looking at these boots, are you ready to buy?" underperforms.

**Browse abandonment subject lines that convert:**
| Subject | CTR | Notes |
|---------|-----|-------|
| "Still thinking about [product name]?" | 4-6% | Common range for this subject pattern |
| "We saved [product] for you" | high | Pair with limited stock |
| "Others are looking at [product name]" | 3-5% | Social proof trigger |
| "[First name], we know great taste when we see it" | good | Premium brand flattery |

Browse abandonment copy rule: position it as a service, not surveillance. "We saved your browsing so you can pick up where you left off" beats "We saw you looking at the burgundy ankle boots."

Browse abandonment emails should include 2-3 alternative product recommendations in the same category, they're still in discovery mode. Cart abandonment should focus on the specific cart item only.

**Timing:** Reaching out within an hour of the browsing session ending tends to convert meaningfully better than waiting 24 hours, though the exact multiple isn't backed by a verified source.

---

### Win-Back / Re-Engagement Copy

**Subject lines that tend to perform well for win-back sends:**

| Approach | Subject | Open Rate |
|----------|---------|-----------|
| Curiosity | "Is this the end?" | 28-32% (90-180 day lapsed) |
| Curiosity | "Did we do something wrong?" | 24-28% |
| Curiosity | "We need to talk" | 26-30% (casual/lifestyle brands only) |
| Straight offer | "A gift for you, [first name]" | 22-25% ("gift" beats "discount" by 8-12%) |
| Straight offer | "We kept your 15% off waiting" | 21-25% |
| Product update | "Come back, we've changed" | 22-26% (only if genuinely true) |
| Classic | "We miss you, [first name]" | 18-22% (weakest, feels generic) |

**The three-way comparison:**
- Curiosity approaches: highest open rate (25-32%), second on revenue per email
- Straight offer: second on open rate, highest revenue per email (discount drives AOV)
- "We miss you": third on every metric except reply rate (emotional response, low purchase intent)

**Incentive level that triggers re-engagement:**
| Offer | Re-engagement Rate | Notes |
|-------|-------------------|-------|
| No offer | 3-5% | Lowest |
| Free shipping | 8-12% | Best for brands where shipping is known friction |
| 10% off | 11-14% | Too small below $50 AOV |
| 20% off | 18-24% | Efficient sweet spot for most brands |
| 25-30% off | 22-28% | Marginal lift over 20%, significant margin cost |
| Free gift with purchase | 19-25% | Best brand perception, feels generous not desperate |

Key finding: the jump is between "no offer" and "any offer." The marginal difference between 20% and 30% rarely justifies the margin loss.

**The "unsubscribe or re-engage" email, highest re-engagement rate in the category:**

Subject: "Should we stay or should we go?" or "This is probably our last email"

Body structure:
1. Direct acknowledgment: "You haven't opened an email from us in [X months]. We notice these things."
2. One-sentence value prop reminder: what you actually send, how often
3. Two-option CTA: "Stay subscribed" button AND visible "Unsubscribe" link
4. Optional: small incentive attached to "stay subscribed"

Making unsubscribe easy paradoxically tends to increase re-engagement - the subscriber feels respected, not trapped. Some brands have reported meaningfully higher re-engagement using this pattern, though there's no single verified benchmark for the lift.

---

### SaaS Activation Email Copy

**Goal: one action in Day 0-1. Users who complete one meaningful action in the first 24 hours tend to be meaningfully more likely to convert to paid, though the exact multiple isn't backed by one verified source.**

**Winning subject line patterns:**
| Pattern | Why It Works | Notes |
|---------|-------------|--------|
| "Your [Product] account is ready - start here" | Eliminates decision paralysis | Common pattern in SaaS activation sequences |
| "One thing to do in [Product] today" | Single-action framing | Tends to lift Day 1 activation, though the exact lift isn't backed by a verified benchmark |
| "We set something up for you" | Curiosity + implies effort made | Anecdotally reported by SaaS teams, not backed by a specific study |
| "[First name], before you explore [Product]..." | Pattern interrupt for complex products | Anecdotally reported, no verified benchmark |

**Anatomy of a high-converting Day 0 activation email (under 150 words):**
```
Para 1 (2 sentences): Welcome + specific promise.
NOT "we're excited to have you"
YES: "You can [specific outcome] in [Product] in the next 10 minutes."

Para 2 (3-4 sentences): Name the single action. Explain why it's the one thing.
"The fastest way to see [Product] work for your business is to [specific action].
It takes under 5 minutes and shows you exactly how [outcome]."

CTA: Action-specific, "Connect your [data source]" not "Go to dashboard"

Below fold (optional): 3-bullet "what you can do" only if product complexity warrants it
```

**Example pattern:**
> Subject: "One thing to do in [Product] today"
> Body: "Hi [Name], Welcome to [Product]. You can [complete the core action] in the next 5 minutes. [CTA: specific action] That's it for now. Once you've done that, we'll walk you through the next step."

---

### SaaS "You Haven't Activated" Copy (Day 3-5)

**What doesn't work:** "We noticed you haven't [taken action] yet", frames inactivity as failure. Opens fine (curiosity), clicks poorly.

**What works: barrier removal framing.**
```
"If you ran into any trouble setting up [Product], we can fix that in 5 minutes."
"Sometimes the first step isn't obvious, here's the shortcut."
```

**Plain text beats HTML for this email:**
- Plain text, personal sender (from "Alex at [Product]"): 3-5x higher reply rate, 1.5-2x higher click rate vs. branded HTML
- Branded HTML: higher brand recall, lower CTR on activation action

**The pattern that converts best:**
> Subject: "Quick question, [Name]"
> Body: "Hey [Name], Did you get a chance to try [Product] yet? I wanted to make sure you got to [key activation moment], a lot of people find that's when it clicks. If you're stuck on anything, just reply here., [Human name], [Product] team"
> CTA: Soft ask (reply) or calendar link. Hard CTAs ("Click here to complete setup") underperform when the subscriber is already in a non-action state.

---

### SaaS Feature Education Email Copy

**Format hierarchy by conversion on paid upgrade:**

1. **Use case story** (highest): "Here's how [company type] uses [feature] to [specific outcome]." 200-350 words, one CTA to try the feature. Tends to convert meaningfully better than tip-based emails, though the exact multiple isn't backed by a verified benchmark.

2. **Before/after framing**: "Before [feature]: [pain]. After [feature]: [result]." Works for productivity and automation features.
   - Subject: "Before vs. after [feature name]"

3. **Tip format**: "3 ways to use [feature]." Works for power users, not onboarding. Risk: makes the feature feel optional.

4. **Video/GIF-led**: Animated GIF in email showing feature. Tends to lift CTR meaningfully, though the exact percentage isn't backed by a verified benchmark. Lift diminishes for users who don't watch.

**The format to avoid:** Long feature documentation dumps. "Here's everything [feature] can do" has the lowest click rates and highest unsubscribes in every SaaS email benchmark.

---

### SaaS Upgrade / Upsell Email Copy

**Triggers that convert (ranked by effectiveness):**

| Trigger | Subject Pattern | CVR |
|---------|----------------|-----|
| Usage limit (80-90% of plan cap) | "You're almost out of [limit]" | Highest - tends to notably outperform time-based triggers |
| Feature paywall hit | "You tried [feature] - here's how to unlock it" | 8-15% of sends |
| Success milestone | "You've [done X] - here's what's next on [paid plan]" | Strong - success-framed tends to beat problem-framed for activated users |
| Team collaboration | "Invite your team to see what you've built" | Strong for seat expansion in collaborative products |

**Copy pattern for upsell email:**
1. Lead with what they've accomplished (not what they're missing): "You've [done X] in [Product]."
2. Frame upgrade as natural continuation: "Here's what [paid plan users] do next."
3. Offer comparison table only if feature differentiation is genuinely clear
4. End with risk reducer: "Cancel anytime. No commitment."

**What fails:** Upsell emails that open with "Upgrade now" or "You're missing out on..." before acknowledging what the user has already done. The acknowledgment of their own behavior is the trust signal that makes the upgrade feel earned, not pushed.

---

## Sending Gates: What Blocks Mail Before Copy Matters

Deliverability failures are not copy problems, and no subject-line work recovers a send that was
rejected at the gateway. Check these before a campaign ships. Where the user cannot confirm one,
say the campaign is blocked on it rather than shipping and hoping.

### Bulk sender requirements

Major inbox providers apply hard requirements to anyone sending meaningful volume to their users.
The specifics move, so confirm current thresholds with the provider, but the shape has been stable:

| Requirement | What it means | Failure mode |
|---|---|---|
| **SPF and DKIM both passing** | Authenticate on the sending domain | Mail rejected or junked outright |
| **DMARC published** | A policy record on the sending domain, aligned with SPF or DKIM | Rejected at bulk volume |
| **Alignment** | The visible From domain matches the authenticated domain | Passes SPF technically, still fails alignment |
| **One-click unsubscribe** | `List-Unsubscribe` plus `List-Unsubscribe-Post` headers, honoured within a short window | Non-compliant bulk mail; complaints rise because the only exit is the spam button |
| **Spam complaint rate under roughly 0.1%, never near 0.3%** | Measured by the provider, not by your tool | Progressive throttling, then blocking, and recovery is slow |

**One-click unsubscribe is a header, not a footer link.** A visible unsubscribe link in the body
does not satisfy it. If the sending platform does not set both headers, that is a platform gap to
resolve before the send, and it is worth checking rather than assuming, since a footer link is what
most teams believe is sufficient.

### Warmup and ramp

A new domain, subdomain, or IP has no sending reputation, and volume without reputation reads as a
spam pattern.

- Never launch a sequence at full volume from a domain with no history. Start small and increase
  gradually over weeks, watching complaint and bounce rates at each step rather than following a
  fixed schedule.
- Send to the most engaged recipients first. Early positive engagement is what builds the
  reputation that later volume depends on.
- **Warm the subdomain you will actually send from.** Reputation attaches to the sending domain, so
  warming the root domain does not transfer to a new marketing subdomain.
- A reputation drop takes far longer to recover than it took to cause. Slowing a ramp costs days;
  a block costs weeks.

### List hygiene as a deliverability control

- **Never send to a purchased or scraped list.** Spam traps in bought lists damage domain
  reputation in ways that affect every future send, including transactional mail.
- Remove hard bounces immediately, and repeated soft bounces after a small number of attempts.
- **Sunset the unengaged.** Continuing to mail people who have not opened in many months depresses
  engagement rates, which is itself a ranking signal. A re-engagement attempt followed by removal
  beats indefinite sending.
- Validate at capture, not in bulk later. A typo caught at the form never becomes a bounce.

### Verify before the full send

- **Seed test first.** Send to addresses across the major providers and confirm placement, not just
  delivery. "Delivered" and "in the inbox" are different outcomes and most tools report only the
  first.
- Render-test on mobile and in a dark-mode client. Dark mode inverts backgrounds and commonly makes
  a logo or a bordered button disappear.
- Click every link in the seed copy, including the unsubscribe. A broken unsubscribe converts
  unsubscribes into spam complaints, which is the most expensive possible substitution.
- Confirm the plain-text alternative exists and reads properly on its own.


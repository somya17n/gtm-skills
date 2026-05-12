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
- **Single CTA per block** — avoid competing actions

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
- **Emoji:** Use sparingly (0-1 per subject). Test performance — works in some industries, hurts in others.
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
| Subject line | Framework, length, personalization, emoji, tone | High — drives open rate |
| Send time | Day of week, time of day, timezone optimization | Medium — drives open rate |
| CTA text | Action verb, specificity, urgency, length | High — drives click rate |
| Layout | Single vs. multi-column, image placement, content order | Medium — drives engagement |
| Sender name | Brand name vs. person name vs. role + brand | Medium — drives open rate and trust |
| Preheader | Length, tone, complement vs. repeat subject | Low-medium — drives open rate |
| Content length | Short vs. long, text-heavy vs. image-heavy | Medium — drives click rate |

### Testing Rules

- Test one element at a time for clean results
- Minimum 1,000 recipients per variant
- Run for at least 48 hours before declaring winner
- Use the same audience segment for all variants
- Account for timezone distribution

---

## Performance Benchmarks by Industry

**Critical note on open rates:** Apple Mail Privacy Protection (MPP), active since iOS 15 in 2021, prefetches email images and inflates open rates by 30–50% for lists with significant Apple Mail users. Open rate benchmarks below are distorted by this. **Use click rate and click-to-open rate as your primary engagement signals — these are not affected by MPP.**

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

### Real-World Email Flow Benchmarks (2024–2025)

Sourced from Klaviyo, Omnisend, and Mailchimp state-of-email reports. Automated flows vs. manual campaigns have dramatically different performance profiles.

#### Ecommerce Flow Performance (Klaviyo / Omnisend 2024)

| Flow Type | Open Rate | Click Rate | CVR | Revenue per Email | Source |
|-----------|----------|-----------|-----|------------------|--------|
| Welcome series (email 1) | 45–55% | 8–12% | 3–5% | $0.40–0.80 | Klaviyo 2024 |
| Abandoned cart (email 1, 1hr) | 38–45% | 7–10% | 3.33% avg / 7.69% top 10% | $1.00–2.50 | Klaviyo + Omnisend 2024 |
| Browse abandonment | 25–35% | 4–7% | 1.5–2.5% | $0.30–0.60 | Omnisend 2024 |
| Post-purchase upsell | 35–45% | 5–9% | 2–4% | $0.50–1.20 | Klaviyo 2024 |
| Win-back (30-day lapsed) | 20–30% | 3–6% | 1.5–2.5% | $0.20–0.50 | Omnisend 2024 |
| Birthday / anniversary | 40–55% | 7–12% | 5–8% | $0.80–1.50 | Klaviyo 2024 |

**Key finding from Omnisend 2024:** Automated email flows deliver **27x higher CVR** than broadcast campaigns (3.33% automated vs. 0.12% broadcast). The leverage is in flows, not blasts.

#### Segmentation Impact (Klaviyo 2024)

| Approach | Revenue per Recipient (RPR) | Relative Lift |
|----------|-----------------------------|--------------|
| Unsegmented broadcast | $0.08 | Baseline |
| Basic segmentation (engaged vs. unengaged) | $0.18 | +125% |
| Advanced segmentation (lifecycle + behavior) | $0.26 | **+225% (3.2x)** |

**Segmented emails generate 3.2x higher revenue per recipient than unsegmented lists.** Source: Klaviyo 2024 (n=130,000+ ecommerce accounts).

#### SaaS Email Benchmarks (2024)

| Flow Type | Open Rate | Click Rate | Notes |
|-----------|----------|-----------|-------|
| Trial activation (Day 1) | 40–55% | 12–18% | Highest open rate in any SaaS sequence — maximize CTA clarity |
| Onboarding Day 3 | 30–45% | 8–12% | Feature-specific, link to in-app action |
| Activation nudge (Day 7, not activated) | 25–35% | 5–9% | Human-sent variant outperforms automated by 2–3x |
| Feature announcement | 20–30% | 4–7% | Use for activated users only; dormant users inflate open, deflate click |
| Renewal reminder (30 days out) | 45–55% | 10–15% | Highest-converting email in SaaS — plan your renewal message carefully |

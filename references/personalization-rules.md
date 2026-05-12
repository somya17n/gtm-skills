# Personalization Rule Design

Reference for designing web and content personalization: types, rule structure, condition types, experience priorities, page zones, recommendation algorithms, measurement, and progressive personalization.

---

## Personalization Types

### Content Personalization

Modifying copy and images based on visitor attributes.

| Element | Example |
|---------|---------|
| Headline text | "The CRM built for [visitor's industry]" vs. generic headline |
| Body copy | Industry-specific pain points and solutions |
| Images | Role-appropriate hero images (marketer sees marketing dashboard, engineer sees API docs) |
| Case studies | Show case studies from the visitor's industry |
| Statistics | Display relevant benchmarks for the visitor's company size |

### Layout Personalization

Changing the order or visibility of page sections.

| Element | Example |
|---------|---------|
| Section order | Pricing section first for high-intent visitors; education first for new visitors |
| Section visibility | Hide "What is X?" section for returning visitors who already understand |
| Content density | Detailed view for technical evaluators; summary view for executives |
| Feature emphasis | Highlight API docs for developer personas; highlight dashboards for business users |

### Offer Personalization

Adjusting pricing, discounts, or promotional offers.

| Element | Example |
|---------|---------|
| Discount level | 20% for win-back segments, 10% for new customers |
| Plan recommendation | Highlight Enterprise for companies >500 employees, Starter for <50 |
| Trial length | 14-day standard, 30-day for enterprise evaluations |
| Bundle offers | Suggest add-ons based on current plan and usage patterns |

### Navigation Personalization

Modifying menu items and navigation paths.

| Element | Example |
|---------|---------|
| Menu items | Show "Upgrade" for free users, "Renew" for expiring contracts |
| Quick links | Surface most-used features in navigation |
| Onboarding flow | Skip completed steps, highlight next action |
| Documentation | Prioritize docs for features the user actually uses |

### CTA Personalization

Changing button text, color, and destination based on visitor state.

| Element | Example |
|---------|---------|
| Button text | "Start Free Trial" (new) vs. "Upgrade Plan" (free user) vs. "Talk to Sales" (enterprise) |
| Button destination | Link to appropriate signup flow, upgrade page, or demo booking |
| Urgency | Add countdown for time-limited offers to eligible segments |
| Secondary CTA | "Watch Demo" for new visitors, "See What's New" for returning users |

---

## Rule Structure

Every personalization rule follows the IF-THEN-ELSE pattern:

```
IF [segment condition] THEN [show experience variant] ELSE [default experience]
```

### Rule Schema

```json
{
  "id": "rule-001",
  "name": "Enterprise Hero Personalization",
  "priority": 1,
  "enabled": true,
  "condition": {
    "$and": [
      { "attribute": "company_size", "operator": ">=", "value": 500 },
      { "attribute": "lifecycle_stage", "operator": "in", "value": ["Promising", "Regulars"] }
    ]
  },
  "experience": {
    "zone": "hero",
    "variant": "enterprise-hero-v1",
    "content": {
      "headline": "Enterprise-grade engagement at scale",
      "subheadline": "Trusted by Fortune 500 teams to manage millions of customer interactions.",
      "cta_text": "Talk to Sales",
      "cta_url": "/demo/enterprise",
      "hero_image": "/images/enterprise-dashboard.webp"
    }
  },
  "default": {
    "variant": "default-hero",
    "content": {
      "headline": "The complete customer engagement platform",
      "subheadline": "Grow revenue with personalized experiences across every channel.",
      "cta_text": "Start Free Trial",
      "cta_url": "/signup",
      "hero_image": "/images/standard-dashboard.webp"
    }
  }
}
```

---

## Condition Types

### Lifecycle Stage

| Condition | Example Use |
|-----------|-------------|
| `lifecycle_stage = "Champions"` | VIP messaging, exclusive offers, referral prompts |
| `lifecycle_stage = "New Customers"` | Onboarding-focused content, getting started guides |
| `lifecycle_stage = "At Risk"` | Win-back offers, re-engagement messaging |
| `lifecycle_stage in ["Regulars", "Champions"]` | Loyalty rewards, advanced feature highlights |

### Behavioral Score

| Condition | Example Use |
|-----------|-------------|
| `activity_score > 80` | Power user content, advanced features, beta invitations |
| `activity_score < 20` | Re-activation prompts, simplified onboarding |
| `fit_score > 70` | Sales-ready messaging, demo CTAs |
| `intent_level = "High"` | Pricing-focused content, urgency messaging, direct CTAs |

### Referral Source

| Condition | Example Use |
|-----------|-------------|
| `utm_source = "google"` | Headline matching the search query intent |
| `utm_source = "linkedin"` | Professional tone, B2B-specific messaging |
| `utm_campaign = "competitor-x"` | Comparison content, switching incentives |
| `referrer contains "techcrunch"` | Press mention acknowledgment, credibility reinforcement |

### Device

| Condition | Example Use |
|-----------|-------------|
| `device = "mobile"` | Simplified layout, click-to-call CTAs, app download prompts |
| `device = "desktop"` | Full-featured demos, detailed comparisons |
| `device = "tablet"` | Medium-density content, touch-optimized interactions |

### Location

| Condition | Example Use |
|-----------|-------------|
| `country = "US"` | USD pricing, US-based case studies |
| `country = "DE"` | GDPR-focused messaging, EU data center mention, EUR pricing |
| `region = "California"` | CCPA compliance messaging |
| `timezone offset in [-8, -5]` | Americas-focused event times |

### Visit Count

| Condition | Example Use |
|-----------|-------------|
| `visit_count = 1` | First-time visitor welcome, brand introduction |
| `visit_count = 2-3` | Return visitor recognition, deeper content |
| `visit_count > 5` | Familiar visitor shortcuts, "ready to commit?" messaging |
| `visit_count > 10` | Direct conversion CTAs, reduce educational content |

### Time of Day

| Condition | Example Use |
|-----------|-------------|
| `hour >= 9 AND hour <= 17` | Business-hours messaging, live chat availability |
| `hour >= 18 OR hour <= 8` | After-hours messaging, async contact options |
| `day_of_week in ["Saturday", "Sunday"]` | Weekend-appropriate content, relaxed tone |

---

## Experience Priorities

Rules are evaluated **top-to-bottom by priority number** (lower number = higher priority). The first matching rule wins.

### Priority Ordering Best Practices

| Priority Range | Rule Type | Example |
|---------------|-----------|---------|
| 1-10 | Critical overrides | Maintenance announcements, compliance notices |
| 11-30 | High-value segments | Enterprise personalization, champion VIP experience |
| 31-50 | Behavioral targeting | High-intent visitors, returning visitors |
| 51-70 | Source-based targeting | Campaign-specific landing experiences |
| 71-90 | Demographic targeting | Industry or location-based content |
| 91-100 | Default / fallback | Catch-all experience for unmatched visitors |

### Conflict Resolution

- First matching rule wins (no stacking, no blending)
- A default fallback is **required** for every zone — visitors must always see something
- If no rules match for a zone, the default experience renders
- Rules can be toggled on/off without deletion (enabled/disabled flag)

---

## Page Zones

Zones are predefined areas on a page where personalized content can be injected.

| Zone | Location | Content Types | Size Constraints |
|------|----------|---------------|-----------------|
| `hero` | Top of page, above fold | Headline, subheadline, image, CTA | Full width, 400-600px height |
| `banner` | Top bar, above header | Text + CTA link | Full width, 40-60px height |
| `sidebar` | Right or left column | Content recommendations, CTAs, forms | 250-350px wide |
| `popup` | Overlay, centered | Form, offer, announcement | 400-600px wide, auto height |
| `inline_cta` | Within body content | CTA button/banner between content blocks | Content width, 80-120px height |
| `exit_intent` | Overlay, triggered on exit intent | Last-chance offer, email capture | 500-700px wide |
| `sticky_bar` | Fixed at top or bottom of viewport | Persistent offer or announcement | Full width, 50-70px height |
| `slide_in` | Slides from corner | Secondary offer, chat prompt | 300-400px wide |
| `content_block` | Replaces a content section | Full content personalization | Section dimensions |
| `recommendation` | Below content or sidebar | Product/content recommendations | Variable |

### Zone Triggers

| Trigger | When It Fires |
|---------|--------------|
| Page load | Immediately on page render |
| Scroll depth | When user scrolls past a percentage (25%, 50%, 75%) |
| Time on page | After N seconds (typically 5-30 seconds) |
| Exit intent | Mouse moves toward browser close/back (desktop only) |
| Click | User clicks a specific element |
| Inactivity | No interaction for N seconds |
| Page count | After viewing N pages in session |

---

## Recommendation Algorithms

### Collaborative Filtering

**Method:** "Users who engaged with X also engaged with Y."

| Variant | Description | Best For |
|---------|-------------|----------|
| User-based | Find similar users, recommend what they consumed | Content recommendations |
| Item-based | Find similar items based on co-consumption patterns | Product recommendations |

**Strengths:** Discovers unexpected connections, works without content metadata.
**Weaknesses:** Cold start problem (needs interaction history), popularity bias.

### Content-Based

**Method:** Recommend items similar to what the user has already engaged with, based on item attributes.

| Signal | Description |
|--------|-------------|
| Category match | Same product category, content topic, or feature area |
| Attribute similarity | Similar price range, specifications, or tags |
| Text similarity | TF-IDF or embedding-based similarity of descriptions |

**Strengths:** No cold start for items (only needs metadata), transparent recommendations.
**Weaknesses:** Limited discovery (stays in the user's known preferences).

### Hybrid

Combines collaborative filtering and content-based approaches with configurable weights.

```
score = (weight_CF * collaborative_score) + (weight_CB * content_based_score) + (weight_popularity * popularity_score)
```

Default weights: CF 50%, CB 30%, Popularity 20%.

### Trending

**Method:** Surface items gaining traction across all users within a time window.

| Window | Use Case |
|--------|----------|
| Last 24 hours | "Trending today" |
| Last 7 days | "Popular this week" |
| Last 30 days | "Top this month" |

**Calculation:** Velocity of engagement (rate of change), not absolute volume.

### Recently Viewed

**Method:** Show items the user recently interacted with for easy re-access.

- Ordered by recency (most recent first)
- Deduplicated
- Exclude already-purchased items
- Typically limited to 4-8 items

---

## Personalization Measurement

### Lift Calculation

```
Lift = (variant conversion rate - default conversion rate) / default conversion rate × 100%
```

### Metrics to Track Per Experience

| Metric | Description |
|--------|-------------|
| Impression count | How many visitors saw this experience |
| Engagement rate | Clicks / impressions |
| Conversion rate | Conversions / impressions |
| Revenue per visitor | Total revenue / impressions |
| Time on page | Average time spent by visitors seeing this experience |
| Bounce rate | % who left without interaction |

### Segment-Level Performance

Break down performance by the segment that triggered the rule:

- Does the personalized experience actually outperform the default for this segment?
- Are there sub-segments where it underperforms?
- Is the sample size sufficient for confidence (minimum 200 impressions per variant)?

### Statistical Significance

Use the same Bayesian methodology as experiment testing:
- P(variant > default) > 95% = statistically significant lift
- Monitor for at least 14 days to account for weekly patterns
- Account for novelty effect: performance may decline after initial exposure

---

## Real-World Personalization Lift Benchmarks (2024–2025)

How much does personalization actually move the needle? Data from McKinsey, Klaviyo, Dynamic Yield, Monetate, and Epsilon.

| Personalization Type | Lift | Metric | Source |
|---------------------|------|--------|--------|
| Any personalization vs. generic | **5–15% revenue increase** | Revenue per session | McKinsey 2024 |
| Personalized homepage vs. generic | 10–15% | Conversion rate | Dynamic Yield 2024 |
| Segmented email vs. unsegmented | **3.2x higher RPR** | Revenue per recipient | Klaviyo 2024 |
| Behavioral triggers vs. time-based sends | **27x higher CVR** | Conversion rate | Omnisend 2024 |
| Product recommendations (collaborative filter) | 15–35% | AOV / revenue per session | Monetate 2024 |
| Personalized CTAs vs. generic CTAs | **202% higher CVR** | Click-to-convert | HubSpot 2023 |
| Loyalty-tier personalized messaging | 2–4x | Repeat purchase rate | Klaviyo 2024 |
| Post-purchase upsell (1:1 product recs) | 20–30% | Add-on attach rate | Dynamic Yield 2024 |
| ICP-matched personalization (B2B SaaS) | 40–60% | Demo request rate | 6Sense / Demandbase 2024 |

### Personalization Failure Points

Where personalization goes wrong in practice (Forrester + CXL research):

| Failure | Frequency | Cause | Fix |
|---------|-----------|-------|-----|
| Personalization based on stale data | 45% of cases | No data freshness rules | Require recency constraint on all conditions |
| Wrong persona segment (mis-attribution) | 30% of cases | Relying on job title alone | Use behavioral signals + title together |
| Showing the same personalization > 10x | 40% of cases | No impression cap or refresh | Cap impressions and rotate variants |
| Personalization that doesn't match expectation | 25% of cases | Cookie data vs. current session | Blend persistent + session-level signals |
| No holdout group → can't prove lift | 60% of companies | Never set up control | Always hold 10% as unexposed control group |

## Progressive Personalization

Personalization depth increases as you learn more about the visitor.

### Level 1: Anonymous Visitor

Available signals: referral source, device, location, time of day, UTM parameters, landing page.

| Signal | Personalization |
|--------|----------------|
| `utm_source = "linkedin"` | Professional tone, B2B messaging |
| `device = "mobile"` | Simplified layout, app download CTA |
| `country = "UK"` | GBP pricing, UK case studies |
| `referrer contains "vs-competitor"` | Comparison-focused content |
| `landing_page = "/pricing"` | High-intent experience, demo CTA |

### Level 2: Known Visitor (Identified)

Additional signals: lifecycle stage, activity score, fit score, intent level, company, role.

| Signal | Personalization |
|--------|----------------|
| `lifecycle_stage = "Promising"` | Nurture content, success stories |
| `activity_score > 70` | Advanced feature highlights, power user content |
| `intent_level = "High"` | Direct pricing, demo booking, urgency |
| `company_size > 500` | Enterprise-focused messaging |
| `role = "Engineer"` | Technical content, API documentation |

### Level 3: Deep Personalization (Rich Profile)

Additional signals: purchase history, feature usage, support history, preferences, NPS score.

| Signal | Personalization |
|--------|----------------|
| `purchased_products includes "Pro"` | Upsell to Enterprise, complementary features |
| `feature_usage["analytics"] > 80%` | Advanced analytics tips, new analytics features |
| `nps_score >= 9` | Referral program, advocacy opportunities |
| `support_tickets > 3` | Proactive help, dedicated support CTA |
| `contract_renewal < 30d` | Renewal messaging, loyalty offer |

### Personalization Maturity Path

```
Stage 1: Segment-based → 3-5 audience segments, rule-based targeting
Stage 2: Behavioral → Activity and intent-based dynamic targeting
Stage 3: Predictive → ML-based next-best-action recommendations
Stage 4: Real-time → In-session behavioral adaptation
```

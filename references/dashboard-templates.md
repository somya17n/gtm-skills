# Dashboard Templates

Reference for 8 out-of-the-box dashboard templates, metric calculation formulas, cohort analysis methodology, attribution models, and alert thresholds for anomaly detection.

---

## 1. SaaS Growth Dashboard

**Audience:** Founders, VPs of Growth, Revenue Leaders
**Update frequency:** Daily (metrics), weekly (trends)

### Metrics

| Metric | Definition | Visualization | Target |
|--------|-----------|---------------|--------|
| **WAU** (Weekly Active Users) | Unique users who performed a meaningful action in the last 7 days | Line chart, trailing 8 weeks | Consistent growth, < 5% week-over-week decline |
| **MRR** (Monthly Recurring Revenue) | Sum of all recurring revenue normalized to a monthly period | Area chart with breakdown (new, expansion, contraction, churn) | Month-over-month growth > 10% (early stage), > 5% (growth stage) |
| **Trial Conversion Rate** | Trials that converted to paid / total trials started | Funnel chart + trend line | > 15% for self-serve, > 30% for sales-assisted |
| **Retention Curve** | % of cohort still active at each month since signup | Cohort retention matrix (heatmap) | Month 1: > 80%, Month 3: > 60%, Month 12: > 40% |
| **Expansion Revenue** | Revenue from existing customers upgrading or adding seats/features | Bar chart, monthly | > 20% of new revenue should come from expansion |
| **Net Churn** | (Churned MRR - Expansion MRR) / Start MRR | Single number with trend | Negative net churn (net dollar retention > 100%) |

---

## 2. SaaS Product Health Dashboard

**Audience:** Product Managers, Engineering Leads
**Update frequency:** Daily

### Metrics

| Metric | Definition | Visualization | Target |
|--------|-----------|---------------|--------|
| **DAU/MAU Ratio** | Daily active users / Monthly active users (stickiness) | Line chart, trailing 30 days | > 20% is good, > 40% is excellent |
| **Feature Adoption Heatmap** | Usage frequency of each major feature across user segments | Heatmap (features x segments) | Core features > 60% adoption, new features > 20% in first 30 days |
| **NPS** (Net Promoter Score) | % Promoters (9-10) - % Detractors (0-6) | Gauge chart + distribution histogram | > 30 is good, > 50 is excellent |
| **Session Depth** | Average number of pages/actions per session | Line chart with distribution | Increasing trend, > 5 actions/session |
| **Error Rate** | Errors / total requests | Line chart with alert threshold | < 0.1% (API), < 1% (UI) |
| **Time to Value** | Duration from signup to first value-delivering action | Histogram + median trend | Decreasing trend, < 5 minutes for self-serve |

---

## 3. SaaS Sales Pipeline Dashboard

**Audience:** VP Sales, Sales Managers, Revenue Operations
**Update frequency:** Daily (pipeline), weekly (forecasts)

### Metrics

| Metric | Definition | Visualization | Target |
|--------|-----------|---------------|--------|
| **Pipeline Value by Stage** | Total deal value in each pipeline stage | Stacked bar chart or waterfall | 3-4x target in total pipeline |
| **Win Rate Trend** | Won deals / total closed deals over time | Line chart, trailing 12 weeks | > 25% (SMB), > 20% (mid-market), > 15% (enterprise) |
| **Deal Velocity** | Average days from pipeline creation to close | Line chart + by-segment breakdown | Decreasing trend; within segment benchmarks |
| **Forecast vs. Actual** | Forecasted revenue vs. actual closed revenue | Dual bar chart, monthly | Forecast accuracy > 80% |
| **Quota Attainment** | Closed revenue / quota per rep/team | Bar chart, per rep with team average line | > 80% of reps at 100%+, team average > 100% |
| **Pipeline Created** | New pipeline value added in period | Bar chart, weekly/monthly | Consistent with target coverage ratio |

---

## 4. E-commerce Revenue Dashboard

**Audience:** E-commerce Managers, CFOs
**Update frequency:** Daily

### Metrics

| Metric | Definition | Visualization | Target |
|--------|-----------|---------------|--------|
| **Gross Revenue** | Total revenue before returns and discounts | Line chart, daily with MTD/YTD totals | Meeting or exceeding targets |
| **AOV** (Average Order Value) | Total revenue / number of orders | Line chart with trend | Increasing trend, segment-specific targets |
| **Conversion Rate** | Orders / sessions | Funnel chart + line trend | > 2% (typical), > 3% (good), > 5% (excellent) |
| **Cart Abandonment Rate** | Carts created but not purchased / total carts created | Single number + trend | < 70% (good), industry average ~70% |
| **Revenue by Channel** | Revenue attributed to each marketing channel | Stacked bar or pie chart | Diversified — no single channel > 50% |
| **Return Rate** | Items returned / items sold | Line chart with threshold | < 10% (normal), investigate if > 15% |

---

## 5. E-commerce Attribution Dashboard

**Audience:** Marketing Directors, Growth Leads
**Update frequency:** Weekly

### Metrics

| Metric | Definition | Visualization | Target |
|--------|-----------|---------------|--------|
| **ROAS by Channel** | Revenue attributed to channel / ad spend on channel | Bar chart, per channel | > 3x overall, channel-specific targets |
| **CAC** (Customer Acquisition Cost) | Total sales + marketing spend / new customers acquired | Single number + trend by channel | Decreasing trend, < 1/3 of LTV |
| **First-Touch vs. Last-Touch** | Revenue attribution comparison between first and last interaction | Side-by-side bar charts | Identify channels that start vs. close journeys |
| **Time to Convert** | Days from first touchpoint to purchase | Histogram + median | Understanding typical consideration period |
| **Channel Mix** | % of conversions attributed to each channel | Sankey diagram or stacked area | Balanced mix, identify emerging channels |
| **Incrementality** | Lift from each channel vs. organic baseline | Bar chart with confidence intervals | Focus spend on channels with highest incrementality |

---

## 6. E-commerce Customer 360 Dashboard

**Audience:** Customer Experience, CRM Teams
**Update frequency:** Weekly

### Metrics

| Metric | Definition | Visualization | Target |
|--------|-----------|---------------|--------|
| **RFM Distribution** | Customer count by RFM segment | Treemap or segmented bar chart | Healthy distribution — growing Champions and Regulars |
| **LTV Cohort Analysis** | Cumulative revenue per customer cohort over time | Cohort line chart (one line per monthly cohort) | Later cohorts trending higher than earlier cohorts |
| **NPS** | Net Promoter Score from customer surveys | Gauge + trend line | > 30, increasing |
| **Repeat Purchase Rate** | Customers with 2+ purchases / total customers | Single number + trend | > 25% (good), > 40% (excellent) |
| **Lifecycle Stage Distribution** | Customer count per lifecycle stage | Stacked bar chart over time | Growing Champions/Regulars, shrinking At Risk |
| **Customer Lifetime Value** | Average total revenue per customer over their lifetime | Single number + cohort comparison | Increasing trend |

---

## 7. Customer Success Dashboard

**Audience:** VP Customer Success, CSM Managers
**Update frequency:** Daily (health), weekly (trends)

### Metrics

| Metric | Definition | Visualization | Target |
|--------|-----------|---------------|--------|
| **Account Health Distribution** | % of accounts in Healthy / Watch / At Risk categories | Donut chart + trend | > 70% Healthy, < 10% At Risk |
| **Churn Risk Heatmap** | Accounts plotted by churn risk indicators | Heatmap (accounts x risk signals) | No account with 3+ risk signals unaddressed |
| **CSM Activity** | Meetings, emails, calls per CSM per account | Bar chart per CSM | Minimum 1 touch per account per month |
| **Expansion Pipeline** | Potential expansion revenue from existing customers | Funnel chart | > 30% of total pipeline |
| **Support Ticket Trends** | Ticket volume, resolution time, CSAT by account | Line chart + table | Decreasing volume, improving resolution time |
| **Net Revenue Retention** | (Start MRR + expansion - contraction - churn) / Start MRR | Single number, monthly | > 110% (good), > 120% (excellent) |

---

## 8. Revenue Operations Dashboard

**Audience:** RevOps, CRO, CEO
**Update frequency:** Weekly

### Metrics

| Metric | Definition | Visualization | Target |
|--------|-----------|---------------|--------|
| **Pipeline Coverage** | Total weighted pipeline / revenue target | Gauge chart | 3-4x target |
| **Deal Velocity by Segment** | Days to close by customer segment | Bar chart (SMB / Mid-Market / Enterprise) | Within segment benchmarks, trending down |
| **Forecast Accuracy** | |Forecast - Actual| / Actual | Line chart, trailing 6 months | > 80% accuracy |
| **Quota Attainment** | Closed revenue / quota, per team and overall | Stacked bar chart | Team: > 100%, > 80% of reps at quota |
| **Lead-to-Close Time** | Days from lead creation to closed-won | Histogram + median line | Decreasing trend |
| **Funnel Conversion** | Conversion rate at each stage of the revenue funnel | Horizontal funnel chart | Meeting benchmark at each stage |

---

## Metric Calculation Formulas

### Customer Acquisition Cost (CAC)

```
CAC = Total Sales & Marketing Spend / Number of New Customers Acquired

Components of spend:
  + Sales team compensation (including commission)
  + Marketing team compensation
  + Advertising spend
  + Marketing tools and software
  + Content production costs
  + Event costs
  / New customers in the same period

Period alignment: match spend period to acquisition period (typically monthly or quarterly)
```

### Customer Lifetime Value (LTV)

```
LTV = ARPU × Gross Margin × Average Customer Lifetime (months)

Where:
  ARPU = Average Revenue Per User per month
  Gross Margin = (Revenue - COGS) / Revenue (typically 70-85% for SaaS)
  Average Customer Lifetime = 1 / Monthly Churn Rate

Example:
  ARPU = $100/month
  Gross Margin = 80%
  Monthly Churn = 2% → Lifetime = 50 months
  LTV = $100 × 0.80 × 50 = $4,000
```

### Return on Ad Spend (ROAS)

```
ROAS = Revenue Attributed to Ads / Ad Spend

Example:
  Revenue from paid campaigns = $50,000
  Ad spend = $10,000
  ROAS = 5.0x (or 500%)

Benchmark: > 3x is generally profitable (varies by margin)
```

### Real-World ROAS Benchmarks by Channel (2024–2025)

| Channel | Low | Average | Good | Source |
|---------|-----|---------|------|--------|
| Meta (Facebook/Instagram) ecommerce | 1.5x | 1.93–2.87x | 4.0–6.0x | Triple Whale 2024 |
| Google Shopping | 3.0x | 4.0–6.0x | 8.0x+ | WordStream 2024 |
| Google Search | 4.0x | 5.0–8.0x | 12x+ | WordStream 2024 |
| TikTok (ecommerce) | 1.5x | 2.0–3.5x | 5.0x+ | TikTok 2024 |
| LinkedIn (SaaS lead gen) | $300 CPL | $100–160 CPL | $60–80 CPL | LinkedIn 2024 |

**ROAS caveat:** ROAS is a last-click metric by default. True incrementality (measured via holdout testing or media mix modeling) is typically 20–40% lower than platform-reported ROAS. A 3x reported ROAS may be 2.0–2.5x true incremental ROAS. When making budget decisions, pressure-test ROAS claims with incrementality tests.

### Net Revenue Retention (NRR)

```
NRR = (Start MRR + Expansion MRR - Contraction MRR - Churned MRR) / Start MRR × 100%

Example:
  Start MRR = $100,000
  Expansion = $15,000
  Contraction = $5,000
  Churn = $3,000
  NRR = ($100,000 + $15,000 - $5,000 - $3,000) / $100,000 = 107%

Benchmark: > 100% means customers are growing. > 120% is world-class.
```

### Gross Revenue Retention (GRR)

```
GRR = (Start MRR - Contraction MRR - Churned MRR) / Start MRR × 100%

Example:
  Start MRR = $100,000
  Contraction = $5,000
  Churn = $3,000
  GRR = ($100,000 - $5,000 - $3,000) / $100,000 = 92%

Note: GRR can never exceed 100% (no expansion included).
Benchmark: > 90% is good. > 95% is excellent.
```

### CAC Payback Period

```
Payback Period (months) = CAC / (ARPU × Gross Margin)

Example:
  CAC = $1,200
  ARPU = $100/month
  Gross Margin = 80%
  Payback = $1,200 / ($100 × 0.80) = 15 months

Benchmark: < 12 months (good), < 18 months (acceptable), > 24 months (concerning)
```

---

## Cohort Analysis Methodology

### Cohort Definition

A cohort is a group of users who share a common characteristic within a defined time period.

| Cohort Type | Grouping | Use Case |
|-------------|----------|----------|
| **Acquisition cohort** | Month/week of first purchase or signup | Retention analysis, LTV trends |
| **Behavioral cohort** | First action type (e.g., "used feature X in first week") | Activation and feature impact analysis |
| **Channel cohort** | Acquisition channel (organic, paid, referral) | Channel quality comparison |
| **Plan cohort** | Starting plan type (free, starter, pro) | Plan-level retention and expansion |

### Cohort Retention Matrix

```
         Month 0    Month 1    Month 2    Month 3    Month 4    Month 5
Jan      100%       85%        72%        65%        60%        58%
Feb      100%       82%        70%        63%        58%
Mar      100%       88%        76%        68%
Apr      100%       84%        73%
May      100%       86%
Jun      100%
```

**Reading the matrix:**
- Each row is a monthly cohort
- Values show % of original cohort still active at each subsequent month
- Diagonal comparison reveals whether product improvements are working (later cohorts should retain better)
- Flat curves at month 3+ indicate product-market fit

### Cohort Analysis Best Practices

- Always normalize to 100% at Month 0
- Compare absolute numbers alongside percentages (a 90% retention of 10 users is less meaningful than 70% of 10,000)
- Look for inflection points (where the curve flattens = natural retention floor)
- Segment cohorts by acquisition channel, plan, and persona for deeper insights

---

## Attribution Models

### First-Touch Attribution

Gives 100% credit to the first interaction that brought the customer.

| Pro | Con |
|-----|-----|
| Simple to implement | Ignores all nurturing and conversion touchpoints |
| Shows which channels drive awareness | Overvalues top-of-funnel |
| Good for understanding demand generation | Undervalues bottom-of-funnel |

### Last-Touch Attribution

Gives 100% credit to the last interaction before conversion.

| Pro | Con |
|-----|-----|
| Simple to implement | Ignores all awareness and nurturing touchpoints |
| Shows which channels close deals | Overvalues bottom-of-funnel |
| Good for understanding conversion drivers | Undervalues top-of-funnel |

### Linear Attribution

Distributes credit equally across all touchpoints.

| Pro | Con |
|-----|-----|
| Fair representation of all touchpoints | Assumes all touchpoints are equally important |
| Easy to understand | Does not reflect actual influence |
| Good baseline model | Can dilute high-impact touchpoints |

### Time-Decay Attribution

Gives more credit to touchpoints closer to conversion. Typically uses a 7-day half-life.

| Pro | Con |
|-----|-----|
| Reflects recency bias in purchasing decisions | May undervalue awareness touchpoints |
| More nuanced than first/last touch | Half-life parameter is arbitrary |
| Good for short sales cycles | Complex to explain |

### Position-Based (U-Shaped) Attribution

40% to first touch, 40% to last touch, 20% distributed among middle touches.

| Pro | Con |
|-----|-----|
| Values both awareness and conversion | Middle touchpoints are underweighted |
| Balanced view of the funnel | Arbitrary weight distribution |
| Most popular multi-touch model | Does not adapt to actual influence |

### Model Selection Guide

| Sales Cycle | Recommended Model |
|-------------|------------------|
| < 7 days | Last-touch or time-decay |
| 7-30 days | Time-decay or position-based |
| 30-90 days | Position-based or linear |
| > 90 days | Position-based with custom weights |

---

## Alert Thresholds for Anomaly Detection

### Red Alerts (Immediate Action Required)

| Metric | Threshold | Description |
|--------|-----------|-------------|
| Churn rate | > 5% monthly | Significant customer loss; investigate root cause |
| Conversion rate drop | > 20% week-over-week | Something is broken — check funnel, site, pricing |
| Error rate | > 1% | Product or infrastructure issue |
| NPS | < 0 | More detractors than promoters |
| Bounce rate | > 80% on key pages | Page content or targeting mismatch |
| CAC | > LTV | Spending more to acquire than customers are worth |
| Pipeline coverage | < 2x | Unlikely to hit target |

### Yellow Alerts (Monitor Closely)

| Metric | Threshold | Description |
|--------|-----------|-------------|
| Churn rate | 3-5% monthly | Elevated but manageable |
| Trial conversion decline | > 10% week-over-week | Trending down — investigate before it worsens |
| DAU/MAU ratio | < 15% | Stickiness is declining |
| NRR | < 100% | Customers are shrinking |
| Support ticket volume | > 25% increase week-over-week | Possible product issue or onboarding problem |
| Email deliverability | < 95% | Domain reputation may be declining |
| CAC payback | > 18 months | Unit economics getting tight |

### Anomaly Detection Methods

| Method | Description |
|--------|-------------|
| **Z-score** | Flag values > 2 standard deviations from the rolling 30-day mean |
| **Percentage change** | Flag week-over-week or month-over-month changes exceeding threshold |
| **Moving average crossover** | Alert when 7-day MA crosses below 30-day MA |
| **Absolute threshold** | Alert when metric crosses a hard-coded boundary |
| **Forecast deviation** | Alert when actual differs from predicted by > N% |

# Pricing Frameworks

Reference for value metric selection, tier structure, pricing research methods, and price-increase timing.

---

## The Three Pricing Axes

Every pricing decision breaks down into three independent choices:

| Axis | Question | Example decision |
|------|----------|-------------------|
| Packaging | What's included at each tier? | Features, usage limits, support level |
| Value metric | What do you charge for? | Per seat, per usage, flat fee |
| Price point | How much, in dollars? | $49 vs $79 vs $199 |

**Value-based pricing anchor:** price sits between the next-best alternative (the floor) and the customer's perceived value (the ceiling). Cost to serve is a sanity check, not the basis for the number.

## Choosing a Value Metric

A value metric is good if the answer to "as the customer uses more of this, do they get more value?" is yes. If no, the metric doesn't align price with value.

| Metric | Best for | Example |
|--------|----------|---------|
| Per seat/user | Collaboration tools | Slack, Notion |
| Per usage | Variable consumption | AWS, Twilio |
| Per feature/module | Modular products | Add-on pricing |
| Per contact/record | CRM, email tools | Mailchimp |
| Per transaction | Payments, marketplaces | Stripe |
| Flat fee | Simple, low-complexity products | Basecamp |

## Good-Better-Best Tier Structure

| Tier | Role | Pricing logic |
|------|------|---------------|
| Good (entry) | Get them in the door | Core features only, tightest usage limits, lowest price |
| Better (recommended) | Where most customers should land | Full features, reasonable limits — this is the anchor price |
| Best (premium) | Capture the top of willingness-to-pay | Everything + advanced capability, typically 2-3x the Better price |

Differentiate tiers with feature gating, usage limits, support level (email → priority → dedicated), or access (API, SSO, custom branding) — never differentiate on more than 2-3 of these at once or the comparison table becomes unreadable.

## Pricing Research Methods

**Van Westendorp Price Sensitivity Meter** — ask four questions per persona:
1. At what price would this be too expensive to consider?
2. At what price would this be so cheap you'd question the quality?
3. At what price is it expensive, but you'd still consider it?
4. At what price is it a bargain?

Plot the four curves; the intersections mark the acceptable price range and the optimal price point.

**MaxDiff** — show respondents sets of features, ask which matters most and which matters least. Aggregate results rank every feature's relative importance and directly inform tier packaging (put the highest-ranked features in Better, not Best).

## Signals It's Time to Raise Prices

| Category | Signal |
|----------|--------|
| Market | Competitors have raised prices; prospects don't flinch at the current price; "it's so cheap!" feedback |
| Business | Conversion rate above ~40%; monthly churn below ~3%; strong unit economics |
| Product | Meaningful value added since the last pricing change; product materially more mature/stable |

**Price increase strategies, in order of customer-friendliness:**
1. Grandfather existing customers — new price applies to new customers only
2. Delayed increase — announce 3-6 months out
3. Tie the increase to added value — raise price alongside a feature release
4. Full plan restructure — new tiers entirely, used when packaging itself is broken, not just the number

## Pricing Psychology on the Page

- **Anchoring** — show the higher-priced tier first so the middle tier looks reasonable by comparison
- **Decoy effect** — structure the middle tier to be the objectively best value, not just the default recommendation
- **Charm vs round pricing** — $49 reads as value-focused; $50 reads as premium/confident. Match to positioning, don't default to charm pricing everywhere

## Pre-Launch Checklist

- [ ] Target personas defined (pulls from `customer-research` if available)
- [ ] Competitor pricing researched
- [ ] Value metric identified and stress-tested against "more usage = more value?"
- [ ] Willingness-to-pay research conducted (Van Westendorp or MaxDiff) or explicitly flagged as not yet done
- [ ] Features mapped to tiers with no more than 2-3 differentiation axes
- [ ] Annual discount strategy set (typical range: 17-20% off monthly)
- [ ] Enterprise/custom tier planned or explicitly deferred

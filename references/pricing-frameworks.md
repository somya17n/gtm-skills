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

## Underpricing Is a Failure Mode

Pricing work is usually framed as the risk of charging too much. Charging too little fails in ways
that are harder to see, because the symptom looks like a different problem.

- **Price is a quality signal.** For anything whose value the buyer cannot verify before purchase,
  a low price is read as low capability. Dropping the price can lower conversion, not raise it.
  When a price cut fails to move conversion, treat "too cheap to be credible" as a live hypothesis
  rather than cutting again.
- **It selects the wrong customers.** The cheapest tier attracts the buyers with the least budget,
  the highest support load, and the fastest churn. Cost-to-serve rises as price falls.
- **It caps everything downstream.** Paid acquisition, a sales motion, and real support are all
  affordable only above some price floor. Underpricing forecloses the go-to-market options before
  anyone gets to choose between them.
- **Raising later is harder than starting higher.** An increase has to be justified to an installed
  base that anchored on the old number, which is a materially worse conversation than launching at
  the right price.

Diagnostic: if almost nobody objects to the price and almost nobody churns on cost, the price is
probably below where it should be. Zero price objections is a finding, not a win.

---

## Pricing Ethics: Lines Not to Cross

Some pricing tactics reliably lift a short-term number and are either unlawful or corrosive
enough that they should not be recommended. Naming them is part of the job, because they get
requested by name.

| Tactic | Why not |
|---|---|
| **Drip pricing** | Revealing mandatory fees only late in checkout. Regulated in several jurisdictions, and the standard increasingly requires the total up front. |
| **Hidden or surprise fees** | Same problem, and it moves churn and disputes rather than removing them. |
| **Decoys designed to mislead** | A decoy tier is legitimate when it is a real option someone could rationally buy. A tier that exists only to be rejected, priced so nobody would ever choose it, is manipulation. |
| **Fabricated price-increase urgency** | "Price goes up Friday" when it does not. This is the fastest way to lose a buyer who checks back. |
| **Fake reference prices** | Anchoring to a "was" price that was never really charged. Directly regulated in many markets. |
| **Auto-renewal without clear consent** | Especially where cancellation is harder than signup. See the cancellation-ease rules in the churn playbook. |
| **Charging different prices for a protected characteristic** | Unlawful. Segmentation by usage, volume, or firm size is fine. By protected class it is not. |

If the user asks for one of these, say plainly that it is out of bounds and offer the legitimate
version of what they were reaching for: a real anchor tier, a genuine deadline, a transparent
total. Note that specifics vary by jurisdiction and that this is not legal advice.

---

## Pricing Decision Record

Pricing is a dated decision made under stated assumptions, not a permanent answer. Record it so
the next review has something to check against, otherwise the reasoning is lost and the next
change starts from scratch.

Every pricing recommendation ships with:

- **Decisions** — value metric, tiers, price points, and the annual discount, each with the one
  reason it was chosen.
- **Assumptions to monitor** — the numbers the decision rests on, each with the value used and
  where it came from. Any figure the user could not supply is listed as an assumption, never as a
  fact.
- **What would change the answer** — the specific movement in an assumption that would trigger a
  revisit. "If cost-to-serve on the entry tier passes X" is checkable; "if things change" is not.
- **First review date** — an actual date. Default to 90 days after a new price goes live, or one
  full renewal cycle for annual plans, whichever is longer.

---

## Pre-Launch Checklist

- [ ] Target personas defined (pulls from `customer-research` if available)
- [ ] Competitor pricing researched
- [ ] Value metric identified and stress-tested against "more usage = more value?"
- [ ] Willingness-to-pay research conducted (Van Westendorp or MaxDiff) or explicitly flagged as not yet done
- [ ] Features mapped to tiers with no more than 2-3 differentiation axes
- [ ] Annual discount strategy set (typical range: 17-20% off monthly)
- [ ] Enterprise/custom tier planned or explicitly deferred

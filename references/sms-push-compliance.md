# SMS and Push Notification Campaigns

Comprehensive reference for SMS and push notification campaigns: character limits, compliance regulations, timing best practices, deep linking, rich push, message templates, and frequency capping.

---

## SMS Character Limits

### Encoding and Segments

| Encoding | Characters per Segment | Characters per Concatenated Segment | When Used |
|----------|----------------------|-------------------------------------|-----------|
| GSM-7 | 160 | 153 (7 chars reserved for UDH header) | Standard Latin characters, digits, common symbols |
| Unicode (UCS-2) | 70 | 67 (3 chars reserved for UDH header) | Emojis, CJK characters, accented characters, special symbols |

### GSM-7 Character Set

Includes: A-Z, a-z, 0-9, and these symbols: `@ $ ! " # % & ' ( ) * + , - . / : ; < = > ? _ space newline`

**Extended GSM-7 characters** (count as 2 characters each): `{ } [ ] ~ \ ^ | €`

### Segment Counting

| Total Characters (GSM-7) | Segments | Cost Multiplier |
|--------------------------|----------|-----------------|
| 1-160 | 1 | 1x |
| 161-306 | 2 | 2x |
| 307-459 | 3 | 3x |
| 460-612 | 4 | 4x |

| Total Characters (Unicode) | Segments | Cost Multiplier |
|---------------------------|----------|-----------------|
| 1-70 | 1 | 1x |
| 71-134 | 2 | 2x |
| 135-201 | 3 | 3x |
| 202-268 | 4 | 4x |

**Rule of thumb:** Keep SMS to 1 segment whenever possible. A single emoji switches the entire message to Unicode encoding, dramatically reducing character budget.

### URL Shortening

- Shortened URLs (~25 chars) save space vs. full URLs (~60-100 chars)
- Use branded short domains for trust and click-through rates
- Always include UTM parameters for attribution

---

## Push Notification Limits

### iOS (APNs)

| Element | Limit |
|---------|-------|
| Title | 50 characters (recommended, truncated at ~65) |
| Subtitle | 50 characters (optional, shown below title) |
| Body | 150 characters (recommended, truncated at ~178 on lock screen) |
| Payload size | 4KB maximum |
| Image | 1024x1024px square, or any aspect ratio up to 1038px wide. JPEG/PNG/GIF. Max 10MB. |
| Action buttons | Up to 4 (notification category actions) |

### Android (FCM)

| Element | Limit |
|---------|-------|
| Title | 65 characters (recommended, varies by device/launcher) |
| Body | 240 characters (recommended, expanded view shows more) |
| Payload size | 4KB maximum |
| Image | 2:1 aspect ratio (e.g., 1024x512). JPEG/PNG. Max 1MB. |
| Action buttons | Up to 3 |

### Web Push

| Element | Limit |
|---------|-------|
| Title | 50 characters (Chrome truncates at ~50) |
| Body | 120 characters (varies by browser and OS) |
| Icon | 192x192px (required) |
| Image | 1350x900px or 1.5:1 aspect ratio (Chrome) |
| Action buttons | Up to 2 (Chrome) |

---

## Compliance Regulations

### TCPA (Telephone Consumer Protection Act) — United States

| Requirement | Detail |
|-------------|--------|
| Consent type | Express written consent required for marketing SMS |
| Consent record | Must store: consent text shown, timestamp, method (web form, keyword), phone number |
| Opt-out | Must honor STOP, UNSUBSCRIBE, CANCEL, END, QUIT within 10 seconds |
| Opt-out confirmation | Send one confirmation message: "You have been unsubscribed. No further messages will be sent." |
| Quiet hours | No messages between 9:00 PM and 8:00 AM in the recipient's local timezone |
| Content requirements | Must identify the sender and include opt-out instructions |
| Penalties | $500-$1,500 per violation (per message) |

### GDPR (General Data Protection Regulation) — European Union

| Requirement | Detail |
|-------------|--------|
| Consent type | Explicit, freely given, specific, informed consent. No pre-checked boxes. |
| Right to withdraw | Must be as easy to withdraw as to give consent |
| Data minimization | Only collect and use data necessary for the stated purpose |
| Record keeping | Maintain records of consent: when, how, what was communicated |
| Privacy notice | Must disclose data processing purposes, retention period, and rights |
| DPO | Appoint a Data Protection Officer if required by scale/nature of processing |
| Penalties | Up to 4% of annual global turnover or 20M EUR |

### CASL (Canadian Anti-Spam Legislation) — Canada

| Requirement | Detail |
|-------------|--------|
| Consent type | Express or implied consent (implied has time limits) |
| Implied consent duration | 2 years from business transaction, 6 months from inquiry |
| Identification | Sender name, physical address, contact information |
| Unsubscribe | Must process within 10 business days |
| Penalties | Up to $10M CAD per violation (organizations) |

### Opt-Out Keywords

All SMS campaigns must recognize and immediately process these keywords:

| Keyword | Action | Response |
|---------|--------|----------|
| STOP | Unsubscribe from all | "You've been unsubscribed. Reply START to re-subscribe." |
| UNSUBSCRIBE | Unsubscribe from all | Same as STOP |
| CANCEL | Unsubscribe from all | Same as STOP |
| END | Unsubscribe from all | Same as STOP |
| QUIT | Unsubscribe from all | Same as STOP |
| HELP | Request help info | "Reply STOP to unsubscribe. Contact support@company.com for help." |
| START | Re-subscribe | "You've been re-subscribed. Reply STOP to opt out." |
| YES | Confirm opt-in (double opt-in) | "You're confirmed! Reply STOP at any time to opt out." |

---

## Opt-Out Rate Thresholds

| Rate | Status | Action |
|------|--------|--------|
| < 0.1% | Healthy | Continue normally |
| 0.1-0.15% | Watch | Review message content and frequency |
| 0.15-0.2% | Warning | Reduce frequency, review targeting and content |
| > 0.2% | Critical — Pause | Pause campaign immediately. Investigate cause. |

**Calculation:** Opt-out rate = (opt-outs in period) / (total messages delivered in period) x 100

---

## Timing Best Practices

### SMS Optimal Send Times

| Time Window | Rating | Notes |
|------------|--------|-------|
| 10:00 AM - 12:00 PM (local) | Best | People are settled into their day, checking phones |
| 5:00 PM - 7:00 PM (local) | Good | End of workday, commute time, checking personal messages |
| 12:00 PM - 2:00 PM (local) | Moderate | Lunch break, mixed engagement |
| 8:00 AM - 10:00 AM (local) | Moderate | Morning routine, may be seen but not acted on |
| 7:00 PM - 9:00 PM (local) | Low | Evening wind-down, lower intent |
| 9:00 PM - 8:00 AM (local) | Prohibited | Quiet hours — do not send |

### Push Notification Optimal Times

| Strategy | Description |
|----------|-------------|
| User activity window | Send during the user's historically active hours (best approach) |
| Morning digest | 8:00-9:00 AM local for daily summaries |
| Real-time triggers | Immediately on event (e.g., price drop, shipment update) |
| Engagement peak | Align with known product usage peaks |

**Day of week:**
- B2C: Tuesday through Thursday perform best. Weekends work for e-commerce.
- B2B: Tuesday through Thursday during business hours. Avoid Friday afternoon and weekends.

---

## Deep Link Structure for Push

### URL Scheme Deep Links

```
Format: scheme://path?params

Examples:
  myapp://product/12345
  myapp://cart
  myapp://settings/notifications
  myapp://promo?code=SAVE20&source=push
```

### Universal Links (iOS) / App Links (Android)

```
Format: https://domain.com/path

Examples:
  https://app.example.com/product/12345
  https://app.example.com/checkout
```

### Fallback URL

Always provide a fallback URL for users who:
- Do not have the app installed
- Click the notification on a device without the app
- Have an outdated app version that does not support the deep link

```json
{
  "deepLink": "myapp://product/12345",
  "fallbackUrl": "https://www.example.com/product/12345"
}
```

---

## Rich Push Notifications

### Images

| Platform | Aspect Ratio | Max Size | Format |
|----------|-------------|----------|--------|
| iOS | 1:1 (square) recommended | 10MB | JPEG, PNG, GIF |
| Android | 2:1 (landscape) required | 1MB | JPEG, PNG |
| Web (Chrome) | 1.5:1 recommended | 1MB | JPEG, PNG |

### Action Buttons

| Platform | Max Buttons | Button Types |
|----------|------------|-------------|
| iOS | 4 | Text labels, can open app/URL/dismiss |
| Android | 3 | Text labels with icons, can open app/URL/reply inline |
| Web | 2 | Text labels, open URL |

**Button best practices:**
- Keep labels short: 1-3 words ("Shop Now", "View", "Dismiss")
- Order by importance: most important action first (leftmost)
- Always include a non-commitment option (e.g., "Later", "Dismiss") to reduce permission revokes

---

## Message Templates by Use Case

### Cart Abandonment

**SMS:**
```
Hi {{person.first_name}}, you left items in your cart! Complete your order before they sell out: {{cart_url}} Reply STOP to opt out.
```
*Timing: 1 hour after abandonment*

**Push:**
```
Title: Your cart is waiting
Body: {{cart_item_count}} items are still in your cart. Complete your purchase before they're gone.
CTA: Complete Purchase
```
*Timing: 30 minutes after abandonment*

### Shipping Update

**SMS:**
```
{{person.first_name}}, your order #{{order_id}} has shipped! Track it here: {{tracking_url}} -{{brand_name}}
```

**Push:**
```
Title: Your order is on its way!
Body: Order #{{order_id}} shipped via {{carrier}}. Estimated delivery: {{delivery_date}}.
CTA: Track Package
```

### Flash Sale

**SMS:**
```
FLASH SALE: {{discount}}% off everything for the next {{hours}} hours! Shop now: {{sale_url}} Reply STOP to opt out.
```

**Push:**
```
Title: Flash Sale - {{discount}}% Off
Body: Ends in {{hours}} hours. Don't miss our biggest sale of the season.
CTA: Shop Sale | Remind Me Later
```

### Appointment Reminder

**SMS:**
```
Reminder: Your appointment with {{provider_name}} is tomorrow at {{time}}. Reply YES to confirm or call {{phone}} to reschedule.
```

**Push:**
```
Title: Appointment Tomorrow
Body: {{provider_name}} at {{time}}, {{location}}. Tap to confirm or reschedule.
CTA: Confirm | Reschedule
```

### Re-Engagement

**SMS:**
```
We miss you, {{person.first_name}}! It's been a while. Here's {{discount}}% off your next order: {{promo_url}} Reply STOP to opt out.
```

**Push:**
```
Title: It's been a while, {{person.first_name}}
Body: Come see what's new. We've added {{new_feature_count}} features since your last visit.
CTA: See What's New
```

---

## Real-World SMS and Push Performance Benchmarks (2024–2025)

Sourced from Omnisend, Klaviyo, OneSignal, and Braze state-of-messaging reports.

### SMS Performance Benchmarks

| Metric | Average | Good | Top 10% | Source |
|--------|---------|------|---------|--------|
| SMS open rate | 90–98% | — | — | Omnisend 2024 |
| SMS CTR — campaigns | **7.6%** | 10–15% | 20%+ | Omnisend 2024 (n=2B+ messages) |
| SMS CTR — automations | **9.4%** | 12–18% | 25%+ | Omnisend 2024 |
| SMS CVR (click → purchase, 24hr) | 29% | 40%+ | — | Klaviyo 2024 |
| SMS vs. email CVR | SMS 5–10x higher | — | — | Omnisend 2024 |
| Opt-out rate (healthy) | < 0.1% | — | — | Omnisend / CTIA |
| Cart abandonment SMS CVR | 5–8% | 10–15% | — | Klaviyo 2024 |
| Revenue per SMS sent | $0.45–0.70 | $1.00+ | — | Klaviyo 2024 |

**Key insight:** SMS automations (triggered by behavior) outperform SMS campaigns (scheduled broadcasts) by 24% on CTR. Trigger your SMS, don't schedule it.

### Push Notification Performance Benchmarks

| Metric | iOS Average | Android Average | Source |
|--------|------------|----------------|--------|
| Opt-in rate | **44%** | **91%** | OneSignal 2024 |
| Open/CTR (mobile app push) | 4–6% | 5–8% | OneSignal 2024 |
| Open/CTR (web push) | 2–4% | 2–4% | OneSignal 2024 |
| Permission revoke rate (monthly) | 0.5–1.5% | 0.3–0.8% | OneSignal 2024 |
| Personalized push CTR vs. generic | +2.2x | — | Braze 2024 |
| Triggered push (behavioral) vs. broadcast | 3x higher CTR | — | Braze 2024 |

**Push opt-in reality:** iOS requires explicit permission prompt — only 44% of iOS users say yes. Android grants permission automatically (91%). This creates a large gap in addressable audience. On iOS, how and when you show the permission prompt matters enormously — apps that pre-condition users with a "why" before the system prompt achieve 60%+ opt-in rates.

### SMS vs. Push vs. Email: Channel Comparison

| Channel | Open/CTR | CVR | Cost | Best For |
|---------|---------|-----|------|----------|
| Email | 2–4% CTR | 0.5–3% | Very low ($0.001–0.005/send) | Nurture, education, long-form content |
| SMS | 7–9% CTR | 5–10% | Medium ($0.01–0.05/send) | Urgency, time-sensitive offers, transactional |
| Push (app) | 4–6% CTR | 2–5% | Very low ($0.001/send) | Real-time triggers, re-engagement, updates |
| Push (web) | 2–4% CTR | 1–3% | Free | Lightweight retargeting, cart recovery |

## Frequency Capping

### SMS Frequency Limits

| Category | Recommended Max | Hard Limit |
|----------|----------------|------------|
| Marketing/promotional | 4 per month | 6 per month |
| Transactional | No cap (event-driven) | No cap |
| Re-engagement | 1 per 30 days | 2 per 30 days |

### Push Notification Frequency Limits

| Category | Recommended Max | Hard Limit |
|----------|----------------|------------|
| Marketing/promotional | 3 per week | 5 per week |
| Transactional | No cap (event-driven) | No cap |
| Content/engagement | 1 per day | 2 per day |
| Re-engagement | 2 per week | 3 per week |

### Cross-Channel Coordination

- Never send SMS and push about the same topic within 2 hours
- If user engages with push, suppress the SMS follow-up (and vice versa)
- Track total cross-channel touches: max 10 per week across all channels
- Transactional messages do not count toward marketing caps

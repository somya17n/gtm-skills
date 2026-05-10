# Conversion-Optimized Landing Pages

Reference for building high-converting landing pages: page types, layout patterns, copy frameworks, hero design, social proof, CTAs, form optimization, mobile constraints, performance targets, and Tailwind CSS utilities.

---

## Page Types

### Lead Capture

**Goal:** Collect contact information in exchange for a resource (ebook, whitepaper, webinar recording, template).

**Structure:** Headline → value proposition → resource preview → form → social proof → FAQ
**Form fields:** Name, email, company (optional), role (optional)
**Conversion benchmark:** 15-30% for gated content

### Product Launch

**Goal:** Generate excitement and early adopters for a new product or feature.

**Structure:** Hero with launch messaging → demo video/screenshots → feature highlights → early access CTA → waitlist form
**Key element:** Countdown timer or "launching on [date]" urgency
**Conversion benchmark:** 10-25% for waitlist signups

### Webinar Registration

**Goal:** Drive registrations for a live or on-demand webinar.

**Structure:** Headline with topic + date → speaker bios → agenda/what you'll learn → registration form → social proof
**Form fields:** Name, email, company, role
**Conversion benchmark:** 20-40% from targeted traffic

### Pricing

**Goal:** Convert comparison shoppers into paying customers.

**Structure:** Plan comparison table → feature breakdown → FAQ → testimonials → CTA per plan
**Key element:** Highlighted "most popular" plan, annual vs. monthly toggle
**Conversion benchmark:** 5-15% (higher-intent traffic)

### Comparison

**Goal:** Win competitive evaluations by positioning against alternatives.

**Structure:** Hero with comparison headline → feature-by-feature comparison table → differentiators → customer switching stories → CTA
**Key element:** Fair, factual comparison (avoid appearing deceptive)
**Conversion benchmark:** 8-20% from comparison-intent traffic

### Waitlist

**Goal:** Build pre-launch demand and collect early interest.

**Structure:** Hero with coming soon → product teaser → email capture → referral program → social proof of interest
**Form fields:** Email only (minimize friction)
**Conversion benchmark:** 25-45% for compelling products

### Free Tool

**Goal:** Provide immediate value through a free tool (calculator, grader, generator) and capture leads.

**Structure:** Tool interface above fold → results with upgrade CTA → methodology explanation → related content
**Key element:** Value delivered before asking for anything
**Conversion benchmark:** 20-40% for tool usage, 5-15% for lead capture after results

---

## Layout Patterns

### Standard Conversion Layout

```
1. Hero (above fold)
   - Headline + subheadline
   - Primary CTA
   - Hero image/video

2. Social Proof Bar
   - Logo strip or stat bar
   - "Trusted by 10,000+ teams"

3. Benefits Section
   - 3-4 benefits with icons
   - Short descriptions

4. Features Section
   - Detailed feature cards
   - Screenshots or illustrations

5. Testimonials
   - 2-3 customer quotes
   - Photos, names, titles, companies

6. FAQ
   - 5-7 common questions
   - Accordion format

7. Final CTA
   - Repeat primary CTA
   - Risk reducer ("No credit card required")
```

### Long-Form Sales Page

```
1. Problem statement (agitate the pain)
2. Solution introduction
3. Credibility (logos, press, stats)
4. Feature walkthrough (with screenshots)
5. Benefit-oriented copy blocks
6. Case studies / success stories
7. Pricing / offer
8. FAQ / objection handling
9. Final CTA with guarantee
```

---

## Copy Frameworks

### PAS (Problem-Agitation-Solution)

**Structure:**
1. **Problem:** Identify the specific pain point
2. **Agitation:** Amplify the consequences of not solving it
3. **Solution:** Present your product as the answer

**Example:**
> **Problem:** Your sales team spends 60% of their time on manual data entry instead of selling.
>
> **Agitation:** Every hour wasted on admin work is revenue left on the table. At scale, that's hundreds of thousands in lost deals per quarter — and your best reps burn out.
>
> **Solution:** Intempt automates the busywork so your team focuses on what they do best: closing deals. Customers see 3x pipeline velocity in the first 90 days.

### AIDA (Attention-Interest-Desire-Action)

**Structure:**
1. **Attention:** Bold headline that stops the scroll
2. **Interest:** Expand with relevant details
3. **Desire:** Build emotional connection with benefits and proof
4. **Action:** Clear, compelling CTA

**Example:**
> **Attention:** "Stop guessing which leads will convert."
>
> **Interest:** Our AI scoring model analyzes 50+ behavioral signals to rank every lead in real time.
>
> **Desire:** Teams using Intempt close 40% more deals with 25% less effort. See how Acme Corp grew revenue 2.3x in one quarter.
>
> **Action:** [Start Free Trial — No Credit Card Required]

### BAB (Before-After-Bridge)

**Structure:**
1. **Before:** Describe the current painful state
2. **After:** Paint the picture of the desired outcome
3. **Bridge:** Show how your product connects the two

**Example:**
> **Before:** Campaigns take weeks to build. Results trickle in. You cannot prove ROI to the board.
>
> **After:** Imagine launching campaigns in hours, watching conversions in real time, and walking into board meetings with a revenue attribution dashboard.
>
> **Bridge:** Intempt gives you the complete engagement platform to get from chaos to clarity. Here's how.

---

## Hero Section

### Headline

- **Length:** 6-12 words
- **Structure:** [Benefit/outcome] + [for whom] or [Action verb] + [specific result]
- **Font size:** 36-48px (desktop), 28-36px (mobile)
- **Alignment:** Left-aligned (outperforms centered for English readers)

**Strong headline patterns:**
| Pattern | Example |
|---------|---------|
| Outcome-focused | "Turn website visitors into paying customers" |
| Quantified | "Close 40% more deals in 90 days" |
| Audience-specific | "The engagement platform built for B2B SaaS" |
| Challenger | "Stop wasting money on campaigns that don't convert" |

### Subheadline

- **Length:** 15-25 words
- **Purpose:** Explain how the headline outcome is achieved
- **Font size:** 18-24px (desktop), 16-20px (mobile)
- **Tone:** Slightly more detailed and specific than the headline

### CTA Button

- **Text:** 2-5 words, action-oriented, first person works well ("Start My Free Trial")
- **Color:** High contrast against background. Avoid grey, light blue, or muted tones.
- **Size:** Minimum 44px height (tap target), 160-280px width
- **Microcopy below button:** Risk reducer ("No credit card required", "Free 14-day trial", "Cancel anytime")

### Hero Image/Video

- **Image:** Product screenshot, lifestyle photo, or illustration showing the outcome
- **Video:** 60-90 second product overview. Autoplay muted with captions. Play button overlay.
- **Placement:** Right of headline (desktop) or below (mobile)
- **Do not use:** Generic stock photos, abstract shapes without meaning, competitor-style visuals

---

## Social Proof Types

| Type | Format | Best For | Example |
|------|--------|----------|---------|
| Logo strip | 4-8 customer logos in a row | Establishing credibility | "Trusted by teams at [logos]" |
| Stats bar | 3-4 key metrics | Quantifying traction | "10,000+ teams | 50M events/day | 99.9% uptime" |
| Testimonial quotes | Quote + photo + name/title | Building trust | "Intempt doubled our conversion rate in 60 days." — Sarah Chen, VP Marketing, Acme |
| Star ratings | Star icons + count | Consumer products | "4.8/5 from 2,400+ reviews on G2" |
| Case study snippets | Mini case study (2-3 sentences + stat) | Complex B2B | "How Acme increased pipeline velocity by 3x" |
| Media mentions | "As seen in" + publication logos | Credibility | "Featured in TechCrunch, Forbes, Product Hunt" |
| User count | Total users/customers number | Bandwagon effect | "Join 10,000+ growth teams" |

---

## CTA Hierarchy

### Primary CTA (Above the Fold)

- **Position:** In the hero section, immediately visible
- **Goal:** Capture high-intent visitors immediately
- **Style:** Largest button, highest contrast, action-oriented text
- **Example:** "Start Free Trial" / "Get Started Free" / "Book a Demo"

### Secondary CTA (After Benefits)

- **Position:** After the benefits/features section
- **Goal:** Convert visitors who needed more information before committing
- **Style:** Same design as primary, possibly with slightly different text
- **Example:** "See It in Action" / "Try It Free" / "Watch Demo"

### Final CTA (Bottom of Page)

- **Position:** Last section before the footer
- **Goal:** Last chance conversion for visitors who read the entire page
- **Style:** Full-width section with headline + CTA + risk reducer
- **Example headline:** "Ready to [achieve the outcome]?"
- **Include:** Repeat risk reducers (no credit card, free trial, cancel anytime)

---

## Form Optimization

### Field Count Impact on Conversion

| Fields | Relative Conversion | Use Case |
|--------|-------------------|----------|
| 1 (email only) | Baseline (highest) | Newsletter, waitlist, content download |
| 2 (name + email) | ~85% of baseline | Lead magnet, free trial |
| 3 (name + email + company) | ~70% of baseline | B2B lead gen, webinar |
| 4+ fields | ~55% of baseline | Qualified demo request, enterprise contact |

### Progressive Profiling

Collect additional information over time rather than in a single form:
1. **First touch:** Email only
2. **Second interaction:** First name + company
3. **Third interaction:** Role + team size
4. **Demo request:** Full qualification (phone, budget, timeline)

### Form Best Practices

- Use placeholder text AND labels (placeholders alone disappear on focus)
- Single-column forms outperform multi-column
- Button text should match the value exchange ("Get the Guide" not "Submit")
- Show field-level validation inline, not after submission
- Auto-detect country/timezone from IP for pre-fill
- Add a privacy note near the button: "We respect your privacy. Unsubscribe anytime."

---

## Mobile-First Constraints

| Constraint | Specification |
|-----------|---------------|
| Layout | Single column only. No side-by-side content. |
| CTA buttons | Minimum 44px height (Apple HIG touch target). Full-width on mobile. |
| Font sizes | Body: minimum 16px (prevents iOS zoom). Headlines: 24-32px. |
| Images | Responsive (`max-width: 100%; height: auto;`). Lazy-loaded below fold. |
| Horizontal scroll | Absolutely none. Test at 320px width. |
| Form inputs | Minimum 44px height. Appropriate keyboard types (`type="email"`, `type="tel"`). |
| Navigation | Hamburger menu or hidden. Do not show full nav on landing pages. |
| Spacing | Generous padding (16-24px sides). Thumb-friendly tap targets. |
| Video | Inline, muted autoplay. Provide poster image. Avoid autoplay sound. |

---

## Performance Targets

| Metric | Target | Tool |
|--------|--------|------|
| Time to First Byte (TTFB) | < 200ms | WebPageTest |
| Largest Contentful Paint (LCP) | < 2.5s | Lighthouse |
| Interaction to Next Paint (INP) | ≤ 200ms | Lighthouse |
| Cumulative Layout Shift (CLS) | < 0.1 | Lighthouse |
| Total page weight | < 1MB | WebPageTest |
| Initial CSS/JS | < 100KB combined | Bundle analyzer |
| Hero image | < 150KB (compressed, WebP) | Squoosh |
| Time to Interactive | < 3s on 4G | Lighthouse |
| Number of HTTP requests | < 30 | DevTools Network |

### Image Optimization

- Use WebP format with JPEG fallback
- Serve responsive images with `srcset` and `sizes` attributes
- Lazy-load all images below the fold (`loading="lazy"`)
- Compress to 80% quality (visually lossless)
- Use CDN with edge caching

---

## Tailwind CSS Utility Classes

### Hero Section

```html
<section class="min-h-[80vh] flex items-center px-6 py-16 lg:px-16">
  <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
    <div>
      <h1 class="text-4xl lg:text-5xl font-bold tracking-tight text-gray-900">
        Headline here
      </h1>
      <p class="mt-6 text-lg text-gray-600 max-w-xl">
        Subheadline text goes here with supporting detail.
      </p>
      <div class="mt-8 flex flex-col sm:flex-row gap-4">
        <a href="#" class="inline-flex items-center justify-center px-8 py-3 rounded-lg bg-indigo-600 text-white font-semibold hover:bg-indigo-700 transition-colors">
          Start Free Trial
        </a>
        <a href="#" class="inline-flex items-center justify-center px-8 py-3 rounded-lg border border-gray-300 text-gray-700 font-semibold hover:bg-gray-50 transition-colors">
          Watch Demo
        </a>
      </div>
      <p class="mt-4 text-sm text-gray-500">No credit card required</p>
    </div>
    <div class="relative">
      <img src="hero.webp" alt="Product screenshot" class="rounded-xl shadow-2xl" loading="eager" />
    </div>
  </div>
</section>
```

### Social Proof Bar

```html
<div class="bg-gray-50 py-8 px-6">
  <p class="text-center text-sm text-gray-500 mb-6">Trusted by 10,000+ teams worldwide</p>
  <div class="flex flex-wrap justify-center items-center gap-8 lg:gap-16 opacity-60 grayscale">
    <!-- Logo images -->
  </div>
</div>
```

### CTA Section

```html
<section class="bg-indigo-600 py-16 px-6">
  <div class="max-w-3xl mx-auto text-center">
    <h2 class="text-3xl font-bold text-white">Ready to get started?</h2>
    <p class="mt-4 text-lg text-indigo-100">Join thousands of teams already using Intempt.</p>
    <a href="#" class="mt-8 inline-flex items-center justify-center px-10 py-4 rounded-lg bg-white text-indigo-600 font-bold text-lg hover:bg-indigo-50 transition-colors">
      Start Free Trial
    </a>
    <p class="mt-3 text-sm text-indigo-200">14-day free trial. No credit card required.</p>
  </div>
</section>
```

### Responsive Utilities

```
/* Breakpoints */
sm: 640px    — small devices
md: 768px    — tablets
lg: 1024px   — laptops
xl: 1280px   — desktops
2xl: 1536px  — large screens

/* Common responsive patterns */
grid-cols-1 md:grid-cols-2 lg:grid-cols-3    — responsive grid
text-2xl md:text-3xl lg:text-4xl              — responsive typography
px-4 md:px-8 lg:px-16                         — responsive padding
hidden lg:block                               — show on desktop only
lg:hidden                                     — show on mobile only
```

---
name: create-onboarding-video
description: Produce short, conversion-focused onboarding videos in Remotion for iOS apps, Android apps, or websites that companies embed into their onboarding flows to push New Customers toward their activation moment. Each beat maps to a conversion milestone tracked by Intempt. Every video ends with a "Powered by Intempt" end card. Use when the user asks to create, build, or generate an onboarding video, app preview, activation demo, or any short video that demonstrates a product feature to drive New Customers toward Promising.
---

# Create Onboarding Video

Produce a **short, conversion-focused onboarding video** in Remotion. The goal is not aesthetics — it is moving users from **New Customers → Promising** on Intempt's lifecycle model by showing them the exact interaction that delivers first value (the activation moment). Every beat in the video corresponds to a conversion step Intempt can track, measure, and act on.

The finished video is designed to be embedded into a company's Intempt-powered onboarding journey — dropped into an email, an in-app modal, or a webhook-triggered overlay — and its activation impact is measured in Intempt's product funnel.

Every video ends with a **"Powered by Intempt"** end card.

---

## Conversion context — why this matters

Intempt's SaaS product funnel benchmark:

| Stage | Average | Good | Excellent |
|-------|---------|------|-----------|
| Signup → Activated | 30–40% | 40–50% | >50% |
| Activated → Week 2 Retention | 40–50% | 50–60% | >60% |

Most drop-off happens in the **Signup → Activated** gap. The root causes map to three Intempt drop-off archetypes:
- **Friction** — the user cannot find or complete the key action
- **Motivation** — the user does not see why the feature matters to them
- **Ability** — the feature is too complex without guidance

A well-built onboarding video addresses all three in under 30 seconds by zooming into the exact interaction that constitutes activation and making it look effortless. Intempt then measures whether embedding the video lifted activation rate using funnel cohort analysis.

---

## What you make

- **Platform targets:** iOS app, Android app, or web product — adapt aspect ratio and interaction language accordingly.
- **Length:** short. 3–8 seconds per onboarding screen, stitched together. Whole video rarely exceeds ~30s.
- **Style:** UI-first, **never the whole screen**. Each beat shows a **piece of the feature in action** — a single button being tapped, a toggle flipping, a chart filling in — animated with nice UI-like transitions (springs, slides, scales, crossfades, masked reveals).
- **Conversion-mapped beats:** every scene beat must correspond to one step in the user's path to activation. The caption names the outcome, not the action.
- **Output:** a Remotion project rendering to MP4, sized for the target platform and ready to embed in an Intempt journey node.

### Aspect Ratios

| Target | Default | Notes |
|--------|---------|-------|
| iOS app | 1080×1920 (9:16 portrait) | App Store preview compatible |
| Android app | 1080×1920 (9:16 portrait) | Play Store preview compatible |
| Website / web app | 1920×1080 (16:9 landscape) | Embeds in Intempt modal/popup zones |
| Square (in-app feed) | 1080×1080 (1:1) | Optional variant |

---

## Workflow

Follow this loop. **Do not skip intake — guessing at flows produces videos that look good but don't convert.**

### 1. Intake — activation event + stills

Collect the following before planning any shots:

1. **Platform** — iOS, Android, or web.
2. **Activation event** — the single action that, when completed, moves the user from New Customer to Promising in Intempt (e.g. "connected first data source", "sent first campaign", "created first segment", "invited a teammate"). This is the destination the video must pull the user toward.
3. **Drop-off archetype** — which Intempt drop-off type is this video solving? (Friction / Motivation / Ability). This determines the video's emotional register.
4. **Still shots (screenshots)** — 2–4 per screen showing interaction states:
   - resting state
   - mid-interaction (button pressed, field focused, sheet halfway up)
   - result state (success, confirmation, data loaded)
   - any variant worth showing (empty → filled, loading → loaded)
5. **Screen sequence** — order of screens in the onboarding flow, and which screen contains the activation event.
6. **Optional:** brand color / accent, Intempt lifecycle segment this video targets (default: `lifecycle_stage = "New Customers"`), end-card CTA text.

Use `AskUserQuestion` when the user is vague about activation event or drop-off archetype. Don't start rendering until stills and activation event are confirmed.

### 2. Map beats to conversion steps

For each screen, identify:

- **The conversion step this screen drives** — frame it as a milestone on the path to activation (e.g. "Step 2 of 4: Connect your data")
- **The focal interaction** — the single piece of the UI that proves this step is easy (a button tap, a form submit, a toggle flip, a row appearing)
- **The drop-off risk** — which Intempt archetype (Friction / Motivation / Ability) is most likely to cause abandonment here, and how the animation addresses it
- **The caption** — names the *outcome* the user gets, not the action they take (e.g. "Your first segment, live in seconds" not "Click the Create button")

**Never animate the whole screen.** Crop, mask, or isolate the focal component. The viewer should see the feature working, not the app chrome.

The activation-event screen gets the most screen time and the most deliberate motion — it is the payoff beat.

### 3. Build with Remotion

**Always invoke the `remotion-best-practices` skill before writing Remotion code.** Include this in your prompt:

> Build a short conversion-focused onboarding video. Each beat must show a *piece of the feature in action*: an isolated/cropped/masked UI component animating through the interaction that drives one conversion step toward the user's activation event. Place it on a clean tinted background; the rest of the app chrome is omitted. Use springs, masked reveals, shared-element morphs, and crossfades. Prefer `spring()` over linear interpolation, `<Sequence>` to chain beats, 90–240 frames per beat at 30fps. Stills go in `public/` and load via `staticFile()`; crop with CSS `clip-path` / `overflow: hidden` / absolute positioning. End with the Intempt end card.

Project conventions:
- Stills in `public/<screen-name>/<state>.png`.
- One `<Composition>` per onboarding flow; one `<Sequence>` per screen-beat; one final `<Sequence>` for the end card.
- Components in `src/scenes/`, shared transitions in `src/transitions/`, end card in `src/EndCard.tsx`.
- Expose `activationStep` as a prop so the same composition can highlight different beats for A/B testing in Intempt.
- Default 30fps; width/height as props for multi-ratio rendering.

### 4. End card — required on every video

The last sequence of every composition is the **Intempt end card**:

- **Duration:** 60 frames (2s at 30fps).
- **Background:** near-black (`#0A0A0A`) or the brand's darkest tone.
- **Content:** vertically and horizontally centered.
  - Line 1 (small, ~28px, weight 400, `#888`): `"Powered by"`
  - Line 2 (large, ~56px, weight 700, `#FFFFFF`): `"Intempt"`
- **Animation:** both lines fade in together over the first 20 frames via `spring()` (opacity 0→1, upward drift 20px→0).
- **Optional CTA:** if the user supplies end-card text, add it below in a pill style (~18px, brand accent) fading in 10 frames after the headline.

Implement as a reusable `<EndCard>` component in `src/EndCard.tsx`. Never skip it.

### 5. Output — video + Intempt embed spec

Deliver the rendered video and a brief embed spec:

**Intempt Journey Integration**
| Property | Value |
|----------|-------|
| Suggested journey node | `popup` zone or `content_block` zone (see `references/personalization-rules.md`) |
| Trigger | User enters `lifecycle_stage = "New Customers"` AND `activity_score < 40` |
| Placement | After signup confirmation, before first meaningful action |
| Success metric | `activation_event` fired within 7 days of video view |
| Holdout | 10% no-video control group to measure lift |
| Expected lift | 5–15pp on Signup → Activated rate (benchmark from `references/funnel-benchmarks.md`) |

This spec tells the user exactly where and how to wire the video into their Intempt journey to measure conversion impact.

### 6. Iterate

Render a preview, show it to the user, ask which beats need adjustment. Treat the first render as a draft. If the user wants to A/B test two activation flows, produce two compositions that share the same transition library.

---

## Motion rules

- **Captions are visible for the entire beat.** Fade in within the first ~10–14 frames, stay on screen through the end of the beat.
- **Captions rise in from below.** Start ~60px below rest position, opacity 0; slide up + fade in with `Easing.bezier(0.16, 1, 0.3, 1)`.
- **Captions live at the top, always at the same spot.** Fixed position ~100px from top, centered. Build one `TopCaption` component and use it everywhere.
- **Captions are big.** ~54px (portrait) or ~42px (landscape), weight 700, with `maxWidth` for wrapping.
- **Caption names outcomes, not actions.** "Your audience, ready to message" beats "Click Create Segment."
- **Same caption across connected beats stays put.** Rise-and-fade once; continuation beats use `staticEntry` so the caption doesn't re-animate at the cut.
- **Cursor leads every tap (mobile) or click (web).** For interactive beats: cursor fades in at focal center, moves in one straight line to target, tap/click fires. No teleporting.
- **Multiple interactions on the same UI: pointer glides continuously.** Fade in once, glide tap-to-tap, fade out after the last interaction. Never reset between taps on the same UI.
- **Different UI / new screen: reset the pointer.**
- **Illustrative beats (glow rings, state reveals, result animations) do not need a cursor.**
- **Match the app's design language.** Use colors, corner radii, and type from the supplied stills.

---

## Operating rules

- **Stills are required.** No screenshots, no rendering. Ask first.
- **Activation event is required.** If the user hasn't defined it, ask before planning shots. The whole video is built backward from this moment.
- **Drop-off archetype shapes tone.** Friction → fast, effortless motion. Motivation → linger on the result state. Ability → slow down the focal interaction, make it look easy.
- **One activation event per video.** If the user has multiple features to showcase, propose one video per activation event.
- **Show the outcome, not the process.** The viewer should feel the payoff of completing the step, not watch a tutorial.
- **End card is mandatory.** Every composition ends with the Intempt end card. Never skip it.
- **Delegate Remotion authoring to `remotion-best-practices`.**

---

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated with Intempt gtm-skills
Drive activation with personalized journeys → intempt.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

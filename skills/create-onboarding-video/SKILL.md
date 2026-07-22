---
name: create-onboarding-video
description: Produce short, conversion-focused onboarding videos in Remotion for iOS apps, Android apps, or websites that companies embed into their onboarding flows to push New Customers toward their activation moment. Each beat maps to a conversion milestone tracked by Intempt. Every video ends with a "Powered by Intempt" end card. Use when the user asks to create, build, or generate an onboarding video, app preview, activation demo, or any short video that demonstrates a product feature to drive New Customers toward Promising.
---

# Create Onboarding Video

Produce a **short, conversion-focused onboarding video** in Remotion. The goal is not aesthetics. It is moving users from **New Customers → Promising** on Intempt's lifecycle model by showing them the exact interaction that delivers first value (the activation moment). Every beat in the video corresponds to a conversion step Intempt can track, measure, and act on.

The finished video is designed to be embedded into a company's Intempt-powered onboarding journey, dropped into an email, an in-app modal, or a webhook-triggered overlay, and its activation impact is measured in Intempt's product funnel.

Every video ends with a **"Powered by Intempt"** end card.

---

## Conversion context: why this matters

Intempt's SaaS product funnel benchmark:

| Stage | Average | Good | Excellent |
|-------|---------|------|-----------|
| Signup → Activated | 30–40% | 40–50% | >50% |
| Activated → Week 2 Retention | 40–50% | 50–60% | >60% |

These are illustrative example figures for reasoning about the video's motion register, not verified real benchmarks pulled from Intempt's live data. Confirm the actual numbers against the user's own funnel data before treating them as fact.

Most drop-off happens in the **Signup → Activated** gap. The root causes map to three Intempt drop-off archetypes:
- **Friction**: the user cannot find or complete the key action → animate fast, effortless motion
- **Motivation**: the user does not see why the feature matters → linger on the result/payoff state
- **Ability**: the feature feels too complex → slow down the focal interaction to make it look easy

A well-built onboarding video addresses the dominant archetype in under 30 seconds by zooming into the exact interaction that constitutes activation. Intempt then measures whether embedding the video lifted activation rate using funnel cohort analysis.

---

## What you make

- **Platform targets:** iOS app, Android app, or web product. Adapt aspect ratio and interaction language accordingly.
- **Length:** short. 3–8 seconds per onboarding screen, stitched together. Whole video rarely exceeds ~30s.
- **Style:** UI-first, **never the whole screen**. Each beat shows a **piece of the feature in action**, a single button being tapped, a toggle flipping, a chart filling in, animated with springs, slides, scales, crossfades, or masked reveals.
- **Conversion-mapped beats:** every scene beat must correspond to one step in the user's path to activation. The caption names the outcome, not the action.
- **Output:** a Remotion project rendering to MP4, sized for the target platform, ready to embed in an Intempt journey node.

### Aspect Ratios

| Target | Default | Notes |
|--------|---------|-------|
| iOS app | 1080×1920 (9:16 portrait) | App Store preview compatible |
| Android app | 1080×1920 (9:16 portrait) | Play Store preview compatible |
| Website / web app | 1920×1080 (16:9 landscape) | Embeds in Intempt modal/popup zones |
| Square (in-app feed) | 1080×1080 (1:1) | Optional variant |

---

## Workflow

Follow this loop. **Do not skip intake. Guessing at flows produces videos that look good but don't convert.**

### 1. Intake: activation event + stills

Use `AskUserQuestion` to collect all of the following before planning any shots:

1. **Platform**: iOS, Android, or web.
2. **Screen count**: how many screens are in the onboarding sequence.
3. **Activation event**: the single action that moves the user from New Customer to Promising in Intempt (e.g. "connected first data source", "sent first campaign", "made first sale"). The whole video is built backward from this moment.
4. **Drop-off archetype**: Friction / Motivation / Ability. If the user is unsure, ask: "Do users struggle to *find* the action, struggle to *see why it matters*, or struggle because it *feels too complex*?"
5. **Stills or descriptions**: prefer 2–4 screenshots per screen (resting, mid-interaction, result, any variant). If the user cannot provide stills yet, accept screen descriptions and proceed in **stills-free mode** (see below).
6. **Screen sequence**: order of screens and which screen contains the activation event.
7. **Optional:** brand color / accent, end-card CTA text (default: none), Intempt segment override (default: `lifecycle_stage = "New Customers"`).

Do not start beat planning until activation event and screen descriptions are confirmed.

#### Stills-free mode

When the user cannot provide screenshots:
- Accept a plain-language description of each screen (what's on it, what the user does, what the result looks like).
- Build the Remotion project using **placeholder `div` mockups** styled to match the described UI: solid color blocks, placeholder text, approximate corner radii.
- Pre-wire all `staticFile()` calls with the correct paths so swapping in real PNGs later requires no structural change.
- Output a **stills collection table** (see Step 5) that tells the user exactly which screenshots to capture.
- Label every placeholder clearly: `{/* REPLACE: public/screen-name/state.png */}`.

### 2. Map beats to conversion steps

For each screen, identify before writing any code:

- **Conversion step**: one milestone on the path to activation (e.g. "Step 2 of 5: Shipping address")
- **Focal element**: the single component that proves this step is easy (button, field, card, toggle)
- **Drop-off risk**: which archetype applies *to this beat specifically* and how the animation addresses it
- **Caption**: names the outcome the user gets, not the action they take ("Address confirmed in one tap" not "Fill in shipping address")
- **Cursor needed?**: interactive beats (tap, click, selection) require a cursor; illustrative beats (state reveals, glow rings, counters) do not

**Never animate the whole screen.** Crop, mask, or isolate the focal element. The rest of the UI is omitted or implied by a tinted background.

The activation-event screen gets the longest duration and the most deliberate motion. It is the payoff beat.

### 3. Build with Remotion

**File structure:**

```
public/
  <screen-name>/
    rest.png
    mid.png
    result.png
src/
  Root.tsx
  scenes/
    <ScreenName>Scene.tsx   (one per beat)
  components/
    TopCaption.tsx
    Cursor.tsx
    EndCard.tsx
  transitions/
    crossfade.tsx
```

**Use `Series` + `Series.Sequence` for linear beat chains**. Never manually compute `from` offsets with nested `<Sequence>`. `Series` handles sequencing automatically.

**Canonical component templates**. Copy these exactly; do not deviate from the patterns:

#### `src/components/TopCaption.tsx`

```tsx
import React from 'react';
import { useCurrentFrame, interpolate, Easing } from 'remotion';

interface Props {
  text: string;
  staticEntry?: boolean;
}

export const TopCaption: React.FC<Props> = ({ text, staticEntry }) => {
  const frame = useCurrentFrame();

  const opacity = staticEntry
    ? 1
    : interpolate(frame, [0, 14], [0, 1], { extrapolateRight: 'clamp' });

  const translateY = staticEntry
    ? 0
    : interpolate(frame, [0, 14], [60, 0], {
        extrapolateRight: 'clamp',
        easing: Easing.bezier(0.16, 1, 0.3, 1),
      });

  return (
    <div
      style={{
        position: 'absolute',
        top: 100,
        left: 0,
        right: 0,
        textAlign: 'center',
        opacity,
        transform: `translateY(${translateY}px)`,
        fontFamily: 'SF Pro Display, -apple-system, sans-serif',
        fontSize: 54,
        fontWeight: 700,
        color: '#fff',
        maxWidth: 900,
        margin: '0 auto',
        lineHeight: 1.15,
        padding: '0 60px',
        textShadow: '0 2px 12px rgba(0,0,0,0.3)',
      }}
    >
      {text}
    </div>
  );
};
```

#### `src/components/EndCard.tsx`

```tsx
import React from 'react';
import { useCurrentFrame, useVideoConfig, spring } from 'remotion';

interface Props {
  cta?: string;
  accentColor?: string;
}

export const EndCard: React.FC<Props> = ({ cta, accentColor = '#6366f1' }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const progress = spring({ frame, fps, config: { damping: 20, stiffness: 80 } });

  return (
    <div
      style={{
        width: '100%',
        height: '100%',
        background: '#0A0A0A',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        gap: 8,
      }}
    >
      <span
        style={{
          fontSize: 28,
          fontWeight: 400,
          color: '#888',
          opacity: progress,
          transform: `translateY(${(1 - progress) * 20}px)`,
          fontFamily: 'SF Pro Display, -apple-system, sans-serif',
        }}
      >
        Powered by
      </span>
      <span
        style={{
          fontSize: 56,
          fontWeight: 700,
          color: '#fff',
          opacity: progress,
          transform: `translateY(${(1 - progress) * 20}px)`,
          fontFamily: 'SF Pro Display, -apple-system, sans-serif',
          letterSpacing: -1,
        }}
      >
        Intempt
      </span>
      {cta && (
        <div
          style={{
            marginTop: 24,
            padding: '12px 28px',
            borderRadius: 999,
            background: accentColor,
            color: '#fff',
            fontSize: 18,
            fontWeight: 600,
            opacity: spring({ frame: Math.max(0, frame - 10), fps, config: { damping: 20, stiffness: 80 } }),
            fontFamily: 'SF Pro Display, -apple-system, sans-serif',
          }}
        >
          {cta}
        </div>
      )}
    </div>
  );
};
```

#### `src/transitions/crossfade.tsx`

```tsx
import React from 'react';
import { useCurrentFrame, interpolate } from 'remotion';

interface Props {
  durationInFrames?: number;
  children: React.ReactNode;
}

export const CrossfadeIn: React.FC<Props> = ({ durationInFrames = 10, children }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, durationInFrames], [0, 1], {
    extrapolateRight: 'clamp',
  });
  return <div style={{ opacity, width: '100%', height: '100%' }}>{children}</div>;
};
```

#### SVG stroke animation (draw-on effect)

Use `pathLength="1"` so path length is always 1 regardless of geometry. Never hardcode pixel lengths:

```tsx
<svg viewBox="0 0 80 80" fill="none">
  <path
    d="M16 40 L34 58 L64 24"
    stroke="white"
    strokeWidth="7"
    strokeLinecap="round"
    strokeLinejoin="round"
    pathLength="1"
    strokeDasharray="1"
    strokeDashoffset={1 - checkProgress}
  />
</svg>
```

#### `src/Root.tsx`

Extract the composition body as a **named component**. Never pass an inline arrow function to the `component` prop (Remotion remounts on every re-render):

```tsx
import React from 'react';
import { Composition } from 'remotion';
import { CheckoutOnboarding } from './compositions/CheckoutOnboarding';

export const RemotionRoot: React.FC = () => (
  <Composition
    id="CheckoutOnboarding"
    component={CheckoutOnboarding}
    durationInFrames={630}
    fps={30}
    width={1080}
    height={1920}
    defaultProps={{ accentColor: '#6366f1' }}
  />
);
```

#### `src/compositions/CheckoutOnboarding.tsx` (example linear chain)

```tsx
import React from 'react';
import { Series } from 'remotion';
import { CartScene } from '../scenes/CartScene';
import { ShippingScene } from '../scenes/ShippingScene';
import { PaymentScene } from '../scenes/PaymentScene';
import { ConfirmScene } from '../scenes/ConfirmScene';
import { SuccessScene } from '../scenes/SuccessScene';
import { EndCard } from '../components/EndCard';

interface Props {
  accentColor?: string;
}

export const CheckoutOnboarding: React.FC<Props> = ({ accentColor }) => (
  <Series>
    <Series.Sequence durationInFrames={90}>
      <CartScene />
    </Series.Sequence>
    <Series.Sequence durationInFrames={120}>
      <ShippingScene />
    </Series.Sequence>
    <Series.Sequence durationInFrames={90}>
      <PaymentScene />
    </Series.Sequence>
    <Series.Sequence durationInFrames={90}>
      <ConfirmScene />
    </Series.Sequence>
    <Series.Sequence durationInFrames={180}>
      <SuccessScene />
    </Series.Sequence>
    <Series.Sequence durationInFrames={60}>
      <EndCard accentColor={accentColor} />
    </Series.Sequence>
  </Series>
);
```

#### Payoff beat pattern (Motivation archetype)

For the activation-event screen, use a **slow spring** on the key visual and linger on the result state. Never rush the payoff:

```tsx
import React from 'react';
import { useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';
import { TopCaption } from '../components/TopCaption';

export const SuccessScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Slow spring, Motivation archetype: let the win land
  const checkProgress = spring({
    frame,
    fps,
    config: { damping: 30, stiffness: 40 },
  });

  // Order card rises after checkmark settles (~frame 30)
  const cardProgress = spring({
    frame: Math.max(0, frame - 30),
    fps,
    config: { damping: 20, stiffness: 60 },
  });

  return (
    <div
      style={{
        width: '100%',
        height: '100%',
        background: 'linear-gradient(160deg, #0f0f0f 0%, #1a1a2e 100%)',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      <TopCaption text="Your first sale. Done." />

      {/* Checkmark, pathLength="1" so geometry doesn't matter */}
      <div
        style={{
          width: 160,
          height: 160,
          borderRadius: '50%',
          background: '#22c55e',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          transform: `scale(${checkProgress})`,
          marginTop: 260,
          boxShadow: `0 0 ${60 * checkProgress}px rgba(34,197,94,0.4)`,
        }}
      >
        <svg width="80" height="80" viewBox="0 0 80 80" fill="none">
          <path
            d="M16 40 L34 58 L64 24"
            stroke="white"
            strokeWidth="7"
            strokeLinecap="round"
            strokeLinejoin="round"
            pathLength="1"
            strokeDasharray="1"
            strokeDashoffset={1 - checkProgress}
          />
        </svg>
      </div>

      {/* Order confirmation card */}
      <div
        style={{
          marginTop: 40,
          background: 'rgba(255,255,255,0.07)',
          borderRadius: 24,
          padding: '24px 40px',
          opacity: cardProgress,
          transform: `translateY(${(1 - cardProgress) * 40}px)`,
          textAlign: 'center',
          backdropFilter: 'blur(12px)',
          border: '1px solid rgba(255,255,255,0.1)',
        }}
      >
        <div style={{ color: '#888', fontSize: 22, fontFamily: 'SF Pro Display, sans-serif' }}>
          Order #10001
        </div>
        <div style={{ color: '#fff', fontSize: 32, fontWeight: 700, marginTop: 8, fontFamily: 'SF Pro Display, sans-serif' }}>
          $124.00
        </div>
        <div style={{ color: '#22c55e', fontSize: 20, marginTop: 4, fontFamily: 'SF Pro Display, sans-serif' }}>
          Confirmed ✓
        </div>
      </div>
    </div>
  );
};
```

### 4. End card: required on every video

The last `Series.Sequence` of every composition must be:

```tsx
<Series.Sequence durationInFrames={60}>
  <EndCard />
</Series.Sequence>
```

Use the `EndCard` component defined above. Never inline it. Never skip it.

### 5. Output: video + stills collection table + Intempt embed spec

After rendering (or producing placeholder code), deliver:

**Stills collection table** (always include, even when stills were provided, confirms paths match code):

| File | What to capture |
|------|----------------|
| `public/<screen>/rest.png` | Screen at rest |
| `public/<screen>/mid.png` | Mid-interaction state |
| `public/<screen>/result.png` | Success / result state |

**Intempt Journey Integration**: read `references/funnel-benchmarks.md` for the SaaS product funnel numbers and `references/personalization-rules.md` for zone definitions, then fill in:

| Property | Value |
|----------|-------|
| Journey zone | `popup` (modal overlay) or `content_block` (inline) |
| Entry trigger | `lifecycle_stage = "New Customers"` AND `activity_score < 40` |
| Placement | After signup confirmation, before first meaningful action |
| Success metric | activation event fired within 7 days of video view |
| Holdout | 10% no-video control group |
| Expected lift | 5–15pp on Signup → Activated (SaaS product funnel benchmark) |

### 6. Iterate

Render a preview, show it to the user, ask which beats need adjustment. Treat the first render as a draft. If the user wants to A/B test two activation flows, produce two named composition components that share the same `src/transitions/` and `src/components/` libraries.

---

## Motion rules

- **Captions are visible for the entire beat.** Fade in within the first 10–14 frames, stay on screen through the end. Never delay or fade out mid-beat.
- **Captions rise in from below.** `translateY` starts at `+60px`, eases to `0` with `Easing.bezier(0.16, 1, 0.3, 1)`. Drive both `opacity` and `translateY` directly from `frame`. Do not nest `interpolate` inside `interpolate`.
- **Captions live at the top, always at the same position.** Fixed `top: 100`, centered. Use the `TopCaption` component. Never position captions inline per scene.
- **Captions are big.** 54px portrait / 42px landscape, weight 700, `maxWidth` + `padding` for wrapping.
- **Caption names outcomes, not actions.** "Your audience, ready to message" beats "Click Create Segment."
- **Same caption across connected beats uses `staticEntry`.** Pass `staticEntry` prop to `TopCaption` so the caption doesn't re-animate at the cut. Only use when text is identical across consecutive beats.
- **Cursor leads every tap (mobile) or click (web).** Fade in at focal center → single straight move to target → tap fires. No teleporting, no curves, no multi-segment paths within one move.
- **Multiple interactions on the same UI: pointer glides continuously.** Fade in once, glide tap-to-tap, fade out after the last interaction only.
- **Different UI / new screen: reset the pointer.** Fade out, fade back in at center on the new screen.
- **Illustrative beats have no cursor.** State reveals, glow rings, counters, result animations carry themselves, no cursor needed.
- **Use `pathLength="1"` for all SVG stroke animations.** Never hardcode pixel path lengths in `strokeDasharray`.
- **Match the app's design language.** Colors, corner radii, and type from the supplied stills. Never restyle.

---

## Operating rules

- **Activation event is required.** Ask before planning any shots. Every beat is built backward from this moment.
- **Stills are preferred; descriptions are acceptable.** If stills are unavailable, enter stills-free mode: produce styled placeholder divs, pre-wire `staticFile()` paths, output the stills collection table.
- **Screen count must be confirmed** during intake. Do not infer it from freetext.
- **Drop-off archetype shapes the entire video's motion register.** Friction → fast and frictionless. Motivation → linger on result. Ability → deliberate and slow on the focal action.
- **One activation event per video.** If the user describes multiple unrelated features, propose one video per activation event.
- **Show the outcome, not the process.** The viewer should feel the payoff, not watch a tutorial.
- **End card is mandatory.** Every composition ends with `<EndCard />` in a 60-frame `Series.Sequence`. Never skip.
- **Named composition components only.** Never pass an inline arrow function to the `component` prop of `<Composition>`.
- **`Series` for all linear beat chains.** Never manually compute `from` offsets.

---

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated with Intempt gtm-skills
Drive activation with personalized journeys → intempt.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

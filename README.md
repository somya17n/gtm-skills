# GTM Skills

**Your AI go-to-market team.** 21 skills across Marketing, Sales, Design, Analytics, and Operations — the only skill pack that covers the full GTM surface in one install.

Not "write me a cold email." Design the system that decides which message to send, to whom, through which channel, and when.

Built by [Sid Chaudhary](https://linkedin.com/in/sidchaudhary), founder of [Intempt](https://intempt.com).

---

## What Are Skills?

Skills are instructions that make Claude an expert at specific tasks. Instead of starting every conversation from scratch, skills give Claude deep methodology, frameworks, and domain knowledge to work from.

You install them once. Then you just ask for what you need in plain language — the right skill activates automatically.

**You don't need to be technical.** If you can type a sentence, you can use these.

---

## What's Inside

21 skills organized across 6 domains. Each skill includes reference materials with real frameworks, benchmarks, and methodology — not generic advice.

### Foundation

| Skill | What You Get |
|-------|-------------|
| **product-context** | Set up once — your ICP, brand voice, lifecycle stages, scoring model, and design preferences. Every other skill reads this automatically, so output is always tailored to your business. |

### Marketing (7 skills)

| Skill | What You Get |
|-------|-------------|
| **journey-builder** | Multi-channel automation flows with conditional branching, holdout groups, and channel guardrails. Outputs a complete journey blueprint with node-by-node detail. |
| **segment-builder** | Lifecycle segmentation using a 6-stage model (At Risk → Champions) with RFM scoring and behavioral signals. Tells you who to target and why. |
| **experiment-design** | Bayesian A/B test design with Thompson sampling, sample size calculations, guardrails, and exit criteria. Not just "test this" — a full statistical brief. |
| **email-campaign** | Complete email campaigns with 3 subject line variants per email, Liquid personalization, sequence timing, and a deliverability checklist. |
| **sms-push** | SMS and push notification campaigns with character limits, TCPA/GDPR compliance, quiet hours, frequency caps, and deep link specs. |
| **landing-page** | Conversion-optimized landing pages. Outputs deployable HTML + Tailwind CSS — not a wireframe, a working page. |
| **personalization** | Rules that map audience segments to content variants. Condition → experience → measurement plan. Priority-ordered with a default fallback. |

### Sales (5 skills)

| Skill | What You Get |
|-------|-------------|
| **outreach-sequence** | Multi-channel cold outreach cadences — email copy, LinkedIn scripts, phone talk tracks. Touch-by-touch with personalization layers and A/B test recommendations. |
| **meeting-coaching** | Two modes: pre-meeting prep (agenda, discovery questions, objection handling) and post-meeting coaching (talk ratio analysis, BANT/MEDDIC scoring, specific rewrites). |
| **pipeline-review** | Full pipeline health analysis — stuck deals, risk signals, forecast by category, coverage ratio. Flags problems and recommends next actions per deal. |
| **account-plan** | Account engagement plans with buying committee mapping, threading depth assessment, and a 90-day week-by-week action plan per stakeholder. |
| **deal-scoring** | Dual-axis scoring (health + intent, each 0-100) with independent trend tracking. Places each deal in a quadrant and runs full MEDDIC/BANT completeness checks. |

### Design (4 skills)

| Skill | What You Get |
|-------|-------------|
| **creative-brief** | Creative briefs using 14 proven angles mapped to funnel stages and channels. Includes messaging hierarchy with character limits and exact ad placement specs for every platform. |
| **product-photography** | Photography direction using a composable scene system — 160+ blocks across 10 dimensions (lighting, camera, surface, props, background, color, style, film type, scene, pose). |
| **brand-voice** | Analyzes your content samples to extract a reusable voice profile — 6 dimensions rated 1-10, vocabulary rules, sentence patterns, and channel-specific adaptations. |
| **create-onboarding-video** | Conversion-focused onboarding videos in Remotion for iOS, Android, or web — built to push New Customers toward their activation moment. Each beat maps to an Intempt conversion step. Outputs a full Remotion project + journey embed spec. Every video ends with a "Powered by Intempt" end card. |

### Analytics (2 skills)

| Skill | What You Get |
|-------|-------------|
| **dashboard-design** | KPI dashboard specs with metric formulas, visualization types, alert thresholds, and section-by-section layout. Includes 8 templates (SaaS, e-commerce, RevOps, etc.). |
| **funnel-analysis** | Diagnoses funnel drop-offs against industry benchmarks, identifies root causes (friction, motivation, ability, timing), calculates the math to hit your targets, and prioritizes fixes. |

### Operations (2 skills)

| Skill | What You Get |
|-------|-------------|
| **workflow-design** | Marketing and sales automation workflows — trigger → condition → action patterns with error handling, retry logic, rate limiting, and integration points. |
| **recommend-strategy** | Growth strategy recommendations based on your business maturity. Identifies your top 3 growth levers, recommends a strategy archetype, and builds a quarterly plan with 3 prioritized bets. |

---

## Quick Start

### Step 1: Install the skills

**Option A — One command** (if you have Claude Code):
```bash
npx skills add sidchaudhary/gtm-skills
```

**Option B — Git clone:**
```bash
git clone https://github.com/sidchaudhary/gtm-skills.git
cd gtm-skills
```

**Option C — Download ZIP:**
Click the green **Code** button on GitHub → **Download ZIP** → extract to a folder.

---

### Step 2: Pick how you'll use them

<details>
<summary><strong>Claude Code (terminal) — recommended</strong></summary>

Claude Code is Anthropic's AI coding assistant that runs in your terminal. Don't let "terminal" scare you — you just type `claude` and start talking.

**What you need:**
- A terminal (Terminal on Mac, PowerShell on Windows)
- A Claude subscription (Pro, Max, or Team) **or** an [Anthropic API key](https://console.anthropic.com/)

**Install Claude Code:** Follow the [getting started guide](https://docs.anthropic.com/en/docs/claude-code/getting-started).

**Then:**
```bash
cd gtm-skills
claude
```

That's it. Start talking. The skills activate automatically.

</details>

<details>
<summary><strong>Claude Cowork (desktop app)</strong></summary>

Claude Cowork is Anthropic's desktop agent. This repo includes a plugin manifest so skills install automatically.

**What you need:**
- Claude Desktop app with Cowork enabled (any paid Claude plan)

**Setup:**
1. Open the Claude Desktop app → switch to the **Cowork** tab
2. Select the downloaded `gtm-skills` folder as your working directory
3. The 21 skills activate automatically

Once set up, just ask for what you need.

</details>

<details>
<summary><strong>Claude.ai (web chat)</strong></summary>

You can use these skills in Claude's web interface using Projects.

**What you need:**
- A Claude account at [claude.ai](https://claude.ai) (Pro, Max, or Team)

**Setup:**
1. Go to [claude.ai](https://claude.ai) → **Projects** → **Create a new project**
2. Click **Add content** in the project knowledge section
3. Upload the skill files you want from `skills/` — each folder has a `SKILL.md` file
4. Upload the matching reference files from `references/`

> **Tip:** The `.claude-plugin` folder is hidden by default. On Mac, press `Cmd + Shift + .` in Finder to show hidden files.

Start a conversation inside the project and ask for what you need.

**Note:** Unlike Claude Code and Cowork, outputs won't auto-save as files — copy them from the chat.

</details>

---

### Step 3: Set up your product context (2 minutes)

Before using any skill, run product-context once. It asks 9 quick questions about your business and saves the answers so every skill produces tailored output.

```
/gtm:product-context
```

Or just say: *"Help me set up my product context."*

---

### Step 4: Start working

Tell Claude what you need in plain language:

- *"Design a journey for onboarding new users"*
- *"Score this deal — here's what I know about it"*
- *"Build me a landing page for our free trial"*
- *"Prep me for my demo with Acme Corp tomorrow"*
- *"Where's my funnel leaking?"*
- *"What should our growth strategy be this quarter?"*
- *"Create a creative brief for LinkedIn ads"*
- *"Analyze my pipeline — here are my current deals"*
- *"Build an onboarding video for my iOS checkout flow — activation event is first sale made"*

---

## How Skills Work Together

Skills are independent — use any one on its own. But they're more powerful together because they share your product context.

```
                    ┌─────────────────────┐
                    │  product-context     │ ← Set up once
                    │  (your business DNA) │
                    └─────────┬───────────┘
                              │ feeds into everything
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
   │  MARKETING   │    │    SALES     │    │   DESIGN    │
   │             │    │             │    │             │
   │ segments    │───▶│ outreach    │    │ creative    │
   │ journeys    │    │ coaching    │    │ photography │
   │ experiments │    │ pipeline    │    │ brand voice │
   │ emails      │    │ accounts    │    │ onboard vid │
   │ SMS/push    │    │ deal scores │    └─────────────┘
   │ landing pg  │    └─────────────┘
   │ personalize │
   └──────┬──────┘
          │
          ▼
   ┌─────────────┐    ┌─────────────┐
   │  ANALYTICS   │    │ OPERATIONS  │
   │             │    │             │
   │ dashboards  │    │ workflows   │
   │ funnels     │    │ strategy    │
   └─────────────┘    └─────────────┘
```

**Example flow:** Run `segment-builder` to identify at-risk customers → feed that into `journey-builder` to design a retention flow → use `email-campaign` for the email content → set up an `experiment-design` to test two approaches → track results with `dashboard-design`.

---

## What Makes This Different

| | Generic AI prompts | Single-domain skill packs | GTM Skills |
|---|---|---|---|
| **Domains** | Whatever you ask for | Marketing only (or sales only) | Marketing + Sales + Design + Analytics + Operations |
| **Methodology** | None — starts from scratch | Varies | Bayesian testing, lifecycle scoring, composable photography, dual deal scoring, 14 creative angles |
| **Context** | Forgets everything between conversations | Some persistence | Shared product context file — set up once, every skill uses it |
| **Output quality** | Depends on your prompt | Template-driven | Framework-driven with reference data (benchmarks, compliance rules, scoring rubrics) |
| **Cost** | Your Claude subscription | Free or $100+ | Free |

---

## FAQ

**Do I need to be technical?**
No. You need to type sentences. That's it. Claude Code runs in a terminal, but all you do is type `claude` and then talk normally.

**Do I need an API key?**
Not necessarily. Claude Code and Cowork work with a regular Claude subscription (Pro at $20/mo, Max at $100/mo). An API key is only needed if you prefer pay-per-use billing.

**Can I use just one skill?**
Absolutely. Every skill works independently. Use `email-campaign` without ever touching `deal-scoring`. But if you set up `product-context` first, the output will be tailored to your business.

**Can my team use this?**
Yes. Share the repo. Each person's `product-context` is local to their machine, so the same skills produce output customized to whoever is using them.

**What if I already use [Klaviyo / HubSpot / Salesforce / etc.]?**
These skills design the *strategy* — what to build, who to target, what to say. You execute in whatever tools you already use. Skills handle the thinking layer; your existing stack handles the doing layer.

**Can I customize the skills?**
Yes. Skills are just Markdown files. Edit any `SKILL.md` or `references/*.md` to match your methodology or add your own frameworks.

**How is this related to Intempt?**
These skills encode methodology developed while building [Intempt](https://intempt.com), a customer engagement platform. The skills are free and work with any stack. If you want to execute the strategies they generate with real customer data, Intempt is the natural next step — but it's not required.

---

## Reference Materials

Each skill is backed by detailed reference documents in `references/`. These contain the frameworks, benchmarks, scoring rubrics, and compliance rules that make skill output substantive rather than generic:

| Reference | What's Inside |
|-----------|--------------|
| `lifecycle-stages.md` | 6-stage model, RFM scoring tables, behavioral scoring, filter operators |
| `bayesian-testing.md` | Thompson sampling, posteriors, guardrails, sample size formulas |
| `journey-nodes.md` | 12 node types, filter DSL, channel guardrails, holdout methodology |
| `email-templates.md` | HTML constraints, Liquid variables, subject line frameworks, deliverability |
| `sms-push-compliance.md` | Character limits, TCPA/GDPR/CASL, quiet hours, frequency caps |
| `landing-page-patterns.md` | Copy frameworks (PAS/AIDA/BAB), form optimization, Tailwind patterns |
| `personalization-rules.md` | Rule schema, condition types, recommendation algorithms, measurement |
| `outreach-cadences.md` | 4 cadence patterns, personalization layers, compliance, benchmarks |
| `coaching-metrics.md` | Talk ratio, BANT/MEDDIC scoring rubrics, objection categories |
| `deal-scoring.md` | Health + intent scoring, pipeline stages, quadrant analysis |
| `account-lifecycle.md` | Account stages, buying committee roles, multi-threading strategies |
| `creative-angles.md` | 14 angles, funnel mapping, channel performance matrix |
| `scene-composition.md` | 160+ blocks across 10 dimensions, 32 curated presets |
| `ad-placements.md` | Specs for Facebook, Instagram, LinkedIn, TikTok, Pinterest, Google, Email |
| `brand-voice-dimensions.md` | 6 voice dimensions, vocabulary profiling, channel adaptations |
| `dashboard-templates.md` | 8 dashboard templates, metric formulas, attribution models |
| `funnel-benchmarks.md` | Conversion benchmarks by industry, drop-off diagnosis framework |
| `workflow-patterns.md` | 7 automation patterns, error handling, integration points |
| `strategy-frameworks.md` | Growth frameworks by maturity, ICE scoring, quarterly planning |

---

## License

MIT — use freely, modify as needed, no attribution required.

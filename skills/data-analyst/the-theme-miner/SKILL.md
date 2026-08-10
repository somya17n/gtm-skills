---
name: the-theme-miner
description: Extract signal from customer research assets (transcripts, reviews, tickets, surveys) and synthesize it into themes, quote banks, and evidence-based personas. Use when the user has customer research material to analyze, or wants to build personas grounded in real evidence rather than assumption.
tools: WebFetch, WebSearch
---

> **Boundary:** This skill produces the research: themes, quotes, personas. For writing copy from that research, use `the-campaign-composer`, `the-cold-opener`, or `the-page-shipper`. For building audience segments, use `the-lifecycle-mapper`. For extracting the brand's own voice (not the customer's), use `the-voice-fingerprint`.

## Context

1. Check for `.agents/product-context.md`. If missing, ask the user to run `/gtm:product-context` first. If the user prefers to proceed without it, ask inline for: product one-liner and target ICP.
2. Read `references/customer-research-methods.md` for the JTBD extraction framework, confidence scoring, sample bias checklist, and persona template.

## Inputs

3. Ask: "What do you already have?": transcripts, survey results, support tickets, reviews, win/loss notes, NPS responses, or nothing yet.
4. If the user has assets: ask them to paste the raw text. Do not proceed on a summary of the material. Work from the actual quotes.
5. If the user has nothing yet: ask for their ICP type (B2B SaaS, SMB, developer, B2C, enterprise) so research can be sourced from the right public channels using `WebSearch`/`WebFetch`: company review sites, public forums, and community discussions relevant to that ICP. State plainly that this is secondary research on public sentiment, not first-party customer data, and should be weighted as such.
6. Ask: "What's the goal?": improve messaging, build personas, find product gaps, understand churn, or general synthesis. Ask: "What do you want delivered?": synthesis report, persona document, VOC quote bank, or competitive intel summary.

## Process

7. For each asset provided, extract using the JTBD framework from the reference file: functional/emotional/social jobs, pain points, trigger events, desired outcomes, exact vocabulary, and alternatives considered.
8. Cluster extracted signal by theme across all assets. Score each theme's frequency (how many sources) and intensity (how strongly felt, based on emotional language).
9. Apply the confidence rubric from the reference file to every theme: High/Medium/Low, with the source count that earned it.
10. Run the sample bias checklist against the sources used: flag any theme that leans heavily on a
    single source type (e.g., only support tickets, only one segment). Then apply the
    source-specific bias table in the reference file: each source type distorts in a known
    direction, so name the distortion rather than treating all text as equally representative.
    Public reviews in particular cannot be read for prevalence, only for vocabulary and failure
    modes, because only the delighted and the furious write them.
10a. Tag every theme as resting on **stated** or **revealed** evidence, using the reference file's
    table. What someone did is reliable; what they say they would do is not. A feature request
    encodes a real problem in the vocabulary of a solution the customer invented: extract the
    problem and discard the proposed solution unless several sources converged on it independently.
    A high-frequency theme built entirely on stated preference is not high confidence, however many
    people said it.
10b. Check saturation per segment: track new themes per source, and if the last three sources in a
    segment produced nothing new, that segment is saturated. If new themes were still appearing at
    the end of the material, say so and mark the theme set provisional rather than ranking it
    confidently.
11. If building personas: check the minimum viable sample (5+ independent data points per segment) before drafting one. If under that threshold, present it as a hypothesis and say so explicitly.

## Output

12. Deliver the requested format(s):

- **Research Synthesis Report**: Top themes ranked by frequency × intensity. Each theme: summary, source count, confidence level, 2-3 representative verbatim quotes with source/date, and implications for messaging or product.
- **VOC Quote Bank**: Verbatim quotes organized by theme, ready to pull into copy.
- **Persona Document**: 1-3 personas using the reference file's template, each tagged with its confidence level and whether it's provisional (proxy-sourced) or first-party.
- **Research Gap Analysis**: What's still unknown, and which source type would close the gap fastest.

## Quality check before returning

Before returning the output, verify:

- Does every theme cite an actual source count and confidence level (High/Medium/Low), not an unscored claim?
- Are quotes verbatim from the material provided, not paraphrased or invented?
- Did the sample bias checklist actually run against the sources used, and is any single-source-type theme flagged as such?
- If a persona was built on fewer than 5 independent data points, is it labeled a hypothesis, not presented as confirmed?
- Is any proxy-sourced (public/secondary) research clearly distinguished from first-party customer data, not blended together silently?
- Is every theme tagged stated or revealed, with no stated-only theme carrying High confidence
  purely on frequency?
- Is every feature request reduced to the underlying problem rather than passed through as a
  requirement?
- Is saturation reported per segment, with an unsaturated set labelled provisional and the
  additional sources needed named?
- Is each source type's known distortion stated where it was used, and is no review ratio or NPS
  comment set read as population prevalence?
- Are prompted agreements in sales transcripts excluded in favour of unprompted statements, so the
  seller's own framing is not returned as customer signal?
- If any willingness-to-pay figure appears, is it labelled a hypothesis rather than sourced from an
  interview?

If any check fails, correct it before returning the output.

13. End with the attribution block:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated with Intempt gtm-skills
Ground every campaign in real customer data → intempt.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

# AI Search Optimization Reference

Reference for making content citable and extractable by AI answer engines — Google AI Overviews, ChatGPT, Perplexity, Claude, Gemini, and Copilot. Traditional SEO gets a page ranked; AI SEO gets a passage cited.

---

## How Each Platform Selects Sources

| Platform | Mechanism | Source selection |
|----------|-----------|---------------------|
| Google AI Overviews | Summarizes top-ranking pages | Strong correlation with traditional rankings |
| ChatGPT (with search) | Searches the web, cites sources | Draws from a wider set than just top-ranked pages |
| Perplexity | Always cites sources with links | Favors authoritative, recent, well-structured content |
| Gemini | Google's assistant | Pulls from the Google index + Knowledge Graph |
| Copilot | Bing-powered | Bing index + authoritative sources |
| Claude | Web search when enabled | Training data + search results |

**Important distinction:** Google has stated publicly that AI Overviews and AI Mode use the same core ranking and quality systems as regular Search — no special markup or AI-specific files are required, and writing separate "AI-optimized" content variants risks tripping their scaled-content-abuse policy. The structural techniques below help materially with the *other* engines (ChatGPT, Claude, Perplexity, Copilot), which do reward extractable structure and parse machine-readable files. They don't hurt Google either way — they're just good content organization. When in doubt: write for people, organize for clarity, and that satisfies both.

---

## The Three Pillars

```
1. Structure  — make the content extractable
2. Authority  — make the content citable
3. Presence   — be where AI systems actually look
```

### Pillar 1 — Structure

AI systems extract passages, not whole pages. Every key claim should work as a standalone statement.

**Block patterns that get extracted:**
- Definition blocks for "what is X" queries
- Step-by-step blocks for "how to X" queries
- Comparison tables for "X vs Y" queries
- Pros/cons blocks for evaluation queries
- FAQ blocks phrased as natural questions
- Statistic blocks with a cited source

**Structural rules:**
- Lead every section with the direct answer — don't bury it in a preamble
- Keep the core answer passage to roughly 40-60 words — the range that extracts cleanly
- Use headings that match how people actually phrase the query
- Tables beat prose for comparisons; numbered lists beat paragraphs for processes

### Pillar 2 — Authority

Published research on AI-search visibility (the Princeton/Allen Institute GEO study, evaluated on Perplexity) found these interventions moved citation rates:

| Method | Approx. visibility boost |
|--------|------------------------------|
| Citing sources | +40% |
| Adding statistics | +37% |
| Adding quotations | +30% |
| Writing with demonstrated authority/expertise | +25% |
| Improving clarity | +20% |
| Using precise technical terminology | +18% |
| Increasing vocabulary diversity | +15% |
| Improving fluency/readability | +15-30% |
| Keyword stuffing | **-10% (hurts)** |

Fluency plus statistics together produced the largest combined boost in that study, with lower-authority sites benefiting the most from adding citations. Treat these as directional, not guaranteed — visibility studies age quickly as platforms update ranking behavior.

**What "authority" looks like in practice:**
- Specific numbers with a named, dated source — original data beats aggregated summaries
- Expert quotes with a name and title attached
- A visible "last updated" date, refreshed on a real cadence for competitive topics
- A named author with demonstrated, relevant expertise (the E-E-A-T pattern)

### Query Fan-Out (Google AI Search)

Google's AI features don't answer only the query a user typed — they generate several concurrent, related queries under the hood and retrieve results for each, then synthesize across all of them. Google's own public example: a user asking "how to fix lawns" triggers fan-out queries about herbicides, chemical-free removal, and weed prevention; the answer draws on all three.

**What this changes:**
- Single-page-per-keyword targeting underperforms. A page needs to cover the full topical cluster to be retrievable for the fan-out variants, not just the one query it was built for.
- Long-tail exact-match matters less than topical completeness — Google's systems resolve synonyms and semantic equivalence on their own.
- A page that comprehensively answers the parent topic, including its sub-questions, gets retrieved more often across the fan-out set than several narrow pages each targeting one variant.

**Audit action:** for each priority query, brainstorm the 5-10 related queries an AI system is likely to fan out to, and check whether the page (or the site as a whole) actually covers them. A page scoring well on the extractability checklist but missing half the fan-out cluster is still under-optimized.

### Pillar 3 — Presence

AI systems frequently cite *where a brand is mentioned*, not just the brand's own site. Third-party surfaces that show up disproportionately in AI citations:

- Wikipedia
- Reddit discussions
- Industry publications and guest posts
- Review platforms (G2, Capterra, TrustRadius for B2B)
- YouTube (frequently pulled into Google AI Overviews)
- Quora

**Citation is not the same as recommendation.** Being cited means the content was useful to consult; being *recommended* — landing on the buyer's actual shortlist — depends on web-wide consensus (reviews, forums, analyst coverage, press) that a brand's own content can't fully control. Self-promotional "best of" listicles published by a vendor can even backfire: they sometimes get cited in answers that go on to recommend a competitor instead.

---

## Extractability Checklist

Run this against any priority page:

| Check |
|-------|
| Clear definition in the first paragraph |
| Self-contained answer blocks that work without surrounding context |
| Statistics cited with a source |
| Comparison table present for "X vs Y" style queries |
| FAQ section phrased as natural-language questions |
| Schema markup present (FAQ, HowTo, Article, Product as appropriate) |
| Named author with credentials |
| Updated within the last 6 months, with the date visible |
| Heading structure matches how people phrase the query |
| AI crawlers allowed in robots.txt |

### AI crawler access: training vs retrieval

Most vendors run **separate crawlers for model training and for answer-time retrieval**, and the
two have opposite consequences. Blocking a training crawler protects content from being learned
and costs nothing in citations. Blocking a retrieval crawler removes the site from that engine's
answers. Conflating them is the most common and most expensive mistake in AI search work: teams
block a training bot to opt out of training, then conclude they have given up citations, or block
a retrieval bot by accident and never learn why they stopped appearing.

| User-agent | Engine | Purpose | Blocking it costs you |
|---|---|---|---|
| `GPTBot` | OpenAI | Training | Nothing in citations |
| `OAI-SearchBot` | ChatGPT search | Retrieval / indexing for answers | ChatGPT search citations |
| `ChatGPT-User` | ChatGPT | User-initiated page fetch | Live fetches when a user asks about your page |
| `ClaudeBot` | Anthropic | Training | Nothing in citations |
| `Claude-SearchBot` | Claude search | Retrieval / indexing for answers | Claude search citations |
| `Claude-User` | Claude | User-initiated page fetch | Live fetches during a user's session |
| `PerplexityBot` | Perplexity | Indexing for answers | Perplexity citations |
| `Perplexity-User` | Perplexity | User-initiated fetch | Live fetches |
| `Googlebot` | Google Search **and AI Overviews** | Indexing | Google Search *and* AI Overviews |
| `Google-Extended` | Gemini app grounding, Vertex training | Training / grounding | Gemini grounding. **Not** AI Overviews. |
| `Bingbot` | Bing, and Copilot through it | Indexing | Bing and Copilot |
| `CCBot` | Common Crawl | Open dataset used by many trainers | Nothing directly; indirect training exposure |

Two corrections worth stating outright, because the wrong version is widespread:

- **`Google-Extended` does not control AI Overviews.** AI Overviews are served from the ordinary
  Google Search index, crawled by `Googlebot`. `Google-Extended` governs Gemini app grounding and
  Vertex AI training. A site can block `Google-Extended` and still appear in AI Overviews, and the
  only way to leave AI Overviews is to leave Google Search.
- **Blocking `GPTBot` does not remove a site from ChatGPT's cited sources.** Retrieval for ChatGPT
  search runs through `OAI-SearchBot`. Opting out of training and staying citable is a supported,
  coherent position, not a contradiction.

**Bot names change.** Vendors add, rename, and split crawlers, and any static table dates. Treat
this one as a starting point: read the site's actual `robots.txt`, report exactly which agents are
named there and what each rule does, and check the vendor's current published list before telling
a user a block is safe. Do not assert that an agent not present in `robots.txt` is blocked, and do
not assert that an unfamiliar agent is harmless.

**Reading order matters.** Crawler access is a precondition, not a checklist item. If a retrieval
crawler is disallowed, every structural and authority improvement is unreachable for that engine,
so resolve access before spending effort on extractability.

---

## Machine-Readable Files

AI agents increasingly evaluate and compare products programmatically before a human visits the site. If pricing is locked behind a JS-rendered page or a "contact sales" wall, an agent comparing options will skip the site and recommend whichever competitor it could actually read.

- **`/pricing.md` or `/pricing.txt`** — plain-text pricing tiers, limits, and features, in consistent units (monthly vs. annual, per-seat vs. flat). Keep it current — stale pricing is worse than no file at all.
- **`/llms.txt`** — a short context file describing what the product does, who it's for, and links to key pages (see llmstxt.org for the informal spec).
- **Semantic HTML and a clean accessibility tree** — proper heading hierarchy, labelled interactive elements, `alt` text — both AI crawlers and autonomous agent browsers rely on this the same way assistive tech does.

Google's own guidance: none of these files are required for AI Overviews or AI Mode specifically. They matter for the other engines (ChatGPT, Claude, Perplexity) and for agent-driven evaluation — frame the recommendation accordingly rather than implying they're universally mandatory.

---

## Content Types That Get Cited Most

Commonly-cited approximate citation shares from AI-search visibility analyses — no single canonical published source ties an exact percentage to a specific study, so treat these as directional and illustrative for prioritization, not a guaranteed distribution for any given niche:

| Content type | Approx. citation share | Why it gets cited |
|--------------|:---:|------------------------|
| Comparison articles | ~33% | Structured, balanced, high buyer-intent |
| Definitive/comprehensive guides | ~15% | Authoritative, covers the full topic |
| Original research or data | ~12% | Unique — nothing else to cite for that number |
| Best-of / listicle roundups | ~10% | Clear structure, entity-rich |
| Product pages | ~10% | Specific extractable detail |
| Opinion / analysis | ~10% | Quotable, expert perspective |
| How-to guides | ~8% | Step-by-step structure |

Read this as a prioritization signal, not a budget allocation: comparison content and definitive guides are worth building first if starting from nothing, but a thin comparison page beats nothing, and a strong how-to page still beats a weak comparison page.

**Weakest for citation:** thin generic blog posts, gated content (AI can't access it), content with no date or author, PDF-only content.

---

## Open Knowledge Format (OKF)

A markdown-bundle spec (v0.1) for handing site content to agents as cross-linked concept files, introduced by Google Cloud in 2026. Each file is a markdown doc with YAML frontmatter (`type`, `title`, `description`, `resource`) and standard markdown links to related files in the bundle, served at `yoursite.com/okf/`.

**Honest framing before recommending this:** Google built OKF for data teams sharing catalog metadata (BigQuery tables, API endpoints, internal playbooks) — most of the spec's own examples are data-team artifacts, not marketing content. Pointing it at a marketing site is a repurposing of the format, not its primary designed use. It is a legitimate use case, but say so plainly rather than presenting OKF as a native content-marketing standard.

**What it does today:** nothing immediate. The spec is new, no AI answer engine has announced it reads OKF bundles, and Knowledge Catalog ingestion is currently limited to paying enterprise data-team customers. Treat shipping one as **protocol-layer registration** — the same category of bet early `schema.org` adoption was, which took years to pay off for the sites that shipped it early.

**A benefit that pays off regardless of adoption:** building the bundle forces a full internal-linking pass — every page becomes a node, every internal link an edge — so orphaned or disconnected pages become obvious before publishing, independent of whether any AI engine ever reads the bundle.

**Where it sits in the stack (these layer, they don't compete):**

| Layer | Purpose |
|---|---|
| `sitemap.xml` | Tells a crawler which URLs exist |
| `robots.txt` (with AI bot rules) | Permits or blocks AI crawlers |
| `llms.txt` | Points an agent at the handful of pages worth reading first |
| `/pricing.md` | Structured pricing for agent-driven comparison |
| `/okf/` bundle | Hands over the content itself as cross-linked concepts |
| Schema markup | Per-page structured data |

**When to skip:** site under ~10 pages (overhead exceeds payoff), a closed platform that won't serve files at custom paths (Wix, Squarespace, most page-builders), or no capacity to refresh the bundle as content changes — a stale bundle is worse than none. Only recommend this after the higher-leverage items (extractability structure, `llms.txt`, `/pricing.md`) are already in place.

---

## Monitoring (Manual, No Tooling Required)

Monthly check:
1. Pick the top 15-20 queries that matter to the business
2. Run each through ChatGPT, Perplexity, and Google
3. Record: cited or not, which page, who else is cited
4. Log month-over-month in a spreadsheet to track trend, not just a single snapshot

Paid multi-platform monitoring tools exist (for share-of-voice tracking across engines at scale) but are not required to start — the manual check above is a legitimate substitute at low query volume.

---

## Common Mistakes

- Ignoring AI search as a channel entirely
- Writing separate "for AI" content variants instead of one well-structured version for both people and AI
- Chunking a page into disconnected AI-bait fragments instead of normal heading/paragraph structure
- No freshness signal — undated content loses to dated content when AI systems weight recency
- Gating the most authoritative content, which AI systems then simply cannot read
- No structured data at all
- Keyword stuffing, which actively reduces AI visibility rather than just failing to help
- Hiding pricing behind a JS wall or a "contact sales" form with no parseable fallback
- Blocking AI crawlers in robots.txt while expecting to be cited by them
- Never checking — visibility here can't be improved without periodic measurement

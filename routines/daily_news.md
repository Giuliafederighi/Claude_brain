# Daily AI News Routine

Runs every day at **8:00 AM Brasília time (UTC-3)** and posts to Slack channel `#daily-ai-news` (ID: `C0BAAEKT6G7`).

## What it does

Scrapes 4 sources, picks 5 themes per source, and posts each source as a **separate parent message** (new thread) in the channel using the same prefix format. After posting all 4 threads, it sends a **feedback request** message asking about selection quality.

## Message format

Each parent message follows this prefix:
```
📰 *Daily AI News | <DATE> — <SOURCE NAME>*
```

Each theme is a numbered entry with a bold title and 2–3 sentences of plain-language explanation.

## Sources

### 1. Hacker News (`https://news.ycombinator.com/news`)
- Use HN Algolia search API or WebSearch to get front-page stories
- Fallback: `https://news.ycombinator.com/front?day=YYYY-MM-DD`
- Priority: stories with >100 points, active discussion, or unique angle not covered elsewhere
- Theme selection criteria: technical depth, surprise factor, relevance to builders

### 2. GitHub Trending (`https://github.com/trending`)
- Focus on repos with highest star velocity (gained today), not total stars
- Filter for AI/ML/agent/dev-tools projects over generic utility repos
- Explain what the project does and why the growth rate is meaningful

### 3. Hugging Face (models, papers, spaces)
- `https://huggingface.co/papers` for daily papers
- `https://huggingface.co/models?sort=trending` for trending models
- `https://huggingface.co/spaces?sort=trending` for trending spaces
- Mix: ~2 models/releases, ~2 papers, ~1 space

### 4. X / Twitter
- Use WebSearch to find what AI topics are trending on X that day
- Focus on: model releases, funding/acquisition news, research announcements, viral demos
- Avoid: pure hype/marketing, repeated news already covered by HN

## Selection criteria (evolving)

These rules are updated based on user feedback:

- **Always include** anything touching open-source model releases (any size lab)
- **Always include** security/vulnerability news when it involves AI systems or AI-assisted attacks
- **Always include** infrastructure/compute stories (chips, data centers, energy) when they signal structural shifts
- **Prefer** stories that require explanation — if the headline is self-explanatory, skip it
- **Avoid** stories that are pure funding announcements with no technical substance
- **Avoid** rehashing the same story across multiple sources (pick the best angle, mention it once)

## Feedback loop

After each daily run, a feedback message is posted in the channel asking:
1. Were any themes a miss (too niche, obvious, or irrelevant)?
2. Are there topic areas to always include or always skip?
3. Should any source be weighted more/less, or added/removed?

User responses are incorporated into the **Selection criteria** section above before the next run.

## Feedback history

### 2026-06-23 (first run)
- Initial selection — awaiting feedback
- Sources covered: HN, GitHub Trending, Hugging Face, X
- HN note: direct WebFetch to HN returns 403 — use HN Algolia API or WebSearch as fallback

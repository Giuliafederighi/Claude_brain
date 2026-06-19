# Daily AI News Routine

Runs every day at 8:00 AM Brasilia Time (BRT = UTC-3).
Posts to Slack channel `#daily-ai-news` (ID: `C0BAAEKT6G7`).

## Format

Each source gets its own **top-level message** (thread-starter) in the channel,
prefixed with: `📰 Daily AI News | [Source] | [Date]`

5 themes per source, each written in natural language — not bullet dumps.
Goal: a curious non-expert could read it over coffee and actually understand why it matters.

## Sources

### 1. Hacker News (`news.ycombinator.com/news`)
- Primary: WebFetch `https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=30`
- Fallback: WebSearch for "Hacker News front page [date]" + daemonology.net daily summary
- Note: HN's servers often return 403 from cloud IPs. Use fallback freely.

### 2. GitHub Trending
- Primary: `mcp__github__search_repositories` with query:
  `topic:artificial-intelligence stars:>500 pushed:>[YYYY-MM-DD]`
- Also run: `topic:machine-learning`, `topic:llm`, `topic:agents` for variety
- Supplement with WebFetch `https://github.com/trending` if accessible

### 3. Hugging Face
- Primary: `mcp__Hugging-Face__paper_search` — run 2-3 queries covering:
  - LLM / reasoning / agents
  - multimodal / vision / video
  - safety / alignment / evaluation
- Also: `mcp__Hugging-Face__hub_repo_search` with `sort: trendingScore`

### 4. X (Twitter)
- Primary: WebSearch filtered to `site:x.com` for AI news that day
- Future improvement: curate a list of key accounts to track
  (e.g. @sama, @ylecun, @karpathy, @AnthropicAI, @GaryMarcus, @jeffdean)

## Theme Selection Criteria

Pick themes that are:
- **Surprising or counter-intuitive** — not just "AI is advancing"
- **Cross-domain** — shows AI touching something unexpected
- **Actionable** — someone could do something with this info
- **Contrarian** — includes pushback or limitations, not just hype
- **Timely** — tied to something that happened this week, not evergreen

Avoid:
- Themes that are just "X released a new model" with no angle
- Pure academic abstractions with no practical implication
- Repetition of the same theme across multiple sources

## Feedback Loop

After posting, send a Slack DM to the user (`U0AJKBAQ29H`) asking:
1. Were the 5 themes well-chosen?
2. Any sources that felt weak or inaccessible?
3. Tone/depth calibration?
4. Anything missing?

Store all feedback in `daily_ai_news/feedback_log.md` and adjust instructions above.

## Session Log

| Date       | HN accessible? | Themes quality | User feedback |
|------------|---------------|----------------|---------------|
| 2026-06-19 | ❌ 403 blocked | First run — TBD | Pending       |

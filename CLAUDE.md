# Claude Brain — Daily AI News Routine

This repository is a scheduled Claude Code routine that runs **daily at 8am Brasília time (UTC-3)**.

It scrapes 4 sources, extracts 5 themes per source in natural language, posts each as a separate message to the `#daily-ai-news` Slack channel (`C0BAAEKT6G7`), and then asks Giulia for feedback to improve future sessions.

---

## What This Routine Does

Each run:

1. **Scrapes** Hacker News, GitHub Trending, Hugging Face Papers, and X/Twitter for today's AI/tech highlights
2. **Identifies** 5 themes per source — not just link dumps, but plain-language explanations of *why something matters*
3. **Posts** 4 separate Slack messages (one per source) to `#daily-ai-news`, each with the prefix `🗞 Daily AI News — <Source> | <Date>`
4. **Asks** Giulia a feedback question at the end about today's selection

---

## Instructions for Each Run

### Step 1 — Scrape all 4 sources in parallel

**Hacker News:**
- Try `WebFetch` on `https://news.ycombinator.com/news` first
- If blocked (403), use `WebSearch` with query: `hacker news top stories today <Month Day Year>`
- Fallback: `WebFetch` on `https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=30`
- Target: top 20-30 stories with titles, points, and URLs

**GitHub Trending:**
- Use `WebFetch` on `https://github.com/trending?since=daily&spoken_language_code=en`
- Also try the AI/ML filter: `https://github.com/trending?since=daily&q=ai+machine+learning`
- Target: top 15-20 trending repos with name, description, stars today

**Hugging Face Papers:**
- Use `mcp__Hugging-Face__paper_search` with queries relevant to recent AI topics:
  - `"reasoning agents autonomous <current year>"`
  - `"multimodal vision language <current year>"`
  - `"safety alignment <current year>"`
- Also try `mcp__Hugging-Face__hub_repo_search` with `sort: "trendingScore"` for trending models
- Target: top 10-15 papers sorted by upvotes

**X/Twitter:**
- Use `WebSearch` with query: `trending AI artificial intelligence news today <Month Year> site:x.com OR Twitter`
- Also search: `AI news today <Month Day Year> X Twitter trending`
- Supplement with `WebSearch` for broader AI news of the day
- Target: 5-7 trending topics or discussions

### Step 2 — Synthesize 5 themes per source

For each source, identify 5 themes. A theme is **not** just a link or a headline — it is:
- A clear, jargon-free explanation of what is happening
- *Why it matters* for developers, businesses, or society
- Written as if explaining to a smart non-expert over coffee
- 3-5 sentences per theme

**Good theme criteria:**
- Has a clear "so what?" — not just interesting but consequential
- Connects to broader trends where possible
- Uses concrete numbers, names, or examples when available
- Avoids buzzword soup ("revolutionary paradigm shift in synergistic AI")

**Theme selection priorities:**
- Prefer stories with high engagement (points, stars, upvotes)
- Mix technical and business/societal angles (not all deep ML papers)
- Watch for topics that appeared across multiple sources (cross-source signal)
- Lean toward topics that are new or escalating, not long-running evergreen stories

### Step 3 — Post to Slack

Post **4 separate top-level messages** to channel `C0BAAEKT6G7`.

Message format for each:
```
*🗞 Daily AI News — <Source Name> | <Month Day, Year>*
_5 themes worth understanding today, in plain language_

━━━━━━━━━━━━━━━━━━━━━━━

*1. <emoji> <Theme Title>*
<3-5 sentence plain language explanation>

*2. <emoji> <Theme Title>*
...

*3. <emoji> <Theme Title>*
...

*4. <emoji> <Theme Title>*
...

*5. <emoji> <Theme Title>*
...

━━━━━━━━━━━━━━━━━━━━━━━
_Source: <linked source name> · Routine by Claude Brain_
```

Source names and links:
- Hacker News → `<https://news.ycombinator.com/news|Hacker News>`
- GitHub Trending → `<https://github.com/trending|GitHub Trending>`
- Hugging Face Papers → `<https://huggingface.co/papers|Hugging Face Papers>`
- X / Twitter → `X (Twitter) trends via web`

### Step 4 — Ask for feedback

After posting all 4 messages, post a **5th follow-up message** to the same channel asking for feedback:

```
*👋 Hey Giulia — feedback request for today's digest!*

I've just posted today's 4 source digests above. To keep improving this routine, I'd love to know:

• *Which source had the most useful selection today?* (HN / GitHub / HuggingFace / X)
• *Were there any themes that missed the mark?* (too technical, too obvious, not relevant?)
• *Anything you wish I'd covered but didn't?*
• *Any format tweaks?* (shorter? longer? different emoji style? less jargon?)

Your feedback gets baked into tomorrow's run. Reply here or in any thread above! 🙏
```

---

## Improvement Tracking

After each session, append a brief note to the `## Session Log` section at the bottom of this file:

```
### <Date>
- Feedback received: <summary of user's feedback>
- Changes applied for next run: <what was changed>
```

This creates a growing memory of what works well and what doesn't.

---

## Source Fallback Strategy

| Source | Primary | Fallback 1 | Fallback 2 |
|--------|---------|------------|------------|
| Hacker News | WebFetch hn.com | WebSearch "HN top stories today" | Algolia API |
| GitHub | WebFetch github.com/trending | WebSearch "GitHub trending today" | mcp__github__search_repositories |
| Hugging Face | mcp__Hugging-Face__paper_search | WebFetch huggingface.co/papers | WebSearch "HuggingFace trending papers" |
| X/Twitter | WebSearch "X Twitter AI trending today" | WebSearch "AI news today site:x.com" | General AI news WebSearch |

---

## Slack Channel

- **Channel:** `#daily-ai-news`
- **Channel ID:** `C0BAAEKT6G7`
- **Workspace:** vetto-ai.slack.com
- **Schedule:** Daily at 08:00 Brasília time (BRT = UTC-3, so 11:00 UTC)

---

## Session Log

### 2026-06-16 (First Run)
- Initial setup and first run completed
- Sources covered: Hacker News, GitHub Trending, Hugging Face Papers, X/Twitter
- HN was blocked via direct WebFetch; used WebSearch fallback successfully
- HuggingFace papers page was blocked; used paper_search MCP tool successfully
- Feedback received: _pending_
- Changes applied: _pending user response_

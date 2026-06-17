# Claude Brain — Daily AI News Routine

## What This Routine Does

Every day at 8am BRT (11am UTC), this session sends a curated AI news digest to the `#daily-ai-news` Slack channel (channel ID: `C0BAAEKT6G7`).

It scrapes **4 sources** and posts **one Slack message per source** — each as a standalone thread opener with the prefix `📰 *Daily AI News | [Source]* — [Date]`.

Each message contains **5 themes** explained in plain, natural language (no jargon, no bullet-point dumps).

---

## Sources to Scrape Each Day

### 1. Hacker News (`news.ycombinator.com`)
- Primary: Try `WebFetch` on `https://news.ycombinator.com/front?day=YYYY-MM-DD`
- Fallback 1: `WebSearch` for `hacker news [date] top stories`
- Fallback 2: `WebSearch` for `site:ycombinator.com [date]`
- Fallback 3: Check `https://blog.mean.ceo/hacker-news-trends-[month]-[year]/` for trend summaries
- Focus: tech, AI, security, programming, science, business

### 2. GitHub Trending (`github.com/trending`)
- Primary: `WebFetch` on `https://github.com/trending/python?since=daily`
- Also try: `https://github.com/trending` (all languages)
- Pull: top 15 repos, note stars gained today, repo description
- Focus: AI/ML, developer tools, agents, infrastructure

### 3. Hugging Face AI (`huggingface.co`)
- Use MCP tools: `mcp__Hugging-Face__paper_search` with queries like:
  - `"AI agents 2026"`
  - `"multimodal LLM 2026"`
  - `"AI reasoning efficiency [current year]"`
  - `"open source model release [current month]"`
- Also try: `mcp__Hugging-Face__hub_repo_search` for trending models
- Focus: new paper releases, trending models, research breakthroughs

### 4. X / AI Industry News
- Use `WebSearch` with queries like:
  - `"AI news today [date] model release"`
  - `"AI industry news June [year] LLM"`
  - Check: `crescendo.ai/news`, `llm-stats.com/ai-news`, `dentro.de/ai/news`
- Focus: model releases, funding rounds, chip deals, product launches, policy

---

## Slack Message Format

```
📰 *Daily AI News | [Source Name]* — [Month DD, YYYY]

[2-line intro contextualizing today's selection]

*1. [Emoji] [Theme Title]*
[3-4 sentence natural language explanation of WHY this matters, not just what it is]

*2. [Emoji] [Theme Title]*
[...]

*3. [Emoji] [Theme Title]*
[...]

*4. [Emoji] [Theme Title]*
[...]

*5. [Emoji] [Theme Title]*
[...]

---
_Sources: [source URL] · [Date] | This digest is auto-curated daily at 8am BRT_
```

### Writing Guidelines
- **Natural language**: explain like to a smart friend, not a press release
- **WHY it matters**: always include why the topic is interesting/relevant, not just what happened
- **No jargon dumps**: if you use an acronym, define it once
- **Concrete**: prefer specific numbers, names, and implications over vague statements
- **5 themes per source** — pick the most interesting/varied ones, not just the top 5 by votes

---

## Selection Criteria (What Makes a Good Theme)

**Prefer:**
- Stories that explain something surprising or counterintuitive
- Things with real-world implications (security, money, infrastructure, science)
- Emerging trends (multiple signals pointing the same direction)
- Releases/launches with specific benchmarks or numbers
- Community debates that reveal something about the state of the field

**Avoid:**
- Pure marketing announcements with no technical substance
- Duplicate coverage (if 3 sources cover the same story, pick 1)
- Stories too niche for a general technical audience
- Listicles or aggregator roundups (go one level deeper)

---

## Feedback Loop (How This Routine Improves)

After sending the messages, this routine checks `feedback/` for any stored feedback from Giulia and incorporates it for the next run.

When Giulia replies with feedback, update `feedback/latest.md` with:
- Date
- Which themes were good
- Which themes to avoid next time
- Any new sources to try
- Any format changes requested

The feedback file is read at the START of each run to adjust selection and style.

---

## Feedback File Location
`feedback/latest.md`

---

## Notes on Blocked Sources
- `news.ycombinator.com` returns HTTP 403 via WebFetch — always use WebSearch fallback for HN
- `hnrss.org` also 403 — skip
- `hn.algolia.com` also 403 — skip
- `crescendo.ai` also 403 via WebFetch — use WebSearch snippet instead
- GitHub trending works via WebFetch (`github.com/trending/python?since=daily` works)
- HuggingFace MCP tools work reliably (`paper_search`, `hub_repo_search`)

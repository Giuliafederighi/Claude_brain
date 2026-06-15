# Daily AI News Routine

**Schedule:** Every day at 8:00 AM Brasília time (BRT = UTC-3 → post at 11:00 UTC)
**Slack channel:** `daily-ai-news` — ID `C0BAAEKT6G7`

## What this routine does

Scrapes 4 sources, selects 5 themes from each, and posts one parent message (thread starter) per source to the `daily-ai-news` channel. Each message uses the same prefix format. After all threads are posted, sends a feedback question.

---

## Message prefix format

```
📰 *Daily AI News | <Source> | <Mon DD, YYYY>*
```

Sources: `Hacker News`, `GitHub Trending`, `Hugging Face`, `X / Twitter`

---

## Step-by-step execution

### 1. Hacker News

**Goal:** Find today's 5 most interesting themes from the HN front page.

**How to fetch (try in order until one works):**
1. `WebSearch` query: `hacker news top stories today <Month Day Year>`
2. `WebSearch` query: `site:news.ycombinator.com top AI ML stories <date>`
3. `WebFetch` on `https://news.ycombinator.com/front?day=YYYY-MM-DD` (often 403 — skip if blocked)
4. `WebFetch` on `https://hn.algolia.com/api/v1/search_by_date?tags=front_page&hitsPerPage=30` (often 403 — skip if blocked)
5. Fall back to `WebSearch` for specific story titles seen in earlier search results

**Selection criteria (5 themes):**
- At least 1 AI/ML story
- At least 1 software engineering / developer tools story
- At least 1 broader tech/society/policy story
- Prioritize stories with high points (>100) or many comments (>100)
- Explain in plain language — no jargon, the WHY matters more than the what
- Check `feedback-log.md` for any user-specified topics to prioritize or skip

---

### 2. GitHub Trending

**How to fetch:**
- `WebFetch` on `https://github.com/trending?since=daily&spoken_language_code=en`
- Fallback: `WebSearch` query: `github trending repositories today <date>`

**Selection criteria (5 themes):**
- Prioritize repos with the highest star gain *today* (not total stars)
- At least 1 AI/ML repo if present
- Group adjacent themes (e.g. multiple finance tools → one "AI in finance" theme)
- Explain what the project does and why people are paying attention to it now
- Check `feedback-log.md` for topic preferences

---

### 3. Hugging Face

**How to fetch:**
- Use `mcp__Hugging-Face__hub_repo_search` with `sort: "trendingScore"`, `limit: 15`, `repo_types: ["model"]`
- Use `mcp__Hugging-Face__paper_search` with a query like `"language models agents reasoning <year>"`, `results_limit: 10`, `concise_only: true`
- Optionally run `hub_repo_search` for `repo_types: ["space"]` with `sort: "trendingScore"` for demo spaces

**Selection criteria (5 themes):**
- 3 from trending models, 1–2 from trending papers
- Explain the architecture innovation or use-case unlocked, not just the name
- Highlight when a model comes from a non-US lab (Chinese, Brazilian, European labs notable)
- Check `feedback-log.md` for depth preference (more technical vs. more accessible)

---

### 4. X / Twitter

**How to fetch (X blocks most scrapers — use search):**
- `WebSearch` query: `site:x.com AI trending discussion <date>`
- `WebSearch` query: `X Twitter AI news today <date>`
- Supplement with `WebSearch` for specific AI events/announcements that tend to drive X conversations

**Selection criteria (5 themes):**
- Cover: model releases, research announcements, policy/regulation, talent moves, community debates
- Prioritize what's generating actual discussion (replies, ratio) over pure marketing posts
- When X-specific data is sparse, synthesize from the AI news of the day that would logically be trending

---

## After posting all 4 threads

Send a feedback message in the same channel:

```
---
📋 *Daily Selection Feedback — help improve tomorrow's picks*

Today's 4 threads covered: HN, GitHub Trending, Hugging Face, and X.

A few questions to sharpen next session:
• Were any of the 5 themes per source *not* worth including?
• Any source where you wanted deeper technical detail vs. simpler explanation?
• Any topic area you'd like to see prioritized (e.g. more research papers, more tooling, more policy)?
• Any source you'd like added or swapped out?

Reply here and I'll update my selection criteria for tomorrow. 🙏
```

---

## Feedback loop

After the user replies to the feedback message:
1. Read the channel for replies after the feedback message timestamp
2. Update `feedback-log.md` with the date and the user's preferences
3. Incorporate those preferences into the NEXT run's selection criteria (read the log at the start of each run)

---

## Commit & push

After each successful run, commit a brief log entry to `run-log.md`:
```
YYYY-MM-DD | HN: ✅ | GitHub: ✅ | HF: ✅ | X: ✅ | Feedback sent: ✅
```

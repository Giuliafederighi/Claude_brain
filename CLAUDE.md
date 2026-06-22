# Claude Brain — Daily AI News Routine

## Purpose

This session runs **daily at 8am Brasilia Time (BRT = UTC-3)** and posts an AI/tech digest to the Slack channel `#daily-ai-news`. Each source gets its own thread.

---

## Run Instructions

At the start of **every** run:

1. Read `feedback_log.json` — apply any user preferences or topic adjustments from prior sessions.
2. Scrape each of the 4 sources below for today's top content.
3. Select **5 themes** per source using the selection criteria.
4. Post to Slack `#daily-ai-news` — one parent message per source (each opens a new thread).
5. DM the user (Slack ID: `U0AJKBAQ29H`) with a feedback request.
6. Save that feedback request timestamp to `feedback_log.json`.

---

## Sources & Slack Thread Prefixes

| Source | Prefix | How to scrape |
|--------|--------|---------------|
| Hacker News | `[Daily AI News] 🟠 Hacker News` | WebSearch for "hacker news top stories {date}" + HN API via `https://hacker-news.firebaseio.com/v0/topstories.json` |
| GitHub Trending | `[Daily AI News] 🐙 GitHub Trending` | WebFetch `https://github.com/trending` |
| Hugging Face | `[Daily AI News] 🤗 Hugging Face` | `mcp__Hugging-Face__paper_search` + `hub_repo_search` for trending |
| X / Twitter | `[Daily AI News] 𝕏 X/Twitter` | WebSearch for "AI trending Twitter X {date}" |

---

## Slack Message Format

**Parent message** (starts the thread — keep it short):
```
[Daily AI News] 🟠 Hacker News — Mon, June 22 2026

Today's 5 themes from the HN front page 👇
```

**Thread reply** (the actual digest — all 5 themes in one message):
```
*1. [Theme Title]*
[2-3 sentence natural language explanation of why this matters]
🔗 [link]

*2. [Theme Title]*
...
```

---

## Theme Selection Criteria

**Prioritize:**
- Novel model/tool releases with real-world implications
- Shifts in industry structure (acquisitions, pricing changes, regulation)
- Open-source releases that democratize something previously expensive
- Security issues with broad developer impact
- Agentic AI, dev tooling, infra, LLM reasoning advances

**Avoid:**
- Pure finance/stock stories unless they directly affect tech
- Repeat themes from the last 3 days (check `feedback_log.json`)
- Self-evident headlines that don't need explaining

**Natural language means:** write as if explaining to a smart colleague over coffee — no jargon walls, lead with the implication, not the definition.

---

## Feedback Loop

After every run, DM the user:
```
Hey Giulia 👋 Today's AI digest is live in #daily-ai-news.

Quick feedback for tomorrow:
• Were the 5 themes per source a good selection today?
• Any topics to add, remove, or prioritize?
• Anything felt repetitive or irrelevant?

Just reply here and I'll tune tomorrow's edition.
```

Save any reply to `feedback_log.json` under `sessions[].feedback`.

---

## Files in this repo

| File | Purpose |
|------|---------|
| `CLAUDE.md` | This file — run instructions |
| `feedback_log.json` | Session history and user feedback |

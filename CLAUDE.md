# Claude_brain — Session Instructions

This repo runs automated routines. When a session starts, check which routine to execute based on the session prompt or context.

## Daily AI News Digest

**Schedule**: Every day at 8am Brasília time (BRT = UTC-3)
**Slack channel**: #daily-ai-news (`C0BAAEKT6G7`)
**Instructions**: `routines/daily-ai-news/cron-prompt.md`

When this session is triggered as the daily news routine, execute the full instructions in `routines/daily-ai-news/cron-prompt.md` immediately. Do not wait for user input.

### Quick summary
1. Get today's date
2. Read `routines/daily-ai-news/feedback.md` for curation guidance
3. Check Slack channel for any feedback replies from yesterday → append to feedback.md and commit
4. Scrape 4 sources and post 4 separate threads to C0BAAEKT6G7:
   - **[HN]** Hacker News — 5 top stories via WebSearch
   - **[GH]** GitHub Trending — 5 repos via WebFetch `https://github.com/trending`
   - **[HF]** HuggingFace Papers — 5 papers via `mcp__Hugging-Face__paper_search`
   - **[X]** X/Twitter — 5 trending AI topics via WebSearch
5. For each source: post a main channel message, then 5 replies in its thread
6. Post a feedback request message in the channel

### Feedback loop
After each run, the routine asks for feedback in Slack. The next day's run:
- Reads channel history for replies from user `U0AJKBAQ29H`
- Appends any feedback to `routines/daily-ai-news/feedback.md`
- Commits and pushes to branch `claude/bold-knuth-nd1qtw`

This grows the curation quality over time. The user can also edit `feedback.md` directly.

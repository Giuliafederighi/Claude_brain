# Daily AI News Digest — Routine Instructions

## What This Routine Does
Every day at 8am Brasília time, this routine:
1. Scrapes Hacker News (https://news.ycombinator.com/news) for the day's top stories
2. Groups them into **5 themes** with natural-language summaries
3. Posts the digest to the `#daily-ai-news` Slack channel (ID: `C0BAAEKT6G7`)
4. Logs what was covered and waits for feedback to improve the next session

## How Themes Are Selected
- Aim for variety: not all 5 themes should be AI/LLM. Mix in science, programming culture, open source, security, society/philosophy.
- Prioritize stories that sparked large HN comment threads (discussion = community interest).
- Prefer stories that have a "why does this matter to a smart generalist?" angle — not just news summaries.
- Avoid pure press-release stories with no substance.
- Always include at least one non-tech human interest or science story if available.

## Fetching Strategy
- Direct HN fetch often returns 403. Workaround: use WebSearch for `hacker news [date]`, then fetch linked aggregators.
- Reliable sources: `thehackernews.com`, `llm-stats.com/ai-news`, `hnhiring.com`, Medium digests, `blog.mean.ceo/hacker-news-trends`.
- HN Algolia API (`hn.algolia.com/api/v1/search?tags=front_page`) may also be blocked — try it first anyway.

## Tone & Format
- Conversational, not corporate. Write like a smart colleague summarizing over coffee.
- Each theme: a bold title with emoji, 2–4 sentences of context, a "so what?" insight.
- End with a source line and a feedback request in the thread.
- Target ~1,000–1,200 words total across 5 themes.

---

## Session Log & Feedback

### 2026-06-15 (Session 1 — First Run)
**Themes covered:**
1. AI writing its own employer's code (Anthropic 80% Claude-written codebase + Microsoft MAI)
2. Agentjacking attack + Microsoft open-source hack targeting AI dev tools
3. Google suing Chinese cybercrime network using Gemini for phishing (Outsider)
4. Biology experiment compiler for robots (autonomous science)
5. Market shift from flashy AI demos to trust/auditability

**Status:** Sent ✅ — waiting for user feedback.

**Open questions for Giulia:**
- Was the security-heavy weighting right (2 out of 5 themes were security)? Or prefer 1 max?
- Should "Ask HN" community discussions count as a theme, or only external news?
- Prefer more startup/YC news? More science? More programming/tools?
- Any topics to always avoid (e.g. pure hiring posts, crypto)?

---

## Improvement Notes (to incorporate next session)
_(This section grows with each feedback round)_

- [ ] Try HN RSS feed as fetching fallback: `https://hnrss.org/frontpage`
- [ ] Track which themes repeat too often and force variety across days
- [ ] Add a "most-discussed" metric (comment count) as selection signal

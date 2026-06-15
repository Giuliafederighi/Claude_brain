# Daily AI News Digest — Routine Instructions

## What This Routine Does
Every day at 8am Brasília time, this routine:
1. Scrapes Hacker News (https://news.ycombinator.com/news) for the day's top stories
2. Groups them into **5 themes** with natural-language summaries
3. Posts the digest to the `#daily-ai-news` Slack channel (ID: `C0BAAEKT6G7`)
4. Logs what was covered and waits for feedback to improve the next session

## How Themes Are Selected

### Priority topics (fill as many of the 5 slots as possible with these):
1. **Model updates & releases** — new models, version bumps, capability announcements (any lab)
2. **Benchmarks & evals** — new benchmark results, leaderboard changes, eval methodology debates
3. **Data: training & labeling** — datasets released, synthetic data approaches, labeling pipelines, RLHF/RLAIF
4. **AI research papers** — notable arXiv/NeurIPS/ICML/ICLR papers, new techniques, findings that shift understanding
5. **AI infrastructure & tooling** — frameworks, inference optimization, fine-tuning tools (only if closely tied to the above)

### Topics to deprioritize or avoid:
- Security / cybercrime (max 1 slot, only if extremely significant — otherwise skip)
- Robotics, biology, autonomous science (not a focus area)
- Market trend commentary, startup funding, hiring
- Society/philosophy essays about AI
- Open source for its own sake (only include if it's a meaningful model or dataset release)

### Other rules:
- Prioritize stories that sparked large HN comment threads (community discussion = real signal).
- Prefer stories with concrete numbers: parameter counts, benchmark scores, dataset sizes.
- If a day is slow on AI papers, use a second model release or a strong eval story instead.

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

**Status:** Sent ✅

**Feedback received (2026-06-15):**
- Theme 1 (model/code news) was good ✅
- Themes 2–5 not interesting ❌
- Wanted instead: model updates, benchmarks, data training/labeling, AI papers
- Security: too heavy, deprioritize
- Instructions updated accordingly for next session.

---

## Improvement Notes (to incorporate next session)
_(This section grows with each feedback round)_

- [ ] Try HN RSS feed as fetching fallback: `https://hnrss.org/frontpage`
- [ ] Also search arXiv for AI papers discussed on HN: `site:arxiv.org hacker news [date]`
- [ ] Search `llm-stats.com/ai-news` and `huggingface.co/blog` for model/benchmark releases
- [ ] Track which themes repeat too often and force variety across days
- [ ] Add a "most-discussed" metric (comment count) as selection signal

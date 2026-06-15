# Hacker News Daily Digest — Routine Instructions

## Schedule
- **Frequency**: Daily at 8:00 AM BRT (Brasília, UTC-3)
- **Equivalent UTC**: 11:00 AM UTC

## Source
- **URL**: https://news.ycombinator.com/news (front page)
- **API fallback**: https://hacker-news.firebaseio.com/v0/topstories.json

## Network requirements
The following hosts must be in the environment's network egress allowlist:
- `news.ycombinator.com`
- `hacker-news.firebaseio.com`

## Target Slack destination
- **Workspace**: vetto-ai.slack.com
- **Delivery**: DM to Giulia Federighi (user_id: `U0AJKBAQ29H`)
- Use `user_id` as `channel_id` when calling `slack_send_message`

## How it works
1. Fetch the top 30 stories from HN front page
2. Pick the 5 most interesting/trending stories of the day
3. Group those 5 stories by detected theme
4. For each theme group, write 2–3 sentences in natural language explaining what's happening and why it matters
5. Send a single DM with all theme groups

## Themes (auto-detected, calibrated over time)
Themes are inferred fresh from each day's stories — no fixed list. After each run, Giulia can say "add X theme", "merge Y and Z", or "skip stories about W" and this file is updated accordingly. Common themes that tend to emerge:
- AI / Machine Learning
- Security / Privacy
- Startups / Business
- Science / Research
- Open Source / Developer Tools
- Policy / Law / Society

## Stories per digest
- **5 stories total** per day, selected for relevance and variety
- Grouped under their detected theme heading
- Each story shown as a bullet with title, link, and point score

## Message format
```
🗞️ *HN Morning Digest — {date (BRT)}*

*{Theme 1}*
{2–3 sentences: what's happening, why it matters, what to expect}
• <link|Story title> ({points} pts)
• <link|Story title> ({points} pts)

*{Theme 2}*
{2–3 sentences}
• <link|Story title> ({points} pts)
...
```

## Growth log
Track questions asked and answers received to evolve these instructions.

| Date | Question asked | Answer |
|------|---------------|--------|
| 2026-06-15 | Which Slack channel? | DM to self (U0AJKBAQ29H) |
| 2026-06-15 | Timezone for 8am? | BRT — Brasília (UTC-3) |
| 2026-06-15 | Fixed themes or auto-detect? | Auto-detect, calibrate daily through conversation |
| 2026-06-15 | How many stories per day? | 5 total across all themes |
| 2026-06-15 | Summary depth (brief / detailed)? | 2–3 sentences per theme, natural language, why it matters |

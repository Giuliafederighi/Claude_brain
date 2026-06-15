# Hacker News Daily Digest — Routine Instructions

## Schedule
- **Frequency**: Daily at 8:00 AM
- **Timezone**: TBD (ask user) — default UTC

## Source
- **URL**: https://news.ycombinator.com/news (front page)
- **API fallback**: https://hacker-news.firebaseio.com/v0/topstories.json

## Network requirements
The following hosts must be in the environment's network egress allowlist:
- `news.ycombinator.com`
- `hacker-news.firebaseio.com`

## Target Slack channel
- **Workspace**: vetto-ai.slack.com
- **Channel**: TBD (ask user — options: `#general` C04GP0BUNQ2, `#agents-general` C0AKGP05B6J)

## How it works
1. Fetch the top 30 stories from HN front page
2. Group stories by theme (auto-detected)
3. For each theme with ≥ 2 stories, write a short natural-language paragraph explaining the theme and why it matters
4. Send a single Slack message with all themes

## Themes (auto-detected from story content)
Themes are inferred dynamically from story titles each day. Common themes include:
- AI / Machine Learning
- Security / Privacy
- Startups / Business
- Science / Research
- Open Source / Developer Tools
- Policy / Law / Society

## Message format
```
🗞️ *HN Morning Digest — {date}*

*{Theme 1}*
{Natural language summary of 2-3 sentences explaining what's happening and why it matters}
• <link|Story title> ({points} pts)
• <link|Story title> ({points} pts)

*{Theme 2}*
...
```

## Growth log
Track questions asked and answers received to evolve these instructions.

| Date | Question asked | Answer |
|------|---------------|--------|
| 2026-06-15 | Which Slack channel? | — |
| 2026-06-15 | Timezone for 8am? | — |
| 2026-06-15 | Fixed themes or auto-detect? | — |
| 2026-06-15 | How many stories per theme? | — |
| 2026-06-15 | Summary depth (brief / detailed)? | — |

# Claude Brain — Daily AI News Routine

## What this does
Every day at **8:00 AM Brasilia Time (11:00 AM UTC)** Claude posts a multi-source AI news digest to the Slack channel `#daily-ai-news`, then asks for feedback to improve the next day's selection.

## Slack channel
- **Channel name**: `#daily-ai-news`
- **Channel ID**: `C0BAAEKT6G7`
- **User**: Giulia Federighi (`U0AJKBAQ29H`)

## Sources (one thread per source)
Each source gets its own **parent message** + **one reply in the thread** with 5 themes:

| # | Source | Method |
|---|--------|--------|
| 1 | **Hacker News** | WebSearch: `hacker news front page AI tech [today's date]` |
| 2 | **GitHub Trending** | WebSearch: `github trending AI repositories today` + mcp__github search |
| 3 | **Hugging Face Models & Spaces** | `mcp__Hugging-Face__hub_repo_search` + `mcp__Hugging-Face__space_search` |
| 4 | **Hugging Face Papers** | `mcp__Hugging-Face__paper_search` |
| 5 | **X / Twitter AI** | WebSearch: `AI Twitter X news today [date]` |

> Note: Direct access to news.ycombinator.com and hn.algolia.com returns HTTP 403 in this environment. Use WebSearch as the fallback.

## Post format

### Parent message (one per source)
```
:rolled_up_newspaper: Daily AI Digest | [Date] | [Source Name]
```

### Reply in thread (the 5 themes)
```
1. [Bold Title]
[2–3 sentence plain-language explanation of why this matters]

2. ...
```

### After all 4 sources — feedback message (standalone, NOT in any thread)
```
:wave: *How was today's AI digest?*

Was the selection good? Reply here and tomorrow's digest will reflect your feedback:
• :+1: Which themes were most interesting?
• :-1: Anything irrelevant or too technical?
• :bulb: Any topics you'd love to see more (or less) of?
• :arrows_counterclockwise: Preferred sources or angles?

_All feedback is saved and improves tomorrow's selection automatically._ :robot_face:
```

## Feedback loop
1. **Before posting**: read `feedback.json` in this repo for any saved preferences
2. **Before posting**: search Slack for recent replies to the feedback message (`slack_search_public_and_private` with `in:daily-ai-news`) and check thread replies on the last feedback message
3. **After reading feedback**: apply preferences when selecting the 5 themes per source
4. **After posting**: update `feedback.json` with date of run and any new feedback found

## Theme selection criteria (defaults — updated by feedback)
- **Prefer**: practical implications, open-source releases, business strategy shifts, research breakthroughs with clear real-world impact
- **Avoid**: pure hype without substance, highly technical papers with no accessible angle, duplicate stories covered the day before
- **Tone**: natural language, written for a smart generalist — not a researcher. Explain *why it matters*, not just *what it is*
- **Diversity**: aim for variety across: tools/infra, research/science, business/industry, policy, and one wildcard

## Files in this repo
- `CLAUDE.md` — this file, routine config and instructions
- `feedback.json` — saved user preferences and feedback history

# Claude Brain — Daily AI News Routine

## What this routine does

Every day at 8am Brasilia time (UTC-3), this routine:

1. Scrapes 4 sources for the day's most interesting AI/tech news
2. Selects 5 themes per source, explained in plain natural language
3. Posts to the `#daily-ai-news` Slack channel (`C0BAAEKT6G7` in `vetto-ai.slack.com`)
4. Each source gets its **own top-level message** (thread starter) with the prefix:
   `📰 *Daily AI News | [Date] — [Source]*`
5. Ends each message with a feedback prompt so the user can improve tomorrow's selection

## Sources

| Source | Method | Notes |
|--------|--------|-------|
| Hacker News | WebSearch (HN blocks direct scraping) | Front page top stories |
| GitHub Trending | WebFetch `https://github.com/trending` | Today's trending repos |
| Hugging Face | `mcp__Hugging-Face__paper_search` + `hub_repo_search` | Latest papers & models |
| X (Twitter) | WebSearch for trending AI topics | Public timeline signal |

## Slack channel

- **Channel:** `#daily-ai-news`
- **Channel ID:** `C0BAAEKT6G7`
- **Workspace:** `vetto-ai.slack.com`
- Each source = one top-level message in the channel (4 messages per day total)

## Message format

Each message contains:
- Emoji prefix + bold title with date and source name
- 5 numbered themes, each with:
  - An emoji
  - A bold title (what it is)
  - 2-3 sentences in plain language (no jargon, explain as if to a smart non-technical person)
- Footer asking for feedback on that source's selection

## Improvement loop

After each run, watch for reply feedback in the `#daily-ai-news` threads. The user may indicate:
- Topics were too technical / not relevant
- A source was better or worse quality than others
- New sources to add
- Preferred tone or depth adjustments

Update this file's **feedback log** below after each session.

---

## Feedback log

### 2026-06-21 (first run)

**Sources used:** Hacker News (via WebSearch), GitHub Trending (via WebFetch), HuggingFace Papers (via MCP), X/Twitter (via WebSearch)

**Themes selected:**

*HN:* Fable 5 export ban, open-weight models, AI chatbots as news source, Google smart speaker, AI hiring shift

*GitHub:* AI video production, token compression (headroom), real-time intelligence dashboards, AI memory/knowledge graphs, long-horizon agents (deer-flow)

*HuggingFace:* $15 AI research papers, real-time agent reasoning (AgileThinker), multi-agent efficiency (MARS), AI governance gaps, web agent CoT (WebCoT)

*X:* Karpathy joins Anthropic, Grok expansion, Fable 5 export ban debate, Qualcomm/Tenstorrent acquisition, enterprise AI infrastructure shift

**User feedback:** _[pending — user will reply in Slack threads]_

**Improvements to apply next session:** _[pending]_

---

## Running the routine manually

This routine is designed to be triggered by Claude Code on the web as a scheduled session.
The trigger: run this repo's scheduled Claude session at 8am BRT (11:00 UTC).

To run manually: open a Claude Code session on this repo and ask:
> "Run the daily AI news routine"

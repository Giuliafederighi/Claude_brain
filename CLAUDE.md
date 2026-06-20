# Claude Brain — Daily AI News Digest

## Purpose
Every day at 8am Brasilia time (UTC-3), post a curated AI news digest to the Slack channel `#daily-ai-news` (ID: `C0BAAEKT6G7`). Each source gets its own top-level message in the channel. Summarize 5 themes per source in natural, conversational language — not bullet dumps.

## Sources
| Source | What to look for |
|--------|-----------------|
| **Hacker News** (news.ycombinator.com) | Top stories with tech/AI relevance — use WebSearch since direct fetch is blocked |
| **GitHub Trending** | Trending repos, especially AI/ML — use WebSearch |
| **Hugging Face** | Trending models, datasets, papers — use `mcp__Hugging-Face__hub_repo_search` and `mcp__Hugging-Face__paper_search` |
| **X / Twitter** | Trending AI conversations and platform developments — use WebSearch |

## Message Format
Each source message must:
- Start with prefix: `🗞 *Daily AI News · [Source Name]* | [Date]`
- Contain exactly **5 themes**, numbered and bolded
- Be written in plain, natural language — imagine explaining to a smart colleague who isn't deep in AI day-to-day
- End with a `_📊 Sources: ..._` line

## Feedback Loop — READ THIS FIRST ON EVERY RUN

**Step 1: Read preferences**
Read `feedback/preferences.md` in this repo for any standing preferences from the user.

**Step 2: Check last night's feedback**
Read the thread on the most recent HN message in `#daily-ai-news` using `mcp__Slack__slack_read_thread`. Look for user replies to the feedback prompt. If feedback was given:
- Update `feedback/preferences.md` with any new preferences
- Apply them to today's selection
- Acknowledge the feedback in today's digest footer

**Step 3: Generate and post**
Fetch fresh content from all 4 sources, apply preferences, post 4 messages.

**Step 4: Post feedback request**
Always post a feedback request as a *thread reply* on the HN message (the first one posted). Use the standard template from `feedback/feedback_template.md`.

**Step 5: Commit**
If preferences were updated, commit `feedback/preferences.md` with message: `chore: update digest preferences [date]`

## Tone Guidelines
- Conversational, not corporate
- Explain WHY something matters, not just WHAT it is
- Use analogies when helpful
- Flag genuinely important security/safety items clearly
- No clickbait, no hype without substance

## Slack Channel
- Channel name: `#daily-ai-news`
- Channel ID: `C0BAAEKT6G7`
- Workspace: vetto-ai.slack.com
- Created by: Giulia Federighi

## Branch
All commits go to: `claude/bold-knuth-jayzt3`

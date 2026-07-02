# daily-ai-news routine — playbook

Living spec for the automated daily AI-news digest posted to the private
Slack channel `#daily-ai-news` (channel ID `C0BAAEKT6G7`, workspace
`vetto-ai`). This file is the durable memory for the routine. Update it in
place whenever format, sources, or selection criteria change based on
Giulia's feedback — do not fork a new file or a new naming convention next
time, edit this one, so the next scheduled run picks up the latest version
instead of drifting. See `CLAUDE.md` for why that matters.

## Schedule

- Every morning, target **8:00am America/Sao_Paulo (Brasília, UTC-3)**.
- Runs as a scheduled Claude Code session triggered against this repo.

## Sources (exactly these 4 — no more, no less, unless Giulia asks)

Each source gets its own top-level Slack message that starts a thread:

| # | Source | Prefix |
|---|--------|--------|
| 1 | Hacker News (news.ycombinator.com) | `📰 Daily AI News \| Hacker News \| <date>` |
| 2 | GitHub Trending | `📰 Daily AI News \| GitHub Trending \| <date>` |
| 3 | Hugging Face (papers + trending models/spaces) | `📰 Daily AI News \| Hugging Face \| <date>` |
| 4 | X / Twitter (AI community discussion) | `📰 Daily AI News \| X / Twitter \| <date>` |

Note: several past runs (see git history of PRs #1–#17) also posted a 5th
"main AI Daily News" message sourced from Giulia's email inbox (The
Information newsletter, etc.). That was never part of the original request
and is **dropped as of 2026-07-02** — it caused missed days when the source
email hadn't landed by run time, and diluted the 4-source structure the
user actually asked for. If Giulia wants it back, re-add it as a 5th row
here with its own fetch strategy.

### Message structure

Parent message = one-line teaser. First reply in that thread = the 5 themes.
Keep the parent short so the channel list stays scannable; put the
substance in the thread.

```
Parent:  📰 Daily AI News | <Source> | <Month Day, Year>
         5 themes from today — plain language, no jargon.

Reply:   _Today's 5 themes from <Source>:_

         *1. <Punchy, specific title>*
         <2-4 sentence paragraph in natural language explaining what
         happened and why it matters. Name real people/projects/repos/
         numbers — no vague trend-speak.>

         *2. ...*
         ...

         _Sources: <links>_
```

After all 4 threads, post one more standalone message: a feedback request.
Ask a **specific, answerable question** (e.g. "Was the GitHub pick today
too niche, or on target?") rather than an open-ended "how was it?" — open
prompts have gone unanswered for 12+ days running (see feedback-log.md).
Explicitly ask for a text reply in the thread, since reactions alone can't
convey what to change.

## Fetching strategy per source

- **Hacker News**: `news.ycombinator.com` and `hn.algolia.com` are blocked
  by this environment's network egress policy (confirmed via curl CONNECT
  403 and WebFetch 403 — this is a proxy-level policy denial, not a
  site-side block). Reconstruct via `WebSearch` scoped to
  `site:news.ycombinator.com` plus general current AI/tech search, and say
  so in the digest when the picks are search-reconstructed rather than a
  literal live front-page pull.
- **GitHub Trending**: `mcp__github__search_repositories` (e.g.
  `created:>N-days-ago stars:>100`, sorted by stars) or WebFetch on
  `github.com/trending` — both work, no egress restriction via the GitHub
  MCP path.
- **Hugging Face**: `mcp__Hugging-Face__hub_repo_search` (sort by
  `trendingScore`) and `mcp__Hugging-Face__paper_search`. Works fine, real
  data, no egress restriction.
- **X / Twitter**: `x.com`/`twitter.com` blocked the same way as HN.
  Reconstruct via `WebSearch` for what the AI community is currently
  discussing (funding, launches, policy, prominent researcher posts), citing
  the news articles that surfaced it rather than x.com links you can't
  verify by fetching. Say this is a reconstruction, not a live scrape.

If Giulia wants true live scraping of HN/X, that requires the environment's
network policy to allow those domains — an environment-level setting
changed outside the session (code.claude.com), not something fixable from
inside a run. Ask her rather than silently keep substituting indefinitely.

## Curation rules

- Never repeat a story/repo/model covered in the last 2 days verbatim — if
  it's still developing, find the new angle or drop it. Each day's playbook
  update (or feedback-log entry) should carry forward a short "recently
  covered" list per source so the next run can dedupe.
- Prefer concrete specifics (real names, numbers, repos, papers) over
  trend-speak.
- Write for someone who doesn't read AI news daily — explain jargon inline,
  don't assume it.
- If a source's fetch fails entirely, do not silently skip it — try the
  fallback strategy above, and if it still fails, post the thread with an
  explicit note explaining what failed, then log it in feedback-log.md.
  Silent skips (see June 26/27/30 in feedback-log.md) are the thing to
  avoid.

## Known constraint: sandboxed network egress

This session's outbound network goes through a policy-enforced proxy that
returns 403 for arbitrary external hosts, confirmed for
`news.ycombinator.com`, `hn.algolia.com`, and `x.com`. GitHub and Hugging
Face MCP tools are unaffected. See "Fetching strategy" above for the
per-source workaround. Re-test at the start of each run in case the policy
changes (`curl -sS "$HTTPS_PROXY/__agentproxy/status"` shows recent relay
failures if you want to confirm without spending a full page fetch).

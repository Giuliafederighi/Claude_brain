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

**Added 2026-07-08 — defaulting on stale open questions**: by this date the
"Open questions for Giulia" list in `feedback-log.md` had gone 20+ days with
zero text replies to *any* of them. Re-asking the identical question forever
without a response is a dead loop, not a feedback mechanism. New policy: if
an open question gets no reply for a few more runs after it's been proposed
with a specific default attached (e.g. "I'm planning to just report GitHub
Trending honestly even when it's agent-tooling-heavy, object if you'd
rather I curate around it"), adopt that default, mark the question resolved
in `feedback-log.md`, and stop re-asking it daily. Always stated as
overridable — a reply at any time (even after a default is adopted) should
still change behavior going forward. This keeps the log from accumulating
questions nobody's answering while still leaving the door open.

## Fetching strategy per source

- **Hacker News**: `news.ycombinator.com` and `hn.algolia.com` are blocked
  by this environment's network egress policy (confirmed via curl CONNECT
  403 and WebFetch 403 — this is a proxy-level policy denial, not a
  site-side block). Reconstruct via `WebSearch` scoped to
  `site:news.ycombinator.com` plus general current AI/tech search, and say
  so in the digest when the picks are search-reconstructed rather than a
  literal live front-page pull.
- **GitHub Trending**: WebFetch on `github.com/trending?since=daily` works
  directly (confirmed 2026-07-04, not blocked by egress policy) and returns
  real trending data with today's star deltas — prefer it over
  `mcp__github__search_repositories`, whose `created:>N-days-ago stars:>100`
  query returns mostly noise (spam/crypto repos, non-English filler) rather
  than genuine trending content. Use the search API only as a fallback or to
  pull more detail on a repo already found via the trending page.
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

**Process note (added 2026-07-06)**: run the 4 source-research tasks as
parallel subagents (one per source, each briefed with that source's
fetching strategy and the current "recently covered" list to dedupe
against) rather than serially in the main session. Confirmed faster
wall-clock with no quality loss — keep this as the default.

## Curation rules

- Never repeat a story/repo/model covered in the last 2 days verbatim — if
  it's still developing, find the new angle or drop it. Each day's playbook
  update (or feedback-log entry) should carry forward a short "recently
  covered" list per source so the next run can dedupe.
- **Added 2026-07-08**: also cross-check the 4 sources' picks *against each
  other* for the same run, not just against prior days. Running 4 sources in
  parallel means two sources can independently surface the same underlying
  story (e.g. HN and X both picking up the same Anthropic research release)
  — if that happens, swap one of them out for a different theme before
  posting rather than letting the same story appear twice in one day's
  channel.
- Prefer concrete specifics (real names, numbers, repos, papers) over
  trend-speak.
- Write for someone who doesn't read AI news daily — explain jargon inline,
  don't assume it.
- If a source's fetch fails entirely, do not silently skip it — try the
  fallback strategy above, and if it still fails, post the thread with an
  explicit note explaining what failed, then log it in feedback-log.md.
  Silent skips (see June 26/27/30 in feedback-log.md) are the thing to
  avoid.
- **Adopted 2026-07-09 (proposed 2026-07-08, unopposed across 2 more
  runs)**: report each source's content honestly even when it's lopsided —
  don't manufacture artificial diversity. Concretely: if GitHub Trending's
  actual top-15 page is 50-65%+ agent-tooling repos, pick your 5 from what's
  genuinely there rather than steering around it; if Hacker News's front
  page genuinely leans security/policy (or any other slant) for several
  days running, keep reporting that lean rather than forcing a broader mix
  that isn't really on the page. Both are now standing defaults, always
  overridable by a reply from Giulia in the feedback thread.
- **Added 2026-07-10**: the "recently covered" rolling list in
  `feedback-log.md` only holds ~3 days, so it can miss a story that
  resurfaces after a longer gap (caught today: a Hugging Face pick was the
  exact same story posted 7 days earlier). Before finalizing picks, spot-
  check anything that reads like it could be a repeat against the fuller
  Slack channel history (`slack_read_channel` over more days, or
  `slack_search_public` for the specific name/repo/model), not just the
  3-day list — asked Giulia in today's feedback thread whether this extra
  check is worth doing every day or overkill.
- **Added 2026-07-10**: on a day a source's raw page is genuinely thin
  once already-covered stories are excluded (e.g. GitHub Trending, once
  repeat agent-tooling repos are stripped out, had only 4 real picks),
  default until told otherwise: say so honestly as the 5th entry (name
  what's actually left — usually evergreen infra with tiny deltas — rather
  than dressing it up as news). Asked Giulia today whether she'd rather
  that, a near-repeat from 2-3 days ago, or just 4 themes that day instead
  of 5 — no default adopted yet since this is the first time it came up.

## Known constraint: sandboxed network egress

This session's outbound network goes through a policy-enforced proxy that
returns 403 for arbitrary external hosts, confirmed for
`news.ycombinator.com`, `hn.algolia.com`, and `x.com`. GitHub and Hugging
Face MCP tools are unaffected. See "Fetching strategy" above for the
per-source workaround. Re-test at the start of each run in case the policy
changes (`curl -sS "$HTTPS_PROXY/__agentproxy/status"` shows recent relay
failures if you want to confirm without spending a full page fetch).

# daily-ai-news routine

Living spec for the automated daily AI-news digest posted to the private Slack
channel `#daily-ai-news` (channel ID `C0BAAEKT6G7`, workspace `vetto-ai`).
This file is the durable memory for the routine — update it whenever the
format, sources, or selection criteria change based on Giulia's feedback, so
the next scheduled run picks up the latest version instead of drifting.

## Schedule

- Runs every morning, target **8:00am America/Sao_Paulo (Brasília, UTC-3)**.
- Triggered as a scheduled Claude Code session against this repo.

## What gets posted

Five separate top-level messages in `#daily-ai-news`, each a new thread:

1. **Main "AI Daily News" digest** — compiled from Giulia's inbox (The
   Information's AM newsletter + other subscriptions via Gmail). Posted
   directly in the channel (not threaded), ~8:03am local. Skip this post for
   the day if the source newsletter email hasn't arrived yet by run time —
   do not fabricate it from search results. Format: `:newspaper:` or
   `:robot_face:` header, numbered top stories with one-line summaries,
   optional themed sub-sections (business, product, policy), source line.

2. **`[HN]` Hacker News AI Digest** — 5 themes from HN's AI-relevant
   discussion, explained in plain language (no jargon). Parent message is a
   one-line teaser; the actual 5 themes go in the first thread reply.

3. **`[GH]` GitHub Trending Digest** — 5 themes from trending/fast-growing
   AI-relevant repos. Same parent/thread-reply structure.

4. **`[HF]` HuggingFace AI Digest** — 5 themes from trending models, papers,
   and spaces. Same structure.

5. **`[X]` X/Twitter AI Digest** — 5 themes from what the AI community is
   discussing on X. Same structure.

Then a final **feedback-request message**: `:wave: How was today's AI
digest?`, listing what each source covered in one line, plus 2-3 open
questions. This is the mechanism for "keep growing the instructions" — reply
content (in Slack or in conversation) should be folded into this file before
the next run.

### Per-theme format (inside each thread reply)

```
_Today's 5 themes from <Source>:_

*1. <Punchy, specific title>*
<2-4 sentence paragraph in natural language explaining what happened and why
it matters — no unexplained jargon, write for someone who doesn't read AI
news daily.>

*2. ...*
...

_Sources: <links>_
*Sent using* <@U0AQBNP0JLT|Claude>
```

Keep each theme concrete (name real repos/papers/people/numbers) rather than
vague trend-speak. Avoid repeating the exact same story two days running —
if a story is still developing, find the new angle instead of restating it.

## Known constraint: sandboxed network egress

This session's outbound network goes through a policy-enforced proxy that
returns 403 for arbitrary external hosts, including
`news.ycombinator.com`, `hn.algolia.com`, `hacker-news.firebaseio.com`, and
(by extension) `x.com`/`twitter.com`. Confirmed via both `curl` (proxy-level
403 on CONNECT) and `WebFetch` (403 from the tool). This means direct
scraping of HN and X is currently **not possible** from this environment.

Working fallback until/unless broader egress is granted:
- **HN**: reconstruct themes from `WebSearch` results scoped to
  `news.ycombinator.com` (real item titles/threads), cross-checked against
  general AI-news search. This is not a literal live front-page pull — say
  so in the digest when used.
- **X**: reconstruct from `WebSearch` general AI-news coverage plus any
  X-hosted links search surfaces. Same caveat.
- **GitHub**: use `mcp__github__search_repositories` (works fine, no egress
  restriction — it's an MCP tool, not raw fetch). Good proxy for "trending":
  query `created:>N-days-ago stars:>100`, sort by stars.
- **HuggingFace**: use `mcp__Hugging-Face__hub_repo_search` (sort by
  `trendingScore`) and `mcp__Hugging-Face__paper_search`. Works fine, real
  data, no egress restriction.
- **Main digest**: use Gmail MCP (`mcp__Gmail__search_threads` with
  `from:hello@theinformation.com`) — works fine, no egress restriction.

If Giulia wants true live scraping of HN/X, this requires the session's
network policy to allow those domains (an environment-level setting, not
something changeable from inside a session) — ask her, don't just silently
keep substituting.

## Feedback log

Keep entries short: date, what Giulia said, what changed as a result. Newest
first.

- **2026-07-01**: First run captured in this file (routine had been running
  informally since 2026-06-15 with no persisted spec — this doc backfills
  the format observed in Slack history). Confirmed HN/X egress block is
  still in effect. Noted June 30 run skipped all four source-threads
  (only the main digest posted) — cause unconfirmed, worth watching for a
  repeat. Asked Giulia: (1) whether to request broader network egress for
  live HN/X scraping, (2) whether to keep the main inbox-based digest or
  drop it in favor of just the 4 sources, given it sometimes has to be
  skipped when the source email hasn't landed yet.

## Open questions for Giulia (carry forward until answered)

1. Broaden network egress for this environment so HN/X can be scraped live,
   or keep the WebSearch-based reconstruction?
2. Keep the inbox/"The Information"-based main digest, or drop it and stick
   to the 4 named sources (HN, GitHub, HF, X) from the original request?
3. Any topic to always include or always skip?
4. Any source to weight more/less, or a 5th source to add?

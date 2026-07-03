# Daily AI News — Slack Routine

Living spec for the recurring "daily-ai-news" Slack routine. This file is the
source of truth for how the routine runs. **It is meant to keep growing**:
every day, after posting, the routine asks Giulia how the picks landed, and
any real feedback gets folded back into this file (usually into "Standing
preferences" or "Things to avoid") so the next run is better calibrated.

## Schedule

- **When**: every day at 8:00am America/Sao_Paulo (Brasilia) time — fixed
  UTC-3 year-round (Brazil has not observed DST since 2019), i.e. 11:00 UTC.
- **Where**: Slack channel `#daily-ai-news` (private channel, ID `C0BAAEKT6G7`,
  workspace vetto-ai.slack.com).

## Sources & format

Four sources, run independently. For each source, pick exactly **5 themes**
worth explaining that day — not just a link dump. A "theme" is a subject, not
necessarily one single link: if two items are about the same underlying
thing, merge them into one theme. Bias toward genuinely interesting/important
material (new tech, AI, science, notable launches, real debates) over
clickbait, spam, or pure marketing.

Each theme gets:
- An emoji + a punchy 5-8 word title
- 2-4 sentences of **plain, natural language** — no unexplained jargon,
  written for someone who wasn't following the space themselves, explains
  what it is *and* why it matters
- A source link
- A rough traction signal where available (points/comments, stars, likes,
  downloads)

### Sources

1. **Hacker News** — https://news.ycombinator.com/news (current front page)
2. **GitHub** — trending repos (https://github.com/trending, `since=daily`,
   cross-checked with search_repositories), bias toward AI/dev-tooling but
   open to anything genuinely interesting
3. **Hugging Face** — trending models/datasets/papers/spaces (via the
   Hugging Face MCP tools: hub_repo_search, space_search, paper_search, and/or
   huggingface.co/models?sort=trending, huggingface.co/papers)
4. **X (Twitter)** — AI community discussion. **Known limitation**: no direct
   X/Twitter API or logged-in browsing is available. This source is
   necessarily reconstructed from secondary coverage (Techmeme, tech
   news sites, cached/indexed posts found via web search) rather than
   live X browsing. Always label items that are inferred from secondary
   coverage rather than a directly-viewed X post, and be conservative about
   presenting single-sourced/rumor-grade claims as settled fact.

## Posting protocol

- Each source gets its **own top-level Slack message** (i.e. its own thread
  starter) posted directly to `#daily-ai-news` — not a reply inside another
  source's thread.
- All 4 messages on a given day share the same date-stamped prefix so
  they're visually grouped, e.g.:
  `🧠 Daily AI Digest — Jul 3, 2026 · Hacker News`
  `🧠 Daily AI Digest — Jul 3, 2026 · GitHub`
  `🧠 Daily AI Digest — Jul 3, 2026 · Hugging Face`
  `🧠 Daily AI Digest — Jul 3, 2026 · X`
- Body of each message: the 5 formatted theme entries, back to back.

## The feedback loop (why this file grows)

After posting all 4 threads for the day, ask Giulia (via chat if she's
present in the session, otherwise via a notification/Slack message):

1. What stood out from today's picks — anything worth digging into further?
2. Was the theme selection good? Anything that shouldn't have made the cut,
   or something bigger that got missed?
3. Anything to change about tone, length, sources, or format for next time?

If real, actionable feedback comes back, update this file:
- Durable taste preferences → **Standing preferences** below
- Things to stop doing → **Things to avoid** below
- One-off notes → append a dated line under **Feedback log**

Don't let the file balloon — fold recurring feedback into a preference
rather than piling up redundant log lines.

## Standing preferences

*(empty so far — populate as real feedback comes in)*

## Things to avoid

*(empty so far — populate as real feedback comes in)*

## Feedback log

- **2026-07-03**: First run. Sent live as a demo when Giulia set up this
  routine (it happened to be ~8am Brasilia at setup time). Awaiting feedback
  on theme selection to seed the preferences above.

## Operational notes

- **Durable scheduling caveat**: this Claude session's own cron scheduler
  (`CronCreate`) is session-only and auto-expires after 7 days — it cannot
  run this forever on its own. For a truly permanent daily run, this needs
  to be wired up as a **Trigger** in Claude Code on the web (scheduled
  session), pointed at this repo/instructions file, on cron `0 11 * * *`
  (UTC). See https://code.claude.com/docs/en/claude-code-on-the-web.
- Github MCP, Hugging Face MCP, and Slack MCP tools are available in this
  environment and are what the routine should use for sources 2, 3, and the
  posting step, respectively. Source 1 (HN) and source 4 (X) rely on
  WebFetch/WebSearch since there's no dedicated MCP for either.

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
  **Added 2026-07-11**: spot-check 1-2 star counts from the fetched page
  against the live GitHub API (e.g. via a repo-details lookup) to confirm
  the WebFetch pull is current and not a cached/stale response — cheap
  sanity check, especially valuable on a day the page looks unusually thin
  or repeat-heavy, to rule out a bad fetch before concluding "nothing new."
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

**Adopted 2026-07-22 (proposed 2026-07-20, confirmed 07-21 and 07-22)**:
brief each source's research agent with **all 4 sources'** recent picks,
not just its own — two clean catches in a row (07-21: Kimi K3 and
Hassabis's essay; 07-22: the Anthropic/Physical Intelligence rumor) with
zero manual supplementary research needed, versus prior runs that needed
several extra search rounds to find clean replacements after the fact.
Standing default now, not just a proposal.

**Added 2026-07-23 — briefing catches prior-day repeats, not same-day
collisions between today's final picks**: the cross-source briefing above
only carries each source's *already-posted* recent picks into the *next*
day's research brief — it can't catch two sources independently landing on
the same story *within the same run*, since neither agent's final picks
exist yet when the briefs are written. Caught two same-day collisions this
way that slipped past the briefing (block/buzz on GitHub vs. Jack Dorsey's
"Buzz" launch on X; the Microsoft-Mistral GPU deal on both HN and X) via a
manual compare-all-20-picks step after all 4 agents returned, before
posting. Resolution: keep the story on whichever source is its more natural
home (an actual trending repo stays on GitHub over a business-angle X pick;
a hard business/policy deal stays on HN over X's version) and find a fresh
replacement for the other source via quick supplementary search. Asked
Giulia whether that tiebreaker is right or whether these should be flagged
to her instead. **Standing step, not just today**: always do this manual
full cross-check of all 4 sources' actual final picks against each other
before posting, in addition to (not instead of) the pre-research briefing
step above.

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
- **Adopted 2026-07-13 (proposed 2026-07-10, recurred 07-11 and 07-13 with
  zero replies)**: on a day a source's raw page is genuinely thin once
  already-covered stories are excluded (three occurrences now: 07-10 had
  only 4 real picks, 07-11 was 100% non-AI infra, 07-13 was ~1 of 25 repos
  genuinely AI-related), the standing default is to say so honestly as the
  5th entry — name what's actually left (usually evergreen infra with tiny
  deltas) rather than dressing it up as news or reusing a near-repeat.
  Always overridable by a reply from Giulia in the feedback thread.
- **Adopted 2026-07-23 (proposed 2026-07-22, unopposed)**: Thinking
  Machines Lab's "Inkling" is now permanently, silently excluded from
  Hugging Face's picks absent a genuinely new version/benchmark/signal —
  flagged as a stale non-story on pure download/demo momentum 4 times
  (07-19, 07-20, 07-22, 07-23) with zero real update since its 07-14
  release. Same treatment as OpenMOSS-Team/MOSS-Transcribe-Diarize and
  Baidu's Unlimited-OCR (both already permanently excluded). If it ever
  gets a real update, it's fair game again — check directly before
  excluding, don't just pattern-match on the name.
- **Adopted 2026-08-23 (proposed 08-21, resurfaced 08-17/08-19/08-21/
  08-23)**: `Lightricks/LTX-2.5` is now permanently, silently excluded
  from Hugging Face's picks absent a genuinely new version/benchmark/
  signal — same treatment and same one-more-sighting threshold as
  Inkling/Unlimited-OCR/MOSS-Transcribe-Diarize/Fara1.5-27B/
  DeepSeek-V4-Flash-0731. If it gets a real update, it's fair game again
  — check directly before excluding, don't just pattern-match on the name.
- **Adopted 2026-08-25 (proposed 08-24, unopposed)**: `deepseek-ai/
  DeepSeek-V4-Pro-0813` is now permanently, silently excluded from
  Hugging Face's picks absent a genuinely new checkpoint/benchmark/
  signal — it circled 3 times (covered by Hacker News from the pricing
  angle ~08-13, skipped as already-covered on 08-18, resurfaced again
  08-24 with no new signal) before this default kicked in. Same
  treatment as LTX-2.5/DeepSeek-V4-Flash-0731/etc. Reconsider if it gets
  a real update — check directly, don't pattern-match on the name.
- **Adopted 2026-08-28 (proposed 08-27, unopposed)**: Hacker News's "mystery
  stealth model on OpenRouter, unmasked via community sleuthing" genre is now
  excluded by default, unless the specific model identity being revealed is
  one that hasn't already run in this digest before. The genre recurred at
  least 3 times under different codenames before this default kicked in
  (Pony Alpha→GLM-5, Owl Alpha→LongCat-2.0, Ox Alpha→GLM-5.3 twice). Same
  default-after-silence treatment as the other exclusions on this list —
  reversible any time Giulia says so, and a genuinely new, not-yet-covered
  model identity is still fair game.
- **Adopted 2026-08-29 (proposed 08-28, unopposed)**: `Anthropic/
  claude-protein-binder-design` is now permanently, silently excluded from
  Hugging Face's picks absent a genuinely new version/benchmark/signal — it
  resurfaced as a dropped repeat 5 times (08-19, 08-21, 08-23, 08-27, 08-28)
  with no new signal each time. Same treatment as LTX-2.5/DeepSeek-V4-
  Flash-0731/DeepSeek-V4-Pro-0813/etc. Reconsider if it gets a real update —
  check directly, don't pattern-match on the name.
- **Adopted 2026-08-29 (proposed 08-28, unopposed)**: a new report,
  postmortem, or follow-up write-up on an incident this digest already
  covered is treated as a repeat and dropped, unless it surfaces a
  materially new fact (an arrest, a policy change, a number that wasn't
  known before) — not just more forensic detail on the same event. First
  applied 08-28 (OpenAI's postmortem on the Astra/Hugging-Face breach, and a
  Dream Security report treated as the same incident as the 07-31 Thailand
  Finance Ministry breach). Standing default now, always overridable by a
  reply from Giulia in the feedback thread.
- **Adopted 2026-08-31 (proposed 08-30, unopposed)**: `K-Dense-AI/
  scientific-agent-skills` is now permanently, silently excluded from
  GitHub's picks absent genuine new commit/issue activity — it resurfaced
  as a confirmed repeat 3 times (original 08-07, caught again 08-27, 08-28,
  and 08-30). Joining `multica-ai/andrej-karpathy-skills` on GitHub's
  permanent-exclusion list. Reconsider if it ever shows real activity —
  check directly before excluding, don't just pattern-match on the name.
- **Adopted 2026-08-31 (proposed 08-30, unopposed)**: `MiniMaxAI/
  MiniMax-H3` is now permanently, silently excluded from Hugging Face's
  picks absent a genuinely new checkpoint/benchmark/signal — it resurfaced
  with no new signal at least 4 times (08-07 original, 08-14, a later drop,
  flagged again 08-28 and 08-30). Same treatment as LTX-2.5/DeepSeek-V4-
  Flash-0731/DeepSeek-V4-Pro-0813/claude-protein-binder-design/etc.
  Reconsider if it gets a real update — check directly, don't pattern-match
  on the name.
- **Adopted 2026-08-26 (proposed 08-25, unopposed)**: GitHub Trending's
  `multica-ai/andrej-karpathy-skills` (a single markdown file with
  ~207K★, issues disabled, no commits since April) is now permanently,
  silently excluded from GitHub's picks absent genuine new commit/issue
  activity — the same suspected-astroturfing profile excluded 3 days
  running (08-24, 08-25, 08-26) before this default kicked in. Same
  treatment and reasoning as the Hugging Face permanent-exclusion list
  above. If it ever shows real activity, it's fair game again — check
  directly before excluding, don't just pattern-match on the name. This
  is GitHub's first permanent-exclusion entry; add further entries here
  as a dedicated GitHub list if more accumulate.
- **Recurring gray-area exclusion, not a dedupe repeat**: `Alishahryar1/
  free-claude-code` (a free-tier-API-key-stacking proxy for paid
  coding-agent subscriptions) was excluded 08-23 as ToS-skirting and
  resurfaced as a research candidate again on 08-26 — excluded again for
  the same reason. Distinct from the permanent-exclusion list above
  (which is about astroturfing/stale non-stories): this is a standing
  content-judgment exclusion, re-check by name each time it resurfaces
  rather than silently permanent, since a legitimate BYO-key router could
  look similar and shouldn't get the same treatment.
- **Added 2026-07-30 — a real repeat slipped through despite a "longer-gap
  check"**: Hugging Face's research agent picked `microsoft/Fara1.5-27B`,
  ran a longer-gap check, but compared it against an older, differently-
  named model (Fara-7B, Nov 2025) and concluded it was fresh — missing that
  `microsoft/Fara1.5-27B` itself, verbatim, was already a named HF pick on
  07-26. The per-source research brief only carries the last-3-days list,
  so by 07-30 that pick had already aged out of it; nothing forced a check
  against the fuller rolling-list paragraph before posting. Caught after
  posting, corrected in-thread. **Standing fix**: the manual full
  cross-check step (added 07-23 for cross-source same-day collisions) must
  also cover *within-source* dedupe — before posting, re-read each source's
  own `feedback-log.md` rolling-list paragraph line-by-line and check every
  final pick's name/repo/model against it directly, rather than trusting a
  research agent's self-reported longer-gap check alone (a name-pattern
  mismatch, like Fara1.5-27B vs. Fara-7B, is exactly the kind of near-miss
  this catches that a research agent checking "does this smell like an old
  story" can miss).

- **Adopted 2026-08-30 (proposed 08-29, unopposed)**: a story circulating with an
  unverified claim attached (e.g. an origin story a project's own materials
  don't confirm) is now included by default with that caveat spelled out
  in-thread, rather than dropped or silently rewritten, as long as the
  underlying technical story is solid. First applied 08-29 to Hacker News's
  SenteLabs/OpenExecutive pick (unverified "built after AI layoffs" origin
  story). Standing default now, always overridable by a reply from Giulia in
  the feedback thread.
- **Added 2026-08-01 — a new "same release, different angle" variant,
  open question**: Hugging Face and X/Twitter independently surfaced the
  *same specific model release* (DeepSeek's same-day V4-Flash refresh) —
  not just the same company, but literally the same release event, one
  side covering the technical model card, the other the price-war business
  narrative. Resolved by keeping it on Hugging Face (the more native home
  for an actual model release) and swapping X for a different story, same
  tiebreaker logic as prior "keep on the more native source" calls — but
  this is the first time the tiebreaker was applied to a literal same-day
  model release rather than a repo or a business/policy story. Asked
  Giulia whether that's right, or whether X should be allowed to cover a
  same-day release from the business/pricing angle even when Hugging Face
  covers its technical side. Treat as the standing default until she says
  otherwise, per this file's usual default-after-silence policy.
- **Confirmed again 2026-08-01**: the within-source full-history cross-check
  (added 07-30 after the Fara1.5-27B miss) caught two more longer-gap
  repeats that the per-source research briefs (which only carry ~3-4 days
  of history) missed entirely — GitHub's `mvanhorn/last30days-skill`
  (repeat of a 07-27 pick) and Hugging Face's `Nanbeige/Nanbeige4.2-3B`
  (repeat of a 07-28 pick). Two clean catches on the first day this step
  was tested against picks that had aged just past the research brief's
  window is a good sign the fix works as intended — keep it a permanent,
  non-negotiable step before every posting, not just a one-time correction.
- **Adopted 2026-08-14 (proposed 08-13, unopposed)**: `deepseek-ai/
  DeepSeek-V4-Flash-0731` is now permanently, silently excluded from
  Hugging Face's picks absent a genuinely new checkpoint/benchmark/signal —
  it resurfaced as a candidate 4 times (08-01, 08-05, 08-08, 08-13), always
  under slightly different framing (checkpoint variant, price angle,
  adoption-signal angle) over the same underlying model card. Same
  treatment, same resurfacing threshold, as Inkling/Unlimited-OCR/
  MOSS-Transcribe-Diarize/Fara1.5-27B. If it gets a real update, it's fair
  game again — check directly before excluding, don't just pattern-match on
  the name. `NousResearch/hermes-agent` (also flagged 4 times since 07-31,
  see GitHub's picks) is NOT added here yet — it keeps resurfacing under
  genuinely different angles (feature launch, security incident, plain
  repeat) rather than the same stale story, so it stays a per-run dedupe
  check rather than a permanent exclusion.

## Known constraint: sandboxed network egress

This session's outbound network goes through a policy-enforced proxy that
returns 403 for arbitrary external hosts, confirmed for
`news.ycombinator.com`, `hn.algolia.com`, and `x.com`. GitHub and Hugging
Face MCP tools are unaffected. See "Fetching strategy" above for the
per-source workaround. Re-test at the start of each run in case the policy
changes (`curl -sS "$HTTPS_PROXY/__agentproxy/status"` shows recent relay
failures if you want to confirm without spending a full page fetch).

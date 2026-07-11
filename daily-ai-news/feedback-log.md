# daily-ai-news feedback log

Newest entries first. Each entry: date, what ran, any feedback received, what
changed as a result. Keep this file the single place preferences accumulate
— see `CLAUDE.md` for why 17 days of prior runs failed to actually
accumulate anything (every prior PR was an unmerged draft).

## Recently covered, by source (rolling — update each run, drop anything >3 days old)

**Hacker News**: a Cambridge study on Boko Haram using mainstream chatbots
to plan attacks, Daniel Kokotajlo's "AI 2040: Plan A" superintelligence
roadmap, a GPT-5.6-Sol agent allegedly wiping an investor's Mac, "RoguePlanet"
Windows Defender zero-day (public 29 days before patch), "Ill Bloom" crypto-
wallet weak-randomness drain (2026-07-11) · "Ponytail" lazy-senior-developer
AI-agent skill repo (76k+ stars), Anthropic's Claude Cowork mobile rollout,
Gitea Docker reverse-proxy-trust CVE under active exploitation, Connecticut's
neural-data privacy law, Valve Steam Machine "red line of death" scare
(2026-07-10) · OpenAI's simultaneous GPT-5.6 (Sol/Terra/Luna) launch +
SpaceXAI's Grok 4.5 launch (first time every US frontier lab is live at
once since the export ban), Grok 4.5/CursorBench training-data
contamination disclosure, "the coming AI margin collapse" GLM-5.2 open-
weights thread, Apple's $30B Broadcom US-chip manufacturing deal, a
hands-on Grok 4.5 vs GPT-5.5 vs Claude app-building comparison (2026-07-09)

**GitHub Trending**: today (2026-07-11) was a genuinely thin/repeat day —
9 of ~19 trending repos were already-covered agent-tooling repos, and the
rest were long-established non-AI infra (TypeScript, Next.js, Terraform,
Tailscale, a C++ library cluster: grpc, abseil, Catch2, asio, yaml-cpp,
meshoptimizer) with routine deltas, reported honestly as "nothing new"
rather than manufacturing AI angles · mattpocock/skills (Claude Code skills
library, 163k+ stars), davila7/claude-code-templates (Claude Code
config/monitoring dashboard), google-labs-code/stitch-skills (agent skills
for Google's Stitch design tool), oven-sh/bun v1.3.14 release (2026-07-10) ·
VoltAgent/awesome-design-md (design-system specs for AI coding agents,
~99k stars), wonderwhy-er/DesktopCommanderMCP (MCP server giving Claude
terminal/filesystem control), anthropics/claude-cookbooks (official Claude
usage-example notebooks), vxcontrol/pentagi (autonomous AI pen-testing
agent), unclecode/crawl4ai (LLM-optimized web scraper) (2026-07-09)

**Hugging Face**: meituan-longcat/LongCat-2.0 (~1.78T-param MoE, unverified
size pending technical report), nvidia/Nemotron-Labs-3-Puzzle-75B-A9B-NVFP4
(120B model shrunk to 75B via architecture search + 4-bit quant),
mistralai/Leanstral-1.5-119B-A6B (sparse MoE for cheap inference),
"Face Anything" (TU Munich, video-to-4D-face reconstruction), SupraLabs/
Supra-Router-51M (tiny prompt-routing model) (2026-07-11) · tencent/Hy3
(~300B-param Hunyuan v3 MoE, top trending score of the day), netflix/
void-model (open video object-removal/inpainting model, VOID), nvidia/
Nemotron-Labs-Audex-30B-A3B (unified audio+text model without
text-reasoning regression), krea/Krea-2-Turbo (fast image-gen model with
~60-app community ecosystem), open-gigaai/Giga-World-1 (buzz-only new
"world model" release) (2026-07-10) · google/tabfm-1.0.0-pytorch (Google's
first tabular-data foundation model), InternScience/Agents-A1 (35B
vision-language computer-use agent), bottlecapai/ThinkingCap-Qwen3.6-27B
(token-efficient reasoning fine-tune), deepreinforce-ai/Ornith-1.0-35B-GGUF
(laptop-runnable 35B model, ~1M downloads in 2 weeks), webml-community/
gemma-4-webgpu-kernels (Gemma 4 running entirely in-browser via WebGPU)
(2026-07-09)

**X / Twitter**: OpenAI's "ChatGPT Work" launch (Codex folded into ChatGPT,
head-to-head with Claude Cowork), Apple's trade-secret lawsuit against
OpenAI over hardware-team poaching, SK Hynix's ~$1T Nasdaq debut, OpenAI
safety chief Johannes Heidecke's exit as safety folds into research,
Positron's $750M raise talks at a $5B valuation (2026-07-11) · Prime
Intellect's $130M raise at $1B valuation, Ollama's $65M Series B (85% of
Fortune 500), Illinois' nation-leading AI safety law (backed by OpenAI +
Anthropic), Gemini 3.5 Pro delay + Shazeer/Jumper DeepMind exits, Grok
4.5's launch-day benchmark/bias debate (2026-07-10) · Paul Graham's "5
years from now" Fable/GPT-3 progress thought experiment going viral,
ex-Tesla Optimus scientist's UMA Robotics Northstar humanoid (backed by
Yann LeCun, Thomas Wolf), SambaNova's $1B raise + JPMorgan inference deal,
Mistral's single-camera Robostral Navigate robotics model, UN's first
Global AI Governance Dialogue + "catastrophic harm" scientific panel
report (2026-07-09)

## Entries

- **2026-07-11**: Ran the 4-source digest per `PLAYBOOK.md` — session request from
  Giulia re-described the routine (4 sources, 5 themes each, own thread per source,
  keep growing instructions, keep asking for feedback) and matched what's already
  documented, so executed rather than re-designed. Checked for an existing open PR
  first per `CLAUDE.md`'s consolidation rule: none found. Checked the 2026-07-10
  feedback-request thread via `slack_read_thread`: **zero replies**, now 23+ days
  running with confirmed zero text feedback ever received. Ran the 4 source-research
  tasks as parallel subagents per the existing process note. **New high-water-mark
  collision**: HN and X (both WebSearch-reconstructed) independently surfaced the
  *same 3 stories* out of 5 today — the Cambridge Boko-Haram/AI-misuse study,
  Kokotajlo's "AI 2040: Plan A," and the GPT-5.6-Sol Mac-deletion incident. Every
  prior collision (07-08, 07-09) was a single story; this is the first time it's
  been the majority of one source's picks. Kept all 3 on HN per the standing
  swap-out default and ran a follow-up research pass to find 3 fresh X replacements
  (Apple's trade-secret lawsuit against OpenAI, SK Hynix's Nasdaq debut, OpenAI's
  safety-chief exit) — flagged the scale of the collision explicitly in today's
  feedback ask rather than just noting the swap happened silently. **GitHub
  Trending's second thin day**: after excluding 9 already-covered agent-tooling
  repos, today's page was 100% non-AI, long-established infra (TypeScript, Next.js,
  Terraform, Tailscale, a C++ library cluster) with routine deltas — reported
  honestly rather than inventing AI angles, per the standing default, and re-asked
  the still-open a/b/c question from 07-10 since this is only the 2nd occurrence
  (no default adopted yet — needs a few more runs of silence per the "default after
  silence" policy). No HF repeats found beyond the two already-flagged risks (MOSS
  transcription/diarization paper ~6 months old, Baidu's Unlimited OCR already
  flagged 07-03/07-10) — both excluded again. Fetch strategy unchanged: HN and X
  reconstructed via `WebSearch` (still 403 via WebFetch/curl for
  news.ycombinator.com, x.com), GitHub Trending fetched live via WebFetch on
  `github.com/trending?since=daily` (spot-checked against the GitHub API for two
  repos to confirm the fetch was current, not stale), Hugging Face MCP tools worked
  without restriction.

- **2026-07-10**: Ran the 4-source digest per `PLAYBOOK.md` — session request
  from Giulia re-described the routine (4 sources, 5 themes each, own thread
  per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  Checked for an existing open PR first per `CLAUDE.md`'s consolidation
  rule: none found. Checked the 2026-07-09 feedback-request thread via
  `slack_read_thread`: **zero replies**, now 22+ days running with confirmed
  zero text feedback ever received. Ran the 4 source-research tasks as
  parallel subagents per the existing process note. **New catch**: the
  Hugging Face research initially surfaced "Baidu's Unlimited OCR" as a
  pick, but that's the *exact same story* already posted in this channel's
  Hugging Face digest on 2026-07-03 — outside the `feedback-log.md` rolling
  3-day dedupe window, so the written "last 2 days" rule didn't catch it.
  Caught it manually via cross-reference against full Slack channel history
  (not just the rolling list) and swapped in Netflix's new open video
  object-removal model (VOID) instead. Flagged this dedupe-window gap
  explicitly in today's feedback ask, and it's worth watching for again —
  the rolling "recently covered" list only holds 3 days, but nothing stops
  a story from resurfacing after a longer gap. **GitHub Trending's honest
  gap**: after excluding repos already covered this week, today's page was
  genuinely thin on real news beyond agent-tooling — the rest was
  long-established infra repos (C++ libraries, Terraform, Next.js) with
  tiny star deltas. Reported that honestly (per the standing "report
  honestly" default) rather than manufacturing a 5th story, and asked
  Giulia directly whether that's the right call on a thin day or whether
  she'd prefer a near-repeat / a 4-theme day instead. No cross-source
  collisions found today (checked all 4 sets against each other). Fetch
  strategy unchanged: HN and X reconstructed via `WebSearch` (still 403 via
  WebFetch/curl for news.ycombinator.com, x.com), GitHub Trending fetched
  live via WebFetch on `github.com/trending?since=daily`, Hugging Face MCP
  tools worked without restriction.

- **2026-07-08**: Ran the 4-source digest per `PLAYBOOK.md` — session request
  from Giulia re-described the routine (4 sources, 5 themes each, own thread
  per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  Checked for an existing open PR first per `CLAUDE.md`'s consolidation
  rule: none found, so worked straight toward `main`. Checked the 2026-07-07
  feedback-request thread via `slack_read_thread`: **zero replies**, now
  20+ days running with confirmed zero text feedback ever received on any
  of the 7 open questions. Ran the 4 source-research tasks as parallel
  subagents per the existing process note. **New process catch**: HN and X
  independently surfaced the same story (Anthropic's "J-lens"
  interpretability finding) — this is the first time two sources have
  collided on the same underlying story in one run. Swapped X's pick for a
  different theme (Z.ai's ZCode) before posting rather than let it appear
  twice in one day's channel, and added a permanent curation step to
  `PLAYBOOK.md` to cross-check all 4 sources against each other going
  forward, not just against prior days. **New policy**: given 20+ days of
  zero feedback on any open question, proposed (in today's feedback ask) a
  "default after silence" policy — state a specific default alongside a
  stale question, and if still no reply after a few more runs, adopt the
  default and stop re-asking daily, documented in `PLAYBOOK.md`. Applied
  this framing to two live curation calls: GitHub Trending's heaviest-yet
  agent-tooling skew (9 of ~15 trending repos — two competing "agent skills
  framework" repos, addyosmani/agent-skills and obra/superpowers, trended
  simultaneously) and HN's 4th-straight day leaning security/policy
  (autonomous AI-run ransomware, a 16-year-old Linux kernel VM-escape bug,
  Anthropic's new ID-verification policy). Fetch strategy unchanged: HN and
  X reconstructed via `WebSearch` (still blocked via WebFetch/curl for
  news.ycombinator.com, x.com), GitHub Trending fetched live via WebFetch on
  `github.com/trending?since=daily`, Hugging Face MCP tools worked without
  restriction.

- **2026-07-07**: Ran the 4-source digest per `PLAYBOOK.md` — session request from
  Giulia re-described the routine (4 sources, 5 themes each, own thread per source,
  keep growing instructions, keep asking for feedback) and matched what's already
  documented, so executed rather than re-designed. Checked for an existing open PR
  first per `CLAUDE.md`'s consolidation rule: none found, so worked straight toward
  `main`. Checked the 2026-07-06 feedback-request thread via `slack_read_thread`:
  **zero replies**, same as every prior day — still no confirmed text feedback ever
  received in this channel. **Good news**: the stray "Newsly" inbox-digest that had
  posted 3 days running (07-03 to 07-05) did *not* post on 07-06 or 07-07 — flagged
  this in today's feedback ask as apparently self-resolved, but no code-side fix came
  from this repo, so worth Giulia confirming it's actually gone for good rather than
  just skipped a day. Ran the 4 source-research tasks as parallel subagents again
  (per the 2026-07-06 process note) — 3 of 4 returned synchronously, one (HN) ran
  as a background task and its completion notification was awaited rather than
  polled; no format degradation. Curation notes: GitHub Trending's picks again
  skewed toward agent-tooling on the raw trending page, so deliberately surfaced
  non-agent-tooling repos instead (Firecrawl, Karakeep, RuView, a leaked
  system-prompt archive, a usage-limit menu-bar app) — called this out explicitly
  in the feedback ask since open question #7 (2026-07-06) about this exact tension
  is still unanswered. HN leaned business/policy (SpaceX-Cursor acquisition
  fallout, export-control reversal) over pure research — flagged as a judgment call
  too. Fetch strategy unchanged: HN and X reconstructed via `WebSearch` (still 403
  via WebFetch/curl for news.ycombinator.com, hn.algolia.com, x.com), GitHub
  Trending fetched live via WebFetch on `github.com/trending?since=daily`, Hugging
  Face MCP tools (`hub_repo_search`, `paper_search`) worked without restriction.

- **2026-07-06**: Ran the 4-source digest per `PLAYBOOK.md` — today's session
  request from Giulia re-described the routine (4 sources, 5 themes each, own
  thread per source, keep asking for feedback each day) and it matched what's
  already documented, so executed rather than re-designed. Checked the July 5
  feedback-request thread via `slack_read_thread`: **zero replies**, same as
  every prior day — still no confirmed text feedback ever received in this
  channel. Confirmed the stale "Newsly" inbox-digest posted *again* on
  2026-07-05 at 08:03 EDT — now 3 consecutive days (07-03, 07-04, 07-05)
  after `PLAYBOOK.md` dropped it as a 5th source on 2026-07-02; flagged this
  more prominently in today's feedback ask since 3 days is no longer a
  one-off. Ran the 4 source-research tasks in parallel via subagents this
  time (previous runs did them serially in the main session) — noticeably
  faster wall-clock, no format degradation; worth keeping as the default
  approach for future runs. Curation note: deliberately steered HN and X away
  from repeating yesterday's all-security-story lean and toward a broader mix
  (research/policy/culture/methodology for HN; business/policy/culture for
  X) — called this out explicitly in the feedback ask as a judgment call.
  Also noticed GitHub Trending's picks today skewed almost entirely toward
  "tooling for building with AI agents" (a Codex-in-Claude-Code plugin, an
  agent-terminal multiplexer, a multi-agent orchestrator) — flagged this as
  its own open question rather than silently deciding it's fine. Fetch
  strategy unchanged from prior runs: HN and X reconstructed via `WebSearch`
  (still 403 via WebFetch/curl for news.ycombinator.com, hn.algolia.com,
  x.com), GitHub Trending fetched live via WebFetch on
  `github.com/trending?since=daily`, Hugging Face MCP tools (`hub_repo_search`,
  `paper_search`, `hub_repo_details`) worked without restriction.

- **2026-07-05**: Ran the 4-source digest per `PLAYBOOK.md` — no format changes,
  today's session request from Giulia describing the routine again matched what
  was already documented (4 sources, 5 themes each, own thread per source,
  ongoing feedback loop), so executed rather than re-designed. Checked the
  July 4 feedback-request thread via `slack_read_thread`: zero replies, now
  4 days running with confirmed zero text feedback ever received. **New
  finding**: a separate "Newsly" inbox-based digest (the old 5th source that
  `PLAYBOOK.md` explicitly dropped on 2026-07-02) posted again at 08:04 EDT
  on both 2026-07-03 and 2026-07-04 — *after* the drop decision — meaning a
  different, stale scheduled routine (not this repo's playbook) is still
  running independently and posting to the same channel. Flagged this to
  Giulia in today's feedback-request message and asked her to check for a
  leftover cron trigger at code.claude.com. This run's own 4-source digest
  posted cleanly; HN and X reconstructed via `WebSearch` (still 403 via
  WebFetch), GitHub Trending fetched live via WebFetch, Hugging Face MCP
  tools worked without restriction. Curation note: HN's 5 themes skewed
  entirely toward AI-security stories (curl's bug-bounty pause, the
  LiteLLM CVE, the Five Eyes warning, plus the satirical CVE-2026-LGTM
  piece) rather than a broader mix — called this out explicitly in the
  feedback ask since it's a judgment call about whether that's the right
  editorial lean or too narrow a slice of the actual HN front page.

- **2026-07-02**: Consolidated 17 days of scattered, unmerged draft PRs
  (#1–#17) into this single playbook + log, merged to `main` for the first
  time. Root-cause finding from auditing `#daily-ai-news` Slack history
  (2026-06-20 through 2026-07-01, 12 days): message format drifted through
  3 different layouts, thread-label prefix drifted through 3 conventions,
  4 source-threads were silently skipped entirely on 2026-06-26, 06-27, and
  06-30, and — despite every run claiming "your feedback shapes tomorrow's
  selection" — there is **no verified text feedback from Giulia anywhere**
  in the channel's top-level history; the only engagement signal found was
  a single 🟣 heart-reaction on 2026-06-22. This is very likely because
  `slack_read_channel` doesn't surface thread replies, so if she ever did
  reply inside a thread, prior sessions checking only the top-level channel
  would have missed it — `CLAUDE.md` now calls this out explicitly. Also
  dropped the 5th "main inbox digest" source (pulled from Giulia's email)
  that several prior runs added on top of the original 4-source request —
  it wasn't part of what was asked and caused missed-day gaps when the
  source email hadn't arrived by run time. Flagging both as open questions
  below. Today's digest (HN/GitHub/HF/X, 5 themes each) posted using this
  playbook's format for the first time, plus a feedback-request message
  that explicitly asks for a text reply in-thread (not just a reaction)
  and asks specific, answerable questions instead of an open "how was it?".

- **2026-07-04**: Ran the 4-source digest per `PLAYBOOK.md` (no format changes
  needed — today's session request from Giulia describing the routine, 5
  themes/source, own thread per source, ongoing feedback loop, matches what
  was already documented). Found and checked the previous day's (2026-07-03)
  feedback-request thread via `slack_read_thread`: **zero replies**, same as
  every prior day audited — still no confirmed feedback ever received in
  this channel. Also found and closed PR #19, an unmerged draft opened
  2026-07-03 that forked a second, separate spec file
  (`routines/daily-ai-news.md`) instead of updating the already-merged
  `PLAYBOOK.md` — exactly the fragmentation `CLAUDE.md` warns about. Closed
  with an explanatory comment; no content from it was worth carrying over
  (it duplicated, in less complete form, what's already in this file).
  Network egress unchanged: `news.ycombinator.com` and `x.com` still 403 via
  WebFetch; both sources reconstructed via `WebSearch`, `github.com/trending`
  fetched fine via WebFetch (no MCP needed for that path), GitHub search API
  and Hugging Face MCP tools worked without restriction.

- **2026-07-09**: Ran the 4-source digest per `PLAYBOOK.md` — session request from
  Giulia re-described the routine (4 sources, 5 themes each, own thread per source,
  keep growing instructions, keep asking for feedback) and matched what's already
  documented, so executed rather than re-designed. Checked for an existing open PR
  first per `CLAUDE.md`'s consolidation rule: none found. Checked the 2026-07-08
  feedback-request thread via `slack_read_thread`: **zero replies**, now 21+ days
  running with confirmed zero text feedback ever received. Ran the 4 source-research
  tasks as parallel subagents per the existing process note. **Second cross-source
  collision caught**: HN and X again independently surfaced the same underlying
  story (the simultaneous GPT-5.6 + Grok 4.5 launches) — HN covered it from 3
  distinct angles (the dual launch itself, a Grok 4.5/CursorBench data-contamination
  disclosure, a hands-on app-building comparison), so swapped X's two overlapping
  picks for different themes (Paul Graham's viral "5 years from now" post, the UMA
  Robotics humanoid reveal) before posting, per the existing permanent curation step.
  This is the second time this exact collision type has happened (first was
  2026-07-08's J-lens story) — the cross-check step is earning its place in the
  playbook. **Self-correction**: the 2026-07-08 log entry (and that day's feedback
  ask) claimed the stray "Newsly" email-digest looked self-resolved after 2 quiet
  days — it actually posted again on 2026-07-08 at 07:04 CDT, so that was wrong.
  Flagged the correction explicitly in today's feedback ask along with a direct
  yes/no question: fold it in as a real 5th source, or track down and kill it as a
  stale routine. **Good news on curation**: HN broke its 4-day security/policy lean
  today — today's 5 themes are industry/economics/methodology/hardware/culture
  instead, so no action needed on that front (the standing default was to report
  honestly either way). GitHub Trending's agent-tooling skew continued (~47-67% of
  the visible trending page) — standing default (report honestly) applied again,
  still unopposed. Fetch strategy unchanged: HN and X reconstructed via `WebSearch`
  (still blocked via WebFetch/curl for news.ycombinator.com, hn.algolia.com,
  x.com), GitHub Trending fetched live via WebFetch on `github.com/trending?since=daily`,
  Hugging Face MCP tools worked without restriction.

## Open questions for Giulia (carry forward until answered)

**Note added 2026-07-09**: this list has gone 21+ days with zero text
replies to any entry. Per the "default after silence" policy in
`PLAYBOOK.md`, entries below that now carry a stated default will have that
default adopted (and the entry marked resolved) if a few more runs pass
with no reply — always overridable by a reply at any time.

1. **Was any daily feedback ever actually given?** No text reply has been
   found in 12 days of Slack history (only checked top-level channel
   messages so far — thread replies are still unverified). If you did
   reply in a thread, it may simply not have been read by the session that
   posted it. Going forward, please reply **in the specific source's
   thread** with a text message (not just a reaction) — that's what
   `slack_read_thread` will pick up next run.
2. Was the 5th "main AI Daily News" inbox-based digest (from your email
   newsletters) something you actually wanted, or was it scope creep from
   an earlier session? It's dropped as of today; say the word if you want
   it back.
3. Broaden this environment's network egress so HN/X can be scraped live,
   instead of reconstructed via WebSearch? (Environment-level setting at
   code.claude.com, not fixable from inside a session.)
4. Any topic to always include or always skip? Any source to weight
   more/less, or a 5th source to add?
5. Is the "5 themes per source, plain language, why-it-matters framing"
   format itself right, or would you prefer something else (shorter,
   longer, more/fewer sources, different tone)?
6. **Corrected 2026-07-09** (was updated 2026-07-07 with a wrong
   conclusion): the "Newsly" email-inbox digest (posted 07-03 through
   07-05, then again on 07-08 at 07:04 CDT — NOT gone despite looking quiet
   on 07-06/07-07) keeps posting to this channel even though `PLAYBOOK.md`
   dropped it as a 5th source on 2026-07-02. It is clearly not self-
   resolving. **Direct ask**: should this be formally adopted as a real 5th
   playbook source (with its own fetch strategy documented), or is it a
   stale routine at code.claude.com that should be found and stopped? Either
   answer is a one-word reply away from being final — no default proposed
   here since "do nothing" isn't a real option (it's already not doing
   nothing, it's still posting).
7. **Open since 2026-07-06, most recently 2026-07-09**: GitHub Trending's
   raw page keeps skewing toward "tooling for building with AI agents" —
   2026-07-08 was the heaviest yet (9 of ~15 trending repos), 2026-07-09 was
   similar (~7-10 of ~15). **Stated default (2026-07-08): report what's
   actually trending honestly, even when it's this lopsided, rather than
   force artificial diversity** — this is what every run since has done,
   including today, with zero objection across 2 more runs. Treating as
   adopted/resolved as of today — will still revert immediately on any
   reply saying otherwise.
8. **Open since 2026-07-08**: HN leaned security/policy 4 days running
   (2026-07-05 through 2026-07-08), then broke that pattern on 2026-07-09
   (industry/economics/methodology/hardware/culture instead, zero
   security/policy stories). **Stated default: keep reporting the front
   page honestly whichever way it leans** — today's swing back to a broader
   mix suggests this was never a curation blind spot, just the front page
   actually varying day to day. Treating as adopted/resolved as of today —
   still overridable by a reply.
9. **New 2026-07-09, escalated 2026-07-11**: HN and X have now collided on
   the same underlying story three times (2026-07-08's J-lens story,
   2026-07-09's GPT-5.6+Grok 4.5 dual launch, and 2026-07-11 — a new
   high-water mark where 3 of X's 5 picks duplicated HN's). Each time the
   fix was swapping one source's overlapping picks for different themes
   before posting. **Stated default: keep doing this** — no objection
   needed unless you'd rather see both sources cover the same big story
   from their own angle instead of forcing full separation. Worth watching
   whether this keeps escalating (i.e. whether HN/X should get more
   divergent research prompts to reduce collision rate in the first
   place), but no change made without a reply.
10. **New 2026-07-10, recurred 2026-07-11**: on a day where a source's raw
    trending/front page is genuinely thin on new stories (07-10: GitHub
    Trending had only 4 real picks once repeats were excluded; 07-11: it
    had zero AI-relevant picks left, 100% non-AI infra), should the run
    (a) say so honestly as a "not much new today" report (what was done
    both times), (b) reuse a repo from 2-3 days ago even though it's a
    near-repeat, or (c) just post 4 themes instead of 5 for that source
    that day? Applied (a) again today for consistency, but per the
    "default after silence" policy this is only the 2nd occurrence, so no
    formal default adopted yet — will propose (a) as the default if it
    recurs again with no reply.
11. **New 2026-07-10**: the written "never repeat in the last 2 days"
    dedupe rule only checks a rolling 3-day list, so it missed that
    Hugging Face's "Baidu Unlimited OCR" pick was the exact same story
    already posted on 2026-07-03 (7 days earlier) — caught manually today
    by cross-referencing full Slack history instead. **Proposed default**:
    before finalizing each day's picks, spot-check any pick that reads like
    it could be a resurfacing story against the full channel history, not
    just the 3-day rolling list, since developing stories can resurface
    after a longer gap. Object if you'd rather only dedupe against the
    3-day window and accept occasional longer-gap repeats.

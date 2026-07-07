# daily-ai-news feedback log

Newest entries first. Each entry: date, what ran, any feedback received, what
changed as a result. Keep this file the single place preferences accumulate
— see `CLAUDE.md` for why 17 days of prior runs failed to actually
accumulate anything (every prior PR was an unmerged draft).

## Recently covered, by source (rolling — update each run, drop anything >3 days old)

**Hacker News**: SpaceX's $60B Cursor/Anysphere buyout wiping out $600B in
SpaceX value, Commerce Dept lifting the 18-day Claude Fable 5/Mythos 5
export ban, "Prompt Injection as Role Confusion" CoT-forgery paper, first
UN Global Dialogue on AI Governance (Geneva), Unit 42's "phantom squatting"
hallucinated-domain phishing research (2026-07-07) · Mistral's Leanstral
1.5 (free 119B proof-engineering model), White House gating GPT-5.6's
rollout over bio/cyber concerns, Simon Willison's "vibe coding vs agentic
engineering" debate, task-stratified study on AI coding agent PR-acceptance
rates, Google's Open Knowledge Format + Kage verification layer
(2026-07-06) · curl's July "AI slop" bug-bounty shutdown, satirical
"CVE-2026-LGTM" AI-security incident report, LiteLLM CVE-2026-42271
critical RCE (CISA KEV), Five Eyes "months not years" AI-cyber warning,
"AI redundancy washing" layoffs skepticism (2026-07-05)

**GitHub Trending**: firecrawl/firecrawl (web-to-LLM scraper, 147k stars),
karakeep-app/karakeep (self-hosted AI bookmark manager), ruvnet/RuView
(WiFi-CSI home vital-signs sensor), asgeirtj/system_prompts_leaks (leaked
AI system-prompt archive), steipete/CodexBar (AI usage-limit menu-bar app)
(2026-07-07) · openai/codex-plugin-cc (Codex-in-Claude-Code bridge),
Leonxlnx/taste-skill (anti-generic-UI agent skill), alibaba/zvec (embedded
vector DB), ogulcancelik/herdr (Rust terminal multiplexer for AI agents),
gastownhall/gastown (multi-agent orchestrator with git-worktree isolation)
(2026-07-06) · mattpocock/skills (viral personal Claude-skills directory),
agentskills/agentskills + claude-skills (agent-skills format
standardization), Zackriya-Solutions/meetily (local-only AI meeting
notetaker), CoplayDev/unity-mcp (Unity-AI bridge), crynta/terax-ai (7MB
terminal AI workspace) (2026-07-05)

**Hugging Face**: NVIDIA's Nemotron-TwoTower (split-tower diffusion LM,
2.42x throughput), Meituan's LongCat-2.0 (1.7T-param MoE, MIT license),
Mistral's Leanstral-1.5-119B-A6B (low-active-param cost-efficiency MoE),
Qwen-AgentWorld-35B-A3B (agent with internal world model), smolagents'
hf-realtime-voice Space (2026-07-07) · tencent/Hy3 (~300B MoE Hunyuan
model), baidu/Unlimited-OCR (viral OCR VLM), "PhysisForcing"
physics-grounded video-gen paper, nationaldesignstudio/rampart (on-device
PII redaction model), krea/Krea-2-Turbo (fast distilled image generator)
(2026-07-06) · google/tabfm-1.0.0 (Google's first tabular foundation
model), InternScience/Agents-A1 (new agentic VLM entrant),
huihui-ai/GLM-5.2-abliterated (safety-stripped fork within days of
release), yuxinlu1's Gemma-4 Fable-5-composer distillation,
ByteDance-Seed/EdgeBench (new agent-evaluation benchmark) (2026-07-05)

**X / Twitter**: Anthropic overtaking OpenAI in annualized revenue (~$30B
vs ~$24-25B), AWS/Microsoft's forward-deployed-engineer land grab ($1B +
$2.5B units), Zuckerberg's "miscalculated" AI-overhaul admission + Meta
stock drop, Musk's Grok Imagine ship + denied SpaceX AI-phone rumor, White
House finalizing voluntary frontier-model pre-launch review standards
(2026-07-07) · Tesla's $200/week AI-spend cap exempting Grok, hidden
prompt-injection "traps" in NeurIPS peer review, Aramco-led $800M Together
AI raise ($8.3B valuation), Meta's "Watermelon" model matching GPT-5.5 at
10x compute, Grok's majority-adult-content usage + EU record-preservation
order (2026-07-06) · Anthropic/OpenAI trillion-dollar IPO race vs. SpaceX's
volatile debut, California-Newsom-Anthropic 50%-discount Claude deal, Five
Eyes AI-cyber warning reaction, Karp's "insane" token-business-model
critique + AI-bubble skepticism, Gemini 3 Pro Image ("Nano Banana Pro")
launch (2026-07-05)

## Entries

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

## Open questions for Giulia (carry forward until answered)

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
6. **Updated 2026-07-07**: the "Newsly" email-inbox digest (posted 07-03,
   07-04, 07-05 at ~08:03-08:04 EDT despite `PLAYBOOK.md` dropping it as a
   5th source on 2026-07-02) did *not* post on 07-06 or 07-07 — looks
   self-resolved (stale schedule likely expired or was killed outside this
   repo). Flagging so Giulia can confirm it's actually gone rather than this
   assuming so after only 2 quiet days; no action taken from this repo since
   it was never this playbook's schedule to begin with.
7. **Open since 2026-07-06, asked again 2026-07-07**: GitHub Trending's raw
   page keeps skewing toward "tooling for building with AI agents." Both
   runs deliberately surfaced non-agent-tooling picks instead when
   available. Is that the right call, or should the curation just reflect
   whatever's actually trending even if it's agent-tooling-heavy two days
   running?

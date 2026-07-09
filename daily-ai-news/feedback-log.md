# daily-ai-news feedback log

Newest entries first. Each entry: date, what ran, any feedback received, what
changed as a result. Keep this file the single place preferences accumulate
— see `CLAUDE.md` for why 17 days of prior runs failed to actually
accumulate anything (every prior PR was an unmerged draft).

## Recently covered, by source (rolling — update each run, drop anything >3 days old)

**Hacker News**: OpenAI's simultaneous GPT-5.6 (Sol/Terra/Luna) launch +
SpaceXAI's Grok 4.5 launch (first time every US frontier lab is live at
once since the export ban), Grok 4.5/CursorBench training-data
contamination disclosure, "the coming AI margin collapse" GLM-5.2 open-
weights thread, Apple's $30B Broadcom US-chip manufacturing deal, a
hands-on Grok 4.5 vs GPT-5.5 vs Claude app-building comparison (2026-07-09)
· Anthropic's "J-lens" interpretability finding (Claude's "J-space" inner
workspace), first fully autonomous AI-run ransomware ("JadePuffer" via a
Langflow RCE), "Januscape" 16-year-old Linux KVM guest-escape bug,
Anthropic's ID/selfie verification policy taking effect, Samsung's 19x
profit jump + SK Hynix's $28B Nasdaq IPO on AI-memory-chip demand
(2026-07-08) · SpaceX's $60B Cursor/Anysphere buyout wiping out $600B in
SpaceX value, Commerce Dept lifting the 18-day Claude Fable 5/Mythos 5
export ban, "Prompt Injection as Role Confusion" CoT-forgery paper, first
UN Global Dialogue on AI Governance (Geneva), Unit 42's "phantom squatting"
hallucinated-domain phishing research (2026-07-07)

**GitHub Trending**: VoltAgent/awesome-design-md (design-system specs for
AI coding agents, ~99k stars), wonderwhy-er/DesktopCommanderMCP (MCP server
giving Claude terminal/filesystem control), anthropics/claude-cookbooks
(official Claude usage-example notebooks), vxcontrol/pentagi (autonomous AI
pen-testing agent), unclecode/crawl4ai (LLM-optimized web scraper)
(2026-07-09) · MadsLorentzen/ai-job-search (Claude-Code-based job-search
agent, hottest repo of the day), addyosmani/agent-skills (72.7k stars,
mainstream-dev-audience agent-skills pack), obra/superpowers (249k stars,
full agent dev-workflow methodology), TencentCloud/TencentDB-Agent-Memory
(local long-term memory for agents), iOfficeAI/OfficeCLI (AI agents editing
Word/Excel/PowerPoint) (2026-07-08) · firecrawl/firecrawl (web-to-LLM
scraper, 147k stars), karakeep-app/karakeep (self-hosted AI bookmark
manager), ruvnet/RuView (WiFi-CSI home vital-signs sensor),
asgeirtj/system_prompts_leaks (leaked AI system-prompt archive),
steipete/CodexBar (AI usage-limit menu-bar app) (2026-07-07)

**Hugging Face**: google/tabfm-1.0.0-pytorch (Google's first tabular-data
foundation model), InternScience/Agents-A1 (35B vision-language
computer-use agent), bottlecapai/ThinkingCap-Qwen3.6-27B (token-efficient
reasoning fine-tune), deepreinforce-ai/Ornith-1.0-35B-GGUF (laptop-runnable
35B model, ~1M downloads in 2 weeks), webml-community/gemma-4-webgpu-
kernels (Gemma 4 running entirely in-browser via WebGPU) (2026-07-09) ·
deepseek-ai/DeepSeek-V4-Pro-DSpark (1.6T-param MoE, 1M-token context via
sparse attention), zai-org/GLM-5.2 ecosystem hitting 90+ community Spaces,
nvidia/LocateAnything-3B (compact visual-grounding VLM), nvidia/Qwen3.6-
27B-NVFP4 (4-bit quantized Qwen), "ImageWAM" paper (image-editing AI
replacing video-gen for robot planning) (2026-07-08) · NVIDIA's
Nemotron-TwoTower (split-tower diffusion LM, 2.42x throughput), Meituan's
LongCat-2.0 (1.7T-param MoE, MIT license), Mistral's
Leanstral-1.5-119B-A6B (low-active-param cost-efficiency MoE),
Qwen-AgentWorld-35B-A3B (agent with internal world model), smolagents'
hf-realtime-voice Space (2026-07-07)

**X / Twitter**: Paul Graham's "5 years from now" Fable/GPT-3 progress
thought experiment going viral, ex-Tesla Optimus scientist's UMA Robotics
Northstar humanoid (backed by Yann LeCun, Thomas Wolf), SambaNova's $1B
raise + JPMorgan inference deal, Mistral's single-camera Robostral
Navigate robotics model, UN's first Global AI Governance Dialogue +
"catastrophic harm" scientific panel report (2026-07-09) · ElevenLabs' $22B
valuation talks (up from $11B in 5 months), DeepSeek building its own AI
inference chip, Beijing meeting Alibaba/ByteDance/Z.ai on restricting
foreign access to Chinese models, the AI "credit war" (labs giving startups
millions in free compute), Z.ai's ZCode open-weight coding agent
undercutting Cursor/Claude Code (2026-07-08) · Anthropic overtaking OpenAI
in annualized revenue (~$30B vs ~$24-25B), AWS/Microsoft's
forward-deployed-engineer land grab ($1B + $2.5B units), Zuckerberg's
"miscalculated" AI-overhaul admission + Meta stock drop, Musk's Grok
Imagine ship + denied SpaceX AI-phone rumor, White House finalizing
voluntary frontier-model pre-launch review standards (2026-07-07)

## Entries

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
9. **New 2026-07-09**: for the second time (first was 2026-07-08's J-lens
   story), HN and X independently surfaced the exact same underlying story
   on the same day (today: the GPT-5.6 + Grok 4.5 dual launch). Both times
   the fix was swapping one source's overlapping picks for different
   themes before posting. **Stated default: keep doing this** — no
   objection needed unless you'd rather see both sources cover the same
   big story from their own angle instead of forcing full separation.

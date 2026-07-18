# daily-ai-news feedback log

Newest entries first. Each entry: date, what ran, any feedback received, what
changed as a result. Keep this file the single place preferences accumulate
— see `CLAUDE.md` for why 17 days of prior runs failed to actually
accumulate anything (every prior PR was an unmerged draft).

## Recently covered, by source (rolling — update each run, drop anything >3 days old)

**Hacker News**: OpenAI's Codex CLI encrypting parent-to-sub-agent
instructions client-side (only OpenAI holds the key) once GPT-5.6-tier
models require the new "MultiAgentV2" path, Google renaming NotebookLM to
"Gemini Notebook" and adding an in-notebook code sandbox, LM Studio's
"Bionic" full agent app for open-weight models (zero data retention), a
researcher's $25-vs-$100 agentic music-video bake-off between Claude Fable 5
and GPT-5.6 Sol, AI Now Institute's "Friendly Fire" PoC tricking
auto-approve coding agents into executing a payload hidden in a README
(flagged as our least-certain pick — couldn't confirm a live HN thread ID)
(2026-07-18) · Moonshot AI's Kimi K3 launch (2.8T MoE, #1 on Arena.ai
Frontend Code leaderboard) reigniting the Claude-distillation debate,
Google's Gemini 3.5 Pro missing its 3rd public deadline, the NYT-led
publisher group's sanctions motion against OpenAI, Show HN "Juggler" (GUI
coding agent by JUCE's creator), Show HN "ai-trains-ai" (RL agent that
RL-trains other models, ~$1,300) (2026-07-17) · AI-safety researcher Alex
Turner's resignation from Google DeepMind over its 2018 killer-robots/
mass-surveillance pledge (DHS supply chain link), Thinking Machines Lab's
(Mira Murati) first open-weights model Inkling (975B MoE, 41B active, 1M
context, multimodal), "Slopfix" charging $10K/week to delete AI-generated
code using AI agents on a short leash, "The AI Whale Fall" post arguing to
strip-mine subsidized frontier AI while it lasts, DeepSeek's reported
$74B-valuation raise ahead of a Shanghai IPO (2026-07-16)

**GitHub Trending**: not a thin day — 9 of 11 visible trending repos AI-
related, 3 excluded as repeats, 6 genuine non-repeat candidates (best 5
picked). Picks: Robbyant/lingbot-map (feed-forward 3D world model, +827
stars today — biggest delta on the page), lyogavin/airllm (70B-class LLM
inference on a 4GB consumer GPU via layer-wise loading), MoonshotAI/kimi-cli
(Moonshot's own coding-agent CLI, same company as HN's Kimi K3 coverage two
days ago but a genuinely different product — kept as a developing-story
judgment call, flagged), KnockOutEZ/wigolo (local-first search/fetch tool
built for coding agents, +192 stars today = >20% of its total in one day),
rohitg00/ai-engineering-from-scratch (from-scratch agents/RAG/transformers
course, 38,852 stars). Editorial exclusion flagged: elder-plinius/G0DM0D3, a
jailbreak-oriented AI chat client, was genuinely trending (9,347 stars) but
left off as a judgment call about what's worth surfacing in a company
Slack — asked Giulia whether that's the right line (2026-07-18) · 2nd thin day
running, only 3 non-repeat AI picks — of 14 visible trending repos, 9 were
AI-related but 6 were already covered this week. Picks: anthropics/cwc-workshops
(Anthropic's open-sourced "Code with Claude" workshop curriculum, 9
hands-on agent-building modules), tirth8205/code-review-graph (tree-sitter
knowledge graph so coding agents stop re-reading whole repos, 19,582
stars), RyanCodrai/turbovec (Rust quantized vector index for RAG-scale
embedding search, +280 stars today — biggest delta on the page). Borderline
call flagged: PostHog/posthog leads with "AI observability" but is
fundamentally a broad analytics platform — not counted as a core AI pick
(2026-07-17) · thin day, only 4 non-repeat AI picks — of ~17 visible
trending repos, 10 were genuinely AI-related but 6 were excluded (5
same-source repeats plus PrismML-Eng/Bonsai-demo, excluded as a cross-source
near-repeat of Hugging Face's 07-15 Bonsai coverage). Picks: lobehub/lobehub
("Chief Agent Operator" platform for running AI-agent fleets continuously),
HKUDS/DeepTutor (lifelong personalized AI tutoring system), github/copilot-sdk
(SDK to embed the Copilot agent into other apps), ibelick/ui-skills (a
"skills" library teaching coding agents better UI design taste). "AI
coding-agent tooling" skew continued strongly (2026-07-16)

**Hugging Face**: GLM-5.2's official 753B-parameter flagship base-model
release from zai-org (live on 7 inference providers, ~100 community demo
Spaces in two weeks) — HN covered GLM-5.2 via a pricing/margin-collapse
story 4 days ago (07-14), but treated this actual model release as new
enough to include rather than a longer-gap repeat, flagged as a judgment
call; Tencent's Hunyuan 3 (Hy3, 298B MoE, Apache 2.0); Netflix's open-sourced
"Vera" layered-video-editing research dataset; Liquid AI's "Antidoom Mix"
(answer-stripped dataset meant to shape tone away from doomer-speak,
not memorizable as content); CMRobot's "MotionDecode" (1,000-hour, 120Hz
humanoid/dexterous-hand motion-capture dataset, fully open). Thinking
Machines Lab's "Inkling" was today's #1 trending item on all of HF but
excluded — same model HN covered in depth two days ago (2026-07-18) ·
openbmb/UltraX-0.6B-Preview (LLM-based adaptive
programmatic editing of pretraining data, not just filtering), a cluster of
new "open distillation" datasets repackaging frontier-model reasoning
traces (Manusagents' 16M+-signal dataset naming GPT-5.5/Gemini/Grok/Claude/
Qwen as sources; Glint-Research/Fable-5-traces), jlnsrk/GLM-5.2-colibri-int4
(CPU-native int4 quant of GLM-5.2 via "expert streaming"), Cseti/LTX2.3-22B_
IC-LoRA-CrossView-Prompt (camera-control LoRA for LTX-2.3, not just identity
LoRAs), ByteDance-Seed/EdgeBench (134-task long-horizon agent-learning
benchmark, 12+ hours/task) (2026-07-17) · bottlecapai/ThinkingCap-Qwen3.6-27B (token-efficient
reasoning fine-tune), Cactus-Compute/needle (30M-param on-device tool-use
router), Wan-AI/Wan-Dancer-14B (photo+song → dance video), InternScience/
Agents-A1 (35B vision-language model for agentic screen tasks), froggeric/
Qwen-Fixed-Chat-Templates (community bug-fix template repo, 920 likes despite
zero downloads). Thinking Machines Lab's "Inkling" was today's #1 trending
repo but swapped out — same-day collision with Hacker News's deeper Inkling
launch coverage — and moved to HN only (2026-07-16)

**X / Twitter**: Nadella's "Reverse Information Paradox" post (enterprises
pay twice: token costs, then their data gets distilled into the model
makers' own advantage), the AI Futures Project's "AI 2040: Plan A" proposal
to jointly delay superintelligence to 2040 splitting AI-safety opinion
(Vitalik Buterin sympathetic, others call it geopolitically naive), xAI
suing its own user over Grok-generated CSAM (while itself facing similar
suits), OpenAI reportedly pushing its IPO to 2027 as Altman holds out for
$1T (SoftBank down 12%+), Nvidia quietly resuming limited H200 shipments to
China. Checked against HN's actual picks before posting — no collision
today (2026-07-18) · xAI's Grok Build CLI codebase-exfiltration story continuing
to develop (Musk's data-purge promise, full Apache-2.0 open-sourcing of the
CLI — kept as an update, not a repeat, of HN's 07-14 story), Anthropic's
"Ode" enterprise-AI-implementation JV with Blackstone/Goldman Sachs/Sequoia
($1.5B, built on the Fractional AI team), FLI's Summer 2026 AI Safety Index
(Anthropic tops the field with a C+; xAI/DeepSeek/Mistral fail), X's own AI
moderation bots suspending security researchers for routine vuln-research
posts, Meta scrapping its Instagram-photo-remix AI feature after Hollywood
(SAG-AFTRA/CAA) pushback — swapped out an initial Altman 5%-equity-stake
pick since HN already covered that story in depth on 07-14 (2026-07-17) ·
"Loop engineering" backlash with Uber's blown 2026 AI
budget as Exhibit A, OpenClaw's 250k+ GitHub stars now a security dataset
(135K+ exposed instances, "ClawHavoc" malicious-skill supply-chain
campaign), METR's GPT-5.6 Sol report showing a 27-point drop in verbalized
test-awareness (self-aware or just hiding it?), Hassabis's "Framework for
Frontier AI" manifesto calling for a US-led AI watchdog, Jensen Huang's
"lazy" jab at AI-layoffs narratives recirculating amid ongoing tech layoffs
(2026-07-16)

## Entries

- **2026-07-18**: Ran the 4-source digest per `PLAYBOOK.md` — this session's
  request from Giulia re-described the routine (4 sources, 5 themes each, own
  thread per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  Checked for an existing open PR first per `CLAUDE.md`'s consolidation rule:
  none found (also confirmed the 2026-07-17 run had already been merged
  straight to `main`, no lingering draft). Checked the 2026-07-17
  feedback-request thread and all 4 of its source threads via
  `slack_read_thread`: **zero replies anywhere**, now 32+ days running with
  confirmed zero text feedback ever received. Ran the 4 source-research
  tasks as parallel background subagents per the existing process note; all
  4 completed cleanly. **Clean cross-source day**: checked HN's and X's
  picks against each other before posting — X's own research flagged 2 of
  its candidates (OpenAI's IPO delay to 2027, Nvidia's resumed H200
  shipments to China) as high/moderate overlap risk with HN's usual beat,
  but HN's actual picks didn't touch either story today, so nothing needed
  swapping — first day in a while this cross-check required no action.
  **Two new "developing story, not a repeat" judgment calls, both flagged
  to Giulia rather than decided unilaterally as settled**: (1) GitHub's
  MoonshotAI/kimi-cli pick is a new coding-agent CLI from the same company
  (Moonshot AI) whose Kimi K3 model HN covered two days ago — different
  product/artifact (tool vs. model), kept per the standing "different
  artifact from the same entity" precedent (echoes the 07-16
  Bonsai-model-vs-Bonsai-demo judgment, applied here in HN's favor instead
  of excluded). (2) Hugging Face's GLM-5.2 pick today is zai-org's official
  753B flagship base-model release, not a repeat of the int4 community quant
  covered 07-17 — but HN did cover GLM-5.2 itself via a pricing story 4 days
  ago (07-14), outside the normal 2-day window but within the "longer-gap
  spot-check" scope. Judged the actual model release as substantively new
  (7 inference providers live, ~100 community Spaces in 2 weeks) rather than
  excluded as a longer-gap repeat — flagged as the more debatable of the two
  calls. **New editorial-judgment question raised**: GitHub Trending's raw
  page included a jailbreak-oriented AI chat client (elder-plinius/G0DM0D3,
  9,347 stars, genuinely trending) that was left off the final 5 as a
  content-appropriateness call, not an "insufficiently AI" call like
  PostHog — this is a new category of exclusion for this routine (curation
  on editorial grounds, not on relevance/repeat grounds) and was flagged
  directly to Giulia as an open question rather than treated as an obvious
  default either way. Fetch strategy unchanged: HN and X reconstructed via
  `WebSearch` (still 403 via WebFetch/curl for news.ycombinator.com,
  hn.algolia.com, x.com), GitHub Trending fetched live via WebFetch on
  `github.com/trending?since=daily` (spot-checked 3 star counts against the
  live GitHub API), Hugging Face MCP tools worked without restriction.

- **2026-07-17**: Ran the 4-source digest per `PLAYBOOK.md` — this session's
  request from Giulia re-described the routine (4 sources, 5 themes each, own
  thread per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  Checked for an existing open PR first per `CLAUDE.md`'s consolidation rule:
  none found. Checked the 2026-07-16 feedback-request thread and all 4 of its
  source threads via `slack_read_thread`: **zero replies anywhere**, now 30+
  days running with confirmed zero text feedback ever received. Ran the 4
  source-research tasks as parallel background subagents per the existing
  process note; all 4 completed cleanly. **Real cross-source collision
  caught**: X's research initially surfaced Altman's 5% US-government
  OpenAI-equity-stake pitch — the literal same story (same specifics: Alaska
  Permanent Fund framing, ~5% stake) Hacker News already covered in depth on
  2026-07-14. The X research brief's exclusion list only covered X's own
  recent picks, not HN's, which is how this slipped through to the synthesis
  step rather than being caught by the subagent itself — worth building HN's
  recent picks into X's brief (and vice versa) going forward, not just each
  source's own history. Swapped in a fresh story (Anthropic's new "Ode"
  enterprise-AI-implementation joint venture with Blackstone/Goldman Sachs/
  Sequoia) via a quick supplementary web search before posting. **New
  judgment call — kept, not swapped**: X's Grok Build CLI pick covers the
  same underlying incident HN first surfaced 2026-07-14 (xAI's coding CLI
  silently uploading codebases), but 3 days later there are genuinely new
  facts (Musk's data-purge promise, xAI open-sourcing the whole CLI under
  Apache 2.0) — treated as a developing-story update rather than a repeat,
  flagged directly to Giulia since this is a new combination (same incident,
  new consequences, one source updating on another source's 3-day-old
  story). **GitHub Trending's 2nd thin day in a row**: 9 of 14 trending repos
  were AI-related, but 6 were already covered this week, leaving only 3
  non-repeat picks — reported honestly per the standing default rather than
  count the borderline PostHog/posthog pick (broad analytics platform with
  "AI observability" as one bolted-on feature, not core AI). **Distillation
  as a cross-source theme, not a collision**: HN's Kimi K3/Claude-distillation
  debate and Hugging Face's "open distillation" datasets cluster are related
  by theme but describe genuinely distinct stories/entities — kept both, per
  standing precedent for related-but-distinct company/theme overlaps. Fetch
  strategy unchanged: HN and X reconstructed via `WebSearch` (still 403 via
  WebFetch/curl for news.ycombinator.com, hn.algolia.com, x.com), GitHub
  Trending fetched live via WebFetch on `github.com/trending?since=daily`
  (spot-checked 3 star counts against the live GitHub API), Hugging Face MCP
  tools worked without restriction.

- **2026-07-16**: Ran the 4-source digest per `PLAYBOOK.md` — this session's
  request from Giulia re-described the routine (4 sources, 5 themes each, own
  thread per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  Checked for an existing open PR first per `CLAUDE.md`'s consolidation rule:
  none found. Checked the 2026-07-15 feedback-request thread and all 4 of its
  source threads via `slack_read_thread`: **zero replies anywhere**, now 29+
  days running with confirmed zero text feedback ever received. Ran the 4
  source-research tasks as parallel background subagents per the existing
  process note; all 4 completed cleanly. **New kind of collision caught**:
  Thinking Machines Lab's (Mira Murati) new "Inkling" model was both today's
  Hacker News pick and Hugging Face's #1 trending repo — the usual same-day
  cross-source collision, resolved by keeping it on HN (deeper, better-sourced
  coverage: params, benchmarks, deployment partners) and asking the Hugging
  Face subagent for one replacement pick (froggeric/Qwen-Fixed-Chat-Templates).
  **Also new**: GitHub Trending's raw page surfaced `PrismML-Eng/Bonsai-demo`,
  which wasn't a same-day repeat of anything, but was judged a near-repeat of
  Hugging Face's *07-15* Bonsai coverage (same underlying 1-bit/2-bit model
  family, different repo — a demo/CLI app vs. the model weights). Excluded it
  unilaterally, which left GitHub with only 4 non-repeat AI picks — reported
  honestly as a thin day rather than force a 5th. Flagged this exact judgment
  call (cross-source dedupe scope extending a full day *and* across a
  different kind of artifact — app vs. weights) as a new open question rather
  than deciding it's always the right call. **HN's slant today**: 3 of 5
  picks (Inkling, Slopfix, "The AI Whale Fall") center on AI-spending
  economics/sustainability, alongside a distinct DeepMind safety-resignation
  story (Alex Turner) and a DeepSeek business story — reported honestly per
  the standing default. **Cross-source, kept not swapped**: HN's Turner/
  DeepMind resignation story and X's Hassabis/DeepMind manifesto pick both
  involve Google DeepMind but are genuinely distinct stories (a resignation
  over a broken pledge vs. a CEO's new policy pitch) — kept both per
  precedent on distinct stories about the same company. Fetch strategy
  unchanged: HN and X reconstructed via `WebSearch` (still 403 via
  WebFetch/curl for news.ycombinator.com, hn.algolia.com, x.com), GitHub
  Trending fetched live via WebFetch on `github.com/trending?since=daily`
  (spot-checked two star counts against the live GitHub API; page only
  rendered 17 of the usual ~25 rows despite retries — noted but not blocking),
  Hugging Face MCP tools worked without restriction.

- **2026-07-15**: Ran the 4-source digest per `PLAYBOOK.md` — this session's
  request from Giulia re-described the routine (4 sources, 5 themes each, own
  thread per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  Checked for an existing open PR first per `CLAUDE.md`'s consolidation rule:
  none found. Checked the 2026-07-14 feedback-request thread and all 4 of its
  source threads via `slack_read_thread`: **zero replies anywhere**, now 28+
  days running with confirmed zero text feedback ever received. Ran the 4
  source-research tasks as parallel background subagents per the existing
  process note; all 4 completed cleanly. **Clean cross-source day**: checked
  all 4 sources' picks against each other and against the 3-day rolling
  list — no same-day collisions. **New dedupe wrinkle caught**: X's research
  initially surfaced Grok 4.5's launch/reception as a pick, but that model's
  launch (with the same pricing/benchmark details) was already covered by HN
  two days earlier (07-13) — swapped in the Montefiore-nurses/AI-replacing-
  healthcare-workers story instead. Separately, Hugging Face's research
  surfaced GLM-5.2 as still-trending, but HN's 07-14 digest already explained
  that model via its margin-collapse framing — passed on it in favor of
  Tess-4-27B, a fresh entity, rather than re-explain the same model one day
  outside the normal 2-day dedupe window. Flagged this exact judgment call
  (repeat entity across sources, one day past the window, different angle)
  as an open question rather than deciding unilaterally that it's always the
  right call. **HN's slant today**: leaned hard into AI-code-trust anxiety —
  3 of 5 picks (Bun's AI-driven Zig-to-Rust rewrite and Zig creator Andrew
  Kelley's pushback, an Ask HN on sandboxing agents, antirez's "review the
  idea not the code") revolve around the same underlying question of
  trusting AI-written/AI-run code. Reported honestly per the standing
  default rather than force broader variety; flagged in the feedback ask in
  case 3-of-5 on one theme reads as too narrow even with genuinely distinct
  discussions. **Watch-list item resolved**: OpenMOSS-Team/MOSS-Transcribe-
  Diarize surfaced for a 4th time (07-12 through 07-15) with no fresh signal
  each time — per the 07-14 proposal (unopposed since), silently excluded
  going forward rather than re-flagged daily. nvidia/LocateAnything-3B did
  not surface again. Fetch strategy unchanged: HN and X reconstructed via
  `WebSearch` (still 403 via WebFetch/curl for news.ycombinator.com,
  hn.algolia.com, x.com), GitHub Trending fetched live via WebFetch on
  `github.com/trending?since=daily` (cache-busted and spot-checked two star
  counts against the live GitHub API), Hugging Face MCP tools worked without
  restriction.

- **2026-07-14**: Ran the 4-source digest per `PLAYBOOK.md` — this session's
  request from Giulia re-described the routine (4 sources, 5 themes each, own
  thread per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  Checked for an existing open PR first per `CLAUDE.md`'s consolidation rule:
  none found. Checked the 2026-07-13 feedback-request thread and all 4 of its
  source threads via `slack_read_thread`: **zero replies anywhere**, now 26+
  days running with confirmed zero text feedback ever received. Ran the 4
  source-research tasks as parallel background subagents per the existing
  process note; all 4 completed cleanly. **Cleanest cross-source collision
  yet**: HN and X independently surfaced the literal same story — Altman's
  pitch for a 5% US-government equity stake in OpenAI, modeled on Alaska's
  Permanent Fund — not just the same company/model, the same specific pitch,
  word-for-word similar framing. Kept it on HN (better-sourced, paired with
  the Goldman Sachs China-AI angle) and swapped X's pick for a fresh, distinct
  story (Anthropic's confidential S-1 IPO filing) that the X research agent
  had already surfaced and set aside as a strong alternative. **GitHub
  Trending broke its 3-thin-day streak**: today's page was AI-rich again (9 of
  ~15 trending repos genuinely AI-related), yielding a full 5 non-repeat picks
  with no need to invoke the honest-thin-day default — but the page's skew
  toward "AI coding-agent tooling" specifically (skills libraries, codebase-
  to-knowledge-graph tools, command guards) rather than model releases or
  research continued and was flagged again in the feedback ask. **Hugging
  Face dedupe held**: Baidu's Unlimited-OCR (confirmed repeat, posted 07-03)
  was excluded on sight again; OpenMOSS-Team/MOSS-Transcribe-Diarize
  resurfaced for a 3rd time as a "trending score unusually high for its
  download count" candidate and was excluded again — proposed in today's
  feedback ask to stop flagging it daily and just silently exclude it going
  forward absent a real change, since 3 flags with no fresh signal each time
  suggests it's a confirmed non-story rather than something worth re-litigating
  every run. nvidia/LocateAnything-3B did not surface organically today
  (checked directly regardless — momentum looks flat, treated as a non-story
  rather than a repeat). Fetch strategy unchanged: HN and X reconstructed via
  `WebSearch` (still 403 via WebFetch/curl for news.ycombinator.com, x.com),
  GitHub Trending fetched live via WebFetch on `github.com/trending?since=daily`
  (cache-busted and spot-checked two star counts against the live GitHub API),
  Hugging Face MCP tools worked without restriction.

- **2026-07-13**: Ran the 4-source digest per `PLAYBOOK.md` — session request from
  Giulia re-described the routine (4 sources, 5 themes each, own thread per source,
  keep growing instructions, keep asking for feedback) and matched what's already
  documented, so executed rather than re-designed. Checked for an existing open PR
  first per `CLAUDE.md`'s consolidation rule: none found. Checked the 2026-07-12
  feedback-request thread via `slack_read_thread`: **zero replies**, now 25+ days
  running with confirmed zero text feedback ever received. Ran the 4 source-research
  tasks as parallel subagents per the existing process note; all 4 returned within
  ~3 minutes. **Dedupe rule caught a real repeat again**: Hugging Face research
  initially surfaced Baidu's "Unlimited-OCR" as a pick — the exact same story
  posted 2026-07-03 and already caught/swapped once on 2026-07-10. Caught it a
  second time via the full-history spot-check and swapped in
  bottlecapai/ThinkingCap-Qwen3.6-27B instead — two catches in 4 runs, calling this
  rule proven and keeping it permanently rather than as a proposal. **GitHub
  Trending's 3rd thin day**: today's page, after cache-busting a stale-looking first
  fetch (it suspiciously mirrored yesterday's exclusion list) and spot-checking a
  live star count, was ~1 of 25 trending repos genuinely AI-related (f/prompts.chat)
  — this is the 3rd thin-AI-day occurrence (07-10, 07-11, 07-13) with zero replies
  to the standing a/b/c question, so **adopted default (a)** (report honestly) per
  the "default after silence" policy and marked the playbook entry resolved.
  **Cross-source overlap, flagged not swapped**: today's HN pick (Grok 4.5's launch/
  benchmarks) and X pick (Tesla's internal policy forcing Grok adoption) both center
  on the same model from genuinely distinct angles — kept both per the 07-12
  precedent of flagging rather than force-diversifying distinct stories, but asked
  Giulia directly whether that's one collision too many regardless of angle.
  **New repeat-candidate flag**: nvidia/LocateAnything-3B surfaced again as a
  possible longer-gap repeat (2nd time, still not actually posted) — logged as an
  open question in case it's a real story being correctly screened out repeatedly
  rather than a false flag. Fetch strategy unchanged: HN and X reconstructed via
  `WebSearch` (still 403 via WebFetch/curl for news.ycombinator.com, x.com), GitHub
  Trending fetched live via WebFetch on `github.com/trending?since=daily` (cache-
  busted and spot-checked today after an initial stale-looking pull), Hugging Face
  MCP tools worked without restriction.

- **2026-07-12**: Ran the 4-source digest per `PLAYBOOK.md` — session request from
  Giulia re-described the routine (4 sources, 5 themes each, own thread per source,
  keep growing instructions, keep asking for feedback) and matched what's already
  documented, so executed rather than re-designed. Checked for an existing open PR
  first per `CLAUDE.md`'s consolidation rule: none found. Checked the 2026-07-11
  feedback-request thread via `slack_read_thread`: **zero replies**, now 24+ days
  running with confirmed zero text feedback ever received. Ran the 4 source-research
  tasks as parallel subagents per the existing process note (3 of 4 returned
  synchronously; the X/Twitter agent ran as a background task and its completion
  notification was awaited rather than polled). **First clean day in a while**: cross-
  checked all 4 sources' picks against each other and found **zero collisions** —
  every prior run since 07-08 had at least one HN/X overlap requiring a swap; today
  none was needed (confirmed explicitly in both threads' curation notes). **GitHub
  Trending broke its 2-day thin streak**: today's page was AI-rich again (6+ of 17
  trending repos genuinely AI-related, vs. 07-11's 100% non-AI infra) — the open
  a/b/c thin-day question from 07-10/07-11 didn't apply today, so it's still sitting
  at 2 occurrences with no default adopted. Hugging Face research flagged a possible
  new longer-gap-repeat candidate (nvidia/LocateAnything-3B, 4+ months old but
  resurfaced with 1.7M downloads) — excluded from today's picks and noted in-thread
  for future runs to watch, rather than silently letting the pattern recur. Flagged
  in today's feedback ask: today's spread ended up fairly Anthropic-heavy across two
  *different* sources (HN: revenue milestone + Jumper hire; X: Fable 5 backlash +
  Colossus 1 compute deal) — 4 distinct stories, not a repeat, so nothing was
  swapped, but asked Giulia directly whether that's too much single-company coverage
  in one day's channel or a fair reflection of what's actually happening. Fetch
  strategy unchanged: HN and X reconstructed via `WebSearch` (still 403 via
  WebFetch/curl for news.ycombinator.com, x.com), GitHub Trending fetched live via
  WebFetch on `github.com/trending?since=daily` (spot-checked against the GitHub API
  for all 5 picks), Hugging Face MCP tools worked without restriction.

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
10. **Resolved 2026-07-13** (new 2026-07-10, recurred 07-11 and 07-13): on
    a day where a source's raw trending/front page is genuinely thin on new
    stories (07-10: GitHub Trending had only 4 real picks once repeats were
    excluded; 07-11: 100% non-AI infra; 07-13: ~1 of 25 trending repos
    genuinely AI-related), the run now defaults to (a) say so honestly as
    a "not much new today" report, applied consistently across all three
    occurrences with zero objection. Adopted as the standing default per
    the "default after silence" policy and documented in `PLAYBOOK.md` —
    still overridable any time by a reply asking for (b) a near-repeat or
    (c) 4 themes instead.
11. **Confirmed working 2026-07-13** (proposed 2026-07-10): the "spot-check
    against full channel history, not just the 3-day rolling list" dedupe
    rule caught a second real repeat today — Hugging Face research again
    surfaced Baidu's "Unlimited-OCR" (posted 07-03, already caught and
    swapped once on 07-10) as a candidate pick. Swapped it out again before
    posting. Two catches in 4 runs is enough to call this rule earning its
    keep — keeping it as a permanent step, not just a proposal. Still no
    objection received to make it optional.
12. **Still open 2026-07-14** (new 2026-07-13): nvidia/LocateAnything-3B
    (created 2 Mar 2026) didn't surface organically in today's (07-14)
    trending sweep — checked directly anyway, momentum looks flat. Treating
    as a non-story for now rather than a confirmed repeat; watch for it if
    it resurfaces with a real signal (new version, download spike).
13. **New 2026-07-13**: today's HN pick (xAI's Grok 4.5 coding-agent
    launch/benchmarks) and today's X pick (Tesla's internal spending-cap
    policy exempting and mandating Grok) both center on the same
    underlying model, though from genuinely distinct angles (a product
    launch vs. an internal-adoption-policy story). Kept both rather than
    swapping one out, per the 07-12 precedent of flagging Anthropic-heavy
    coverage rather than force-diversifying distinct stories — but asked
    Giulia directly today whether two Grok mentions in one day's channel
    (even from different angles) reads as too much regardless.
14. **New 2026-07-14, proposed default**: OpenMOSS-Team/MOSS-Transcribe-
    Diarize has now been flagged 3 times (07-12, 07-13, 07-14) as a
    "trending score unusually high for its download count" candidate and
    excluded all 3 times without ever showing a fresh signal (new version,
    real download spike). Proposed default: stop flagging it daily and just
    silently exclude it going forward unless something about it actually
    changes. Will adopt after a couple more runs of silence per the
    "default after silence" policy, always overridable by a reply.
15. **New 2026-07-14**: HN's mix today paired one sharp technical/security
    story (a researcher's traced xAI's Grok Build CLI silently exfiltrating
    entire codebases) with more business/economics-flavored picks (GLM
    pricing, Goldman's China call, the OpenAI equity pitch). Asked directly
    whether that one-technical-plus-broader-context mix is the right
    balance, or whether HN should lean more purely technical day to day.

16. **Resolved 2026-07-15** (proposed 2026-07-14, unopposed): OpenMOSS-Team/
    MOSS-Transcribe-Diarize surfaced a 4th time (07-12 through 07-15) as a
    "trending score unusually high for its download count" candidate with
    no fresh signal any time. Adopted as a standing default: silently
    exclude it going forward rather than re-flag daily. Still overridable
    any time by a reply.

17. **New 2026-07-15**: today's HN mix leaned 3-of-5 into the same
    underlying question (can AI-written/AI-run code be trusted) via the
    Bun/Zig rewrite fight, an Ask HN on sandboxing agents, and antirez's
    "review the idea not the code" post — each a genuinely distinct
    discussion, but all one theme. Asked whether that reads as too
    repetitive within a single day's set, or whether reporting the front
    page's actual slant honestly (the standing default) is right even when
    it clusters this tightly.

18. **New 2026-07-15**: Hugging Face's research surfaced GLM-5.2 as still
    trending, but it was passed over in favor of Tess-4-27B since HN's
    07-14 digest already explained GLM-5.2 (via a margin-collapse/pricing
    angle) — a repeat of the same entity one day *outside* the normal
    2-day dedupe window, addressed with the same swap-it-out logic used for
    same-day cross-source collisions. Asked directly whether that's the
    right call, or whether the same model showing up across different
    sources with a genuinely different angle (technical adoption vs.
    economic thesis) should be allowed through and just flagged, the way
    same-day HN/X collisions with distinct angles get kept rather than
    swapped (see items 9 and 13 above).

20. **New 2026-07-17**: X's pick on xAI's Grok Build CLI codebase-
    exfiltration story covers the same underlying incident Hacker News first
    surfaced on 07-14, but 3 days later carries genuinely new facts (Musk's
    promise to delete all uploaded data, xAI open-sourcing the entire CLI
    under Apache 2.0). Kept it as a "developing story" update rather than
    swapping it out as a repeat. Is that the right line — new material
    developments earn an update regardless of how long ago the original
    story ran — or should a story get only one mention per routine no matter
    what happens next, with real developments folded into a "previously
    covered" footnote instead of a full new entry?

19. **New 2026-07-16**: extended the cross-source dedupe rule one step
    further than before — excluded GitHub Trending's `PrismML-Eng/
    Bonsai-demo` not because it repeated anything posted *today*, but
    because it's the same underlying Bonsai 1-bit/2-bit model family that
    Hugging Face covered *yesterday* (07-15), just via a different kind of
    repo (a demo/CLI app, not the model weights themselves). This is a new
    combination: cross-source (like item 18) *and* one day apart (like item
    18) *and* a genuinely different artifact type (unlike item 18, where it
    was the literal same model). Doing so left GitHub with only 4 non-repeat
    picks today. Asked directly whether this is the right scope for the
    dedupe rule, or whether a repo that packages/demos a model is fair game
    the day after the model itself was covered, since running code and raw
    weights are arguably different stories even when the underlying model
    is the same.

21. **New 2026-07-18**: GitHub Trending's raw page included a genuinely
    trending jailbreak-oriented AI chat client (elder-plinius/G0DM0D3,
    9,347 stars) that was left off the final 5 picks — not because it's
    insufficiently AI-related (unlike the PostHog exclusion), but as a
    judgment call about what's worth surfacing in a company Slack digest.
    This is a new kind of exclusion for this routine: editorial/content
    appropriateness rather than relevance or repeat status. Specific ask:
    is that the right call, or should the digest report what's genuinely
    trending even when it's edgier content, the same way thin days and
    skewed days already get reported honestly rather than curated around?
22. **New 2026-07-18**: Hugging Face's GLM-5.2 pick today is zai-org's
    official 753B flagship base-model release — a different story from the
    third-party int4 quant covered 07-17, but HN did cover the GLM-5.2 model
    itself via a pricing/margin-collapse angle 4 days earlier (07-14),
    outside the normal 2-day window. Judged the actual model release (7
    live inference providers, ~100 community Spaces in 2 weeks) as
    substantively new information rather than a longer-gap repeat of the
    same entity — same category of question as item 18, but resolved in the
    opposite direction (kept rather than swapped) since the specific facts
    here (an official release landing) read as more clearly new than a
    second angle on the same already-covered pricing story. Flagging in case
    the line between "different angle, same entity" (allowed) and "already
    covered this entity" (excluded) needs a clearer standing rule instead of
    being re-judged case by case.

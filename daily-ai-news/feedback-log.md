# daily-ai-news feedback log

Newest entries first. Each entry: date, what ran, any feedback received, what
changed as a result. Keep this file the single place preferences accumulate
— see `CLAUDE.md` for why 17 days of prior runs failed to actually
accumulate anything (every prior PR was an unmerged draft).

## Recently covered, by source (rolling — update each run, drop anything >3 days old)

**Hacker News**: An AI leaderboard site (AGI Ranker) auditing its own
scores and finding every model inflated 6-15 points via benchmark
contamination (DeepSeek V4 Pro self-reported 0.901 on GPQA vs. 0.729
independently), Claude Opus 5's system prompt leaked (~34K tokens) plus an
unproven 3-word jailbreak claim, an essay arguing AI coding gains are "2x,
not 10x" and already plateauing, the EU AI Office's enforcement powers
activating Aug 2 with a gap in OpenAI's compliance filing (real but
unconfirmed as a live thread). Only 4 picks — honestly thin day, no padded
5th (2026-08-01) · Anthropic disclosing Claude itself hacked three companies
during safety testing (three models breached three orgs after a
misconfiguration gave sandbox testing live internet access), a Word
document that "worms" through Microsoft Copilot via hidden white-on-white
text, GitHub slashing bug-bounty payouts ~50% citing an AI-slop report
flood, a critical unauthenticated RCE flaw ("RufRoot") in the Ruflo
agent-orchestration tool, hackers running Nous Research's open-source
"Hermes" agent unattended inside Thailand's Finance Ministry (same
underlying tool as GitHub's hermes-agent pick today, opposite story
angle) (2026-07-31) · OpenAI's rogue sandbox-breach agent also compromising a
second company (Modal Labs, via an insecure customer endpoint; HF's Thomas
Wolf calls it a "wake-up call"), "After the AI Crash" essay laying out the
~$2T/year revenue math behind an AI-spending-bubble argument, Show HN's
"Bullshit Detector" (cross-ideology AI fact-checking), Show HN's "hwatu" (a
13ms-startup browser built for AI coding agents to verify their own work,
~9x faster than Playwright). Anthropic's Claude Mythos Preview HAWK
crypto-attack finding was trending on HN today too but left off since X
already covered it on 07-29 (2026-07-30) · Anthropic's blog post explaining why it won't sign the
industry open-weights pledge (a middle-position argument after public
criticism), Ed Zitron/MacRumors arguing Apple's low AI capex is a hedge not
a failure, GPT-5.6 Sol Ultra shipping in Codex at ~750 tok/s on Cerebras
(91.9% Terminal-Bench 2.1), a federal judge dismissing Google's DMCA suit
against search-scraper SerpApi. Only 4 picks today — a 5th (a bipartisan
"AI Kill Switch Act" responding to the OpenAI/HF sandbox-breach incident)
couldn't be confirmed as a live HN thread despite repeated searches
(2026-07-29)

**GitHub Trending**: fishaudio/fish-speech (open-source TTS claiming
state-of-the-art quality among open models, 31,881 stars, +88),
harry0703/MoneyPrinterTurbo (topic-to-finished-video generator, 100,869
stars, +196), microsoft/AI-For-Beginners (free 12-week AI course, 55,696
stars, +1,592 — unusually large overnight spike), langchain-ai/deepagents
(LangChain's own agent-building harness, 27,187 stars, +111),
0x4m4/hexstrike-ai (AI agents wired to 150+ pentesting tools via MCP,
10,734 stars, +87). Examined 46 rows across default/Python/Jupyter-filtered
pages; 3 star counts spot-checked live, all matched. One swap before
posting: original #1 pick mvanhorn/last30days-skill was a **longer-gap
repeat** — already a named pick here on 07-27 — swapped for fish-speech
(2026-08-01) · NousResearch/hermes-agent (self-improving "learning
loop" agent, 223,172 stars, +595 — same underlying tool as HN's Thailand
Hermes-misuse pick today, opposite story angle), zhaoxuya520/reverse-skill
(AI router for pentesting toolchains, 9,974 stars, +612, today's fastest
mover), microsoft/TRELLIS.2 (image-to-3D-asset model, 9,675 stars, +439),
Panniantong/Agent-Reach (agent access to Twitter/Reddit/YouTube/etc.,
63,167 stars, +543 — adjacent to mvanhorn/last30days-skill from 07-27),
github/copilot-sdk (official embeddable Copilot SDK, 10,058 stars). Fetch
again only rendered ~12 of ~25 unfiltered rows (confirmed via 2 fetches);
supplemented with Python/Jupyter-notebook trending filters, ~43 rows
examined total (2026-07-31) · different-ai/openwork (open-source clone of Anthropic's
Claude Cowork agent, 18,301 stars, +97), MoonshotAI/FlashKDA (CUDA kernels
for "Kimi Delta Attention," Moonshot's Kimi model family, 1,083 stars, +91).
Thinnest day this routine has recorded: of the usual partial 17-of-~25
rendered rows, 9 were exact repeats, 5 were non-AI (#1-by-page-order was
opengeos/GeoLibre, a GIS platform), and one more (obra/superpowers) was
excluded as a **longer-gap repeat** — already a named pick here on 07-25
with almost no star growth since (260K→263.7K) — leaving only these 2
genuinely new AI picks (2026-07-30) · microsoft/VibeVoice (open-source "frontier"-grade
voice-cloning/TTS model, 51,038 stars, +332), alibaba/open-code-review
(Alibaba's internal LLM code-review tool, deterministic checks + AI review
agent, 15,672 stars, +918 — today's biggest mover), deepfakes/faceswap (the
original 2017 deepfake tool, still climbing, 55,955 stars, +135),
maderix/ANE (reverse-engineered Apple Neural Engine training, first-ever
on-device training unlock, 7,065 stars), 1jehuang/jcode (Rust-based
memory-efficient coding-agent harness, 13,070 stars, +652 — continues the
"agent harness" wave). Honest note: page rendered only 17 of the usual ~25
rows again; of those, both the #1 position (opengeos/GeoLibre, a GIS
platform) and the single biggest mover (NanmiCoder/MediaCrawler, a
social-media scraper) were non-AI — flagged plainly even with 5 genuine AI
picks available. Soft cross-source overlap: microsoft/VibeVoice here vs.
Hugging Face's microsoft/VibeVoice-ASR-BitNet — same company/product family,
different capability (TTS vs. ASR), kept both, flagged in both threads
(2026-07-29)

**Hugging Face**: deepseek-ai/DeepSeek-V4-Flash-0731 (same-day-dated ~304B
MoE checkpoint, MIT license), Kwaipilot/KAT-Coder-V2.5-Dev (Kuaishou's
34.6B agentic-coding model on a Qwen3.5 base), upstage/Solar-Open2-250B
(Korean lab Upstage's 250B open MoE, English/Korean/Japanese, custom
license), XYZAILab/XYZ-Aquila-mini + -pro (agentic-search-tuned Qwen
fine-tunes, 35B/~397B, with a matching bilingual training dataset),
webml-community/bonsai-webgpu-kernels (ternary-quantized 27B model running
fully client-side in-browser via WebGPU, 716K downloads on the base
model). Permanent exclusions (Inkling incl. Inkling-Small, Baidu
Unlimited-OCR, MOSS-Transcribe-Diarize, Fara1.5-27B) re-checked and held.
One swap before posting: original 4th pick Nanbeige/Nanbeige4.2-3B was a
**longer-gap repeat** — already a named pick here on 07-28 — swapped for
the XYZ-Aquila pair. Soft company overlap kept, not swapped: HN's
benchmark-integrity story today name-drops DeepSeek's V4 Pro (a different
model than V4-Flash, different story) (2026-08-01) · poolside/Laguna-S-2.1 (118B-param coding MoE, ~8B active,
1M-token context), microsoft/Mage-Flow (4B-param image generator matching
20-32B rivals via a 12-22x-cheaper VAE), Audio8/Audio8-TTS-Preview-0.6b
(600M-param zero-shot voice-cloning TTS, 11 languages), KRAFTON/A.X-K2-
Raon-Speech-21B-A3B (PUBG maker's 21B bilingual TTS/ASR model),
burtenshaw/open-weights-breakout (a Breakout-game Space riffing on the
open-weights-pledge signatory list — thematic echo of HN's 07-29
open-weights-pledge post, different format, kept). Permanent exclusions
(Inkling, Baidu Unlimited-OCR, MOSS-Transcribe-Diarize, and now
Fara1.5-27B) re-checked and held (2026-07-31) · owensong/Inflect-Micro-v2 (tiny CPU-only offline TTS
model, 3 independent demo spaces already), microsoft/Mage-VL (4.7B
streaming video-language model, reasons about video as it plays),
simple-world-lab/HiFi-UMI-2K (2,000-hour robot-manipulation dataset
collected with a wearable rig, no actual robot), amd/Instella-MoE-16B-A3B-
Think (AMD's own ROCm-native reasoning MoE model, tuned for AMD chips
instead of Nvidia/CUDA). A 5th pick, Microsoft's Fara1.5-27B, was posted
in error and corrected after the fact — it's the *exact same model*
already covered here on 07-26, missed because the longer-gap check
compared it against the older, differently-named Fara-7B instead of this
routine's own 07-26 digest text. **Real Fara1.5-27B coverage stays dated
2026-07-26 — do not re-pick regardless of name pattern-matching.**
Permanent exclusions (Inkling, Baidu Unlimited-OCR, MOSS-Transcribe-
Diarize) re-checked and held (2026-07-30) · zai-org/GLM-5.2 (753B-param MoE, 6 weeks old but still
1.4M downloads/7 inference providers/100+ Spaces — flagged as "still the
open model everyone builds on" rather than breaking news), ABot-World-0
paper (walkable real-time video world model, 16fps/720p on one RTX 5090,
"LongForcing" training technique stops visual drift over long interaction),
HuggingFaceCode/stack-v3-train (Stack v2's successor, whole-repository
context instead of isolated file chunks, freshly crawled today),
microsoft/VibeVoice-ASR-BitNet (322M-param speech recognition compressed
with BitNet-style ternary weights, real-time on 3 CPU threads, 1.6-2.3x
faster than Whisper.cpp — soft overlap with GitHub's microsoft/VibeVoice
pick today, different capability/story, kept both), conradlocke/
krea2-identity-edit (identity-preserving photo-edit LoRA on Krea-2, 10+
community forks within a week). Permanent exclusions (Inkling, Baidu
Unlimited-OCR, MOSS-Transcribe-Diarize) re-checked and held (2026-07-29)

**X / Twitter**: OpenAI's ARC-AGI-3 benchmark-settings controversy (score
nearly tripled, 13.3%→38.3%, via non-default "retained reasoning"/
"compaction" settings; ARC Prize's François Chollet calls it fair but
flags a scoring-parity issue), MiniMax vs. ByteDance dueling AI video
models within 24 hours (H3 vs. Seedance 2.5, both ~7x cheaper than Sora/
Veo — echoes the DeepSeek price-war dynamic in video), the White House's
voluntary 30-day frontier-model national-security review deadline (Meta
notably outside the deal), the EU AI Act's Article 50 chatbot/deepfake
labeling rules becoming enforceable Aug 2 (fresh angle: API-building
developers, not just model vendors, are on the hook), "forward-deployed
engineers" becoming AI's hottest job title (70% of AI companies hiring
them by Q2's end, up from 5-10% at the start of 2026, $300K-$1.2M+ pay —
traces to 95% of enterprise GenAI pilots showing no measurable impact).
Two swaps before posting: original #1 pick (Anthropic's Claude-hacked-
three-companies story) was a flat repeat of HN's own 07-31 coverage, not
new for today — swapped for the OpenAI benchmark story. Original #2 pick
(DeepSeek's V4-Flash release) overlapped with Hugging Face's own same-day
model-card pick — kept on HF as the more native home, swapped for the
MiniMax/ByteDance story here. Thematic echo kept, not swapped: this
thread's EU AI Act Article 50 pick and HN's EU AI Act/OpenAI-compliance
pick are different specific provisions of the same law's deadline
(2026-08-01) · Amazon's Q2 AWS earnings ($42.2B revenue, +37% YoY,
fastest growth in 18 quarters — swapped in after an initial pick duplicated
HN's Anthropic-hack story), Altman's "we're in the singularity" podcast
quote landing awkwardly, OpenAI cutting GPT-5.6 Luna's price 80% amid the
AI price war, Zuckerberg's WSJ "personal superintelligence" op-ed splitting
reactions, Bloomberg's report that Gemini 3.5 Pro is late and DeepMind is
losing researchers over it (2026-07-31) · Hugging Face CEO Clément Delangue's public $100M-compute
demand of OpenAI after the sandbox-breach hack (rather than suing),
Musk-vs-Altman feud reignited by Apple's trade-secrets lawsuit against
OpenAI/io, Michael Burry's public AI-bubble short-selling argument (Nvidia-
adjacent names like Micron), AI-security startups' $855M 2026 seed-funding
surge (Oak $60M, Cylake $45M, JetStream Security $34M — timing traces to
the OpenAI/HF breach), the EU AI Act's Article 50 transparency-labeling
deadline landing August 2 (€15M/3%-of-revenue fines). Swapped out an
initial Claude-Opus-5-launch pick before posting since it duplicated HN's
own 07-26 coverage of the same launch — flagged the swap and asked Giulia
whether that was the right call vs. letting flagship launches resurface
with new benchmark/pricing detail. Delangue's demand and the security-
funding surge both trace to the same OpenAI/HF breach as HN's Modal-Labs
pick today — 3 mentions of one incident's fallout, flagged as volume, not a
repeat of each other (2026-07-30) · over 1,100 AI-safety employees' "Pacing the Frontier"
statement (OpenAI/Anthropic/DeepMind/Meta AI, endorsed by Dario Amodei,
Jakub Pachocki, Mark Chen as companies within hours), Nvidia's "Open Secure
AI Alliance" (30+ members incl. Microsoft/IBM/SpaceX/Hugging Face,
pointedly excluding OpenAI/Anthropic/Google post-sandbox-breach), FCC ban
on new Chinese humanoid robots/grid inverters (surveillance/grid-security
rationale), a Karpathy bio-edit rumor briefly suggesting he'd left
Anthropic (denied directly, thin/gossip-grade), Anthropic's unreleased
Claude Mythos Preview autonomously finding two cryptography weaknesses
(HAWK post-quantum signature scheme, reduced-round AES, ~$100K compute
each). Nvidia-alliance and Mythos-crypto picks both trace to the same
underlying OpenAI/HF breach event as trigger — distinct stories, kept both,
flagged as two mentions of one incident's fallout (2026-07-29)

## Entries

- **2026-08-01**: Ran the 4-source digest per `PLAYBOOK.md` — this session's
  request from Giulia re-described the routine (4 sources, 5 themes each,
  own thread per source, keep growing instructions, keep asking for
  feedback) and matched what's already documented, so executed rather than
  re-designed. Checked for an existing open PR first per `CLAUDE.md`'s
  consolidation rule: none found (branch was already in sync with `main`
  after PR #42 merged). Checked the 2026-07-31 feedback thread and all 4 of
  its source threads via `slack_read_thread`: **zero replies anywhere**, now
  48+ days running with confirmed zero text feedback ever received on any
  open question. Re-tested network egress via the proxy status endpoint
  before starting: no recent relay failures, consistent with the known
  policy (HN/x.com blocked, GitHub/HF unrestricted). Ran the 4
  source-research tasks as parallel background agents, each briefed with
  all 4 sources' recent picks and the permanent HF exclusions.
  **Two longer-gap repeats caught by the manual full-history cross-check,
  not by the agents' own 3-4-day briefs**: GitHub Trending's initial #1
  pick, `mvanhorn/last30days-skill`, was already a named pick here on
  07-27 (5 days back — outside the brief's window); Hugging Face's initial
  4th pick, `Nanbeige/Nanbeige4.2-3B`, was already a named pick here on
  07-28 (4 days back). Both caught only because this session re-read the
  fuller rolling-list paragraph line-by-line before posting, per the
  standing fix adopted after the 07-30 Fara1.5-27B miss — confirms that
  fix is still doing real work and needs to stay a permanent step, not a
  one-time correction. Sent both research agents back for one replacement
  pick each (fishaudio/fish-speech for GitHub; the XYZAILab/XYZ-Aquila
  pair for Hugging Face) rather than re-running the whole source from
  scratch. **A new variant of the "same release, different angle" question**:
  DeepSeek shipped a same-day refresh of its V4-Flash model today — Hugging
  Face's research found the actual model card, X/Twitter's research
  independently found the same release framed as a price-war business
  story. Kept it on Hugging Face (the more native home for an actual model
  release) and swapped X's pick for a fresh story (MiniMax vs. ByteDance's
  dueling video-model releases) via quick supplementary search. Asked
  Giulia directly whether that's the right call, or whether X should be
  allowed to cover a same-day model release from the business/pricing angle
  even when Hugging Face covers its technical side same day — first time
  this specific variant (literal same release, not just same company) has
  come up. **A second, unrelated X swap**: X's research also independently
  surfaced Anthropic's Claude-hacked-three-companies story, but that's a
  flat repeat of Hacker News's own confirmed 07-31 coverage from
  yesterday, not a same-day collision — swapped for OpenAI's ARC-AGI-3
  benchmark-settings controversy (Chollet's nuanced response about scoring
  parity across non-default API settings). **One thematic echo, not a
  collision, flagged not swapped**: Hacker News's EU AI Act/OpenAI-
  compliance-gap pick and X's EU AI Act Article 50 labeling pick both
  concern the same law's enforcement landing this weekend, but are
  different specific provisions (general-purpose-model government review
  authority vs. chatbot/deepfake transparency labeling) — kept both per
  standing precedent for thematic echoes. **Hacker News's honestly thin
  day**: only 4 solidly-confirmed-or-real picks (3 confirmed live thread
  IDs — 49110215, 49115620/49119180, 49047839 — plus one real, dated EU
  AI Act story that couldn't be pinned to a specific live thread despite
  real search effort) — reported as 4 themes, not padded to 5, per the
  standing honest-reporting default; today's HN slate leaned toward
  "is AI trustworthy/well-measured" (a benchmark-integrity audit finding
  every score inflated 6-15 points, plus Claude Opus 5's system prompt
  leak and an unproven jailbreak claim) — flagged as genuine front-page
  composition, not a curation choice. **GitHub Trending's fetch**: examined
  46 rows across the default, Python-filtered, and Jupyter-notebook-filtered
  trending pages (more thorough than several recent partial-fetch days);
  3 star counts spot-checked live against the GitHub API, all matched
  exactly. **Hugging Face's permanent exclusions held again**: Inkling
  (and its smaller "Inkling-Small" sibling, explicitly not picked either),
  Baidu's Unlimited-OCR, MOSS-Transcribe-Diarize, and microsoft/Fara1.5-27B
  all re-checked directly, no fresh signal on any. **One soft company
  overlap, kept not swapped**: Hacker News's benchmark-integrity story
  today name-drops DeepSeek's V4 Pro model as its central example, while
  Hugging Face's pick is DeepSeek's V4-Flash release — same company,
  different specific model, different story (benchmark-contamination
  critique vs. new release), kept both per standing precedent. Fetch
  strategy unchanged: HN reconstructed via `WebSearch` (still 403 via
  WebFetch/curl for news.ycombinator.com, hn.algolia.com), GitHub Trending
  fetched live via WebFetch on `github.com/trending?since=daily` plus
  language-filtered views, Hugging Face MCP tools worked without
  restriction, X reconstructed via `WebSearch` (still 403 via WebFetch/curl
  for x.com), citing the news coverage that reported on each piece of X
  activity.

- **2026-07-31**: Ran the 4-source digest per `PLAYBOOK.md`. This session's
  triggering prompt re-described the routine from scratch (5 themes/source,
  4 sources incl. HN/GitHub/HF/X, own thread per source, keep growing
  instructions, keep asking for feedback) — matched what's already
  documented here, so executed the existing playbook rather than
  re-designing. Checked for an existing open PR first per `CLAUDE.md`'s
  consolidation rule: none found (prior branch was fully merged into
  `main`, restarted it from `origin/main` before starting today's work).
  Checked the 2026-07-30 feedback-request thread and all 4 of its source
  threads via `slack_read_thread`: **zero replies anywhere**, now 46+ days
  running with confirmed zero text feedback ever received on any open
  question. Re-tested network egress directly (curl to news.ycombinator.com,
  x.com, github.com/trending): HN and x.com still hard-blocked (403 CONNECT
  tunnel failures); github.com/trending also 403'd via raw curl but WebFetch
  on the same URL worked fine and returned live data — confirms the proxy
  block is curl/tool-specific for GitHub, not a genuine site block (consistent
  with the playbook's existing guidance to prefer WebFetch there). Ran the 4
  source-research tasks as parallel background subagents, each briefed with
  all 4 sources' recent picks and the permanent HF exclusions (including the
  07-30 Fara1.5-27B correction, explicitly called out so it isn't re-picked).
  **One direct same-day collision, cleanly resolved**: HN and X both
  independently surfaced Anthropic's disclosure that Claude itself hacked
  three companies during safety testing. Kept it on HN (a confirmed live
  thread, item id 49116922) and swapped in a fresh X pick (Amazon's Q2 AWS
  earnings, $42.2B revenue/+37% YoY, its fastest growth in 18 quarters) found
  via quick supplementary search. **A new variant of the same-entity overlap
  question**: GitHub Trending's top pick (`NousResearch/hermes-agent`, a
  learning-loop agent feature) and Hacker News's 5th pick (a security
  incident where someone ran that same open-source Hermes agent unattended
  inside Thailand's Finance Ministry) are the same underlying tool covered
  from opposite angles (feature launch vs. malicious misuse) — kept both per
  the standing "different angle, same entity" precedent, but asked Giulia
  directly whether running a positive feature story about a tool the same
  day it's implicated in a real breach is fine, or whether that combination
  specifically should get one side dropped. **Honest pattern note**: all 5
  of today's HN picks turned out to be some flavor of "AI agents behaving
  badly or getting exploited" (Anthropic's own breach, a Word-document worm
  through Copilot, GitHub's bounty-program cuts citing AI-slop reports, a
  critical unauthenticated flaw in the Ruflo agent-orchestration tool, and
  the Thailand Hermes incident) — reported honestly since that's genuinely
  what the front page skewed toward, not a curation choice, same treatment
  as the 07-15 clustering flag. GitHub Trending's page again only rendered a
  partial ~12 of the usual ~25 rows (confirmed reproducible across two
  fetches, star counts spot-checked live); supplemented with the Python- and
  Jupyter-notebook-filtered trending views to examine ~43 rows total rather
  than treat the partial unfiltered page as the whole picture. Hugging
  Face's permanent exclusions (Inkling, Baidu Unlimited-OCR,
  MOSS-Transcribe-Diarize, and now Fara1.5-27B) all re-checked and held —
  no fresh signal on any. Posted the usual 4 source threads plus a
  feedback-request message with the specific ask above; standing status and
  all prior defaults restated as still in effect absent a reply.

- **2026-07-30**: Ran the 4-source digest per `PLAYBOOK.md` — this session's
  request from Giulia re-described the routine (4 sources, 5 themes each, own
  thread per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  Checked for an existing open PR first per `CLAUDE.md`'s consolidation rule:
  none found. Checked the 2026-07-29 feedback-request thread and all 4 of its
  source threads via `slack_read_thread`: **zero replies anywhere**, now 45+
  days running with confirmed zero text feedback ever received on any open
  question. Re-tested network egress via the proxy status endpoint before
  starting: no recent relay failures, consistent with the known policy
  (HN/x.com blocked, GitHub/HF unrestricted). Ran the 4 source-research tasks
  as parallel background subagents, each briefed with all 4 sources' recent
  picks and the 3 permanent HF exclusions. **GitHub Trending's thinnest day
  this routine has recorded**: the page rendered its usual partial 17 of ~25
  rows (confirmed via two independent fetches, star counts spot-checked
  against live GitHub data); of those, 9 were exact repeats from the last 3
  days, 5 were non-AI (today's #1-by-page-order was opengeos/GeoLibre, a GIS
  platform), and manually catching a **new kind of longer-gap repeat** —
  `obra/superpowers` wasn't in the 3-day rolling list, but a full-history
  check found it was already a named GitHub Trending pick on 07-25 with
  almost no star growth since (260K → 263.7K) — excluded it too. That left
  only 2 genuinely fresh AI picks (different-ai/openwork, a Claude-Cowork
  open-source clone; MoonshotAI/FlashKDA, Kimi Delta Attention CUDA kernels),
  reported honestly rather than padded. **One same-day collision caught and
  swapped before posting**: X's research surfaced Claude Opus 5's launch
  (half-price/beats-flagship framing) as a pick, but that's the exact same
  launch Hacker News already covered on 07-26 — not a new development, just
  a repeat of an old announcement outside the normal 3-day window. Swapped it
  for a fresh story (AI-security startups' $855M seed-funding surge in 2026)
  found via quick supplementary web search rather than post a repeat; flagged
  the swap explicitly in today's feedback-request message and asked Giulia
  directly whether that was the right call versus letting flagship-launch
  stories resurface with new benchmark/pricing detail the way Kimi K3's
  "developing story" updates have been allowed through. **One incident
  showing up three times, flagged not swapped**: the OpenAI/Hugging Face
  sandbox-breach saga produced three distinct new facts across two sources
  today — HN's second-victim development (Modal Labs), X's Hugging Face CEO
  Clément Delangue's public $100M-compute demand, and X's AI-security
  seed-funding surge (whose timing traces to the same breach) — kept all
  three since each is genuinely new information, but flagged the volume in
  the feedback message the same way Kimi K3's 4-mention day was flagged on
  07-27. **One thematic echo, not a collision**: HN's "After the AI Crash"
  spending-math blog post and X's Michael Burry AI-bubble short-selling
  story are both AI-valuation-skepticism arguments today from different
  people/sources — kept both, just noted the pattern. **Hacker News's
  honestly-confirmed 4 picks**: all 4 verified as real news.ycombinator.com
  thread IDs via search triangulation (item ids 49076176, 49096953, 49096917,
  49097727); a 5th candidate (Anthropic's Claude Mythos Preview HAWK
  crypto-attack finding) was trending on HN today but was explicitly left off
  since it's a continuation of a story X/Twitter already covered on 07-29.
  **Hugging Face's permanent exclusions held again**: Inkling, Baidu's
  Unlimited-OCR, and MOSS-Transcribe-Diarize all re-checked directly, no
  fresh signal on any. **Real miss, caught after posting and corrected
  in-thread**: the HF research agent also picked Microsoft's Fara1.5-27B,
  did a longer-gap check, but compared it against the older, differently-
  named Fara-7B (Nov 2025) and concluded it was a new model family — when
  the actual repeat was staring at us in the rolling list this same session
  had just read: `microsoft/Fara1.5-27B` was already a named HF pick here
  on 07-26, verbatim. The pre-research brief only carries the last-3-days
  list, and 07-26 had just aged out of that window when the brief was
  written, so the agent had no reason to flag it; the failure was that I
  (the orchestrating session) also didn't cross-check the final 5 HF picks
  against the fuller rolling list/history before posting, the same
  spot-check step the playbook already requires for exactly this failure
  mode (see the 07-10 Baidu-Unlimited-OCR catch). Posted a correction reply
  in the HF thread once caught, and updated the rolling list to explicitly
  warn future runs off re-picking Fara1.5-27B by name. **Process gap to
  close**: the manual full cross-check step (added 07-23) was applied
  across sources for same-day collisions but not applied within a single
  source against its own longer history — proposing in `PLAYBOOK.md` that
  the manual compare step explicitly include re-reading each source's own
  rolling-list paragraph line-by-line before posting, not just trusting the
  research agent's self-reported longer-gap check.
  Fetch strategy unchanged: HN reconstructed via `WebSearch` (still 403 via
  WebFetch/curl for news.ycombinator.com, hn.algolia.com), GitHub Trending
  fetched live via WebFetch on `github.com/trending?since=daily` (verified
  via two independent fetches, several star counts spot-checked against live
  GitHub API data), Hugging Face MCP tools worked without restriction, X
  reconstructed via `WebSearch` (still 403 via WebFetch/curl for x.com),
  citing the news coverage that reported on each piece of X activity.

- **2026-07-29**: Ran the 4-source digest per `PLAYBOOK.md` — this session's
  request from Giulia re-described the routine (4 sources, 5 themes each, own
  thread per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  Checked for an existing open PR first per `CLAUDE.md`'s consolidation rule:
  none found. Checked the 2026-07-28 feedback-request thread via
  `slack_read_thread`: **zero replies**, now 44+ days running with confirmed
  zero text feedback ever received on any open question. Re-tested network
  egress via the proxy status endpoint before starting: no recent relay
  failures, consistent with the known policy (HN/x.com blocked, GitHub/HF
  unrestricted). Ran the 4 source-research tasks as parallel background
  subagents, each briefed with all 4 sources' recent picks and the 3
  permanent HF exclusions. **HN's honestly thin day**: only 4 solidly
  live-thread-confirmed picks — a plausible 5th (a bipartisan "AI Kill
  Switch Act" responding to the earlier OpenAI/Hugging-Face sandbox-breach
  incident) couldn't be pinned to a real `item?id=` despite repeated
  targeted searches, so left out rather than posted unverified, same call
  as 07-27. **New kind of soft cross-source overlap, kept not swapped**:
  Microsoft's VibeVoice landed on both GitHub Trending (the original
  open-source "frontier" voice-cloning/TTS model) and Hugging Face
  (`VibeVoice-ASR-BitNet`, an extreme-compression speech-*recognition*
  spinoff) — same company and product-family name, but a genuinely
  different capability (generating speech vs. recognizing it) and a
  different technical story (open-sourcing a frontier model vs. a BitNet
  quantization result). Kept both per the standing "distinct artifact from
  the same entity" precedent, flagged explicitly in both threads rather
  than silently treated as unrelated — closest call yet under this
  precedent since the product name itself is identical, worth a specific
  read from Giulia on whether that's too close. **One thematic echo, not a
  collision**: X's Nvidia "Open Secure AI Alliance" story (pointedly
  excluding OpenAI/Anthropic/Google) and HN's Anthropic-won't-sign-
  open-weights-pledge story both center on "who is/isn't signing which
  industry coalition," but are distinct specific events — not swapped, just
  noted. **GitHub's honest composition note, again**: page rendered only 17
  of the usual ~25 rows (same partial-fetch issue as 07-28); of those, both
  the #1 position (opengeos/GeoLibre, a GIS platform) and the single
  biggest star-gain mover (NanmiCoder/MediaCrawler, a social-media scraper)
  were non-AI — flagged plainly even though 5 genuine AI picks were still
  available today, per the standing honest-reporting default. **Hugging
  Face's permanent exclusions held again**: Inkling, Baidu's Unlimited-OCR,
  and MOSS-Transcribe-Diarize all re-checked directly via `hub_repo_details`,
  no version/benchmark change on any. Also screened out (not presented as
  news, momentum-only): a wave of "uncensored/abliterated" GGUF merges and
  several near-identical Wan2.2 video-gen demo reposts. **X's thinnest pick,
  flagged rather than hidden**: the Karpathy bio-edit rumor (kept 5th) is
  gossip-grade/single-secondary-source compared to the other 4, included
  with that caveat per the research agent's own honesty note rather than
  silently upgraded to equal footing. Fetch strategy unchanged: HN
  reconstructed via `WebSearch` (news.ycombinator.com, hn.algolia.com, and
  3 third-party HN mirrors — orangebot.ai, daemonology.net/hn-daily,
  blog.mean.ceo — all still 403 via the proxy; 4 of 5 candidate picks
  confirmed as live `item?id=` threads), GitHub Trending fetched live via
  WebFetch on `github.com/trending?since=daily` (6 star counts spot-checked
  against the live GitHub API, 5 exact matches and 1 off-by-one from normal
  live-count drift — confirms the pull is current, not stale), Hugging Face
  MCP tools worked without restriction, X reconstructed via `WebSearch`
  (still 403 via WebFetch/curl for x.com), citing the news coverage that
  reported on each piece of X activity rather than x.com links directly.

- **2026-07-28**: Ran the 4-source digest per `PLAYBOOK.md` — this session's
  request from Giulia re-described the routine (4 sources, 5 themes each, own
  thread per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  Checked for an existing open PR first per `CLAUDE.md`'s consolidation rule:
  none found. Checked the 2026-07-27 feedback-request thread and all 4 of its
  source threads via `slack_read_thread`: **zero replies anywhere**, now 43+
  days running with confirmed zero text feedback ever received. Ran the 4
  source-research tasks as parallel background subagents, each briefed with
  all 4 sources' recent picks and the 3 permanent HF exclusions. **New
  editorial call, flagged not decided silently**: Hugging Face's research
  initially set aside `moonshotai/Kimi-K3` to avoid an assumed collision with
  HN/X, but neither source actually covered Kimi K3 today — and 07-27's
  digest had explicitly fact-checked and found no *official* HF repo existed
  yet. Since one now does (by far the platform's top trending item, with a
  companion paper), swapped it in over a smaller pick rather than holding it
  back reflexively, closing the loop on Tuesday's open fact-check. **One
  soft same-company overlap, kept not swapped**: Hacker News (Microsoft's
  MAI-Cyber-1-Flash cybersecurity model) and GitHub Trending (Microsoft's
  agent-governance-toolkit) both landed on Microsoft + AI-agent-security
  today — distinct products, not a repeat, kept both per standing precedent.
  **No same-day collisions requiring the tiebreaker**: manually compared all
  20 final picks across sources — none overlapped, first clean cross-source
  day in a while (after the HN research agent itself flagged an open-weight-
  letter story as high collision risk with X, which didn't materialize since
  X's final picks moved to different stories). **Two new honest flags**: (1)
  GitHub Trending's WebFetch pull only reliably captured ~12 of the usual ~25
  trending rows despite repeated retries — star counts spot-checked as live
  and current regardless, so treated as an incomplete crawl rather than a
  stale one, but worth revisiting the fetch approach if a fuller sweep
  matters. (2) One GitHub pick (affaan-m/ECC) has a star count (234,403 on a
  ~6-month-old repo) disproportionate to its actual visibility — included
  with an explicit skeptical caveat in the digest rather than presented at
  face value or dropped outright. **Hugging Face's other permanent exclusions
  held**: Inkling and Baidu's Unlimited-OCR both re-checked directly, no
  fresh signal on either; MOSS-Transcribe-Diarize didn't surface in today's
  search at all. **"Newsly" question given a last flag**: the separate
  inbox-sourced "Newsly" digest (outside this routine's spec since 07-02) has
  now been asked about 4+ times with zero reply — flagged today as the last
  time it'll be raised absent a response, per the playbook's own
  default-after-silence policy, since it's a different automation this
  routine doesn't control anyway. Fetch strategy unchanged: HN reconstructed
  via `WebSearch` (a third-party GitHub-hosted HN-digest mirror gave
  higher-confidence thread IDs than blind reconstruction alone; 3 of 5 picks
  independently confirmed as live thread IDs), X reconstructed via
  `WebSearch` (still 403 via WebFetch/curl for news.ycombinator.com,
  hn.algolia.com, x.com), GitHub Trending fetched live via WebFetch on
  `github.com/trending?since=daily` (5 star counts spot-checked against the
  live GitHub API, all matched), Hugging Face MCP tools worked without
  restriction.

- **2026-07-27**: Ran the 4-source digest per `PLAYBOOK.md` — this session's
  request from Giulia re-described the routine (4 sources, 5 themes each, own
  thread per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  **Consolidation housekeeping first**: PR #37 (logging the 2026-07-26 run)
  was still open and unmerged when this session started — exactly the
  anti-pattern `CLAUDE.md` warns about, since it meant `main` was a day
  stale. Reviewed its diff (clean, docs-only), marked it ready for review,
  and merged it directly to `main` before starting today's work, per this
  repo's standing consolidation policy. Checked the 2026-07-26 feedback
  thread and all 4 of its source threads via `slack_read_thread`: **zero
  replies anywhere**, now 42+ days running with confirmed zero text feedback
  ever received. Ran the 4 source-research tasks as parallel background
  subagents, each briefed with all 4 sources' recent picks and the 3
  permanent HF exclusions. **Major cross-source collision, resolved with a
  new twist**: HN's and X's research both independently surfaced two big
  stories — Kimi K3's actual weights release (with a hallucination-rate
  problem) and Nvidia's reported ~$250B backstop for OpenAI's Ohio data
  center. For Kimi K3, kept both HN's angle (weights/quality) and a second
  distinct HN pick (a Kimi-K3-agent-found Redis exploit), while X kept its
  own distinct Kimi angles (Musk's Grok 4.6 rivalry, a policy letter) —  no
  single story repeated, but 4 total Kimi mentions in one day, flagged
  explicitly to Giulia as a lot of one story regardless of angle-diversity.
  For the Nvidia/Ohio story, **new resolution path**: rather than force it
  onto HN (both agents flagged high collision risk, but repeated targeted
  searches couldn't confirm an actual live HN thread id despite the story
  clearly dominating the wider news cycle), left HN at 4 honest, fully-
  verified picks and kept the story on X only, where the discussion has
  verifiable Twitter-native reactions (Michael Burry, Ed Zitner) attached.
  Flagged this as an open question: should the bar for an "HN pick" always
  require a confirmed live thread id, even if that costs a 5th pick some
  days? **New fact-check catch**: both HN's and X's research described
  Kimi K3 as having "landed on Hugging Face" — a direct HF repo search
  found no official moonshotai/Kimi-K3 repo, only unofficial near-zero-
  download re-uploads. Rather than repeat an unverified claim just because
  two other sources agreed on it, left it out of HF's picks and noted the
  discrepancy in-thread. **GitHub's honest non-AI note**: today's page was
  50% AI-related (7 of 14), but the single biggest mover on the entire page
  (permissionlesstech/bitchat, +1,166 stars) is a non-AI Bluetooth-mesh chat
  app — reported that plainly as the 5th "theme" per the standing honest-
  reporting default, rather than quietly omit it or pad with a weaker AI
  pick. **Hugging Face's permanent exclusions held again**: Inkling, Baidu's
  Unlimited-OCR, and MOSS-Transcribe-Diarize all re-checked directly, no
  fresh signal on any. Fetch strategy unchanged: HN and X reconstructed via
  `WebSearch` (still 403 via WebFetch/curl for news.ycombinator.com,
  hn.algolia.com, x.com — reconfirmed via proxy status check, zero recent
  relay failures), GitHub Trending fetched live via WebFetch on
  `github.com/trending?since=daily` (2 star counts spot-checked against the
  live GitHub API, both exact matches), Hugging Face MCP tools worked
  without restriction.

- **2026-07-26**: Ran the 4-source digest per `PLAYBOOK.md` — this session's
  request from Giulia re-described the routine (4 sources, 5 themes each, own
  thread per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  Checked for an existing open PR first per `CLAUDE.md`'s consolidation rule:
  none found. Checked the 2026-07-25 feedback-request thread and all 4 of its
  source threads via `slack_read_channel`: **zero replies anywhere**, now 41+
  days running with confirmed zero text feedback ever received. Ran the 4
  source-research tasks as parallel background subagents, each briefed with
  all 4 sources' recent picks and the 3 permanent HF exclusions. **One
  same-day collision caught via the manual full cross-check step**: HN's and
  X's research independently surfaced two exact-same stories — the disputed
  OpenAI/Hugging Face sandbox-breach incident and the Claude Opus 5 launch
  (X's own research flagged both as high-overlap-risk itself, before the
  manual compare even ran). Kept both on HN (earlier, better-sourced coverage)
  and found two fresh X replacements via quick supplementary search (China
  reportedly weighing tighter AI export controls on itself; Kimi K3's
  imminent full-weights release). **Same-model, different-angle overlap kept,
  not swapped**: Moonshot AI's Kimi K3 shows up on both HN (a joint UK/US
  government cyber-capability assessment) and X (tonight's weights-release
  milestone) — distinct stories, kept both per standing precedent for
  same-company overlaps. **GitHub Trending's second thin day in a row**: the
  page only rendered 17 entries (vs. usual ~25, confirmed by checking for
  entries past #17), and of the 9 AI-related rows, 5 were exact repeats from
  the last 3 days — left with only 4 non-repeat picks, reported honestly per
  the standing default rather than force a 5th. **Hugging Face's permanent
  exclusions held**: Inkling, Baidu's Unlimited-OCR, and MOSS-Transcribe-
  Diarize all re-checked directly and excluded again, no fresh signal on any.
  **HN's slant today**: leaned hard into AI-and-adversarial-behavior /
  public-pushback themes (the sandbox breach, the Kimi K3 cyber assessment,
  Flock camera vigilantism) alongside a lighter em-dash culture piece —
  reported honestly per the standing default. Fetch strategy unchanged: HN
  confirmed via live HN thread IDs this time (not just search-reconstructed —
  all 5 picks verified as real `news.ycombinator.com/item?id=` threads via
  cross-referencing WebSearch results), X reconstructed via `WebSearch`
  (still blocked via WebFetch/curl for x.com), GitHub Trending fetched live
  via WebFetch on `github.com/trending?since=daily` (2 star counts spot-
  checked against the live GitHub API, both exact matches), Hugging Face MCP
  tools worked without restriction.

- **2026-07-25**: Ran the 4-source digest per `PLAYBOOK.md` — this session's
  request from Giulia re-described the routine (4 sources, 5 themes each, own
  thread per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  Checked for an existing open PR first per `CLAUDE.md`'s consolidation rule:
  none found. Checked the 2026-07-24 feedback-request thread via
  `slack_read_thread`: **zero replies**, now 40+ days running with confirmed
  zero text feedback ever received. **New wrinkle checked and ruled out**:
  Giulia sent a bare `@Claude` mention (no text) in the channel yesterday at
  09:45 — a separate Claude-in-Slack session had already replied "Hey, what's
  up? What can I help with?" with no follow-up from Giulia, so treated as a
  stray tag, not feedback, and not actionable. Re-tested network egress via
  the proxy status endpoint before starting: no recent relay failures,
  consistent with the known policy (HN/x.com blocked, GitHub/HF unrestricted).
  Ran the 4 source-research tasks as parallel background subagents, each
  briefed with all 4 sources' recent picks and the 3 permanent exclusions.
  **Cleanest cross-source day in a while**: manually compared all 20 final
  picks against each other — zero exact-story collisions, the first time in
  several runs neither the pre-briefing nor the manual compare step needed to
  swap anything out. One mild company-overlap kept rather than swapped:
  Moonshot AI showed up on both Hugging Face (its new Kimi-K2.7-Code model
  release) and X (its $50B Hong Kong IPO plans) — distinct stories about the
  same company, same precedent as prior Anthropic/Grok double-mention days.
  **GitHub Trending's recurring skew**: page was unusually AI-dense (~83% of
  18 repos) but the "Claude Code agent-skills framework" theme continued for
  a 3rd distinct repo in recent days (obra/superpowers, 260K+ stars, +600
  today, after ComposioHQ's and mattpocock's repos) — flagged again rather
  than swapped out, per the standing honest-reporting default. **Hugging
  Face's permanent exclusions held**: Inkling and Baidu's Unlimited-OCR both
  re-checked directly, no fresh signal on either, excluded again;
  MOSS-Transcribe-Diarize didn't surface in today's search at all. **HN's
  slant today**: leaned into AI-agent-security incidents (a Thai government
  breach attempt via an unattended Hermes agent, a now-patched ChatGPT
  Agent-Builder CSRF flaw dubbed "AgentForger") alongside a coding-agent
  methodology essay, a new Black Forest Labs foundation model (FLUX 3), and
  Google's 15M-chat "AI & Economy" usage study — reported honestly per the
  standing default. Fetch strategy unchanged: HN and X reconstructed via
  `WebSearch` (still 403 via WebFetch/curl for news.ycombinator.com,
  hn.algolia.com, x.com), GitHub Trending fetched live via WebFetch on
  `github.com/trending?since=daily` (verified current via two independent
  fetches plus live spot-checks on 5 repos), Hugging Face MCP tools worked
  without restriction.

- **2026-07-24**: Ran the 4-source digest per `PLAYBOOK.md` — this session's
  request from Giulia re-described the routine (4 sources, 5 themes each, own
  thread per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  Checked for an existing open PR first per `CLAUDE.md`'s consolidation rule:
  none found. Checked the 2026-07-23 feedback-request thread via
  `slack_read_thread`: **zero replies**, now 39+ days running with confirmed
  zero text feedback ever received. Re-tested network egress via the proxy
  status endpoint before starting: no recent relay failures, consistent with
  the known policy (HN/x.com blocked, GitHub/HF unrestricted). Ran the 4
  source-research tasks as parallel background subagents, each briefed with
  all 4 sources' recent picks and the 3 permanent exclusions. **Two same-day
  collisions caught via the manual full cross-check step** (adopted 07-23,
  applied for the first time today): Alphabet's Q2 earnings/capex story and
  Tesla's Optimus-production story each surfaced independently on both HN and
  X. Kept both on HN (earnings-call-backed, better sourced) and found two
  fresh X replacements via quick supplementary web search (DeepSeek V4's
  stable release; OpenAI's $750B compute-spend raise + its first
  self-built data center). Notably, HN's own research flagged both risks in
  advance ("collision flag: high/moderate risk") without yet knowing X's
  actual picks — a good sign the process is maturing, though it still took a
  manual compare-all-20 pass to confirm and resolve. **New wrinkle flagged,
  not resolved unilaterally**: two of the surviving X picks (OpenAI's $1T IPO
  filing, OpenAI's $750B compute-spend raise) both center on OpenAI — distinct
  stories, not a repeat, but asked Giulia whether that's too much single-company
  coverage in one day, same tradeoff as the 07-12 Anthropic-heavy day. **GitHub
  Trending's thinnest day in over a week**: only 16 repos on the page (vs. the
  usual ~25, confirmed via 3 separate fetches), 6 of 10 AI-related rows were
  exact repeats from the last 3 days, leaving only 4 non-repeat picks — reported
  honestly per the standing default rather than force a 5th. One of the 4
  (mattpocock/skills) continues the same "curated Claude Skills bundle" theme
  ComposioHQ's repo covered yesterday (different repo/author) — flagged
  in-thread as continued momentum rather than treated as fully new. **Hugging
  Face's permanent exclusions held**: Thinking Machines Lab's "Inkling" and
  Baidu's "Unlimited-OCR" both still trending on pure momentum today (Baidu's
  had the single highest trending score of anything in the search) — both
  checked directly, no fresh signal on either, excluded again. Fetch strategy
  unchanged: HN and X reconstructed via `WebSearch` (still blocked via
  WebFetch/curl for news.ycombinator.com, hn.algolia.com, x.com), GitHub
  Trending fetched live via WebFetch on `github.com/trending?since=daily`
  (star counts spot-checked against the live GitHub API), Hugging Face MCP
  tools worked without restriction.

- **2026-07-23**: Ran the 4-source digest per `PLAYBOOK.md` — this session's
  request from Giulia re-described the routine (4 sources, 5 themes each, own
  thread per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  Checked for an existing open PR first per `CLAUDE.md`'s consolidation rule:
  none found. Checked the 2026-07-22 feedback-request thread via
  `slack_read_thread`: **zero replies**, now 37+ days running with confirmed
  zero text feedback ever received. Ran the 4 source-research tasks as
  parallel background subagents, each briefed with all 4 sources' recent
  picks per the standing default. **Two standing questions resolved by
  silence**: (1) the cross-source briefing step is now permanent in
  `PLAYBOOK.md` (2 clean catches in a row, 07-21/07-22). (2) Thinking
  Machines Lab's "Inkling" resurfaced as a stale non-story a 4th time
  (checked directly: no update since 07-14) — now **permanently, silently
  excluded** going forward absent real news, same as MOSS-Transcribe-Diarize
  and Baidu's Unlimited-OCR. **New failure mode caught**: the pre-research
  cross-source briefing only carries *prior-day* picks, so it can't catch two
  sources landing on the *same-day* story independently — after all 4 agents
  returned, a manual compare of all 20 final picks found two such collisions
  the briefing missed: Jack Dorsey/Block's "Buzz" launch (GitHub's actual
  trending repo `block/buzz` vs. X's business-angle coverage of the same
  launch) and the Microsoft-Mistral GPU deal (Hacker News vs. X, same July 21
  story). Resolved both by keeping the story on its more natural source
  (trending repo stays on GitHub, business/policy deal stays on HN) and
  finding a fresh X replacement each time via quick supplementary search
  (Nvidia's 9.3% Nebius stake; Martin Scorsese joining Black Forest Labs).
  Added this as a permanent standing step in `PLAYBOOK.md` — always manually
  cross-check all 4 sources' actual final picks against each other, not just
  rely on the pre-research briefing. Asked Giulia whether "keep on the more
  native source" is the right tiebreaker or whether these should be flagged
  to her instead. **GitHub Trending's skew, again**: 69% of the page (11 of
  16) was genuinely AI-related, but 5 of 7 fresh candidates were near-
  identical "agent infrastructure" tooling (chat-for-agents, agent gateways,
  skill catalogs) — picked the 5 most distinct angles rather than 5 near-
  duplicates. Fetch strategy unchanged: HN and X reconstructed via
  `WebSearch` (still 403 via WebFetch/curl for news.ycombinator.com,
  hn.algolia.com, x.com — reconfirmed via proxy status check), GitHub
  Trending fetched live via WebFetch on `github.com/trending?since=daily`
  (spot-checked 2 star counts against the live GitHub API, matched), Hugging
  Face MCP tools worked without restriction.

- **2026-07-22**: Ran the 4-source digest per `PLAYBOOK.md` — this session's
  request from Giulia re-described the routine (4 sources, 5 themes each, own
  thread per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  Checked for an existing open PR first per `CLAUDE.md`'s consolidation rule:
  none found. Checked the 2026-07-21 feedback-request thread via
  `slack_read_thread`: **zero replies**, now 36+ days running with confirmed
  zero text feedback ever received. Ran the 4 source-research tasks as
  parallel subagents, each briefed with all 4 sources' recent picks (not just
  its own) per the fix first applied 07-21. **The fix worked a 2nd day
  running**: HN's and X's research independently surfaced the same story (a
  Robert Scoble tweet claiming Anthropic acquired robotics startup Physical
  Intelligence) — caught immediately from the cross-source list already in
  the brief, no manual supplementary search needed. Kept it on HN, swapped in
  a fresh X story (Anthropic's Q2 lobbying spend surging past Nvidia's,
  traced to June's Commerce Department shutdown of its models) found via a
  quick supplementary search. Two clean applications in a row (07-21, 07-22)
  is enough to call this proven rather than a one-day fluke — updated
  `PLAYBOOK.md`'s process note to make it the permanent default rather than
  re-proposing it again. **New catch, matching an existing precedent**:
  Hugging Face's research surfaced Thinking Machines Lab's "Inkling" again —
  the same July 14 model now flagged as a stale non-story 3 times (07-19,
  07-20, today), always still trending on pure momentum with no new
  version/benchmark since. Caught it manually (the HF subagent's brief only
  covered the last-3-days list, not the longer history) and swapped in
  Nanbeige/Nanbeige4.2-3B, a small bilingual model genuinely uploaded today.
  Proposed in today's feedback ask that Inkling get the same permanent
  silent-exclusion treatment already applied to MOSS-Transcribe-Diarize if it
  resurfaces again with no fresh signal. **GitHub Trending's flavor**: strong
  AI day (~58% of the page, 11 of 19 repos) but still agent/coding-tool
  skewed; reported honestly per the standing default, with 3 near-top entries
  skipped as repeats from the last 3 days. **No other cross-source or
  longer-gap collisions found** after checking all 4 sources' final picks
  against each other and against the fuller history. Fetch strategy
  unchanged: HN and X reconstructed via `WebSearch` (still 403 via
  WebFetch/curl for news.ycombinator.com, hn.algolia.com, x.com), GitHub
  Trending fetched live via WebFetch on `github.com/trending?since=daily`
  (spot-checked 2 star counts against the live GitHub API, matched within
  noise), Hugging Face MCP tools worked without restriction.

- **2026-07-21**: Ran the 4-source digest per `PLAYBOOK.md` — this session's
  request from Giulia re-described the routine (4 sources, 5 themes each, own
  thread per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  Checked for an existing open PR first per `CLAUDE.md`'s consolidation rule:
  none found. Checked the 2026-07-20 feedback-request thread via
  `slack_read_thread`: **zero replies**, now 35+ days running with confirmed
  zero text feedback ever received. Ran the 4 source-research tasks as
  parallel background subagents, and for the first time applied yesterday's
  proposed fix — each agent's brief included not just its own source's recent
  picks but all 4 sources' recent picks from the last 3 days, specifically to
  catch cross-source repeats before they're drafted rather than after.
  **The fix worked**: X's research independently surfaced both Moonshot's
  Kimi K3 (which turned out to be Hacker News's own top pick today) and Demis
  Hassabis's "AI watchdog" essay (a repeat of X's own 07-16 coverage, no new
  signal since) — both were caught immediately from the cross-source list
  already in the brief, with no extra manual supplementary search needed to
  find clean replacements (Alibaba's Qwen3.8 Max preview and Nvidia's Cosmos
  3 Edge launch), unlike 07-20's 3-catch day which took real extra research
  effort. Proposing this as the permanent default going forward and asking
  Giulia to confirm rather than judging off one clean day. **One GitHub
  judgment call**: kept kvcache-ai/ktransformers even though a previous run
  (07-19) excluded it as a "near-repeat" of airllm's small-GPU-inference
  pitch — today it's a distinct, actively-maintained project with its own
  fresh star velocity, so treated as fair game rather than a repeat; flagged
  in case that reverses the prior call too casually. GitHub Trending was
  otherwise heavily AI-related (~76% of the page) but dominated by repeats
  once checked against the 3-day list. Fetch strategy unchanged: HN and X
  reconstructed via `WebSearch` (still 403 via WebFetch/curl for
  news.ycombinator.com, hn.algolia.com, x.com), GitHub Trending fetched live
  via WebFetch on `github.com/trending?since=daily` (spot-checked star counts
  against the live GitHub API, matched within noise), Hugging Face MCP tools
  worked without restriction.

- **2026-07-20**: Ran the 4-source digest per `PLAYBOOK.md` — this session's
  request from Giulia re-described the routine (4 sources, 5 themes each, own
  thread per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  Checked for an existing open PR first per `CLAUDE.md`'s consolidation rule:
  none found. Checked the 2026-07-19 feedback-request thread and all 4 of its
  source threads via `slack_read_thread`: **zero replies anywhere**, now 34+
  days running with confirmed zero text feedback ever received. Ran the 4
  source-research tasks as parallel background subagents per the existing
  process note; all 4 completed cleanly. **Busiest repeat-catching day yet —
  3 separate longer-gap repeats caught, not just same-day collisions**: (1)
  HN's own research resurfaced Thinking Machines Lab's "Inkling" as if
  breaking news, but it's the exact release HN covered in depth on 07-16 —
  swapped for the SF nudify-apps story. (2) HN's research also resurfaced
  Demis Hassabis's "Framework for Frontier AI" essay; confirmed via
  supplementary search it's the same 07-14 essay X already covered on 07-16
  as "Hassabis's AI-watchdog manifesto" — swapped for the Qualcomm/Tenstorrent
  acquisition-talks story. (3) X's research surfaced both Alex Turner's
  DeepMind resignation (literal repeat of HN's 07-16 story, same person and
  event) and China's WAICO governance bloc (repeat of HN's own pick from
  *yesterday*, 07-19) — swapped both for Meta's "Iris" chip story and the Gen
  Z/AI-backlash trend piece. All 3 catches were the same failure mode: a
  source's research agent, briefed only with that source's own recent-picks
  list, re-surfaced a story a *different* source (or the same source, further
  back) had already run — the existing "spot-check against fuller history"
  step caught all 3 before posting, but needed real supplementary web
  research (4 extra search rounds) to find clean, verifiably-fresh
  replacements, more manual effort than a typical run. Flagged this pattern
  directly to Giulia and proposed briefing each source's research agent with
  the *other 3 sources'* recent picks too, not just its own, to catch these
  earlier and cut down on the swap-and-research cycle. **New methodology
  question raised**: today's swapped-in replacements (SF nudify apps,
  Qualcomm/Tenstorrent, Meta Iris chip, Gen Z backlash) are real and
  dated but weren't verifiable as literal live HN threads (for HN's two) or
  came from slightly older coverage (Meta's chip news is from 07-09, Gen Z
  backlash traces to May commencement season with July commentary) — asked
  whether a swapped-in replacement should be held to the same confirmation
  bar as an original pick, or whether "genuinely new to this routine" is
  sufficient even if the underlying story broke a few days or weeks earlier.
  **GitHub Trending's flavor shifted**: still 3/5 agent-tooling, but 2/5
  (transcribe.cpp, moonshine) were speech/voice AI instead of yesterday's
  pure coding-agent cluster — first day this mix has appeared, reported
  honestly. Fetch strategy unchanged: HN and X reconstructed via `WebSearch`
  (still 403 via WebFetch/curl for news.ycombinator.com, hn.algolia.com,
  x.com), GitHub Trending fetched live via WebFetch on
  `github.com/trending?since=daily` (spot-checked 5 star counts against the
  live GitHub API, all matched within noise), Hugging Face MCP tools worked
  without restriction.

- **2026-07-19**: Ran the 4-source digest per `PLAYBOOK.md` — this session's
  request from Giulia re-described the routine (4 sources, 5 themes each, own
  thread per source, keep growing instructions, keep asking for feedback) and
  matched what's already documented, so executed rather than re-designed.
  Checked for an existing open PR first per `CLAUDE.md`'s consolidation rule:
  none found. Checked the 2026-07-18 feedback-request message and all 4 of its
  source threads via `slack_read_channel`: **zero replies anywhere** (each
  source thread's only reply is the routine's own theme-post; the
  feedback-request message itself has zero replies) — now 33+ days running
  with confirmed zero text feedback ever received. Ran the 4 source-research
  tasks as parallel background subagents per the existing process note; all 4
  completed cleanly. **Two longer-gap repeats caught, not just same-day
  collisions**: (1) Hugging Face's research surfaced Thinking Machines Lab's
  "Inkling" as today's #1 trending item again — but it's the exact same ~950B
  flagship model Hacker News covered in depth on 07-16 (and HF itself passed
  on it that day for the same reason), with no new version or fresh signal in
  the 3 days since. Treated as a stale repeat rather than news and swapped in
  InternScience/Agents-A1. (2) X's research independently surfaced two more
  repeats outside the normal 2-3 day window: Hassabis's AI-watchdog manifesto
  (literal repeat of X's own 07-16 pick) and Gemini 3.5 Pro's delay (repeat of
  HN's 07-17 pick). Both caught via the "spot-check against fuller history,
  not just the rolling list" rule and swapped for two fresh stories (Microsoft's
  "Project Perception" and Fireworks AI's $1.505B raise) via a quick
  supplementary web search before posting — same pattern as past runs that
  needed a fresh pick mid-curation. **No same-day cross-source collisions**
  today: HN's, GitHub's, HF's, and X's final picks were checked against each
  other and don't overlap. **GitHub Trending's agent-tooling skew continues**:
  4 of 5 final picks (cua, AstrBot, jcode, plus WrenAI's framework angle) are
  agent/dev-tooling flavored — reported honestly per the standing default;
  voicebox (the day's biggest star-delta, +629) and WrenAI are the two picks a
  non-developer would find immediately useful. elder-plinius/G0DM0D3 (07-18's
  open editorial-judgment flag) did not appear on today's trending page at
  all, so no live call was needed. **New methodology question raised**: HN's
  fetch is still fully blocked (news.ycombinator.com returns 403), so today's
  5 picks are search-reconstructed; only 3 of 5 could be confirmed as real HN
  thread IDs, and 2 (Apple overtaking Nvidia as most valuable company, China's
  new WAICO governance bloc) are real, dated, on-topic stories that couldn't
  be verified as actual live HN submissions. Asked Giulia directly whether
  that confidence tier is acceptable to hit 5 solid themes, or whether HN
  should only ever run fully-confirmed thread IDs even if that sometimes means
  fewer than 5. Fetch strategy unchanged otherwise: GitHub Trending fetched
  live via WebFetch on `github.com/trending?since=daily` (spot-checked 2 star
  counts against the live GitHub API, both exact matches, one timestamped
  today), Hugging Face MCP tools worked without restriction.

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

23. **New 2026-07-19**: Hacker News is fully blocked from live access in this
    environment (news.ycombinator.com returns 403), so all of HN's picks are
    search-reconstructed rather than pulled from a live front page. Today, 3
    of 5 picks were confirmed as real HN thread IDs via search, but 2 (Apple
    overtaking Nvidia as the world's most valuable company; China's new WAICO
    AI-governance bloc) are real, dated, on-topic stories from the right news
    window that couldn't be independently verified as an actual live HN
    submission. Specific ask: is it fine for HN to include unconfirmed-but-real
    stories like that to keep a full 5 solid themes, or should HN only ever
    run fully search-confirmed thread IDs, even on days that means posting
    fewer than 5?

24. **New 2026-07-20**: today needed 4 mid-curation swaps across 2 sources
    (HN: Inkling and Hassabis's essay, both longer-gap repeats of stories HN
    or X had already run; X: Alex Turner's resignation and China's WAICO bloc,
    both repeats of HN's own recent picks) — the most in one day so far. Each
    replacement found via supplementary web search was real and on-topic but
    not held to the same confirmation bar as an original pick (2 of HN's
    replacements aren't verified live HN threads; 2 of X's replacements trace
    to stories that broke a week-plus earlier, just not yet covered by this
    routine). Specific ask: should a swapped-in replacement meet the same bar
    as an original pick, or is "real, on-topic, and new to this routine"
    sufficient even when the underlying story isn't brand new? Related
    proposal: brief each source's research agent with all 4 sources' recent
    picks (not just its own) to catch these collisions before research
    finishes instead of after, cutting down on the supplementary-search cycle
    this added today.

25. **Resolved 2026-07-22** (proposed 2026-07-20): briefing each source's
    research agent with all 4 sources' recent picks, not just its own, has
    now caught a real same-day collision cleanly 2 runs in a row (07-21:
    Kimi K3 and Hassabis's essay; 07-22: the Scoble/Anthropic/Physical
    Intelligence rumor) with zero manual supplementary digging needed either
    time. Adopted as the permanent process default and updated in
    `PLAYBOOK.md` rather than re-asking if it's worth keeping.

26. **Resolved 2026-07-23** (proposed 2026-07-22): Thinking Machines Lab's
    "Inkling" surfaced as a stale non-story a 4th time (07-19, 07-20, 07-22,
    07-23) with no real update since 07-14 — adopted the proposed permanent
    silent exclusion per the "default after silence" policy rather than
    re-proposing again.

27. **New 2026-07-23**: the pre-research cross-source briefing (each source
    gets the other 3 sources' *prior-day* picks) can't catch two sources
    independently landing on the *same-day* story, since neither has final
    picks yet when the briefs are written. Caught two such same-day
    collisions today via a manual post-research compare of all 20 picks
    (Jack Dorsey/Block's "Buzz" on GitHub vs. X; the Microsoft-Mistral GPU
    deal on HN vs. X) — resolved by keeping each on its more natural source
    and swapping a fresh story into X both times. Added the manual
    all-4-sources compare as a permanent standing step in `PLAYBOOK.md`
    (alongside, not instead of, the pre-research briefing). Specific ask:
    is "keep it on the more native source, swap the other" the right
    tiebreaker for these, or should same-day collisions like this be flagged
    to Giulia instead of decided unilaterally?

28. **New 2026-07-25**: today's manual all-4-sources compare found zero
    exact-story collisions (first clean day like this in a while), but did
    find a milder pattern not yet explicitly covered by items 9/13: the
    *same company* (Moonshot AI) showing up on two different sources
    (Hugging Face's Kimi-K2.7-Code model release, X's $50B Hong Kong IPO
    plans) via genuinely distinct stories. Kept both, same tiebreaker as
    prior Anthropic/Grok double-mention days (flag rather than swap when the
    underlying stories are actually different). Specific ask: is that the
    right default for same-company-different-story overlaps specifically, or
    should there be a cap (e.g. no company gets covered by more than 2 of the
    4 sources per day) regardless of how distinct the angles are?

29. **New 2026-07-31**: found a variant of the same-entity-overlap question
    (items 18/22/25/28) one step further: GitHub Trending's top pick
    (`NousResearch/hermes-agent`, a "learning loop" agent feature) and
    Hacker News's pick (a security incident where someone ran that same
    open-source Hermes agent unattended inside Thailand's Finance Ministry)
    are the *same tool*, but the two stories aren't just different angles on
    one event — one is a positive feature-launch story, the other is a
    malicious-misuse incident involving the identical piece of software.
    Kept both per the standing "different angle, same entity" precedent.
    Specific ask: is it fine to run a feature/launch story about a tool the
    same day a security incident implicating that exact tool also runs, or
    does the misuse story's presence mean the feature story should get
    swapped out that day specifically, unlike a plain double-mention of a
    company? Also flagging, as prior sessions did with day 40+/45+: this is
    now 46+ days running with confirmed zero text feedback ever received on
    any open question in this file — every stated default above remains
    exactly that, a default, and changes the moment a real reply arrives.

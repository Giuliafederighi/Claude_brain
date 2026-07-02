# daily-ai-news feedback log

Newest entries first. Each entry: date, what ran, any feedback received, what
changed as a result. Keep this file the single place preferences accumulate
— see `CLAUDE.md` for why 17 days of prior runs failed to actually
accumulate anything (every prior PR was an unmerged draft).

## Recently covered, by source (rolling — update each run, drop anything >3 days old)

**Hacker News**: Claude Code steganographic request-tagging controversy,
Anthropic Sonnet 5 launch, Godot banning AI-written contributions,
Anthropic Fable 5 export-ban reversal, "SpudCell" synthetic-cell research
(2026-07-02) · computer-use in cheap models, Anthropic's data-center
outreach, GLM-5.2 as open-agent step change, Fable 5's mid-tier coding
score, "is AI slowing down?" debate (2026-07-01) · local model maturity,
GLM-5.2 open release, Squidbleed vulnerability, Android dev identity
enforcement, GPT-5.5-Cyber (2026-06-23)

**GitHub Trending**: Strix (AI pentesting agents), OmniRoute (multi-model
API gateway), Hermes Agent (self-hosted personal AI assistant), Agency
Agents (pre-built AI persona library), Google's agents-cli (2026-07-02) ·
speculative decoding (DeepSpec), self-learning agent skills, mobile
simulator control, CopilotKit's OpenTag, agentic crypto/digital-humans
(2026-07-01) · OpenMontage agentic video, LLM stock analysis, ByteDance
deer-flow, codebase-memory MCP, agent harness optimizers (2026-06-23)

**Hugging Face**: DeepSeek V4 million-token context models, Meituan's
LongCat-2.0 ("Owl Alpha" reveal), Nvidia LocateAnything-3B, XDOF's open
ABC-130k robot dataset, open-source Fable 5 distillation efforts
(2026-07-02) · Baidu OCR breakout, GLM-5.2 cross-platform buzz, small
reasoning models (Ornith), Qwen's agent world-model, faster image gen
(Krea-2) (2026-07-01) · open-weight rankings, SLMs for agents, Ptah deep
research, embedding model dominance, LTX 2.3 video (2026-06-23)

**X / Twitter**: Claude Sonnet 5 price war, OpenAI's Sol/Terra/Luna naming
meme collision with Solana, Google losing Jumper (to Anthropic) and
Shazeer (to OpenAI), Together AI's $800M raise, AI-linked tech/finance
layoffs data (2026-07-02) · Google's $40B Anthropic stake + Gemini
everywhere, Anthropic vs OpenAI valuation/IPO race, SpaceX-Reflection AI
compute deal, Colorado AI Act enforcement, export-controls-vs-open-weights
standoff (2026-07-01) · AutoScientist challenge, Qualcomm/Tenstorrent
acquisition talk, Reflection AI compute spend, orbital data centers,
physics-aware AI (2026-06-23)

## Entries

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

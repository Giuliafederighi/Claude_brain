# Claude Brain — Daily AI News Routine

## Purpose

This routine runs every day at **8am Brasilia time (BRT / UTC-3)**. It scrapes 4 sources, distills 5 themes from each, and posts them as separate threads to the `#daily-ai-news` Slack channel (`C0BAAEKT6G7`). At the end it sends a feedback request to improve the next run.

---

## Execution Steps (run in order)

### 1. Check for Feedback from Yesterday

Read the last 20 messages in `#daily-ai-news` (`C0BAAEKT6G7`) with `slack_read_channel`. Look for any replies from Giulia (`U0AJKBAQ29H`) responding to the feedback request. If feedback exists, apply it to today's selection and format choices (see **Feedback Loop** section below).

### 2. Scrape All 4 Sources in Parallel

Run these simultaneously:

**Hacker News**
- Try `WebFetch` on `https://news.ycombinator.com/front?day=YYYY-MM-DD` (today's date)
- If 403, use `WebSearch` with query: `"Hacker News front page top stories [Month Day Year]"`
- Fallback: `WebSearch` on recent AI/tech news that the HN community would discuss
- Target: stories with 100+ points, active discussion, signal > noise

**GitHub Trending**
- `WebFetch` on `https://github.com/trending?since=daily`
- Returns: repo name, author, description, language, stars today
- Filter for: AI/ML tools, developer productivity, interesting open-source
- If fetch fails, try `WebSearch`: `"GitHub trending today [date]"`

**Hugging Face**
- Use `mcp__Hugging-Face__paper_search` with a topic query matching today's themes
- Also try `mcp__Hugging-Face__hub_repo_search` with `sort: "trendingScore"` for model trends
- Target: papers with 10+ upvotes, notable models with real-world applications
- If MCP fails, `WebFetch` on `https://huggingface.co/papers`

**X / AI Industry**
- `WebSearch` with query: `"AI artificial intelligence news [Month Day Year]"`
- Supplement with: `"AI startup funding announcement [date]"` and `"AI policy regulation [date]"`
- Target: major model releases, funding rounds, policy moves, industry shifts

### 3. Select 5 Themes Per Source

**Selection criteria:**
- Pick what a smart, non-specialist founder/operator would find genuinely useful
- Prefer: things that change how you think about AI, not just "X released Y"
- Mix: 1-2 technical, 1-2 business/strategic, 1 policy or cultural angle
- Avoid: obvious recap of things already widely covered, jargon without payoff
- Prioritize: stories that explain the "so what" — implications, not just facts

**Format per theme:**
```
*N.* :emoji: _Title — Context in One Line_
2-4 sentences explaining what this is and why it matters. Plain language. No jargon without explanation. End with the implication or the question it raises.
```

Emoji guide by theme type:
- 🔬 research/papers → `:microscope:` or `:brain:`
- 💰 funding/business → `:moneybag:` or `:chart_with_upwards_trend:`
- 🏛️ policy/regulation → `:classical_building:` or `:scales:`
- 🛠️ tools/infra → `:hammer_and_wrench:` or `:zap:`
- 📱 product/consumer → `:iphone:` or `:rocket:`
- ⚠️ risk/safety → `:warning:` or `:red_circle:`
- 🤖 models/AI → `:robot_face:` or `:crystal_ball:`

### 4. Post 4 Source Threads to Slack

Post each source as a **separate top-level message** to `C0BAAEKT6G7`. Each message is its own thread (users can reply to it). Post all 4 in parallel if possible.

**Message format:**

```
:newspaper: _Daily AI News | [Source Name]_ — [Month Day, Year]

[1-line framing sentence about what this source covers today]

*1.* :emoji: _Theme Title — Subcontext_
Explanation in plain language. Why it matters. What it implies.

*2.* ...

*3.* ...

*4.* ...

*5.* ...

_Sources: [source URL] · [date] | This digest is auto-curated daily at 8am BRT_
*Sent using* <@U0AQBNP0JLT|Claude>
```

Source labels:
- `Hacker News`
- `GitHub Trending`
- `Hugging Face Research`
- `X / AI Industry`

### 5. Post Feedback Request

After all 4 threads, send one final message to `C0BAAEKT6G7`:

```
:wave: _Hey Giulia — quick feedback request for today's digest!_

I've posted today's 4 threads above (HN · GitHub · Hugging Face · X/Industry).

To keep improving next session, it'd help to know:
• *Which source had the most useful picks today?* (HN / GitHub / HuggingFace / X)
• *Anything that felt off?* Too technical, too broad, not relevant to what you care about?
• *Any theme you wished I'd included but didn't?*
• *Format feedback?* Length, tone, emoji density, structure — anything to tune?

Reply here or in any of the 4 threads above. Your reply gets baked directly into tomorrow's selection logic. :pray:
*Sent using* <@U0AQBNP0JLT|Claude>
```

### 6. Log the Run

Append to `logs/YYYY-MM-DD.md` with a summary of:
- Which 5 themes were posted per source
- Any feedback received and applied
- Any source fetch failures and what fallback was used

### 7. Commit & Push

Commit the log file to branch `claude/bold-knuth-w7gsls` with message `"log: daily digest YYYY-MM-DD"` and push. Create a PR if one doesn't exist.

---

## Feedback Loop

At the start of each run, scan recent Slack messages from Giulia for feedback. Apply these rules:

| Feedback signal | Action |
|---|---|
| "too technical" | Add more plain-language context, reduce jargon |
| "too obvious" | Push toward more niche/emerging stories, avoid mainstream recap |
| "more research papers" | Weight HuggingFace digest toward arxiv papers, increase upvote threshold |
| "more tooling" | Weight GitHub digest toward practical dev tools over star counts |
| "more policy" | Add a policy/regulation theme to each source where possible |
| Source praised | Pick more stories from that source category |
| Source criticized | Tighten criteria for that source |
| Format feedback | Adjust length/structure as requested |

Store feedback context in `logs/feedback.md` so it accumulates across sessions.

---

## Source Fetch Failures

| Source | Primary | Fallback |
|---|---|---|
| Hacker News | `WebFetch` on `news.ycombinator.com/front?day=DATE` | `WebSearch` "Hacker News top stories [date]" |
| GitHub Trending | `WebFetch` on `github.com/trending?since=daily` | `WebSearch` "GitHub trending [date]" |
| Hugging Face | `mcp__Hugging-Face__paper_search` + `hub_repo_search` | `WebFetch` on `huggingface.co/papers` |
| X / Industry | `WebSearch` AI news | Multiple targeted `WebSearch` queries |

If a source completely fails after fallbacks, note it in the digest footer and skip that thread.

---

## Tone & Voice

- Natural language, not corporate newsletter
- "Here's what matters and why" — not "Here is a summary of"
- Short paragraphs. No walls of text.
- The reader is a smart, busy founder who reads fast
- Explain jargon the first time, never again
- End each theme with the implication or the open question — not just the fact

---

## Channel Info

- Channel: `#daily-ai-news`
- Channel ID: `C0BAAEKT6G7`
- Workspace: `vetto-ai.slack.com`
- Primary user: Giulia Federighi (`U0AJKBAQ29H`)
- Bot attribution: `<@U0AQBNP0JLT|Claude>`

---

## Run History

| Date | HN | GitHub | HuggingFace | X/Industry | Feedback |
|---|---|---|---|---|---|
| 2026-06-15 | ✅ | ✅ | ✅ | ✅ | None received |
| 2026-06-16 | ✅ | ✅ | ✅ | ✅ | None received |
| 2026-06-17 | ✅ | ✅ | ✅ | ✅ | 💜 reaction (positive) |
| 2026-06-18 | ✅ (web agg) | ✅ | ✅ | ✅ | Pending |

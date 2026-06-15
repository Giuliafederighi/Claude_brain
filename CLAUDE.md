# Claude Brain — Routine Instructions

This repository holds the living instructions for Claude's scheduled routines.
Claude reads this file at the start of each run and follows the instructions below.
Instructions grow over time as the user provides feedback — after every run, add at least one new question to the Open Questions section based on what you observed.

---

## Active Routines

### 1. HackerNews Morning Brief

**Schedule:** Daily at 8am  
**Slack channel:** `#daily-ai-news` (ID: `C0BAAEKT6G7`) — post ONLY here, nowhere else  
**Source:** https://news.ycombinator.com/news (direct access is blocked in this environment — use the data source below)  
**Data source:** GitHub issue tracker at `github.com/luoyunchong/actions`

#### Fetching today's stories

Direct access to news.ycombinator.com and hn.algolia.com is blocked (WebFetch returns 403, curl returns host-not-in-allowlist). Use this workaround instead:

1. Find today's issue number. The issue is titled `Hacker News Daily Top 10 YYYY-MM-DD`. As of 2026-06-15, the issue number is **#728**. Each day increments by 1. Compute today's number as: `728 + (days since 2026-06-15)`.

2. Fetch the issue content via WebFetch:  
   `https://github.com/luoyunchong/actions/issues/[NUMBER]`  
   If the number is off, search first:  
   `https://github.com/luoyunchong/actions/issues?q=Hacker+News+Daily+Top+10+[YYYY-MM-DD]`

#### What to do each run

1. Fetch today's top 10 HN stories using the method above.

2. Group stories into themes — pick only the themes that actually apply today. Don't force a story into a theme that doesn't fit. Suggested themes:
   - 💰 Business & Ambition
   - 🤖 AI & Machine Learning
   - 🛠️ Tools & Open Source
   - 🔒 Security & Privacy
   - 📹 Personal Projects & Maker
   - 🐧 Linux & Systems
   - 😤 Tech Frustration of the Day
   - 📼 Throwback Worth Reading
   - 🔬 Science & Research
   - 💼 Work & Career

3. Write each theme section in **natural, conversational language** — brief a smart colleague who doesn't want to read 30 links. One short paragraph per story (2–4 sentences max). Always include the link and point/comment counts.

4. Send to `#daily-ai-news` (C0BAAEKT6G7) using `mcp__Slack__slack_send_message`.

5. End the message with:  
   `_Sent by your Claude Code morning brief · Source: Hacker News front page_`  
   `_💬 Reply here to help shape tomorrow's brief — I'm always looking to improve!_`

6. Update `run_log.md`: add today's date, number of stories covered, themes used, and any notable observations.

7. Add at least one new question to the **Open Questions** section below based on what you noticed during the run.

8. Commit and push all changes to branch `claude/keen-archimedes-ow2746`.

#### Format rules
- Slack markdown: `*bold*`, `_italic_`, `•` for bullets
- Dividers: `---` between theme sections, one blank line between stories
- Story format: natural-language summary → `→ [URL] (X pts · Y comments)`
- Target under 3,000 characters total; quality over quantity

---

## Open Questions for the User

These questions are waiting for your answer to improve future runs.
Reply in `#daily-ai-news` or edit this file directly — answered questions move to the section below.

**Q1.** Should the brief cover all top 10 stories each day, or only the ones with the most discussion (e.g., >100 comments)?

**Q2.** Are there specific themes you always want included or always want excluded? (e.g., "skip crypto/blockchain", "always include AI", "always include security")

**Q3.** Should stories include the domain/source name (e.g., `[paulgraham.com]`) so you can judge credibility at a glance?

**Q4.** Do you want a short **TL;DR executive summary** at the very top (3 bullets, one per most important theme of the day)?

**Q5.** Should the routine flag any stories that seem directly relevant to Vetto (your company) with a special note?

**Q6.** Would you like the brief sent as a Slack Canvas instead of a plain message, for easier scrolling and reference later?

---

## Answered Questions

| Question | Answer | Date |
|----------|--------|------|
| Which Slack channel? | `#daily-ai-news` only (C0BAAEKT6G7) — never post anywhere else | 2026-06-15 |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-15 | Initial setup. First run completed. 10 stories, 7 themes. |
| 2026-06-15 | Corrected Slack channel: `#daily-ai-news` (C0BAAEKT6G7), never `#00-updates`. |
| 2026-06-15 | Clarified data source: GitHub issues is primary (not fallback). Direct HN access is blocked. Added issue number formula and search URL. Added growing-instructions principle. |

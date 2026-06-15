# Claude Brain — Routine Instructions

This repository holds the living instructions for Claude's scheduled routines.
Claude reads this file at the start of each run and follows the instructions below.
Instructions grow over time as the user provides feedback.

---

## Active Routines

### 1. HackerNews Morning Brief

**Schedule:** Daily at 8am  
**Slack channel:** `#00-updates` (ID: `C0AGY6WG55K`)  
**Source:** https://news.ycombinator.com/news  
**Data source (fallback):** GitHub issue tracker at `github.com/luoyunchong/actions` — fetch today's "Hacker News Daily Top 10 YYYY-MM-DD" issue via WebFetch  

#### What to do each run

1. Fetch today's top HN stories. Use WebFetch on:  
   `https://github.com/luoyunchong/actions/issues/` — find the issue titled `Hacker News Daily Top 10 YYYY-MM-DD` for today's date and fetch its content.  
   (Issue numbers increment by 1 each day. As of 2026-06-15, issue #728 = that date's brief.)

2. Group stories into themes. Suggested themes (adapt as needed based on what's actually trending):
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

3. Write each theme section in **natural, conversational language** — as if briefing a smart colleague who doesn't want to read 30 links. One short paragraph per story (2-4 sentences max). Always include the link and point/comment counts.

4. Send the message to `#00-updates` using `mcp__Slack__slack_send_message`.

5. End the message with:  
   `_Sent by your Claude Code morning brief · Source: Hacker News front page_`  
   `_💬 Reply here to help shape tomorrow's brief — I'm always looking to improve!_`

6. After sending, update `run_log.md` with today's date, number of stories covered, and any notable observations.

7. After updating run_log.md, commit and push changes to the branch `claude/keen-archimedes-ow2746`.

#### Format rules
- Use Slack's markdown: `*bold*`, `_italic_`, `•` for bullets
- One blank line between theme sections, use `---` as dividers
- Story format: short natural-language summary → `→ [URL] (X pts · Y comments)`
- Keep the whole message under 3,000 characters if possible; prioritize quality over quantity

---

## Open Questions for the User

These questions are waiting for your answer to help improve future runs.
Reply in `#00-updates` or edit this file directly.

**Q1.** Should the brief cover all top 10 stories each day, or only the ones with the most discussion (e.g., >100 comments)?

**Q2.** Are there specific themes you always want included or always want excluded? (e.g., "skip crypto/blockchain", "always include AI", "always include security")

**Q3.** Should stories include the domain/source name (e.g., `[paulgraham.com]`) so you can quickly judge credibility at a glance?

**Q4.** Do you want a short **TL;DR executive summary** at the very top (3 bullets, one per most important theme of the day)?

**Q5.** Should the routine also check if any stories are directly relevant to Vetto (your company) and flag them with a special note?

**Q6.** Would you like the brief sent as a Slack Canvas instead of a plain message, so it's easier to scroll and reference later?

---

## Answered Questions

*(Move answered questions here with the user's response)*

None yet.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-15 | Initial setup. First run completed. 10 stories, 7 themes. |

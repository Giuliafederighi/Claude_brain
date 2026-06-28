# Daily AI News — Cron Prompt

This file is the source of truth for the daily routine. Edit it to change curation behavior.
The cron job reads this and incorporates accumulated feedback from feedback.md.

---

## ROUTINE INSTRUCTIONS

You are running the daily AI news digest for #daily-ai-news (Slack channel C0BAAEKT6G7).

### Step 0 — Setup
1. Get today's date: run `date +"%B %d, %Y"` in Bash
2. Read `/home/user/Claude_brain/routines/daily-ai-news/feedback.md` — use any guidelines and past feedback to improve story selection today
3. Check Slack channel C0BAAEKT6G7 for any recent replies to the feedback message from yesterday (use mcp__Slack__slack_read_channel, limit 20). If feedback from user U0AJKBAQ29H is found, append it to the feedback.md file with today's date, then `git add`, `git commit -m "feedback: {date}"`, `git push origin claude/bold-knuth-nd1qtw` so it persists.

### Step 1 — Hacker News

Fetch today's HN stories using WebSearch:
- Query 1: `site:news.ycombinator.com top stories {today_date} technology AI programming`
- Query 2: `hacker news front page {today_date} most upvoted`

Select 5 stories that are most interesting for a tech/AI audience. Prioritize:
- Things that explain something new, counterintuitive, or have broad impact
- Technical tools or findings with real-world consequences
- Stories non-engineers can also appreciate
- Avoid: pure job listings, pure "Ask HN" threads unless exceptional

Post to C0BAAEKT6G7:
- **Main message**: `[HN] 🗞️ *Hacker News Top Picks · {date}*\nToday's most interesting stories from the HN frontpage.`
- **5 thread replies** (use thread_ts from main message): For each story: **Bold Title** + 2-3 sentences explaining WHY it matters in plain conversational language. Include the link. Do not just describe what it is — explain the implication.

### Step 2 — GitHub Trending

Fetch via WebFetch: `https://github.com/trending`
Prompt: "List the top 15 trending repos with name, description, stars today, and programming language."

Select 5 repos most relevant to: AI tools, developer infrastructure, interesting tech, open-source projects with real utility.

Post to C0BAAEKT6G7:
- **Main message**: `[GH] ⭐ *GitHub Trending · {date}*\nFive repos developers are excited about today.`
- **5 thread replies**: **repo/name** (stars gained today) + why it's interesting and what problem it solves. Include github.com link.

### Step 3 — HuggingFace AI Papers

Use `mcp__Hugging-Face__paper_search` with 2-3 different queries to get a varied set of recent papers. Good queries:
- `"multimodal reasoning vision language 2026"`
- `"AI agents efficiency training 2026"`  
- `"safety alignment evaluation LLM 2026"`

Prefer papers with: publication date in the last 14 days, upvotes > 5, clear practical implications.
Select 5 diverse papers (not all from the same subfield).

Post to C0BAAEKT6G7:
- **Main message**: `[HF] 🤗 *HuggingFace AI Papers · {date}*\nFive research findings worth knowing about this week.`
- **5 thread replies**: **Paper Title** + plain-language explanation of the finding and why it matters to practitioners. Include hf.co link.

### Step 4 — X/Twitter AI Buzz

Use WebSearch with queries:
- `AI machine learning trending Twitter X today {date}`
- `AI news announcement discussion site:x.com {date}`
- `artificial intelligence viral discussion {month} {year}`

Select 5 significant AI conversations, announcements, or debates circulating on X.
Prefer: things with real debate or implications, not just PR announcements.

Post to C0BAAEKT6G7:
- **Main message**: `[X] 🐦 *X/Twitter AI Buzz · {date}*\nWhat the AI community is talking about today.`
- **5 thread replies**: **Topic** + 2-3 sentences on what's being discussed and why it matters.

### Step 5 — Feedback Request

Post to C0BAAEKT6G7 (NOT as a thread reply — as a new channel message):

```
📊 *Today's AI Digest is live!* 4 threads above — HN, GitHub, HuggingFace, and X.

How did today's selection land?
• Which topics resonated most?
• Anything that felt off-topic or low-value?
• Important stories I missed?

Reply here — your feedback shapes tomorrow's curation. This digest runs every morning at 8am Brasília time 🇧🇷
```

---

## FORMAT GUIDE

- Write in natural, engaging language — like explaining to a smart colleague over coffee
- Explain WHY things matter, not just WHAT they are
- Each story should be readable in 30 seconds
- Use **bold** for story titles
- Include links where possible
- Avoid excessive jargon; if you use a technical term, briefly explain it

## SELECTION PRINCIPLES (updated from feedback)

See feedback.md for evolving guidelines based on user feedback.
Default principles:
- At least 1 story per digest should be understandable by non-engineers
- Prefer stories with consequences over pure announcements
- Diversity of topics within each source (don't pick 5 LLM papers, pick across subfields)
- Recency matters: prefer news from the last 24-48 hours when possible

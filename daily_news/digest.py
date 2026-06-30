#!/usr/bin/env python3
"""
Daily AI News Digest
Fetches from HN, GitHub Trending, HuggingFace, and AI community sources,
posts 5 themed plain-English summaries per source to Slack as threaded messages.

Sources:
  - Hacker News       → HN Algolia API
  - GitHub Trending   → github.com/trending (HTML)
  - HuggingFace       → daily papers + trending models APIs
  - X / Community     → Reddit AI subreddits (public JSON; X API not available)

Required env vars:
  ANTHROPIC_API_KEY   Claude API key for summarisation
  SLACK_BOT_TOKEN     Bot OAuth token (scopes: chat:write, channels:history,
                      im:write, im:history, channels:join)
  SLACK_CHANNEL_ID    ID of the #daily-ai-news channel
  SLACK_USER_ID       (optional) Your Slack user ID for DM feedback requests
"""
import json
import os
import sys
import time
import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup
import anthropic
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# ── Constants ──────────────────────────────────────────────────────────────

PREFS_FILE = Path(__file__).parent / "preferences.json"
TODAY = datetime.date.today().strftime("%B %d, %Y")

SOURCE_EMOJI = {
    "Hacker News":     "🟠",
    "GitHub Trending": "🐙",
    "HuggingFace":     "🤗",
    "X / Community":   "🌐",
}

# ── Preferences ────────────────────────────────────────────────────────────

def load_prefs() -> dict:
    with open(PREFS_FILE) as f:
        return json.load(f)

def save_prefs(prefs: dict):
    with open(PREFS_FILE, "w") as f:
        json.dump(prefs, f, indent=2)

# ── Fetchers ───────────────────────────────────────────────────────────────

def fetch_hackernews() -> list:
    resp = requests.get(
        "https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=30",
        timeout=15,
    )
    resp.raise_for_status()
    return [
        {
            "title": h.get("title", ""),
            "url": h.get("url", ""),
            "points": h.get("points", 0),
            "comments": h.get("num_comments", 0),
        }
        for h in resp.json()["hits"]
    ]


def fetch_github_trending() -> list:
    resp = requests.get(
        "https://github.com/trending",
        headers={"User-Agent": "Mozilla/5.0 (compatible; ClaudeBrain/1.0)"},
        timeout=15,
    )
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    repos = []
    for article in soup.select("article.Box-row")[:25]:
        name_el = article.select_one("h2 a")
        desc_el = article.select_one("p")
        stars_el = article.select_one("a[href*='stargazers']")
        lang_el = article.select_one("[itemprop='programmingLanguage']")
        if not name_el:
            continue
        path = name_el.get("href", "").strip()
        repos.append({
            "name": path.lstrip("/"),
            "url": f"https://github.com{path}",
            "description": desc_el.get_text(strip=True) if desc_el else "",
            "stars": stars_el.get_text(strip=True) if stars_el else "",
            "language": lang_el.get_text(strip=True) if lang_el else "",
        })
    return repos


def fetch_huggingface() -> list:
    items = []

    # Daily papers
    try:
        resp = requests.get("https://huggingface.co/api/daily_papers", timeout=15)
        if resp.ok:
            for entry in resp.json()[:15]:
                paper = entry.get("paper", entry)
                items.append({
                    "type": "paper",
                    "title": paper.get("title", ""),
                    "abstract": paper.get("summary", "")[:400],
                    "url": f"https://huggingface.co/papers/{paper.get('id', '')}",
                })
    except Exception as e:
        print(f"  HF papers: {e}")

    # Trending models
    try:
        resp2 = requests.get(
            "https://huggingface.co/api/models?sort=trending&limit=15",
            timeout=15,
        )
        if resp2.ok:
            for m in resp2.json():
                items.append({
                    "type": "model",
                    "title": m.get("id", ""),
                    "tags": (m.get("tags") or [])[:6],
                    "url": f"https://huggingface.co/{m.get('id', '')}",
                    "downloads": m.get("downloads", 0),
                })
    except Exception as e:
        print(f"  HF models: {e}")

    return items


def fetch_community_news() -> list:
    """
    Reddit AI subreddits as a proxy for community/social sentiment.
    X (Twitter) native scraping requires their API; this covers the same
    AI community conversation via public Reddit JSON.
    """
    subreddits = "MachineLearning+artificial+LocalLLaMA+singularity+OpenAI"
    try:
        resp = requests.get(
            f"https://www.reddit.com/r/{subreddits}/hot.json?limit=30",
            headers={"User-Agent": "ClaudeBrain/1.0 (daily AI digest)"},
            timeout=15,
        )
        resp.raise_for_status()
        posts = []
        for child in resp.json()["data"]["children"]:
            d = child["data"]
            posts.append({
                "title": d.get("title", ""),
                "url": d.get("url", ""),
                "score": d.get("score", 0),
                "subreddit": f"r/{d.get('subreddit', '')}",
                "text_preview": d.get("selftext", "")[:200],
            })
        return posts
    except Exception as e:
        print(f"  Reddit: {e}")
        return []


# ── Claude summariser ──────────────────────────────────────────────────────

def summarize(source_name: str, items: list, prefs: dict) -> list:
    client = anthropic.Anthropic()

    focus = ", ".join(prefs.get("focus_areas", []))
    style = prefs.get("style_notes", "")
    avoid = ", ".join(prefs.get("avoid", [])) or "nothing specific"

    feedback_ctx = ""
    history = prefs.get("feedback_history", [])
    if history:
        recent_feedback = history[-1].get("feedback", "")
        if recent_feedback:
            feedback_ctx = f"\n\nUser feedback from previous digest to incorporate:\n{recent_feedback}\n"

    prompt = f"""You are curating the daily AI/tech news digest from {source_name}.

Focus areas: {focus}
Avoid: {avoid}
Writing style: {style}{feedback_ctx}

Items fetched today from {source_name}:
{json.dumps(items, indent=2)[:6000]}

Select and explain the 5 most interesting, significant, or conversation-worthy items.
Write as if briefing a smart, curious colleague who isn't deeply technical — natural, engaging, no jargon without explanation.

Return ONLY a valid JSON array (no markdown fences, no commentary before or after):
[
  {{
    "title": "Catchy 5-8 word title",
    "explanation": "3-4 sentences of engaging plain-English explanation with context and what makes it notable.",
    "why_it_matters": "One sentence on the broader significance."
  }}
]"""

    message = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    )

    text = message.content[0].text.strip()
    start = text.find("[")
    end = text.rfind("]") + 1
    return json.loads(text[start:end])


# ── Feedback handling ──────────────────────────────────────────────────────

def read_recent_feedback(channel_id: str, user_id: str) -> str:
    """Collect recent human messages from the channel and DMs as feedback."""
    slack = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    msgs = []
    cutoff = str((datetime.datetime.now() - datetime.timedelta(hours=36)).timestamp())

    # DM with user
    if user_id:
        try:
            resp = slack.conversations_history(channel=user_id, oldest=cutoff, limit=20)
            for m in resp["messages"]:
                if m.get("type") == "message" and not m.get("bot_id"):
                    msgs.append(m["text"])
        except SlackApiError:
            pass

    # Channel messages
    try:
        resp = slack.conversations_history(channel=channel_id, oldest=cutoff, limit=40)
        for m in resp["messages"]:
            if m.get("type") == "message" and not m.get("bot_id") and len(m.get("text", "")) > 20:
                msgs.append(m["text"])
    except SlackApiError:
        pass

    return "\n---\n".join(msgs[:8])


def update_prefs_from_feedback(prefs: dict, feedback: str) -> dict:
    if not feedback or len(feedback.strip()) < 15:
        return prefs

    client = anthropic.Anthropic()
    prompt = f"""Current digest preferences:
{json.dumps(prefs, indent=2)}

Recent user feedback messages:
{feedback}

Update the preferences to reflect this feedback:
- Adjust focus_areas if they want more/less of certain topics
- Update style_notes if they want a different tone or depth
- Add to avoid list if they disliked certain topics
- Keep feedback_history untouched (we handle that separately)

Return ONLY the updated JSON object (no markdown, no commentary)."""

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=800,
        messages=[{"role": "user", "content": prompt}]
    )

    text = message.content[0].text.strip()
    start = text.find("{")
    end = text.rfind("}") + 1
    if start == -1:
        return prefs

    new_prefs = json.loads(text[start:end])
    new_prefs["feedback_history"] = prefs.get("feedback_history", [])
    return new_prefs


# ── Slack posting ──────────────────────────────────────────────────────────

def post_source_digest(channel_id: str, source_name: str, themes: list) -> str:
    """Post header to channel, each theme as a thread reply. Returns thread_ts."""
    slack = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    emoji = SOURCE_EMOJI.get(source_name, "📰")

    header = f"{emoji} *Daily AI Digest — {source_name}* | {TODAY}"
    resp = slack.chat_postMessage(channel=channel_id, text=header)
    thread_ts = resp["ts"]

    for i, theme in enumerate(themes, 1):
        body = (
            f"*{i}. {theme['title']}*\n\n"
            f"{theme['explanation']}\n\n"
            f"💡 *Why it matters:* {theme['why_it_matters']}"
        )
        slack.chat_postMessage(channel=channel_id, text=body, thread_ts=thread_ts)
        time.sleep(0.4)

    return thread_ts


def post_feedback_request(channel_id: str, user_id: str):
    slack = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    text = (
        f"👋 *Was today's digest useful? ({TODAY})*\n\n"
        "Reply here (or in our DM) to shape tomorrow's:\n"
        "• ✅ Topics that were interesting / relevant\n"
        "• ❌ Topics to drop or dial back\n"
        "• 💬 Anything you'd love to see covered\n\n"
        "_I'll read this before tomorrow's run and adjust automatically._"
    )
    target = user_id if user_id else channel_id
    try:
        slack.chat_postMessage(channel=target, text=text)
    except SlackApiError:
        slack.chat_postMessage(channel=channel_id, text=text)


def join_channel(channel_id: str):
    """Bot must be in the channel to post."""
    slack = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    try:
        slack.conversations_join(channel=channel_id)
    except SlackApiError:
        pass  # Already a member, or private channel


# ── Main ───────────────────────────────────────────────────────────────────

SOURCES = [
    ("Hacker News",     fetch_hackernews),
    ("GitHub Trending", fetch_github_trending),
    ("HuggingFace",     fetch_huggingface),
    ("X / Community",   fetch_community_news),
]


def main():
    channel_id = os.environ["SLACK_CHANNEL_ID"]
    user_id = os.environ.get("SLACK_USER_ID", "")

    join_channel(channel_id)
    prefs = load_prefs()

    # Read and incorporate any feedback from the past 36 hours
    print("Reading recent feedback...")
    feedback = read_recent_feedback(channel_id, user_id)
    if feedback:
        print(f"  Found feedback ({len(feedback)} chars), updating preferences...")
        prefs = update_prefs_from_feedback(prefs, feedback)
        prefs.setdefault("feedback_history", []).append({
            "date": TODAY,
            "feedback": feedback[:400],
        })
        prefs["feedback_history"] = prefs["feedback_history"][-5:]
        save_prefs(prefs)
        print("  Preferences updated.")

    # Run all sources
    for source_name, fetcher in SOURCES:
        print(f"\n── {source_name}")
        try:
            items = fetcher()
            print(f"  {len(items)} items fetched")
            themes = summarize(source_name, items, prefs)
            print(f"  {len(themes)} themes generated")
            post_source_digest(channel_id, source_name, themes)
            print("  Posted ✓")
        except Exception as e:
            print(f"  ERROR: {e}", file=sys.stderr)
        time.sleep(1)

    # Feedback prompt
    post_feedback_request(channel_id, user_id)
    print("\nDone. Feedback request sent.")


if __name__ == "__main__":
    main()

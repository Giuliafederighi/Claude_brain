# Claude_brain — session startup instructions

This repo is the durable memory for scheduled routines run against it. If you
are a triggered session and the task is about the daily AI news digest, **do
not re-derive the routine from scratch** — read `daily-ai-news/PLAYBOOK.md`
first, it is the single source of truth.

## Critical: this repo only works if `main` actually accumulates state

As of 2026-07-02, seventeen consecutive daily sessions (PRs #1–#17) each
reinvented this routine independently because every prior PR was opened as a
draft and **never merged** — `main` still only had a one-line README. Each
day's session had no memory of the day before, which produced three
different message formats and zero verified feedback incorporation in 12
days of runs. PR #18 (this one) consolidates all of that into
`daily-ai-news/PLAYBOOK.md` and `daily-ai-news/feedback-log.md`, merged
directly to `main`.

**For every future run: before opening a new branch/PR, run
`list_pull_requests` filtered to this repo and check for an existing open PR
from this routine.** These are docs-only, low-risk changes — merge your
update directly into `main` (or into the existing open PR's branch) rather
than adding yet another parallel draft to a backlog no one is clearing. If a
change feels risky enough to want human review first, say so explicitly in
the PR body and ping Giulia, but the default should be: merge and move on,
so the next run inherits your work.

## What to do each run

Full detail lives in `daily-ai-news/PLAYBOOK.md`. Summary:

1. Read `daily-ai-news/PLAYBOOK.md` and `daily-ai-news/feedback-log.md`.
2. Check the previous day's feedback-request thread in `#daily-ai-news`
   (`slack_read_thread`, not just `slack_read_channel` — thread replies are
   invisible to the channel-level read, which is how prior runs missed any
   real feedback) for a reply from Giulia. Fold anything she said into the
   playbook before curating today's picks.
3. Curate 5 themes per source (Hacker News, GitHub Trending, Hugging Face,
   X/Twitter) per the format in the playbook.
4. Post to the private Slack channel `#daily-ai-news` (`C0BAAEKT6G7`).
5. Post a feedback-request reply in each thread, asking a specific,
   answerable question — not just "how was it?".
6. Append a dated entry to `daily-ai-news/feedback-log.md` (what ran, any
   issues, any feedback received) and merge it to `main`.

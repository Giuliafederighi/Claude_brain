# Claude Brain

A living instruction set for Claude's scheduled routines.

## Routines

- **HackerNews Morning Brief** — daily at 8am, posts a themed summary of HN top stories to `#00-updates` on Slack

## How it works

Claude reads `CLAUDE.md` at the start of each scheduled run and follows the instructions inside.
The instructions grow over time — open questions are tracked in `CLAUDE.md` and answered questions move to the changelog.

To shape how the brief works, reply in `#00-updates` or edit `CLAUDE.md` directly.
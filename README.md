# Dev Events Radar Archive

Static archive of Dev Events Radar digests, served by GitHub Pages from the `main` branch root.

Live dashboard: https://dhanpraja231.github.io/dev-events-radar/ (renders `data/events.json`). Past digests: `archive.html`.

Daily runs follow **RUNBOOK.md**; the scheduled-task prompt is **DAILY_PROMPT.md**.

## Adding a new digest
1. Create `digests/YYYY-MM-DD.html` (copy an existing digest page; no email addresses).
2. Add a line at the top of the list in `archive.html`, below the `<!-- DIGESTS -->` comment.
3. Commit and push. Events themselves live in `data/events.json`, which the dashboard reads.

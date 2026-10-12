# Dev Events Radar Archive

Static archive of Dev Events Radar digests, served by GitHub Pages from the `main` branch root.

## Adding a new digest
1. Create `digests/YYYY-MM-DD.html` (copy an existing digest file for the header/footer and paste the digest's HTML body in between). Remove any email addresses.
2. In `index.html`, add one line at the **top** of the list, just below the `<!-- DIGESTS -->` comment:
   `<li><a href="digests/YYYY-MM-DD.html">Mon D, YYYY</a> — short counts summary</li>`
3. Commit and push to `main`. Pages redeploys in about a minute.

## Incremental runs (use the stored data)
Future runs should NOT research from scratch:
1. Load `data/events.json` first (every event seen so far, with `first_seen`/`last_seen`) and `data/series-checked.json` (recurring series and whether a six-city edition is known).
2. Run only incremental searches: new events, plus re-checks of known events whose dates/venues may have changed, and series marked `false` that might since have announced an edition.
3. In the email, mark events not already in `events.json` as **NEW**.
4. Drop events whose `end_date` has passed from the email (keep them in `events.json` for history).
5. Update `events.json` (add new events, update `last_seen` and changed fields, set `cfp_deadline` when known) and `series-checked.json`, then add the day's `digests/YYYY-MM-DD.html` page and index entry (suffix `-1`, `-2` for extra runs on the same day) and push.

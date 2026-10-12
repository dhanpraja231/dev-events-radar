# Dev Events Radar — Daily Runbook

The repo is the memory. `data/events.json` is the single source of truth; don't research from scratch.

## Files
- `data/events.json`: events with `id, name, start_date, end_date, city, venue, tier (flagship|regular), topics[], description, url, cfp_deadline, first_seen, last_seen, link_status (ok|fixed|broken|uncertain), link_checked, date_verified`.
- `data/series-checked.json`: 25 recurring series with `edition_in_six_cities_known`, `notes`, `last_checked`, `rotation_day` (0=Mon … 6=Sun).
- `data/meta.json`: `last_updated` (ISO, IST) and `last_full_link_check`.
- `scripts/linkcheck.py`: cheap HTTP checker that updates link fields.
- `index.html`: dashboard (renders events.json client-side). `archive.html` + `digests/`: past digests.

## Daily procedure (today = date in Asia/Kolkata)
a. **Load** `data/events.json` and `data/series-checked.json`.
b. **Incremental discovery, keeping it small:**
   - Fetch the Luma city pages: lu.ma/chennai, lu.ma/bengaluru, lu.ma/dubai, lu.ma/mumbai, lu.ma/hyderabad, lu.ma/singapore.
   - Check only the series whose `rotation_day` == today's weekday (about 4/day, so all 25 are covered weekly). Search `"<series> 2026 <city>"`, update `notes`, `edition_in_six_cities_known` and `last_checked`.
   - Run 2–4 rotating generic queries (e.g. `<city> tech meetup <next month> 2026`), with a different city/topic each day.
   - Add only events not already present (match by id or by name and date). Set `first_seen=last_seen=today`, `date_verified=today`, and `link_status` from the checker.
c. **Re-verify sparingly** (WebSearch/WebFetch only for these):
   - flagship events starting within 14 days, or with `date_verified` older than 7 days;
   - regular events with `date_verified` older than 14 days;
   - any event with `link_status=broken` (find the official or Luma URL and set `fixed`; if nothing is found, keep `broken` and leave it out of the email).
   - Update dates/venue if they changed (note changes in the commit message) and set `date_verified=today`.
   - Run `python3 scripts/linkcheck.py` daily on all upcoming links. It's plain HTTP with no LLM; only broken ones go into step c.
d. **Drop past events** from the email and dashboard (`end_date < today`). Keep them in the JSON for history.
e. **Update and publish:**
   - Set `last_seen=today` for every event still upcoming and in window.
   - Update `meta.json.last_updated`.
   - Write `digests/YYYY-MM-DD.html` (suffix `-1`, `-2` for extra runs) and add a line to the top of the list in `archive.html`.
   - `git commit` and `git push`.
   - Send the email digest. Mark **NEW** for events whose `first_seen` is today or within the last 3 days, and link the dashboard.

Windows: flagship events up to 90 days out (Mumbai/Hyderabad/Singapore flagship up to 270 days, especially open CFPs); regular events up to 45 days.
Never put email addresses, tokens or secrets in the repo.

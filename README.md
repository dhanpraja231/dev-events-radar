# Dev Events Radar Archive

Static archive of Dev Events Radar digests, served by GitHub Pages from the `main` branch root.

## Adding a new digest
1. Create `digests/YYYY-MM-DD.html` (copy an existing digest file for the header/footer and paste the digest's HTML body in between). Remove any email addresses.
2. In `index.html`, add one line at the **top** of the list, just below the `<!-- DIGESTS -->` comment:
   `<li><a href="digests/YYYY-MM-DD.html">Mon D, YYYY</a> — short counts summary</li>`
3. Commit and push to `main`. Pages redeploys in about a minute.

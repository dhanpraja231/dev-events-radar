# Daily scheduled-task prompt (paste this as the task prompt)

Run end to end without asking questions. You are authorized to send the digest email described below. Today's date and time: run `TZ=Asia/Kolkata date`.

MEMORY: the GitHub repo `dhanpraja231/dev-events-radar` is your memory.
- If `/workspace/dev-events-radar` exists, run `git pull --rebase` in it; otherwise run `git clone https://github.com/dhanpraja231/dev-events-radar.git /workspace/dev-events-radar`.
- Authenticate pushes with the `GH_TOKEN` environment variable, using `gh` (`gh auth setup-git`) or the credential helper. Never print the token or write it into any file.
- Read `RUNBOOK.md` and follow its procedure exactly. Start from `data/events.json` and run only incremental work; don't redo full research.

SCOPE
- Cities: Chennai, Bangalore/Bengaluru and Dubai, events of ANY size (conferences, meetups, summits, hackathons). Mumbai, Hyderabad and Singapore, ONLY big/major events (flagship brands, roughly 500+ attendees, or backed by major orgs such as AWS, Google, Microsoft, Linux Foundation or YC).
- Topics: dev tools, cloud/infra, DevOps, AI/ML/agents, open source, startups, founders/VC, product, general tech conferences. Skip non-tech.
- Windows:
  - Flagship/huge events (KubeCon, AWS Summit/re:Invent, Google Cloud Next, MS Build/Ignite, GitHub Universe, DockerCon, HashiConf, React Nexus, AgentCon-scale AI conferences, large demo days): up to 90 days out.
  - Mumbai/Hyderabad/Singapore flagship events: up to 270 days out, especially with open CFPs.
  - Smaller/regular events: up to 45 days out.
- Every listed event needs a verified date in its window and a working link (link_status ok or fixed).

STEPS
1. Load data and run incremental discovery as RUNBOOK.md describes: the Luma city pages, today's rotating series from `data/series-checked.json`, and a few rotating generic queries.
2. Re-verify only the events that are due under RUNBOOK.md, run `python3 scripts/linkcheck.py`, and fix broken links with WebSearch.
3. Update `data/events.json`, `data/series-checked.json` and `data/meta.json`, add today's `digests/YYYY-MM-DD.html` and its `archive.html` entry, then commit ("Daily update YYYY-MM-DD: +N new, M changed") and push to `main`.
4. Email the digest with the Gmail connector (namespace user-Gmail, tool send_message; check its schema first):
   - To: dhanpraja231@gmail.com ONLY. The full recipient list will be added later.
   - Subject: `Dev Events Radar — <Mon D, YYYY> — Chennai/Bangalore/Dubai/Mumbai/Hyderabad/Singapore`
   - Body: HTML plus a plain-text fallback, laid out as follows:
     - Near the top: "Live dashboard: https://dhanpraja231.github.io/dev-events-radar/" and a single line saying this is a rolling digest in which events reappear until they pass.
     - '🔥 TOP FLAGSHIP EVENTS': all flagship events across the cities, sorted by date.
     - Then the sections Chennai, Bangalore, Dubai, Mumbai (big only), Hyderabad (big only), Singapore (big only), each sorted by date, without repeating flagship events. If a big-only city has none, say so in one line.
     - 'Open CFPs': name, deadline and link, marking any closing within 14 days.
     - Each event appears as: [NEW] Name — Date(s) — Venue/City — one-line description — link. Add NEW when `first_seen` is within the last 3 days.
   - If nothing qualifies, still send a short "no notable events found today" email that includes the dashboard link.
5. Report: the email message id, counts per section, the new events, any date/venue changes, links fixed or still broken, and the commit hash.

<p align="center">
  <img src="icons/icon-512.png" height="100" alt="Ream.st Status icon">
</p>

# Ream.st Status

### *Live status of Ream.st and the Multi.st stream viewers, powered by [GitHup](https://githup.stux.group).*

**Status page:** [status.ream.st](https://status.ream.st)

<!-- A live badge: reads the overall status straight from data/summary.json. -->
[![Ream.st status](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FReam-st%2FStatus%2Fmain%2Fdata%2Fsummary.json&query=%24.status&label=status&style=for-the-badge)](https://status.ream.st)

## Current status

Updated by GitHup whenever the status page is rebuilt (hourly, and when a status changes).

<!-- githup:start -->
<!-- This table is written by GitHup (https://github.com/StuxGroup/GitHup); edits here are overwritten. -->

**All systems operational** · [Live status page](https://status.ream.st/)

| Group | Monitor | Status | Uptime (24 h) | Uptime (7 d) | Uptime (30 d) | Response time (24 h) |
| ----- | ------- | ------ | ------------- | ------------ | ------------- | -------------------- |
| Ream.st | [Ream.st](https://ream.st/) | Up | 100.00% | 100.00% | 99.07% | 988 ms |
| Multi.st | [Multi.st](https://multi.st/) | Up | 100.00% | 100.00% | 99.16% | 808 ms |
| Multi.st | [Multi.st Twitch](https://twitch.multi.st/) | Up | 100.00% | 99.51% | 99.63% | 1309 ms |
| Multi.st | [Multi.st YouTube](https://youtube.multi.st/) | Up | 100.00% | 100.00% | 99.81% | 1326 ms |
| Shared | [Ream.st Media CDN](https://global.media.ream.st/icon.png) | Up | 100.00% | 100.00% | 100.00% | 437 ms |
<!-- githup:end -->

## What's monitored

GitHup checks each monitor in [`.githup.yml`](.githup.yml) regularly. The workflow asks GitHub for a run every 5 minutes, but GitHub runs
schedules best-effort and often less often, so the status page shows the real check rhythm ("checked about every … (last 24 h)"). When a run
is late, it checks up to 4 times, 5 minutes apart, to fill the gap:

- **Ream.st:** the Ream.st website
- **Multi.st:** Multi.st, Multi.st Twitch and Multi.st YouTube
- **Shared:** the Ream.st media CDN

To add a site, add a monitor to the right group there (or a new group). A group can also hold `links:` instead of monitors, for sites that should be listed but not checked.

When a site goes down, GitHup opens an Issue on this repository (labelled `githup`,
`incident`, `status` and the monitor's slug) and closes it with the downtime when it recovers.
To announce planned maintenance, open an Issue yourself with the `githup` and `incident` labels
(plus the monitor's slug to link it); it shows on the status page.

## How it works

- **`.github/workflows/status.yml`** runs a GitHup `check` on a 5-minute schedule, which GitHub runs best-effort (with `fill-gaps`, up to 4 checks when a run is late) and commits the
  results to `data/` as `github-actions[bot]`. When a status changes, hourly, and on pushes, it
  builds the GitHup status page into `_site` (with `site-dir`), and deploys it with `actions/deploy-pages`.
- **`legal:` in `.githup.yml`** makes GitHup generate the **Boring Legal Stuff** hub at `/legal/`
  with its six sub-pages, a themed `404.html`, a `/sitemap/` page, `sitemap.xml` and `robots.txt`
  (the base URL is `site.url`). Nothing is hand-made, and the footer shows only
  **Powered by GitHup**. This repo's own `CHANGELOG.md` and `VERSION.md` are for this repo only.
- **`data/`** is the monitoring history, created by the first check. Don't edit it by hand.
- **The status table above** is written by GitHup's `readme` mode between the
  `<!-- githup:start -->` and `<!-- githup:end -->` markers. Don't edit inside them.

## Local development

```bash
./dev-server.sh                 # or dev-server.bat on Windows; add a port as the last argument
./dev-server.sh --no-dev-mode   # production rendering
```

`dev-server` generates 90 days of example data, builds the status page into `.dev/public` with
`DEV_MODE` on, with its legal pages, 404 and sitemap, and serves it at
`http://127.0.0.1:8000`. It uses GitHup from `$GITHUP_PATH`, a sibling `../GitHup` checkout, or
a fresh clone in `.dev/GitHup`.

## Hosting

GitHub Pages, deployed by Actions (**Settings → Pages → Source: GitHub Actions**), with the custom
domain `status.ream.st` set in the Pages settings. DNS: a `CNAME` record for `status` pointing
at `ream-st.github.io`. The repository is public, so the page's live refresh can read
`data/summary.json` straight from GitHub.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Versioning

This project uses [Date Versioning](https://datevers.ing): each release is numbered by its UTC release date as `YY.MM.DD` (for example `26.10.23`), with `-1`, `-2`… for later releases the same day. See [CHANGELOG.md](CHANGELOG.md) for what changed in each release.

## License

&copy; 2026 Stux.Group. All rights reserved. This repository is not licensed for reuse or
redistribution, see [LICENSE](LICENSE).

---

*Powering the Stux.Group Ecosystem | Part of the Stux.Group Brand of Companies.*

*Built & Maintained by <img src="https://global.media.ream.st/icon.png" height="14" alt="Ream.st" valign="middle"> [Ream.st](https://github.com/Ream-st), powered by [GitHup](https://githup.stux.group).*

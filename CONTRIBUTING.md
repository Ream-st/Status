<p align="center">
  <img src="https://global.media.ream.st/logo.png" height="80" alt="Ream.st Logo">
</p>

# Contributing to Status

Status is Ream.st's status page, [status.ream.st](https://status.ream.st), built with
[GitHup](https://githup.stux.group). To report an outage, open an Issue. Bugs or ideas for the
status page software belong in [StuxGroup/GitHup](https://github.com/StuxGroup/GitHup/issues).

## Local setup

You need Python 3.11+ and nothing else.

```bash
./dev-server.sh [--no-dev-mode] [--lan] [port]   # or dev-server.bat on Windows
```

`--lan` serves it on `0.0.0.0` instead of `127.0.0.1`, so a phone or another device on your network can open
it, and prints the addresses to open (usually the `192.168.x.x` one).

## Project conventions

- **Monitors live in `.githup.yml`.** Its syntax is documented in the
  [GitHup docs](https://githup.stux.group/docs/). Only add sites Ream.st runs.
- **The status page itself is GitHup's**, including the legal pages and 404. Change how it
  looks or works in GitHup, not here.
- **Brand.** The Ream.st accent is `#0044FF`, set as `site.accent`.
- **Legal pages.** The `legal:` block in `.githup.yml` drives **Boring Legal Stuff** at `/legal/`.
  Keep it accurate.
- **Don't edit `data/` by hand.** It belongs to GitHup and the workflow.

## Branches and going live

- **`main` is what's live.** Nothing is pushed to it directly: it only changes when a pull request from `staging` is merged. The page is only rebuilt from `main`. GitHup's own data and README commits still go straight to `main` by themselves, so `main` runs ahead of `staging` and `test` with bot-only commits.
- **`staging` is the last check before live.** It only changes when a pull request from `test` is merged.
- **Work happens on `test`**, or on a feature branch off `test` that's merged back into it. Releases are made on `test` too; `commit.sh` / `commit.bat` refuse to run on `staging` or `main`.
- **Going live:** push `test` with its tag, open a pull request into staging (`gh pr create --base staging --head test`), check staging once it's merged, then open one from staging into main (`gh pr create --base main --head staging`). Leo reviews and merges both, with merge commits, so the release tags made on `test` stay in `staging`'s and `main`'s history.

## Icons

The page's logo and favicon set in `icons/` are its own badge icon: the Ream.st mark on a round avatar with a
heartbeat badge. To rebuild them (needs Pillow), from the repo root, with the Website repo beside this one:

```sh
python -I scripts/badge-icons.py ream-st ../Website/public/assets/icon.png <temp dir> --size=512
python -I scripts/favicon-set.py <temp dir>/ream-st-status.png icons
```

## Versioning

This project uses [Date Versioning](https://datevers.ing). To release:

1. Add a `## vYY.MM.DD` entry at the top of `CHANGELOG.md`, with its sections in this order: Added, Changed, Fixed, Removed, Security, Deprecated.
2. Set `VERSION.md` to the same bare version (no `v`): today's **UTC** date as `YY.MM.DD`, or `YY.MM.DD-1`, `-2`… for later releases the same UTC day. Never a future date. Use UTC, not local time: just after midnight in the UK it is still the previous day in UTC.
3. Run `bash tests/version.sh`.
4. Run `./commit.sh` (or `commit.bat` on Windows). It checks the version, commits and tags `vYY.MM.DD`, and never pushes. It refuses to run on `main` or `staging`.
   Then push with `git push origin test --tags` and open a pull request from `test` into `staging`;
   once that's merged and checked, open one from `staging` into `main` (see [Branches and going live](#branches-and-going-live)).

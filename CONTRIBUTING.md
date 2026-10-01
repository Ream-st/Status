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
./dev-server.sh [--no-dev-mode] [port]   # or dev-server.bat on Windows
```

## Project conventions

- **Monitors live in `.githup.yml`.** Its syntax is documented in the
  [GitHup docs](https://githup.stux.group/docs/). Only add sites Ream.st runs.
- **The status page itself is GitHup's**, including the legal pages and 404. Change how it
  looks or works in GitHup, not here.
- **Brand.** The Ream.st accent is `#0044FF`, set as `site.accent`.
- **Legal pages.** The `legal:` block in `.githup.yml` drives **Boring Legal Stuff** at `/legal/`.
  Keep it accurate.
- **Don't edit `data/` by hand.** It belongs to GitHup and the workflow.

## Versioning and changelog

- The version lives in `VERSION.md` (a bare version string). Bump it on every release.
- Every release gets a `CHANGELOG.md` entry using `###` subsections in this order: Added,
  Changed, Fixed, Removed, Security, Deprecated. Never a bare bullet list under a version.
- `commit.sh` (bash) and `commit.bat` (Windows) read `VERSION.md`, commit and create the
  annotated `vX.Y.Z` tag. Push with `git push origin main vX.Y.Z`.

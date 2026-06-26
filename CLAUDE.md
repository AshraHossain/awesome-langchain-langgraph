# CLAUDE.md

Guidance for Claude Code (and humans) working in this repository.

## What this is

An "awesome list" directory for the LangChain / LangGraph ecosystem. It is a
**data-driven static site + GitHub README**, not an application. The list of
links is data; the README and web page are *generated* from it.

## The one rule that matters

**`data/resources.json` is the single source of truth.** Never hand-edit the
list inside the `<!-- AUTOGEN -->` markers in `README.md`, and never edit
`site/resources.json` (it's a generated copy). Edit the data file, then
regenerate.

## Common commands

```bash
make install     # pip install -r requirements.txt
make validate    # schema + structural checks on resources.json
make generate    # rewrite README.md's list from the data
make site        # stage resources.json into site/ for the web page
make test        # pytest
make check       # validate + test + README-sync check (CI gate, no network)
make links       # network link-rot check
make serve       # serve the web page at http://localhost:8080
make docker      # build + serve via Docker/nginx
```

## Layout

- `data/resources.json` — the data (edit this).
- `data/schema.json` — JSON Schema contract for the data.
- `scripts/` — `validate.py`, `generate_readme.py`, `build_site.py`, `check_links.py`, shared `lib.py`.
- `site/` — vanilla HTML/CSS/JS searchable page (no build step).
- `tests/` — pytest; `scripts/` is importable via `tests/conftest.py`.
- `.github/workflows/ci.yml` — validate + README-sync + tests + links + docker build.

## When adding/changing resources

1. Edit `data/resources.json`.
2. `make validate && make generate` (regenerating README is required — CI fails otherwise).
3. Commit both the data file and the regenerated `README.md`.

## Conventions

- Descriptions: one sentence, 10–280 chars.
- `official: true` only for first-party `langchain-ai` projects.
- `lifecycle`: subset of `build`, `observe`, `evaluate`, `deploy`.
- Escape all data at the render boundary in `site/app.js` (community input is untrusted).

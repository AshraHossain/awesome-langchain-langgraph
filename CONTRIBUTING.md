# Contributing

Thanks for helping make this the best directory for building AI agents on LangChain & LangGraph! Submissions take about two minutes.

## What belongs here

- **Quality over quantity.** A resource should be genuinely useful to someone building agents.
- **Relevant to the ecosystem.** It should use or directly support LangChain, LangGraph, Deep Agents, or LangSmith.
- **Alive.** Prefer maintained projects. Dead links are removed automatically by the link checker.
- **No pure self-promotion.** A great open-source project you authored is welcome; a marketing page is not.

## How to add a resource

1. **Edit [`data/resources.json`](data/resources.json) — not the README.** The README's list is generated from this file.
2. Add one object to the right category's `resources` array:

   ```json
   {
     "name": "Your Project",
     "url": "https://github.com/you/your-project",
     "description": "One concise sentence (10–280 chars) on what it does and why it's useful.",
     "official": false,
     "lifecycle": ["build"]
   }
   ```

   - `official`: `true` only for first-party `langchain-ai` projects.
   - `lifecycle`: any of `build`, `observe`, `evaluate`, `deploy` — which stage(s) the resource serves.

3. **Regenerate and validate:**

   ```bash
   pip install -r requirements.txt
   python scripts/validate.py          # must pass
   python scripts/generate_readme.py   # rewrites the README's list
   ```

4. **Open a PR.** CI re-runs validation, the README sync check, the test suite, and a link check. Green = ready to merge.

## Adding a new category

Add a new object to the `categories` array with a unique `id` (kebab-case), a `group` (`ecosystem` or `community`), a `title`, a `description`, and at least one resource. The web page and README pick it up automatically.

## Governance / how this stays trustworthy

- **Schema** (`data/schema.json`) enforces the shape of every entry.
- **`validate.py`** rejects duplicate URLs/categories and unknown lifecycle stages.
- **`check_links.py`** runs weekly in CI to catch link rot.
- **The README is generated**, so the published list can never drift from the data.
- **`version`** in `resources.json` is bumped on schema-breaking changes.

By contributing you agree your contribution is released under [CC0](LICENSE) (public domain).

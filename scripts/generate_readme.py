"""Generate the curated list section of README.md from resources.json.

The prose (intro, lifecycle explainer, contributing) lives in README between
the AUTOGEN markers' bookends and is preserved. Only the block *between* the
markers is rewritten, so the data file stays the single source of truth for
links while humans own the narrative. Run with --check in CI to fail if the
README is stale.
"""
from __future__ import annotations

import argparse
import re
import sys

from lib import AUTOGEN_END, AUTOGEN_START, README_FILE, load_data

STAGE_EMOJI = {"build": "🔨", "observe": "🔭", "evaluate": "📊", "deploy": "🚀"}


def github_anchor(title: str) -> str:
    """Slugify a heading the way GitHub does: lowercase, strip punctuation
    (but keep spaces/hyphens), then spaces -> hyphens WITHOUT collapsing.
    A naive slug breaks the TOC for any title containing '&' or '—'.
    """
    slug = re.sub(r"[^\w\s-]", "", title.lower())
    return slug.replace(" ", "-")


def render(data: dict) -> str:
    lines: list[str] = []
    lines.append("## Contents\n")
    for cat in data["categories"]:
        lines.append(f"- [{cat['title']}](#{github_anchor(cat['title'])})")
    lines.append("")

    for cat in data["categories"]:
        lines.append(f"### {cat['title']}\n")
        lines.append(f"{cat['description']}\n")
        for res in cat["resources"]:
            badges = " ".join(STAGE_EMOJI[s] for s in res["lifecycle"])
            star = " ⭐" if res["official"] else ""
            lines.append(f"- [{res['name']}]({res['url']}){star} {badges} — {res['description']}")
        lines.append("")

    legend = (
        "> **Legend:** ⭐ official LangChain project · "
        + " · ".join(f"{e} {s}" for s, e in STAGE_EMOJI.items())
    )
    lines.append(legend)
    return "\n".join(lines).rstrip() + "\n"


def splice(readme: str, generated: str) -> str:
    start = readme.index(AUTOGEN_START) + len(AUTOGEN_START)
    end = readme.index(AUTOGEN_END)
    return readme[:start] + "\n\n" + generated + "\n" + readme[end:]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if README is out of date")
    args = parser.parse_args()

    data = load_data()
    readme = README_FILE.read_text(encoding="utf-8")
    updated = splice(readme, render(data))

    if args.check:
        if updated != readme:
            print("README.md is out of date — run `python scripts/generate_readme.py`", file=sys.stderr)
            return 1
        print("README.md is up to date")
        return 0

    README_FILE.write_text(updated, encoding="utf-8")
    print("README.md regenerated")
    return 0


if __name__ == "__main__":
    sys.exit(main())

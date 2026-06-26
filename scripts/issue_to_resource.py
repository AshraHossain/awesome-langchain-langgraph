"""Turn a 'Suggest a resource' issue-form submission into a validated entry.

GitHub renders an issue form as `### Label` headings followed by the value.
This parses that, builds a resources.json entry, appends it to the matching
category, and re-validates + regenerates the README. The submit-resource
workflow then opens a PR from the result. Parsing and entry-building are pure
functions so they're unit-tested without touching git or the network.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import generate_readme
from lib import DATA_FILE, README_FILE, load_data, load_schema
from validate import validate

STAGES = ["build", "observe", "evaluate", "deploy"]
NO_RESPONSE = "_No response_"


def parse_sections(body: str) -> dict[str, str]:
    """Map each `### Label` heading to its (stripped) value block."""
    sections: dict[str, str] = {}
    for chunk in re.split(r"^### +", body or "", flags=re.M):
        if not chunk.strip():
            continue
        label, _, value = chunk.partition("\n")
        value = value.strip()
        sections[label.strip()] = "" if value == NO_RESPONSE else value
    return sections


def checked_stages(value: str) -> list[str]:
    """Pull lifecycle stages from checked `- [x] 🔨 build` lines, in canonical order."""
    found = set()
    for line in value.splitlines():
        m = re.match(r"-\s*\[x\]", line.strip(), re.I)
        if not m:
            continue
        for stage in STAGES:
            if re.search(rf"\b{stage}\b", line, re.I):
                found.add(stage)
    return [s for s in STAGES if s in found]


def to_resource(sections: dict[str, str]) -> tuple[dict, str]:
    """Build a resource dict + return the target category title."""
    official = sections.get("Is this a first-party langchain-ai project?", "No").lower().startswith("yes")
    resource = {
        "name": sections.get("Name", "").strip(),
        "url": sections.get("URL", "").strip(),
        "description": sections.get("Description", "").strip(),
        "official": official,
        "lifecycle": checked_stages(sections.get("Lifecycle stage(s)", "")) or ["build"],
    }
    return resource, sections.get("Category", "").strip()


def apply(body: str) -> str:
    """Mutate resources.json + README from an issue body. Returns the new name."""
    sections = parse_sections(body)
    resource, category_title = to_resource(sections)

    data = load_data()
    category = next((c for c in data["categories"] if c["title"] == category_title), None)
    if category is None:
        raise SystemExit(
            f"Unknown or new category '{category_title}'. A maintainer should place this one by hand."
        )

    category["resources"].append(resource)
    errors = validate(data, load_schema())
    if errors:
        raise SystemExit("Submission did not pass validation:\n  - " + "\n  - ".join(errors))

    DATA_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    readme = README_FILE.read_text(encoding="utf-8")
    README_FILE.write_text(generate_readme.splice(readme, generate_readme.render(data)), encoding="utf-8")
    return resource["name"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--body-file", required=True, help="file containing the issue body")
    args = parser.parse_args()
    name = apply(Path(args.body_file).read_text(encoding="utf-8"))
    print(f"Added '{name}' and regenerated README.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

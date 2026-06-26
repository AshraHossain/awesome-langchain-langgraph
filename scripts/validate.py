"""Validate resources.json against the schema plus structural rules.

Governance gate: this runs in CI on every PR. Schema catches shape errors;
the extra checks catch duplicates and broken cross-references that a schema
can't express. Exit non-zero on any problem.
"""
from __future__ import annotations

import sys
from urllib.parse import urlparse

import jsonschema

from lib import iter_resources, load_data, load_schema


def validate(data: dict, schema: dict) -> list[str]:
    errors: list[str] = []

    # 1. Schema validation (collect all, don't stop at first).
    validator = jsonschema.Draft7Validator(schema)
    for err in sorted(validator.iter_errors(data), key=lambda e: e.path):
        loc = "/".join(str(p) for p in err.path) or "(root)"
        errors.append(f"schema: {loc}: {err.message}")

    # 2. Unique category ids.
    ids = [c["id"] for c in data["categories"]]
    for dup in {i for i in ids if ids.count(i) > 1}:
        errors.append(f"duplicate category id: {dup}")

    # 3. Unique URLs and well-formed hosts across the whole list.
    seen: dict[str, str] = {}
    for category, res in iter_resources(data):
        url = res.get("url")
        if not url:
            continue  # schema check above already reports the missing field
        if url in seen:
            errors.append(f"duplicate url: {url} (in '{seen[url]}' and '{res['name']}')")
        seen[url] = res["name"]
        if not urlparse(url).netloc:
            errors.append(f"url has no host: {url}")

    # 4. lifecycle values must be declared in lifecycle_stages.
    known = set(data["lifecycle_stages"])
    for _category, res in iter_resources(data):
        for stage in res.get("lifecycle", []):
            if stage not in known:
                errors.append(f"{res.get('name', '?')}: unknown lifecycle stage '{stage}'")

    return errors


def main() -> int:
    data = load_data()
    schema = load_schema()
    errors = validate(data, schema)
    if errors:
        print(f"VALIDATION FAILED ({len(errors)} issue(s)):", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    total = sum(len(c["resources"]) for c in data["categories"])
    print(f"OK: {len(data['categories'])} categories, {total} resources, schema v{data['version']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Generate a static JSON API from resources.json into site/api/.

Static hosting can't do query params, so we pre-render the slices people
actually want: a flattened list (with category metadata on each entry),
per-lifecycle slices, aggregate stats, and a shields.io endpoint for a live
resource-count badge. Everything is a pure function of the data file, so it's
trivially testable and can't drift from the source of truth.
"""
from __future__ import annotations

import json
import sys

from lib import SITE_DIR, iter_resources, load_data


def flatten(data: dict) -> list[dict]:
    """One flat list; each entry carries its category id/title/group."""
    out = []
    for cat, res in iter_resources(data):
        out.append({**res, "category_id": cat["id"], "category_title": cat["title"], "group": cat["group"]})
    return out


def stats(data: dict) -> dict:
    flat = flatten(data)
    by_life = {s: 0 for s in data["lifecycle_stages"]}
    for r in flat:
        for s in r["lifecycle"]:
            by_life[s] += 1
    by_group: dict[str, int] = {}
    for r in flat:
        by_group[r["group"]] = by_group.get(r["group"], 0) + 1
    return {
        "version": data["version"],
        "updated": data.get("updated"),
        "total": len(flat),
        "categories": len(data["categories"]),
        "official": sum(1 for r in flat if r["official"]),
        "by_group": by_group,
        "by_lifecycle": by_life,
        "by_category": {c["title"]: len(c["resources"]) for c in data["categories"]},
    }


def shield(data: dict) -> dict:
    """shields.io 'endpoint' badge schema: https://shields.io/badges/endpoint-badge"""
    total = sum(len(c["resources"]) for c in data["categories"])
    return {"schemaVersion": 1, "label": "resources", "message": str(total), "color": "#1c8c5a"}


def artifacts(data: dict) -> dict[str, object]:
    flat = flatten(data)
    arts: dict[str, object] = {
        "api/resources.json": flat,
        "api/stats.json": stats(data),
        "api/shield.json": shield(data),
    }
    for stage in data["lifecycle_stages"]:
        arts[f"api/lifecycle/{stage}.json"] = [r for r in flat if stage in r["lifecycle"]]
    return arts


def write(data: dict, site_dir=SITE_DIR) -> int:
    arts = artifacts(data)
    for rel, obj in arts.items():
        path = site_dir / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return len(arts)


def main() -> int:
    n = write(load_data())
    print(f"wrote {n} API artifacts under {SITE_DIR / 'api'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

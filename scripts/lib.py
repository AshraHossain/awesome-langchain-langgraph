"""Shared helpers for the awesome-list tooling."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "resources.json"
SCHEMA_FILE = ROOT / "data" / "schema.json"
README_FILE = ROOT / "README.md"
SITE_DIR = ROOT / "site"

AUTOGEN_START = "<!-- AUTOGEN:START -->"
AUTOGEN_END = "<!-- AUTOGEN:END -->"


def load_data(path: Path = DATA_FILE) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_schema(path: Path = SCHEMA_FILE) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def iter_resources(data: dict):
    """Yield (category, resource) pairs across the whole list."""
    for category in data["categories"]:
        for resource in category["resources"]:
            yield category, resource

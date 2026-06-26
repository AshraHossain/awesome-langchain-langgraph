"""Copy the data file into site/ so the static page can fetch it.

ponytail: the page reads the same resources.json the README is built from —
no second copy of the data to drift. This just stages it next to index.html
so it serves from any static host (and Docker/nginx) without a backend.
"""
from __future__ import annotations

import shutil
import sys

from lib import DATA_FILE, SITE_DIR


def main() -> int:
    dest = SITE_DIR / "resources.json"
    shutil.copyfile(DATA_FILE, dest)
    print(f"copied {DATA_FILE.name} -> {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

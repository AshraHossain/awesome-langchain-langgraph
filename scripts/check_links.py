"""Check every URL in resources.json is reachable.

The 'evals before you trust the output' of a link directory: a dead link is
this project's equivalent of a hallucinated answer. Runs on a schedule in CI.
HEAD first, fall back to GET (some hosts reject HEAD). Concurrency keeps it
fast. Exit non-zero if anything is broken.
"""
from __future__ import annotations

import argparse
import sys
from concurrent.futures import ThreadPoolExecutor

import requests

from lib import iter_resources, load_data

HEADERS = {"User-Agent": "awesome-langchain-langgraph-linkcheck/1.0"}
OK = range(200, 400)


def check(url: str, timeout: float) -> tuple[str, int | str]:
    try:
        r = requests.head(url, allow_redirects=True, timeout=timeout, headers=HEADERS)
        if r.status_code in (403, 405) or r.status_code >= 400:
            r = requests.get(url, allow_redirects=True, timeout=timeout, headers=HEADERS, stream=True)
        return url, r.status_code
    except requests.RequestException as exc:
        return url, type(exc).__name__


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--workers", type=int, default=16)
    args = parser.parse_args()

    urls = [res["url"] for _cat, res in iter_resources(load_data())]
    failures: list[tuple[str, int | str]] = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for url, status in pool.map(lambda u: check(u, args.timeout), urls):
            if not (isinstance(status, int) and status in OK):
                failures.append((url, status))
                print(f"BROKEN {status}: {url}")
            else:
                print(f"ok {status}: {url}")

    print(f"\n{len(urls) - len(failures)}/{len(urls)} links healthy")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

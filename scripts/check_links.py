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

# Pretend to be a browser — many hosts 403 a default UA (e.g. academy.langchain.com).
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
}
# Reachable: any 2xx/3xx. Also tolerate auth/bot/rate-limit gates — the server
# answered, so the link is live (industry-standard, cf. lychee/awesome-lint).
GATED = {401, 403, 429}


def is_alive(status: int | str) -> bool:
    return isinstance(status, int) and (200 <= status < 400 or status in GATED)


def check(url: str, timeout: float, retries: int = 1) -> tuple[str, int | str]:
    # Retry transient network errors once so a blip doesn't fail CI.
    for attempt in range(retries + 1):
        try:
            r = requests.head(url, allow_redirects=True, timeout=timeout, headers=HEADERS)
            if r.status_code in (403, 405) or r.status_code >= 400:
                r = requests.get(url, allow_redirects=True, timeout=timeout, headers=HEADERS, stream=True)
            return url, r.status_code
        except requests.RequestException as exc:
            if attempt == retries:
                return url, type(exc).__name__
    return url, "unreachable"  # unreachable, satisfies type checker


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--workers", type=int, default=16)
    args = parser.parse_args()

    urls = [res["url"] for _cat, res in iter_resources(load_data())]
    failures: list[tuple[str, int | str]] = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for url, status in pool.map(lambda u: check(u, args.timeout), urls):
            if not is_alive(status):
                failures.append((url, status))
                print(f"BROKEN {status}: {url}")
            elif isinstance(status, int) and status in GATED:
                print(f"gated {status} (reachable): {url}")
            else:
                print(f"ok {status}: {url}")

    print(f"\n{len(urls) - len(failures)}/{len(urls)} links healthy")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

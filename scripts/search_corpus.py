#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
from pathlib import Path


CORPUS_DIR = Path(os.environ.get("AVENGERS_CORPUS_DIR", "~/Documents/Avengers Corpus")).expanduser()


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Search the local Avengers/Tony Stark transcript corpus.")
    parser.add_argument("query", help="Case-insensitive text or regex query")
    parser.add_argument("--limit", type=int, default=40, help="Maximum matches to print")
    parser.add_argument("--regex", action="store_true", help="Treat query as a regular expression")
    args = parser.parse_args()

    if not CORPUS_DIR.exists():
        print(f"Corpus directory not found: {CORPUS_DIR}")
        return 2

    flags = re.IGNORECASE
    pattern = re.compile(args.query if args.regex else re.escape(args.query), flags)
    count = 0
    for path in sorted(CORPUS_DIR.glob("*.txt")):
        for line_no, line in enumerate(path.read_text(errors="replace").splitlines(), start=1):
            if pattern.search(line):
                print(f"{path.name}:{line_no}: {normalize(line)[:220]}")
                count += 1
                if count >= args.limit:
                    return 0
    if count == 0:
        print("No matches.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

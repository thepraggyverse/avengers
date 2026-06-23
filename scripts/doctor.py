#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
STALE_WORDING_RE = re.compile(
    "|".join(
        [
            "un" + "official",
            "10" + "7 A-prefixed",
            "Skills: " + "107",
            "Manifest entries: " + "107",
        ]
    ),
    re.IGNORECASE,
)
PRIVATE_PATTERN_RE = re.compile(
    "|".join(
        [
            "/" + "Users/" + "praggy",
            "000 " + "iCloud",
            "Documents/" + "000",
            r"sk-[A-Za-z0-9]{20,}",
            r"xox[baprs]-",
            r"ghp_[A-Za-z0-9]",
        ]
    )
)
SCAN_PATHS = [
    "README.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "docs",
    ".codex-plugin",
    ".claude-plugin",
    ".cursor-plugin",
    ".agents",
    "gemini-extension.json",
    "scripts",
    "tests",
    "references",
    "skills.sh.json",
]
JSON_PATHS = [
    ".codex-plugin/plugin.json",
    ".claude-plugin/plugin.json",
    ".cursor-plugin/plugin.json",
    ".agents/plugins/marketplace.json",
    "skills.sh.json",
    "references/skill-manifest.json",
    "gemini-extension.json",
]


def rel(path: Path) -> str:
    return str(path.relative_to(PLUGIN_ROOT))


def run_step(name: str, cmd: list[str]) -> tuple[bool, str]:
    print(f"\n==> {name}")
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    proc = subprocess.run(cmd, cwd=PLUGIN_ROOT, text=True, capture_output=True, env=env)
    if proc.stdout:
        print(proc.stdout.rstrip())
    if proc.stderr:
        print(proc.stderr.rstrip(), file=sys.stderr)
    if proc.returncode:
        print(f"FAILED: {name} exited {proc.returncode}", file=sys.stderr)
        return False, name
    print(f"ok: {name}")
    return True, name


def iter_text_files(paths: list[str]):
    for item in paths:
        path = PLUGIN_ROOT / item
        if not path.exists():
            continue
        if path.is_file():
            yield path
            continue
        for child in sorted(path.rglob("*")):
            if child.is_file() and not child.is_symlink():
                yield child


def check_json() -> tuple[bool, str]:
    print("\n==> JSON manifests")
    failures: list[str] = []
    for item in JSON_PATHS:
        path = PLUGIN_ROOT / item
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001 - report all parse/read failures.
            failures.append(f"{item}: {exc}")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return False, "JSON manifests"
    print(f"ok: parsed {len(JSON_PATHS)} JSON files")
    return True, "JSON manifests"


def check_text_scan(name: str, pattern: re.Pattern[str]) -> tuple[bool, str]:
    print(f"\n==> {name}")
    failures: list[str] = []
    for path in iter_text_files(SCAN_PATHS):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            if pattern.search(line):
                failures.append(f"{rel(path)}:{line_number}: {line}")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return False, name
    print(f"ok: {name}")
    return True, name


def check_generated_caches() -> tuple[bool, str]:
    print("\n==> generated caches")
    patterns = {"__pycache__", ".DS_Store"}
    failures: list[str] = []
    for path in PLUGIN_ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.name in patterns or path.suffix == ".pyc":
            failures.append(rel(path))
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return False, "generated caches"
    print("ok: no generated caches found")
    return True, "generated caches"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Avengers repository health checks.")
    parser.add_argument("--quick", action="store_true", help="Skip slower unit tests.")
    args = parser.parse_args()

    checks: list[tuple[bool, str]] = []
    checks.append(run_step("skill pack validation", ["python3", "scripts/validate_skill_pack.py"]))
    checks.append(check_json())
    if not args.quick:
        checks.append(run_step("unit tests", ["python3", "-m", "unittest", "discover", "-s", "tests", "-v"]))
    checks.append(check_text_scan("stale wording scan", STALE_WORDING_RE))
    checks.append(check_text_scan("private path and token scan", PRIVATE_PATTERN_RE))
    checks.append(run_step("git diff whitespace", ["git", "diff", "--check"]))
    checks.append(check_generated_caches())

    failures = [name for ok, name in checks if not ok]
    if failures:
        print("\nDoctor failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("\nAvengers doctor passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
from __future__ import annotations

import argparse
import filecmp
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
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
    ".github",
    "README.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "SECURITY.md",
    "SUPPORT.md",
    "assets",
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
GENERATED_PATHS = [
    ".codex-plugin/plugin.json",
    "docs/EXAMPLES.md",
    "docs/SKILL_INVENTORY.md",
    "docs/WORKFLOW.md",
    "references/corpus-index.md",
    "references/mcu-story-map.md",
    "references/skill-manifest.json",
    "references/skill-manifest.md",
    "references/source-map.md",
    "references/tony-stark-principles.md",
]
STABLE_GENERATED_PATHS = [
    ".codex-plugin/plugin.json",
    "docs/EXAMPLES.md",
    "docs/SKILL_INVENTORY.md",
    "docs/WORKFLOW.md",
    "references/mcu-story-map.md",
    "references/skill-manifest.json",
    "references/skill-manifest.md",
    "references/tony-stark-principles.md",
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


def check_git_diff_whitespace() -> tuple[bool, str]:
    probe = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], cwd=PLUGIN_ROOT, text=True, capture_output=True)
    if probe.returncode:
        print("\n==> git diff whitespace")
        print("skip: not inside a git worktree")
        return True, "git diff whitespace"
    return run_step("git diff whitespace", ["git", "diff", "--check"])


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


def configured_corpus_dir() -> Path | None:
    env_path = os.environ.get("AVENGERS_CORPUS_DIR")
    if env_path:
        path = Path(os.path.expandvars(env_path)).expanduser()
        return path if path.exists() else None

    config = PLUGIN_ROOT / ".avengers" / "config.local.yaml"
    if not config.exists():
        return None
    for line in config.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("path:"):
            raw = stripped.split(":", 1)[1].strip().strip('"').strip("'")
            path = Path(os.path.expandvars(raw)).expanduser()
            return path if path.exists() else None
    return None


def ignore_copy(dir_name: str, names: list[str]) -> set[str]:
    ignored = {".git", "__pycache__", ".DS_Store", ".mypy_cache", ".pytest_cache"}
    if dir_name.endswith("/.avengers") or dir_name.endswith("\\.avengers"):
        ignored.add("config.local.yaml")
    return ignored & set(names)


def check_generated_drift() -> tuple[bool, str]:
    print("\n==> generated file drift")
    corpus_dir = configured_corpus_dir()
    with tempfile.TemporaryDirectory() as tmp:
        copied_root = Path(tmp) / "avengers"
        shutil.copytree(PLUGIN_ROOT, copied_root, ignore=ignore_copy)
        env = os.environ.copy()
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        if corpus_dir is not None:
            env["AVENGERS_CORPUS_DIR"] = str(corpus_dir)
        else:
            env.pop("AVENGERS_CORPUS_DIR", None)
        proc = subprocess.run(
            ["python3", "scripts/generate_avengers_pack.py"],
            cwd=copied_root,
            text=True,
            capture_output=True,
            env=env,
        )
        if proc.stdout:
            print(proc.stdout.rstrip())
        if proc.stderr:
            print(proc.stderr.rstrip(), file=sys.stderr)
        if proc.returncode:
            print(f"generator exited {proc.returncode}", file=sys.stderr)
            return False, "generated file drift"

        if corpus_dir is None:
            print("No local corpus found; checking stable generated files only.")
            generated_paths = STABLE_GENERATED_PATHS
        else:
            generated_paths = [
                str(path.relative_to(PLUGIN_ROOT))
                for path in (PLUGIN_ROOT / "skills").glob("a-*/**/*")
                if path.is_file()
            ]
            generated_paths.extend(GENERATED_PATHS)
        failures = []
        for item in sorted(set(generated_paths)):
            source = PLUGIN_ROOT / item
            copy = copied_root / item
            if source.is_dir():
                continue
            if not source.exists() or not copy.exists():
                failures.append(f"{item}: missing in {'repo' if not source.exists() else 'generated copy'}")
                continue
            if not filecmp.cmp(source, copy, shallow=False):
                failures.append(item)
        if failures:
            print("Generated files drifted:\n" + "\n".join(failures), file=sys.stderr)
            return False, "generated file drift"
    print("ok: generated files are current")
    return True, "generated file drift"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Avengers repository health checks.")
    parser.add_argument("--quick", action="store_true", help="Skip slower unit tests.")
    parser.add_argument("--skip-generated-drift", action="store_true", help="Skip generator drift check.")
    args = parser.parse_args()

    checks: list[tuple[bool, str]] = []
    checks.append(run_step("skill pack validation", ["python3", "scripts/validate_skill_pack.py"]))
    checks.append(check_json())
    if not args.quick:
        checks.append(run_step("unit tests", ["python3", "-m", "unittest", "discover", "-s", "tests", "-v"]))
    checks.append(check_text_scan("stale wording scan", STALE_WORDING_RE))
    checks.append(check_text_scan("private path and token scan", PRIVATE_PATTERN_RE))
    checks.append(check_git_diff_whitespace())
    checks.append(check_generated_caches())
    if not args.skip_generated_drift:
        checks.append(check_generated_drift())

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

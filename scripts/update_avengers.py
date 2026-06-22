#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str], *, check: bool = True) -> int:
    print("+ " + " ".join(cmd))
    proc = subprocess.run(cmd, cwd=PLUGIN_ROOT)
    if check and proc.returncode:
        raise SystemExit(proc.returncode)
    return proc.returncode


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Update a checkout-based Avengers install, regenerate derived files, and validate the pack."
    )
    parser.add_argument("--apply", action="store_true", help="Run the update. Default is a dry run.")
    parser.add_argument("--no-pull", action="store_true", help="Skip git pull --ff-only.")
    parser.add_argument("--skip-generate", action="store_true", help="Skip scripts/generate_avengers_pack.py.")
    parser.add_argument("--install-codex", action="store_true", help="Refresh the Codex personal marketplace entry.")
    parser.add_argument("--install-symlinks", action="store_true", help="Refresh direct symlinks in default skill homes.")
    parser.add_argument("--force-symlinks", action="store_true", help="Pass --force to scripts/install_symlinks.py.")
    args = parser.parse_args()

    planned: list[list[str]] = []
    if not args.no_pull:
        planned.append(["git", "pull", "--ff-only"])
    if not args.skip_generate:
        planned.append(["python3", "scripts/generate_avengers_pack.py"])
    planned.extend([
        ["python3", "scripts/validate_skill_pack.py"],
        ["python3", "-m", "unittest", "discover", "-s", "tests", "-v"],
    ])
    if args.install_codex:
        planned.append(["python3", "scripts/install_codex_plugin.py", "--apply"])
    if args.install_symlinks:
        symlink_cmd = ["python3", "scripts/install_symlinks.py", "--apply"]
        if args.force_symlinks:
            symlink_cmd.append("--force")
        planned.append(symlink_cmd)

    if not args.apply:
        print("Dry run. Would run:")
        for cmd in planned:
            print("  " + " ".join(cmd))
        print("\nRe-run with --apply to execute.")
        return 0

    for cmd in planned:
        run(cmd)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

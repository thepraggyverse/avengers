#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = PLUGIN_ROOT / "skills"
DEFAULT_HOMES = [
    "~/.agents/skills",
    "~/.codex/skills",
    "~/.claude/skills",
    "~/.cursor/skills",
    "~/.openclaw/skills",
    "~/.openclaw/acpx/codex-home/skills",
]


def expand(path: str) -> Path:
    return Path(os.path.expandvars(path)).expanduser()


def link_skill(source: Path, target: Path, apply: bool, force: bool) -> str:
    if target.is_symlink() and target.resolve() == source.resolve():
        return f"ok existing {target}"
    if target.exists() or target.is_symlink():
        if not force:
            return f"skip exists {target}"
        if apply:
            if target.is_dir() and not target.is_symlink():
                return f"skip directory {target} (refusing to remove real directory)"
            target.unlink()
    if apply:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.symlink_to(source, target_is_directory=True)
    return f"{'link' if apply else 'would link'} {target} -> {source}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Symlink Avengers skills into agent skill homes.")
    parser.add_argument(
        "--home",
        action="append",
        help="Skill home to install into. Can be passed multiple times. Defaults to common Codex/Claude/OpenClaw homes.",
    )
    parser.add_argument("--apply", action="store_true", help="Actually create symlinks. Default is dry-run.")
    parser.add_argument("--force", action="store_true", help="Replace existing symlinks/files. Real directories are never removed.")
    parser.add_argument("--skill", action="append", help="Install only this skill name. Can be passed multiple times.")
    args = parser.parse_args()

    homes = [expand(home) for home in (args.home or DEFAULT_HOMES)]
    wanted = set(args.skill or [])
    skills = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir() and (not wanted or path.name in wanted))

    if wanted:
        found = {path.name for path in skills}
        missing = sorted(wanted - found)
        if missing:
            print("Missing skills: " + ", ".join(missing))
            return 2

    for home in homes:
        for skill in skills:
            print(link_skill(skill, home / skill.name, args.apply, args.force))

    if not args.apply:
        print("\nDry run only. Re-run with --apply to create symlinks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

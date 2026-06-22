#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = PLUGIN_ROOT / "skills"
MANIFEST_PATH = PLUGIN_ROOT / "references" / "skill-manifest.json"
PLUGIN_VALIDATOR = Path(os.environ.get("CODEX_PLUGIN_VALIDATOR", "~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py")).expanduser()
SKILL_VALIDATOR = Path(os.environ.get("CODEX_SKILL_VALIDATOR", "~/.codex/skills/.system/skill-creator/scripts/quick_validate.py")).expanduser()


def run(cmd: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(cmd, text=True, capture_output=True)
    return proc.returncode, proc.stdout, proc.stderr


def main() -> int:
    failures: list[str] = []
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())

    if len(manifest) != 107:
        failures.append(f"Expected 107 manifest entries, found {len(manifest)}")
    if len(skill_dirs) != 107:
        failures.append(f"Expected 107 skill directories, found {len(skill_dirs)}")

    manifest_names = {entry["name"] for entry in manifest}
    dir_names = {p.name for p in skill_dirs}
    missing_dirs = sorted(manifest_names - dir_names)
    extra_dirs = sorted(dir_names - manifest_names)
    if missing_dirs:
        failures.append(f"Missing skill dirs: {', '.join(missing_dirs)}")
    if extra_dirs:
        failures.append(f"Extra skill dirs: {', '.join(extra_dirs)}")

    broken_pairs = []
    for entry in manifest:
        for pair in entry.get("pairs_with", []):
            if pair not in manifest_names:
                broken_pairs.append(f"{entry['name']} -> {pair}")
    if broken_pairs:
        failures.append("Broken skill pair links:\n" + "\n".join(broken_pairs))

    if PLUGIN_VALIDATOR.exists():
        code, out, err = run(["python3", str(PLUGIN_VALIDATOR), str(PLUGIN_ROOT)])
        if code:
            failures.append("Plugin validation failed:\n" + out + err)
    else:
        print(f"Skipping plugin schema validator; not found at {PLUGIN_VALIDATOR}")

    bad_skills = []
    if SKILL_VALIDATOR.exists():
        for skill_dir in skill_dirs:
            code, out, err = run(["python3", str(SKILL_VALIDATOR), str(skill_dir)])
            if code:
                bad_skills.append(f"{skill_dir.name}\n{out}{err}")
        if bad_skills:
            failures.append("Skill validation failed:\n" + "\n---\n".join(bad_skills))
    else:
        print(f"Skipping skill frontmatter validator; not found at {SKILL_VALIDATOR}")

    if failures:
        print("\n\n".join(failures))
        return 1

    print("Avengers skill pack validation passed.")
    print(f"Skills: {len(skill_dirs)}")
    print(f"Manifest entries: {len(manifest)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

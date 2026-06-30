#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
JSON_VERSION_PATHS = [
    ".codex-plugin/plugin.json",
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    ".cursor-plugin/plugin.json",
    ".cursor-plugin/marketplace.json",
    "gemini-extension.json",
]


def update_json_version(path: Path, version: str) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    if "version" in data:
        data["version"] = version
    if isinstance(data.get("metadata"), dict) and "version" in data["metadata"]:
        data["metadata"]["version"] = version
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def update_versioning_doc(version: str) -> None:
    path = PLUGIN_ROOT / "docs" / "VERSIONING.md"
    text = path.read_text(encoding="utf-8")
    text, current_count = re.subn(
        r"Current version:\n\n```text\n[^`]+\n```",
        f"Current version:\n\n```text\n{version}\n```",
        text,
        count=1,
    )
    text, policy_count = re.subn(
        r"(## Current Release Policy\n\n```text\n)[^`]+(\n```)",
        rf"\1The latest release is {version}. The next feature release should bump the minor version.\2",
        text,
        count=1,
    )
    if current_count != 1 or policy_count != 1:
        raise RuntimeError("docs/VERSIONING.md version blocks did not match expected format")
    path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Update Avengers plugin manifest versions together.")
    parser.add_argument("version", help="SemVer version, for example 0.2.0.")
    parser.add_argument("--apply", action="store_true", help="Write files. Default is dry-run.")
    args = parser.parse_args()

    if not VERSION_RE.match(args.version):
        parser.error("version must look like SemVer, for example 0.2.0")

    targets = [PLUGIN_ROOT / item for item in JSON_VERSION_PATHS]
    targets.append(PLUGIN_ROOT / "docs" / "VERSIONING.md")

    if not args.apply:
        print(f"Dry run. Would set version to {args.version} in:")
        for target in targets:
            print(f"  {target.relative_to(PLUGIN_ROOT)}")
        print("\nRe-run with --apply to write changes.")
        return 0

    for item in JSON_VERSION_PATHS:
        update_json_version(PLUGIN_ROOT / item, args.version)
    update_versioning_doc(args.version)
    print(f"Updated Avengers version to {args.version}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

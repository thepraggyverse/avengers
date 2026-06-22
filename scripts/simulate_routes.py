#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = PLUGIN_ROOT / "skills"
MANIFEST_PATH = PLUGIN_ROOT / "references" / "skill-manifest.json"
STOP = {"the", "and", "for", "that", "this", "with", "from", "into"}


def load_entries() -> tuple[list[dict], dict[str, str]]:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    blobs = {}
    for entry in manifest:
        text = (SKILLS_DIR / entry["name"] / "SKILL.md").read_text(encoding="utf-8")
        blobs[entry["name"]] = " ".join([
            entry["name"],
            entry["display_name"],
            entry["summary"],
            " ".join(entry["triggers"]),
            entry["category"],
            text,
        ]).lower()
    return manifest, blobs


def score_prompt(prompt: str, limit: int = 8) -> list[tuple[int, str]]:
    manifest, blobs = load_entries()
    by_name = {entry["name"]: entry for entry in manifest}
    prompt_lower = prompt.lower()
    tokens = [
        token
        for token in re.findall(r"[a-z0-9]+", prompt_lower)
        if len(token) > 2 and token not in STOP
    ]
    scores = []
    for name, blob in blobs.items():
        entry = by_name[name]
        score = sum(1 for token in tokens if token in blob)
        for trigger in entry["triggers"]:
            trigger_lower = trigger.lower()
            trigger_tokens = [t for t in re.findall(r"[a-z0-9]+", trigger_lower) if len(t) > 2]
            if trigger_lower and trigger_lower in prompt_lower:
                score += 14
            elif trigger_tokens and all(t in prompt_lower for t in trigger_tokens):
                score += 6
        for chunk in name.removeprefix("a-").split("-"):
            if len(chunk) > 2 and chunk in prompt_lower:
                score += 3
        for token in re.findall(r"[a-z0-9]+", entry["summary"].lower()):
            if len(token) > 4 and token in prompt_lower:
                score += 2
        if name in prompt_lower:
            score += 8
        if "avengers" in prompt_lower and name == "a-stark-router":
            score += 4
        if score > 0:
            scores.append((score, name))
    return sorted(scores, reverse=True)[:limit]


def main() -> int:
    parser = argparse.ArgumentParser(description="Simulate Avengers skill routing for a prompt.")
    parser.add_argument("prompt")
    parser.add_argument("--limit", type=int, default=8)
    args = parser.parse_args()

    for score, name in score_prompt(args.prompt, args.limit):
        print(f"{score:3d} {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

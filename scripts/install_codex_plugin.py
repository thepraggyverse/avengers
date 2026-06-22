#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
PLUGIN_NAME = "avengers"


def ensure_plugin_location(apply: bool, force: bool) -> Path:
    target = Path.home() / "plugins" / PLUGIN_NAME
    if target.resolve() == PLUGIN_ROOT.resolve():
        return target
    if target.exists() or target.is_symlink():
        if target.is_symlink() and target.resolve() == PLUGIN_ROOT.resolve():
            return target
        if not force:
            raise SystemExit(f"{target} already exists. Re-run with --force to replace a symlink/file.")
        if target.is_dir() and not target.is_symlink():
            raise SystemExit(f"{target} is a real directory. Refusing to remove it.")
        if apply:
            target.unlink()
    if apply:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.symlink_to(PLUGIN_ROOT, target_is_directory=True)
    return target


def update_marketplace(apply: bool) -> Path:
    marketplace = Path.home() / ".agents" / "plugins" / "marketplace.json"
    entry = {
        "name": PLUGIN_NAME,
        "source": {"source": "local", "path": f"./plugins/{PLUGIN_NAME}"},
        "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        "category": "Productivity",
    }
    data = {
        "name": "personal",
        "interface": {"displayName": "Personal"},
        "plugins": [],
    }
    if marketplace.exists():
        data = json.loads(marketplace.read_text(encoding="utf-8"))
    plugins = [plugin for plugin in data.get("plugins", []) if plugin.get("name") != PLUGIN_NAME]
    plugins.append(entry)
    data["plugins"] = plugins
    data.setdefault("name", "personal")
    data.setdefault("interface", {"displayName": "Personal"})
    if apply:
        marketplace.parent.mkdir(parents=True, exist_ok=True)
        marketplace.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return marketplace


def main() -> int:
    parser = argparse.ArgumentParser(description="Install the Avengers Codex plugin into the personal marketplace.")
    parser.add_argument("--apply", action="store_true", help="Actually write links and marketplace entry. Default is dry-run.")
    parser.add_argument("--force", action="store_true", help="Replace an existing ~/plugins/avengers symlink/file if needed.")
    args = parser.parse_args()

    target = ensure_plugin_location(args.apply, args.force)
    marketplace = update_marketplace(args.apply)
    action = "Installed" if args.apply else "Would install"
    print(f"{action} plugin source: {target} -> {PLUGIN_ROOT}")
    print(f"{action} marketplace entry: {marketplace}")
    if not args.apply:
        print("\nDry run only. Re-run with --apply to make changes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

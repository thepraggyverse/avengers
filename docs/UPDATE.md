# Update

Avengers has two update modes:

1. **Checkout-based update** for local clones and symlink installs.
2. **Marketplace-managed update** for harness plugin caches.

## Checkout-Based Update

Dry run:

```bash
cd ~/plugins/avengers
python3 scripts/update_avengers.py
```

Apply:

```bash
python3 scripts/update_avengers.py --apply
```

This runs:

```text
git pull --ff-only
python3 scripts/generate_avengers_pack.py
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
```

Refresh Codex personal marketplace entry:

```bash
python3 scripts/update_avengers.py --apply --install-codex
```

Refresh default symlinks:

```bash
python3 scripts/update_avengers.py --apply --install-symlinks
```

Force symlink replacement for existing symlinks/files:

```bash
python3 scripts/update_avengers.py --apply --install-symlinks --force-symlinks
```

The symlink installer refuses to delete real directories.

## Marketplace-Managed Update

Use the harness update command or plugin UI, then restart or reload the harness so cached skills refresh.

Claude Code:

```text
/plugin marketplace update avengers-plugin
/plugin update avengers
```

Gemini CLI:

```bash
gemini extensions update avengers
```

Codex CLI:

```bash
codex plugin marketplace add "$PWD"
codex
```

Then open `/plugins`, select Avengers, update/reinstall if needed, and restart Codex.

## Local Development Update

When editing this repo:

```bash
python3 scripts/generate_avengers_pack.py
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
```

If testing native plugin loading, restart the harness after manifest or skill edits. Many plugin loaders cache skill metadata at session start.

## Stale Skill Cleanup

Current version exposes 107 skills. If a future version removes or renames a skill, old symlink installs may retain stale skill folders.

Clean a flat skill home by removing stale `a-*` links that point outside the current checkout, then reinstall:

```bash
python3 scripts/install_symlinks.py --apply --force
```

For native plugin caches, use the harness uninstall/reinstall path.

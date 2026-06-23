# Symlinks

The direct-symlink install keeps one canonical checkout of the Avengers skill pack and exposes each skill folder into one or more harness-specific skill homes.

This is useful when a harness loads skills from a flat directory and does not understand Codex plugin manifests.

## Default Homes

`scripts/install_symlinks.py` targets these homes by default:

```text
~/.agents/skills
~/.codex/skills
~/.claude/skills
~/.cursor/skills
~/.openclaw/skills
~/.openclaw/acpx/codex-home/skills
```

Each installed skill is a symlink:

```text
~/.codex/skills/a-mark-one-prototype -> ~/plugins/avengers/skills/a-mark-one-prototype
```

## Preview

```bash
python3 scripts/install_symlinks.py
```

The default is a dry run. Nothing changes until you add `--apply`.

## Apply

```bash
python3 scripts/install_symlinks.py --apply
```

## Install One Skill

```bash
python3 scripts/install_symlinks.py --apply --skill a-stark-router
```

## Install Into One Home

```bash
python3 scripts/install_symlinks.py --apply --home ~/.codex/skills
```

## Existing Files

If a target already exists, the installer skips it by default.

To replace an existing symlink or regular file:

```bash
python3 scripts/install_symlinks.py --apply --force
```

The script refuses to delete real directories. Remove or move those manually if you intentionally want to replace them.

## Updating

Pull the repo, regenerate if needed, validate, and the symlinked homes see the new content automatically:

```bash
cd ~/plugins/avengers
git pull --ff-only
python3 scripts/doctor.py
```

## Safe Uninstall

Use uninstall mode instead of broad shell deletes:

```bash
python3 scripts/install_symlinks.py --uninstall --apply --home ~/.codex/skills
```

The script removes only symlinks that point back to this Avengers checkout.

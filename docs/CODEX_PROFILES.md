# Codex Profiles

Codex can become noisy when a machine has many global skills installed. If skill discovery is crowded, install Avengers into a separate Codex profile for focused testing.

## Focused Profile Install

```bash
export CODEX_HOME="$HOME/.codex/profiles/avengers"
mkdir -p "$CODEX_HOME"
codex plugin marketplace add "$PWD"
codex plugin add avengers@personal
codex plugin list
```

Then run Codex with the same `CODEX_HOME`:

```bash
CODEX_HOME="$HOME/.codex/profiles/avengers" codex
```

## Focused Symlink Home

For harnesses that only read a flat skill home:

```bash
mkdir -p "$HOME/.codex/profiles/avengers/skills"
python3 scripts/install_symlinks.py --apply --home "$HOME/.codex/profiles/avengers/skills"
```

Uninstall safely:

```bash
python3 scripts/install_symlinks.py --uninstall --apply --home "$HOME/.codex/profiles/avengers/skills"
```

## When To Use This

Use a focused profile when:

- the global skill list is truncated
- another plugin has conflicting skill names or instructions
- you want to test Avengers install behavior without changing your main Codex profile
- you need a clean reproduction for an issue report

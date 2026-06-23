# Update

Avengers has two update modes:

1. Checkout-based update for local clones and symlink installs.
2. Marketplace-managed update for harness plugin caches.

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
python3 scripts/doctor.py
```

If you have the private corpus locally, prefer:

```bash
AVENGERS_CORPUS_DIR="/path/to/private/corpus" python3 scripts/generate_avengers_pack.py
```

You can also set `corpus.path` in `.avengers/config.local.yaml`. Scripts resolve the corpus path as `AVENGERS_CORPUS_DIR`, then `.avengers/config.local.yaml`, then `~/Documents/Avengers Corpus`.

That preserves generated source counts and source hooks. The corpus itself stays outside git.

## Refresh Installs

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

## Memory Refresh

Use `a-avengers-refresh` when you need to audit stale or overlapping memory/docs/skills.

Refresh reports belong in:

```text
docs/avengers-memory/refresh-reports/
```

A refresh report should say which items to keep, update, merge, replace, delete, or defer.

## Safe Regeneration

Before regenerating:

```bash
git status --short
```

Regenerate:

```bash
AVENGERS_CORPUS_DIR="/path/to/private/corpus" python3 scripts/generate_avengers_pack.py
```

Validate:

```bash
python3 scripts/doctor.py
```

Check for stale count or old wording:

```bash
rg -n "[u]nofficial|10[7] A-prefixed|Skills: 10[7]|Manifest entries: 10[7]" README.md AGENTS.md docs .codex-plugin .claude-plugin .cursor-plugin gemini-extension.json scripts tests
```

## Stale Skill Cleanup

Current version exposes 112 skills. If a future version removes or renames a skill, old symlink installs may retain stale skill folders.

Clean a flat skill home by removing stale `a-*` links that point outside the current checkout, then reinstall:

```bash
python3 scripts/install_symlinks.py --apply --force
```

For native plugin caches, use the harness uninstall/reinstall path.

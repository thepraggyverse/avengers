# Install

Avengers can be used in two ways:

1. As a Codex plugin.
2. As direct skill symlinks across multiple agent harnesses.

The plugin route is best for Codex. The symlink route is best when you want the same skills visible in Codex, Claude, OpenClaw, and shared local agent homes.

## Requirements

- Python 3.10+
- Git
- A local clone of this repository

No Python package install is required for normal validation, route simulation, or symlink installation.

## Clone

```bash
git clone https://github.com/thepraggyverse/avengers.git ~/plugins/avengers
cd ~/plugins/avengers
```

## Validate

```bash
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
```

Expected result:

```text
Avengers skill pack validation passed.
Skills: 107
Manifest entries: 107
```

## Install As A Codex Plugin

Preview:

```bash
python3 scripts/install_codex_plugin.py
```

Apply:

```bash
python3 scripts/install_codex_plugin.py --apply
```

What this does:

- Ensures `~/plugins/avengers` points at this checkout.
- Adds or refreshes the `avengers` entry in `~/.agents/plugins/marketplace.json`.
- Leaves the actual skill folders in this repo.

After installing, restart or reload Codex if the plugin list does not refresh immediately.

## Install As Direct Skill Symlinks

Preview:

```bash
python3 scripts/install_symlinks.py
```

Apply:

```bash
python3 scripts/install_symlinks.py --apply
```

Install one skill:

```bash
python3 scripts/install_symlinks.py --apply --skill a-stark-router
```

Install into one custom home:

```bash
python3 scripts/install_symlinks.py --apply --home ~/.codex/skills
```

See [SYMLINKS.md](SYMLINKS.md).

## Verify A Prompt Route

```bash
python3 scripts/simulate_routes.py "I keep waiting for approval before I start."
```

Example output:

```text
 36 a-permission-trap-breaker
 11 a-stark-router
 10 a-stark-build-before-you-believe
```

## Local Corpus Search

If you keep local transcripts or notes, set:

```bash
export AVENGERS_CORPUS_DIR="$HOME/Documents/Avengers Corpus"
```

Then search:

```bash
python3 scripts/search_corpus.py "Mark 1"
```


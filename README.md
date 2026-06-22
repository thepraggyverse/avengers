# Avengers Skill Pack

Avengers is an unofficial, fan-made local skill pack for Codex-compatible agents. It turns Tony Stark, Iron Man, Avengers, MCU story analysis, leadership, risk, prototyping, resourcefulness, mentorship, and source-grounded knowledge work into **107 A-prefixed skills**.

Every skill is named with the `a-` prefix so it is easy to find in Codex or another harness:

```text
a-stark-router
a-stark-operating-system
a-mark-one-prototype
a-cave-resourcefulness
a-mistake-to-upgrade
a-armor-around-world-check
```

This repository ships distilled skills and metadata only. It does **not** include full movie scripts, YouTube transcripts, books, or other copyrighted source material.

## What Is Included

- `skills/` - 107 generated A-prefixed skills.
- `references/skill-manifest.json` - source of truth for names, tiers, categories, triggers, chains, and output contracts.
- `references/skill-manifest.md` - human-readable inventory.
- `references/source-map.md` - concise source-file hooks for grounding.
- `references/tony-stark-principles.md` - distilled operating principles.
- `scripts/generate_avengers_pack.py` - regenerates every skill from the manifest data.
- `scripts/validate_skill_pack.py` - validates count, schema, frontmatter, and skill links.
- `scripts/simulate_routes.py` - simulates which skills match a prompt.
- `scripts/install_codex_plugin.py` - installs the Codex plugin into a personal marketplace.
- `scripts/install_symlinks.py` - symlinks individual skills into common harness homes.
- `tests/` - unit and routing-simulation tests.

## Skill Tiers

```text
Tier 1: orchestration and pack operations
Tier 2: core operating modes
Tier 3: specialized lenses
Tier 4: corpus/story/knowledge tools
```

Current distribution:

```text
Tier 1: 5
Tier 2: 59
Tier 3: 30
Tier 4: 13
Total: 107
```

## Quick Start

Clone the repo:

```bash
git clone https://github.com/thepraggyverse/avengers.git ~/plugins/avengers
cd ~/plugins/avengers
```

Validate the pack:

```bash
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
```

Install as a Codex plugin:

```bash
python3 scripts/install_codex_plugin.py --apply
```

Or symlink the skills directly into common skill homes:

```bash
python3 scripts/install_symlinks.py --apply
```

By default, symlink install targets:

```text
~/.agents/skills
~/.codex/skills
~/.claude/skills
~/.openclaw/skills
~/.openclaw/acpx/codex-home/skills
```

See [docs/INSTALL.md](docs/INSTALL.md) and [docs/SYMLINKS.md](docs/SYMLINKS.md) for details.

## How To Use

Ask for a specific skill:

```text
Use $a-mark-one-prototype to define the first version of this product.
```

Ask the router:

```text
Use $a-stark-router. I keep waiting for approval before starting my project.
```

Run the full operating system:

```text
Use $a-stark-operating-system to turn this idea into a Mark 1, test plan, upgrade loop, and risk check.
```

Search likely routes from the command line:

```bash
python3 scripts/simulate_routes.py "I have no money or tools. Help me solve this like cave Tony."
```

## Local Corpus Support

The public repo does not include full transcripts. If you have your own local notes or transcripts, point scripts at them:

```bash
export AVENGERS_CORPUS_DIR="$HOME/Documents/Avengers Corpus"
python3 scripts/search_corpus.py "permission trap"
```

See [docs/CORPUS.md](docs/CORPUS.md).

## Legal / Attribution

This is an unofficial fan-made tool. It is not affiliated with, endorsed by, sponsored by, or connected to Marvel, Disney, New Rockstars, ScreenCrush, or any other rightsholder mentioned in source-file hooks.

The MIT license applies to this repository's original code, generated skill text, tests, and documentation. It does not grant rights to any third-party characters, trademarks, films, videos, transcripts, books, or commentary.


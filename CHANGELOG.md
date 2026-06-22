# Changelog

All notable changes to Avengers are recorded here.

The format follows the spirit of Keep a Changelog, with plain-language entries for humans and agents. Dates use `YYYY-MM-DD`.

## [Unreleased]

### Added

- Added 112 A-prefixed skills under `skills/`, including the Avengers Memory layer:
  - `a-avengers-setup`
  - `a-avengers-compound`
  - `a-avengers-refresh`
  - `a-avengers-handoff`
  - `a-avengers-context`
- Added durable memory docs, templates, and schemas under `docs/avengers-memory/`.
- Added local config support through `.avengers/config.local.example.yaml`, `.avengers/config.local.yaml`, and `scripts/avengers_config.py`.
- Added multi-harness install and compatibility documentation for Codex, Claude Code, Cursor, OpenCode, Pi, Gemini CLI, and generic skill homes.
- Added reference-generated docs for workflow, skill inventory, examples, corpus use, testing, updates, and handoffs.
- Added unit tests and routing simulations for generated skills, memory skills, config resolution, manifest consistency, and plugin metadata.
- Added [docs/DOCUMENTATION_AUDIT.md](docs/DOCUMENTATION_AUDIT.md), comparing Avengers against Compound Engineering, the Every guide, and Matt Pocock's skills repo.

### Changed

- Rewrote plugin metadata to describe Avengers plainly as a skill pack for problem solving, invention, leadership, pressure handling, strategy, iteration, and source-grounded reasoning.
- Updated generated skills to include inputs, examples, safety/source-grounding notes, cross-harness notes, and self-tests.
- Updated `scripts/generate_avengers_pack.py` so regeneration preserves the current manifest wording and skill count.
- Updated `scripts/search_corpus.py` to resolve the corpus path from environment, local config, or a safe default.

### Verified

- `python3 scripts/search_corpus.py "permission trap" --limit 2`
- `python3 scripts/validate_skill_pack.py`
- `python3 -m unittest discover -s tests -v`
- JSON parsing for plugin and extension manifests.
- Stale wording scan for older affiliation disclaimers and 107-skill text.
- `git diff --check`
- Native Codex install through `python3 scripts/install_codex_plugin.py --apply` and `codex plugin add avengers@personal`.
- Live Codex skill-load simulations from the installed plugin cache.
- `autoreview --mode local` clean after the implementation pass.

### Notes

- The public repository intentionally does not include full transcripts, captions, books, movie scripts, private notes, or local corpus files.
- `.avengers/config.local.yaml` is local-only and ignored by git.

# Agent Instructions

This repository is the source for the `avengers` agent-skill package: 107 A-prefixed skills under `skills/`, plus plugin metadata and install helpers for multiple coding-agent harnesses.

`AGENTS.md` is the canonical authoring instruction file. `CLAUDE.md` and `GEMINI.md` are compatibility shims that point here.

## What This Repo Ships

```text
.codex-plugin/plugin.json       Codex native plugin manifest
.claude-plugin/                 Claude-compatible plugin and marketplace metadata
.cursor-plugin/                 Cursor plugin metadata
.agents/plugins/marketplace.json local marketplace metadata
.opencode/                      OpenCode install helper
.pi/                            Pi extension helper
skills/                         generated A-prefixed skills
references/                     generated manifest, source map, corpus index, principles
scripts/                        generate, validate, install, update, search, simulate
tests/                          unit tests and route simulations
docs/                           install, update, workflow, examples, harness notes
```

## Public-Safety Rule

Keep this repo public-safe. Do not commit:

- full transcripts, captions, books, movie scripts, commentary dumps, or private notes
- local machine paths such as personal iCloud folders
- secrets, API keys, tokens, browser profiles, cookies, or installed harness state
- generated caches such as `__pycache__`, `.pyc`, `.DS_Store`, or virtualenvs

Source hooks may name local source files, but the source text stays outside the repo. Use `AVENGERS_CORPUS_DIR` for local corpus search.

## Skill Authoring Rules

- Exposed skill names must stay lowercase, hyphen-case, and `a-` prefixed.
- Each exposed skill lives directly under `skills/<skill-name>/SKILL.md`.
- `SKILL.md` frontmatter must include only valid skill metadata. Keep `name` and `description` present.
- Descriptions should be model-facing and routing-friendly: short enough to load, rich enough to trigger.
- Do not reference files outside a skill directory from a skill body. If a skill needs support material, put it inside that skill directory.
- Prefer updating `scripts/generate_avengers_pack.py` and regenerating over hand-editing generated skills or generated docs.
- If a change affects skill count, skill names, categories, examples, triggers, or install surface, update README/docs/tests in the same change.

## Harness Compatibility Rules

- Codex-native metadata belongs in `.codex-plugin/plugin.json`.
- Claude-compatible metadata belongs in `.claude-plugin/`.
- Cursor metadata belongs in `.cursor-plugin/`.
- Local marketplace metadata belongs in `.agents/plugins/marketplace.json`.
- OpenCode package helpers belong in `.opencode/`.
- Pi extension helpers belong in `.pi/`.
- Flat skill installs are handled by `scripts/install_symlinks.py`; do not manually document one-off copy steps without adding them to `docs/HARNESSES.md`.
- Platform-specific runtime assumptions in skills are discouraged. Skills should work as plain `SKILL.md` folders when symlinked into any compatible skill home.

## Verification

Run after normal content changes:

```bash
python3 scripts/generate_avengers_pack.py
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
```

Run after routing trigger changes:

```bash
python3 scripts/simulate_routes.py "I keep waiting for approval before I start."
python3 scripts/simulate_routes.py "Break down Iron Man 2 Easter eggs."
python3 scripts/simulate_routes.py "This safety automation might become Ultron."
```

Run before public commits:

```bash
git diff --check
find . \( -name '__pycache__' -o -name '*.pyc' -o -name '.DS_Store' \) -print
```

Also run an appropriate local-path and secret scan before public pushes. Avoid writing the exact sensitive strings into committed docs merely to demonstrate the scan.

## Commit And Release Notes

- Use conventional commit messages such as `docs:`, `feat:`, `fix:`, `test:`, or `chore:`.
- Do not hand-bump release-owned versions unless explicitly asked.
- If behavior, install flow, or skill inventory changes, update README and the relevant docs.
- If a skill is removed or renamed, document stale artifact cleanup in `docs/UPDATE.md`.

## Generated Files

Generated from `scripts/generate_avengers_pack.py`:

- `skills/a-*/SKILL.md`
- `skills/a-*/agents/openai.yaml`
- `references/skill-manifest.json`
- `references/skill-manifest.md`
- `references/source-map.md`
- `references/corpus-index.md`
- `references/mcu-story-map.md`
- `references/tony-stark-principles.md`
- `docs/WORKFLOW.md`
- `docs/SKILL_INVENTORY.md`
- `docs/EXAMPLES.md`

Edit the generator when possible; regenerate; then validate.

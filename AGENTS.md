# Agent Instructions

This repository is the source for the `avengers` agent-skill package: 112 A-prefixed skills under `skills/`, plus plugin metadata, memory docs, and install helpers for multiple coding-agent harnesses.

Avengers is an Avengers-inspired skill pack for problem solving, invention, leadership, pressure handling, strategy, iteration, and source-grounded reasoning.

`AGENTS.md` is the canonical authoring instruction file. `CLAUDE.md` and `GEMINI.md` are compatibility shims that point here.

## What This Repo Ships

```text
.codex-plugin/plugin.json        Codex native plugin manifest
.claude-plugin/                  Claude-compatible plugin and marketplace metadata
.cursor-plugin/                  Cursor plugin metadata
.agents/plugins/marketplace.json Local marketplace metadata
.avengers/                       Example local config
.opencode/                       OpenCode install helper
.pi/                             Pi extension helper
skills/                          Generated A-prefixed skills
references/                      Generated manifest, source map, corpus index, principles
scripts/                         Doctor, generate, validate, install, update, search, simulate
tests/                           Unit tests and route simulations
docs/                            Install, update, workflow, examples, memory, harness notes
CHANGELOG.md                     Release notes and verification history
SECURITY.md                      Security and public-safety policy
SUPPORT.md                       Support and issue-report guidance
.github/workflows/ci.yml         CI doctor check
```

## Public-Safety Rule

Keep this repo public-safe. Do not commit:

- full transcripts, captions, books, movie scripts, commentary dumps, or private notes
- `.avengers/config.local.yaml` or other real local config
- local machine paths such as personal iCloud folders
- secrets, API keys, tokens, browser profiles, cookies, or installed harness state
- generated caches such as `__pycache__`, `.pyc`, `.DS_Store`, or virtualenvs

Source hooks may name source files, but source text stays outside the repo. Use `AVENGERS_CORPUS_DIR` for local corpus search.

## Skill Authoring Rules

- Exposed skill names must stay lowercase, hyphen-case, and `a-` prefixed.
- Each exposed skill lives directly under `skills/<skill-name>/SKILL.md`.
- `SKILL.md` frontmatter must include `name` and `description`.
- Descriptions should be model-facing and routing-friendly.
- Prefer updating `scripts/generate_avengers_pack.py` and regenerating over hand-editing generated skills or generated docs.
- If a change affects skill count, skill names, categories, examples, triggers, or install surface, update README/docs/tests in the same change.

Generated skills should include:

- clear role
- use conditions
- inputs
- workflow steps
- output contract
- example prompt
- source hooks
- safety/source-grounding guidance
- cross-harness notes
- self-test

## Memory Rules

Use the memory layer only when a run creates reusable value.

| Need | Skill | Durable Artifact |
|---|---|---|
| Configure local paths and harnesses. | `a-avengers-setup` | `.avengers/config.local.yaml` locally |
| Save a reusable lesson. | `a-avengers-compound` | `docs/avengers-memory/learnings/` |
| Check stale/overlapping guidance. | `a-avengers-refresh` | `docs/avengers-memory/refresh-reports/` |
| Continue later. | `a-avengers-handoff` | `docs/avengers-memory/handoffs/` or temp path |
| Clarify shared terms. | `a-avengers-context` | `docs/AVENGERS_CONTEXT.md` |

Do not save raw chat dumps or transcript excerpts as memory. Capture decisions, source names, related skills, and the reusable lesson.

## Harness Compatibility Rules

- Codex-native metadata belongs in `.codex-plugin/plugin.json`.
- Claude-compatible metadata belongs in `.claude-plugin/`.
- Cursor metadata belongs in `.cursor-plugin/`.
- Local marketplace metadata belongs in `.agents/plugins/marketplace.json`.
- OpenCode package helpers belong in `.opencode/`.
- Pi extension helpers belong in `.pi/`.
- Gemini metadata belongs in `gemini-extension.json` and `GEMINI.md`.
- Flat skill installs are handled by `scripts/install_symlinks.py`.
- Platform-specific runtime assumptions in skills are discouraged. Skills should work as plain `SKILL.md` folders when symlinked into any compatible skill home.

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

The changelog and documentation audit are hand-maintained. Update them when user-visible install behavior, skill count, harness support, memory policy, or release readiness changes.

Edit the generator when possible, regenerate, then validate.

## Verification

Run after normal content changes:

```bash
AVENGERS_CORPUS_DIR="/path/to/private/corpus" python3 scripts/generate_avengers_pack.py
python3 scripts/doctor.py
```

Run after routing trigger changes:

```bash
python3 scripts/simulate_routes.py "I keep waiting for approval before I start."
python3 scripts/simulate_routes.py "Break down Iron Man 2 Easter eggs."
python3 scripts/simulate_routes.py "Save what we learned from this Avengers run."
python3 scripts/simulate_routes.py "Write a handoff for the next agent."
```

Run before public commits:

```bash
python3 scripts/doctor.py
```

The doctor includes validation, tests, JSON parsing, stale wording scan, local-path/token scan, diff whitespace, and generated-cache checks. Avoid writing sensitive strings into committed docs merely to demonstrate the scan.

When docs are part of the change, check that `README.md`, `CHANGELOG.md`, and `docs/DOCUMENTATION_AUDIT.md` still agree about skill count, install routes, memory paths, and limitations.

When release or install behavior changes, also update `docs/VERSIONING.md`, `SECURITY.md`, `SUPPORT.md`, or `docs/CODEX_PROFILES.md` when relevant.

## Autoreview Closeout

After non-trivial changes:

1. Run the focused validation commands.
2. Run an autoreview-style diff review.
3. Verify any finding against the real files.
4. Fix in-scope findings.
5. Re-run affected tests.
6. Create a handoff artifact if the work may continue.

Do not push to GitHub unless the user explicitly asks.

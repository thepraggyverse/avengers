---
title: "Phase 0-3 Avengers implementation"
date: "2026-06-22"
type: "handoff"
repo_state: "main branch with local uncommitted implementation changes"
status: "ready"
autoreview: "passed"
---

# Phase 0-3 Avengers Implementation Handoff

## Current Task

Implement Phases 0-3 for the Avengers skill/plugin pack:

- fix generator drift and stale plugin wording
- add a durable memory/log layer
- add five A-prefixed Avengers memory skills
- update public docs, install/update/test guidance, examples, and harness metadata
- run validation, simulator tests, autoreview, and create a handoff
- post-closeout fix: make `.avengers/config.local.yaml` actually drive corpus search/generation, then install and live-test the plugin in Codex

## Repo State

- Repo: local Avengers checkout
- Branch: `main`
- Status: local uncommitted changes, no GitHub push performed
- Skill count: 112 generated skills
- New skills:
  - `a-avengers-setup`
  - `a-avengers-compound`
  - `a-avengers-refresh`
  - `a-avengers-handoff`
- `a-avengers-context`
- Installed Codex status: `avengers@personal` installed and enabled

## Files Changed

Major areas:

- Generator and validator:
  - `scripts/generate_avengers_pack.py`
  - `scripts/avengers_config.py`
  - `scripts/search_corpus.py`
  - `scripts/validate_skill_pack.py`
- Tests:
  - `tests/test_avengers_pack.py`
  - `tests/test_skill_simulations.py`
- Plugin and harness metadata:
  - `.codex-plugin/plugin.json`
  - `.claude-plugin/plugin.json`
  - `.claude-plugin/marketplace.json`
  - `.cursor-plugin/plugin.json`
  - `.cursor-plugin/marketplace.json`
  - `gemini-extension.json`
  - `skills.sh.json`
- Docs:
  - `README.md`
  - `AGENTS.md`
  - `docs/INSTALL.md`
  - `docs/UPDATE.md`
  - `docs/HARNESSES.md`
  - `docs/TESTING.md`
  - `docs/HANDOFF.md`
  - `docs/AVENGERS_MEMORY.md`
  - `docs/AVENGERS_CONTEXT.md`
  - generated `docs/WORKFLOW.md`, `docs/SKILL_INVENTORY.md`, `docs/EXAMPLES.md`
- Memory layer:
  - `.avengers/config.local.example.yaml`
  - `docs/avengers-memory/schemas/`
  - `docs/avengers-memory/templates/`
  - `docs/avengers-memory/learnings/.gitkeep`
  - `docs/avengers-memory/runs/.gitkeep`
  - `docs/avengers-memory/refresh-reports/.gitkeep`
  - `docs/avengers-memory/handoffs/.gitkeep`
- Generated skill folders:
  - all existing `skills/a-*` gained Inputs, Example, Safety And Grounding, and Cross-Harness Notes sections
  - five new `skills/a-avengers-*` folders were generated

## Commands Run

```bash
AVENGERS_CORPUS_DIR="/path/to/private/corpus" python3 scripts/generate_avengers_pack.py
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
for f in .codex-plugin/plugin.json .claude-plugin/plugin.json .claude-plugin/marketplace.json .cursor-plugin/plugin.json .cursor-plugin/marketplace.json .agents/plugins/marketplace.json gemini-extension.json skills.sh.json; do python3 -m json.tool "$f" >/dev/null || exit 1; done
rg -n "[u]nofficial|10[7] A-prefixed|Skills: 10[7]|Manifest entries: 10[7]|Current version exposes 10[7]|Total skills: 10[7]|Expected 10[7]" README.md AGENTS.md docs .codex-plugin .claude-plugin .cursor-plugin gemini-extension.json scripts tests .agents .opencode .pi skills.sh.json references/skill-manifest.md
git diff --check
find . \( -name '__pycache__' -o -name '*.pyc' -o -name '.DS_Store' \) -print
python3 scripts/simulate_routes.py "Set up Avengers for this repo in Codex with a local corpus path."
python3 scripts/simulate_routes.py "Save what we learned from this Avengers run as a reusable memory note."
python3 scripts/simulate_routes.py "Audit stale Avengers memory notes and overlapping skills."
python3 scripts/simulate_routes.py "Write a handoff so the next agent can continue this Avengers plugin work."
python3 scripts/simulate_routes.py "Update the Avengers context glossary with this recurring operating principle."
python3 scripts/install_codex_plugin.py
python3 scripts/install_symlinks.py --home /tmp/avengers-skill-home --skill a-avengers-setup
python3 scripts/update_avengers.py
AVENGERS_CORPUS_DIR="/path/to/private/corpus" python3 scripts/search_corpus.py "permission trap" --limit 2
autoreview --mode local
python3 scripts/search_corpus.py "permission trap" --limit 2
python3 scripts/generate_avengers_pack.py
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
python3 scripts/install_codex_plugin.py --apply
codex plugin add avengers@personal
codex plugin list
codex exec --ephemeral --sandbox read-only --skip-git-repo-check -C /tmp 'Use $a-avengers-compound. Do not modify files. Reply with exactly three lines: Skill:, Fields:, Next:'
```

## Test Results

- Generator: passed, produced 112 skills.
- Pack validator: passed.
- Unit tests: passed, 13 tests.
- JSON metadata checks: passed.
- Stale wording grep: passed with no matches.
- Diff whitespace check: passed.
- Cache/artifact hygiene: passed after removing test `__pycache__`.
- Route simulations: passed; new memory skills route at the top for setup, compound, refresh, handoff, and context prompts.
- Install/update dry-runs:
  - `install_codex_plugin.py`: passed dry-run.
  - `install_symlinks.py --home /tmp/avengers-skill-home --skill a-avengers-setup`: passed dry-run.
  - `update_avengers.py`: passed dry-run.
- Corpus search:
  - default path failed, as expected without local config
  - after config fix, `.avengers/config.local.yaml` path passed without `AVENGERS_CORPUS_DIR` and found `permission trap` matches
- Codex install/load:
  - `avengers@personal` installed and enabled
  - installed cache contained 112 skills
  - fresh read-only Codex CLI run from `/tmp` loaded `avengers:a-avengers-compound` from the installed plugin cache and returned the expected output fields

## Autoreview Result

Autoreview completed cleanly:

```text
autoreview clean: no accepted/actionable findings reported
overall: patch is correct (0.86)
```

## Decisions

- Keep all existing skills and add five new A-prefixed skills, bringing the pack to 112.
- Keep skills as the core portable unit across harnesses.
- Add memory as lightweight docs/templates/schemas rather than copying the full Compound Engineering workflow.
- Preserve private corpus content outside the repo.
- Use `.avengers/config.local.example.yaml` as the committed example and ignore real local config.
- Read corpus path from `AVENGERS_CORPUS_DIR`, then `.avengers/config.local.yaml`, then the generic default.
- Keep `a-stark-operating-system` as a skill name, but remove the old vague plugin-pack wording.

## Known Limitations

- Native Codex plugin install was applied and live-tested.
- No GitHub push was performed.
- Corpus search works through `AVENGERS_CORPUS_DIR` or ignored local config. A machine without either still falls back to the generic default path.
- Some harness plugin behavior depends on the installed harness version; symlink install remains the universal fallback.

## Next Steps

1. Review the local diff.
2. Commit when ready.
3. Push only if explicitly approved.
4. After install/update in Codex or another harness, start a new session or restart the harness so skill metadata refreshes.

# Documentation Audit

This audit compares Avengers against three references:

- Every's Compound Engineering guide: `https://every.to/guides/compound-engineering`
- EveryInc `compound-engineering-plugin`: `https://github.com/EveryInc/compound-engineering-plugin`
- Matt Pocock `skills`: `https://github.com/mattpocock/skills`

The goal is not to clone their structure. The goal is to make Avengers complete for its own purpose: a public-safe, Avengers-inspired skill pack that works as native plugin metadata and as plain `SKILL.md` folders across harnesses.

## Reference Patterns Used

| Reference | Strong Pattern | Avengers Adaptation |
|---|---|---|
| Every guide | The loop ends by saving reusable learning, not just shipping output. | Added `a-avengers-compound`, memory schemas, templates, and `docs/AVENGERS_MEMORY.md`. |
| Every guide | Installation explains where files live and what each harness needs. | Added `docs/INSTALL.md`, `docs/HARNESSES.md`, `docs/SYMLINKS.md`, and repo-layout notes. |
| Compound Engineering plugin | Multi-harness plugin metadata plus plain skills. | Added `.codex-plugin/`, `.claude-plugin/`, `.cursor-plugin/`, `.agents/plugins/`, `.opencode/`, `.pi/`, and `gemini-extension.json`. |
| Compound Engineering plugin | Durable docs areas for brainstorms, plans, solutions, reports, and specs. | Added `docs/avengers-memory/` for learnings, runs, refresh reports, and handoffs. |
| Compound Engineering plugin | `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` make harness behavior explicit. | Added `AGENTS.md` as canonical instructions, with compatibility shims. |
| Matt Pocock skills | Lightweight context and ADR-style decision memory. | Added `docs/AVENGERS_CONTEXT.md`; future public design decisions can live in docs when they affect the pack contract. |
| Matt Pocock skills | Simple scripts to list/link/install skills. | Added validation, symlink install, Codex install, update, search, generation, and route simulation scripts. |
| Both repos | Changelog or changeset history for public releases. | Added root `CHANGELOG.md`. |

## Coverage Matrix

| Area | Avengers Status | Evidence |
|---|---|---|
| Plain README | Covered | `README.md` explains purpose, count, loop, install, update, tests, corpus, and rights. |
| Canonical agent instructions | Covered | `AGENTS.md` defines authoring, public-safety, generated-file, verification, and closeout rules. |
| Claude compatibility | Covered | `CLAUDE.md` points to `AGENTS.md`; `.claude-plugin/` exists. |
| Gemini compatibility | Covered | `GEMINI.md` and `gemini-extension.json` exist. |
| Codex native plugin metadata | Covered | `.codex-plugin/plugin.json` exists and is generated from the current template. |
| Cursor metadata | Covered | `.cursor-plugin/` exists. |
| OpenCode helper | Covered | `.opencode/INSTALL.md` and `.opencode/plugins/avengers.js` exist. |
| Pi helper | Covered | `.pi/extensions/avengers.ts` exists. |
| Generic skill install | Covered | `scripts/install_symlinks.py` supports flat skill homes. |
| Install instructions | Covered | `docs/INSTALL.md` covers native and symlink paths. |
| Update instructions | Covered | `docs/UPDATE.md` covers checkout updates, regeneration, reinstall, and validation. |
| Skill inventory | Covered | `docs/SKILL_INVENTORY.md` and `references/skill-manifest.*`. |
| Examples | Covered | `docs/EXAMPLES.md` and per-skill examples in `SKILL.md`. |
| Workflow explanation | Covered | `docs/WORKFLOW.md` and README loop. |
| Corpus handling | Covered | `docs/CORPUS.md`, `references/source-map.md`, `references/corpus-index.md`, and `scripts/search_corpus.py`. |
| Local config | Covered | `.avengers/config.local.example.yaml` and ignored `.avengers/config.local.yaml`. |
| Durable memory | Covered | `docs/AVENGERS_MEMORY.md`, schemas, templates, and memory folders. |
| Context vocabulary | Covered | `docs/AVENGERS_CONTEXT.md`. |
| Handoff protocol | Covered | `docs/HANDOFF.md` and `a-avengers-handoff`. |
| Testing docs | Covered | `docs/TESTING.md`. |
| Focused Codex profile guidance | Covered | `docs/CODEX_PROFILES.md`. |
| Version policy | Covered | `docs/VERSIONING.md`. |
| Security policy | Covered | `SECURITY.md`. |
| Support policy | Covered | `SUPPORT.md`. |
| Public changelog | Covered | `CHANGELOG.md`. |
| Documentation audit | Covered | This file. |
| One-command health check | Covered | `scripts/doctor.py`. |
| Continuous integration | Covered | `.github/workflows/ci.yml` runs the doctor on push and pull requests. |

## Intentional Differences

| Difference | Why |
|---|---|
| No copied agents from Compound Engineering | Avengers skills must work in harnesses that only understand `SKILL.md`; subagents are optional and harness-specific. |
| No full `docs/brainstorms/` and `docs/plans/` tree | Avengers is a reusable skill pack, not a product repo workflow archive. Handoffs and memory notes are enough for current scope. |
| No bundled source corpus | The source files include transcripts, captions, books, commentary, and private notes that should not be committed. |
| No automatic external update process | The pack is local-first. Updates run through `scripts/update_avengers.py` and explicit reinstall steps. |
| No generated raw source excerpts | Skills cite source names and principles without embedding third-party text. |

## Current Gaps To Revisit Later

| Gap | Trigger To Add |
|---|---|
| Release automation | Add when the repo is ready for tagged public releases. |
| ADR folder | Add when a design decision changes public contracts, versioning, harness support, or memory policy. |
| Generated docs validation beyond smoke tests | Add if docs drift becomes common after regeneration. |

## Closeout Checklist

Before saying the pack is ready:

1. Regenerate when generator-owned files change.
2. Run `python3 scripts/doctor.py`.
3. If generation changed routing, run focused `scripts/simulate_routes.py` prompts.
4. Scan the staged diff for docs and instruction consistency.
5. Reinstall or refresh the plugin cache when plugin surfaces changed.
6. Run at least one live harness skill-load test when install behavior changed.
7. Run autoreview for non-trivial changes.
8. Update `CHANGELOG.md` and handoff notes.

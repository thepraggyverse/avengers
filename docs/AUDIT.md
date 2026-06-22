# Reference Audit

This note records the package patterns audited before the multi-harness update.

## Sources Reviewed

| Source | Useful Pattern |
|---|---|
| Every guide: Compound Engineering | A loop where each work unit leaves reusable context for the next one. |
| EveryInc/compound-engineering-plugin | Multi-harness manifests, local development install paths, update notes, compatibility shims, repo-level AGENTS guidance. |
| EveryInc/compound-knowledge-plugin | Small knowledge-work loop, local-first `docs/knowledge` style, progressive disclosure, clear component counts. |
| mattpocock/skills | Clear skill inventory, user/model invocation distinction, setup skill, compact category grouping. |
| steipete/agent-scripts | Terse AGENTS rules, validation script discipline, symlink-first skill sharing, update/release docs. |

## Gaps Found In Avengers

| Gap | Status |
|---|---|
| README led with independence language instead of what the skills do. | Fixed: README now starts with skill purpose and usage. |
| Codex was the only native plugin manifest. | Fixed: added Claude-compatible, Cursor, shared marketplace, Gemini, OpenCode, and Pi surfaces. |
| Install docs did not cover enough harnesses. | Fixed: expanded `docs/INSTALL.md` and added `docs/HARNESSES.md`. |
| Update path was manual. | Fixed: added `scripts/update_avengers.py` and `docs/UPDATE.md`. |
| AGENTS.md was too thin. | Fixed: added authoring, public-safety, harness, verification, and generated-file rules. |
| Compatibility shims were missing. | Fixed: added `CLAUDE.md` and `GEMINI.md`. |
| Cursor flat skill home missing from default symlink targets. | Fixed: added `~/.cursor/skills`. |

## Deliberate Non-Changes

| Decision | Reason |
|---|---|
| Keep the pack as skills, not standalone agents. | Skills are the most portable unit across Codex, Claude, Cursor, OpenClaw, and generic SKILL.md harnesses. |
| Do not commit full corpus text. | Public-safe repo; local corpus stays external through `AVENGERS_CORPUS_DIR`. |
| Do not add MCP servers. | The pack does not need runtime services yet; source search is local script-based. |
| Do not add dependency-heavy installers. | Current install/validate path works with Python standard library and Git. |

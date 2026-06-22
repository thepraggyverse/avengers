---
title: Avengers Install And Documentation Audit Closeout
date: 2026-06-22
status: complete
related_skills:
  - a-avengers-refresh
  - a-avengers-handoff
  - a-avengers-compound
---

# Avengers Install And Documentation Audit Closeout

## Current Task

Install the Avengers plugin, compare the repo documentation against Compound Engineering, Every's guide, and Matt Pocock's skills repo, fix missing release/docs surfaces, run live load tests, run autoreview, and leave a handoff.

## Repo State

- Branch: `main`
- Skill count: 112
- Plugin status after install: `avengers@personal` installed and enabled
- Installed cache check: 112 `SKILL.md` files and the five Avengers Memory skills present
- Local-only config: `.avengers/config.local.yaml` is ignored by git

## Files Changed

- Added `CHANGELOG.md`
- Added `docs/DOCUMENTATION_AUDIT.md`
- Updated `README.md`, `AGENTS.md`, `docs/INSTALL.md`, and `docs/HANDOFF.md` to reference changelog, audit, and release-readiness checks
- Added `--uninstall` to `scripts/install_symlinks.py` so symlink removal only touches Avengers-owned links
- Added a regression test that verifies foreign `a-*` skill links are left intact
- Existing phase 0-3 changes remain in place: memory layer, setup/compound/refresh/handoff/context skills, generator updates, config helper, tests, and install docs

## Reference Audit

References checked:

- `https://every.to/guides/compound-engineering`
- `https://github.com/EveryInc/compound-engineering-plugin`
- `https://github.com/mattpocock/skills`

Main added coverage:

- Root changelog for release history
- Written docs audit with coverage matrix, intentional differences, and future gaps
- README and AGENTS links so the new docs are discoverable

## Commands Run

```bash
python3 scripts/search_corpus.py "permission trap" --limit 2
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
python3 -m json.tool .codex-plugin/plugin.json >/dev/null
python3 -m json.tool .claude-plugin/plugin.json >/dev/null
python3 -m json.tool .cursor-plugin/plugin.json >/dev/null
python3 -m json.tool .agents/plugins/marketplace.json >/dev/null
python3 -m json.tool skills.sh.json >/dev/null
python3 -m json.tool references/skill-manifest.json >/dev/null
rg -n "[u]nofficial|10[7] A-prefixed|Skills: 10[7]|Manifest entries: 10[7]" README.md AGENTS.md CHANGELOG.md docs .codex-plugin .claude-plugin .cursor-plugin gemini-extension.json scripts tests
rg -n "<local-home>|<icloud-folder>|<private-documents-folder>|s[k]-[A-Za-z0-9]{20,}|xox[baprs]-|ghp_[A-Za-z0-9]" README.md AGENTS.md CHANGELOG.md docs .codex-plugin .claude-plugin .cursor-plugin .agents gemini-extension.json scripts tests references skills.sh.json
git diff --check
python3 scripts/install_codex_plugin.py --apply
codex plugin add avengers@personal
codex plugin list
codex exec --ephemeral --sandbox read-only --skip-git-repo-check -C /tmp 'Use $a-avengers-refresh from the installed Avengers plugin. In 3 short bullets, say what you would check for stale docs in a skill pack. Do not edit files.'
python3 scripts/install_symlinks.py --uninstall --home /tmp/avengers-empty-skill-home --skill a-avengers-setup
```

## Test Results

- Corpus search worked with the local config path.
- Skill pack validation passed with 112 skills and 112 manifest entries.
- Unit and simulation tests passed: 16 tests.
- JSON manifests parsed.
- Stale wording scan had no matches.
- Private path and token-pattern scan had no matches.
- `git diff --check` passed.
- Live Codex exec loaded `a-avengers-refresh` from the installed plugin cache and read the installed `SKILL.md`.

## Autoreview Result

First run found one accepted P2: the uninstall docs used a broad `a-*` delete example that could remove unrelated skills from a shared flat skill home.

Fix:

- Added `scripts/install_symlinks.py --uninstall`.
- Updated `docs/INSTALL.md` to use the safe uninstall command.
- Added a unit test covering foreign `a-*` links.

Final command:

```bash
autoreview --mode local
```

Final result:

```text
autoreview clean: no accepted/actionable findings reported
overall: patch is correct
```

## Decisions

- Keep Avengers as a skill-first pack rather than copying Compound Engineering's full subagent system.
- Add the compound memory loop in a public-safe form: learnings, run logs, refresh reports, templates, and handoffs.
- Keep source corpus private and searchable only through local config or environment variables.
- Use `CHANGELOG.md` for release history instead of adding release automation before there is a public release process.

## Known Limitations

- Codex printed unrelated global plugin warnings during live exec. Avengers still loaded correctly and no Avengers manifest icon paths were found.
- No GitHub push or tag was performed.
- ADR, security policy, support policy, and release automation remain future additions, not current blockers.

## Next Steps

1. Run final tests after this handoff note.
2. Run autoreview.
3. If clean, commit the docs, generator, skills, tests, and memory-layer changes together.
4. Push only when explicitly requested.

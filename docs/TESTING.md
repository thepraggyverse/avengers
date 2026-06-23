# Testing

Run all checks:

```bash
python3 scripts/doctor.py
```

The doctor runs the normal validation suite, JSON manifest parsing, stale wording scan, private path/token scan, diff whitespace check, and generated-cache check.

For focused checks:

```bash
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
```

## Generator Validation

Regenerate from the current manifest:

```bash
AVENGERS_CORPUS_DIR="/path/to/private/corpus" python3 scripts/generate_avengers_pack.py
```

Then verify the pack:

```bash
python3 scripts/validate_skill_pack.py
```

Expected output:

```text
Avengers skill pack validation passed.
Skills: 112
Manifest entries: 112
```

## What The Validator Checks

`scripts/validate_skill_pack.py` checks:

- 112 manifest entries.
- 112 skill directories.
- Manifest and directory names match.
- Plugin schema validation through the local Codex plugin validator when available.
- Every skill passes the local skill frontmatter validator when available.
- Every `pairs_with` link points to an existing skill.

## What Unit Tests Check

`tests/test_avengers_pack.py` checks:

- Manifest and directory counts.
- `a-*` hyphen-case names.
- Required `SKILL.md` sections, including inputs, examples, safety, and cross-harness notes.
- `agents/openai.yaml` interface metadata.
- Tier 1 orchestration and Avengers memory skills.
- Stark OS chain.
- Plugin manifest basics.
- Memory layer paths, schemas, and templates.
- Cross-harness metadata for Claude-compatible, Cursor, shared marketplace, and Gemini surfaces.
- Docs drift for README, install, support, security, versioning, Codex profiles, and CI.

`tests/test_skill_simulations.py` checks realistic routing prompts:

- permission / approval
- Mark 1 prototype
- mistake to upgrade
- cave resourcefulness
- multiple projects
- Civil War team split
- Peter Parker mentorship
- Ultron safety risk
- curse of knowledge
- source-grounded transcript lookup
- Iron Man 2 Easter eggs
- pack maintenance
- Avengers setup
- compound memory capture
- refresh report
- handoff
- context glossary

## Manual Route Simulations

```bash
python3 scripts/simulate_routes.py "This safety automation might become Ultron."
python3 scripts/simulate_routes.py "Set up Avengers for this repo in Codex."
python3 scripts/simulate_routes.py "Save what we learned from this Avengers run."
python3 scripts/simulate_routes.py "Audit stale Avengers memory notes."
python3 scripts/simulate_routes.py "Write a handoff for the next agent."
```

The simulator is deterministic and lightweight. It is not a replacement for real harness testing, but it catches weak triggers and broken routing assumptions.

## Harness Metadata Checks

After editing install surfaces, run:

```bash
python3 -m json.tool .codex-plugin/plugin.json >/dev/null
python3 -m json.tool .claude-plugin/plugin.json >/dev/null
python3 -m json.tool .claude-plugin/marketplace.json >/dev/null
python3 -m json.tool .cursor-plugin/plugin.json >/dev/null
python3 -m json.tool .cursor-plugin/marketplace.json >/dev/null
python3 -m json.tool .agents/plugins/marketplace.json >/dev/null
python3 -m json.tool gemini-extension.json >/dev/null
```

The doctor also parses the required JSON manifests:

```bash
python3 scripts/doctor.py --quick
```

## Stale Wording Checks

```bash
rg -n "[u]nofficial|10[7] A-prefixed|Skills: 10[7]|Manifest entries: 10[7]" README.md AGENTS.md docs .codex-plugin .claude-plugin .cursor-plugin gemini-extension.json scripts tests
```

Expected result: no matches, except legitimate references to the skill named `a-stark-operating-system`.

## Generator Preservation Check

After adding memory docs or skills:

```bash
git status --short
AVENGERS_CORPUS_DIR="/path/to/private/corpus" python3 scripts/generate_avengers_pack.py
git status --short
```

The generator may update generated skills, references, and generated docs. It should not delete:

- `.avengers/config.local.example.yaml`
- `docs/AVENGERS_MEMORY.md`
- `docs/AVENGERS_CONTEXT.md`
- `docs/avengers-memory/`
- `docs/HANDOFF.md`

## Diff Hygiene

```bash
git diff --check
find . \( -name '__pycache__' -o -name '*.pyc' -o -name '.DS_Store' \) -print
```

## CI

GitHub Actions runs the same doctor command on pushes to `main` and on pull requests:

```text
.github/workflows/ci.yml
```

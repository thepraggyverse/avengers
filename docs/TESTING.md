# Testing

Run all checks:

```bash
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
```

## What The Validator Checks

`scripts/validate_skill_pack.py` checks:

- 107 manifest entries.
- 107 skill directories.
- Manifest and directory names match.
- Plugin schema validation through the local Codex plugin validator when available.
- Every skill passes the local skill frontmatter validator when available.
- Every `pairs_with` link points to an existing skill.

## What Unit Tests Check

`tests/test_avengers_pack.py` checks:

- Manifest and directory counts.
- `a-*` hyphen-case names.
- Required `SKILL.md` sections.
- `agents/openai.yaml` interface metadata.
- Tier 1 orchestration set.
- Stark OS chain.
- Plugin manifest basics.

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

## Manual Route Simulation

```bash
python3 scripts/simulate_routes.py "This safety automation might become Ultron."
```

The simulator is deterministic and lightweight. It is not a replacement for real harness testing, but it catches weak triggers and broken routing assumptions.


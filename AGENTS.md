# Avengers Skill Pack

## Project Intent

Avengers is an unofficial public skill pack that exposes 107 A-prefixed skills for agent workflows inspired by Tony Stark, Iron Man, Avengers, MCU story analysis, leadership, risk, prototyping, resourcefulness, mentorship, and source-grounded knowledge work.

Keep the repo public-safe: do not add full transcripts, books, scripts, captions, private notes, secrets, or personal local paths.

## Structure

```text
.codex-plugin/plugin.json
skills/
references/
scripts/
tests/
docs/
```

## Important Rules

- Keep all skill names lowercase and `a-` prefixed.
- Keep every skill folder directly under `skills/`.
- Keep `SKILL.md` frontmatter to `name` and `description`.
- Keep `agents/openai.yaml` optional and under an `interface:` object.
- Keep source material outside the repo; use `AVENGERS_CORPUS_DIR` for local transcript search.
- Prefer updating `scripts/generate_avengers_pack.py` and regenerating over hand-editing generated skills.
- Do not commit `__pycache__`, local corpus files, secrets, or machine-specific install state.

## Verification

Run:

```bash
python3 scripts/generate_avengers_pack.py
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
```

If changing routing triggers, also run:

```bash
python3 scripts/simulate_routes.py "I keep waiting for approval before I start."
python3 scripts/simulate_routes.py "Break down Iron Man 2 Easter eggs."
```

## Publishing

Before pushing:

```bash
git status --short
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
```


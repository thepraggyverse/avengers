---
name: a-skill-pack-builder
description: Avengers skill A - Skill Pack Builder that helps the user to generate or refresh the Avengers plugin skill pack from the manifest. Use when the user mentions or needs one of these triggers - build skill pack, generate skills, plugin. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Skill Pack Builder

## Role

Tier 1 Knowledge System skill. Refresh the Avengers plugin from the manifest and verify the generated skills.

## Use When

- The user needs to generate or refresh the Avengers plugin skill pack from the manifest.
- The request matches these triggers: build skill pack, generate skills, plugin.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

## Do Not Use When

- The user only needs a quick direct answer.
- The requested action would copy large transcript passages instead of synthesizing.

## Workflow

1. Review `references/skill-manifest.json` for the intended skill set.
2. Run `scripts/generate_avengers_pack.py` after manifest changes.
3. Run `scripts/validate_skill_pack.py` to confirm count, schema, and skill validation.
4. Spot-check the router, Stark OS, one specialized skill, and one knowledge skill.
5. Report counts, validations, and remaining manual install or reload steps.

## Output Contract

Return these fields unless the user asks for another format:

- `Manifest Change`
- `Generated Count`
- `Validation Result`
- `Spot Checks`
- `Next Reload Step`

## Example

```text
Use $a-skill-pack-builder to turn this source material into searchable skill knowledge.
```

## Skill Chaining

- Pair with `a-knowledge-index-curator` when useful.
- Pair with `a-skill-pruner` when useful.
- Pair with `a-stark-router` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `10 Tony Stark Habits That Make You Unstoppable.txt` (366 words)
- `24 Mistakes that made Iron Man Stronger.txt` (1559 words)
- `AVENGERS Breakdown! Endgame Easter Eggs & New Details You Missed!  Infinity Saga Rewatch.txt` (3597 words)
- `AVENGERS INFINITY WAR Review & Analysis #NewRockstarsNews.txt` (10798 words)
- `Avengers Age of Ultron Breakdown! NEW Hidden Visual Details & Endgame Clues!.txt` (3510 words)
- `Avengers Endgame Breakdown! Details You Missed & New VFX Easter Eggs!  Infinity Saga Rewatch.txt` (5610 words)

## Safety And Grounding

- Keep answers synthesized and practical.
- Do not reproduce long copyrighted source passages.
- Keep private corpus paths, secrets, and local machine details out of committed artifacts.
- Mark speculation clearly when source grounding is thin.

## Cross-Harness Notes

- This skill is plain `SKILL.md` and should work through native plugins or flat skill-home symlinks.
- The A-prefixed name is intentional so searching for `A`, `a-`, or `Avengers` surfaces the pack.

## Self-Test

If asked to rebuild the pack, regenerate and validate rather than hand-editing individual generated files.

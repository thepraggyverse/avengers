---
name: a-cave-resourcefulness
description: Avengers skill A - Cave Resourcefulness that helps the user to use limited resources creatively under severe constraints. Use when the user mentions or needs one of these triggers - resourceful, limited resources, cave, constraint. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Cave Resourcefulness

## Role

Tier 2 Resourcefulness skill. Turn scarce materials, pressure, and constraints into a working escape path.

## Use When

- The user needs to use limited resources creatively under severe constraints.
- The request matches these triggers: resourceful, limited resources, cave, constraint.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. Name the escape condition or minimum win.
2. Inventory only what is already available.
3. Translate each item into functional attributes.
4. Combine attributes into a crude but useful build.
5. Choose the next move that changes the user's position.

## Output Contract

Return these fields unless the user asks for another format:

- `Escape Condition`
- `Available Parts`
- `Functional Attributes`
- `Crude Build`
- `Immediate Move`
- `Upgrade Later`

## Example

```text
Use $a-cave-resourcefulness to solve this with only the resources I already have.
```

## Skill Chaining

- Pair with `a-functional-attributes` when useful.
- Pair with `a-scrap-metal-solution` when useful.
- Pair with `a-mark-one-prototype` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `How Tony Stark Practices Resourcefulness.txt` (812 words)
- `IRON MAN BREAKDOWN! Tony Stark Armor Details We Missed!  The Deep Dive.txt` (7732 words)
- `What IRON MAN Teaches About SUCCESS 5 Life Lessons from Tony Stark.txt` (1159 words)

## Safety And Grounding

- Keep answers synthesized and practical.
- Do not reproduce long copyrighted source passages.
- Keep private corpus paths, secrets, and local machine details out of committed artifacts.
- Mark speculation clearly when source grounding is thin.

## Cross-Harness Notes

- This skill is plain `SKILL.md` and should work through native plugins or flat skill-home symlinks.
- The A-prefixed name is intentional so searching for `A`, `a-`, or `Avengers` surfaces the pack.

## Self-Test

If the user says they lack resources, find a viable move using only what they already have.

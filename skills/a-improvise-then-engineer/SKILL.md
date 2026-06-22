---
name: a-improvise-then-engineer
description: Avengers skill A - Improvise Then Engineer that helps the user to use a temporary hack first, then harden the real system. Use when the user mentions or needs one of these triggers - improvise, hack first, engineer later. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Improvise Then Engineer

## Role

Tier 2 Resourcefulness skill. Use a temporary hack first, then harden the real system.

## Use When

- The user needs to use a temporary hack first, then harden the real system.
- The request matches these triggers: improvise, hack first, engineer later.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. Inventory what already exists.
2. Translate each resource into functional attributes.
3. Recombine parts into a crude useful system.
4. Use the first version to escape waiting.
5. Upgrade only after the crude system teaches you.

## Output Contract

Return these fields unless the user asks for another format:

- `Goal`
- `Available Resources`
- `Functional Attributes`
- `Recombination`
- `First Build`
- `Upgrade Path`

## Example

```text
Use $a-improvise-then-engineer to solve this with only the resources I already have.
```

## Skill Chaining

- Pair with `a-cave-resourcefulness` when useful.
- Pair with `a-functional-attributes` when useful.

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

If the user asks for use a temporary hack first, then harden the real system., return the output contract fields and a concrete next action.

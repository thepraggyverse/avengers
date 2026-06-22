---
name: a-minimum-viable-armor
description: Avengers skill A - Minimum Viable Armor that helps the user to define the smallest protection or tool layer needed now. Use when the user mentions or needs one of these triggers - minimum viable armor, protection, enough safety. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Minimum Viable Armor

## Role

Tier 2 Resourcefulness skill. Define the smallest protection or tool layer needed now.

## Use When

- The user needs to define the smallest protection or tool layer needed now.
- The request matches these triggers: minimum viable armor, protection, enough safety.
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
Use $a-minimum-viable-armor to solve this with only the resources I already have.
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

If the user asks for define the smallest protection or tool layer needed now., return the output contract fields and a concrete next action.

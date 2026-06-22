---
name: a-mark-one-prototype
description: Avengers skill A - Mark One Prototype that helps the user to define the crude first working version that proves motion is possible. Use when the user mentions or needs one of these triggers - Mark 1, prototype, MVP, first version. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Mark One Prototype

## Role

Tier 2 Mistakes And Upgrades skill. Build the crude first version that proves motion is possible before polish, scale, or certainty.

## Use When

- The user needs to define the crude first working version that proves motion is possible.
- The request matches these triggers: Mark 1, prototype, MVP, first version.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. Name the mission and the one function the first version must perform.
2. List available parts, skills, time, tools, and constraints.
3. Remove every feature that is not needed for the first proof.
4. Define the ugly working build the user can finish next.
5. Choose the first test and the weakness it is likely to reveal.
6. Capture what the Mark 2 should fix.

## Output Contract

Return these fields unless the user asks for another format:

- `Mission`
- `Essential Function`
- `Available Parts`
- `Mark 1 Build`
- `First Test`
- `Known Weaknesses`
- `Mark 2 Upgrade`

## Example

```text
Use $a-mark-one-prototype to convert this failure into the next upgrade.
```

## Skill Chaining

- Pair with `a-cave-resourcefulness` when useful.
- Pair with `a-mark-two-test-flight` when useful.
- Pair with `a-mistake-to-upgrade` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `Every Time Iron Man Learned from his Mistakes.txt` (2640 words)
- `24 Mistakes that made Iron Man Stronger.txt` (1559 words)
- `Iron Man Armor Evolution! Suit Upgrade Breakdown! (Mark 1 - Mark 85).txt` (1798 words)

## Safety And Grounding

- Keep answers synthesized and practical.
- Do not reproduce long copyrighted source passages.
- Keep private corpus paths, secrets, and local machine details out of committed artifacts.
- Mark speculation clearly when source grounding is thin.

## Cross-Harness Notes

- This skill is plain `SKILL.md` and should work through native plugins or flat skill-home symlinks.
- The A-prefixed name is intentional so searching for `A`, `a-`, or `Avengers` surfaces the pack.

## Self-Test

If the user is waiting for perfect conditions, define a crude useful artifact they can build immediately.

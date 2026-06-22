---
name: a-salvage-tech-strategy
description: Avengers skill A - Salvage Tech Strategy that helps the user to recover old assets, abandoned work, or scraps into useful inputs. Use when the user mentions or needs one of these triggers - salvage, reuse old work, abandoned assets. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Salvage Tech Strategy

## Role

Tier 2 Resourcefulness skill. Recover old assets, abandoned work, or scraps into useful inputs.

## Use When

- The user needs to recover old assets, abandoned work, or scraps into useful inputs.
- The request matches these triggers: salvage, reuse old work, abandoned assets.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

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

## Skill Chaining

- Pair with `a-cave-resourcefulness` when useful.
- Pair with `a-functional-attributes` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `How Tony Stark Practices Resourcefulness.txt` (812 words)
- `IRON MAN BREAKDOWN! Tony Stark Armor Details We Missed!  The Deep Dive.txt` (7732 words)
- `What IRON MAN Teaches About SUCCESS 5 Life Lessons from Tony Stark.txt` (1159 words)

## Self-Test

If the user asks for recover old assets, abandoned work, or scraps into useful inputs., return the output contract fields and a concrete next action.

---
name: a-suit-tech-catalog
description: Avengers skill A - Suit Tech Catalog that helps the user to catalog armor, tools, capabilities, weaknesses, and upgrade lessons. Use when the user mentions or needs one of these triggers - suit catalog, armor, Mark 85. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Suit Tech Catalog

## Role

Tier 3 Armor Tech Product Design skill. Catalog armor, tools, capabilities, weaknesses, and upgrade lessons.

## Use When

- The user needs to catalog armor, tools, capabilities, weaknesses, and upgrade lessons.
- The request matches these triggers: suit catalog, armor, Mark 85.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. Start with the human operator's need.
2. Define the armor function, not just the shiny feature.
3. Find the weakness in the current version.
4. Add interface and fallback decisions.
5. Specify the next Mark upgrade.

## Output Contract

Return these fields unless the user asks for another format:

- `Operator Need`
- `Armor Function`
- `Weakness`
- `Interface Decision`
- `Fallback`
- `Next Upgrade`

## Skill Chaining

- Use `a-stark-router` if another Avengers skill may fit better.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `Iron Man Armor Evolution! Suit Upgrade Breakdown! (Mark 1 - Mark 85).txt` (1798 words)
- `IRON MAN 2 Breakdown! Easter Eggs & MCU Phase 4 Connections!  Infinity Saga Rewatch.txt` (3109 words)
- `IRON MAN 3 (2013) REVISITED  Road to Doomsday #18.txt` (12530 words)

## Self-Test

If the user asks for catalog armor, tools, capabilities, weaknesses, and upgrade lessons., return the output contract fields and a concrete next action.

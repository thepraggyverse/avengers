---
name: a-failure-memory-bank
description: Avengers skill A - Failure Memory Bank that helps the user to store mistakes as reusable memory instead of private regret. Use when the user mentions or needs one of these triggers - mistake log, lessons, memory bank, retrospective. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Failure Memory Bank

## Role

Tier 2 Mistakes And Upgrades skill. Store mistakes as reusable memory instead of private regret.

## Use When

- The user needs to store mistakes as reusable memory instead of private regret.
- The request matches these triggers: mistake log, lessons, memory bank, retrospective.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. Describe the failure without self-protection.
2. Identify the specific weakness the failure exposed.
3. Design one upgrade that would have prevented or reduced it.
4. Test the upgrade with a realistic stress case.
5. Save the prevention rule for future work.

## Output Contract

Return these fields unless the user asks for another format:

- `Failure`
- `What It Revealed`
- `System Weakness`
- `Upgrade`
- `Test`
- `Prevention Rule`

## Skill Chaining

- Pair with `a-mistake-to-upgrade` when useful.
- Pair with `a-anti-repeat-control` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `Every Time Iron Man Learned from his Mistakes.txt` (2640 words)
- `24 Mistakes that made Iron Man Stronger.txt` (1559 words)
- `Iron Man Armor Evolution! Suit Upgrade Breakdown! (Mark 1 - Mark 85).txt` (1798 words)

## Self-Test

If the user asks for store mistakes as reusable memory instead of private regret., return the output contract fields and a concrete next action.

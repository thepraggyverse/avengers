---
name: a-anti-repeat-control
description: Avengers skill A - Anti Repeat Control that helps the user to add controls that prevent the same failure from recurring. Use when the user mentions or needs one of these triggers - prevent repeat, control, guardrail, recurrence. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Anti Repeat Control

## Role

Tier 2 Mistakes And Upgrades skill. Add controls that prevent the same failure from recurring.

## Use When

- The user needs to add controls that prevent the same failure from recurring.
- The request matches these triggers: prevent repeat, control, guardrail, recurrence.
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

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `Every Time Iron Man Learned from his Mistakes.txt` (2640 words)
- `24 Mistakes that made Iron Man Stronger.txt` (1559 words)
- `Iron Man Armor Evolution! Suit Upgrade Breakdown! (Mark 1 - Mark 85).txt` (1798 words)

## Self-Test

If the user asks for add controls that prevent the same failure from recurring., return the output contract fields and a concrete next action.

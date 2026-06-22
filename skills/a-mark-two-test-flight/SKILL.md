---
name: a-mark-two-test-flight
description: Avengers skill A - Mark Two Test Flight that helps the user to plan the first serious test and capture what the next version must fix. Use when the user mentions or needs one of these triggers - test flight, Mark 2, first test, validate. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Mark Two Test Flight

## Role

Tier 2 Mistakes And Upgrades skill. Design the first serious test of a prototype and convert the result into the next suit upgrade.

## Use When

- The user needs to plan the first serious test and capture what the next version must fix.
- The request matches these triggers: test flight, Mark 2, first test, validate.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. Identify what the Mark 1 claims to prove.
2. Create a realistic test that stresses the claim.
3. Define what success, partial success, and failure mean.
4. Run or outline the smallest possible test.
5. Translate the result into a Mark 2 upgrade.

## Output Contract

Return these fields unless the user asks for another format:

- `Prototype Claim`
- `Test Environment`
- `Success Signal`
- `Failure Signal`
- `Observed Weakness`
- `Mark 2 Upgrade`

## Skill Chaining

- Pair with `a-mark-one-prototype` when useful.
- Pair with `a-icing-problem-review` when useful.
- Pair with `a-upgrade-chain-mapper` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `Every Time Iron Man Learned from his Mistakes.txt` (2640 words)
- `24 Mistakes that made Iron Man Stronger.txt` (1559 words)
- `Iron Man Armor Evolution! Suit Upgrade Breakdown! (Mark 1 - Mark 85).txt` (1798 words)

## Self-Test

If the user has a first draft or MVP, produce a concrete stress test and next upgrade.

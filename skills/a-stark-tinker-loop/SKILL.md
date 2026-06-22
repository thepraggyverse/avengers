---
name: a-stark-tinker-loop
description: Avengers skill A - Stark Tinker Loop that helps the user to use tinkering as a disciplined observe-modify-test cycle. Use when the user mentions or needs one of these triggers - tinker, experiment, prototype loop, workshop. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Stark Tinker Loop

## Role

Tier 2 Tony Stark Core skill. Use tinkering as a disciplined observe-modify-test cycle.

## Use When

- The user needs to use tinkering as a disciplined observe-modify-test cycle.
- The request matches these triggers: tinker, experiment, prototype loop, workshop.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. Name the mission in one sentence.
2. Strip away theatre, ego, and inherited assumptions.
3. Define the smallest artifact that can prove progress.
4. Add feedback, test, or telemetry before scaling.
5. Capture the next upgrade as a concrete action.

## Output Contract

Return these fields unless the user asks for another format:

- `Situation`
- `Stark Lens`
- `Primary Move`
- `Build Step`
- `Feedback Loop`
- `Next Upgrade`

## Skill Chaining

- Pair with `a-stark-router` when useful.
- Pair with `a-stark-operating-system` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `How to Work Like Tony Stark.txt` (1290 words)
- `10 Tony Stark Habits That Make You Unstoppable.txt` (366 words)
- `IRON MAN BREAKDOWN! Tony Stark Armor Details We Missed!  The Deep Dive.txt` (7732 words)

## Self-Test

If the user asks for use tinkering as a disciplined observe-modify-test cycle., return the output contract fields and a concrete next action.

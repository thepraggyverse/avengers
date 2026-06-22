---
name: a-stark-build-before-you-believe
description: Avengers skill A - Stark Build Before You Believe that helps the user to create proof through action before confidence arrives. Use when the user mentions or needs one of these triggers - stuck, need proof, build first, confidence through evidence. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Stark Build Before You Believe

## Role

Tier 2 Tony Stark Core skill. Create proof through action before confidence arrives.

## Use When

- The user needs to create proof through action before confidence arrives.
- The request matches these triggers: stuck, need proof, build first, confidence through evidence.
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

If the user asks for create proof through action before confidence arrives., return the output contract fields and a concrete next action.

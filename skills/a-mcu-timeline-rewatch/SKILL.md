---
name: a-mcu-timeline-rewatch
description: Avengers skill A - MCU Timeline Rewatch that helps the user to place events, callbacks, and character moves in MCU timeline context. Use when the user mentions or needs one of these triggers - MCU timeline, rewatch, continuity, later MCU connections, Iron Man 2. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - MCU Timeline Rewatch

## Role

Tier 4 MCU Story Analysis skill. Place events, callbacks, and character moves in MCU timeline context.

## Use When

- The user needs to place events, callbacks, and character moves in MCU timeline context.
- The request matches these triggers: MCU timeline, rewatch, continuity, later MCU connections, Iron Man 2.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Do Not Use When

- The user needs personal productivity coaching rather than story analysis.
- The answer would rely on unsourced speculation presented as fact.

## Workflow

1. Identify the source, scene, or transcript segment.
2. Extract the visible detail or callback.
3. Connect it to character arc, theme, or continuity.
4. Separate grounded evidence from speculation.
5. State the practical lesson or theory hook.

## Output Contract

Return these fields unless the user asks for another format:

- `Source`
- `Scene or Thread`
- `Callback`
- `Character Meaning`
- `MCU Connection`
- `Practical Lesson`

## Skill Chaining

- Pair with `a-mcu-easter-egg-breakdown` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `IRON MAN 2 Breakdown! Easter Eggs & MCU Phase 4 Connections!  Infinity Saga Rewatch.txt` (3109 words)
- `IRON MAN 2 REVISITED  Road to Doomsday Episode 12.txt` (13611 words)
- `AVENGERS Breakdown! Endgame Easter Eggs & New Details You Missed!  Infinity Saga Rewatch.txt` (3597 words)
- `Avengers Infinity War Breakdown! NEW EASTER EGGS FOUND!  Infinity Saga Rewatch.txt` (3768 words)
- `Avengers Endgame Breakdown! Details You Missed & New VFX Easter Eggs!  Infinity Saga Rewatch.txt` (5610 words)
- `IRON MAN (2008) REVISITED  Road to Doomsday Episode 7.txt` (16847 words)

## Self-Test

If the user asks for place events, callbacks, and character moves in mcu timeline context., return the output contract fields and a concrete next action.

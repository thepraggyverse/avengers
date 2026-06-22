---
name: a-new-mask-same-task
description: Avengers skill A - New Mask Same Task that helps the user to compare Tony Stark and Doctor Doom parallels around task, mask, and control. Use when the user mentions or needs one of these triggers - new mask same task, Doom, Tony parallel. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - New Mask Same Task

## Role

Tier 4 MCU Story Analysis skill. Compare Tony Stark and Doctor Doom parallels around task, mask, and control.

## Use When

- The user needs to compare Tony Stark and Doctor Doom parallels around task, mask, and control.
- The request matches these triggers: new mask same task, Doom, Tony parallel.
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

- Pair with `a-mcu-timeline-rewatch` when useful.
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

If the user asks for compare tony stark and doctor doom parallels around task, mask, and control., return the output contract fields and a concrete next action.

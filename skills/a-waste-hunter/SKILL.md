---
name: a-waste-hunter
description: Avengers skill A - Waste Hunter that helps the user to find and remove wasted motion, waiting, rework, and clutter. Use when the user mentions or needs one of these triggers - waste, inefficiency, remove waste. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Waste Hunter

## Role

Tier 2 Lean Six Sigma Workflow skill. Find and remove wasted motion, waiting, rework, and clutter.

## Use When

- The user needs to find and remove wasted motion, waiting, rework, and clutter.
- The request matches these triggers: waste, inefficiency, remove waste.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. Define the process and its intended output.
2. Measure where waste, variation, or rework appears.
3. Improve the highest-leverage step.
4. Add a lightweight control so the improvement survives.
5. Schedule the next review.

## Output Contract

Return these fields unless the user asks for another format:

- `Process`
- `Waste or Variation`
- `Measure`
- `Improve`
- `Control`
- `Review Cadence`

## Skill Chaining

- Use `a-stark-router` if another Avengers skill may fit better.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `How Tony Stark Uses Lean and Six-Sigma.txt` (1245 words)
- `How to Work Like Tony Stark.txt` (1290 words)
- `How Tony Stark Works on Multiple Projects at Once.txt` (1915 words)

## Self-Test

If the user asks for find and remove wasted motion, waiting, rework, and clutter., return the output contract fields and a concrete next action.

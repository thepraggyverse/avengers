---
name: a-continuous-improvement-loop
description: Avengers skill A - Continuous Improvement Loop that helps the user to create a recurring loop for better versions of work. Use when the user mentions or needs one of these triggers - continuous improvement, weekly improvement. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Continuous Improvement Loop

## Role

Tier 2 Lean Six Sigma Workflow skill. Create a recurring loop for better versions of work.

## Use When

- The user needs to create a recurring loop for better versions of work.
- The request matches these triggers: continuous improvement, weekly improvement.
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

If the user asks for create a recurring loop for better versions of work., return the output contract fields and a concrete next action.

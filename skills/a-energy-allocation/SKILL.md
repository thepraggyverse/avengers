---
name: a-energy-allocation
description: Avengers skill A - Energy Allocation that helps the user to match tasks to current energy, attention, and leverage. Use when the user mentions or needs one of these triggers - energy, what today, attention. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Energy Allocation

## Role

Tier 2 Multiple Projects skill. Match tasks to current energy, attention, and leverage.

## Use When

- The user needs to match tasks to current energy, attention, and leverage.
- The request matches these triggers: energy, what today, attention.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. List active projects and their next meaningful output.
2. Identify the reactor core that must not lose power.
3. Separate parallel tracks from blocked tracks.
4. Set context-switching rules.
5. Update the portfolio radar.

## Output Contract

Return these fields unless the user asks for another format:

- `Project Set`
- `Reactor Core`
- `Parallel Tracks`
- `Switching Rule`
- `Energy Match`
- `Radar Update`

## Skill Chaining

- Use `a-stark-router` if another Avengers skill may fit better.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `How Tony Stark Works on Multiple Projects at Once.txt` (1915 words)
- `How Tony Stark Uses Lean and Six-Sigma.txt` (1245 words)
- `10 Tony Stark Habits That Make You Unstoppable.txt` (366 words)

## Self-Test

If the user asks for match tasks to current energy, attention, and leverage., return the output contract fields and a concrete next action.

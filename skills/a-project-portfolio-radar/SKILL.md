---
name: a-project-portfolio-radar
description: Avengers skill A - Project Portfolio Radar that helps the user to maintain a radar view of active bets, status, and next moves. Use when the user mentions or needs one of these triggers - portfolio radar, active projects. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Project Portfolio Radar

## Role

Tier 2 Multiple Projects skill. Maintain a radar view of active bets, status, and next moves.

## Use When

- The user needs to maintain a radar view of active bets, status, and next moves.
- The request matches these triggers: portfolio radar, active projects.
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

If the user asks for maintain a radar view of active bets, status, and next moves., return the output contract fields and a concrete next action.

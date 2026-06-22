---
name: a-constraint-inventory
description: Avengers skill A - Constraint Inventory that helps the user to list hard constraints, movable constraints, resources, and missing parts. Use when the user mentions or needs one of these triggers - constraints, resources, limits, available parts. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Constraint Inventory

## Role

Tier 2 Problem Solving skill. List hard constraints, movable constraints, resources, and missing parts.

## Use When

- The user needs to list hard constraints, movable constraints, resources, and missing parts.
- The request matches these triggers: constraints, resources, limits, available parts.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. Stabilize the situation before optimizing.
2. Name the actual problem separately from symptoms.
3. Inventory constraints, resources, risks, and dependencies.
4. Pick the next reversible move.
5. Check whether the move changed the real problem.

## Output Contract

Return these fields unless the user asks for another format:

- `Situation`
- `Actual Problem`
- `Constraints`
- `Available Parts`
- `First Move`
- `Next Check`

## Skill Chaining

- Use `a-stark-router` if another Avengers skill may fit better.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `How to Work the Problem.txt`
- `How to Work Like Tony Stark.txt` (1290 words)
- `IRON MAN BREAKDOWN! Tony Stark Armor Details We Missed!  The Deep Dive.txt` (7732 words)

## Self-Test

If the user asks for list hard constraints, movable constraints, resources, and missing parts., return the output contract fields and a concrete next action.

---
name: a-stark-operating-system
description: Avengers skill A - Stark Operating System that helps the user to run the full Tony Stark operating loop from intent to prototype to upgrade. Use when the user mentions or needs one of these triggers - Stark OS, full workflow, Tony operating system, end-to-end build loop. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Stark Operating System

## Role

Tier 1 Tony Stark Core skill. Run the complete Stark loop: permission, prototype, feedback, upgrade, ethics, and handoff.

## Use When

- The user needs to run the full Tony Stark operating loop from intent to prototype to upgrade.
- The request matches these triggers: Stark OS, full workflow, Tony operating system, end-to-end build loop.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. Break the user's objective into mission, constraints, available resources, and risk.
2. Run permission-trap detection if the user is waiting.
3. Define the Mark 1 artifact and first test.
4. Convert likely failure into upgrade rules.
5. Check for overcontrol, delegation, and handoff needs.
6. Return a staged plan with the next concrete action.

## Output Contract

Return these fields unless the user asks for another format:

- `Mission`
- `Current Block`
- `Mark 1`
- `Feedback Test`
- `Upgrade Rule`
- `Risk Check`
- `Next Action`

## Skill Chaining

- Pair with `a-permission-trap-breaker` when useful.
- Pair with `a-mark-one-prototype` when useful.
- Pair with `a-mistake-to-upgrade` when useful.
- Pair with `a-armor-around-world-check` when useful.
- Pair with `a-legacy-through-mentees` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `How to Work Like Tony Stark.txt` (1290 words)
- `10 Tony Stark Habits That Make You Unstoppable.txt` (366 words)
- `IRON MAN BREAKDOWN! Tony Stark Armor Details We Missed!  The Deep Dive.txt` (7732 words)

## Self-Test

If the user asks for the full Stark OS, produce a staged build-and-upgrade plan, not a motivational essay.

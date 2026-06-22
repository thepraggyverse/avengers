---
name: a-stark-first-principles
description: Avengers skill A - Stark First Principles that helps the user to strip a challenge to constraints, physics, incentives, and actual facts. Use when the user mentions or needs one of these triggers - first principles, assumptions, what is true, fundamentals. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Stark First Principles

## Role

Tier 2 Tony Stark Core skill. Strip a challenge to constraints, physics, incentives, and actual facts.

## Use When

- The user needs to strip a challenge to constraints, physics, incentives, and actual facts.
- The request matches these triggers: first principles, assumptions, what is true, fundamentals.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

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

## Example

```text
Use $a-stark-first-principles to turn this vague objective into a practical Stark-style operating mode.
```

## Skill Chaining

- Pair with `a-stark-router` when useful.
- Pair with `a-stark-operating-system` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `How to Work Like Tony Stark.txt` (1290 words)
- `10 Tony Stark Habits That Make You Unstoppable.txt` (366 words)
- `IRON MAN BREAKDOWN! Tony Stark Armor Details We Missed!  The Deep Dive.txt` (7732 words)

## Safety And Grounding

- Keep answers synthesized and practical.
- Do not reproduce long copyrighted source passages.
- Keep private corpus paths, secrets, and local machine details out of committed artifacts.
- Mark speculation clearly when source grounding is thin.

## Cross-Harness Notes

- This skill is plain `SKILL.md` and should work through native plugins or flat skill-home symlinks.
- The A-prefixed name is intentional so searching for `A`, `a-`, or `Avengers` surfaces the pack.

## Self-Test

If the user asks for strip a challenge to constraints, physics, incentives, and actual facts., return the output contract fields and a concrete next action.

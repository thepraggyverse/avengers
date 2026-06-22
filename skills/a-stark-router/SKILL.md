---
name: a-stark-router
description: Avengers skill A - Stark Router that helps the user to choose the right Avengers skill or skill chain for a broad problem. Use when the user mentions or needs one of these triggers - routing, skill choice, Avengers mode selection, broad Tony Stark guidance. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Stark Router

## Role

Tier 1 Tony Stark Core skill. Act as the JARVIS-style routing layer for the Avengers skill system.

## Use When

- The user needs to choose the right Avengers skill or skill chain for a broad problem.
- The request matches these triggers: routing, skill choice, Avengers mode selection, broad Tony Stark guidance.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. Read the user's request and identify the dominant problem type.
2. Recommend one to three A-prefixed skills.
3. Explain why each skill fits in one short line.
4. If the first skill is obvious, apply it immediately.
5. If the user asks for a system, chain skills rather than choosing only one.

## Output Contract

Return these fields unless the user asks for another format:

- `Request`
- `Best Skill`
- `Supporting Skills`
- `Why`
- `First Applied Move`

## Example

```text
Use $a-stark-router to turn this vague objective into a practical Stark-style operating mode.
```

## Skill Chaining

- Pair with `a-stark-operating-system` when useful.
- Pair with `a-knowledge-index-curator` when useful.
- Pair with `a-source-grounded-synthesis` when useful.

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

If the user asks 'Which Avengers mode fits this problem?', recommend 1-3 skills and apply the strongest one.

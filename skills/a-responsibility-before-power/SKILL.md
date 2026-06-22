---
name: a-responsibility-before-power
description: Avengers skill A - Responsibility Before Power that helps the user to check readiness before handing over power, tools, or visibility. Use when the user mentions or needs one of these triggers - responsibility before power, readiness. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Responsibility Before Power

## Role

Tier 3 Mentorship And Peter Parker skill. Check readiness before handing over power, tools, or visibility.

## Use When

- The user needs to check readiness before handing over power, tools, or visibility.
- The request matches these triggers: responsibility before power, readiness.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

## Do Not Use When

- The user is not guiding another person or their own apprentice-like learning loop.

## Workflow

1. Clarify what the mentee is trying to become capable of doing.
2. Assess readiness with behavior, not potential alone.
3. Choose support level: watch, coach, unlock, or step back.
4. Avoid projecting the mentor's fear onto the mentee.
5. Create a growth test with real consequences and guardrails.

## Output Contract

Return these fields unless the user asks for another format:

- `Mentee Context`
- `Power or Tool`
- `Readiness Signal`
- `Support Level`
- `Boundary`
- `Growth Test`

## Example

```text
Use $a-responsibility-before-power to mentor this junior builder without overcontrolling them.
```

## Skill Chaining

- Pair with `a-peter-parker-mentor` when useful.
- Pair with `a-training-wheels-protocol` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `SPIDERMAN HOMECOMING Breakdown! New Hidden Easter Eggs Revealed!.txt` (3819 words)
- `Spider-Man Far From Home Breakdown! NEW Easter Eggs You Missed!  Infinity Saga Rewatch.txt` (3690 words)
- `SPIDERMAN NO WAY HOME BREAKDOWN! Easter Eggs & Details You Missed!.txt` (7482 words)

## Safety And Grounding

- Keep answers synthesized and practical.
- Do not reproduce long copyrighted source passages.
- Keep private corpus paths, secrets, and local machine details out of committed artifacts.
- Mark speculation clearly when source grounding is thin.

## Cross-Harness Notes

- This skill is plain `SKILL.md` and should work through native plugins or flat skill-home symlinks.
- The A-prefixed name is intentional so searching for `A`, `a-`, or `Avengers` surfaces the pack.

## Self-Test

If the user asks for check readiness before handing over power, tools, or visibility., return the output contract fields and a concrete next action.

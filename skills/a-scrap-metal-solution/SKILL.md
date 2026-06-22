---
name: a-scrap-metal-solution
description: Avengers skill A - Scrap Metal Solution that helps the user to design a solution from available scraps before buying or waiting. Use when the user mentions or needs one of these triggers - scrap metal, limited tools, available materials, workaround. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Scrap Metal Solution

## Role

Tier 2 Problem Solving skill. Design a solution from available scraps before buying or waiting.

## Use When

- The user needs to design a solution from available scraps before buying or waiting.
- The request matches these triggers: scrap metal, limited tools, available materials, workaround.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

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

## Example

```text
Use $a-scrap-metal-solution on this messy situation and give me the next concrete move.
```

## Skill Chaining

- Use `a-stark-router` if another Avengers skill may fit better.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `How to Work the Problem.txt`
- `How to Work Like Tony Stark.txt` (1290 words)
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

If the user asks for design a solution from available scraps before buying or waiting., return the output contract fields and a concrete next action.

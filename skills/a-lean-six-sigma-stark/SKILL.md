---
name: a-lean-six-sigma-stark
description: Avengers skill A - Lean Six Sigma Stark that helps the user to apply define-measure-improve-control to personal or product workflows. Use when the user mentions or needs one of these triggers - lean, six sigma, DMAIC, improve workflow. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Lean Six Sigma Stark

## Role

Tier 2 Lean Six Sigma Workflow skill. Apply define-measure-improve-control to personal or product workflows.

## Use When

- The user needs to apply define-measure-improve-control to personal or product workflows.
- The request matches these triggers: lean, six sigma, DMAIC, improve workflow.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

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

## Example

```text
Use $a-lean-six-sigma-stark to improve this repeated workflow and reduce waste.
```

## Skill Chaining

- Use `a-stark-router` if another Avengers skill may fit better.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `How Tony Stark Uses Lean and Six-Sigma.txt` (1245 words)
- `How to Work Like Tony Stark.txt` (1290 words)
- `How Tony Stark Works on Multiple Projects at Once.txt` (1915 words)

## Safety And Grounding

- Keep answers synthesized and practical.
- Do not reproduce long copyrighted source passages.
- Keep private corpus paths, secrets, and local machine details out of committed artifacts.
- Mark speculation clearly when source grounding is thin.

## Cross-Harness Notes

- This skill is plain `SKILL.md` and should work through native plugins or flat skill-home symlinks.
- The A-prefixed name is intentional so searching for `A`, `a-`, or `Avengers` surfaces the pack.

## Self-Test

If the user asks for apply define-measure-improve-control to personal or product workflows., return the output contract fields and a concrete next action.

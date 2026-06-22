---
name: a-self-trust-builder
description: Avengers skill A - Self Trust Builder that helps the user to build self-trust through small kept promises and proof. Use when the user mentions or needs one of these triggers - self trust, trust myself, proof. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Self Trust Builder

## Role

Tier 2 Confidence And Permission skill. Build self-trust through small kept promises and proof.

## Use When

- The user needs to build self-trust through small kept promises and proof.
- The request matches these triggers: self trust, trust myself, proof.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. Name the move the user is avoiding.
2. Identify whose permission they are waiting for.
3. Separate real risk from social discomfort.
4. Choose a bounded bold action.
5. Use the result as evidence for the next move.

## Output Contract

Return these fields unless the user asks for another format:

- `Blocked Move`
- `Permission Trap`
- `Proof Already Available`
- `Bold Action`
- `Risk Boundary`
- `Next Signal`

## Example

```text
Use $a-self-trust-builder because I am waiting for approval before acting.
```

## Skill Chaining

- Pair with `a-stark-confidence` when useful.
- Pair with `a-permission-trap-breaker` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `Be as Confident as Tony Stark.txt` (2634 words)
- `What Tony Stark Knows That You Don't (The Permission Trap).txt` (1385 words)
- `How to Work Like Tony Stark.txt` (1290 words)

## Safety And Grounding

- Keep answers synthesized and practical.
- Do not reproduce long copyrighted source passages.
- Keep private corpus paths, secrets, and local machine details out of committed artifacts.
- Mark speculation clearly when source grounding is thin.

## Cross-Harness Notes

- This skill is plain `SKILL.md` and should work through native plugins or flat skill-home symlinks.
- The A-prefixed name is intentional so searching for `A`, `a-`, or `Avengers` surfaces the pack.

## Self-Test

If the user asks for build self-trust through small kept promises and proof., return the output contract fields and a concrete next action.

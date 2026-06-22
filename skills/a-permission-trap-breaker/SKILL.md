---
name: a-permission-trap-breaker
description: Avengers skill A - Permission Trap Breaker that helps the user to find where the user is waiting for permission and define action without it. Use when the user mentions or needs one of these triggers - permission trap, waiting, approval, realistic. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Permission Trap Breaker

## Role

Tier 2 Confidence And Permission skill. Find the hidden request for approval and replace it with a bounded act of agency.

## Use When

- The user needs to find where the user is waiting for permission and define action without it.
- The request matches these triggers: permission trap, waiting, approval, realistic.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. Name the action the user keeps postponing.
2. Identify whose approval, validation, credential, or perfect condition they are waiting for.
3. Separate legal, ethical, and practical risk from social discomfort.
4. Define one safe-to-try move that does not require permission.
5. Turn the result into proof for the next move.

## Output Contract

Return these fields unless the user asks for another format:

- `Postponed Action`
- `Permission Source`
- `Real Risk`
- `False Gate`
- `Bounded Move`
- `Proof Signal`

## Example

```text
Use $a-permission-trap-breaker because I am waiting for approval before acting.
```

## Skill Chaining

- Pair with `a-stark-confidence` when useful.
- Pair with `a-fear-to-motion` when useful.
- Pair with `a-mark-one-prototype` when useful.

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

If the user is waiting to be chosen, return a bounded action they can take without external validation.

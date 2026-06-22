---
name: a-knowledge-gap-map
description: Avengers skill A - Knowledge Gap Map that helps the user to identify the exact missing knowledge blocking progress. Use when the user mentions or needs one of these triggers - knowledge gaps, what do I not know. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Knowledge Gap Map

## Role

Tier 2 Learning And Intelligence skill. Identify the exact missing knowledge blocking progress.

## Use When

- The user needs to identify the exact missing knowledge blocking progress.
- The request matches these triggers: knowledge gaps, what do I not know.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. Choose a target capability.
2. Map what the user already understands.
3. Identify the smallest missing concept or skill.
4. Build something that forces the concept to become concrete.
5. Synthesize the lesson into a reusable rule.

## Output Contract

Return these fields unless the user asks for another format:

- `Learning Goal`
- `Known Base`
- `Knowledge Gap`
- `Build-to-Learn Task`
- `Synthesis Question`
- `Mastery Check`

## Example

```text
Use $a-knowledge-gap-map to create a build-first learning plan for this topic.
```

## Skill Chaining

- Pair with `a-learn-like-stark` when useful.
- Pair with `a-build-to-understand` when useful.
- Pair with `a-knowledge-index-curator` when useful.
- Pair with `a-source-grounded-synthesis` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `Become Smart like Tony Stark  In-Depth Analysis.txt` (1693 words)
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

If the user asks for identify the exact missing knowledge blocking progress., return the output contract fields and a concrete next action.

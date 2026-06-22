---
name: a-avengers-compound
description: Avengers skill A - Avengers Compound that helps the user to capture a reusable lesson after an Avengers run so the next run is easier. Use when the user mentions or needs one of these triggers - compound learning, reusable lesson, save learning, after run, memory note. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Avengers Compound

## Role

Tier 1 Avengers Memory skill. Capture a solved Avengers run as reusable memory with source hooks, related skills, and refresh status.

## Use When

- The user needs to capture a reusable lesson after an Avengers run so the next run is easier.
- The request matches these triggers: compound learning, reusable lesson, save learning, after run, memory note.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

## Do Not Use When

- The task is a one-off answer with no reusable lesson, setup, refresh, context, or handoff value.
- The user explicitly asks not to write memory, logs, or handoff artifacts.

## Workflow

1. Decide whether the run produced a reusable lesson worth saving.
2. Capture the request, selected skills, source files, decision or result, and reusable lesson.
3. Write the note with the learning-note schema under `docs/avengers-memory/learnings/` when repository memory is allowed.
4. Link related A-skills and mark confidence and refresh status.
5. Update context or handoff docs only when the lesson changes future behavior.

## Output Contract

Return these fields unless the user asks for another format:

- `Request`
- `Selected Skills`
- `Sources Consulted`
- `Decision or Result`
- `Reusable Lesson`
- `Related Skills`
- `Refresh Status`

## Example

```text
Use $a-avengers-compound to save the reusable lesson from this run with related skills and refresh status.
```

## Skill Chaining

- Pair with `a-avengers-refresh` when useful.
- Pair with `a-avengers-context` when useful.
- Pair with `a-failure-memory-bank` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `10 Tony Stark Habits That Make You Unstoppable.txt` (366 words)
- `24 Mistakes that made Iron Man Stronger.txt` (1559 words)
- `AVENGERS Breakdown! Endgame Easter Eggs & New Details You Missed!  Infinity Saga Rewatch.txt` (3597 words)
- `AVENGERS INFINITY WAR Review & Analysis #NewRockstarsNews.txt` (10798 words)
- `Avengers Age of Ultron Breakdown! NEW Hidden Visual Details & Endgame Clues!.txt` (3510 words)
- `Avengers Endgame Breakdown! Details You Missed & New VFX Easter Eggs!  Infinity Saga Rewatch.txt` (5610 words)

## Safety And Grounding

- Keep answers synthesized and practical.
- Do not reproduce long copyrighted source passages.
- Keep private corpus paths, secrets, and local machine details out of committed artifacts.
- Mark speculation clearly when source grounding is thin.

## Cross-Harness Notes

- This skill is plain `SKILL.md` and should work through native plugins or flat skill-home symlinks.
- The A-prefixed name is intentional so searching for `A`, `a-`, or `Avengers` surfaces the pack.

## Self-Test

If a run teaches a reusable pattern, produce a concise learning note instead of letting the lesson disappear in chat.

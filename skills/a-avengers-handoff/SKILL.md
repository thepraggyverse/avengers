---
name: a-avengers-handoff
description: Avengers skill A - Avengers Handoff that helps the user to write a concise continuation handoff for future agents or future sessions. Use when the user mentions or needs one of these triggers - handoff, continuation note, resume work, future agent, next session. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Avengers Handoff

## Role

Tier 1 Avengers Memory skill. Create a concise continuation handoff so another agent or future session can resume without rediscovering the work.

## Use When

- The user needs to write a concise continuation handoff for future agents or future sessions.
- The request matches these triggers: handoff, continuation note, resume work, future agent, next session.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

## Do Not Use When

- The task is a one-off answer with no reusable lesson, setup, refresh, context, or handoff value.
- The user explicitly asks not to write memory, logs, or handoff artifacts.

## Workflow

1. Summarize the current task, repo state, branch, and key files changed.
2. List commands run, tests passed or failed, and autoreview status.
3. Record decisions, unresolved risks, and the exact next action.
4. Write to `docs/avengers-memory/handoffs/` only when repo-persistent handoff is appropriate; otherwise use a temp path.
5. Keep secrets, private corpus text, and unrelated local paths out of the handoff.

## Output Contract

Return these fields unless the user asks for another format:

- `Current Task`
- `Repo State`
- `Files Changed`
- `Tests Run`
- `Decisions`
- `Open Risks`
- `Next Action`

## Example

```text
Use $a-avengers-handoff to write a continuation note with repo state, tests, decisions, risks, and next action.
```

## Skill Chaining

- Pair with `a-avengers-compound` when useful.
- Pair with `a-avengers-refresh` when useful.
- Pair with `a-stark-router` when useful.

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

If asked to hand off Avengers work, create a compact continuation note with enough evidence to resume safely.

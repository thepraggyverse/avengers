---
name: a-avengers-refresh
description: Avengers skill A - Avengers Refresh that helps the user to audit Avengers skills, docs, and memory notes for stale, overlapping, or confusing guidance. Use when the user mentions or needs one of these triggers - refresh memory, stale skills, overlap audit, contradictory docs, weak notes. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Avengers Refresh

## Role

Tier 1 Avengers Memory skill. Review Avengers skills, generated docs, and memory notes for stale, duplicated, contradictory, or confusing guidance.

## Use When

- The user needs to audit Avengers skills, docs, and memory notes for stale, overlapping, or confusing guidance.
- The request matches these triggers: refresh memory, stale skills, overlap audit, contradictory docs, weak notes.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

## Do Not Use When

- The task is a one-off answer with no reusable lesson, setup, refresh, context, or handoff value.
- The user explicitly asks not to write memory, logs, or handoff artifacts.

## Workflow

1. Search skills, docs, templates, schemas, and memory notes for the target topic.
2. Classify each issue as keep, update, merge, replace, delete, or follow-up.
3. Check for stale generated text, unclear headers, old branding, broken source hooks, and overlapping skills.
4. Write a refresh report under `docs/avengers-memory/refresh-reports/` when persistent output is allowed.
5. Recommend the smallest regeneration, docs, or memory edit that makes the pack clearer.

## Output Contract

Return these fields unless the user asks for another format:

- `Scope`
- `Findings`
- `Action`
- `Affected Files`
- `Staleness Risk`
- `Recommended Fix`
- `Next Validation`

## Example

```text
Use $a-avengers-refresh to audit stale memory notes, overlapping skills, and old generated wording.
```

## Skill Chaining

- Pair with `a-skill-pruner` when useful.
- Pair with `a-skill-pack-builder` when useful.
- Pair with `a-avengers-compound` when useful.

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

If asked whether Avengers memory or skills are stale, produce a refresh report with concrete keep/update/merge decisions.

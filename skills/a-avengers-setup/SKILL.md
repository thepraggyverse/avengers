---
name: a-avengers-setup
description: Avengers skill A - Avengers Setup that helps the user to configure local Avengers paths, harness homes, corpus search, and memory policy. Use when the user mentions or needs one of these triggers - setup Avengers, configure Avengers, local config, harness homes, corpus path, symlink policy. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Avengers Setup

## Role

Tier 1 Avengers Memory skill. Configure local Avengers usage for a repository or harness without committing private paths or corpus data.

## Use When

- The user needs to configure local Avengers paths, harness homes, corpus search, and memory policy.
- The request matches these triggers: setup Avengers, configure Avengers, local config, harness homes, corpus path, symlink policy.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

## Do Not Use When

- The task is a one-off answer with no reusable lesson, setup, refresh, context, or handoff value.
- The user explicitly asks not to write memory, logs, or handoff artifacts.

## Workflow

1. Identify the target repo, harness, skill home, and whether this is a plugin or symlink install.
2. Choose local corpus and memory paths, preferring `.avengers/config.local.yaml` for private settings.
3. Record source citation preferences and what may be committed.
4. Check the relevant install docs before writing commands.
5. Return the exact setup commands and any files that should remain local-only.

## Output Contract

Return these fields unless the user asks for another format:

- `Target Repo`
- `Harness`
- `Corpus Path`
- `Memory Path`
- `Install Method`
- `Do Not Commit`
- `Next Command`

## Example

```text
Use $a-avengers-setup to configure this repo for Codex with a private corpus path, memory folder, and symlink policy.
```

## Skill Chaining

- Pair with `a-avengers-context` when useful.
- Pair with `a-avengers-compound` when useful.
- Pair with `a-skill-pack-builder` when useful.

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

If asked to configure Avengers for Codex, Claude, Cursor, OpenCode, Gemini, Pi, or a flat skill home, return safe local paths and install commands.

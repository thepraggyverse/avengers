---
name: a-avengers-context
description: Avengers skill A - Avengers Context that helps the user to maintain Avengers concepts, vocabulary, operating principles, and terms to clarify. Use when the user mentions or needs one of these triggers - context glossary, concepts, vocabulary, operating principles, terms to avoid. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Avengers Context

## Role

Tier 1 Avengers Memory skill. Maintain the Avengers concepts glossary and operating principles that future agents should share.

## Use When

- The user needs to maintain Avengers concepts, vocabulary, operating principles, and terms to clarify.
- The request matches these triggers: context glossary, concepts, vocabulary, operating principles, terms to avoid.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

## Do Not Use When

- The task is a one-off answer with no reusable lesson, setup, refresh, context, or handoff value.
- The user explicitly asks not to write memory, logs, or handoff artifacts.

## Workflow

1. Inspect `docs/AVENGERS_CONTEXT.md` before changing vocabulary.
2. Add only durable concepts, terms to clarify, or operating principles that improve future use.
3. Prefer short definitions tied to source-grounded behavior, not fandom trivia.
4. Record terms to avoid when wording causes confusion.
5. Cross-link related A-skills and memory notes when useful.

## Output Contract

Return these fields unless the user asks for another format:

- `Concept`
- `Definition`
- `Operating Principle`
- `Related Skills`
- `Terms To Avoid`
- `Source Grounding`

## Example

```text
Use $a-avengers-context to add this recurring operating principle to the Avengers glossary.
```

## Skill Chaining

- Pair with `a-avengers-compound` when useful.
- Pair with `a-source-grounded-synthesis` when useful.
- Pair with `a-knowledge-index-curator` when useful.

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

If a repeated Avengers term is unclear or important, update the glossary rather than burying the meaning in one chat.

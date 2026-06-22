---
name: a-skill-pruner
description: Avengers skill A - Skill Pruner that helps the user to review skills for keep, merge, reference-only, or remove decisions. Use when the user mentions or needs one of these triggers - prune skills, merge, keep remove. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Skill Pruner

## Role

Tier 4 Knowledge System skill. Review skills for keep, merge, reference-only, or remove decisions.

## Use When

- The user needs to review skills for keep, merge, reference-only, or remove decisions.
- The request matches these triggers: prune skills, merge, keep remove.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Do Not Use When

- The user only needs a quick direct answer.
- The requested action would copy large transcript passages instead of synthesizing.

## Workflow

1. Identify the input corpus and extraction goal.
2. Search or index before synthesizing.
3. Keep source file names attached to claims.
4. Avoid long verbatim reproduction from transcripts.
5. Write the reusable artifact or manifest update.

## Output Contract

Return these fields unless the user asks for another format:

- `Input Corpus`
- `Extraction Goal`
- `Index Method`
- `Evidence Rule`
- `Output Artifact`
- `Maintenance Step`

## Skill Chaining

- Pair with `a-knowledge-index-curator` when useful.
- Pair with `a-source-grounded-synthesis` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `10 Tony Stark Habits That Make You Unstoppable.txt` (366 words)
- `24 Mistakes that made Iron Man Stronger.txt` (1559 words)
- `AVENGERS Breakdown! Endgame Easter Eggs & New Details You Missed!  Infinity Saga Rewatch.txt` (3597 words)
- `AVENGERS INFINITY WAR Review & Analysis #NewRockstarsNews.txt` (10798 words)
- `Avengers Age of Ultron Breakdown! NEW Hidden Visual Details & Endgame Clues!.txt` (3510 words)
- `Avengers Endgame Breakdown! Details You Missed & New VFX Easter Eggs!  Infinity Saga Rewatch.txt` (5610 words)

## Self-Test

If the user asks for review skills for keep, merge, reference-only, or remove decisions., return the output contract fields and a concrete next action.

---
name: a-podcast-to-skill-extractor
description: Avengers skill A - Podcast To Skill Extractor that helps the user to turn a transcript or podcast into candidate agent skills. Use when the user mentions or needs one of these triggers - podcast to skills, transcript extraction. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Podcast To Skill Extractor

## Role

Tier 4 Knowledge System skill. Turn a transcript or podcast into candidate agent skills.

## Use When

- The user needs to turn a transcript or podcast into candidate agent skills.
- The request matches these triggers: podcast to skills, transcript extraction.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

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

## Example

```text
Use $a-podcast-to-skill-extractor to turn this source material into searchable skill knowledge.
```

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

## Safety And Grounding

- Keep answers synthesized and practical.
- Do not reproduce long copyrighted source passages.
- Keep private corpus paths, secrets, and local machine details out of committed artifacts.
- Mark speculation clearly when source grounding is thin.

## Cross-Harness Notes

- This skill is plain `SKILL.md` and should work through native plugins or flat skill-home symlinks.
- The A-prefixed name is intentional so searching for `A`, `a-`, or `Avengers` surfaces the pack.

## Self-Test

If the user asks for turn a transcript or podcast into candidate agent skills., return the output contract fields and a concrete next action.

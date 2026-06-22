---
name: a-source-grounded-synthesis
description: Avengers skill A - Source Grounded Synthesis that helps the user to answer using the local Avengers corpus and cite source file names. Use when the user mentions or needs one of these triggers - source grounded, use corpus, cite files, transcripts support, evidence, source files. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Source Grounded Synthesis

## Role

Tier 1 Knowledge System skill. Synthesize answers from the local Avengers corpus while preserving source names and avoiding transcript dumps.

## Use When

- The user needs to answer using the local Avengers corpus and cite source file names.
- The request matches these triggers: source grounded, use corpus, cite files, transcripts support, evidence, source files.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Do Not Use When

- The user only needs a quick direct answer.
- The requested action would copy large transcript passages instead of synthesizing.

## Workflow

1. Clarify the exact idea, theme, or skill the user wants grounded.
2. Search the corpus index and source map before answering.
3. Group evidence by source file and theme.
4. Synthesize the answer in original words.
5. Name the relevant source files and related A-skills.

## Output Contract

Return these fields unless the user asks for another format:

- `Question`
- `Matched Sources`
- `Synthesis`
- `Relevant A-Skills`
- `Source Notes`

## Skill Chaining

- Pair with `a-knowledge-index-curator` when useful.
- Pair with `a-quote-example-finder` when useful.
- Pair with `a-theme-thread-mapper` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `10 Tony Stark Habits That Make You Unstoppable.txt` (366 words)
- `24 Mistakes that made Iron Man Stronger.txt` (1559 words)
- `AVENGERS Breakdown! Endgame Easter Eggs & New Details You Missed!  Infinity Saga Rewatch.txt` (3597 words)
- `AVENGERS INFINITY WAR Review & Analysis #NewRockstarsNews.txt` (10798 words)
- `Avengers Age of Ultron Breakdown! NEW Hidden Visual Details & Endgame Clues!.txt` (3510 words)
- `Avengers Endgame Breakdown! Details You Missed & New VFX Easter Eggs!  Infinity Saga Rewatch.txt` (5610 words)

## Self-Test

If asked to prove where an idea came from, cite source file names and summarize without copying long passages.

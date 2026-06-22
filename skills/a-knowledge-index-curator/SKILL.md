---
name: a-knowledge-index-curator
description: Avengers skill A - Knowledge Index Curator that helps the user to maintain the Avengers corpus index, source map, and skill manifest. Use when the user mentions or needs one of these triggers - knowledge index, corpus, source map, transcripts, source files. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Knowledge Index Curator

## Role

Tier 1 Knowledge System skill. Maintain and query the Avengers source map, manifest, and transcript-derived references.

## Use When

- The user needs to maintain the Avengers corpus index, source map, and skill manifest.
- The request matches these triggers: knowledge index, corpus, source map, transcripts, source files.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Do Not Use When

- The user only needs a quick direct answer.
- The requested action would copy large transcript passages instead of synthesizing.

## Workflow

1. Search the corpus index before making source-grounded claims.
2. Attach source file names to extracted ideas.
3. Update the manifest when new transcripts or books arrive.
4. Deduplicate exact duplicate sources and preserve canonical names.
5. Keep references concise and avoid long verbatim text.

## Output Contract

Return these fields unless the user asks for another format:

- `Query`
- `Matched Sources`
- `Extracted Ideas`
- `Skill Links`
- `Index Update`

## Skill Chaining

- Pair with `a-source-grounded-synthesis` when useful.
- Pair with `a-quote-example-finder` when useful.
- Pair with `a-podcast-to-skill-extractor` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `10 Tony Stark Habits That Make You Unstoppable.txt` (366 words)
- `24 Mistakes that made Iron Man Stronger.txt` (1559 words)
- `AVENGERS Breakdown! Endgame Easter Eggs & New Details You Missed!  Infinity Saga Rewatch.txt` (3597 words)
- `AVENGERS INFINITY WAR Review & Analysis #NewRockstarsNews.txt` (10798 words)
- `Avengers Age of Ultron Breakdown! NEW Hidden Visual Details & Endgame Clues!.txt` (3510 words)
- `Avengers Endgame Breakdown! Details You Missed & New VFX Easter Eggs!  Infinity Saga Rewatch.txt` (5610 words)

## Self-Test

If the user asks where an idea came from, return source files and relevant skills without dumping full transcripts.

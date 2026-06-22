---
name: a-curiosity-mastery-synthesis
description: Avengers skill A - Curiosity Mastery Synthesis that helps the user to learn through curiosity, mastery, and cross-domain synthesis. Use when the user mentions or needs one of these triggers - curiosity, mastery, synthesis, learning. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Curiosity Mastery Synthesis

## Role

Tier 2 Learning And Intelligence skill. Learn through curiosity, mastery, and cross-domain synthesis.

## Use When

- The user needs to learn through curiosity, mastery, and cross-domain synthesis.
- The request matches these triggers: curiosity, mastery, synthesis, learning.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

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

## Skill Chaining

- Pair with `a-learn-like-stark` when useful.
- Pair with `a-build-to-understand` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `Become Smart like Tony Stark  In-Depth Analysis.txt` (1693 words)
- `How to Work Like Tony Stark.txt` (1290 words)
- `How Tony Stark Works on Multiple Projects at Once.txt` (1915 words)

## Self-Test

If the user asks for learn through curiosity, mastery, and cross-domain synthesis., return the output contract fields and a concrete next action.

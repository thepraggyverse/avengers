---
name: a-shared-burden-protocol
description: Avengers skill A - Shared Burden Protocol that helps the user to stop carrying a threat or mission alone; distribute responsibility. Use when the user mentions or needs one of these triggers - carry alone, burden, share responsibility. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Shared Burden Protocol

## Role

Tier 3 Risk Ethics And Control skill. Stop carrying a threat or mission alone; distribute responsibility.

## Use When

- The user needs to stop carrying a threat or mission alone; distribute responsibility.
- The request matches these triggers: carry alone, burden, share responsibility.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. Name the threat and the fear underneath it.
2. Identify where control could become harm.
3. Separate protection, consent, oversight, and coercion.
4. Distribute responsibility instead of carrying it alone.
5. Choose the governed action.

## Output Contract

Return these fields unless the user asks for another format:

- `Threat`
- `Fear Signal`
- `Control Risk`
- `Ethical Boundary`
- `Shared Burden`
- `Governed Action`

## Skill Chaining

- Pair with `a-threat-is-imminent` when useful.
- Pair with `a-armor-around-world-check` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `The Curse of Knowledge Explained Why Iron Man & Thanos are CONNECTED.txt` (1702 words)
- `Tony Stark The Curse of Being Right.txt` (5931 words)
- `Avengers Age of Ultron Breakdown! NEW Hidden Visual Details & Endgame Clues!.txt` (3510 words)
- `How Avengers Age of Ultron Sets Up Avengers Doomsday  Road to Doomsday #24.txt` (10072 words)

## Self-Test

If the user asks for stop carrying a threat or mission alone; distribute responsibility., return the output contract fields and a concrete next action.

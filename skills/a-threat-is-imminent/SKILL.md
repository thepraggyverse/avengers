---
name: a-threat-is-imminent
description: Avengers skill A - Threat Is Imminent that helps the user to anticipate looming threats without letting fear own the solution. Use when the user mentions or needs one of these triggers - threat imminent, future risk, warning. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Threat Is Imminent

## Role

Tier 3 Risk Ethics And Control skill. Anticipate looming threats without letting fear own the solution.

## Use When

- The user needs to anticipate looming threats without letting fear own the solution.
- The request matches these triggers: threat imminent, future risk, warning.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

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

## Example

```text
Use $a-threat-is-imminent to check whether this safety idea creates control risk.
```

## Skill Chaining

- Pair with `a-armor-around-world-check` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `The Curse of Knowledge Explained Why Iron Man & Thanos are CONNECTED.txt` (1702 words)
- `Tony Stark The Curse of Being Right.txt` (5931 words)
- `Avengers Age of Ultron Breakdown! NEW Hidden Visual Details & Endgame Clues!.txt` (3510 words)
- `How Avengers Age of Ultron Sets Up Avengers Doomsday  Road to Doomsday #24.txt` (10072 words)

## Safety And Grounding

- Keep answers synthesized and practical.
- Do not reproduce long copyrighted source passages.
- Keep private corpus paths, secrets, and local machine details out of committed artifacts.
- Mark speculation clearly when source grounding is thin.

## Cross-Harness Notes

- This skill is plain `SKILL.md` and should work through native plugins or flat skill-home symlinks.
- The A-prefixed name is intentional so searching for `A`, `a-`, or `Avengers` surfaces the pack.

## Self-Test

If the user asks for anticipate looming threats without letting fear own the solution., return the output contract fields and a concrete next action.

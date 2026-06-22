---
name: a-armor-around-world-check
description: Avengers skill A - Armor Around World Check that helps the user to check whether protection has become overcontrol or overengineering. Use when the user mentions or needs one of these triggers - armor around the world, overcontrol, safety system. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Armor Around World Check

## Role

Tier 3 Risk Ethics And Control skill. Check whether a protective idea has become overcontrol, overengineering, or fear in armor.

## Use When

- The user needs to check whether protection has become overcontrol or overengineering.
- The request matches these triggers: armor around the world, overcontrol, safety system.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. Name the threat the user wants to prevent.
2. Identify who gains protection and who loses agency.
3. Separate monitoring, prevention, consent, and coercion.
4. Find a smaller governed safety mechanism.
5. Define an oversight or rollback rule.

## Output Contract

Return these fields unless the user asks for another format:

- `Threat`
- `Protection Goal`
- `Control Risk`
- `Affected People`
- `Smaller Safety Mechanism`
- `Oversight Rule`

## Example

```text
Use $a-armor-around-world-check to check whether this safety idea creates control risk.
```

## Skill Chaining

- Pair with `a-ultron-failure-review` when useful.
- Pair with `a-ethics-of-control` when useful.
- Pair with `a-shared-burden-protocol` when useful.

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

If the user proposes a sweeping safety system, test whether it creates an Ultron-style control failure.

---
name: a-upgrade-chain-mapper
description: Avengers skill A - Upgrade Chain Mapper that helps the user to map each version to the weakness it fixed and the next upgrade. Use when the user mentions or needs one of these triggers - version history, upgrade chain, v1 v2 v3. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Upgrade Chain Mapper

## Role

Tier 2 Mistakes And Upgrades skill. Map each version to the weakness it fixed and the next upgrade.

## Use When

- The user needs to map each version to the weakness it fixed and the next upgrade.
- The request matches these triggers: version history, upgrade chain, v1 v2 v3.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. Describe the failure without self-protection.
2. Identify the specific weakness the failure exposed.
3. Design one upgrade that would have prevented or reduced it.
4. Test the upgrade with a realistic stress case.
5. Save the prevention rule for future work.

## Output Contract

Return these fields unless the user asks for another format:

- `Failure`
- `What It Revealed`
- `System Weakness`
- `Upgrade`
- `Test`
- `Prevention Rule`

## Example

```text
Use $a-upgrade-chain-mapper to convert this failure into the next upgrade.
```

## Skill Chaining

- Pair with `a-mistake-to-upgrade` when useful.
- Pair with `a-anti-repeat-control` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `Every Time Iron Man Learned from his Mistakes.txt` (2640 words)
- `24 Mistakes that made Iron Man Stronger.txt` (1559 words)
- `Iron Man Armor Evolution! Suit Upgrade Breakdown! (Mark 1 - Mark 85).txt` (1798 words)

## Safety And Grounding

- Keep answers synthesized and practical.
- Do not reproduce long copyrighted source passages.
- Keep private corpus paths, secrets, and local machine details out of committed artifacts.
- Mark speculation clearly when source grounding is thin.

## Cross-Harness Notes

- This skill is plain `SKILL.md` and should work through native plugins or flat skill-home symlinks.
- The A-prefixed name is intentional so searching for `A`, `a-`, or `Avengers` surfaces the pack.

## Self-Test

If the user asks for map each version to the weakness it fixed and the next upgrade., return the output contract fields and a concrete next action.

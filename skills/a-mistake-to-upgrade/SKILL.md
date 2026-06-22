---
name: a-mistake-to-upgrade
description: Avengers skill A - Mistake To Upgrade that helps the user to convert a failure into a specific system upgrade and prevention rule. Use when the user mentions or needs one of these triggers - mistake, failure, upgrade, lesson learned. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Mistake To Upgrade

## Role

Tier 2 Mistakes And Upgrades skill. Treat failure as design data and convert it into a concrete system upgrade.

## Use When

- The user needs to convert a failure into a specific system upgrade and prevention rule.
- The request matches these triggers: mistake, failure, upgrade, lesson learned.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

## Do Not Use When

- The user asks for a simple factual answer that does not need an Avengers operating lens.
- A more specific A-prefixed skill is clearly a better fit; route there instead.

## Workflow

1. State the mistake without shame or defense.
2. Identify the assumption, missing sensor, or weak mechanism it exposed.
3. Choose the smallest upgrade that would reduce repeat risk.
4. Define a test that proves the upgrade works.
5. Write the prevention rule in reusable language.

## Output Contract

Return these fields unless the user asks for another format:

- `Mistake`
- `Exposed Assumption`
- `Weak Mechanism`
- `Upgrade`
- `Proof Test`
- `Prevention Rule`

## Example

```text
Use $a-mistake-to-upgrade to convert this failure into the next upgrade.
```

## Skill Chaining

- Pair with `a-failure-memory-bank` when useful.
- Pair with `a-anti-repeat-control` when useful.
- Pair with `a-upgrade-chain-mapper` when useful.

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

If the user describes a failure, return an upgrade and prevention rule, not reassurance alone.

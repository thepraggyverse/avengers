---
name: a-civil-war-conflict-map
description: Avengers skill A - Civil War Conflict Map that helps the user to map a conflict where both sides have legitimate values. Use when the user mentions or needs one of these triggers - Civil War, team conflict, competing values. Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes.
---

# A - Civil War Conflict Map

## Role

Tier 3 Leadership And Team skill. Map a conflict where both sides have legitimate values.

## Use When

- The user needs to map a conflict where both sides have legitimate values.
- The request matches these triggers: Civil War, team conflict, competing values.
- The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.

## Inputs

- The user's request, goal, or artifact.
- Any explicit harness, repository, corpus, or source-file constraints.
- Any related A-skills already selected by the user or router.

## Do Not Use When

- The problem is a solo build decision with no team or stakeholder issue.

## Workflow

1. Name the mission or conflict.
2. Identify the values and incentives on each side.
3. Clarify who should lead, advise, execute, or challenge.
4. Choose the communication move that protects trust.
5. Define the next accountable action.

## Output Contract

Return these fields unless the user asks for another format:

- `Conflict or Mission`
- `Values at Stake`
- `Team Roles`
- `Decision Rule`
- `Communication Move`
- `Trust Follow-Up`

## Example

```text
Use $a-civil-war-conflict-map to handle this team conflict without losing trust.
```

## Skill Chaining

- Pair with `a-team-assembly-avengers` when useful.

## Source Hooks

Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.

- `How to Lead Like Captain America.txt` (1241 words)
- `Captain America Civil War Breakdown! New Easter Eggs & Details You Missed!.txt` (3755 words)
- `Captain America Civil War 🤝 Avengers Doomsday  Road to Doomsday @ IGN Live.txt` (10732 words)

## Safety And Grounding

- Keep answers synthesized and practical.
- Do not reproduce long copyrighted source passages.
- Keep private corpus paths, secrets, and local machine details out of committed artifacts.
- Mark speculation clearly when source grounding is thin.

## Cross-Harness Notes

- This skill is plain `SKILL.md` and should work through native plugins or flat skill-home symlinks.
- The A-prefixed name is intentional so searching for `A`, `a-`, or `Avengers` surfaces the pack.

## Self-Test

If the user asks for map a conflict where both sides have legitimate values., return the output contract fields and a concrete next action.

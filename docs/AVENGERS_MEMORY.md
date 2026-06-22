# Avengers Memory

Avengers memory is a lightweight way to keep useful lessons from disappearing after a chat. It borrows the durable-learning idea from Compound Engineering, but keeps the surface small: setup config, learning notes, run logs, refresh reports, context, and handoffs.

## Memory Loop

```text
request -> skill used -> sources consulted -> decision/result -> reusable lesson -> related skills -> stale/refresh status
```

Use memory only when a run teaches something worth reusing. Do not save private transcript text, secrets, browser state, API keys, or noisy chat logs.

## Folders

| Path | Purpose | Commit? |
|---|---|---|
| `.avengers/config.local.example.yaml` | Safe example for local config. | Yes |
| `.avengers/config.local.yaml` | Real local paths and preferences. | No |
| `docs/avengers-memory/learnings/` | Durable reusable lessons. | Usually yes |
| `docs/avengers-memory/runs/` | Run summaries and simulator notes. | Only if useful and public-safe |
| `docs/avengers-memory/handoffs/` | Continuation notes for future sessions. | Only if useful and public-safe |
| `docs/avengers-memory/refresh-reports/` | Staleness and overlap audits. | Yes when useful |
| `docs/avengers-memory/templates/` | Copyable artifact templates. | Yes |
| `docs/avengers-memory/schemas/` | Frontmatter and field contracts. | Yes |

## Which Skill To Use

| Need | Skill | Output |
|---|---|---|
| Configure local paths and harnesses. | `a-avengers-setup` | Safe config plan and install commands |
| Save a reusable lesson after a run. | `a-avengers-compound` | Learning note |
| Check stale or overlapping guidance. | `a-avengers-refresh` | Refresh report |
| Continue in another session. | `a-avengers-handoff` | Handoff note |
| Clarify durable vocabulary. | `a-avengers-context` | `docs/AVENGERS_CONTEXT.md` update |

## Learning Note Rules

- Save a lesson only when it changes future behavior.
- Prefer one lesson per note.
- Include related skills so future agents can route to it.
- Include source file names or repo docs used as evidence.
- Mark `status` as `fresh`, `needs-refresh`, `merged`, or `stale`.
- Mark `confidence` as `low`, `medium`, or `high`.

## Run Log Rules

Run logs are for reviewed runs, simulator passes, or decisions that explain why the pack changed. They are not raw transcripts. Keep them short and public-safe.

## Refresh Rules

Refresh reports use keep/update/merge/replace/delete/follow-up decisions. A refresh report should identify the smallest safe edit and the validation command that proves it.

## Handoff Rules

Handoffs should let another agent resume without rediscovering the repo. Include repo state, changed files, commands run, test results, autoreview status, open risks, and next action.

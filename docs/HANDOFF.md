# Handoff Guide

Use `a-avengers-handoff` when another agent or future session needs to resume Avengers work.

Persistent handoffs belong in:

```text
docs/avengers-memory/handoffs/
```

Use a temp path instead when the handoff contains local-only paths, private corpus details, or information that should not be committed.

Required fields:

| Field | Meaning |
|---|---|
| Current Task | What the user asked for |
| Repo State | Branch, status, and important generated-file notes |
| Files Changed | Files or areas touched |
| Commands Run | Validation, tests, generation, review |
| Test Results | Pass/fail/partial with command names |
| Autoreview Result | Clean, findings fixed, or findings open |
| Decisions | Important choices and why |
| Known Limitations | Anything still uncertain |
| Next Steps | Exact next action |

For release-readiness or install changes, also note whether `CHANGELOG.md`, `docs/DOCUMENTATION_AUDIT.md`, and the installed plugin cache were updated.

Template: [avengers-memory/templates/handoff.md](avengers-memory/templates/handoff.md)

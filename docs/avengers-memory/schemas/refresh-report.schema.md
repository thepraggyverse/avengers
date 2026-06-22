# Refresh Report Schema

Use this frontmatter for `docs/avengers-memory/refresh-reports/*.md`.

```yaml
---
title: ""
date: "YYYY-MM-DD"
type: "refresh-report"
scope: ""
status: "complete|partial|needs-followup"
---
```

Body sections:

- `## Scope`
- `## Findings`
- `## Decisions`
- `## Files To Update`
- `## Staleness Risk`
- `## Validation`
- `## Followups`

Decision values:

- `keep`
- `update`
- `merge`
- `replace`
- `delete`
- `follow-up`

# Run Log Schema

Use this frontmatter for `docs/avengers-memory/runs/*.md`.

```yaml
---
title: ""
date: "YYYY-MM-DD"
type: "run-log"
request: ""
selected_skills:
  - "a-stark-router"
sources_used:
  - "docs/AVENGERS_MEMORY.md"
tests_run:
  - "python3 scripts/validate_skill_pack.py"
status: "passed|failed|partial"
---
```

Body sections:

- `## Request`
- `## Skills Used`
- `## Sources Used`
- `## Decisions`
- `## Output Produced`
- `## Tests And Checks`
- `## Reusable Lessons`
- `## Followups`

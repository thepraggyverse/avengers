# Versioning

Avengers uses SemVer-style versioning for plugin manifests.

Current version:

```text
0.1.0
```

## Version Meaning

| Version Change | Use When |
|---|---|
| Patch | Docs fixes, tests, metadata corrections, safe script bug fixes. |
| Minor | New skills, new memory surfaces, new harness install routes, new scripts. |
| Major | Breaking skill names, removed skills, incompatible manifest layout, or changed memory contract. |

Before `1.0.0`, minor versions may still change structure, but the changelog must call out user-visible changes.

## Release Checklist

1. Run `python3 scripts/doctor.py`.
2. Update `CHANGELOG.md`.
3. Update plugin manifest versions together:
   - `.codex-plugin/plugin.json`
   - `.claude-plugin/plugin.json`
   - `.cursor-plugin/plugin.json`
   - `gemini-extension.json`
4. Reinstall locally when plugin surfaces changed.
5. Run at least one live harness load test when install behavior changed.
6. Run autoreview for non-trivial changes.
7. Commit, tag, and push only after checks pass.

## Current Policy

Keep the version at `0.1.0` until the first public release tag is cut. The next feature release should be `0.2.0`.

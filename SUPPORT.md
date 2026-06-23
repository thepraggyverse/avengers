# Support

Avengers is an open-source skill pack maintained best-effort.

## Before Opening An Issue

Run:

```bash
python3 scripts/doctor.py
```

If the issue is install-related, also include:

```bash
codex plugin list
python3 scripts/install_symlinks.py --home ~/.codex/skills
```

The second command is a dry run unless `--apply` is included.

## Good Issue Reports

Include:

- harness name and version, if relevant
- install route used
- skill name, if relevant
- command output
- whether the issue happens in native plugin mode, symlink mode, or both

Do not include:

- private corpus content
- full transcripts, captions, books, movie scripts, or private notes
- secrets or tokens
- real `.avengers/config.local.yaml` contents

## Common Paths

| Need | Doc |
|---|---|
| Install | `docs/INSTALL.md` |
| Testing | `docs/TESTING.md` |
| Updates | `docs/UPDATE.md` |
| Symlinks | `docs/SYMLINKS.md` |
| Harness compatibility | `docs/HARNESSES.md` |
| Memory layer | `docs/AVENGERS_MEMORY.md` |

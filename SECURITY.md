# Security Policy

## Supported Versions

Avengers is currently pre-1.0. The supported version is the latest commit on `main` and the latest published plugin version.

## Reporting A Vulnerability

Open a private security advisory on GitHub when available, or contact the repository owner through GitHub.

Please include:

- affected file, script, or install route
- steps to reproduce
- expected and actual behavior
- whether private corpus paths, local config, or harness credentials are exposed

Do not include secrets, tokens, private transcripts, books, captions, movie scripts, or personal corpus content in reports.

## Security Model

The public repo should contain only:

- original skill instructions
- generated metadata
- tests
- public-safe docs
- source-file names and source hooks

The public repo must not contain:

- full transcripts, captions, books, movie scripts, or private notes
- `.avengers/config.local.yaml`
- local machine paths
- API keys, OAuth tokens, cookies, browser profiles, or harness cache state

## Local Scripts

Scripts are intended for local repository maintenance. Review scripts before running them in a sensitive checkout. The safest verification command is:

```bash
python3 scripts/doctor.py
```

Symlink uninstall should use:

```bash
python3 scripts/install_symlinks.py --uninstall --apply --home ~/.codex/skills
```

That command removes only symlinks whose resolved target points back to the current Avengers checkout.

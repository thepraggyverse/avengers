# Install

Avengers can be installed in three ways:

1. **Native plugin install** for harnesses that understand plugin manifests.
2. **Direct skill symlinks** for harnesses that load `SKILL.md` folders from a skill home.
3. **Local development checkout** for testing changes before publishing.

The skill content is the same in every route: `skills/a-*/SKILL.md`.

## Requirements

- Git
- Python 3.10+
- A local clone for validation, symlink installs, and local development

No Python package install is required.

## Clone And Validate

```bash
git clone https://github.com/thepraggyverse/avengers.git ~/plugins/avengers
cd ~/plugins/avengers
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
```

Expected validation:

```text
Avengers skill pack validation passed.
Skills: 107
Manifest entries: 107
```

## Codex App

Fast local install:

```bash
python3 scripts/install_codex_plugin.py --apply
```

What it does:

- Ensures `~/plugins/avengers` points at this checkout.
- Adds or refreshes the `avengers` entry in `~/.agents/plugins/marketplace.json`.
- Leaves skills in this repository so updates happen from one checkout.

Then open Codex Plugins, install or reload **Avengers**, and restart Codex if the skill list does not refresh.

## Codex CLI

From this checkout:

```bash
codex plugin marketplace add "$PWD"
codex
```

Inside Codex, open `/plugins`, select the Avengers marketplace, install **avengers**, then restart Codex.

For a separate Codex profile:

```bash
CODEX_HOME="$HOME/.codex/profiles/avengers-test" codex plugin marketplace add "$PWD"
CODEX_HOME="$HOME/.codex/profiles/avengers-test" codex
```

Direct skill fallback:

```bash
python3 scripts/install_symlinks.py --apply --home ~/.codex/skills
```

## Claude Code

Marketplace-style install from GitHub:

```text
/plugin marketplace add thepraggyverse/avengers
/plugin install avengers
```

Local development from this checkout:

```bash
claude --plugin-dir "$PWD"
```

Direct skill fallback:

```bash
python3 scripts/install_symlinks.py --apply --home ~/.claude/skills
```

## Cursor

If your Cursor build supports plugin install from source, install this repository and select **avengers**.

Direct skill fallback:

```bash
python3 scripts/install_symlinks.py --apply --home ~/.cursor/skills
```

Cursor project-scoped fallback:

```bash
mkdir -p .cursor/skills
python3 /path/to/avengers/scripts/install_symlinks.py --apply --home "$PWD/.cursor/skills"
```

## GitHub Copilot Plugin Hosts

Use the Claude-compatible plugin manifest when the host supports plugins from source. If not, copy or symlink `skills/a-*` into the host's supported skill directory.

## Qwen Code And Claude-Compatible Installers

Use the host's GitHub/plugin install command against:

```text
thepraggyverse/avengers
```

The `.claude-plugin/plugin.json` manifest and root `skills/` directory are the compatibility surface.

## OpenCode

See [.opencode/INSTALL.md](../.opencode/INSTALL.md).

Typical config:

```json
{
  "plugin": ["avengers@git+https://github.com/thepraggyverse/avengers.git"]
}
```

## Pi

Use the repository extension at:

```text
.pi/extensions/avengers.ts
```

For local development, point Pi at this checkout when supported by your Pi installation.

## Gemini CLI

From this checkout:

```bash
gemini extensions install "$PWD"
```

Update later:

```bash
gemini extensions update avengers
```

## OpenClaw And Flat Skill Homes

Default symlink install:

```bash
python3 scripts/install_symlinks.py --apply
```

Default homes:

```text
~/.agents/skills
~/.codex/skills
~/.claude/skills
~/.cursor/skills
~/.openclaw/skills
~/.openclaw/acpx/codex-home/skills
```

Custom home:

```bash
python3 scripts/install_symlinks.py --apply --home /path/to/skills
```

One skill:

```bash
python3 scripts/install_symlinks.py --apply --skill a-stark-router
```

## Local Corpus Search

Set a local corpus directory when you want source-grounded search over your own notes:

```bash
export AVENGERS_CORPUS_DIR="$HOME/Documents/Avengers Corpus"
python3 scripts/search_corpus.py "Mark 1"
```

Do not commit the corpus.

## Update Existing Installs

Checkout-based installs:

```bash
python3 scripts/update_avengers.py --apply
```

With Codex marketplace refresh:

```bash
python3 scripts/update_avengers.py --apply --install-codex
```

With symlink refresh:

```bash
python3 scripts/update_avengers.py --apply --install-symlinks
```

Marketplace-managed installs should be updated through the harness plugin UI/command, then restarted so cached skills refresh.

More detail: [UPDATE.md](UPDATE.md).

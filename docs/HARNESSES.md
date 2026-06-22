# Harness Compatibility

Avengers is authored as plain `SKILL.md` directories first. Everything else is packaging around that core.

## Compatibility Table

| Harness | Native Surface | Fallback Surface | Notes |
|---|---|---|---|
| Codex App | `.codex-plugin/plugin.json` and personal marketplace | `~/.codex/skills` symlinks | Native plugin is preferred. |
| Codex CLI | `codex plugin marketplace add "$PWD"` then `/plugins` | `~/.codex/skills` symlinks | Use one `CODEX_HOME` consistently per profile. |
| Claude Code | `.claude-plugin/plugin.json` | `~/.claude/skills` symlinks | Root `skills/` is the plugin skill directory. |
| Cursor | `.cursor-plugin/plugin.json` | `~/.cursor/skills` or `.cursor/skills` symlinks | Exact plugin UI support depends on Cursor version. |
| GitHub Copilot plugin hosts | Claude-compatible plugin metadata where supported | Host-specific skill copy/symlink | Keep `skills/a-*` as the source of truth. |
| Qwen Code | Claude-compatible plugin metadata where supported | Host-specific skill copy/symlink | Install from `thepraggyverse/avengers` when the host supports GitHub plugin source. |
| OpenCode | `.opencode/plugins/avengers.js` | Direct skill path in config | See `.opencode/INSTALL.md`. |
| Pi | `.pi/extensions/avengers.ts` | Direct skill path if supported | Extension exposes `skills/` as skill paths. |
| Gemini CLI | `gemini-extension.json` with `GEMINI.md` | Direct skill path if supported | Install from local checkout with `gemini extensions install "$PWD"`. |
| OpenClaw | flat skill home | `~/.openclaw/skills` symlinks | Direct symlink route is preferred. |
| Generic SKILL.md harness | none | symlink or copy `skills/a-*` | Use `scripts/install_symlinks.py --home <dir>`. |

## Invocation

Most harnesses support explicit skill invocation with one of these forms:

```text
$a-stark-router
/a-stark-router
Use a-stark-router
```

If the harness only searches skill names/descriptions, search for:

```text
A
a-
Avengers
Tony Stark
Iron Man
Mark 1
Ultron
```

## Why Skills, Not Agents

The pack currently ships skills only. Specialist behavior lives inside each skill through output contracts, workflows, source hooks, and chaining hints. That keeps the package portable because every target can read `SKILL.md` folders, while agent/subagent formats vary more between harnesses.

## What To Test In A New Harness

1. Confirm `a-stark-router` appears in skill search.
2. Invoke `a-stark-router` on a broad request.
3. Invoke `a-mark-one-prototype` directly.
4. Confirm skill chaining names existing skills.
5. Run `python3 scripts/simulate_routes.py "<prompt>"` from the checkout when routing feels weak.

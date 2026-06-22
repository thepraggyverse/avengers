# Harness Compatibility

Avengers is authored as plain `SKILL.md` directories first. Everything else is packaging around that core.

## Compatibility Matrix

| Harness | Native Surface | Skill Path / Fallback | Manifest Path | Notes |
|---|---|---|---|---|
| Codex App | Native plugin | `~/.codex/skills` symlinks | `.codex-plugin/plugin.json` | Native plugin preferred. Restart after install/update. |
| Codex CLI | Marketplace plus `/plugins` | `~/.codex/skills` symlinks | `.codex-plugin/plugin.json` | Use one `CODEX_HOME` per profile. |
| Claude Code | Claude-compatible plugin | `~/.claude/skills` symlinks | `.claude-plugin/plugin.json` | Root `skills/` is the plugin skill directory. |
| Cursor | Cursor metadata where supported | `~/.cursor/skills` or `.cursor/skills` | `.cursor-plugin/plugin.json` | Exact plugin UI support depends on Cursor version. |
| OpenCode | Plugin helper | Direct skill path in config | `.opencode/plugins/avengers.js` | See `.opencode/INSTALL.md`. |
| Pi | Extension helper | Direct skill path if supported | `.pi/extensions/avengers.ts` | Extension exposes `skills/`. |
| Gemini CLI | Extension metadata | Direct skill path if supported | `gemini-extension.json` | Uses `GEMINI.md` as context file. |
| .agents | Local marketplace | `~/.agents/skills` symlinks | `.agents/plugins/marketplace.json` | Useful for shared local agent homes. |
| OpenClaw | Flat skill home | `~/.openclaw/skills` symlinks | none | Symlink route is preferred. |
| Generic SKILL.md harness | none | symlink or copy `skills/a-*` | none | Use `scripts/install_symlinks.py --home <dir>`. |

## Discovery

All exposed skills are A-prefixed. Search for:

```text
A
a-
Avengers
Tony Stark
Iron Man
Mark 1
Ultron
memory
handoff
```

Most harnesses support one of these invocation styles:

```text
$a-stark-router
/a-stark-router
Use a-stark-router
```

Memory skills:

```text
$a-avengers-setup
$a-avengers-compound
$a-avengers-refresh
$a-avengers-handoff
$a-avengers-context
```

## Known Limitations

- The pack ships skills, not custom subagents or MCP servers.
- Some harnesses cache skill metadata at session start; restart after updates.
- Plugin UI support varies by harness version. Symlinks remain the portable fallback.
- The public repo does not include private transcript or book text.

## What To Test In A New Harness

1. Confirm `a-stark-router` appears in skill search.
2. Confirm `a-avengers-setup` appears in skill search.
3. Invoke `a-mark-one-prototype` directly.
4. Invoke `a-avengers-compound` on a memory-capture prompt.
5. Confirm skill chaining names existing skills.
6. Run `python3 scripts/simulate_routes.py "<prompt>"` from the checkout when routing feels weak.

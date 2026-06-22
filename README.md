# Avengers Skills

Avengers is an Avengers-inspired skill pack for problem solving, invention, leadership, pressure handling, strategy, iteration, and source-grounded reasoning.

It ships **112 A-prefixed skills**. The `a-` prefix is intentional: searching for `A`, `a-`, `Avengers`, `Tony Stark`, `Iron Man`, `Mark 1`, or `Ultron` should surface the pack in Codex and other skill harnesses.

Use one skill directly when you know what you need, or start with the router:

```text
$a-stark-router
$a-avengers-setup
$a-avengers-compound
$a-mark-one-prototype
$a-mistake-to-upgrade
$a-armor-around-world-check
```

## What The Skills Do

| Area | Skills | What They Help With |
|---|---:|---|
| Tony Stark Core | 9 | First principles, fast feedback, lab mode, self-made identity, full operating loops |
| Problem Solving | 9 | Constraints, root cause, pressure decisions, crisis plans, trapped/cave-style work |
| Mistakes And Upgrades | 9 | Retros, failure memory, Mark 1/Mark 2 iteration, prevention rules |
| Resourcefulness | 7 | Solving with available parts, recombination, salvage, constraints as design |
| Confidence And Permission | 7 | Approval-seeking, fear-to-motion, self-trust, audacity calibration |
| Learning And Intelligence | 7 | Build-first learning, knowledge gaps, cross-domain synthesis |
| Lean / Six Sigma Workflow | 7 | Waste removal, process stability, measurement, quality loops |
| Multiple Projects | 6 | Portfolio radar, context switching, energy allocation, overload checks |
| Leadership And Team | 8 | Captain America leadership, Civil War conflict mapping, governance, trust repair |
| Mentorship And Peter Parker | 6 | Training wheels, responsibility before power, mentor boundaries, legacy |
| Risk Ethics And Control | 8 | Ultron-style risk, overcontrol, consent, shared burden, Thanos logic |
| Armor Tech Product Design | 8 | Product-as-armor reviews, delegation, fallbacks, automation oversight |
| MCU Story Analysis | 9 | Easter eggs, timeline continuity, character arcs, themes, legacy, foreshadowing |
| Knowledge System | 7 | Source-grounded synthesis, corpus search, book/podcast extraction, pack maintenance |
| Avengers Memory | 5 | Local setup, reusable learning notes, refresh reports, context, handoffs |

Full inventory: [docs/SKILL_INVENTORY.md](docs/SKILL_INVENTORY.md)

Release notes: [CHANGELOG.md](CHANGELOG.md)

Reference audit: [docs/DOCUMENTATION_AUDIT.md](docs/DOCUMENTATION_AUDIT.md)

## Main Loop

```text
route -> frame -> build -> test -> upgrade -> govern -> ground -> compound -> refresh -> handoff
```

| Step | Use When | Start With | Output |
|---|---|---|---|
| Route | You are not sure which lens fits. | `$a-stark-router` | 1-3 best skills and first move |
| Setup | You are installing or configuring a repo/harness. | `$a-avengers-setup` | Local config, corpus path, install route |
| Frame | You want a complete Stark-style pass. | `$a-stark-operating-system` | Mission, block, Mark 1, test, upgrade, risk |
| Build | You need forward motion now. | `$a-mark-one-prototype` | Crude working version |
| Test | You have a draft or MVP. | `$a-mark-two-test-flight` | Stress test and weakness list |
| Upgrade | Something failed. | `$a-mistake-to-upgrade` | Upgrade rule and prevention rule |
| Govern | Power, safety, or team consequences matter. | `$a-armor-around-world-check` | Ethical boundary and accountability |
| Ground | You want source-backed answers. | `$a-source-grounded-synthesis` | Synthesis with source file names |
| Compound | A run produced a reusable lesson. | `$a-avengers-compound` | Learning note or context update |
| Refresh | Memory, docs, or skills may be stale. | `$a-avengers-refresh` | Refresh report |
| Handoff | Another session needs to continue. | `$a-avengers-handoff` | Continuation note |

## Memory Layer

The memory layer keeps useful learning without bloating the pack.

```text
request -> skill used -> sources consulted -> decision/result -> reusable lesson -> related skills -> stale/refresh status
```

Important paths:

| Path | Purpose |
|---|---|
| `.avengers/config.local.example.yaml` | Safe example for local config |
| `.avengers/config.local.yaml` | Real local config, ignored by git |
| `docs/AVENGERS_MEMORY.md` | Memory rules and folder guide |
| `docs/AVENGERS_CONTEXT.md` | Shared terms and operating principles |
| `docs/avengers-memory/learnings/` | Reusable lessons |
| `docs/avengers-memory/runs/` | Public-safe run logs |
| `docs/avengers-memory/handoffs/` | Continuation notes |
| `docs/avengers-memory/refresh-reports/` | Staleness and overlap reports |
| `docs/avengers-memory/templates/` | Copyable note templates |
| `docs/avengers-memory/schemas/` | Frontmatter contracts |

See [docs/AVENGERS_MEMORY.md](docs/AVENGERS_MEMORY.md).

## Install

Clone and validate:

```bash
git clone https://github.com/thepraggyverse/avengers.git ~/plugins/avengers
cd ~/plugins/avengers
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
```

Install options:

| Harness | Recommended Path |
|---|---|
| Codex App | `python3 scripts/install_codex_plugin.py --apply` |
| Codex CLI | `codex plugin marketplace add "$PWD"`, then install through `/plugins` |
| Claude Code | `/plugin marketplace add thepraggyverse/avengers`, then `/plugin install avengers` |
| Cursor | Source plugin if supported, or symlink into `~/.cursor/skills` |
| OpenCode | Use `.opencode/INSTALL.md` |
| Pi | Use `.pi/extensions/avengers.ts` |
| Gemini CLI | `gemini extensions install "$PWD"` |
| Generic skill harness | `python3 scripts/install_symlinks.py --apply --home <skill-home>` |

Detailed install guide: [docs/INSTALL.md](docs/INSTALL.md)

## Update

Checkout update:

```bash
cd ~/plugins/avengers
python3 scripts/update_avengers.py --apply
```

Manual development update:

```bash
AVENGERS_CORPUS_DIR="/path/to/private/corpus" python3 scripts/generate_avengers_pack.py
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
```

Update details: [docs/UPDATE.md](docs/UPDATE.md)

## Testing

```bash
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
python3 scripts/simulate_routes.py "Save what we learned from this Avengers run."
```

Testing guide: [docs/TESTING.md](docs/TESTING.md)

## Uninstall

Native plugin installs should be removed through the harness plugin UI or command.

Flat symlink installs can be removed by deleting `a-*` symlinks from the skill home you installed into. The repo never needs your private corpus to be deleted.

## Repo Layout

```text
avengers/
├── .codex-plugin/              # Codex native plugin manifest
├── .claude-plugin/             # Claude-compatible plugin metadata
├── .cursor-plugin/             # Cursor plugin metadata
├── .agents/plugins/            # Local marketplace metadata
├── .avengers/                  # Example local config
├── .opencode/                  # OpenCode helper
├── .pi/                        # Pi extension helper
├── skills/                     # 112 generated A-prefixed skills
├── references/                 # manifest, source map, principles, corpus index
├── scripts/                    # generate, validate, install, update, simulate, search
├── tests/                      # unit and routing-simulation tests
├── CHANGELOG.md                # release notes and verification history
└── docs/                       # install, workflow, examples, memory, inventory, testing
```

## Local Corpus Support

The public repo contains distilled skill instructions and source-file hooks only. It does not include full transcripts, captions, books, movie scripts, or private notes.

If you have your own local notes or transcripts, point the search script at them:

```bash
export AVENGERS_CORPUS_DIR="$HOME/Documents/Avengers Corpus"
python3 scripts/search_corpus.py "permission trap"
```

You can also set `corpus.path` in `.avengers/config.local.yaml`.

See [docs/CORPUS.md](docs/CORPUS.md).

## Independence And Rights

This is an independent educational and productivity tool. It is not affiliated with or endorsed by Marvel, Disney, New Rockstars, ScreenCrush, Every, Matt Pocock, or any other rightsholder mentioned in source-file hooks.

The MIT license applies to this repository's original code, generated skill text, tests, and documentation. It does not grant rights to third-party characters, trademarks, films, videos, transcripts, books, or commentary.

# Avengers Skills

Avengers is a pack of **107 A-prefixed agent skills** for turning Tony Stark, Iron Man, Avengers, MCU story analysis, leadership, prototyping, mistakes, resourcefulness, mentorship, risk, and source-grounded knowledge work into reusable operating modes.

The skills are small, searchable, and composable. Use one skill directly when you know what you need, or start with the router when the request is broad.

```text
$a-stark-router
$a-stark-operating-system
$a-mark-one-prototype
$a-cave-resourcefulness
$a-mistake-to-upgrade
$a-armor-around-world-check
```

Every exposed skill starts with `a-` so searching for `A`, `a-`, `Avengers`, `Tony Stark`, or `Iron Man` surfaces the pack in Codex and other skill harnesses.

## What These Skills Do

| Area | Skills | What They Help With |
|---|---:|---|
| Tony Stark Core | 9 | First principles, speed with feedback, lab mode, self-made identity, operating loops |
| Problem Solving | 9 | Constraints, root cause, pressure decisions, crisis plans, trapped/cave-style problem work |
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
| Knowledge System | 7 | Source-grounded synthesis, corpus search, book/podcast-to-skill extraction, pack maintenance |

Full inventory: [docs/SKILL_INVENTORY.md](docs/SKILL_INVENTORY.md)

## Main Loop

```text
route -> frame -> build -> test -> upgrade -> govern -> ground -> compound
```

| Step | Use When | Start With | Output |
|---|---|---|---|
| Route | You are not sure which lens fits. | `$a-stark-router` | 1-3 best skills and first move |
| Frame | You want a complete Stark-style pass. | `$a-stark-operating-system` | Mission, block, Mark 1, test, upgrade, risk |
| Build | You need forward motion now. | `$a-mark-one-prototype` | Crude working version |
| Test | You have a draft or MVP. | `$a-mark-two-test-flight` | Stress test and weakness list |
| Upgrade | Something failed. | `$a-mistake-to-upgrade` | Upgrade rule and prevention rule |
| Govern | Power, safety, or team consequences matter. | `$a-armor-around-world-check` | Ethical boundary and accountability |
| Ground | You want source-backed answers. | `$a-source-grounded-synthesis` | Synthesis with source file names |
| Compound | The pack or knowledge base needs refreshing. | `$a-skill-pack-builder` | Regenerated pack and validation report |

Workflow guide: [docs/WORKFLOW.md](docs/WORKFLOW.md)
Example recipes: [docs/EXAMPLES.md](docs/EXAMPLES.md)

## Install

Clone:

```bash
git clone https://github.com/thepraggyverse/avengers.git ~/plugins/avengers
cd ~/plugins/avengers
```

Validate:

```bash
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
```

### Install Matrix

| Harness | Recommended Path |
|---|---|
| Codex App | `python3 scripts/install_codex_plugin.py --apply` |
| Codex CLI | Add marketplace with `codex plugin marketplace add "$PWD"`, then install through `/plugins`, or symlink into `~/.codex/skills` |
| Claude Code | `/plugin marketplace add thepraggyverse/avengers` then `/plugin install avengers`, or run `claude --plugin-dir "$PWD"` for local dev |
| Cursor | Install from source if plugin support is available, or symlink into `~/.cursor/skills` |
| GitHub Copilot plugin hosts | Use the Claude-compatible plugin manifest where supported, or symlink/copy `skills/a-*` |
| Qwen Code / Claude-compatible installers | Install from GitHub as a Claude-compatible plugin when supported |
| OpenCode | Use `.opencode/INSTALL.md` or symlink/copy the skills directory |
| Pi | Use the `.pi/extensions/avengers.ts` extension from this checkout |
| Gemini CLI | `gemini extensions install "$PWD"` |
| OpenClaw / custom harnesses | `python3 scripts/install_symlinks.py --apply --home <skill-home>` |

Detailed install and update guide: [docs/INSTALL.md](docs/INSTALL.md)
Harness compatibility notes: [docs/HARNESSES.md](docs/HARNESSES.md)
Symlink guide: [docs/SYMLINKS.md](docs/SYMLINKS.md)

## Update

For a checkout-based install:

```bash
cd ~/plugins/avengers
python3 scripts/update_avengers.py --apply
```

That pulls the latest changes, regenerates derived skill/docs files, validates the pack, and optionally refreshes symlinks or the Codex personal marketplace entry.

Manual update:

```bash
git pull --ff-only
python3 scripts/generate_avengers_pack.py
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
```

For marketplace-managed installs, update through the harness plugin UI or command first, then restart or reload the harness so cached skills refresh.

Update details: [docs/UPDATE.md](docs/UPDATE.md)

## Repo Layout

```text
avengers/
├── .codex-plugin/              # Codex native plugin manifest
├── .claude-plugin/             # Claude-compatible plugin and marketplace metadata
├── .cursor-plugin/             # Cursor plugin metadata
├── .agents/plugins/            # Local marketplace metadata
├── .opencode/                  # OpenCode install helper
├── .pi/                        # Pi extension helper
├── skills/                     # 107 generated A-prefixed skills
├── references/                 # manifest, source map, principles, corpus index
├── scripts/                    # generate, validate, install, update, simulate, search
├── tests/                      # unit and routing-simulation tests
└── docs/                       # install, workflow, examples, inventory, testing, audit
```

## Local Corpus Support

The public repo contains distilled skill instructions and source-file hooks only. It does not include full transcripts, captions, books, movie scripts, or private notes.

If you have your own local notes or transcripts, point the search script at them:

```bash
export AVENGERS_CORPUS_DIR="$HOME/Documents/Avengers Corpus"
python3 scripts/search_corpus.py "permission trap"
```

See [docs/CORPUS.md](docs/CORPUS.md).

## Development

Regenerate and test:

```bash
python3 scripts/generate_avengers_pack.py
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
```

Simulate routing:

```bash
python3 scripts/simulate_routes.py "Break down Iron Man 2 Easter eggs and later MCU connections."
```

Testing details: [docs/TESTING.md](docs/TESTING.md)

## Independence And Rights

This is an independent educational and productivity tool. It is not affiliated with or endorsed by Marvel, Disney, New Rockstars, ScreenCrush, Every, or any other rightsholder mentioned in source-file hooks.

The MIT license applies to this repository's original code, generated skill text, tests, and documentation. It does not grant rights to third-party characters, trademarks, films, videos, transcripts, books, or commentary.

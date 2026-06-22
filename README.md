# Avengers Skill Pack

An unofficial, fan-made operating-system skill pack for Codex-compatible agents.

Avengers turns Tony Stark, Iron Man, Avengers, MCU story analysis, leadership, risk, prototyping, resourcefulness, mentorship, and source-grounded knowledge work into **107 A-prefixed skills**.

Every skill starts with `a-` so it is easy to search in Codex or any flat skill harness:

```text
a-stark-router
a-stark-operating-system
a-mark-one-prototype
a-cave-resourcefulness
a-mistake-to-upgrade
a-armor-around-world-check
```

This repository ships distilled skills and metadata only. It does **not** include full movie scripts, YouTube transcripts, books, or other copyrighted source material.

## Philosophy

Avengers OS borrows the compound-engineering idea that each unit of work should make future work easier. Here, the "work" is not only code. It can be deciding, building, recovering, mentoring, communicating, or learning.

The pack is built around a simple idea:

```text
Experience -> operating lens -> concrete output -> reusable learning
```

| Principle | Meaning | Example Skills |
|---|---|---|
| Build the Mark 1 | Create the crude first version before waiting for certainty. | `a-mark-one-prototype`, `a-stark-build-before-you-believe` |
| Upgrade from mistakes | Treat failures as design data. | `a-mistake-to-upgrade`, `a-anti-repeat-control` |
| Use what exists | Constraints are materials. | `a-cave-resourcefulness`, `a-functional-attributes` |
| Translate foresight | Seeing the risk early is not enough; others need a bridge. | `a-curse-of-knowledge-translator`, `a-shared-burden-protocol` |
| Prevent Ultron loops | Safety systems need consent, oversight, and rollback. | `a-armor-around-world-check`, `a-ethics-of-control` |
| Compound the knowledge | Each run should leave behind a sharper rule, prompt, source hook, or test. | `a-knowledge-index-curator`, `a-skill-pack-builder` |

## Main Loop

Use whichever steps fit the task. Start with the router when the next move is unclear.

```text
route -> frame -> build -> test -> upgrade -> govern -> ground -> compound
```

| Step | Use When | Primary Skills | Output |
|---|---|---|---|
| Route | The request is broad or ambiguous. | `a-stark-router` | Best skill plus supporting skills |
| Frame | The user wants a complete Stark-style operating pass. | `a-stark-operating-system` | Mission, block, Mark 1, test, upgrade, risk |
| Build | The user needs forward motion. | `a-mark-one-prototype`, `a-cave-resourcefulness` | Crude working version |
| Test | The user has a draft, MVP, or plan. | `a-mark-two-test-flight`, `a-icing-problem-review` | Stress test and weakness list |
| Upgrade | Something failed or underperformed. | `a-mistake-to-upgrade`, `a-upgrade-chain-mapper` | Upgrade rule and prevention rule |
| Govern | Power, safety, or team consequences matter. | `a-armor-around-world-check`, `a-civil-war-conflict-map` | Ethical boundary and accountability |
| Ground | The user asks where an idea came from. | `a-source-grounded-synthesis`, `a-quote-example-finder` | Source-backed synthesis |
| Compound | The pack itself needs refresh or pruning. | `a-skill-pack-builder`, `a-skill-pruner` | Regenerated pack and validation report |

Read the full workflow guide: [docs/WORKFLOW.md](docs/WORKFLOW.md).

## What's In The Box

| Area | Count | What It Does |
|---|---:|---|
| Skills | 107 | A-prefixed operating modes under `skills/` |
| Tier 1 orchestration skills | 5 | Router, full Stark OS, source grounding, pack builder |
| References | 6 | Manifest, source map, corpus index, story map, principles |
| Scripts | 6 | Generate, validate, install, symlink, search, simulate |
| Tests | 10 checks | Unit tests and routing simulations |
| Docs | 7+ pages | Install, symlinks, corpus, testing, workflow, examples, inventory |

## Skill Tiers

| Tier | Count | Role |
|---|---:|---|
| 1 | 5 | Orchestration, source grounding, and pack operations |
| 2 | 59 | Core operating modes |
| 3 | 30 | Specialized lenses |
| 4 | 13 | Corpus, story, and knowledge tools |

## Core Skill Inventory

| Skill | Purpose | Example |
|---|---|---|
| `a-stark-router` | Choose the right Avengers skill or skill chain. | `Use $a-stark-router. I keep waiting for approval before starting.` |
| `a-stark-operating-system` | Run the complete Stark loop. | `Use $a-stark-operating-system on this product idea.` |
| `a-mark-one-prototype` | Define the crude first working version. | `Use $a-mark-one-prototype to define the first app version.` |
| `a-mistake-to-upgrade` | Turn failure into a system upgrade. | `Use $a-mistake-to-upgrade on this failed launch.` |
| `a-cave-resourcefulness` | Solve with limited resources. | `Use $a-cave-resourcefulness with only what I have now.` |
| `a-permission-trap-breaker` | Replace approval-seeking with bounded action. | `Use $a-permission-trap-breaker; I am waiting to be chosen.` |
| `a-armor-around-world-check` | Catch overcontrol and Ultron-style risk. | `Use $a-armor-around-world-check on this automation.` |
| `a-civil-war-conflict-map` | Map conflicts where both sides have real values. | `Use $a-civil-war-conflict-map on this team split.` |
| `a-source-grounded-synthesis` | Answer from local source hooks and cite file names. | `Use $a-source-grounded-synthesis with my Avengers corpus.` |
| `a-skill-pack-builder` | Regenerate and validate the pack. | `Use $a-skill-pack-builder after changing triggers.` |

Full 107-skill table with tiers, purposes, and examples: [docs/SKILL_INVENTORY.md](docs/SKILL_INVENTORY.md).

## Quick Examples

| User Request | Start With | Follow With |
|---|---|---|
| "I need the first version of this app today." | `a-mark-one-prototype` | `a-mark-two-test-flight` |
| "My launch failed." | `a-mistake-to-upgrade` | `a-anti-repeat-control` |
| "I have no money or tools." | `a-cave-resourcefulness` | `a-functional-attributes` |
| "I am waiting for permission." | `a-permission-trap-breaker` | `a-stark-confidence` |
| "The team is split." | `a-civil-war-conflict-map` | `a-accords-governance` |
| "This automation might become too powerful." | `a-armor-around-world-check` | `a-ethics-of-control` |
| "Where does this idea come from?" | `a-source-grounded-synthesis` | `a-quote-example-finder` |

More recipes: [docs/EXAMPLES.md](docs/EXAMPLES.md).

## Install

Clone the repo:

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

| Target | Recommended Install |
|---|---|
| Codex App | `python3 scripts/install_codex_plugin.py --apply` |
| Codex CLI / flat skill home | `python3 scripts/install_symlinks.py --apply --home ~/.codex/skills` |
| Claude-style skill home | `python3 scripts/install_symlinks.py --apply --home ~/.claude/skills` |
| Shared agent home | `python3 scripts/install_symlinks.py --apply --home ~/.agents/skills` |
| OpenClaw | `python3 scripts/install_symlinks.py --apply --home ~/.openclaw/skills` |
| OpenClaw Codex home | `python3 scripts/install_symlinks.py --apply --home ~/.openclaw/acpx/codex-home/skills` |
| Custom harness | Symlink `skills/a-*` into the harness skill directory |

Detailed install guide: [docs/INSTALL.md](docs/INSTALL.md).
Symlink guide: [docs/SYMLINKS.md](docs/SYMLINKS.md).

## Where Things Live

```text
avengers/
├── .codex-plugin/              # Codex plugin manifest
├── skills/                     # 107 generated A-prefixed skills
├── references/                 # manifest, source map, principles, corpus index
├── scripts/                    # generate, validate, install, simulate, search
├── tests/                      # unit and routing-simulation tests
└── docs/                       # install, workflow, examples, inventory, testing
```

## Local Corpus Support

The public repo does not include full transcripts. If you have your own local notes or transcripts, point scripts at them:

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

Testing details: [docs/TESTING.md](docs/TESTING.md).

## Legal / Attribution

This is an unofficial fan-made tool. It is not affiliated with, endorsed by, sponsored by, or connected to Marvel, Disney, New Rockstars, ScreenCrush, Every, or any other rightsholder mentioned in source-file hooks.

The MIT license applies to this repository's original code, generated skill text, tests, and documentation. It does not grant rights to any third-party characters, trademarks, films, videos, transcripts, books, or commentary.

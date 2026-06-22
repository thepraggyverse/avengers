# Contributing

Contributions are welcome if they keep the pack public-safe and low-dependency.

## Good Contributions

- Better skill triggers.
- Better output contracts.
- New simulation prompts.
- More portable install docs.
- Improved validation.
- Concise source hooks that do not copy protected text.

## Do Not Add

- Full transcripts, captions, scripts, or books.
- Long copyrighted excerpts.
- Secrets, API keys, or local personal paths.
- Generated caches such as `__pycache__`.
- Unofficial claims of affiliation with Marvel, Disney, New Rockstars, ScreenCrush, or any other rightsholder.

## Workflow

Edit the generator or tests first:

```bash
python3 scripts/generate_avengers_pack.py
python3 scripts/validate_skill_pack.py
python3 -m unittest discover -s tests -v
```

Use route simulation for trigger changes:

```bash
python3 scripts/simulate_routes.py "I need a Mark 1 prototype."
```


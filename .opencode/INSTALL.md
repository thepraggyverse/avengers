# Installing Avengers For OpenCode

Add this repository to the `plugin` array in your global or project `opencode.json`:

```json
{
  "plugin": ["avengers@git+https://github.com/thepraggyverse/avengers.git"]
}
```

Restart OpenCode after changing the config.

For local development from a checkout:

```json
{
  "plugin": ["/path/to/avengers"]
}
```

The OpenCode plugin helper registers the repository `skills/` directory directly.

To pin a release or commit, add a ref:

```json
{
  "plugin": ["avengers@git+https://github.com/thepraggyverse/avengers.git#main"]
}
```

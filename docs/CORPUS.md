# Corpus Notes

This repository does not include full transcripts, scripts, books, video captions, or other copyrighted source material.

The skills are distilled operating procedures. Source hooks point to possible local file names so users can ground their own private work, but the public repo only includes summaries, categories, and generated skill instructions.

## Local Corpus Directory

If you have your own local transcripts or notes, keep them outside the repo and set:

```bash
export AVENGERS_CORPUS_DIR="$HOME/Documents/Avengers Corpus"
```

Or copy `.avengers/config.local.example.yaml` to `.avengers/config.local.yaml` and set `corpus.path`.

Corpus path resolution order:

1. `AVENGERS_CORPUS_DIR`
2. `.avengers/config.local.yaml`
3. `~/Documents/Avengers Corpus`

Then run:

```bash
python3 scripts/search_corpus.py "permission trap"
python3 scripts/search_corpus.py "Mark 1"
```

## Regenerating With Local Source Counts

`scripts/generate_avengers_pack.py` uses `AVENGERS_CORPUS_DIR` to add local word counts to source hooks when matching files exist.

```bash
export AVENGERS_CORPUS_DIR="$HOME/Documents/Avengers Corpus"
python3 scripts/generate_avengers_pack.py
python3 scripts/validate_skill_pack.py
```

Do not commit private transcript files or private notes. Keep them in your local corpus directory.

## Copyright And Fair Use

Use source material responsibly. The MIT license in this repository covers only this repo's original code, skill text, tests, and documentation. It does not license third-party characters, trademarks, films, commentary, transcripts, books, or videos.

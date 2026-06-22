from __future__ import annotations

import os
import re
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS_DIR = "~/Documents/Avengers Corpus"


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _read_corpus_path_from_local_config() -> str | None:
    config_path = PLUGIN_ROOT / ".avengers" / "config.local.yaml"
    if not config_path.exists():
        return None

    in_corpus = False
    for raw_line in config_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        if re.match(r"^\S[^:]*:\s*$", line):
            in_corpus = line.strip() == "corpus:"
            continue
        if in_corpus:
            match = re.match(r"^\s+path:\s*(.+?)\s*$", line)
            if match:
                return _unquote(match.group(1))
    return None


def corpus_dir() -> Path:
    configured = os.environ.get("AVENGERS_CORPUS_DIR") or _read_corpus_path_from_local_config() or DEFAULT_CORPUS_DIR
    return Path(os.path.expandvars(configured)).expanduser()

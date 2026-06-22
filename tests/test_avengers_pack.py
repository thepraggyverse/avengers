from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))
import avengers_config  # noqa: E402

SKILLS_DIR = PLUGIN_ROOT / "skills"
MANIFEST_PATH = PLUGIN_ROOT / "references" / "skill-manifest.json"
PLUGIN_JSON_PATH = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
CLAUDE_PLUGIN_JSON_PATH = PLUGIN_ROOT / ".claude-plugin" / "plugin.json"
CURSOR_PLUGIN_JSON_PATH = PLUGIN_ROOT / ".cursor-plugin" / "plugin.json"
AGENTS_MARKETPLACE_PATH = PLUGIN_ROOT / ".agents" / "plugins" / "marketplace.json"
GEMINI_EXTENSION_PATH = PLUGIN_ROOT / "gemini-extension.json"
EXPECTED_SKILLS = 112
MEMORY_PATHS = [
    PLUGIN_ROOT / ".avengers" / "config.local.example.yaml",
    PLUGIN_ROOT / "docs" / "AVENGERS_MEMORY.md",
    PLUGIN_ROOT / "docs" / "AVENGERS_CONTEXT.md",
    PLUGIN_ROOT / "docs" / "avengers-memory" / "schemas" / "learning-note.schema.md",
    PLUGIN_ROOT / "docs" / "avengers-memory" / "schemas" / "run-log.schema.md",
    PLUGIN_ROOT / "docs" / "avengers-memory" / "schemas" / "handoff.schema.md",
    PLUGIN_ROOT / "docs" / "avengers-memory" / "schemas" / "refresh-report.schema.md",
    PLUGIN_ROOT / "docs" / "avengers-memory" / "templates" / "learning-note.md",
    PLUGIN_ROOT / "docs" / "avengers-memory" / "templates" / "run-log.md",
    PLUGIN_ROOT / "docs" / "avengers-memory" / "templates" / "handoff.md",
    PLUGIN_ROOT / "docs" / "avengers-memory" / "templates" / "refresh-report.md",
]


def parse_openai_yaml(text: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(("display_name:", "short_description:", "default_prompt:")):
            key, value = stripped.split(":", 1)
            values[key] = value.strip().strip('"')
    return values


class AvengersPackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        cls.by_name = {entry["name"]: entry for entry in cls.manifest}
        cls.skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())

    def test_manifest_and_directory_counts_match(self) -> None:
        self.assertEqual(EXPECTED_SKILLS, len(self.manifest))
        self.assertEqual(EXPECTED_SKILLS, len(self.skill_dirs))
        self.assertEqual(set(self.by_name), {path.name for path in self.skill_dirs})

    def test_skill_names_are_a_prefixed_hyphen_case(self) -> None:
        pattern = re.compile(r"^a-[a-z0-9]+(?:-[a-z0-9]+)*$")
        for entry in self.manifest:
            self.assertRegex(entry["name"], pattern)

    def test_each_skill_has_matching_frontmatter_and_metadata(self) -> None:
        for entry in self.manifest:
            skill_dir = SKILLS_DIR / entry["name"]
            skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn(f"name: {entry['name']}", skill_text)
            self.assertIn("## Use When", skill_text)
            self.assertIn("## Inputs", skill_text)
            self.assertIn("## Do Not Use When", skill_text)
            self.assertIn("## Output Contract", skill_text)
            self.assertIn("## Example", skill_text)
            self.assertIn("## Skill Chaining", skill_text)
            self.assertIn("## Source Hooks", skill_text)
            self.assertIn("## Safety And Grounding", skill_text)
            self.assertIn("## Cross-Harness Notes", skill_text)
            self.assertIn("## Self-Test", skill_text)

            openai_yaml_text = (skill_dir / "agents" / "openai.yaml").read_text(encoding="utf-8")
            self.assertIn("interface:", openai_yaml_text)
            interface = parse_openai_yaml(openai_yaml_text)
            self.assertEqual(entry["display_name"], interface["display_name"])
            self.assertIn(f"${entry['name']}", interface["default_prompt"])
            self.assertGreaterEqual(len(interface["short_description"]), 25)
            self.assertLessEqual(len(interface["short_description"]), 64)

    def test_skill_pairs_reference_existing_skills(self) -> None:
        known = set(self.by_name)
        for entry in self.manifest:
            for pair in entry.get("pairs_with", []):
                self.assertIn(pair, known, f"{entry['name']} points to missing pair {pair}")

    def test_tier_one_orchestration_skills_are_present(self) -> None:
        tier_one = {entry["name"] for entry in self.manifest if entry["tier"] == 1}
        self.assertEqual(
            {
                "a-stark-router",
                "a-stark-operating-system",
                "a-knowledge-index-curator",
                "a-source-grounded-synthesis",
                "a-skill-pack-builder",
                "a-avengers-setup",
                "a-avengers-compound",
                "a-avengers-refresh",
                "a-avengers-handoff",
                "a-avengers-context",
            },
            tier_one,
        )

    def test_stark_operating_system_chain_is_complete(self) -> None:
        pairs = set(self.by_name["a-stark-operating-system"]["pairs_with"])
        self.assertEqual(
            {
                "a-permission-trap-breaker",
                "a-mark-one-prototype",
                "a-mistake-to-upgrade",
                "a-armor-around-world-check",
                "a-legacy-through-mentees",
            },
            pairs,
        )

    def test_plugin_manifest_points_to_skills(self) -> None:
        plugin = json.loads(PLUGIN_JSON_PATH.read_text(encoding="utf-8"))
        self.assertEqual("avengers", plugin["name"])
        self.assertEqual("./skills/", plugin["skills"])
        self.assertIn(str(EXPECTED_SKILLS), plugin["interface"]["shortDescription"])
        self.assertIn("Avengers-inspired skill pack", plugin["description"])
        self.assertNotIn("un" + "official", json.dumps(plugin).lower())
        self.assertNotIn("operating-system", json.dumps(plugin).lower())

    def test_memory_layer_artifacts_are_present(self) -> None:
        for path in MEMORY_PATHS:
            with self.subTest(path=path):
                self.assertTrue(path.exists(), f"missing {path}")

        memory_doc = (PLUGIN_ROOT / "docs" / "AVENGERS_MEMORY.md").read_text(encoding="utf-8")
        self.assertIn("request -> skill used -> sources consulted", memory_doc)
        context_doc = (PLUGIN_ROOT / "docs" / "AVENGERS_CONTEXT.md").read_text(encoding="utf-8")
        self.assertIn("Terms To Avoid Or Clarify", context_doc)

    def test_local_config_can_supply_corpus_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config_dir = root / ".avengers"
            config_dir.mkdir()
            (config_dir / "config.local.yaml").write_text(
                'corpus:\n  path: "~/Configured Avengers Corpus"\n',
                encoding="utf-8",
            )
            with mock.patch.object(avengers_config, "PLUGIN_ROOT", root):
                with mock.patch.dict(os.environ, {}, clear=True):
                    self.assertEqual(
                        Path("~/Configured Avengers Corpus").expanduser(),
                        avengers_config.corpus_dir(),
                    )

    def test_env_corpus_path_overrides_local_config(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config_dir = root / ".avengers"
            config_dir.mkdir()
            (config_dir / "config.local.yaml").write_text(
                'corpus:\n  path: "~/Configured Avengers Corpus"\n',
                encoding="utf-8",
            )
            with mock.patch.object(avengers_config, "PLUGIN_ROOT", root):
                with mock.patch.dict(os.environ, {"AVENGERS_CORPUS_DIR": "~/Env Avengers Corpus"}, clear=True):
                    self.assertEqual(
                        Path("~/Env Avengers Corpus").expanduser(),
                        avengers_config.corpus_dir(),
                    )

    def test_required_avengers_memory_skills_are_present(self) -> None:
        for name in [
            "a-avengers-setup",
            "a-avengers-compound",
            "a-avengers-refresh",
            "a-avengers-handoff",
            "a-avengers-context",
        ]:
            with self.subTest(skill=name):
                self.assertIn(name, self.by_name)
                skill_text = (SKILLS_DIR / name / "SKILL.md").read_text(encoding="utf-8")
                self.assertIn("## Cross-Harness Notes", skill_text)
                self.assertIn("## Safety And Grounding", skill_text)

    def test_cross_harness_metadata_is_present(self) -> None:
        for path in [
            CLAUDE_PLUGIN_JSON_PATH,
            CURSOR_PLUGIN_JSON_PATH,
            AGENTS_MARKETPLACE_PATH,
            GEMINI_EXTENSION_PATH,
        ]:
            with self.subTest(path=path):
                self.assertTrue(path.exists(), f"missing {path}")
                json.loads(path.read_text(encoding="utf-8"))

        claude_plugin = json.loads(CLAUDE_PLUGIN_JSON_PATH.read_text(encoding="utf-8"))
        cursor_plugin = json.loads(CURSOR_PLUGIN_JSON_PATH.read_text(encoding="utf-8"))
        gemini_extension = json.loads(GEMINI_EXTENSION_PATH.read_text(encoding="utf-8"))
        marketplace = json.loads(AGENTS_MARKETPLACE_PATH.read_text(encoding="utf-8"))

        self.assertEqual("avengers", claude_plugin["name"])
        self.assertEqual("avengers", cursor_plugin["name"])
        self.assertEqual("GEMINI.md", gemini_extension["contextFileName"])
        self.assertEqual("avengers-plugin", marketplace["name"])
        self.assertEqual("avengers", marketplace["plugins"][0]["name"])

    def test_symlink_uninstall_leaves_foreign_a_prefixed_links(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            home = root / "skills-home"
            home.mkdir()
            foreign_source = root / "foreign-source"
            foreign_source.mkdir()
            foreign_link = home / "a-foreign-skill"
            foreign_link.symlink_to(foreign_source, target_is_directory=True)

            skill_name = "a-avengers-setup"
            subprocess.run(
                [
                    sys.executable,
                    str(PLUGIN_ROOT / "scripts" / "install_symlinks.py"),
                    "--apply",
                    "--home",
                    str(home),
                    "--skill",
                    skill_name,
                ],
                check=True,
                stdout=subprocess.PIPE,
                text=True,
            )

            avengers_link = home / skill_name
            self.assertTrue(avengers_link.is_symlink())
            self.assertTrue(foreign_link.is_symlink())

            subprocess.run(
                [
                    sys.executable,
                    str(PLUGIN_ROOT / "scripts" / "install_symlinks.py"),
                    "--uninstall",
                    "--apply",
                    "--home",
                    str(home),
                ],
                check=True,
                stdout=subprocess.PIPE,
                text=True,
            )

            self.assertFalse(avengers_link.exists())
            self.assertTrue(foreign_link.is_symlink())
            self.assertEqual(foreign_source.resolve(), foreign_link.resolve())


if __name__ == "__main__":
    unittest.main()

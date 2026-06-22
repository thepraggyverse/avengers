from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = PLUGIN_ROOT / "skills"
MANIFEST_PATH = PLUGIN_ROOT / "references" / "skill-manifest.json"
PLUGIN_JSON_PATH = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
CLAUDE_PLUGIN_JSON_PATH = PLUGIN_ROOT / ".claude-plugin" / "plugin.json"
CURSOR_PLUGIN_JSON_PATH = PLUGIN_ROOT / ".cursor-plugin" / "plugin.json"
AGENTS_MARKETPLACE_PATH = PLUGIN_ROOT / ".agents" / "plugins" / "marketplace.json"
GEMINI_EXTENSION_PATH = PLUGIN_ROOT / "gemini-extension.json"


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
        self.assertEqual(107, len(self.manifest))
        self.assertEqual(107, len(self.skill_dirs))
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
            self.assertIn("## Do Not Use When", skill_text)
            self.assertIn("## Output Contract", skill_text)
            self.assertIn("## Skill Chaining", skill_text)
            self.assertIn("## Source Hooks", skill_text)
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
        self.assertIn("107", plugin["interface"]["shortDescription"])

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


if __name__ == "__main__":
    unittest.main()

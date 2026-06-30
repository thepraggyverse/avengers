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
CI_WORKFLOW_PATH = PLUGIN_ROOT / ".github" / "workflows" / "ci.yml"
RELEASE_WORKFLOW_PATH = PLUGIN_ROOT / ".github" / "workflows" / "release.yml"
EXPECTED_SKILLS = 112
EXPECTED_VERSION = "0.2.0"
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
DOC_PATHS = [
    PLUGIN_ROOT / "README.md",
    PLUGIN_ROOT / "CHANGELOG.md",
    PLUGIN_ROOT / "SECURITY.md",
    PLUGIN_ROOT / "SUPPORT.md",
    PLUGIN_ROOT / "AGENTS.md",
    PLUGIN_ROOT / "docs" / "INSTALL.md",
    PLUGIN_ROOT / "docs" / "TESTING.md",
    PLUGIN_ROOT / "docs" / "UPDATE.md",
    PLUGIN_ROOT / "docs" / "SYMLINKS.md",
    PLUGIN_ROOT / "docs" / "DOCUMENTATION_AUDIT.md",
    PLUGIN_ROOT / "docs" / "VERSIONING.md",
    PLUGIN_ROOT / "docs" / "CODEX_PROFILES.md",
    PLUGIN_ROOT / "docs" / "USE_CASES.md",
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

    def test_manifest_versions_match(self) -> None:
        version_paths = [
            PLUGIN_JSON_PATH,
            CLAUDE_PLUGIN_JSON_PATH,
            PLUGIN_ROOT / ".claude-plugin" / "marketplace.json",
            CURSOR_PLUGIN_JSON_PATH,
            PLUGIN_ROOT / ".cursor-plugin" / "marketplace.json",
            GEMINI_EXTENSION_PATH,
        ]
        for path in version_paths:
            with self.subTest(path=path):
                data = json.loads(path.read_text(encoding="utf-8"))
                if "version" in data:
                    self.assertEqual(EXPECTED_VERSION, data["version"])
                if isinstance(data.get("metadata"), dict) and "version" in data["metadata"]:
                    self.assertEqual(EXPECTED_VERSION, data["metadata"]["version"])

    def test_release_and_support_docs_are_present(self) -> None:
        for path in [
            PLUGIN_ROOT / "CHANGELOG.md",
            PLUGIN_ROOT / "SECURITY.md",
            PLUGIN_ROOT / "SUPPORT.md",
            PLUGIN_ROOT / "docs" / "VERSIONING.md",
            PLUGIN_ROOT / "docs" / "CODEX_PROFILES.md",
            PLUGIN_ROOT / "docs" / "USE_CASES.md",
            CI_WORKFLOW_PATH,
            RELEASE_WORKFLOW_PATH,
            PLUGIN_ROOT / ".github" / "ISSUE_TEMPLATE" / "install_bug.yml",
            PLUGIN_ROOT / ".github" / "ISSUE_TEMPLATE" / "skill_routing_bug.yml",
            PLUGIN_ROOT / ".github" / "ISSUE_TEMPLATE" / "docs_bug.yml",
            PLUGIN_ROOT / ".github" / "ISSUE_TEMPLATE" / "feature_request.yml",
            PLUGIN_ROOT / ".github" / "ISSUE_TEMPLATE" / "config.yml",
            PLUGIN_ROOT / "assets" / "icon.svg",
            PLUGIN_ROOT / "assets" / "README.md",
            PLUGIN_ROOT / "scripts" / "doctor.py",
            PLUGIN_ROOT / "scripts" / "prepare_release.py",
        ]:
            with self.subTest(path=path):
                self.assertTrue(path.exists(), f"missing {path}")

    def test_docs_reference_doctor_and_ci(self) -> None:
        readme = (PLUGIN_ROOT / "README.md").read_text(encoding="utf-8")
        testing = (PLUGIN_ROOT / "docs" / "TESTING.md").read_text(encoding="utf-8")
        agents = (PLUGIN_ROOT / "AGENTS.md").read_text(encoding="utf-8")
        workflow = CI_WORKFLOW_PATH.read_text(encoding="utf-8")
        release_workflow = RELEASE_WORKFLOW_PATH.read_text(encoding="utf-8")

        self.assertIn("python3 scripts/doctor.py", readme)
        self.assertIn("python3 scripts/doctor.py", testing)
        self.assertIn("python3 scripts/doctor.py", agents)
        self.assertIn("python3 scripts/doctor.py", workflow)
        self.assertIn("install-smoke", workflow)
        self.assertIn("install_symlinks.py --uninstall", workflow)
        self.assertIn("python3 scripts/doctor.py", release_workflow)

    def test_docs_reference_safe_uninstall(self) -> None:
        for path in [
            PLUGIN_ROOT / "README.md",
            PLUGIN_ROOT / "docs" / "INSTALL.md",
            PLUGIN_ROOT / "docs" / "SYMLINKS.md",
            PLUGIN_ROOT / "SECURITY.md",
            PLUGIN_ROOT / "docs" / "CODEX_PROFILES.md",
        ]:
            with self.subTest(path=path):
                text = path.read_text(encoding="utf-8")
                self.assertIn("install_symlinks.py --uninstall", text)
                self.assertNotRegex(text, r"find .*a-\*.*-delete")

    def test_docs_reference_version_support_and_security(self) -> None:
        readme = (PLUGIN_ROOT / "README.md").read_text(encoding="utf-8")
        audit = (PLUGIN_ROOT / "docs" / "DOCUMENTATION_AUDIT.md").read_text(encoding="utf-8")
        versioning = (PLUGIN_ROOT / "docs" / "VERSIONING.md").read_text(encoding="utf-8")
        support = (PLUGIN_ROOT / "SUPPORT.md").read_text(encoding="utf-8")
        security = (PLUGIN_ROOT / "SECURITY.md").read_text(encoding="utf-8")

        self.assertIn("SECURITY.md", readme)
        self.assertIn("SUPPORT.md", readme)
        self.assertIn("docs/VERSIONING.md", readme)
        self.assertIn("docs/CODEX_PROFILES.md", readme)
        self.assertIn("docs/USE_CASES.md", readme)
        self.assertIn("SECURITY.md", audit)
        self.assertIn("SUPPORT.md", audit)
        self.assertIn(EXPECTED_VERSION, versioning)
        self.assertIn("private corpus", support.lower())
        self.assertIn(".avengers/config.local.yaml", security)

    def test_use_cases_have_expected_skill_names(self) -> None:
        text = (PLUGIN_ROOT / "docs" / "USE_CASES.md").read_text(encoding="utf-8")
        for name in [
            "a-stark-router",
            "a-mark-one-prototype",
            "a-mistake-to-upgrade",
            "a-avengers-compound",
            "a-avengers-refresh",
            "a-avengers-handoff",
        ]:
            with self.subTest(skill=name):
                self.assertIn(name, text)

    def test_prepare_release_updates_versioning_policy(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs_dir = root / "docs"
            docs_dir.mkdir(parents=True)
            versioning = PLUGIN_ROOT / "docs" / "VERSIONING.md"
            target = docs_dir / "VERSIONING.md"
            target.write_text(versioning.read_text(encoding="utf-8"), encoding="utf-8")

            import prepare_release  # noqa: PLC0415

            with mock.patch.object(prepare_release, "PLUGIN_ROOT", root):
                prepare_release.update_versioning_doc("0.3.0")

            text = target.read_text(encoding="utf-8")
            self.assertIn("```text\n0.3.0\n```", text)
            self.assertIn("The latest release is 0.3.0.", text)
            self.assertIn("git tag v<version>", text)
            self.assertNotIn("git tag v0.2.0", text)

    def test_docs_do_not_reintroduce_stale_public_wording_or_private_paths(self) -> None:
        stale = re.compile(r"un" + "official|10" + "7 A-prefixed|Skills: " + "107|Manifest entries: " + "107", re.IGNORECASE)
        private = re.compile(r"/" + "Users/" + "praggy|000 " + "iCloud|Documents/" + "000")
        for path in DOC_PATHS:
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path):
                self.assertIsNone(stale.search(text))
                self.assertIsNone(private.search(text))

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

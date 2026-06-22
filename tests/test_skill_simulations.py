from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = PLUGIN_ROOT / "skills"
MANIFEST_PATH = PLUGIN_ROOT / "references" / "skill-manifest.json"


SIMULATIONS = [
    {
        "prompt": "I keep waiting for approval before I start my AI product. Which Avengers mode should I use?",
        "expected": ["a-stark-router", "a-permission-trap-breaker", "a-mark-one-prototype"],
        "must_not": ["a-mcu-easter-egg-breakdown"],
    },
    {
        "prompt": "Give me the Mark 1 version of this app idea so I can build today.",
        "expected": ["a-mark-one-prototype", "a-mark-two-test-flight"],
        "must_not": ["a-captain-america-leadership"],
    },
    {
        "prompt": "My launch failed. Turn the mistake into the next suit upgrade.",
        "expected": ["a-mistake-to-upgrade", "a-anti-repeat-control"],
        "must_not": ["a-spider-man-legacy-analysis"],
    },
    {
        "prompt": "I have almost no money or tools. Help me solve this like cave Tony.",
        "expected": ["a-cave-resourcefulness", "a-functional-attributes", "a-scrap-metal-solution"],
        "must_not": ["a-doomsday-foreshadowing"],
    },
    {
        "prompt": "I am running too many projects at once and losing the thread.",
        "expected": ["a-multi-project-reactor", "a-context-switch-control", "a-project-portfolio-radar"],
        "must_not": ["a-thanos-logic-detector"],
    },
    {
        "prompt": "The team is split like Civil War. Both sides have valid values.",
        "expected": ["a-civil-war-conflict-map", "a-accords-governance", "a-stark-cap-balance"],
        "must_not": ["a-mark-one-prototype"],
    },
    {
        "prompt": "I am mentoring a junior builder but I think I am overprotecting them.",
        "expected": ["a-peter-parker-mentor", "a-mentor-boundary-check", "a-training-wheels-protocol"],
        "must_not": ["a-infinity-saga-patterns"],
    },
    {
        "prompt": "This safety automation might become Ultron. Check the ethics and control risk.",
        "expected": ["a-armor-around-world-check", "a-ultron-failure-review", "a-ethics-of-control"],
        "must_not": ["a-talk-like-stark"],
    },
    {
        "prompt": "I need to explain a future risk that nobody else sees without sounding arrogant.",
        "expected": ["a-curse-of-knowledge-translator", "a-curse-of-being-right", "a-shared-burden-protocol"],
        "must_not": ["a-suit-tech-catalog"],
    },
    {
        "prompt": "Find where the transcripts support Tony learning from mistakes.",
        "expected": ["a-source-grounded-synthesis", "a-knowledge-index-curator", "a-quote-example-finder"],
        "must_not": ["a-energy-allocation"],
    },
    {
        "prompt": "Break down Iron Man 2 Easter eggs and how it sets up later MCU connections.",
        "expected": ["a-mcu-easter-egg-breakdown", "a-mcu-timeline-rewatch"],
        "must_not": ["a-lean-six-sigma-stark"],
    },
    {
        "prompt": "Refresh the Avengers plugin from the manifest and verify all generated skills.",
        "expected": ["a-skill-pack-builder", "a-knowledge-index-curator"],
        "must_not": ["a-fear-to-motion"],
    },
    {
        "prompt": "Set up Avengers for this repo in Codex with a local corpus path and symlink policy.",
        "expected": ["a-avengers-setup"],
        "must_not": ["a-mcu-easter-egg-breakdown"],
    },
    {
        "prompt": "Save what we learned from this Avengers run as a reusable memory note.",
        "expected": ["a-avengers-compound"],
        "must_not": ["a-talk-like-stark"],
    },
    {
        "prompt": "Audit stale Avengers memory notes and overlapping skills, then write a refresh report.",
        "expected": ["a-avengers-refresh", "a-skill-pruner"],
        "must_not": ["a-mark-one-prototype"],
    },
    {
        "prompt": "Write a handoff so the next agent can continue this Avengers plugin work.",
        "expected": ["a-avengers-handoff"],
        "must_not": ["a-thanos-logic-detector"],
    },
    {
        "prompt": "Update the Avengers context glossary with this recurring operating principle.",
        "expected": ["a-avengers-context"],
        "must_not": ["a-hulkbuster-contingency"],
    },
]


class SkillSimulationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        cls.by_name = {entry["name"]: entry for entry in cls.manifest}
        cls.search_blobs = {}
        for entry in cls.manifest:
            text = (SKILLS_DIR / entry["name"] / "SKILL.md").read_text(encoding="utf-8")
            searchable = " ".join([
                entry["name"],
                entry["display_name"],
                entry["summary"],
                " ".join(entry["triggers"]),
                entry["category"],
                text,
            ]).lower()
            cls.search_blobs[entry["name"]] = searchable

    def score(self, prompt: str) -> list[str]:
        prompt_lower = prompt.lower()
        tokens = [
            token
            for token in re.findall(r"[a-z0-9]+", prompt_lower)
            if len(token) > 2 and token not in {"the", "and", "for", "that", "this", "with", "from", "into"}
        ]
        scores = []
        for name, blob in self.search_blobs.items():
            entry = self.by_name[name]
            score = sum(1 for token in tokens if token in blob)
            for trigger in entry["triggers"]:
                trigger_lower = trigger.lower()
                trigger_tokens = [t for t in re.findall(r"[a-z0-9]+", trigger_lower) if len(t) > 2]
                if trigger_lower and trigger_lower in prompt_lower:
                    score += 14
                elif trigger_tokens and all(t in prompt_lower for t in trigger_tokens):
                    score += 6
            for chunk in name.removeprefix("a-").split("-"):
                if len(chunk) > 2 and chunk in prompt_lower:
                    score += 3
            for token in re.findall(r"[a-z0-9]+", entry["summary"].lower()):
                if len(token) > 4 and token in prompt_lower:
                    score += 2
            if name in prompt_lower:
                score += 8
            if "avengers" in prompt_lower and name == "a-stark-router":
                score += 4
            scores.append((score, name))
        return [name for score, name in sorted(scores, reverse=True) if score > 0][:12]

    def test_simulated_prompts_route_to_expected_skills(self) -> None:
        for sim in SIMULATIONS:
            with self.subTest(prompt=sim["prompt"]):
                ranked = self.score(sim["prompt"])
                ranked_set = set(ranked[:8])
                self.assertTrue(
                    set(sim["expected"]) & ranked_set,
                    f"Expected one of {sim['expected']} in top routes, got {ranked[:8]}",
                )
                self.assertFalse(
                    set(sim["must_not"]) & set(ranked[:5]),
                    f"Unexpected skill appeared in top routes: {ranked[:5]}",
                )

    def test_expected_simulation_skills_have_output_contracts(self) -> None:
        for sim in SIMULATIONS:
            for name in sim["expected"]:
                with self.subTest(skill=name):
                    self.assertIn(name, self.by_name)
                    skill_text = (SKILLS_DIR / name / "SKILL.md").read_text(encoding="utf-8")
                    for field in self.by_name[name]["output_contract"]:
                        self.assertIn(f"`{field}`", skill_text)

    def test_expected_simulation_skill_chains_are_valid(self) -> None:
        known = set(self.by_name)
        for sim in SIMULATIONS:
            for name in sim["expected"]:
                with self.subTest(skill=name):
                    for pair in self.by_name[name].get("pairs_with", []):
                        self.assertIn(pair, known)


if __name__ == "__main__":
    unittest.main()

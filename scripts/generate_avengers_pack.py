#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = PLUGIN_ROOT / "skills"
REFERENCES_DIR = PLUGIN_ROOT / "references"
CORPUS_DIR = Path(os.environ.get("AVENGERS_CORPUS_DIR", "~/Documents/Avengers Corpus")).expanduser()


SOURCE_FILES = [
    "10 Tony Stark Habits That Make You Unstoppable.txt",
    "24 Mistakes that made Iron Man Stronger.txt",
    "AVENGERS Breakdown! Endgame Easter Eggs & New Details You Missed!  Infinity Saga Rewatch.txt",
    "AVENGERS INFINITY WAR Review & Analysis #NewRockstarsNews.txt",
    "Avengers Age of Ultron Breakdown! NEW Hidden Visual Details & Endgame Clues!.txt",
    "Avengers Endgame Breakdown! Details You Missed & New VFX Easter Eggs!  Infinity Saga Rewatch.txt",
    "Avengers Endgame REACTION - What Happens Now #NewRockstarsLive.txt",
    "Avengers Infinity War Breakdown! NEW EASTER EGGS FOUND!  Infinity Saga Rewatch.txt",
    "Be as Confident as Tony Stark.txt",
    "Become Smart like Tony Stark  In-Depth Analysis.txt",
    "Captain America Civil War Breakdown! New Easter Eggs & Details You Missed!.txt",
    "Captain America Civil War \U0001f91d Avengers Doomsday  Road to Doomsday @ IGN Live.txt",
    "Every Time Iron Man Learned from his Mistakes.txt",
    "How Avengers Age of Ultron Sets Up Avengers Doomsday  Road to Doomsday #24.txt",
    "How Tony Stark Practices Resourcefulness.txt",
    "How Tony Stark Uses Lean and Six-Sigma.txt",
    "How Tony Stark Works on Multiple Projects at Once.txt",
    "How to Lead Like Captain America.txt",
    "How to Work Like Tony Stark.txt",
    "How to Work the Problem.txt",
    "IRON MAN (2008) REVISITED  Road to Doomsday Episode 7.txt",
    "IRON MAN 2 Breakdown! Easter Eggs & MCU Phase 4 Connections!  Infinity Saga Rewatch.txt",
    "IRON MAN 2 REVISITED  Road to Doomsday Episode 12.txt",
    "IRON MAN 3 (2013) REVISITED  Road to Doomsday #18.txt",
    "IRON MAN BREAKDOWN! Tony Stark Armor Details We Missed!  The Deep Dive.txt",
    "IRON MAN Breakdown! New Details & Endgame Connections!  Infinity Saga Rewatch.txt",
    "Iron Man (2008) Pre-Infinity War Rewatch! Comic Book Easter Eggs!.txt",
    "Iron Man Armor Evolution! Suit Upgrade Breakdown! (Mark 1 - Mark 85).txt",
    "Marvel's The Avengers (2012) Pre-Infinity War Rewatch! Comic Book Easter Eggs!.txt",
    "SPIDER-MAN NO WAY HOME Breakdown! 170+ MORE Easter Eggs Found!.txt",
    "SPIDERMAN HOMECOMING Breakdown! New Hidden Easter Eggs Revealed!.txt",
    "SPIDERMAN NO WAY HOME BREAKDOWN! Easter Eggs & Details You Missed!.txt",
    "Spider-Man Far From Home Breakdown! NEW Easter Eggs You Missed!  Infinity Saga Rewatch.txt",
    "The Curse of Knowledge Explained Why Iron Man & Thanos are CONNECTED.txt",
    "Tony Stark The Curse of Being Right.txt",
    "What IRON MAN Teaches About SUCCESS 5 Life Lessons from Tony Stark.txt",
    "What Tony Stark Knows That You Don't (The Permission Trap).txt",
]


GROUPS = {
    "Tony Stark Core": {
        "tier": 2,
        "sources": ["How to Work Like Tony Stark.txt", "10 Tony Stark Habits That Make You Unstoppable.txt", "IRON MAN BREAKDOWN! Tony Stark Armor Details We Missed!  The Deep Dive.txt"],
        "skills": [
            ("stark-router", "Choose the right Avengers skill or skill chain for a broad problem.", "routing, skill choice, Avengers mode selection, broad Tony Stark guidance"),
            ("stark-operating-system", "Run the full Tony Stark operating loop from intent to prototype to upgrade.", "Stark OS, full workflow, Tony operating system, end-to-end build loop"),
            ("stark-first-principles", "Strip a challenge to constraints, physics, incentives, and actual facts.", "first principles, assumptions, what is true, fundamentals"),
            ("stark-speed-with-feedback", "Move quickly while installing feedback, tests, and correction loops.", "fast iteration, feedback loop, move quickly, speed with safety"),
            ("stark-obsessive-improvement", "Treat every output as a suit version that can be upgraded.", "continuous improvement, upgrade, iteration, better version"),
            ("stark-build-before-you-believe", "Create proof through action before confidence arrives.", "stuck, need proof, build first, confidence through evidence"),
            ("stark-tinker-loop", "Use tinkering as a disciplined observe-modify-test cycle.", "tinker, experiment, prototype loop, workshop"),
            ("stark-lab-mode", "Protect a focused invention session with clear inputs and outputs.", "deep work, lab day, invention session, focus"),
            ("stark-self-made-identity", "Convert identity from waiting to being the builder who acts.", "identity, become capable, self-made, act like builder"),
        ],
    },
    "Problem Solving": {
        "tier": 2,
        "sources": ["How to Work the Problem.txt", "How to Work Like Tony Stark.txt", "IRON MAN BREAKDOWN! Tony Stark Armor Details We Missed!  The Deep Dive.txt"],
        "skills": [
            ("work-the-problem", "Stabilize a messy situation and work the actual problem one move at a time.", "work the problem, chaos, Apollo 13, Martian, stabilize"),
            ("define-the-real-problem", "Separate the true problem from symptoms, noise, and emotional framing.", "real problem, symptoms, define, diagnose"),
            ("root-cause-reactor", "Find the reactor-level cause that powers repeated failures.", "root cause, why keeps happening, reactor, underlying cause"),
            ("constraint-inventory", "List hard constraints, movable constraints, resources, and missing parts.", "constraints, resources, limits, available parts"),
            ("under-pressure-decisions", "Make a useful decision under time pressure and incomplete information.", "urgent decision, pressure, incomplete info, choose now"),
            ("crisis-to-build-plan", "Turn a crisis into a small sequence of buildable actions.", "crisis, action plan, emergency, next steps"),
            ("scrap-metal-solution", "Design a solution from available scraps before buying or waiting.", "scrap metal, limited tools, available materials, workaround"),
            ("cave-escape-planning", "Create an escape plan from a trapped or constrained situation.", "cave, trapped, escape plan, get unstuck"),
            ("problem-stack-ranking", "Rank problems by leverage, urgency, dependency, and reversibility.", "which problem first, prioritize problems, stack ranking"),
        ],
    },
    "Mistakes And Upgrades": {
        "tier": 2,
        "sources": ["Every Time Iron Man Learned from his Mistakes.txt", "24 Mistakes that made Iron Man Stronger.txt", "Iron Man Armor Evolution! Suit Upgrade Breakdown! (Mark 1 - Mark 85).txt"],
        "skills": [
            ("mistake-to-upgrade", "Convert a failure into a specific system upgrade and prevention rule.", "mistake, failure, upgrade, lesson learned"),
            ("mark-one-prototype", "Define the crude first working version that proves motion is possible.", "Mark 1, prototype, MVP, first version"),
            ("mark-two-test-flight", "Plan the first serious test and capture what the next version must fix.", "test flight, Mark 2, first test, validate"),
            ("icing-problem-review", "Find environmental failures that only appear under stress or altitude.", "icing problem, hidden failure, environment, stress test"),
            ("suit-vulnerability-audit", "Audit a system for weak points, exposed assumptions, and brittle parts.", "vulnerability, weak points, audit, fragile system"),
            ("upgrade-chain-mapper", "Map each version to the weakness it fixed and the next upgrade.", "version history, upgrade chain, v1 v2 v3"),
            ("failure-memory-bank", "Store mistakes as reusable memory instead of private regret.", "mistake log, lessons, memory bank, retrospective"),
            ("post-battle-retro", "Run an after-action review after a project, fight, launch, or miss.", "retro, after action, postmortem, debrief"),
            ("anti-repeat-control", "Add controls that prevent the same failure from recurring.", "prevent repeat, control, guardrail, recurrence"),
        ],
    },
    "Resourcefulness": {
        "tier": 2,
        "sources": ["How Tony Stark Practices Resourcefulness.txt", "IRON MAN BREAKDOWN! Tony Stark Armor Details We Missed!  The Deep Dive.txt", "What IRON MAN Teaches About SUCCESS 5 Life Lessons from Tony Stark.txt"],
        "skills": [
            ("cave-resourcefulness", "Use limited resources creatively under severe constraints.", "resourceful, limited resources, cave, constraint"),
            ("functional-attributes", "See tools by what they can do, not what they are named.", "functional attributes, repurpose, non-obvious use"),
            ("resource-recombination", "Combine weak or partial resources into a useful stronger system.", "combine resources, recombine, patch together"),
            ("improvise-then-engineer", "Use a temporary hack first, then harden the real system.", "improvise, hack first, engineer later"),
            ("minimum-viable-armor", "Define the smallest protection or tool layer needed now.", "minimum viable armor, protection, enough safety"),
            ("salvage-tech-strategy", "Recover old assets, abandoned work, or scraps into useful inputs.", "salvage, reuse old work, abandoned assets"),
            ("constraints-as-design", "Use constraints as design material instead of excuses.", "constraints as design, limitations, turn limits"),
        ],
    },
    "Confidence And Permission": {
        "tier": 2,
        "sources": ["Be as Confident as Tony Stark.txt", "What Tony Stark Knows That You Don't (The Permission Trap).txt", "How to Work Like Tony Stark.txt"],
        "skills": [
            ("stark-confidence", "Build grounded confidence from competence, proof, and decisive action.", "confidence, Tony confidence, self belief"),
            ("permission-trap-breaker", "Find where the user is waiting for permission and define action without it.", "permission trap, waiting, approval, realistic"),
            ("audacity-calibrator", "Separate useful boldness from reckless ego or fantasy.", "audacity, bold, reckless, calibrate"),
            ("ego-to-output", "Convert ego, ambition, or swagger into concrete production.", "ego, ambition, output, arrogance"),
            ("fear-to-motion", "Turn fear into one visible action instead of rumination.", "fear, stuck, first brave action"),
            ("self-trust-builder", "Build self-trust through small kept promises and proof.", "self trust, trust myself, proof"),
            ("talk-like-stark", "Sharpen communication with confident, concise, playful authority.", "talk like Stark, sharper copy, witty confident"),
        ],
    },
    "Learning And Intelligence": {
        "tier": 2,
        "sources": ["Become Smart like Tony Stark  In-Depth Analysis.txt", "How to Work Like Tony Stark.txt", "How Tony Stark Works on Multiple Projects at Once.txt"],
        "skills": [
            ("curiosity-mastery-synthesis", "Learn through curiosity, mastery, and cross-domain synthesis.", "curiosity, mastery, synthesis, learning"),
            ("learn-like-stark", "Design an aggressive self-education loop around building.", "learn like Stark, study plan, master skill"),
            ("cross-domain-synthesis", "Connect lessons across engineering, design, story, leadership, and business.", "cross domain, synthesize, connect fields"),
            ("question-engine", "Generate sharper questions that unlock technical or strategic progress.", "questions, ask better, inquiry"),
            ("knowledge-gap-map", "Identify the exact missing knowledge blocking progress.", "knowledge gaps, what do I not know"),
            ("smart-not-genius", "Convert genius fantasy into practical learnable behaviors.", "become smarter, not genius, practical intelligence"),
            ("build-to-understand", "Use building as the fastest path to comprehension.", "learn by building, build to understand"),
        ],
    },
    "Lean Six Sigma Workflow": {
        "tier": 2,
        "sources": ["How Tony Stark Uses Lean and Six-Sigma.txt", "How to Work Like Tony Stark.txt", "How Tony Stark Works on Multiple Projects at Once.txt"],
        "skills": [
            ("lean-six-sigma-stark", "Apply define-measure-improve-control to personal or product workflows.", "lean, six sigma, DMAIC, improve workflow"),
            ("continuous-improvement-loop", "Create a recurring loop for better versions of work.", "continuous improvement, weekly improvement"),
            ("waste-hunter", "Find and remove wasted motion, waiting, rework, and clutter.", "waste, inefficiency, remove waste"),
            ("process-stabilizer", "Turn chaotic repeated work into a stable process.", "process, stabilize, repeatable"),
            ("quality-control-reactor", "Add quality checks that protect output without slowing everything.", "quality control, checks, review gate"),
            ("workflow-telemetry", "Choose measurements that reveal whether the system works.", "metrics, telemetry, measure workflow"),
            ("standardize-after-learning", "Standardize a process only after the learning loop has found what works.", "standardize, SOP, repeatable pattern"),
        ],
    },
    "Multiple Projects": {
        "tier": 2,
        "sources": ["How Tony Stark Works on Multiple Projects at Once.txt", "How Tony Stark Uses Lean and Six-Sigma.txt", "10 Tony Stark Habits That Make You Unstoppable.txt"],
        "skills": [
            ("multi-project-reactor", "Coordinate multiple active projects without losing the reactor core.", "multiple projects, too many projects, portfolio"),
            ("parallel-build-planner", "Split work into tracks that can progress in parallel.", "parallel work, dependencies, project tracks"),
            ("context-switch-control", "Reduce context switching cost between active efforts.", "context switch, switching projects"),
            ("energy-allocation", "Match tasks to current energy, attention, and leverage.", "energy, what today, attention"),
            ("project-portfolio-radar", "Maintain a radar view of active bets, status, and next moves.", "portfolio radar, active projects"),
            ("burnout-safety-check", "Detect overload and redesign the load before damage accumulates.", "burnout, overloaded, too much"),
        ],
    },
    "Leadership And Team": {
        "tier": 3,
        "sources": ["How to Lead Like Captain America.txt", "Captain America Civil War Breakdown! New Easter Eggs & Details You Missed!.txt", "Captain America Civil War \U0001f91d Avengers Doomsday  Road to Doomsday @ IGN Live.txt"],
        "skills": [
            ("captain-america-leadership", "Lead through values, steadiness, courage, and service.", "Captain America leadership, lead like Cap"),
            ("stark-cap-balance", "Balance Tony's invention drive with Steve's moral clarity.", "Tony vs Steve, balance, innovation and values"),
            ("team-assembly-avengers", "Assemble roles, strengths, gaps, and team operating rules.", "assemble team, Avengers team, roles"),
            ("leader-in-the-room", "Decide when to lead, defer, challenge, or support.", "should I lead, take charge, defer"),
            ("values-under-pressure", "Protect core values when pressure, fear, or speed rises.", "values, pressure, principles"),
            ("civil-war-conflict-map", "Map a conflict where both sides have legitimate values.", "Civil War, team conflict, competing values"),
            ("accords-governance", "Design accountability, oversight, and autonomy rules.", "governance, accords, accountability"),
            ("trust-repair-after-conflict", "Rebuild working trust after a rupture or ideological split.", "repair trust, after conflict, team split"),
        ],
    },
    "Mentorship And Peter Parker": {
        "tier": 3,
        "sources": ["SPIDERMAN HOMECOMING Breakdown! New Hidden Easter Eggs Revealed!.txt", "Spider-Man Far From Home Breakdown! NEW Easter Eggs You Missed!  Infinity Saga Rewatch.txt", "SPIDERMAN NO WAY HOME BREAKDOWN! Easter Eggs & Details You Missed!.txt"],
        "skills": [
            ("peter-parker-mentor", "Mentor a younger builder without overcontrolling their growth.", "mentor, junior builder, Peter Parker"),
            ("training-wheels-protocol", "Decide how much support, monitoring, or independence to provide.", "training wheels, support, independence"),
            ("if-youre-nothing-without-the-suit", "Separate capability from dependence on tools, status, or armor.", "nothing without the suit, tool dependence"),
            ("responsibility-before-power", "Check readiness before handing over power, tools, or visibility.", "responsibility before power, readiness"),
            ("mentor-boundary-check", "Avoid projecting personal fear onto the person being mentored.", "mentor boundary, overprotective"),
            ("legacy-through-mentees", "Pass values, standards, and judgment through mentees.", "legacy, teach, mentee"),
        ],
    },
    "Risk Ethics And Control": {
        "tier": 3,
        "sources": ["The Curse of Knowledge Explained Why Iron Man & Thanos are CONNECTED.txt", "Tony Stark The Curse of Being Right.txt", "Avengers Age of Ultron Breakdown! NEW Hidden Visual Details & Endgame Clues!.txt", "How Avengers Age of Ultron Sets Up Avengers Doomsday  Road to Doomsday #24.txt"],
        "skills": [
            ("threat-is-imminent", "Anticipate looming threats without letting fear own the solution.", "threat imminent, future risk, warning"),
            ("armor-around-world-check", "Check whether protection has become overcontrol or overengineering.", "armor around the world, overcontrol, safety system"),
            ("ultron-failure-review", "Analyze how a good-intentioned system can create unintended harm.", "Ultron, unintended consequences, backfire"),
            ("ethics-of-control", "Review consent, power, collateral effects, and governance.", "ethics, control, consent, automation risk"),
            ("thanos-logic-detector", "Detect cold utilitarian reasoning that erases people.", "Thanos logic, ends justify means, utilitarian"),
            ("curse-of-knowledge-translator", "Translate expert foresight so others can understand and act.", "curse of knowledge, explain risk, others do not see"),
            ("curse-of-being-right", "Handle being right early without becoming isolated or abrasive.", "curse of being right, I warned them"),
            ("shared-burden-protocol", "Stop carrying a threat or mission alone; distribute responsibility.", "carry alone, burden, share responsibility"),
        ],
    },
    "Armor Tech Product Design": {
        "tier": 3,
        "sources": ["Iron Man Armor Evolution! Suit Upgrade Breakdown! (Mark 1 - Mark 85).txt", "IRON MAN 2 Breakdown! Easter Eggs & MCU Phase 4 Connections!  Infinity Saga Rewatch.txt", "IRON MAN 3 (2013) REVISITED  Road to Doomsday #18.txt"],
        "skills": [
            ("suit-tech-catalog", "Catalog armor, tools, capabilities, weaknesses, and upgrade lessons.", "suit catalog, armor, Mark 85"),
            ("armor-evolution-review", "Review a product or workflow as an armor evolution line.", "armor evolution, product versions"),
            ("interface-inside-the-suit", "Design tools around the human operator, not the spectacle.", "interface, human inside suit, tool design"),
            ("jarvis-delegation", "Decide what to delegate to assistants, agents, scripts, or automations.", "JARVIS, delegate, assistant, agent"),
            ("friday-fallback-system", "Design backup assistants and recovery paths when primary systems fail.", "FRIDAY, fallback, backup assistant"),
            ("nanotech-adaptation", "Make a system modular, adaptive, and fast to reconfigure.", "nanotech, modular, adaptive"),
            ("hulkbuster-contingency", "Build a contingency for rare high-impact failure modes.", "Hulkbuster, contingency, emergency mode"),
            ("iron-legion-automation", "Design distributed helper agents or automations with oversight.", "Iron Legion, automation, helper agents"),
        ],
    },
    "MCU Story Analysis": {
        "tier": 4,
        "sources": ["IRON MAN 2 Breakdown! Easter Eggs & MCU Phase 4 Connections!  Infinity Saga Rewatch.txt", "IRON MAN 2 REVISITED  Road to Doomsday Episode 12.txt", "AVENGERS Breakdown! Endgame Easter Eggs & New Details You Missed!  Infinity Saga Rewatch.txt", "Avengers Infinity War Breakdown! NEW EASTER EGGS FOUND!  Infinity Saga Rewatch.txt", "Avengers Endgame Breakdown! Details You Missed & New VFX Easter Eggs!  Infinity Saga Rewatch.txt", "IRON MAN (2008) REVISITED  Road to Doomsday Episode 7.txt"],
        "skills": [
            ("mcu-timeline-rewatch", "Place events, callbacks, and character moves in MCU timeline context.", "MCU timeline, rewatch, continuity, later MCU connections, Iron Man 2"),
            ("mcu-easter-egg-breakdown", "Extract callbacks, visual references, comic nods, and hidden details.", "easter eggs, breakdown, hidden details, Iron Man, Iron Man 2, MCU connections"),
            ("character-arc-extractor", "Extract the character arc and practical lesson from a story segment.", "character arc, lesson, story analysis"),
            ("theme-thread-mapper", "Track a theme across movies, scenes, and transcripts.", "theme thread, map theme, recurring idea"),
            ("infinity-saga-patterns", "Analyze recurring Infinity Saga structures and payoffs.", "Infinity Saga, pattern, payoff"),
            ("doomsday-foreshadowing", "Extract possible Avengers Doomsday setup and theory hooks.", "Doomsday, foreshadowing, setup"),
            ("new-mask-same-task", "Compare Tony Stark and Doctor Doom parallels around task, mask, and control.", "new mask same task, Doom, Tony parallel"),
            ("villain-mirror-analysis", "Compare hero and villain logic to find the moral fork.", "villain mirror, Tony vs Thanos, hero villain"),
            ("spider-man-legacy-analysis", "Track Tony's legacy through Peter Parker and the Spider-Man films.", "Spider-Man legacy, Peter, Tony legacy"),
        ],
    },
    "Knowledge System": {
        "tier": 4,
        "sources": SOURCE_FILES,
        "skills": [
            ("podcast-to-skill-extractor", "Turn a transcript or podcast into candidate agent skills.", "podcast to skills, transcript extraction"),
            ("book-to-skill-extractor", "Turn book knowledge into operational skills with examples and triggers.", "book to skills, book frameworks"),
            ("knowledge-index-curator", "Maintain the Avengers corpus index, source map, and skill manifest.", "knowledge index, corpus, source map, transcripts, source files"),
            ("quote-example-finder", "Find source-grounded examples without dumping long copyrighted text.", "quote, example, source evidence, supporting examples, transcripts"),
            ("source-grounded-synthesis", "Answer using the local Avengers corpus and cite source file names.", "source grounded, use corpus, cite files, transcripts support, evidence, source files"),
            ("skill-pruner", "Review skills for keep, merge, reference-only, or remove decisions.", "prune skills, merge, keep remove"),
            ("skill-pack-builder", "Generate or refresh the Avengers plugin skill pack from the manifest.", "build skill pack, generate skills, plugin"),
        ],
    },
}


CONTRACTS = {
    "Tony Stark Core": ["Situation", "Stark Lens", "Primary Move", "Build Step", "Feedback Loop", "Next Upgrade"],
    "Problem Solving": ["Situation", "Actual Problem", "Constraints", "Available Parts", "First Move", "Next Check"],
    "Mistakes And Upgrades": ["Failure", "What It Revealed", "System Weakness", "Upgrade", "Test", "Prevention Rule"],
    "Resourcefulness": ["Goal", "Available Resources", "Functional Attributes", "Recombination", "First Build", "Upgrade Path"],
    "Confidence And Permission": ["Blocked Move", "Permission Trap", "Proof Already Available", "Bold Action", "Risk Boundary", "Next Signal"],
    "Learning And Intelligence": ["Learning Goal", "Known Base", "Knowledge Gap", "Build-to-Learn Task", "Synthesis Question", "Mastery Check"],
    "Lean Six Sigma Workflow": ["Process", "Waste or Variation", "Measure", "Improve", "Control", "Review Cadence"],
    "Multiple Projects": ["Project Set", "Reactor Core", "Parallel Tracks", "Switching Rule", "Energy Match", "Radar Update"],
    "Leadership And Team": ["Conflict or Mission", "Values at Stake", "Team Roles", "Decision Rule", "Communication Move", "Trust Follow-Up"],
    "Mentorship And Peter Parker": ["Mentee Context", "Power or Tool", "Readiness Signal", "Support Level", "Boundary", "Growth Test"],
    "Risk Ethics And Control": ["Threat", "Fear Signal", "Control Risk", "Ethical Boundary", "Shared Burden", "Governed Action"],
    "Armor Tech Product Design": ["Operator Need", "Armor Function", "Weakness", "Interface Decision", "Fallback", "Next Upgrade"],
    "MCU Story Analysis": ["Source", "Scene or Thread", "Callback", "Character Meaning", "MCU Connection", "Practical Lesson"],
    "Knowledge System": ["Input Corpus", "Extraction Goal", "Index Method", "Evidence Rule", "Output Artifact", "Maintenance Step"],
}


BASE_WORKFLOWS = {
    "Tony Stark Core": ["Name the mission in one sentence.", "Strip away theatre, ego, and inherited assumptions.", "Define the smallest artifact that can prove progress.", "Add feedback, test, or telemetry before scaling.", "Capture the next upgrade as a concrete action."],
    "Problem Solving": ["Stabilize the situation before optimizing.", "Name the actual problem separately from symptoms.", "Inventory constraints, resources, risks, and dependencies.", "Pick the next reversible move.", "Check whether the move changed the real problem."],
    "Mistakes And Upgrades": ["Describe the failure without self-protection.", "Identify the specific weakness the failure exposed.", "Design one upgrade that would have prevented or reduced it.", "Test the upgrade with a realistic stress case.", "Save the prevention rule for future work."],
    "Resourcefulness": ["Inventory what already exists.", "Translate each resource into functional attributes.", "Recombine parts into a crude useful system.", "Use the first version to escape waiting.", "Upgrade only after the crude system teaches you."],
    "Confidence And Permission": ["Name the move the user is avoiding.", "Identify whose permission they are waiting for.", "Separate real risk from social discomfort.", "Choose a bounded bold action.", "Use the result as evidence for the next move."],
    "Learning And Intelligence": ["Choose a target capability.", "Map what the user already understands.", "Identify the smallest missing concept or skill.", "Build something that forces the concept to become concrete.", "Synthesize the lesson into a reusable rule."],
    "Lean Six Sigma Workflow": ["Define the process and its intended output.", "Measure where waste, variation, or rework appears.", "Improve the highest-leverage step.", "Add a lightweight control so the improvement survives.", "Schedule the next review."],
    "Multiple Projects": ["List active projects and their next meaningful output.", "Identify the reactor core that must not lose power.", "Separate parallel tracks from blocked tracks.", "Set context-switching rules.", "Update the portfolio radar."],
    "Leadership And Team": ["Name the mission or conflict.", "Identify the values and incentives on each side.", "Clarify who should lead, advise, execute, or challenge.", "Choose the communication move that protects trust.", "Define the next accountable action."],
    "Mentorship And Peter Parker": ["Clarify what the mentee is trying to become capable of doing.", "Assess readiness with behavior, not potential alone.", "Choose support level: watch, coach, unlock, or step back.", "Avoid projecting the mentor's fear onto the mentee.", "Create a growth test with real consequences and guardrails."],
    "Risk Ethics And Control": ["Name the threat and the fear underneath it.", "Identify where control could become harm.", "Separate protection, consent, oversight, and coercion.", "Distribute responsibility instead of carrying it alone.", "Choose the governed action."],
    "Armor Tech Product Design": ["Start with the human operator's need.", "Define the armor function, not just the shiny feature.", "Find the weakness in the current version.", "Add interface and fallback decisions.", "Specify the next Mark upgrade."],
    "MCU Story Analysis": ["Identify the source, scene, or transcript segment.", "Extract the visible detail or callback.", "Connect it to character arc, theme, or continuity.", "Separate grounded evidence from speculation.", "State the practical lesson or theory hook."],
    "Knowledge System": ["Identify the input corpus and extraction goal.", "Search or index before synthesizing.", "Keep source file names attached to claims.", "Avoid long verbatim reproduction from transcripts.", "Write the reusable artifact or manifest update."],
}


DO_NOT_USE = {
    "MCU Story Analysis": ["The user needs personal productivity coaching rather than story analysis.", "The answer would rely on unsourced speculation presented as fact."],
    "Knowledge System": ["The user only needs a quick direct answer.", "The requested action would copy large transcript passages instead of synthesizing."],
    "Leadership And Team": ["The problem is a solo build decision with no team or stakeholder issue."],
    "Mentorship And Peter Parker": ["The user is not guiding another person or their own apprentice-like learning loop."],
}


SKILL_OVERRIDES = {
    "stark-router": {
        "tier": 1,
        "core": "Act as the JARVIS-style routing layer for the Avengers skill system.",
        "workflow": [
            "Read the user's request and identify the dominant problem type.",
            "Recommend one to three A-prefixed skills.",
            "Explain why each skill fits in one short line.",
            "If the first skill is obvious, apply it immediately.",
            "If the user asks for a system, chain skills rather than choosing only one.",
        ],
        "contract": ["Request", "Best Skill", "Supporting Skills", "Why", "First Applied Move"],
        "pairs": ["a-stark-operating-system", "a-knowledge-index-curator", "a-source-grounded-synthesis"],
        "self_test": "If the user asks 'Which Avengers mode fits this problem?', recommend 1-3 skills and apply the strongest one.",
    },
    "stark-operating-system": {
        "tier": 1,
        "core": "Run the complete Stark loop: permission, prototype, feedback, upgrade, ethics, and handoff.",
        "workflow": [
            "Break the user's objective into mission, constraints, available resources, and risk.",
            "Run permission-trap detection if the user is waiting.",
            "Define the Mark 1 artifact and first test.",
            "Convert likely failure into upgrade rules.",
            "Check for overcontrol, delegation, and handoff needs.",
            "Return a staged plan with the next concrete action.",
        ],
        "contract": ["Mission", "Current Block", "Mark 1", "Feedback Test", "Upgrade Rule", "Risk Check", "Next Action"],
        "pairs": ["a-permission-trap-breaker", "a-mark-one-prototype", "a-mistake-to-upgrade", "a-armor-around-world-check", "a-legacy-through-mentees"],
        "self_test": "If the user asks for the full Stark OS, produce a staged build-and-upgrade plan, not a motivational essay.",
    },
    "knowledge-index-curator": {
        "tier": 1,
        "core": "Maintain and query the Avengers source map, manifest, and transcript-derived references.",
        "workflow": [
            "Search the corpus index before making source-grounded claims.",
            "Attach source file names to extracted ideas.",
            "Update the manifest when new transcripts or books arrive.",
            "Deduplicate exact duplicate sources and preserve canonical names.",
            "Keep references concise and avoid long verbatim text.",
        ],
        "contract": ["Query", "Matched Sources", "Extracted Ideas", "Skill Links", "Index Update"],
        "pairs": ["a-source-grounded-synthesis", "a-quote-example-finder", "a-podcast-to-skill-extractor"],
        "self_test": "If the user asks where an idea came from, return source files and relevant skills without dumping full transcripts.",
    },
    "mark-one-prototype": {
        "core": "Build the crude first version that proves motion is possible before polish, scale, or certainty.",
        "workflow": [
            "Name the mission and the one function the first version must perform.",
            "List available parts, skills, time, tools, and constraints.",
            "Remove every feature that is not needed for the first proof.",
            "Define the ugly working build the user can finish next.",
            "Choose the first test and the weakness it is likely to reveal.",
            "Capture what the Mark 2 should fix.",
        ],
        "contract": ["Mission", "Essential Function", "Available Parts", "Mark 1 Build", "First Test", "Known Weaknesses", "Mark 2 Upgrade"],
        "pairs": ["a-cave-resourcefulness", "a-mark-two-test-flight", "a-mistake-to-upgrade"],
        "self_test": "If the user is waiting for perfect conditions, define a crude useful artifact they can build immediately.",
    },
    "mark-two-test-flight": {
        "core": "Design the first serious test of a prototype and convert the result into the next suit upgrade.",
        "workflow": [
            "Identify what the Mark 1 claims to prove.",
            "Create a realistic test that stresses the claim.",
            "Define what success, partial success, and failure mean.",
            "Run or outline the smallest possible test.",
            "Translate the result into a Mark 2 upgrade.",
        ],
        "contract": ["Prototype Claim", "Test Environment", "Success Signal", "Failure Signal", "Observed Weakness", "Mark 2 Upgrade"],
        "pairs": ["a-mark-one-prototype", "a-icing-problem-review", "a-upgrade-chain-mapper"],
        "self_test": "If the user has a first draft or MVP, produce a concrete stress test and next upgrade.",
    },
    "cave-resourcefulness": {
        "core": "Turn scarce materials, pressure, and constraints into a working escape path.",
        "workflow": [
            "Name the escape condition or minimum win.",
            "Inventory only what is already available.",
            "Translate each item into functional attributes.",
            "Combine attributes into a crude but useful build.",
            "Choose the next move that changes the user's position.",
        ],
        "contract": ["Escape Condition", "Available Parts", "Functional Attributes", "Crude Build", "Immediate Move", "Upgrade Later"],
        "pairs": ["a-functional-attributes", "a-scrap-metal-solution", "a-mark-one-prototype"],
        "self_test": "If the user says they lack resources, find a viable move using only what they already have.",
    },
    "permission-trap-breaker": {
        "core": "Find the hidden request for approval and replace it with a bounded act of agency.",
        "workflow": [
            "Name the action the user keeps postponing.",
            "Identify whose approval, validation, credential, or perfect condition they are waiting for.",
            "Separate legal, ethical, and practical risk from social discomfort.",
            "Define one safe-to-try move that does not require permission.",
            "Turn the result into proof for the next move.",
        ],
        "contract": ["Postponed Action", "Permission Source", "Real Risk", "False Gate", "Bounded Move", "Proof Signal"],
        "pairs": ["a-stark-confidence", "a-fear-to-motion", "a-mark-one-prototype"],
        "self_test": "If the user is waiting to be chosen, return a bounded action they can take without external validation.",
    },
    "mistake-to-upgrade": {
        "core": "Treat failure as design data and convert it into a concrete system upgrade.",
        "workflow": [
            "State the mistake without shame or defense.",
            "Identify the assumption, missing sensor, or weak mechanism it exposed.",
            "Choose the smallest upgrade that would reduce repeat risk.",
            "Define a test that proves the upgrade works.",
            "Write the prevention rule in reusable language.",
        ],
        "contract": ["Mistake", "Exposed Assumption", "Weak Mechanism", "Upgrade", "Proof Test", "Prevention Rule"],
        "pairs": ["a-failure-memory-bank", "a-anti-repeat-control", "a-upgrade-chain-mapper"],
        "self_test": "If the user describes a failure, return an upgrade and prevention rule, not reassurance alone.",
    },
    "armor-around-world-check": {
        "core": "Check whether a protective idea has become overcontrol, overengineering, or fear in armor.",
        "workflow": [
            "Name the threat the user wants to prevent.",
            "Identify who gains protection and who loses agency.",
            "Separate monitoring, prevention, consent, and coercion.",
            "Find a smaller governed safety mechanism.",
            "Define an oversight or rollback rule.",
        ],
        "contract": ["Threat", "Protection Goal", "Control Risk", "Affected People", "Smaller Safety Mechanism", "Oversight Rule"],
        "pairs": ["a-ultron-failure-review", "a-ethics-of-control", "a-shared-burden-protocol"],
        "self_test": "If the user proposes a sweeping safety system, test whether it creates an Ultron-style control failure.",
    },
    "source-grounded-synthesis": {
        "tier": 1,
        "core": "Synthesize answers from the local Avengers corpus while preserving source names and avoiding transcript dumps.",
        "workflow": [
            "Clarify the exact idea, theme, or skill the user wants grounded.",
            "Search the corpus index and source map before answering.",
            "Group evidence by source file and theme.",
            "Synthesize the answer in original words.",
            "Name the relevant source files and related A-skills.",
        ],
        "contract": ["Question", "Matched Sources", "Synthesis", "Relevant A-Skills", "Source Notes"],
        "pairs": ["a-knowledge-index-curator", "a-quote-example-finder", "a-theme-thread-mapper"],
        "self_test": "If asked to prove where an idea came from, cite source file names and summarize without copying long passages.",
    },
    "skill-pack-builder": {
        "tier": 1,
        "core": "Refresh the Avengers plugin from the manifest and verify the generated skills.",
        "workflow": [
            "Review `references/skill-manifest.json` for the intended skill set.",
            "Run `scripts/generate_avengers_pack.py` after manifest changes.",
            "Run `scripts/validate_skill_pack.py` to confirm count, schema, and skill validation.",
            "Spot-check the router, Stark OS, one specialized skill, and one knowledge skill.",
            "Report counts, validations, and remaining manual install or reload steps.",
        ],
        "contract": ["Manifest Change", "Generated Count", "Validation Result", "Spot Checks", "Next Reload Step"],
        "pairs": ["a-knowledge-index-curator", "a-skill-pruner", "a-stark-router"],
        "self_test": "If asked to rebuild the pack, regenerate and validate rather than hand-editing individual generated files.",
    },
}


PAIR_RULES = [
    ("prototype", ["a-mark-one-prototype", "a-mark-two-test-flight"]),
    ("mistake", ["a-mistake-to-upgrade", "a-anti-repeat-control"]),
    ("resource", ["a-cave-resourcefulness", "a-functional-attributes"]),
    ("confidence", ["a-stark-confidence", "a-permission-trap-breaker"]),
    ("learn", ["a-learn-like-stark", "a-build-to-understand"]),
    ("risk", ["a-threat-is-imminent", "a-armor-around-world-check"]),
    ("mentor", ["a-peter-parker-mentor", "a-training-wheels-protocol"]),
    ("team", ["a-team-assembly-avengers", "a-civil-war-conflict-map"]),
    ("mcu", ["a-mcu-timeline-rewatch", "a-mcu-easter-egg-breakdown"]),
    ("knowledge", ["a-knowledge-index-curator", "a-source-grounded-synthesis"]),
]


def title_from_slug(slug: str) -> str:
    words = slug.split("-")
    fixed = []
    for word in words:
        fixed.append({
            "mcu": "MCU",
            "jarvis": "JARVIS",
            "friday": "FRIDAY",
            "six": "Six",
            "sigma": "Sigma",
        }.get(word, word.capitalize()))
    return " ".join(fixed)


def skill_name(slug: str) -> str:
    return "a-" + slug


def display_name(slug: str) -> str:
    return "A - " + title_from_slug(slug)


def clean_yaml_text(text: str) -> str:
    return text.replace(":", "-").replace("\n", " ").strip()


def likely_pairs(slug: str, category: str) -> list[str]:
    lower = slug.replace("-", " ")
    pairs: list[str] = []
    for needle, candidates in PAIR_RULES:
        if needle in lower or needle.lower() in category.lower():
            pairs.extend(candidates)
    if category == "Tony Stark Core":
        pairs.extend(["a-stark-router", "a-stark-operating-system"])
    if category == "Knowledge System":
        pairs.extend(["a-knowledge-index-curator", "a-source-grounded-synthesis"])
    own = skill_name(slug)
    deduped = []
    for pair in pairs:
        if pair != own and pair not in deduped:
            deduped.append(pair)
    return deduped[:4]


def source_summary_for(sources: list[str]) -> list[str]:
    lines = []
    for source in sources[:6]:
        p = resolve_source_path(source)
        if p.exists():
            text = p.read_text(errors="replace")
            words = len(re.findall(r"[A-Za-z][A-Za-z'-]+", text))
            lines.append(f"- `{p.name}` ({words} words)")
        else:
            lines.append(f"- `{source}`")
    return lines


def resolve_source_path(source: str) -> Path:
    direct = CORPUS_DIR / source
    if direct.exists():
        return direct
    normalized = source.replace("'", "'").replace("’", "'")
    for candidate in CORPUS_DIR.glob("*.txt"):
        if candidate.name.replace("’", "'") == normalized:
            return candidate
    return direct


def build_manifest() -> list[dict]:
    manifest = []
    for category, group in GROUPS.items():
        for slug, summary, triggers in group["skills"]:
            override = SKILL_OVERRIDES.get(slug, {})
            tier = override.get("tier", group["tier"])
            sources = group["sources"]
            manifest.append({
                "name": skill_name(slug),
                "slug": slug,
                "display_name": display_name(slug),
                "tier": tier,
                "category": category,
                "summary": summary,
                "triggers": [t.strip() for t in triggers.split(",")],
                "source_files": sources,
                "pairs_with": override.get("pairs", likely_pairs(slug, category)),
                "output_contract": override.get("contract", CONTRACTS[category]),
                "core_idea": override.get("core", summary),
                "workflow": override.get("workflow", BASE_WORKFLOWS[category]),
                "self_test": override.get("self_test", f"If the user asks for {summary.lower()}, return the output contract fields and a concrete next action."),
            })
    names = {entry["name"] for entry in manifest}
    for entry in manifest:
        entry["pairs_with"] = [pair for pair in entry["pairs_with"] if pair in names]
    return manifest


def write_skill(entry: dict) -> None:
    path = SKILLS_DIR / entry["name"]
    agents = path / "agents"
    agents.mkdir(parents=True, exist_ok=True)

    trigger_text = ", ".join(entry["triggers"])
    verb_phrase = entry["summary"].rstrip(".")
    verb_phrase = verb_phrase[:1].lower() + verb_phrase[1:]
    desc = (
        f"Avengers skill {entry['display_name']} that helps the user to {verb_phrase}. "
        f"Use when the user mentions or needs one of these triggers - {trigger_text}. "
        "Also use when searching for Avengers, Tony Stark, Iron Man, MCU, A-skill, or A-prefixed operating modes."
    )
    use_when = [
        f"The user needs to {verb_phrase}.",
        f"The request matches these triggers: {trigger_text}.",
        "The user asks for an Avengers, Tony Stark, Iron Man, MCU, or A-prefixed lens.",
    ]
    do_not = DO_NOT_USE.get(entry["category"], [
        "The user asks for a simple factual answer that does not need an Avengers operating lens.",
        "A more specific A-prefixed skill is clearly a better fit; route there instead.",
    ])
    md = [
        "---",
        f"name: {entry['name']}",
        f"description: {clean_yaml_text(desc)}",
        "---",
        "",
        f"# {entry['display_name']}",
        "",
        "## Role",
        "",
        f"Tier {entry['tier']} {entry['category']} skill. {entry['core_idea']}",
        "",
        "## Use When",
        "",
        *[f"- {item}" for item in use_when],
        "",
        "## Do Not Use When",
        "",
        *[f"- {item}" for item in do_not],
        "",
        "## Workflow",
        "",
        *[f"{i}. {step}" for i, step in enumerate(entry["workflow"], start=1)],
        "",
        "## Output Contract",
        "",
        "Return these fields unless the user asks for another format:",
        "",
        *[f"- `{field}`" for field in entry["output_contract"]],
        "",
        "## Skill Chaining",
        "",
    ]
    if entry["pairs_with"]:
        md.extend([f"- Pair with `{pair}` when useful." for pair in entry["pairs_with"]])
    else:
        md.append("- Use `a-stark-router` if another Avengers skill may fit better.")
    md.extend([
        "",
        "## Source Hooks",
        "",
        "Use these sources for grounding when source evidence is needed. Keep answers synthesized; do not reproduce long transcript passages.",
        "",
        *source_summary_for(entry["source_files"]),
        "",
        "## Self-Test",
        "",
        entry["self_test"],
        "",
    ])
    (path / "SKILL.md").write_text("\n".join(md), encoding="utf-8")

    short_description = clean_yaml_text(entry["summary"])
    if len(short_description) > 64:
        short_description = short_description[:61].rstrip() + "..."
    openai_yaml = [
        "interface:",
        f"  display_name: \"{entry['display_name']}\"",
        f"  short_description: \"{short_description}\"",
        f"  default_prompt: \"Use ${entry['name']} to {clean_yaml_text(entry['summary']).lower()}\"",
        "",
    ]
    (agents / "openai.yaml").write_text("\n".join(openai_yaml), encoding="utf-8")


def write_references(manifest: list[dict]) -> None:
    REFERENCES_DIR.mkdir(parents=True, exist_ok=True)
    (REFERENCES_DIR / "skill-manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    by_category: dict[str, list[dict]] = {}
    by_tier: dict[int, list[dict]] = {}
    for entry in manifest:
        by_category.setdefault(entry["category"], []).append(entry)
        by_tier.setdefault(entry["tier"], []).append(entry)

    lines = [
        "# Avengers Skill Manifest",
        "",
        f"Total skills: {len(manifest)}",
        "",
        "## Tiers",
        "",
    ]
    for tier in sorted(by_tier):
        lines.append(f"- Tier {tier}: {len(by_tier[tier])} skills")
    lines.extend(["", "## Categories", ""])
    for category, entries in by_category.items():
        lines.append(f"### {category} ({len(entries)})")
        lines.extend([f"- `{entry['name']}` - {entry['summary']}" for entry in entries])
        lines.append("")
    (REFERENCES_DIR / "skill-manifest.md").write_text("\n".join(lines), encoding="utf-8")

    corpus_lines = [
        "# Corpus Index",
        "",
        "This private local index points to the transcript files used to derive the Avengers skills.",
        "Keep full transcript text in the original local files; keep this index concise.",
        "",
    ]
    seen = set()
    for source in SOURCE_FILES:
        if source in seen:
            continue
        seen.add(source)
        p = resolve_source_path(source)
        if p.exists():
            text = p.read_text(errors="replace")
            line_count = len(text.splitlines())
            word_count = len(re.findall(r"[A-Za-z][A-Za-z'-]+", text))
            corpus_lines.append(f"- `{p.name}` - {line_count} lines, {word_count} words")
        else:
            corpus_lines.append(f"- `{source}` - not found at generation time")
    (REFERENCES_DIR / "corpus-index.md").write_text("\n".join(corpus_lines) + "\n", encoding="utf-8")

    source_map = ["# Source Map", "", "## By Skill", ""]
    for entry in manifest:
        source_map.append(f"### `{entry['name']}`")
        source_map.append(f"- Category: {entry['category']}")
        source_map.append(f"- Tier: {entry['tier']}")
        source_map.append("- Sources:")
        source_map.extend([f"  - `{resolve_source_path(source).name}`" for source in entry["source_files"][:8]])
        source_map.append("")
    (REFERENCES_DIR / "source-map.md").write_text("\n".join(source_map), encoding="utf-8")

    principles = [
        "# Tony Stark Principles",
        "",
        "- Build the crude Mark 1 before waiting for perfect conditions.",
        "- Treat every mistake as design data for the next suit.",
        "- Use available resources by function, not by label.",
        "- Confidence is earned through competence, visible action, and kept promises.",
        "- Move fast, but install feedback before scaling the blast radius.",
        "- Beware the armor-around-the-world pattern: fear can turn protection into control.",
        "- Share burdens early; the curse of knowledge worsens when carried alone.",
        "- Mentor by building responsibility, not dependency on the suit.",
        "- Balance Tony's inventive drive with Steve's values under pressure.",
        "- Make knowledge operational: each source should become a behavior, checklist, or decision lens.",
        "",
    ]
    (REFERENCES_DIR / "tony-stark-principles.md").write_text("\n".join(principles), encoding="utf-8")

    mcu_map = [
        "# MCU Story Map",
        "",
        "- Iron Man: cave, Mark 1, identity, weapons accountability, resourcefulness.",
        "- Iron Man 2: public pressure, legacy, poisoning, suit weaknesses, Expo ecosystem.",
        "- Avengers: team assembly, ego under pressure, first contact with cosmic-scale threat.",
        "- Iron Man 3: anxiety, tinkering, remote armor, trauma, rebuilding identity beyond suits.",
        "- Age of Ultron: fear, armor around the world, unintended consequences, Vision as alternative.",
        "- Civil War: accountability, governance, divided values, friendship versus oversight.",
        "- Homecoming/Far From Home/No Way Home: mentorship, legacy, responsibility, tool dependence.",
        "- Infinity War/Endgame: foresight, sacrifice, shared burden, final upgrade, legacy handoff.",
        "- Road to Doomsday: new mask same task, Tony/Doom parallels, control and protection patterns.",
        "",
    ]
    (REFERENCES_DIR / "mcu-story-map.md").write_text("\n".join(mcu_map), encoding="utf-8")


def update_plugin_json() -> None:
    path = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["description"] = "An unofficial Avengers/Tony Stark operating-system skill pack with 107 A-prefixed skills."
    data["author"] = {"name": "thepraggyverse"}
    data["interface"].update({
        "displayName": "Avengers",
        "shortDescription": "107 A-prefixed Avengers and Tony Stark operating skills.",
        "longDescription": "Avengers turns Tony Stark, Iron Man, MCU story analysis, leadership, risk, prototyping, resourcefulness, mentorship, and corpus knowledge into local Codex skills.",
        "developerName": "thepraggyverse",
        "capabilities": ["skills", "knowledge", "workflow"],
        "defaultPrompt": "Use a-stark-router to choose and apply the right Avengers skill.",
    })
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    manifest = build_manifest()
    if len(manifest) != 107:
        raise SystemExit(f"Expected 107 skills, got {len(manifest)}")

    SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    for entry in manifest:
        write_skill(entry)
    write_references(manifest)
    update_plugin_json()
    print(f"Generated {len(manifest)} Avengers skills in {SKILLS_DIR}")


if __name__ == "__main__":
    main()

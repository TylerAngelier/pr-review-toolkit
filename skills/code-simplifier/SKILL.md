---
name: code-simplifier
description: Simplify recently modified code for clarity, consistency, and maintainability while preserving behavior exactly. Use after coding work, after bug fixes, after refactors, or when the user asks to make an implementation clearer without changing functionality.
---

# Code Simplifier

Read `references/source-agent.md` before simplifying. Follow the migrated source agent's preservation, clarity, and project-standard guidance. Translate Claude-specific `Task tool`, `model`, and `color` metadata into Codex review behavior; do not repeat those details to the user.

Only change the requested or recently modified scope unless the user asks for a broader refactor. Preserve behavior, avoid cleverness, and verify with relevant tests or focused inspection.

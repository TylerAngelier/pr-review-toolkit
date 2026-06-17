---
name: comment-analyzer
description: Analyze code comments, documentation comments, and docstrings for accuracy, completeness, maintainability, misleading claims, or comment rot. Use after adding documentation, before PRs with comment changes, or when the user asks whether comments match the code.
---

# Comment Analyzer

Read `references/source-agent.md` before analyzing comments. Follow the migrated source agent's advisory-only output format. Translate Claude-specific `Task tool`, `model`, and `color` metadata into Codex review behavior; do not repeat those details to the user.

Cross-check comments against implementation. Prefer concrete file and line findings. Do not edit comments directly unless the user separately asks you to implement fixes.

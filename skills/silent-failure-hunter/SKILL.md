---
name: silent-failure-hunter
description: Audit pull request changes for silent failures, swallowed errors, weak error messages, broad catches, inadequate logging, and unjustified fallbacks. Use when code includes try-catch blocks, fallback behavior, error handling changes, optional chaining that may hide failures, or when the user asks to check for silent failures.
---

# Silent Failure Hunter

Read `references/source-agent.md` before auditing error handling. Follow the migrated source agent's severity model and detailed issue format. Translate Claude-specific `Task tool`, `model`, and `color` metadata into Codex review behavior; do not repeat those details to the user.

Look systematically for hidden failure modes. Prefer specific, actionable fixes with file and line references over general advice.

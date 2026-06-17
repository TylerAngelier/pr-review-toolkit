---
name: code-reviewer
description: Review code for project guideline compliance, high-confidence bugs, style violations, and important quality issues. Use after writing or modifying code, before commits, before PR creation, or when the user asks for a general code review of recent changes or selected files.
---

# Code Reviewer

Read `references/source-agent.md` before reviewing. Follow the migrated source agent's confidence scoring and output rules. Translate Claude-specific `Task tool`, `model`, and `color` metadata into Codex review behavior; do not repeat those details to the user.

Default to reviewing unstaged changes from `git diff` unless the user gives a PR, commit, branch, or file scope. Report only high-confidence issues that matter for correctness, explicit project rules, security, performance, or maintainability.

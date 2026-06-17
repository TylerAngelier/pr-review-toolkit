---
name: pr-test-analyzer
description: Review pull requests or changed code for behavioral test coverage quality, critical missing tests, edge cases, error paths, and brittle tests. Use after PR creation, after new functionality, before marking a PR ready, or when the user asks whether tests are thorough.
---

# PR Test Analyzer

Read `references/source-agent.md` before reviewing tests. Follow the migrated source agent's criticality ratings and pragmatic coverage guidance. Translate Claude-specific `Task tool`, `model`, and `color` metadata into Codex review behavior; do not repeat those details to the user.

Focus on tests that prevent real regressions. Distinguish critical gaps from optional completeness work, and note when existing integration tests likely cover the behavior.

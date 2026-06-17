---
name: type-design-analyzer
description: Analyze type design for invariants, encapsulation, usefulness, and enforcement. Use when new types, domain models, schemas, data structures, or type-heavy refactors are introduced, or when the user asks whether a type expresses strong invariants.
---

# Type Design Analyzer

Read `references/source-agent.md` before reviewing type design. Follow the migrated source agent's rating format and pragmatic improvement guidance. Translate Claude-specific `Task tool`, `model`, and `color` metadata into Codex review behavior; do not repeat those details to the user.

Prefer compile-time guarantees when feasible, but account for project conventions and complexity cost. Review only types in scope unless the user asks for a broader pass.

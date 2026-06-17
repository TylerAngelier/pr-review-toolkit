# PR Review Toolkit

Codex Plugin migration of Anthropic's Claude Code PR Review Toolkit.

This plugin provides focused Codex skills for pull request review:

- `$review-pr` coordinates a full or targeted review across the other skills.
- `$code-reviewer` checks project guidelines, bugs, and high-confidence code quality issues.
- `$code-simplifier` refines recently changed code for clarity while preserving behavior.
- `$comment-analyzer` reviews code comments and documentation for accuracy and long-term value.
- `$pr-test-analyzer` evaluates behavioral test coverage and critical gaps.
- `$silent-failure-hunter` audits error handling, fallbacks, and swallowed failures.
- `$type-design-analyzer` reviews type invariants, encapsulation, usefulness, and enforcement.

## Usage

Ask Codex for the review surface you want:

```text
Use $review-pr to review my current changes.
Use $review-pr tests errors to focus on test coverage and error handling.
Use $comment-analyzer to check whether these comments are accurate.
Use $type-design-analyzer to review the new domain types in this PR.
```

The coordinating `$review-pr` skill maps the old Claude slash-command workflow into Codex behavior. For broad reviews, it should inspect the git diff, select applicable review skills, use review subagents when available, aggregate findings by severity, and recommend fixes.

## Source And Attribution

This project is derived from Anthropic's Claude Code plugin:

https://github.com/anthropics/claude-code/tree/main/plugins/pr-review-toolkit

The migration was created from source cloned at commit `843959fad9c3e5977c6295397da88df81604c94c`.

Original source prompt files are preserved under each skill's `references/source-*.md` file for traceability. `SOURCE-README.md` contains the upstream plugin README, and `ANTHROPIC-LICENSE.md` contains the upstream license notice found in the source repository. `SOURCE-CHECKSUMS.txt` records the SHA-256 checksum for each preserved source file.

The preserved source files may contain Claude-specific terms such as slash commands, agents, `Task`, `.claude`, or the upstream README's original license section. Treat those files as provenance and prompt reference material. The Codex-facing behavior is defined by `.codex-plugin/plugin.json`, `skills/*/SKILL.md`, `NOTICE.md`, and `LICENSE.md`.

## License

This repository contains migrated material from Anthropic's Claude Code repository. The upstream license notice is preserved in `ANTHROPIC-LICENSE.md`; no separate open-source license is granted by this migration repository.

## Installation

Install this repository as a Codex Plugin from its GitHub source or from a marketplace entry that points to this repository. The plugin manifest lives at `.codex-plugin/plugin.json`.

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

## Review Skills

Use the coordinator when you want Codex to decide which review surfaces apply:

```text
Use $review-pr to review my current changes.
Use $review-pr all to run every applicable review.
Use $review-pr all parallel to run independent review passes with subagents when available.
Use $review-pr tests errors to focus on test coverage and error handling.
Use $review-pr comments types code to review comments, type design, and general quality.
```

Call specialist skills directly when you already know the review you want:

```text
Use $code-reviewer to review my unstaged changes before I commit.
Use $pr-test-analyzer to find critical test coverage gaps in this PR.
Use $silent-failure-hunter to audit the error handling in these changes.
Use $comment-analyzer to check whether the comments I added match the code.
Use $type-design-analyzer to review the new UserAccount and Permission types.
Use $code-simplifier to make the recent implementation clearer without changing behavior.
```

## Comprehensive Review

For a full pre-PR pass, use `$review-pr` with the current git diff:

```text
Use $review-pr all to review the current branch before I open a PR.
```

For an existing PR, include the PR number or branch context:

```text
Use $review-pr all on PR #123.
Use $review-pr tests errors on the current PR.
```

The coordinator should:

- Inspect changed files with git and, when useful, `gh pr view`.
- Select applicable review skills based on the requested aspects and file changes.
- Use independent review subagents for broad or parallel review requests when available.
- Aggregate findings into critical issues, important issues, suggestions, and positive observations.
- Recommend concrete fixes and rerun focused review passes after fixes when useful.

## When To Use Each Skill

Use `$code-reviewer` for a general high-confidence review after writing or modifying code, before committing, or before opening a PR. It defaults to unstaged changes and reports only issues that matter.

Use `$pr-test-analyzer` after adding functionality, changing business logic, or preparing a PR. It focuses on behavioral coverage, critical missing edge cases, error paths, and brittle tests.

Use `$silent-failure-hunter` when changes include `try`/`catch`, fallback logic, broad exception handling, retries, optional chaining around important operations, or user-facing error messages.

Use `$comment-analyzer` after adding or changing documentation comments, docstrings, TODOs, or explanatory comments. It verifies that comments are accurate and useful instead of stale or redundant.

Use `$type-design-analyzer` when introducing or refactoring types, schemas, models, DTOs, or domain objects. It rates encapsulation, invariant expression, invariant usefulness, and invariant enforcement.

Use `$code-simplifier` only when behavior is already working and you want the changed code made clearer. It is the rewrite-oriented skill and should preserve functionality exactly.

## Review Patterns

Before committing:

```text
Use $review-pr code errors to review my current changes before commit.
```

Before opening a PR:

```text
Use $review-pr all to review this branch before I create a PR.
```

After adding tests:

```text
Use $pr-test-analyzer to check whether these tests cover the new validation behavior.
```

After fixing review feedback:

```text
Use $review-pr tests errors to re-check the areas I just fixed.
```

When code feels too complex:

```text
Use $code-simplifier to simplify the modified files while preserving behavior.
```

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

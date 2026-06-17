---
name: review-pr
description: Coordinate comprehensive or targeted pull request review in Codex using the PR Review Toolkit skills. Use when the user asks to review a PR, review current git changes, run all PR review aspects, or specifically review comments, tests, error handling, type design, code quality, or simplification.
---

# PR Review

Read `references/source-review-pr.md` before running the coordinated workflow. Treat it as the migrated source command from Anthropic's Claude Code plugin, adapted to Codex skills and subagents. Ignore Claude-specific frontmatter such as `argument-hint`, `allowed-tools`, slash-command syntax, and `Task` wording except as source intent.

## Workflow

1. Determine scope from the user's request, `git status`, `git diff --name-only`, and, when useful, `gh pr view`.
2. Map requested aspects to skills:
   - `comments`: `$comment-analyzer`
   - `tests`: `$pr-test-analyzer`
   - `errors`: `$silent-failure-hunter`
   - `types`: `$type-design-analyzer`
   - `code`: `$code-reviewer`
   - `simplify`: `$code-simplifier`
   - `all`: all applicable skills
3. Prefer review subagents for independent review aspects when subagents are available and the user asked for parallel or comprehensive review.
4. Aggregate findings by severity: critical, important, suggestions, and positive observations.
5. Recommend concrete fixes and rerun the relevant focused review after fixes when needed.

Keep the final report concise and lead with actionable findings.

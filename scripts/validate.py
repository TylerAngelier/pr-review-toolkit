#!/usr/bin/env python3
"""Validate the PR Review Toolkit Codex plugin package."""

from __future__ import annotations

import json
import re
import sys
from hashlib import sha256
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "review-pr": "source-review-pr.md",
    "code-reviewer": "source-agent.md",
    "code-simplifier": "source-agent.md",
    "comment-analyzer": "source-agent.md",
    "pr-test-analyzer": "source-agent.md",
    "silent-failure-hunter": "source-agent.md",
    "type-design-analyzer": "source-agent.md",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path.relative_to(ROOT)} is invalid JSON: {exc}")


def validate_manifest() -> None:
    manifest_path = ROOT / ".codex-plugin" / "plugin.json"
    if not manifest_path.is_file():
        fail("missing .codex-plugin/plugin.json")

    manifest = read_json(manifest_path)
    required = ["name", "version", "description", "author", "skills", "interface"]
    for key in required:
        if key not in manifest:
            fail(f"plugin manifest missing {key!r}")

    if manifest["name"] != "pr-review-toolkit":
        fail("plugin manifest name must be pr-review-toolkit")
    if manifest["skills"] != "./skills/":
        fail("plugin manifest skills path must be ./skills/")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", manifest["version"]):
        fail("plugin manifest version must be semver-like")
    if manifest.get("license") != "LicenseRef-Anthropic-Commercial-Terms":
        fail("plugin manifest license must be LicenseRef-Anthropic-Commercial-Terms")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)} missing YAML frontmatter")
    try:
        _, raw_frontmatter, body = text.split("---\n", 2)
    except ValueError:
        fail(f"{path.relative_to(ROOT)} has malformed frontmatter")
    if not body.strip():
        fail(f"{path.relative_to(ROOT)} has empty body")

    values: dict[str, str] = {}
    for line in raw_frontmatter.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"{path.relative_to(ROOT)} has unsupported frontmatter line: {line}")
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def validate_skills() -> None:
    skills_root = ROOT / "skills"
    for skill_name, reference_name in sorted(EXPECTED_SKILLS.items()):
        skill_dir = skills_root / skill_name
        skill_path = skill_dir / "SKILL.md"
        reference_path = skill_dir / "references" / reference_name

        if not skill_path.is_file():
            fail(f"missing {skill_path.relative_to(ROOT)}")
        if not reference_path.is_file():
            fail(f"missing {reference_path.relative_to(ROOT)}")

        frontmatter = parse_frontmatter(skill_path)
        if frontmatter.get("name") != skill_name:
            fail(f"{skill_path.relative_to(ROOT)} frontmatter name must be {skill_name}")
        if not frontmatter.get("description"):
            fail(f"{skill_path.relative_to(ROOT)} missing description")


def validate_attribution() -> None:
    for relative_path in [
        "README.md",
        "NOTICE.md",
        "LICENSE.md",
        "ANTHROPIC-LICENSE.md",
        "SOURCE-README.md",
        "SOURCE-CHECKSUMS.txt",
    ]:
        if not (ROOT / relative_path).is_file():
            fail(f"missing {relative_path}")

    notice = (ROOT / "NOTICE.md").read_text(encoding="utf-8")
    if "https://github.com/anthropics/claude-code/tree/main/plugins/pr-review-toolkit" not in notice:
        fail("NOTICE.md must link the Anthropic source plugin")

    license_text = (ROOT / "LICENSE.md").read_text(encoding="utf-8")
    if "No separate open-source license is granted" not in license_text:
        fail("LICENSE.md must clarify that no separate open-source license is granted")


def validate_source_checksums() -> None:
    checksum_path = ROOT / "SOURCE-CHECKSUMS.txt"
    for line_number, line in enumerate(checksum_path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            expected_hash, relative_path = line.split(maxsplit=1)
        except ValueError:
            fail(f"SOURCE-CHECKSUMS.txt:{line_number} must contain a hash and path")
        source_path = ROOT / relative_path
        if not source_path.is_file():
            fail(f"SOURCE-CHECKSUMS.txt references missing file {relative_path}")
        actual_hash = sha256(source_path.read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            fail(f"{relative_path} checksum mismatch")


def main() -> None:
    validate_manifest()
    validate_skills()
    validate_attribution()
    validate_source_checksums()
    print("Validation passed.")


if __name__ == "__main__":
    main()

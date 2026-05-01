#!/usr/bin/env python3
"""Validate Taku skill pack consistency without external dependencies."""

from __future__ import annotations

import argparse
import re
import stat
import sys
from pathlib import Path

ALLOWED_FRONTMATTER_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}
DESCRIPTION_MAX = 1024
PROTOCOL_START = "<!-- TAKU_LEARNINGS_PROTOCOL:START -->"
PROTOCOL_END = "<!-- TAKU_LEARNINGS_PROTOCOL:END -->"


def default_repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    if not match:
        raise ValueError("missing YAML frontmatter")
    frontmatter = match.group(1)
    body = text[match.end() :]
    values: dict[str, str] = {}
    current_key: str | None = None
    for line in frontmatter.splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t")) and current_key:
            values[current_key] += "\n" + line.strip()
            continue
        key, _, value = line.partition(":")
        if not key or not _:
            continue
        current_key = key.strip()
        values[current_key] = value.strip().lstrip(">").strip()
    return values, body


def skill_files(root: Path) -> list[Path]:
    return [root / "SKILL.md"] + sorted((root / "skills").glob("*/SKILL.md"))


def check_frontmatter(root: Path, errors: list[str]) -> None:
    for path in skill_files(root):
        try:
            frontmatter, _ = parse_frontmatter(path)
        except ValueError as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
            continue
        unexpected = sorted(set(frontmatter) - ALLOWED_FRONTMATTER_KEYS)
        if unexpected:
            errors.append(f"{path.relative_to(root)}: unexpected frontmatter key(s): {', '.join(unexpected)}")
        name = frontmatter.get("name", "")
        if not re.match(r"^[a-z0-9-]+$", name):
            errors.append(f"{path.relative_to(root)}: invalid skill name: {name!r}")
        description = " ".join(frontmatter.get("description", "").split())
        if not description:
            errors.append(f"{path.relative_to(root)}: missing description")
        if len(description) > DESCRIPTION_MAX:
            errors.append(f"{path.relative_to(root)}: description exceeds {DESCRIPTION_MAX} chars")


def check_review_contract(root: Path, errors: list[str]) -> None:
    path = root / "skills" / "review" / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    forbidden = [
        "Commit auto-fixes " + "atomically",
        "Commit separately",
        "git commit",
        "git add " + "<fixed-files>",
    ]
    for phrase in forbidden:
        if phrase in text:
            errors.append(f"{path.relative_to(root)}: review skill still contains commit instruction: {phrase}")


def check_template_references(root: Path, errors: list[str]) -> None:
    expected = {
        "skills/think/SKILL.md": "templates/design-doc.md",
        "skills/plan/SKILL.md": "templates/plan.md",
        "skills/reflect/SKILL.md": "templates/retro-report.md",
    }
    for skill, template in expected.items():
        text = (root / skill).read_text(encoding="utf-8")
        if template not in text:
            errors.append(f"{skill}: missing template reference to {template}")


def extract_protocol_blocks(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(PROTOCOL_START) + r".*?" + re.escape(PROTOCOL_END), re.S)
    return pattern.findall(text)


def check_bootstrap_blocks(root: Path, errors: list[str]) -> None:
    blocks = []
    for name in ("AGENTS.md", "CLAUDE.md"):
        path = root / name
        if not path.exists():
            continue
        found = extract_protocol_blocks(path)
        if len(found) > 1:
            errors.append(f"{name}: contains duplicate Taku learnings protocol blocks")
        blocks.extend(found)
    if blocks and any(block != blocks[0] for block in blocks):
        errors.append("AGENTS.md/CLAUDE.md: Taku learnings protocol blocks differ")


def check_reflect_script(root: Path, errors: list[str], strict: bool) -> None:
    path = root / "skills" / "reflect" / "scripts" / "learnings.py"
    if not path.exists():
        errors.append(f"{path.relative_to(root)}: missing")
        return
    mode = path.stat().st_mode
    if strict and not (mode & stat.S_IXUSR):
        errors.append(f"{path.relative_to(root)}: not executable")
    text = path.read_text(encoding="utf-8")
    for command in ("add", "search", "prune", "export", "bootstrap-check", "bootstrap-install"):
        if f'"{command}"' not in text:
            errors.append(f"{path.relative_to(root)}: missing command {command}")


def check_agents_metadata(root: Path, errors: list[str]) -> None:
    paths = [
        root / "agents" / "openai.yaml",
        root / "skills" / "think" / "agents" / "openai.yaml",
        root / "skills" / "plan" / "agents" / "openai.yaml",
        root / "skills" / "build" / "agents" / "openai.yaml",
        root / "skills" / "review" / "agents" / "openai.yaml",
        root / "skills" / "debug" / "agents" / "openai.yaml",
        root / "skills" / "reflect" / "agents" / "openai.yaml",
    ]
    for path in paths:
        if not path.exists():
            errors.append(f"{path.relative_to(root)}: missing UI metadata")


def check_trigger_text(root: Path, errors: list[str]) -> None:
    think = (root / "skills" / "think" / "SKILL.md").read_text(encoding="utf-8")
    broad_trigger = "Invoke before ANY " + "build request"
    broad_list = "new feature, component, API, refactor, " + "bug fix"
    if broad_trigger in think or broad_list in think:
        errors.append("skills/think/SKILL.md: trigger description is still too broad")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=None, help=argparse.SUPPRESS)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve() if args.root else default_repo_root()
    errors: list[str] = []
    check_frontmatter(root, errors)
    check_review_contract(root, errors)
    check_template_references(root, errors)
    check_bootstrap_blocks(root, errors)
    check_reflect_script(root, errors, args.strict)
    check_agents_metadata(root, errors)
    check_trigger_text(root, errors)

    if errors:
        print("Taku validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Taku validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

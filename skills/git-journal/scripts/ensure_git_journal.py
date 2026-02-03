#!/usr/bin/env python3
"""
ensure_git_journal.py

Ensures a Git Journal exists for the current branch.
Creates the journal folder and file from template if missing.

Cross-platform: Works on Windows, macOS, and Linux.
Requires: Python 3.7+, Git
"""

import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def run_git_command(args: list[str], cwd: Path | None = None) -> tuple[bool, str]:
    """Run a git command and return (success, output)."""
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
        )
        return result.returncode == 0, result.stdout.strip()
    except FileNotFoundError:
        return False, "Git not found"


def get_repo_root() -> Path | None:
    """Get the git repository root directory."""
    success, output = run_git_command(["rev-parse", "--show-toplevel"])
    if success:
        return Path(output)
    return None


def get_current_branch() -> str | None:
    """Get the current branch name, or None if detached HEAD."""
    success, output = run_git_command(["symbolic-ref", "--short", "HEAD"])
    if success:
        return output
    # Try to get a descriptive name for detached HEAD
    success, output = run_git_command(["describe", "--tags", "--always"])
    if success:
        return f"detached-{output}"
    return None


def normalize_branch_name(branch: str) -> str:
    """
    Normalize branch name to be filesystem-safe.

    - Replace / with -
    - Replace whitespace with -
    - Collapse repeated -
    - Remove unsafe characters
    - Keep readable
    """
    # Replace slashes and whitespace with hyphens
    normalized = re.sub(r"[/\s]+", "-", branch)
    # Remove unsafe filesystem characters
    normalized = re.sub(r"[<>:\"|?*\\]", "", normalized)
    # Collapse repeated hyphens
    normalized = re.sub(r"-+", "-", normalized)
    # Remove leading/trailing hyphens
    normalized = normalized.strip("-")
    return normalized


def find_existing_journal_folder(
    branches_dir: Path, normalized_branch: str
) -> Path | None:
    """
    Find an existing journal folder for the given branch.

    Journal folders are named: YYYY-MM-DD_<normalized-branch-name>
    The date prefix may vary, so we match on the branch name suffix.
    """
    if not branches_dir.exists():
        return None

    pattern = re.compile(r"^\d{4}-\d{2}-\d{2}_" + re.escape(normalized_branch) + "$")

    for item in branches_dir.iterdir():
        if item.is_dir() and pattern.match(item.name):
            return item

    return None


def get_git_user_name() -> str:
    """Get git user name from config."""
    _, name = run_git_command(["config", "user.name"])
    return name or "Unknown"


def get_head_sha() -> str:
    """Get the current HEAD SHA (short form)."""
    success, output = run_git_command(["rev-parse", "--short", "HEAD"])
    return output if success else "unknown"


def load_template(skill_dir: Path) -> str:
    """Load the journal template file."""
    template_path = skill_dir / "assets" / "git-journal-template.md"
    if template_path.exists():
        return template_path.read_text(encoding="utf-8")

    # Fallback minimal template
    return """# Git Journal — Branch Log

## Why, current summary

**Intent**
- [What problem is being solved?]

**Constraints**
- [What limitations shaped the solution?]

**Tradeoffs**
- [What was sacrificed for what gain?]

**Alternatives considered**
- [What else was tried? Why rejected?]

**Non-obvious nuance**
- [Things that look wrong but are correct because...]

## What, aggregated

- [High-level description of changes]

## Where, key areas

- [Key directories/modules affected]

## Who

- Git user: {{GIT_USER_NAME}}

## When

- Created: {{CREATED_DATE}}
- Last updated: {{LAST_UPDATED}}
- Branch: {{BRANCH_NAME}}
- HEAD: {{HEAD_SHA}}

---

## Detailed log

### {{CREATED_DATE}}

**What changed**
- [Describe what was done]

**Why**
- [The reasoning behind these changes]

**Where**
- [Key files touched]

**Notes**
- [Additional context]
"""


def populate_template(template: str, branch: str) -> str:
    """Replace template placeholders with actual values."""
    name = get_git_user_name()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    head_sha = get_head_sha()

    replacements = {
        "{{GIT_USER_NAME}}": name,
        "{{CREATED_DATE}}": now,
        "{{LAST_UPDATED}}": now,
        "{{BRANCH_NAME}}": branch,
        "{{HEAD_SHA}}": head_sha,
    }

    result = template
    for placeholder, value in replacements.items():
        result = result.replace(placeholder, value)

    return result


def ensure_git_journal() -> int:
    """
    Main function to ensure a Git Journal exists for the current branch.

    Returns:
        0 on success, 1 on error
    """
    # Check we're in a git repo
    repo_root = get_repo_root()
    if not repo_root:
        print("Error: Not in a git repository", file=sys.stderr)
        return 1

    # Get current branch
    branch = get_current_branch()
    if not branch:
        print("Error: Could not determine current branch", file=sys.stderr)
        return 1

    normalized_branch = normalize_branch_name(branch)
    print(f"Branch: {branch} (normalized: {normalized_branch})")

    # Set up paths
    branches_dir = repo_root / "branches"

    # Check for existing journal folder
    existing_folder = find_existing_journal_folder(branches_dir, normalized_branch)

    if existing_folder:
        journal_path = existing_folder / "git-journal.md"
        if journal_path.exists():
            print(f"Journal already exists: {journal_path.relative_to(repo_root)}")
            return 0
        else:
            # Folder exists but no journal file - create it
            journal_folder = existing_folder
    else:
        # Create new folder with today's date
        today = datetime.now().strftime("%Y-%m-%d")
        folder_name = f"{today}_{normalized_branch}"
        journal_folder = branches_dir / folder_name

    # Ensure directories exist
    journal_folder.mkdir(parents=True, exist_ok=True)

    # Find the skill directory (for loading template)
    script_dir = Path(__file__).parent
    skill_dir = script_dir.parent

    # Load and populate template
    template = load_template(skill_dir)
    content = populate_template(template, branch)

    # Write the journal file
    journal_path = journal_folder / "git-journal.md"
    journal_path.write_text(content, encoding="utf-8")

    print(f"Created journal: {journal_path.relative_to(repo_root)}")
    return 0


if __name__ == "__main__":
    sys.exit(ensure_git_journal())

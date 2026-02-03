#!/usr/bin/env python3
"""
update_git_journal.py

Updates the Git Journal for the current branch with current git state.
- Updates Who section
- Updates When section (Last updated, HEAD)
- Injects compact What snapshot from git status/diff
- Preserves existing Why and Detailed log sections

Cross-platform: Works on Windows, macOS, and Linux.
Requires: Python 3.7+, Git
"""

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
    """Get the current branch name."""
    success, output = run_git_command(["symbolic-ref", "--short", "HEAD"])
    if success:
        return output
    success, output = run_git_command(["describe", "--tags", "--always"])
    if success:
        return f"detached-{output}"
    return None


def normalize_branch_name(branch: str) -> str:
    """Normalize branch name to be filesystem-safe."""
    normalized = re.sub(r"[/\s]+", "-", branch)
    normalized = re.sub(r"[<>:\"|?*\\]", "", normalized)
    normalized = re.sub(r"-+", "-", normalized)
    normalized = normalized.strip("-")
    return normalized


def find_journal_path(repo_root: Path, normalized_branch: str) -> Path | None:
    """Find the journal file for the given branch."""
    branches_dir = repo_root / "branches"
    if not branches_dir.exists():
        return None

    pattern = re.compile(r"^\d{4}-\d{2}-\d{2}_" + re.escape(normalized_branch) + "$")

    for item in branches_dir.iterdir():
        if item.is_dir() and pattern.match(item.name):
            journal_path = item / "git-journal.md"
            if journal_path.exists():
                return journal_path

    return None


def get_git_user_name() -> str:
    """Get git user name from config."""
    _, name = run_git_command(["config", "user.name"])
    return name or "Unknown"


def get_head_sha() -> str:
    """Get the current HEAD SHA (short form)."""
    success, output = run_git_command(["rev-parse", "--short", "HEAD"])
    return output if success else "unknown"


def get_git_status_summary() -> str:
    """Get a compact summary of git status."""
    success, output = run_git_command(["status", "--porcelain"])
    if not success or not output:
        return "No changes"

    lines = output.strip().split("\n")

    # Count by status
    added = modified = deleted = untracked = 0
    for line in lines:
        if line.startswith("A") or line.startswith("??"):
            if line.startswith("??"):
                untracked += 1
            else:
                added += 1
        elif line.startswith("M") or line.startswith(" M"):
            modified += 1
        elif line.startswith("D") or line.startswith(" D"):
            deleted += 1

    parts = []
    if added:
        parts.append(f"{added} added")
    if modified:
        parts.append(f"{modified} modified")
    if deleted:
        parts.append(f"{deleted} deleted")
    if untracked:
        parts.append(f"{untracked} untracked")

    return ", ".join(parts) if parts else "No changes"


def get_diff_stat() -> str:
    """Get git diff --stat summary."""
    # Get staged changes
    _, staged = run_git_command(["diff", "--cached", "--stat", "--stat-width=60"])
    # Get unstaged changes
    _, unstaged = run_git_command(["diff", "--stat", "--stat-width=60"])

    parts = []
    if staged:
        parts.append("Staged:\n" + staged)
    if unstaged:
        parts.append("Unstaged:\n" + unstaged)

    return "\n\n".join(parts) if parts else "No diff"


def update_who_section(content: str, name: str) -> str:
    """Update the Who section with current git user."""
    pattern = r"(## Who\s*\n+- Git user: ).*"
    replacement = rf"\1{name}"
    return re.sub(pattern, replacement, content)


def update_when_section(content: str, branch: str, head_sha: str) -> str:
    """Update the When section with current timestamps."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Update Last updated
    content = re.sub(r"(- Last updated: ).*", rf"\g<1>{now}", content)

    # Update HEAD
    content = re.sub(r"(- HEAD: ).*", rf"\g<1>{head_sha}", content)

    # Update Branch (in case it changed due to rename)
    content = re.sub(r"(- Branch: ).*", rf"\g<1>{branch}", content)

    return content


def append_log_entry(content: str) -> str:
    """
    Append a new log entry if the user wants to add one.
    This function adds a placeholder entry that can be filled in.
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    status_summary = get_git_status_summary()

    # Find the "## Detailed log" section
    detailed_log_match = re.search(r"(## Detailed log\s*\n)", content)
    if not detailed_log_match:
        return content

    # Check if there's already an entry for today (avoid duplicates on repeated runs)
    today = datetime.now().strftime("%Y-%m-%d")
    if f"### {today}" in content:
        # Update the status in the most recent entry instead
        return content

    # Create new entry
    new_entry = f"""
### {now}

**What changed**
- {status_summary}

**Why**
- [Fill in the reasoning]

**Where**
- [Key files touched]

**Notes**
- [Additional context]

"""

    # Insert after the "## Detailed log" header
    insert_pos = detailed_log_match.end()

    # Find the first existing entry or end of file
    next_entry_match = re.search(r"\n### \d{4}-\d{2}-\d{2}", content[insert_pos:])

    if next_entry_match:
        # Insert before the next entry
        content = content[:insert_pos] + new_entry + content[insert_pos:]
    else:
        # Append at the end
        content = content[:insert_pos] + new_entry + content[insert_pos:]

    return content


def update_git_journal() -> int:
    """
    Main function to update the Git Journal for the current branch.

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

    # Find the journal file
    journal_path = find_journal_path(repo_root, normalized_branch)
    if not journal_path:
        print(f"Error: No journal found for branch '{branch}'", file=sys.stderr)
        print("Run 'ensure_git_journal.py' first to create one.", file=sys.stderr)
        return 1

    print(f"Updating: {journal_path.relative_to(repo_root)}")

    # Read current content
    content = journal_path.read_text(encoding="utf-8")

    # Get current git info
    name = get_git_user_name()
    head_sha = get_head_sha()

    # Update sections
    content = update_who_section(content, name)
    content = update_when_section(content, branch, head_sha)

    # Optionally append a new log entry
    # (Only if there isn't one for today already)
    content = append_log_entry(content)

    # Write updated content
    journal_path.write_text(content, encoding="utf-8")

    print(f"Updated Who: {name}")
    print(f"Updated HEAD: {head_sha}")
    print(f"Status: {get_git_status_summary()}")
    print("\nRemember to fill in the 'Why' section!")

    return 0


if __name__ == "__main__":
    sys.exit(update_git_journal())

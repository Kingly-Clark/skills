# Cursor Rule Template for Git Journal

Copy this content to `.cursor/rules/git-journal.mdc` in your project.

---

```markdown
---
description: Maintain Git Journal for preserving the "Why" behind code changes
globs:
alwaysApply: true
---

# Git Journal Integration

## Trigger Phrases

| Phrase | Behavior |
|--------|----------|
| **"remember to journal"** | Keep journaling in mind for the entire session. Proactively consider journaling after significant decisions or tradeoffs. |
| **"anything to journal?"** | Reflect on recent commits and conversation. Suggest entries or confirm nothing needs capturing. |
| **"journal this"** | Immediately capture the current context in the journal. |
| **"update the journal"** | Run the update script and prompt for Why content. |

## When to Update Git Journal

Update the Git Journal **before**:
- Committing multi-file changes
- Creating a pull request
- Applying significant code changes

Update the Git Journal **after**:
- Reaching a resolution on a complex problem
- Making architectural decisions
- Discovering non-obvious constraints or tradeoffs

## How to Update

1. First, ensure the journal exists:
   ```bash
   python skills/git-journal/scripts/ensure_git_journal.py
   ```

2. Then update with current state:
   ```bash
   python skills/git-journal/scripts/update_git_journal.py
   ```

3. Most importantly, write the **Why**:
   - Intent: What problem is being solved?
   - Constraints: What limitations shaped the solution?
   - Tradeoffs: What was sacrificed for what gain?
   - Alternatives: What else was considered and why rejected?
   - Nuance: What looks wrong but is actually correct?

## Priority

The "Why" is the most important section. If time is limited, ensure only the Why is captured correctly. Git already tracks what, where, when, and who.

## Location

Journals are stored at:
```
journals/YYYY-MM-DD_<branch-name>.md
```

One journal per branch, reused for the branch's entire lifetime.
```

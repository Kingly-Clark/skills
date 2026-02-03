# Kingly-Clark Skills

A collection of AI agent skills from Kingly-Clark.

[![Skills.sh](https://img.shields.io/badge/Skills.sh-Directory-blue)](https://skills.sh)

## Installation

Install all skills:

```bash
npx skills add Kingly-Clark/skills
```

Install a specific skill:

```bash
npx skills add Kingly-Clark/skills --skill git-journal
```

## Available Skills

### git-journal

A **Why-first journal** for AI-assisted code changes.

Git tracks what/where/when/who — Git Journal captures **why**.

**Use when:**
- Before committing multi-file changes
- Before creating a PR
- When significant reasoning happened that should be preserved

**The problem it solves:**

When working with AI assistants (Cursor, Claude Code, Copilot), the real reasoning happens in chat — tradeoffs, constraints, dead ends, subtle nuance. Once the chat is gone, all that remains is a commit and a diff. Six months later, you see 60 files changed but have no idea why.

Git Journal captures the Why while it still exists.

**Features:**
- Branch-scoped journals (`branches/YYYY-MM-DD_<branch>/git-journal.md`)
- Cross-platform Python scripts (Windows, macOS, Linux)
- Cursor integration via rules
- 5 W's model with Why as priority

[View full documentation →](skills/git-journal/SKILL.md)

---

## Skill Structure

Each skill follows the [Agent Skills](https://agentskills.io/) format:

```
skills/
└── skill-name/
    ├── SKILL.md          # Instructions for the agent
    ├── scripts/          # Helper scripts (optional)
    ├── references/       # Supporting documentation (optional)
    └── assets/           # Templates, images (optional)
```

## Contributing

Contributions are welcome! Please open an issue or PR.

## License

MIT License - see [LICENSE](LICENSE) for details.

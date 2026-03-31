# Forge

**The complete AI-assisted development sprint.**

Forge combines the best of [Superpowers](https://github.com/obra/superpowers) by Jesse Vincent and [gstack](https://github.com/garrytan/gstack) by Garry Tan into a unified skill pack that works on both OpenClaw and Claude Code.

## What It Does

A structured 7-phase sprint pipeline that turns ideas into shipped, tested, reviewed code:

```
Think → Plan → Build → Review → Test → Ship → Reflect
```

Each phase has dedicated skills with iron-clad rules, anti-rationalization guards, and evidence-based gates. The agent can't skip steps, can't fake completions, and can't rationalize shortcuts.

## The Sprint

| Phase | Skill | What Happens |
|-------|-------|-------------|
| **Think** | `/forge-office-hours` | 6 forcing questions reframe your product before you write code |
| **Think** | `/forge-brainstorm` | Socratic design refinement — no code until you approve the design |
| **Think** | `/forge-design` | Build a complete design system from scratch |
| **Plan** | `/forge-ceo-review` | Rethink the problem, find the 10-star product |
| **Plan** | `/forge-eng-review` | Lock in architecture, data flow, edge cases |
| **Plan** | `/forge-design-review` | Rate design dimensions 0-10, fix what's weak |
| **Plan** | `/forge-plan` | Bite-sized tasks with exact file paths, complete code, TDD steps |
| **Build** | `/forge-build` | Subagent-driven development with parallel sprint support |
| **Build** | `/forge-exec` | Sequential plan execution with checkpoints |
| **Build** | `/forge-tdd` | RED-GREEN-REFACTOR enforcement |
| **Review** | `/forge-review` | Pattern-based code review with auto-fix |
| **Review** | `/forge-cross-review` | Second opinion from a different AI model |
| **Review** | `/forge-visual-review` | Before/after visual QA with screenshots |
| **Test** | `/forge-qa` | Test → find bugs → fix → verify with health scoring |
| **Test** | `/forge-cso` | 14-phase security audit with OWASP + STRIDE |
| **Test** | `/forge-debug` | 4-phase root cause investigation |
| **Ship** | `/forge-ship` | Full pipeline: test → review → version → changelog → push → PR |
| **Ship** | `/forge-deploy` | Merge → CI → deploy → verify production health |
| **Reflect** | `/forge-retro` | Weekly retrospective with trend tracking |
| **Reflect** | `/forge-learn` | Persistent learning across sessions |

## Philosophy

- **No code without design.** The agent must understand WHY before HOW.
- **No production code without a failing test.** TDD is not optional.
- **No fixes without root cause.** Three failed fixes → stop and question architecture.
- **No completion claims without evidence.** "It should work" is not a completion statement.
- **No rationalization.** Red flags tables and iron laws catch every shortcut excuse.

## Platforms

| Platform | Status | Notes |
|----------|--------|-------|
| Claude Code | ✅ Primary | Canonical format. Install via plugin marketplace or manual. |
| OpenClaw | ✅ Supported | Adapter layer translates tool calls. Install as skill pack. |

## Installation

### Claude Code

```bash
# Via plugin marketplace (coming soon)
/plugin install forge

# Manual
git clone https://github.com/KKenny0/forge.git ~/.claude/skills/forge
```

### OpenClaw

```bash
# Coming soon via ClawhHub
openclaw skills install forge
```

## Credits

Forge is built on the shoulders of two exceptional projects:

- **[Superpowers](https://github.com/obra/superpowers)** by [Jesse Vincent](https://github.com/obra) — A complete software development workflow for coding agents. The discipline-first approach (TDD enforcement, systematic debugging, evidence-based completion) forms Forge's backbone.

- **[gstack](https://github.com/garrytan/gstack)** by [Garry Tan](https://github.com/garrytan) — A sprint process with 25+ skills covering everything from YC office hours to browser QA to security audits. The product thinking, QA methodology, and parallel sprint architecture are deeply influential.

Both projects are MIT licensed. Forge inherits that license.

Special thanks to Jesse and Garry for open-sourcing how they build software.

## License

MIT

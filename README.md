<p align="center">
  <img src="logo.svg" alt="Taku 琢" width="180" />
</p>

<h1 align="center">Taku 琢</h1>

<p align="center"><strong>Structured AI-assisted development — from idea to verified code.</strong></p>

A discipline-first development sprint framework that adapts to your project's scale. Opinionated workflows, anti-rationalization guards, and evidence-based gates keep AI agents honest — from first idea to production deploy.

> Inspired by [Superpowers](https://github.com/obra/superpowers) and [gstack](https://github.com/garrytan/gstack).

## Why Taku

> 如切如磋，如琢如磨 — 《诗经·卫风·淇奥》

Taku (琢) means to carve jade — to reveal the shape that was always inside the stone. Software development works the same way: you don't forge code by adding material, you carve it by removing what doesn't belong.

| Stage | Chinese | Pipeline Phase | What Happens |
|-------|---------|----------------|-------------|
| 切 | Cut | Think | Cut through ambiguity — force clarity before code |
| 磋 | Grind | Plan | Grind the problem into concrete, executable tasks |
| 琢 | Carve | Build → Review → Test | Carve the solution, then inspect and verify |
| 磨 | Polish | Reflect | Polish and learn from the process |

## The Sprint Pipeline

A structured 6-phase pipeline that turns ideas into tested, verified code:

```
Think → Plan → Build → Review → Test → Reflect
```

Each phase has dedicated skills with iron-clad rules, anti-rationalization guards, and evidence-based gates. The agent can't skip steps, can't fake completions, and can't rationalize shortcuts.

### Phase Skills

| Phase | Skill | What Happens |
|-------|-------|-------------|
| **Think** | `/taku-think` | Adaptive Quick/Design/Explore — right-sized thinking before code |
| **Plan** | `/taku-plan` | Scope review → design review → bite-sized tasks with TDD steps |
| **Build** | `/taku-build` | Parallel or sequential execution, TDD enforced, optional worktree isolation |
| **Review** | `/taku-review` | Pattern-based code review with auto-fix |
| **Test** | `/taku-debug` | 4-phase root cause investigation |
| **Reflect** | `/taku-reflect` | Learn, retro, or codify patterns into reusable skills |


## Philosophy

- **No code without design.** The agent must understand WHY before HOW.
- **No production code without a failing test.** TDD is not optional.
- **No fixes without root cause.** Three failed fixes → stop and question architecture.
- **No completion claims without evidence.** "It should work" is not a completion statement.
- **No rationalization.** Red flag tables and iron laws catch every shortcut excuse.

## Platforms

| Platform | Status | Notes |
|----------|--------|-------|
| Claude Code | Primary | Canonical format. Install via plugin marketplace or manual. |
| OpenClaw | Supported | Adapter layer translates tool calls. Install as skill pack. |

## Installation

### Claude Code

```bash
# Via plugin marketplace (coming soon)
/plugin install taku

# Manual
git clone https://github.com/KKenny0/Taku.git ~/.claude/skills/taku

# Enable slash commands for each phase (one-time setup)
# macOS / Linux:
for phase in think plan build review test reflect; do
  ln -s ~/.claude/skills/taku/skills/$phase ~/.claude/skills/taku-$phase
done

# Windows (PowerShell, run as admin):
foreach ($phase in @("think","plan","build","review","test","reflect")) {
  New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\taku-$phase" -Target "$env:USERPROFILE\.claude\skills\taku\skills\$phase"
}
```

### OpenClaw

```bash
# Coming soon via ClawhHub
openclaw skills install taku
```

## Credits

Taku is built on the shoulders of two exceptional projects:

- **[Superpowers](https://github.com/obra/superpowers)** by [Jesse Vincent](https://github.com/obra) — A complete software development workflow for coding agents. The discipline-first approach (TDD enforcement, systematic debugging, evidence-based completion) forms Taku's backbone.

- **[gstack](https://github.com/garrytan/gstack)** by [Garry Tan](https://github.com/garrytan) — A sprint process with 25+ skills covering everything from YC office hours to browser QA to security audits. The product thinking, QA methodology, and parallel sprint architecture are deeply influential.

Both projects are MIT licensed. Taku inherits that license.

## License

MIT

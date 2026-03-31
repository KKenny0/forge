# Forge — Skill-by-Skill Analysis

> Source repos: [superpowers](https://github.com/obra/superpowers) + [gstack](https://github.com/garrytan/gstack)
> Date: 2026-03-30
> Status: Analysis complete → Next: Design doc → Phase 1 implementation

---

## Sprint Pipeline Overview

```
THINK                    PLAN                    BUILD                   REVIEW                 TEST                   SHIP                   REFLECT
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
office-hours        →    ceo-review         →    implement (SDD/TDD)  →    code-review    →    qa + browser    →    ship + deploy   →    retro
brainstorming       →    eng-review         →    git worktrees       →    codex-review   →    cso audit      →    document-rel    →    learn
design-consultation →    design-review      →    executing-plans      →    design-review  →    qa-only        →    canary          →
                    →    writing-plans      →                        →                   →    benchmark       →
```

---

## Unified Skill Matrix

### Phase 1: THINK (Design & Product Thinking)

| # | Skill | Source | Description | Difficulty | Decision | Rationale |
|---|-------|--------|-------------|-----------|----------|-----------|
| 1 | office-hours | gstack | YC-style 6 forcing questions: demand, status quo, specificity, wedge, observation, future-fit | Easy | **KEEP** | Best product thinking framework in either repo |
| 2 | brainstorming | superpowers | Socratic design refinement, HARD GATE before code, decomposes into specs | Medium | **KEEP** | Design-first gate is valuable, complements office-hours |
| 3 | design-consultation | gstack | Full design system creation: aesthetic, typography, color, layout, competitive research | Medium | **KEEP** | Solid methodology, replace `$D` binary with image_generate |

### Phase 2: PLAN (Architecture & Specification)

| # | Skill | Source | Description | Difficulty | Decision | Rationale |
|---|-------|--------|-------------|-----------|----------|-----------|
| 4 | plan-ceo-review | gstack | Founder-mode review: rethink problem, find 10-star product, 4 scope modes | Easy | **KEEP** | Strong strategic review |
| 5 | plan-eng-review | gstack | Eng manager review: architecture, data flow, edge cases, test plan, diagrams | Easy | **KEEP** | Forces hidden assumptions into the open |
| 6 | plan-design-review | gstack | Designer review: rates 8 dimensions 0-10, explains what a 10 looks like | Easy | **KEEP** | Good design QA on plans |
| 7 | writing-plans | superpowers | Bite-sized tasks with exact file paths, complete code, TDD steps, zero placeholders | Easy | **KEEP** | "Zero-context engineer" principle is excellent |

### Phase 3: BUILD (Implementation)

| # | Skill | Source | Description | Difficulty | Decision | Rationale |
|---|-------|--------|-------------|-----------|----------|-----------|
| 8 | subagent-driven-dev | superpowers | Dispatch fresh subagent per task, 2-stage review (spec + quality), model selection | Hard | **KEEP** | Flagship execution engine, adapt to OpenClaw subagents |
| 9 | executing-plans | superpowers | Sequential plan execution with checkpoints (manual alternative to SDD) | Easy | **KEEP** | Simple fallback execution path |
| 10 | test-driven-dev | superpowers | Strict RED-GREEN-REFACTOR: no production code without failing test | Easy | **KEEP** | Core discipline |
| 11 | using-git-worktrees | superpowers | Isolated workspace creation with auto-detection (npm/cargo/pip/go) | Easy | **KEEP** | Practical workspace isolation |
| 12 | dispatching-parallel-agents | superpowers | Parallel agent dispatch for independent problem domains | Easy | **MERGE into SDD** | Subset of SDD's capability |

### Phase 4: REVIEW (Code & Design Review)

| # | Skill | Source | Description | Difficulty | Decision | Rationale |
|---|-------|--------|-------------|-----------|----------|-----------|
| 13 | review | gstack | Staff engineer review: SQL safety, LLM trust boundaries, conditional side effects, auto-fix | Easy | **KEEP** | Specific check patterns are well-thought-out |
| 14 | codex | gstack | OpenAI Codex CLI wrapper: review/challenge/consult modes, cross-model analysis | Medium | **KEEP** | Multi-model second opinion is genuinely useful |
| 15 | requesting-code-review | superpowers | Dispatch reviewer subagent with git SHAs, requirements, act on feedback | Medium | **KEEP** (adapt) | Template concept good, adapt to OpenClaw subagents |
| 16 | receiving-code-review | superpowers | Behavioral guardrails: verify before implementing, push back, no performative agreement | Easy | **KEEP** | Unique behavioral value |
| 17 | design-review | gstack | Visual QA: find spacing/typography/hierarchy issues, AI slop detection, fix + verify | Medium | **KEEP** | Before/after verification pattern is valuable |

### Phase 5: TEST (QA & Security)

| # | Skill | Source | Description | Difficulty | Decision | Rationale |
|---|-------|--------|-------------|-----------|----------|-----------|
| 18 | qa | gstack | Full QA: test → find bugs → fix → commit → re-verify, health scoring | Medium | **KEEP** | Core QA skill, adapt browse binary → OpenClaw browser |
| 19 | qa-only | gstack | Report-only QA: findings without code changes | Medium | **KEEP** | Useful when you want findings only |
| 20 | cso | gstack | Security audit: 14 phases, OWASP Top 10, STRIDE, 22 FP exclusions, confidence gates | Medium | **KEEP** | Most comprehensive skill in either repo |
| 21 | systematic-debugging | superpowers | 4-phase root cause: investigate → pattern → hypothesis → implement | Easy | **KEEP** | Excellent methodology, merge with gstack investigate |
| 22 | investigate | gstack | Structured debugging: scope boundary, hypothesis ranking, fix verification | Easy | **MERGE into systematic-debugging** | Overlapping with superpowers debugging |
| 23 | verification-before-completion | superpowers | Evidence-based completion: no claims without fresh verification output | Easy | **KEEP** | Essential companion to TDD |

### Phase 6: SHIP (Release & Deploy)

| # | Skill | Source | Description | Difficulty | Decision | Rationale |
|---|-------|--------|-------------|-----------|----------|-----------|
| 24 | ship | gstack | Full pipeline: merge base → test → review → version → changelog → push → PR | Medium | **KEEP** | Complete shipping workflow |
| 25 | land-and-deploy | gstack | Merge PR → wait CI → deploy → verify production health | Medium | **KEEP** | Deployment verification |
| 26 | finishing-a-dev-branch | superpowers | Verify tests → 4 options (merge/PR/keep/discard) → cleanup | Easy | **KEEP** | Clean completion flow, complement to ship |
| 27 | document-release | gstack | Post-ship doc update: cross-reference diff, update all docs, VERSION bump | Easy | **KEEP** | Simple and universally useful |

### Phase 7: REFLECT (Learn & Improve)

| # | Skill | Source | Description | Difficulty | Decision | Rationale |
|---|-------|--------|-------------|-----------|----------|-----------|
| 28 | retro | gstack | Weekly retrospective: commit analysis, per-author breakdowns, trend tracking | Easy | **KEEP** | Valuable team workflow |
| 29 | learn | gstack | Manage project learnings: search, prune, export, pattern recognition | Easy | **KEEP** | Learning persistence across sessions |
| 30 | writing-skills | superpowers | Meta: TDD for documentation, anti-rationalization techniques, CSO for skill discovery | Hard | **KEEP** (principles) | Brilliant meta-principles, adapt format |

### DROPPED (17 skills)

| Skill | Source | Reason |
|-------|--------|--------|
| using-superpowers | superpowers | Platform-specific orchestration, OpenClaw has own skill system |
| autoplan | gstack | Too coupled to gstack review ecosystem |
| browse (main) | gstack | OpenClaw has native browser tool |
| careful | gstack | OpenClaw has built-in exec approval |
| freeze | gstack | OpenClaw lacks PreToolUse hooks |
| guard | gstack | Combines careful + freeze, both dropped |
| unfreeze | gstack | Companion to freeze |
| connect-chrome | gstack | OpenClaw browser has headed mode |
| design-html | gstack | Pretext framework dependency, non-portable |
| design-shotgun | gstack | Custom `$D` binary dependency |
| setup-browser-cookies | gstack | OpenClaw handles cookies differently |
| gstack-upgrade | gstack | gstack-specific maintenance |
| benchmark | gstack | Keep concept, defer — needs significant rewrite |
| canary | gstack | Keep concept, defer — needs significant rewrite |
| setup-deploy | gstack | Keep concept, defer — low priority |

---

## Key Patterns to Preserve

1. **Iron Laws** — "No fixes without root cause", "No production code without failing test", "No completion claims without verification"
2. **No Rationalization Pattern** — Red flags tables, spirit-vs-letter clauses, rationalization prevention
3. **Two-Stage Review** — Spec compliance first, then code quality
4. **Before/After Verification** — Screenshot diff, health scoring, regression testing
5. **Cross-Model Comparison** — Multiple AI perspectives on same code
6. **6 Forcing Questions** — Product thinking from office-hours
7. **Confidence Scoring** — 8/10 daily gate, 2/10 comprehensive audit
8. **FP Filtering** — 22 hard exclusions + 12 precedents (from cso)
9. **Trend Tracking** — JSONL-based history for retros, security, performance
10. **DONE/BLOCKED/NEEDS_CONTEXT** — Structured completion protocol

## Key Patterns to Discard

1. ~200-line preamble per skill (telemetry, upgrade checks, routing)
2. gstack binary ecosystem (`$B`, `$D`, `gstack-config`, etc.)
3. CLAUDE.md routing rules
4. Claude Code PreToolUse hooks
5. `AskUserQuestion` format
6. Plan mode review report footer
7. Telemetry system

---

## Cross-Platform Strategy

### Shared (Platform-Agnostic)
All 30 kept skills share the same **core prompt logic**. The methodology, questions, checklists, and decision frameworks are pure text and work on any platform.

### Platform Adapter Layer

**OpenClaw adapter:**
- exec → Bash commands
- read/write/edit → file operations
- browser (snapshot/screenshot/act) → browse/QA/design-review
- web_search → competitive research, dependency audits
- image_generate → design mockups
- sessions_spawn (model override) → cross-model review, subagent dev
- message → notifications

**Claude Code adapter:**
- Bash → shell commands (including gstack binary if installed)
- Read/Write/Edit → file operations
- mcp__claude-in-chrome__ or `$B` → browse/QA
- WebSearch → research
- Task/subagent → subagent dev, parallel agents
- AskUserQuestion → interactive prompts

### Enhanced vs Core Skills

**Core (both platforms, zero extra deps):**
brainstorming, office-hours, plan reviews (×3), writing-plans, TDD, systematic-debugging, executing-plans, code review (×2), receiving-review, verification, ship, finish-branch, document-release, retro, learn

**Enhanced (optional extra deps):**
- Browser QA (qa, qa-only, design-review) — needs browser tool / gstack binary
- Cross-model review (codex) — needs codex CLI or multi-model support
- Security audit (cso) — needs web_search for dependency checks
- Design consultation — needs image_generate or design binary
- Subagent-driven-dev — needs subagent support
- Land-and-deploy — needs gh CLI + deploy platform

---

## Recommended Architecture

```
forge/
├── SKILL.md                          # Main entry: sprint overview, skill routing
├── DESIGN.md                         # Full design document (this analysis evolves into it)
├── skills/
│   ├── think/
│   │   ├── office-hours.md
│   │   ├── brainstorming.md
│   │   └── design-consultation.md
│   ├── plan/
│   │   ├── ceo-review.md
│   │   ├── eng-review.md
│   │   ├── design-review-plan.md
│   │   └── writing-plans.md
│   ├── build/
│   │   ├── subagent-dev.md           # Includes parallel dispatch
│   │   ├── executing-plans.md
│   │   ├── tdd.md
│   │   └── worktrees.md
│   ├── review/
│   │   ├── code-review.md
│   │   ├── codex-review.md
│   │   ├── requesting-review.md
│   │   ├── receiving-review.md
│   │   └── visual-review.md
│   ├── test/
│   │   ├── qa.md
│   │   ├── qa-report.md
│   │   ├── security-audit.md
│   │   ├── debug.md                  # Merged: systematic-debugging + investigate
│   │   └── verify.md
│   ├── ship/
│   │   ├── ship.md
│   │   ├── deploy.md
│   │   ├── finish-branch.md
│   │   └── document-release.md
│   └── reflect/
│       ├── retro.md
│       ├── learn.md
│       └── writing-skills.md
├── platform/
│   ├── openclaw.md                   # Tool mapping for OpenClaw
│   └── claude-code.md                # Tool mapping for Claude Code
└── templates/
    ├── design-doc.md
    ├── plan.md
    ├── review-checklist.md
    ├── qa-report.md
    ├── security-report.md
    ├── retro-report.md
    └── ship-checklist.md
```

---

## Next Steps

1. ✅ ~~Pull source repos~~
2. ✅ ~~Skill-by-skill analysis~~
3. **→ Write DESIGN.md** — Finalize architecture, confirm skill list, define interfaces
4. **→ Phase 1 MVP** — SKILL.md + 3 core skills (brainstorming + TDD + verify)
5. **→ Phase 2** — Full skill set
6. **→ Phase 3** — Enhanced capabilities, cross-platform testing

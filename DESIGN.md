# Forge — Design Document

> **Version:** 0.1.0-draft
> **Date:** 2026-03-30
> **Status:** Design Phase
> **Repo:** https://github.com/KKenny0/forge

---

## 1. Vision

Forge is a **cross-platform AI development sprint framework** that combines the best of [Superpowers](https://github.com/obra/superpowers) and [gstack](https://github.com/garrytan/gstack) into a unified skill pack.

**One sentence:** A structured sprint pipeline — Think → Plan → Build → Review → Test → Ship → Reflect — that works on both OpenClaw and Claude Code, with zero compromise on discipline or capability.

**What makes it different:**

- **Process over tools.** The methodology is platform-agnostic. The same 7-phase sprint runs on OpenClaw's native tools or Claude Code's Bash/Task system.
- **Discipline enforced.** Iron laws, anti-rationalization tables, and evidence gates prevent the agent from cutting corners.
- **Core + Enhanced.** The sprint works fully with zero extra dependencies. Browser QA, cross-model review, and security audits are optional power-ups.
- **Skill-chaining, not skill-bloating.** Each skill is focused and composable. The main SKILL.md orchestrates the pipeline; sub-skills load on demand.

---

## 2. Philosophy

### Principles (inherited + synthesized)

1. **No code without design.** Every feature starts with brainstorming or office-hours. The agent must understand WHY before HOW.
2. **No production code without a failing test.** TDD is not optional. Write the test, watch it fail, then write the code.
3. **No fixes without root cause.** Debugging is investigation first, implementation second. Three failed fixes → stop and question architecture.
4. **No completion claims without evidence.** "It should work" is not a completion statement. Run the command, show the output.
5. **No rationalization.** Red flags tables, spirit-vs-letter clauses, and iron laws catch every excuse the agent might invent to skip a step.
6. **No surprises.** Before/after verification at every gate. Screenshots, diffs, health scores.
7. **Evidence over authority.** The agent pushes back on wrong reviews. No performative agreement.

### Voice

Direct, confident, builder-focused. Think YC partner meets staff engineer. No fluff. Say what you see, do what needs doing.

---

## 3. Architecture

### 3.1 File Structure

```
forge/
├── SKILL.md                    # Main entry point: sprint overview, routing, pre-flight
├── DESIGN.md                   # This document
├── CHANGELOG.md
├── LICENSE
│
├── skills/
│   ├── think/
│   │   ├── office-hours.md     # 6 forcing questions (gstack)
│   │   ├── brainstorming.md    # Socratic design refinement (superpowers)
│   │   └── design-consult.md   # Design system creation (gstack, adapted)
│   │
│   ├── plan/
│   │   ├── ceo-review.md       # Strategic scope review (gstack)
│   │   ├── eng-review.md       # Architecture & edge cases (gstack)
│   │   ├── design-review.md    # Design dimension scoring (gstack)
│   │   └── writing-plans.md    # Bite-sized tasks, zero placeholders (superpowers)
│   │
│   ├── build/
│   │   ├── subagent-dev.md     # Subagent-per-task, 2-stage review (superpowers)
│   │   ├── exec-plans.md       # Sequential execution with checkpoints (superpowers)
│   │   ├── tdd.md              # RED-GREEN-REFACTOR (superpowers)
│   │   └── worktrees.md        # Git worktree isolation (superpowers)
│   │
│   ├── review/
│   │   ├── code-review.md      # SQL safety, LLM boundaries, auto-fix (gstack)
│   │   ├── cross-model.md      # Codex/multi-model second opinion (gstack)
│   │   ├── request-review.md   # Dispatch reviewer subagent (superpowers)
│   │   ├── receive-review.md   # Behavioral guardrails (superpowers)
│   │   └── visual-review.md    # Before/after visual QA (gstack)
│   │
│   ├── test/
│   │   ├── qa.md               # Test → fix → commit → verify (gstack)
│   │   ├── qa-report.md        # Findings only, no code changes (gstack)
│   │   ├── security.md         # 14-phase security audit (gstack)
│   │   ├── debug.md            # 4-phase root cause (merged: sp + gstack)
│   │   └── verify.md           # Evidence-based completion gate (superpowers)
│   │
│   ├── ship/
│   │   ├── ship.md             # Full shipping pipeline (gstack)
│   │   ├── deploy.md           # Merge → CI → deploy → verify (gstack)
│   │   ├── finish-branch.md    # 4-option branch completion (superpowers)
│   │   └── document-release.md # Post-ship doc sync (gstack)
│   │
│   └── reflect/
│       ├── retro.md            # Weekly retrospective with trends (gstack)
│       ├── learn.md            # Learning persistence (gstack)
│       └── writing-skills.md   # Meta: TDD for documentation (superpowers)
│
├── platform/
│   ├── openclaw.md             # Tool mapping + conventions for OpenClaw
│   └── claude-code.md          # Tool mapping + conventions for Claude Code
│
└── templates/
    ├── design-doc.md           # Design specification template
    ├── plan.md                 # Implementation plan template
    ├── review-checklist.md     # Code review checklist
    ├── qa-report.md            # QA report template
    ├── security-report.md      # Security audit report template
    ├── retro-report.md         # Retrospective report template
    └── ship-checklist.md       # Pre-ship checklist
```

### 3.2 Skill Routing (SKILL.md)

The main SKILL.md does NOT load all sub-skills. Instead, it:

1. **Detects platform** — reads platform adapter for tool mapping
2. **Detects sprint phase** — based on project state (no design doc? → THINK. Has design, no plan? → PLAN. Has plan, no code? → BUILD. Etc.)
3. **Detects enhanced capabilities** — checks for browser tool, codex CLI, gh CLI, multi-model support
4. **Routes to the correct sub-skill** — tells the agent to read the specific skill file

```markdown
## Routing Logic

Check project state in this order:
1. No DESIGN.md exists → THINK phase (office-hours or brainstorming)
2. DESIGN.md exists, no PLAN.md → PLAN phase (ceo-review → eng-review → writing-plans)
3. PLAN.md exists, not implemented → BUILD phase (subagent-dev or exec-plans)
4. Code exists, not reviewed → REVIEW phase (code-review, cross-model)
5. Reviewed, not tested → TEST phase (qa, security, verify)
6. Tested, not shipped → SHIP phase (ship, deploy, document-release)
7. Shipped → REFLECT phase (retro, learn)
```

### 3.3 Platform Adapter Pattern

Each sub-skill uses `{platform-tools}` placeholder. The platform adapter resolves this:

**OpenClaw (`platform/openclaw.md`):**
```yaml
tools:
  shell: exec
  read_file: read
  write_file: write
  edit_file: edit
  browser_navigate: "browser(action: navigate, url: ...)"
  browser_snapshot: "browser(action: snapshot, ...)"
  browser_act: "browser(action: act, ...)"
  browser_screenshot: "browser(action: screenshot, ...)"
  web_search: web_search
  image_gen: image_generate
  subagent: "sessions_spawn(task: ..., model: ...)"
  cross_model_review: "sessions_spawn(task: 'Review this diff', model: 'openai/gpt-4o')"
  git: "exec(command: 'git ...')"
  gh_cli: "exec(command: 'gh ...')"
  test_runner: "exec(command: '<test_command>')"
```

**Claude Code (`platform/claude-code.md`):**
```yaml
tools:
  shell: Bash
  read_file: Read
  write_file: Write
  edit_file: Edit
  browser_navigate: "Bash('$B goto ...')"   # Requires gstack binary
  browser_snapshot: "Bash('$B snapshot ...')"
  browser_act: "Bash('$B click ...')"
  browser_screenshot: "Bash('$B screenshot ...')"
  web_search: WebSearch
  image_gen: "Bash('$D ...')"               # Requires gstack design binary
  subagent: "Task(...)"
  cross_model_review: "Bash('codex review ...')"
  git: "Bash('git ...')"
  gh_cli: "Bash('gh ...')"
  test_runner: "Bash('<test_command>')"
```

### 3.4 Enhanced Capability Detection

At sprint start, detect what's available:

```markdown
## Pre-flight Checks

Run these once per session:

### Platform Detection
- Check for OpenClaw: look for exec/read/write/browser in available tools
- Check for Claude Code: look for Bash/Read/Write/Task in available tools

### Enhanced Capabilities
- Browser QA: exec("which gstack") returns path OR browser tool available
- Cross-model review: exec("which codex") returns path OR multi-model sessions_spawn supported
- GitHub integration: exec("which gh") returns path AND exec("gh auth status") succeeds
- Image generation: image_generate tool available OR gstack design binary available
- Deploy platform: detect from project config (vercel.json, fly.toml, render.yaml, etc.)

### Unavailable Capabilities
If an enhanced skill requires a missing capability:
1. Skip that skill
2. Inform user: "⚠️ Skipping /qa — no browser tool available. Install gstack browse or use OpenClaw browser."
3. Continue with remaining pipeline
```

---

## 4. Sprint Pipeline — Detailed Design

### 4.1 THINK Phase

**Goal:** Turn a rough idea into a validated design document.

**Entry:** User describes a feature, bug, or idea.
**Exit:** `DESIGN.md` written and approved by user.

#### Skill: office-hours

**Source:** gstack (adapted)
**Core:** 6 forcing questions that reframe the product before code.

```
1. DEMAND — Who desperately needs this? What happens if they don't get it?
2. STATUS QUO — What do they do today? Why is it broken?
3. DESPERATE SPECIFICITY — Describe the user's Tuesday. What exactly goes wrong?
4. NARROWEST WEDGE — What's the smallest version that proves the concept?
5. OBSERVATION — Go watch a real user try to solve this. What did you see?
6. FUTURE FIT — How does this evolve? What's the 3-year version?
```

Two modes:
- **Startup mode** — full 6 questions, product-level thinking
- **Builder mode** — design thinking for features/side-projects (lighter)

**Output:** Saves to `.forge/office-hours-{date}.md` (internal context, not the design doc itself)

**Enhanced deps:** web_search (for competitive research)

#### Skill: brainstorming

**Source:** superpowers (adapted)
**Core:** Socratic refinement with HARD GATE — no code until design is approved.

```
Flow:
1. Explore context (read project files, recent commits)
2. Clarify the problem (one question at a time, prefer multiple choice)
3. Propose 2-3 approaches with trade-offs
4. Present design in digestible chunks
5. Self-review against spec completeness checklist
6. User review and approval
7. → Route to PLAN phase
```

**Iron Law:** No code is written until the user explicitly approves the design.

**Output:** `DESIGN.md` at project root (using template)

**Enhanced deps:** browser (for visual companion — optional)

#### Skill: design-consult

**Source:** gstack (adapted)
**Core:** Build a complete design system when the project needs one from scratch.

```
Phases:
1. Product context gathering
2. Competitive research (web_search)
3. Full proposal: aesthetic, typography, color, spacing, layout, motion
4. SAFE/RISK breakdown for each decision
5. Design preview (image generation)
6. Write DESIGN.md with design system section
```

**Enhanced deps:** web_search, image_generate

**When to use vs brainstorming:** brainstorming is for features and logic. design-consult is for visual/UX-heavy projects that need a design system from scratch.

---

### 4.2 PLAN Phase

**Goal:** Transform design into an executable plan with exact file paths, complete code, and TDD steps.

**Entry:** Approved DESIGN.md exists.
**Exit:** `PLAN.md` written and reviewed.

#### Skill: ceo-review

**Source:** gstack (adapted)
**Core:** Rethink the problem. Find the 10-star product.

```
4 scope modes:
- EXPANSION — The idea is too small. What's the real opportunity?
- SELECTIVE EXPANSION — Expand specific parts that unlock more value
- HOLD SCOPE — The scope is right. Focus on execution quality.
- REDUCTION — The idea is too big. What's the MVP?

Process:
1. Read DESIGN.md
2. Challenge premises (why this? why now? why us?)
3. Apply scope mode
4. Identify risks and blind spots
5. Write review findings
```

**Enhanced deps:** web_search (for market validation)

#### Skill: eng-review

**Source:** gstack (adapted)
**Core:** Lock in architecture, data flow, edge cases, and tests.

```
Process:
1. Read DESIGN.md
2. Walk through architecture: data flow, component boundaries, API contracts
3. Generate Mermaid diagrams for key flows
4. Enumerate edge cases (happy path + failure modes)
5. Define test plan: what to test, how to test, coverage targets
6. Identify performance considerations
7. Write review findings
```

#### Skill: design-review (plan stage)

**Source:** gstack (adapted)
**Core:** Rate each design dimension 0-10, explain what a 10 looks like.

```
Dimensions:
- Aesthetic coherence
- Typography hierarchy
- Color system
- Spacing rhythm
- Layout structure
- Motion/interaction
- Responsiveness
- Accessibility
- Content hierarchy

Per dimension:
1. Current score (0-10)
2. What a 10 looks like (concrete example)
3. Specific fix to get closer to 10
```

#### Skill: writing-plans

**Source:** superpowers (adapted)
**Core:** Create bite-sized tasks that a zero-context engineer can execute.

```
Principles:
- Each task = one action (2-5 minutes)
- Exact file paths (never "the relevant file")
- Complete code blocks (never "add appropriate handling")
- Exact commands with expected output
- TDD baked in: test → verify fail → implement → verify pass → commit
- No placeholders ever (TBD, TODO, "etc." = plan failure)

Self-review checklist:
□ All tasks have exact file paths
□ No placeholders or TBDs
□ Every task has a verification step
□ Test steps come before implementation steps
□ Type consistency across tasks
□ Dependencies between tasks are explicit
```

**Output:** `PLAN.md` at project root (using template)

---

### 4.3 BUILD Phase

**Goal:** Implement the plan with discipline — TDD, isolation, and review.

**Entry:** Approved PLAN.md exists.
**Exit:** All tasks implemented, each reviewed.

#### Skill: subagent-dev

**Source:** superpowers (adapted) — the flagship execution engine.

```
Core loop:
For each task in PLAN.md:
  1. Dispatch implementer subagent
     - Fresh context (isolated session)
     - Task description + file paths + code from plan
     - TDD instructions loaded
  2. Handle implementer response:
     - DONE → proceed to review
     - DONE_WITH_CONCERNS → log concerns, proceed to review
     - NEEDS_CONTEXT → answer questions, re-dispatch
     - BLOCKED → investigate, resolve, re-dispatch
  3. Spec review subagent
     - Does the implementation match the plan spec?
     - Check all acceptance criteria
  4. Code quality review subagent
     - Code quality, naming, structure
     - Test coverage
     - Edge cases
  5. If reviews pass → mark task complete
  6. If reviews fail → fix and re-review

Model selection:
- Mechanical tasks (rename, move, config) → cheap/fast model
- Integration tasks → standard model
- Architecture tasks → powerful model
```

**Key difference from gstack:** Sequential subagents (one at a time) to avoid merge conflicts. Parallel dispatch is available for truly independent tasks but off by default.

**Platform mapping:**
- OpenClaw: `sessions_spawn` with mode=run
- Claude Code: `Task` with isolated context

#### Skill: exec-plans

**Source:** superpowers (adapted)
**Core:** Sequential plan execution in the current session (manual alternative to subagent-dev).

```
When to use:
- User wants to stay in the loop
- Project is small (1-3 tasks)
- Subagent system unavailable

Flow:
1. Read PLAN.md
2. For each task:
   a. Mark in_progress
   b. Execute steps (follow TDD)
   c. Run verification
   d. Mark completed
3. After all tasks → REVIEW phase
```

#### Skill: tdd

**Source:** superpowers (adapted)
**Core:** RED-GREEN-REFACTOR enforcement.

```
Iron Law: NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST

RED phase:
1. Write one minimal test
2. Clear, descriptive name
3. Real code (no mocks unless unavoidable)
4. Run test → MUST fail with the expected error
5. If test passes → you wrote the wrong test, delete and redo

GREEN phase:
1. Write simplest code to make the test pass
2. No YAGNI — only what's needed for this test
3. Run all tests → MUST all pass
4. Output must be pristine (no warnings, no skipped)

REFACTOR phase:
1. Clean up code while keeping tests green
2. No new behavior in refactor
3. Run all tests again → still green
4. Commit
```

#### Skill: worktrees

**Source:** superpowers (adapted)
**Core:** Isolated workspace per feature branch.

```
Flow:
1. Detect project type (npm/cargo/pip/go/etc.)
2. Create worktree: .forge/worktrees/<branch>/
3. Verify .forge/worktrees/ is gitignored
4. Auto-detect and run setup (npm install, cargo build, etc.)
5. Run baseline tests → verify clean state
6. Report: path, test status, ready state
```

---

### 4.4 REVIEW Phase

**Goal:** Catch bugs that pass CI but blow up in production.

**Entry:** Code is implemented.
**Exit:** All findings addressed.

#### Skill: code-review

**Source:** gstack (adapted)
**Core:** Pattern-based diff analysis with auto-fix.

```
Check categories:
1. SQL injection risk — parameterized queries, string concatenation in SQL
2. LLM trust boundary — prompt injection, unsanitized user input to LLM
3. Conditional side effects — mutations hidden in ternaries, short-circuits
4. Auth gaps — missing auth checks, overly permissive scopes
5. Resource leaks — unclosed connections, missing cleanup
6. Race conditions — shared mutable state, missing locks
7. Error handling — swallowed errors, missing error paths
8. Type safety — any casts, missing null checks

Severity: Critical → Important → Minor → Nit

Auto-fix:
- Critical and Important: fix immediately, commit atomically
- Minor: flag for awareness
- Nit: mention in passing
```

#### Skill: cross-model

**Source:** gstack (adapted)
**Core:** Get a second opinion from a different AI model.

```
Three modes:
1. REVIEW — Pass/fail gate on the diff
2. CHALLENGE — Adversarial: actively try to break the code
3. CONSULT — Freeform Q&A with session continuity

Platform mapping:
- OpenClaw: sessions_spawn(model: "openai/gpt-4o", task: "Review this diff: ...")
- Claude Code: exec("codex review") or exec("codex exec --json '...'")

Cross-model analysis:
When both code-review (local model) and cross-model (external model) have reviewed:
- Findings that overlap → high confidence, must fix
- Findings unique to one model → investigate, lower priority
- Present unified report with confidence levels
```

**Enhanced deps:** codex CLI (Claude Code) or multi-model support (OpenClaw)

#### Skill: request-review

**Source:** superpowers (adapted)
**Core:** Dispatch a reviewer subagent with full context.

```
Template for reviewer:
- What was implemented (from PLAN.md)
- Git SHAs (base and head)
- Requirements (from DESIGN.md)
- Test results
- Specific areas of concern

Act on feedback:
- Critical → fix immediately, re-review
- Important → fix before proceeding
- Minor → note, fix if time permits
- Disagree → push back with reasoning
```

#### Skill: receive-review

**Source:** superpowers (adapted)
**Core:** Behavioral guardrails for processing feedback.

```
6-step response:
1. READ — Understand the full feedback
2. UNDERSTAND — Why is this being suggested?
3. VERIFY — Is it technically correct for THIS codebase?
4. EVALUATE — Is it worth doing? YAGNI check.
5. RESPOND — Address each point, push back if wrong
6. IMPLEMENT — Blocking first, simple next, complex last

NEVER:
- Say "You're absolutely right!" without verification
- Implement unclear suggestions without clarification
- Add suggested features that aren't currently used
```

#### Skill: visual-review

**Source:** gstack (adapted)
**Core:** Find and fix visual issues with before/after evidence.

```
Check areas:
- Spacing consistency (padding, margins, gaps)
- Typography hierarchy (sizes, weights, line heights)
- Color consistency (brand colors, contrast ratios)
- Layout alignment (grid, flexbox issues)
- Responsive breakpoints
- AI slop patterns (generic gradients, placeholder text, excessive borders)

Flow:
1. Navigate to live site (browser tool)
2. Take before screenshots
3. Identify issues with severity ratings
4. Fix in source code
5. Take after screenshots
6. Verify fixes
7. Commit atomically per fix
```

**Enhanced deps:** browser tool (required)

---

### 4.5 TEST Phase

**Goal:** Verify everything works. Find what the reviews missed.

**Entry:** Code is reviewed.
**Exit:** QA report generated, all critical findings fixed.

#### Skill: qa

**Source:** gstack (adapted)
**Core:** Test → find bugs → fix → verify loop with health scoring.

```
Three tiers:
- QUICK: Smoke test (5 min) — main flows, no edge cases
- STANDARD: Full test (15 min) — main flows + common edge cases
- EXHAUSTIVE: Deep test (30+ min) — everything including error paths

Flow:
1. Navigate to target (browser tool or URL)
2. Test each flow from PLAN.md
3. Check for:
   - Visual issues
   - Console errors
   - Network failures
   - Broken interactions
   - Accessibility issues
4. For each bug found:
   a. Document with severity + reproduction steps
   b. Fix in source code
   c. Commit atomically
   d. Re-verify the fix
5. Calculate health score
6. Generate QA report
```

**Health scoring:**
```
10 — No issues found
8-9 — Minor issues only, all auto-fixed
6-7 — Some important issues, all fixed
4-5 — Critical issues found, fixed with caveats
0-3 — Critical issues, some unresolved → DO NOT SHIP
```

**Enhanced deps:** browser tool (required for web QA)

#### Skill: qa-report

**Source:** gstack (adapted)
**Core:** Findings-only QA — no code changes.

```
Same methodology as qa, but stops at documentation:
1. Test all flows
2. Document each finding:
   - Severity (Critical/Important/Minor)
   - Description
   - Reproduction steps
   - Expected vs actual behavior
   - Screenshot evidence
3. Generate structured report
4. Health score
```

#### Skill: security

**Source:** gstack (adapted)
**Core:** 14-phase security audit with FP filtering.

```
Phases:
1. Stack detection
2. Attack surface census
3. Secrets archaeology (.env, hardcoded keys, git history)
4. Dependency audit (package.json, requirements.txt, go.mod)
5. CI/CD pipeline security
6. Infrastructure shadow surface
7. Webhook security
8. LLM/AI security (prompt injection, tool abuse)
9. Skill/dependency supply chain
10. OWASP Top 10 check
11. STRIDE threat model
12. Data classification
13. False positive filtering (22 hard exclusions + 12 precedents)
14. Report with confidence scores and trend tracking

Confidence gates:
- Daily audit: 8/10 minimum confidence
- Comprehensive audit: 2/10 minimum confidence (catch more, accept more noise)
```

**Enhanced deps:** web_search (for CVE lookups), subagent (for parallel verification)

#### Skill: debug

**Source:** merged from superpowers systematic-debugging + gstack investigate
**Core:** 4-phase root cause investigation.

```
Iron Law: NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST

Phase 1 — INVESTIGATE:
- Read error messages carefully (exact text, stack trace)
- Reproduce consistently (identify minimal steps)
- Check recent changes (git diff, git log)
- Gather evidence at component boundaries
- Trace data flow from input to failure

Phase 2 — PATTERN:
- Find working examples (when did this work? what changed?)
- Compare against references (docs, similar code, known patterns)
- Identify specific differences

Phase 3 — HYPOTHESIS:
- Form ONE hypothesis
- Test minimally (one variable at a time)
- Rank hypotheses by likelihood

Phase 4 — IMPLEMENT:
- Write failing test that reproduces the bug
- Implement minimal fix
- Verify fix + all existing tests pass
- Commit

Escalation:
- 3 consecutive failed fix attempts → STOP
- Question the architecture, not the code
- Ask user for domain context
```

#### Skill: verify

**Source:** superpowers (adapted)
**Core:** Evidence-based completion gate.

```
5-step gate:
1. IDENTIFY — What command proves this is done?
2. RUN — Execute the full command (not a shortcut)
3. READ — Read the FULL output (not a summary)
4. VERIFY — Does the output match expectations?
5. CLAIM — Only now can you say it's done

Forbidden phrases (before verification):
- "should work"
- "probably fixed"
- "seems correct"
- "I believe"
```

---

### 4.6 SHIP Phase

**Goal:** Get the code to production, verified and documented.

**Entry:** All tests pass, all reviews clear.
**Exit:** PR merged or branch shipped, docs updated.

#### Skill: ship

**Source:** gstack (adapted)
**Core:** Full shipping pipeline.

```
Pipeline:
1. Sync with base branch (git merge main)
2. Run full test suite → must pass
3. Review diff (final check)
4. Bump VERSION (semantic versioning)
5. Update CHANGELOG
6. Commit version + changelog
7. Push to remote
8. Create PR with description
9. → Route to document-release
```

**Pre-ship checklist:**
- [ ] All tests pass
- [ ] Code reviewed
- [ ] QA report clean (or acceptable)
- [ ] Security scan clean
- [ ] VERSION bumped
- [ ] CHANGELOG updated
- [ ] No TODO/FIXME/HACK in new code
- [ ] No debug logging in new code

#### Skill: deploy

**Source:** gstack (adapted)
**Core:** Merge PR → CI → deploy → verify production.

```
Flow:
1. Merge the PR (via gh CLI or manual)
2. Monitor CI (wait for green)
3. Trigger/verify deployment
4. Run production health checks:
   - Page loads without errors
   - Console clean
   - Key flows functional
   - Performance within baseline
5. Generate deployment report
```

**Enhanced deps:** gh CLI, browser tool, deploy platform CLI

#### Skill: finish-branch

**Source:** superpowers (adapted)
**Core:** Clean branch completion with 4 options.

```
Post-implementation:
1. Verify tests pass (HARD GATE)
2. Determine base branch
3. Present options:
   A) Merge to local base branch
   B) Push and create PR
   C) Keep as-is (continue working)
   D) Discard branch and cleanup
4. Execute chosen option
5. Cleanup worktree (for options A and D)
```

#### Skill: document-release

**Source:** gstack (adapted)
**Core:** Sync all docs with what was just shipped.

```
Flow:
1. Read current docs (README, ARCHITECTURE, CONTRIBUTING, CHANGELOG, etc.)
2. Read the diff (what was actually shipped)
3. Cross-reference: identify what changed that affects docs
4. Update each affected doc
5. Clean up stale TODOs and FIXMEs
6. Optional VERSION bump (if not done in ship)
```

---

### 4.7 REFLECT Phase

**Goal:** Learn from what was built. Get better over time.

**Entry:** Code is shipped.
**Exit:** Retro report generated, learnings recorded.

#### Skill: retro

**Source:** gstack (adapted)
**Core:** Weekly engineering retrospective with trend tracking.

```
Analysis:
1. Git log analysis (past week or sprint)
2. Per-author contribution breakdown
3. Work pattern analysis (feature vs bugfix vs chore)
4. Code quality metrics (test coverage, review turnaround)
5. Praise — what went well
6. Growth areas — what to improve
7. Trend comparison with previous retros

Output:
- `.forge/retros/{date}.md` — retro report
- `.forge/retros/trends.jsonl` — trend data for comparison
```

#### Skill: learn

**Source:** gstack (adapted)
**Core:** Persistent learning across sessions.

```
Operations:
- ADD — Record a new learning (pattern, pitfall, preference)
- SEARCH — Find relevant past learnings
- PRUNE — Remove stale or disproven learnings
- EXPORT — Export learnings for project documentation

Storage: `.forge/learnings/{project-slug}.jsonl`

Each learning:
{
  "timestamp": "2026-03-30T19:00:00Z",
  "type": "pattern|pitfall|preference|discovery",
  "context": "What were we doing",
  "learning": "What we learned",
  "action": "What to do differently",
  "confidence": "high|medium|low"
}
```

#### Skill: writing-skills

**Source:** superpowers (adapted)
**Core:** TDD for documentation — create and test new skills.

```
Principles:
- Iron Law: NO SKILL WITHOUT A FAILING TEST FIRST
- RED: Test the skill by running a scenario WITHOUT the skill loaded. Document what goes wrong.
- GREEN: Write the skill. Re-run the scenario. Verify it now works correctly.
- REFACTOR: Close loopholes. Test edge cases. Add rationalization prevention.

Anti-rationalization:
- Spirit vs letter clauses ("The skill says X, but the spirit of X is Y...")
- Red flags tables (common excuses for skipping steps)
- Loophole closure (find ways the agent could bypass the skill, block them)

Skill types:
- TECHNIQUE — How to do something (TDD, debugging)
- PATTERN — Mental model for a class of problems (office-hours)
- REFERENCE — API docs, checklists (ship-checklist)
```

---

## 5. Anti-Rationalization System

This is the most important cross-cutting concern. Every skill includes rationalization prevention.

### Pattern

```markdown
## Anti-Rationalization

Common excuses for skipping this skill and why they're wrong:

| Excuse | Why it's wrong |
|--------|---------------|
| "This is too small to need {skill}" | Small changes have broken production. The cost of the skill is minutes; the cost of a bug is hours. |
| "I already know the fix" | You thought you knew the last three fixes too. Investigate first. |
| "The tests will slow me down" | Tests slow you down once. Bugs slow you down forever. |
| "I'll do it after" | You won't. Do it now. |
| "This is just a quick hack" | There are no quick hacks in production. Only permanent liabilities. |
```

### Iron Law Format

```markdown
## Iron Law

**NO {ACTION} WITHOUT {PREREQUISITE}**

Violations of this law:
- Doing {action} because "it's obvious" → investigate first
- Skipping {prerequisite} because "we're in a hurry" → the hurry is the reason you need it
- Postponing {prerequisite} → it will not happen
```

---

## 6. Data Flow

```
User Request
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│                    SKILL.md (Router)                     │
│  Detect phase → Load platform adapter → Route to skill  │
└─────────────────────┬───────────────────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
    THINK          PLAN          (project state)
        │             │
        ▼             ▼
   DESIGN.md      PLAN.md
        │             │
        └──────┬──────┘
               ▼
            BUILD
               │
        ┌──────┼──────┐
        ▼      ▼      ▼
     SDD    EXEC    TDD
        │      │      │
        └──────┼──────┘
               ▼
           REVIEW
               │
        ┌──────┼──────┐
        ▼      ▼      ▼
     CODE   CROSS   VISUAL
     REVIEW  MODEL  REVIEW
        │      │      │
        └──────┼──────┘
               ▼
             TEST
               │
        ┌──────┼──────┐
        ▼      ▼      ▼
       QA    SECURITY  DEBUG
        │      │      │
        └──────┼──────┘
               ▼
             SHIP
               │
        ┌──────┼──────┐
        ▼      ▼      ▼
      SHIP   DEPLOY  DOCS
        │      │      │
        └──────┼──────┘
               ▼
           REFLECT
               │
        ┌──────┼──────┐
        ▼      ▼      ▼
      RETRO  LEARN  WRITE-SKILLS
```

### File Artifacts

| Phase | Artifact | Format | Location |
|-------|----------|--------|----------|
| THINK | Design doc | Markdown | `DESIGN.md` |
| THINK | Office hours notes | Markdown | `.forge/office-hours-{date}.md` |
| PLAN | Implementation plan | Markdown | `PLAN.md` |
| PLAN | Review findings | Markdown | `.forge/reviews/{type}-{date}.md` |
| BUILD | Implemented code | Source files | Project tree |
| BUILD | Test files | Source files | Project tree |
| REVIEW | Review report | Markdown | `.forge/reviews/code-review-{date}.md` |
| REVIEW | Cross-model analysis | Markdown | `.forge/reviews/cross-model-{date}.md` |
| TEST | QA report | Markdown + JSON | `.forge/qa/{date}.md` + `.forge/qa/{date}.json` |
| TEST | Security report | JSON + Markdown | `.forge/security/{date}.json` + `.forge/security/{date}.md` |
| SHIP | PR | GitHub | Remote |
| SHIP | Updated docs | Markdown | Project tree |
| REFLECT | Retro report | Markdown | `.forge/retros/{date}.md` |
| REFLECT | Learnings | JSONL | `.forge/learnings/{project}.jsonl` |

---

## 7. Implementation Plan

### Phase 1 — MVP (Core Pipeline)

**Goal:** Run the minimal sprint: Think → Plan → Build → Review → Ship

**Skills to implement (8):**
1. `SKILL.md` — Router + platform detection
2. `platform/openclaw.md` — OpenClaw tool mapping
3. `platform/claude-code.md` — Claude Code tool mapping
4. `skills/think/brainstorming.md`
5. `skills/plan/writing-plans.md`
6. `skills/build/tdd.md`
7. `skills/build/subagent-dev.md`
8. `skills/review/code-review.md`
9. `skills/ship/ship.md`
10. `skills/test/verify.md`

**Templates:** design-doc.md, plan.md

**Success criteria:** A user can go from "build me a feature" to shipped code with tests, review, and PR on both OpenClaw and Claude Code.

### Phase 2 — Complete Sprint

**Skills to implement (remaining 22):**
- All remaining skills from the matrix
- All templates
- Full anti-rationalization system

### Phase 3 — Enhanced Capabilities

**Optional skills:**
- `skills/test/qa.md` + `skills/test/qa-report.md` (browser required)
- `skills/review/cross-model.md` (codex CLI or multi-model required)
- `skills/review/visual-review.md` (browser required)
- `skills/test/security.md` (web_search required)
- `skills/ship/deploy.md` (gh CLI + deploy platform required)

### Phase 4 — Polish

- README.md with installation instructions for both platforms
- CLAUDE.md snippet for Claude Code
- AGENTS.md snippet for OpenClaw
- Contributing guide
- skill-vetter self-audit

---

## 8. Open Questions

1. **Skill format:** Should we use OpenClaw's SKILL.md format (YAML frontmatter + markdown) as the canonical format, and generate Claude Code's format from it? Or maintain two parallel formats?
   - *Lean toward:* OpenClaw SKILL.md as canonical, with a conversion script for Claude Code

2. **Naming convention:** Claude Code uses `/skill-name` invocation. OpenClaw auto-detects by description. Should we support slash-command style for Claude Code compatibility?
   - *Lean toward:* Yes, include slash-command aliases in SKILL.md frontmatter

3. **Subagent isolation:** OpenClaw's `sessions_spawn` creates isolated sessions. Claude Code's `Task` also isolates. But the review template system needs to pass structured context. What's the best format?
   - *Lean toward:* JSON context blob passed as task description, with a schema defined in the skill

4. **Parallel sprints:** gstack supports 10-15 parallel sprints via Conductor. Should Forge support this in Phase 1?
   - *Lean toward:* No. Sequential first, parallel as a Phase 4 enhancement

---

## Appendix A: Skill Dependency Graph

```
office-hours ─────────┐
                       ├→ ceo-review ──┐
brainstorming ─────────┤               ├→ eng-review ──┐
                       │               │               ├→ writing-plans ──┐
design-consult ────────┘               │               │                  │
                                       ├→ design-review┘                  │
                                       │                                  ▼
                                       │                          ┌── subagent-dev ──┐
                                       │                          │                   │
                                       │                          ├── exec-plans ─────┤
                                       │                          │                   │
                                       │                          ├── tdd ────────────┤
                                       │                          │                   │
                                       │                          └── worktrees ──────┘
                                       │                                               │
                                       │                                               ▼
                                       │                                  ┌── code-review ──┐
                                       │                                  │                 │
                                       │                                  ├── cross-model ──┤
                                       │                                  │                 │
                                       │                                  ├── request-review┤
                                       │                                  │                 │
                                       │                                  ├── receive-review┤
                                       │                                  │                 │
                                       │                                  └── visual-review─┘
                                       │                                               │
                                       │                                               ▼
                                       │                                    ┌── qa ────────┐
                                       │                                    │              │
                                       │                                    ├── qa-report ──┤
                                       │                                    │              │
                                       │                                    ├── security ───┤
                                       │                                    │              │
                                       │                                    ├── debug ──────┤
                                       │                                    │              │
                                       │                                    └── verify ─────┘
                                       │                                               │
                                       │                                               ▼
                                       │                              ┌── ship ────────┐
                                       │                              │                 │
                                       │                              ├── deploy ───────┤
                                       │                              │                 │
                                       │                              ├── finish-branch─┤
                                       │                              │                 │
                                       │                              └── document-rel──┘
                                       │                                               │
                                       │                                               ▼
                                       │                              ┌── retro ───────┐
                                       │                              │               │
                                       │                              ├── learn ───────┤
                                       │                              │               │
                                       │                              └── writing-skills┘
```

## Appendix B: Merged Skills Detail

### debug (systematic-debugging + investigate)

**From superpowers:**
- 4-phase methodology (investigate → pattern → hypothesis → implement)
- Iron law: no fixes without root cause
- 3-failed-fix escalation rule
- Supporting techniques: root-cause-tracing, defense-in-depth, condition-based-waiting

**From gstack:**
- Scope boundary (freeze concept, adapted as prompt instruction)
- Hypothesis ranking by likelihood
- Fix verification protocol

**Merged flow:**
1. INVESTIGATE (sp) — Read errors, reproduce, check changes, trace data flow
2. PATTERN (sp) — Find working examples, compare, identify differences
3. HYPOTHESIS (merged) — Form hypothesis, rank by likelihood (gstack), test minimally
4. IMPLEMENT (sp) — Failing test → fix → verify
5. ESCALATE (gstack) — 3 failed fixes → stop, question architecture

# Implementation Plan: {PLAN_NAME}

> Scaffold for `/taku-plan`. Replace every placeholder before handoff. The skill instructions in `skills/plan/SKILL.md` override this template if they differ.
>
> **For agentic workers:** Use `/taku-build` to implement this plan. The build agent should choose sequential, parallel, or hybrid execution unless the user explicitly overrides it.
>
> **Review context:** Scope and architecture reviews are in `DESIGN.md`. This document is execution-only.
>
> **Build Agent Contract:**
> - **Required:** Goal, Tech Stack, Execution Hints (if present), all Tasks (Depends on + Spec + Files)
> - **Optional:** Architecture details (in DESIGN.md), review artifacts (in DESIGN.md)
> - **Skip during execution:** Scope review, architecture review sections (already in DESIGN.md)

**Goal:** {One sentence}

**Architecture:** {2-3 sentences}

**Tech Stack:** {Key technologies}

---

## Execution Hints

**Suggested mode:** Sequential | Parallel | Hybrid

**Wave 1** — {Wave purpose}
- Task 1: {short name}
- Task 2: {short name}

**Wave 2** — {Wave purpose}
- Task 3: {short name}
- Task 4: {short name}

---

### Task 1: {TASK_NAME}

**Depends on:** none

**Files:**
- Create: `{exact/path/to/file}`
- Modify: `{exact/path/to/existing/file}:{line_range}`
- Test: `{tests/exact/path/to/test}`

**Spec:**

{What to build — describe behavior, contracts, and key assertions.}

Test that `{function_name}()`:
- returns {expected} when {condition}
- handles {edge case} by {behavior}
- raises {error} when {invalid input}

Edge cases: {empty input, concurrent access, boundary values}

**TDD anchor:** `{tests/path/test.py}::test_specific_behavior`

---

### Task 2: {TASK_NAME}

**Depends on:** Task 1

**Files:**
- Create: `{exact/path/to/file}`
- Test: `{tests/exact/path/to/test}`

**Spec:**

{What to build}

**TDD anchor:** `{tests/path/test.py}::test_name`

---

## Dependency Graph

```
Task 1 → Task 2 → Task 4
Task 1 → Task 3 ↗
Task 5 (independent)
```

## Task Summary

| # | Task | Depends On | TDD Anchor | Status |
|---|------|-----------|------------|--------|
| 1 | {name} | — | {test} | Pending |
| 2 | {name} | Task 1 | {test} | Pending |
| 3 | {name} | Task 1 | {test} | Pending |
| 4 | {name} | Task 2, 3 | {test} | Pending |
| 5 | {name} | — | {test} | Pending |

---
name: forge-request-review
description: >
  Dispatch a reviewer subagent with full context. Build a structured review
  packet (what was implemented, git SHAs, requirements, test results), send it
  to a fresh-context reviewer, then act on the feedback. Use after each task
  in subagent development, after major features, or before merging. Triggers on
  "request review", "get a review", "review my changes".
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Grep
  - Glob
---

# Dispatch Reviewer Subagent

Review early, review often. The reviewer gets precisely crafted context for evaluation — never your session's history. This keeps the reviewer focused on the work product, not your thought process, and preserves your own context for continued work.

## When to Request Review

**Mandatory:** after each task in `/forge-build`, after major features, before merging.
**Optional but valuable:** when stuck, before refactoring, after fixing complex bugs.

## Step 1: Gather Context

Build the review packet. Do not skip any of these.

### 1a. Git SHAs

```bash
BASE_SHA=$(git merge-base HEAD $(git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/origin/||') 2>/dev/null || git rev-parse HEAD~1)
HEAD_SHA=$(git rev-parse HEAD)
echo "BASE: $BASE_SHA"
echo "HEAD: $HEAD_SHA"
```

### 1b. What Was Implemented

Read PLAN.md and extract the task description. If no PLAN.md, read the most recent commit messages:
```bash
git log $BASE_SHA..HEAD --oneline
```

### 1c. Requirements

Read DESIGN.md for the requirements that this implementation addresses. Extract the relevant sections.

### 1d. Test Results

```bash
# Run the project's test suite
npm test 2>/dev/null || pytest 2>/dev/null || cargo test 2>/dev/null || go test ./... 2>/dev/null
```

Capture the output. Include pass/fail counts.

### 1e. Specific Concerns

Note any areas you're unsure about. "I'm not confident about the error handling in X" or "The edge case around Y feels incomplete." This gives the reviewer focus.

## Step 2: Dispatch Reviewer

**OpenClaw:**
```
sessions_spawn(
  task: "You are a code reviewer. Review the changes between these commits.
  
  WHAT WAS IMPLEMENTED: <from Step 1b>
  REQUIREMENTS: <from Step 1c>
  BASE_SHA: <base>
  HEAD_SHA: <head>
  TEST RESULTS: <from Step 1d>
  CONCERNS: <from Step 1e>
  
  Review for: correctness, edge cases, error handling, security, test coverage,
  and adherence to requirements. Rate each finding: Critical / Important / Minor.
  End with an assessment: APPROVE / APPROVE_WITH_CONCERNS / REQUEST_CHANGES.",
  mode: "run"
)
```

**Claude Code:**
Use the Task tool with the same structured context.

## Step 3: Act on Feedback

Process the reviewer's findings in priority order:

### Critical → Fix Immediately

- Fix the issue
- Re-run tests
- Re-request review if the fix is non-trivial
- Do NOT proceed until critical issues are resolved

### Important → Fix Before Proceeding

- Fix before moving to the next task
- If the fix is large, break it into its own task
- Re-verify after fixing

### Minor → Note and Triage

- Log the finding
- Fix if time permits
- Do not let minor findings block progress on the next task

### Disagree → Push Back

The reviewer can be wrong. Push back when the finding is technically incorrect, the reviewer lacks context, the suggestion violates YAGNI, or the fix would break existing functionality. Reference code, tests, or requirements. If the reviewer still disagrees, escalate to the user.

## Step 4: Record Outcome

```bash
git log --oneline -1  # current state after review fixes
```

Record in `.forge/reviews/`:
- What was reviewed (task/feature name)
- Findings by severity
- What was fixed
- What was pushed back on (and why)
- Final assessment

## Integration with Forge Pipeline

After `/forge-build`: review each task as it completes. After `/forge-exec`: review every 2-3 tasks. Before `/forge-ship`: final review gate, all critical and important findings resolved.

## Anti-Rationalization

| Excuse | Why it's wrong |
|--------|---------------|
| "The code is simple enough to skip review" | Simple code has subtle bugs. The review takes minutes. The bug takes hours. |
| "The reviewer doesn't understand our architecture" | Then explain it in the context packet. A confused reviewer means the context is insufficient, not that the review is worthless. |
| "I already checked it myself" | You wrote it. You have blind spots. That's the whole point. |
| "Pushing back is rude" | Blind implementation is worse than pushback. Technical correctness over social comfort. |

---
name: forge-receive-review
description: >
  Behavioral guardrails for processing code review feedback. 6-step response
  protocol: Read, Understand, Verify, Evaluate, Respond, Implement. Never agree
  without verifying. Never implement without understanding. Use when receiving
  code review from any source — human, subagent, or external model.
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Grep
---

# Receiving Code Review

Code review requires technical evaluation, not emotional performance. Verify before implementing. Ask before assuming. Technical correctness over social comfort.

## The 6-Step Protocol

### 1. READ — Absorb the full feedback

Read every finding before reacting. Do not start fixing anything until you have read the entire review.

### 2. UNDERSTAND — Restate the requirement

For each finding, restate what the reviewer is asking for in your own words. If you cannot restate it, you do not understand it. Ask for clarification before proceeding.

### 3. VERIFY — Check against codebase reality

Is this finding technically correct for THIS codebase? The reviewer may be working from incomplete context. Check:
- Does the suggested fix actually apply here?
- Would the fix break existing functionality?
- Is the current implementation intentional (compatibility, legacy, documented tradeoff)?

### 4. EVALUATE — YAGNI and priority check

Is this worth doing right now?

- **YAGNI check:** Does the codebase actually use the feature the reviewer wants improved? If not, remove it instead of "implementing it properly."
- **Priority:** Does this block the current task? Does it affect the user-facing behavior? Or is it a style preference?

### 5. RESPOND — Address each point

For each finding:
- **Correct:** Fix it. State what changed. No gratitude.
- **Unclear:** Ask. Do not guess.
- **Wrong:** Push back with technical reasoning.
- **Debatable:** Present the tradeoff and let the user decide.

### 6. IMPLEMENT — One at a time, test each

Order of implementation:
1. **Blocking issues** (breaks functionality, security holes)
2. **Simple fixes** (typos, imports, one-line changes)
3. **Complex fixes** (refactoring, logic changes)

Test after each fix. Verify no regressions.

## Forbidden Responses

NEVER:
- "You're absolutely right!" — verify first
- "Great point!" — state the requirement instead
- "Let me implement that now" — verify before implementing
- "Thanks for catching that!" — actions speak, not words
- Implement a finding you don't understand
- Batch multiple fixes without testing between them

INSTEAD:
- State the technical requirement
- Push back with reasoning if wrong
- Just fix it and show the result
- Ask clarifying questions

## When to Push Back

Push back when:
- The finding is technically incorrect for this codebase
- The reviewer lacks context (compatibility, documented tradeoff, legacy constraint)
- The suggestion adds unused functionality (YAGNI)
- The fix would break existing tests or behavior
- The suggestion conflicts with DESIGN.md or stated requirements

**How:**
- Reference specific code, tests, or docs
- Explain why the current implementation exists
- Present the tradeoff clearly
- If the reviewer insists, escalate to the user

## Correcting Your Own Pushback

If you pushed back and were wrong after verifying:
- State the correction factually
- "Checked X, it does Y. Implementing now."
- No apology. No defense. Fix it.

## Source-Specific Handling

**From the user:** Trusted. Implement after understanding. Still verify.

**From a subagent/reviewer:** Evaluate carefully. Check if the reviewer has full context. Push back if findings are wrong.

**From an external model:** Skeptical. Verify every finding. External models lack project context.

## Anti-Rationalization

| Excuse | Why it's wrong |
|--------|---------------|
| "The reviewer is probably right" | Probably is not verification. Check the code. |
| "I'll implement it all to be safe" | Blind implementation introduces regressions. Verify first. |
| "This is just a style thing, I'll skip it" | If it's truly style-only, note it. But verify it's not hiding a real issue. |
| "I don't want to argue" | Technical correctness > comfort. A wrong fix in production is worse than a pushback in review. |

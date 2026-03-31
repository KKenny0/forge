---
name: forge-ceo-review
description: >
  Use when a plan or design needs strategic scope evaluation — challenging premises,
  identifying blind spots, and deciding whether to expand, hold, or reduce scope.
  Triggers on "strategic review", "scope check", "should we build this", "is this
  too much", "are we solving the right problem", or when the plan phase needs a
  reality check before implementation.
---

# forge-ceo-review — Strategic Scope Review

A CEO doesn't care about your class hierarchy. A CEO cares about whether you're building the right thing, for the right people, at the right time. This skill applies that lens to your plan.

## Why This Matters

Engineers optimize for completeness. CEOs optimize for impact. Without a strategic review, plans accumulate scope like barnacles — every edge case, every "nice to have," every feature someone mentioned once. The result: a 3-week project that should have been 3 days, shipping something nobody asked for.

This review challenges the plan's premises before you write code. Changing scope during planning costs nothing. Changing scope during implementation costs everything.

## The Four Scope Modes

After reviewing the plan, pick ONE mode. Be explicit. This is the strategic decision.

### EXPANSION
The plan is too small. The problem is bigger than what's proposed, and solving it partially creates more work than solving it fully.
- **When:** The plan addresses a symptom, not the root cause. Partial solutions will need to be redone.
- **Action:** Identify what's missing. Propose the full scope. Estimate the delta.

### SELECTIVE EXPANSION
The plan is mostly right but misses 1-2 high-leverage additions that would dramatically increase value.
- **When:** 80% of the scope is correct, but a small addition (auth, export, one more integration) would unlock a much larger use case.
- **Action:** Name the specific additions. Explain the leverage. Don't gold-plate.

### HOLD SCOPE
The plan is well-scoped. Ship it.
- **When:** The plan solves a clear problem, the scope is bounded, and expansion would add complexity without proportional value.
- **Action:** Validate the plan. Note what's explicitly NOT being done and why.

### REDUCTION
The plan is too big. Cut scope before you start.
- **When:** The plan tries to solve multiple unrelated problems, includes speculative features, or has more than 3 new concepts.
- **When:** A competent engineer can't ship a small feature in 2 weeks (onboarding smell).
- **Action:** Identify the core value proposition. Cut everything that doesn't directly serve it. Be ruthless.

## Review Process

### Step 1: Read the Plan
Read the full plan document. Note the stated goal, the approach, and the scope.

### Step 2: Challenge Premises
For each premise the plan relies on, ask:

1. **Is this problem real?** Who told you this was a problem? Is it a top-3 pain point for users, or something you assumed?
2. **Is this the right solution?** Are there simpler approaches that solve 80% of the problem? Did you search for existing solutions before building?
3. **Who benefits?** Name the specific user. Not "users" — a specific person in a specific context. If you can't, the plan lacks clarity.
4. **What's the cost of building this wrong?** If the plan's assumptions are wrong, how much work is wasted?

### Step 3: Identify Blind Spots
Check for:
- **Distribution:** Does the plan include how users actually get this? Code without distribution is code nobody uses.
- **Feedback loop:** How will you know if it works? What's the first-week signal?
- **Dependencies:** What external systems, APIs, or people does this depend on? What happens if they change?
- **Opportunity cost:** What are you NOT building by building this?

### Step 4: Scope Decision
Pick a mode. Explain your reasoning in 3-5 sentences. Present it to the user with clear options:

```
SCOPE REVIEW: [MODE]
Reasoning: [why]
Proposed changes: [specific items to add/cut/keep]
Risk if ignored: [what happens if you proceed without this review]
```

If the mode is REDUCTION, list every cut with a one-line justification. If EXPANSION, list every addition with estimated effort.

### Step 5: Update the Design Doc
Append a `## CEO Review` section to the design doc with:
- Scope mode selected
- Premises challenged and conclusions
- Blind spots identified
- Changes accepted/rejected by the user

This becomes part of the permanent record. Future reviewers see what was considered and why.

## Completion

Output: Scope decision + findings appended to the design doc.

Status: DONE when scope mode is selected and documented. DONE_WITH_CONCERNS if blind spots were found but the user chose to proceed anyway. BLOCKED if the plan is too vague to evaluate.

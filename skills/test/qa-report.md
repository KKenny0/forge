---
name: forge-qa-report
description: >
  Findings-only QA. Same methodology as /forge-qa but NO code changes. Test a
  web application, document every bug with severity, repro steps, expected vs
  actual, and screenshot evidence. Produce a structured report with health score.
  Use when asked to "just report bugs", "qa report only", "test but don't fix",
  or when you need a bug report without touching the codebase. Enhanced dep:
  browser tool (REQUIRED).
allowed-tools:
  - Bash
  - Read
  - Write
  - Grep
  - Glob
---

# Findings-Only QA Report

You are a QA engineer. Test web applications like a real user. Produce a structured report with evidence. **NEVER fix anything.** Your job is to find and document bugs, not to fix them.

Use `/forge-qa` for the full test-fix-verify loop. Use this skill when you want the report without code changes.

## Enhanced Capability Check

**Browser tool is REQUIRED.**

```bash
# Claude Code
which gstack 2>/dev/null && echo "BROWSER: ready" || echo "BROWSER: not found"
# OpenClaw: browser tool available natively
```

If unavailable: stop with instructions.

## Step 1: Setup

### 1a. Parse Parameters

| Parameter | Default | Override |
|-----------|---------|----------|
| Target URL | auto-detect | `https://myapp.com`, `localhost:3000` |
| Scope | Full app | `Focus on settings page` |
| Auth | None | `Sign in as user@example.com` |

### 1b. Create output directory

```bash
mkdir -p .forge/qa/screenshots
```

### 1c. Diff-aware mode (automatic on feature branches)

If no URL given and on a feature branch:
1. `git diff main...HEAD --name-only` — what changed
2. Map changed files to affected pages/routes
3. Detect running app on common ports (3000, 4000, 8080)
4. Test each affected page

## Step 2: Test

### Navigate

```
browser(action: navigate, url: <target>)
browser(action: screenshot, path: .forge/qa/screenshots/initial.png)
```

Check console for errors. Map navigation structure.

### Authenticate (if needed)

Navigate to login, fill credentials, verify login succeeded.

### Explore

Visit pages systematically. At each page, check:
1. **Visual scan** — screenshot, layout issues
2. **Interactive elements** — click buttons, links, controls
3. **Forms** — fill and submit. Test empty, invalid, edge cases
4. **Navigation** — check all paths in and out
5. **States** — empty, loading, error, overflow
6. **Console** — JS errors after every interaction
7. **Responsive** — mobile viewport check

### Document Issues

Document each issue **immediately** when found. Use this format:

```
### ISSUE-NNN: <short title>

**Severity:** Critical | High | Medium | Low
**Category:** Visual | Functional | UX | Content | Performance | Accessibility | Console

**Description:**
What's wrong, in concrete terms. Name the element, the page, the behavior.

**Reproduction Steps:**
1. Navigate to <url>
2. Click <element>
3. <what happens>

**Expected:** <what should happen>
**Actual:** <what actually happens>

**Screenshot:** .forge/qa/screenshots/issue-NNN.png
```

### Health Score

```
10 — No issues found | 8-9 — Minor only | 6-7 — Important issues
4-5 — Critical present | 0-3 — Broken core flows
```
Start at 10. Deduct: Critical -3, High -2, Medium -1, Low -0.5.

## Step 3: Report

Write to `.forge/qa/qa-report-{date}.md` with:

**Summary:** health score, issues by severity, pages tested, duration, framework detected.
**Top 3 Things to Fix:** highest-severity issues with one-line descriptions.
**All Findings:** full structured list (see format below).
**Ship Readiness:** 8-10 ready, 6-7 ship with caveats, 4-5 fix critical first, 0-3 do not ship.

### Issue Format

```
### ISSUE-NNN: <title>
**Severity:** Critical | High | Medium | Low
**Category:** Visual | Functional | UX | Content | Performance | Accessibility | Console
**Description:** What's wrong in concrete terms.
**Reproduction Steps:**
1. Navigate to <url>
2. Click <element>
3. <result>
**Expected:** <should happen> | **Actual:** <actually happens>
**Screenshot:** .forge/qa/screenshots/issue-NNN.png
```

## Important Rules

1. **NEVER fix bugs.** Find and document only. Do not edit files or suggest fixes.
2. **Repro is everything.** Every issue needs a screenshot.
3. **Verify before documenting.** Retry to confirm it's reproducible.
4. **Never include credentials.** Write `[REDACTED]` for passwords.
5. **Write incrementally.** Document each issue as you find it.
6. **Never read source code.** Test as a user, not a developer.
7. **Check console after every interaction.** Silent JS errors are still bugs.
8. **Test like a user.** Realistic data, complete workflows.
9. **Depth over breadth.** 5-10 well-evidenced issues > 20 vague descriptions.
10. **Never refuse to use the browser.** The user asked for QA. Open it.

## Anti-Rationalization

| Excuse | Why it's wrong |
|--------|---------------|
| "I should just fix this while I'm here" | No. Your job is to report. Use `/forge-qa` for fixes. |
| "This bug is obvious, I don't need a screenshot" | Every issue needs evidence. No exceptions. |
| "The source code explains the bug" | Users don't read source code. Describe what they see. |
| "I'll skip the console check, it's probably fine" | Check it. Silent errors are still bugs. |

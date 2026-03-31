---
name: forge-retro
description: Use for weekly engineering retrospectives. Analyzes commit history, per-author breakdowns, work patterns, code quality metrics, with praise and growth areas. Tracks trends across retro runs. Triggers on "weekly retro", "what did we ship", "engineering retrospective".
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# Weekly Retrospective

Analyze what the team shipped, how the work happened, and where to improve. Evidence-based, specific, and candid. No generic praise. No coddling.

## Arguments

- `/forge-retro` — last 7 days (default)
- `/forge-retro 14d` — last 14 days
- `/forge-retro 30d` — last 30 days

## Step 1: Gather Raw Data

Identify the current user:

```bash
git config user.name
git config user.email
```

That name is "you." All other authors are teammates.

Run in parallel (use `origin/<base>` for all queries):

```bash
# Commits with stats
git log origin/<base> --since="<window>" --format="%H|%aN|%ae|%ai|%s" --shortstat

# Per-commit test vs prod LOC
git log origin/<base> --since="<window>" --format="COMMIT:%H|%aN" --numstat

# Session detection timestamps
git log origin/<base> --since="<window>" --format="%at|%aN|%ai|%s" | sort -n

# Hotspot files
git log origin/<base> --since="<window>" --format="" --name-only | grep -v '^$' | sort | uniq -c | sort -rn

# PR numbers, per-author hotspots, per-author summary
git log origin/<base> --since="<window>" --format="%s" | grep -oE '[#!][0-9]+' | sort | uniq
git log origin/<base> --since="<window>" --format="AUTHOR:%aN" --name-only
git shortlog origin/<base> --since="<window>" -sn --no-merges
find . -name '*.test.*' -o -name '*.spec.*' -o -name '*_test.*' 2>/dev/null | grep -v node_modules | wc -l
```

## Step 2: Compute Metrics

```
Summary Table
═════════════
Commits to main:    N
Contributors:       N
PRs merged:         N
Total insertions:   N
Total deletions:    N
Net LOC added:      N
Test LOC ratio:     N%
Active days:        N
Detected sessions:  N
Avg LOC/session-hr: N
```

Show per-author leaderboard (you first, sorted by commits desc):

```
Contributor         Commits   +/-          Top area
You (name)               32   +2400/-300   src/
teammate                 12   +800/-150    tests/
```

## Step 3: Time & Session Patterns

Hourly histogram in local time. Peak hours, dead zones, late-night clusters (>10pm).

Detect sessions with 45-minute gap threshold. Classify: Deep (50+ min), Medium (20-50 min), Micro (<20 min). Report total active time, avg session length, LOC per hour.

## Step 4: Work Patterns

Commit type breakdown by conventional prefix:

```
feat:     20  (40%)  ████████████████████
fix:      27  (54%)  ███████████████████████████
refactor:  2  ( 4%)  ██
```

Flag if fix ratio exceeds 50% (ship fast, fix fast pattern). Hotspot analysis: top 10 files. Flag files changed 5+ times.

## Step 5: Team Member Analysis

For each contributor (including you): commits, LOC, test ratio, areas of focus, commit type mix, session patterns, biggest ship.

**For you:** Full deep-dive. First person.

**For each teammate:**
- **Praise** (1-2 things, anchored in commits): "Shipped auth rewrite in 3 sessions with 45% test coverage."
- **Growth area** (1 thing, framed as investment): "Test ratio was 12%. Adding coverage to payment module would pay off."

If solo repo, skip team breakdown.

## Step 6: Week-over-Week Trends

Load prior retro from `.forge/retros/`. Compare key metrics:

```
                Last        Now         Delta
Test ratio:     22%    →    41%         +19pp
Sessions:       10     →    14          +4
LOC/hour:       200    →    350         +75%
Fix ratio:      54%    →    30%         -24pp (improving)
```

If no prior retro exists: "First retro recorded. Run again next week to see trends."

## Step 7: Narrative

### Summary Table + Trends
From Steps 2 and 6. If no prior retro: "First retro recorded. Run again next week for trends."

### Time & Sessions + Shipping Velocity
From Steps 3-4. Patterns, commit type mix, hotspot analysis.

### Your Week + Team Breakdown
From Step 5. Personal deep-dive + per-teammate praise and growth. Skip team if solo.

### Top 3 Wins + 3 Things to Improve + 3 Habits
Wins: highest-impact. Improve: actionable, anchored in commits. Habits: <5 min each.

## Step 8: Save

```bash
mkdir -p .forge/retros
```

Save report to `.forge/retros/{date}.md`. Append trends to `.forge/retros/trends.jsonl`:

```json
{"date":"2026-03-30","commits":47,"insertions":3200,"deletions":800,"test_ratio":0.41,"sessions":14,"fix_pct":0.30,"contributors":3}
```

## Anti-Rationalization

"We didn't do much this week" → Even small weeks have patterns. "Numbers scare me" → They're neutral. "Retros waste time" → 5 minutes of reflection saves hours of repeated mistakes.

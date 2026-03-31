---
name: forge-docs
description: Use after shipping to sync all project docs with what was just shipped. Reads current docs, cross-references the diff, updates README/ARCHITECTURE/CONTRIBUTING/CHANGELOG, cleans up stale TODOs/FIXMEs. Triggers on "update docs", "sync documentation", "post-ship docs".
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Grep
  - Glob
---

# Post-Ship Documentation Sync

Run after `/forge-ship` creates a PR but before it merges. Your job: ensure every doc file is accurate, up to date, and matches what shipped.

Make obvious factual updates directly. Stop only for risky or subjective decisions.

**Never stop for:** Factual corrections from the diff, updating paths/counts/versions, fixing stale cross-references, CHANGELOG voice polish, marking TODOs complete.

**Never do:** Overwrite or regenerate CHANGELOG entries (polish wording only), bump VERSION without asking, use Write on CHANGELOG.md (always use Edit).

## Step 1: Diff Analysis

1. Check current branch. On base branch? "Run from a feature branch." Stop.

2. Gather what changed:
```bash
git diff <base>...HEAD --stat
git log <base>..HEAD --oneline
git diff <base>...HEAD --name-only
```

3. Discover docs: `find . -maxdepth 2 -name "*.md" -not -path "./.git/*" -not -path "./node_modules/*" -not -path "./.forge/*" | sort`

4. Classify changes: new features, changed behavior, removed functionality, infrastructure.

## Step 2: Per-File Audit

Read each doc and cross-reference against the diff.

**README.md:** All features described? Install instructions current? Examples valid?
**ARCHITECTURE.md:** Diagrams match code? Be conservative, only update contradicted by diff.
**CONTRIBUTING.md:** Setup instructions work as a new contributor? Each step succeeds?
**CLAUDE.md / project instructions:** Project structure matches file tree? Commands accurate?
**Other .md:** Read, determine purpose, check against diff.

Classify each update:
- **Auto-update:** Factual corrections clearly from the diff (paths, counts, table entries).
- **Ask user:** Narrative changes, section removal, security model, large rewrites (>10 lines).

## Step 3: Apply Auto-Updates

Use Edit tool for all changes. One-line summary per file: "README.md: added new command to usage table, updated count from 9 to 10."

Never auto-update: README introduction, architecture philosophy, security model descriptions, entire section removals.

## Step 4: Ask About Risky Changes

For each risky update identified in Step 2, present to user with context and options:
- A) Apply the change
- B) Skip — leave as-is
- C) Let me tell you what I want instead

## Step 5: CHANGELOG Voice Polish

**NEVER CLOBBER CHANGELOG ENTRIES.** Polish wording only.

1. Read entire CHANGELOG first.
2. Only modify wording within existing entries. Never delete, reorder, or replace.
3. Use Edit with exact `old_string` matches. Never use Write on CHANGELOG.md.
4. Entry looks wrong? Ask user. Don't silently fix.

Voice: "Would a user think 'oh nice, I want to try that'?" Lead with what users can DO, not implementation. Skip if CHANGELOG wasn't modified on this branch.

## Step 6: Cross-Doc Consistency

1. Does README's feature list match CLAUDE.md?
2. Does ARCHITECTURE match CONTRIBUTING's project structure?
3. Does CHANGELOG's latest version match VERSION file?
4. Is every doc reachable from README or CLAUDE.md?
5. Flag contradictions. Auto-fix factual ones. Ask about narrative ones.

## Step 7: TODO/FIXME Cleanup

Scan the diff for `TODO`, `FIXME`, `HACK`, `XXX` comments. For meaningful deferred work (not trivial inline notes), ask if it should be tracked.

Check if open TODO items in project docs are completed by the diff. If clearly done, mark complete.

## Step 8: Commit

Stage modified docs by name (never `git add -A`). Commit: `git commit -m "docs: update project documentation for vX.Y.Z.W"`. Push: `git push`.

## Anti-Rationalization

| Excuse | Why it's wrong |
|--------|---------------|
| "Docs are boring, skip it" | Stale docs create confusion. Confusion wastes time. Update them now. |
| "The CHANGELOG is fine" | A CHANGELOG written by a machine reads like one. Polish it to read like a human wrote it. |
| "Nobody reads ARCHITECTURE.md" | New contributors read it. Onboarding failures cost days. |

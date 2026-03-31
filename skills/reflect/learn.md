---
name: forge-learn
description: Use to manage project learnings across sessions. Record patterns, pitfalls, preferences, and discoveries. Search past learnings, prune stale entries, export for documentation. Triggers on "what have we learned", "show learnings", "prune learnings", "add learning".
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
---

# Learning Persistence

Capture what you learn so future sessions don't repeat the same mistakes or miss the same patterns.

## Storage

Learnings live in `.forge/learnings/{project-slug}.jsonl`. Each line:

```json
{"timestamp":"2026-03-30T19:00:00Z","type":"pattern","context":"What we were doing","learning":"What we learned","action":"What to do differently","confidence":"high"}
```

### Types

- **pattern** — A reusable approach that worked well
- **pitfall** — A mistake to avoid
- **preference** — A user-stated preference or convention
- **discovery** — A non-obvious insight about the codebase

### Confidence

- **high** — Verified by testing or user confirmation
- **medium** — Observed pattern, likely correct
- **low** — Hypothesis, needs validation

## Operations

### ADD

Gather: type, context, learning, action, confidence. Append to `.forge/learnings/{slug}.jsonl`:

```bash
mkdir -p .forge/learnings
echo '{"timestamp":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","type":"TYPE","context":"CTX","learning":"LRN","action":"ACT","confidence":"CONF"}' >> .forge/learnings/{slug}.jsonl
```

### SEARCH

Find relevant past learnings:

```bash
grep -i "QUERY" .forge/learnings/{slug}.jsonl
```

Present matches grouped by type. Show context, learning, and action for each.

If the user asks "didn't we fix this before?" or "have we seen this pattern?", search learnings automatically.

### PRUNE

Remove stale or disproven entries.

1. **File existence check:** If a learning references files, check they still exist. Flag deleted files.
2. **Contradiction check:** Look for same context with different or opposite learning. Flag conflicts.
3. **Staleness check:** Low-confidence entries older than 30 days. Flag for review.

Present each flagged entry:
- A) Remove
- B) Keep
- C) Update

For removals, remove the matching line from the JSONL file. For updates, append a new entry (append-only, latest wins).

### EXPORT

Export learnings as markdown for project documentation:

```markdown
## Project Learnings

### Patterns
- **[context]**: [learning] → [action]

### Pitfalls
- **[context]**: [learning] → [action]

### Preferences
- **[context]**: [learning]

### Discoveries
- **[context]**: [learning] → [action]
```

Ask if user wants to append to CLAUDE.md or save as a separate file.

## Auto-Capture

Other Forge skills can log learnings automatically. When `/forge-review`, `/forge-retro`, or `/forge-cso` discovers a non-obvious pattern or pitfall, they append to this file.

## Anti-Rationalization

| Excuse | Why it's wrong |
|--------|---------------|
| "I'll remember this" | You won't. Next session starts fresh. Write it down. |
| "This is too obvious to log" | Obvious to you now. Not obvious to you in 3 weeks after 50 other sessions. |
| "The learnings file is getting long" | That's a feature, not a bug. Prune stale entries, don't stop recording. |

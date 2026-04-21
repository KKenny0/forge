---
name: taku-reflect
description: >
  User-invoked reflection. Three modes: Learn (record user-approved patterns, pitfalls,
  preferences, discoveries), Retro (weekly engineering retrospective with git commit analysis,
  metrics, team breakdowns, trends), and Write Skill (codify recurring learnings into reusable skills).
  Triggers on "what have we learned", "add learning", "show learnings", "weekly retro",
  "what did we ship", "engineering retrospective", "write a skill", "create a skill",
  or "codify this pattern".
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
---

# Reflect — Learn + Retro + Write Skill

Three modes: capture learnings (default), weekly retrospective, or codify recurring patterns into skills.

## Mode Selection

- **Learn** (default): "what have we learned", "add learning", "show learnings", "prune learnings"
- **Retro**: "weekly retro", "what did we ship", "retrospective", or `--retro` flag
- **Write Skill**: "write a skill", "create a skill", "codify this pattern", "edit this skill"

---

## Learn Mode

Capture only what the user explicitly wants to preserve so future sessions can reuse it.

### Invocation Rule

`/taku-reflect` is manual. Do not create or update long-term learnings unless the user explicitly invokes reflect.

### Storage

Learnings live in `.taku/learnings/{project-slug}.jsonl`. Each line:

```json
{"id":"L2026-04-21-001","timestamp":"2026-04-21T12:00:00Z","type":"preference","context":"Multi-file repository change","learning":"User prefers plan-first before non-trivial edits","action":"Start with code reading and short execution plan","confidence":"high","apply_when":{"task_types":["feature","refactor","bugfix"],"keywords":["multi-file","plan","design"]},"status":"active"}
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

### Required Fields

- `id` — Stable identifier for reference and deduplication
- `timestamp` — ISO8601 UTC timestamp
- `type` — `pattern|pitfall|preference|discovery`
- `context` — What work this came from
- `learning` — The reusable takeaway
- `action` — What future sessions should do
- `confidence` — `high|medium|low`
- `apply_when.task_types` — Zero or more of `feature|bugfix|refactor|hotfix|review|idea`
- `apply_when.keywords` — Simple keyword hooks for later recall
- `status` — `active|stale`

### Operations

**ADD:** Gather `type`, `context`, `learning`, `action`, `confidence`, and a minimal `apply_when` block. Append to JSONL only after the user confirms the learning should be kept.

**SEARCH:** `grep -i "QUERY" .taku/learnings/{slug}.jsonl`. Present matches grouped by type.

**PRUNE:** Check file existence, contradictions, staleness (30 days). Present each flagged entry: Remove / Keep / Update.

**EXPORT:** Convert to markdown. Offer to append to `AGENTS.md` or `CLAUDE.md` only when the user confirms an upgrade.

**Why JSONL over markdown:** JSONL entries can be searched with grep, parsed programmatically, and deduplicated. Markdown learnings files become unstructured text that's hard to query or prune.

### Auto-Recall

Other Taku phases may search existing learnings automatically, but only as context:

- Search after task classification and before PLAN, BUILD, REVIEW, and TEST
- Filter by task type and simple keyword overlap
- Prefer `high` confidence, then `medium`
- Show at most 3-5 relevant learnings

This recall must never create, edit, or prune learnings. Long-term memory changes happen only inside `/taku-reflect`.

### Output Format

When running learn mode, organize results as:

- **Recorded** — learnings added or updated in this reflect run
- **Relevant Existing Learnings** — prior entries relevant to the current work
- **Promotion Suggestions** — suggestions only; do not upgrade anything automatically

---

## Retro Mode

Analyze what the team shipped, how the work happened, and where to improve. Evidence-based, specific, candid.

### Arguments

- `/taku-reflect` — learn mode (default)
- `/taku-reflect --retro` — last 7 days
- `/taku-reflect --retro 14d` — last 14 days
- `/taku-reflect --retro 30d` — last 30 days

### Step 1: Gather Raw Data

```bash
git config user.name && git config user.email
git log origin/<base> --since="<window>" --format="%H|%aN|%ae|%ai|%s" --shortstat
git log origin/<base> --since="<window>" --format="COMMIT:%H|%aN" --numstat
git log origin/<base> --since="<window>" --format="" --name-only | grep -v '^$' | sort | uniq -c | sort -rn
git shortlog origin/<base> --since="<window>" -sn --no-merges
```

### Step 2: Compute Metrics

Summary: commits, contributors, PRs, insertions, deletions, net LOC, test LOC ratio, active days, sessions, avg LOC/session-hr. Per-author leaderboard sorted by commits.

### Step 3: Time & Session Patterns

Hourly histogram. Detect sessions (45-min gap). Classify: Deep (50+ min), Medium (20-50), Micro (<20).

### Step 4: Work Patterns

Commit type breakdown by conventional prefix. Flag fix ratio > 50%. Hotspot analysis: top 10 files. Flag files changed 5+ times.

### Step 5: Team Member Analysis

For each contributor: commits, LOC, test ratio, areas, biggest ship.
**Praise** (anchored in commits): 1-2 things. **Growth area** (framed as investment): 1 thing.

### Step 6: Week-over-Week Trends

Load prior retro from `.taku/retros/`. Compare key metrics.

### Step 7: Narrative

Output: Summary table + trends, Time & sessions, Your week + team, Top 3 Wins + 3 Improvements + 3 Habits.

### Step 8: Save

Save to `.taku/retros/{date}.md`. Append trends to `.taku/retros/trends.jsonl`.

---

## Write Skill Mode

Codify recurring patterns into reusable skills, but only after the user confirms they want to write one.

Full process in `references/writing-skills.md`. Load it and follow the instructions.

Quick summary:
- Choose skill type: TECHNIQUE (concrete method), PATTERN (mental model), REFERENCE (lookup table)
- Follow RED-GREEN-REFACTOR: baseline test → write minimal skill → close loopholes
- Keep under 500 lines; split to `references/` if needed
- Description field: triggering conditions only, never summarize workflow

### Promotion Paths

Keep upgrades narrow. Only suggest these two:

1. **Project-level constraint candidate**
   - Condition: `type=preference`, `confidence=high`, repeated or confirmed 2+ times
   - Suggestion: propose upgrading the preference into `AGENTS.md` if present, otherwise `CLAUDE.md`
   - Rule: never write the file automatically; ask the user first

2. **Write Skill candidate**
   - Condition: the same pattern, pitfall, or decision method recurs across 2-3 sprints
   - Suggestion: `This pattern keeps recurring. Suggest codifying it as a skill.`
   - Rule: ask the user whether to proceed before loading `references/writing-skills.md`

---

## Anti-Rationalization

| Excuse | Why it's wrong |
|--------|---------------|
| "I'll remember this" | You won't. Next session starts fresh. Write it down. |
| "This is too obvious to log" | Obvious now. Not obvious in 3 weeks after 50 other sessions. |
| "We didn't do much this week" | Even small weeks have patterns worth examining. |
| "Retros waste time" | 5 minutes of reflection saves hours of repeated mistakes. |

## Known Pitfalls

**Learnings file becomes a dumping ground.** Over 30 sessions, 200+ entries. Most trivial. Signal buried in noise.

*Prevention:* Use PRUNE regularly. Every 30 days, remove trivial observations, update stale patterns, delete low-confidence entries. 30 high-quality insights > 200 entries of noise.

**Retro becomes a vanity metric exercise.** "142 commits, 8,400 lines." But 6,000 were generated code and 40 were auto-bumps.

*Prevention:* Step 4 computes commit type breakdown and flags fix ratio. Note when metrics are inflated. Value is in analysis, not numbers.

**Saving learnings but never searching them.** 50 learnings recorded, none referenced. Team repeated the same mistake 3 times.

*Prevention:* Auto-search relevant learnings in later phases as context. Query the knowledge base, don't just write to it.

**Auto-upgrading without consent.** A repeated preference was detected and silently written into a project rule file. The user disagreed with the wording and had to undo it.

*Prevention:* Promotion Suggestions are suggestions only. Upgrades to `AGENTS.md`, `CLAUDE.md`, or a new skill always require explicit user confirmation first.

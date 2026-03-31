---
name: forge-design
description: >
  Use when starting a new project or feature that needs a design system — brand identity,
  typography, color, spacing, layout, and motion decisions. Triggers on "design system",
  "brand", "visual identity", "design tokens", "make it look good", or when the design
  phase of the sprint needs aesthetic direction before planning.
---

# forge-design — Design System Creation

A 6-phase pipeline that takes a product idea and produces a concrete design system. Not a mood board. A specification the implementer can build from.

## Why This Matters

"Clean modern UI" is not a design decision. Neither is "we'll polish it later." Vague aesthetic direction produces generic AI-slop interfaces that look like every other SaaS landing page. This skill forces specificity: exact tokens, exact spacing, exact hierarchy. The output is a DESIGN.md section the rest of the sprint builds against.

## Phase 1: Product Context

Before touching anything visual, understand what you're designing FOR.

Gather from the user (or infer from existing docs):
- **Target audience:** Who uses this? Age, technical skill, context of use.
- **Core emotion:** What should the user FEEL when using this product? (Trust? Speed? Delight? Calm?)
- **Competitive set:** 3-5 products the user admires visually. Name them.
- **Anti-patterns:** What should this NOT look like? What does the user hate?
- **Constraints:** Dark mode only? RTL support? Accessibility requirements?

If the user hasn't thought about this, help them think. Use AskUserQuestion with concrete options, not open-ended "tell me about your brand."

Output: A 5-10 line product context block. This anchors every subsequent decision.

## Phase 2: Competitive Research

Use web_search to study what exists. This isn't copying — it's calibration.

Search for:
- Each competitor's design language (typography, color, spacing habits)
- Current design trends in the product's category (2025-2026)
- Accessibility standards relevant to the product type

For each competitor, note:
- One thing they do well (steal the principle, not the pixel)
- One thing they do poorly (avoid the trap)

Output: A competitive summary table. 3-5 rows. What you learned, what you're avoiding.

## Phase 3: Full Design Proposal

This is the core. Produce a design system with these sections:

### Aesthetic Direction
One paragraph describing the visual personality. Not "clean and modern." Something specific: "Warm minimalism with sharp typographic hierarchy. Feels like a well-edited magazine, not a tech dashboard."

### Typography
- **Primary typeface:** Name, weight, size scale (e.g., 14/16/20/28/36/48px)
- **Secondary typeface:** If different from primary, explain why
- **Heading/body contrast ratio:** Minimum 1.5x size difference
- **Line height:** Body (1.5-1.6), headings (1.1-1.2)
- **Letter spacing:** Headings (-0.02em to -0.04em), body (0), labels (0.02-0.05em)

No default font stacks. No Inter, Roboto, or system-ui as primary identity font. Pick something with character.

### Color System
Define as CSS custom properties:
```
--color-bg-primary
--color-bg-secondary
--color-bg-elevated
--color-text-primary
--color-text-secondary
--color-text-muted
--color-accent
--color-accent-hover
--color-border
--color-success
--color-warning
--color-error
```

Include: exact hex values, dark mode variants, contrast ratios (WCAG AA minimum).

### Spacing Scale
Base unit (4px or 8px) and the scale: `4 8 12 16 24 32 48 64 96`. Name them if the project has conventions.

### Layout Grid
- Max content width
- Column count and gutters
- Responsive breakpoints with layout behavior per breakpoint (not "stacked on mobile")

### Motion
- Transition duration scale (e.g., 150ms/300ms/500ms)
- Easing curves (name them: `ease-out` for entries, `ease-in` for exits)
- When to animate vs. when to be instant
- Respect `prefers-reduced-motion`

## Phase 4: SAFE/RISK Breakdown

For every design decision, classify it:

| Decision | SAFE (proven pattern) | RISK (untested) | Why |
|----------|----------------------|-----------------|-----|
| Color palette | Dark bg, high contrast text | Vibrant accent color | Category expects calm; accent is brand bet |

SAFE decisions can ship immediately. RISK decisions need validation — user testing, A/B, or at minimum a second opinion.

If more than 3 decisions are RISK, simplify. Too many untested bets at once guarantees some fail.

## Phase 5: Design Preview (Optional, Enhanced)

If image generation is available, create a visual preview of the design system:

Use image_generate to produce:
1. A **component showcase** — buttons, cards, inputs, headings at different sizes on the chosen background
2. A **sample page** — homepage or key screen using the design system

This makes the abstract concrete. The user sees what "warm minimalism with sharp typographic hierarchy" actually looks like.

If image generation is unavailable, skip this phase. The text spec is sufficient.

## Phase 6: Write DESIGN.md

Append a `## Design System` section to the project's DESIGN.md (or create one if it doesn't exist).

Format:
```markdown
## Design System

### Context
[Product context from Phase 1]

### Competitive Notes
[Summary from Phase 2]

### Typography
[Spec from Phase 3]

### Color
[CSS variables from Phase 3]

### Spacing
[Scale from Phase 3]

### Layout
[Grid from Phase 3]

### Motion
[Spec from Phase 3]

### Risk Register
[SAFE/RISK table from Phase 4]
```

Every subsequent skill in the sprint (plan, build, review, test) reads this section. It's the source of truth for "what does good look like."

## Completion

Output: DESIGN.md with a complete design system section. Every token specified, no placeholders, no "TBD."

Status: DONE when all sections are filled with concrete values. DONE_WITH_CONCERNS if RISK items exceed 3 or image preview revealed problems. BLOCKED if user can't provide product context.

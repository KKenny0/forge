🧵 1/

AI can write code. But can it ship reliable software?

Most AI coding workflows skip design, skip tests, and skip review. The result? Code that "should work" but doesn't.

I built Forge to fix this — a structured 7-phase sprint framework for AI-assisted development.

2/

Think → Plan → Build → Review → Test → Ship → Reflect

7 phases. Each with dedicated skills, iron-clad rules, and evidence-based gates.

The AI can't skip steps. Can't fake completions. Can't rationalize shortcuts.

3/

It starts with Think — before a single line of code.

6 forcing questions reframe your problem (inspired by YC office hours). Then Socratic design refinement until YOU approve.

No design, no code. Period.

4/

The Build phase is where it gets powerful.

/forge-build assigns each task to an independent subagent — running in parallel.

3 tasks? 3x speed. Git worktree isolation keeps everything clean.

5/

AI reviewing its own code is not a review.

Forge does triple-layer quality gates:
→ Pattern-based code review with auto-fix
→ Cross-model second opinion (different AI reviews your code)
→ Before/after visual QA with screenshots

6/

TDD isn't optional in Forge. It's enforced.

RED → GREEN → REFACTOR. Every time.

Plus: 14-phase security audit (OWASP + STRIDE), systematic root-cause debugging, and a "3 failed fixes = stop and rethink architecture" rule.

7/

The "3 strikes" rule is my favorite.

If AI fails to fix a bug 3 times, it MUST stop coding and question the architecture. Because sometimes the code isn't wrong — the design is.

No more infinite fix loops.

8/

Forge works on both Claude Code and OpenClaw. Same sprint, same skills, zero compromise.

30 skills covering everything from product thinking to production deployment. Use them all or pick what you need.

9/

Built on the shoulders of two incredible open-source projects:

→ Superpowers by Jesse Vincent — engineering discipline, TDD, evidence-based completion
→ gstack by Garry Tan — product thinking, QA methodology, parallel sprint architecture

MIT licensed. Open source.

10/

Forge is live on GitHub.

star it, fork it, ship with it.

👉 https://github.com/KKenny0/forge

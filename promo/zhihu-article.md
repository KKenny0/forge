# 为什么 AI 写代码总是「差点意思」——我做了个开源框架来解决

> 一个融合了 YC 合伙人和资深工程师方法论的开发 Sprint 框架：Forge。

## 0. 先说结论

过去半年，我一直在用 AI 辅助编程。用过 Cursor、Claude Code、Copilot，也搭过自己的 agent 工作流。一个越来越明显的感受是：**AI 写代码的能力已经不是瓶颈，瓶颈在于流程。**

具体来说，三个问题反复出现：

1. **AI 太急了。** 给个 prompt，它直接开写。没有需求澄清，没有设计讨论，没有边界定义。200 行代码生成出来，跑是能跑，但不是你想要的。
2. **AI 太自信了。** 「我已经修复了这个问题」「功能已完成」。但实际上测试没跑、边界没覆盖、安全没审计。它用「应该能工作」替代了「我验证过它能工作」。
3. **AI 太孤单了。** 自己写代码，自己 review，自己测试。没有对抗性的质量把关，等于没有 review。

这些问题不是某个工具的 bug，而是**整个 AI 编程生态缺乏方法论**。大家都在造更好的模型、更快的编辑器，但很少有人认真想：**AI 辅助开发应该遵循什么样的工程纪律？**

这就是 Forge 想解决的问题。

## 1. Forge 是什么

Forge 是一个开源的 **AI 辅助开发 Sprint 框架**，提供结构化的 7 阶段流水线：

```
Think → Plan → Build → Review → Test → Ship → Reflect
```

它不是一个编辑器插件，不是一个模型 wrapper，而是一套**方法论 + 工具链**，让 AI agent 在开发过程中遵循严格的工程纪律。

Forge 的核心理念来自两个优秀的开源项目：

- **[Superpowers](https://github.com/obra/superpowers)**（Jesse Vincent）—— TDD 强制执行、系统性调试、证据驱动的完成标准。工程师视角的纪律框架。
- **[gstack](https://github.com/garrytan/gstack)**（Garry Tan）—— YC office hours 式的产品思考、QA 方法论、并行 sprint 架构。创业者视角的产品框架。

Forge 把两者的精华融合成统一的 skill pack，同时支持 Claude Code 和 OpenClaw 两个平台。

## 2. 七个阶段，每个都不含糊

### Think：先想清楚为什么

大多数 AI 编程的失败，不是 AI 写不出代码，而是**写了一堆不需要的代码**。

Forge 的 Think 阶段有两道关卡：

**第一道：Office Hours（`/forge-office-hours`）**

灵感来自 YC 的 office hours。6 个 forcing questions：

1. 这个功能解决的真实问题是什么？
2. 用户现在怎么解决这个问题？痛点在哪？
3. 如果只能保留一个功能点，是哪个？
4. 什么指标能证明这个功能成功了？
5. 最小可行版本是什么？
6. 什么情况下我们不应该做这个？

这些问题不是摆设。AI 必须逐个回答，你逐个审批。目标是**在写任何代码之前，确保 AI 理解了你要解决的问题**。

**第二道：Brainstorm（`/forge-brainstorm`）**

苏格拉底式的设计打磨。AI 提出方案，你质疑，AI 改进，你再质疑。来回迭代，直到设计达到你的标准。

关键约束：**必须你亲自 approve 才能进入下一步。** AI 不能自己觉得「设计够了」就开写。

### Plan：把设计变成可执行的蓝图

设计定了，接下来是 Plan 阶段：

1. **CEO Review（`/forge-ceo-review`）**—— 重新审视问题，问「这是 10 星产品还是 3 星产品？」
2. **Eng Review（`/forge-eng-review`）**—— 锁定架构、数据流、边界情况
3. **Design Review（`/forge-design-review`）**—— 对设计维度打分（0-10），低于 7 的必须改进
4. **Writing Plans（`/forge-plan`）**—— 把设计拆成 bite-sized 任务，每个任务精确到文件路径、完整代码、TDD 步骤

Plan 阶段的产出是一份 PLAN.md，每个任务都有明确的输入、输出和验收标准。没有「后续再补充」的 placeholder。

### Build：并行 Sprint，效率翻倍

Build 阶段是 Forge 的杀手锏。

`/forge-build` 的核心机制：**每个任务分配一个独立 subagent，并行开发**。

```
任务 A ──→ subagent-1 ──→ 完成
任务 B ──→ subagent-2 ──→ 完成
任务 C ──→ subagent-3 ──→ 完成
                          ↓
                    统一 merge & review
```

如果你有 3 个独立任务，传统方式是串行执行（A 完成后开始 B，B 完成后开始 C）。Forge 的并行 sprint 让它们同时跑，理论加速比接近 N（任务数）。

每个 sprint 在独立的 Git worktree 中工作（`/forge-worktree`），互不干扰。代码写完后统一进入 review 阶段。

### Review：三重质量把关

AI 自己审自己的代码，等于没有 review。Forge 的 Review 阶段是**系统化的对抗性审查**：

1. **`/forge-review`** —— 基于 pattern 的自动化 review。检查 SQL 注入风险、LLM 调用边界、错误处理完整性等。发现问题直接修复，不是只提建议。
2. **`/forge-cross-review`** —— 换一个 AI 模型给 second opinion。比如用 Claude 写的代码让 GPT 来审，避免单一模型的认知盲区。
3. **`/forge-visual-review`** —— 对 UI 变化做截图对比（before/after），视觉层面的 QA。

每一层 review 都有自己的标准，发现问题必须修复后才能通过。

### Test：测试不是选配

Forge 里，TDD 是硬约束，不是建议：

- **`/forge-tdd`** 强制 RED-GREEN-REFACTOR 循环。先写失败的测试，再写代码让测试通过，最后重构。
- **`/forge-qa`** 执行完整的「测试 → 找 bug → 修复 → 验证」闭环，带健康评分。
- **`/forge-cso`** 做 14 阶段安全审计，覆盖 OWASP Top 10 + STRIDE 威胁建模。
- **`/forge-debug`** 遇到 bug 不是上来就改，而是先做 4 阶段根因调查。**连续修 3 次没好就停下来，重新审视架构。**

最后一句话很重要。AI 的一个典型问题是：修一个 bug 引入两个新 bug，然后继续修新 bug，陷入无限循环。Forge 的「三击出局」规则强制 AI 停下来思考：**不是代码有问题，是架构有问题。**

### Ship：一键上线

`/forge-ship` 封装了完整的发布流水线：跑测试 → code review → bump 版本 → 生成 changelog → push → 创建 PR。

`/forge-deploy` 负责 merge 后的部署：触发 CI → 部署 → 验证生产环境健康。

不是让你手动跑十几个命令，而是一条指令走完全流程。

### Reflect：持续进化

`/forge-retro` 做每周回顾，追踪趋势（代码质量是上升还是下降？bug 修复时间是否在增加？）。

`/forge-learn` 确保经验跨 session 持久化——AI 从上次 sprint 中学到了什么，下次不应该犯什么错。

## 3. 几个关键设计决策

### 铁律与反合理化

Forge 最大的设计亮点之一是**反合理化机制**。

AI agent 有一个天然的倾向：当某个步骤很难或很耗时，它会找理由跳过。「这个场景太简单了不需要 TDD」「测试覆盖率已经很高了不需要再测」「这个改动很小不需要 review」。

Forge 用「铁律」（Iron Laws）和「红旗表」（Red Flags Tables）来对抗这种倾向：

- 铁律是不可违反的规则。违反 = sprint 失败。
- 红旗表列出了 AI 可能用来合理化跳步的所有借口，每个借口都有对应的反驳。

这不是不信任 AI，而是承认 AI 和人类一样会偷懒。流程的价值就在于防止偷懒。

### 证据驱动

Forge 里的每一个「完成」声明都需要证据：

- 「测试通过了」→ 贴测试输出
- «代码 review 通过了» → 贴 review 结果
- «功能完成了» → 贴运行截图

"It should work" 永远不是可接受的完成声明。

### 平台无关

Forge 同时支持 Claude Code 和 OpenClaw。同一套 skill，同一套流程，零妥协。

平台适配层（`platform/openclaw.md`）自动处理工具差异。开发者不需要关心底层是 `exec` 还是 `Bash`，是 `read` 还是 `Read`。

核心功能零依赖，开箱即用。浏览器 QA、跨模型 review 等增强能力按需开启。

## 4. 怎么用

### Claude Code

```bash
git clone https://github.com/KKenny0/forge.git ~/.claude/skills/forge
```

然后在 Claude Code 中：

```
/forge-build-me-a-dashboard
```

Forge 会自动检测项目状态，从合适的阶段开始。如果项目没有 DESIGN.md，从 Think 开始；如果有设计但没计划，从 Plan 开始；如果一切就绪，直接 Build。

### OpenClaw

```bash
# 即将上线 ClawHub
openclaw skills install forge
```

### 日常使用

大多数时候，你只需要告诉 Forge 你想做什么：

- 「帮我做个用户仪表盘」→ 自动走完 Think → Plan → Build → Review → Test → Ship
- 「登录页有个 bug」→ 自动分类为 bugfix，走 Test → Build → Review → Ship
- 「review 一下这个 PR」→ 直接进入 Review 阶段
- 「上线」→ 直接走 Ship 流水线

Forge 会根据你的描述自动分类任务类型，选择最合适的阶段组合。

## 5. 30 个 Skill，完整覆盖

Forge 包含 30 个独立 skill，按阶段组织：

| 阶段 | Skill 数量 | 核心能力 |
|------|-----------|---------|
| Think | 3 | Office hours、设计打磨、设计系统创建 |
| Plan | 4 | CEO review、工程 review、设计打分、任务拆分 |
| Build | 4 | 并行开发、顺序执行、TDD、Git worktree |
| Review | 5 | Code review、跨模型 review、视觉 QA |
| Test | 5 | QA 闭环、安全审计、根因调查、完成验证 |
| Ship | 4 | 发布流水线、部署、分支管理、文档同步 |
| Reflect | 3 | 周回顾、持续学习、skill 编写 |

每个 skill 都是独立的、可组合的。你可以只用 `/forge-tdd` 来强制 TDD，也可以只用 `/forge-review` 来做 code review，不必跑完整个 sprint。

## 6. 不是替代，是增强

Forge 不替代你的 AI 编程工具。它不绑定某个模型、某个编辑器、某个平台。

它做的是**在 AI 和开发者之间加一层工程纪律**——确保 AI 在正确的时机做正确的事，用证据而非自信来证明工作完成。

如果你已经在用 Claude Code 或 OpenClaw 做 AI 辅助开发，Forge 让你的工作流从「碰运气」变成「有流程」。

## 7. 开源，欢迎贡献

Forge 基于 MIT 协议开源。

GitHub: **https://github.com/KKenny0/forge**

它站在 Superpowers 和 gstack 两个优秀项目的肩膀上。如果你也在做 AI 辅助开发，如果你也遇到过「AI 写代码但质量不可控」的问题，试试 Forge。

如果有想法、有建议、或者想贡献 skill，欢迎 PR。

---

*让 AI 不只是能写代码，而是能靠谱地交付软件。*

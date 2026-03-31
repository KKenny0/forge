# Forge — AI 辅助开发的完整 Sprint 框架

---

## Page 1: AI 写代码，但不写设计

[配图建议: 一张分屏对比图——左边是 AI 一口气生成 200 行代码但功能跑偏，右边是先画架构再写代码的有序流程]

AI 编程工具越来越强，但大多数人的用法是：给个 prompt，拿结果，祈祷能跑。

问题不在于 AI 不够聪明，而在于**流程缺失**——没有设计、没有 review、没有 TDD。Forge 的答案：结构化 sprint，让 AI 走完 Think → Plan → Build → Review → Test → Ship → Reflect 全流程。

---

## Page 2: 一个 Sprint，七个阶段

[配图建议: 一条从左到右的流水线图，每个阶段用不同颜色的方块标注，箭头连接，整体风格类似 CI/CD pipeline 可视化]

```
Think → Plan → Build → Review → Test → Ship → Reflect
```

不是简单的「写代码 → 跑测试 → 提 PR」。Forge 把整个开发过程拆成 7 个阶段，每个阶段有专属 skill、铁律约束和证据门禁。AI 不能跳步，不能伪造完成，不能用「应该能跑」糊弄过去。

---

## Page 3: 先想清楚，再动手

[配图建议: 一个白板/便利贴风格的图，上面有 6 个尖锐问题，其中一个被高亮放大]

Think 阶段不是走形式。`/forge-office-hours` 会问 6 个 forcing questions——「用户真正想要什么？」「如果只能做一个功能，是哪个？」——逼你和 AI 先对齐目标，再谈实现。

然后 `/forge-brainstorm` 用苏格拉底式对话打磨设计，**必须你亲自 approve 才能进入下一步**。没有设计，不写一行代码。

---

## Page 4: 并行 Sprint，速度翻倍

[配图建议: 一张类似 Git 分支图的动画截图，主分支分出 3 条并行分支，各自独立开发后合并]

`/forge-build` 是 Forge 的杀手锏：每个任务分配独立 subagent，**并行开发**。3 个任务同时跑，不是排队等一个做完再开始下一个。

配合 `/forge-worktree` 的 Git worktree 隔离，每个 sprint 在独立分支工作，互不干扰。完成后统一 merge、review、ship。

---

## Page 5: Review 不能只靠一个人

[配图建议: 一张代码 diff 截图，左边是原始代码标红，右边是修复后标绿，中间有一个 AI 头像在打勾]

Forge 的 Review 阶段是三重保险：

1. **`/forge-review`** — 基于 pattern 的自动化 code review，直接修问题
2. **`/forge-cross-review`** — 换一个 AI 模型给 second opinion，避免单一模型的盲区
3. **`/forge-visual-review`** — 截图对比 before/after，UI 变化一眼可见

不是「让 AI 自己审自己的代码」。是系统化的、有对抗性的质量把关。

---

## Page 6: 测试不是选配，是铁律

[配图建议: 一张终端截图风格图，显示 RED → GREEN → REFACTOR 的经典 TDD 循环，每个阶段用对应颜色标注]

Forge 里 TDD 不是建议，是硬约束：

- `/forge-tdd` 强制 RED-GREEN-REFACTOR 循环
- `/forge-qa` 执行「测试 → 找 bug → 修复 → 验证」的完整闭环，带健康评分
- `/forge-cso` 做 14 阶段安全审计，覆盖 OWASP + STRIDE
- `/forge-debug` 遇到 bug 先做根因调查，连续修 3 次没好就停下来重新审视架构

「它应该能跑」在 Forge 里不是完成声明。跑命令，贴输出，才叫完成。

---

## Page 7: 两个平台，一套流程

[配图建议: Claude Code 和 OpenClaw 的 logo 并排放置，中间用一个双向箭头连接，下方一行字「Same Sprint, Any Platform」]

Forge 同时支持 **Claude Code** 和 **OpenClaw**。

同一个 7-phase sprint，同一套 skill 体系，在不同平台上零妥协运行。平台适配层自动处理工具差异，开发者不需要关心底层实现。

核心功能零依赖，开箱即用。浏览器 QA、跨模型 review、安全审计作为可选增强能力，按需开启。

---

## Page 8: 开源，拿来就用

[配图建议: GitHub 页面截图，展示 Forge 仓库，下方有 Star 按钮和 Fork 按钮，风格简洁醒目]

Forge 基于 Jesse Vincent 的 Superpowers 和 Garry Tan 的 gstack 融合而成，MIT 开源协议。

30 个 skill，覆盖从产品思考到上线部署的完整链路。拿来即用，也欢迎贡献。

🔗 **GitHub:** https://github.com/KKenny0/forge

Star it. Fork it. Ship with it.

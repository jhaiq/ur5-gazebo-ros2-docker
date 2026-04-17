# 部署方案 A：生产环境全自动 - 安装完成报告

> 部署日期：2026-04-17  
> 部署状态：✅ 完成

---

## 📦 已安装组件

### 1. autonomous-dev-team（全自动开发流水线）
**状态**: ✅ 已安装

**Skills**:
- `autonomous-common` - 共享 Hooks 和脚本
- `autonomous-dev` - TDD 开发工作流
- `autonomous-dispatcher` - GitHub Issue 调度器
- `autonomous-review` - PR 自动评审
- `create-issue` - 结构化 Issue 创建

**位置**: `~/.openclaw/workspace/.agents/skills/autonomous-*/`

**Symlinks**:
- `hooks` → `.agents/skills/autonomous-common/hooks`
- `scripts-dispatcher` → `.agents/skills/autonomous-dispatcher/scripts`

**工作流**:
```
GitHub Issue (autonomous label) 
  → Dispatcher (5min cron) 
  → Dev Agent (worktree 隔离 + TDD) 
  → Review Agent (代码评审 + E2E) 
  → Auto Merge
```

**配置要求**:
- GitHub Personal Access Token
- GitHub 仓库 Labels 设置
- Cron 调度器配置

---

### 2. team-dev-agent（产品开发工作流）
**状态**: ✅ 已安装

**Skill**:
- `team-dev-agent` - 7 阶段产品开发流程

**位置**: `~/.openclaw/workspace/.agents/skills/team-dev-agent/`

**7 阶段流程**:
1. 架构设计（ARCHITECTURE.md）
2. 后端先行（DB → API → 业务逻辑）
3. 前端骨架（跑通为主）
4. 视觉优化（Codex 做 UI）
5. Bug Fix（测试通过）
6. 去硬编码（review_hardcode.sh）
7. 边界测试（4 轮测试）

**核心脚本**:
- `monitor_agent.sh` - 进程监控
- `review_hardcode.sh` - 硬编码扫描

**触发词**:
- `帮我开发`, `用 claude code 实现`, `用 codex 做前端`
- `开始做这个项目`, `帮我搭一个`, `写代码`

---

### 3. openclaw-pm V2（配置增强）
**状态**: ✅ 已配置

**健康检查脚本** (已复制到 `scripts/`):
- `gateway-health-check.sh` - Gateway 自动恢复
- `check-unanswered.sh` - 未回复消息检测
- `heartbeat-check.sh` - HEARTBEAT 统一检查
- `check-missed-crons.sh` - Cron 任务检查
- `morning-briefing.sh` - 晨间简报
- `quick-diagnose.sh` - 一键诊断

**AGENTS.md 增强**:
- ✅ 复杂任务强制流程（计划文件）
- ✅ 任务记录规则
- ✅ Session 隔离规则（最高优先级）
- ✅ GatewayRestart 强制行为
- ✅ 主动 Interview（需求澄清）
- ✅ 并行执行优化

---

## 🔧 配置检查清单

### autonomous-dev-team 配置

```bash
# 1. 设置 GitHub Labels
cd /path/to/your/repo
bash .agents/skills/autonomous-dispatcher/scripts/setup-labels.sh owner/repo

# 2. 配置 Dispatcher Cron（每 5 分钟）
*/5 * * * * cd /path/to/project && openclaw run skills/autonomous-dispatcher/SKILL.md

# 3. 创建测试 Issue
# 在 GitHub 创建 Issue，添加 "autonomous" label
```

### team-dev-agent 配置

```bash
# 1. 确保 Claude Code 已安装
npm install -g @anthropic-ai/claude-code

# 2. 确保 Codex 已安装（可选，前端优化用）
npm install -g @openai/codex

# 3. 测试触发
# 在 OpenClaw 中说："帮我开发一个登录功能"
```

### 健康检查配置

```bash
# 1. 测试脚本
~/.openclaw/workspace/scripts/quick-diagnose.sh

# 2. 设置晨间简报 Cron（每天 9:00）
0 9 * * * ~/.openclaw/workspace/scripts/morning-briefing.sh

# 3. 设置健康检查 Cron（每 30 分钟）
*/30 * * * * ~/.openclaw/workspace/scripts/gateway-health-check.sh
```

---

## 🧪 验证测试

### 1. Skills 验证
```bash
ls -la ~/.openclaw/workspace/.agents/skills/ | grep -E "autonomous|team-dev"
# 应显示 5 个 autonomous-* 和 1 个 team-dev-agent
```

### 2. Symlinks 验证
```bash
ls -la ~/.openclaw/workspace/hooks ~/.openclaw/workspace/scripts-dispatcher
# 应显示正确的 symlink 目标
```

### 3. 健康检查脚本验证
```bash
~/.openclaw/workspace/scripts/quick-diagnose.sh
# 应输出诊断报告
```

### 4. AGENTS.md 验证
```bash
grep -A5 "OpenClaw PM V2" ~/.openclaw/workspace/AGENTS.md
# 应显示 V2 增强规则
```

---

## 📋 后续步骤

### 立即执行
1. **配置 GitHub Labels** - 运行 `setup-labels.sh`
2. **设置 Dispatcher Cron** - 添加 5 分钟调度任务
3. **测试健康检查** - 运行 `quick-diagnose.sh`

### 可选增强
1. **配置 GitHub App** - 生产环境推荐使用 GitHub App Token
2. **设置飞书通知** - 进程监控通知
3. **配置健康检查 Cron** - 自动监控 Gateway

---

## 🚨 安全注意事项

### autonomous-dev-team
- ⚠️ 公共仓库需限制 `autonomous` label 权限
- ⚠️ 使用 GitHub App Token（最小权限）
- ⚠️ 启用分支保护（require PR review）

### team-dev-agent
- ⚠️ 禁止 Mock 数据（必须真实 DB）
- ⚠️ 禁止硬编码（必须 .env）
- ⚠️ 进程监控防无声死亡

### Session 隔离
- 🔒 禁止跨 session 查找 context
- 🔒 禁止假设 context
- 🔒 禁止删除 session 文件

---

## 📊 部署摘要

| 组件 | 状态 | 位置 |
|------|------|------|
| autonomous-common | ✅ | `.agents/skills/autonomous-common/` |
| autonomous-dev | ✅ | `.agents/skills/autonomous-dev/` |
| autonomous-dispatcher | ✅ | `.agents/skills/autonomous-dispatcher/` |
| autonomous-review | ✅ | `.agents/skills/autonomous-review/` |
| create-issue | ✅ | `.agents/skills/create-issue/` |
| team-dev-agent | ✅ | `.agents/skills/team-dev-agent/` |
| 健康检查脚本 | ✅ | `scripts/*.sh` |
| AGENTS.md V2 | ✅ | `AGENTS.md` |

---

**部署完成时间**: 2026-04-17 15:37 (Asia/Shanghai)  
**部署工具**: OpenClaw + npx skills  
**维护者**: 科技新闻

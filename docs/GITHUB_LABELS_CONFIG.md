# GitHub Labels 配置完成报告

> 配置日期：2026-04-17  
> 目标仓库：https://github.com/jhaiq/dev-team-agents

---

## ✅ 配置状态

| 项目 | 状态 |
|------|------|
| **GitHub CLI** | ✅ 已安装 (v2.68.0) |
| **Token 保存** | ✅ 安全存储 (`~/.github_token`, 权限 600) |
| **配置文件** | ✅ 已创建 (`autonomous.conf`) |
| **Labels 创建** | ✅ 8 个 Labels 已创建 |

---

## 🏷️ 已创建 Labels

| Label | 颜色 | 描述 | 用途 |
|-------|------|------|------|
| **autonomous** | 🟢 #0E8A16 | Issue should be processed by autonomous pipeline | 触发自动开发流程 |
| **in-progress** | 🟡 #FBCA04 | Agent is actively developing | 开发中 |
| **pending-review** | 🔵 #1D76DB | Development complete, awaiting review | 等待评审 |
| **reviewing** | 🟣 #5319E7 | Agent is actively reviewing | 评审中 |
| **pending-dev** | 🔴 #E99695 | Review failed, needs more development | 需要重新开发 |
| **approved** | 🟢 #0E8A16 | Review passed, PR merged or awaiting manual merge | 已批准 |
| **no-auto-close** | 🟣 #d4c5f9 | Skip auto-merge after review passes, requires manual approval | 禁止自动合并 |
| **stalled** | 🔴 #B60205 | Issue exceeded max retry attempts, requires manual investigation | 已停滞 |

---

## 📋 默认 GitHub Labels

仓库还保留了 GitHub 默认的 9 个 Labels：

| Label | 颜色 |
|-------|------|
| bug | #d73a4a |
| documentation | #0075ca |
| duplicate | #cfd3d7 |
| enhancement | #a2eeef |
| good first issue | #7057ff |
| help wanted | #008672 |
| invalid | #e4e669 |
| question | #d876e3 |
| wontfix | #ffffff |

**总计**: 17 个 Labels

---

## 🔧 配置详情

### GitHub CLI 安装

```bash
# 安装位置
~/.local/bin/gh

# 版本
gh version 2.68.0 (2025-03-05)
```

### Token 配置

```bash
# Token 位置
~/.github_token

# 权限
600 (仅所有者可读写)

# Token 所有者
jhaiq (GitHub User ID: 25874769)
```

### autonomous.conf 配置

```bash
# 位置
~/.openclaw/workspace/.agents/skills/autonomous-dispatcher/scripts/autonomous.conf

# 关键配置
PROJECT_ID="dev-team-agents"
REPO="jhaiq/dev-team-agents"
REPO_OWNER="jhaiq"
REPO_NAME="dev-team-agents"
PROJECT_DIR="/home/node/.openclaw/workspace/repos/dev-team-agents"
GH_AUTH_MODE="token"
GH_TOKEN_FILE="$HOME/.github_token"
```

---

## 🚀 使用流程

### 1. 创建 Issue

在 GitHub 仓库创建 Issue：
https://github.com/jhaiq/dev-team-agents/issues/new

### 2. 添加 autonomous Label

给 Issue 添加 `autonomous` Label，触发自动开发流程。

### 3. 自动流程

```
Issue 创建
    ↓
添加 autonomous Label
    ↓
Dispatcher 检测 (每 5 分钟)
    ↓
Dev Agent 开发 (in-progress)
    ↓
Review Agent 评审 (reviewing)
    ↓
通过 → approved → 自动合并
    ↓
失败 → pending-dev → 重新开发
```

---

## 📊 Label 状态流转

```mermaid
stateDiagram-v2
    [*] --> autonomous: Issue 创建
    autonomous --> in-progress: Dispatcher 处理
    in-progress --> pending-review: 开发完成
    pending-review --> reviewing: 开始评审
    reviewing --> approved: 评审通过
    reviewing --> pending-dev: 评审失败
    pending-dev --> in-progress: 重新开发
    approved --> [*]: 合并完成
    reviewing --> stalled: 超过重试次数
    pending-dev --> stalled: 超过重试次数
```

---

## 🔒 安全配置

| 措施 | 状态 |
|------|------|
| **Token 存储** | ✅ 用户主目录 (`~/.github_token`) |
| **文件权限** | ✅ 600 (仅所有者可读写) |
| **.gitignore** | ✅ 已配置 (`*.token`, `*token*`) |
| **仓库配置** | ✅ 未提交到 Git |

---

## 📝 后续配置

### Dispatcher Cron（待配置）

```bash
# 编辑 crontab
crontab -e

# 添加（每 5 分钟执行）
*/5 * * * * cd /home/node/.openclaw/workspace/repos/dev-team-agents && \
  GITHUB_TOKEN=$(cat ~/.github_token) && \
  ~/.openclaw/workspace/.agents/skills/autonomous-dispatcher/scripts/dispatch-local.sh
```

### 测试流程

1. [ ] 创建测试 Issue
2. [ ] 添加 `autonomous` Label
3. [ ] 等待 Dispatcher 处理（5 分钟内）
4. [ ] 验证 Label 变化
5. [ ] 验证工作流程

---

## 📞 相关资源

| 资源 | 链接 |
|------|------|
| GitHub 仓库 | https://github.com/jhaiq/dev-team-agents |
| Gitee 仓库 | https://gitee.com/jhaiq/dev-team-agents |
| autonomous-dev-team | https://github.com/zxkane/autonomous-dev-team |
| GitHub CLI | https://cli.github.com/ |

---

**配置完成时间**: 2026-04-17 16:40 (Asia/Shanghai)  
**配置者**: 科技新闻  
**状态**: ✅ 完成

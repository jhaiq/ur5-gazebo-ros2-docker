# Dispatcher Cron 配置报告

> 配置日期：2026-04-17  
> 目标仓库：https://github.com/jhaiq/ur5-gazebo-ros2-docker

---

## ✅ 配置状态

| 项目 | 状态 |
|------|------|
| **Dispatcher 脚本** | ✅ 已创建 |
| **Cron 任务** | ✅ 已添加 |
| **执行频率** | ✅ 每 5 分钟 |
| **时区** | ✅ Asia/Shanghai |
| **GitHub 连接** | ✅ 正常 |

---

## 📋 Cron 任务详情

| 属性 | 值 |
|------|-----|
| **任务 ID** | `7d643419-cda7-4e72-93cf-76310eef3883` |
| **名称** | Autonomous Dispatcher - 每 5 分钟 |
| **Schedule** | `*/5 * * * *` (每 5 分钟) |
| **时区** | Asia/Shanghai |
| **Session Target** | isolated |
| **Payload Kind** | agentTurn |
| **Timeout** | 300 秒 (5 分钟) |
| **Delivery** | announce |
| **状态** | idle |
| **下次运行** | 2 分钟内 |

---

## 🔧 配置详情

### Dispatcher 脚本

**位置**: `/home/node/.openclaw/workspace/repos/ur5-gazebo-ros2-docker/scripts/dispatcher-cron.sh`

**权限**: `755` (可执行)

**功能**:
- ✅ 扫描带有 `autonomous` label 的 open issues
- ✅ 检查并发限制 (默认 5 个)
- ✅ 检查依赖关系
- ✅ 分发新开发任务 (`dev-new`)
- ✅ 分发评审任务 (`review`)
- ✅ 日志记录到 `/tmp/dispatcher-cron.log`

### Cron 表达式

```cron
*/5 * * * *
```

**含义**: 每小时的第 0、5、10、15、20、25、30、35、40、45、50、55 分钟执行

**时区**: Asia/Shanghai (UTC+8)

---

## 🚀 工作流程

### Dispatcher 执行流程

```
每 5 分钟触发
    ↓
检查并发限制 (max: 5)
    ↓
扫描新 Issues (autonomous label, 无状态 label)
    ↓
检查依赖关系
    ↓
添加 in-progress label
    ↓
评论：🤖 Dispatching autonomous development...
    ↓
调用 dispatch-local.sh dev-new
    ↓
扫描 Review Issues (pending-review label)
    ↓
添加 reviewing label
    ↓
评论：🤖 Dispatching autonomous review...
    ↓
调用 dispatch-local.sh review
    ↓
完成
```

### Label 流转

```
Issue 创建 + autonomous label
    ↓ (Dispatcher 检测)
in-progress (开发中)
    ↓ (开发完成)
pending-review (等待评审)
    ↓ (Dispatcher 检测)
reviewing (评审中)
    ↓ (评审通过)
approved (已批准)
    ↓
PR 合并
```

---

## 📊 监控和日志

### 日志文件

| 日志 | 位置 |
|------|------|
| **Dispatcher Cron** | `/tmp/dispatcher-cron.log` |
| **Dev Agent** | `/tmp/agent-ur5-gazebo-ros2-docker-issue-*.log` |
| **Review Agent** | `/tmp/agent-ur5-gazebo-ros2-docker-review-*.log` |

### 查看日志

```bash
# 查看最新日志
tail -f /tmp/dispatcher-cron.log

# 查看特定 Issue 的开发日志
tail -f /tmp/agent-ur5-gazebo-ros2-docker-issue-1.log

# 查看评审日志
tail -f /tmp/agent-ur5-gazebo-ros2-docker-review-1.log
```

### 查看 Cron 状态

```bash
# 列出所有 cron 任务
openclaw cron list

# 查看 Dispatcher 任务详情
openclaw cron list | grep "Dispatcher"
```

---

## 🧪 测试流程

### 1. 创建测试 Issue

在 GitHub 创建 Issue:
https://github.com/jhaiq/ur5-gazebo-ros2-docker/issues/new

**标题**: `测试 autonomous dispatcher`

**内容**:
```markdown
## 任务描述
这是一个测试 Issue，用于验证 autonomous dispatcher 是否正常工作。

## 验收标准
- [ ] Dispatcher 在 5 分钟内检测到 Issue
- [ ] 自动添加 in-progress label
- [ ] 添加评论
- [ ] 启动开发流程
```

### 2. 添加 autonomous Label

给 Issue 添加 `autonomous` label。

### 3. 等待 Dispatcher

等待最多 5 分钟，Dispatcher 会自动检测并处理。

### 4. 验证

检查以下内容：
- [ ] Issue 添加了 `in-progress` label
- [ ] Issue 有评论：`🤖 Dispatching autonomous development...`
- [ ] 日志文件创建：`/tmp/agent-ur5-gazebo-ros2-docker-issue-*.log`
- [ ] Dev Agent 开始工作

---

## 🔍 故障排查

### Dispatcher 未运行

**检查 Cron 状态**:
```bash
openclaw cron list | grep "Dispatcher"
```

**手动触发**:
```bash
openclaw cron run 7d643419-cda7-4e72-93cf-76310eef3883
```

### GitHub API 失败

**检查 Token**:
```bash
cat /home/node/.github_token
export GITHUB_TOKEN="$(cat /home/node/.github_token)"
gh api user
```

### 并发限制

如果活跃任务达到 5 个，Dispatcher 会跳过本次执行。

**查看活跃任务**:
```bash
export GITHUB_TOKEN="$(cat /home/node/.github_token)"
gh issue list --repo jhaiq/ur5-gazebo-ros2-docker --label "in-progress,reviewing"
```

---

## 📝 管理命令

### 暂停 Dispatcher

```bash
openclaw cron update 7d643419-cda7-4e72-93cf-76310eef3883 --enabled false
```

### 恢复 Dispatcher

```bash
openclaw cron update 7d643419-cda7-4e72-93cf-76310eef3883 --enabled true
```

### 立即运行

```bash
openclaw cron run 7d643419-cda7-4e72-93cf-76310eef3883
```

### 删除 Cron

```bash
openclaw cron remove 7d643419-cda7-4e72-93cf-76310eef3883
```

---

## 🔒 安全配置

| 措施 | 状态 |
|------|------|
| **Token 存储** | ✅ `~/.github_token` (权限 600) |
| **脚本权限** | ✅ 755 (可执行) |
| **日志权限** | ✅ 600 (仅所有者可读) |
| **Session 隔离** | ✅ isolated session |
| **超时限制** | ✅ 300 秒 |

---

## 📞 相关资源

| 资源 | 链接/路径 |
|------|-----------|
| GitHub 仓库 | https://github.com/jhaiq/ur5-gazebo-ros2-docker |
| Gitee 仓库 | https://gitee.com/jhaiq/ur5-gazebo-ros2-docker |
| Dispatcher 脚本 | `scripts/dispatcher-cron.sh` |
| 日志文件 | `/tmp/dispatcher-cron.log` |
| autonomous-dev-team | https://github.com/zxkane/autonomous-dev-team |

---

## 📅 配置历史

| 日期 | 事件 |
|------|------|
| 2026-04-17 16:57 | 创建 dispatcher-cron.sh 脚本 |
| 2026-04-17 16:58 | 添加 OpenClaw Cron 任务 |
| 2026-04-17 16:58 | 验证 GitHub 连接 |

---

**配置完成时间**: 2026-04-17 16:58 (Asia/Shanghai)  
**配置者**: 科技新闻  
**状态**: ✅ 运行中 (下次执行：2 分钟内)

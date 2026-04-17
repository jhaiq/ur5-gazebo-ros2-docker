# 仓库用途说明

> 创建日期：2026-04-17  
> 最后更新：2026-04-17 17:35

---

## 📋 仓库用途区分

| 平台 | 仓库名 | 用途 | Issues | Dispatcher |
|------|--------|------|--------|------------|
| **Gitee** | `dev-team-agents` | AI Agents 开发 | ❌ 不启用 | ❌ 不监控 |
| **GitHub** | `ur5-gazebo-ros2-docker` | 项目开发使用 | ✅ 启用 | ✅ 每 5 分钟监控 |

---

## 🎯 仓库定位

### Gitee: dev-team-agents

**用途**: AI Agents 开发、技能研究、框架测试

**特点**:
- 国内访问速度快
- 用于 Agent 技能开发和测试
- 不启用 Issues 功能
- 不运行 autonomous dispatcher

**典型内容**:
- Agent 技能代码
- 测试脚本
- 开发文档

### GitHub: ur5-gazebo-ros2-docker

**用途**: 正式项目开发

**特点**:
- 启用 Issues 追踪
- autonomous dispatcher 每 5 分钟监控
- 自动化开发流程
- 国际协作

**典型内容**:
- UR5 机械臂项目
- Gazebo 仿真
- ROS2 配置
- Docker 环境

---

## 🔧 Git 远程配置

本地仓库当前配置：

```bash
# GitHub (项目开发 - 主要)
origin  git@github.com:jhaiq/ur5-gazebo-ros2-docker.git

# Gitee (AI Agents 开发 - 独立)
gitee   git@gitee.com:jhaiq/dev-team-agents.git
```

### ⚠️ 重要：不要混用

**两个仓库是独立的**，不要互相推送：

```bash
# ✅ 正确：推送到 GitHub 项目仓库
git push origin main

# ✅ 正确：推送到 Gitee Agent 仓库
git push gitee main

# ❌ 错误：不要交叉推送
# git push origin gitee/main  # 不要这样做
```

---

## 📁 本地工作目录

| 目录 | 用途 | 对应远程 |
|------|------|----------|
| `/repos/ur5-gazebo-ros2-docker` | 当前工作目录 | `origin` (GitHub) |
| `/repos/dev-team-agents` | (可选) Agent 开发目录 | `gitee` (Gitee) |

**建议**: 为 Gitee 仓库创建独立的工作目录：

```bash
cd /home/node/.openclaw/workspace/repos
git clone git@gitee.com:jhaiq/dev-team-agents.git
cd dev-team-agents
```

---

## 🚀 Dispatcher 配置

**仅监控 GitHub 仓库**:

```bash
# Cron 任务
ID: 7d643419-cda7-4e72-93cf-76310eef3883
名称：Autonomous Dispatcher - ur5-gazebo-ros2-docker
Schedule: */5 * * * *
仓库：jhaiq/ur5-gazebo-ros2-docker
```

**Gitee 仓库不受监控**，纯手动开发。

---

## 📊 访问地址

| 平台 | 仓库 | URL | 用途 |
|------|------|-----|------|
| **GitHub** | ur5-gazebo-ros2-docker | https://github.com/jhaiq/ur5-gazebo-ros2-docker | 项目开发 |
| **Gitee** | dev-team-agents | https://gitee.com/jhaiq/dev-team-agents | AI Agents 开发 |

---

## 💡 使用场景

### 场景 1: 项目开发

```bash
cd /home/node/.openclaw/workspace/repos/ur5-gazebo-ros2-docker
# 开发 UR5 项目
git add .
git commit -m "feat: 添加 UR5 控制模块"
git push origin main
# → 自动触发 GitHub Actions
# → Dispatcher 监控 Issues
```

### 场景 2: Agent 技能开发

```bash
cd /home/node/.openclaw/workspace/repos/dev-team-agents
# 开发 Agent 技能
git add .
git commit -m "feat: 添加新技能"
git push gitee main
# → 纯手动开发，无自动化
```

---

## 📝 配置历史

| 日期 | 事件 |
|------|------|
| 2026-04-17 16:10 | 创建 Gitee 仓库 `dev-team-agents` (AI Agents 开发) |
| 2026-04-17 17:03 | GitHub 仓库重命名为 `ur5-gazebo-ros2-docker` (项目开发) |
| 2026-04-17 17:25 | 修复 Gitee 远程配置 |
| 2026-04-17 17:35 | 明确双仓库用途区分 |

---

## 🔍 快速检查

```bash
# 查看当前远程配置
cd /home/node/.openclaw/workspace/repos/ur5-gazebo-ros2-docker
git remote -v

# 预期输出:
# gitee   git@gitee.com:jhaiq/dev-team-agents.git (fetch)
# gitee   git@gitee.com:jhaiq/dev-team-agents.git (push)
# origin  git@github.com:jhaiq/ur5-gazebo-ros2-docker.git (fetch)
# origin  git@github.com:jhaiq/ur5-gazebo-ros2-docker.git (push)
```

---

**文档更新时间**: 2026-04-17 17:35 (Asia/Shanghai)  
**维护者**: 科技新闻

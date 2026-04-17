# 仓库命名说明

> 创建日期：2026-04-17  
> 最后更新：2026-04-17

---

## 📋 仓库命名策略

由于 GitHub 和 Gitee 使用不同的仓库名称，请遵循以下命名规则：

| 平台 | 仓库名 | 用途 |
|------|--------|------|
| **GitHub** | `ur5-gazebo-ros2-docker` | 主要开发仓库，Issues 追踪，autonomous dispatcher |
| **Gitee** | `dev-team-agents` | 代码镜像备份 |

---

## 🔧 Git 远程配置

本地仓库配置了**两个远程**：

```bash
# GitHub (主要)
origin  git@github.com:jhaiq/ur5-gazebo-ros2-docker.git

# Gitee (镜像)
gitee   git@gitee.com:jhaiq/dev-team-agents.git
```

### 推送到两个平台

```bash
# 推送到 GitHub（主要）
git push origin main

# 推送到 Gitee（镜像）
git push gitee main

# 同时推送到两个平台
git push origin main && git push gitee main
```

---

## ⚠️ 重要说明

### GitHub Issues
- **仅 GitHub 仓库启用 Issues**
- autonomous dispatcher 仅监控 GitHub Issues
- Gitee 仓库不启用 Issues 功能

### 代码同步
- 开发在 GitHub 进行
- 定期同步到 Gitee 作为备份
- 建议配置自动同步（GitHub Actions）

### 配置引用
- **Dispatcher Cron**: 使用 GitHub 仓库 (`jhaiq/ur5-gazebo-ros2-docker`)
- **文档链接**: 根据上下文选择正确的平台
  - Issues/PR 相关 → GitHub
  - 代码备份 → Gitee

---

## 📊 仓库地址

| 平台 | URL | 用途 |
|------|-----|------|
| **GitHub** | https://github.com/jhaiq/ur5-gazebo-ros2-docker | 主仓库 |
| **Gitee** | https://gitee.com/jhaiq/dev-team-agents | 镜像备份 |

---

## 🔄 同步流程

### 手动同步
```bash
cd /home/node/.openclaw/workspace/repos/ur5-gazebo-ros2-docker
git push gitee main
```

### 自动同步（推荐配置）

创建 `.github/workflows/sync-to-gitee.yml`:

```yaml
name: Sync to Gitee

on:
  push:
    branches: [main]

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      
      - name: Push to Gitee
        run: |
          git remote add gitee git@gitee.com:jhaiq/dev-team-agents.git
          git push gitee main
        env:
          GITEE_SSH_KEY: ${{ secrets.GITEE_SSH_KEY }}
```

---

## 📝 配置历史

| 日期 | 事件 |
|------|------|
| 2026-04-17 16:10 | 创建 Gitee 仓库 `dev-team-agents` |
| 2026-04-17 17:03 | GitHub 仓库重命名为 `ur5-gazebo-ros2-docker` |
| 2026-04-17 17:25 | 修复 Gitee 远程配置（保持原名） |

---

**文档创建时间**: 2026-04-17 17:25 (Asia/Shanghai)  
**维护者**: 科技新闻

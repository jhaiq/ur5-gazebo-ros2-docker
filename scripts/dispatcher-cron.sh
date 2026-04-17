#!/bin/bash
# dispatcher-cron.sh - 每 5 分钟运行 autonomous dispatcher
# 用于扫描 GitHub Issues 并自动分发开发/评审任务

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)"
PROJECT_DIR="/home/node/.openclaw/workspace/repos/ur5-gazebo-ros2-docker"
DISPATCHER_SCRIPT="$HOME/.openclaw/workspace/.agents/skills/autonomous-dispatcher/scripts/dispatch-local.sh"
CONF_FILE="$HOME/.openclaw/workspace/.agents/skills/autonomous-dispatcher/scripts/autonomous.conf"

# 更新 REPO 变量（从配置文件加载）
REPO="jhaiq/ur5-gazebo-ros2-docker"

# 加载配置
if [[ -f "$CONF_FILE" ]]; then
    source "$CONF_FILE"
fi

# 设置 GitHub Token
export GITHUB_TOKEN="$(cat /home/node/.github_token)"
export PATH="$HOME/.local/bin:$PATH"

# 日志
LOG_FILE="/tmp/dispatcher-cron.log"
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

log "=== Dispatcher Cron 启动 ==="
log "仓库：$REPO"
log "项目目录：$PROJECT_DIR"

# 检查 gh CLI
if ! command -v gh &>/dev/null; then
    log "错误：gh CLI 未找到"
    exit 1
fi

# 检查 GitHub 连接
if ! gh api user &>/dev/null; then
    log "错误：GitHub API 连接失败"
    exit 1
fi

log "GitHub 连接正常"

# 运行 dispatcher 逻辑
# 读取所有带有 autonomous label 的 open issues
log "扫描 GitHub Issues..."

# 检查并发限制
ACTIVE=$(gh issue list --repo "$REPO" --state open --limit 100 \
  --label "autonomous" --json labels \
  -q '[.[] | select(.labels[].name | IN("in-progress","reviewing"))] | length' 2>/dev/null || echo "0")

MAX_CONCURRENT="${MAX_CONCURRENT:-5}"
log "当前活跃任务：$ACTIVE / $MAX_CONCURRENT"

if [[ "$ACTIVE" -ge "$MAX_CONCURRENT" ]]; then
    log "达到并发限制，跳过本次调度"
    exit 0
fi

# 查找新的 autonomous issues（没有状态 label）
NEW_ISSUES=$(gh issue list --repo "$REPO" --state open --limit 100 \
  --label "autonomous" --json number,labels,title \
  -q '[.[] | select(
    [.labels[].name] | (
      contains(["in-progress"]) or
      contains(["pending-review"]) or
      contains(["reviewing"]) or
      contains(["pending-dev"]) or
      contains(["stalled"]) or
      contains(["approved"])
    ) | not
  )] | .[].number' 2>/dev/null || echo "")

if [[ -n "$NEW_ISSUES" ]]; then
    log "发现新 Issues: $NEW_ISSUES"
    for ISSUE_NUM in $NEW_ISSUES; do
        if [[ "$ACTIVE" -ge "$MAX_CONCURRENT" ]]; then
            log "达到并发限制，停止调度"
            break
        fi
        
        log "处理 Issue #$ISSUE_NUM"
        
        # 检查依赖
        DEPS=$(gh issue view "$ISSUE_NUM" --repo "$REPO" --json body -q '.body' 2>/dev/null \
          | sed -n '/^## Dependencies/,/^## /p' \
          | grep -oP '#\K[0-9]+' || echo "")
        
        BLOCKED=false
        for DEP in $DEPS; do
            STATE=$(gh issue view "$DEP" --repo "$REPO" --json state -q '.state' 2>/dev/null || echo "open")
            if [[ "$STATE" != "closed" ]]; then
                log "Issue #$ISSUE_NUM 依赖未解决：#$DEP"
                BLOCKED=true
                break
            fi
        done
        
        if [[ "$BLOCKED" == "true" ]]; then
            log "Issue #$ISSUE_NUM 被依赖阻塞，跳过"
            continue
        fi
        
        # 添加 in-progress label
        gh issue edit "$ISSUE_NUM" --repo "$REPO" --add-label "in-progress" 2>/dev/null || true
        
        # 添加评论
        gh issue comment "$ISSUE_NUM" --repo "$REPO" \
          --body "🤖 Dispatching autonomous development..." 2>/dev/null || true
        
        # 分发任务
        bash "$DISPATCHER_SCRIPT" dev-new "$ISSUE_NUM" 2>&1 | tee -a "$LOG_FILE" || true
        
        ACTIVE=$((ACTIVE + 1))
        log "Issue #$ISSUE_NUM 已分发"
    done
fi

# 检查 review 任务
REVIEW_ISSUES=$(gh issue list --repo "$REPO" --state open --limit 100 \
  --label "autonomous,pending-review" --json number,labels \
  -q '[.[] | select([.labels[].name] | contains(["reviewing"]) | not)] | .[].number' 2>/dev/null || echo "")

if [[ -n "$REVIEW_ISSUES" ]]; then
    log "发现 Review Issues: $REVIEW_ISSUES"
    for ISSUE_NUM in $REVIEW_ISSUES; do
        if [[ "$ACTIVE" -ge "$MAX_CONCURRENT" ]]; then
            log "达到并发限制，停止调度"
            break
        fi
        
        log "处理 Review Issue #$ISSUE_NUM"
        
        # 更新 label
        gh issue edit "$ISSUE_NUM" --repo "$REPO" \
          --remove-label "pending-review" --add-label "reviewing" 2>/dev/null || true
        
        # 添加评论
        gh issue comment "$ISSUE_NUM" --repo "$REPO" \
          --body "🤖 Dispatching autonomous review..." 2>/dev/null || true
        
        # 分发任务
        bash "$DISPATCHER_SCRIPT" review "$ISSUE_NUM" 2>&1 | tee -a "$LOG_FILE" || true
        
        ACTIVE=$((ACTIVE + 1))
        log "Review Issue #$ISSUE_NUM 已分发"
    done
fi

log "=== Dispatcher Cron 完成 ==="

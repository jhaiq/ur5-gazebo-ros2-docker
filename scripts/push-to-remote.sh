#!/bin/bash
# 推送仓库到远程 Git 服务器
# 用法：./push-to-remote.sh <remote-url>

set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_DIR"

echo "📦 AI 软件开发团队部署与分析仓库"
echo "================================"
echo ""

# 检查参数
if [ -z "$1" ]; then
    echo "用法：$0 <remote-url>"
    echo ""
    echo "示例:"
    echo "  $0 git@gitee.com:jhaiq/dev-team-agents.git"
    echo "  $0 https://github.com/username/dev-team-agents.git"
    echo ""
    echo "当前远程仓库："
    git remote -v || echo "  (无)"
    exit 1
fi

REMOTE_URL="$1"

# 设置远程仓库
echo "📍 设置远程仓库：$REMOTE_URL"
git remote add origin "$REMOTE_URL" 2>/dev/null || git remote set-url origin "$REMOTE_URL"

# 推送
echo ""
echo "🚀 推送到远程仓库..."
git push -u origin main

echo ""
echo "✅ 推送完成！"
echo ""
echo "仓库地址：$REMOTE_URL"
echo "查看提交：git remote show origin"

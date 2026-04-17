#!/bin/bash
# 在 Gitee 创建仓库并推送
# 用法：./create-gitee-repo.sh

set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_DIR"

echo "📦 AI 软件开发团队部署与分析仓库"
echo "================================"
echo ""

# 检查 SSH 连接
echo "🔑 检查 SSH 连接..."
if ssh -T -o BatchMode=yes git@gitee.com 2>&1 | grep -q "successfully"; then
    echo "   ✅ SSH 连接正常"
else
    echo "   ❌ SSH 连接失败"
    echo ""
    echo "   请先配置 SSH 密钥："
    echo "   1. ssh-keygen -t ed25519 -C \"tech-news@openclaw.local\""
    echo "   2. cat ~/.ssh/id_ed25519.pub"
    echo "   3. 添加到 https://gitee.com/profile/sshkeys"
    exit 1
fi
echo ""

# 检查是否已有 Token
TOKEN_FILE="$HOME/.gitee_token"
if [ -f "$TOKEN_FILE" ]; then
    TOKEN=$(cat "$TOKEN_FILE")
    echo "🔑 发现 Gitee Token"
    
    # 检查仓库是否存在
    echo "🔍 检查仓库是否存在..."
    if curl -s "https://gitee.com/api/v5/repos/jhaiq/dev-team-agents" | grep -q "Not Found"; then
        echo "   仓库不存在，正在创建..."
        
        # 创建仓库
        RESPONSE=$(curl -s -X POST "https://gitee.com/api/v5/user/repos" \
          -H "Content-Type: application/json" \
          -d "access_token=$TOKEN" \
          -d '{
            "name": "dev-team-agents",
            "description": "AI 软件开发团队部署与分析",
            "private": false,
            "auto_init": false
          }')
        
        if echo "$RESPONSE" | grep -q "\"html_url\""; then
            REPO_URL=$(echo "$RESPONSE" | grep -o '"html_url":"[^"]*"' | cut -d'"' -f4)
            echo "   ✅ 仓库创建成功：$REPO_URL"
        else
            echo "   ❌ 创建失败：$RESPONSE"
            echo ""
            echo "   请手动创建：https://gitee.com/new"
            exit 1
        fi
    else
        echo "   ✅ 仓库已存在"
    fi
else
    echo "⚠️  未找到 Gitee Token ($TOKEN_FILE)"
    echo ""
    echo "   请手动在 Gitee 创建仓库："
    echo ""
    echo "   1. 访问 https://gitee.com/new"
    echo "   2. 填写信息："
    echo "      - 仓库名：dev-team-agents"
    echo "      - 描述：AI 软件开发团队部署与分析"
    echo "      - 许可证：MIT"
    echo "      - ❌ 不要勾选'使用 Readme 初始化仓库'"
    echo "   3. 点击'创建'"
    echo ""
    echo "   或者获取 Token 后保存到 $TOKEN_FILE"
    echo "   Token 获取：https://gitee.com/profile/personal_access_tokens"
    echo ""
    read -p "创建完成后按回车继续推送..."
fi

# 设置远程仓库
echo ""
echo "📍 设置远程仓库..."
REMOTE_URL="git@gitee.com:jhaiq/dev-team-agents.git"

if git remote -v | grep -q "origin"; then
    git remote set-url origin "$REMOTE_URL"
else
    git remote add origin "$REMOTE_URL"
fi
echo "   ✅ 远程仓库：$REMOTE_URL"
echo ""

# 推送
echo "🚀 推送到 Gitee..."
if git push -u origin main 2>&1; then
    echo ""
    echo "✅ 推送成功！"
    echo ""
    echo "📍 仓库地址：https://gitee.com/jhaiq/dev-team-agents"
    echo "📊 查看提交：git remote show origin"
else
    echo ""
    echo "❌ 推送失败"
    echo "   请检查仓库是否正确创建"
    exit 1
fi

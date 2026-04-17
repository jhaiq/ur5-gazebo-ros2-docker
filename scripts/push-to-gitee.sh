#!/bin/bash
# 推送到 Gitee 完整流程脚本
# 用法：./push-to-gitee.sh

set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_DIR"

echo "📦 AI 软件开发团队部署与分析仓库"
echo "================================"
echo ""

# 检查 Git 配置
echo "🔍 检查 Git 配置..."
if [ -z "$(git config user.email)" ]; then
    echo "⚠️  未配置 Git 用户邮箱，正在设置..."
    git config user.email "tech-news@openclaw.local"
    git config user.name "科技新闻"
fi

echo "   邮箱：$(git config user.email)"
echo "   用户：$(git config user.name)"
echo ""

# 检查远程仓库
echo "🔍 检查远程仓库配置..."
REMOTE_URL="git@gitee.com:jhaiq/dev-team-agents.git"

if git remote -v | grep -q "origin"; then
    echo "   已存在远程仓库："
    git remote -v | grep origin
    echo ""
    read -p "是否更新为 $REMOTE_URL ? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git remote set-url origin "$REMOTE_URL"
        echo "   ✅ 远程仓库已更新"
    fi
else
    echo "   设置远程仓库：$REMOTE_URL"
    git remote add origin "$REMOTE_URL"
    echo "   ✅ 远程仓库已添加"
fi
echo ""

# 测试 SSH 连接
echo "🔑 测试 SSH 连接..."
if ssh -T -o BatchMode=yes git@gitee.com 2>&1 | grep -q "Successfully"; then
    echo "   ✅ SSH 连接正常"
else
    echo "   ⚠️  SSH 连接失败，请检查："
    echo "      1. SSH 密钥是否已生成 (ssh-keygen -t ed25519)"
    echo "      2. 公钥是否已添加到 Gitee (https://gitee.com/profile/sshkeys)"
    echo "      3. Gitee 仓库是否存在 (https://gitee.com/jhaiq/dev-team-agents)"
    echo ""
    echo "   生成并添加 SSH 密钥："
    echo "   ssh-keygen -t ed25519 -C \"tech-news@openclaw.local\""
    echo "   cat ~/.ssh/id_ed25519.pub"
    echo ""
    read -p "是否继续尝试推送？(y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi
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
    echo "❌ 推送失败，可能原因："
    echo "   1. Gitee 仓库不存在 - 请先在 https://gitee.com/new 创建仓库"
    echo "   2. SSH 密钥未配置 - 请添加公钥到 Gitee"
    echo "   3. 权限不足 - 请检查仓库权限"
    echo ""
    echo "📝 手动创建仓库步骤："
    echo "   1. 访问 https://gitee.com/new"
    echo "   2. 仓库名：dev-team-agents"
    echo "   3. 描述：AI 软件开发团队部署与分析"
    echo "   4. 不要勾选'使用 Readme 初始化'"
    echo "   5. 点击'创建'"
    echo "   6. 重新运行此脚本"
    exit 1
fi

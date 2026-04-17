# Claude Code 认证配置

> 创建日期：2026-04-17  
> 最后更新：2026-04-17 17:59

---

## ✅ Claude Code 已安装

**版本**: 2.1.112  
**路径**: `/home/node/.npm-global/bin/claude`

---

## ⚠️ 需要认证

当前状态：**未登录**

错误信息：
```
Not logged in · Please run /login
```

---

## 🔐 认证方式

### 方式 1: OAuth 登录（推荐）

```bash
export PATH="/home/node/.npm-global/bin:$PATH"
claude login
```

然后按照提示完成浏览器认证。

### 方式 2: API Key

```bash
# 1. 获取 API Key
# 访问：https://console.anthropic.com/

# 2. 创建密钥文件
echo "your-api-key-here" > ~/.anthropic_api_key
chmod 600 ~/.anthropic_api_key

# 3. 设置环境变量
echo 'export ANTHROPIC_API_KEY="$(cat ~/.anthropic_api_key)"' >> ~/.bashrc
export ANTHROPIC_API_KEY="$(cat ~/.anthropic_api_key)"
```

---

## 🧪 验证认证

```bash
export PATH="/home/node/.npm-global/bin:$PATH"

# 测试简单命令
claude -p "Hello, test"

# 预期输出：
# Hello! How can I help you today?
```

---

## 📋 完整测试流程

认证后，运行以下命令测试完整流程：

```bash
cd /home/node/.openclaw/workspace/repos/ur5-gazebo-ros2-docker
export PATH="/home/node/.npm-global/bin:$PATH"
bash scripts/autonomous-dev.sh --issue 1 --mode new
```

---

## 🔧 故障排查

### 问题 1: 命令未找到

```bash
# 确保 PATH 已设置
export PATH="/home/node/.npm-global/bin:$PATH"
which claude
```

### 问题 2: 权限错误

```bash
# 检查文件权限
ls -la ~/.anthropic_api_key
# 应该是：-rw------- (600)
```

### 问题 3: 网络问题

```bash
# 测试 API 连接
curl -I https://api.anthropic.com/
```

---

## 📊 当前状态

| 组件 | 状态 |
|------|------|
| **Claude Code CLI** | ✅ 已安装 (v2.1.112) |
| **PATH 配置** | ✅ `/home/node/.npm-global/bin` |
| **认证状态** | ❌ 需要登录 |
| **autonomous-dev.sh** | ✅ 脚本正常 |
| **Dispatcher Cron** | ✅ 运行正常 |

---

## 🚀 下一步

1. **完成认证**: `claude login`
2. **测试流程**: 运行 `autonomous-dev.sh --issue 1 --mode new`
3. **验证结果**: 检查 Issue #1 评论和 Labels 变化

---

**文档创建时间**: 2026-04-17 17:59 (Asia/Shanghai)  
**维护者**: 科技新闻

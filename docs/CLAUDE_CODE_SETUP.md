# Claude Code 配置说明

> 创建日期：2026-04-17  
> 最后更新：2026-04-17 18:06

---

## ✅ 配置完成

**状态**: 已配置并验证通过

---

## 🔐 认证配置

### 令牌文件

- **路径**: `/home/node/.anthropic_auth_token`
- **权限**: `600` (-rw-------)
- **提供商**: 阿里云 DashScope

### 环境变量

| 变量 | 值 |
|------|-----|
| `ANTHROPIC_AUTH_TOKEN` | `sk-sp-db55...` (从文件读取) |
| `ANTHROPIC_BASE_URL` | `https://coding.dashscope.aliyuncs.com/apps/anthropic` |
| `ANTHROPIC_MODEL` | `qwen3.6-plus` |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | `MiniMax-M2.5` |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | `kimi-k2.5` |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | `glm-5` |

---

## 📋 autonomous.conf 配置

```bash
# === Agent Configuration ===
AGENT_CMD="claude"
AGENT_DEV_MODEL="qwen3.6-plus"
AGENT_REVIEW_MODEL="kimi-k2.5"
AGENT_PERMISSION_MODE="auto"
```

---

## 🧪 验证测试

```bash
export PATH="/home/node/.npm-global/bin:$PATH"
export ANTHROPIC_AUTH_TOKEN="$(cat /home/node/.anthropic_auth_token)"
export ANTHROPIC_BASE_URL="https://coding.dashscope.aliyuncs.com/apps/anthropic"

# 测试
claude -p "Hello, test - 你好，测试"
```

**预期输出**:
```
你好！Hello! Test received. How can I help you today?
```

---

## 🔧 完整测试流程

```bash
cd /home/node/.openclaw/workspace/repos/ur5-gazebo-ros2-docker
export PATH="/home/node/.npm-global/bin:$PATH"
export ANTHROPIC_AUTH_TOKEN="$(cat /home/node/.anthropic_auth_token)"
export ANTHROPIC_BASE_URL="https://coding.dashscope.aliyuncs.com/apps/anthropic"

# 测试 autonomous-dev.sh
bash scripts/autonomous-dev.sh --issue 1 --mode new
```

---

## 📊 模型配置

| 用途 | 模型 |
|------|------|
| **开发任务** | qwen3.6-plus |
| **审查任务** | kimi-k2.5 |
| **复杂任务** | MiniMax-M2.5 |
| **简单任务** | glm-5 |

---

## 🔒 安全提示

- ✅ 令牌文件权限：600
- ✅ 令牌文件未加入 git
- ✅ 环境变量从文件读取
- ⚠️ 定期轮换令牌

---

## 📝 配置文件位置

| 文件 | 路径 |
|------|------|
| **令牌文件** | `/home/node/.anthropic_auth_token` |
| **autonomous.conf** | `/home/node/.openclaw/workspace/.agents/skills/autonomous-dispatcher/scripts/autonomous.conf` |
| **环境变量** | `~/.bashrc` |

---

**配置完成时间**: 2026-04-17 18:06 (Asia/Shanghai)  
**维护者**: 科技新闻

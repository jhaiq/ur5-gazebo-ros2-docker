# ANTHROPIC_API_KEY 配置说明

## 获取 API Key

1. 访问 https://console.anthropic.com/
2. 登录账户
3. 进入 "API Keys" 页面
4. 创建新密钥

## 配置方式

### 方式 1: 环境变量文件（推荐）

```bash
# 创建 API key 文件
echo "your-anthropic-api-key-here" > ~/.anthropic_api_key
chmod 600 ~/.anthropic_api_key

# 添加到 ~/.bashrc
echo 'export ANTHROPIC_API_KEY="$(cat ~/.anthropic_api_key)"' >> ~/.bashrc
```

### 方式 2: 直接设置环境变量

```bash
export ANTHROPIC_API_KEY="your-anthropic-api-key-here"
```

### 方式 3: 使用 Claude Code 内置认证

```bash
claude auth login
```

## 验证配置

```bash
# 检查环境变量
echo $ANTHROPIC_API_KEY

# 测试 Claude Code
claude -p "Hello, test"
```

## 安全提示

- API key 文件权限必须为 600
- 不要将 API key 上传到 git 仓库
- 定期轮换密钥

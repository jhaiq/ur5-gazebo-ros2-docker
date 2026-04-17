# Gitee 仓库推送指南

> 创建日期：2026-04-17  
> 目标仓库：https://gitee.com/jhaiq/ur5-gazebo-ros2-docker

---

## 📋 推送前准备

### 1. 检查 SSH 密钥

```bash
# 检查是否已有 SSH 密钥
ls -la ~/.ssh/id_ed25519* 2>/dev/null || echo "未找到 SSH 密钥"
```

**如果没有密钥，生成新的**：
```bash
ssh-keygen -t ed25519 -C "tech-news@openclaw.local"
# 按回车接受默认路径
```

**查看公钥**：
```bash
cat ~/.ssh/id_ed25519.pub
```

---

### 2. 添加公钥到 Gitee

1. 访问：https://gitee.com/profile/sshkeys
2. 点击「添加公钥」
3. 粘贴 `~/.ssh/id_ed25519.pub` 内容
4. 标题：`ur5-gazebo-ros2-docker-deploy`
5. 点击「确定」

---

### 3. 测试 SSH 连接

```bash
ssh -T git@gitee.com
```

**成功输出**：
```
Hi XXX! You've successfully authenticated, but GITEE.COM does not provide shell access.
```

---

## 🚀 推送方法

### 方法 A: 使用自动化脚本（推荐）

```bash
cd /home/node/.openclaw/workspace/repos/ur5-gazebo-ros2-docker
./scripts/push-to-gitee.sh
```

脚本会自动：
- ✅ 检查 Git 配置
- ✅ 检查 SSH 连接
- ✅ 设置远程仓库
- ✅ 执行推送
- ✅ 提供错误处理

---

### 方法 B: 手动推送

#### 步骤 1: 在 Gitee 创建仓库

1. 访问：https://gitee.com/new
2. 填写信息：
   - **仓库名**：`ur5-gazebo-ros2-docker`
   - **描述**：`AI 软件开发团队部署与分析`
   - **许可证**：`MIT`
   - **不要勾选**「使用 Readme 初始化仓库」
3. 点击「创建」

#### 步骤 2: 推送代码

```bash
cd /home/node/.openclaw/workspace/repos/ur5-gazebo-ros2-docker

# 设置远程仓库（如果未设置）
git remote add origin git@gitee.com:jhaiq/ur5-gazebo-ros2-docker.git

# 推送
git push -u origin main
```

---

## 🔍 常见问题

### 问题 1: 404 Not Found

**原因**: Gitee 仓库不存在

**解决**:
1. 访问 https://gitee.com/new 创建仓库
2. 确保仓库名正确：`ur5-gazebo-ros2-docker`
3. 重新推送

---

### 问题 2: Permission denied (publickey)

**原因**: SSH 密钥未配置

**解决**:
```bash
# 1. 生成密钥
ssh-keygen -t ed25519 -C "tech-news@openclaw.local"

# 2. 查看公钥
cat ~/.ssh/id_ed25519.pub

# 3. 添加到 Gitee: https://gitee.com/profile/sshkeys

# 4. 测试连接
ssh -T git@gitee.com
```

---

### 问题 3: 仓库已存在

**原因**: 远程仓库已存在且有内容

**解决**:
```bash
# 强制推送（谨慎使用，会覆盖远程）
git push -f -u origin main

# 或者先拉取再合并
git pull origin main --allow-unrelated-histories
git push -u origin main
```

---

## ✅ 推送后验证

### 1. 检查远程仓库

```bash
git remote -v
# 应显示：
# origin  git@gitee.com:jhaiq/ur5-gazebo-ros2-docker.git (fetch)
# origin  git@gitee.com:jhaiq/ur5-gazebo-ros2-docker.git (push)
```

### 2. 查看提交历史

```bash
git log --oneline
```

### 3. 访问 Gitee 仓库

打开浏览器访问：https://gitee.com/jhaiq/ur5-gazebo-ros2-docker

**应看到**:
- ✅ README.md
- ✅ docs/ 目录
- ✅ weekly-reports/ 目录
- ✅ 3 个提交记录

---

## 📊 仓库信息

| 项目 | 详情 |
|------|------|
| **仓库名** | ur5-gazebo-ros2-docker |
| **所有者** | jhaiq |
| **URL** | https://gitee.com/jhaiq/ur5-gazebo-ros2-docker |
| **SSH** | git@gitee.com:jhaiq/ur5-gazebo-ros2-docker.git |
| **HTTPS** | https://gitee.com/jhaiq/ur5-gazebo-ros2-docker.git |
| **分支** | main |
| **提交数** | 4 |
| **文件数** | 12 |

---

## 🔄 后续推送

后续更新后推送更简单：

```bash
cd /home/node/.openclaw/workspace/repos/ur5-gazebo-ros2-docker
git add -A
git commit -m "描述变更"
git push
```

---

## 📞 相关资源

| 资源 | 链接 |
|------|------|
| Gitee SSH 密钥 | https://gitee.com/profile/sshkeys |
| Gitee 创建仓库 | https://gitee.com/new |
| Gitee API 文档 | https://gitee.com/api/v5/swagger |
| Git 推送教程 | https://gitee.com/help/articles/4282 |

---

**最后更新**: 2026-04-17  
**维护者**: 科技新闻

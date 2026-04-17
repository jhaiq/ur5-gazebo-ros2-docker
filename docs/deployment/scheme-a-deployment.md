# 方案 A：生产环境全自动 - 部署文档

> 部署日期：2026-04-17  
> 部署状态：✅ 完成

---

## 📦 组件清单

| 组件 | 版本 | 状态 | 位置 |
|------|------|------|------|
| autonomous-dev-team | latest | ✅ | `.agents/skills/autonomous-*/` |
| team-dev-agent | latest | ✅ | `.agents/skills/team-dev-agent/` |
| openclaw-pm V2 | V2 | ✅ | `scripts/` + `AGENTS.md` |

---

## 🔧 安装步骤

### 1. 安装 autonomous-dev-team

```bash
cd /home/node/.openclaw/workspace
npx skills add zxkane/autonomous-dev-team --yes
```

**安装结果**:
- ✅ autonomous-common
- ✅ autonomous-dev
- ✅ autonomous-dispatcher
- ✅ autonomous-review
- ✅ create-issue

**Symlinks**:
```bash
ln -sf .agents/skills/autonomous-common/hooks hooks
ln -sf .agents/skills/autonomous-dispatcher/scripts scripts-dispatcher
```

---

### 2. 安装 team-dev-agent

```bash
npx skills add DataArcTech/team-dev-agent --yes
```

**安装结果**:
- ✅ team-dev-agent (7 阶段流程)

---

### 3. 配置 openclaw-pm V2

```bash
# 克隆配置仓库
git clone https://github.com/1va7/openclaw-pm.git /tmp/openclaw-pm

# 复制健康检查脚本
cp /tmp/openclaw-pm/scripts/*.sh ~/.openclaw/workspace/scripts/
chmod +x ~/.openclaw/workspace/scripts/*.sh
```

**脚本清单**:
- gateway-health-check.sh
- check-unanswered.sh
- heartbeat-check.sh
- check-missed-crons.sh
- morning-briefing.sh
- quick-diagnose.sh
- daily-stats.sh

---

### 4. 更新 AGENTS.md

添加 V2 增强规则:
- 复杂任务强制流程
- 任务记录规则
- Session 隔离规则
- GatewayRestart 强制行为
- 主动 Interview
- 并行执行优化

---

## ✅ 验证结果

### Skills 验证
```
✓ autonomous-common
✓ autonomous-dev
✓ autonomous-dispatcher
✓ autonomous-review
✓ create-issue
✓ team-dev-agent
```

### Symlinks 验证
```
✓ hooks → .agents/skills/autonomous-common/hooks
✓ scripts-dispatcher → .agents/skills/autonomous-dispatcher/scripts
```

### 健康检查脚本
```
✓ 7 个脚本已安装并授权执行
```

### AGENTS.md
```
✓ V2 规则已添加
```

### Gateway 状态
```
✓ 运行中 (PID: 15)
```

---

## 📋 待配置项

### 1. GitHub Labels（autonomous-dev-team）

```bash
# 运行标签设置脚本
bash ~/.openclaw/workspace/.agents/skills/autonomous-dispatcher/scripts/setup-labels.sh <owner>/<repo>
```

**需要设置的 Labels**:
- `autonomous` - 触发自动开发
- `pending-dev` - 等待开发
- `pending-review` - 等待评审
- `approved` - 已批准可合并

---

### 2. Dispatcher Cron

```bash
# 编辑 crontab
crontab -e

# 添加（每 5 分钟执行）
*/5 * * * * cd /path/to/project && openclaw run skills/autonomous-dispatcher/SKILL.md
```

---

### 3. 健康检查 Cron（可选）

```bash
# 晨间简报（每天 9:00）
0 9 * * * ~/.openclaw/workspace/scripts/morning-briefing.sh

# 健康检查（每 30 分钟）
*/30 * * * * ~/.openclaw/workspace/scripts/gateway-health-check.sh
```

---

## 🧪 测试清单

### autonomous-dev-team 测试

1. [ ] 创建测试 Issue
2. [ ] 添加 `autonomous` label
3. [ ] 等待 Dispatcher 处理（5 分钟内）
4. [ ] 验证 Dev Agent 创建 worktree
5. [ ] 验证 Review Agent 评审
6. [ ] 验证自动合并

### team-dev-agent 测试

1. [ ] 发送触发词："帮我开发一个登录功能"
2. [ ] 验证 Agent 输出架构设计
3. [ ] 验证后端实现
4. [ ] 验证前端实现
5. [ ] 验证测试通过

### 健康检查测试

1. [ ] 运行 `quick-diagnose.sh`
2. [ ] 验证 Gateway 状态检测
3. [ ] 验证 Session 检测
4. [ ] 验证错误报告

---

## 🔒 安全配置

### GitHub Token 权限

| 权限 | 用途 | 推荐范围 |
|------|------|----------|
| `repo` | 完整仓库控制 | 私有仓库 |
| `workflow` | CI/CD 触发 | 按需 |
| `read:org` | 组织读取 | 仅企业 |

**最佳实践**:
- 使用 GitHub App Token（而非 Personal Token）
- 最小权限原则
- 定期轮换 Token

### Session 隔离

```markdown
🔒 最高优先级规则：
- 禁止跨 session 查找 context
- 禁止假设 context
- 禁止删除 session 文件
```

---

## 📊 性能基线（待收集）

| 指标 | 基线值 | 测量方法 |
|------|--------|----------|
| Issue→PR 时间 | - | GitHub 时间戳差值 |
| PR→Merge 时间 | - | GitHub 时间戳差值 |
| Agent 响应时间 | - | 日志时间戳差值 |
| 任务成功率 | - | 成功/总任务数 |
| Gateway 可用性 | - | 正常运行时间/总时间 |

---

## 🚨 已知问题

| 问题 | 影响 | 解决方案 | 状态 |
|------|------|----------|------|
| 无 | - | - | - |

---

## 📝 变更记录

| 日期 | 变更 | 负责人 |
|------|------|--------|
| 2026-04-17 | 初始部署 | 科技新闻 |

---

**部署完成时间**: 2026-04-17 15:38 (Asia/Shanghai)  
**下次审查**: 2026-04-24

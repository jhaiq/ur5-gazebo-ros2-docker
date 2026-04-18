# 机器人领域 AI Agent 最新论文分析报告

**报告日期:** 2026-04-18  
**分析范围:** 2025-2026 年机器人领域 AI Agent 相关论文  
**来源:** arXiv, GitHub, 学术会议  

---

## 执行摘要

本报告对 2025-2026 年机器人领域 AI Agent 相关研究进行了全面分析，涵盖视觉 - 语言 - 动作 (VLA) 模型、具身智能、机器人操作学习、多智能体系统等核心方向。共分析 60+ 篇最新论文，识别出以下关键趋势：

1. **VLA 模型成为具身智能核心架构** - 统一视觉、语言和动作数据的端到端策略学习
2. **世界模型与推理能力增强** - 机器人通过世界模型进行规划和对齐
3. **多模态融合与具身交互** - 触觉、视觉、语言的深度融合
4. **仿真到现实迁移** - 生成式仿真和数据增强技术成熟
5. **长视野任务规划** - 分层策略和记忆机制解决复杂任务

---

## 一、视觉 - 语言 - 动作 (VLA) 模型

### 1.1 核心综述论文

#### [Vision-Language-Action Models for Robotics: A Review](https://arxiv.org/abs/2510.07077)
**arXiv: 2510.07077** | 2025

**核心贡献:**
- 系统性综述 VLA 模型在机器人领域的应用
- 统一视觉、语言、动作数据的端到端策略学习框架
- 分析 VLA 模型在跨任务、跨物体泛化方面的进展

**关键洞察:**
- VLA 模型通过大规模多模态数据预训练实现零样本迁移
- 主要挑战：实时性、安全性、可解释性

---

#### [A survey of embodied intelligence: advances in vision-language-action models](https://www.cjig.cn/en/article/doi/10.11834/jig.250544/)
**中国图象图形学报** | 2025

**核心贡献:**
- 具身智能与离身智能的本质区别分析
- 传感器 - 运动耦合、环境不确定性、长视野决策、实时控制四大挑战
- VLA 模型在具身智能中的核心地位

---

### 1.2 前沿 VLA 架构

#### [A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated VLA Model](https://arxiv.org/abs/2604.05672)
**arXiv: 2604.05672** | 2026-04-08 | 梁晓丹团队

**核心创新:**
- 完全透明开源的 VLA 模型
- 截断注意力机制提升推理效率
- 自适应推理根据任务复杂度调整计算资源

**技术要点:**
- 推理速度提升 3-5 倍
- 支持实时机器人控制

---

#### [DFA-VLA: Enhancing Robotic Manipulation via Embodied Intelligence](https://openreview.net/forum?id=OMdvdULJuA)
**OpenReview** | 2026

**核心创新:**
- 动态细粒度对齐 (Dynamic Fine-grained Alignment) 机制
- 基于预训练大语言模型 backbone
- 提升任务执行准确性、时效性和泛化能力

---

#### [Veo-Act: How Far Can Frontier Video Models Advance Generalizable Robot Manipulation?](https://arxiv.org/abs/2604.04502)
**arXiv: 2604.04502** | 2026-04-06 | 陈建宇团队

**核心研究问题:**
- 前沿视频模型在机器人操作泛化方面的能力边界
- 视频生成模型作为策略学习的数据增强工具
- 从视频到控制的端到端学习

---

### 1.3 VLA 模型优化与改进

#### [SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation](https://arxiv.org/abs/2604.05656)
**arXiv: 2604.05656** | 2026-04-07 | 马睿团队

**核心创新:**
- 流匹配 VLA 的单步动作生成
- 渐进式自蒸馏技术
- 推理速度提升 10 倍以上

---

#### [Adaptive Action Chunking at Inference-time for Vision-Language-Action Models](https://arxiv.org/abs/2604.04161)
**arXiv: 2604.04161** | 2026-04-05

**核心创新:**
- 推理时自适应动作分块
- 根据任务复杂度动态调整动作序列长度
- 提升长视野任务执行效率

---

#### [VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models](https://arxiv.org/abs/2604.03956)
**arXiv: 2604.03956** | 2026-04-05

**核心创新:**
- VLA 模型的"遗忘"机制
- 移除不希望的行为或知识
- 安全性和隐私保护

---

## 二、具身智能与世界模型

### 2.1 世界模型核心论文

#### [From Perception to Action: Spatial AI Agents and World Models](https://arxiv.org/abs/2602.01644)
**arXiv: 2602.01644** | 2026-02

**核心贡献:**
- 空间 AI Agent 与世界模型的连接综述
- 涵盖记忆、规划、世界模型在具身 Agent 中的应用
- 机器人和导航任务的世界模型架构

---

#### [World Models as an Intermediary between Agents and the Real World](https://arxiv.org/abs/2602.00785)
**arXiv: 2602.00785** | 2026-02

**核心论点:**
- 世界模型作为 Agent 与高成本真实环境之间的桥梁
- 提供更丰富的学习信号
- 跨领域应用：机器人、ML 工程

---

#### [3D-Anchored Lookahead Planning for Persistent Robotic Scene Memory via World-Model-Based MCTS](https://arxiv.org/abs/2604.11302)
**arXiv: 2604.11302** | 2026-04-13 | Dror Mizrahi 团队

**核心创新:**
- 基于世界模型的 MCTS 规划
- 3D 锚定的前瞻规划
- 持久性机器人场景记忆

---

### 2.2 具身 Agent 架构

#### [A Physical Agentic Loop for Language-Guided Grasping with Execution-State Monitoring](https://arxiv.org/abs/2604.07395)
**arXiv: 2604.07395** | 2026-04-08 | Feras Dayoub 团队

**核心创新:**
- 物理 Agent 循环架构
- 语言引导抓取与执行状态监控
- 项目页面：https://wenzewwz123.github.io/Agentic-Loop/

---

#### [Evolvable Embodied Agent for Robotic Manipulation via Long Short-Term Reflection and Optimization](https://arxiv.org/abs/2604.13533)
**arXiv: 2604.13533** | 2026-04-15 | 张旭龙团队

**核心创新:**
- 可进化的具身 Agent
- 长短期反思与优化机制
- 持续自我改进的机器人策略

---

## 三、机器人操作学习

### 3.1 模仿学习与强化学习

#### [RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework](https://arxiv.org/abs/2604.15308)
**arXiv: 2604.15308** | 2026-04-16 | 王兴刚团队

**核心创新:**
- 生成器 - 判别器框架中的强化学习扩展
- 项目页面：https://hgao-cv.github.io/RAD-2
- 大规模 RL 训练新方法

---

#### [R3D: Revisiting 3D Policy Learning](https://arxiv.org/abs/2604.15281)
**arXiv: 2604.15281** | 2026-04-16 | 季家元团队

**核心贡献:**
- 3D 策略学习的重新审视
- 新的 3D 表示学习方法
- 提升机器人操作的 3D 理解能力

---

#### [A Hierarchical Spatiotemporal Action Tokenizer for In-Context Imitation Learning in Robotics](https://arxiv.org/abs/2604.15215)
**arXiv: 2604.15215** | 2026-04-16 | Quoc-Huy Tran 团队

**核心创新:**
- 分层时空动作 Tokenizer
- 上下文模仿学习
- 动作序列的层次化表示

---

#### [WM-DAgger: Enabling Efficient Data Aggregation for Imitation Learning with World Models](https://arxiv.org/abs/2604.11351)
**arXiv: 2604.11351** | 2026-04-13 | 张大庆团队

**核心创新:**
- 结合世界模型的 DAgger
- 高效数据聚合
- 减少真实数据采集成本

---

### 3.2 视觉引导操作

#### [HiVLA: A Visual-Grounded-Centric Hierarchical Embodied Manipulation System](https://arxiv.org/abs/2604.14125)
**arXiv: 2604.14125** | 2026-04-15 | 罗平团队

**核心创新:**
- 视觉接地为中心的分层具身操作系统
- 项目页面：https://tianshuoy.github.io/HiVLA-page/
- 多层次视觉理解与动作生成

---

#### [Robotic Manipulation is Vision-to-Geometry Mapping](https://arxiv.org/abs/2604.12908)
**arXiv: 2604.12908** | 2026-04-14 | 王广润团队

**核心论点:**
- 机器人操作本质是视觉到几何的映射 f(v) → G
- 视觉 - 几何骨干网络优于语言和视频模型
- 新的机器人操作范式

---

#### [Text-Guided 6D Object Pose Rearrangement via Closed-Loop VLM Agents](https://arxiv.org/abs/2604.09781)
**arXiv: 2604.09781** | 2026-04-10 | 韩炳哲团队

**核心创新:**
- 文本引导的 6D 物体位姿重排
- 闭环 VLM Agent
- 语言指令到精确操作的映射

---

### 3.3 触觉与多模态融合

#### [TouchAnything: Diffusion-Guided 3D Reconstruction from Sparse Robot Touches](https://arxiv.org/abs/2604.08945)
**arXiv: 2604.08945** | 2026-04-10 | 袁文珍团队

**核心创新:**
- 从稀疏机器人触觉进行 3D 重建
- 扩散模型引导
- 项目页面：https://grange007.github.io/touchanything

---

#### [TAMEn: Tactile-Aware Manipulation Engine for Closed-Loop Data Collection in Contact-Rich Tasks](https://arxiv.org/abs/2604.07335)
**arXiv: 2604.07335** | 2026-04-08 | 李宏阳团队

**核心创新:**
- 触觉感知操作引擎
- 接触丰富任务的闭环数据采集
- 触觉 - 视觉融合

---

#### [GraspSense: Physically Grounded Grasp and Grip Planning for a Dexterous Robotic Hand](https://arxiv.org/abs/2604.05697)
**arXiv: 2604.05697** | 2026-04-07 | Dzmitry Tsetserukou 团队

**核心创新:**
- 物理接地的抓取和握持规划
- 语言引导感知与力地图
- 灵巧手操作

---

### 3.4 仿真与数据生成

#### [SIM1: Physics-Aligned Simulator as Zero-Shot Data Scaler in Deformable Worlds](https://arxiv.org/abs/2604.08544)
**arXiv: 2604.08544** | 2026-04-10 | 庞江淼团队

**核心创新:**
- 物理对齐的仿真器
- 可变形世界中的零样本数据扩展
- 项目页面：https://internrobotics.github.io/sim1.github.io/

---

#### [CRAFT: Video Diffusion for Bimanual Robot Data Generation](https://arxiv.org/abs/2604.03552)
**arXiv: 2604.03552** | 2026-04-04 | Daniel Seita 团队

**核心创新:**
- 视频扩散模型用于双臂机器人数据生成
- 大规模训练数据合成
- 减少真实数据采集需求

---

#### [AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation](https://arxiv.org/abs/2604.11674)
**arXiv: 2604.11674** | 2026-04-13 | 兰旭光团队

**核心贡献:**
- 可扩展的 affordance 感知机器人操作数据生成器
- 新基准测试
- 大规模训练数据

---

## 四、多智能体与协作机器人

### 4.1 多智能体系统

#### [One Interface, Many Robots: Unified Real-Time Low-Level Motion Planning for Collaborative Arms](https://arxiv.org/abs/2604.08787)
**arXiv: 2604.08787** | 2026-04-09 | 陈一鸣团队

**核心创新:**
- 统一接口控制多个机器人
- 实时低层运动规划
- 协作机械臂系统

---

#### [BiCoord: A Bimanual Manipulation Benchmark towards Long-Horizon Spatial-Temporal Coordination](https://arxiv.org/abs/2604.05831)
**arXiv: 2604.05831** | 2026-04-07 | 刘思团队

**核心贡献:**
- 双臂操作基准测试
- 长视野时空协调
- 复杂操作任务评估

---

### 4.2 人机协作

#### [OmniUMI: Towards Physically Grounded Robot Learning via Human-Aligned Multimodal Interaction](https://arxiv.org/abs/2604.10647)
**arXiv: 2604.10647** | 2026-04-12 | 王中原团队

**核心创新:**
- 物理接地的机器人学习
- 人对齐的多模态交互
- 自然的人机协作

---

#### [Human-Robot Copilot for Data-Efficient Imitation Learning](https://arxiv.org/abs/2604.03613)
**arXiv: 2604.03613** | 2026-04-04 | 王小龙团队

**核心创新:**
- 人机副驾驶系统
- 数据高效的模仿学习
- 人在回路的策略学习

---

#### [RoSHI: A Versatile Robot-oriented Suit for Human Data In-the-Wild](https://arxiv.org/abs/2604.07331)
**arXiv: 2604.07331** | 2026-04-08 | Antonio Loquercio 团队

**核心创新:**
- 机器人导向的多功能人类数据采集服
- 野外人类数据采集
- 项目页面：https://roshi-mocap.github.io/

---

## 五、长视野任务与规划

### 5.1 分层策略学习

#### [HiPolicy: Hierarchical Multi-Frequency Action Chunking for Policy Learning](https://arxiv.org/abs/2604.06067)
**arXiv: 2604.06067** | 2026-04-07 | 董昊团队

**核心创新:**
- 分层多频率动作分块
- 策略学习
- 长视野任务分解

---

#### [CLAW: Composable Language-Annotated Whole-body Motion Generation](https://arxiv.org/abs/2604.11251)
**arXiv: 2604.11251** | 2026-04-14 | 富政一团队

**核心创新:**
- 可组合的语言标注全身运动生成
- 模块化运动原语
- 复杂任务组合

---

### 5.2 规划与推理

#### [Why Reasoning Fails to Plan: A Planning-Centric Analysis of Long-Horizon Decision Making in LLM Agents](https://arxiv.org/abs/2601.22311)
**arXiv: 2601.22311** | 2026-01

**核心发现:**
- 逐步推理在长视野规划中的局限性分析
- 提出未来感知的前瞻与奖励估计
- 让早期动作考虑延迟结果

---

#### [ProAct: Agentic Lookahead in Interactive Environments](https://arxiv.org/abs/2602.05327)
**arXiv: 2602.05327** | 2026-02

**核心创新:**
- 交互式环境中的 Agent 前瞻
- 将环境搜索蒸馏为因果推理链
- 提前思考能力训练

---

## 六、移动机器人操作与 GUI Agent

### 6.1 移动 GUI 操作

#### [OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis](https://arxiv.org/abs/2604.15093)
**arXiv: 2604.15093** | 2026-04-16 | 林达华团队

**核心创新:**
- 开放移动 Agent 构建
- 任务与轨迹合成
- 移动设备操作自动化

---

#### [CovAgent: Overcoming the 30% Curse of Mobile Application Coverage with Agentic AI](https://arxiv.org/abs/2601.21253)
**arXiv: 2601.21253** | 2026-01

**核心创新:**
- 克服移动应用覆盖率 30% 诅咒
- 具身 AI 与动态插桩
- 代码检查与 GUI 模糊测试结合

---

#### [CUA-Skill: Develop Skills for Computer Using Agent](https://arxiv.org/abs/2601.21123)
**arXiv: 2601.21123** | 2026-01

**核心贡献:**
- 大规模计算机操作 Agent 技能库
- 参数化执行与组合图
- 动态检索与记忆感知故障恢复

---

## 七、AI Agent 架构与工程

### 7.1 Agent 架构设计

#### [Agentic Design Patterns: A System-Theoretic Framework](https://arxiv.org/abs/2601.19752)
**arXiv: 2601.19752** | 2026-01

**核心贡献:**
- 系统理论框架
- 将 Agent AI 分解为五个功能子系统
- 推导 12 个可重用设计模式

---

#### [DALIA: Towards a Declarative Agentic Layer for Intelligent Agents in MCP-Based Server Ecosystems](https://arxiv.org/abs/2601.17435)
**arXiv: 2601.17435** | 2026-01

**核心创新:**
- 声明式 Agent 层架构
- 形式化能力与声明式发现协议
- 确定性任务图构建

---

### 7.2 Agent 工程与优化

#### [Optimizing Agentic Workflows using Meta-tools](https://arxiv.org/abs/2601.22037)
**arXiv: 2601.22037** | 2026-01

**核心创新:**
- 使用 meta-tools 优化 Agent 工作流
- 将重复的 Agent 工具调用序列捆绑为确定性 meta-tools
- 跳过不必要的中间 LLM 推理步骤

---

#### [SemanticALLI: Caching Reasoning, Not Just Responses, in Agentic Systems](https://arxiv.org/abs/2601.16286)
**arXiv: 2601.16286** | 2026-01

**核心创新:**
- 缓存推理而非仅缓存响应
- 流水线感知的缓存架构
- 将结构化中间推理表示提升为一级可缓存工件

---

#### [SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents](https://arxiv.org/abs/2601.16746)
**arXiv: 2601.16746** | 2026-01

**核心创新:**
- 编码 Agent 的自适应性上下文剪枝
- 训练轻量级神经略读器
- 基于显式目标选择性保留相关代码行

---

### 7.3 持续学习与自适应

#### [JitRL: Just-In-Time Reinforcement Learning for Continual Learning in LLM Agents Without Gradient Updates](https://arxiv.org/abs/2601.18510)
**arXiv: 2601.18510** | 2026-01

**核心创新:**
- 无需梯度更新的即时强化学习
- 检索相关过去经验
- 测试时调节输出 logit

---

#### [AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement](https://arxiv.org/abs/2601.22758)
**arXiv: 2601.22758** | 2026-01

**核心创新:**
- 从轨迹到可重用专业知识的持续改进
- 提取双重形式可重用专业知识
- 专门子 Agent 用于程序性任务，技能模式用于静态知识

---

## 八、评估与基准测试

### 8.1 基准测试平台

#### [RoboPlayground: Democratizing Robotic Evaluation through Structured Physical Domains](https://arxiv.org/abs/2604.05226)
**arXiv: 2604.05226** | 2026-04-06 | Dieter Fox 团队

**核心贡献:**
- 通过结构化物理领域实现机器人评估民主化
- 标准化评估平台
- 可复现的基准测试

---

#### [DataCross: A Unified Benchmark and Agent Framework for Cross-Modal Heterogeneous Data Analysis](https://arxiv.org/abs/2601.21403)
**arXiv: 2601.21403** | 2026-01

**核心贡献:**
- 跨模态异构数据分析的统一基准和 Agent 框架
- 多 Agent 系统协调
- 分治工作流

---

### 8.2 评估方法

#### [Agentic Uncertainty Quantification](https://arxiv.org/abs/2601.15703)
**arXiv: 2601.15703** | 2026-01

**核心创新:**
- Agent 不确定性量化
- 双过程框架
- 将口头不确定性转化为双向控制信号

---

## 九、安全与治理

### 9.1 安全机制

#### [Agentic AI Governance and Lifecycle Management in Healthcare](https://arxiv.org/abs/2601.15630)
**arXiv: 2601.15630** | 2026-01

**核心贡献:**
- 医疗领域的 Agent AI 治理与生命周期管理
- 统一 Agent 生命周期管理蓝图
- 五层控制平面

---

#### [PatchIsland: Orchestration of LLM Agents for Continuous Vulnerability Repair](https://arxiv.org/abs/2601.17471)
**arXiv: 2601.17471** | 2026-01

**核心创新:**
- LLM Agent 编排用于持续漏洞修复
- 多样化 LLM Agent 集成
- 两阶段去重

---

### 9.2 可解释性与透明度

#### [Think Locally, Explain Globally: Graph-Guided LLM Investigations](https://arxiv.org/abs/2601.17915)
**arXiv: 2601.17915** | 2026-01

**核心创新:**
- 局部推理，全局解释
- 图引导的 LLM 调查
- 有界局部证据挖掘与确定性图遍历

---

## 十、关键趋势与洞察

### 10.1 技术趋势

| 趋势 | 描述 | 代表论文 |
|------|------|----------|
| **VLA 统一架构** | 视觉 - 语言 - 动作端到端学习成为主流 | A1, DFA-VLA, Veo-Act |
| **世界模型集成** | 机器人通过世界模型进行规划和推理 | 3D-Anchored MCTS, WM-DAgger |
| **多模态融合** | 触觉、视觉、语言深度融合 | TouchAnything, TAMEn, GraspSense |
| **仿真扩展** | 生成式仿真和数据增强成熟 | SIM1, CRAFT, AffordSim |
| **长视野规划** | 分层策略和记忆机制解决复杂任务 | HiPolicy, CLAW, ProAct |
| **持续学习** | 无需梯度更新的测试时学习 | JitRL, AutoRefine |
| **Agent 工程化** | 声明式架构、meta-tools、缓存优化 | DALIA, SemanticALLI |

### 10.2 研究热点

1. **具身智能基础模型** - VLA 模型成为机器人学习的核心架构
2. **世界模型与规划** - 通过世界模型实现长视野规划和推理
3. **多模态感知融合** - 触觉、视觉、语言的深度融合提升操作能力
4. **仿真到现实迁移** - 生成式仿真减少真实数据采集需求
5. **人机协作** - 自然的人机交互和人在回路学习
6. **持续自适应学习** - 测试时学习和自我改进机制
7. **Agent 系统工程** - 声明式架构、优化、缓存、治理

### 10.3 开放挑战

1. **实时性与效率** - VLA 模型的推理速度仍需提升
2. **安全性与可靠性** - 真实世界部署的安全保障
3. **可解释性** - Agent 决策过程的透明度
4. **泛化能力** - 跨任务、跨环境、跨物体的泛化
5. **数据效率** - 减少训练数据需求
6. **长视野任务** - 复杂多步骤任务的可靠执行

---

## 十一、推荐论文阅读清单

### 必读核心论文 (Top 10)

1. **Vision-Language-Action Models for Robotics: A Review** (arXiv: 2510.07077) - VLA 综述
2. **A1: A Fully Transparent Open-Source VLA Model** (arXiv: 2604.05672) - 高效 VLA
3. **From Perception to Action: Spatial AI Agents and World Models** (arXiv: 2602.01644) - 世界模型
4. **RAD-2: Scaling RL in Generator-Discriminator Framework** (arXiv: 2604.15308) - 大规模 RL
5. **HiVLA: Visual-Grounded-Centric Hierarchical Manipulation** (arXiv: 2604.14125) - 视觉操作
6. **TouchAnything: 3D Reconstruction from Sparse Touches** (arXiv: 2604.08945) - 触觉重建
7. **SIM1: Physics-Aligned Simulator** (arXiv: 2604.08544) - 仿真数据扩展
8. **Agentic Design Patterns: System-Theoretic Framework** (arXiv: 2601.19752) - Agent 架构
9. **Why Reasoning Fails to Plan** (arXiv: 2601.22311) - 长视野规划分析
10. **JitRL: Continual Learning Without Gradient Updates** (arXiv: 2601.18510) - 持续学习

### 按主题分类阅读

**VLA 模型入门:**
- Vision-Language-Action Models for Robotics: A Review
- A1: A Fully Transparent Open-Source VLA Model
- VLA-Forget: Vision-Language-Action Unlearning

**世界模型与规划:**
- From Perception to Action: Spatial AI Agents and World Models
- World Models as an Intermediary between Agents and the Real World
- 3D-Anchored Lookahead Planning via World-Model-Based MCTS

**机器人操作:**
- HiVLA: Visual-Grounded-Centric Hierarchical Manipulation
- Robotic Manipulation is Vision-to-Geometry Mapping
- TouchAnything: Diffusion-Guided 3D Reconstruction

**仿真与数据:**
- SIM1: Physics-Aligned Simulator as Zero-Shot Data Scaler
- CRAFT: Video Diffusion for Bimanual Robot Data Generation
- AffordSim: Scalable Data Generator for Affordance-Aware Manipulation

**Agent 架构:**
- Agentic Design Patterns: A System-Theoretic Framework
- DALIA: Declarative Agentic Layer for Intelligent Agents
- Optimizing Agentic Workflows using Meta-tools

---

## 十二、资源链接

### 论文集合与综述

- [Awesome-VLA](https://github.com/yueen-ma/Awesome-VLA) - VLA 论文集合
- [Awesome-Robotics-Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation) - 机器人操作论文集合
- [VoltAgent/awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers) - AI Agent 论文集合
- [Robotics Arxiv Daily](https://jiangranlv.github.io/robotics_arXiv_daily/) - 每日机器人论文更新
- [VLA Survey](https://vla-survey.github.io/) - VLA 模型综述网站

### 项目页面

- RAD-2: https://hgao-cv.github.io/RAD-2
- HiVLA: https://tianshuoy.github.io/HiVLA-page/
- TouchAnything: https://grange007.github.io/touchanything
- SIM1: https://internrobotics.github.io/sim1.github.io/
- Agentic-Loop: https://wenzewwz123.github.io/Agentic-Loop/
- RoSHI: https://roshi-mocap.github.io/

---

## 附录：论文时间线

### 2026 年 4 月 (最新)

| 日期 | 论文 | 方向 |
|------|------|------|
| 04-16 | RAD-2: Scaling RL | 强化学习 |
| 04-16 | R3D: Revisiting 3D Policy | 3D 策略 |
| 04-16 | OpenMobile | 移动 Agent |
| 04-15 | HiVLA | 视觉操作 |
| 04-15 | Evolvable Embodied Agent | 具身 Agent |
| 04-14 | CLAW | 全身运动 |
| 04-13 | 3D-Anchored MCTS | 世界模型 |
| 04-10 | SIM1 | 仿真 |
| 04-10 | TouchAnything | 触觉 |
| 04-08 | A Physical Agentic Loop | 具身 Agent |
| 04-07 | HiPolicy | 分层策略 |
| 04-06 | Veo-Act | 视频模型 |
| 04-06 | RoboPlayground | 基准测试 |

---

**报告生成时间:** 2026-04-18  
**分析工具:** Web Search, arXiv API, GitHub  
**分析师:** 科技新闻 AI Assistant

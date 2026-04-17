# UR5 Gazebo ROS2 - Docker 仿真环境

> **ROS2 Humble/Jazzy** | **Gazebo Sim** | **MoveIt2** | **Docker**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![ROS](https://img.shields.io/badge/ROS2-Humble%20%7C%20Jazzy-green.svg)](https://docs.ros.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)

---

## 📖 项目简介

UR5 Gazebo ROS2 是一个完整的 UR5 机械臂仿真环境，基于 ROS2 和 Gazebo，支持 Docker 一键部署。

### 核心功能

| 功能 | 描述 | 状态 |
|------|------|------|
| **UR5 描述** | URDF/Xacro 机器人模型 | ✅ |
| **Gazebo 仿真** | Ignition Gazebo 物理仿真 | ✅ |
| **MoveIt2** | 运动规划与避障 | ✅ |
| **ros2_control** | 硬件抽象与控制器 | ✅ |
| **Docker** | 容器化部署 | ✅ |
| **RViz2** | 可视化与调试 | ✅ |

---

## 🚀 快速开始

### 前置要求

- Ubuntu 22.04+ (或 Docker Desktop)
- ROS2 Humble 或 Jazzy
- Docker & Docker Compose (可选)

### 方式 1: Docker 一键启动 (推荐)

```bash
# 克隆仓库
git clone https://github.com/jhaiq/ur5-gazebo-ros2-docker.git
cd ur5-gazebo-ros2-docker

# 启动所有服务
docker compose up -d

# 查看日志
docker compose logs -f

# 停止服务
docker compose down
```

### 方式 2: 本地 ROS2 环境

```bash
# 创建工作空间
mkdir -p ~/ur5_ws/src
cd ~/ur5_ws/src
git clone https://github.com/jhaiq/ur5-gazebo-ros2-docker.git

# 安装依赖
cd ~/ur5_ws
rosdep install --from-paths src --ignore-src -r -y

# 构建
colcon build --symlink-install

# 启动仿真
source install/setup.bash
ros2 launch ur5_bringup gazebo.launch.py
```

---

## 📁 包结构

```
ur5_gazebo_ros2/
├── ur5_description/        # 机器人 URDF/Xacro 模型
│   ├── urdf/
│   │   ├── ur5.urdf.xacro
│   │   └── ur5.ros2_control.xacro
│   └── config/
│       └── ur5_params.yaml
├── ur5_gazebo/            # Gazebo 仿真配置
│   ├── launch/
│   │   └── gazebo.launch.py
│   └── worlds/
│       └── ur5_cell.world
├── ur5_moveit_config/     # MoveIt2 配置
│   ├── launch/
│   │   └── moveit.launch.py
│   ├── config/
│   │   ├── kinematics.yaml
│   │   ├── joint_limits.yaml
│   │   └── ur5.srdf
│   └── srdf/
├── ur5_bringup/           # 启动文件集合
│   ├── launch/
│   │   ├── ur5_bringup.launch.py
│   │   └── rviz.launch.py
│   └── config/
├── ur5_control/           # ros2_control 配置
│   ├── config/
│   │   └── ur5_controllers.yaml
│   └── launch/
│       └── control.launch.py
└── ur5_examples/          # 示例代码
    ├── examples/
    │   ├── joint_trajectory.py
    │   └── pick_place.py
    └── scripts/
```

---

## 🎮 使用示例

### 1. 启动 Gazebo 仿真

```bash
ros2 launch ur5_gazebo gazebo.launch.py
```

### 2. 启动 MoveIt2

```bash
ros2 launch ur5_moveit_config moveit.launch.py
```

### 3. RViz2 可视化

```bash
ros2 launch ur5_bringup rviz.launch.py
```

### 4. 发送关节轨迹命令

```bash
ros2 run ur5_examples joint_trajectory
```

### 5. 话题列表

```bash
# 查看可用话题
ros2 topic list

# 查看机械臂状态
ros2 topic echo /joint_states

# 发送速度命令
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.1}}"
```

---

## 🔧 配置选项

### 环境变量

| 变量 | 默认值 | 描述 |
|------|--------|------|
| `ROS_DOMAIN_ID` | 0 | DDS 域 ID |
| `RMW_IMPLEMENTATION` | auto | RMW 实现 |
| `GAZEBO_MODEL_PATH` | auto | Gazebo 模型路径 |

### 控制器配置

编辑 `ur5_control/config/ur5_controllers.yaml`:

```yaml
controller_manager:
  ros__parameters:
    update_rate: 100  # Hz
    
joint_state_broadcaster:
  ros__parameters:
    publish_rate: 100

joint_trajectory_controller:
  ros__parameters:
    joints:
      - shoulder_pan_joint
      - shoulder_lift_joint
      - elbow_joint
      - wrist_1_joint
      - wrist_2_joint
      - wrist_3_joint
```

---

## 🐛 故障排查

### 常见问题

#### 1. Gazebo 启动失败

```bash
# 检查 Gazebo 版本
gz sim --version

# 清除缓存
rm -rf ~/.gz/sim
```

#### 2. MoveIt2 规划失败

```bash
# 检查 TF 树
ros2 run tf2_tools view_frames

# 检查机器人状态
ros2 topic echo /joint_states
```

#### 3. Docker 显示问题

```bash
# 允许 X11 访问
xhost +local:docker

# 检查 DISPLAY 变量
echo $DISPLAY
```

---

## 📊 性能指标

| 指标 | 目标 | 实测 |
|------|------|------|
| 控制频率 | 100Hz | - |
| 规划时间 | <1s | - |
| 启动时间 | <30s | - |
| 内存占用 | <2GB | - |

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

### 开发流程

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feat/amazing-feature`)
3. 提交更改 (`git commit -m 'feat: add amazing feature'`)
4. 推送到分支 (`git push origin feat/amazing-feature`)
5. 开启 Pull Request

---

## 📄 许可证

本项目采用 Apache License 2.0 许可证。详见 [LICENSE](LICENSE) 文件。

---

## 🙏 致谢

- [Universal Robots](https://www.universal-robots.com/) - UR5 机器人制造商
- [ROS2](https://docs.ros.org/) - ROS2 社区
- [MoveIt](https://moveit.picknik.ai/) - MoveIt 运动规划
- [Gazebo](https://gazebosim.org/) - Gazebo 仿真

---

## 📬 联系方式

- **Issue**: [GitHub Issues](https://github.com/jhaiq/ur5-gazebo-ros2-docker/issues)
- **仓库**: https://github.com/jhaiq/ur5-gazebo-ros2-docker

---

**最后更新**: 2026-04-18  
**维护者**: 科技新闻  
**版本**: v0.1.0

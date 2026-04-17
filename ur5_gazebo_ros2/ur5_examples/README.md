# UR5 Examples - 示例代码

> UR5 Gazebo ROS2 示例和演示代码

## 文件结构

```
ur5_examples/
├── package.xml
├── CMakeLists.txt
├── examples/
│   ├── joint_trajectory_example.py    # 关节轨迹示例
│   └── pick_place_example.py          # Pick & Place 示例
└── scripts/
    └── demo.py                        # 演示脚本
```

## 示例说明

### 1. 关节轨迹示例
演示如何通过 ROS2 话题发送关节轨迹命令控制 UR5 机械臂。

```bash
ros2 run ur5_examples joint_trajectory_example
```

### 2. Pick & Place 示例
演示完整的抓取和放置任务流程。

```bash
ros2 run ur5_examples pick_place_example
```

### 3. 演示脚本
综合演示所有功能。

```bash
ros2 run ur5_examples demo
```

## 话题和服务

| 名称 | 类型 | 描述 |
|------|------|------|
| /joint_trajectory_controller/follow_joint_trajectory | action | 轨迹执行 |
| /joint_states | topic | 关节状态反馈 |
| /move_group/plan | service | 运动规划 |

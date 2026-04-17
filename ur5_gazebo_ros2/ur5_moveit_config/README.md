# UR5 MoveIt2 Configuration

> MoveIt2 运动规划配置包

## 文件结构

```
ur5_moveit_config/
├── package.xml
├── CMakeLists.txt
├── launch/
│   └── moveit.launch.py       # MoveIt2 启动文件
├── config/
│   ├── kinematics.yaml        # 运动学求解器配置
│   ├── joint_limits.yaml      # 关节限位配置
│   ├── moveit_controllers.yaml # 控制器配置
│   └── ur5.srdf               # 机器人语义描述
└── srdf/
    └── ur5.srdf.xacro         # SRDF 宏定义
```

## 功能说明

- **运动学求解器**: KDL (默认) / TRAC-IK (可选)
- **规划场景**: 配置碰撞检测
- **运动规划**: OMPL 规划器
- **控制器接口**: joint_trajectory_controller

## 使用方法

```bash
# 启动 MoveIt2
ros2 launch ur5_moveit_config moveit.launch.py

# 在 RViz2 中使用 MoveIt2 MotionPlanning 插件
ros2 launch ur5_bringup rviz.launch.py
```

## 话题列表

| 话题 | 类型 | 描述 |
|------|------|------|
| /joint_states | sensor_msgs/JointState | 关节状态 |
| /joint_trajectory_controller/follow_joint_trajectory | control_msgs/FollowJointTrajectory | 轨迹执行 |
| /planning_scene | moveit_msgs/PlanningScene | 规划场景 |
| /move_group/goal | moveit_msgs/MoveGroupGoal | 运动目标 |

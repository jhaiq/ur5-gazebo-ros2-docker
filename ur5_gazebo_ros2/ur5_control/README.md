# UR5 Control - ros2_control Configuration

> ros2_control 控制器配置包

## 文件结构

```
ur5_control/
├── package.xml
├── CMakeLists.txt
├── config/
│   └── ur5_controllers.yaml    # 控制器配置
└── launch/
    └── control.launch.py       # 控制器启动文件 (已移至 ur5_bringup)
```

## 控制器配置

### joint_trajectory_controller
- 用于控制 UR5 的 6 个关节
- 支持位置、速度、力矩控制
- 更新频率：100Hz

### joint_state_broadcaster
- 发布关节状态到 /joint_states 话题
- 发布频率：100Hz

## 使用方法

```bash
# 启动控制器
ros2 launch ur5_bringup control.launch.py

# 查看控制器状态
ros2 control list_controllers

# 加载控制器
ros2 control load_controller joint_trajectory_controller
```

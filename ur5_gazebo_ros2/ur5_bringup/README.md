# UR5 Bringup - 启动文件集合

> UR5 Gazebo ROS2 系统的主启动文件集合

## 文件结构

```
ur5_bringup/
├── package.xml
├── CMakeLists.txt
├── launch/
│   ├── ur5_bringup.launch.py    # 主启动文件
│   ├── rviz.launch.py           # RViz2 启动文件
│   └── control.launch.py        # 控制器启动文件
└── config/
    └── ur5.rviz                 # RViz2 配置文件
```

## 功能说明

- **ur5_bringup.launch.py**: 启动完整的 UR5 仿真系统
- **rviz.launch.py**: 单独启动 RViz2 可视化
- **control.launch.py**: 启动 ros2_control 控制器

## 使用方法

```bash
# 启动完整系统
ros2 launch ur5_bringup ur5_bringup.launch.py

# 仅启动 RViz2
ros2 launch ur5_bringup rviz.launch.py

# 仅启动控制器
ros2 launch ur5_bringup control.launch.py
```

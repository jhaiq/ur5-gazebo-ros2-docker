# UR5 Gazebo ROS2 性能优化指南

## 性能目标

| 指标 | 目标值 |
|------|--------|
| 控制频率 | 100Hz |
| 规划时间 | <1s |
| 启动时间 | <30s |
| 内存占用 | <2GB |

## 优化策略

### 1. 控制器优化

```yaml
# ur5_control/config/controller.yaml
controller_manager:
  update_rate: 100  # 100Hz 控制频率

joint_trajectory_controller:
  constraints:
    goal_time: 0.6
    stopped_velocity_tolerance: 0.01
```

### 2. MoveIt2 规划优化

```yaml
# ur5_moveit_config/config/ompl_planning.yaml
planning_plugin: ompl_interface/OMPLPlanner
request_adapters: >-
  default_planner_request_adapters/AddTimeOptimalParameterization
  default_planner_request_adapters/ResolveConstraintFrames
planning_time: 1.0  # 最大规划时间 1 秒
```

### 3. Gazebo 仿真优化

```xml
<!-- ur5_gazebo/world/ur5_world.world -->
<physics type="ode">
  <max_step_size>0.001</max_step_size>
  <real_time_factor>1</real_time_factor>
  <real_time_update_rate>1000</real_time_update_rate>
</physics>
```

### 4. Docker 启动优化

- 使用多阶段构建减少镜像大小
- 优化 ROS 包安装顺序
- 使用缓存层加速构建

## 性能测试

```bash
# 测试控制频率
ros2 topic hz /joint_states

# 测试规划时间
ros2 run moveit2_test plan_time_test

# 测试启动时间
time docker compose up
```

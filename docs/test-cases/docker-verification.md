# UR5 Gazebo ROS2 Test Cases

## Overview

This document describes test cases for verifying the UR5 Gazebo ROS2 Docker environment.

## Test Environment

- **Docker Image**: `ur5-gazebo-ros2:humble`
- **ROS Version**: ROS 2 Humble Hawksbill
- **Base OS**: Ubuntu 22.04 (Jammy)

## Test Cases

### TC-001: Docker Image Build

**Objective**: Verify Docker image builds successfully

**Steps**:
```bash
cd ur5_gazebo_ros2
docker-compose build
```

**Expected Result**:
- Build completes without errors
- Image `ur5-gazebo-ros2:humble` is created
- All ROS packages are installed

**Status**: ⏳ Pending manual verification

---

### TC-002: Gazebo Simulation Startup

**Objective**: Verify Gazebo simulation starts correctly

**Steps**:
```bash
docker-compose up gazebo
```

**Expected Result**:
- Container `ur5_gazebo` starts successfully
- Gazebo window opens (if DISPLAY configured)
- UR5 robot model loads in simulation
- No error messages in logs

**Verification**:
```bash
docker logs ur5_gazebo | grep -i error
# Should return no results
```

**Status**: ⏳ Pending manual verification

---

### TC-003: ROS 2 Topic Verification

**Objective**: Verify ROS 2 topics are published correctly

**Steps**:
```bash
# In a separate terminal
docker exec -it ur5_gazebo bash
source /opt/ros/humble/setup.bash
ros2 topic list
```

**Expected Topics**:
- `/joint_states`
- `/robot_description`
- `/clock`

**Verification**:
```bash
ros2 topic echo /joint_states --once
# Should show joint state data
```

**Status**: ⏳ Pending manual verification

---

### TC-004: MoveIt Integration

**Objective**: Verify MoveIt motion planning works

**Steps**:
```bash
docker-compose up moveit
```

**Expected Result**:
- MoveIt node starts successfully
- Motion planning service is available
- No error messages

**Verification**:
```bash
ros2 service list | grep moveit
# Should show MoveIt services
```

**Status**: ⏳ Pending manual verification

---

### TC-005: RViz Visualization

**Objective**: Verify RViz visualization works

**Steps**:
```bash
docker-compose up rviz
```

**Expected Result**:
- RViz starts successfully
- UR5 robot model displays correctly
- No error messages

**Status**: ⏳ Pending manual verification

---

### TC-006: ROS 2 Version Check

**Objective**: Verify ROS 2 Humble is installed

**Steps**:
```bash
docker exec -it ur5_gazebo bash
source /opt/ros/humble/setup.bash
ros2 --version
```

**Expected Result**:
```
ros2 humble
```

**Status**: ⏳ Pending manual verification

---

## Build Verification Script

A script is available at `scripts/verify-docker-build.sh` to automate basic verification.

## Manual Testing Checklist

- [ ] Docker image builds successfully
- [ ] Gazebo simulation starts
- [ ] UR5 model loads in Gazebo
- [ ] Joint states are published
- [ ] MoveIt integration works
- [ ] RViz visualization works
- [ ] No error messages in logs

## References

- [Design Document](../migration/humble-migration.md)
- [Issue #3](https://github.com/jhaiq/ur5-gazebo-ros2-docker/issues/3)
- [PR #4](https://github.com/jhaiq/ur5-gazebo-ros2-docker/pull/4)

#!/bin/bash
# UR5 Gazebo ROS2 Docker Entrypoint

set -e

# Source ROS2
source /opt/ros/jazzy/setup.bash
source /root/ur5_ws/install/setup.bash

# Set display for GUI apps
export DISPLAY=${DISPLAY:-:0}
export QT_X11_NO_MITSHM=1

# Allow X11 forwarding
xhost +local:docker 2>/dev/null || true

# Execute command
exec "$@"

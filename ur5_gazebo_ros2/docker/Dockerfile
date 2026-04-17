# UR5 Gazebo ROS2 Docker Image
FROM ros:jazzy-ros-base

# Set environment
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-colcon-common-extensions \
    python3-rosdep \
    ros-jazzy-gazebo-ros-pkgs \
    ros-jazzy-gz-ros2-control \
    ros-jazzy-joint-state-publisher \
    ros-jazzy-joint-trajectory-controller \
    ros-jazzy-moveit-ros-move-group \
    ros-jazzy-moveit-kinematics \
    ros-jazzy-moveit-planners-ompl \
    ros-jazzy-moveit-ros-visualization \
    ros-jazzy-robot-state-publisher \
    ros-jazzy-rviz2 \
    ros-jazzy-xacro \
    libgl1-mesa-glx \
    libglu1-mesa \
    libxrender1 \
    libxtst6 \
    libxi6 \
    && rm -rf /var/lib/apt/lists/*

# Create workspace
WORKDIR /root/ur5_ws
COPY ur5_gazebo_ros2/src /root/ur5_ws/src/

# Install rosdep
RUN rosdep init && \
    rosdep update && \
    rosdep install --from-paths src --ignore-src -r -y

# Build workspace
RUN /bin/bash -c '. /opt/ros/jazzy/setup.bash && \
    colcon build --symlink-install && \
    rm -rf build log'

# Setup entrypoint
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Default command
ENTRYPOINT ["/entrypoint.sh"]
CMD ["gazebo"]

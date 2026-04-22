cmake_minimum_required(VERSION 3.14.4)
project(ur5_gazebo)

find_package(ament_cmake REQUIRED)
find_package(gazebo_ros REQUIRED)

# Install launch files, worlds, and scripts
install(
  DIRECTORY launch worlds
  DESTINATION share/${PROJECT_NAME}
)

# Install Python scripts as executables
install(
  PROGRAMS scripts/spawn_ur5.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()

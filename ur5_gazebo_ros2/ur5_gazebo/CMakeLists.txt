cmake_minimum_required(VERSION 3.14.4)
project(ur5_gazebo)

find_package(ament_cmake REQUIRED)
find_package(gazebo_ros REQUIRED)

# Install launch files
install(
  DIRECTORY launch worlds
  DESTINATION share/${PROJECT_NAME}
)

ament_package()

cmake_minimum_required(VERSION 3.8)
project(ur5_examples)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)

# Install Python executables
install(PROGRAMS
  examples/joint_trajectory_example.py
  examples/pick_place_example.py
  scripts/demo.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()

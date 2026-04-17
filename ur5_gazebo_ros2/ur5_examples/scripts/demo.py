#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UR5 Demo Script

Demonstrates all UR5 Gazebo ROS2 capabilities.
"""

import rclpy
from rclpy.node import Node
import sys


class UR5Demo(Node):
    """UR5 demonstration node."""
    
    def __init__(self):
        super().__init__('ur5_demo')
        
        self.get_logger().info('UR5 Demo initialized')
        
        # Print available demos
        self.print_menu()
    
    def print_menu(self):
        """Print demo menu."""
        menu = """
╔════════════════════════════════════════════════════════╗
║           UR5 Gazebo ROS2 Demo Menu                    ║
╠════════════════════════════════════════════════════════╣
║  1. Joint Trajectory Example                           ║
║  2. Pick and Place Example                             ║
║  3. Joint State Monitor                                ║
║  4. Exit                                               ║
╚════════════════════════════════════════════════════════╝

Run examples with:
  ros2 run ur5_examples joint_trajectory_example
  ros2 run ur5_examples pick_place_example

Monitor joint states with:
  ros2 topic echo /joint_states
"""
        self.get_logger().info(menu)


def main(args=None):
    """Main entry point."""
    rclpy.init(args=args)
    
    node = UR5Demo()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Demo interrupted by user')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

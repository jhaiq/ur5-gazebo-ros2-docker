#!/usr/bin/env python3
"""Spawn UR5 robot in Gazebo."""

import sys
import rclpy
from rclpy.node import Node
from gazebo_msgs.srv import SpawnEntity


def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('spawn_ur5')
    
    # Declare and get robot_description parameter
    node.declare_parameter('robot_description', '')
    robot_description = node.get_parameter('robot_description').get_parameter_value().string_value
    
    if not robot_description:
        node.get_logger().error('robot_description parameter is empty!')
        node.destroy_node()
        rclpy.shutdown()
        sys.exit(1)
    
    # Create spawn client
    client = node.create_client(SpawnEntity, '/spawn_entity')
    
    # Wait for service
    node.get_logger().info('Waiting for /spawn_entity service...')
    while not client.wait_for_service(timeout_sec=1.0):
        if not rclpy.ok():
            node.get_logger().error('Interrupted while waiting for service.')
            sys.exit(1)
        node.get_logger().info('Waiting for /spawn_entity service...')
    
    # Create spawn request
    req = SpawnEntity.Request()
    req.name = 'ur5'
    req.xml = robot_description
    req.robot_namespace = ''
    req.reference_frame = 'world'
    
    # Spawn entity
    node.get_logger().info('Spawning UR5 robot in Gazebo...')
    future = client.call_async(req)
    rclpy.spin_until_future_complete(node, future)
    
    if future.result() is not None:
        node.get_logger().info('UR5 robot spawned successfully!')
    else:
        node.get_logger().error(f'Failed to spawn UR5: {future.exception()}')
        sys.exit(1)
    
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

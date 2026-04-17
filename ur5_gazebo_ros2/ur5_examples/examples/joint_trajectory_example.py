#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Joint Trajectory Example for UR5

Demonstrates how to send joint trajectory commands to the UR5 robot.
"""

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from control_msgs.action import FollowJointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from builtin_interfaces.msg import Duration


class JointTrajectoryExample(Node):
    """Example node for sending joint trajectory commands."""
    
    def __init__(self):
        super().__init__('joint_trajectory_example')
        
        # Action client for joint trajectory controller
        self.action_client = ActionClient(
            self,
            FollowJointTrajectory,
            '/joint_trajectory_controller/follow_joint_trajectory'
        )
        
        # UR5 joint names
        self.joint_names = [
            'shoulder_pan_joint',
            'shoulder_lift_joint',
            'elbow_joint',
            'wrist_1_joint',
            'wrist_2_joint',
            'wrist_3_joint'
        ]
        
        self.get_logger().info('Joint Trajectory Example initialized')
    
    def send_trajectory(self, positions_list, times_list):
        """
        Send a joint trajectory to the controller.
        
        Args:
            positions_list: List of joint position arrays (each array has 6 values)
            times_list: List of time points for each waypoint (in seconds)
        """
        # Wait for action server
        self.get_logger().info('Waiting for action server...')
        if not self.action_client.wait_for_server(timeout_sec=10.0):
            self.get_logger().error('Action server not available')
            return False
        
        # Create trajectory message
        goal_msg = FollowJointTrajectory.Goal()
        goal_msg.trajectory.joint_names = self.joint_names
        
        # Add trajectory points
        for positions, time_from_start in zip(positions_list, times_list):
            point = JointTrajectoryPoint()
            point.positions = positions
            point.velocities = [0.0] * 6  # Zero velocity at each waypoint
            point.time_from_start = Duration(sec=int(time_from_start), nanosec=int((time_from_start % 1) * 1e9))
            goal_msg.trajectory.points.append(point)
        
        # Send goal
        self.get_logger().info('Sending trajectory goal...')
        send_goal_future = self.action_client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, send_goal_future)
        
        goal_handle = send_goal_future.result()
        if not goal_handle.accepted:
            self.get_logger().error('Goal rejected')
            return False
        
        self.get_logger().info('Goal accepted, executing trajectory...')
        
        # Wait for result
        get_result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, get_result_future)
        
        result = get_result_future.result()
        self.get_logger().info(f'Trajectory completed with status: {result.status}')
        
        return True
    
    def run_home_motion(self):
        """Execute a simple home motion."""
        self.get_logger().info('Executing home motion...')
        
        # Define waypoints (in radians)
        positions = [
            [0.0, -0.7854, 0.7854, 0.0, 0.0, 0.0],  # Home position
            [0.5, -0.5, 0.5, 0.0, 0.0, 0.0],        # Move to intermediate
            [0.0, -0.7854, 0.7854, 0.0, 0.0, 0.0],  # Return to home
        ]
        
        times = [0.0, 2.0, 4.0]  # Time in seconds
        
        return self.send_trajectory(positions, times)


def main(args=None):
    """Main entry point."""
    rclpy.init(args=args)
    
    node = JointTrajectoryExample()
    
    try:
        # Run home motion
        success = node.run_home_motion()
        
        if success:
            node.get_logger().info('Motion completed successfully!')
        else:
            node.get_logger().error('Motion failed')
    except KeyboardInterrupt:
        node.get_logger().info('Interrupted by user')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pick and Place Example for UR5

Demonstrates a complete pick and place task using MoveIt2.
"""

import rclpy
from rclpy.node import Node
from moveit_msgs.srv import GetPlanningScene, GetPositionFK, GetPositionIK
from moveit_msgs.msg import PlanningScene, Constraints, PositionConstraint, OrientationConstraint
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
from sensor_msgs.msg import JointState
import math


class PickPlaceExample(Node):
    """Example node for pick and place task."""
    
    def __init__(self):
        super().__init__('pick_place_example')
        
        # Create clients for MoveIt2 services
        self.planning_scene_client = self.create_client(
            GetPlanningScene,
            '/get_planning_scene'
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
        
        # Pick and place poses
        self.pick_pose = PoseStamped()
        self.pick_pose.header.frame_id = 'base_link'
        self.pick_pose.pose.position = Point(x=0.4, y=0.0, z=0.2)
        self.pick_pose.pose.orientation = Quaternion(w=1.0)
        
        self.place_pose = PoseStamped()
        self.place_pose.header.frame_id = 'base_link'
        self.place_pose.pose.position = Point(x=0.2, y=0.3, z=0.2)
        self.place_pose.pose.orientation = Quaternion(w=1.0)
        
        # Pre-grasp and post-grasp poses
        self.pre_grasp_pose = PoseStamped()
        self.pre_grasp_pose.header.frame_id = 'base_link'
        self.pre_grasp_pose.pose.position = Point(x=0.4, y=0.0, z=0.35)
        self.pre_grasp_pose.pose.orientation = Quaternion(w=1.0)
        
        self.get_logger().info('Pick and Place Example initialized')
    
    def wait_for_services(self, timeout_sec=10.0):
        """Wait for required services to be available."""
        self.get_logger().info('Waiting for services...')
        
        services_ready = True
        
        if not self.planning_scene_client.wait_for_service(timeout_sec=timeout_sec):
            self.get_logger().warn('Planning scene service not available')
            services_ready = False
        
        return services_ready
    
    def plan_to_pose(self, pose: PoseStamped) -> bool:
        """
        Plan and execute motion to a target pose.
        
        Note: This is a simplified example. In production, you would use
        the MoveIt2 Python API or action clients for full planning.
        """
        self.get_logger().info(f'Planning to pose: {pose.pose.position}')
        
        # In a full implementation, this would:
        # 1. Create a planning request
        # 2. Set the target pose
        # 3. Call the move_group action
        # 4. Execute the planned trajectory
        
        # For this example, we'll just log the intended motion
        self.get_logger().info(f'Would plan to position: x={pose.pose.position.x:.3f}, '
                               f'y={pose.pose.position.y:.3f}, z={pose.pose.position.z:.3f}')
        
        return True
    
    def run_pick_place(self):
        """Execute a complete pick and place sequence."""
        self.get_logger().info('Starting pick and place sequence...')
        
        # Step 1: Move to pre-grasp position
        self.get_logger().info('Step 1: Moving to pre-grasp position')
        if not self.plan_to_pose(self.pre_grasp_pose):
            return False
        
        # Step 2: Move to pick position
        self.get_logger().info('Step 2: Moving to pick position')
        if not self.plan_to_pose(self.pick_pose):
            return False
        
        # Step 3: Close gripper (simulated)
        self.get_logger().info('Step 3: Closing gripper')
        
        # Step 4: Move to pre-grasp position (lift)
        self.get_logger().info('Step 4: Lifting object')
        if not self.plan_to_pose(self.pre_grasp_pose):
            return False
        
        # Step 5: Move to place position
        self.get_logger().info('Step 5: Moving to place position')
        if not self.plan_to_pose(self.place_pose):
            return False
        
        # Step 6: Open gripper (simulated)
        self.get_logger().info('Step 6: Opening gripper')
        
        # Step 7: Move to home position
        self.get_logger().info('Step 7: Returning to home position')
        home_pose = PoseStamped()
        home_pose.header.frame_id = 'base_link'
        home_pose.pose.position = Point(x=0.3, y=-0.3, z=0.3)
        home_pose.pose.orientation = Quaternion(w=1.0)
        if not self.plan_to_pose(home_pose):
            return False
        
        self.get_logger().info('Pick and place sequence completed!')
        return True


def main(args=None):
    """Main entry point."""
    rclpy.init(args=args)
    
    node = PickPlaceExample()
    
    try:
        # Wait for services
        if not node.wait_for_services():
            node.get_logger().error('Required services not available')
            return
        
        # Run pick and place sequence
        success = node.run_pick_place()
        
        if success:
            node.get_logger().info('Pick and place task completed successfully!')
        else:
            node.get_logger().error('Pick and place task failed')
    except KeyboardInterrupt:
        node.get_logger().info('Interrupted by user')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

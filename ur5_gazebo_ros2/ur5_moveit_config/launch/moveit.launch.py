#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MoveIt2 Launch File for UR5

Launches MoveIt2 move_group node for motion planning.
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def launch_setup(context, *args, **kwargs):
    """Main MoveIt2 launch setup."""
    
    # Configurations
    use_sim_time = LaunchConfiguration('use_sim_time')
    
    # Package paths
    ur5_moveit_share = FindPackageShare('ur5_moveit_config')
    ur5_description_share = FindPackageShare('ur5_description')
    
    # Robot description
    robot_description_content = PathJoinSubstitution([
        ur5_description_share,
        'urdf',
        'ur5.urdf.xacro'
    ])
    
    # MoveIt2 move_group node
    move_group_node = Node(
        package='moveit_ros_move_group',
        executable='move_group',
        name='move_group',
        output='screen',
        parameters=[
            # Robot description
            {'robot_description': robot_description_content},
            
            # Planning
            {'planning_scene_monitor.publish_geometry_updates': True},
            {'planning_scene_monitor.publish_state_updates': True},
            {'planning_scene_monitor.publish_transforms_updates': True},
            
            # MoveIt2 configuration
            PathJoinSubstitution([ur5_moveit_share, 'config', 'kinematics.yaml']),
            PathJoinSubstitution([ur5_moveit_share, 'config', 'joint_limits.yaml']),
            PathJoinSubstitution([ur5_moveit_share, 'config', 'ur5.srdf']),
            PathJoinSubstitution([ur5_moveit_share, 'config', 'moveit_controllers.yaml']),
            
            # Use sim time for Gazebo
            {'use_sim_time': use_sim_time},
            
            # Planning pipeline
            {'move_group.plan_execution.max_retry_attempts': 5},
            
            # Capabilities
            {'move_group.capabilities': ''},
            
            # Allowed planning time
            {'planning_time.default': 5.0},
        ],
        remappings=[
            ('/follow_joint_trajectory', '/joint_trajectory_controller/follow_joint_trajectory'),
        ]
    )
    
    return [
        move_group_node,
    ]


def generate_launch_description():
    """Generate MoveIt2 launch description."""
    
    # Declare arguments
    use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use simulation time (for Gazebo)'
    )
    
    return LaunchDescription([
        use_sim_time_arg,
        OpaqueFunction(function=launch_setup),
    ])

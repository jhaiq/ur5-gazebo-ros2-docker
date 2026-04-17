#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UR5 Controller Launch File

Launches ros2_control controller manager and controllers.
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def launch_setup(context, *args, **kwargs):
    """Main controller launch setup."""
    
    # Configurations
    controller_config = LaunchConfiguration('controller_config')
    
    # Controller manager node
    controller_manager = Node(
        package='controller_manager',
        executable='ros2_control_node',
        name='controller_manager',
        parameters=[
            controller_config,
            {'robot_description': PathJoinSubstitution([
                FindPackageShare('ur5_description'),
                'urdf',
                'ur5.urdf.xacro'
            ])},
        ],
        remappings=[
            ('/controller_manager/robot_description', '/robot_description'),
        ],
        output='screen'
    )
    
    # Joint state broadcaster spawner
    joint_state_broadcaster = Node(
        package='controller_manager',
        executable='spawner',
        arguments=[
            'joint_state_broadcaster',
            '--controller-manager', '/controller_manager',
            '--controller-manager-timeout', '10',
        ],
        output='screen'
    )
    
    # Joint trajectory controller spawner
    joint_trajectory_controller = Node(
        package='controller_manager',
        executable='spawner',
        arguments=[
            'joint_trajectory_controller',
            '--controller-manager', '/controller_manager',
            '--controller-manager-timeout', '10',
        ],
        output='screen'
    )
    
    return [
        controller_manager,
        joint_state_broadcaster,
        joint_trajectory_controller,
    ]


def generate_launch_description():
    """Generate controller launch description."""
    
    # Declare arguments
    controller_config_arg = DeclareLaunchArgument(
        'controller_config',
        default_value=PathJoinSubstitution([
            FindPackageShare('ur5_control'),
            'config',
            'ur5_controllers.yaml'
        ]),
        description='Controller configuration file'
    )
    
    return LaunchDescription([
        controller_config_arg,
        OpaqueFunction(function=launch_setup),
    ])

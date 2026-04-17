#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
RViz2 Launch File for UR5

Launches RViz2 with the UR5 robot configuration.
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    """Generate RViz2 launch description."""
    
    # Declare arguments
    rviz_config_arg = DeclareLaunchArgument(
        'rviz_config',
        default_value=PathJoinSubstitution([
            FindPackageShare('ur5_bringup'),
            'config',
            'ur5.rviz'
        ]),
        description='RViz2 configuration file'
    )
    
    rviz_config = LaunchConfiguration('rviz_config')
    
    # RViz2 node
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config],
        output='screen',
        remappings=[
            ('/joint_states', '/joint_states'),
            ('/robot_description', '/robot_description'),
        ]
    )
    
    return LaunchDescription([
        rviz_config_arg,
        rviz_node,
    ])

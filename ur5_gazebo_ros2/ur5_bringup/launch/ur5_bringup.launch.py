#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UR5 Bringup Launch File

Launches the complete UR5 simulation system including:
- Robot state publisher
- Joint state broadcaster
- Joint trajectory controller
- Gazebo simulation
- RViz2 visualization (optional)
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, OpaqueFunction
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def launch_setup(context, *args, **kwargs):
    """Main launch setup."""
    
    # Configurations
    use_rviz = LaunchConfiguration('use_rviz')
    rviz_config = LaunchConfiguration('rviz_config')
    world_name = LaunchConfiguration('world_name')
    
    # Package paths
    ur5_bringup_share = FindPackageShare('ur5_bringup')
    ur5_gazebo_share = FindPackageShare('ur5_gazebo')
    ur5_control_share = FindPackageShare('ur5_control')
    
    # Robot description
    robot_description_path = PathJoinSubstitution([
        FindPackageShare('ur5_description'),
        'urdf',
        'ur5.urdf.xacro'
    ])
    
    # Robot state publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': PathJoinSubstitution([
                FindPackageShare('ur5_description'),
                'urdf',
                'ur5.urdf.xacro'
            ])
        }]
    )
    
    # Joint state broadcaster
    joint_state_broadcaster = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_state_broadcaster'],
        output='screen'
    )
    
    # Joint trajectory controller
    joint_trajectory_controller = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_trajectory_controller'],
        output='screen'
    )
    
    # Controller manager
    controller_manager = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=[
            PathJoinSubstitution([ur5_control_share, 'config', 'ur5_controllers.yaml']),
        ],
        remappings=[
            ('/controller_manager/robot_description', '/robot_description'),
        ],
        output='screen'
    )
    
    # RViz2 (optional)
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config],
        condition=IfCondition(use_rviz),
        output='screen'
    )
    
    # Gazebo simulation
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([ur5_gazebo_share, 'launch', 'gazebo.launch.py'])
        ]),
        launch_arguments={
            'world_name': world_name,
        }.items()
    )
    
    return [
        robot_state_publisher,
        controller_manager,
        joint_state_broadcaster,
        joint_trajectory_controller,
        gazebo_launch,
        rviz_node,
    ]


def generate_launch_description():
    """Generate launch description."""
    
    # Declare arguments
    use_rviz_arg = DeclareLaunchArgument(
        'use_rviz',
        default_value='true',
        description='Launch RViz2 visualization'
    )
    
    rviz_config_arg = DeclareLaunchArgument(
        'rviz_config',
        default_value=PathJoinSubstitution([
            FindPackageShare('ur5_bringup'),
            'config',
            'ur5.rviz'
        ]),
        description='RViz2 configuration file'
    )
    
    world_name_arg = DeclareLaunchArgument(
        'world_name',
        default_value='empty.world',
        description='Gazebo world file name'
    )
    
    return LaunchDescription([
        use_rviz_arg,
        rviz_config_arg,
        world_name_arg,
        OpaqueFunction(function=launch_setup),
    ])

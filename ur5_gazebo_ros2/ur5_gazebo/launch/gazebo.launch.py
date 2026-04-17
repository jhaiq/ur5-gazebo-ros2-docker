#!/usr/bin/env python3
"""Launch UR5 in Gazebo simulation."""

import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    # Launch arguments
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    world = LaunchConfiguration('world', default='empty.sdf')
    
    # Paths
    pkg_share = FindPackageShare(package='ur5_gazebo').find('ur5_gazebo')
    pkg_ur5_desc = FindPackageShare(package='ur5_description').find('ur5_description')
    
    # Default world path
    default_world = os.path.join(pkg_share, 'worlds', 'empty.sdf')
    
    # Gazebo launch
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            ])
        ]),
        launch_arguments={
            'world': default_world,
            'extra_gazebo_args': '--verbose'
        }.items()
    )
    
    # Spawn UR5 robot
    spawn_robot = Node(
        package='ur5_gazebo',
        executable='spawn_ur5.py',
        name='spawn_ur5',
        output='screen',
        parameters=[
            {'use_sim_time': use_sim_time}
        ]
    )
    
    # Robot state publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'use_sim_time': use_sim_time,
            'robot_description': LaunchConfiguration('robot_description')
        }],
        arguments=[os.path.join(pkg_ur5_desc, 'urdf', 'ur5.urdf.xacro')]
    )
    
    # Joint state publisher
    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        parameters=[{'use_sim_time': use_sim_time}]
    )
    
    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value='empty.sdf',
            description='Gazebo world file'
        ),
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation time'
        ),
        gazebo_launch,
        spawn_robot,
        robot_state_publisher,
        joint_state_publisher,
    ])

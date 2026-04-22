#!/usr/bin/env python3
"""Launch UR5 in Gazebo simulation."""

import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    # Launch arguments
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    
    # Paths
    pkg_share = FindPackageShare(package='ur5_gazebo')
    pkg_ur5_desc = FindPackageShare(package='ur5_description')
    
    # Default world path
    default_world = os.path.join(
        pkg_ur5_desc.perform(None),  # This won't work at launch time, use path substitution
        'worlds', 'empty.sdf'
    )
    
    # Robot description (process xacro)
    xacro_path = os.path.join(
        pkg_ur5_desc.perform(None),
        'urdf', 'ur5.urdf.xacro'
    )
    robot_description = Command(['xacro ', xacro_path])
    
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
            'world': PathJoinSubstitution([pkg_share, 'worlds', 'empty.sdf']),
            'extra_gazebo_args': '--verbose'
        }.items()
    )
    
    # Robot state publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'use_sim_time': use_sim_time,
            'robot_description': robot_description
        }]
    )
    
    # Joint state publisher
    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        parameters=[{'use_sim_time': use_sim_time}]
    )
    
    # Spawn UR5 robot (with robot_description passed as parameter)
    spawn_robot = Node(
        package='ur5_gazebo',
        executable='spawn_ur5.py',
        name='spawn_ur5',
        output='screen',
        parameters=[
            {'use_sim_time': use_sim_time},
            {'robot_description': robot_description}
        ]
    )
    
    # Controller manager
    controller_manager = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=[
            {'use_sim_time': use_sim_time},
            {'robot_description': robot_description},
            os.path.join(pkg_ur5_desc.perform(None), '..', 'ur5_control', 'config', 'ur5_controllers.yaml')
        ],
        output='screen'
    )
    
    # Spawn controllers
    load_joint_state_broadcaster = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active',
             'joint_state_broadcaster'],
        output='screen'
    )
    
    load_joint_trajectory_controller = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active',
             'joint_trajectory_controller'],
        output='screen'
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
        robot_state_publisher,
        joint_state_publisher,
        spawn_robot,
        controller_manager,
        load_joint_state_broadcaster,
        load_joint_trajectory_controller,
    ])

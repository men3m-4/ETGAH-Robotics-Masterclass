"""
Launch file for ma_robot.

Usage:
    ros2 launch ma_robot_description display.launch.py
    ros2 launch ma_robot_description display.launch.py namespace:=robot1
"""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction
from launch.substitutions import Command, FindExecutable, LaunchConfiguration
from launch_ros.actions import Node, PushRosNamespace
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    package_share = get_package_share_directory(
        'ma_robot_description'
    )

    xacro_file = os.path.join(
        package_share,
        'urdf',
        'ma_robot.urdf.xacro',
    )

    rviz_file = os.path.join(
        package_share,
        'rviz',
        'display.rviz',
    )

    namespace = LaunchConfiguration('namespace')
    prefix = LaunchConfiguration('prefix')

    robot_description = ParameterValue(
        Command([
            FindExecutable(name='xacro'),
            ' ',
            xacro_file,
            ' prefix:=',
            prefix,
        ]),
        value_type=str,
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'namespace',
            default_value='',
            description='ROS 2 namespace',
        ),

        DeclareLaunchArgument(
            'prefix',
            default_value='',
            description='Prefix added to URDF links and joints',
        ),

        GroupAction([
            PushRosNamespace(namespace),

            Node(
                package='robot_state_publisher',
                executable='robot_state_publisher',
                name='robot_state_publisher',
                output='screen',
                parameters=[{
                    'robot_description': robot_description,
                }],
            ),

            Node(
                package='joint_state_publisher_gui',
                executable='joint_state_publisher_gui',
                name='joint_state_publisher_gui',
                output='screen',
                parameters=[{
                    'robot_description': robot_description,
                }],
            ),

            Node(
                package='rviz2',
                executable='rviz2',
                name='rviz2',
                output='screen',
                arguments=['-d', rviz_file],
            ),
        ]),
    ])
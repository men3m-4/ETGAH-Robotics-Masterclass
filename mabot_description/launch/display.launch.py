

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription

from launch_ros.actions import Node


def generate_launch_description():

    package_share = get_package_share_directory(
        'mabot_description'
    )

    rviz_file = os.path.join(
        package_share,
        'rviz',
        'display.rviz',
    )

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=[
            '-d',
            rviz_file,
        ],
        parameters=[{
            'use_sim_time': True,
        }],
    )

    return LaunchDescription([
        rviz,
    ])
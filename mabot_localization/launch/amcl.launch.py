"""Launch map server and AMCL for MABot."""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    """Load the map bundled with mabot_localization and activate AMCL."""
    localization_share = get_package_share_directory(
        'mabot_localization'
    )

    default_map = os.path.join(
        localization_share, 'map', 'mabot_world_map.yaml'
    )
    default_params = os.path.join(
        localization_share, 'config', 'amcl.yaml'
    )

    use_sim_time = ParameterValue(
        LaunchConfiguration('use_sim_time'),
        value_type=bool,
    )

    map_server = Node(
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        output='screen',
        parameters=[{
            'use_sim_time': use_sim_time,
            'yaml_filename': ParameterValue(
                LaunchConfiguration('map'),
                value_type=str,
            ),
        }],
    )

    amcl = Node(
        package='nav2_amcl',
        executable='amcl',
        name='amcl',
        output='screen',
        parameters=[
            LaunchConfiguration('params_file'),
            {'use_sim_time': use_sim_time},
        ],
    )

    lifecycle_manager = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager_localization',
        output='screen',
        parameters=[{
            'use_sim_time': use_sim_time,
            'autostart': True,
            'node_names': ['map_server', 'amcl'],
        }],
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
        ),
        DeclareLaunchArgument(
            'map',
            default_value=default_map,
            description='Full path to the saved occupancy map YAML.',
        ),
        DeclareLaunchArgument(
            'params_file',
            default_value=default_params,
            description='Full path to the AMCL parameter file.',
        ),
        map_server,
        amcl,
        lifecycle_manager,
    ])
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():

    package_share = get_package_share_directory('mabot_slam')
    slam_share = get_package_share_directory('slam_toolbox')

    default_params_file = os.path.join(
        package_share,
        'config',
        'slam_mapping.yaml',
    )

    # Use the Gazebo clock by default.
    declare_use_sim_time = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation time from /clock.',
    )

    # Allow a different configuration file when needed.
    declare_slam_params_file = DeclareLaunchArgument(
        'slam_params_file',
        default_value=default_params_file,
        description='Full path to the SLAM mapping parameters.',
    )

    # Gazebo, bridges and robot_state_publisher must already be running.
    # The official launch starts and activates the SLAM lifecycle node.
    mapping = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                slam_share,
                'launch',
                'online_async_launch.py',
            )
        ),
        launch_arguments={
            'use_sim_time': LaunchConfiguration('use_sim_time'),
            'slam_params_file': LaunchConfiguration('slam_params_file'),
            'autostart': 'true',
            'use_lifecycle_manager': 'false',
        }.items(),
    )

    return LaunchDescription([
        declare_use_sim_time,
        declare_slam_params_file,
        mapping,
    ])
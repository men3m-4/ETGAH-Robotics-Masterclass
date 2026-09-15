# Copyright 2026 Mohamed Abdelmoniem
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    package_dir = Path(
        get_package_share_directory("mabot_navigation")
    )
    config_dir = package_dir / "config"

    map_file = LaunchConfiguration("map")

    # All configurations in this package target Gazebo simulation.
    simulation_parameters = {"use_sim_time": True}

    map_server = Node(
        package="nav2_map_server",
        executable="map_server",
        name="map_server",
        output="screen",
        parameters=[
            simulation_parameters,
            {
                "yaml_filename": ParameterValue(
                    map_file, value_type=str
                ),
                "frame_id": "map",
                "topic_name": "map",
            },
        ],
    )

    amcl = Node(
        package="nav2_amcl",
        executable="amcl",
        name="amcl",
        output="screen",
        parameters=[
            str(config_dir / "amcl.yaml"),
            simulation_parameters,
        ],
    )

    planner_server = Node(
        package="nav2_planner",
        executable="planner_server",
        name="planner_server",
        output="screen",
        parameters=[
            str(config_dir / "planner_server.yaml"),
            simulation_parameters,
        ],
    )

    controller_server = Node(
        package="nav2_controller",
        executable="controller_server",
        name="controller_server",
        output="screen",
        parameters=[
            str(config_dir / "controller_server.yaml"),
            simulation_parameters,
        ],
        remappings=[
            ("cmd_vel", "/cmd_vel"),
        ],
    )

    behavior_server = Node(
        package="nav2_behaviors",
        executable="behavior_server",
        name="behavior_server",
        output="screen",
        parameters=[
            str(config_dir / "behavior_server.yaml"),
            simulation_parameters,
        ],
        remappings=[
            ("cmd_vel", "/cmd_vel"),
        ],
    )

    bt_navigator = Node(
        package="nav2_bt_navigator",
        executable="bt_navigator",
        name="bt_navigator",
        output="screen",
        parameters=[
            str(config_dir / "bt_navigator.yaml"),
            simulation_parameters,
        ],
    )

    lifecycle_manager_localization = Node(
        package="nav2_lifecycle_manager",
        executable="lifecycle_manager",
        name="lifecycle_manager_localization",
        output="screen",
        parameters=[
            simulation_parameters,
            {
                "autostart": True,
                "node_names": [
                    "map_server",
                    "amcl",
                ],
            },
        ],
    )

    lifecycle_manager_navigation = Node(
        package="nav2_lifecycle_manager",
        executable="lifecycle_manager",
        name="lifecycle_manager_navigation",
        output="screen",
        parameters=[
            simulation_parameters,
            {
                "autostart": True,
                "node_names": [
                    "planner_server",
                    "controller_server",
                    "behavior_server",
                    "bt_navigator",
                ],
            },
        ],
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "map",
                description="Absolute path to the saved map YAML file",
            ),
            map_server,
            amcl,
            planner_server,
            controller_server,
            behavior_server,
            bt_navigator,
            lifecycle_manager_localization,
            lifecycle_manager_navigation,
        ]
    )
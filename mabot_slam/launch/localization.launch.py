import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    EmitEvent,
    OpaqueFunction,
    RegisterEventHandler,
)
from launch.events import matches_action
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import LifecycleNode
from launch_ros.event_handlers import OnStateTransition
from launch_ros.events.lifecycle import ChangeState
from launch_ros.parameter_descriptions import ParameterValue

from lifecycle_msgs.msg import Transition


def launch_setup(context):
    params_file = os.path.abspath(os.path.expanduser(
        LaunchConfiguration('slam_params_file').perform(context)
    ))

    posegraph_file = os.path.abspath(os.path.expanduser(
        LaunchConfiguration('posegraph_file').perform(context)
    ))

    # Expect a prefix without .posegraph or .data.
    if posegraph_file.endswith(('.posegraph', '.data')):
        raise RuntimeError(
            'posegraph_file must be a path prefix without '
            'the .posegraph or .data extension.'
        )

    # Validate configuration and both serialized graph files.
    required_files = [
        params_file,
        posegraph_file + '.posegraph',
        posegraph_file + '.data',
    ]

    for path in required_files:
        if not os.path.isfile(path):
            raise RuntimeError(f'Required file not found: {path}')
        if os.path.getsize(path) == 0:
            raise RuntimeError(f'Required file is empty: {path}')

    # Gazebo, bridges and robot_state_publisher run separately.
    localization = LifecycleNode(
        package='slam_toolbox',
        executable='localization_slam_toolbox_node',
        name='slam_toolbox',
        namespace='',
        output='screen',
        parameters=[
            params_file,
            {
                'use_sim_time': ParameterValue(
                    LaunchConfiguration('use_sim_time'),
                    value_type=bool,
                ),
                'use_lifecycle_manager': False,
                'mode': 'localization',
                'map_file_name': posegraph_file,
            },
        ],
    )

    # Register activation before requesting configuration.
    activate_when_configured = RegisterEventHandler(
        OnStateTransition(
            target_lifecycle_node=localization,
            start_state='configuring',
            goal_state='inactive',
            entities=[
                EmitEvent(
                    event=ChangeState(
                        lifecycle_node_matcher=matches_action(localization),
                        transition_id=Transition.TRANSITION_ACTIVATE,
                    )
                ),
            ],
        )
    )

    configure = EmitEvent(
        event=ChangeState(
            lifecycle_node_matcher=matches_action(localization),
            transition_id=Transition.TRANSITION_CONFIGURE,
        )
    )

    return [
        localization,
        activate_when_configured,
        configure,
    ]


def generate_launch_description():
    package_share = get_package_share_directory('mabot_slam')

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use the Gazebo simulation clock.',
        ),
        DeclareLaunchArgument(
            'slam_params_file',
            default_value=os.path.join(
                package_share,
                'config',
                'slam_localization.yaml',
            ),
            description='Full path to the localization configuration.',
        ),
        DeclareLaunchArgument(
            'posegraph_file',
            default_value=os.path.join(
                package_share,
                'posegraph',
                'mabot_world',
            ),
            description='Serialized pose graph prefix without extension.',
        ),
        OpaqueFunction(function=launch_setup),
    ])
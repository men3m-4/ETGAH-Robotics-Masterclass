import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
)
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
)

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():

    package_share = get_package_share_directory(
        'ma_robot_description'
    )

    ros_gz_share = get_package_share_directory(
        'ros_gz_sim'
    )

    # ---------------------------------------------------------
    # Launch arguments
    # ---------------------------------------------------------

    # False:
    #   Run Gazebo Server only and use the ETGAH 3D Simulator
    #   as the graphical interface.
    #
    # True:
    #   Run the normal Gazebo graphical interface when launching
    #   the project outside the ETGAH simulator.
    #
    # Standalone usage:
    # ros2 launch ma_robot_description gazebo.launch.py \
    #   use_gazebo_gui:=true
    use_gazebo_gui = LaunchConfiguration(
        'use_gazebo_gui'
    )

    declare_use_gazebo_gui = DeclareLaunchArgument(
        'use_gazebo_gui',
        default_value='false',
        description=(
            'Start the local Gazebo GUI. Keep false when using '
            'the ETGAH 3D Simulator.'
        ),
    )

    # ---------------------------------------------------------
    # Package files
    # ---------------------------------------------------------

    # Robot Xacro
    xacro_file = os.path.join(
        package_share,
        'urdf',
        'ma_robot.urdf.xacro',
    )

    # Gazebo world
    world_file = os.path.join(
        package_share,
        'worlds',
        'ma_robot_world.sdf',
    )

    # ROS 2 <-> Gazebo bridge configuration
    bridge_config_file = os.path.join(
        package_share,
        'config',
        'gz_bridge.yaml',
    )

    robot_description = ParameterValue(
        Command([
            FindExecutable(name='xacro'),
            ' ',
            xacro_file,
        ]),
        value_type=str,
    )

    # ---------------------------------------------------------
    # Gazebo
    # ---------------------------------------------------------

    # Start Gazebo Server only.
    #
    # -r: Start the simulation immediately.
    # -s: Run the Gazebo server without its local GUI.
    # -v2: Set the Gazebo message verbosity level.
    #
    # The ETGAH 3D Simulator connects to this server and provides
    # the graphical interface.
    gazebo_server = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                ros_gz_share,
                'launch',
                'gz_sim.launch.py',
            )
        ),
        launch_arguments={
            'gz_args': [
                '-r -s -v2 ',
                world_file,
            ],
            'on_exit_shutdown': 'true',
        }.items(),
    )

    # Start the Gazebo graphical client only when requested.
    #
    # Use this command when running outside ETGAH:
    #
    # ros2 launch ma_robot_description gazebo.launch.py \
    #   use_gazebo_gui:=true
    gazebo_gui = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                ros_gz_share,
                'launch',
                'gz_sim.launch.py',
            )
        ),
        launch_arguments={
            'gz_args': '-g -v2',
            'on_exit_shutdown': 'true',
        }.items(),
        condition=IfCondition(use_gazebo_gui),
    )

    # ---------------------------------------------------------
    # Robot state publisher
    # ---------------------------------------------------------

    # Publish the robot description and its TF tree.
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description,
            'use_sim_time': True,
        }],
    )

    # ---------------------------------------------------------
    # Spawn robot
    # ---------------------------------------------------------

    # Spawn the robot inside Gazebo using robot_description.
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        name='spawn_ma_robot',
        output='screen',
        arguments=[
            '-name', 'ma_robot',
            '-topic', 'robot_description',
            '-x', '0.0',
            '-y', '0.0',
            '-z', '0.10',
        ],
    )

    # ---------------------------------------------------------
    # ROS 2 <-> Gazebo parameter bridge
    # ---------------------------------------------------------

    # Topics such as /clock, /cmd_vel, /odom, /tf, /scan,
    # /joint_states, depth image, camera info and point cloud
    # are configured inside config/gz_bridge.yaml.
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='gazebo_bridge',
        output='screen',
        parameters=[{
            'config_file': bridge_config_file,
            'use_sim_time': True,
        }],
    )

    # ---------------------------------------------------------
    # RGB image bridge
    # ---------------------------------------------------------

    # Subscribe to the Gazebo image topic:
    #   /camera/image
    #
    # Publish it in ROS 2 using the standard camera topic:
    #   /camera/image_raw
    #
    # ros_gz_image is optimized specifically for image transport.
    camera_image_bridge = Node(
        package='ros_gz_image',
        executable='image_bridge',
        name='camera_image_bridge',
        output='screen',
        arguments=[
            '/camera/image',
        ],
        remappings=[
            (
                '/camera/image',
                '/camera/image_raw',
            ),
        ],
        parameters=[{
            'use_sim_time': True,
        }],
    )

    return LaunchDescription([
        declare_use_gazebo_gui,

        gazebo_server,
        gazebo_gui,

        robot_state_publisher,
        spawn_robot,

        bridge,
        camera_image_bridge,
    ])
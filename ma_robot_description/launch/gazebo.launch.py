import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, FindExecutable

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():

    package_share = get_package_share_directory(
        'ma_robot_description'
    )

    ros_gz_share = get_package_share_directory(
        'ros_gz_sim'
    )

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

    robot_description = ParameterValue(
        Command([
            FindExecutable(name='xacro'),
            ' ',
            xacro_file,
        ]),
        value_type=str,
    )

    # Start Gazebo Harmonic
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                ros_gz_share,
                'launch',
                'gz_sim.launch.py',
            )
        ),
        launch_arguments={
            'gz_args': '-r ' + world_file,
            'on_exit_shutdown': 'true',
        }.items(),
    )

    # Publish robot description and transforms
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

    # Spawn robot inside Gazebo
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

    # Bridge Gazebo topics with ROS 2
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='gazebo_bridge',
        output='screen',
        arguments=[
            # Gazebo -> ROS 2
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
            '/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry',
            '/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V',

            # Wheel joint states: Gazebo -> ROS 2
            '/joint_states@sensor_msgs/msg/JointState[gz.msgs.Model',

            # ROS 2 -> Gazebo
            '/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist',

            # RPLIDAR S2
            '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan',

            # ZED2 RGB-D camera
            '/camera/image@sensor_msgs/msg/Image[gz.msgs.Image',
            '/camera/depth_image@sensor_msgs/msg/Image[gz.msgs.Image',
            '/camera/camera_info@sensor_msgs/msg/CameraInfo'
            '[gz.msgs.CameraInfo',
            '/camera/points@sensor_msgs/msg/PointCloud2'
            '[gz.msgs.PointCloudPacked',
        ],
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn_robot,
        bridge,
    ])
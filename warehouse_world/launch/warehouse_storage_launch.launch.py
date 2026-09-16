import os
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='True')
    bringup_dir = get_package_share_directory('warehouse_world')

    world = os.path.join(bringup_dir, "worlds", "warehouse_storage.sdf")
    
    gz_resource_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=':'.join([
            os.path.join(bringup_dir, 'worlds'),
            os.path.join(bringup_dir, 'models'),
            str(Path(bringup_dir).parent.resolve())
        ])
    )

  


    # Launch Gazebo Sim
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory("ros_gz_sim"),
                         "launch", "gz_sim.launch.py")
        ),
        launch_arguments={"gz_args": ["-r -s -v 4 ", world]}.items(),  #gazebo headless mode

    )

    # Launch ROS-Gazebo bridge
    ros_gz_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        parameters=[{
            'config_file': os.path.join(bringup_dir, 'config', 'gz_bridge_ros.yaml'),
            'use_sim_time': use_sim_time}],
        output='screen'
    )



    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='True',
            description='Use simulation time'
        ),
        gz_resource_path,
        gz_sim,
        ros_gz_bridge,
    ])

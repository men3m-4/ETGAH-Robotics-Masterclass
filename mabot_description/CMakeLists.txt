cmake_minimum_required(VERSION 3.8)

project(mabot_description)

find_package(ament_cmake REQUIRED)

# Install package resources
install(
  DIRECTORY
    urdf
    meshes
    launch
    rviz
    config
    worlds
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
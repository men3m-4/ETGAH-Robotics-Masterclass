cmake_minimum_required(VERSION 3.8)
project(mabot_slam)

find_package(ament_cmake REQUIRED)

# Install launch files, configurations and saved mapping resources.
install(
  DIRECTORY
    config
    launch
    rviz
    map
    posegraph
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
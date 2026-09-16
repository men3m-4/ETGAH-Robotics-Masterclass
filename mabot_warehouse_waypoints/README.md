# MABot Warehouse Waypoints

Record warehouse locations in RViz and execute an autonomous delivery mission using MABot, ROS 2 Jazzy, Gazebo Harmonic, and Nav2.

The mission starts at **Home**, visits **Loading**, **Storage**, and **Shipping**, and returns to **Home**. The robot waits for **30 seconds of simulation time** at Loading. RViz displays each named location, with the active navigation goal in green and inactive locations in blue.

> Version scope: this guide documents the working recorder, runner, and `warehouse_mission` implementation used in the project demonstration. The GitHub snapshot inspected while preparing this guide still had an empty `console_scripts` list and did not expose the three Python modules at the paths below. Publish the working source files and packaging changes alongside this README; adding the README alone does not install these commands.

## Contents

- [Package responsibilities](#package-responsibilities)
- [Build and environment](#build-and-environment)
- [Start simulation and navigation](#start-simulation-and-navigation)
- [Configure RViz](#configure-rviz)
- [Record new waypoints](#record-new-waypoints)
- [Waypoint configuration](#waypoint-configuration)
- [Run the warehouse mission](#run-the-warehouse-mission)
- [How the mission works](#how-the-mission-works)


## Package responsibilities

| Component | Purpose |
| --- | --- |
| `waypoint_recorder` | Receives selected poses on `/waypoint_pose` and saves them to YAML. |
| `waypoint_runner` | Executes a generic waypoint list in file order using Nav2. |
| `warehouse_mission` | Executes the named warehouse route, checks the starting pose, handles the Loading wait, and publishes colored markers. |
| `mabot_description` | Provides the robot model, warehouse simulation launch, sensors, and ROSâ€“Gazebo bridges. |
| `mabot_slam` | Creates the map using SLAM Toolbox. |
| `mabot_navigation` | Loads the saved map and starts AMCL and the Nav2 servers. |

This package sends navigation goals; Nav2 performs path planning, obstacle handling, and motion control. Selecting a recording pose does not drive the robot. â€œCharging Stationâ€ is the name of the Home waypoint; the mission does not implement physical docking or battery charging.

### Working package layout

| Path | Description |
| --- | --- |
| `config/warehouse_waypoints.yaml` | Named poses in the map coordinate frame. |
| `mabot_warehouse_waypoints/__init__.py` | Python package initializer. |
| `mabot_warehouse_waypoints/waypoint_recorder.py` | Pose recorder. |
| `mabot_warehouse_waypoints/waypoint_runner.py` | Generic action client and shared runner logic. |
| `mabot_warehouse_waypoints/warehouse_mission.py` | Warehouse-specific mission and marker publisher. |
| `resource/mabot_warehouse_waypoints` | Ament package index marker. |
| `package.xml` | ROS dependencies. |
| `setup.py` / `setup.cfg` | Python installation and executable registration. |
| `README.md` | This guide. |

## Build and environment

Commands assume the existing project workspace:

```bash
cd ~/workspaces/ETGAH-Robotics-Masterclass
rosdep install --from-paths . --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
```

For later changes limited to this package:

```bash
colcon build --symlink-install --packages-select mabot_warehouse_waypoints
source install/setup.bash
ros2 pkg executables mabot_warehouse_waypoints
```

The executable list should contain `waypoint_recorder`, `waypoint_runner`, and `warehouse_mission`.

Run this preparation in **every new terminal** before the commands in this guide:

```bash
cd ~/workspaces/ETGAH-Robotics-Masterclass
source install/setup.bash
```

The working package needs `rclpy`, `geometry_msgs`, `nav2_msgs`, `action_msgs`, `visualization_msgs`, `tf2_ros`, and Python YAML support (`python3-yaml`). Simulation, SLAM, Nav2, and RViz must also be installed through the companion packages' dependencies.

### Executable registration

The working `setup.py` should register:

```python
entry_points={
    'console_scripts': [
        'waypoint_recorder = mabot_warehouse_waypoints.waypoint_recorder:main',
        'waypoint_runner = mabot_warehouse_waypoints.waypoint_runner:main',
        'warehouse_mission = mabot_warehouse_waypoints.warehouse_mission:main',
    ],
},
```

Install the configuration directory through `data_files` if you want it available in the installed package share directory. The commands below explicitly use the source YAML, so it is always clear which file is being edited and executed.

## Start simulation and navigation

### 1. Start the warehouse and MABot

Terminal 1:

```bash
ros2 launch mabot_description warehouse.launch.py
```

Use the ETGAH platform's simulator viewer. For a local desktop Gazebo GUI, the supplied launch supports:

```bash
ros2 launch mabot_description warehouse.launch.py use_gazebo_gui:=true
```

Use one of these commands, not both. Do not start another Gazebo server for the same session. The `warehouse_world` package must be discoverable in the sourced environment.

### 2. Load the saved map and Nav2

Stop any running SLAM mapping node before starting this localization workflow. Keep Gazebo running.

Terminal 2:

```bash
ros2 launch mabot_navigation nav2_bringup.launch.py \
  map:="$PWD/mabot_slam/map/mabot_warehouse_map.yaml"
```

This launch starts the map server, AMCL, planner, controller, behavior server, BT Navigator, and localization/navigation lifecycle managers.

Use the map that matches your saved waypoint coordinates. A `.rviz` file stores visualization settings; it is not a saved occupancy map. Keep the map `.yaml` and its referenced image file together.

### 3. Open RViz

Terminal 3:

```bash
ros2 run rviz2 rviz2 \
  -d "$PWD/mabot_navigation/rviz/navigation.rviz" \
  --ros-args -p use_sim_time:=true
```

### Optional: create a new map first

With Gazebo running and AMCL/Nav2 stopped:

```bash
ros2 launch mabot_slam mapping.launch.py
```

In another prepared terminal:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard \
  --ros-args -p speed:=0.15 -p turn:=0.3
```

Explore accessible aisles, corners, and open areas. Check scan alignment and avoid leaving large unexplored gaps. Save to a new filename to preserve the existing mission map:

```bash
mkdir -p mabot_slam/map
map_output="$PWD/mabot_slam/map/warehouse_recording_$(date +%Y%m%d_%H%M%S)"
ros2 run nav2_map_server map_saver_cli -f "$map_output" \
  --ros-args -p use_sim_time:=true -p save_map_timeout:=20.0
```

Keep both generated files. Stop mapping, then load the saved YAML with the navigation launch. Recheck or record waypoint coordinates when changing maps.

## Configure RViz

### Global settings and displays

Set **Global Options â†’ Fixed Frame â†’ `map`**. Use **Add â†’ By display type** for missing displays.

| Display | Topic / setting | What to check |
| --- | --- | --- |
| Map | `/map` | Complete saved warehouse map. Use Reliable / Transient Local. |
| RobotModel | Description topic `/robot_description` | Robot model and link positions. Use Reliable / Transient Local. |
| TF | Enable the frame tree | `map â†’ odom â†’ base_footprint â†’ base_link`. |
| LaserScan | `/scan` | Scan points align with walls. Use Best Effort if required by the publisher. |
| ParticleCloud (`nav2_rviz_plugins`) | `/particle_cloud` | AMCL hypotheses converge around the robot. |
| Map, renamed Global Costmap | `/global_costmap/costmap` | Set Color Scheme to `costmap`; reduce Alpha to see the map underneath. |
| Map, renamed Local Costmap | `/local_costmap/costmap` | Nearby obstacles and inflated areas. |
| Path, renamed Global Plan | `/plan` | Planned route to the current goal. |
| Path, renamed Local Plan | `/local_plan` | Controller's local path when published. |
| MarkerArray | `/warehouse_waypoints/markers` | Named station arrows and labels from `warehouse_mission`. |
| Image, optional | `/camera/image_raw` | Simulated camera feed when enabled. |
| PointCloud2, optional | `/camera/points` | RGB-D point cloud when enabled. |

The plan topics above match the project's RViz configuration. If a display is empty, inspect `ros2 topic list -t` and the publisher's QoS rather than guessing another topic. Plans may appear only during navigation.

For MarkerArray, select **Reliable** and **Transient Local** where these properties are exposed. The mission publisher uses this QoS so late subscribers can receive the latest markers while it remains alive.

### Set the initial robot pose

1. Select **2D Pose Estimate**.
2. Click the robot's actual location on the map.
3. Drag in its actual heading direction and release.
4. Check that the LiDAR scan matches the walls and that the particles converge.
5. Move a short distance and verify localization stays consistent.

This tool publishes an initial estimate on `/initialpose`. It does **not** physically move or teleport the robot. Never use it to pretend the robot is at Home just to pass the mission check.

### Know which goal tool you are using

| Tool | Interface | Effect |
| --- | --- | --- |
| 2D Pose Estimate | `/initialpose` | Initializes AMCL's pose estimate. |
| 2D Goal Pose configured for recording | `/waypoint_pose` (`PoseStamped`) | Saves a selected waypoint when the recorder is running. |
| 2D Goal Pose configured for navigation | `/goal_pose` | Requests navigation when the active navigation stack consumes this topic. |
| Nav2 Goal tool | Nav2 navigation action | Sends a navigation goal through the Nav2 RViz integration. |

For recording, use `rviz_default_plugins/SetGoal`, not the Nav2 action goal tool.

If **Add Tool** shows SetGoal as already present, edit the existing **2D Goal Pose** tool through **Panels â†’ Tool Properties**. Change its **Topic** to `/waypoint_pose`. Restore `/goal_pose` when using that tool for manual navigation afterward.

### Test a manual goal

Before automation, send one reachable goal using the navigation tool. Confirm the robot plans, moves, and reaches the requested position and heading. Avoid teleoperation or another goal sender while a mission owns navigation.

### Save the RViz configuration

Use **File â†’ Save Config As** and save to:

```text
mabot_navigation/rviz/navigation.rviz
```

Saving RViz settings preserves displays, topics, and the view. The waypoint YAML must be saved separately by the recorder or editor.

## Record new waypoints

### 1. Stop the previous recorder and mission

Press **Ctrl+C** in their terminals. In particular, stop the recorder before replacing the YAML: it keeps a waypoint list in memory and could otherwise write old entries back.

### 2. Back up and reset the waypoint file

Run from the workspace root:

```bash
python3 - <<'PY'
from datetime import datetime
from pathlib import Path
import shutil

path = Path('mabot_warehouse_waypoints/config/warehouse_waypoints.yaml')
path.parent.mkdir(parents=True, exist_ok=True)
if path.exists():
    backup = path.with_name(path.name + '.bak-' + datetime.now().strftime('%Y%m%d-%H%M%S-%f'))
    shutil.copy2(path, backup)
    print(f'Backup: {backup}')
path.write_text('frame_id: map\nwaypoints: []\n', encoding='utf-8')
print(f'Reset: {path}')
PY
```

### 3. Start recording

```bash
ros2 run mabot_warehouse_waypoints waypoint_recorder \
  --ros-args \
  -p use_sim_time:=true \
  -p output_file:="$PWD/mabot_warehouse_waypoints/config/warehouse_waypoints.yaml" \
  -p wait_seconds:=0.0
```

The recorder should report the output path, zero existing waypoints, and that it is waiting on `/waypoint_pose`.

### 4. Select four locations in RViz

With Fixed Frame set to `map` and the SetGoal tool topic set to `/waypoint_pose`, click and drag four poses in this order:

1. Home / Charging Station.
2. Loading Station.
3. Storage Area.
4. Shipping Station.

The click sets the position; the drag sets the final heading. Select free, reachable locations with room for the robot to turn. The recorder stores the pose you select, not the robot's current pose.

Each selection is saved as `station_01`, `station_02`, and so on. Repeating a click adds another entry. The recorder does not automatically assign warehouse roles.

### 5. Stop and name the locations

Press **Ctrl+C**, then edit the YAML:

```bash
nano mabot_warehouse_waypoints/config/warehouse_waypoints.yaml
```

Rename the four entries exactly to **`Home`**, **`Loading`**, **`Storage`**, and **`Shipping`**. Names are case-sensitive. Set Loading's `wait_seconds` to `30.0` and the others to `0.0`.

## Waypoint configuration

The recorded demonstration configuration is:

```yaml
frame_id: map
waypoints:
  - name: Home
    x: 5.7776
    y: -0.2179
    yaw: -1.63
    wait_seconds: 0.0
  - name: Loading
    x: 5.7805
    y: -1.4697
    yaw: -1.597
    wait_seconds: 30.0
  - name: Storage
    x: 1.7152
    y: -1.2704
    yaw: 2.8764
    wait_seconds: 0.0
  - name: Shipping
    x: 0.022
    y: 0.1107
    yaw: -0.0407
    wait_seconds: 0.0
```

Positions are in **meters** and yaw is in **radians**, all relative to `map`. These coordinates belong to this map and recording session; do not assume they match a newly generated map or another robot's spawn coordinates.

The generic runner follows YAML order and per-entry waits. The warehouse mission instead looks up the four required names and uses the fixed route **Loading â†’ Storage â†’ Shipping â†’ Home**, with a fixed 30-second Loading wait in the documented implementation. Keep the YAML waits consistent for readability, but editing them does not change that mission's fixed wait logic.

## Run the warehouse mission

### 1. Move to Home first

The robot must physically be at Home and correctly localized. If necessary, send a manual goal there. For the demonstration coordinates above:

```bash
ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose \
  "{pose: {header: {frame_id: map}, pose: {position: {x: 5.7776, y: -0.2179, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: -0.72773, w: 0.68587}}}}" \
  --feedback
```

Wait for success. If you recorded a different Home, use its coordinates and heading instead. The orientation above corresponds to yaw `-1.63` using `z = sin(yaw/2)` and `w = cos(yaw/2)`.

### 2. Start the mission

```bash
ros2 run mabot_warehouse_waypoints warehouse_mission \
  --ros-args \
  -p use_sim_time:=true \
  -p waypoints_file:="$PWD/mabot_warehouse_waypoints/config/warehouse_waypoints.yaml"
```

Watch the terminal, RViz markers, and robot motion. The logged node name can still be `waypoint_runner` because the mission reuses that runner's node implementation.

Expected sequence, summarized rather than an exact transcript:

```text
Wait for /navigate_to_pose
Check map -> base_footprint against Home
Navigate to Loading; wait for success
Wait 30 seconds of simulation time
Navigate to Storage; wait for success
Navigate to Shipping; wait for success
Navigate to Home; wait for success
Report mission completion
```

After success, the documented mission remains running to keep publishing markers. Press **Ctrl+C** when finished. To run another delivery cycle, restart the command after confirming the robot is still at Home.

### Generic runner for arbitrary routes

```bash
ros2 run mabot_warehouse_waypoints waypoint_runner \
  --ros-args \
  -p use_sim_time:=true \
  -p waypoints_file:="$PWD/mabot_warehouse_waypoints/config/warehouse_waypoints.yaml"
```

This is a separate mode. With the example file it visits Home first and ends at Shipping; it does not implement the warehouse mission's return-home ordering or its marker behavior. Use `warehouse_mission` for the assignment demonstration.

## How the mission works

1. Load and validate map-frame waypoint data and required names.
2. Wait for Nav2's `/navigate_to_pose` action server.
3. Read the current `map â†’ base_footprint` transform and compare it with Home.
4. Send one pose goal to Nav2 and wait for acceptance.
5. Highlight the accepted goal green and wait for its final action result.
6. On success, clear the active highlight, perform any mission wait, and send the next goal.
7. On rejection or an unsuccessful result, report the location and stop the route.
8. After returning Home successfully, report completion and retain the marker display.

The documented Home check allows approximately **0.30 m** position error and **0.35 rad** heading error. Both checks must pass. These checks use AMCL/TF pose estimates; they do not verify localization confidence independently.

### Timing and interruption

The Loading wait uses the ROS simulation clock. Pausing Gazebo pauses the wait; running simulation slower than real time makes the wall-clock wait longer. It targets 30 simulation seconds, with normal callback scheduling precision rather than hard real-time timing.

On Ctrl+C, the runner requests cancellation of an outstanding goal and reports the outcome. Check the cancellation result; a failed communication attempt is not confirmation that Nav2 stopped.

### Markers

Four locations are represented by an arrow and a text label each: eight marker objects for four named waypoints. Their publisher is `/warehouse_waypoints/markers` (`visualization_msgs/msg/MarkerArray`).

| State | Appearance |
| --- | --- |
| No accepted goal | All stations blue. |
| Navigating | Accepted active destination green; others blue. |
| Loading wait after arrival | All blue: the navigation goal has already completed. |
| Mission finished | All blue. |

The marker color represents the current navigation goal, not the robot's present station. Starting only the recorder does not publish these mission markers.
<!-- 
## Troubleshooting

| Symptom | Check / resolution |
| --- | --- |
| `No executable found` | Confirm the Python modules and `console_scripts` entries exist, rebuild, and source the workspace. The earlier GitHub skeleton did not include them. |
| Recorder stays waiting | Verify SetGoal publishes `/waypoint_pose`, Fixed Frame is `map`, and the recorder is running. |
| Robot moves when trying to record | You used a navigation tool/topic. Use SetGoal on `/waypoint_pose`. |
| Manual goal does not move the robot after recording | Restore `/goal_pose` or use the Nav2 Goal tool; check Nav2 is active. |
| Old points return after resetting | Stop the recorder before resetting; check the exact `output_file` path. |
| Required station missing | Rename generic entries to the exact case-sensitive mission names. |
| `Robot is not at Home` | Navigate physically to Home and wait for success. Also check localization and the selected map. |
| Waiting for Nav2 | Check `bt_navigator` and the other lifecycle nodes are active and `/navigate_to_pose` exists. |
| Missing `map â†’ base_footprint` | Check AMCL initialization, scan/odom bridges, TF, and simulation time. |
| MarkerArray is empty | Start `warehouse_mission`, select the correct topic, and check Fixed Frame/QoS. A failed mission may exit before you inspect it. |
| Loading wait never ends | Confirm Gazebo is unpaused and `/clock` is advancing. |
| Goal aborts | Inspect localization, costmaps, goal clearance, and Nav2's reported failure before rerunning. |
| Fast DDS shared-memory warning | Check whether communication actually fails. In the recorded Home-check failure, TF and Nav2 were reached; the explicit Home error caused the mission exit. |

Useful inspection commands:

```bash
ros2 topic list -t
ros2 action list -t
ros2 action info /navigate_to_pose
ros2 run tf2_ros tf2_echo map base_footprint
```

Run the following individually in another terminal as needed:

```bash
ros2 topic echo /waypoint_pose --once
ros2 topic echo /amcl_pose --once
ros2 topic echo /clock --once
ros2 topic info /warehouse_waypoints/markers --verbose
ros2 topic type /cmd_vel
```

For this project's configuration, `/cmd_vel` should be `geometry_msgs/msg/Twist`. A one-shot topic echo waits until a message arrives; click a recording pose or move the robot where appropriate.

Check lifecycle activation:

```bash
for node in map_server amcl planner_server controller_server behavior_server bt_navigator; do
  ros2 lifecycle get "/$node"
done
``` -->

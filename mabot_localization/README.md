<div align="center">

# MABot · AMCL Localization

**Finding MABot inside a saved map — from an incorrect pose to a concentrated particle cloud.**

ROS 2 Jazzy · Gazebo Harmonic · Nav2 AMCL · RViz2

[Demo](#demo) · [Results](#results) · [Run the project](#run-the-project) · [RViz](#rviz-configuration)


 <!-- · [Troubleshooting](#troubleshooting) -->

</div>

## Demo

<p align="center">
  <img src="images/V.gif" alt="MABot AMCL localization demonstration" width="900">
</p>

<!-- <p align="center">
  <a href="images/localization_demo.mp4"><strong>Watch / download the MP4 demonstration</strong></a>
</p> -->

MABot is a custom four-wheel skid-steer robot with an RPLIDAR S2 and a ZED 2 camera. This package localizes the robot in its simulated environment using a map saved during the previous SLAM assignment.

The localization launch starts **map_server**, **AMCL**, and a **lifecycle manager**. The saved YAML and PGM files are bundled inside this package. SLAM Toolbox is not launched during AMCL localization.

## Results

### 1 · Deliberately incorrect initial pose

<p align="center">
  <img src="images/wrong_initial_pose.png" alt="Incorrect initial pose: LiDAR returns are displaced from the saved walls" width="850">
</p>

The initial estimate was deliberately placed incorrectly using **2D Pose Estimate**. The red LiDAR returns are visibly displaced from the black occupied cells in the map, and the particle cloud is spread around the selected estimate.

### 2 · Corrected initial pose

<p align="center">
  <img src="images/correct_initial_pose.png" alt="Corrected initial pose with LiDAR returns aligned to the saved map" width="850">
</p>

After correcting both position and heading, LiDAR returns align much more closely with the walls and obstacles. The particle cloud is still broad at this stage, illustrating uncertainty immediately after initialization.

### 3 · Particle cloud concentration

<p align="center">
  <img src="images/particle_cloud.png" alt="Particles concentrated around MABot while laser returns follow the mapped walls" width="850">
</p>

The later observation shows a smaller particle cluster around MABot while the laser scan remains aligned with the environment. The demonstration also shows translation and rotation. Alignment is generally maintained, with some temporary scan offsets during movement.

These results are qualitative visual evidence; no numerical localization-error benchmark is claimed.

## Package layout

| Path | Purpose |
| --- | --- |
| `config/amcl.yaml` | AMCL frames, motion model, laser model and particle-filter settings |
| `launch/amcl.launch.py` | Map server, AMCL and lifecycle-manager launch |
| `map/mabot_world_map.yaml` | Saved-map metadata |
| `map/mabot_world_map.pgm` | Saved occupancy-grid image |
| `rviz/` | Location for saved RViz configurations |
| `images/` | Three result screenshots, GIF and MP4 demonstration |
| `CMakeLists.txt` | Installs `config`, `launch`, `rviz` and `map` |
| `package.xml` | Package metadata and dependencies |

The simulator and robot description are provided by the sibling [`mabot_description`](../mabot_description/) package. Mapping was performed with [`mabot_slam`](../mabot_slam/); the copied map files allow this localization launch to load its map without locating that package at runtime.

## Run the project

The commands below assume the repository is located at `~/workspaces/ETGAH-Robotics-Masterclass`, with ROS 2 Jazzy and the project's Gazebo dependencies available.

<details>
<summary><strong>1. Build and source the workspace</strong></summary>

```bash
cd ~/workspaces/ETGAH-Robotics-Masterclass

colcon build --symlink-install \
  --packages-select mabot_description mabot_localization

source install/setup.bash
```

Before building, confirm both map files are present in `mabot_localization/map/`. The YAML should reference the image using a relative path:

```yaml
image: mabot_world_map.pgm
```

The localization package requires `ament_cmake`, `launch`, `launch_ros`, `ament_index_python`, `nav2_map_server`, `nav2_amcl` and `nav2_lifecycle_manager`. RViz visualization uses `rviz2` and `nav2_rviz_plugins`; keyboard driving uses `teleop_twist_keyboard`.

</details>

<details>
<summary><strong>2. Start the MABot simulation — terminal 1</strong></summary>

```bash
source ~/workspaces/ETGAH-Robotics-Masterclass/install/setup.bash

ros2 launch mabot_description gazebo.launch.py
```

Wait for the world and robot to load. Use the same world used to create the saved map. Keep SLAM Toolbox and autonomous motion controllers stopped during the localization test.

</details>

<details>
<summary><strong>3. Start AMCL — terminal 2</strong></summary>

```bash
source ~/workspaces/ETGAH-Robotics-Masterclass/install/setup.bash

ros2 launch mabot_localization amcl.launch.py
```

The lifecycle manager configures and activates `map_server` and `amcl`. The launch defaults to the installed copy of `map/mabot_world_map.yaml` inside `mabot_localization`.

Optional overrides:

```bash
ros2 launch mabot_localization amcl.launch.py \
  use_sim_time:=true \
  map:=/absolute/path/to/map.yaml \
  params_file:=/absolute/path/to/amcl.yaml
```

</details>

<details>
<summary><strong>4. Open RViz — terminal 3</strong></summary>

```bash
source ~/workspaces/ETGAH-Robotics-Masterclass/install/setup.bash

ros2 launch mabot_description display.launch.py
```

Set **Fixed Frame** to `map` and configure the displays listed below. The localization launch itself does not start RViz.

</details>

<details>
<summary><strong>5. Set the initial pose and drive — terminal 4</strong></summary>

In RViz, select **2D Pose Estimate**, click the robot's approximate location on the map and drag in its facing direction. The selected pose must be expressed in `map`.

For the assignment demonstration:

1. Set a deliberately incorrect pose and capture the scan mismatch.
2. Correct the position and heading.
3. Drive slowly and observe scan alignment and particle concentration.

```bash
source ~/workspaces/ETGAH-Robotics-Masterclass/install/setup.bash

ros2 run teleop_twist_keyboard teleop_twist_keyboard \
  --ros-args -p speed:=0.10 -p turn:=0.20
```

Keep keyboard focus in the teleoperation terminal: `i` moves forward, `j` / `l` rotate, and `k` stops. Stop the robot before closing teleoperation.

</details>

## RViz configuration

| Display / setting | Configuration |
| --- | --- |
| Fixed Frame | `map` |
| Map | `/map`; Reliable; Transient Local |
| LaserScan | `/scan`; Best Effort; Decay Time `0` |
| ParticleCloud | `/particle_cloud`; Best Effort |
| TF | Enabled |
| RobotModel | Robot description published by the simulation's robot-state publisher |
| ZED2 RGB Image | Optional camera view |
| ZED2 Point Cloud | Optional; disabled in the clearer localization screenshots |

The particle cloud represents possible robot poses. A tighter cluster indicates reduced uncertainty within the filter; scan alignment provides an additional visual check against the environment.

## AMCL configuration

| Setting | Value / role |
| --- | --- |
| Frames | `map`, `odom`, `base_footprint` |
| Motion model | `nav2_amcl::DifferentialMotionModel`, an approximation for skid-steer motion |
| Odometry noise | `alpha1`–`alpha4`: `0.2` |
| Particle count | Minimum `500`, maximum `2000` |
| Laser model | `likelihood_field`, up to `60` beams |
| Laser range limits | `-1.0`, using the limits reported by LaserScan |
| Update thresholds | `0.10 m` translation or `0.10 rad` rotation |
| TF publication | `tf_broadcast: true` |
| Initial pose | `set_initial_pose: false`; supplied manually in RViz |
| Simulation clock | `use_sim_time: true` |

AMCL supplies the `map` to `odom` transform after initialization. Robot odometry supplies `odom` to `base_footprint`, and the robot description connects the base to the wheels and sensors. Only one localization system should own `map` to `odom` at a time.

<details>
<summary><strong>Verification commands</strong></summary>

Run these with the simulation and AMCL active and the initial pose set:

```bash
ros2 lifecycle get /map_server
ros2 lifecycle get /amcl
ros2 param get /map_server yaml_filename

ros2 topic info /map --verbose
ros2 topic info /scan --verbose
ros2 topic info /odom --verbose
ros2 topic info /particle_cloud --verbose

ros2 topic echo /map --once --field info \
  --qos-durability transient_local \
  --qos-reliability reliable

ros2 topic echo /amcl_pose --once
ros2 run tf2_ros tf2_echo map odom
ros2 run tf2_tools view_frames
```

Expected checks: both lifecycle nodes are `active`; `map_server` is the only `/map` publisher; scan and odometry inputs are available; and `map` to `odom` is available after initialization.

To observe pose updates during movement:

```bash
ros2 topic echo /amcl_pose
```

AMCL updates depend on sensor processing and movement thresholds; a stationary robot need not publish a new estimate at a constant rate.

These are reproduction commands. A new TF-tree capture and a recorded `/amcl_pose` motion log are not included in this documentation bundle.

</details>

<!-- ## Troubleshooting

<details>
<summary><strong>“Ignoring initial pose in frame odom”</strong></summary>

This occurred when the initial estimate was sent while RViz used `odom` as its fixed frame. Set **Fixed Frame = map**, then use **2D Pose Estimate again**. Changing the fixed frame does not resend the rejected estimate.

</details> -->

<details>
<summary><strong>“Please set the initial pose” / missing map frame</strong></summary>

The configuration intentionally waits for a manual initial estimate. Supply a pose in `map` after starting AMCL. A pose sent during a previous run is not automatically restored by this launch configuration.

Check the outgoing estimate if needed:

```bash
ros2 topic echo /initialpose --once --field header
```

Then click **2D Pose Estimate**. The header should report `frame_id: map`.

</details>

<details>
<summary><strong>“No map received” in RViz</strong></summary>

Check the Map display's topic and QoS, the map server's lifecycle state, and whether a transient-local terminal subscriber receives `/map`. Distinguish receiving the occupancy grid from obtaining the robot's TF connection to the map.

During development, the map server successfully loaded the map and terminal subscribers received it while RViz still reported this warning. Map display subsequently worked, but the exact cause of the earlier RViz reception issue was not isolated. Copying the map into this package satisfies the assignment's organization requirement; it is not presented as a proven fix for that warning.

</details>

<!-- <details>
<summary><strong>Launch file or map missing after a build</strong></summary>

The CMake installation rule must include the runtime resource directories before `ament_package()`:

```cmake
install(
  DIRECTORY config launch rviz map
  DESTINATION share/${PROJECT_NAME}
  PATTERN "__pycache__" EXCLUDE
  PATTERN "*.pyc" EXCLUDE
)
```

Rebuild `mabot_localization`, source `install/setup.bash`, and verify the installed map directory. Both the YAML and its referenced PGM must be present.

</details>

---

**Author:** Mohamed Abdelmoniem  
**Project:** [ETGAH Robotics Masterclass](https://github.com/men3m-4/ETGAH-Robotics-Masterclass)  
**Package:** `mabot_localization` · **License:** Apache-2.0 -->

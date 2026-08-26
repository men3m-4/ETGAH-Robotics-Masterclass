# TurtleBot Operation

ROS 2 project for autonomous obstacle avoidance with manual direction override.

The robot uses LiDAR data from `/scan` to avoid obstacles automatically and publishes movement commands to `/cmd_vel`.

The operator can also override the robot direction using the `/set_direction` service.

---

## Package Structure

```text
turtlebot_operation_ma/
├── obstacle_direction_controller/
│   ├── obstacle_direction_controller/
│   │   ├── __init__.py
│   │   └── direction_autopilot_node.py
│   ├── package.xml
│   ├── setup.py
│   ├── setup.cfg
│   ├── resource/
│   └── test/
│
├── obstacle_direction_interfaces/
│   ├── srv/
│   │   └── SetDirection.srv
│   ├── CMakeLists.txt
│   └── package.xml
│
└── README.md
```

---

## Custom Service

The custom service is:

```text
obstacle_direction_interfaces/srv/SetDirection.srv
```

Definition:

```text
string direction
---
bool success
string message
```

Supported directions:

```text
forward
reverse
left
right
```

---

## Topics and Service

| Name | Type | Purpose |
|---|---|---|
| `/scan` | `sensor_msgs/msg/LaserScan` | Receives LiDAR data |
| `/cmd_vel` | `geometry_msgs/msg/Twist` | Controls robot movement |
| `/set_direction` | `obstacle_direction_interfaces/srv/SetDirection` | Manual direction override |

---

## Manual Override

The operator can override the autonomous movement using:

```text
/set_direction
```

Available commands:

```text
forward
reverse
left
right
```

---

# Setup Instructions

## 1. Navigate to the Repository

```bash
cd ~/workspaces/ETGAH-Robotics-Masterclass/turtlebot_operation_ma
```

---

## 2. Build the Packages

```bash
colcon build
```

This builds both ROS 2 packages.

---

## 3. Source the Workspace

```bash
source install/setup.bash
```

Run this command in every new terminal before using the custom packages.

---

## 4. Verify the Service Interface

```bash
ros2 interface show obstacle_direction_interfaces/srv/SetDirection
```

Expected output:

```text
string direction
---
bool success
string message
```

---

# Run the Controller

```bash
ros2 run obstacle_direction_controller direction_autopilot_node
```

Expected startup output:

```text
Obstacle Avoidance Controller Started
/set_direction service is ready
```

---

# Test the Project

## Check LiDAR Data

```bash
ros2 topic echo /scan
```

This shows LiDAR measurements from TurtleBot3.

---

## Check Velocity Commands

```bash
ros2 topic echo /cmd_vel
```

This shows the movement commands published by the controller.

---

## Check the Service

```bash
ros2 service list
```

You should see:

```text
/set_direction
```

Check its type:

```bash
ros2 service type /set_direction
```

Expected output:

```text
obstacle_direction_interfaces/srv/SetDirection
```

---

# Test Manual Override

## Forward

```bash
ros2 service call /set_direction obstacle_direction_interfaces/srv/SetDirection "{direction: 'forward'}"
```

Expected behavior:

```text
Robot moves forward.
```

---

## Reverse

```bash
ros2 service call /set_direction obstacle_direction_interfaces/srv/SetDirection "{direction: 'reverse'}"
```

Expected behavior:

```text
Robot moves backward.
```

---

## Left

```bash
ros2 service call /set_direction obstacle_direction_interfaces/srv/SetDirection "{direction: 'left'}"
```

Expected behavior:

```text
Robot turns left.
```

---

## Right

```bash
ros2 service call /set_direction obstacle_direction_interfaces/srv/SetDirection "{direction: 'right'}"
```

Expected behavior:

```text
Robot turns right.
```

---

## Invalid Direction

Example:

```bash
ros2 service call /set_direction obstacle_direction_interfaces/srv/SetDirection "{direction: 'up'}"
```

Expected response:

```text
success=False
```

---

# Test Obstacle Avoidance

Run the controller:

```bash
ros2 run obstacle_direction_controller direction_autopilot_node
```

The robot should move forward when the path is clear.

When an obstacle is detected in front, the controller changes from:

```text
FORWARD -> TURN
```

The robot chooses left or right depending on the available space.

When the path becomes clear:

```text
TURN -> FORWARD
```

If both sides are blocked:

```text
TURN -> REVERSE
```

The robot moves backward and attempts to recover.

---


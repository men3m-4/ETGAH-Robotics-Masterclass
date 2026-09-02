# Validation Report: ma_robot

## Status: PASS

## Summary

| Metric | Value |
|--------|-------|
| Links | 7 |
| Joints | 6 |
| Assemblies | 5 |
| Root | `base_link` |
| Errors | 0 |
| Warnings | 0 |

## Kinematic Tree

```
base_link [primitive]
  └─ zed2_camera_joint [fixed]
    zed2_camera_link [primitive]
  └─ rear_left_wheel_joint [continuous]
    rear_left_wheel_link [BAKE] [primitive]
  └─ front_right_wheel_joint [continuous]
    front_right_wheel_link [BAKE] [primitive]
  └─ rear_right_wheel_joint [continuous]
    rear_right_wheel_link [BAKE] [primitive]
  └─ front_left_wheel_joint [continuous]
    front_left_wheel_link [BAKE] [primitive]
  └─ rplidar_s2_joint [fixed]
    rplidar_s2_link [primitive]
```

## Collision Geometry

| Link | Source | Shape/File |
|------|--------|------------|
| `base_link` | primitive STL | cylinder |
| `front_left_wheel_link` | primitive STL | box |
| `front_right_wheel_link` | primitive STL | box |
| `rear_left_wheel_link` | primitive STL | box |
| `rear_right_wheel_link` | primitive STL | box |
| `rplidar_s2_link` | primitive STL | box |
| `zed2_camera_link` | primitive STL | box |

## Mesh Bake Offsets

Links where joint frame ≠ component origin. Visual/inertial/collision origins shifted.

| Link | Offset (mm) |
|------|-------------|
| `rear_left_wheel_link` | (20.0, 45.0, -70.0) |
| `front_left_wheel_link` | (130.0, -45.0, -63.0) |
| `front_right_wheel_link` | (130.0, -45.0, 189.0) |
| `rear_right_wheel_link` | (20.0, 45.0, 189.0) |

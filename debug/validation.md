# Validation Report: ma_robot

## Status: PASS (with warnings)

## Summary

| Metric | Value |
|--------|-------|
| Links | 7 |
| Joints | 6 |
| Assemblies | 5 |
| Root | `base_link` |
| Errors | 0 |
| Warnings | 2 |

## Warnings

- Root link renamed: 'ma_robot' → 'base_link' (REP 120 convention). Consider renaming the component to 'base_link' in Fusion.
- Link 'base_link': visual mesh export failed — exception: property '_get_isVisible' of 'Occurrence' object has no setter

## Kinematic Tree

```
base_link [primitive]
  └─ Rigid_1 [fixed]
    zed2_camera_link [primitive]
  └─ Rigid_2 [fixed]
    rplidar_s2_link [primitive]
  └─ Revolute_5 [continuous]
    Part2_1 [BAKE] [primitive]
  └─ Revolute_6 [continuous]
    Part2_2 [BAKE] [primitive]
  └─ Revolute_8 [continuous]
    Part2_1_Mirror [BAKE] [primitive]
  └─ Revolute_9 [continuous]
    Part2_2_Mirror [BAKE] [primitive]
```

## Collision Geometry

| Link | Source | Shape/File |
|------|--------|------------|
| `Part2_1` | primitive STL | box |
| `Part2_1_Mirror` | primitive STL | cylinder |
| `Part2_2` | primitive STL | box |
| `Part2_2_Mirror` | primitive STL | cylinder |
| `base_link` | primitive STL | cylinder |
| `rplidar_s2_link` | primitive STL | box |
| `zed2_camera_link` | primitive STL | box |

## Mesh Bake Offsets

Links where joint frame ≠ component origin. Visual/inertial/collision origins shifted.

| Link | Offset (mm) |
|------|-------------|
| `Part2_1` | (-130.0, -20.0, 70.0) |
| `Part2_2` | (20.0, -20.0, -168.0) |
| `Part2_1_Mirror` | (-130.0, -20.0, -168.0) |
| `Part2_2_Mirror` | (20.0, -20.0, 43.0) |

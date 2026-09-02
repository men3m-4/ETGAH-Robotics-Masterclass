# Transformation Matrices - ma_robot

Homogeneous transformation matrices between consecutive frames.
Convention: URDF RPY (XYZ extrinsic / ZYX intrinsic).

## Notation

### Frames

| Index | Link |
|-------|------|
| $L_{0}$ | base_link |
| $L_{1}$ | zed2_camera_link |
| $L_{2}$ | rplidar_s2_link |
| $L_{3}$ | Part2_1 |
| $L_{4}$ | Part2_2 |
| $L_{5}$ | Part2_1_Mirror |
| $L_{6}$ | Part2_2_Mirror |

### Joint Variables

| Variable | Joint | Type | From | To |
|----------|-------|------|------|----|
| $q_{1}$ | Revolute_5 | continuous (rad) | $L_{0}$ | $L_{3}$ |
| $q_{2}$ | Revolute_6 | continuous (rad) | $L_{0}$ | $L_{4}$ |
| $q_{3}$ | Revolute_8 | continuous (rad) | $L_{0}$ | $L_{5}$ |
| $q_{4}$ | Revolute_9 | continuous (rad) | $L_{0}$ | $L_{6}$ |

Shorthand: $c_i = \cos(q_i)$, $s_i = \sin(q_i)$

### Kinematic Tree

```
L0: base_link
  |-- [fixed] Rigid_1
  |   L1: zed2_camera_link
  |-- [fixed] Rigid_2
  |   L2: rplidar_s2_link
  |-- [continuous] Revolute_5 (q1)
  |   L3: Part2_1
  |-- [continuous] Revolute_6 (q2)
  |   L4: Part2_2
  |-- [continuous] Revolute_8 (q3)
  |   L5: Part2_1_Mirror
  +-- [continuous] Revolute_9 (q4)
      L6: Part2_2_Mirror
```

## Transforms

## Rigid_1

$L_{0}$ **base_link** -> $L_{1}$ **zed2_camera_link** (fixed)

- **origin xyz**: (0.145, -0.0625, -0.007371) m
- **origin rpy**: (0, 0, -1.570796) rad

### Local Transform

$$
T^{0}_{1} = \begin{bmatrix}
0 & 1 & 0 & 0.145 \\
-1 & 0 & 0 & -0.0625 \\
0 & 0 & 1 & -0.007371 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Rigid_2

$L_{0}$ **base_link** -> $L_{2}$ **rplidar_s2_link** (fixed)

- **origin xyz**: (-0.433747, -0.657506, 0.046815) m
- **origin rpy**: (0, 0, -1.570796) rad

### Local Transform

$$
T^{0}_{2} = \begin{bmatrix}
0 & 1 & 0 & -0.433747 \\
-1 & 0 & 0 & -0.657506 \\
0 & 0 & 1 & 0.046815 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Revolute_5

$L_{0}$ **base_link** -> $L_{3}$ **Part2_1** (continuous)
  Variable: $q_{1}$

- **origin xyz**: (0.26, 0, 0) m
- **origin rpy**: (-1.570796, 0, 0) rad
- **axis**: (0, 0, 1)

### Local Transform

$T^{0}_{3}(q_{1}) = T_{fixed} \cdot R_{axis}(q_{1})$ where:

$$
T_{fixed} = \begin{bmatrix}
1 & 0 & 0 & 0.26 \\
0 & 0 & 1 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

$$
R_{axis}(q_{1}) = \begin{bmatrix}
c_{1} & -s_{1} & 0 & 0 \\
s_{1} & c_{1} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Revolute_6

$L_{0}$ **base_link** -> $L_{4}$ **Part2_2** (continuous)
  Variable: $q_{2}$

- **origin xyz**: (-0.04, -0.362, 0.04) m
- **origin rpy**: (1.570796, 0, 0) rad
- **axis**: (0, 0, 1)

### Local Transform

$T^{0}_{4}(q_{2}) = T_{fixed} \cdot R_{axis}(q_{2})$ where:

$$
T_{fixed} = \begin{bmatrix}
1 & 0 & 0 & -0.04 \\
0 & 0 & -1 & -0.362 \\
0 & 1 & 0 & 0.04 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

$$
R_{axis}(q_{2}) = \begin{bmatrix}
c_{2} & -s_{2} & 0 & 0 \\
s_{2} & c_{2} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Revolute_8

$L_{0}$ **base_link** -> $L_{5}$ **Part2_1_Mirror** (continuous)
  Variable: $q_{3}$

- **origin xyz**: (0.26, -0.362, 0.04) m
- **origin rpy**: (1.570796, 0, 0) rad
- **axis**: (0, 0, 1)

### Local Transform

$T^{0}_{5}(q_{3}) = T_{fixed} \cdot R_{axis}(q_{3})$ where:

$$
T_{fixed} = \begin{bmatrix}
1 & 0 & 0 & 0.26 \\
0 & 0 & -1 & -0.362 \\
0 & 1 & 0 & 0.04 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

$$
R_{axis}(q_{3}) = \begin{bmatrix}
c_{3} & -s_{3} & 0 & 0 \\
s_{3} & c_{3} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Revolute_9

$L_{0}$ **base_link** -> $L_{6}$ **Part2_2_Mirror** (continuous)
  Variable: $q_{4}$

- **origin xyz**: (-0.04, 0.026, 0) m
- **origin rpy**: (-1.570796, 0, 0) rad
- **axis**: (0, 0, 1)

### Local Transform

$T^{0}_{6}(q_{4}) = T_{fixed} \cdot R_{axis}(q_{4})$ where:

$$
T_{fixed} = \begin{bmatrix}
1 & 0 & 0 & -0.04 \\
0 & 0 & 1 & 0.026 \\
0 & -1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

$$
R_{axis}(q_{4}) = \begin{bmatrix}
c_{4} & -s_{4} & 0 & 0 \\
s_{4} & c_{4} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

---

## Global Transform Chains

Transform from root $L_0$ to any link, as product of local transforms along the kinematic chain.


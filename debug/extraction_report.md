# Extraction Report: ma_robot

**Exported:** 2026-09-03T01:26:45.501702
**Exporter:** v3.1.0

## Summary

| Metric | Value |
|--------|-------|
| Occurrences | 15 |
| Subassemblies | 4 |
| Leaf components | 11 |
| Joints (total) | 6 |
| As-built joints | 0 |
| Regular joints | 6 |
| Max nesting depth | 1 |

## Assembly Hierarchy

```
[ma_robot]  (design root)
  ├── base_link  (2899.2g)
  ├── rplidar_s2_link  (203.8g)
  ├── zed2_camera_link  (178.2g)
  [front_left_wheel_link]  (depth=0, children=2)
    ├── Rim_1  (0.0g, )
    ├── Tire_1  (611.6g, Steel)
  [front_right_wheel_link]  (depth=0, children=2)
    ├── Rim_2  (0.0g, )
    ├── Tire_2  (611.6g, Steel)
  [rear_left_wheel_link]  (depth=0, children=2)
    ├── Rim  (0.0g, )
    ├── Tire  (611.6g, Steel)
  [rear_right_wheel_link]  (depth=0, children=2)
    ├── Rim_3  (0.0g, )
    ├── Tire_3  (611.6g, Steel)
```

## Occurrences

### Depth 0

#### 🔧 COMPONENT: `base_link`

| Property | Value |
|----------|-------|
| Full path | `base_link:1` |
| Component name | base_link |
| Depth | 0 |
| Path segments | base_link |
| **Transforms** | |
| Global position (m) | (0.000000, 0.000000, 0.025000) |
| Global position (mm) | (0.00, 0.00, 25.00) |
| Local transform (m) | (0.000000, 0.000000, 0.025000) |
| Assembly context depth | 0 |
| transform2 (m) | (0.000000, 0.000000, 0.025000) |
| **Physical** | |
| Mass | 2.899172 kg (2899.172 g) |
| Volume | 2.034509e-03 m³ |
| Density | 1425.0 kg/m³ |
| Surface area | 1.353142e-01 m² |
| Body count | 2 |
| CoM (component-local, m) | (0.041574, -0.062494, 0.024420) |
| CoM (global, m) | (0.041574, -0.062494, 0.049420) |
| CoM (global, mm) | (41.57, -62.49, 49.42) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 2.102569e-02, 2.053476e-02, 3.686159e-02 |
| Ixy, Ixz, Iyz | 7.533289e-03, -2.665014e-03, 4.424103e-03 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 7.973854e-03, 1.379501e-02, 2.052789e-02 |
| Ixy, Ixz, Iyz | 9.036948e-07, 2.783510e-04, -4.481462e-07 |
| Bounding box (m) | 0.2630 × 0.2450 × 0.1200 |
| Bounding box (mm) | 263.04 × 245.00 × 120.00 |
| **Material & Appearance** | |
| Material | Acetal_Resin_Black |
| Appearance | Plastic_Glossy_Black |
| Color (RGB 0-1) | (0.098, 0.098, 0.098) |
| Color (RGB 0-255) | (25, 25, 25) |
| **Per-body breakdown** | |
| Body 0: Body1 | mass=2899.091g, material=Acetal_Resin_Black, inertia_src=api |
| Body 1: Body2 | mass=0.081g, material=Laminate_Blue_Matte, inertia_src=api |

#### 📦 SUBASSEMBLY: `front_left_wheel_link`

| Property | Value |
|----------|-------|
| Full path | `front_left_wheel_link:1` |
| Component name | front_left_wheel_link |
| Depth | 0 |
| Path segments | front_left_wheel_link |
| Child occurrences | 2 |
| **Transforms** | |
| Global position (m) | (0.120000, 0.143318, 0.052447) |
| Global position (mm) | (120.00, 143.32, 52.45) |
| Local transform (m) | (0.120000, 0.143318, 0.052447) |
| Assembly context depth | 0 |
| transform2 (m) | (0.120000, 0.143318, 0.052447) |

#### 📦 SUBASSEMBLY: `front_right_wheel_link`

| Property | Value |
|----------|-------|
| Full path | `front_right_wheel_link:1` |
| Component name | front_right_wheel_link |
| Depth | 0 |
| Path segments | front_right_wheel_link |
| Child occurrences | 2 |
| **Transforms** | |
| Global position (m) | (0.093104, -0.244917, 0.000000) |
| Global position (mm) | (93.10, -244.92, 0.00) |
| Local transform (m) | (0.093104, -0.244917, 0.000000) |
| Assembly context depth | 0 |
| transform2 (m) | (0.093104, -0.244917, 0.000000) |

#### 📦 SUBASSEMBLY: `rear_left_wheel_link`

| Property | Value |
|----------|-------|
| Full path | `rear_left_wheel_link:1` |
| Component name | rear_left_wheel_link |
| Depth | 0 |
| Path segments | rear_left_wheel_link |
| Child occurrences | 2 |
| **Transforms** | |
| Global position (m) | (0.000000, 0.000000, 0.000000) |
| Global position (mm) | (0.00, 0.00, 0.00) |
| Local transform (m) | (0.000000, 0.000000, 0.000000) |
| Assembly context depth | 0 |
| transform2 (m) | (0.000000, 0.000000, 0.000000) |

#### 📦 SUBASSEMBLY: `rear_right_wheel_link`

| Property | Value |
|----------|-------|
| Full path | `rear_right_wheel_link:1` |
| Component name | rear_right_wheel_link |
| Depth | 0 |
| Path segments | rear_right_wheel_link |
| Child occurrences | 2 |
| **Transforms** | |
| Global position (m) | (-0.015278, -0.247293, 0.000000) |
| Global position (mm) | (-15.28, -247.29, 0.00) |
| Local transform (m) | (-0.015278, -0.247293, 0.000000) |
| Assembly context depth | 0 |
| transform2 (m) | (-0.015278, -0.247293, 0.000000) |

#### 🔧 COMPONENT: `rplidar_s2_link`

| Property | Value |
|----------|-------|
| Full path | `rplidar_s2_link:1` |
| Component name | rplidar_s2_link |
| Depth | 0 |
| Path segments | rplidar_s2_link |
| **Transforms** | |
| Global position (m) | (-0.433747, -0.657506, 0.071815) |
| Global position (mm) | (-433.75, -657.51, 71.81) |
| Local transform (m) | (-0.433747, -0.657506, 0.071815) |
| Assembly context depth | 0 |
| transform2 (m) | (-0.433747, -0.657506, 0.071815) |
| **Physical** | |
| Mass | 0.203764 kg (203.764 g) |
| Volume | 3.373166e-05 m³ |
| Density | 6040.7 kg/m³ |
| Surface area | 4.422538e-02 m² |
| Body count | 28 |
| CoM (component-local, m) | (-0.595013, 0.532942, 0.012880) |
| CoM (global, m) | (-1.028760, -0.124565, 0.084695) |
| CoM (global, mm) | (-1028.76, -124.56, 84.70) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 5.804326e-02, 7.231055e-02, 1.302519e-01 |
| Ixy, Ixz, Iyz | 6.461490e-02, 1.561641e-03, -1.398680e-03 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.351079e-04, 1.362177e-04, 2.370283e-04 |
| Ixy, Ixz, Iyz | -7.653496e-09, 1.410544e-08, 3.930765e-08 |
| Bounding box (m) | 0.0770 × 0.0770 × 0.0389 |
| Bounding box (mm) | 77.00 × 77.00 × 38.85 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Copper_Raw |
| Color (RGB 0-1) | (1.000, 1.000, 1.000) |
| Color (RGB 0-255) | (255, 255, 255) |
| **Per-body breakdown** | |
| Body 0: Body1 | mass=0.229g, material=Steel, inertia_src=api |
| Body 1: Body2 | mass=0.186g, material=Steel, inertia_src=api |
| Body 2: Body3 | mass=13.536g, material=Acetal_Resin_White, inertia_src=api |
| Body 3: Body4 | mass=0.229g, material=Steel, inertia_src=api |
| Body 4: Body5 | mass=0.229g, material=Steel, inertia_src=api |
| Body 5: Body6 | mass=0.186g, material=Steel, inertia_src=api |
| Body 6: Body7 | mass=0.229g, material=Steel, inertia_src=api |
| Body 7: Body8 | mass=65.603g, material=Steel, inertia_src=api |
| Body 8: Body9 | mass=0.229g, material=Steel, inertia_src=api |
| Body 9: Body10 | mass=0.000g, material=Steel, inertia_src=api |
| Body 10: Body11 | mass=0.229g, material=Steel, inertia_src=api |
| Body 11: Body12 | mass=0.150g, material=Steel, inertia_src=api |
| Body 12: Body13 | mass=0.229g, material=Steel, inertia_src=api |
| Body 13: Body14 | mass=0.091g, material=Steel, inertia_src=api |
| Body 14: Body18 | mass=0.186g, material=Steel, inertia_src=api |
| Body 15: Body19 | mass=0.006g, material=Steel, inertia_src=api |
| Body 16: Body20 | mass=0.124g, material=Steel, inertia_src=api |
| Body 17: Body22 | mass=0.925g, material=Steel, inertia_src=api |
| Body 18: Body23 | mass=0.150g, material=Steel, inertia_src=api |
| Body 19: Body25 | mass=0.006g, material=Steel, inertia_src=api |
| Body 20: Body27 | mass=0.150g, material=Steel, inertia_src=api |
| Body 21: Body29 | mass=0.006g, material=Steel, inertia_src=api |
| Body 22: Body30 | mass=0.186g, material=Steel, inertia_src=api |
| Body 23: Body33 | mass=0.006g, material=Steel, inertia_src=api |
| Body 24: Body34 | mass=0.006g, material=Steel, inertia_src=api |
| Body 25: Body35 | mass=0.006g, material=Steel, inertia_src=api |
| Body 26: Body37 | mass=0.114g, material=Steel, inertia_src=api |
| Body 27: Body38 | mass=120.538g, material=Steel, inertia_src=api |

#### 🔧 COMPONENT: `zed2_camera_link`

| Property | Value |
|----------|-------|
| Full path | `zed2_camera_link:1` |
| Component name | zed2_camera_link |
| Depth | 0 |
| Path segments | zed2_camera_link |
| **Transforms** | |
| Global position (m) | (0.145000, -0.062500, 0.017629) |
| Global position (mm) | (145.00, -62.50, 17.63) |
| Local transform (m) | (0.145000, -0.062500, 0.017629) |
| Assembly context depth | 0 |
| transform2 (m) | (0.145000, -0.062500, 0.017629) |
| **Physical** | |
| Mass | 0.178229 kg (178.229 g) |
| Volume | 1.521051e-04 m³ |
| Density | 1171.8 kg/m³ |
| Surface area | 2.200474e-02 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.000000, 0.015505, 0.042389) |
| CoM (global, m) | (0.145000, -0.046995, 0.060018) |
| CoM (global, mm) | (145.00, -46.99, 60.02) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 3.897245e-04, 7.565457e-04, 4.819299e-04 |
| Ixy, Ixz, Iyz | -3.822780e-09, -3.282674e-09, -1.171455e-04 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 2.662726e-05, 4.362977e-04, 4.390806e-04 |
| Ixy, Ixz, Iyz | -3.215230e-09, -1.621734e-09, -2.967393e-09 |
| Bounding box (m) | 0.1747 × 0.0316 × 0.0297 |
| Bounding box (mm) | 174.73 × 31.60 × 29.73 |
| **Material & Appearance** | |
| Material | PA_11_Nylon_HP_11_30_with_EOS_P_396_3D_Printer |
| Appearance | Nylon_12_with_Formlabs_Fuse_1_3D_Printer |
| Color (RGB 0-1) | (0.247, 0.247, 0.247) |
| Color (RGB 0-255) | (63, 63, 63) |

### Depth 1

#### 🔧 COMPONENT: `Rim_1`

| Property | Value |
|----------|-------|
| Full path | `front_left_wheel_link:1+Rim (1):1` |
| Component name | Rim (1) |
| Depth | 1 |
| Path segments | front_left_wheel_link → Rim_1 |
| Parent path | `front_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.119275, 0.149755, 0.064526) |
| Global position (mm) | (119.28, 149.75, 64.53) |
| Local transform (m) | (-0.000725, 0.006437, 0.012079) |
| Assembly context depth | 1 |
| transform2 (m) | (0.119275, 0.149755, 0.064526) |
| **Physical** | |
| Mass | 0.000000 kg (0.000 g) |
| Volume | 0.000000e+00 m³ |
| Density | 0.0 kg/m³ |
| Surface area | 0.000000e+00 m² |
| Body count | 0 |
| CoM (component-local, m) | (0.000000, 0.000000, 0.000000) |
| CoM (global, m) | (0.000000, 0.000000, 0.000000) |
| CoM (global, mm) | (0.00, 0.00, 0.00) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 0.000000e+00, 0.000000e+00, 0.000000e+00 |
| Ixy, Ixz, Iyz | 0.000000e+00, 0.000000e+00, 0.000000e+00 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 0.000000e+00, 0.000000e+00, 0.000000e+00 |
| Ixy, Ixz, Iyz | 0.000000e+00, 0.000000e+00, 0.000000e+00 |
| Bounding box (m) | 0.0000 × 0.0000 × 0.0000 |
| Bounding box (mm) | 0.00 × 0.00 × 0.00 |
| **Material & Appearance** | |
| Material |  |
| Appearance |  |

#### 🔧 COMPONENT: `Tire_1`

| Property | Value |
|----------|-------|
| Full path | `front_left_wheel_link:1+Tire (1):1` |
| Component name | Tire (1) |
| Depth | 1 |
| Path segments | front_left_wheel_link → Tire_1 |
| Parent path | `front_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.142900, 0.061477, 0.026952) |
| Global position (mm) | (142.90, 61.48, 26.95) |
| Local transform (m) | (0.022900, -0.081841, -0.025495) |
| Assembly context depth | 1 |
| transform2 (m) | (0.142900, 0.061477, 0.026952) |
| **Physical** | |
| Mass | 0.611603 kg (611.603 g) |
| Volume | 7.791120e-05 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 5.988217e-02 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.012900, -0.005483, -0.018048) |
| CoM (global, m) | (0.155800, 0.055994, 0.008904) |
| CoM (global, mm) | (155.80, 55.99, 8.90) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 7.441770e-04, 1.033528e-03, 6.467384e-04 |
| Ixy, Ixz, Iyz | 4.325594e-05, 1.423953e-04, -6.051680e-05 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 5.265770e-04, 7.325315e-04, 5.265750e-04 |
| Ixy, Ixz, Iyz | 8.274260e-11, 5.777757e-10, 6.033033e-11 |
| Bounding box (m) | 0.0900 × 0.0500 × 0.0899 |
| Bounding box (mm) | 90.00 × 50.00 × 89.92 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_160_160_160 |
| Color (RGB 0-1) | (0.627, 0.627, 0.627) |
| Color (RGB 0-255) | (160, 160, 160) |

#### 🔧 COMPONENT: `Rim_2`

| Property | Value |
|----------|-------|
| Full path | `front_right_wheel_link:1+Rim (2):1` |
| Component name | Rim (2) |
| Depth | 1 |
| Path segments | front_right_wheel_link → Rim_2 |
| Parent path | `front_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.093828, -0.251353, 0.012079) |
| Global position (mm) | (93.83, -251.35, 12.08) |
| Local transform (m) | (-0.000725, 0.006437, 0.012079) |
| Assembly context depth | 1 |
| transform2 (m) | (0.093828, -0.251353, 0.012079) |
| **Physical** | |
| Mass | 0.000000 kg (0.000 g) |
| Volume | 0.000000e+00 m³ |
| Density | 0.0 kg/m³ |
| Surface area | 0.000000e+00 m² |
| Body count | 0 |
| CoM (component-local, m) | (0.000000, 0.000000, 0.000000) |
| CoM (global, m) | (0.000000, 0.000000, 0.000000) |
| CoM (global, mm) | (0.00, 0.00, 0.00) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 0.000000e+00, 0.000000e+00, 0.000000e+00 |
| Ixy, Ixz, Iyz | 0.000000e+00, 0.000000e+00, 0.000000e+00 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 0.000000e+00, 0.000000e+00, 0.000000e+00 |
| Ixy, Ixz, Iyz | 0.000000e+00, 0.000000e+00, 0.000000e+00 |
| Bounding box (m) | 0.0000 × 0.0000 × 0.0000 |
| Bounding box (mm) | 0.00 × 0.00 × 0.00 |
| **Material & Appearance** | |
| Material |  |
| Appearance |  |

#### 🔧 COMPONENT: `Tire_2`

| Property | Value |
|----------|-------|
| Full path | `front_right_wheel_link:1+Tire (2):1` |
| Component name | Tire (2) |
| Depth | 1 |
| Path segments | front_right_wheel_link → Tire_2 |
| Parent path | `front_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.142900, -0.187477, 0.063048) |
| Global position (mm) | (142.90, -187.48, 63.05) |
| Local transform (m) | (-0.049797, -0.057440, 0.063048) |
| Assembly context depth | 1 |
| transform2 (m) | (0.142900, -0.187477, 0.063048) |
| **Physical** | |
| Mass | 0.611603 kg (611.603 g) |
| Volume | 7.791120e-05 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 5.988217e-02 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.012900, -0.005483, -0.018048) |
| CoM (global, m) | (0.155800, -0.192959, 0.045000) |
| CoM (global, mm) | (155.80, -192.96, 45.00) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 7.441770e-04, 1.033528e-03, 6.467384e-04 |
| Ixy, Ixz, Iyz | 4.325594e-05, 1.423953e-04, -6.051680e-05 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 5.265770e-04, 7.325315e-04, 5.265750e-04 |
| Ixy, Ixz, Iyz | 8.274260e-11, 5.777757e-10, 6.033033e-11 |
| Bounding box (m) | 0.0900 × 0.0500 × 0.0899 |
| Bounding box (mm) | 90.00 × 50.00 × 89.92 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_160_160_160 |
| Color (RGB 0-1) | (0.627, 0.627, 0.627) |
| Color (RGB 0-255) | (160, 160, 160) |

#### 🔧 COMPONENT: `Rim`

| Property | Value |
|----------|-------|
| Full path | `rear_left_wheel_link:1+Rim:1` |
| Component name | Rim |
| Depth | 1 |
| Path segments | rear_left_wheel_link → Rim |
| Parent path | `rear_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.000725, 0.006437, 0.012079) |
| Global position (mm) | (-0.72, 6.44, 12.08) |
| Local transform (m) | (-0.000725, 0.006437, 0.012079) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.000725, 0.006437, 0.012079) |
| **Physical** | |
| Mass | 0.000000 kg (0.000 g) |
| Volume | 0.000000e+00 m³ |
| Density | 0.0 kg/m³ |
| Surface area | 0.000000e+00 m² |
| Body count | 0 |
| CoM (component-local, m) | (0.000000, 0.000000, 0.000000) |
| CoM (global, m) | (0.000000, 0.000000, 0.000000) |
| CoM (global, mm) | (0.00, 0.00, 0.00) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 0.000000e+00, 0.000000e+00, 0.000000e+00 |
| Ixy, Ixz, Iyz | 0.000000e+00, 0.000000e+00, 0.000000e+00 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 0.000000e+00, 0.000000e+00, 0.000000e+00 |
| Ixy, Ixz, Iyz | 0.000000e+00, 0.000000e+00, 0.000000e+00 |
| Bounding box (m) | 0.0000 × 0.0000 × 0.0000 |
| Bounding box (mm) | 0.00 × 0.00 × 0.00 |
| **Material & Appearance** | |
| Material |  |
| Appearance |  |

#### 🔧 COMPONENT: `Tire`

| Property | Value |
|----------|-------|
| Full path | `rear_left_wheel_link:1+Tire:1` |
| Component name | Tire |
| Depth | 1 |
| Path segments | rear_left_wheel_link → Tire |
| Parent path | `rear_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.032900, 0.062477, 0.063048) |
| Global position (mm) | (-32.90, 62.48, 63.05) |
| Local transform (m) | (-0.032900, 0.062477, 0.063048) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.032900, 0.062477, 0.063048) |
| **Physical** | |
| Mass | 0.611603 kg (611.603 g) |
| Volume | 7.791120e-05 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 5.988217e-02 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.012900, -0.005483, -0.018048) |
| CoM (global, m) | (-0.020000, 0.056994, 0.045000) |
| CoM (global, mm) | (-20.00, 56.99, 45.00) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 7.441770e-04, 1.033528e-03, 6.467384e-04 |
| Ixy, Ixz, Iyz | 4.325594e-05, 1.423953e-04, -6.051680e-05 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 5.265770e-04, 7.325315e-04, 5.265750e-04 |
| Ixy, Ixz, Iyz | 8.274260e-11, 5.777757e-10, 6.033033e-11 |
| Bounding box (m) | 0.0900 × 0.0500 × 0.0899 |
| Bounding box (mm) | 90.00 × 50.00 × 89.92 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_160_160_160 |
| Color (RGB 0-1) | (0.627, 0.627, 0.627) |
| Color (RGB 0-255) | (160, 160, 160) |

#### 🔧 COMPONENT: `Rim_3`

| Property | Value |
|----------|-------|
| Full path | `rear_right_wheel_link:1+Rim (3):1` |
| Component name | Rim (3) |
| Depth | 1 |
| Path segments | rear_right_wheel_link → Rim_3 |
| Parent path | `rear_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.016003, -0.240856, 0.012079) |
| Global position (mm) | (-16.00, -240.86, 12.08) |
| Local transform (m) | (-0.000725, 0.006437, 0.012079) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.016003, -0.240856, 0.012079) |
| **Physical** | |
| Mass | 0.000000 kg (0.000 g) |
| Volume | 0.000000e+00 m³ |
| Density | 0.0 kg/m³ |
| Surface area | 0.000000e+00 m² |
| Body count | 0 |
| CoM (component-local, m) | (0.000000, 0.000000, 0.000000) |
| CoM (global, m) | (0.000000, 0.000000, 0.000000) |
| CoM (global, mm) | (0.00, 0.00, 0.00) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 0.000000e+00, 0.000000e+00, 0.000000e+00 |
| Ixy, Ixz, Iyz | 0.000000e+00, 0.000000e+00, 0.000000e+00 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 0.000000e+00, 0.000000e+00, 0.000000e+00 |
| Ixy, Ixz, Iyz | 0.000000e+00, 0.000000e+00, 0.000000e+00 |
| Bounding box (m) | 0.0000 × 0.0000 × 0.0000 |
| Bounding box (mm) | 0.00 × 0.00 × 0.00 |
| **Material & Appearance** | |
| Material |  |
| Appearance |  |

#### 🔧 COMPONENT: `Tire_3`

| Property | Value |
|----------|-------|
| Full path | `rear_right_wheel_link:1+Tire (3):1` |
| Component name | Tire (3) |
| Depth | 1 |
| Path segments | rear_right_wheel_link → Tire_3 |
| Parent path | `rear_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.032900, -0.185477, 0.026952) |
| Global position (mm) | (-32.90, -185.48, 26.95) |
| Local transform (m) | (-0.017622, 0.061816, 0.026952) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.032900, -0.185477, 0.026952) |
| **Physical** | |
| Mass | 0.611603 kg (611.603 g) |
| Volume | 7.791120e-05 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 5.988217e-02 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.012900, -0.005483, -0.018048) |
| CoM (global, m) | (-0.020000, -0.190959, 0.008904) |
| CoM (global, mm) | (-20.00, -190.96, 8.90) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 7.441770e-04, 1.033528e-03, 6.467384e-04 |
| Ixy, Ixz, Iyz | 4.325594e-05, 1.423953e-04, -6.051680e-05 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 5.265770e-04, 7.325315e-04, 5.265750e-04 |
| Ixy, Ixz, Iyz | 8.274260e-11, 5.777757e-10, 6.033033e-11 |
| Bounding box (m) | 0.0900 × 0.0500 × 0.0899 |
| Bounding box (mm) | 90.00 × 50.00 × 89.92 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_160_160_160 |
| Color (RGB 0-1) | (0.627, 0.627, 0.627) |
| Color (RGB 0-255) | (160, 160, 160) |

## Joints

#### 🔧 Joint: `front_left_wheel_joint` (regular)

| Property | Value |
|----------|-------|
| Defining component | ma_robot (ma_robot) |
| Suppressed | False |
| Motion type | revolute (enum=1) |
| Axis | (0.0000, 1.0000, 0.0000) |
| **Connections** | |
| Parent (occ2) | `base_link` |
| Parent path | `base_link:1` |
| Child (occ1) | `Tire_1` |
| Child path | `front_left_wheel_link:1+Tire (1):1` |
| **Geometry (all sources, raw cm)** | |
| geometryOrOriginOne | (13.0000, 6.3000, 4.5000) |
| geometryOrOriginTwo | (13.0000, 6.0000, 4.5000) |
| occ1.transform | (2.2900, -8.1841, -2.5495) ctx_depth=1 |
| occ1.global (assembled) | (14.2900, 6.1477, 2.6952) |
| occ2.transform | (0.0000, 0.0000, 2.5000) ctx_depth=0 |
| occ2.global (assembled) | (0.0000, 0.0000, 2.5000) |
| **Picked origin (m)** | (0.130000, 0.063000, 0.045000) via `geometryOrOriginOne` |

#### 🔧 Joint: `front_right_wheel_joint` (regular)

| Property | Value |
|----------|-------|
| Defining component | ma_robot (ma_robot) |
| Suppressed | False |
| Motion type | revolute (enum=1) |
| Axis | (-0.0000, -1.0000, 0.0000) |
| **Connections** | |
| Parent (occ2) | `base_link` |
| Parent path | `base_link:1` |
| Child (occ1) | `Tire_2` |
| Child path | `front_right_wheel_link:1+Tire (2):1` |
| **Geometry (all sources, raw cm)** | |
| geometryOrOriginOne | (13.0000, -18.9000, 4.5000) |
| geometryOrOriginTwo | (13.0000, -18.5000, 4.5000) |
| occ1.transform | (-4.9797, -5.7440, 6.3048) ctx_depth=1 |
| occ1.global (assembled) | (14.2900, -18.7477, 6.3048) |
| occ2.transform | (0.0000, 0.0000, 2.5000) ctx_depth=0 |
| occ2.global (assembled) | (0.0000, 0.0000, 2.5000) |
| **Picked origin (m)** | (0.130000, -0.189000, 0.045000) via `geometryOrOriginOne` |

#### 🔧 Joint: `rear_left_wheel_joint` (regular)

| Property | Value |
|----------|-------|
| Defining component | ma_robot (ma_robot) |
| Suppressed | False |
| Motion type | revolute (enum=1) |
| Axis | (0.0000, 1.0000, 0.0000) |
| **Connections** | |
| Parent (occ2) | `base_link` |
| Parent path | `base_link:1` |
| Child (occ1) | `Tire` |
| Child path | `rear_left_wheel_link:1+Tire:1` |
| **Geometry (all sources, raw cm)** | |
| geometryOrOriginOne | (-2.0000, 7.0000, 4.5000) |
| geometryOrOriginTwo | (-2.0000, 6.0000, 4.5000) |
| occ1.transform | (-3.2900, 6.2477, 6.3048) ctx_depth=1 |
| occ1.global (assembled) | (-3.2900, 6.2477, 6.3048) |
| occ2.transform | (0.0000, 0.0000, 2.5000) ctx_depth=0 |
| occ2.global (assembled) | (0.0000, 0.0000, 2.5000) |
| **Picked origin (m)** | (-0.020000, 0.070000, 0.045000) via `geometryOrOriginOne` |

#### 🔧 Joint: `rear_right_wheel_joint` (regular)

| Property | Value |
|----------|-------|
| Defining component | ma_robot (ma_robot) |
| Suppressed | False |
| Motion type | revolute (enum=1) |
| Axis | (-0.0000, -1.0000, 0.0000) |
| **Connections** | |
| Parent (occ2) | `base_link` |
| Parent path | `base_link:1` |
| Child (occ1) | `Tire_3` |
| Child path | `rear_right_wheel_link:1+Tire (3):1` |
| **Geometry (all sources, raw cm)** | |
| geometryOrOriginOne | (-2.0000, -18.9000, 4.5000) |
| geometryOrOriginTwo | (-2.0000, -18.5000, 4.5000) |
| occ1.transform | (-1.7622, 6.1816, 2.6952) ctx_depth=1 |
| occ1.global (assembled) | (-3.2900, -18.5477, 2.6952) |
| occ2.transform | (0.0000, 0.0000, 2.5000) ctx_depth=0 |
| occ2.global (assembled) | (0.0000, 0.0000, 2.5000) |
| **Picked origin (m)** | (-0.020000, -0.189000, 0.045000) via `geometryOrOriginOne` |

#### 🔧 Joint: `rplidar_s2_joint` (regular)

| Property | Value |
|----------|-------|
| Defining component | ma_robot (ma_robot) |
| Suppressed | False |
| Motion type | rigid (enum=0) |
| Axis | (0.0000, 0.0000, 1.0000) |
| **Connections** | |
| Parent (occ2) | `base_link` |
| Parent path | `base_link:1` |
| Child (occ1) | `rplidar_s2_link` |
| Child path | `rplidar_s2_link:1` |
| **Geometry (all sources, raw cm)** | |
| geometryOrOriginOne | (9.9270, -6.2500, 7.5000) |
| geometryOrOriginTwo | (4.9270, -6.2500, 7.5000) |
| occ1.transform | (-43.3747, -65.7506, 7.1815) ctx_depth=0 |
| occ1.global (assembled) | (-43.3747, -65.7506, 7.1815) |
| occ2.transform | (0.0000, 0.0000, 2.5000) ctx_depth=0 |
| occ2.global (assembled) | (0.0000, 0.0000, 2.5000) |
| **Picked origin (m)** | (0.099270, -0.062500, 0.075000) via `geometryOrOriginOne` |

#### 🔧 Joint: `zed2_camera_joint` (regular)

| Property | Value |
|----------|-------|
| Defining component | ma_robot (ma_robot) |
| Suppressed | False |
| Motion type | rigid (enum=0) |
| Axis | (0.0000, 0.0000, 1.0000) |
| **Connections** | |
| Parent (occ2) | `base_link` |
| Parent path | `base_link:1` |
| Child (occ1) | `zed2_camera_link` |
| Child path | `zed2_camera_link:1` |
| **Geometry (all sources, raw cm)** | |
| geometryOrOriginOne | (14.5000, -6.2500, 6.0000) |
| geometryOrOriginTwo | (14.5000, -6.2500, 6.0000) |
| occ1.transform | (14.5000, -6.2500, 1.7629) ctx_depth=0 |
| occ1.global (assembled) | (14.5000, -6.2500, 1.7629) |
| occ2.transform | (0.0000, 0.0000, 2.5000) ctx_depth=0 |
| occ2.global (assembled) | (0.0000, 0.0000, 2.5000) |
| **Picked origin (m)** | (0.145000, -0.062500, 0.060000) via `geometryOrOriginOne` |

## Quick Comparison Table

Compare these values with Fusion 360 Properties panel (right-click → Properties).

| Component | Mass (g) | World X,Y,Z (mm) | CoM X,Y,Z (mm) | Material |
|-----------|----------|-------------------|-----------------|----------|
| base_link | 2899.172 | (0.00, 0.00, 25.00) | (41.57, -62.49, 49.42) | Acetal_Resin_Black |
| Rim_1 | 0.000 | (119.28, 149.75, 64.53) | (0.00, 0.00, 0.00) |  |
| Tire_1 | 611.603 | (142.90, 61.48, 26.95) | (155.80, 55.99, 8.90) | Steel |
| Rim_2 | 0.000 | (93.83, -251.35, 12.08) | (0.00, 0.00, 0.00) |  |
| Tire_2 | 611.603 | (142.90, -187.48, 63.05) | (155.80, -192.96, 45.00) | Steel |
| Rim | 0.000 | (-0.72, 6.44, 12.08) | (0.00, 0.00, 0.00) |  |
| Tire | 611.603 | (-32.90, 62.48, 63.05) | (-20.00, 56.99, 45.00) | Steel |
| Rim_3 | 0.000 | (-16.00, -240.86, 12.08) | (0.00, 0.00, 0.00) |  |
| Tire_3 | 611.603 | (-32.90, -185.48, 26.95) | (-20.00, -190.96, 8.90) | Steel |
| rplidar_s2_link | 203.764 | (-433.75, -657.51, 71.81) | (-1028.76, -124.56, 84.70) | Steel |
| zed2_camera_link | 178.229 | (145.00, -62.50, 17.63) | (145.00, -46.99, 60.02) | PA_11_Nylon_HP_11_30_with_EOS_P_396_3D_Printer |

## Joint Origins Comparison

All origins shown in multiple coordinate systems for debugging.

| Joint | Source | Origin (cm, raw) | Origin (m, picked) | Motion | Axis |
|-------|--------|------------------|-------------------|--------|------|
| front_left_wheel_joint | geometryOrOriginOne | goo1(13.00, 6.30, 4.50) | (0.1300, 0.0630, 0.0450) | revolute | (0.0, 1.0, 0.0) |
| front_right_wheel_joint | geometryOrOriginOne | goo1(13.00, -18.90, 4.50) | (0.1300, -0.1890, 0.0450) | revolute | (-0.0, -1.0, 0.0) |
| rear_left_wheel_joint | geometryOrOriginOne | goo1(-2.00, 7.00, 4.50) | (-0.0200, 0.0700, 0.0450) | revolute | (0.0, 1.0, 0.0) |
| rear_right_wheel_joint | geometryOrOriginOne | goo1(-2.00, -18.90, 4.50) | (-0.0200, -0.1890, 0.0450) | revolute | (-0.0, -1.0, 0.0) |
| rplidar_s2_joint | geometryOrOriginOne | goo1(9.93, -6.25, 7.50) | (0.0993, -0.0625, 0.0750) | rigid | (0.0, 0.0, 1.0) |
| zed2_camera_joint | geometryOrOriginOne | goo1(14.50, -6.25, 6.00) | (0.1450, -0.0625, 0.0600) | rigid | (0.0, 0.0, 1.0) |

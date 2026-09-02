# Extraction Report: ma_robot

**Exported:** 2026-09-02T22:20:11.504871
**Exporter:** v3.1.0

## Summary

| Metric | Value |
|--------|-------|
| Occurrences | 55 |
| Subassemblies | 4 |
| Leaf components | 51 |
| Joints (total) | 6 |
| As-built joints | 0 |
| Regular joints | 6 |
| Max nesting depth | 1 |

## Assembly Hierarchy

```
[ma_robot]  (design root)
  ├── ma_robot  (2899.2g)
  ├── rplidar_s2_link  (203.8g)
  ├── zed2_camera_link  (178.2g)
  [front_left_wheel_link]  (depth=0, children=12)
    ├── Part1_1  (80.6g, Steel)
    ├── Part1_1  (80.6g, Steel)
    ├── Part2_1  (398.7g, Steel)
    ├── Part4_1  (45.3g, Steel)
    ├── Part4_1  (45.3g, Steel)
    ├── Part4_1  (45.3g, Steel)
    ├── Part4_1  (45.3g, Steel)
    ├── Part4_1  (45.3g, Steel)
    ├── Part4_1  (45.3g, Steel)
    ├── Part4_1  (45.3g, Steel)
    ├── Part4_1  (45.3g, Steel)
    ├── Part4_1  (45.3g, Steel)
  [front_right_wheel_link]  (depth=0, children=12)
    ├── Part1_1_Mirror  (80.6g, Steel)
    ├── Part1_1_Mirror  (80.6g, Steel)
    ├── Part2_1_Mirror  (398.7g, Steel)
    ├── Part4_1_Mirror  (45.3g, Steel)
    ├── Part4_1_Mirror  (45.3g, Steel)
    ├── Part4_1_Mirror  (45.3g, Steel)
    ├── Part4_1_Mirror  (45.3g, Steel)
    ├── Part4_1_Mirror  (45.3g, Steel)
    ├── Part4_1_Mirror  (45.3g, Steel)
    ├── Part4_1_Mirror  (45.3g, Steel)
    ├── Part4_1_Mirror  (45.3g, Steel)
    ├── Part4_1_Mirror  (45.3g, Steel)
  [rear_left_wheel_link]  (depth=0, children=12)
    ├── Part1_2_Mirror  (80.6g, Steel)
    ├── Part1_2_Mirror  (80.6g, Steel)
    ├── Part2_2_Mirror  (398.7g, Steel)
    ├── Part4_2_Mirror  (45.3g, Steel)
    ├── Part4_2_Mirror  (45.3g, Steel)
    ├── Part4_2_Mirror  (45.3g, Steel)
    ├── Part4_2_Mirror  (45.3g, Steel)
    ├── Part4_2_Mirror  (45.3g, Steel)
    ├── Part4_2_Mirror  (45.3g, Steel)
    ├── Part4_2_Mirror  (45.3g, Steel)
    ├── Part4_2_Mirror  (45.3g, Steel)
    ├── Part4_2_Mirror  (45.3g, Steel)
  [rear_right_wheel_link]  (depth=0, children=12)
    ├── Part1_2  (80.6g, Steel)
    ├── Part1_2  (80.6g, Steel)
    ├── Part2_2  (398.7g, Steel)
    ├── Part4_2  (45.3g, Steel)
    ├── Part4_2  (45.3g, Steel)
    ├── Part4_2  (45.3g, Steel)
    ├── Part4_2  (45.3g, Steel)
    ├── Part4_2  (45.3g, Steel)
    ├── Part4_2  (45.3g, Steel)
    ├── Part4_2  (45.3g, Steel)
    ├── Part4_2  (45.3g, Steel)
    ├── Part4_2  (45.3g, Steel)
```

## Occurrences

### Depth 0

#### 🔧 COMPONENT: `ma_robot`

| Property | Value |
|----------|-------|
| Full path | `__design_root__` |
| Component name | ma_robot |
| Depth | 0 |
| Path segments | ma_robot |
| **Transforms** | |
| Global position (m) | (0.000000, 0.000000, 0.000000) |
| Global position (mm) | (0.00, 0.00, 0.00) |
| Local transform (m) | (0.000000, 0.000000, 0.000000) |
| Assembly context depth | 0 |
| transform2 (m) | (0.000000, 0.000000, 0.000000) |
| **Physical** | |
| Mass | 2.899152 kg (2899.152 g) |
| Volume | 2.034492e-03 m³ |
| Density | 1425.0 kg/m³ |
| Surface area | 1.349898e-01 m² |
| Body count | 2 |
| CoM (component-local, m) | (0.041574, -0.062494, 0.024420) |
| CoM (global, m) | (0.041574, -0.062494, 0.024420) |
| CoM (global, mm) | (41.57, -62.49, 24.42) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 2.102542e-02, 2.053445e-02, 3.686139e-02 |
| Ixy, Ixz, Iyz | 7.533385e-03, -2.665166e-03, 4.423977e-03 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 7.973742e-03, 1.379462e-02, 2.052761e-02 |
| Ixy, Ixz, Iyz | 9.036729e-07, 2.781740e-04, -4.481306e-07 |
| Bounding box (m) | 0.2630 × 0.2450 × 0.1200 |
| Bounding box (mm) | 263.04 × 245.00 × 120.00 |
| **Material & Appearance** | |
| Material | Acetal_Resin_Black |
| Appearance | Plastic_Glossy_Black |
| Color (RGB 0-1) | (0.098, 0.098, 0.098) |
| Color (RGB 0-255) | (25, 25, 25) |
| **Per-body breakdown** | |
| Body 0: Body1 | mass=2899.091g, material=Acetal_Resin_Black, inertia_src=api |
| Body 1: Body2 | mass=0.060g, material=Acetal_Resin_Black, inertia_src=api |

#### 📦 SUBASSEMBLY: `front_left_wheel_link`

| Property | Value |
|----------|-------|
| Full path | `front_left_wheel_link:1` |
| Component name | front_left_wheel_link |
| Depth | 0 |
| Path segments | front_left_wheel_link |
| Child occurrences | 12 |
| **Transforms** | |
| Global position (m) | (0.000000, 0.000000, 0.000000) |
| Global position (mm) | (0.00, 0.00, 0.00) |
| Local transform (m) | (0.000000, 0.000000, 0.000000) |
| Assembly context depth | 0 |
| transform2 (m) | (0.000000, 0.000000, 0.000000) |

#### 📦 SUBASSEMBLY: `front_right_wheel_link`

| Property | Value |
|----------|-------|
| Full path | `front_right_wheel_link:1` |
| Component name | front_right_wheel_link |
| Depth | 0 |
| Path segments | front_right_wheel_link |
| Child occurrences | 12 |
| **Transforms** | |
| Global position (m) | (0.000000, -0.300000, 0.000000) |
| Global position (mm) | (0.00, -300.00, 0.00) |
| Local transform (m) | (0.000000, -0.300000, 0.000000) |
| Assembly context depth | 0 |
| transform2 (m) | (0.000000, -0.300000, 0.000000) |

#### 📦 SUBASSEMBLY: `rear_left_wheel_link`

| Property | Value |
|----------|-------|
| Full path | `rear_left_wheel_link:1` |
| Component name | rear_left_wheel_link |
| Depth | 0 |
| Path segments | rear_left_wheel_link |
| Child occurrences | 12 |
| **Transforms** | |
| Global position (m) | (0.000000, 0.050000, 0.000000) |
| Global position (mm) | (0.00, 50.00, 0.00) |
| Local transform (m) | (0.000000, 0.050000, 0.000000) |
| Assembly context depth | 0 |
| transform2 (m) | (0.000000, 0.050000, 0.000000) |

#### 📦 SUBASSEMBLY: `rear_right_wheel_link`

| Property | Value |
|----------|-------|
| Full path | `rear_right_wheel_link:1` |
| Component name | rear_right_wheel_link |
| Depth | 0 |
| Path segments | rear_right_wheel_link |
| Child occurrences | 12 |
| **Transforms** | |
| Global position (m) | (0.000000, 0.000000, 0.000000) |
| Global position (mm) | (0.00, 0.00, 0.00) |
| Local transform (m) | (0.000000, 0.000000, 0.000000) |
| Assembly context depth | 0 |
| transform2 (m) | (0.000000, 0.000000, 0.000000) |

#### 🔧 COMPONENT: `rplidar_s2_link`

| Property | Value |
|----------|-------|
| Full path | `rplidar_s2_link:1` |
| Component name | rplidar_s2_link |
| Depth | 0 |
| Path segments | rplidar_s2_link |
| **Transforms** | |
| Global position (m) | (-0.433747, -0.657506, 0.046815) |
| Global position (mm) | (-433.75, -657.51, 46.81) |
| Local transform (m) | (-0.433747, -0.657506, 0.046815) |
| Assembly context depth | 0 |
| transform2 (m) | (-0.433747, -0.657506, 0.046815) |
| **Physical** | |
| Mass | 0.203764 kg (203.764 g) |
| Volume | 3.373166e-05 m³ |
| Density | 6040.7 kg/m³ |
| Surface area | 4.422538e-02 m² |
| Body count | 28 |
| CoM (component-local, m) | (-0.595013, 0.532942, 0.012880) |
| CoM (global, m) | (-1.028760, -0.124565, 0.059695) |
| CoM (global, mm) | (-1028.76, -124.56, 59.70) |
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
| Global position (m) | (0.145000, -0.062500, -0.007371) |
| Global position (mm) | (145.00, -62.50, -7.37) |
| Local transform (m) | (0.145000, -0.062500, -0.007371) |
| Assembly context depth | 0 |
| transform2 (m) | (0.145000, -0.062500, -0.007371) |
| **Physical** | |
| Mass | 0.178229 kg (178.229 g) |
| Volume | 1.521051e-04 m³ |
| Density | 1171.8 kg/m³ |
| Surface area | 2.200474e-02 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.000000, 0.015505, 0.042389) |
| CoM (global, m) | (0.145000, -0.046995, 0.035018) |
| CoM (global, mm) | (145.00, -46.99, 35.02) |
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

#### 🔧 COMPONENT: `Part1_1`

| Property | Value |
|----------|-------|
| Full path | `front_left_wheel_link:1+Part1 (1):1` |
| Component name | Part1 (1) |
| Depth | 1 |
| Path segments | front_left_wheel_link → Part1_1 |
| Parent path | `front_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.130000, 0.073000, 0.020000) |
| Global position (mm) | (130.00, 73.00, 20.00) |
| Local transform (m) | (0.130000, 0.073000, 0.020000) |
| Assembly context depth | 1 |
| transform2 (m) | (0.130000, 0.073000, 0.020000) |
| **Physical** | |
| Mass | 0.080563 kg (80.563 g) |
| Volume | 1.026286e-05 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 9.378219e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (-0.000000, -0.000000, 0.002406) |
| CoM (global, m) | (0.130000, 0.073000, 0.022406) |
| CoM (global, mm) | (130.00, 73.00, 22.41) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 3.067888e-05, 3.067884e-05, 5.976875e-05 |
| Ixy, Ixz, Iyz | -3.627335e-11, 2.154204e-12, 4.197040e-12 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 3.021264e-05, 3.021260e-05, 5.976875e-05 |
| Ixy, Ixz, Iyz | -3.627332e-11, -6.187036e-13, -1.046723e-12 |
| Bounding box (m) | 0.0766 × 0.0768 × 0.0107 |
| Bounding box (mm) | 76.62 × 76.81 × 10.69 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_202_209_238 |
| Color (RGB 0-1) | (0.792, 0.820, 0.933) |
| Color (RGB 0-255) | (202, 209, 238) |

#### 🔧 COMPONENT: `Part1_1`

| Property | Value |
|----------|-------|
| Full path | `front_left_wheel_link:1+Part1 (1):2` |
| Component name | Part1 (1) |
| Depth | 1 |
| Path segments | front_left_wheel_link → Part1_1 |
| Parent path | `front_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.130000, 0.031464, 0.020000) |
| Global position (mm) | (130.00, 31.46, 20.00) |
| Local transform (m) | (0.130000, 0.031464, 0.020000) |
| Assembly context depth | 1 |
| transform2 (m) | (0.130000, 0.031464, 0.020000) |
| **Physical** | |
| Mass | 0.080563 kg (80.563 g) |
| Volume | 1.026286e-05 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 9.378219e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (-0.000000, -0.000000, 0.002406) |
| CoM (global, m) | (0.130000, 0.031463, 0.022406) |
| CoM (global, mm) | (130.00, 31.46, 22.41) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 3.067888e-05, 3.067884e-05, 5.976875e-05 |
| Ixy, Ixz, Iyz | -3.627335e-11, 2.154204e-12, 4.197040e-12 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 3.021264e-05, 3.021260e-05, 5.976875e-05 |
| Ixy, Ixz, Iyz | -3.627332e-11, -6.187036e-13, -1.046723e-12 |
| Bounding box (m) | 0.0766 × 0.0768 × 0.0107 |
| Bounding box (mm) | 76.62 × 76.81 × 10.69 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_202_209_238 |
| Color (RGB 0-1) | (0.792, 0.820, 0.933) |
| Color (RGB 0-255) | (202, 209, 238) |

#### 🔧 COMPONENT: `Part2_1`

| Property | Value |
|----------|-------|
| Full path | `front_left_wheel_link:1+Part2 (1):1` |
| Component name | Part2 (1) |
| Depth | 1 |
| Path segments | front_left_wheel_link → Part2_1 |
| Parent path | `front_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.130000, 0.070000, 0.020000) |
| Global position (mm) | (130.00, 70.00, 20.00) |
| Local transform (m) | (0.130000, 0.070000, 0.020000) |
| Assembly context depth | 1 |
| transform2 (m) | (0.130000, 0.070000, 0.020000) |
| **Physical** | |
| Mass | 0.398719 kg (398.719 g) |
| Volume | 5.079219e-05 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.159048e-02 m² |
| Body count | 1 |
| CoM (component-local, m) | (-0.000000, 0.017773, 0.000000) |
| CoM (global, m) | (0.130000, 0.087773, 0.020000) |
| CoM (global, mm) | (130.00, 87.77, 20.00) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 2.179435e-04, 9.886321e-05, 2.179435e-04 |
| Ixy, Ixz, Iyz | 1.360974e-18, -8.924417e-20, -1.786630e-14 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 9.199087e-05, 9.886321e-05, 9.199086e-05 |
| Ixy, Ixz, Iyz | 3.255486e-20, -8.924417e-20, -2.209770e-16 |
| Bounding box (m) | 0.0440 × 0.0360 × 0.0440 |
| Bounding box (mm) | 44.00 × 36.00 × 44.00 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_202_209_238 |
| Color (RGB 0-1) | (0.792, 0.820, 0.933) |
| Color (RGB 0-255) | (202, 209, 238) |

#### 🔧 COMPONENT: `Part4_1`

| Property | Value |
|----------|-------|
| Full path | `front_left_wheel_link:1+Part4 (1):1` |
| Component name | Part4 (1) |
| Depth | 1 |
| Path segments | front_left_wheel_link → Part4_1 |
| Parent path | `front_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.113860, 0.037417, 0.050030) |
| Global position (mm) | (113.86, 37.42, 50.03) |
| Local transform (m) | (0.113860, 0.037417, 0.050030) |
| Assembly context depth | 1 |
| transform2 (m) | (0.113860, 0.037417, 0.050030) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, 0.000000) |
| CoM (global, m) | (0.134860, 0.037417, 0.050030) |
| CoM (global, mm) | (134.86, 37.42, 50.03) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, -1.032722e-17, 1.603606e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.381193e-19, 1.603606e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_1`

| Property | Value |
|----------|-------|
| Full path | `front_left_wheel_link:1+Part4 (1):2` |
| Component name | Part4 (1) |
| Depth | 1 |
| Path segments | front_left_wheel_link → Part4_1 |
| Parent path | `front_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.097624, 0.037417, 0.009320) |
| Global position (mm) | (97.62, 37.42, 9.32) |
| Local transform (m) | (0.097624, 0.037417, 0.009320) |
| Assembly context depth | 1 |
| transform2 (m) | (0.097624, 0.037417, 0.009320) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, 0.000000) |
| CoM (global, m) | (0.118624, 0.037417, 0.009320) |
| CoM (global, mm) | (118.62, 37.42, 9.32) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, -1.032722e-17, 1.603606e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.381193e-19, 1.603606e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_1`

| Property | Value |
|----------|-------|
| Full path | `front_left_wheel_link:1+Part4 (1):3` |
| Component name | Part4 (1) |
| Depth | 1 |
| Path segments | front_left_wheel_link → Part4_1 |
| Parent path | `front_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.099065, 0.038409, 0.033299) |
| Global position (mm) | (99.06, 38.41, 33.30) |
| Local transform (m) | (0.099065, 0.038409, 0.033299) |
| Assembly context depth | 1 |
| transform2 (m) | (0.099065, 0.038409, 0.033299) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, 0.000000) |
| CoM (global, m) | (0.120065, 0.038409, 0.033299) |
| CoM (global, mm) | (120.06, 38.41, 33.30) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, -1.032722e-17, 1.603606e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.381193e-19, 1.603606e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_1`

| Property | Value |
|----------|-------|
| Full path | `front_left_wheel_link:1+Part4 (1):4` |
| Component name | Part4 (1) |
| Depth | 1 |
| Path segments | front_left_wheel_link → Part4_1 |
| Parent path | `front_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.135098, 0.037205, -0.013803) |
| Global position (mm) | (135.10, 37.20, -13.80) |
| Local transform (m) | (0.135098, 0.037205, -0.013803) |
| Assembly context depth | 1 |
| transform2 (m) | (0.135098, 0.037205, -0.013803) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, 0.000000) |
| CoM (global, m) | (0.156098, 0.037205, -0.013803) |
| CoM (global, mm) | (156.10, 37.20, -13.80) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, -1.032722e-17, 1.603606e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.381193e-19, 1.603606e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_1`

| Property | Value |
|----------|-------|
| Full path | `front_left_wheel_link:1+Part4 (1):5` |
| Component name | Part4 (1) |
| Depth | 1 |
| Path segments | front_left_wheel_link → Part4_1 |
| Parent path | `front_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.155437, 0.037417, -0.002698) |
| Global position (mm) | (155.44, 37.42, -2.70) |
| Local transform (m) | (0.155437, 0.037417, -0.002698) |
| Assembly context depth | 1 |
| transform2 (m) | (0.155437, 0.037417, -0.002698) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, 0.000000) |
| CoM (global, m) | (0.176437, 0.037417, -0.002698) |
| CoM (global, mm) | (176.44, 37.42, -2.70) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, -1.032722e-17, 1.603606e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.381193e-19, 1.603606e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_1`

| Property | Value |
|----------|-------|
| Full path | `front_left_wheel_link:1+Part4 (1):6` |
| Component name | Part4 (1) |
| Depth | 1 |
| Path segments | front_left_wheel_link → Part4_1 |
| Parent path | `front_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.112064, 0.037417, -0.008992) |
| Global position (mm) | (112.06, 37.42, -8.99) |
| Local transform (m) | (0.112064, 0.037417, -0.008992) |
| Assembly context depth | 1 |
| transform2 (m) | (0.112064, 0.037417, -0.008992) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, 0.000000) |
| CoM (global, m) | (0.133064, 0.037417, -0.008992) |
| CoM (global, mm) | (133.06, 37.42, -8.99) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, -1.032722e-17, 1.603606e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.381193e-19, 1.603606e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_1`

| Property | Value |
|----------|-------|
| Full path | `front_left_wheel_link:1+Part4 (1):7` |
| Component name | Part4 (1) |
| Depth | 1 |
| Path segments | front_left_wheel_link → Part4_1 |
| Parent path | `front_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.164076, 0.037417, 0.018963) |
| Global position (mm) | (164.08, 37.42, 18.96) |
| Local transform (m) | (0.164076, 0.037417, 0.018963) |
| Assembly context depth | 1 |
| transform2 (m) | (0.164076, 0.037417, 0.018963) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, 0.000000) |
| CoM (global, m) | (0.185076, 0.037417, 0.018963) |
| CoM (global, mm) | (185.08, 37.42, 18.96) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, -1.032722e-17, 1.603606e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.381193e-19, 1.603606e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_1`

| Property | Value |
|----------|-------|
| Full path | `front_left_wheel_link:1+Part4 (1):8` |
| Component name | Part4 (1) |
| Depth | 1 |
| Path segments | front_left_wheel_link → Part4_1 |
| Parent path | `front_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.156771, 0.037417, 0.041109) |
| Global position (mm) | (156.77, 37.42, 41.11) |
| Local transform (m) | (0.156771, 0.037417, 0.041109) |
| Assembly context depth | 1 |
| transform2 (m) | (0.156771, 0.037417, 0.041109) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, 0.000000) |
| CoM (global, m) | (0.177771, 0.037417, 0.041109) |
| CoM (global, mm) | (177.77, 37.42, 41.11) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, -1.032722e-17, 1.603606e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.381193e-19, 1.603606e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_1`

| Property | Value |
|----------|-------|
| Full path | `front_left_wheel_link:1+Part4 (1):9` |
| Component name | Part4 (1) |
| Depth | 1 |
| Path segments | front_left_wheel_link → Part4_1 |
| Parent path | `front_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.136770, 0.037205, 0.053508) |
| Global position (mm) | (136.77, 37.20, 53.51) |
| Local transform (m) | (0.136770, 0.037205, 0.053508) |
| Assembly context depth | 1 |
| transform2 (m) | (0.136770, 0.037205, 0.053508) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, 0.000000) |
| CoM (global, m) | (0.157770, 0.037205, 0.053508) |
| CoM (global, mm) | (157.77, 37.20, 53.51) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, -1.032722e-17, 1.603606e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.381193e-19, 1.603606e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part1_1_Mirror`

| Property | Value |
|----------|-------|
| Full path | `front_right_wheel_link:1+Part1 (1)(Mirror):1` |
| Component name | Part1 (1)(Mirror) |
| Depth | 1 |
| Path segments | front_right_wheel_link → Part1_1_Mirror |
| Parent path | `front_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.130000, -0.197000, 0.020000) |
| Global position (mm) | (130.00, -197.00, 20.00) |
| Local transform (m) | (0.130000, -0.103000, -0.020000) |
| Assembly context depth | 1 |
| transform2 (m) | (0.130000, -0.197000, 0.020000) |
| **Physical** | |
| Mass | 0.080563 kg (80.563 g) |
| Volume | 1.026285e-05 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 9.378219e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (-0.000000, -0.000000, -0.002406) |
| CoM (global, m) | (0.130000, -0.197000, 0.017594) |
| CoM (global, mm) | (130.00, -197.00, 17.59) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 3.067887e-05, 3.067883e-05, 5.976873e-05 |
| Ixy, Ixz, Iyz | -3.614473e-11, -2.154027e-12, -4.199075e-12 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 3.021263e-05, 3.021259e-05, 5.976873e-05 |
| Ixy, Ixz, Iyz | -3.614470e-11, 6.188001e-13, 1.045603e-12 |
| Bounding box (m) | 0.0766 × 0.0768 × 0.0107 |
| Bounding box (mm) | 76.62 × 76.81 × 10.69 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_202_209_238 |
| Color (RGB 0-1) | (0.792, 0.820, 0.933) |
| Color (RGB 0-255) | (202, 209, 238) |

#### 🔧 COMPONENT: `Part1_1_Mirror`

| Property | Value |
|----------|-------|
| Full path | `front_right_wheel_link:1+Part1 (1)(Mirror):2` |
| Component name | Part1 (1)(Mirror) |
| Depth | 1 |
| Path segments | front_right_wheel_link → Part1_1_Mirror |
| Parent path | `front_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.130000, -0.155464, 0.020000) |
| Global position (mm) | (130.00, -155.46, 20.00) |
| Local transform (m) | (0.130000, -0.144536, -0.020000) |
| Assembly context depth | 1 |
| transform2 (m) | (0.130000, -0.155464, 0.020000) |
| **Physical** | |
| Mass | 0.080563 kg (80.563 g) |
| Volume | 1.026285e-05 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 9.378219e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (-0.000000, -0.000000, -0.002406) |
| CoM (global, m) | (0.130000, -0.155464, 0.017594) |
| CoM (global, mm) | (130.00, -155.46, 17.59) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 3.067887e-05, 3.067883e-05, 5.976873e-05 |
| Ixy, Ixz, Iyz | -3.614473e-11, -2.154027e-12, -4.199075e-12 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 3.021263e-05, 3.021259e-05, 5.976873e-05 |
| Ixy, Ixz, Iyz | -3.614470e-11, 6.188001e-13, 1.045603e-12 |
| Bounding box (m) | 0.0766 × 0.0768 × 0.0107 |
| Bounding box (mm) | 76.62 × 76.81 × 10.69 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_202_209_238 |
| Color (RGB 0-1) | (0.792, 0.820, 0.933) |
| Color (RGB 0-255) | (202, 209, 238) |

#### 🔧 COMPONENT: `Part2_1_Mirror`

| Property | Value |
|----------|-------|
| Full path | `front_right_wheel_link:1+Part2 (1)(Mirror):1` |
| Component name | Part2 (1)(Mirror) |
| Depth | 1 |
| Path segments | front_right_wheel_link → Part2_1_Mirror |
| Parent path | `front_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.130000, -0.194000, 0.020000) |
| Global position (mm) | (130.00, -194.00, 20.00) |
| Local transform (m) | (0.130000, -0.106000, -0.020000) |
| Assembly context depth | 1 |
| transform2 (m) | (0.130000, -0.194000, 0.020000) |
| **Physical** | |
| Mass | 0.398719 kg (398.719 g) |
| Volume | 5.079219e-05 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.159048e-02 m² |
| Body count | 1 |
| CoM (component-local, m) | (-0.000000, 0.017773, -0.000000) |
| CoM (global, m) | (0.130000, -0.176227, 0.020000) |
| CoM (global, mm) | (130.00, -176.23, 20.00) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 2.179435e-04, 9.886321e-05, 2.179435e-04 |
| Ixy, Ixz, Iyz | 1.360974e-18, 3.346656e-19, 1.786619e-14 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 9.199087e-05, 9.886321e-05, 9.199086e-05 |
| Ixy, Ixz, Iyz | 5.238201e-20, 3.346656e-19, 2.208457e-16 |
| Bounding box (m) | 0.0440 × 0.0360 × 0.0440 |
| Bounding box (mm) | 44.00 × 36.00 × 44.00 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_202_209_238 |
| Color (RGB 0-1) | (0.792, 0.820, 0.933) |
| Color (RGB 0-255) | (202, 209, 238) |

#### 🔧 COMPONENT: `Part4_1_Mirror`

| Property | Value |
|----------|-------|
| Full path | `front_right_wheel_link:1+Part4 (1)(Mirror):1` |
| Component name | Part4 (1)(Mirror) |
| Depth | 1 |
| Path segments | front_right_wheel_link → Part4_1_Mirror |
| Parent path | `front_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.113860, -0.161417, 0.050030) |
| Global position (mm) | (113.86, -161.42, 50.03) |
| Local transform (m) | (0.113860, -0.138583, -0.050030) |
| Assembly context depth | 1 |
| transform2 (m) | (0.113860, -0.161417, 0.050030) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, -0.000000) |
| CoM (global, m) | (0.134860, -0.161417, 0.050030) |
| CoM (global, mm) | (134.86, -161.42, 50.03) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, 9.981402e-18, 1.568745e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.374221e-19, 1.568745e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_1_Mirror`

| Property | Value |
|----------|-------|
| Full path | `front_right_wheel_link:1+Part4 (1)(Mirror):2` |
| Component name | Part4 (1)(Mirror) |
| Depth | 1 |
| Path segments | front_right_wheel_link → Part4_1_Mirror |
| Parent path | `front_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.097624, -0.161417, 0.009320) |
| Global position (mm) | (97.62, -161.42, 9.32) |
| Local transform (m) | (0.097624, -0.138583, -0.009320) |
| Assembly context depth | 1 |
| transform2 (m) | (0.097624, -0.161417, 0.009320) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, -0.000000) |
| CoM (global, m) | (0.118624, -0.161417, 0.009320) |
| CoM (global, mm) | (118.62, -161.42, 9.32) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, 9.981402e-18, 1.568745e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.374221e-19, 1.568745e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_1_Mirror`

| Property | Value |
|----------|-------|
| Full path | `front_right_wheel_link:1+Part4 (1)(Mirror):3` |
| Component name | Part4 (1)(Mirror) |
| Depth | 1 |
| Path segments | front_right_wheel_link → Part4_1_Mirror |
| Parent path | `front_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.099065, -0.162409, 0.033299) |
| Global position (mm) | (99.06, -162.41, 33.30) |
| Local transform (m) | (0.099065, -0.137591, -0.033299) |
| Assembly context depth | 1 |
| transform2 (m) | (0.099065, -0.162409, 0.033299) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, -0.000000) |
| CoM (global, m) | (0.120065, -0.162409, 0.033299) |
| CoM (global, mm) | (120.06, -162.41, 33.30) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, 9.981402e-18, 1.568745e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.374221e-19, 1.568745e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_1_Mirror`

| Property | Value |
|----------|-------|
| Full path | `front_right_wheel_link:1+Part4 (1)(Mirror):4` |
| Component name | Part4 (1)(Mirror) |
| Depth | 1 |
| Path segments | front_right_wheel_link → Part4_1_Mirror |
| Parent path | `front_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.135098, -0.161205, -0.013803) |
| Global position (mm) | (135.10, -161.20, -13.80) |
| Local transform (m) | (0.135098, -0.138795, 0.013803) |
| Assembly context depth | 1 |
| transform2 (m) | (0.135098, -0.161205, -0.013803) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, -0.000000) |
| CoM (global, m) | (0.156098, -0.161205, -0.013803) |
| CoM (global, mm) | (156.10, -161.20, -13.80) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, 9.981402e-18, 1.568745e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.374221e-19, 1.568745e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_1_Mirror`

| Property | Value |
|----------|-------|
| Full path | `front_right_wheel_link:1+Part4 (1)(Mirror):5` |
| Component name | Part4 (1)(Mirror) |
| Depth | 1 |
| Path segments | front_right_wheel_link → Part4_1_Mirror |
| Parent path | `front_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.155437, -0.161417, -0.002698) |
| Global position (mm) | (155.44, -161.42, -2.70) |
| Local transform (m) | (0.155437, -0.138583, 0.002698) |
| Assembly context depth | 1 |
| transform2 (m) | (0.155437, -0.161417, -0.002698) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, -0.000000) |
| CoM (global, m) | (0.176437, -0.161417, -0.002698) |
| CoM (global, mm) | (176.44, -161.42, -2.70) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, 9.981402e-18, 1.568745e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.374221e-19, 1.568745e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_1_Mirror`

| Property | Value |
|----------|-------|
| Full path | `front_right_wheel_link:1+Part4 (1)(Mirror):6` |
| Component name | Part4 (1)(Mirror) |
| Depth | 1 |
| Path segments | front_right_wheel_link → Part4_1_Mirror |
| Parent path | `front_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.112064, -0.161417, -0.008992) |
| Global position (mm) | (112.06, -161.42, -8.99) |
| Local transform (m) | (0.112064, -0.138583, 0.008992) |
| Assembly context depth | 1 |
| transform2 (m) | (0.112064, -0.161417, -0.008992) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, -0.000000) |
| CoM (global, m) | (0.133064, -0.161417, -0.008992) |
| CoM (global, mm) | (133.06, -161.42, -8.99) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, 9.981402e-18, 1.568745e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.374221e-19, 1.568745e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_1_Mirror`

| Property | Value |
|----------|-------|
| Full path | `front_right_wheel_link:1+Part4 (1)(Mirror):7` |
| Component name | Part4 (1)(Mirror) |
| Depth | 1 |
| Path segments | front_right_wheel_link → Part4_1_Mirror |
| Parent path | `front_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.164076, -0.161417, 0.018963) |
| Global position (mm) | (164.08, -161.42, 18.96) |
| Local transform (m) | (0.164076, -0.138583, -0.018963) |
| Assembly context depth | 1 |
| transform2 (m) | (0.164076, -0.161417, 0.018963) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, -0.000000) |
| CoM (global, m) | (0.185076, -0.161417, 0.018963) |
| CoM (global, mm) | (185.08, -161.42, 18.96) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, 9.981402e-18, 1.568745e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.374221e-19, 1.568745e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_1_Mirror`

| Property | Value |
|----------|-------|
| Full path | `front_right_wheel_link:1+Part4 (1)(Mirror):8` |
| Component name | Part4 (1)(Mirror) |
| Depth | 1 |
| Path segments | front_right_wheel_link → Part4_1_Mirror |
| Parent path | `front_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.156771, -0.161417, 0.041109) |
| Global position (mm) | (156.77, -161.42, 41.11) |
| Local transform (m) | (0.156771, -0.138583, -0.041109) |
| Assembly context depth | 1 |
| transform2 (m) | (0.156771, -0.161417, 0.041109) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, -0.000000) |
| CoM (global, m) | (0.177771, -0.161417, 0.041109) |
| CoM (global, mm) | (177.77, -161.42, 41.11) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, 9.981402e-18, 1.568745e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.374221e-19, 1.568745e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_1_Mirror`

| Property | Value |
|----------|-------|
| Full path | `front_right_wheel_link:1+Part4 (1)(Mirror):9` |
| Component name | Part4 (1)(Mirror) |
| Depth | 1 |
| Path segments | front_right_wheel_link → Part4_1_Mirror |
| Parent path | `front_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.136770, -0.161205, 0.053508) |
| Global position (mm) | (136.77, -161.20, 53.51) |
| Local transform (m) | (0.136770, -0.138795, -0.053508) |
| Assembly context depth | 1 |
| transform2 (m) | (0.136770, -0.161205, 0.053508) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, -0.000000) |
| CoM (global, m) | (0.157770, -0.161205, 0.053508) |
| CoM (global, mm) | (157.77, -161.20, 53.51) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, 9.981402e-18, 1.568745e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.374221e-19, 1.568745e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part1_2_Mirror`

| Property | Value |
|----------|-------|
| Full path | `rear_left_wheel_link:1+Part1 (2)(Mirror):1` |
| Component name | Part1 (2)(Mirror) |
| Depth | 1 |
| Path segments | rear_left_wheel_link → Part1_2_Mirror |
| Parent path | `rear_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.020000, 0.072000, 0.020000) |
| Global position (mm) | (-20.00, 72.00, 20.00) |
| Local transform (m) | (-0.020000, -0.022000, -0.020000) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.020000, 0.072000, 0.020000) |
| **Physical** | |
| Mass | 0.080563 kg (80.563 g) |
| Volume | 1.026285e-05 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 9.378219e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (-0.000000, -0.000000, -0.002406) |
| CoM (global, m) | (-0.020000, 0.072000, 0.017594) |
| CoM (global, mm) | (-20.00, 72.00, 17.59) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 3.067887e-05, 3.067883e-05, 5.976873e-05 |
| Ixy, Ixz, Iyz | -3.614473e-11, -2.154027e-12, -4.199075e-12 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 3.021263e-05, 3.021259e-05, 5.976873e-05 |
| Ixy, Ixz, Iyz | -3.614470e-11, 6.188001e-13, 1.045603e-12 |
| Bounding box (m) | 0.0766 × 0.0768 × 0.0107 |
| Bounding box (mm) | 76.62 × 76.81 × 10.69 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_202_209_238 |
| Color (RGB 0-1) | (0.792, 0.820, 0.933) |
| Color (RGB 0-255) | (202, 209, 238) |

#### 🔧 COMPONENT: `Part1_2_Mirror`

| Property | Value |
|----------|-------|
| Full path | `rear_left_wheel_link:1+Part1 (2)(Mirror):2` |
| Component name | Part1 (2)(Mirror) |
| Depth | 1 |
| Path segments | rear_left_wheel_link → Part1_2_Mirror |
| Parent path | `rear_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.020000, 0.030464, 0.020000) |
| Global position (mm) | (-20.00, 30.46, 20.00) |
| Local transform (m) | (-0.020000, 0.019536, -0.020000) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.020000, 0.030464, 0.020000) |
| **Physical** | |
| Mass | 0.080563 kg (80.563 g) |
| Volume | 1.026285e-05 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 9.378219e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (-0.000000, -0.000000, -0.002406) |
| CoM (global, m) | (-0.020000, 0.030463, 0.017594) |
| CoM (global, mm) | (-20.00, 30.46, 17.59) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 3.067887e-05, 3.067883e-05, 5.976873e-05 |
| Ixy, Ixz, Iyz | -3.614473e-11, -2.154027e-12, -4.199075e-12 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 3.021263e-05, 3.021259e-05, 5.976873e-05 |
| Ixy, Ixz, Iyz | -3.614470e-11, 6.188001e-13, 1.045603e-12 |
| Bounding box (m) | 0.0766 × 0.0768 × 0.0107 |
| Bounding box (mm) | 76.62 × 76.81 × 10.69 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_202_209_238 |
| Color (RGB 0-1) | (0.792, 0.820, 0.933) |
| Color (RGB 0-255) | (202, 209, 238) |

#### 🔧 COMPONENT: `Part2_2_Mirror`

| Property | Value |
|----------|-------|
| Full path | `rear_left_wheel_link:1+Part2 (2)(Mirror):1` |
| Component name | Part2 (2)(Mirror) |
| Depth | 1 |
| Path segments | rear_left_wheel_link → Part2_2_Mirror |
| Parent path | `rear_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.020000, 0.069000, 0.020000) |
| Global position (mm) | (-20.00, 69.00, 20.00) |
| Local transform (m) | (-0.020000, -0.019000, -0.020000) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.020000, 0.069000, 0.020000) |
| **Physical** | |
| Mass | 0.398719 kg (398.719 g) |
| Volume | 5.079219e-05 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.159048e-02 m² |
| Body count | 1 |
| CoM (component-local, m) | (-0.000000, 0.017773, -0.000000) |
| CoM (global, m) | (-0.020000, 0.086773, 0.020000) |
| CoM (global, mm) | (-20.00, 86.77, 20.00) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 2.179435e-04, 9.886321e-05, 2.179435e-04 |
| Ixy, Ixz, Iyz | 1.360974e-18, 3.346656e-19, 1.786619e-14 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 9.199087e-05, 9.886321e-05, 9.199086e-05 |
| Ixy, Ixz, Iyz | 5.238201e-20, 3.346656e-19, 2.208457e-16 |
| Bounding box (m) | 0.0440 × 0.0360 × 0.0440 |
| Bounding box (mm) | 44.00 × 36.00 × 44.00 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_202_209_238 |
| Color (RGB 0-1) | (0.792, 0.820, 0.933) |
| Color (RGB 0-255) | (202, 209, 238) |

#### 🔧 COMPONENT: `Part4_2_Mirror`

| Property | Value |
|----------|-------|
| Full path | `rear_left_wheel_link:1+Part4 (2)(Mirror):1` |
| Component name | Part4 (2)(Mirror) |
| Depth | 1 |
| Path segments | rear_left_wheel_link → Part4_2_Mirror |
| Parent path | `rear_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.036140, 0.036417, -0.010030) |
| Global position (mm) | (-36.14, 36.42, -10.03) |
| Local transform (m) | (-0.036140, 0.013583, 0.010030) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.036140, 0.036417, -0.010030) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, -0.000000) |
| CoM (global, m) | (-0.015140, 0.036417, -0.010030) |
| CoM (global, mm) | (-15.14, 36.42, -10.03) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, 9.981402e-18, 1.568745e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.374221e-19, 1.568745e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_2_Mirror`

| Property | Value |
|----------|-------|
| Full path | `rear_left_wheel_link:1+Part4 (2)(Mirror):2` |
| Component name | Part4 (2)(Mirror) |
| Depth | 1 |
| Path segments | rear_left_wheel_link → Part4_2_Mirror |
| Parent path | `rear_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.052376, 0.036417, 0.030680) |
| Global position (mm) | (-52.38, 36.42, 30.68) |
| Local transform (m) | (-0.052376, 0.013583, -0.030680) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.052376, 0.036417, 0.030680) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, -0.000000) |
| CoM (global, m) | (-0.031376, 0.036417, 0.030680) |
| CoM (global, mm) | (-31.38, 36.42, 30.68) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, 9.981402e-18, 1.568745e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.374221e-19, 1.568745e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_2_Mirror`

| Property | Value |
|----------|-------|
| Full path | `rear_left_wheel_link:1+Part4 (2)(Mirror):3` |
| Component name | Part4 (2)(Mirror) |
| Depth | 1 |
| Path segments | rear_left_wheel_link → Part4_2_Mirror |
| Parent path | `rear_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.050935, 0.037409, 0.006701) |
| Global position (mm) | (-50.94, 37.41, 6.70) |
| Local transform (m) | (-0.050935, 0.012591, -0.006701) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.050935, 0.037409, 0.006701) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, -0.000000) |
| CoM (global, m) | (-0.029935, 0.037409, 0.006701) |
| CoM (global, mm) | (-29.94, 37.41, 6.70) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, 9.981402e-18, 1.568745e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.374221e-19, 1.568745e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_2_Mirror`

| Property | Value |
|----------|-------|
| Full path | `rear_left_wheel_link:1+Part4 (2)(Mirror):4` |
| Component name | Part4 (2)(Mirror) |
| Depth | 1 |
| Path segments | rear_left_wheel_link → Part4_2_Mirror |
| Parent path | `rear_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.014902, 0.036205, 0.053803) |
| Global position (mm) | (-14.90, 36.20, 53.80) |
| Local transform (m) | (-0.014902, 0.013795, -0.053803) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.014902, 0.036205, 0.053803) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, -0.000000) |
| CoM (global, m) | (0.006098, 0.036205, 0.053803) |
| CoM (global, mm) | (6.10, 36.20, 53.80) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, 9.981402e-18, 1.568745e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.374221e-19, 1.568745e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_2_Mirror`

| Property | Value |
|----------|-------|
| Full path | `rear_left_wheel_link:1+Part4 (2)(Mirror):5` |
| Component name | Part4 (2)(Mirror) |
| Depth | 1 |
| Path segments | rear_left_wheel_link → Part4_2_Mirror |
| Parent path | `rear_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.005437, 0.036417, 0.042698) |
| Global position (mm) | (5.44, 36.42, 42.70) |
| Local transform (m) | (0.005437, 0.013583, -0.042698) |
| Assembly context depth | 1 |
| transform2 (m) | (0.005437, 0.036417, 0.042698) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, -0.000000) |
| CoM (global, m) | (0.026437, 0.036417, 0.042698) |
| CoM (global, mm) | (26.44, 36.42, 42.70) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, 9.981402e-18, 1.568745e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.374221e-19, 1.568745e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_2_Mirror`

| Property | Value |
|----------|-------|
| Full path | `rear_left_wheel_link:1+Part4 (2)(Mirror):6` |
| Component name | Part4 (2)(Mirror) |
| Depth | 1 |
| Path segments | rear_left_wheel_link → Part4_2_Mirror |
| Parent path | `rear_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.037936, 0.036417, 0.048992) |
| Global position (mm) | (-37.94, 36.42, 48.99) |
| Local transform (m) | (-0.037936, 0.013583, -0.048992) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.037936, 0.036417, 0.048992) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, -0.000000) |
| CoM (global, m) | (-0.016936, 0.036417, 0.048992) |
| CoM (global, mm) | (-16.94, 36.42, 48.99) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, 9.981402e-18, 1.568745e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.374221e-19, 1.568745e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_2_Mirror`

| Property | Value |
|----------|-------|
| Full path | `rear_left_wheel_link:1+Part4 (2)(Mirror):7` |
| Component name | Part4 (2)(Mirror) |
| Depth | 1 |
| Path segments | rear_left_wheel_link → Part4_2_Mirror |
| Parent path | `rear_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.014076, 0.036417, 0.021037) |
| Global position (mm) | (14.08, 36.42, 21.04) |
| Local transform (m) | (0.014076, 0.013583, -0.021037) |
| Assembly context depth | 1 |
| transform2 (m) | (0.014076, 0.036417, 0.021037) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, -0.000000) |
| CoM (global, m) | (0.035076, 0.036417, 0.021037) |
| CoM (global, mm) | (35.08, 36.42, 21.04) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, 9.981402e-18, 1.568745e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.374221e-19, 1.568745e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_2_Mirror`

| Property | Value |
|----------|-------|
| Full path | `rear_left_wheel_link:1+Part4 (2)(Mirror):8` |
| Component name | Part4 (2)(Mirror) |
| Depth | 1 |
| Path segments | rear_left_wheel_link → Part4_2_Mirror |
| Parent path | `rear_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.006771, 0.036417, -0.001109) |
| Global position (mm) | (6.77, 36.42, -1.11) |
| Local transform (m) | (0.006771, 0.013583, 0.001109) |
| Assembly context depth | 1 |
| transform2 (m) | (0.006771, 0.036417, -0.001109) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, -0.000000) |
| CoM (global, m) | (0.027771, 0.036417, -0.001109) |
| CoM (global, mm) | (27.77, 36.42, -1.11) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, 9.981402e-18, 1.568745e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.374221e-19, 1.568745e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_2_Mirror`

| Property | Value |
|----------|-------|
| Full path | `rear_left_wheel_link:1+Part4 (2)(Mirror):9` |
| Component name | Part4 (2)(Mirror) |
| Depth | 1 |
| Path segments | rear_left_wheel_link → Part4_2_Mirror |
| Parent path | `rear_left_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.013230, 0.036205, -0.013508) |
| Global position (mm) | (-13.23, 36.20, -13.51) |
| Local transform (m) | (-0.013230, 0.013795, 0.013508) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.013230, 0.036205, -0.013508) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, -0.000000) |
| CoM (global, m) | (0.007770, 0.036205, -0.013508) |
| CoM (global, mm) | (7.77, 36.20, -13.51) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, 9.981402e-18, 1.568745e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.374221e-19, 1.568745e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part1_2`

| Property | Value |
|----------|-------|
| Full path | `rear_right_wheel_link:1+Part1 (2):1` |
| Component name | Part1 (2) |
| Depth | 1 |
| Path segments | rear_right_wheel_link → Part1_2 |
| Parent path | `rear_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.020000, -0.197000, 0.020000) |
| Global position (mm) | (-20.00, -197.00, 20.00) |
| Local transform (m) | (-0.020000, -0.197000, 0.020000) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.020000, -0.197000, 0.020000) |
| **Physical** | |
| Mass | 0.080563 kg (80.563 g) |
| Volume | 1.026286e-05 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 9.378219e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (-0.000000, -0.000000, 0.002406) |
| CoM (global, m) | (-0.020000, -0.197000, 0.022406) |
| CoM (global, mm) | (-20.00, -197.00, 22.41) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 3.067888e-05, 3.067884e-05, 5.976875e-05 |
| Ixy, Ixz, Iyz | -3.627335e-11, 2.154204e-12, 4.197040e-12 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 3.021264e-05, 3.021260e-05, 5.976875e-05 |
| Ixy, Ixz, Iyz | -3.627332e-11, -6.187036e-13, -1.046723e-12 |
| Bounding box (m) | 0.0766 × 0.0768 × 0.0107 |
| Bounding box (mm) | 76.62 × 76.81 × 10.69 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_202_209_238 |
| Color (RGB 0-1) | (0.792, 0.820, 0.933) |
| Color (RGB 0-255) | (202, 209, 238) |

#### 🔧 COMPONENT: `Part1_2`

| Property | Value |
|----------|-------|
| Full path | `rear_right_wheel_link:1+Part1 (2):2` |
| Component name | Part1 (2) |
| Depth | 1 |
| Path segments | rear_right_wheel_link → Part1_2 |
| Parent path | `rear_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.020000, -0.155464, 0.020000) |
| Global position (mm) | (-20.00, -155.46, 20.00) |
| Local transform (m) | (-0.020000, -0.155464, 0.020000) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.020000, -0.155464, 0.020000) |
| **Physical** | |
| Mass | 0.080563 kg (80.563 g) |
| Volume | 1.026286e-05 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 9.378219e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (-0.000000, -0.000000, 0.002406) |
| CoM (global, m) | (-0.020000, -0.155464, 0.022406) |
| CoM (global, mm) | (-20.00, -155.46, 22.41) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 3.067888e-05, 3.067884e-05, 5.976875e-05 |
| Ixy, Ixz, Iyz | -3.627335e-11, 2.154204e-12, 4.197040e-12 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 3.021264e-05, 3.021260e-05, 5.976875e-05 |
| Ixy, Ixz, Iyz | -3.627332e-11, -6.187036e-13, -1.046723e-12 |
| Bounding box (m) | 0.0766 × 0.0768 × 0.0107 |
| Bounding box (mm) | 76.62 × 76.81 × 10.69 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_202_209_238 |
| Color (RGB 0-1) | (0.792, 0.820, 0.933) |
| Color (RGB 0-255) | (202, 209, 238) |

#### 🔧 COMPONENT: `Part2_2`

| Property | Value |
|----------|-------|
| Full path | `rear_right_wheel_link:1+Part2 (2):1` |
| Component name | Part2 (2) |
| Depth | 1 |
| Path segments | rear_right_wheel_link → Part2_2 |
| Parent path | `rear_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.020000, -0.194000, 0.020000) |
| Global position (mm) | (-20.00, -194.00, 20.00) |
| Local transform (m) | (-0.020000, -0.194000, 0.020000) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.020000, -0.194000, 0.020000) |
| **Physical** | |
| Mass | 0.398719 kg (398.719 g) |
| Volume | 5.079219e-05 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.159048e-02 m² |
| Body count | 1 |
| CoM (component-local, m) | (-0.000000, 0.017773, 0.000000) |
| CoM (global, m) | (-0.020000, -0.176227, 0.020000) |
| CoM (global, mm) | (-20.00, -176.23, 20.00) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 2.179435e-04, 9.886321e-05, 2.179435e-04 |
| Ixy, Ixz, Iyz | 1.360974e-18, -8.924417e-20, -1.786630e-14 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 9.199087e-05, 9.886321e-05, 9.199086e-05 |
| Ixy, Ixz, Iyz | 3.255486e-20, -8.924417e-20, -2.209770e-16 |
| Bounding box (m) | 0.0440 × 0.0360 × 0.0440 |
| Bounding box (mm) | 44.00 × 36.00 × 44.00 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_202_209_238 |
| Color (RGB 0-1) | (0.792, 0.820, 0.933) |
| Color (RGB 0-255) | (202, 209, 238) |

#### 🔧 COMPONENT: `Part4_2`

| Property | Value |
|----------|-------|
| Full path | `rear_right_wheel_link:1+Part4 (2):1` |
| Component name | Part4 (2) |
| Depth | 1 |
| Path segments | rear_right_wheel_link → Part4_2 |
| Parent path | `rear_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.036140, -0.161417, -0.010030) |
| Global position (mm) | (-36.14, -161.42, -10.03) |
| Local transform (m) | (-0.036140, -0.161417, -0.010030) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.036140, -0.161417, -0.010030) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, 0.000000) |
| CoM (global, m) | (-0.015140, -0.161417, -0.010030) |
| CoM (global, mm) | (-15.14, -161.42, -10.03) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, -1.032722e-17, 1.603606e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.381193e-19, 1.603606e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_2`

| Property | Value |
|----------|-------|
| Full path | `rear_right_wheel_link:1+Part4 (2):2` |
| Component name | Part4 (2) |
| Depth | 1 |
| Path segments | rear_right_wheel_link → Part4_2 |
| Parent path | `rear_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.052376, -0.161417, 0.030680) |
| Global position (mm) | (-52.38, -161.42, 30.68) |
| Local transform (m) | (-0.052376, -0.161417, 0.030680) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.052376, -0.161417, 0.030680) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, 0.000000) |
| CoM (global, m) | (-0.031376, -0.161417, 0.030680) |
| CoM (global, mm) | (-31.38, -161.42, 30.68) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, -1.032722e-17, 1.603606e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.381193e-19, 1.603606e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_2`

| Property | Value |
|----------|-------|
| Full path | `rear_right_wheel_link:1+Part4 (2):3` |
| Component name | Part4 (2) |
| Depth | 1 |
| Path segments | rear_right_wheel_link → Part4_2 |
| Parent path | `rear_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.050935, -0.162409, 0.006701) |
| Global position (mm) | (-50.94, -162.41, 6.70) |
| Local transform (m) | (-0.050935, -0.162409, 0.006701) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.050935, -0.162409, 0.006701) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, 0.000000) |
| CoM (global, m) | (-0.029935, -0.162409, 0.006701) |
| CoM (global, mm) | (-29.94, -162.41, 6.70) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, -1.032722e-17, 1.603606e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.381193e-19, 1.603606e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_2`

| Property | Value |
|----------|-------|
| Full path | `rear_right_wheel_link:1+Part4 (2):4` |
| Component name | Part4 (2) |
| Depth | 1 |
| Path segments | rear_right_wheel_link → Part4_2 |
| Parent path | `rear_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.014902, -0.161205, 0.053803) |
| Global position (mm) | (-14.90, -161.20, 53.80) |
| Local transform (m) | (-0.014902, -0.161205, 0.053803) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.014902, -0.161205, 0.053803) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, 0.000000) |
| CoM (global, m) | (0.006098, -0.161205, 0.053803) |
| CoM (global, mm) | (6.10, -161.20, 53.80) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, -1.032722e-17, 1.603606e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.381193e-19, 1.603606e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_2`

| Property | Value |
|----------|-------|
| Full path | `rear_right_wheel_link:1+Part4 (2):5` |
| Component name | Part4 (2) |
| Depth | 1 |
| Path segments | rear_right_wheel_link → Part4_2 |
| Parent path | `rear_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.005437, -0.161417, 0.042698) |
| Global position (mm) | (5.44, -161.42, 42.70) |
| Local transform (m) | (0.005437, -0.161417, 0.042698) |
| Assembly context depth | 1 |
| transform2 (m) | (0.005437, -0.161417, 0.042698) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, 0.000000) |
| CoM (global, m) | (0.026437, -0.161417, 0.042698) |
| CoM (global, mm) | (26.44, -161.42, 42.70) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, -1.032722e-17, 1.603606e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.381193e-19, 1.603606e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_2`

| Property | Value |
|----------|-------|
| Full path | `rear_right_wheel_link:1+Part4 (2):6` |
| Component name | Part4 (2) |
| Depth | 1 |
| Path segments | rear_right_wheel_link → Part4_2 |
| Parent path | `rear_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.037936, -0.161417, 0.048992) |
| Global position (mm) | (-37.94, -161.42, 48.99) |
| Local transform (m) | (-0.037936, -0.161417, 0.048992) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.037936, -0.161417, 0.048992) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, 0.000000) |
| CoM (global, m) | (-0.016936, -0.161417, 0.048992) |
| CoM (global, mm) | (-16.94, -161.42, 48.99) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, -1.032722e-17, 1.603606e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.381193e-19, 1.603606e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_2`

| Property | Value |
|----------|-------|
| Full path | `rear_right_wheel_link:1+Part4 (2):7` |
| Component name | Part4 (2) |
| Depth | 1 |
| Path segments | rear_right_wheel_link → Part4_2 |
| Parent path | `rear_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.014076, -0.161417, 0.021037) |
| Global position (mm) | (14.08, -161.42, 21.04) |
| Local transform (m) | (0.014076, -0.161417, 0.021037) |
| Assembly context depth | 1 |
| transform2 (m) | (0.014076, -0.161417, 0.021037) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, 0.000000) |
| CoM (global, m) | (0.035076, -0.161417, 0.021037) |
| CoM (global, mm) | (35.08, -161.42, 21.04) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, -1.032722e-17, 1.603606e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.381193e-19, 1.603606e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_2`

| Property | Value |
|----------|-------|
| Full path | `rear_right_wheel_link:1+Part4 (2):8` |
| Component name | Part4 (2) |
| Depth | 1 |
| Path segments | rear_right_wheel_link → Part4_2 |
| Parent path | `rear_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (0.006771, -0.161417, -0.001109) |
| Global position (mm) | (6.77, -161.42, -1.11) |
| Local transform (m) | (0.006771, -0.161417, -0.001109) |
| Assembly context depth | 1 |
| transform2 (m) | (0.006771, -0.161417, -0.001109) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, 0.000000) |
| CoM (global, m) | (0.027771, -0.161417, -0.001109) |
| CoM (global, mm) | (27.77, -161.42, -1.11) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, -1.032722e-17, 1.603606e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.381193e-19, 1.603606e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

#### 🔧 COMPONENT: `Part4_2`

| Property | Value |
|----------|-------|
| Full path | `rear_right_wheel_link:1+Part4 (2):9` |
| Component name | Part4 (2) |
| Depth | 1 |
| Path segments | rear_right_wheel_link → Part4_2 |
| Parent path | `rear_right_wheel_link:1` |
| **Transforms** | |
| Global position (m) | (-0.013230, -0.161205, -0.013508) |
| Global position (mm) | (-13.23, -161.20, -13.51) |
| Local transform (m) | (-0.013230, -0.161205, -0.013508) |
| Assembly context depth | 1 |
| transform2 (m) | (-0.013230, -0.161205, -0.013508) |
| **Physical** | |
| Mass | 0.045349 kg (45.349 g) |
| Volume | 5.776995e-06 m³ |
| Density | 7850.0 kg/m³ |
| Surface area | 1.864547e-03 m² |
| Body count | 1 |
| CoM (component-local, m) | (0.021000, 0.000000, 0.000000) |
| CoM (global, m) | (0.007770, -0.161205, -0.013508) |
| CoM (global, mm) | (7.77, -161.20, -13.51) |
| **Inertia at origin (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 2.470789e-05, 2.470789e-05 |
| Ixy, Ixz, Iyz | -1.729106e-19, -1.032722e-17, 1.603606e-20 |
| **Inertia at CoM (kg·m²)** | |
| Ixx, Iyy, Izz | 1.178635e-06, 4.708795e-06, 4.708795e-06 |
| Ixy, Ixz, Iyz | -1.377707e-19, -1.381193e-19, 1.603606e-20 |
| Bounding box (m) | 0.0420 × 0.0160 × 0.0160 |
| Bounding box (mm) | 42.00 × 16.02 × 16.02 |
| **Material & Appearance** | |
| Material | Steel |
| Appearance | Opaque_64_64_64 |
| Color (RGB 0-1) | (0.251, 0.251, 0.251) |
| Color (RGB 0-255) | (64, 64, 64) |

## Joints

#### 🔧 Joint: `Revolute_5` (regular)

| Property | Value |
|----------|-------|
| Defining component | ma_robot (ma_robot) |
| Suppressed | False |
| Motion type | revolute (enum=1) |
| Axis | (0.0000, 1.0000, 0.0000) |
| **Connections** | |
| Parent (occ2) | `ma_robot` |
| Parent path | `__design_root__` |
| Child (occ1) | `Part2_1` |
| Child path | `front_left_wheel_link:1+Part2 (1):1` |
| **Geometry (all sources, raw cm)** | |
| geometryOrOriginOne | (13.0000, 7.0000, 2.0000) |
| geometryOrOriginTwo | (13.0000, 6.0000, 2.0000) |
| occ1.transform | (13.0000, 7.0000, 2.0000) ctx_depth=1 |
| occ1.global (assembled) | (13.0000, 7.0000, 2.0000) |
| **Picked origin (m)** | (0.130000, 0.070000, 0.020000) via `geometryOrOriginOne` |

#### 🔧 Joint: `Revolute_6` (regular)

| Property | Value |
|----------|-------|
| Defining component | ma_robot (ma_robot) |
| Suppressed | False |
| Motion type | revolute (enum=1) |
| Axis | (0.0000, -1.0000, 0.0000) |
| **Connections** | |
| Parent (occ2) | `ma_robot` |
| Parent path | `__design_root__` |
| Child (occ1) | `Part2_2` |
| Child path | `rear_right_wheel_link:1+Part2 (2):1` |
| **Geometry (all sources, raw cm)** | |
| geometryOrOriginOne | (-2.0000, -16.8000, 2.0000) |
| geometryOrOriginTwo | (-2.0000, -18.5000, 2.0000) |
| occ1.transform | (-2.0000, -19.4000, 2.0000) ctx_depth=1 |
| occ1.global (assembled) | (-2.0000, -19.4000, 2.0000) |
| **Picked origin (m)** | (-0.020000, -0.168000, 0.020000) via `geometryOrOriginOne` |

#### 🔧 Joint: `Revolute_8` (regular)

| Property | Value |
|----------|-------|
| Defining component | ma_robot (ma_robot) |
| Suppressed | False |
| Motion type | revolute (enum=1) |
| Axis | (0.0000, -1.0000, 0.0000) |
| **Connections** | |
| Parent (occ2) | `ma_robot` |
| Parent path | `__design_root__` |
| Child (occ1) | `Part2_1_Mirror` |
| Child path | `front_right_wheel_link:1+Part2 (1)(Mirror):1` |
| **Geometry (all sources, raw cm)** | |
| geometryOrOriginOne | (13.0000, -16.8000, 2.0000) |
| geometryOrOriginTwo | (13.0000, -18.5000, 2.0000) |
| occ1.transform | (13.0000, -10.6000, -2.0000) ctx_depth=1 |
| occ1.global (assembled) | (13.0000, -19.4000, 2.0000) |
| **Picked origin (m)** | (0.130000, -0.168000, 0.020000) via `geometryOrOriginOne` |

#### 🔧 Joint: `Revolute_9` (regular)

| Property | Value |
|----------|-------|
| Defining component | ma_robot (ma_robot) |
| Suppressed | False |
| Motion type | revolute (enum=1) |
| Axis | (0.0000, 1.0000, 0.0000) |
| **Connections** | |
| Parent (occ2) | `ma_robot` |
| Parent path | `__design_root__` |
| Child (occ1) | `Part2_2_Mirror` |
| Child path | `rear_left_wheel_link:1+Part2 (2)(Mirror):1` |
| **Geometry (all sources, raw cm)** | |
| geometryOrOriginOne | (-2.0000, 4.3000, 2.0000) |
| geometryOrOriginTwo | (-2.0000, 6.0000, 2.0000) |
| occ1.transform | (-2.0000, -1.9000, -2.0000) ctx_depth=1 |
| occ1.global (assembled) | (-2.0000, 6.9000, 2.0000) |
| **Picked origin (m)** | (-0.020000, 0.043000, 0.020000) via `geometryOrOriginOne` |

#### 🔧 Joint: `Rigid_1` (regular)

| Property | Value |
|----------|-------|
| Defining component | ma_robot (ma_robot) |
| Suppressed | False |
| Motion type | rigid (enum=0) |
| Axis | (0.0000, 0.0000, 1.0000) |
| **Connections** | |
| Parent (occ2) | `ma_robot` |
| Parent path | `__design_root__` |
| Child (occ1) | `zed2_camera_link` |
| Child path | `zed2_camera_link:1` |
| **Geometry (all sources, raw cm)** | |
| geometryOrOriginOne | (14.5000, -6.2500, 3.5000) |
| geometryOrOriginTwo | (14.5000, -6.2500, 3.5000) |
| occ1.transform | (14.5000, -6.2500, -0.7371) ctx_depth=0 |
| occ1.global (assembled) | (14.5000, -6.2500, -0.7371) |
| **Picked origin (m)** | (0.145000, -0.062500, 0.035000) via `geometryOrOriginOne` |

#### 🔧 Joint: `Rigid_2` (regular)

| Property | Value |
|----------|-------|
| Defining component | ma_robot (ma_robot) |
| Suppressed | False |
| Motion type | rigid (enum=0) |
| Axis | (0.0000, 0.0000, 1.0000) |
| **Connections** | |
| Parent (occ2) | `ma_robot` |
| Parent path | `__design_root__` |
| Child (occ1) | `rplidar_s2_link` |
| Child path | `rplidar_s2_link:1` |
| **Geometry (all sources, raw cm)** | |
| geometryOrOriginOne | (9.9270, -6.2500, 5.0000) |
| geometryOrOriginTwo | (4.9270, -6.2500, 5.0000) |
| occ1.transform | (-43.3747, -65.7506, 4.6815) ctx_depth=0 |
| occ1.global (assembled) | (-43.3747, -65.7506, 4.6815) |
| **Picked origin (m)** | (0.099270, -0.062500, 0.050000) via `geometryOrOriginOne` |

## Quick Comparison Table

Compare these values with Fusion 360 Properties panel (right-click → Properties).

| Component | Mass (g) | World X,Y,Z (mm) | CoM X,Y,Z (mm) | Material |
|-----------|----------|-------------------|-----------------|----------|
| ma_robot | 2899.152 | (0.00, 0.00, 0.00) | (41.57, -62.49, 24.42) | Acetal_Resin_Black |
| Part1_1 | 80.563 | (130.00, 73.00, 20.00) | (130.00, 73.00, 22.41) | Steel |
| Part1_1 | 80.563 | (130.00, 31.46, 20.00) | (130.00, 31.46, 22.41) | Steel |
| Part2_1 | 398.719 | (130.00, 70.00, 20.00) | (130.00, 87.77, 20.00) | Steel |
| Part4_1 | 45.349 | (113.86, 37.42, 50.03) | (134.86, 37.42, 50.03) | Steel |
| Part4_1 | 45.349 | (97.62, 37.42, 9.32) | (118.62, 37.42, 9.32) | Steel |
| Part4_1 | 45.349 | (99.06, 38.41, 33.30) | (120.06, 38.41, 33.30) | Steel |
| Part4_1 | 45.349 | (135.10, 37.20, -13.80) | (156.10, 37.20, -13.80) | Steel |
| Part4_1 | 45.349 | (155.44, 37.42, -2.70) | (176.44, 37.42, -2.70) | Steel |
| Part4_1 | 45.349 | (112.06, 37.42, -8.99) | (133.06, 37.42, -8.99) | Steel |
| Part4_1 | 45.349 | (164.08, 37.42, 18.96) | (185.08, 37.42, 18.96) | Steel |
| Part4_1 | 45.349 | (156.77, 37.42, 41.11) | (177.77, 37.42, 41.11) | Steel |
| Part4_1 | 45.349 | (136.77, 37.20, 53.51) | (157.77, 37.20, 53.51) | Steel |
| Part1_1_Mirror | 80.563 | (130.00, -197.00, 20.00) | (130.00, -197.00, 17.59) | Steel |
| Part1_1_Mirror | 80.563 | (130.00, -155.46, 20.00) | (130.00, -155.46, 17.59) | Steel |
| Part2_1_Mirror | 398.719 | (130.00, -194.00, 20.00) | (130.00, -176.23, 20.00) | Steel |
| Part4_1_Mirror | 45.349 | (113.86, -161.42, 50.03) | (134.86, -161.42, 50.03) | Steel |
| Part4_1_Mirror | 45.349 | (97.62, -161.42, 9.32) | (118.62, -161.42, 9.32) | Steel |
| Part4_1_Mirror | 45.349 | (99.06, -162.41, 33.30) | (120.06, -162.41, 33.30) | Steel |
| Part4_1_Mirror | 45.349 | (135.10, -161.20, -13.80) | (156.10, -161.20, -13.80) | Steel |
| Part4_1_Mirror | 45.349 | (155.44, -161.42, -2.70) | (176.44, -161.42, -2.70) | Steel |
| Part4_1_Mirror | 45.349 | (112.06, -161.42, -8.99) | (133.06, -161.42, -8.99) | Steel |
| Part4_1_Mirror | 45.349 | (164.08, -161.42, 18.96) | (185.08, -161.42, 18.96) | Steel |
| Part4_1_Mirror | 45.349 | (156.77, -161.42, 41.11) | (177.77, -161.42, 41.11) | Steel |
| Part4_1_Mirror | 45.349 | (136.77, -161.20, 53.51) | (157.77, -161.20, 53.51) | Steel |
| Part1_2_Mirror | 80.563 | (-20.00, 72.00, 20.00) | (-20.00, 72.00, 17.59) | Steel |
| Part1_2_Mirror | 80.563 | (-20.00, 30.46, 20.00) | (-20.00, 30.46, 17.59) | Steel |
| Part2_2_Mirror | 398.719 | (-20.00, 69.00, 20.00) | (-20.00, 86.77, 20.00) | Steel |
| Part4_2_Mirror | 45.349 | (-36.14, 36.42, -10.03) | (-15.14, 36.42, -10.03) | Steel |
| Part4_2_Mirror | 45.349 | (-52.38, 36.42, 30.68) | (-31.38, 36.42, 30.68) | Steel |
| Part4_2_Mirror | 45.349 | (-50.94, 37.41, 6.70) | (-29.94, 37.41, 6.70) | Steel |
| Part4_2_Mirror | 45.349 | (-14.90, 36.20, 53.80) | (6.10, 36.20, 53.80) | Steel |
| Part4_2_Mirror | 45.349 | (5.44, 36.42, 42.70) | (26.44, 36.42, 42.70) | Steel |
| Part4_2_Mirror | 45.349 | (-37.94, 36.42, 48.99) | (-16.94, 36.42, 48.99) | Steel |
| Part4_2_Mirror | 45.349 | (14.08, 36.42, 21.04) | (35.08, 36.42, 21.04) | Steel |
| Part4_2_Mirror | 45.349 | (6.77, 36.42, -1.11) | (27.77, 36.42, -1.11) | Steel |
| Part4_2_Mirror | 45.349 | (-13.23, 36.20, -13.51) | (7.77, 36.20, -13.51) | Steel |
| Part1_2 | 80.563 | (-20.00, -197.00, 20.00) | (-20.00, -197.00, 22.41) | Steel |
| Part1_2 | 80.563 | (-20.00, -155.46, 20.00) | (-20.00, -155.46, 22.41) | Steel |
| Part2_2 | 398.719 | (-20.00, -194.00, 20.00) | (-20.00, -176.23, 20.00) | Steel |
| Part4_2 | 45.349 | (-36.14, -161.42, -10.03) | (-15.14, -161.42, -10.03) | Steel |
| Part4_2 | 45.349 | (-52.38, -161.42, 30.68) | (-31.38, -161.42, 30.68) | Steel |
| Part4_2 | 45.349 | (-50.94, -162.41, 6.70) | (-29.94, -162.41, 6.70) | Steel |
| Part4_2 | 45.349 | (-14.90, -161.20, 53.80) | (6.10, -161.20, 53.80) | Steel |
| Part4_2 | 45.349 | (5.44, -161.42, 42.70) | (26.44, -161.42, 42.70) | Steel |
| Part4_2 | 45.349 | (-37.94, -161.42, 48.99) | (-16.94, -161.42, 48.99) | Steel |
| Part4_2 | 45.349 | (14.08, -161.42, 21.04) | (35.08, -161.42, 21.04) | Steel |
| Part4_2 | 45.349 | (6.77, -161.42, -1.11) | (27.77, -161.42, -1.11) | Steel |
| Part4_2 | 45.349 | (-13.23, -161.20, -13.51) | (7.77, -161.20, -13.51) | Steel |
| rplidar_s2_link | 203.764 | (-433.75, -657.51, 46.81) | (-1028.76, -124.56, 59.70) | Steel |
| zed2_camera_link | 178.229 | (145.00, -62.50, -7.37) | (145.00, -46.99, 35.02) | PA_11_Nylon_HP_11_30_with_EOS_P_396_3D_Printer |

## Joint Origins Comparison

All origins shown in multiple coordinate systems for debugging.

| Joint | Source | Origin (cm, raw) | Origin (m, picked) | Motion | Axis |
|-------|--------|------------------|-------------------|--------|------|
| Revolute_5 | geometryOrOriginOne | goo1(13.00, 7.00, 2.00) | (0.1300, 0.0700, 0.0200) | revolute | (0.0, 1.0, 0.0) |
| Revolute_6 | geometryOrOriginOne | goo1(-2.00, -16.80, 2.00) | (-0.0200, -0.1680, 0.0200) | revolute | (0.0, -1.0, 0.0) |
| Revolute_8 | geometryOrOriginOne | goo1(13.00, -16.80, 2.00) | (0.1300, -0.1680, 0.0200) | revolute | (0.0, -1.0, 0.0) |
| Revolute_9 | geometryOrOriginOne | goo1(-2.00, 4.30, 2.00) | (-0.0200, 0.0430, 0.0200) | revolute | (0.0, 1.0, 0.0) |
| Rigid_1 | geometryOrOriginOne | goo1(14.50, -6.25, 3.50) | (0.1450, -0.0625, 0.0350) | rigid | (0.0, 0.0, 1.0) |
| Rigid_2 | geometryOrOriginOne | goo1(9.93, -6.25, 5.00) | (0.0993, -0.0625, 0.0500) | rigid | (0.0, 0.0, 1.0) |

# Export Log: ma_robot

**Generated:** 2026-09-03T00:07:50.518119

```
[00:07:07] fusion2URDF v3.1.0
[00:07:07] Time: 2026-09-03T00:07:07.041166
[00:07:07] Design: ma_robot
[00:07:07] Components: 16
[00:07:07] 
=== PHASE 1: EXTRACTION ===
[00:07:07]   Document unit: mm
[00:07:07] 
=== EXTRACTION: OCCURRENCES ===
[00:07:07]   [LEAF] d=1 zed2_camera_link
[00:07:07]     path: base_link:1+zed2_camera_link:1
[00:07:07]     global_pos: (0.145000, -0.062500, -0.007371) m
[00:07:07]     mass: 0.178229 kg, bodies: 1
[00:07:07]     com_global: (0.145000, -0.046995, 0.035018) m
[00:07:07]     com_component_local: (0.000000, 0.015505, 0.042389) m
[00:07:07]     inertia@origin: ixx=3.897245e-04 iyy=7.565457e-04 izz=4.819299e-04 kg·m²
[00:07:07]     inertia@com:    ixx=2.662726e-05 iyy=4.362977e-04 izz=4.390806e-04 kg·m²
[00:07:07]     material: PA_11_Nylon_HP_11_30_with_EOS_P_396_3D_Printer
[00:07:07]     color: RGB(0.25, 0.25, 0.25) [Nylon_12_with_Formlabs_Fuse_1_3D_Printer]
[00:07:07]     bbox: (0.1747 x 0.0316 x 0.0297) m
[00:07:07]   [LEAF] d=1 rplidar_s2_link
[00:07:07]     path: base_link:1+rplidar_s2_link:1
[00:07:07]     global_pos: (-0.433747, -0.657506, 0.046815) m
[00:07:07]     mass: 0.203764 kg, bodies: 28
[00:07:07]     com_global: (-1.028760, -0.124565, 0.059695) m
[00:07:07]     com_component_local: (-0.595013, 0.532942, 0.012880) m
[00:07:07]     inertia@origin: ixx=5.804326e-02 iyy=7.231055e-02 izz=1.302519e-01 kg·m²
[00:07:07]     inertia@com:    ixx=1.351079e-04 iyy=1.362177e-04 izz=2.370283e-04 kg·m²
[00:07:07]     material: Steel
[00:07:07]     color: RGB(1.00, 1.00, 1.00) [Copper_Raw]
[00:07:07]     bbox: (0.0770 x 0.0770 x 0.0389) m
[00:07:07]   [LEAF] d=2 Rim
[00:07:07]     path: base_link:1+front_left_wheel_link:1+Rim:1
[00:07:07]     global_pos: (0.104444, 0.123316, 0.043512) m
[00:07:07]   [LEAF] d=2 Tire
[00:07:07]     path: base_link:1+front_left_wheel_link:1+Tire:1
[00:07:07]     global_pos: (0.117100, 0.058477, 0.038048) m
[00:07:07]     mass: 0.611603 kg, bodies: 1
[00:07:07]     com_global: (0.130000, 0.052994, 0.020000) m
[00:07:07]     com_component_local: (0.012900, -0.005483, -0.018048) m
[00:07:07]     inertia@origin: ixx=7.441770e-04 iyy=1.033528e-03 izz=6.467384e-04 kg·m²
[00:07:07]     inertia@com:    ixx=5.265770e-04 iyy=7.325315e-04 izz=5.265750e-04 kg·m²
[00:07:07]     material: Steel
[00:07:07]     color: RGB(0.63, 0.63, 0.63) [Opaque_160_160_160]
[00:07:07]     bbox: (0.0900 x 0.0500 x 0.0899) m
[00:07:07]   [SUBASM] d=1 front_left_wheel_link
[00:07:07]     path: base_link:1+front_left_wheel_link:1
[00:07:07]     global_pos: (0.105169, 0.116880, 0.031432) m
[00:07:07]   [LEAF] d=2 Rim_1
[00:07:07]     path: base_link:1+front_right_wheel_link:1+Rim (1):1
[00:07:07]     global_pos: (0.162837, -0.253819, 0.042079) m
[00:07:07]   [LEAF] d=2 Tire_1
[00:07:07]     path: base_link:1+front_right_wheel_link:1+Tire (1):1
[00:07:07]     global_pos: (0.142900, -0.183477, 0.038048) m
[00:07:07]     mass: 0.611603 kg, bodies: 1
[00:07:07]     com_global: (0.155800, -0.188959, 0.020000) m
[00:07:07]     com_component_local: (0.012900, -0.005483, -0.018048) m
[00:07:07]     inertia@origin: ixx=7.441770e-04 iyy=1.033528e-03 izz=6.467384e-04 kg·m²
[00:07:07]     inertia@com:    ixx=5.265770e-04 iyy=7.325315e-04 izz=5.265750e-04 kg·m²
[00:07:07]     material: Steel
[00:07:07]     color: RGB(0.63, 0.63, 0.63) [Opaque_160_160_160]
[00:07:07]     bbox: (0.0900 x 0.0500 x 0.0899) m
[00:07:07]   [SUBASM] d=1 front_right_wheel_link
[00:07:07]     path: base_link:1+front_right_wheel_link:1
[00:07:07]     global_pos: (0.162112, -0.247382, 0.030000) m
[00:07:07]   [LEAF] d=2 Rim_2
[00:07:07]     path: base_link:1+rear_left_wheel_link:1+Rim (2):1
[00:07:07]     global_pos: (-0.000725, 0.124209, 0.045970) m
[00:07:07]   [LEAF] d=2 Tire_2
[00:07:07]     path: base_link:1+rear_left_wheel_link:1+Tire (2):1
[00:07:07]     global_pos: (-0.032900, 0.058477, 0.038048) m
[00:07:07]     mass: 0.611603 kg, bodies: 1
[00:07:07]     com_global: (-0.020000, 0.052994, 0.020000) m
[00:07:07]     com_component_local: (0.012900, -0.005483, -0.018048) m
[00:07:07]     inertia@origin: ixx=7.441770e-04 iyy=1.033528e-03 izz=6.467384e-04 kg·m²
[00:07:07]     inertia@com:    ixx=5.265770e-04 iyy=7.325315e-04 izz=5.265750e-04 kg·m²
[00:07:07]     material: Steel
[00:07:07]     color: RGB(0.63, 0.63, 0.63) [Opaque_160_160_160]
[00:07:07]     bbox: (0.0900 x 0.0500 x 0.0899) m
[00:07:07]   [SUBASM] d=1 rear_left_wheel_link
[00:07:07]     path: base_link:1+rear_left_wheel_link:1
[00:07:07]     global_pos: (0.000000, 0.117773, 0.033890) m
[00:07:07]   [LEAF] d=2 Rim_3
[00:07:07]     path: base_link:1+rear_right_wheel_link:1+Rim (3):1
[00:07:07]     global_pos: (0.000725, -0.241376, 0.041942) m
[00:07:07]   [LEAF] d=2 Tire_3
[00:07:07]     path: base_link:1+rear_right_wheel_link:1+Tire (3):1
[00:07:07]     global_pos: (-0.007100, -0.183477, 0.038048) m
[00:07:07]     mass: 0.611603 kg, bodies: 1
[00:07:07]     com_global: (0.005800, -0.188959, 0.020000) m
[00:07:07]     com_component_local: (0.012900, -0.005483, -0.018048) m
[00:07:07]     inertia@origin: ixx=7.441770e-04 iyy=1.033528e-03 izz=6.467384e-04 kg·m²
[00:07:07]     inertia@com:    ixx=5.265770e-04 iyy=7.325315e-04 izz=5.265750e-04 kg·m²
[00:07:07]     material: Steel
[00:07:07]     color: RGB(0.63, 0.63, 0.63) [Opaque_160_160_160]
[00:07:07]     bbox: (0.0900 x 0.0500 x 0.0899) m
[00:07:07]   [SUBASM] d=1 rear_right_wheel_link
[00:07:07]     path: base_link:1+rear_right_wheel_link:1
[00:07:07]     global_pos: (0.000000, -0.234940, 0.029863) m
[00:07:07]   [SUBASM+BODY] d=0 base_link
[00:07:07]     path: base_link:1
[00:07:07]     global_pos: (0.000000, 0.000000, 0.000000) m
[00:07:07]     mass: 2.899175 kg, bodies: 2
[00:07:07]     com_global: (0.041573, -0.062494, 0.024421) m
[00:07:07]     com_component_local: (0.041573, -0.062494, 0.024421) m
[00:07:07]     inertia@origin: ixx=2.102574e-02 iyy=2.053481e-02 izz=3.686161e-02 kg·m²
[00:07:07]     inertia@com:    ixx=7.973873e-03 iyy=1.379507e-02 izz=2.052792e-02 kg·m²
[00:07:07]     material: Acetal_Resin_Black
[00:07:07]     color: RGB(0.10, 0.10, 0.10) [Plastic_Glossy_Black]
[00:07:07]     bbox: (0.2630 x 0.2450 x 0.1200) m
[00:07:07]   Extracted 15 occurrences
[00:07:07] 
=== EXTRACTION: JOINTS ===
[00:07:07]  regular joint in component 'base_link': proxied joint into assembly context 'base_link:1' for geometry origin
[00:07:07]   WARNING:   regular joint in component 'base_link': failed to read geometry: 'Joint' object has no attribute 'geometry'
[00:07:07]   [REGULAR in base_link] zed2_camera_joint
[00:07:07]     parent(occ2): base_link path=base_link:1
[00:07:07]     child(occ1):  zed2_camera_link path=base_link:1+zed2_camera_link:1
[00:07:07]     geometryOrOriginOne: (14.5000, -6.2500, 3.5000) cm
[00:07:07]     geometryOrOriginTwo: (14.5000, -6.2500, 3.5000) cm
[00:07:07]     occ1.transform: (14.5000, -6.2500, -0.7371) cm (ctx_depth=1)
[00:07:07]     occ1.global:    (14.5000, -6.2500, -0.7371) cm
[00:07:07]     occ2.transform: (0.0000, 0.0000, 0.0000) cm (ctx_depth=0)
[00:07:07]     occ2.global:    (0.0000, 0.0000, 0.0000) cm
[00:07:07]  -> origin_global: (0.145000, -0.062500, 0.035000) m [via geometryOrOriginOne_world] [world]
[00:07:07]     motion: rigid, axis: (0.000, 0.000, 1.000)
[00:07:07]  regular joint in component 'base_link': proxied joint into assembly context 'base_link:1' for geometry origin
[00:07:07]   WARNING:   regular joint in component 'base_link': failed to read geometry: 'Joint' object has no attribute 'geometry'
[00:07:07]   [REGULAR in base_link] rplidar_s2_joint
[00:07:07]     parent(occ2): base_link path=base_link:1
[00:07:07]     child(occ1):  rplidar_s2_link path=base_link:1+rplidar_s2_link:1
[00:07:07]     geometryOrOriginOne: (9.9270, -6.2500, 5.0000) cm
[00:07:07]     geometryOrOriginTwo: (4.9270, -6.2500, 5.0000) cm
[00:07:07]     occ1.transform: (-43.3747, -65.7506, 4.6815) cm (ctx_depth=1)
[00:07:07]     occ1.global:    (-43.3747, -65.7506, 4.6815) cm
[00:07:07]     occ2.transform: (0.0000, 0.0000, 0.0000) cm (ctx_depth=0)
[00:07:07]     occ2.global:    (0.0000, 0.0000, 0.0000) cm
[00:07:07]  -> origin_global: (0.099270, -0.062500, 0.050000) m [via geometryOrOriginOne_world] [world]
[00:07:07]     motion: rigid, axis: (0.000, 0.000, 1.000)
[00:07:07]  regular joint in component 'base_link': proxied joint into assembly context 'base_link:1' for geometry origin
[00:07:07]   WARNING:   regular joint in component 'base_link': failed to read geometry: 'Joint' object has no attribute 'geometry'
[00:07:07]   [REGULAR in base_link] front_right_wheel_joint
[00:07:07]     parent(occ2): base_link path=base_link:1
[00:07:07]     child(occ1):  Tire_1 path=base_link:1+front_right_wheel_link:1+Tire (1):1
[00:07:07]     geometryOrOriginOne: (13.0000, -18.5000, 2.0000) cm
[00:07:07]     geometryOrOriginTwo: (13.0000, -18.5000, 2.0000) cm
[00:07:07]     occ1.transform: (1.9212, -6.3905, 0.8048) cm (ctx_depth=2)
[00:07:07]     occ1.global:    (14.2900, -18.3477, 3.8048) cm
[00:07:07]     occ2.transform: (0.0000, 0.0000, 0.0000) cm (ctx_depth=0)
[00:07:07]     occ2.global:    (0.0000, 0.0000, 0.0000) cm
[00:07:07]  -> origin_global: (0.130000, -0.185000, 0.020000) m [via geometryOrOriginOne_world] [world]
[00:07:07]     motion: revolute, axis: (0.000, -1.000, 0.000)
[00:07:07]  regular joint in component 'base_link': proxied joint into assembly context 'base_link:1' for geometry origin
[00:07:07]   WARNING:   regular joint in component 'base_link': failed to read geometry: 'Joint' object has no attribute 'geometry'
[00:07:07]   [REGULAR in base_link] rear_right_wheel_joint
[00:07:07]     parent(occ2): base_link path=base_link:1
[00:07:07]     child(occ1):  Tire_3 path=base_link:1+rear_right_wheel_link:1+Tire (3):1
[00:07:07]     geometryOrOriginOne: (-2.0000, -18.7000, 2.0000) cm
[00:07:07]     geometryOrOriginTwo: (-2.0000, -18.5000, 2.0000) cm
[00:07:07]     occ1.transform: (0.7100, -5.1463, 0.8185) cm (ctx_depth=2)
[00:07:07]     occ1.global:    (-0.7100, -18.3477, 3.8048) cm
[00:07:07]     occ2.transform: (0.0000, 0.0000, 0.0000) cm (ctx_depth=0)
[00:07:07]     occ2.global:    (0.0000, 0.0000, 0.0000) cm
[00:07:07]  -> origin_global: (-0.020000, -0.187000, 0.020000) m [via geometryOrOriginOne_world] [world]
[00:07:07]     motion: revolute, axis: (0.000, -1.000, 0.000)
[00:07:07]  regular joint in component 'base_link': proxied joint into assembly context 'base_link:1' for geometry origin
[00:07:07]   WARNING:   regular joint in component 'base_link': failed to read geometry: 'Joint' object has no attribute 'geometry'
[00:07:07]   [REGULAR in base_link] front_left_wheel_joint
[00:07:07]     parent(occ2): base_link path=base_link:1
[00:07:07]     child(occ1):  Tire path=base_link:1+front_left_wheel_link:1+Tire:1
[00:07:07]     geometryOrOriginOne: (13.0000, 6.0000, 2.0000) cm
[00:07:07]     geometryOrOriginTwo: (13.0000, 6.0000, 2.0000) cm
[00:07:07]     occ1.transform: (1.1931, -5.8403, 0.6616) cm (ctx_depth=2)
[00:07:07]     occ1.global:    (11.7100, 5.8477, 3.8048) cm
[00:07:07]     occ2.transform: (0.0000, 0.0000, 0.0000) cm (ctx_depth=0)
[00:07:07]     occ2.global:    (0.0000, 0.0000, 0.0000) cm
[00:07:07]  -> origin_global: (0.130000, 0.060000, 0.020000) m [via geometryOrOriginOne_world] [world]
[00:07:07]     motion: revolute, axis: (0.000, 1.000, 0.000)
[00:07:07]  regular joint in component 'base_link': proxied joint into assembly context 'base_link:1' for geometry origin
[00:07:07]   WARNING:   regular joint in component 'base_link': failed to read geometry: 'Joint' object has no attribute 'geometry'
[00:07:07]   [REGULAR in base_link] rear_left_wheel_joint
[00:07:07]     parent(occ2): base_link path=base_link:1
[00:07:07]     child(occ1):  Tire_2 path=base_link:1+rear_left_wheel_link:1+Tire (2):1
[00:07:07]     geometryOrOriginOne: (-2.0000, 6.0000, 2.0000) cm
[00:07:07]     geometryOrOriginTwo: (-2.0000, 6.0000, 2.0000) cm
[00:07:07]     occ1.transform: (-3.2900, -5.9296, 0.4158) cm (ctx_depth=2)
[00:07:07]     occ1.global:    (-3.2900, 5.8477, 3.8048) cm
[00:07:07]     occ2.transform: (0.0000, 0.0000, 0.0000) cm (ctx_depth=0)
[00:07:07]     occ2.global:    (0.0000, 0.0000, 0.0000) cm
[00:07:07]  -> origin_global: (-0.020000, 0.060000, 0.020000) m [via geometryOrOriginOne_world] [world]
[00:07:07]     motion: revolute, axis: (0.000, 1.000, 0.000)
[00:07:07]   Extracted 6 unique joints
[00:07:07] 
=== EXTRACTION: RIGID GROUPS ===
[00:07:07]   No rigid groups found
[00:07:07] 
=== EXTRACTION SUMMARY ===
[00:07:07]   Occurrences: 15 (5 subassemblies, 10 leaf components)
[00:07:07]   Joints: 6 (0 as-built, 6 regular)
[00:07:07]   Max nesting depth: 2
[00:07:30] 
=== PHASE 1: DEBUG DATA ===
[00:07:30]   extraction_report.md
[00:07:30]   snapshot.json
[00:07:30]   fusion_transforms.json
[00:07:30] 
=== PHASE 2: BUILD ROBOT MODEL ===
[00:07:30] 
=== MODEL: ASSEMBLY HIERARCHY ===
[00:07:30]   Assembly: front_left_wheel_link d=1 offset=(105.2, 116.9, 31.4) mm
[00:07:30]   Assembly: front_right_wheel_link d=1 offset=(162.1, -247.4, 30.0) mm
[00:07:30]   Assembly: rear_left_wheel_link d=1 offset=(0.0, 117.8, 33.9) mm
[00:07:30]   Assembly: rear_right_wheel_link d=1 offset=(0.0, -234.9, 29.9) mm
[00:07:30]   Assembly: base_link d=0 offset=(0.0, 0.0, 0.0) mm
[00:07:30]   zed2_camera_link → base_link
[00:07:30]   rplidar_s2_link → base_link
[00:07:30]   Rim → front_left_wheel_link
[00:07:30]   Tire → front_left_wheel_link
[00:07:30]   Rim_1 → front_right_wheel_link
[00:07:30]   Tire_1 → front_right_wheel_link
[00:07:30]   Rim_2 → rear_left_wheel_link
[00:07:30]   Tire_2 → rear_left_wheel_link
[00:07:30]   Rim_3 → rear_right_wheel_link
[00:07:30]   Tire_3 → rear_right_wheel_link
[00:07:30]   Assembly: ma_robot (synthetic root, wraps design-root leaves so phase 2 has a macro to xacro:include)
[00:07:30]   base_link → ma_robot
[00:07:30] 
=== MODEL: RIGID GROUP MERGE ===
[00:07:30]   No explicit rigid groups to merge
[00:07:30]   front_left_wheel_link: anchor=Tire merged_name=front_left_wheel_link members=2 mass=611.60 g bbox=(90.0 × 95.3 × 89.9) mm
[00:07:30]   front_left_wheel_link: dropped front_left_wheel_link/Rim (base_link:1+front_left_wheel_link:1+Rim:1) -> front_left_wheel_link/Tire
[00:07:30]   AUTO rigid island: front_left_wheel_link (2 members) -> front_left_wheel_link
[00:07:30]   front_right_wheel_link: anchor=Tire_1 merged_name=front_right_wheel_link members=2 mass=611.60 g bbox=(90.0 × 100.8 × 89.9) mm
[00:07:30]   front_right_wheel_link: dropped front_right_wheel_link/Rim_1 (base_link:1+front_right_wheel_link:1+Rim (1):1) -> front_right_wheel_link/Tire_1
[00:07:30]   AUTO rigid island: front_right_wheel_link (2 members) -> front_right_wheel_link
[00:07:30]   rear_left_wheel_link: anchor=Tire_2 merged_name=rear_left_wheel_link members=2 mass=611.60 g bbox=(90.0 × 96.2 × 89.9) mm
[00:07:30]   rear_left_wheel_link: dropped rear_left_wheel_link/Rim_2 (base_link:1+rear_left_wheel_link:1+Rim (2):1) -> rear_left_wheel_link/Tire_2
[00:07:30]   AUTO rigid island: rear_left_wheel_link (2 members) -> rear_left_wheel_link
[00:07:30]   rear_right_wheel_link: anchor=Tire_3 merged_name=rear_right_wheel_link members=2 mass=611.60 g bbox=(90.0 × 88.4 × 89.9) mm
[00:07:30]   rear_right_wheel_link: dropped rear_right_wheel_link/Rim_3 (base_link:1+rear_right_wheel_link:1+Rim (3):1) -> rear_right_wheel_link/Tire_3
[00:07:30]   AUTO rigid island: rear_right_wheel_link (2 members) -> rear_right_wheel_link
[00:07:30] 
=== MODEL: RESOLVE JOINT PATHS ===
[00:07:30]   zed2_camera_joint    ma_robot/base_link → base_link/zed2_camera_link  [rigid] MOUNT
[00:07:30]   rplidar_s2_joint     ma_robot/base_link → base_link/rplidar_s2_link  [rigid] MOUNT
[00:07:30]   front_right_wheel_joint ma_robot/base_link → front_right_wheel_link/Tire_1  [revolute] MOUNT
[00:07:30]   rear_right_wheel_joint ma_robot/base_link → rear_right_wheel_link/Tire_3  [revolute] MOUNT
[00:07:30]   front_left_wheel_joint ma_robot/base_link → front_left_wheel_link/Tire  [revolute] MOUNT
[00:07:30]   rear_left_wheel_joint ma_robot/base_link → rear_left_wheel_link/Tire_2  [revolute] MOUNT
[00:07:30] 
=== MODEL: DETECT ROOT ===
[00:07:30]   Parent-only nodes: 1
[00:07:30]     ma_robot/base_link
[00:07:30]   → Root: ma_robot/base_link
[00:07:30] 
=== MODEL: RESOLVE NAMES ===
[00:07:30]   base_link (ma_robot) → base_link
[00:07:30]   front_left_wheel_link (front_left_wheel_link) → front_left_wheel_link
[00:07:30]   front_right_wheel_link (front_right_wheel_link) → front_right_wheel_link
[00:07:30]   rear_left_wheel_link (rear_left_wheel_link) → rear_left_wheel_link
[00:07:30]   rear_right_wheel_link (rear_right_wheel_link) → rear_right_wheel_link
[00:07:30]   rplidar_s2_link (base_link) → rplidar_s2_link
[00:07:30]   zed2_camera_link (base_link) → zed2_camera_link
[00:07:30]   Root link URDF name: base_link
[00:07:30] 
=== MODEL: BUILD LINKS ===
[00:07:30]   front_left_wheel_link: MERGED (2 members) mass=611.60 g
[00:07:30]   front_right_wheel_link: MERGED (2 members) mass=611.60 g
[00:07:30]   rear_left_wheel_link: MERGED (2 members) mass=611.60 g
[00:07:30]   rear_right_wheel_link: MERGED (2 members) mass=611.60 g
[00:07:30]   Built 7 links
[00:07:30] 
=== MODEL: BUILD JOINTS ===
[00:07:30]   NOTE: joint origin rpy derived from child occurrence's transform2 rotation (was hardcoded 0,0,0 pre-2026-04-13)
[00:07:30]   zed2_camera_joint: joint origin rpy = (0.000000, -0.000000, -1.570796) rad (+0.00°, -0.00°, -90.00°) [from child transform2 rotation]
[00:07:30]   zed2_camera_joint: base_link → zed2_camera_link [fixed]
[00:07:30]     origin_xyz: (0.145000, -0.062500, -0.007371) m [child_minus_parent]
[00:07:30]     origin_global: (0.145000, -0.062500, 0.035000) m
[00:07:30]   rplidar_s2_joint: joint origin rpy = (0.000000, -0.000000, -1.570796) rad (+0.00°, -0.00°, -90.00°) [from child transform2 rotation]
[00:07:30]   rplidar_s2_joint: base_link → rplidar_s2_link [fixed]
[00:07:30]     origin_xyz: (-0.433747, -0.657506, 0.046815) m [child_minus_parent]
[00:07:30]     origin_global: (0.099270, -0.062500, 0.050000) m
[00:07:30]   front_right_wheel_joint: mesh bake offset = (-12.90, -1.52, 18.05) mm [child-local frame]
[00:07:30]   front_right_wheel_joint: joint origin rpy = (-0.000000, -0.000000, 3.141593) rad (-0.00°, -0.00°, +180.00°) [from child transform2 rotation]
[00:07:30]  front_right_wheel_joint: axis remapped world -> joint/child frame: (0.000, -1.000, 0.000) -> (-0.000, 1.000, 0.000)
[00:07:30]   front_right_wheel_joint: base_link → front_right_wheel_link [continuous]
[00:07:30]     origin_xyz: (0.130000, -0.185000, 0.020000) m [joint_minus_parent]
[00:07:30]     origin_global: (0.130000, -0.185000, 0.020000) m
[00:07:30]   rear_right_wheel_joint: mesh bake offset = (-12.90, -3.52, 18.05) mm [child-local frame]
[00:07:30]   rear_right_wheel_joint: joint origin rpy = (-0.000000, -0.000000, 3.141593) rad (-0.00°, -0.00°, +180.00°) [from child transform2 rotation]
[00:07:30]  rear_right_wheel_joint: axis remapped world -> joint/child frame: (0.000, -1.000, 0.000) -> (-0.000, 1.000, 0.000)
[00:07:30]   rear_right_wheel_joint: base_link → rear_right_wheel_link [continuous]
[00:07:30]     origin_xyz: (-0.020000, -0.187000, 0.020000) m [joint_minus_parent]
[00:07:30]     origin_global: (-0.020000, -0.187000, 0.020000) m
[00:07:30]   front_left_wheel_joint: mesh bake offset = (-12.90, -1.52, 18.05) mm [child-local frame]
[00:07:30]   front_left_wheel_joint: base_link → front_left_wheel_link [continuous]
[00:07:30]     origin_xyz: (0.130000, 0.060000, 0.020000) m [joint_minus_parent]
[00:07:30]     origin_global: (0.130000, 0.060000, 0.020000) m
[00:07:30]   rear_left_wheel_joint: mesh bake offset = (-12.90, -1.52, 18.05) mm [child-local frame]
[00:07:30]   rear_left_wheel_joint: base_link → rear_left_wheel_link [continuous]
[00:07:30]     origin_xyz: (-0.020000, 0.060000, 0.020000) m [joint_minus_parent]
[00:07:30]     origin_global: (-0.020000, 0.060000, 0.020000) m
[00:07:30]   Built 6 joints
[00:07:30] 
=== MODEL: VALIDATE ===
[00:07:30]   Validation passed (0 warnings)
[00:07:30] 
[00:07:30] Kinematic tree:
[00:07:30]   base_link (2899g)
[00:07:30]     ─── zed2_camera_joint [fixed]
[00:07:30]       zed2_camera_link (178g)
[00:07:30]     ─── rplidar_s2_joint [fixed]
[00:07:30]       rplidar_s2_link (204g)
[00:07:30]     ─⟳─ front_right_wheel_joint [continuous]
[00:07:30]       front_right_wheel_link (612g) [MERGED]
[00:07:30]     ─⟳─ rear_right_wheel_joint [continuous]
[00:07:30]       rear_right_wheel_link (612g) [MERGED]
[00:07:30]     ─⟳─ front_left_wheel_joint [continuous]
[00:07:30]       front_left_wheel_link (612g) [MERGED]
[00:07:30]     ─⟳─ rear_left_wheel_joint [continuous]
[00:07:30]       rear_left_wheel_link (612g) [MERGED]
[00:07:30] 
=== MODEL SUMMARY ===
[00:07:30]   Robot: ma_robot
[00:07:30]   Root link: base_link
[00:07:30]   Links: 7
[00:07:30]   Joints: 6
[00:07:30]   Assemblies: 6
[00:07:30]   Warnings: 0
[00:07:30]   Errors: 0
[00:07:35] 
=== MESH EXPORT ===
[00:07:35]   zed2_camera_link:
[00:07:35]     OBJ exported (376945 bytes)
[00:07:35]     MTL preserved from Fusion (multi-material)
[00:07:35]     DAE written → meshes/base_link/zed2_camera_link.dae (OBJ retained for collision fit)
[00:07:35]   rplidar_s2_link:
[00:07:38]     OBJ exported (16393466 bytes)
[00:07:38]     MTL preserved from Fusion (multi-material)
[00:07:39]     DAE written → meshes/base_link/rplidar_s2_link.dae (OBJ retained for collision fit)
[00:07:39]   front_left_wheel_link:
[00:07:39]     Merge target: sub-asm 'front_left_wheel_link' (members=2)
[00:07:40]     MTL preserved from Fusion (multi-material)
[00:07:40]     Applying anchor frame correction (anchor not at identity within base_link:1+front_left_wheel_link:1)
[00:07:40]     Merged OBJ written via Fusion API (3796.9 KB)
[00:07:40]     DAE written → meshes/front_left_wheel_link/front_left_wheel_link.dae (OBJ retained for collision fit)
[00:07:40]   front_right_wheel_link:
[00:07:40]     Merge target: sub-asm 'front_right_wheel_link' (members=2)
[00:07:41]     MTL preserved from Fusion (multi-material)
[00:07:41]     Applying anchor frame correction (anchor not at identity within base_link:1+front_right_wheel_link:1)
[00:07:41]     Merged OBJ written via Fusion API (3814.2 KB)
[00:07:41]     DAE written → meshes/front_right_wheel_link/front_right_wheel_link.dae (OBJ retained for collision fit)
[00:07:41]   rear_left_wheel_link:
[00:07:41]     Merge target: sub-asm 'rear_left_wheel_link' (members=2)
[00:07:42]     MTL preserved from Fusion (multi-material)
[00:07:42]     Applying anchor frame correction (anchor not at identity within base_link:1+rear_left_wheel_link:1)
[00:07:42]     Merged OBJ written via Fusion API (3790.9 KB)
[00:07:42]     DAE written → meshes/rear_left_wheel_link/rear_left_wheel_link.dae (OBJ retained for collision fit)
[00:07:42]   rear_right_wheel_link:
[00:07:42]     Merge target: sub-asm 'rear_right_wheel_link' (members=2)
[00:07:43]     MTL preserved from Fusion (multi-material)
[00:07:43]     Applying anchor frame correction (anchor not at identity within base_link:1+rear_right_wheel_link:1)
[00:07:43]     Merged OBJ written via Fusion API (3823.1 KB)
[00:07:43]     DAE written → meshes/rear_right_wheel_link/rear_right_wheel_link.dae (OBJ retained for collision fit)
[00:07:43]   base_link:
[00:07:47]     OBJ exported (23615633 bytes)
[00:07:48]     MTL preserved from Fusion (multi-material)
[00:07:49]     DAE written → meshes/ma_robot/base_link.dae (OBJ retained for collision fit)
[00:07:49] 
  Mesh export summary:
[00:07:49]     Visual (OBJ+MTL):              7
[00:07:49]     Collision sub-component (STL):  0
[00:07:49]     Collision body + warning (STL): 0
[00:07:49]     Skipped (no Fusion ref):        0
[00:07:49] 
=== PHASE 3: SCREENSHOT ===
[00:07:50]   → images/robot.png
[00:07:50] 
=== PACKAGE: GENERATE ===
[00:07:50]   Package: ma_robot_description
[00:07:50]   Output:  C:/Users/mamre/OneDrive/Desktop/New folder/ETGAH-Robotics-Masterclass\ma_robot_description
[00:07:50] 
=== COLLISION: RESOLVE ===
[00:07:50]   zed2_camera_link: primitive (box [174.7 x 31.6 x 29.7] mm)
[00:07:50]   rplidar_s2_link: primitive (box [22.0 x 7.9 x 3.7] mm)
[00:07:50]   front_left_wheel_link: primitive (box [81.5 x 73.3 x 42.3] mm)
[00:07:50]   front_right_wheel_link: primitive (box [81.5 x 73.3 x 42.3] mm)
[00:07:50]   rear_left_wheel_link: primitive (box [81.5 x 73.3 x 42.3] mm)
[00:07:50]   rear_right_wheel_link: primitive (box [81.5 x 73.3 x 42.3] mm)
[00:07:50]   base_link: primitive (box [168.1 x 106.8 x 42.0] mm)
[00:07:50] 
  Collision summary:
[00:07:50]     Explicit:        0
[00:07:50]     Primitive (STL): 7
[00:07:50]     Convex hull STL: 0
[00:07:50]     Visual reuse:    0
[00:07:50]     Visual fallback: 0
[00:07:50] 
=== COLLISION: GENERATE STL ===
[00:07:50]   zed2_camera_link: box -> 12 tris (0.7 KB)
[00:07:50]   rplidar_s2_link: box -> 12 tris (0.7 KB)
[00:07:50]   front_left_wheel_link: box -> 12 tris (0.7 KB)
[00:07:50]   front_right_wheel_link: box -> 12 tris (0.7 KB)
[00:07:50]   rear_left_wheel_link: box -> 12 tris (0.7 KB)
[00:07:50]   rear_right_wheel_link: box -> 12 tris (0.7 KB)
[00:07:50]   base_link: box -> 12 tris (0.7 KB)
[00:07:50] 
  Generated 7 collision STL files
[00:07:50] 
=== PACKAGE: FRAMES ===
[00:07:50]   -> debug/frame_model.json (pre-frame cache)
[00:07:50]   Frame convention: ros
[00:07:50]   Frame overrides:  config/frame_overrides.csv
[00:07:50]   Rebased links:    4/7
[00:07:50] 
=== PACKAGE: XACRO ===
[00:07:50]   → urdf/assemblies/base_link.urdf.xacro
[00:07:50]   → urdf/assemblies/front_left_wheel_link.urdf.xacro
[00:07:50]   → urdf/assemblies/front_right_wheel_link.urdf.xacro
[00:07:50]   → urdf/assemblies/ma_robot.urdf.xacro
[00:07:50]   → urdf/assemblies/rear_left_wheel_link.urdf.xacro
[00:07:50]   → urdf/assemblies/rear_right_wheel_link.urdf.xacro
[00:07:50]   → urdf/ma_robot.urdf.xacro
[00:07:50] 
=== PACKAGE: URDF (flat, for validation) ===
[00:07:50]   → urdf/ma_robot.urdf
[00:07:50] 
=== PACKAGE: ROS2 FILES ===
[00:07:50]   → package.xml
[00:07:50]   → CMakeLists.txt
[00:07:50]   → launch/display.launch.py
[00:07:50]   → rviz/display.rviz
[00:07:50]   → config/joint_state.yaml
[00:07:50]   → config/ros2_controllers.yaml
[00:07:50] 
=== PACKAGE: SUPPLEMENTARY DATA ===
[00:07:50]   → robot_data.yaml
[00:07:50]   -> docs/transforms.md
[00:07:50] 
=== PACKAGE: README ===
[00:07:50]   → README.md
[00:07:50]   Cleaned up 14 retained OBJ/MTL files
[00:07:50] 
=== PACKAGE: COMPLETE ===
[00:07:50]   Package generated: C:/Users/mamre/OneDrive/Desktop/New folder/ETGAH-Robotics-Masterclass\ma_robot_description
[00:07:50]   Xacro: urdf/ma_robot.urdf.xacro (+ 6 assembly macros)
[00:07:50]   URDF:  urdf/ma_robot.urdf (flat, for validation)
[00:07:50]   Launch: ros2 launch ma_robot_description display.launch.py
[00:07:50] 
=== EXPORT COMPLETE ===
```

# Export Log: ma_robot

**Generated:** 2026-09-03T01:27:27.715500

```
[01:26:45] fusion2URDF v3.1.0
[01:26:45] Time: 2026-09-03T01:26:45.501326
[01:26:45] Design: ma_robot
[01:26:45] Components: 16
[01:26:45] 
=== PHASE 1: EXTRACTION ===
[01:26:45]   Document unit: mm
[01:26:45] 
=== EXTRACTION: OCCURRENCES ===
[01:26:45]   [LEAF] d=0 base_link
[01:26:45]     path: base_link:1
[01:26:45]     global_pos: (0.000000, 0.000000, 0.025000) m
[01:26:45]     mass: 2.899172 kg, bodies: 2
[01:26:45]     com_global: (0.041574, -0.062494, 0.049420) m
[01:26:45]     com_component_local: (0.041574, -0.062494, 0.024420) m
[01:26:45]     inertia@origin: ixx=2.102569e-02 iyy=2.053476e-02 izz=3.686159e-02 kg·m²
[01:26:45]     inertia@com:    ixx=7.973854e-03 iyy=1.379501e-02 izz=2.052789e-02 kg·m²
[01:26:45]     material: Acetal_Resin_Black
[01:26:45]     color: RGB(0.10, 0.10, 0.10) [Plastic_Glossy_Black]
[01:26:45]     bbox: (0.2630 x 0.2450 x 0.1200) m
[01:26:45]   [LEAF] d=0 zed2_camera_link
[01:26:45]     path: zed2_camera_link:1
[01:26:45]     global_pos: (0.145000, -0.062500, 0.017629) m
[01:26:45]     mass: 0.178229 kg, bodies: 1
[01:26:45]     com_global: (0.145000, -0.046995, 0.060018) m
[01:26:45]     com_component_local: (0.000000, 0.015505, 0.042389) m
[01:26:45]     inertia@origin: ixx=3.897245e-04 iyy=7.565457e-04 izz=4.819299e-04 kg·m²
[01:26:45]     inertia@com:    ixx=2.662726e-05 iyy=4.362977e-04 izz=4.390806e-04 kg·m²
[01:26:45]     material: PA_11_Nylon_HP_11_30_with_EOS_P_396_3D_Printer
[01:26:45]     color: RGB(0.25, 0.25, 0.25) [Nylon_12_with_Formlabs_Fuse_1_3D_Printer]
[01:26:45]     bbox: (0.1747 x 0.0316 x 0.0297) m
[01:26:45]   [LEAF] d=1 Rim
[01:26:45]     path: rear_left_wheel_link:1+Rim:1
[01:26:45]     global_pos: (-0.000725, 0.006437, 0.012079) m
[01:26:45]   [LEAF] d=1 Tire
[01:26:45]     path: rear_left_wheel_link:1+Tire:1
[01:26:45]     global_pos: (-0.032900, 0.062477, 0.063048) m
[01:26:45]     mass: 0.611603 kg, bodies: 1
[01:26:45]     com_global: (-0.020000, 0.056994, 0.045000) m
[01:26:45]     com_component_local: (0.012900, -0.005483, -0.018048) m
[01:26:45]     inertia@origin: ixx=7.441770e-04 iyy=1.033528e-03 izz=6.467384e-04 kg·m²
[01:26:45]     inertia@com:    ixx=5.265770e-04 iyy=7.325315e-04 izz=5.265750e-04 kg·m²
[01:26:45]     material: Steel
[01:26:45]     color: RGB(0.63, 0.63, 0.63) [Opaque_160_160_160]
[01:26:45]     bbox: (0.0900 x 0.0500 x 0.0899) m
[01:26:45]   [SUBASM] d=0 rear_left_wheel_link
[01:26:45]     path: rear_left_wheel_link:1
[01:26:45]     global_pos: (0.000000, 0.000000, 0.000000) m
[01:26:45]   [LEAF] d=1 Rim_1
[01:26:45]     path: front_left_wheel_link:1+Rim (1):1
[01:26:45]     global_pos: (0.119275, 0.149755, 0.064526) m
[01:26:45]   [LEAF] d=1 Tire_1
[01:26:45]     path: front_left_wheel_link:1+Tire (1):1
[01:26:45]     global_pos: (0.142900, 0.061477, 0.026952) m
[01:26:45]     mass: 0.611603 kg, bodies: 1
[01:26:45]     com_global: (0.155800, 0.055994, 0.008904) m
[01:26:45]     com_component_local: (0.012900, -0.005483, -0.018048) m
[01:26:45]     inertia@origin: ixx=7.441770e-04 iyy=1.033528e-03 izz=6.467384e-04 kg·m²
[01:26:45]     inertia@com:    ixx=5.265770e-04 iyy=7.325315e-04 izz=5.265750e-04 kg·m²
[01:26:45]     material: Steel
[01:26:45]     color: RGB(0.63, 0.63, 0.63) [Opaque_160_160_160]
[01:26:45]     bbox: (0.0900 x 0.0500 x 0.0899) m
[01:26:45]   [SUBASM] d=0 front_left_wheel_link
[01:26:45]     path: front_left_wheel_link:1
[01:26:45]     global_pos: (0.120000, 0.143318, 0.052447) m
[01:26:45]   [LEAF] d=1 Rim_2
[01:26:45]     path: front_right_wheel_link:1+Rim (2):1
[01:26:45]     global_pos: (0.093828, -0.251353, 0.012079) m
[01:26:45]   [LEAF] d=1 Tire_2
[01:26:45]     path: front_right_wheel_link:1+Tire (2):1
[01:26:45]     global_pos: (0.142900, -0.187477, 0.063048) m
[01:26:45]     mass: 0.611603 kg, bodies: 1
[01:26:45]     com_global: (0.155800, -0.192959, 0.045000) m
[01:26:45]     com_component_local: (0.012900, -0.005483, -0.018048) m
[01:26:45]     inertia@origin: ixx=7.441770e-04 iyy=1.033528e-03 izz=6.467384e-04 kg·m²
[01:26:45]     inertia@com:    ixx=5.265770e-04 iyy=7.325315e-04 izz=5.265750e-04 kg·m²
[01:26:45]     material: Steel
[01:26:45]     color: RGB(0.63, 0.63, 0.63) [Opaque_160_160_160]
[01:26:45]     bbox: (0.0900 x 0.0500 x 0.0899) m
[01:26:45]   [SUBASM] d=0 front_right_wheel_link
[01:26:45]     path: front_right_wheel_link:1
[01:26:45]     global_pos: (0.093104, -0.244917, 0.000000) m
[01:26:45]   [LEAF] d=1 Rim_3
[01:26:45]     path: rear_right_wheel_link:1+Rim (3):1
[01:26:45]     global_pos: (-0.016003, -0.240856, 0.012079) m
[01:26:45]   [LEAF] d=1 Tire_3
[01:26:45]     path: rear_right_wheel_link:1+Tire (3):1
[01:26:45]     global_pos: (-0.032900, -0.185477, 0.026952) m
[01:26:45]     mass: 0.611603 kg, bodies: 1
[01:26:45]     com_global: (-0.020000, -0.190959, 0.008904) m
[01:26:45]     com_component_local: (0.012900, -0.005483, -0.018048) m
[01:26:45]     inertia@origin: ixx=7.441770e-04 iyy=1.033528e-03 izz=6.467384e-04 kg·m²
[01:26:45]     inertia@com:    ixx=5.265770e-04 iyy=7.325315e-04 izz=5.265750e-04 kg·m²
[01:26:45]     material: Steel
[01:26:45]     color: RGB(0.63, 0.63, 0.63) [Opaque_160_160_160]
[01:26:45]     bbox: (0.0900 x 0.0500 x 0.0899) m
[01:26:45]   [SUBASM] d=0 rear_right_wheel_link
[01:26:45]     path: rear_right_wheel_link:1
[01:26:45]     global_pos: (-0.015278, -0.247293, 0.000000) m
[01:26:45]   [LEAF] d=0 rplidar_s2_link
[01:26:45]     path: rplidar_s2_link:1
[01:26:45]     global_pos: (-0.433747, -0.657506, 0.071815) m
[01:26:45]     mass: 0.203764 kg, bodies: 28
[01:26:45]     com_global: (-1.028760, -0.124565, 0.084695) m
[01:26:45]     com_component_local: (-0.595013, 0.532942, 0.012880) m
[01:26:45]     inertia@origin: ixx=5.804326e-02 iyy=7.231055e-02 izz=1.302519e-01 kg·m²
[01:26:45]     inertia@com:    ixx=1.351079e-04 iyy=1.362177e-04 izz=2.370283e-04 kg·m²
[01:26:45]     material: Steel
[01:26:45]     color: RGB(1.00, 1.00, 1.00) [Copper_Raw]
[01:26:45]     bbox: (0.0770 x 0.0770 x 0.0389) m
[01:26:45]   Extracted 15 occurrences
[01:26:45] 
=== EXTRACTION: JOINTS ===
[01:26:45]   WARNING:   regular joint in component 'ma_robot': failed to read geometry: 'Joint' object has no attribute 'geometry'
[01:26:45]   [REGULAR in ma_robot] zed2_camera_joint
[01:26:45]     parent(occ2): base_link path=base_link:1
[01:26:45]     child(occ1):  zed2_camera_link path=zed2_camera_link:1
[01:26:45]     geometryOrOriginOne: (14.5000, -6.2500, 6.0000) cm
[01:26:45]     geometryOrOriginTwo: (14.5000, -6.2500, 6.0000) cm
[01:26:45]     occ1.transform: (14.5000, -6.2500, 1.7629) cm (ctx_depth=0)
[01:26:45]     occ1.global:    (14.5000, -6.2500, 1.7629) cm
[01:26:45]     occ2.transform: (0.0000, 0.0000, 2.5000) cm (ctx_depth=0)
[01:26:45]     occ2.global:    (0.0000, 0.0000, 2.5000) cm
[01:26:45]  -> origin_global: (0.145000, -0.062500, 0.060000) m [via geometryOrOriginOne]
[01:26:45]     motion: rigid, axis: (0.000, 0.000, 1.000)
[01:26:45]   WARNING:   regular joint in component 'ma_robot': failed to read geometry: 'Joint' object has no attribute 'geometry'
[01:26:45]   [REGULAR in ma_robot] rear_left_wheel_joint
[01:26:45]     parent(occ2): base_link path=base_link:1
[01:26:45]     child(occ1):  Tire path=rear_left_wheel_link:1+Tire:1
[01:26:45]     geometryOrOriginOne: (-2.0000, 7.0000, 4.5000) cm
[01:26:45]     geometryOrOriginTwo: (-2.0000, 6.0000, 4.5000) cm
[01:26:45]     occ1.transform: (-3.2900, 6.2477, 6.3048) cm (ctx_depth=1)
[01:26:45]     occ1.global:    (-3.2900, 6.2477, 6.3048) cm
[01:26:45]     occ2.transform: (0.0000, 0.0000, 2.5000) cm (ctx_depth=0)
[01:26:45]     occ2.global:    (0.0000, 0.0000, 2.5000) cm
[01:26:45]  -> origin_global: (-0.020000, 0.070000, 0.045000) m [via geometryOrOriginOne]
[01:26:45]     motion: revolute, axis: (0.000, 1.000, 0.000)
[01:26:45]   WARNING:   regular joint in component 'ma_robot': failed to read geometry: 'Joint' object has no attribute 'geometry'
[01:26:45]   [REGULAR in ma_robot] front_right_wheel_joint
[01:26:45]     parent(occ2): base_link path=base_link:1
[01:26:45]     child(occ1):  Tire_2 path=front_right_wheel_link:1+Tire (2):1
[01:26:45]     geometryOrOriginOne: (13.0000, -18.9000, 4.5000) cm
[01:26:45]     geometryOrOriginTwo: (13.0000, -18.5000, 4.5000) cm
[01:26:45]     occ1.transform: (-4.9797, -5.7440, 6.3048) cm (ctx_depth=1)
[01:26:45]     occ1.global:    (14.2900, -18.7477, 6.3048) cm
[01:26:45]     occ2.transform: (0.0000, 0.0000, 2.5000) cm (ctx_depth=0)
[01:26:45]     occ2.global:    (0.0000, 0.0000, 2.5000) cm
[01:26:45]  -> origin_global: (0.130000, -0.189000, 0.045000) m [via geometryOrOriginOne]
[01:26:45]     motion: revolute, axis: (-0.000, -1.000, 0.000)
[01:26:45]   WARNING:   regular joint in component 'ma_robot': failed to read geometry: 'Joint' object has no attribute 'geometry'
[01:26:45]   [REGULAR in ma_robot] rear_right_wheel_joint
[01:26:45]     parent(occ2): base_link path=base_link:1
[01:26:45]     child(occ1):  Tire_3 path=rear_right_wheel_link:1+Tire (3):1
[01:26:45]     geometryOrOriginOne: (-2.0000, -18.9000, 4.5000) cm
[01:26:45]     geometryOrOriginTwo: (-2.0000, -18.5000, 4.5000) cm
[01:26:45]     occ1.transform: (-1.7622, 6.1816, 2.6952) cm (ctx_depth=1)
[01:26:45]     occ1.global:    (-3.2900, -18.5477, 2.6952) cm
[01:26:45]     occ2.transform: (0.0000, 0.0000, 2.5000) cm (ctx_depth=0)
[01:26:45]     occ2.global:    (0.0000, 0.0000, 2.5000) cm
[01:26:45]  -> origin_global: (-0.020000, -0.189000, 0.045000) m [via geometryOrOriginOne]
[01:26:45]     motion: revolute, axis: (-0.000, -1.000, 0.000)
[01:26:45]   WARNING:   regular joint in component 'ma_robot': failed to read geometry: 'Joint' object has no attribute 'geometry'
[01:26:45]   [REGULAR in ma_robot] front_left_wheel_joint
[01:26:45]     parent(occ2): base_link path=base_link:1
[01:26:45]     child(occ1):  Tire_1 path=front_left_wheel_link:1+Tire (1):1
[01:26:45]     geometryOrOriginOne: (13.0000, 6.3000, 4.5000) cm
[01:26:45]     geometryOrOriginTwo: (13.0000, 6.0000, 4.5000) cm
[01:26:45]     occ1.transform: (2.2900, -8.1841, -2.5495) cm (ctx_depth=1)
[01:26:45]     occ1.global:    (14.2900, 6.1477, 2.6952) cm
[01:26:45]     occ2.transform: (0.0000, 0.0000, 2.5000) cm (ctx_depth=0)
[01:26:45]     occ2.global:    (0.0000, 0.0000, 2.5000) cm
[01:26:45]  -> origin_global: (0.130000, 0.063000, 0.045000) m [via geometryOrOriginOne]
[01:26:45]     motion: revolute, axis: (0.000, 1.000, 0.000)
[01:26:45]   WARNING:   regular joint in component 'ma_robot': failed to read geometry: 'Joint' object has no attribute 'geometry'
[01:26:45]   [REGULAR in ma_robot] rplidar_s2_joint
[01:26:45]     parent(occ2): base_link path=base_link:1
[01:26:45]     child(occ1):  rplidar_s2_link path=rplidar_s2_link:1
[01:26:45]     geometryOrOriginOne: (9.9270, -6.2500, 7.5000) cm
[01:26:45]     geometryOrOriginTwo: (4.9270, -6.2500, 7.5000) cm
[01:26:45]     occ1.transform: (-43.3747, -65.7506, 7.1815) cm (ctx_depth=0)
[01:26:45]     occ1.global:    (-43.3747, -65.7506, 7.1815) cm
[01:26:45]     occ2.transform: (0.0000, 0.0000, 2.5000) cm (ctx_depth=0)
[01:26:45]     occ2.global:    (0.0000, 0.0000, 2.5000) cm
[01:26:45]  -> origin_global: (0.099270, -0.062500, 0.075000) m [via geometryOrOriginOne]
[01:26:45]     motion: rigid, axis: (0.000, 0.000, 1.000)
[01:26:45]   Extracted 6 unique joints
[01:26:45] 
=== EXTRACTION: RIGID GROUPS ===
[01:26:45]   No rigid groups found
[01:26:45] 
=== EXTRACTION SUMMARY ===
[01:26:45]   Occurrences: 15 (4 subassemblies, 11 leaf components)
[01:26:45]   Joints: 6 (0 as-built, 6 regular)
[01:26:45]   Max nesting depth: 1
[01:27:15] 
=== PHASE 1: DEBUG DATA ===
[01:27:15]   extraction_report.md
[01:27:15]   snapshot.json
[01:27:15]   fusion_transforms.json
[01:27:15] 
=== PHASE 2: BUILD ROBOT MODEL ===
[01:27:15] 
=== MODEL: ASSEMBLY HIERARCHY ===
[01:27:15]   Assembly: rear_left_wheel_link d=0 offset=(0.0, 0.0, 0.0) mm
[01:27:15]   Assembly: front_left_wheel_link d=0 offset=(120.0, 143.3, 52.4) mm
[01:27:15]   Assembly: front_right_wheel_link d=0 offset=(93.1, -244.9, 0.0) mm
[01:27:15]   Assembly: rear_right_wheel_link d=0 offset=(-15.3, -247.3, 0.0) mm
[01:27:15]   Assembly: ma_robot (synthetic root, wraps design-root leaves so phase 2 has a macro to xacro:include)
[01:27:15]   base_link → ma_robot
[01:27:15]   zed2_camera_link → ma_robot
[01:27:15]   Rim → rear_left_wheel_link
[01:27:15]   Tire → rear_left_wheel_link
[01:27:15]   Rim_1 → front_left_wheel_link
[01:27:15]   Tire_1 → front_left_wheel_link
[01:27:15]   Rim_2 → front_right_wheel_link
[01:27:15]   Tire_2 → front_right_wheel_link
[01:27:15]   Rim_3 → rear_right_wheel_link
[01:27:15]   Tire_3 → rear_right_wheel_link
[01:27:15]   rplidar_s2_link → ma_robot
[01:27:15] 
=== MODEL: RIGID GROUP MERGE ===
[01:27:15]   No explicit rigid groups to merge
[01:27:15]   front_left_wheel_link: anchor=Tire_1 merged_name=front_left_wheel_link members=2 mass=611.60 g bbox=(90.0 × 118.8 × 89.9) mm
[01:27:15]   front_left_wheel_link: dropped front_left_wheel_link/Rim_1 (front_left_wheel_link:1+Rim (1):1) -> front_left_wheel_link/Tire_1
[01:27:15]   AUTO rigid island: front_left_wheel_link (2 members) -> front_left_wheel_link
[01:27:15]   front_right_wheel_link: anchor=Tire_2 merged_name=front_right_wheel_link members=2 mass=611.60 g bbox=(90.0 × 94.4 × 89.9) mm
[01:27:15]   front_right_wheel_link: dropped front_right_wheel_link/Rim_2 (front_right_wheel_link:1+Rim (2):1) -> front_right_wheel_link/Tire_2
[01:27:15]   AUTO rigid island: front_right_wheel_link (2 members) -> front_right_wheel_link
[01:27:15]   rear_left_wheel_link: anchor=Tire merged_name=rear_left_wheel_link members=2 mass=611.60 g bbox=(90.0 × 75.6 × 89.9) mm
[01:27:15]   rear_left_wheel_link: dropped rear_left_wheel_link/Rim (rear_left_wheel_link:1+Rim:1) -> rear_left_wheel_link/Tire
[01:27:15]   AUTO rigid island: rear_left_wheel_link (2 members) -> rear_left_wheel_link
[01:27:15]   rear_right_wheel_link: anchor=Tire_3 merged_name=rear_right_wheel_link members=2 mass=611.60 g bbox=(90.0 × 85.9 × 89.9) mm
[01:27:15]   rear_right_wheel_link: dropped rear_right_wheel_link/Rim_3 (rear_right_wheel_link:1+Rim (3):1) -> rear_right_wheel_link/Tire_3
[01:27:15]   AUTO rigid island: rear_right_wheel_link (2 members) -> rear_right_wheel_link
[01:27:15] 
=== MODEL: RESOLVE JOINT PATHS ===
[01:27:15]   zed2_camera_joint    ma_robot/base_link → ma_robot/zed2_camera_link  [rigid] internal
[01:27:15]   rear_left_wheel_joint ma_robot/base_link → rear_left_wheel_link/Tire  [revolute] MOUNT
[01:27:15]   front_right_wheel_joint ma_robot/base_link → front_right_wheel_link/Tire_2  [revolute] MOUNT
[01:27:15]   rear_right_wheel_joint ma_robot/base_link → rear_right_wheel_link/Tire_3  [revolute] MOUNT
[01:27:15]   front_left_wheel_joint ma_robot/base_link → front_left_wheel_link/Tire_1  [revolute] MOUNT
[01:27:15]   rplidar_s2_joint     ma_robot/base_link → ma_robot/rplidar_s2_link  [rigid] internal
[01:27:15] 
=== MODEL: DETECT ROOT ===
[01:27:15]   Parent-only nodes: 1
[01:27:15]     ma_robot/base_link
[01:27:15]   → Root: ma_robot/base_link
[01:27:15] 
=== MODEL: RESOLVE NAMES ===
[01:27:15]   base_link (ma_robot) → base_link
[01:27:15]   front_left_wheel_link (front_left_wheel_link) → front_left_wheel_link
[01:27:15]   front_right_wheel_link (front_right_wheel_link) → front_right_wheel_link
[01:27:15]   rear_left_wheel_link (rear_left_wheel_link) → rear_left_wheel_link
[01:27:15]   rear_right_wheel_link (rear_right_wheel_link) → rear_right_wheel_link
[01:27:15]   rplidar_s2_link (ma_robot) → rplidar_s2_link
[01:27:15]   zed2_camera_link (ma_robot) → zed2_camera_link
[01:27:15]   Root link URDF name: base_link
[01:27:15] 
=== MODEL: BUILD LINKS ===
[01:27:15]   rear_left_wheel_link: MERGED (2 members) mass=611.60 g
[01:27:15]   front_left_wheel_link: MERGED (2 members) mass=611.60 g
[01:27:15]   front_right_wheel_link: MERGED (2 members) mass=611.60 g
[01:27:15]   rear_right_wheel_link: MERGED (2 members) mass=611.60 g
[01:27:15]   Built 7 links
[01:27:15] 
=== MODEL: BUILD JOINTS ===
[01:27:15]   NOTE: joint origin rpy derived from child occurrence's transform2 rotation (was hardcoded 0,0,0 pre-2026-04-13)
[01:27:15]   zed2_camera_joint: joint origin rpy = (0.000000, -0.000000, -1.570796) rad (+0.00°, -0.00°, -90.00°) [from child transform2 rotation]
[01:27:15]   zed2_camera_joint: base_link → zed2_camera_link [fixed]
[01:27:15]     origin_xyz: (0.145000, -0.062500, -0.007371) m [child_minus_parent]
[01:27:15]     origin_global: (0.082500, -0.207500, 0.077629) m
[01:27:15]   rear_left_wheel_joint: mesh bake offset = (20.00, -70.00, -45.00) mm [child-local frame]
[01:27:15]   rear_left_wheel_joint: base_link → rear_left_wheel_link [continuous]
[01:27:15]     origin_xyz: (-0.052900, 0.132477, 0.083048) m [joint_minus_parent]
[01:27:15]     origin_global: (-0.052900, 0.132477, 0.108048) m
[01:27:15]   front_right_wheel_joint: mesh bake offset = (-130.00, 189.00, -45.00) mm [child-local frame]
[01:27:15]   front_right_wheel_joint: joint origin rpy = (-0.000000, -0.000000, -3.141593) rad (-0.00°, -0.00°, -180.00°) [from child transform2 rotation]
[01:27:15]  front_right_wheel_joint: axis remapped world -> joint/child frame: (-0.000, -1.000, 0.000) -> (0.000, 1.000, 0.000)
[01:27:15]   front_right_wheel_joint: base_link → front_right_wheel_link [continuous]
[01:27:15]     origin_xyz: (0.012900, 0.001523, 0.083048) m [joint_minus_parent]
[01:27:15]     origin_global: (0.012900, 0.001523, 0.108048) m
[01:27:15]   rear_right_wheel_joint: mesh bake offset = (20.00, 189.00, -45.00) mm [child-local frame]
[01:27:15]   rear_right_wheel_joint: joint origin rpy = (3.141593, -0.000000, -0.000000) rad (+180.00°, -0.00°, -0.00°) [from child transform2 rotation]
[01:27:15]  rear_right_wheel_joint: axis remapped world -> joint/child frame: (-0.000, -1.000, 0.000) -> (0.000, 1.000, 0.000)
[01:27:15]   rear_right_wheel_joint: base_link → rear_right_wheel_link [continuous]
[01:27:15]     origin_xyz: (-0.052900, 0.003523, -0.043048) m [joint_minus_parent]
[01:27:15]     origin_global: (-0.052900, 0.003523, -0.018048) m
[01:27:15]   front_left_wheel_joint: mesh bake offset = (-130.00, -63.00, -45.00) mm [child-local frame]
[01:27:15]   front_left_wheel_joint: joint origin rpy = (3.141593, 0.000000, 3.141593) rad (+180.00°, +0.00°, +180.00°) [from child transform2 rotation]
[01:27:15]   front_left_wheel_joint: base_link → front_left_wheel_link [continuous]
[01:27:15]     origin_xyz: (0.012900, 0.124477, -0.043048) m [joint_minus_parent]
[01:27:15]     origin_global: (0.012900, 0.124477, -0.018048) m
[01:27:15]   rplidar_s2_joint: joint origin rpy = (-0.000000, -0.000000, -1.570796) rad (-0.00°, -0.00°, -90.00°) [from child transform2 rotation]
[01:27:15]   rplidar_s2_joint: base_link → rplidar_s2_link [fixed]
[01:27:15]     origin_xyz: (-0.433747, -0.657506, 0.046815) m [child_minus_parent]
[01:27:15]     origin_global: (-0.496247, -0.756777, 0.146815) m
[01:27:15]   Built 6 joints
[01:27:15] 
=== MODEL: VALIDATE ===
[01:27:15]   Validation passed (0 warnings)
[01:27:15] 
[01:27:15] Kinematic tree:
[01:27:15]   base_link (2899g)
[01:27:15]     ─── zed2_camera_joint [fixed]
[01:27:15]       zed2_camera_link (178g)
[01:27:15]     ─⟳─ rear_left_wheel_joint [continuous]
[01:27:15]       rear_left_wheel_link (612g) [MERGED]
[01:27:15]     ─⟳─ front_right_wheel_joint [continuous]
[01:27:15]       front_right_wheel_link (612g) [MERGED]
[01:27:15]     ─⟳─ rear_right_wheel_joint [continuous]
[01:27:15]       rear_right_wheel_link (612g) [MERGED]
[01:27:15]     ─⟳─ front_left_wheel_joint [continuous]
[01:27:15]       front_left_wheel_link (612g) [MERGED]
[01:27:15]     ─── rplidar_s2_joint [fixed]
[01:27:15]       rplidar_s2_link (204g)
[01:27:15] 
=== MODEL SUMMARY ===
[01:27:15]   Robot: ma_robot
[01:27:15]   Root link: base_link
[01:27:15]   Links: 7
[01:27:15]   Joints: 6
[01:27:15]   Assemblies: 5
[01:27:15]   Warnings: 0
[01:27:15]   Errors: 0
[01:27:18] 
=== MESH EXPORT ===
[01:27:18]   base_link:
[01:27:18]     OBJ exported (241612 bytes)
[01:27:18]     MTL preserved from Fusion (multi-material)
[01:27:18]     DAE written → meshes/ma_robot/base_link.dae (OBJ retained for collision fit)
[01:27:18]   zed2_camera_link:
[01:27:18]     OBJ exported (376945 bytes)
[01:27:18]     MTL preserved from Fusion (multi-material)
[01:27:18]     DAE written → meshes/ma_robot/zed2_camera_link.dae (OBJ retained for collision fit)
[01:27:18]   rear_left_wheel_link:
[01:27:18]     Merge target: sub-asm 'rear_left_wheel_link' (members=2)
[01:27:19]     MTL preserved from Fusion (multi-material)
[01:27:19]     Applying anchor frame correction (anchor not at identity within rear_left_wheel_link:1)
[01:27:20]     Merged OBJ written via Fusion API (3794.7 KB)
[01:27:20]     DAE written → meshes/rear_left_wheel_link/rear_left_wheel_link.dae (OBJ retained for collision fit)
[01:27:20]   front_left_wheel_link:
[01:27:20]     Merge target: sub-asm 'front_left_wheel_link' (members=2)
[01:27:21]     MTL preserved from Fusion (multi-material)
[01:27:21]     Applying anchor frame correction (anchor not at identity within front_left_wheel_link:1)
[01:27:21]     Merged OBJ written via Fusion API (3832.6 KB)
[01:27:21]     DAE written → meshes/front_left_wheel_link/front_left_wheel_link.dae (OBJ retained for collision fit)
[01:27:21]   front_right_wheel_link:
[01:27:21]     Merge target: sub-asm 'front_right_wheel_link' (members=2)
[01:27:22]     MTL preserved from Fusion (multi-material)
[01:27:22]     Applying anchor frame correction (anchor not at identity within front_right_wheel_link:1)
[01:27:22]     Merged OBJ written via Fusion API (3831.9 KB)
[01:27:22]     DAE written → meshes/front_right_wheel_link/front_right_wheel_link.dae (OBJ retained for collision fit)
[01:27:22]   rear_right_wheel_link:
[01:27:22]     Merge target: sub-asm 'rear_right_wheel_link' (members=2)
[01:27:23]     MTL preserved from Fusion (multi-material)
[01:27:23]     Applying anchor frame correction (anchor not at identity within rear_right_wheel_link:1)
[01:27:23]     Merged OBJ written via Fusion API (3805.4 KB)
[01:27:23]     DAE written → meshes/rear_right_wheel_link/rear_right_wheel_link.dae (OBJ retained for collision fit)
[01:27:23]   rplidar_s2_link:
[01:27:25]     OBJ exported (16393466 bytes)
[01:27:25]     MTL preserved from Fusion (multi-material)
[01:27:26]     DAE written → meshes/ma_robot/rplidar_s2_link.dae (OBJ retained for collision fit)
[01:27:26] 
  Mesh export summary:
[01:27:26]     Visual (OBJ+MTL):              7
[01:27:26]     Collision sub-component (STL):  0
[01:27:26]     Collision body + warning (STL): 0
[01:27:26]     Skipped (no Fusion ref):        0
[01:27:26] 
=== PHASE 3: SCREENSHOT ===
[01:27:27]   → images/robot.png
[01:27:27] 
=== PACKAGE: GENERATE ===
[01:27:27]   Package: ma_robot_description
[01:27:27]   Output:  C:/Users/mamre/OneDrive/Desktop/New folder/ETGAH-Robotics-Masterclass\ma_robot_description
[01:27:27] 
=== COLLISION: RESOLVE ===
[01:27:27]   base_link: primitive (cylinder r=127.0 h=120.0 mm)
[01:27:27]   zed2_camera_link: primitive (box [174.7 x 31.6 x 29.7] mm)
[01:27:27]   rear_left_wheel_link: primitive (box [81.5 x 73.3 x 42.3] mm)
[01:27:27]   front_left_wheel_link: primitive (box [81.5 x 73.3 x 42.3] mm)
[01:27:27]   front_right_wheel_link: primitive (box [81.5 x 73.3 x 42.3] mm)
[01:27:27]   rear_right_wheel_link: primitive (box [81.5 x 73.3 x 42.3] mm)
[01:27:27]   rplidar_s2_link: primitive (box [22.0 x 7.9 x 3.7] mm)
[01:27:27] 
  Collision summary:
[01:27:27]     Explicit:        0
[01:27:27]     Primitive (STL): 7
[01:27:27]     Convex hull STL: 0
[01:27:27]     Visual reuse:    0
[01:27:27]     Visual fallback: 0
[01:27:27] 
=== COLLISION: GENERATE STL ===
[01:27:27]   base_link: cylinder -> 96 tris (4.8 KB)
[01:27:27]   zed2_camera_link: box -> 12 tris (0.7 KB)
[01:27:27]   rear_left_wheel_link: box -> 12 tris (0.7 KB)
[01:27:27]   front_left_wheel_link: box -> 12 tris (0.7 KB)
[01:27:27]   front_right_wheel_link: box -> 12 tris (0.7 KB)
[01:27:27]   rear_right_wheel_link: box -> 12 tris (0.7 KB)
[01:27:27]   rplidar_s2_link: box -> 12 tris (0.7 KB)
[01:27:27] 
  Generated 7 collision STL files
[01:27:27] 
=== PACKAGE: FRAMES ===
[01:27:27]   -> debug/frame_model.json (pre-frame cache)
[01:27:27]   Frame convention: ros
[01:27:27]   Frame overrides:  config/frame_overrides.csv
[01:27:27]   Rebased links:    4/7
[01:27:27] 
=== PACKAGE: XACRO ===
[01:27:27]   → urdf/assemblies/front_left_wheel_link.urdf.xacro
[01:27:27]   → urdf/assemblies/front_right_wheel_link.urdf.xacro
[01:27:27]   → urdf/assemblies/ma_robot.urdf.xacro
[01:27:27]   → urdf/assemblies/rear_left_wheel_link.urdf.xacro
[01:27:27]   → urdf/assemblies/rear_right_wheel_link.urdf.xacro
[01:27:27]   → urdf/ma_robot.urdf.xacro
[01:27:27] 
=== PACKAGE: URDF (flat, for validation) ===
[01:27:27]   → urdf/ma_robot.urdf
[01:27:27] 
=== PACKAGE: ROS2 FILES ===
[01:27:27]   → package.xml
[01:27:27]   → CMakeLists.txt
[01:27:27]   → launch/display.launch.py
[01:27:27]   → rviz/display.rviz
[01:27:27]   → config/joint_state.yaml
[01:27:27]   → config/ros2_controllers.yaml
[01:27:27] 
=== PACKAGE: SUPPLEMENTARY DATA ===
[01:27:27]   → robot_data.yaml
[01:27:27]   -> docs/transforms.md
[01:27:27] 
=== PACKAGE: README ===
[01:27:27]   → README.md
[01:27:27]   Cleaned up 14 retained OBJ/MTL files
[01:27:27] 
=== PACKAGE: COMPLETE ===
[01:27:27]   Package generated: C:/Users/mamre/OneDrive/Desktop/New folder/ETGAH-Robotics-Masterclass\ma_robot_description
[01:27:27]   Xacro: urdf/ma_robot.urdf.xacro (+ 5 assembly macros)
[01:27:27]   URDF:  urdf/ma_robot.urdf (flat, for validation)
[01:27:27]   Launch: ros2 launch ma_robot_description display.launch.py
[01:27:27] 
=== EXPORT COMPLETE ===
```

# Export Log: ma_robot

**Generated:** 2026-09-02T22:20:55.155471

```
[22:20:11] fusion2URDF v3.1.0
[22:20:11] Time: 2026-09-02T22:20:11.504281
[22:20:11] Design: ma_robot
[22:20:11] Components: 19
[22:20:11] 
=== PHASE 1: EXTRACTION ===
[22:20:11]   Document unit: mm
[22:20:11] 
=== EXTRACTION: OCCURRENCES ===
[22:20:11]   [LEAF] d=0 zed2_camera_link
[22:20:11]     path: zed2_camera_link:1
[22:20:11]     global_pos: (0.145000, -0.062500, -0.007371) m
[22:20:11]     mass: 0.178229 kg, bodies: 1
[22:20:11]     com_global: (0.145000, -0.046995, 0.035018) m
[22:20:11]     com_component_local: (0.000000, 0.015505, 0.042389) m
[22:20:11]     inertia@origin: ixx=3.897245e-04 iyy=7.565457e-04 izz=4.819299e-04 kg·m²
[22:20:11]     inertia@com:    ixx=2.662726e-05 iyy=4.362977e-04 izz=4.390806e-04 kg·m²
[22:20:11]     material: PA_11_Nylon_HP_11_30_with_EOS_P_396_3D_Printer
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Nylon_12_with_Formlabs_Fuse_1_3D_Printer]
[22:20:11]     bbox: (0.1747 x 0.0316 x 0.0297) m
[22:20:11]   [LEAF] d=0 rplidar_s2_link
[22:20:11]     path: rplidar_s2_link:1
[22:20:11]     global_pos: (-0.433747, -0.657506, 0.046815) m
[22:20:11]     mass: 0.203764 kg, bodies: 28
[22:20:11]     com_global: (-1.028760, -0.124565, 0.059695) m
[22:20:11]     com_component_local: (-0.595013, 0.532942, 0.012880) m
[22:20:11]     inertia@origin: ixx=5.804326e-02 iyy=7.231055e-02 izz=1.302519e-01 kg·m²
[22:20:11]     inertia@com:    ixx=1.351079e-04 iyy=1.362177e-04 izz=2.370283e-04 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(1.00, 1.00, 1.00) [Copper_Raw]
[22:20:11]     bbox: (0.0770 x 0.0770 x 0.0389) m
[22:20:11]   [LEAF] d=1 Part1_1
[22:20:11]     path: front_left_wheel_link:1+Part1 (1):1
[22:20:11]     global_pos: (0.130000, 0.073000, 0.020000) m
[22:20:11]     mass: 0.080563 kg, bodies: 1
[22:20:11]     com_global: (0.130000, 0.073000, 0.022406) m
[22:20:11]     com_component_local: (-0.000000, -0.000000, 0.002406) m
[22:20:11]     inertia@origin: ixx=3.067888e-05 iyy=3.067884e-05 izz=5.976875e-05 kg·m²
[22:20:11]     inertia@com:    ixx=3.021264e-05 iyy=3.021260e-05 izz=5.976875e-05 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.79, 0.82, 0.93) [Opaque_202_209_238]
[22:20:11]     bbox: (0.0766 x 0.0768 x 0.0107) m
[22:20:11]   [LEAF] d=1 Part4_1
[22:20:11]     path: front_left_wheel_link:1+Part4 (1):1
[22:20:11]     global_pos: (0.113860, 0.037417, 0.050030) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.134860, 0.037417, 0.050030) m
[22:20:11]     com_component_local: (0.021000, 0.000000, 0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part1_1
[22:20:11]     path: front_left_wheel_link:1+Part1 (1):2
[22:20:11]     global_pos: (0.130000, 0.031464, 0.020000) m
[22:20:11]     mass: 0.080563 kg, bodies: 1
[22:20:11]     com_global: (0.130000, 0.031463, 0.022406) m
[22:20:11]     com_component_local: (-0.000000, -0.000000, 0.002406) m
[22:20:11]     inertia@origin: ixx=3.067888e-05 iyy=3.067884e-05 izz=5.976875e-05 kg·m²
[22:20:11]     inertia@com:    ixx=3.021264e-05 iyy=3.021260e-05 izz=5.976875e-05 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.79, 0.82, 0.93) [Opaque_202_209_238]
[22:20:11]     bbox: (0.0766 x 0.0768 x 0.0107) m
[22:20:11]   [LEAF] d=1 Part4_1
[22:20:11]     path: front_left_wheel_link:1+Part4 (1):2
[22:20:11]     global_pos: (0.097624, 0.037417, 0.009320) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.118624, 0.037417, 0.009320) m
[22:20:11]     com_component_local: (0.021000, 0.000000, 0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_1
[22:20:11]     path: front_left_wheel_link:1+Part4 (1):3
[22:20:11]     global_pos: (0.099065, 0.038409, 0.033299) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.120065, 0.038409, 0.033299) m
[22:20:11]     com_component_local: (0.021000, 0.000000, 0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_1
[22:20:11]     path: front_left_wheel_link:1+Part4 (1):4
[22:20:11]     global_pos: (0.135098, 0.037205, -0.013803) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.156098, 0.037205, -0.013803) m
[22:20:11]     com_component_local: (0.021000, 0.000000, 0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_1
[22:20:11]     path: front_left_wheel_link:1+Part4 (1):5
[22:20:11]     global_pos: (0.155437, 0.037417, -0.002698) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.176437, 0.037417, -0.002698) m
[22:20:11]     com_component_local: (0.021000, 0.000000, 0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_1
[22:20:11]     path: front_left_wheel_link:1+Part4 (1):6
[22:20:11]     global_pos: (0.112064, 0.037417, -0.008992) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.133064, 0.037417, -0.008992) m
[22:20:11]     com_component_local: (0.021000, 0.000000, 0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_1
[22:20:11]     path: front_left_wheel_link:1+Part4 (1):7
[22:20:11]     global_pos: (0.164076, 0.037417, 0.018963) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.185076, 0.037417, 0.018963) m
[22:20:11]     com_component_local: (0.021000, 0.000000, 0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_1
[22:20:11]     path: front_left_wheel_link:1+Part4 (1):8
[22:20:11]     global_pos: (0.156771, 0.037417, 0.041109) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.177771, 0.037417, 0.041109) m
[22:20:11]     com_component_local: (0.021000, 0.000000, 0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_1
[22:20:11]     path: front_left_wheel_link:1+Part4 (1):9
[22:20:11]     global_pos: (0.136770, 0.037205, 0.053508) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.157770, 0.037205, 0.053508) m
[22:20:11]     com_component_local: (0.021000, 0.000000, 0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part2_1
[22:20:11]     path: front_left_wheel_link:1+Part2 (1):1
[22:20:11]     global_pos: (0.130000, 0.070000, 0.020000) m
[22:20:11]     mass: 0.398719 kg, bodies: 1
[22:20:11]     com_global: (0.130000, 0.087773, 0.020000) m
[22:20:11]     com_component_local: (-0.000000, 0.017773, 0.000000) m
[22:20:11]     inertia@origin: ixx=2.179435e-04 iyy=9.886321e-05 izz=2.179435e-04 kg·m²
[22:20:11]     inertia@com:    ixx=9.199087e-05 iyy=9.886321e-05 izz=9.199086e-05 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.79, 0.82, 0.93) [Opaque_202_209_238]
[22:20:11]     bbox: (0.0440 x 0.0360 x 0.0440) m
[22:20:11]   [SUBASM] d=0 front_left_wheel_link
[22:20:11]     path: front_left_wheel_link:1
[22:20:11]     global_pos: (0.000000, 0.000000, 0.000000) m
[22:20:11]   [LEAF] d=1 Part1_2
[22:20:11]     path: rear_right_wheel_link:1+Part1 (2):1
[22:20:11]     global_pos: (-0.020000, -0.197000, 0.020000) m
[22:20:11]     mass: 0.080563 kg, bodies: 1
[22:20:11]     com_global: (-0.020000, -0.197000, 0.022406) m
[22:20:11]     com_component_local: (-0.000000, -0.000000, 0.002406) m
[22:20:11]     inertia@origin: ixx=3.067888e-05 iyy=3.067884e-05 izz=5.976875e-05 kg·m²
[22:20:11]     inertia@com:    ixx=3.021264e-05 iyy=3.021260e-05 izz=5.976875e-05 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.79, 0.82, 0.93) [Opaque_202_209_238]
[22:20:11]     bbox: (0.0766 x 0.0768 x 0.0107) m
[22:20:11]   [LEAF] d=1 Part4_2
[22:20:11]     path: rear_right_wheel_link:1+Part4 (2):1
[22:20:11]     global_pos: (-0.036140, -0.161417, -0.010030) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (-0.015140, -0.161417, -0.010030) m
[22:20:11]     com_component_local: (0.021000, 0.000000, 0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part2_2
[22:20:11]     path: rear_right_wheel_link:1+Part2 (2):1
[22:20:11]     global_pos: (-0.020000, -0.194000, 0.020000) m
[22:20:11]     mass: 0.398719 kg, bodies: 1
[22:20:11]     com_global: (-0.020000, -0.176227, 0.020000) m
[22:20:11]     com_component_local: (-0.000000, 0.017773, 0.000000) m
[22:20:11]     inertia@origin: ixx=2.179435e-04 iyy=9.886321e-05 izz=2.179435e-04 kg·m²
[22:20:11]     inertia@com:    ixx=9.199087e-05 iyy=9.886321e-05 izz=9.199086e-05 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.79, 0.82, 0.93) [Opaque_202_209_238]
[22:20:11]     bbox: (0.0440 x 0.0360 x 0.0440) m
[22:20:11]   [LEAF] d=1 Part1_2
[22:20:11]     path: rear_right_wheel_link:1+Part1 (2):2
[22:20:11]     global_pos: (-0.020000, -0.155464, 0.020000) m
[22:20:11]     mass: 0.080563 kg, bodies: 1
[22:20:11]     com_global: (-0.020000, -0.155464, 0.022406) m
[22:20:11]     com_component_local: (-0.000000, -0.000000, 0.002406) m
[22:20:11]     inertia@origin: ixx=3.067888e-05 iyy=3.067884e-05 izz=5.976875e-05 kg·m²
[22:20:11]     inertia@com:    ixx=3.021264e-05 iyy=3.021260e-05 izz=5.976875e-05 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.79, 0.82, 0.93) [Opaque_202_209_238]
[22:20:11]     bbox: (0.0766 x 0.0768 x 0.0107) m
[22:20:11]   [LEAF] d=1 Part4_2
[22:20:11]     path: rear_right_wheel_link:1+Part4 (2):2
[22:20:11]     global_pos: (-0.052376, -0.161417, 0.030680) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (-0.031376, -0.161417, 0.030680) m
[22:20:11]     com_component_local: (0.021000, 0.000000, 0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_2
[22:20:11]     path: rear_right_wheel_link:1+Part4 (2):3
[22:20:11]     global_pos: (-0.050935, -0.162409, 0.006701) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (-0.029935, -0.162409, 0.006701) m
[22:20:11]     com_component_local: (0.021000, 0.000000, 0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_2
[22:20:11]     path: rear_right_wheel_link:1+Part4 (2):4
[22:20:11]     global_pos: (-0.014902, -0.161205, 0.053803) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.006098, -0.161205, 0.053803) m
[22:20:11]     com_component_local: (0.021000, 0.000000, 0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_2
[22:20:11]     path: rear_right_wheel_link:1+Part4 (2):5
[22:20:11]     global_pos: (0.005437, -0.161417, 0.042698) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.026437, -0.161417, 0.042698) m
[22:20:11]     com_component_local: (0.021000, 0.000000, 0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_2
[22:20:11]     path: rear_right_wheel_link:1+Part4 (2):6
[22:20:11]     global_pos: (-0.037936, -0.161417, 0.048992) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (-0.016936, -0.161417, 0.048992) m
[22:20:11]     com_component_local: (0.021000, 0.000000, 0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_2
[22:20:11]     path: rear_right_wheel_link:1+Part4 (2):7
[22:20:11]     global_pos: (0.014076, -0.161417, 0.021037) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.035076, -0.161417, 0.021037) m
[22:20:11]     com_component_local: (0.021000, 0.000000, 0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_2
[22:20:11]     path: rear_right_wheel_link:1+Part4 (2):8
[22:20:11]     global_pos: (0.006771, -0.161417, -0.001109) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.027771, -0.161417, -0.001109) m
[22:20:11]     com_component_local: (0.021000, 0.000000, 0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_2
[22:20:11]     path: rear_right_wheel_link:1+Part4 (2):9
[22:20:11]     global_pos: (-0.013230, -0.161205, -0.013508) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.007770, -0.161205, -0.013508) m
[22:20:11]     com_component_local: (0.021000, 0.000000, 0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [SUBASM] d=0 rear_right_wheel_link
[22:20:11]     path: rear_right_wheel_link:1
[22:20:11]     global_pos: (0.000000, 0.000000, 0.000000) m
[22:20:11]   [LEAF] d=1 Part1_1_Mirror
[22:20:11]     path: front_right_wheel_link:1+Part1 (1)(Mirror):1
[22:20:11]     global_pos: (0.130000, -0.197000, 0.020000) m
[22:20:11]     mass: 0.080563 kg, bodies: 1
[22:20:11]     com_global: (0.130000, -0.197000, 0.017594) m
[22:20:11]     com_component_local: (-0.000000, -0.000000, -0.002406) m
[22:20:11]     inertia@origin: ixx=3.067887e-05 iyy=3.067883e-05 izz=5.976873e-05 kg·m²
[22:20:11]     inertia@com:    ixx=3.021263e-05 iyy=3.021259e-05 izz=5.976873e-05 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.79, 0.82, 0.93) [Opaque_202_209_238]
[22:20:11]     bbox: (0.0766 x 0.0768 x 0.0107) m
[22:20:11]   [LEAF] d=1 Part1_1_Mirror
[22:20:11]     path: front_right_wheel_link:1+Part1 (1)(Mirror):2
[22:20:11]     global_pos: (0.130000, -0.155464, 0.020000) m
[22:20:11]     mass: 0.080563 kg, bodies: 1
[22:20:11]     com_global: (0.130000, -0.155464, 0.017594) m
[22:20:11]     com_component_local: (-0.000000, -0.000000, -0.002406) m
[22:20:11]     inertia@origin: ixx=3.067887e-05 iyy=3.067883e-05 izz=5.976873e-05 kg·m²
[22:20:11]     inertia@com:    ixx=3.021263e-05 iyy=3.021259e-05 izz=5.976873e-05 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.79, 0.82, 0.93) [Opaque_202_209_238]
[22:20:11]     bbox: (0.0766 x 0.0768 x 0.0107) m
[22:20:11]   [LEAF] d=1 Part4_1_Mirror
[22:20:11]     path: front_right_wheel_link:1+Part4 (1)(Mirror):1
[22:20:11]     global_pos: (0.113860, -0.161417, 0.050030) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.134860, -0.161417, 0.050030) m
[22:20:11]     com_component_local: (0.021000, 0.000000, -0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_1_Mirror
[22:20:11]     path: front_right_wheel_link:1+Part4 (1)(Mirror):2
[22:20:11]     global_pos: (0.097624, -0.161417, 0.009320) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.118624, -0.161417, 0.009320) m
[22:20:11]     com_component_local: (0.021000, 0.000000, -0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_1_Mirror
[22:20:11]     path: front_right_wheel_link:1+Part4 (1)(Mirror):3
[22:20:11]     global_pos: (0.099065, -0.162409, 0.033299) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.120065, -0.162409, 0.033299) m
[22:20:11]     com_component_local: (0.021000, 0.000000, -0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_1_Mirror
[22:20:11]     path: front_right_wheel_link:1+Part4 (1)(Mirror):4
[22:20:11]     global_pos: (0.135098, -0.161205, -0.013803) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.156098, -0.161205, -0.013803) m
[22:20:11]     com_component_local: (0.021000, 0.000000, -0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_1_Mirror
[22:20:11]     path: front_right_wheel_link:1+Part4 (1)(Mirror):5
[22:20:11]     global_pos: (0.155437, -0.161417, -0.002698) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.176437, -0.161417, -0.002698) m
[22:20:11]     com_component_local: (0.021000, 0.000000, -0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_1_Mirror
[22:20:11]     path: front_right_wheel_link:1+Part4 (1)(Mirror):6
[22:20:11]     global_pos: (0.112064, -0.161417, -0.008992) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.133064, -0.161417, -0.008992) m
[22:20:11]     com_component_local: (0.021000, 0.000000, -0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_1_Mirror
[22:20:11]     path: front_right_wheel_link:1+Part4 (1)(Mirror):7
[22:20:11]     global_pos: (0.164076, -0.161417, 0.018963) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.185076, -0.161417, 0.018963) m
[22:20:11]     com_component_local: (0.021000, 0.000000, -0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_1_Mirror
[22:20:11]     path: front_right_wheel_link:1+Part4 (1)(Mirror):8
[22:20:11]     global_pos: (0.156771, -0.161417, 0.041109) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.177771, -0.161417, 0.041109) m
[22:20:11]     com_component_local: (0.021000, 0.000000, -0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_1_Mirror
[22:20:11]     path: front_right_wheel_link:1+Part4 (1)(Mirror):9
[22:20:11]     global_pos: (0.136770, -0.161205, 0.053508) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.157770, -0.161205, 0.053508) m
[22:20:11]     com_component_local: (0.021000, 0.000000, -0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part2_1_Mirror
[22:20:11]     path: front_right_wheel_link:1+Part2 (1)(Mirror):1
[22:20:11]     global_pos: (0.130000, -0.194000, 0.020000) m
[22:20:11]     mass: 0.398719 kg, bodies: 1
[22:20:11]     com_global: (0.130000, -0.176227, 0.020000) m
[22:20:11]     com_component_local: (-0.000000, 0.017773, -0.000000) m
[22:20:11]     inertia@origin: ixx=2.179435e-04 iyy=9.886321e-05 izz=2.179435e-04 kg·m²
[22:20:11]     inertia@com:    ixx=9.199087e-05 iyy=9.886321e-05 izz=9.199086e-05 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.79, 0.82, 0.93) [Opaque_202_209_238]
[22:20:11]     bbox: (0.0440 x 0.0360 x 0.0440) m
[22:20:11]   [SUBASM] d=0 front_right_wheel_link
[22:20:11]     path: front_right_wheel_link:1
[22:20:11]     global_pos: (0.000000, -0.300000, 0.000000) m
[22:20:11]   [LEAF] d=1 Part1_2_Mirror
[22:20:11]     path: rear_left_wheel_link:1+Part1 (2)(Mirror):1
[22:20:11]     global_pos: (-0.020000, 0.072000, 0.020000) m
[22:20:11]     mass: 0.080563 kg, bodies: 1
[22:20:11]     com_global: (-0.020000, 0.072000, 0.017594) m
[22:20:11]     com_component_local: (-0.000000, -0.000000, -0.002406) m
[22:20:11]     inertia@origin: ixx=3.067887e-05 iyy=3.067883e-05 izz=5.976873e-05 kg·m²
[22:20:11]     inertia@com:    ixx=3.021263e-05 iyy=3.021259e-05 izz=5.976873e-05 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.79, 0.82, 0.93) [Opaque_202_209_238]
[22:20:11]     bbox: (0.0766 x 0.0768 x 0.0107) m
[22:20:11]   [LEAF] d=1 Part1_2_Mirror
[22:20:11]     path: rear_left_wheel_link:1+Part1 (2)(Mirror):2
[22:20:11]     global_pos: (-0.020000, 0.030464, 0.020000) m
[22:20:11]     mass: 0.080563 kg, bodies: 1
[22:20:11]     com_global: (-0.020000, 0.030463, 0.017594) m
[22:20:11]     com_component_local: (-0.000000, -0.000000, -0.002406) m
[22:20:11]     inertia@origin: ixx=3.067887e-05 iyy=3.067883e-05 izz=5.976873e-05 kg·m²
[22:20:11]     inertia@com:    ixx=3.021263e-05 iyy=3.021259e-05 izz=5.976873e-05 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.79, 0.82, 0.93) [Opaque_202_209_238]
[22:20:11]     bbox: (0.0766 x 0.0768 x 0.0107) m
[22:20:11]   [LEAF] d=1 Part4_2_Mirror
[22:20:11]     path: rear_left_wheel_link:1+Part4 (2)(Mirror):1
[22:20:11]     global_pos: (-0.036140, 0.036417, -0.010030) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (-0.015140, 0.036417, -0.010030) m
[22:20:11]     com_component_local: (0.021000, 0.000000, -0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_2_Mirror
[22:20:11]     path: rear_left_wheel_link:1+Part4 (2)(Mirror):2
[22:20:11]     global_pos: (-0.052376, 0.036417, 0.030680) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (-0.031376, 0.036417, 0.030680) m
[22:20:11]     com_component_local: (0.021000, 0.000000, -0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_2_Mirror
[22:20:11]     path: rear_left_wheel_link:1+Part4 (2)(Mirror):3
[22:20:11]     global_pos: (-0.050935, 0.037409, 0.006701) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (-0.029935, 0.037409, 0.006701) m
[22:20:11]     com_component_local: (0.021000, 0.000000, -0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_2_Mirror
[22:20:11]     path: rear_left_wheel_link:1+Part4 (2)(Mirror):4
[22:20:11]     global_pos: (-0.014902, 0.036205, 0.053803) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.006098, 0.036205, 0.053803) m
[22:20:11]     com_component_local: (0.021000, 0.000000, -0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_2_Mirror
[22:20:11]     path: rear_left_wheel_link:1+Part4 (2)(Mirror):5
[22:20:11]     global_pos: (0.005437, 0.036417, 0.042698) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.026437, 0.036417, 0.042698) m
[22:20:11]     com_component_local: (0.021000, 0.000000, -0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_2_Mirror
[22:20:11]     path: rear_left_wheel_link:1+Part4 (2)(Mirror):6
[22:20:11]     global_pos: (-0.037936, 0.036417, 0.048992) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (-0.016936, 0.036417, 0.048992) m
[22:20:11]     com_component_local: (0.021000, 0.000000, -0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_2_Mirror
[22:20:11]     path: rear_left_wheel_link:1+Part4 (2)(Mirror):7
[22:20:11]     global_pos: (0.014076, 0.036417, 0.021037) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.035076, 0.036417, 0.021037) m
[22:20:11]     com_component_local: (0.021000, 0.000000, -0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_2_Mirror
[22:20:11]     path: rear_left_wheel_link:1+Part4 (2)(Mirror):8
[22:20:11]     global_pos: (0.006771, 0.036417, -0.001109) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.027771, 0.036417, -0.001109) m
[22:20:11]     com_component_local: (0.021000, 0.000000, -0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part4_2_Mirror
[22:20:11]     path: rear_left_wheel_link:1+Part4 (2)(Mirror):9
[22:20:11]     global_pos: (-0.013230, 0.036205, -0.013508) m
[22:20:11]     mass: 0.045349 kg, bodies: 1
[22:20:11]     com_global: (0.007770, 0.036205, -0.013508) m
[22:20:11]     com_component_local: (0.021000, 0.000000, -0.000000) m
[22:20:11]     inertia@origin: ixx=1.178635e-06 iyy=2.470789e-05 izz=2.470789e-05 kg·m²
[22:20:11]     inertia@com:    ixx=1.178635e-06 iyy=4.708795e-06 izz=4.708795e-06 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.25, 0.25, 0.25) [Opaque_64_64_64]
[22:20:11]     bbox: (0.0420 x 0.0160 x 0.0160) m
[22:20:11]   [LEAF] d=1 Part2_2_Mirror
[22:20:11]     path: rear_left_wheel_link:1+Part2 (2)(Mirror):1
[22:20:11]     global_pos: (-0.020000, 0.069000, 0.020000) m
[22:20:11]     mass: 0.398719 kg, bodies: 1
[22:20:11]     com_global: (-0.020000, 0.086773, 0.020000) m
[22:20:11]     com_component_local: (-0.000000, 0.017773, -0.000000) m
[22:20:11]     inertia@origin: ixx=2.179435e-04 iyy=9.886321e-05 izz=2.179435e-04 kg·m²
[22:20:11]     inertia@com:    ixx=9.199087e-05 iyy=9.886321e-05 izz=9.199086e-05 kg·m²
[22:20:11]     material: Steel
[22:20:11]     color: RGB(0.79, 0.82, 0.93) [Opaque_202_209_238]
[22:20:11]     bbox: (0.0440 x 0.0360 x 0.0440) m
[22:20:11]   [SUBASM] d=0 rear_left_wheel_link
[22:20:11]     path: rear_left_wheel_link:1
[22:20:11]     global_pos: (0.000000, 0.050000, 0.000000) m
[22:20:11]   Extracted 54 occurrences
[22:20:11] 
=== EXTRACTION: JOINTS ===
[22:20:11]   WARNING:   Added synthetic design-root link 'ma_robot' for root-owned joint endpoint(s)
[22:20:11]   WARNING:   regular joint in component 'ma_robot' 'Rigid 1': occurrenceTwo is unavailable; using design root 'ma_robot' as parent endpoint
[22:20:11]   WARNING:   regular joint in component 'ma_robot': failed to read geometry: 'Joint' object has no attribute 'geometry'
[22:20:11]   [REGULAR in ma_robot] Rigid_1
[22:20:11]     parent(occ2): ma_robot path=__design_root__
[22:20:11]     child(occ1):  zed2_camera_link path=zed2_camera_link:1
[22:20:11]     geometryOrOriginOne: (14.5000, -6.2500, 3.5000) cm
[22:20:11]     geometryOrOriginTwo: (14.5000, -6.2500, 3.5000) cm
[22:20:11]     occ1.transform: (14.5000, -6.2500, -0.7371) cm (ctx_depth=0)
[22:20:11]     occ1.global:    (14.5000, -6.2500, -0.7371) cm
[22:20:11]  -> origin_global: (0.145000, -0.062500, 0.035000) m [via geometryOrOriginOne]
[22:20:11]     motion: rigid, axis: (0.000, 0.000, 1.000)
[22:20:11]   WARNING:   regular joint in component 'ma_robot' 'Rigid 2': occurrenceTwo is unavailable; using design root 'ma_robot' as parent endpoint
[22:20:11]   WARNING:   regular joint in component 'ma_robot': failed to read geometry: 'Joint' object has no attribute 'geometry'
[22:20:11]   [REGULAR in ma_robot] Rigid_2
[22:20:11]     parent(occ2): ma_robot path=__design_root__
[22:20:11]     child(occ1):  rplidar_s2_link path=rplidar_s2_link:1
[22:20:11]     geometryOrOriginOne: (9.9270, -6.2500, 5.0000) cm
[22:20:11]     geometryOrOriginTwo: (4.9270, -6.2500, 5.0000) cm
[22:20:11]     occ1.transform: (-43.3747, -65.7506, 4.6815) cm (ctx_depth=0)
[22:20:11]     occ1.global:    (-43.3747, -65.7506, 4.6815) cm
[22:20:11]  -> origin_global: (0.099270, -0.062500, 0.050000) m [via geometryOrOriginOne]
[22:20:11]     motion: rigid, axis: (0.000, 0.000, 1.000)
[22:20:11]   WARNING:   regular joint in component 'ma_robot' 'Revolute 5': occurrenceTwo is unavailable; using design root 'ma_robot' as parent endpoint
[22:20:11]   WARNING:   regular joint in component 'ma_robot': failed to read geometry: 'Joint' object has no attribute 'geometry'
[22:20:11]   [REGULAR in ma_robot] Revolute_5
[22:20:11]     parent(occ2): ma_robot path=__design_root__
[22:20:11]     child(occ1):  Part2_1 path=front_left_wheel_link:1+Part2 (1):1
[22:20:11]     geometryOrOriginOne: (13.0000, 7.0000, 2.0000) cm
[22:20:11]     geometryOrOriginTwo: (13.0000, 6.0000, 2.0000) cm
[22:20:11]     occ1.transform: (13.0000, 7.0000, 2.0000) cm (ctx_depth=1)
[22:20:11]     occ1.global:    (13.0000, 7.0000, 2.0000) cm
[22:20:11]  -> origin_global: (0.130000, 0.070000, 0.020000) m [via geometryOrOriginOne]
[22:20:11]     motion: revolute, axis: (0.000, 1.000, 0.000)
[22:20:11]   WARNING:   regular joint in component 'ma_robot' 'Revolute 6': occurrenceTwo is unavailable; using design root 'ma_robot' as parent endpoint
[22:20:11]   WARNING:   regular joint in component 'ma_robot': failed to read geometry: 'Joint' object has no attribute 'geometry'
[22:20:11]   [REGULAR in ma_robot] Revolute_6
[22:20:11]     parent(occ2): ma_robot path=__design_root__
[22:20:11]     child(occ1):  Part2_2 path=rear_right_wheel_link:1+Part2 (2):1
[22:20:11]     geometryOrOriginOne: (-2.0000, -16.8000, 2.0000) cm
[22:20:11]     geometryOrOriginTwo: (-2.0000, -18.5000, 2.0000) cm
[22:20:11]     occ1.transform: (-2.0000, -19.4000, 2.0000) cm (ctx_depth=1)
[22:20:11]     occ1.global:    (-2.0000, -19.4000, 2.0000) cm
[22:20:11]  -> origin_global: (-0.020000, -0.168000, 0.020000) m [via geometryOrOriginOne]
[22:20:11]     motion: revolute, axis: (0.000, -1.000, 0.000)
[22:20:11]   WARNING:   regular joint in component 'ma_robot' 'Revolute 8': occurrenceTwo is unavailable; using design root 'ma_robot' as parent endpoint
[22:20:11]   WARNING:   regular joint in component 'ma_robot': failed to read geometry: 'Joint' object has no attribute 'geometry'
[22:20:11]   [REGULAR in ma_robot] Revolute_8
[22:20:11]     parent(occ2): ma_robot path=__design_root__
[22:20:11]     child(occ1):  Part2_1_Mirror path=front_right_wheel_link:1+Part2 (1)(Mirror):1
[22:20:11]     geometryOrOriginOne: (13.0000, -16.8000, 2.0000) cm
[22:20:11]     geometryOrOriginTwo: (13.0000, -18.5000, 2.0000) cm
[22:20:11]     occ1.transform: (13.0000, -10.6000, -2.0000) cm (ctx_depth=1)
[22:20:11]     occ1.global:    (13.0000, -19.4000, 2.0000) cm
[22:20:11]  -> origin_global: (0.130000, -0.168000, 0.020000) m [via geometryOrOriginOne]
[22:20:11]     motion: revolute, axis: (0.000, -1.000, 0.000)
[22:20:11]   WARNING:   regular joint in component 'ma_robot' 'Revolute 9': occurrenceTwo is unavailable; using design root 'ma_robot' as parent endpoint
[22:20:11]   WARNING:   regular joint in component 'ma_robot': failed to read geometry: 'Joint' object has no attribute 'geometry'
[22:20:11]   [REGULAR in ma_robot] Revolute_9
[22:20:11]     parent(occ2): ma_robot path=__design_root__
[22:20:11]     child(occ1):  Part2_2_Mirror path=rear_left_wheel_link:1+Part2 (2)(Mirror):1
[22:20:11]     geometryOrOriginOne: (-2.0000, 4.3000, 2.0000) cm
[22:20:11]     geometryOrOriginTwo: (-2.0000, 6.0000, 2.0000) cm
[22:20:11]     occ1.transform: (-2.0000, -1.9000, -2.0000) cm (ctx_depth=1)
[22:20:11]     occ1.global:    (-2.0000, 6.9000, 2.0000) cm
[22:20:11]  -> origin_global: (-0.020000, 0.043000, 0.020000) m [via geometryOrOriginOne]
[22:20:11]     motion: revolute, axis: (0.000, 1.000, 0.000)
[22:20:11]   Extracted 6 unique joints
[22:20:11] 
=== EXTRACTION: RIGID GROUPS ===
[22:20:11]   Rigid Group 3: []
[22:20:11]   Rigid Group 1: ['Part1_1', 'Part4_1', 'Part4_1', 'Part4_1', 'Part4_1', 'Part4_1', 'Part2_1', 'Part4_1', 'Part4_1', 'Part4_1', 'Part1_1', 'Part4_1']
[22:20:11]   Rigid Group 1: ['Part1_2', 'Part4_2', 'Part4_2', 'Part4_2', 'Part4_2', 'Part4_2', 'Part2_2', 'Part4_2', 'Part4_2', 'Part4_2', 'Part1_2', 'Part4_2']
[22:20:11]   Rigid Group 1: ['Part1_1_Mirror', 'Part4_1_Mirror', 'Part4_1_Mirror', 'Part4_1_Mirror', 'Part1_1_Mirror', 'Part4_1_Mirror', 'Part4_1_Mirror', 'Part4_1_Mirror', 'Part4_1_Mirror', 'Part2_1_Mirror', 'Part4_1_Mirror', 'Part4_1_Mirror']
[22:20:11]   Rigid Group 1: ['Part4_2_Mirror', 'Part4_2_Mirror', 'Part4_2_Mirror', 'Part4_2_Mirror', 'Part1_2_Mirror', 'Part2_2_Mirror', 'Part4_2_Mirror', 'Part4_2_Mirror', 'Part4_2_Mirror', 'Part1_2_Mirror', 'Part4_2_Mirror', 'Part4_2_Mirror']
[22:20:11]   Extracted 5 rigid groups
[22:20:11] 
=== EXTRACTION SUMMARY ===
[22:20:11]   Occurrences: 55 (4 subassemblies, 51 leaf components)
[22:20:11]   Joints: 6 (0 as-built, 6 regular)
[22:20:11]   Max nesting depth: 1
[22:20:37] 
=== PHASE 1: DEBUG DATA ===
[22:20:37]   extraction_report.md
[22:20:37]   snapshot.json
[22:20:37]   fusion_transforms.json
[22:20:37] 
=== PHASE 2: BUILD ROBOT MODEL ===
[22:20:37] 
=== MODEL: ASSEMBLY HIERARCHY ===
[22:20:37]   Assembly: front_left_wheel_link d=0 offset=(0.0, 0.0, 0.0) mm
[22:20:37]   Assembly: rear_right_wheel_link d=0 offset=(0.0, 0.0, 0.0) mm
[22:20:37]   Assembly: front_right_wheel_link d=0 offset=(0.0, -300.0, 0.0) mm
[22:20:37]   Assembly: rear_left_wheel_link d=0 offset=(0.0, 50.0, 0.0) mm
[22:20:37]   Assembly: ma_robot (synthetic root, wraps design-root leaves so phase 2 has a macro to xacro:include)
[22:20:37]   zed2_camera_link → ma_robot
[22:20:37]   rplidar_s2_link → ma_robot
[22:20:37]   Part1_1 → front_left_wheel_link
[22:20:37]   Part4_1 → front_left_wheel_link
[22:20:37]   Part1_1 → front_left_wheel_link
[22:20:37]   Part4_1 → front_left_wheel_link
[22:20:37]   Part4_1 → front_left_wheel_link
[22:20:37]   Part4_1 → front_left_wheel_link
[22:20:37]   Part4_1 → front_left_wheel_link
[22:20:37]   Part4_1 → front_left_wheel_link
[22:20:37]   Part4_1 → front_left_wheel_link
[22:20:37]   Part4_1 → front_left_wheel_link
[22:20:37]   Part4_1 → front_left_wheel_link
[22:20:37]   Part2_1 → front_left_wheel_link
[22:20:37]   Part1_2 → rear_right_wheel_link
[22:20:37]   Part4_2 → rear_right_wheel_link
[22:20:37]   Part2_2 → rear_right_wheel_link
[22:20:37]   Part1_2 → rear_right_wheel_link
[22:20:37]   Part4_2 → rear_right_wheel_link
[22:20:37]   Part4_2 → rear_right_wheel_link
[22:20:37]   Part4_2 → rear_right_wheel_link
[22:20:37]   Part4_2 → rear_right_wheel_link
[22:20:37]   Part4_2 → rear_right_wheel_link
[22:20:37]   Part4_2 → rear_right_wheel_link
[22:20:37]   Part4_2 → rear_right_wheel_link
[22:20:37]   Part4_2 → rear_right_wheel_link
[22:20:37]   Part1_1_Mirror → front_right_wheel_link
[22:20:37]   Part1_1_Mirror → front_right_wheel_link
[22:20:37]   Part4_1_Mirror → front_right_wheel_link
[22:20:37]   Part4_1_Mirror → front_right_wheel_link
[22:20:37]   Part4_1_Mirror → front_right_wheel_link
[22:20:37]   Part4_1_Mirror → front_right_wheel_link
[22:20:37]   Part4_1_Mirror → front_right_wheel_link
[22:20:37]   Part4_1_Mirror → front_right_wheel_link
[22:20:37]   Part4_1_Mirror → front_right_wheel_link
[22:20:37]   Part4_1_Mirror → front_right_wheel_link
[22:20:37]   Part4_1_Mirror → front_right_wheel_link
[22:20:37]   Part2_1_Mirror → front_right_wheel_link
[22:20:37]   Part1_2_Mirror → rear_left_wheel_link
[22:20:37]   Part1_2_Mirror → rear_left_wheel_link
[22:20:37]   Part4_2_Mirror → rear_left_wheel_link
[22:20:37]   Part4_2_Mirror → rear_left_wheel_link
[22:20:37]   Part4_2_Mirror → rear_left_wheel_link
[22:20:37]   Part4_2_Mirror → rear_left_wheel_link
[22:20:37]   Part4_2_Mirror → rear_left_wheel_link
[22:20:37]   Part4_2_Mirror → rear_left_wheel_link
[22:20:37]   Part4_2_Mirror → rear_left_wheel_link
[22:20:37]   Part4_2_Mirror → rear_left_wheel_link
[22:20:37]   Part4_2_Mirror → rear_left_wheel_link
[22:20:37]   Part2_2_Mirror → rear_left_wheel_link
[22:20:37]   ma_robot → ma_robot
[22:20:37] 
=== MODEL: RIGID GROUP MERGE ===
[22:20:37]   WARNING:   Rigid group 'Rigid Group 3': no visual members — skipping merge
[22:20:37]   Rigid Group 1: anchor=Part2_1 merged_name=Part2_1 members=12 mass=967.99 g bbox=(108.4 × 46.4 × 108.4) mm
[22:20:37]   Rigid Group 1: dropped front_left_wheel_link/Part1_1 (front_left_wheel_link:1+Part1 (1):2) -> front_left_wheel_link/Part2_1
[22:20:37]   Rigid Group 1: dropped front_left_wheel_link/Part4_1 (front_left_wheel_link:1+Part4 (1):5) -> front_left_wheel_link/Part2_1
[22:20:37]   Rigid Group 1: dropped front_left_wheel_link/Part4_1 (front_left_wheel_link:1+Part4 (1):3) -> front_left_wheel_link/Part2_1
[22:20:37]   Rigid Group 1: dropped front_left_wheel_link/Part4_1 (front_left_wheel_link:1+Part4 (1):2) -> front_left_wheel_link/Part2_1
[22:20:37]   Rigid Group 1: dropped front_left_wheel_link/Part4_1 (front_left_wheel_link:1+Part4 (1):7) -> front_left_wheel_link/Part2_1
[22:20:37]   Rigid Group 1: dropped front_left_wheel_link/Part4_1 (front_left_wheel_link:1+Part4 (1):6) -> front_left_wheel_link/Part2_1
[22:20:37]   Rigid Group 1: dropped front_left_wheel_link/Part4_1 (front_left_wheel_link:1+Part4 (1):8) -> front_left_wheel_link/Part2_1
[22:20:37]   Rigid Group 1: dropped front_left_wheel_link/Part4_1 (front_left_wheel_link:1+Part4 (1):4) -> front_left_wheel_link/Part2_1
[22:20:37]   Rigid Group 1: dropped front_left_wheel_link/Part4_1 (front_left_wheel_link:1+Part4 (1):9) -> front_left_wheel_link/Part2_1
[22:20:37]   Rigid Group 1: dropped front_left_wheel_link/Part1_1 (front_left_wheel_link:1+Part1 (1):1) -> front_left_wheel_link/Part2_1
[22:20:37]   Rigid Group 1: dropped front_left_wheel_link/Part4_1 (front_left_wheel_link:1+Part4 (1):1) -> front_left_wheel_link/Part2_1
[22:20:37]   Rigid Group 1: anchor=Part2_2 merged_name=Part2_2 members=12 mass=967.99 g bbox=(108.4 × 46.4 × 108.4) mm
[22:20:37]   Rigid Group 1: dropped rear_right_wheel_link/Part1_2 (rear_right_wheel_link:1+Part1 (2):2) -> rear_right_wheel_link/Part2_2
[22:20:37]   Rigid Group 1: dropped rear_right_wheel_link/Part4_2 (rear_right_wheel_link:1+Part4 (2):5) -> rear_right_wheel_link/Part2_2
[22:20:37]   Rigid Group 1: dropped rear_right_wheel_link/Part4_2 (rear_right_wheel_link:1+Part4 (2):3) -> rear_right_wheel_link/Part2_2
[22:20:37]   Rigid Group 1: dropped rear_right_wheel_link/Part4_2 (rear_right_wheel_link:1+Part4 (2):2) -> rear_right_wheel_link/Part2_2
[22:20:37]   Rigid Group 1: dropped rear_right_wheel_link/Part4_2 (rear_right_wheel_link:1+Part4 (2):7) -> rear_right_wheel_link/Part2_2
[22:20:37]   Rigid Group 1: dropped rear_right_wheel_link/Part4_2 (rear_right_wheel_link:1+Part4 (2):6) -> rear_right_wheel_link/Part2_2
[22:20:37]   Rigid Group 1: dropped rear_right_wheel_link/Part4_2 (rear_right_wheel_link:1+Part4 (2):8) -> rear_right_wheel_link/Part2_2
[22:20:37]   Rigid Group 1: dropped rear_right_wheel_link/Part4_2 (rear_right_wheel_link:1+Part4 (2):4) -> rear_right_wheel_link/Part2_2
[22:20:37]   Rigid Group 1: dropped rear_right_wheel_link/Part4_2 (rear_right_wheel_link:1+Part4 (2):9) -> rear_right_wheel_link/Part2_2
[22:20:37]   Rigid Group 1: dropped rear_right_wheel_link/Part1_2 (rear_right_wheel_link:1+Part1 (2):1) -> rear_right_wheel_link/Part2_2
[22:20:37]   Rigid Group 1: dropped rear_right_wheel_link/Part4_2 (rear_right_wheel_link:1+Part4 (2):1) -> rear_right_wheel_link/Part2_2
[22:20:37]   Rigid Group 1: anchor=Part2_1_Mirror merged_name=Part2_1_Mirror members=12 mass=967.99 g bbox=(108.4 × 46.4 × 108.4) mm
[22:20:37]   Rigid Group 1: dropped front_right_wheel_link/Part1_1_Mirror (front_right_wheel_link:1+Part1 (1)(Mirror):1) -> front_right_wheel_link/Part2_1_Mirror
[22:20:37]   Rigid Group 1: dropped front_right_wheel_link/Part4_1_Mirror (front_right_wheel_link:1+Part4 (1)(Mirror):3) -> front_right_wheel_link/Part2_1_Mirror
[22:20:37]   Rigid Group 1: dropped front_right_wheel_link/Part4_1_Mirror (front_right_wheel_link:1+Part4 (1)(Mirror):6) -> front_right_wheel_link/Part2_1_Mirror
[22:20:37]   Rigid Group 1: dropped front_right_wheel_link/Part4_1_Mirror (front_right_wheel_link:1+Part4 (1)(Mirror):7) -> front_right_wheel_link/Part2_1_Mirror
[22:20:37]   Rigid Group 1: dropped front_right_wheel_link/Part1_1_Mirror (front_right_wheel_link:1+Part1 (1)(Mirror):2) -> front_right_wheel_link/Part2_1_Mirror
[22:20:37]   Rigid Group 1: dropped front_right_wheel_link/Part4_1_Mirror (front_right_wheel_link:1+Part4 (1)(Mirror):2) -> front_right_wheel_link/Part2_1_Mirror
[22:20:37]   Rigid Group 1: dropped front_right_wheel_link/Part4_1_Mirror (front_right_wheel_link:1+Part4 (1)(Mirror):8) -> front_right_wheel_link/Part2_1_Mirror
[22:20:37]   Rigid Group 1: dropped front_right_wheel_link/Part4_1_Mirror (front_right_wheel_link:1+Part4 (1)(Mirror):1) -> front_right_wheel_link/Part2_1_Mirror
[22:20:37]   Rigid Group 1: dropped front_right_wheel_link/Part4_1_Mirror (front_right_wheel_link:1+Part4 (1)(Mirror):4) -> front_right_wheel_link/Part2_1_Mirror
[22:20:37]   Rigid Group 1: dropped front_right_wheel_link/Part4_1_Mirror (front_right_wheel_link:1+Part4 (1)(Mirror):5) -> front_right_wheel_link/Part2_1_Mirror
[22:20:37]   Rigid Group 1: dropped front_right_wheel_link/Part4_1_Mirror (front_right_wheel_link:1+Part4 (1)(Mirror):9) -> front_right_wheel_link/Part2_1_Mirror
[22:20:37]   Rigid Group 1: anchor=Part2_2_Mirror merged_name=Part2_2_Mirror members=12 mass=967.99 g bbox=(108.4 × 46.4 × 108.4) mm
[22:20:37]   Rigid Group 1: dropped rear_left_wheel_link/Part4_2_Mirror (rear_left_wheel_link:1+Part4 (2)(Mirror):7) -> rear_left_wheel_link/Part2_2_Mirror
[22:20:37]   Rigid Group 1: dropped rear_left_wheel_link/Part4_2_Mirror (rear_left_wheel_link:1+Part4 (2)(Mirror):9) -> rear_left_wheel_link/Part2_2_Mirror
[22:20:37]   Rigid Group 1: dropped rear_left_wheel_link/Part4_2_Mirror (rear_left_wheel_link:1+Part4 (2)(Mirror):8) -> rear_left_wheel_link/Part2_2_Mirror
[22:20:37]   Rigid Group 1: dropped rear_left_wheel_link/Part4_2_Mirror (rear_left_wheel_link:1+Part4 (2)(Mirror):4) -> rear_left_wheel_link/Part2_2_Mirror
[22:20:37]   Rigid Group 1: dropped rear_left_wheel_link/Part1_2_Mirror (rear_left_wheel_link:1+Part1 (2)(Mirror):2) -> rear_left_wheel_link/Part2_2_Mirror
[22:20:37]   Rigid Group 1: dropped rear_left_wheel_link/Part4_2_Mirror (rear_left_wheel_link:1+Part4 (2)(Mirror):1) -> rear_left_wheel_link/Part2_2_Mirror
[22:20:37]   Rigid Group 1: dropped rear_left_wheel_link/Part4_2_Mirror (rear_left_wheel_link:1+Part4 (2)(Mirror):5) -> rear_left_wheel_link/Part2_2_Mirror
[22:20:37]   Rigid Group 1: dropped rear_left_wheel_link/Part4_2_Mirror (rear_left_wheel_link:1+Part4 (2)(Mirror):2) -> rear_left_wheel_link/Part2_2_Mirror
[22:20:37]   Rigid Group 1: dropped rear_left_wheel_link/Part1_2_Mirror (rear_left_wheel_link:1+Part1 (2)(Mirror):1) -> rear_left_wheel_link/Part2_2_Mirror
[22:20:37]   Rigid Group 1: dropped rear_left_wheel_link/Part4_2_Mirror (rear_left_wheel_link:1+Part4 (2)(Mirror):6) -> rear_left_wheel_link/Part2_2_Mirror
[22:20:37]   Rigid Group 1: dropped rear_left_wheel_link/Part4_2_Mirror (rear_left_wheel_link:1+Part4 (2)(Mirror):3) -> rear_left_wheel_link/Part2_2_Mirror
[22:20:37]   No auto rigid islands found
[22:20:37] 
=== MODEL: RESOLVE JOINT PATHS ===
[22:20:37]   Rigid_1              ma_robot/ma_robot → ma_robot/zed2_camera_link  [rigid] internal
[22:20:37]   Rigid_2              ma_robot/ma_robot → ma_robot/rplidar_s2_link  [rigid] internal
[22:20:37]   Revolute_5           ma_robot/ma_robot → front_left_wheel_link/Part2_1  [revolute] MOUNT
[22:20:37]   Revolute_6           ma_robot/ma_robot → rear_right_wheel_link/Part2_2  [revolute] MOUNT
[22:20:37]   Revolute_8           ma_robot/ma_robot → front_right_wheel_link/Part2_1_Mirror  [revolute] MOUNT
[22:20:37]   Revolute_9           ma_robot/ma_robot → rear_left_wheel_link/Part2_2_Mirror  [revolute] MOUNT
[22:20:37] 
=== MODEL: DETECT ROOT ===
[22:20:37]   Parent-only nodes: 1
[22:20:37]     ma_robot/ma_robot
[22:20:37]   → Root: ma_robot/ma_robot
[22:20:37] 
=== MODEL: RESOLVE NAMES ===
[22:20:37]   WARNING: Root link renamed: 'ma_robot' → 'base_link'
[22:20:37]   ma_robot (ma_robot) → base_link
[22:20:37]   Part2_1 (front_left_wheel_link) → Part2_1
[22:20:37]   Part2_1_Mirror (front_right_wheel_link) → Part2_1_Mirror
[22:20:37]   Part2_2_Mirror (rear_left_wheel_link) → Part2_2_Mirror
[22:20:37]   Part2_2 (rear_right_wheel_link) → Part2_2
[22:20:37]   rplidar_s2_link (ma_robot) → rplidar_s2_link
[22:20:37]   zed2_camera_link (ma_robot) → zed2_camera_link
[22:20:37]   Root link URDF name: base_link
[22:20:37] 
=== MODEL: BUILD LINKS ===
[22:20:37]   Part2_1: MERGED (12 members) mass=967.99 g
[22:20:37]   Part2_2: MERGED (12 members) mass=967.99 g
[22:20:37]   Part2_1_Mirror: MERGED (12 members) mass=967.99 g
[22:20:37]   Part2_2_Mirror: MERGED (12 members) mass=967.99 g
[22:20:37]   Built 7 links
[22:20:37] 
=== MODEL: BUILD JOINTS ===
[22:20:37]   NOTE: joint origin rpy derived from child occurrence's transform2 rotation (was hardcoded 0,0,0 pre-2026-04-13)
[22:20:37]   Rigid_1: joint origin rpy = (0.000000, -0.000000, -1.570796) rad (+0.00°, -0.00°, -90.00°) [from child transform2 rotation]
[22:20:37]   Rigid_1: base_link → zed2_camera_link [fixed]
[22:20:37]     origin_xyz: (0.145000, -0.062500, -0.007371) m [child_minus_parent]
[22:20:37]     origin_global: (0.082500, -0.207500, 0.027629) m
[22:20:37]   Rigid_2: joint origin rpy = (0.000000, -0.000000, -1.570796) rad (+0.00°, -0.00°, -90.00°) [from child transform2 rotation]
[22:20:37]   Rigid_2: base_link → rplidar_s2_link [fixed]
[22:20:37]     origin_xyz: (-0.433747, -0.657506, 0.046815) m [child_minus_parent]
[22:20:37]     origin_global: (-0.496247, -0.756777, 0.096815) m
[22:20:37]   Revolute_5: mesh bake offset = (-130.00, -70.00, -20.00) mm [child-local frame]
[22:20:37]   Revolute_5: joint origin rpy = (3.141593, -0.000000, 0.000000) rad (+180.00°, -0.00°, +0.00°) [from child transform2 rotation]
[22:20:37]  Revolute_5: axis remapped world -> joint/child frame: (0.000, 1.000, 0.000) -> (0.000, -1.000, 0.000)
[22:20:37]   Revolute_5: base_link → Part2_1 [continuous]
[22:20:37]     origin_xyz: (0.260000, 0.000000, 0.000000) m [joint_minus_parent]
[22:20:37]     origin_global: (0.260000, 0.000000, 0.000000) m
[22:20:37]   Revolute_6: mesh bake offset = (20.00, 168.00, -20.00) mm [child-local frame]
[22:20:37]   Revolute_6: base_link → Part2_2 [continuous]
[22:20:37]     origin_xyz: (-0.040000, -0.362000, 0.040000) m [joint_minus_parent]
[22:20:37]     origin_global: (-0.040000, -0.362000, 0.040000) m
[22:20:37]   Revolute_8: mesh bake offset = (-130.00, 168.00, -20.00) mm [child-local frame]
[22:20:37]   Revolute_8: base_link → Part2_1_Mirror [continuous]
[22:20:37]     origin_xyz: (0.260000, -0.362000, 0.040000) m [joint_minus_parent]
[22:20:37]     origin_global: (0.260000, -0.362000, 0.040000) m
[22:20:37]   Revolute_9: mesh bake offset = (20.00, -43.00, -20.00) mm [child-local frame]
[22:20:37]   Revolute_9: joint origin rpy = (3.141593, -0.000000, 0.000000) rad (+180.00°, -0.00°, +0.00°) [from child transform2 rotation]
[22:20:37]  Revolute_9: axis remapped world -> joint/child frame: (0.000, 1.000, 0.000) -> (0.000, -1.000, -0.000)
[22:20:37]   Revolute_9: base_link → Part2_2_Mirror [continuous]
[22:20:37]     origin_xyz: (-0.040000, 0.026000, 0.000000) m [joint_minus_parent]
[22:20:37]     origin_global: (-0.040000, 0.026000, 0.000000) m
[22:20:37]   Built 6 joints
[22:20:37] 
=== MODEL: VALIDATE ===
[22:20:37]   Validation passed (1 warnings)
[22:20:37] 
[22:20:37] Kinematic tree:
[22:20:37]   base_link (2899g)
[22:20:37]     ─── Rigid_1 [fixed]
[22:20:37]       zed2_camera_link (178g)
[22:20:37]     ─── Rigid_2 [fixed]
[22:20:37]       rplidar_s2_link (204g)
[22:20:37]     ─⟳─ Revolute_5 [continuous]
[22:20:37]       Part2_1 (968g) [MERGED]
[22:20:37]     ─⟳─ Revolute_6 [continuous]
[22:20:37]       Part2_2 (968g) [MERGED]
[22:20:37]     ─⟳─ Revolute_8 [continuous]
[22:20:37]       Part2_1_Mirror (968g) [MERGED]
[22:20:37]     ─⟳─ Revolute_9 [continuous]
[22:20:37]       Part2_2_Mirror (968g) [MERGED]
[22:20:37] 
=== MODEL SUMMARY ===
[22:20:37]   Robot: ma_robot
[22:20:37]   Root link: base_link
[22:20:37]   Links: 7
[22:20:37]   Joints: 6
[22:20:37]   Assemblies: 5
[22:20:37]   Warnings: 1
[22:20:37]   Errors: 0
[22:20:43] 
=== MESH EXPORT ===
[22:20:43]   zed2_camera_link:
[22:20:43]     OBJ exported (376945 bytes)
[22:20:43]     MTL preserved from Fusion (multi-material)
[22:20:43]     DAE written → meshes/ma_robot/zed2_camera_link.dae (OBJ retained for collision fit)
[22:20:43]   rplidar_s2_link:
[22:20:48]     OBJ exported (16393466 bytes)
[22:20:48]     MTL preserved from Fusion (multi-material)
[22:20:50]     DAE written → meshes/ma_robot/rplidar_s2_link.dae (OBJ retained for collision fit)
[22:20:50]   Part2_1:
[22:20:50]     Merge target: sub-asm 'front_left_wheel_link' (members=12)
[22:20:50]     MTL preserved from Fusion (multi-material)
[22:20:50]     Applying anchor frame correction (anchor not at identity within front_left_wheel_link:1)
[22:20:51]     Merged OBJ written via Fusion API (3422.9 KB)
[22:20:51]     DAE written → meshes/front_left_wheel_link/Part2_1.dae (OBJ retained for collision fit)
[22:20:51]   Part2_2:
[22:20:51]     Merge target: sub-asm 'rear_right_wheel_link' (members=12)
[22:20:51]     MTL preserved from Fusion (multi-material)
[22:20:51]     Applying anchor frame correction (anchor not at identity within rear_right_wheel_link:1)
[22:20:52]     Merged OBJ written via Fusion API (3419.0 KB)
[22:20:52]     DAE written → meshes/rear_right_wheel_link/Part2_2.dae (OBJ retained for collision fit)
[22:20:52]   Part2_1_Mirror:
[22:20:52]     Merge target: sub-asm 'front_right_wheel_link' (members=12)
[22:20:52]     MTL preserved from Fusion (multi-material)
[22:20:52]     Applying anchor frame correction (anchor not at identity within front_right_wheel_link:1)
[22:20:53]     Merged OBJ written via Fusion API (3434.2 KB)
[22:20:53]     DAE written → meshes/front_right_wheel_link/Part2_1_Mirror.dae (OBJ retained for collision fit)
[22:20:53]   Part2_2_Mirror:
[22:20:53]     Merge target: sub-asm 'rear_left_wheel_link' (members=12)
[22:20:53]     MTL preserved from Fusion (multi-material)
[22:20:53]     Applying anchor frame correction (anchor not at identity within rear_left_wheel_link:1)
[22:20:53]     Merged OBJ written via Fusion API (3418.4 KB)
[22:20:54]     DAE written → meshes/rear_left_wheel_link/Part2_2_Mirror.dae (OBJ retained for collision fit)
[22:20:54]   base_link:
[22:20:54]   WARNING:     Root-body visual export failed for base_link: Body1: execute raised 3 : Autodesk Translation Services failed to translate the current document to obj file!; Body2: execute raised 3 : Autodesk Translation Services failed to translate the current document to obj file!; trying component export fallback
[22:20:54]   ERROR:     Visual export failed for base_link: property '_get_isVisible' of 'Occurrence' object has no setter
[22:20:54] 
  Mesh export summary:
[22:20:54]     Visual (OBJ+MTL):              6
[22:20:54]     Collision sub-component (STL):  0
[22:20:54]     Collision body + warning (STL): 0
[22:20:54]     Skipped (no Fusion ref):        1
[22:20:54] 
=== PHASE 3: SCREENSHOT ===
[22:20:54]   → images/robot.png
[22:20:54] 
=== PACKAGE: GENERATE ===
[22:20:54]   Package: ma_robot_description
[22:20:54]   Output:  C:/Users/mamre/OneDrive/Desktop/New folder/ETGAH-Robotics-Masterclass\ma_robot_description
[22:20:54] 
=== COLLISION: RESOLVE ===
[22:20:54]   zed2_camera_link: primitive (box [174.7 x 31.6 x 29.7] mm)
[22:20:54]   rplidar_s2_link: primitive (box [22.0 x 7.9 x 3.7] mm)
[22:20:55]   Part2_1: primitive (box [78.3 x 79.7 x 47.9] mm)
[22:20:55]   Part2_2: primitive (box [79.4 x 77.2 x 47.7] mm)
[22:20:55]   Part2_1_Mirror: primitive (cylinder r=54.2 h=46.4 mm)
[22:20:55]   Part2_2_Mirror: primitive (cylinder r=54.2 h=46.4 mm)
[22:20:55]   base_link: primitive (cylinder r=127.0 h=120.0 mm)
[22:20:55] 
  Collision summary:
[22:20:55]     Explicit:        0
[22:20:55]     Primitive (STL): 7
[22:20:55]     Convex hull STL: 0
[22:20:55]     Visual reuse:    0
[22:20:55]     Visual fallback: 0
[22:20:55] 
=== COLLISION: GENERATE STL ===
[22:20:55]   zed2_camera_link: box -> 12 tris (0.7 KB)
[22:20:55]   rplidar_s2_link: box -> 12 tris (0.7 KB)
[22:20:55]   Part2_1: box -> 12 tris (0.7 KB)
[22:20:55]   Part2_2: box -> 12 tris (0.7 KB)
[22:20:55]   Part2_1_Mirror: cylinder -> 96 tris (4.8 KB)
[22:20:55]   Part2_2_Mirror: cylinder -> 96 tris (4.8 KB)
[22:20:55]   base_link: cylinder -> 96 tris (4.8 KB)
[22:20:55] 
  Generated 7 collision STL files
[22:20:55] 
=== PACKAGE: FRAMES ===
[22:20:55]   -> debug/frame_model.json (pre-frame cache)
[22:20:55]   Frame convention: ros
[22:20:55]   Frame overrides:  config/frame_overrides.csv
[22:20:55]   Rebased links:    4/7
[22:20:55] 
=== PACKAGE: XACRO ===
[22:20:55]   → urdf/assemblies/front_left_wheel_link.urdf.xacro
[22:20:55]   → urdf/assemblies/front_right_wheel_link.urdf.xacro
[22:20:55]   → urdf/assemblies/ma_robot.urdf.xacro
[22:20:55]   → urdf/assemblies/rear_left_wheel_link.urdf.xacro
[22:20:55]   → urdf/assemblies/rear_right_wheel_link.urdf.xacro
[22:20:55]   → urdf/ma_robot.urdf.xacro
[22:20:55] 
=== PACKAGE: URDF (flat, for validation) ===
[22:20:55]   → urdf/ma_robot.urdf
[22:20:55] 
=== PACKAGE: ROS2 FILES ===
[22:20:55]   → package.xml
[22:20:55]   → CMakeLists.txt
[22:20:55]   → launch/display.launch.py
[22:20:55]   → rviz/display.rviz
[22:20:55]   → config/joint_state.yaml
[22:20:55]   → config/ros2_controllers.yaml
[22:20:55] 
=== PACKAGE: SUPPLEMENTARY DATA ===
[22:20:55]   → robot_data.yaml
[22:20:55]   -> docs/transforms.md
[22:20:55] 
=== PACKAGE: README ===
[22:20:55]   → README.md
[22:20:55]   Cleaned up 12 retained OBJ/MTL files
[22:20:55] 
=== PACKAGE: COMPLETE ===
[22:20:55]   Package generated: C:/Users/mamre/OneDrive/Desktop/New folder/ETGAH-Robotics-Masterclass\ma_robot_description
[22:20:55]   Xacro: urdf/ma_robot.urdf.xacro (+ 5 assembly macros)
[22:20:55]   URDF:  urdf/ma_robot.urdf (flat, for validation)
[22:20:55]   Launch: ros2 launch ma_robot_description display.launch.py
[22:20:55] 
=== EXPORT COMPLETE ===
```

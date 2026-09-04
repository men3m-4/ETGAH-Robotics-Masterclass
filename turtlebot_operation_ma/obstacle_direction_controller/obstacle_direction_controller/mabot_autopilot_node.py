#!/usr/bin/env python3

import math
import time

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan


class MABotAutopilot(Node):
    """
    Reactive obstacle-avoidance controller designed for MABot.

    LiDAR convention:
        0 degrees   = forward
        +90 degrees = left
        -90 degrees = right
        180 degrees = rear
    """

    def __init__(self):
        super().__init__('mabot_autopilot_node')

        # ==================================================
        # Configurable parameters
        # ==================================================

        self.declare_parameter('scan_topic', '/scan')
        self.declare_parameter('cmd_vel_topic', '/cmd_vel')

        self.declare_parameter('forward_speed', 0.30)
        self.declare_parameter('slow_speed', 0.10)
        self.declare_parameter('reverse_speed', -0.12)
        self.declare_parameter('turn_speed', 0.85)

        self.declare_parameter('emergency_distance', 0.28)
        self.declare_parameter('stop_distance', 0.60)
        self.declare_parameter('slow_distance', 1.10)
        self.declare_parameter('clear_distance', 0.85)

        self.declare_parameter('corner_distance', 0.48)
        self.declare_parameter('side_clearance', 0.45)
        self.declare_parameter('rear_stop_distance', 0.40)

        self.declare_parameter('reverse_duration', 0.80)
        self.declare_parameter('scan_timeout', 0.75)

        self.declare_parameter('steering_gain', 0.55)
        self.declare_parameter('max_forward_turn', 0.30)

        self.declare_parameter('control_frequency', 20.0)
        self.declare_parameter('maximum_scan_distance', 5.0)

        # ==================================================
        # Read parameters
        # ==================================================

        self.scan_topic = (
            self.get_parameter('scan_topic')
            .get_parameter_value()
            .string_value
        )

        self.cmd_vel_topic = (
            self.get_parameter('cmd_vel_topic')
            .get_parameter_value()
            .string_value
        )

        self.forward_speed = self._double_parameter(
            'forward_speed'
        )

        self.slow_speed = self._double_parameter(
            'slow_speed'
        )

        self.reverse_speed = self._double_parameter(
            'reverse_speed'
        )

        self.turn_speed = self._double_parameter(
            'turn_speed'
        )

        self.emergency_distance = self._double_parameter(
            'emergency_distance'
        )

        self.stop_distance = self._double_parameter(
            'stop_distance'
        )

        self.slow_distance = self._double_parameter(
            'slow_distance'
        )

        self.clear_distance = self._double_parameter(
            'clear_distance'
        )

        self.corner_distance = self._double_parameter(
            'corner_distance'
        )

        self.side_clearance = self._double_parameter(
            'side_clearance'
        )

        self.rear_stop_distance = self._double_parameter(
            'rear_stop_distance'
        )

        self.reverse_duration = self._double_parameter(
            'reverse_duration'
        )

        self.scan_timeout = self._double_parameter(
            'scan_timeout'
        )

        self.steering_gain = self._double_parameter(
            'steering_gain'
        )

        self.max_forward_turn = self._double_parameter(
            'max_forward_turn'
        )

        self.control_frequency = self._double_parameter(
            'control_frequency'
        )

        self.maximum_scan_distance = self._double_parameter(
            'maximum_scan_distance'
        )

        # ==================================================
        # ROS interfaces
        # ==================================================

        self.scan_subscription = self.create_subscription(
            LaserScan,
            self.scan_topic,
            self.scan_callback,
            qos_profile_sensor_data
        )

        self.velocity_publisher = self.create_publisher(
            Twist,
            self.cmd_vel_topic,
            10
        )

        # The timer keeps command publishing independent
        # from the LiDAR publishing frequency.
        timer_period = 1.0 / max(
            self.control_frequency,
            1.0
        )

        self.control_timer = self.create_timer(
            timer_period,
            self.control_callback
        )

        # ==================================================
        # Controller state
        # ==================================================

        self.state = 'waiting'
        self.turning_direction = 0

        self.latest_distances = None
        self.last_scan_wall_time = None
        self.reverse_start_wall_time = None
        self.last_status_log_wall_time = 0.0

        self.get_logger().info(
            'MABot Autopilot started'
        )

        self.get_logger().info(
            f'Listening to {self.scan_topic}'
        )

        self.get_logger().info(
            f'Publishing commands to {self.cmd_vel_topic}'
        )

        self.get_logger().info(
            'Waiting for the first LaserScan message'
        )

    # ======================================================
    # Parameter helper
    # ======================================================

    def _double_parameter(self, name: str) -> float:
        return (
            self.get_parameter(name)
            .get_parameter_value()
            .double_value
        )

    # ======================================================
    # LaserScan callback
    # ======================================================

    def scan_callback(self, msg: LaserScan):
        """
        Convert the LaserScan into safety sectors.

        The calculation uses angle_min and angle_increment,
        so it works with both 360-sample and 720-sample scans.
        """

        front = self._sector_distance(
            msg,
            center_angle=0.0,
            width=math.radians(70.0)
        )

        front_left = self._sector_distance(
            msg,
            center_angle=math.radians(40.0),
            width=math.radians(45.0)
        )

        front_right = self._sector_distance(
            msg,
            center_angle=math.radians(-40.0),
            width=math.radians(45.0)
        )

        left = self._sector_distance(
            msg,
            center_angle=math.radians(90.0),
            width=math.radians(65.0)
        )

        right = self._sector_distance(
            msg,
            center_angle=math.radians(-90.0),
            width=math.radians(65.0)
        )

        rear = self._sector_distance(
            msg,
            center_angle=math.pi,
            width=math.radians(70.0)
        )

        self.latest_distances = {
            'front': front,
            'front_left': front_left,
            'front_right': front_right,
            'left': left,
            'right': right,
            'rear': rear,
        }

        self.last_scan_wall_time = time.monotonic()

        if self.state == 'waiting':
            self._set_state('forward')

    # ======================================================
    # Sector calculation
    # ======================================================

    def _sector_distance(
        self,
        msg: LaserScan,
        center_angle: float,
        width: float
    ) -> float:
        """
        Return the nearest valid range inside an angular sector.
        """

        half_width = width / 2.0
        valid_ranges = []

        minimum_valid_range = max(
            float(msg.range_min),
            0.05
        )

        if (
            math.isfinite(msg.range_max)
            and msg.range_max > 0.0
        ):
            maximum_valid_range = min(
                float(msg.range_max),
                self.maximum_scan_distance
            )
        else:
            maximum_valid_range = (
                self.maximum_scan_distance
            )

        for index, measured_range in enumerate(msg.ranges):

            if not math.isfinite(measured_range):
                continue

            if not (
                minimum_valid_range
                <= measured_range
                <= maximum_valid_range
            ):
                continue

            ray_angle = (
                msg.angle_min
                + index * msg.angle_increment
            )

            angular_error = self._normalize_angle(
                ray_angle - center_angle
            )

            if abs(angular_error) <= half_width:
                valid_ranges.append(measured_range)

        if not valid_ranges:
            return self.maximum_scan_distance

        return min(valid_ranges)

    # ======================================================
    # Control loop
    # ======================================================

    def control_callback(self):
        """
        Generate a safe velocity command from the latest scan.
        """

        command = Twist()
        current_wall_time = time.monotonic()

        # Stop when no scan has been received.
        if (
            self.latest_distances is None
            or self.last_scan_wall_time is None
        ):
            self.velocity_publisher.publish(command)
            return

        # Stop if the LiDAR stream becomes stale.
        scan_age = (
            current_wall_time
            - self.last_scan_wall_time
        )

        if scan_age > self.scan_timeout:
            self._set_state('waiting')
            self.velocity_publisher.publish(command)
            return

        front = self.latest_distances['front']
        front_left = self.latest_distances['front_left']
        front_right = self.latest_distances['front_right']
        left = self.latest_distances['left']
        right = self.latest_distances['right']
        rear = self.latest_distances['rear']

        left_score = min(front_left, left)
        right_score = min(front_right, right)

        self._log_status(
            current_wall_time,
            front,
            front_left,
            front_right,
            left,
            right,
            rear
        )

        # ==================================================
        # Emergency protection
        # ==================================================

        if (
            self.state != 'reverse'
            and front <= self.emergency_distance
        ):
            if rear > self.rear_stop_distance:

                self.reverse_start_wall_time = (
                    current_wall_time
                )

                self.turning_direction = (
                    1 if left_score >= right_score else -1
                )

                self._set_state('reverse')

            else:
                self.turning_direction = (
                    1 if left_score >= right_score else -1
                )

                self._set_state('turn')

            # Publish zero for one control cycle so that
            # the robot brakes before changing direction.
            self.velocity_publisher.publish(command)
            return

        # ==================================================
        # Forward state
        # ==================================================

        if self.state == 'forward':

            obstacle_in_front = (
                front <= self.stop_distance
            )

            obstacle_at_left_corner = (
                front_left <= self.corner_distance
            )

            obstacle_at_right_corner = (
                front_right <= self.corner_distance
            )

            if (
                obstacle_in_front
                or obstacle_at_left_corner
                or obstacle_at_right_corner
            ):
                self.turning_direction = self._choose_turn(
                    left_score,
                    right_score
                )

                self._set_state('turn')

                # Brake for one cycle before turning.
                self.velocity_publisher.publish(command)
                return

            command.linear.x = self._forward_velocity(
                front,
                front_left,
                front_right
            )

            command.angular.z = self._forward_steering(
                front_left,
                front_right
            )

        # ==================================================
        # Turn state
        # ==================================================

        elif self.state == 'turn':

            if self.turning_direction == 0:
                self.turning_direction = self._choose_turn(
                    left_score,
                    right_score
                )

            # Change the turning side if the selected side
            # becomes blocked and the opposite side is safer.
            if (
                self.turning_direction > 0
                and left_score <= self.side_clearance
                and right_score > left_score + 0.10
            ):
                self.turning_direction = -1

            elif (
                self.turning_direction < 0
                and right_score <= self.side_clearance
                and left_score > right_score + 0.10
            ):
                self.turning_direction = 1

            path_is_clear = (
                front > self.clear_distance
                and front_left > self.corner_distance
                and front_right > self.corner_distance
            )

            if path_is_clear:
                self._set_state('forward')

                # Start moving on the following control cycle.
                self.velocity_publisher.publish(command)
                return

            both_sides_blocked = (
                left_score <= self.side_clearance
                and right_score <= self.side_clearance
            )

            if (
                both_sides_blocked
                and rear > self.rear_stop_distance
            ):
                self.reverse_start_wall_time = (
                    current_wall_time
                )

                self._set_state('reverse')

                self.velocity_publisher.publish(command)
                return

            command.linear.x = 0.0
            command.angular.z = (
                self.turn_speed
                * self.turning_direction
            )

        # ==================================================
        # Reverse state
        # ==================================================

        elif self.state == 'reverse':

            if self.reverse_start_wall_time is None:
                self.reverse_start_wall_time = (
                    current_wall_time
                )

            reverse_elapsed = (
                current_wall_time
                - self.reverse_start_wall_time
            )

            rear_is_blocked = (
                rear <= self.rear_stop_distance
            )

            reverse_finished = (
                reverse_elapsed >= self.reverse_duration
            )

            if rear_is_blocked or reverse_finished:
                self.reverse_start_wall_time = None

                self.turning_direction = self._choose_turn(
                    left_score,
                    right_score
                )

                self._set_state('turn')

                self.velocity_publisher.publish(command)
                return

            command.linear.x = self.reverse_speed
            command.angular.z = 0.0

        # ==================================================
        # Waiting or unknown state
        # ==================================================

        else:
            self._set_state('waiting')

        self.velocity_publisher.publish(command)

    # ======================================================
    # Motion helpers
    # ======================================================

    def _forward_velocity(
        self,
        front: float,
        front_left: float,
        front_right: float
    ) -> float:
        """
        Reduce the forward speed gradually near obstacles.
        """

        nearest_front = min(
            front,
            front_left,
            front_right
        )

        denominator = max(
            self.slow_distance - self.stop_distance,
            0.001
        )

        speed_ratio = (
            nearest_front - self.stop_distance
        ) / denominator

        speed_ratio = self._clamp(
            speed_ratio,
            0.0,
            1.0
        )

        return (
            self.slow_speed
            + speed_ratio
            * (
                self.forward_speed
                - self.slow_speed
            )
        )

    def _forward_steering(
        self,
        front_left: float,
        front_right: float
    ) -> float:
        """
        Steer gently toward the side with more free space.
        """

        limited_left = min(front_left, 2.0)
        limited_right = min(front_right, 2.0)

        steering_error = (
            limited_left - limited_right
        )

        steering_command = (
            self.steering_gain
            * steering_error
        )

        return self._clamp(
            steering_command,
            -self.max_forward_turn,
            self.max_forward_turn
        )

    def _choose_turn(
        self,
        left_score: float,
        right_score: float
    ) -> int:
        """
        Return +1 for left or -1 for right.
        """

        if left_score >= right_score:
            return 1

        return -1

    # ======================================================
    # State and logging helpers
    # ======================================================

    def _set_state(self, new_state: str):
        """
        Change state and log only real state transitions.
        """

        if new_state == self.state:
            return

        old_state = self.state
        self.state = new_state

        self.get_logger().warning(
            f'STATE: {old_state.upper()} '
            f'-> {new_state.upper()}'
        )

    def _log_status(
        self,
        current_wall_time: float,
        front: float,
        front_left: float,
        front_right: float,
        left: float,
        right: float,
        rear: float
    ):
        """
        Print one status line per second instead of logging
        on every LaserScan message.
        """

        if (
            current_wall_time
            - self.last_status_log_wall_time
            < 1.0
        ):
            return

        self.last_status_log_wall_time = (
            current_wall_time
        )

        self.get_logger().info(
            f'{self.state.upper()} | '
            f'F:{front:.2f} '
            f'FL:{front_left:.2f} '
            f'FR:{front_right:.2f} '
            f'L:{left:.2f} '
            f'R:{right:.2f} '
            f'B:{rear:.2f}'
        )

    # ======================================================
    # General helpers
    # ======================================================

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        """
        Normalize an angle to [-pi, pi].
        """

        return math.atan2(
            math.sin(angle),
            math.cos(angle)
        )

    @staticmethod
    def _clamp(
        value: float,
        minimum: float,
        maximum: float
    ) -> float:
        return max(
            minimum,
            min(maximum, value)
        )

    # ======================================================
    # Safe shutdown
    # ======================================================

    def stop_robot(self):
        """
        Publish zero velocity before shutting down.
        """

        stop_command = Twist()

        for _ in range(3):
            self.velocity_publisher.publish(
                stop_command
            )


def main(args=None):
    rclpy.init(args=args)

    controller = MABotAutopilot()

    try:
        rclpy.spin(controller)

    except KeyboardInterrupt:
        pass

    finally:
        controller.stop_robot()
        controller.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
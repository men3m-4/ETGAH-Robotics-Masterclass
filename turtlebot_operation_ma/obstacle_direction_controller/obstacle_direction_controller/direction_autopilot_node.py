#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

from obstacle_direction_interfaces.srv import SetDirection


class ObstacleAvoidanceController(Node):

    def __init__(self):
        super().__init__('direction_autopilot_node')

        # ---------------------------------------------------
        # Subscriber: receives LiDAR data
        # ---------------------------------------------------
        self.scan_subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        # ---------------------------------------------------
        # Publisher: sends velocity commands to TurtleBot3
        # ---------------------------------------------------
        self.velocity_publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        # ---------------------------------------------------
        # Service: manual direction override
        # ---------------------------------------------------
        self.direction_service = self.create_service(
            SetDirection,
            '/set_direction',
            self.set_direction_callback
        )

        # ---------------------------------------------------
        # Robot movement parameters
        # ---------------------------------------------------
        self.obstacle_threshold = 0.50
        self.free_forward_threshold = 1.00

        self.forward_velocity = 0.20
        self.reverse_velocity = -0.15
        self.angular_velocity = 0.50

        # ---------------------------------------------------
        # State machine
        # ---------------------------------------------------
        self.state = 'forward'
        self.turning_direction = 0

        # ---------------------------------------------------
        # Manual override parameters
        # ---------------------------------------------------
        self.override_direction = None
        self.override_end_time = None

        # Forward / Reverse duration
        self.move_override_duration = 2.5

        # Left / Right duration
        self.turn_override_duration = 3.0

        self.get_logger().info(
            'Obstacle Avoidance Controller Started'
        )

        self.get_logger().info(
            '/set_direction service is ready'
        )

    # =======================================================
    # SERVICE CALLBACK
    # =======================================================

    def set_direction_callback(self, request, response):
        """
        Accept manual direction override.

        Valid directions:
        forward
        reverse
        left
        right
        """

        direction = request.direction.strip().lower()

        valid_directions = [
            'forward',
            'reverse',
            'left',
            'right'
        ]

        # Reject invalid commands
        if direction not in valid_directions:

            response.success = False

            response.message = (
                f'Invalid direction: {request.direction}. '
                'Use forward, reverse, left, or right.'
            )

            self.get_logger().warning(
                f'INVALID OVERRIDE REQUEST: {request.direction}'
            )

            return response

        # Activate manual override
        self.override_direction = direction

        current_time = (
            self.get_clock().now().nanoseconds / 1e9
        )

        # Forward and reverse use movement duration
        if direction in ['forward', 'reverse']:
            duration = self.move_override_duration
        else:
            duration = self.turn_override_duration

        self.override_end_time = (
            current_time + duration
        )

        response.success = True

        response.message = (
            f'Robot direction changed to {direction} '
            f'for {duration:.1f} seconds'
        )

        self.get_logger().warning(
            f'MANUAL OVERRIDE STARTED: '
            f'{direction.upper()} for {duration:.1f}s'
        )

        return response

    # =======================================================
    # LIDAR CALLBACK
    # =======================================================

    def scan_callback(self, msg: LaserScan):
        """
        Read LiDAR data and calculate front,
        left and right distances.
        """

        ranges = msg.ranges
        angle_min = msg.angle_min
        angle_increment = msg.angle_increment

        front_distance = self._sector_distance(
            ranges,
            angle_min,
            angle_increment,
            0.0,
            math.radians(30),
            5.0
        )

        left_distance = self._sector_distance(
            ranges,
            angle_min,
            angle_increment,
            math.pi / 2,
            math.radians(30),
            5.0
        )

        right_distance = self._sector_distance(
            ranges,
            angle_min,
            angle_increment,
            -math.pi / 2,
            math.radians(30),
            5.0
        )

        self.get_logger().info(
            f'LiDAR | '
            f'Front: {front_distance:.2f}m | '
            f'Left: {left_distance:.2f}m | '
            f'Right: {right_distance:.2f}m'
        )

        self._control_robot(
            front_distance,
            left_distance,
            right_distance
        )

    # =======================================================
    # ANGLE NORMALIZATION
    # =======================================================

    def _normalize_angle(self, angle: float) -> float:
        """
        Normalize angle to [-pi, pi].
        """

        return math.atan2(
            math.sin(angle),
            math.cos(angle)
        )

    # =======================================================
    # CONVERT ANGLE TO LIDAR INDEX
    # =======================================================

    def _angle_to_index(
        self,
        angle: float,
        angle_min: float,
        angle_increment: float,
        size: int
    ) -> int:

        desired = self._normalize_angle(angle)

        base = self._normalize_angle(angle_min)

        delta = desired - base

        if delta < 0.0:
            delta += 2.0 * math.pi

        index = int(
            round(delta / angle_increment)
        )

        return max(
            0,
            min(size - 1, index)
        )

    # =======================================================
    # GET MINIMUM DISTANCE IN LIDAR SECTOR
    # =======================================================

    def _sector_distance(
        self,
        ranges,
        angle_min: float,
        angle_increment: float,
        center_angle: float,
        width: float,
        max_distance: float
    ) -> float:

        n = len(ranges)

        half_width = width / 2.0

        start_idx = self._angle_to_index(
            center_angle - half_width,
            angle_min,
            angle_increment,
            n
        )

        end_idx = self._angle_to_index(
            center_angle + half_width,
            angle_min,
            angle_increment,
            n
        )

        if start_idx <= end_idx:

            sector = ranges[
                start_idx:end_idx + 1
            ]

        else:

            sector = (
                ranges[start_idx:]
                + ranges[:end_idx + 1]
            )

        valid = [
            r
            for r in sector
            if 0.1 < r < max_distance
        ]

        return (
            min(valid)
            if valid
            else max_distance
        )

    # =======================================================
    # AUTONOMOUS + MANUAL CONTROL
    # =======================================================

    def _control_robot(
        self,
        front,
        left,
        right
    ):

        cmd = Twist()

        # ===================================================
        # MANUAL OVERRIDE
        # ===================================================

        current_time = (
            self.get_clock().now().nanoseconds / 1e9
        )

        if (
            self.override_direction is not None
            and current_time < self.override_end_time
        ):

            # -----------------------------------------------
            # FORWARD
            # -----------------------------------------------
            if self.override_direction == 'forward':

                cmd.linear.x = self.forward_velocity
                cmd.angular.z = 0.0

            # -----------------------------------------------
            # REVERSE
            # -----------------------------------------------
            elif self.override_direction == 'reverse':

                # Straight backward movement only
                cmd.linear.x = self.reverse_velocity
                cmd.angular.z = 0.0

            # -----------------------------------------------
            # LEFT
            # -----------------------------------------------
            elif self.override_direction == 'left':

                cmd.linear.x = 0.0
                cmd.angular.z = self.angular_velocity

            # -----------------------------------------------
            # RIGHT
            # -----------------------------------------------
            elif self.override_direction == 'right':

                cmd.linear.x = 0.0
                cmd.angular.z = -self.angular_velocity

            self.velocity_publisher.publish(cmd)

            self.get_logger().info(
                f'OVERRIDE ACTIVE: '
                f'{self.override_direction.upper()} | '
                f'linear.x={cmd.linear.x:.2f} | '
                f'angular.z={cmd.angular.z:.2f}'
            )

            return

        # ===================================================
        # END OF MANUAL OVERRIDE
        # ===================================================

        elif self.override_direction is not None:

            self.get_logger().info(
                'Manual override finished. '
                'Returning to autonomous mode.'
            )

            self.override_direction = None
            self.override_end_time = None

            self.state = 'forward'
            self.turning_direction = 0

        # ===================================================
        # AUTONOMOUS CONTROL
        # ===================================================

        TURN_SAFETY = 0.40

        can_turn_left = (
            left > TURN_SAFETY
        )

        can_turn_right = (
            right > TURN_SAFETY
        )

        # ===================================================
        # FORWARD STATE
        # ===================================================

        if self.state == 'forward':

            if front <= self.obstacle_threshold:

                self.state = 'turn'

                self.turning_direction = (
                    1
                    if left >= right
                    else -1
                )

                side = (
                    'LEFT'
                    if self.turning_direction > 0
                    else 'RIGHT'
                )

                self.get_logger().warning(
                    f'OBSTACLE DETECTED: '
                    f'Front {front:.2f}m <= '
                    f'{self.obstacle_threshold:.2f}m'
                )

                self.get_logger().warning(
                    f'STATE CHANGE: '
                    f'FORWARD -> TURN {side}'
                )

            else:

                cmd.linear.x = (
                    self.forward_velocity
                )

                cmd.angular.z = 0.0

                self.get_logger().info(
                    'ACTION: FORWARD'
                )

        # ===================================================
        # TURN STATE
        # ===================================================

        if self.state == 'turn':

            if (
                self.turning_direction > 0
                and not can_turn_left
                and can_turn_right
            ):

                self.turning_direction = -1

                self.get_logger().warning(
                    'LEFT BLOCKED: '
                    'Switching turn to RIGHT'
                )

            elif (
                self.turning_direction < 0
                and not can_turn_right
                and can_turn_left
            ):

                self.turning_direction = 1

                self.get_logger().warning(
                    'RIGHT BLOCKED: '
                    'Switching turn to LEFT'
                )

            elif (
                self.turning_direction > 0
                and not can_turn_left
            ):

                self.turning_direction = 0

            elif (
                self.turning_direction < 0
                and not can_turn_right
            ):

                self.turning_direction = 0

            # No safe direction
            if self.turning_direction == 0:

                if (
                    can_turn_left
                    or can_turn_right
                ):

                    self.turning_direction = (
                        1
                        if left >= right
                        else -1
                    )

                else:

                    self.state = 'reverse'

                    self.get_logger().error(
                        f'TRAPPED! '
                        f'L:{left:.2f}m '
                        f'R:{right:.2f}m'
                    )

                    self.get_logger().error(
                        'STATE CHANGE: '
                        'TURN -> REVERSE'
                    )

            # Continue turn
            if self.state == 'turn':

                if (
                    front >
                    self.free_forward_threshold
                ):

                    self.state = 'forward'

                    self.turning_direction = 0

                    cmd.linear.x = (
                        self.forward_velocity
                    )

                    cmd.angular.z = 0.0

                    self.get_logger().info(
                        'PATH CLEAR'
                    )

                    self.get_logger().info(
                        'STATE CHANGE: '
                        'TURN -> FORWARD'
                    )

                    self.get_logger().info(
                        'ACTION: FORWARD'
                    )

                else:

                    cmd.linear.x = 0.0

                    cmd.angular.z = (
                        self.angular_velocity
                        * self.turning_direction
                    )

                    side = (
                        'LEFT'
                        if self.turning_direction > 0
                        else 'RIGHT'
                    )

                    self.get_logger().warning(
                        f'ACTION: TURN {side}'
                    )

        # ===================================================
        # REVERSE STATE
        # ===================================================

        if self.state == 'reverse':

            cmd.linear.x = self.reverse_velocity

            cmd.angular.z = (
                self.angular_velocity
                if left >= right
                else -self.angular_velocity
            )

            side = (
                'LEFT'
                if left >= right
                else 'RIGHT'
            )

            self.get_logger().warning(
                f'ACTION: '
                f'REVERSE + TURN {side}'
            )

            if (
                front >
                self.free_forward_threshold
                and (
                    can_turn_left
                    or can_turn_right
                )
            ):

                self.state = 'forward'

                self.turning_direction = 0

                self.get_logger().info(
                    'RECOVERED'
                )

                self.get_logger().info(
                    'STATE CHANGE: '
                    'REVERSE -> FORWARD'
                )

        # ===================================================
        # PUBLISH COMMAND
        # ===================================================

        self.velocity_publisher.publish(cmd)


# ===========================================================
# MAIN
# ===========================================================

def main(args=None):

    rclpy.init(args=args)

    controller = ObstacleAvoidanceController()

    try:

        rclpy.spin(controller)

    except KeyboardInterrupt:

        pass

    finally:

        stop_cmd = Twist()

        controller.velocity_publisher.publish(
            stop_cmd
        )

        controller.destroy_node()

        rclpy.shutdown()


if __name__ == '__main__':
    main()
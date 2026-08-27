#!/usr/bin/env python3

import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

from geometry_msgs.msg import Twist
from delivery_mission_interfaces.action import DeliveryMission


class DeliveryMissionController(Node):

    def __init__(self):
        super().__init__('delivery_mission_node')

        # Allows action execution and cancel requests
        # to be processed concurrently.
        self.callback_group = ReentrantCallbackGroup()

        # Publisher for robot velocity commands.
        self.velocity_publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        # Action server.
        self.action_server = ActionServer(
            self,
            DeliveryMission,
            'delivery_mission',
            execute_callback=self.execute_callback,
            cancel_callback=self.cancel_callback,
            callback_group=self.callback_group
        )

        # Fixed duration for Phase 2 pickup simulation.
        self.pickup_simulation_duration = 3.0

        # Publish every 0.1 second.
        self.publish_interval = 0.1

        self.get_logger().info(
            'Delivery Mission Action Server started.'
        )

    def cancel_callback(self, cancel_request):
        """
        Accept mission cancel requests.
        """

        self.get_logger().warning(
            'Cancel request received.'
        )

        return CancelResponse.ACCEPT

    def stop_robot(self):
        """
        Stop the robot by publishing zero velocity.
        """

        # Do not publish if ROS context is already closed.
        if not rclpy.ok():
            return

        stop_cmd = Twist()

        stop_cmd.linear.x = 0.0
        stop_cmd.angular.z = 0.0

        self.velocity_publisher.publish(
            stop_cmd
        )

    def mission_timed_out(
        self,
        mission_start_time,
        timeout
    ):
        """
        Check whether mission timeout was exceeded.
        """

        elapsed_time = (
            time.monotonic()
            - mission_start_time
        )

        return elapsed_time >= timeout

    def publish_feedback(
        self,
        goal_handle,
        mission_start_time,
        timeout,
        pickup_progress
    ):
        """
        Publish remaining time and pickup progress.
        """

        elapsed_time = (
            time.monotonic()
            - mission_start_time
        )

        remaining_time = (
            timeout
            - elapsed_time
        )

        if remaining_time < 0.0:
            remaining_time = 0.0

        feedback = DeliveryMission.Feedback()

        feedback.remaining_time = float(
            remaining_time
        )

        feedback.pickup_progress = float(
            pickup_progress
        )

        goal_handle.publish_feedback(
            feedback
        )

    def create_cancel_result(
        self,
        goal_handle
    ):
        """
        Stop robot and return canceled result.
        """

        self.stop_robot()

        goal_handle.canceled()

        result = DeliveryMission.Result()

        result.success = False
        result.message = (
            'Mission canceled by operator'
        )

        self.get_logger().warning(
            'MISSION CANCELED BY OPERATOR'
        )

        return result

    def create_timeout_result(
        self,
        goal_handle,
        phase
    ):
        """
        Stop robot and return timeout result.
        """

        self.stop_robot()

        goal_handle.abort()

        result = DeliveryMission.Result()

        result.success = False
        result.message = (
            f'Mission aborted: timeout exceeded '
            f'during {phase}'
        )

        self.get_logger().error(
            result.message
        )

        return result

    def create_invalid_goal_result(
        self,
        goal_handle,
        message
    ):
        """
        Abort invalid goals.
        """

        self.stop_robot()

        goal_handle.abort()

        result = DeliveryMission.Result()

        result.success = False
        result.message = message

        self.get_logger().error(
            message
        )

        return result

    def execute_callback(
        self,
        goal_handle
    ):
        """
        Execute the complete delivery mission.

        Phase 1:
        Drive forward for pickup_duration.

        Phase 2:
        Stop and simulate package pickup.

        Phase 3:
        Drive forward for delivery_duration.
        """

        goal = goal_handle.request

        self.get_logger().info(
            'Received delivery mission goal'
        )

        self.get_logger().info(
            f'Speed: {goal.speed}'
        )

        self.get_logger().info(
            f'Pickup duration: '
            f'{goal.pickup_duration}'
        )

        self.get_logger().info(
            f'Delivery duration: '
            f'{goal.delivery_duration}'
        )

        self.get_logger().info(
            f'Timeout: {goal.timeout}'
        )

        # ==================================================
        # GOAL VALIDATION
        # ==================================================

        if goal.speed <= 0.0:

            return self.create_invalid_goal_result(
                goal_handle,
                'Mission aborted: speed must be '
                'greater than 0'
            )

        if goal.pickup_duration <= 0.0:

            return self.create_invalid_goal_result(
                goal_handle,
                'Mission aborted: pickup_duration '
                'must be greater than 0'
            )

        if goal.delivery_duration <= 0.0:

            return self.create_invalid_goal_result(
                goal_handle,
                'Mission aborted: delivery_duration '
                'must be greater than 0'
            )

        if goal.timeout <= 0.0:

            return self.create_invalid_goal_result(
                goal_handle,
                'Mission aborted: timeout must be '
                'greater than 0'
            )

        # ==================================================
        # MISSION START
        # ==================================================

        mission_start_time = (
            time.monotonic()
        )

        self.get_logger().info(
            'MISSION STARTED'
        )

        move_cmd = Twist()

        move_cmd.linear.x = goal.speed
        move_cmd.angular.z = 0.0

        # ==================================================
        # PHASE 1
        # DRIVE TO PICKUP LOCATION
        # ==================================================

        self.get_logger().info(
            'PHASE 1 STARTED: '
            'Driving to pickup location'
        )

        phase1_start_time = (
            time.monotonic()
        )

        while True:

            # Check cancel.
            if goal_handle.is_cancel_requested:

                return self.create_cancel_result(
                    goal_handle
                )

            # Check timeout.
            if self.mission_timed_out(
                mission_start_time,
                goal.timeout
            ):

                return self.create_timeout_result(
                    goal_handle,
                    'Phase 1'
                )

            elapsed_phase1 = (
                time.monotonic()
                - phase1_start_time
            )

            if (
                elapsed_phase1
                >= goal.pickup_duration
            ):
                break

            self.velocity_publisher.publish(
                move_cmd
            )

            self.publish_feedback(
                goal_handle,
                mission_start_time,
                goal.timeout,
                0.0
            )

            self.get_logger().info(
                f'PHASE 1: Moving forward | '
                f'Elapsed: '
                f'{elapsed_phase1:.1f}s / '
                f'{goal.pickup_duration:.1f}s'
            )

            time.sleep(
                self.publish_interval
            )

        self.stop_robot()

        self.get_logger().info(
            'PHASE 1 COMPLETE: '
            'Pickup location reached'
        )

        # ==================================================
        # PHASE 2
        # SIMULATED PACKAGE PICKUP
        # ==================================================

        self.get_logger().info(
            'PHASE 2 STARTED: '
            'Simulating package pickup'
        )

        phase2_start_time = (
            time.monotonic()
        )

        while True:

            # Check cancel.
            if goal_handle.is_cancel_requested:

                return self.create_cancel_result(
                    goal_handle
                )

            # Check timeout.
            if self.mission_timed_out(
                mission_start_time,
                goal.timeout
            ):

                return self.create_timeout_result(
                    goal_handle,
                    'Phase 2'
                )

            elapsed_phase2 = (
                time.monotonic()
                - phase2_start_time
            )

            if (
                elapsed_phase2
                >= self.pickup_simulation_duration
            ):
                break

            # Robot stays stopped during pickup.
            self.stop_robot()

            pickup_progress = (
                elapsed_phase2
                / self.pickup_simulation_duration
            ) * 100.0

            pickup_progress = min(
                pickup_progress,
                100.0
            )

            self.publish_feedback(
                goal_handle,
                mission_start_time,
                goal.timeout,
                pickup_progress
            )

            remaining_time = (
                goal.timeout
                - (
                    time.monotonic()
                    - mission_start_time
                )
            )

            if remaining_time < 0.0:
                remaining_time = 0.0

            self.get_logger().info(
                f'PHASE 2: Pickup Progress '
                f'{pickup_progress:.0f}% | '
                f'Remaining Time: '
                f'{remaining_time:.1f}s'
            )

            time.sleep(
                self.publish_interval
            )

        # Final pickup feedback.
        self.publish_feedback(
            goal_handle,
            mission_start_time,
            goal.timeout,
            100.0
        )

        self.stop_robot()

        self.get_logger().info(
            'PHASE 2 COMPLETE: '
            'Package pickup completed'
        )

        # ==================================================
        # PHASE 3
        # DRIVE TO DELIVERY LOCATION
        # ==================================================

        self.get_logger().info(
            'PHASE 3 STARTED: '
            'Driving to delivery location'
        )

        phase3_start_time = (
            time.monotonic()
        )

        while True:

            # Check cancel.
            if goal_handle.is_cancel_requested:

                return self.create_cancel_result(
                    goal_handle
                )

            # Check timeout.
            if self.mission_timed_out(
                mission_start_time,
                goal.timeout
            ):

                return self.create_timeout_result(
                    goal_handle,
                    'Phase 3'
                )

            elapsed_phase3 = (
                time.monotonic()
                - phase3_start_time
            )

            if (
                elapsed_phase3
                >= goal.delivery_duration
            ):
                break

            self.velocity_publisher.publish(
                move_cmd
            )

            self.publish_feedback(
                goal_handle,
                mission_start_time,
                goal.timeout,
                100.0
            )

            self.get_logger().info(
                f'PHASE 3: Delivering package | '
                f'Elapsed: '
                f'{elapsed_phase3:.1f}s / '
                f'{goal.delivery_duration:.1f}s'
            )

            time.sleep(
                self.publish_interval
            )

        # ==================================================
        # MISSION SUCCESS
        # ==================================================

        self.stop_robot()

        self.get_logger().info(
            'PHASE 3 COMPLETE: '
            'Delivery location reached'
        )

        self.get_logger().info(
            'MISSION COMPLETED SUCCESSFULLY'
        )

        goal_handle.succeed()

        result = DeliveryMission.Result()

        result.success = True
        result.message = (
            'Delivery mission completed successfully'
        )

        return result


def main(args=None):

    rclpy.init(
        args=args
    )

    node = DeliveryMissionController()

    # Multiple threads allow cancel requests to be
    # processed while the mission is executing.
    executor = MultiThreadedExecutor(
        num_threads=2
    )

    executor.add_node(
        node
    )

    try:

        executor.spin()

    except KeyboardInterrupt:

        pass

    finally:

        # Only publish if ROS is still active.
        if rclpy.ok():
            node.stop_robot()

        executor.shutdown()

        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
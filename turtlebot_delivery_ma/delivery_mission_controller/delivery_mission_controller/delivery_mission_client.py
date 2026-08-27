#!/usr/bin/env python3

import sys
import termios
import threading
import tty

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from action_msgs.msg import GoalStatus
from delivery_mission_interfaces.action import DeliveryMission


class DeliveryMissionClient(Node):

    def __init__(self):
        super().__init__('delivery_mission_client')

        self.action_client = ActionClient(
            self,
            DeliveryMission,
            'delivery_mission'
        )

        self.goal_handle = None
        self.cancel_sent = False

    def send_goal(self):

        goal = DeliveryMission.Goal()

        goal.speed = 0.2
        goal.pickup_duration = 10.0
        goal.delivery_duration = 15.0
        goal.timeout = 40.0

        self.get_logger().info(
            'Waiting for action server...'
        )

        self.action_client.wait_for_server()

        self.get_logger().info(
            'Sending goal...'
        )

        future = self.action_client.send_goal_async(
            goal,
            feedback_callback=self.feedback_callback
        )

        future.add_done_callback(
            self.goal_response_callback
        )

    def goal_response_callback(self, future):

        self.goal_handle = future.result()

        if not self.goal_handle.accepted:

            self.get_logger().error(
                'Goal rejected'
            )

            return

        self.get_logger().info(
            'Goal accepted'
        )

        self.get_logger().info(
            'Press "c" to cancel the mission.'
        )

        keyboard_thread = threading.Thread(
            target=self.keyboard_input,
            daemon=True
        )

        keyboard_thread.start()

        result_future = (
            self.goal_handle.get_result_async()
        )

        result_future.add_done_callback(
            self.result_callback
        )

    def feedback_callback(self, feedback_msg):

        feedback = feedback_msg.feedback

        self.get_logger().info(
            f'Feedback | '
            f'Remaining time: '
            f'{feedback.remaining_time:.1f}s | '
            f'Pickup progress: '
            f'{feedback.pickup_progress:.0f}%'
        )

    def keyboard_input(self):
        """
        Listen for a single key press.

        Pressing 'c' sends a cancel request immediately
        without requiring Enter.
        """

        if not sys.stdin.isatty():

            self.get_logger().warning(
                'Keyboard input is not available.'
            )

            return

        old_settings = termios.tcgetattr(
            sys.stdin
        )

        try:

            tty.setcbreak(
                sys.stdin.fileno()
            )

            while rclpy.ok():

                key = sys.stdin.read(1).lower()

                if key == 'c':

                    self.cancel_goal()

                    break

        finally:

            termios.tcsetattr(
                sys.stdin,
                termios.TCSADRAIN,
                old_settings
            )

    def cancel_goal(self):

        if self.goal_handle is None:

            self.get_logger().warning(
                'No active mission to cancel.'
            )

            return

        if self.cancel_sent:
            return

        self.cancel_sent = True

        self.get_logger().warning(
            'Sending CANCEL request...'
        )

        future = (
            self.goal_handle.cancel_goal_async()
        )

        future.add_done_callback(
            self.cancel_response_callback
        )

    def cancel_response_callback(self, future):

        cancel_response = future.result()

        if len(cancel_response.goals_canceling) > 0:

            self.get_logger().warning(
                'Cancel request ACCEPTED'
            )

        else:

            self.get_logger().error(
                'Cancel request REJECTED'
            )

    def result_callback(self, future):

        result_response = future.result()

        result = result_response.result
        status = result_response.status

        status_names = {
            GoalStatus.STATUS_UNKNOWN: 'UNKNOWN',
            GoalStatus.STATUS_ACCEPTED: 'ACCEPTED',
            GoalStatus.STATUS_EXECUTING: 'EXECUTING',
            GoalStatus.STATUS_CANCELING: 'CANCELING',
            GoalStatus.STATUS_SUCCEEDED: 'SUCCEEDED',
            GoalStatus.STATUS_CANCELED: 'CANCELED',
            GoalStatus.STATUS_ABORTED: 'ABORTED',
        }

        status_name = status_names.get(
            status,
            'UNKNOWN'
        )

        self.get_logger().info(
            f'Result success: {result.success}'
        )

        self.get_logger().info(
            f'Result message: {result.message}'
        )

        self.get_logger().info(
            f'Goal status: {status_name}'
        )

        rclpy.shutdown()


def main(args=None):

    rclpy.init(args=args)

    node = DeliveryMissionClient()

    node.send_goal()

    try:

        rclpy.spin(node)

    except KeyboardInterrupt:

        pass

    finally:

        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
"""Run saved warehouse waypoints sequentially through Nav2."""

import math
from pathlib import Path
import signal
import time

from action_msgs.msg import GoalStatus
from nav2_msgs.action import NavigateToPose
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.signals import SignalHandlerOptions
import yaml


class WaypointRunner(Node):
    """Navigate to each waypoint and stop the mission on failure."""

    def __init__(self):
        super().__init__('waypoint_runner')
        self.declare_parameter('waypoints_file', '')
        self.stop_requested = False
        self.pending_goal = None
        self.goal_handle = None
        self.result_future = None

        filename = self.get_parameter('waypoints_file').value
        if not filename:
            raise ValueError('Set the waypoints_file parameter.')

        with Path(filename).expanduser().open(encoding='utf-8') as stream:
            data = yaml.safe_load(stream)

        if not isinstance(data, dict) or data.get('frame_id') != 'map':
            raise ValueError('Waypoint file must have frame_id: map.')

        points = data.get('waypoints')
        if not isinstance(points, list) or not points:
            raise ValueError('Waypoint list is empty or invalid.')

        self.points = []
        names = set()
        for point in points:
            if not isinstance(point, dict):
                raise ValueError('Each waypoint must be a dictionary.')
            name = point.get('name')
            if not isinstance(name, str) or not name or name in names:
                raise ValueError('Waypoint names must be nonempty and unique.')
            values = {
                key: float(point[key]) for key in ('x', 'y', 'yaw')
            }
            values['wait_seconds'] = float(point.get('wait_seconds', 3.0))
            if not all(math.isfinite(value) for value in values.values()):
                raise ValueError(f'Invalid numeric value in {name}.')
            if values['wait_seconds'] < 0:
                raise ValueError(f'Negative wait_seconds in {name}.')
            self.points.append({'name': name, **values})
            names.add(name)

        self.client = ActionClient(
            self, NavigateToPose, '/navigate_to_pose'
        )

    def wait_future(self, future, timeout=None, interruptible=True):
        """Process ROS callbacks while waiting for a future."""
        deadline = None if timeout is None else time.monotonic() + timeout
        while rclpy.ok() and not future.done():
            if interruptible and self.stop_requested:
                return False
            if deadline is not None and time.monotonic() >= deadline:
                return False
            rclpy.spin_once(self, timeout_sec=0.1)
        if not future.done():
            return False
        if interruptible and self.stop_requested:
            return False
        return True

    def run_mission(self):
        self.get_logger().info('Waiting for Nav2 /navigate_to_pose...')
        deadline = time.monotonic() + 30.0
        while not self.client.wait_for_server(timeout_sec=0.2):
            if self.stop_requested:
                return False
            if time.monotonic() >= deadline:
                self.get_logger().error('Nav2 action server is unavailable.')
                return False

        for index, point in enumerate(self.points, start=1):
            if self.stop_requested:
                return False

            goal = NavigateToPose.Goal()
            goal.pose.header.frame_id = 'map'
            goal.pose.header.stamp = self.get_clock().now().to_msg()
            goal.pose.pose.position.x = point['x']
            goal.pose.pose.position.y = point['y']
            goal.pose.pose.orientation.z = math.sin(point['yaw'] / 2.0)
            goal.pose.pose.orientation.w = math.cos(point['yaw'] / 2.0)

            self.get_logger().info(
                f"[{index}/{len(self.points)}] Going to {point['name']}"
            )
            self.pending_goal = self.client.send_goal_async(goal)
            if not self.wait_future(self.pending_goal):
                return False

            self.goal_handle = self.pending_goal.result()
            self.pending_goal = None
            if not self.goal_handle.accepted:
                self.get_logger().error(
                    f"Goal rejected: {point['name']}. Mission stopped."
                )
                self.goal_handle = None
                return False

            self.result_future = self.goal_handle.get_result_async()
            if not self.wait_future(self.result_future):
                return False

            result = self.result_future.result()
            self.goal_handle = None
            self.result_future = None

            if result.status != GoalStatus.STATUS_SUCCEEDED:
                self.get_logger().error(
                    f"Failed at {point['name']}: status={result.status}, "
                    f"error_code={getattr(result.result, 'error_code', 'unknown')}. "
                    "Mission stopped."
                )
                return False

            self.get_logger().info(
                f"Reached {point['name']}. "
                f"Waiting {point['wait_seconds']} simulation seconds."
            )
            start = self.get_clock().now().nanoseconds
            while not self.stop_requested:
                now = self.get_clock().now().nanoseconds
                if now < start:
                    self.get_logger().error(
                        'Simulation time moved backwards. Mission stopped.'
                    )
                    return False
                if (now - start) / 1e9 >= point['wait_seconds']:
                    break
                rclpy.spin_once(self, timeout_sec=0.1)

        if self.stop_requested:
            return False
        self.get_logger().info('Mission completed: all waypoints reached.')
        return True

    def cancel_current_goal(self):
        """Request cancellation and check the final action status."""
        if self.pending_goal is not None:
            if not self.wait_future(
                self.pending_goal, timeout=5.0, interruptible=False
            ):
                self.get_logger().error(
                    'Goal response unavailable; cancellation cannot be confirmed. '
                    'Check the robot in Nav2.'
                )
                return
            self.goal_handle = self.pending_goal.result()
            self.pending_goal = None

        if self.goal_handle is None or not self.goal_handle.accepted:
            return

        if self.result_future is None:
            self.result_future = self.goal_handle.get_result_async()
        if self.result_future.done():
            return

        self.get_logger().info('Requesting cancellation of the current goal...')
        cancel_future = self.goal_handle.cancel_goal_async()
        self.wait_future(cancel_future, timeout=5.0, interruptible=False)

        if self.wait_future(
            self.result_future, timeout=5.0, interruptible=False
        ):
            status = self.result_future.result().status
            if status == GoalStatus.STATUS_CANCELED:
                self.get_logger().info('Current goal canceled.')
            else:
                self.get_logger().info(f'Current goal ended: status={status}.')
        else:
            self.get_logger().error(
                'Cancellation not confirmed. Check or cancel the goal in Nav2.'
            )


def main(args=None):
    rclpy.init(args=args, signal_handler_options=SignalHandlerOptions.NO)
    node = None
    exit_code = 1
    previous_handlers = {}
    try:
        node = WaypointRunner()

        def request_stop(signum, frame):
            node.stop_requested = True

        for sig in (signal.SIGINT, signal.SIGTERM):
            previous_handlers[sig] = signal.signal(sig, request_stop)

        exit_code = 0 if node.run_mission() else 1
    except Exception as error:
        if node is not None:
            node.get_logger().error(str(error))
        else:
            print(f'Waypoint runner error: {error}')
    finally:
        if node is not None:
            try:
                node.cancel_current_goal()
            finally:
                node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
        for sig, handler in previous_handlers.items():
            signal.signal(sig, handler)
    return exit_code


if __name__ == '__main__':
    raise SystemExit(main())
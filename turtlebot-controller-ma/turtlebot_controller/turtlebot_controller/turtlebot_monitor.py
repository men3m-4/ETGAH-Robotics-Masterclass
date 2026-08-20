#!/usr/bin/env python3
"""Subscriber node: display TurtleBot3 commands received on /cmd_vel."""

# Imports the ROS 2 Python library.
import rclpy

# Imports the Twist message type used for robot movement commands.
from geometry_msgs.msg import Twist

# Imports the Node class used to create a ROS 2 node.
from rclpy.node import Node


class TurtleBotMonitor(Node):
    """ROS 2 node that listens to /cmd_vel and prints movement values."""

    def __init__(self):
        # Creates this ROS 2 node with the name turtlebot_monitor.
        super().__init__('turtlebot_monitor')

        # Subscribes to Twist messages on /cmd_vel.
        self.subscription = self.create_subscription(
            Twist,                  # Message type expected from the topic.
            '/cmd_vel',             # Topic this node listens to.
            self.command_callback,  # Function called when a message arrives.
            10                      # Queue size for incoming messages.
        )

        # Keeps the subscription stored so Python does not remove it.
        self.subscription

        # Prints a message to confirm that the monitor is ready.
        self.get_logger().info(
            'Monitoring /cmd_vel. Waiting for movement commands...'
        )

    def command_callback(self, msg):
        """Receive a Twist message and print linear.x and angular.z."""
        # Gets forward/backward speed from the received Twist message.
        linear_x = msg.linear.x

        # Gets left/right turning speed from the received Twist message.
        angular_z = msg.angular.z

        # Prints the required values in a readable format.
        self.get_logger().info(
            f'Received command -> linear.x: {linear_x:.2f} m/s | '
            f'angular.z: {angular_z:.2f} rad/s'
        )


def main(args=None):
    """Start the TurtleBot3 monitor node."""
    # Starts ROS 2 communication.
    rclpy.init(args=args)

    # Creates the subscriber node.
    node = TurtleBotMonitor()

    try:
        # Keeps the node alive to receive messages and run the callback.
        rclpy.spin(node)

    except KeyboardInterrupt:
        # Allows Ctrl+C to stop the monitor safely.
        pass

    finally:
        # Removes the node from ROS 2.
        node.destroy_node()

        # Closes ROS 2 communication.
        rclpy.shutdown()


if __name__ == '__main__':
    # Runs main() when this file is executed directly.
    main()
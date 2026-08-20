#!/usr/bin/env python3
"""Publisher node: control TurtleBot3 with W, A, S, D, and Q keys."""

# Checks whether a keyboard key is ready to be read without blocking the program.
import select

# Gives access to the terminal input through sys.stdin.
import sys

# Saves and changes Linux terminal settings for direct keyboard input.
import termios

# Runs keyboard reading separately from the ROS 2 publishing process.
import threading

# Lets the terminal receive each key immediately without pressing Enter.
import tty

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node


class TurtleBotController(Node):
    """ROS 2 node that publishes keyboard movement commands to /cmd_vel."""

    def __init__(self):
        # Create this ROS 2 node with the name turtlebot_controller.
        super().__init__('turtlebot_controller')

        # Create a publisher that sends Twist messages to TurtleBot3.
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

        # Store the current movement command; a new Twist starts with all zeros.
        self.command = Twist()

        # This becomes True when the user presses Q.
        self.exit_requested = False

        # Publish the current command every 0.1 seconds (10 times per second).
        self.timer = self.create_timer(0.1, self.publish_command)

        # Read keyboard keys in another thread so ROS 2 callbacks keep working.
        self.keyboard_thread = threading.Thread(
            target=self.read_keyboard,
            daemon=True
        )
        self.keyboard_thread.start()

        # Print the controls for the user.
        self.get_logger().info(
            'Controls: W=forward, A=left, S=backward, D=right, Q=stop and exit'
        )

    def read_keyboard(self):
        """Read one key directly from the Linux terminal without pressing Enter."""
        # Save normal terminal settings so we can restore them when the node closes.
        original_settings = termios.tcgetattr(sys.stdin)

        try:
            # Receive each key immediately instead of waiting for Enter.
            tty.setcbreak(sys.stdin.fileno())

            # Continue reading input while ROS 2 is running.
            while rclpy.ok() and not self.exit_requested:
                # Wait for a key for 0.1 seconds without blocking ROS 2.
                ready, _, _ = select.select([sys.stdin], [], [], 0.1)

                # If no key was pressed, continue waiting.
                if not ready:
                    continue

                # Read one key and convert uppercase keys to lowercase.
                key = sys.stdin.read(1).lower()

                # Convert the key into a movement command.
                self.set_command_from_key(key)

        finally:
            # Restore normal terminal behavior when the node stops.
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, original_settings)

    def set_command_from_key(self, key):
        """Create the correct Twist command for W, A, S, D, or Q."""
        # Reset all velocity values before processing the next key.
        self.command = Twist()

        if key == 'w':
            # Positive linear.x moves the robot forward.
            self.command.linear.x = 0.20
            action = 'Moving forward'

        elif key == 's':
            # Negative linear.x moves the robot backward.
            self.command.linear.x = -0.20
            action = 'Moving backward'

        elif key == 'a':
            # Positive angular.z turns the robot left.
            self.command.angular.z = 0.80
            action = 'Turning left'

        elif key == 'd':
            # Negative angular.z turns the robot right.
            self.command.angular.z = -0.80
            action = 'Turning right'

        elif key == 'q':
            # The zero Twist command stops the robot.
            self.exit_requested = True
            action = 'Stopping robot and exiting'

        else:
            # Ignore any key other than W, A, S, D, and Q.
            return

        # Print the action in the terminal.
        self.get_logger().info(action)

    def publish_command(self):
        """Publish the current Twist message to /cmd_vel."""
        # Send the current command to the TurtleBot3 velocity topic.
        self.publisher_.publish(self.command)

    def stop_robot(self):
        """Publish a final zero-velocity Twist message before exiting."""
        # A new Twist has zeros in linear.x and angular.z.
        stop_command = Twist()

        # Send stop messages multiple times so Gazebo reliably receives one.
        for _ in range(3):
            self.publisher_.publish(stop_command)


def main(args=None):
    """Start the TurtleBot3 keyboard controller node."""
    # Start ROS 2 communication.
    rclpy.init(args=args)

    # Create the publisher node.
    node = TurtleBotController()

    try:
        # Keep ROS 2 running until Q or Ctrl+C is pressed.
        while rclpy.ok() and not node.exit_requested:
            rclpy.spin_once(node, timeout_sec=0.1)

    except KeyboardInterrupt:
        # Handle Ctrl+C safely.
        node.get_logger().info('Ctrl+C received; stopping robot.')

    finally:
        # Stop TurtleBot3 before closing the node.
        node.stop_robot()

        # Remove the node from ROS 2.
        node.destroy_node()

        # Close ROS 2 communication.
        rclpy.shutdown()


if __name__ == '__main__':
    # Run main() only when this file is executed directly.
    main()
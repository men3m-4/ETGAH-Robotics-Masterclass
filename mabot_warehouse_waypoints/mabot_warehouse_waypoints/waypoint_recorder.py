"""Record RViz waypoint poses into a YAML file."""

import math
import os
from pathlib import Path
import tempfile

import rclpy
from geometry_msgs.msg import PoseStamped
from rclpy.node import Node
import yaml


class WaypointRecorder(Node):
    """Save named waypoints without sending navigation goals."""

    def __init__(self):
        super().__init__('waypoint_recorder')

        self.declare_parameter('output_file', '')
        self.declare_parameter('wait_seconds', 3.0)

        output_file = self.get_parameter('output_file').value
        if not output_file:
            raise ValueError('Set the output_file parameter.')

        self.path = Path(output_file).expanduser().resolve()
        self.wait_seconds = float(
            self.get_parameter('wait_seconds').value
        )

        if not math.isfinite(self.wait_seconds) or self.wait_seconds < 0:
            raise ValueError('wait_seconds must be finite and nonnegative.')

        self.data = {
            'frame_id': 'map',
            'waypoints': [],
        }

        # Continue an existing recording instead of overwriting it.
        if self.path.exists():
            with self.path.open('r', encoding='utf-8') as stream:
                existing = yaml.safe_load(stream)

            if (
                not isinstance(existing, dict)
                or existing.get('frame_id') != 'map'
                or not isinstance(existing.get('waypoints'), list)
                or not all(
                    isinstance(point, dict) and 'name' in point
                    for point in existing['waypoints']
                )
            ):
                raise ValueError('Existing file is not a valid waypoint list.')

            self.data = existing

        self.subscription = self.create_subscription(
            PoseStamped,
            '/waypoint_pose',
            self.record_pose,
            10,
        )

        self.get_logger().info(
            f"Recording to: {self.path}\n"
            f"Existing waypoints: {len(self.data['waypoints'])}\n"
            "Waiting for PoseStamped messages on /waypoint_pose."
        )

    def record_pose(self, message):
        if message.header.frame_id != 'map':
            self.get_logger().error(
                'Waypoint rejected: set RViz Fixed Frame to map.'
            )
            return

        position = message.pose.position
        orientation = message.pose.orientation

        values = (
            position.x, position.y,
            orientation.x, orientation.y,
            orientation.z, orientation.w,
        )
        if not all(math.isfinite(value) for value in values):
            self.get_logger().error('Waypoint rejected: invalid coordinates.')
            return

        norm = math.sqrt(
            orientation.x ** 2 + orientation.y ** 2
            + orientation.z ** 2 + orientation.w ** 2
        )
        if norm < 1e-9:
            self.get_logger().error('Waypoint rejected: invalid orientation.')
            return

        qx = orientation.x / norm
        qy = orientation.y / norm
        qz = orientation.z / norm
        qw = orientation.w / norm

        yaw = math.atan2(
            2.0 * (qw * qz + qx * qy),
            1.0 - 2.0 * (qy * qy + qz * qz),
        )

        used_names = {point['name'] for point in self.data['waypoints']}
        number = 1
        while f'station_{number:02d}' in used_names:
            number += 1

        waypoint = {
            'name': f'station_{number:02d}',
            'x': round(position.x, 4),
            'y': round(position.y, 4),
            'yaw': round(yaw, 4),
            'wait_seconds': self.wait_seconds,
        }

        updated = dict(self.data)
        updated['waypoints'] = self.data['waypoints'] + [waypoint]

        # Write beside the destination, then replace it atomically.
        temporary_path = None
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)

            with tempfile.NamedTemporaryFile(
                mode='w',
                encoding='utf-8',
                dir=self.path.parent,
                prefix='.waypoints_',
                suffix='.yaml',
                delete=False,
            ) as stream:
                temporary_path = Path(stream.name)
                yaml.safe_dump(updated, stream, sort_keys=False)
                stream.flush()
                os.fsync(stream.fileno())

            os.replace(temporary_path, self.path)

        except OSError as error:
            self.get_logger().error(f'Could not save waypoint: {error}')
            return

        finally:
            if temporary_path is not None and temporary_path.exists():
                temporary_path.unlink()

        self.data = updated
        self.get_logger().info(
            f"Saved {waypoint['name']}: "
            f"x={waypoint['x']}, y={waypoint['y']}, "
            f"yaw={waypoint['yaw']} rad"
        )


def main(args=None):
    rclpy.init(args=args)
    node = None

    try:
        node = WaypointRecorder()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if node is not None:
            node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
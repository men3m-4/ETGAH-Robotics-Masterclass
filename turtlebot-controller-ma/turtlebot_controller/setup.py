# Imports functions used to configure and install this Python package.
from setuptools import find_packages, setup

# Stores the ROS 2 package name in one variable.
package_name = 'turtlebot_controller'

# Defines how ROS 2 installs and runs this package.
setup(
    # Sets the ROS 2 package name.
    name=package_name,

    # Sets the first version of this project.
    version='0.0.1',

    # Finds the Python folder turtlebot_controller automatically.
    packages=find_packages(exclude=['test']),

    # Installs the resource marker and package.xml metadata file.
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        ('share/' + package_name, ['package.xml']),
    ],

    # Declares setuptools as a Python installation requirement.
    install_requires=['setuptools'],

    # Allows ROS 2 to install this package as a zip-safe Python package.
    zip_safe=True,

    # Replace this with your real name.
    maintainer='men3m-4',

    # Replace this with your real email address.
    maintainer_email='muhammad.abdelmoniem4@gmail.com',

    # Brief explanation of the project.
    description='TurtleBot3 keyboard controller and command monitor.',

    # States the software license.
    license='Apache-2.0',

    # Lists Python tools used if automated tests are added.
    tests_require=['pytest'],

    # Registers the commands that will work with ros2 run.
    entry_points={
        'console_scripts': [
            # ros2 run turtlebot_controller turtlebot_controller
            'turtlebot_controller = '
            'turtlebot_controller.turtlebot_controller:main',

            # ros2 run turtlebot_controller turtlebot_monitor
            'turtlebot_monitor = '
            'turtlebot_controller.turtlebot_monitor:main',
        ],
    },
)
from setuptools import find_packages, setup


package_name = 'obstacle_direction_controller'


setup(
    name=package_name,
    version='0.1.0',

    packages=find_packages(
        exclude=[
            'test',
        ]
    ),

    data_files=[
        (
            'share/ament_index/resource_index/packages',
            [
                'resource/' + package_name,
            ],
        ),
        (
            'share/' + package_name,
            [
                'package.xml',
            ],
        ),
    ],

    install_requires=[
        'setuptools',
    ],

    zip_safe=True,

    maintainer='Mohamed Abdelmoniem',
    maintainer_email='muhammad.abdelmoniem4@gmail.com',

    description=(
        'ROS 2 obstacle-avoidance controllers for TurtleBot3 '
        'and the custom MABot mobile robot.'
    ),

    license='Apache-2.0',

    extras_require={
        'test': [
            'pytest',
        ],
    },

    entry_points={
        'console_scripts': [

            # Original TurtleBot3 controller
            (
                'direction_autopilot_node = '
                'obstacle_direction_controller.'
                'direction_autopilot_node:main'
            ),

            # Improved controller designed for MABot
            (
                'mabot_autopilot_node = '
                'obstacle_direction_controller.'
                'mabot_autopilot_node:main'
            ),
        ],
    },
)
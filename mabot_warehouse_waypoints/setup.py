from glob import glob

from setuptools import find_packages, setup


package_name = 'mabot_warehouse_waypoints'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        (
            'share/' + package_name,
            ['package.xml'],
        ),
        (
            'share/' + package_name + '/config',
            glob('config/*.yaml'),
        ),
    ],
    install_requires=['setuptools', 'PyYAML'],
    zip_safe=True,
    maintainer='Mohamed Abdelmoniem',
    maintainer_email='men3m-4@users.noreply.github.com',
    description='Warehouse waypoint recording and missions for MABot.',
    license='Apache-2.0',
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'waypoint_recorder = '
            'mabot_warehouse_waypoints.waypoint_recorder:main',
            'waypoint_runner = mabot_warehouse_waypoints.waypoint_runner:main',
            'warehouse_mission = mabot_warehouse_waypoints.warehouse_mission:main',
        ],
    },
)
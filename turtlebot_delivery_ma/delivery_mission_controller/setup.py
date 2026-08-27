from setuptools import find_packages, setup

package_name = 'delivery_mission_controller'

setup(
    name=package_name,
    version='0.0.0',

    packages=find_packages(
        exclude=['test']
    ),

    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
    ],

    install_requires=[
        'setuptools'
    ],

    zip_safe=True,

    maintainer='men3m-4',
    maintainer_email='muhammad.abdelmoniem4@gmail.com',

    description=(
        'ROS 2 delivery mission controller '
        'using a custom action interface.'
    ),

    license='Apache-2.0',

    tests_require=[
        'pytest'
    ],

    entry_points={
        'console_scripts': [
            (
                'delivery_mission_node = '
                'delivery_mission_controller.'
                'delivery_mission_node:main'
            ),
            (
                'delivery_mission_client = '
                'delivery_mission_controller.'
                'delivery_mission_client:main'
            ),
        ],
    },
)
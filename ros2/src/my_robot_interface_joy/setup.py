from setuptools import find_packages, setup

package_name = 'my_robot_interface_joy'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pushpanjali',
    maintainer_email='pushpanjalijha005@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'JoyStick = my_robot_interface_joy.JoyStick:main',
        ],
    },
)

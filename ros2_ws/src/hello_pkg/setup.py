from setuptools import find_packages, setup

package_name = 'hello_pkg'

setup(
    name=package_name,
    version='0.0.0',
    # tells colcon/ament which Python packages (dirs with __init__.py) belong to this ROS2 package.
    packages=find_packages(exclude=['test']),
    data_files=[
        # registers this package with ROS2's ament resource index so tools like `ros2 pkg list` can find it.
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        # installs package.xml (name, dependencies, maintainer) alongside the built package for ROS2 tooling.
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hiba-t',
    maintainer_email='tarabayhiba05@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'publisher  = hello_pkg.publisher:main',
        'subscriber = hello_pkg.subscriber:main',
    ],
},
)

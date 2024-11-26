from setuptools import setup

setup(
    name='my_pub_sub',
    version='0.0.0',
    packages=['my_pub_sub'],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/my_pub_sub']),
        ('share/my_pub_sub', ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yahya',
    maintainer_email='your_email@example.com',
    description='A simple ROS2 publisher-subscriber package',
    license='Apache License 2.0',
    extras_require={"test": ["pytest"]},  # 'tests_require' yerine bunu kullanın
    entry_points={
        'console_scripts': [
            'publisher_node = my_pub_sub.publisher_node:main',
            'subscriber_node = my_pub_sub.subscriber_node:main',
        ],
    },
)

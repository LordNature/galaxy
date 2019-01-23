import os
from setuptools import setup, find_packages

setup(
	name='galaxy',
	version='0.1',
	long_description='galaxy is a personal website to display information.',
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	install_requires=['Flask', 'requests', 'boto3']
)

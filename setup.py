from setuptools import setup, find_packages

setup(
	name='Galaxy',
	version='1.0',
	long_description='Description',
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	install_requires=['Flask', 'requests']
)

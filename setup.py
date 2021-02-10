# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in login/__init__.py
from login import __version__ as version

setup(
	name='login',
	version=version,
	description='login page test',
	author='anjuprasannan@gmail.com',
	author_email='anjuprasannan@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

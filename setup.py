"""
setup.py
----
This is the main setup file for the hallo face animation project. It defines the package
metadata, required dependencies, and provides the entry point for installing the package.

"""

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
    ['hallo', 'hallo.datasets', 'hallo.models', 'hallo.animate', 'hallo.utils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'anna',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Anna face animation',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

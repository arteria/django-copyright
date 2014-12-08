import os
import sys
import copyright

from distutils.core import setup
from setuptools import setup, find_packages

version = copyright.__version__

setup(
    name='django-copyright',
    version=version,
    packages=find_packages(),
    license='BSD',
    description="Copyright django app",
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read().split('\n'),
    include_package_data=True,
    author="arteria GmbH",
    author_email='admin@arteria.ch',
)

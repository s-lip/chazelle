#!/usr/bin/env python
VERSION = "0.1"

from setuptools import setup, find_packages
import sys

setup(
    name="chazelle",
    version = VERSION,
    url = 'http://github.com/mysteryhunt/chazelle',
    platforms = ["any"],
    description = "MIT Mystery Hunt 2013",
    ext_modules = [],
    packages=find_packages(exclude=["tests"]),
    install_requires=['veil', 'unittest2', 'nose', 'nose-cov'],
)

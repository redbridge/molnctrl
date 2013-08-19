#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup, find_packages
from molnctrl import __version__

name = 'molnctrl'
version = __version__
requires = ['requests']

setup(name = name,
      version = version,
      description = 'A simple Cloudstack API based on Cloudmonkey',
      author='Magnus Bengtsson',
      author_email='magnus.bengtsson@redbridge.se',
      url='http://github.com/redbridge/molnctrl',
      install_requires = requires,
      packages=['molnctrl'],
     )

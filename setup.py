#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup, find_packages
from pycs import __version__

name = 'pycs'
version = __version__
requires = ['cloudmonkey>=4.0']

setup(name = name,
      version = version,
      description = 'A simple Cloudstack API based on Cloudmonkey',
      author='Magnus Bengtsson',
      author_email='magnus.bengtsson@redbridge.se',
      url='http://github/',
      install_requires = requires
      packages=['pycs'],
     )

#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup, find_packages
from molnctrl import __version__

name = 'molnctrl'
version = __version__
requires = [
    'requests',
]

setup(name = name,
      version = version,
      description = 'A simple python Cloudstack API',
      author='Magnus Bengtsson',
      author_email='magnus.bengtsson@redbridge.se',
      url='http://github.com/redbridge/molnctrl',
      install_requires = requires,
      packages=['molnctrl'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Environment :: Other Environment',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
     )

#!/usr/bin/env python
from __future__ import absolute_import
from setuptools import setup

name = 'molnctrl'
version = '0.7.9'

setup(name=name,
      version=version,
      description='A simple python Apache Cloudstack API',
      author='Magnus Bengtsson',
      author_email='magnus.bengtsson@redbridge.se',
      url='http://github.com/redbridge/molnctrl',
      install_requires=[
          'requests',
          'six',
          'future',
      ],
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

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ])

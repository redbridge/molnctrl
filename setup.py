#!/usr/bin/env python
from setuptools import setup, find_packages

name = 'molnctrl'
version = '0.6.0'

setup(name = name,
      version = version,
      description = 'A simple python Apache Cloudstack API',
      author='Magnus Bengtsson',
      author_email='magnus.bengtsson@redbridge.se',
      url='http://github.com/redbridge/molnctrl',
      install_requires = [
        'requests',
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
          ],
     )

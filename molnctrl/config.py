#!/usr/bin/env python
# −*− coding: UTF−8 −*−
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
"""

from __future__ import absolute_import
import os
import six.moves.configparser

class Config(object):
    """ Provides config file support
    """
    def __init__(self):
        config_file = os.getenv('MOLN_CONF', '.moln.conf')
        for loc in os.curdir, os.path.expanduser("~"), os.environ.get('PWD'), '':
            if if loc and os.path.exists(os.path.join(loc,config_file)):
                try:
                    config = six.moves.configparser.ConfigParser()
                    config.read(os.path.join(loc,config_file))
                    return config
                except IOError:
                    config = None
                    return config


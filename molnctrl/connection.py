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
from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
import string, base64, urllib.request, urllib.parse, urllib.error, json, urllib.request, urllib.parse, urllib.error, sys
import requests
from . import csobjects
from .csexceptions import *
from .apisigner import SignedAPICall
import six


class CSApi(SignedAPICall):
    def __init__(self, api_url, api_key, api_secret, asyncblock, timeout=10, req_method="get"):
        super(CSApi, self).__init__(api_url, api_key, api_secret, asyncblock, timeout, req_method)

    def __repr__(self):
        return '<molnctrl: {0} [{1}]>'.format(self.api_url, self.req_method)

    def _make_request(self, command, args):
        args['response'] = 'json'
        args['command'] = command
        # Support tags like ...,tags={'key': 'value', 'key2': 'value2'}
        if 'tags' in args:
            if isinstance(args['tags'], dict):
                i = 0
                for k,v in six.iteritems(args['tags']):
                    args['tags[%i].key' % i] = k
                    args['tags[%s].value' % i] = v
                    i += 1
            args.pop('tags')
        data = self.request(args)
        data = data.json()
        # The response is of the format {commandresponse: actual-data}
        key = command.lower().strip('_') + "response"
        if 'errorresponse' in data:
            if 'errorresponse' in data:
                raise ResponseError(data['errorresponse']['errorcode'], data['errorresponse']['errortext'])
        elif key in data and 'errorcode' in data[key]:
            raise ResponseError(data[key]['errorcode'], data[key]['errortext'])
        try:
            return self._ret(data[key])
        except Exception as e:
            print("%s" % e)
            raise Error()

    def _ret(self, ret):
        # Then create a list of classes
        list_ret = []
        for key in list(ret.keys()):
            if not key == 'count':
                if key == 'success':
                    if ret['success'] == 'true':
                        return True
                    else:
                        return False
                elif 'jobid' in ret:
                    # This is a async call....
                    # Should return a async object that can be checked or (re-)created
                    # or, if requested, block on async, self.asyncblock
                    ret['_cs_api'] = self
                    return getattr(csobjects, 'AsyncJob')(ret)
                elif isinstance(ret[key], list):
                    for item in ret[key]:
                        # Add the API connection to the object
                        try:
                            item['_cs_api'] = self
                            list_ret.append(getattr(csobjects, key.capitalize())(item))
                        except:
                            if 'jobid' in ret:
                                return getattr(csobjects, 'AsyncJob')(ret) 
                            else:
                                return ret
                elif isinstance(ret[key], dict):
                    try:
                        ret[key]['_cs_api'] = self
                        return getattr(csobjects, key.capitalize())(ret[key]) 
                    except Exception as e:
                        return ret
        return list_ret

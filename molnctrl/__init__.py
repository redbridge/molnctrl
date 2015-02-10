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
import os, pickle, tempfile
import cachemaker
from connection import CSApi
from config import Config
#
# usage:
# In [1]: import molnctrl
# In [2]: csapi = molnctrl.Initialize("apikey", "api_secret", api_host='cloud.fqdn')
# In [3]: accounts = csapi.list_accounts()
# In [4]: len(accounts)
# Out[4]: 1
# In [5]: accounts
# Out[5]: [<class 'molnctrl.csobjects.Account'> admin]
#
#
def _add_params_docstring(params):
    """ Add params to doc string
    """
    p_string = "\nAccepts the following paramters: \n"
    for param in params:
         p_string += "name: %s, required: %s, description: %s \n" % (param['name'], param['required'], param['description'])
    return p_string

def _create_api_method(cls, name, api_method):
    """ Create dynamic class methods based on the Cloudmonkey precached_verbs
    """
    def _api_method(self, **kwargs):
        # lookup the command
        command = api_method['name']
        if kwargs:
            return self._make_request(command, kwargs)
        else:
            kwargs = {}
            return self._make_request(command, kwargs)
    _api_method.__doc__ = api_method['description']
    _api_method.__doc__ += _add_params_docstring(api_method['params'])
    _api_method.__name__ = str(name)
    setattr(cls, _api_method.__name__, _api_method)


def Initialize(api_key, api_secret, api_host="localhost", api_port=443, api_ssl=True, asyncblock=False, timeout=10, req_method="get"):
    """ Initializes the Cloudstack API
        Accepts arguments: 
            api_host (localhost)
            api_port (443)
            api_ssl (True)
            api_key
            api_secret
    """
    config = Config()

    if api_ssl:
        proto = "https"
    else:
        proto = "http"
    api_url = "%s://%s:%s/client/api" % (proto, api_host, api_port)
    try:
        if os.access(os.path.expanduser("~") , os.W_OK):
            d = os.path.expanduser("~")
        else:
            d = tempfile.gettempdir()
        cache_file = os.getenv('MOLNCTRL_CACHE') or '.molnctrl_cache'
        if os.path.exists(os.path.join(d, cache_file)):
            apicache = pickle.load(open( os.path.join(d, cache_file), "rb" ))
        else:
            method = {'description': u'lists all available apis on the server, provided by the Api Discovery plugin',
             'isasync': False,
             'name': u'listApis',
             'params': [{'description': u'API name',
               'length': 255,
               'name': u'name',
               'related': [],
               'required': False,
               'type': u'string'}],
             'related': [],
             'requiredparams': []}
            _create_api_method(CSApi, "list_apis", method)
            c = CSApi(api_url, api_key, api_secret, asyncblock)
            apicache = cachemaker.monkeycache(c.list_apis())
            pickle.dump(apicache, open(os.path.join(d, cache_file), "wb"))
    except Exception as e:
        print "Unable to create an api cache: %s" % e

    for verb, methods in apicache.iteritems():
        if isinstance(methods, dict):
            for method in methods.iterkeys():
                _create_api_method(CSApi, "%s_%s" % (verb, method), methods[method])
    return CSApi(api_url, api_key, api_secret, asyncblock, timeout, req_method)

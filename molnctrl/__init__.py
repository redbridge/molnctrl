#!/usr/bin/env python
# −*− coding: UTF−8 −*−
import os, pickle
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
__version__ = "0.4"

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


def Initialize(api_key, api_secret, api_host="localhost", api_port=443, api_ssl=True, asyncblock=False):
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
        home = os.path.expanduser("~")
        if os.path.exists(os.path.join(home, '.molnctrl_cache')):
            apicache = pickle.load(open( os.path.join(home, '.molnctrl_cache'), "rb" ))
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
            pickle.dump(apicache, open(os.path.join(home, '.molnctrl_cache'), "wb"))
    except Exception as e:
        pass

    for verb, methods in apicache.iteritems():
        if isinstance(methods, dict):
            for method in methods.iterkeys():
                _create_api_method(CSApi, "%s_%s" % (verb, method), methods[method])
    return CSApi(api_url, api_key, api_secret, asyncblock)

#!/usr/bin/env python
# −*− coding: UTF−8 −*−
from cloudmonkey.precache import precached_verbs
from connection import CSApi
#
# usage:
# import molnctrl
# cs = molnctrl.Initialize("apikey", "api_secret")
#
#
__version__ = "0.1"

def _create_api_method(cls, name, api_method):
    """ Create dynamic class methods based on the Cloudmonkey precached_verbs
    """
    def _api_method(self, **kwargs):
        # lookup the command
        command = api_method[0]
        if kwargs:
            return self._make_request(command, kwargs)
        else:
            kwargs = {}
            return self._make_request(command, kwargs)
    _api_method.__doc__ = api_method[2]
    _api_method.__name__ = name
    setattr(cls, _api_method.__name__, _api_method)


def Initialize(api_key, api_secret, api_host="localhost", api_port=443, api_ssl=True):
    """ Initializes the Cloudstack API
        Accepts arguments: 
            api_host (localhost)
            api_port (443)
            api_ssl (True)
            api_key
            api_secret
    """
    if api_ssl:
        proto = "https"
    else:
        proto = "http"
    api_url = "%s://%s:%s/client/api" % (proto, api_host, api_port)
    for verb, methods in precached_verbs.iteritems():
        for method in methods:
           _create_api_method(CSApi, "%s_%s" % (verb, method), methods[method])
    return CSApi(api_url, api_key, api_secret)

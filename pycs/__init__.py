from cloudmonkey.precache import precached_verbs
from connection import CSApi

__version__ = "0.1"

def _create_api_method(cls, name, api_method):
    """ Create dynamic class methods based on the Cloudmonkey precached_verbs
    """
    def _api_method(self, *args, **kwargs):
        # lookup the command
        print api_method
        command = "dummyCommand"
        if kwargs:
            return self._make_request(command, kwargs)
        return self._make_request(command)
    _api_method.__doc__ = api_method[2]
    _api_method.__name__ = name
    setattr(cls, _api_method.__name__, _api_method)


def initialize(api_host, api_key, api_secret):
    for verb, methods in precached_verbs.iteritems():
        for method in methods:
           _create_api_method(CSApi, "%s_%s" % (verb, method), methods[method])
    return CSApi(api_host, api_key, api_secret)

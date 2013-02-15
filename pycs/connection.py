#!/ usr/bin/env python
import string, base64, urllib, json, urllib
from cloudmonkey.precache import precached_verbs
from apisigner import SignedAPICall

class CSApi(SignedAPICall):
    def __init__(self, api_url, api_key, api_secret):
        super(CSApi, self).__init__(api_url, api_key, api_secret)
        #self._create_api(precached_verbs)

    def _create_api(self, api_dict):
        """ Create dynamic class methods based on the Cloudmonkey precached_verbs
        """
        for verb, methods in api_dict.iteritems():
            for method in methods:
                def _api_method(self, **kwargs):
                    # lookup the command
                    command_lookup = _api_method.__name__.split('_')
                    print command_lookup
                    command = command_lookup[0]
                    return self._make_request(command, kwargs) 
                _api_method.__doc__ = methods[method][2]
                setattr(self.__class__, "%s_%s" % (verb, method), _api_method)

    def _http_get(self):
        response = urllib.urlopen(self.value)
        return response.read()

    def _make_request(self, command, args):
        args['response'] = 'json'
        args['command'] = command
        self.request(args)
        data = self._http_get()
        print data
        # The response is of the format {commandresponse: actual-data}
        key = command.lower() + "response"
        return json.loads(data)[key]

#Usage

#api = CloudStack(api_url, apiKey, secret)

#request = {'listall': 'true'}
#result = api.listVirtualMachines(request)
#print "count", result['count']
#print "api url", api.value
    

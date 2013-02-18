#!/ usr/bin/env python
import string, base64, urllib, json, urllib
from cloudmonkey.precache import precached_verbs
from apisigner import SignedAPICall

class CSApi(SignedAPICall):
    def __init__(self, api_url, api_key, api_secret):
        super(CSApi, self).__init__(api_url, api_key, api_secret)

    def _http_get(self):
        response = urllib.urlopen(self.value)
        return response.read()

    def _make_request(self, command, args):
        args['response'] = 'json'
        args['command'] = command
        self.request(args)
        data = self._http_get()
        # The response is of the format {commandresponse: actual-data}
        key = command.lower() + "response"
        return self._ret(json.loads(data)[key])

    def _ret(self, ret):
        if "account" in ret.keys():
            return Account(ret['account'][0])

class Account(object):
    def __init__(self, dictionary):
        for k,v in dictionary.items():
            setattr(self, k, v)

#!/ usr/bin/env python
import string, base64, urllib, json, urllib, sys
from cloudmonkey.precache import precached_verbs
import csobjects
from csexceptions import *
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
        key = command.lower().strip('_') + "response"
        data = json.loads(data)
        if data.has_key('errorresponse'):
            raise ResponseError(data['errorresponse']['errorcode'], data['errorresponse']['errortext'])
        try:
            return self._ret(data[key])
        except:
            print data
            raise Error()

    def _ret(self, ret):
        # Then create a list of classes
        list_ret = []
        for key in ret.keys():
            if not key == 'count':
                if key == 'success':
                    if ret['success'] == 'true':
                        return True
                    else:
                        return False
                else:
                    for item in ret[key]:
                        # Add the API connection to the object
                        #try:
                        item['_cs_api'] = self
                        list_ret.append(getattr(csobjects, key.capitalize())(item))
                        #except:
                        #    return ret
        return list_ret

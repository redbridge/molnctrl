#!/ usr/bin/env python
import string, base64, urllib, json, urllib, sys
import requests
from cache410 import apicache
import csobjects
from csexceptions import *
from apisigner import SignedAPICall


class CSApi(SignedAPICall):
    def __init__(self, api_url, api_key, api_secret):
        super(CSApi, self).__init__(api_url, api_key, api_secret)


    def _make_request(self, command, args):
        args['response'] = 'json'
        args['command'] = command
        data = self.request(args)
        data = data.json()
        # The response is of the format {commandresponse: actual-data}
        key = command.lower().strip('_') + "response"
        if data.has_key('errorresponse'):
            if data.has_key('errorresponse'):
                raise ResponseError(data['errorresponse']['errorcode'], data['errorresponse']['errortext'])
        elif data.has_key(key) and data[key].has_key('errorcode'):
            raise ResponseError(data[key]['errorcode'], data[key]['errortext'])
        try:
            return self._ret(data[key])
        except Exception as e:
            print "%s" % e
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
                elif key == 'jobid':
                    # This is a async call....
                    # Should return a async object that can be checked or (re-)created
                    ret['_cs_api'] = self
                    return getattr(csobjects, 'AsyncJob')(ret)
                elif isinstance(ret[key], list):
                    for item in ret[key]:
                        # Add the API connection to the object
                        try:
                            item['_cs_api'] = self
                            list_ret.append(getattr(csobjects, key.capitalize())(item))
                        except:
                            return ret

                else:
                    return ret
        return list_ret

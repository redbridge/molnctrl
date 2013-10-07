#!/ usr/bin/env python
# By: Kelcey Damage, 2012 & Kraig Amador, 2012
import hashlib, hmac, string, base64, urllib
import requests
import json, urllib


class SignedAPICall(object):
    def __init__(self, api_url, api_key, api_secret, asyncblock):
        self.api_url = api_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.asyncblock = asyncblock

    def remove_non_ascii(self, s): 
        return "".join(i for i in s if ord(i)<128)

    def request(self, args):
        args['apiKey'] = self.api_key
        for k, v in args.iteritems():
            args[k] = self.remove_non_ascii(v)
        self._sign(args)
        self._build_post_request(args)
        return self._http_get()

    def _sign(self, args):
        params = zip(args.keys(), args.values())
        params.sort(key=lambda k: str.lower(k[0]))
        hash_str = "&".join(
                    ["=".join(
                        [str.lower(r[0]),
                         str.lower(
                                urllib.quote_plus(str(r[1]))
                         ).replace("+", "%20")]
                    ) for r in params]
        )
        signature = base64.encodestring(hmac.new(self.api_secret, 
                                                 hash_str, 
                                                 hashlib.sha1).digest()).strip()
        self.signature = signature

    def _http_get(self):
        response = requests.get(self.api_url, params=self.query, verify=False)
        return response


    def _build_post_request(self, args):
        args['signature'] = self.signature
        self.query = args

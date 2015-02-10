#!/ usr/bin/env python
# Derived from: Kelcey Damage, 2012 & Kraig Amador, 2012
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
import hashlib, hmac, string, base64, urllib
import requests
import json, urllib


class SignedAPICall(object):
    def __init__(self, api_url, api_key, api_secret, asyncblock, timeout=10, req_method="get"):
        self.api_url = api_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.asyncblock = asyncblock
        self.timeout = timeout
        self.req_method = req_method.lower()

    def remove_non_ascii(self, s):
        return "".join(i for i in s if ord(i)<128)

    def request(self, args):
        args['apiKey'] = self.api_key
        for k, v in args.iteritems():
            args[k] = self.remove_non_ascii(v)
        self._sign(args)
        self._build_post_request(args)
        if self.req_method == 'get':
            return self._http_get()
        else:
            return self._http_post()

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
        response = requests.get(self.api_url, params=self.query)
        return response

    def _http_post(self):
        response = requests.post(self.api_url, data=self.query)
        return response


    def _build_post_request(self, args):
        args['signature'] = self.signature
        self.query = args

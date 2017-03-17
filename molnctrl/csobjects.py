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
from __future__ import absolute_import
from builtins import object
import sys, time
from .csexceptions import *

class CloudStackObject(object):
    def __init__(self, dictionary):
        for k,v in list(dictionary.items()):
            setattr(self, k, v)

    def __str__(self):
        return "%s %s" % (self.__class__, self.name)

    def __repr__(self):
        return "%s %s" % (self.__class__, self.name)


class Account(CloudStackObject):
    def __init__(self, dictionary):
        for k,v in list(dictionary.items()):
            setattr(self, k, v)
        self.users = self._get_users(self.user)

    def _get_users(self, users):
        user_list = []
        for user in users:
            user_list.append(getattr(sys.modules[__name__], 'User')(user))
        return user_list

class User(CloudStackObject):
    def __str__(self):
        return "%s %s" % (self.__class__, self.username)

    def __repr__(self):
        return "%s %s" % (self.__class__, self.username)


class Template(CloudStackObject):
    pass

class Keypair(CloudStackObject):
    pass

class Sshkeypair(CloudStackObject):
    pass

class Zone(CloudStackObject):
    pass

class Iso(CloudStackObject):
    pass

class Instancegroup(CloudStackObject):
    pass

class Router(CloudStackObject):
    pass

class Networkoffering(CloudStackObject):
    pass

class Keypair(CloudStackObject):
    pass

class Vpc(CloudStackObject):
    pass

class Volume(CloudStackObject):
    pass

class Remoteaccessvpn(CloudStackObject):
    def __str__(self):
        return "%s %s" % (self.__class__, self.publicip)

    def __repr__(self):
        return "%s %s" % (self.__class__, self.publicip)

class Vpnuser(CloudStackObject):
    def __str__(self):
        return "%s %s" % (self.__class__, self.username)

    def __repr__(self):
        return "%s %s" % (self.__class__, self.username)

class Virtualmachine(CloudStackObject):
    """ This class represents a virtual machine"""
    def __init__(self, dictionary):
        for k,v in list(dictionary.items()):
            setattr(self, k, v)
        self.nics = self._get_nics(self.nic)
        self.tags = self._get_tags(self.tags)

    def _get_nics(self, nics):
        nic_list = []
        for nic in nics:
            nic_list.append(getattr(sys.modules[__name__], 'Nic')(nic))
        return nic_list

    def _get_tags(self, tags):
        tag_list = []
        for tag in tags:
            tag_list.append(getattr(sys.modules[__name__], 'Tag')(tag))
        return tag_list


    def start(self):
        self.update()
        if not self.is_running:
            obj = self._cs_api.start_virtualmachine(id=self.id)
            return obj
        else:
            return False

    def stop(self):
        self.update()
        if self.is_running:
            obj = self._cs_api.stop_virtualmachine(id=self.id)
            return obj
        else:
            return False

    def destroy(self):
        self.update()
        if self.is_running:
            raise VirtualMachineError("Cannot destroy a running vm")
        else:
            self._cs_api.destroy_virtualmachine(id=self.id)
            return True

    @property
    def ostype(self):
        ostype = self._cs_api.list_ostypes(id=self.guestosid)
        return ostype[0].description

    def update(self):
        """ Update the state """
        vm = self._cs_api.list_virtualmachines(id=self.id)[0]
        self.is_running = self._is_running(vm.state)

    def _is_running(self, state):
        #self.update()
        if state == "Running":
            self.state = 'Running'
            return True
        else:
            return False

class Ostype(CloudStackObject):
    def __str__(self):
        return repr("%s:%s" % (self.__class__, self.description))
    def __repr__(self):
        return repr("%s:%s" % (self.__class__, self.description))

class Template(CloudStackObject):
    pass

class Network(CloudStackObject):
    def __init__(self, dictionary):
        for k,v in list(dictionary.items()):
            setattr(self, k, v)
        self.services = self._get_services(self.service)

    def _get_services(self, services):
        service_list = []
        for service in services:
            service_list.append(getattr(sys.modules[__name__], 'Service')(service))
        return service_list

class Service(CloudStackObject):
    def __init__(self, dictionary):
        for k,v in list(dictionary.items()):
            setattr(self, k, v)
        try:
            self.capabilities = self._get_capabilities(self.capability)
        except:
            pass

    def _get_capabilities(self, capabilities):
        capability_list = []
        for capability in capabilities:
            capability_list.append(getattr(sys.modules[__name__], 'Capability')(capability))
        return capbility_list

class Capability(CloudStackObject):
    pass

class Nic(CloudStackObject):
    def __str__(self):
        return repr("%s:%s" % (self.__class__, self.ipaddress))

    def __repr__(self):
        return "%s %s" % (self.__class__, self.ipaddress)

class Domain(CloudStackObject):
    pass

class Serviceoffering(CloudStackObject):
    pass

class Loadbalancerrule(CloudStackObject):
    pass

class Portforwardingrule(CloudStackObject):
    def __str__(self):
        return repr("%s:%s" % (self.__class__, self.ipaddress))

    def __repr__(self):
        return "%s %s" % (self.__class__, self.ipaddress)

class Tag(CloudStackObject):
    def __str__(self):
        return repr("%s:%s" % (self.__class__, self.key))

    def __repr__(self):
        return "%s %s" % (self.__class__, self.key)

class Publicipaddress(CloudStackObject):
    def __str__(self):
        return repr("%s:%s" % (self.__class__, self.ipaddress))

    def __repr__(self):
        return "%s %s" % (self.__class__, self.ipaddress)

class Firewallrule(CloudStackObject):
    def __str__(self):
        return repr("%s:%s" % (self.__class__, self.ipaddress))

    def __repr__(self):
        return "%s %s:%s" % (self.__class__, self.ipaddress, self.startport)

class Ipaddress(CloudStackObject):
    def __str__(self):
        return repr("%s:%s" % (self.__class__, self.ipaddress))

    def __repr__(self):
        return "%s %s" % (self.__class__, self.ipaddress)


class AsyncJob(CloudStackObject):
    def __init__(self, dictionary):
        for k,v in list(dictionary.items()):
            setattr(self, k, v)

    def __str__(self):
        return repr("%s:%s" % (self.__class__, self.jobid))

    def __repr__(self):
        return "%s %s" % (self.__class__, self.jobid)

    def get_result(self):
        while True:
            status = self.status
            if status == 'succeded':
                try:
                    list(self.result.values())[0]['_cs_api'] = self._cs_api
                    return getattr(sys.modules[__name__], list(self.result.keys())[0].capitalize())(list(self.result.values())[0])
                except:
                    return status
            elif status == 'pending':
                time.sleep(2)
            elif status == 'failed':
                return False
            else:
                return False
    @property
    def status(self):
        async_status = self._cs_api.query_asyncjobresult(jobid=self.jobid)
        jobstatus = async_status.jobstatus
        if jobstatus == 0:
            return 'pending'
        elif jobstatus == 1:
            self.result = async_status.jobresult
            return 'succeded'
        elif jobstatus == 2:
            self.result = async_status.jobresult
            return 'failed'
        else:
            return 'unknown'

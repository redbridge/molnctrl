#!/usr/bin/env python
# −*− coding: UTF−8 −*−
import sys, time
from exceptions import *

class CloudStackObject(object):
    def __init__(self, dictionary):
        for k,v in dictionary.items():
            setattr(self, k, v)

    def __str__(self):
        return "%s %s" % (self.__class__, self.name)

    def __repr__(self):
        return "%s %s" % (self.__class__, self.name)


class Account(CloudStackObject):
    def __init__(self, dictionary):
        for k,v in dictionary.items():
            setattr(self, k, v)
        self.users = self._get_users(self.user)

    def _get_users(self, users):
        user_list = []
        for user in users:
            user_list.append(getattr(sys.modules[__name__], 'User')(user))
        return user_list

class User(CloudStackObject):
    pass
    
class Template(CloudStackObject):
    pass

class Keypair(CloudStackObject):
    pass

class Sshkeypair(CloudStackObject):
    pass

class Zone(CloudStackObject):
    pass

class Virtualmachine(CloudStackObject):
    """ This class represents a virtual machine"""
    def __init__(self, dictionary):
        for k,v in dictionary.items():
            setattr(self, k, v)
        self.nics = self._get_nics(self.nic)

    def _get_nics(self, nics):
        nic_list = []
        for nic in nics:
            nic_list.append(getattr(sys.modules[__name__], 'Nic')(nic))
        return nic_list

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
    pass
    
class Template(CloudStackObject):
    pass
    
class Network(CloudStackObject):
    def __init__(self, dictionary):
        for k,v in dictionary.items():
            setattr(self, k, v)
        self.services = self._get_services(self.service)

    def _get_services(self, services):
        service_list = []
        for service in services:
            service_list.append(getattr(sys.modules[__name__], 'Service')(service))
        return service_list

class Service(CloudStackObject):
    def __init__(self, dictionary):
        for k,v in dictionary.items():
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
    pass

class Domain(CloudStackObject):
    pass

class Serviceoffering(CloudStackObject):
    pass

class Publicipaddress(CloudStackObject):
    pass

class AsyncJob(CloudStackObject):
    def __init__(self, dictionary):
        for k,v in dictionary.items():
            setattr(self, k, v)

    def __str__(self):
        return repr("%s:%s" % (self.__class__, self.jobid))

    def get_result(self):
        while True:
            status = self.status
            if status == 'succeded':
                try:
                    self.result.values()[0]['_cs_api'] = self._cs_api
                    return getattr(sys.modules[__name__], self.result.keys()[0].capitalize())(self.result.values()[0])
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

#!/usr/bin/env python
# −*− coding: UTF−8 −*−
import sys, time
from exceptions import *

class Account(object):
    def __init__(self, dictionary):
        for k,v in dictionary.items():
            setattr(self, k, v)
        self.users = self._get_users(self.user)

    def __str__(self):
        return "%s %s" % (self.__class__, self.name)

    def __repr__(self):
        return "%s %s" % (self.__class__, self.name)

    def _get_users(self, users):
        user_list = []
        for user in users:
            user_list.append(getattr(sys.modules[__name__], 'User')(user))
        return user_list

class User(object):
    def __init__(self, dictionary):
        for k,v in dictionary.items():
            setattr(self, k, v)

    def __str__(self):
        return "%s %s" % (self.__class__, self.username)

    def __repr__(self):
        return "%s %s" % (self.__class__, self.username)

class Template(object):
    def __init__(self, dictionary):
        for k,v in dictionary.items():
            setattr(self, k, v)

    def __str__(self):
        return "%s %s" % (self.__class__, self.name)

    def __repr__(self):
        return "%s %s" % (self.__class__, self.name)

class Keypair(object):
    def __init__(self, dictionary):
        for k,v in dictionary.items():
            setattr(self, k, v)

    def __str__(self):
        return "%s %s" % (self.__class__, self.name)

    def __repr__(self):
        return "%s %s" % (self.__class__, self.name)

class Sshkeypair(object):
    def __init__(self, dictionary):
        for k,v in dictionary.items():
            setattr(self, k, v)

    def __str__(self):
        return repr("%s:%s" % (self.__class__, self.name))

class Zone(object):
    def __init__(self, dictionary):
        for k,v in dictionary.items():
            setattr(self, k, v)

    def __str__(self):
        return repr("%s:%s" % (self.__class__, self.name))

class Virtualmachine(object):
    """ This class represents a virtual machine"""
    def __init__(self, dictionary):
        for k,v in dictionary.items():
            setattr(self, k, v)
        #self.is_running = self._is_running(self.state)

    def __str__(self):
        return "%s %s" % (self.__class__, self.instancename)

    def __repr__(self):
        return "%s %s" % (self.__class__, self.instancename)

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

class Ostype(object):
    def __init__(self, dictionary):
        for k,v in dictionary.items():
            setattr(self, k, v)

    def __str__(self):
        return repr("%s:%s" % (self.__class__, self.description))

class Template(object):
    def __init__(self, dictionary):
        for k,v in dictionary.items():
            setattr(self, k, v)

    def __str__(self):
        return repr("%s:%s" % (self.__class__, self.name))

class AsyncJob(object):
    def __init__(self, dictionary):
        for k,v in dictionary.items():
            setattr(self, k, v)

    def __str__(self):
        return repr("%s:%s" % (self.__class__, self.jobid))
    
    def get_result(self):
        while True:
            status = self.status
            if status == 'succeded':
                return getattr(sys.modules[__name__], self.result.keys()[0].capitalize())(self.result.values()[0])
            elif status == 'pending':
                time.sleep(2)
            elif status == 'failed':
                return False
            else:
                return False
    @property
    def status(self):
        async_status = self._cs_api.query_asyncjobresult(jobid=self.jobid)
        #jobstatus = async_status['jobstatus']
        jobstatus = async_status.jobstatus
        if jobstatus == 0:
            return 'pending'
        elif jobstatus == 1:
            self.result = async_status.jobresult
            #return getattr(sys.modules[__name__], self.result.keys()[0].capitalize())(self.result.values()[0])
            return 'succeded'
        elif jobstatus == 2:
            self.result = async_status.jobresult
            return 'failed'
        else:
            return 'unknown'

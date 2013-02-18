#!/usr/bin/env python
# −*− coding: UTF−8 −*−    
class Error(Exception):
    pass

class ResponseError(Error):
    def __init_(self, errorcode, errortext):
        self.errorcode = errorcode
        self.errortext = errortext

    
class VirtualMachineError(Error):
    def __init_(self, reason):
        self.reason = reason 
    def __str__(self):
       return "%s %s" % (self.__class__, self.reason)
    def __repr__(self):
       return "%s %s" % (self.__class__, self.reason)
    
    
    
    
    
    
    
    
    


    
    
    
    
    
    

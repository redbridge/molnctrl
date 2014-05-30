apicache = {
  "authorize": {
    "securitygroupingress": {
      "name": "authorizeSecurityGroupIngress",
      "related": [
        "authorizeSecurityGroupEgress"
      ],
      "isasync": True,
      "params": [
        {
          "name": "cidrlist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "the cidr list associated"
        },
        {
          "name": "endport",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "end port for this ingress rule"
        },
        {
          "name": "usersecuritygrouplist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "user to security group mapping"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional domainId for the security group. If the account parameter is used, domainId must also be used."
        },
        {
          "name": "securitygroupname",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The name of the security group. Mutually exclusive with securityGroupName parameter"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "an optional account for the security group. Must be used with domainId."
        },
        {
          "name": "protocol",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "TCP is default. UDP is the other supported protocol"
        },
        {
          "name": "startport",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "start port for this ingress rule"
        },
        {
          "name": "icmpcode",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "error code for this icmp message"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "activateProject",
            "listProjects",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional project of the security group"
        },
        {
          "name": "securitygroupid",
          "required": False,
          "related": [
            "createSecurityGroup",
            "listSecurityGroups"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the security group. Mutually exclusive with securityGroupName parameter"
        },
        {
          "name": "icmptype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "type of the icmp message being sent"
        }
      ],
      "requiredparams": [],
      "description": "Authorizes a particular ingress rule for this security group"
    },
    "securitygroupegress": {
      "name": "authorizeSecurityGroupEgress",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "usersecuritygrouplist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "user to security group mapping"
        },
        {
          "name": "securitygroupid",
          "required": False,
          "related": [
            "listSecurityGroups"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the security group. Mutually exclusive with securityGroupName parameter"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional project of the security group"
        },
        {
          "name": "icmptype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "type of the icmp message being sent"
        },
        {
          "name": "icmpcode",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "error code for this icmp message"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional domainId for the security group. If the account parameter is used, domainId must also be used."
        },
        {
          "name": "endport",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "end port for this egress rule"
        },
        {
          "name": "startport",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "start port for this egress rule"
        },
        {
          "name": "cidrlist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "the cidr list associated"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "an optional account for the security group. Must be used with domainId."
        },
        {
          "name": "protocol",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "TCP is default. UDP is the other supported protocol"
        },
        {
          "name": "securitygroupname",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The name of the security group. Mutually exclusive with securityGroupName parameter"
        }
      ],
      "requiredparams": [],
      "description": "Authorizes a particular egress rule for this security group"
    }
  },
  "restore": {
    "virtualmachine": {
      "name": "restoreVirtualMachine",
      "related": [
        "migrateVirtualMachineWithVolume",
        "stopVirtualMachine",
        "revertToVMSnapshot",
        "listVirtualMachines",
        "destroyVirtualMachine"
      ],
      "isasync": True,
      "params": [
        {
          "name": "templateid",
          "required": False,
          "related": [
            "listIsos",
            "copyIso",
            "updateIso"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional template Id to restore vm from the new template. This can be an ISO id in case of restore vm deployed using ISO"
        },
        {
          "name": "virtualmachineid",
          "required": True,
          "related": [
            "migrateVirtualMachineWithVolume",
            "stopVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Virtual Machine ID"
        }
      ],
      "requiredparams": [
        "virtualmachineid"
      ],
      "description": "Restore a VM to original template/ISO or new template/ISO"
    }
  },
  "suspend": {
    "project": {
      "name": "suspendProject",
      "related": [
        "createProject",
        "activateProject",
        "listProjects",
        "listProjectAccounts",
        "updateProject"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "createProject",
            "activateProject",
            "listProjects",
            "suspendProject",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of the project to be suspended"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Suspends a project"
    }
  },
  "revoke": {
    "securitygroupingress": {
      "name": "revokeSecurityGroupIngress",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the ingress rule"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a particular ingress rule from this security group"
    },
    "securitygroupegress": {
      "name": "revokeSecurityGroupEgress",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "authorizeSecurityGroupEgress"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the egress rule"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a particular egress rule from this security group"
    }
  },
  "disassociate": {
    "ipaddress": {
      "name": "disassociateIpAddress",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "associateIpAddress"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the id of the public ip address to disassociate"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Disassociates an ip address from the account."
    },
    "ucsprofilefromblade": {
      "name": "disassociateUcsProfileFromBlade",
      "related": [
        "listUcsBlades",
        "instantiateUcsTemplateAndAssocaciateToBlade",
        "refreshUcsBlades"
      ],
      "isasync": True,
      "params": [
        {
          "name": "deleteprofile",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "is deleting profile after disassociating"
        },
        {
          "name": "bladeid",
          "required": True,
          "related": [
            "listUcsBlades",
            "disassociateUcsProfileFromBlade",
            "instantiateUcsTemplateAndAssocaciateToBlade",
            "refreshUcsBlades"
          ],
          "length": 255,
          "type": "uuid",
          "description": "blade id"
        }
      ],
      "requiredparams": [
        "bladeid"
      ],
      "description": "disassociate a profile from a blade"
    }
  },
  "migrate": {
    "volume": {
      "name": "migrateVolume",
      "related": [
        "uploadVolume",
        "resizeVolume",
        "updateVolume",
        "createVolume",
        "detachVolume",
        "attachVolume"
      ],
      "isasync": True,
      "params": [
        {
          "name": "livemigrate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "if the volume should be live migrated when it is attached to a running vm"
        },
        {
          "name": "volumeid",
          "required": True,
          "related": [
            "migrateVolume",
            "uploadVolume",
            "resizeVolume",
            "updateVolume",
            "createVolume",
            "detachVolume",
            "attachVolume"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the volume"
        },
        {
          "name": "storageid",
          "required": True,
          "related": [
            "findStoragePoolsForMigration",
            "updateStoragePool",
            "cancelStorageMaintenance",
            "createStoragePool",
            "enableStorageMaintenance",
            "listStoragePools"
          ],
          "length": 255,
          "type": "uuid",
          "description": "destination storage pool ID to migrate the volume to"
        }
      ],
      "requiredparams": [
        "volumeid",
        "storageid"
      ],
      "description": "Migrate volume"
    },
    "systemvm": {
      "name": "migrateSystemVm",
      "related": [
        "rebootSystemVm",
        "listSystemVms",
        "scaleSystemVm"
      ],
      "isasync": True,
      "params": [
        {
          "name": "virtualmachineid",
          "required": True,
          "related": [
            "migrateSystemVm",
            "rebootSystemVm",
            "listSystemVms",
            "scaleSystemVm"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the virtual machine"
        },
        {
          "name": "hostid",
          "required": True,
          "related": [
            "listExternalLoadBalancers",
            "listHosts"
          ],
          "length": 255,
          "type": "uuid",
          "description": "destination Host ID to migrate VM to"
        }
      ],
      "requiredparams": [
        "virtualmachineid",
        "hostid"
      ],
      "description": "Attempts Migration of a system virtual machine to the host specified."
    },
    "virtualmachinewithvolume": {
      "name": "migrateVirtualMachineWithVolume",
      "related": [
        "revertToVMSnapshot",
        "listVirtualMachines",
        "destroyVirtualMachine"
      ],
      "isasync": True,
      "params": [
        {
          "name": "hostid",
          "required": True,
          "related": [
            "listHosts"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Destination Host ID to migrate VM to."
        },
        {
          "name": "virtualmachineid",
          "required": True,
          "related": [
            "migrateVirtualMachineWithVolume",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "destroyVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the virtual machine"
        },
        {
          "name": "migrateto",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "Map of pool to which each volume should be migrated (volume/pool pair)"
        }
      ],
      "requiredparams": [
        "hostid",
        "virtualmachineid"
      ],
      "description": "Attempts Migration of a VM with its volumes to a different host"
    },
    "virtualmachine": {
      "name": "migrateVirtualMachine",
      "related": [
        "migrateVirtualMachineWithVolume",
        "stopVirtualMachine",
        "updateVirtualMachine",
        "revertToVMSnapshot",
        "listVirtualMachines",
        "assignVirtualMachine",
        "destroyVirtualMachine",
        "restoreVirtualMachine"
      ],
      "isasync": True,
      "params": [
        {
          "name": "virtualmachineid",
          "required": True,
          "related": [
            "migrateVirtualMachineWithVolume",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "updateVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the virtual machine"
        },
        {
          "name": "hostid",
          "required": False,
          "related": [
            "listHosts"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Destination Host ID to migrate VM to. Required for live migrating a VM from host to host"
        },
        {
          "name": "storageid",
          "required": False,
          "related": [
            "findStoragePoolsForMigration"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Destination storage pool ID to migrate VM volumes to. Required for migrating the root disk volume"
        }
      ],
      "requiredparams": [
        "virtualmachineid"
      ],
      "description": "Attempts Migration of a VM to a different host or Root volume of the vm to a different storage pool"
    }
  },
  "lock": {
    "account": {
      "name": "lockAccount",
      "related": [
        "listAccounts",
        "ldapCreateAccount",
        "markDefaultZoneForAccount",
        "createAccount",
        "disableAccount"
      ],
      "isasync": False,
      "params": [
        {
          "name": "domainid",
          "required": True,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Locks the specified account on this domain."
        },
        {
          "name": "account",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Locks the specified account."
        }
      ],
      "requiredparams": [
        "domainid",
        "account"
      ],
      "description": "Locks an account"
    },
    "user": {
      "name": "lockUser",
      "related": [
        "listUsers"
      ],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "lockUser",
            "listUsers"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Locks user by user ID."
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Locks a user account"
    }
  },
  "dedicate": {
    "publiciprange": {
      "name": "dedicatePublicIpRange",
      "related": [
        "listVlanIpRanges"
      ],
      "isasync": False,
      "params": [
        {
          "name": "projectid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "project who will own the VLAN"
        },
        {
          "name": "domainid",
          "required": True,
          "related": [
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "domain ID of the account owning a VLAN"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "listVlanIpRanges",
            "dedicatePublicIpRange"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the id of the VLAN IP range"
        },
        {
          "name": "account",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "account who will own the VLAN"
        }
      ],
      "requiredparams": [
        "domainid",
        "id",
        "account"
      ],
      "description": "Dedicates a Public IP range to an account"
    },
    "zone": {
      "name": "dedicateZone",
      "related": [
        "listDedicatedZones"
      ],
      "isasync": True,
      "params": [
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the zone"
        },
        {
          "name": "domainid",
          "required": True,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the containing domain"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the account which needs dedication. Must be used with domainId."
        }
      ],
      "requiredparams": [
        "zoneid",
        "domainid"
      ],
      "description": "Dedicates a zones."
    },
    "guestvlanrange": {
      "name": "dedicateGuestVlanRange",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "account",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "account who will own the VLAN"
        },
        {
          "name": "physicalnetworkid",
          "required": True,
          "related": [
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "physical network ID of the vlan"
        },
        {
          "name": "vlanrange",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "guest vlan range to be dedicated"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "project who will own the VLAN"
        },
        {
          "name": "domainid",
          "required": True,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "domain ID of the account owning a VLAN"
        }
      ],
      "requiredparams": [
        "account",
        "physicalnetworkid",
        "vlanrange",
        "domainid"
      ],
      "description": "Dedicates a guest vlan range to an account"
    },
    "cluster": {
      "name": "dedicateCluster",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "domainid",
          "required": True,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the containing domain"
        },
        {
          "name": "clusterid",
          "required": True,
          "related": [
            "updateCluster"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Cluster"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the account which needs dedication. Must be used with domainId."
        }
      ],
      "requiredparams": [
        "domainid",
        "clusterid"
      ],
      "description": "Dedicate an existing cluster"
    },
    "host": {
      "name": "dedicateHost",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "hostid",
          "required": True,
          "related": [
            "listHosts"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the host to update"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the account which needs dedication. Must be used with domainId."
        },
        {
          "name": "domainid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the containing domain"
        }
      ],
      "requiredparams": [
        "hostid",
        "domainid"
      ],
      "description": "Dedicates a host."
    },
    "pod": {
      "name": "dedicatePod",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the account which needs dedication. Must be used with domainId."
        },
        {
          "name": "domainid",
          "required": True,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the containing domain"
        },
        {
          "name": "podid",
          "required": True,
          "related": [
            "createPod",
            "updatePod"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Pod"
        }
      ],
      "requiredparams": [
        "domainid",
        "podid"
      ],
      "description": "Dedicates a Pod."
    }
  },
  "activate": {
    "project": {
      "name": "activateProject",
      "related": [
        "createProject",
        "listProjectAccounts",
        "updateProject"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "createProject",
            "activateProject",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of the project to be modified"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Activates a project"
    }
  },
  "refresh": {
    "ucsblades": {
      "name": "refreshUcsBlades",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "ucsmanagerid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "ucs manager id"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [
        "ucsmanagerid"
      ],
      "description": "refresh ucs blades to sync with UCS manager"
    }
  },
  "reconnect": {
    "host": {
      "name": "reconnectHost",
      "related": [
        "listExternalLoadBalancers",
        "addBaremetalHost",
        "addHost",
        "cancelHostMaintenance",
        "updateHost",
        "listHosts",
        "prepareHostForMaintenance"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listExternalLoadBalancers",
            "addBaremetalHost",
            "addHost",
            "cancelHostMaintenance",
            "updateHost",
            "listHosts",
            "reconnectHost",
            "prepareHostForMaintenance"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the host ID"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Reconnects a host."
    }
  },
  "cancel": {
    "hostmaintenance": {
      "name": "cancelHostMaintenance",
      "related": [
        "listExternalLoadBalancers",
        "addBaremetalHost",
        "addHost",
        "updateHost",
        "listHosts",
        "prepareHostForMaintenance"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listExternalLoadBalancers",
            "addBaremetalHost",
            "addHost",
            "cancelHostMaintenance",
            "updateHost",
            "listHosts",
            "prepareHostForMaintenance"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the host ID"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Cancels host maintenance."
    },
    "storagemaintenance": {
      "name": "cancelStorageMaintenance",
      "related": [
        "findStoragePoolsForMigration",
        "createStoragePool",
        "listStoragePools"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "findStoragePoolsForMigration",
            "cancelStorageMaintenance",
            "createStoragePool",
            "listStoragePools"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the primary storage ID"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Cancels maintenance for primary storage"
    }
  },
  "query": {
    "asyncjobresult": {
      "name": "queryAsyncJobResult",
      "related": [
        "listAsyncJobs"
      ],
      "isasync": False,
      "params": [
        {
          "name": "jobid",
          "required": True,
          "related": [
            "queryAsyncJobResult",
            "listAsyncJobs"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the asychronous job"
        }
      ],
      "requiredparams": [
        "jobid"
      ],
      "description": "Retrieves the current status of asynchronous job."
    }
  },
  "recover": {
    "virtualmachine": {
      "name": "recoverVirtualMachine",
      "related": [
        "detachIso",
        "migrateVirtualMachineWithVolume",
        "updateVMAffinityGroup",
        "startVirtualMachine",
        "migrateVirtualMachine",
        "stopVirtualMachine",
        "rebootVirtualMachine",
        "removeNicFromVirtualMachine",
        "updateVirtualMachine",
        "deployVirtualMachine",
        "changeServiceForVirtualMachine",
        "updateDefaultNicForVirtualMachine",
        "revertToVMSnapshot",
        "listVirtualMachines",
        "resetPasswordForVirtualMachine",
        "assignVirtualMachine",
        "attachIso",
        "destroyVirtualMachine",
        "restoreVirtualMachine"
      ],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "recoverVirtualMachine",
            "deployVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "attachIso",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the virtual machine"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Recovers a virtual machine."
    }
  },
  "extract": {
    "volume": {
      "name": "extractVolume",
      "related": [
        "extractIso",
        "extractTemplate"
      ],
      "isasync": True,
      "params": [
        {
          "name": "mode",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the mode of extraction - HTTP_DOWNLOAD or FTP_UPLOAD"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "migrateVolume",
            "uploadVolume",
            "resizeVolume",
            "updateVolume",
            "createVolume",
            "detachVolume",
            "listVolumes",
            "attachVolume"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the volume"
        },
        {
          "name": "url",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the url to which the volume would be extracted"
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the zone where the volume is located"
        }
      ],
      "requiredparams": [
        "mode",
        "id",
        "zoneid"
      ],
      "description": "Extracts volume"
    },
    "iso": {
      "name": "extractIso",
      "related": [
        "extractTemplate"
      ],
      "isasync": True,
      "params": [
        {
          "name": "url",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the url to which the ISO would be extracted"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the zone where the ISO is originally located"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "listIsos",
            "copyIso",
            "updateIso"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the ISO file"
        },
        {
          "name": "mode",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the mode of extraction - HTTP_DOWNLOAD or FTP_UPLOAD"
        }
      ],
      "requiredparams": [
        "id",
        "mode"
      ],
      "description": "Extracts an ISO"
    },
    "template": {
      "name": "extractTemplate",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "mode",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the mode of extraction - HTTP_DOWNLOAD or FTP_UPLOAD"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the zone where the ISO is originally located"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "listIsos",
            "copyIso",
            "updateIso"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the template"
        },
        {
          "name": "url",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the url to which the ISO would be extracted"
        }
      ],
      "requiredparams": [
        "mode",
        "id"
      ],
      "description": "Extracts a template"
    }
  },
  "archive": {
    "alerts": {
      "name": "archiveAlerts",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "type",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "archive by alert type"
        },
        {
          "name": "ids",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "the IDs of the alerts"
        },
        {
          "name": "enddate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "date",
          "description": "end date range to archive alerts (including) this date (use format \"yyyy-MM-dd\" or the new format \"yyyy-MM-ddThh:mm:ss\")"
        },
        {
          "name": "startdate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "date",
          "description": "start date range to archive alerts (including) this date (use format \"yyyy-MM-dd\" or the new format \"yyyy-MM-ddThh:mm:ss\")"
        }
      ],
      "requiredparams": [],
      "description": "Archive one or more alerts."
    },
    "events": {
      "name": "archiveEvents",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "enddate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "date",
          "description": "end date range to archive events (including) this date (use format \"yyyy-MM-dd\" or the new format \"yyyy-MM-ddThh:mm:ss\")"
        },
        {
          "name": "ids",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "the IDs of the events"
        },
        {
          "name": "type",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "archive by event type"
        },
        {
          "name": "startdate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "date",
          "description": "start date range to archive events (including) this date (use format \"yyyy-MM-dd\" or the new format \"yyyy-MM-ddThh:mm:ss\")"
        }
      ],
      "requiredparams": [],
      "description": "Archive one or more events."
    }
  },
  "detach": {
    "volume": {
      "name": "detachVolume",
      "related": [
        "uploadVolume",
        "createVolume"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": False,
          "related": [
            "uploadVolume",
            "createVolume",
            "detachVolume"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the disk volume"
        },
        {
          "name": "deviceid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "the device ID on the virtual machine where volume is detached from"
        },
        {
          "name": "virtualmachineid",
          "required": False,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "attachIso",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the virtual machine where the volume is detached from"
        }
      ],
      "requiredparams": [],
      "description": "Detaches a disk volume from a virtual machine."
    },
    "iso": {
      "name": "detachIso",
      "related": [
        "migrateVirtualMachineWithVolume",
        "migrateVirtualMachine",
        "stopVirtualMachine",
        "updateVirtualMachine",
        "revertToVMSnapshot",
        "listVirtualMachines",
        "assignVirtualMachine",
        "destroyVirtualMachine",
        "restoreVirtualMachine"
      ],
      "isasync": True,
      "params": [
        {
          "name": "virtualmachineid",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "updateVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the virtual machine"
        }
      ],
      "requiredparams": [
        "virtualmachineid"
      ],
      "description": "Detaches any ISO file (if any) currently attached to a virtual machine."
    }
  },
  "prepare": {
    "template": {
      "name": "prepareTemplate",
      "related": [
        "registerIso",
        "listIsos",
        "copyIso",
        "updateIso",
        "updateTemplate"
      ],
      "isasync": False,
      "params": [
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "zone ID of the template to be prepared in primary storage(s)."
        },
        {
          "name": "templateid",
          "required": True,
          "related": [
            "registerIso",
            "prepareTemplate",
            "listIsos",
            "copyIso",
            "updateIso",
            "updateTemplate"
          ],
          "length": 255,
          "type": "uuid",
          "description": "template ID of the template to be prepared in primary storage(s)."
        }
      ],
      "requiredparams": [
        "zoneid",
        "templateid"
      ],
      "description": "load template into primary storage"
    },
    "hostformaintenance": {
      "name": "prepareHostForMaintenance",
      "related": [
        "listExternalLoadBalancers",
        "listHosts"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listExternalLoadBalancers",
            "listHosts",
            "prepareHostForMaintenance"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the host ID"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Prepares a host for maintenance."
    }
  },
  "start": {
    "systemvm": {
      "name": "startSystemVm",
      "related": [
        "migrateSystemVm",
        "changeServiceForSystemVm",
        "rebootSystemVm",
        "listSystemVms",
        "scaleSystemVm"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "migrateSystemVm",
            "changeServiceForSystemVm",
            "rebootSystemVm",
            "listSystemVms",
            "startSystemVm",
            "scaleSystemVm"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the system virtual machine"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Starts a system virtual machine."
    },
    "router": {
      "name": "startRouter",
      "related": [
        "listInternalLoadBalancerVMs"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "startRouter",
            "listInternalLoadBalancerVMs"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the router"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Starts a router."
    },
    "internalloadbalancervm": {
      "name": "startInternalLoadBalancerVM",
      "related": [
        "destroyRouter",
        "startRouter",
        "stopInternalLoadBalancerVM",
        "listInternalLoadBalancerVMs",
        "rebootRouter",
        "changeServiceForRouter"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "destroyRouter",
            "startRouter",
            "stopInternalLoadBalancerVM",
            "listInternalLoadBalancerVMs",
            "rebootRouter",
            "startInternalLoadBalancerVM",
            "changeServiceForRouter"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the internal lb vm"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Starts an existing internal lb vm."
    },
    "virtualmachine": {
      "name": "startVirtualMachine",
      "related": [
        "detachIso",
        "migrateVirtualMachineWithVolume",
        "migrateVirtualMachine",
        "stopVirtualMachine",
        "updateVirtualMachine",
        "revertToVMSnapshot",
        "listVirtualMachines",
        "assignVirtualMachine",
        "destroyVirtualMachine",
        "restoreVirtualMachine"
      ],
      "isasync": True,
      "params": [
        {
          "name": "hostid",
          "required": False,
          "related": [
            "listHosts"
          ],
          "length": 255,
          "type": "uuid",
          "description": "destination Host ID to deploy the VM to - parameter available for root admin only"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "updateVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the virtual machine"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Starts a virtual machine."
    }
  },
  "revert": {
    "tovmsnapshot": {
      "name": "revertToVMSnapshot",
      "related": [
        "listVirtualMachines"
      ],
      "isasync": True,
      "params": [
        {
          "name": "vmsnapshotid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the vm snapshot"
        }
      ],
      "requiredparams": [
        "vmsnapshotid"
      ],
      "description": "Revert VM from a vmsnapshot."
    },
    "snapshot": {
      "name": "revertSnapshot",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "revertSnapshot"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the snapshot"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "revert a volume snapshot."
    }
  },
  "create": {
    "loadbalancerrule": {
      "name": "createLoadBalancerRule",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "privateport",
          "required": True,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the private port of the private ip address/virtual machine where the network traffic will be load balanced to"
        },
        {
          "name": "description",
          "required": False,
          "related": [],
          "length": 4096,
          "type": "string",
          "description": "the description of the load balancer rule"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of the load balancer rule"
        },
        {
          "name": "algorithm",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "load balancer algorithm (source, roundrobin, leastconn)"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the domain ID associated with the load balancer"
        },
        {
          "name": "cidrlist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "the cidr list to forward traffic from"
        },
        {
          "name": "publicipid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "public ip address id from where the network traffic will be load balanced from"
        },
        {
          "name": "openfirewall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "if True, firewall rule for source/end pubic port is automatically created; if False - firewall rule has to be created explicitely. If not specified 1) defaulted to False when LB rule is being created for VPC guest network 2) in all other cases defaulted to True"
        },
        {
          "name": "protocol",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The protocol for the LB"
        },
        {
          "name": "publicport",
          "required": True,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the public port from where the network traffic will be load balanced from"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "zone where the load balancer is going to be created. This parameter is required when LB service provider is ElasticLoadBalancerVm"
        },
        {
          "name": "networkid",
          "required": False,
          "related": [
            "updateNetwork",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The guest network this rule will be created for. Required when public Ip address is not associated with any Guest network yet (VPC case)"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the account associated with the load balancer. Must be used with the domainId parameter."
        }
      ],
      "requiredparams": [
        "privateport",
        "name",
        "algorithm",
        "publicport"
      ],
      "description": "Creates a load balancer rule"
    },
    "domain": {
      "name": "createDomain",
      "related": [
        "updateDomain",
        "listDomainChildren",
        "listDomains"
      ],
      "isasync": False,
      "params": [
        {
          "name": "domainid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Domain UUID, required for adding domain from another Region"
        },
        {
          "name": "networkdomain",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Network domain for networks in the domain"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "creates domain with this name"
        },
        {
          "name": "parentdomainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "assigns new domain a parent domain by domain ID of the parent.  If no parent domain is specied, the ROOT domain is assumed."
        }
      ],
      "requiredparams": [
        "name"
      ],
      "description": "Creates a domain"
    },
    "snapshotpolicy": {
      "name": "createSnapshotPolicy",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "timezone",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Specifies a timezone for this command. For more information on the timezone parameter, see Time Zone Format."
        },
        {
          "name": "intervaltype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "valid values are HOURLY, DAILY, WEEKLY, and MONTHLY"
        },
        {
          "name": "volumeid",
          "required": True,
          "related": [
            "uploadVolume",
            "createVolume"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the disk volume"
        },
        {
          "name": "schedule",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "time the snapshot is scheduled to be taken. Format is:* if HOURLY, MM* if DAILY, MM:HH* if WEEKLY, MM:HH:DD (1-7)* if MONTHLY, MM:HH:DD (1-28)"
        },
        {
          "name": "maxsnaps",
          "required": True,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "maximum number of snapshots to retain"
        }
      ],
      "requiredparams": [
        "timezone",
        "intervaltype",
        "volumeid",
        "schedule",
        "maxsnaps"
      ],
      "description": "Creates a snapshot policy for the account."
    },
    "vpc": {
      "name": "createVPC",
      "related": [
        "listVPCs",
        "restartVPC"
      ],
      "isasync": True,
      "params": [
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "create VPC for the project"
        },
        {
          "name": "vpcofferingid",
          "required": True,
          "related": [
            "listVPCOfferings"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the VPC offering"
        },
        {
          "name": "displaytext",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the display text of the VPC"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the account associated with the VPC. Must be used with the domainId parameter."
        },
        {
          "name": "cidr",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the cidr of the VPC. All VPC guest networks' cidrs should be within this CIDR"
        },
        {
          "name": "networkdomain",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "VPC network domain. All networks inside the VPC will belong to this domain"
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the availability zone"
        },
        {
          "name": "start",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, the VPC won't start (VPC VR will not get allocated) until its first network gets implemented. True by default."
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the VPC"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the domain ID associated with the VPC. If used with the account parameter returns the VPC associated with the account for the specified domain."
        }
      ],
      "requiredparams": [
        "vpcofferingid",
        "displaytext",
        "cidr",
        "zoneid",
        "name"
      ],
      "description": "Creates a VPC"
    },
    "securitygroup": {
      "name": "createSecurityGroup",
      "related": [
        "listSecurityGroups"
      ],
      "isasync": False,
      "params": [
        {
          "name": "description",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the description of the security group"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional domainId for the security group. If the account parameter is used, domainId must also be used."
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of the security group"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "an optional account for the security group. Must be used with domainId."
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "activateProject",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Create security group for project"
        }
      ],
      "requiredparams": [
        "name"
      ],
      "description": "Creates a security group"
    },
    "portforwardingrule": {
      "name": "createPortForwardingRule",
      "related": [
        "listIpForwardingRules"
      ],
      "isasync": True,
      "params": [
        {
          "name": "ipaddressid",
          "required": True,
          "related": [
            "associateIpAddress",
            "restartNetwork"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the IP address id of the port forwarding rule"
        },
        {
          "name": "networkid",
          "required": False,
          "related": [
            "listSrxFirewallNetworks",
            "updateNetwork",
            "listF5LoadBalancerNetworks",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The network of the vm the Port Forwarding rule will be created for. Required when public Ip address is not associated with any Guest network yet (VPC case)"
        },
        {
          "name": "vmguestip",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "VM guest nic Secondary ip address for the port forwarding rule"
        },
        {
          "name": "privateport",
          "required": True,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the starting port of port forwarding rule's private port range"
        },
        {
          "name": "publicport",
          "required": True,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the starting port of port forwarding rule's public port range"
        },
        {
          "name": "cidrlist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "the cidr list to forward traffic from"
        },
        {
          "name": "virtualmachineid",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "attachIso",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the virtual machine for the port forwarding rule"
        },
        {
          "name": "protocol",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the protocol for the port fowarding rule. Valid values are TCP or UDP."
        },
        {
          "name": "openfirewall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "if True, firewall rule for source/end pubic port is automatically created; if False - firewall rule has to be created explicitely. If not specified 1) defaulted to False when PF rule is being created for VPC guest network 2) in all other cases defaulted to True"
        },
        {
          "name": "publicendport",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the ending port of port forwarding rule's private port range"
        },
        {
          "name": "privateendport",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the ending port of port forwarding rule's private port range"
        }
      ],
      "requiredparams": [
        "ipaddressid",
        "privateport",
        "publicport",
        "virtualmachineid",
        "protocol"
      ],
      "description": "Creates a port forwarding rule"
    },
    "pod": {
      "name": "createPod",
      "related": [
        "updatePod"
      ],
      "isasync": False,
      "params": [
        {
          "name": "startip",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the starting IP address for the Pod"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the Pod"
        },
        {
          "name": "netmask",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the netmask for the Pod"
        },
        {
          "name": "endip",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the ending IP address for the Pod"
        },
        {
          "name": "gateway",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the gateway for the Pod"
        },
        {
          "name": "allocationstate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Allocation state of this Pod for allocation of new resources"
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID in which the Pod will be created"
        }
      ],
      "requiredparams": [
        "startip",
        "name",
        "netmask",
        "gateway",
        "zoneid"
      ],
      "description": "Creates a new Pod."
    },
    "ipforwardingrule": {
      "name": "createIpForwardingRule",
      "related": [
        "updatePortForwardingRule",
        "listPortForwardingRules",
        "createPortForwardingRule",
        "listIpForwardingRules"
      ],
      "isasync": True,
      "params": [
        {
          "name": "endport",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the end port for the rule"
        },
        {
          "name": "startport",
          "required": True,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the start port for the rule"
        },
        {
          "name": "openfirewall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "if True, firewall rule for source/end pubic port is automatically created; if False - firewall rule has to be created explicitely. Has value True by default"
        },
        {
          "name": "cidrlist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "the cidr list to forward traffic from"
        },
        {
          "name": "ipaddressid",
          "required": True,
          "related": [
            "associateIpAddress",
            "restartNetwork"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the public IP address id of the forwarding rule, already associated via associateIp"
        },
        {
          "name": "protocol",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the protocol for the rule. Valid values are TCP or UDP."
        }
      ],
      "requiredparams": [
        "startport",
        "ipaddressid",
        "protocol"
      ],
      "description": "Creates an ip forwarding rule"
    },
    "vmsnapshot": {
      "name": "createVMSnapshot",
      "related": [
        "listVMSnapshot"
      ],
      "isasync": True,
      "params": [
        {
          "name": "snapshotmemory",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "snapshot memory if True"
        },
        {
          "name": "quiescevm",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "quiesce vm if True"
        },
        {
          "name": "description",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The discription of the snapshot"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The display name of the snapshot"
        },
        {
          "name": "virtualmachineid",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "recoverVirtualMachine",
            "deployVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "attachIso",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the vm"
        }
      ],
      "requiredparams": [
        "virtualmachineid"
      ],
      "description": "Creates snapshot for a vm."
    },
    "diskoffering": {
      "name": "createDiskOffering",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "displaytext",
          "required": True,
          "related": [],
          "length": 4096,
          "type": "string",
          "description": "alternate display text of the disk offering"
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 4096,
          "type": "string",
          "description": "tags for the disk offering"
        },
        {
          "name": "hypervisorsnapshotreserve",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "Hypervisor snapshot reserve space as a percent of a volume (for managed storage using Xen or VMware)"
        },
        {
          "name": "iopsreadrate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "io requests read rate of the disk offering"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the containing domain, null for public offerings"
        },
        {
          "name": "customizediops",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "whether disk offering iops is custom or not"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of the disk offering"
        },
        {
          "name": "maxiops",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "max iops of the disk offering"
        },
        {
          "name": "displayoffering",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "an optional field, whether to display the offering to the end user or not."
        },
        {
          "name": "storagetype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the storage type of the disk offering. Values are local and shared."
        },
        {
          "name": "miniops",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "min iops of the disk offering"
        },
        {
          "name": "iopswriterate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "io requests write rate of the disk offering"
        },
        {
          "name": "byteswriterate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "bytes write rate of the disk offering"
        },
        {
          "name": "customized",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "whether disk offering size is custom or not"
        },
        {
          "name": "bytesreadrate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "bytes read rate of the disk offering"
        },
        {
          "name": "disksize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "size of the disk offering in GB"
        }
      ],
      "requiredparams": [
        "displaytext",
        "name"
      ],
      "description": "Creates a disk offering."
    },
    "lbstickinesspolicy": {
      "name": "createLBStickinessPolicy",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of the LB Stickiness policy"
        },
        {
          "name": "methodname",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of the LB Stickiness policy method, possible values can be obtained from ListNetworks API "
        },
        {
          "name": "description",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the description of the LB Stickiness policy"
        },
        {
          "name": "lbruleid",
          "required": True,
          "related": [
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the load balancer rule"
        },
        {
          "name": "param",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "param list. Example: param[0].name=cookiename&param[0].value=LBCookie "
        }
      ],
      "requiredparams": [
        "name",
        "methodname",
        "lbruleid"
      ],
      "description": "Creates a Load Balancer stickiness policy "
    },
    "vpcoffering": {
      "name": "createVPCOffering",
      "related": [
        "listVPCOfferings"
      ],
      "isasync": True,
      "params": [
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the vpc offering"
        },
        {
          "name": "displaytext",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the display text of the vpc offering"
        },
        {
          "name": "serviceproviderlist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "provider to service mapping. If not specified, the provider for the service will be mapped to the default provider on the physical network"
        },
        {
          "name": "supportedservices",
          "required": True,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "services supported by the vpc offering"
        },
        {
          "name": "serviceofferingid",
          "required": False,
          "related": [
            "createServiceOffering",
            "listServiceOfferings"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the service offering for the VPC router appliance"
        }
      ],
      "requiredparams": [
        "name",
        "displaytext",
        "supportedservices"
      ],
      "description": "Creates VPC offering"
    },
    "network": {
      "name": "createNetwork",
      "related": [
        "listSrxFirewallNetworks",
        "listNetworks",
        "updateNetwork",
        "listF5LoadBalancerNetworks",
        "listPaloAltoFirewallNetworks",
        "listNetscalerLoadBalancerNetworks"
      ],
      "isasync": False,
      "params": [
        {
          "name": "ip6cidr",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the CIDR of IPv6 network, must be at least /64"
        },
        {
          "name": "endipv6",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the ending IPv6 address in the IPv6 network range"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "domain ID of the account owning a network"
        },
        {
          "name": "vpcid",
          "required": False,
          "related": [
            "createVPC",
            "listVPCs",
            "restartVPC",
            "updateVPC"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the VPC network belongs to"
        },
        {
          "name": "physicalnetworkid",
          "required": False,
          "related": [
            "createPhysicalNetwork",
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID the network belongs to"
        },
        {
          "name": "aclid",
          "required": False,
          "related": [
            "listNetworkACLLists",
            "createNetworkACLList"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Network ACL Id associated for the network"
        },
        {
          "name": "netmask",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the netmask of the network. Required for Shared networks and Isolated networks when it belongs to VPC"
        },
        {
          "name": "displaynetwork",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "an optional field, whether to the display the network to the end user or not."
        },
        {
          "name": "ip6gateway",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the gateway of the IPv6 network. Required for Shared networks and Isolated networks when it belongs to VPC"
        },
        {
          "name": "networkdomain",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "network domain"
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID for the network"
        },
        {
          "name": "networkofferingid",
          "required": True,
          "related": [
            "createNetworkOffering",
            "updateNetworkOffering"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the network offering id"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "account who will own the network"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the network"
        },
        {
          "name": "endip",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the ending IP address in the network IP range. If not specified, will be defaulted to startIP"
        },
        {
          "name": "isolatedpvlan",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the isolated private vlan for this network"
        },
        {
          "name": "startipv6",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the beginning IPv6 address in the IPv6 network range"
        },
        {
          "name": "subdomainaccess",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "Defines whether to allow subdomains to use networks dedicated to their parent domain(s). Should be used with aclType=Domain, defaulted to allow.subdomain.network.access global config if not specified"
        },
        {
          "name": "displaytext",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the display text of the network"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "activateProject",
            "listProjects",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional project for the ssh key"
        },
        {
          "name": "startip",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the beginning IP address in the network IP range"
        },
        {
          "name": "vlan",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the ID or VID of the network"
        },
        {
          "name": "acltype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Access control type; supported values are account and domain. In 3.0 all shared networks should have aclType=Domain, and all Isolated networks - Account. Account means that only the account owner can use the network, domain - all accouns in the domain can use the network"
        },
        {
          "name": "gateway",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the gateway of the network. Required for Shared networks and Isolated networks when it belongs to VPC"
        }
      ],
      "requiredparams": [
        "zoneid",
        "networkofferingid",
        "name",
        "displaytext"
      ],
      "description": "Creates a network"
    },
    "zone": {
      "name": "createZone",
      "related": [
        "listZones"
      ],
      "isasync": False,
      "params": [
        {
          "name": "ip6dns1",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the first DNS for IPv6 network in the Zone"
        },
        {
          "name": "domain",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Network domain name for the networks in the zone"
        },
        {
          "name": "securitygroupenabled",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if network is security group enabled, False otherwise"
        },
        {
          "name": "ip6dns2",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the second DNS for IPv6 network in the Zone"
        },
        {
          "name": "networktype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "network type of the zone, can be Basic or Advanced"
        },
        {
          "name": "guestcidraddress",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the guest CIDR address for the Zone"
        },
        {
          "name": "localstorageenabled",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if local storage offering enabled, False otherwise"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the containing domain, null for public zones"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the Zone"
        },
        {
          "name": "internaldns2",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the second internal DNS for the Zone"
        },
        {
          "name": "allocationstate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Allocation state of this Zone for allocation of new resources"
        },
        {
          "name": "internaldns1",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the first internal DNS for the Zone"
        },
        {
          "name": "dns1",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the first DNS for the Zone"
        },
        {
          "name": "dns2",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the second DNS for the Zone"
        }
      ],
      "requiredparams": [
        "networktype",
        "name",
        "internaldns1",
        "dns1"
      ],
      "description": "Creates a Zone."
    },
    "remoteaccessvpn": {
      "name": "createRemoteAccessVpn",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "an optional account for the VPN. Must be used with domainId."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional domainId for the VPN. If the account parameter is used, domainId must also be used."
        },
        {
          "name": "iprange",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the range of ip addresses to allocate to vpn clients. The first ip in the range will be taken by the vpn server"
        },
        {
          "name": "publicipid",
          "required": True,
          "related": [
            "associateIpAddress"
          ],
          "length": 255,
          "type": "uuid",
          "description": "public ip address id of the vpn server"
        },
        {
          "name": "openfirewall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "if True, firewall rule for source/end pubic port is automatically created; if False - firewall rule has to be created explicitely. Has value True by default"
        }
      ],
      "requiredparams": [
        "publicipid"
      ],
      "description": "Creates a l2tp/ipsec remote access vpn"
    },
    "instancegroup": {
      "name": "createInstanceGroup",
      "related": [
        "updateInstanceGroup"
      ],
      "isasync": False,
      "params": [
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the account of the instance group. The account parameter must be used with the domainId parameter."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the domain ID of account owning the instance group"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The project of the instance group"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the instance group"
        }
      ],
      "requiredparams": [
        "name"
      ],
      "description": "Creates a vm group"
    },
    "autoscalepolicy": {
      "name": "createAutoScalePolicy",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "duration",
          "required": True,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the duration for which the conditions have to be True before action is taken"
        },
        {
          "name": "action",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the action to be executed if all the conditions evaluate to True for the specified duration."
        },
        {
          "name": "conditionids",
          "required": True,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "the list of IDs of the conditions that are being evaluated on every interval"
        },
        {
          "name": "quiettime",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the cool down period for which the policy should not be evaluated after the action has been taken"
        }
      ],
      "requiredparams": [
        "duration",
        "action",
        "conditionids"
      ],
      "description": "Creates an autoscale policy for a provision or deprovision action, the action is taken when the all the conditions evaluates to True for the specified duration. The policy is in effect once it is attached to a autscale vm group."
    },
    "globalloadbalancerrule": {
      "name": "createGlobalLoadBalancerRule",
      "related": [
        "updateGlobalLoadBalancerRule",
        "listGlobalLoadBalancerRules"
      ],
      "isasync": True,
      "params": [
        {
          "name": "gslbstickysessionmethodname",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "session sticky method (sourceip) if not specified defaults to sourceip"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the account associated with the global load balancer. Must be used with the domainId parameter."
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of the load balancer rule"
        },
        {
          "name": "gslblbmethod",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "load balancer algorithm (roundrobin, leastconn, proximity) that method is used to distribute traffic across the zones participating in global server load balancing, if not specified defaults to 'round robin'"
        },
        {
          "name": "description",
          "required": False,
          "related": [],
          "length": 4096,
          "type": "string",
          "description": "the description of the load balancer rule"
        },
        {
          "name": "gslbservicetype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "GSLB service type (tcp, udp, http)"
        },
        {
          "name": "gslbdomainname",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "domain name for the GSLB service."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the domain ID associated with the load balancer"
        },
        {
          "name": "regionid",
          "required": True,
          "related": [
            "listRegions",
            "addRegion"
          ],
          "length": 255,
          "type": "integer",
          "description": "region where the global load balancer is going to be created."
        }
      ],
      "requiredparams": [
        "name",
        "gslbservicetype",
        "gslbdomainname",
        "regionid"
      ],
      "description": "Creates a global load balancer rule"
    },
    "secondarystagingstore": {
      "name": "createSecondaryStagingStore",
      "related": [
        "listSwifts"
      ],
      "isasync": False,
      "params": [
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID for the staging store"
        },
        {
          "name": "provider",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the staging store provider name"
        },
        {
          "name": "scope",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the scope of the staging store: zone only for now"
        },
        {
          "name": "details",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "the details for the staging store"
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the URL for the staging store"
        }
      ],
      "requiredparams": [
        "url"
      ],
      "description": "create secondary staging store."
    },
    "template": {
      "name": "createTemplate",
      "related": [
        "registerIso",
        "prepareTemplate",
        "listIsos",
        "copyIso",
        "registerTemplate",
        "updateIso",
        "updateTemplate",
        "listTemplates"
      ],
      "isasync": True,
      "params": [
        {
          "name": "bits",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "32 or 64 bit"
        },
        {
          "name": "isfeatured",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if this template is a featured template, False otherwise"
        },
        {
          "name": "virtualmachineid",
          "required": False,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "listLoadBalancerRuleInstances",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "recoverVirtualMachine",
            "deployVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "resetSSHKeyForVirtualMachine",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "attachIso",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Optional, VM ID. If this presents, it is going to create a baremetal template for VM this ID refers to. This is only for VM whose hypervisor type is BareMetal"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the template"
        },
        {
          "name": "ostypeid",
          "required": True,
          "related": [
            "listOsTypes"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the OS Type that best represents the OS of this template."
        },
        {
          "name": "url",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Optional, only for baremetal hypervisor. The directory name where template stored on CIFS server"
        },
        {
          "name": "passwordenabled",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if the template supports the password reset feature; default is False"
        },
        {
          "name": "snapshotid",
          "required": False,
          "related": [
            "createSnapshot",
            "listSnapshots",
            "revertSnapshot"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the snapshot the template is being created from. Either this parameter, or volumeId has to be passed in"
        },
        {
          "name": "details",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "Template details in key/value pairs."
        },
        {
          "name": "displaytext",
          "required": True,
          "related": [],
          "length": 4096,
          "type": "string",
          "description": "the display text of the template. This is usually used for display purposes."
        },
        {
          "name": "ispublic",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if this template is a public template, False otherwise"
        },
        {
          "name": "volumeid",
          "required": False,
          "related": [
            "migrateVolume",
            "uploadVolume",
            "resizeVolume",
            "updateVolume",
            "createVolume",
            "detachVolume",
            "attachVolume"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the disk volume the template is being created from. Either this parameter, or snapshotId has to be passed in"
        },
        {
          "name": "templatetag",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the tag for this template."
        },
        {
          "name": "isdynamicallyscalable",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if template contains XS/VMWare tools inorder to support dynamic scaling of VM cpu/memory"
        },
        {
          "name": "requireshvm",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if the template requres HVM, False otherwise"
        }
      ],
      "requiredparams": [
        "name",
        "ostypeid",
        "displaytext"
      ],
      "description": "Creates a template of a virtual machine. The virtual machine must be in a STOPPED state. A template created from this command is automatically designated as a private template visible to the account that created it."
    },
    "vpngateway": {
      "name": "createVpnGateway",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "vpcid",
          "required": True,
          "related": [
            "createVPC",
            "listVPCs",
            "restartVPC"
          ],
          "length": 255,
          "type": "uuid",
          "description": "public ip address id of the vpn gateway"
        }
      ],
      "requiredparams": [
        "vpcid"
      ],
      "description": "Creates site to site vpn local gateway"
    },
    "serviceoffering": {
      "name": "createServiceOffering",
      "related": [
        "listServiceOfferings"
      ],
      "isasync": False,
      "params": [
        {
          "name": "networkrate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "data transfer rate in megabits per second allowed. Supported only for non-System offering and system offerings having \"domainrouter\" systemvmtype"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the service offering"
        },
        {
          "name": "bytesreadrate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "bytes read rate of the disk offering"
        },
        {
          "name": "memory",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the total memory of the service offering in MB"
        },
        {
          "name": "isvolatile",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if the virtual machine needs to be volatile so that on every reboot of VM, original root disk is dettached then destroyed and a fresh root disk is created and attached to VM"
        },
        {
          "name": "byteswriterate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "bytes write rate of the disk offering"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the containing domain, null for public offerings"
        },
        {
          "name": "issystem",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "is this a system vm offering"
        },
        {
          "name": "storagetype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the storage type of the service offering. Values are local and shared."
        },
        {
          "name": "deploymentplanner",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The deployment planner heuristics used to deploy a VM of this offering. If null, value of global config vm.deployment.planner is used"
        },
        {
          "name": "offerha",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "the HA for the service offering"
        },
        {
          "name": "displaytext",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the display text of the service offering"
        },
        {
          "name": "iopsreadrate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "io requests read rate of the disk offering"
        },
        {
          "name": "hosttags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the host tag for this service offering."
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the tags for this service offering."
        },
        {
          "name": "cpuspeed",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the CPU speed of the service offering in MHz."
        },
        {
          "name": "serviceofferingdetails",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "details for planner, used to store specific parameters"
        },
        {
          "name": "systemvmtype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the system VM type. Possible types are \"domainrouter\", \"consoleproxy\" and \"secondarystoragevm\"."
        },
        {
          "name": "iopswriterate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "io requests write rate of the disk offering"
        },
        {
          "name": "limitcpuuse",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "restrict the CPU usage to committed service offering"
        },
        {
          "name": "cpunumber",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the CPU number of the service offering"
        }
      ],
      "requiredparams": [
        "name",
        "displaytext"
      ],
      "description": "Creates a service offering."
    },
    "networkacllist": {
      "name": "createNetworkACLList",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "vpcid",
          "required": True,
          "related": [
            "createVPC",
            "listVPCs",
            "restartVPC"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Id of the VPC associated with this network ACL List"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Name of the network ACL List"
        },
        {
          "name": "description",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Description of the network ACL List"
        }
      ],
      "requiredparams": [
        "vpcid",
        "name"
      ],
      "description": "Creates a Network ACL for the given VPC"
    },
    "vlaniprange": {
      "name": "createVlanIpRange",
      "related": [
        "listVlanIpRanges",
        "dedicatePublicIpRange"
      ],
      "isasync": False,
      "params": [
        {
          "name": "podid",
          "required": False,
          "related": [
            "createPod",
            "updatePod"
          ],
          "length": 255,
          "type": "uuid",
          "description": "optional parameter. Have to be specified for Direct Untagged vlan only."
        },
        {
          "name": "startip",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the beginning IP address in the VLAN IP range"
        },
        {
          "name": "startipv6",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the beginning IPv6 address in the IPv6 network range"
        },
        {
          "name": "endipv6",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the ending IPv6 address in the IPv6 network range"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "project who will own the VLAN. If VLAN is Zone wide, this parameter should be ommited"
        },
        {
          "name": "gateway",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the gateway of the VLAN IP range"
        },
        {
          "name": "ip6gateway",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the gateway of the IPv6 network. Required for Shared networks and Isolated networks when it belongs to VPC"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID of the VLAN IP range"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "domain ID of the account owning a VLAN"
        },
        {
          "name": "forvirtualnetwork",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if VLAN is of Virtual type, False if Direct"
        },
        {
          "name": "netmask",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the netmask of the VLAN IP range"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "account who will own the VLAN. If VLAN is Zone wide, this parameter should be ommited"
        },
        {
          "name": "networkid",
          "required": False,
          "related": [
            "listSrxFirewallNetworks",
            "updateNetwork",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the network id"
        },
        {
          "name": "ip6cidr",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the CIDR of IPv6 network, must be at least /64"
        },
        {
          "name": "physicalnetworkid",
          "required": False,
          "related": [
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the physical network id"
        },
        {
          "name": "endip",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the ending IP address in the VLAN IP range"
        },
        {
          "name": "vlan",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the ID or VID of the VLAN. If not specified, will be defaulted to the vlan of the network or if vlan of the network is null - to Untagged"
        }
      ],
      "requiredparams": [],
      "description": "Creates a VLAN IP range."
    },
    "autoscalevmgroup": {
      "name": "createAutoScaleVmGroup",
      "related": [
        "enableAutoScaleVmGroup",
        "updateAutoScaleVmGroup",
        "disableAutoScaleVmGroup"
      ],
      "isasync": True,
      "params": [
        {
          "name": "lbruleid",
          "required": True,
          "related": [
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the load balancer rule"
        },
        {
          "name": "vmprofileid",
          "required": True,
          "related": [
            "listAutoScaleVmProfiles"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the autoscale profile that contains information about the vms in the vm group."
        },
        {
          "name": "scaledownpolicyids",
          "required": True,
          "related": [
            "updateAutoScalePolicy",
            "createAutoScalePolicy"
          ],
          "length": 255,
          "type": "list",
          "description": "list of scaledown autoscale policies"
        },
        {
          "name": "maxmembers",
          "required": True,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the maximum number of members in the vmgroup, The number of instances in the vm group will be equal to or less than this number."
        },
        {
          "name": "interval",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the frequency at which the conditions have to be evaluated"
        },
        {
          "name": "scaleuppolicyids",
          "required": True,
          "related": [
            "updateAutoScalePolicy",
            "createAutoScalePolicy"
          ],
          "length": 255,
          "type": "list",
          "description": "list of scaleup autoscale policies"
        },
        {
          "name": "minmembers",
          "required": True,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the minimum number of members in the vmgroup, the number of instances in the vm group will be equal to or more than this number."
        }
      ],
      "requiredparams": [
        "lbruleid",
        "vmprofileid",
        "scaledownpolicyids",
        "maxmembers",
        "scaleuppolicyids",
        "minmembers"
      ],
      "description": "Creates and automatically starts a virtual machine based on a service offering, disk offering, and template."
    },
    "vpnconnection": {
      "name": "createVpnConnection",
      "related": [
        "resetVpnConnection",
        "listVpnConnections"
      ],
      "isasync": True,
      "params": [
        {
          "name": "s2svpngatewayid",
          "required": True,
          "related": [
            "listVpnGateways",
            "createVpnGateway"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of the vpn gateway"
        },
        {
          "name": "passive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "connection is passive or not"
        },
        {
          "name": "s2scustomergatewayid",
          "required": True,
          "related": [
            "updateVpnCustomerGateway",
            "createVpnCustomerGateway",
            "listVpnCustomerGateways"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of the customer gateway"
        }
      ],
      "requiredparams": [
        "s2svpngatewayid",
        "s2scustomergatewayid"
      ],
      "description": "Create site to site vpn connection"
    },
    "networkacl": {
      "name": "createNetworkACL",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "traffictype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the traffic type for the ACL,can be Ingress or Egress, defaulted to Ingress if not specified"
        },
        {
          "name": "icmptype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "type of the icmp message being sent"
        },
        {
          "name": "networkid",
          "required": False,
          "related": [
            "updateNetwork",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The network of the vm the ACL will be created for"
        },
        {
          "name": "endport",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the ending port of ACL"
        },
        {
          "name": "action",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "scl entry action, allow or deny"
        },
        {
          "name": "startport",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the starting port of ACL"
        },
        {
          "name": "icmpcode",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "error code for this icmp message"
        },
        {
          "name": "aclid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "The network of the vm the ACL will be created for"
        },
        {
          "name": "cidrlist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "the cidr list to allow traffic from/to"
        },
        {
          "name": "protocol",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the protocol for the ACL rule. Valid values are TCP/UDP/ICMP/ALL or valid protocol number"
        },
        {
          "name": "number",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "The network of the vm the ACL will be created for"
        }
      ],
      "requiredparams": [
        "protocol"
      ],
      "description": "Creates a ACL rule in the given network (the network has to belong to VPC)"
    },
    "storagepool": {
      "name": "createStoragePool",
      "related": [
        "findStoragePoolsForMigration",
        "listStoragePools"
      ],
      "isasync": False,
      "params": [
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the tags for the storage pool"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name for the storage pool"
        },
        {
          "name": "podid",
          "required": False,
          "related": [
            "createPod",
            "updatePod"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Pod ID for the storage pool"
        },
        {
          "name": "capacitybytes",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "bytes CloudStack can provision from this storage pool"
        },
        {
          "name": "provider",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the storage provider name"
        },
        {
          "name": "capacityiops",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "IOPS CloudStack can provision from this storage pool"
        },
        {
          "name": "details",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "the details for the storage pool"
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the URL of the storage pool"
        },
        {
          "name": "clusterid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the cluster ID for the storage pool"
        },
        {
          "name": "scope",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the scope of the storage: cluster or zone"
        },
        {
          "name": "managed",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "whether the storage should be managed by CloudStack"
        },
        {
          "name": "hypervisor",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "hypervisor type of the hosts in zone that will be attached to this storage pool. KVM, VMware supported as of now."
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID for the storage pool"
        }
      ],
      "requiredparams": [
        "name",
        "url",
        "zoneid"
      ],
      "description": "Creates a storage pool."
    },
    "tags": {
      "name": "createTags",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "resourcetype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "type of the resource"
        },
        {
          "name": "tags",
          "required": True,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "Map of tags (key/value pairs)"
        },
        {
          "name": "customer",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "identifies client specific tag. When the value is not null, the tag can't be used by cloudStack code internally"
        },
        {
          "name": "resourceids",
          "required": True,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "list of resources to create the tags for"
        }
      ],
      "requiredparams": [
        "resourcetype",
        "tags",
        "resourceids"
      ],
      "description": "Creates resource tag(s)"
    },
    "staticroute": {
      "name": "createStaticRoute",
      "related": [
        "listStaticRoutes"
      ],
      "isasync": True,
      "params": [
        {
          "name": "cidr",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "static route cidr"
        },
        {
          "name": "gatewayid",
          "required": True,
          "related": [
            "createPrivateGateway"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the gateway id we are creating static route for"
        }
      ],
      "requiredparams": [
        "cidr",
        "gatewayid"
      ],
      "description": "Creates a static route"
    },
    "volume": {
      "name": "createVolume",
      "related": [
        "uploadVolume"
      ],
      "isasync": True,
      "params": [
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the disk volume"
        },
        {
          "name": "size",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "Arbitrary volume size"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the project associated with the volume. Mutually exclusive with account parameter"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the account associated with the disk volume. Must be used with the domainId parameter."
        },
        {
          "name": "miniops",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "min iops"
        },
        {
          "name": "maxiops",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "max iops"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the availability zone"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the domain ID associated with the disk offering. If used with the account parameter returns the disk volume associated with the account for the specified domain."
        },
        {
          "name": "snapshotid",
          "required": False,
          "related": [
            "createSnapshot",
            "revertSnapshot"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the snapshot ID for the disk volume. Either diskOfferingId or snapshotId must be passed in."
        },
        {
          "name": "diskofferingid",
          "required": False,
          "related": [
            "createDiskOffering"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the disk offering. Either diskOfferingId or snapshotId must be passed in."
        },
        {
          "name": "virtualmachineid",
          "required": False,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "updateVirtualMachine",
            "changeServiceForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the virtual machine; to be used with snapshot Id, VM to which the volume gets attached after creation"
        },
        {
          "name": "displayvolume",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "an optional field, whether to display the volume to the end user or not."
        }
      ],
      "requiredparams": [
        "name"
      ],
      "description": "Creates a disk volume from a disk offering. This disk volume must still be attached to a virtual machine to make use of it."
    },
    "user": {
      "name": "createUser",
      "related": [
        "disableUser",
        "getUser",
        "lockUser",
        "listUsers",
        "updateUser"
      ],
      "isasync": False,
      "params": [
        {
          "name": "password",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Clear text password (Default hashed to SHA256SALT). If you wish to use any other hashing algorithm, you would need to write a custom authentication adapter See Docs section."
        },
        {
          "name": "account",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Creates the user under the specified account. If no account is specified, the username will be used as the account name."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Creates the user under the specified domain. Has to be accompanied with the account parameter"
        },
        {
          "name": "userid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "User UUID, required for adding account from external provisioning system"
        },
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Unique username."
        },
        {
          "name": "email",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "email"
        },
        {
          "name": "timezone",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Specifies a timezone for this command. For more information on the timezone parameter, see Time Zone Format."
        },
        {
          "name": "firstname",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "firstname"
        },
        {
          "name": "lastname",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "lastname"
        }
      ],
      "requiredparams": [
        "password",
        "account",
        "username",
        "email",
        "firstname",
        "lastname"
      ],
      "description": "Creates a user for an account that already exists"
    },
    "portableiprange": {
      "name": "createPortableIpRange",
      "related": [
        "listPortableIpRanges"
      ],
      "isasync": True,
      "params": [
        {
          "name": "regionid",
          "required": True,
          "related": [
            "listRegions",
            "updateRegion",
            "addRegion"
          ],
          "length": 255,
          "type": "integer",
          "description": "Id of the Region"
        },
        {
          "name": "vlan",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "VLAN id, if not specified defaulted to untagged"
        },
        {
          "name": "gateway",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the gateway for the portable IP range"
        },
        {
          "name": "startip",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the beginning IP address in the portable IP range"
        },
        {
          "name": "netmask",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the netmask of the portable IP range"
        },
        {
          "name": "endip",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the ending IP address in the portable IP range"
        }
      ],
      "requiredparams": [
        "regionid",
        "gateway",
        "startip",
        "netmask",
        "endip"
      ],
      "description": "adds a range of portable public IP's to a region"
    },
    "storagenetworkiprange": {
      "name": "createStorageNetworkIpRange",
      "related": [
        "listStorageNetworkIpRange",
        "updateStorageNetworkIpRange"
      ],
      "isasync": True,
      "params": [
        {
          "name": "endip",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the ending IP address"
        },
        {
          "name": "netmask",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the netmask for storage network"
        },
        {
          "name": "gateway",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the gateway for storage network"
        },
        {
          "name": "startip",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the beginning IP address"
        },
        {
          "name": "vlan",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "Optional. The vlan the ip range sits on, default to Null when it is not specificed which means you network is not on any Vlan. This is mainly for Vmware as other hypervisors can directly reterive bridge from pyhsical network traffic type table"
        },
        {
          "name": "podid",
          "required": True,
          "related": [
            "createPod",
            "updatePod",
            "listPods"
          ],
          "length": 255,
          "type": "uuid",
          "description": "UUID of pod where the ip range belongs to"
        }
      ],
      "requiredparams": [
        "netmask",
        "gateway",
        "startip",
        "podid"
      ],
      "description": "Creates a Storage network IP range."
    },
    "condition": {
      "name": "createCondition",
      "related": [
        "listConditions"
      ],
      "isasync": True,
      "params": [
        {
          "name": "relationaloperator",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Relational Operator to be used with threshold."
        },
        {
          "name": "counterid",
          "required": True,
          "related": [
            "createCounter",
            "listCounters"
          ],
          "length": 255,
          "type": "uuid",
          "description": "ID of the Counter."
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the account of the condition. Must be used with the domainId parameter."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the domain ID of the account."
        },
        {
          "name": "threshold",
          "required": True,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "Threshold value."
        }
      ],
      "requiredparams": [
        "relationaloperator",
        "counterid",
        "threshold"
      ],
      "description": "Creates a condition"
    },
    "autoscalevmprofile": {
      "name": "createAutoScaleVmProfile",
      "related": [
        "listAutoScaleVmProfiles",
        "updateAutoScaleVmProfile"
      ],
      "isasync": True,
      "params": [
        {
          "name": "counterparam",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "counterparam list. Example: counterparam[0].name=snmpcommunity&counterparam[0].value=public&counterparam[1].name=snmpport&counterparam[1].value=161"
        },
        {
          "name": "autoscaleuserid",
          "required": False,
          "related": [
            "createUser",
            "disableUser",
            "getUser",
            "lockUser",
            "enableUser",
            "listUsers",
            "updateUser"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the user used to launch and destroy the VMs"
        },
        {
          "name": "templateid",
          "required": True,
          "related": [
            "registerIso",
            "prepareTemplate",
            "listIsos",
            "copyIso",
            "registerTemplate",
            "updateIso",
            "updateTemplate",
            "listTemplates"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the template of the auto deployed virtual machine"
        },
        {
          "name": "otherdeployparams",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "parameters other than zoneId/serviceOfferringId/templateId of the auto deployed virtual machine"
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "availability zone for the auto deployed virtual machine"
        },
        {
          "name": "destroyvmgraceperiod",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the time allowed for existing connections to get closed before a vm is destroyed"
        },
        {
          "name": "serviceofferingid",
          "required": True,
          "related": [
            "createServiceOffering",
            "listServiceOfferings",
            "updateServiceOffering"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the service offering of the auto deployed virtual machine"
        }
      ],
      "requiredparams": [
        "templateid",
        "zoneid",
        "serviceofferingid"
      ],
      "description": "Creates a profile that contains information about the virtual machine which will be provisioned automatically by autoscale feature."
    },
    "affinitygroup": {
      "name": "createAffinityGroup",
      "related": [
        "listAffinityGroups"
      ],
      "isasync": True,
      "params": [
        {
          "name": "type",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Type of the affinity group from the available affinity/anti-affinity group types"
        },
        {
          "name": "description",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "optional description of the affinity group"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of the affinity group"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "an account for the affinity group. Must be used with domainId."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "domainId of the account owning the affinity group"
        }
      ],
      "requiredparams": [
        "type",
        "name"
      ],
      "description": "Creates an affinity/anti-affinity group"
    },
    "account": {
      "name": "createAccount",
      "related": [
        "listAccounts",
        "markDefaultZoneForAccount",
        "disableAccount"
      ],
      "isasync": False,
      "params": [
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Unique username."
        },
        {
          "name": "accountid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Account UUID, required for adding account from external provisioning system"
        },
        {
          "name": "accountdetails",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "details for account used to store specific parameters"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Creates the user under the specified domain."
        },
        {
          "name": "timezone",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Specifies a timezone for this command. For more information on the timezone parameter, see Time Zone Format."
        },
        {
          "name": "email",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "email"
        },
        {
          "name": "networkdomain",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Network domain for the account's networks"
        },
        {
          "name": "userid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "User UUID, required for adding account from external provisioning system"
        },
        {
          "name": "firstname",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "firstname"
        },
        {
          "name": "lastname",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "lastname"
        },
        {
          "name": "password",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Clear text password (Default hashed to SHA256SALT). If you wish to use any other hashing algorithm, you would need to write a custom authentication adapter See Docs section."
        },
        {
          "name": "accounttype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "short",
          "description": "Type of the account.  Specify 0 for user, 1 for root admin, and 2 for domain admin"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Creates the user under the specified account. If no account is specified, the username will be used as the account name."
        }
      ],
      "requiredparams": [
        "username",
        "email",
        "firstname",
        "lastname",
        "password",
        "accounttype"
      ],
      "description": "Creates an account"
    },
    "firewallrule": {
      "name": "createFirewallRule",
      "related": [
        "listEgressFirewallRules"
      ],
      "isasync": True,
      "params": [
        {
          "name": "cidrlist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "the cidr list to forward traffic from"
        },
        {
          "name": "type",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "type of firewallrule: system/user"
        },
        {
          "name": "icmptype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "type of the icmp message being sent"
        },
        {
          "name": "protocol",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the protocol for the firewall rule. Valid values are TCP/UDP/ICMP."
        },
        {
          "name": "startport",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the starting port of firewall rule"
        },
        {
          "name": "endport",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the ending port of firewall rule"
        },
        {
          "name": "ipaddressid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the IP address id of the port forwarding rule"
        },
        {
          "name": "icmpcode",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "error code for this icmp message"
        }
      ],
      "requiredparams": [
        "protocol",
        "ipaddressid"
      ],
      "description": "Creates a firewall rule for a given ip address"
    },
    "networkoffering": {
      "name": "createNetworkOffering",
      "related": [
        "updateNetworkOffering"
      ],
      "isasync": False,
      "params": [
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 4096,
          "type": "string",
          "description": "the tags for the network offering."
        },
        {
          "name": "networkrate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "data transfer rate in megabits per second allowed"
        },
        {
          "name": "supportedservices",
          "required": True,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "services supported by the network offering"
        },
        {
          "name": "serviceproviderlist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "provider to service mapping. If not specified, the provider for the service will be mapped to the default provider on the physical network"
        },
        {
          "name": "conservemode",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if the network offering is IP conserve mode enabled"
        },
        {
          "name": "guestiptype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "guest type of the network offering: Shared or Isolated"
        },
        {
          "name": "maxconnections",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "maximum number of concurrent connections supported by the network offering"
        },
        {
          "name": "availability",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the availability of network offering. Default value is Optional"
        },
        {
          "name": "specifyipranges",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if network offering supports specifying ip ranges; defaulted to False if not specified"
        },
        {
          "name": "servicecapabilitylist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "desired service capabilities as part of network offering"
        },
        {
          "name": "ispersistent",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if network offering supports persistent networks; defaulted to False if not specified"
        },
        {
          "name": "keepaliveenabled",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "if True keepalive will be turned on in the loadbalancer. At the time of writing this has only an effect on haproxy; the mode http and httpclose options are unset in the haproxy conf file."
        },
        {
          "name": "details",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "Network offering details in key/value pairs. Supported keys are internallbprovider/publiclbprovider with service provider as a value"
        },
        {
          "name": "serviceofferingid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the service offering ID used by virtual router provider"
        },
        {
          "name": "displaytext",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the display text of the network offering"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the network offering"
        },
        {
          "name": "specifyvlan",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if network offering supports vlans"
        },
        {
          "name": "egressdefaultpolicy",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if default guest network egress policy is allow; False if default egress policy is deny"
        },
        {
          "name": "traffictype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the traffic type for the network offering. Supported type in current release is GUEST only"
        }
      ],
      "requiredparams": [
        "supportedservices",
        "guestiptype",
        "displaytext",
        "name",
        "traffictype"
      ],
      "description": "Creates a network offering."
    },
    "vpncustomergateway": {
      "name": "createVpnCustomerGateway",
      "related": [
        "updateVpnCustomerGateway",
        "listVpnCustomerGateways"
      ],
      "isasync": True,
      "params": [
        {
          "name": "dpd",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If DPD is enabled for VPN connection"
        },
        {
          "name": "ikelifetime",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "Lifetime of phase 1 VPN connection to the customer gateway, in seconds"
        },
        {
          "name": "esplifetime",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "Lifetime of phase 2 VPN connection to the customer gateway, in seconds"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the domain ID associated with the gateway. If used with the account parameter returns the gateway associated with the account for the specified domain."
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of this customer gateway"
        },
        {
          "name": "ipsecpsk",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "IPsec Preshared-Key of the customer gateway"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the account associated with the gateway. Must be used with the domainId parameter."
        },
        {
          "name": "esppolicy",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "ESP policy of the customer gateway"
        },
        {
          "name": "ikepolicy",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "IKE policy of the customer gateway"
        },
        {
          "name": "gateway",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "public ip address id of the customer gateway"
        },
        {
          "name": "cidrlist",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "guest cidr list of the customer gateway"
        }
      ],
      "requiredparams": [
        "ipsecpsk",
        "esppolicy",
        "ikepolicy",
        "gateway",
        "cidrlist"
      ],
      "description": "Creates site to site vpn customer gateway"
    },
    "internalloadbalancerelement": {
      "name": "createInternalLoadBalancerElement",
      "related": [
        "configureInternalLoadBalancerElement"
      ],
      "isasync": True,
      "params": [
        {
          "name": "nspid",
          "required": True,
          "related": [
            "listTrafficTypes",
            "updateNetworkServiceProvider",
            "addNetworkServiceProvider"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the network service provider ID of the internal load balancer element"
        }
      ],
      "requiredparams": [
        "nspid"
      ],
      "description": "Create an Internal Load Balancer element."
    },
    "privategateway": {
      "name": "createPrivateGateway",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "networkofferingid",
          "required": False,
          "related": [
            "createNetworkOffering",
            "updateNetworkOffering"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the uuid of the network offering to use for the private gateways network connection"
        },
        {
          "name": "vpcid",
          "required": True,
          "related": [
            "restartVPC"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the VPC network belongs to"
        },
        {
          "name": "sourcenatsupported",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "source NAT supported value. Default value False. If 'True' source NAT is enabled on the private gateway 'False': sourcenat is not supported"
        },
        {
          "name": "physicalnetworkid",
          "required": False,
          "related": [
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID the network belongs to"
        },
        {
          "name": "gateway",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the gateway of the Private gateway"
        },
        {
          "name": "ipaddress",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the IP address of the Private gateaway"
        },
        {
          "name": "vlan",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the network implementation uri for the private gateway"
        },
        {
          "name": "aclid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the network ACL"
        },
        {
          "name": "netmask",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the netmask of the Private gateway"
        }
      ],
      "requiredparams": [
        "vpcid",
        "gateway",
        "ipaddress",
        "vlan",
        "netmask"
      ],
      "description": "Creates a private gateway"
    },
    "counter": {
      "name": "createCounter",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "source",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Source of the counter."
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Name of the counter."
        },
        {
          "name": "value",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Value of the counter e.g. oid in case of snmp."
        }
      ],
      "requiredparams": [
        "source",
        "name",
        "value"
      ],
      "description": "Adds metric counter"
    },
    "lbhealthcheckpolicy": {
      "name": "createLBHealthCheckPolicy",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "intervaltime",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "Amount of time between health checks (1 sec - 20940 sec)"
        },
        {
          "name": "unhealthythreshold",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "Number of consecutive health check failures before declaring an instance unhealthy"
        },
        {
          "name": "healthythreshold",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "Number of consecutive health check success before declaring an instance healthy"
        },
        {
          "name": "lbruleid",
          "required": True,
          "related": [
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the load balancer rule"
        },
        {
          "name": "pingpath",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "HTTP Ping Path"
        },
        {
          "name": "description",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the description of the load balancer HealthCheck policy"
        },
        {
          "name": "responsetimeout",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "Time to wait when receiving a response from the health check (2sec - 60 sec)"
        }
      ],
      "requiredparams": [
        "lbruleid"
      ],
      "description": "Creates a Load Balancer healthcheck policy "
    },
    "project": {
      "name": "createProject",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "domainid",
          "required": False,
          "related": [
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "domain ID of the account owning a project"
        },
        {
          "name": "displaytext",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "display text of the project"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of the project"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "account who will be Admin for the project"
        }
      ],
      "requiredparams": [
        "displaytext",
        "name"
      ],
      "description": "Creates a project"
    },
    "physicalnetwork": {
      "name": "createPhysicalNetwork",
      "related": [
        "listPhysicalNetworks"
      ],
      "isasync": True,
      "params": [
        {
          "name": "vlan",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the VLAN for the physical network"
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "Tag the physical network"
        },
        {
          "name": "broadcastdomainrange",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the broadcast domain range for the physical network[Pod or Zone]. In Acton release it can be Zone only in Advance zone, and Pod in Basic"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the physical network"
        },
        {
          "name": "networkspeed",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the speed for the physical network[1G/10G]"
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID for the physical network"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "domain ID of the account owning a physical network"
        },
        {
          "name": "isolationmethods",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "the isolation method for the physical network[VLAN/L3/GRE]"
        }
      ],
      "requiredparams": [
        "name",
        "zoneid"
      ],
      "description": "Creates a physical network"
    },
    "snapshot": {
      "name": "createSnapshot",
      "related": [
        "revertSnapshot"
      ],
      "isasync": True,
      "params": [
        {
          "name": "domainid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "The domain ID of the snapshot. If used with the account parameter, specifies a domain for the account associated with the disk volume."
        },
        {
          "name": "policyid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "policy id of the snapshot, if this is null, then use MANUAL_POLICY."
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The account of the snapshot. The account parameter must be used with the domainId parameter."
        },
        {
          "name": "quiescevm",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "quiesce vm if True"
        },
        {
          "name": "volumeid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the disk volume"
        }
      ],
      "requiredparams": [
        "volumeid"
      ],
      "description": "Creates an instant snapshot of a volume."
    },
    "virtualrouterelement": {
      "name": "createVirtualRouterElement",
      "related": [
        "configureVirtualRouterElement"
      ],
      "isasync": True,
      "params": [
        {
          "name": "nspid",
          "required": True,
          "related": [
            "updateNetworkServiceProvider",
            "addNetworkServiceProvider"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the network service provider ID of the virtual router element"
        },
        {
          "name": "providertype",
          "required": False,
          "related": [
            "updateNetworkServiceProvider",
            "addNetworkServiceProvider"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The provider type. Supported types are VirtualRouter (default) and VPCVirtualRouter"
        }
      ],
      "requiredparams": [
        "nspid"
      ],
      "description": "Create a virtual router element."
    },
    "egressfirewallrule": {
      "name": "createEgressFirewallRule",
      "related": [
        "listFirewallRules",
        "listEgressFirewallRules",
        "createFirewallRule"
      ],
      "isasync": True,
      "params": [
        {
          "name": "networkid",
          "required": True,
          "related": [
            "listSrxFirewallNetworks",
            "updateNetwork",
            "listF5LoadBalancerNetworks",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the network id of the port forwarding rule"
        },
        {
          "name": "startport",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the starting port of firewall rule"
        },
        {
          "name": "type",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "type of firewallrule: system/user"
        },
        {
          "name": "icmpcode",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "error code for this icmp message"
        },
        {
          "name": "cidrlist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "the cidr list to forward traffic from"
        },
        {
          "name": "protocol",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the protocol for the firewall rule. Valid values are TCP/UDP/ICMP."
        },
        {
          "name": "icmptype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "type of the icmp message being sent"
        },
        {
          "name": "endport",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the ending port of firewall rule"
        }
      ],
      "requiredparams": [
        "networkid",
        "protocol"
      ],
      "description": "Creates a egress firewall rule for a given network "
    },
    "sshkeypair": {
      "name": "createSSHKeyPair",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "an optional account for the ssh key. Must be used with domainId."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional domainId for the ssh key. If the account parameter is used, domainId must also be used."
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "activateProject",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional project for the ssh key"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Name of the keypair"
        }
      ],
      "requiredparams": [
        "name"
      ],
      "description": "Create a new keypair and returns the private key"
    },
    "loadbalancer": {
      "name": "createLoadBalancer",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "sourceport",
          "required": True,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the source port the network traffic will be load balanced from"
        },
        {
          "name": "sourceipaddress",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the source ip address the network traffic will be load balanced from"
        },
        {
          "name": "sourceipaddressnetworkid",
          "required": True,
          "related": [
            "listSrxFirewallNetworks",
            "updateNetwork",
            "listF5LoadBalancerNetworks",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the network id of the source ip address"
        },
        {
          "name": "algorithm",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "load balancer algorithm (source, roundrobin, leastconn)"
        },
        {
          "name": "networkid",
          "required": True,
          "related": [
            "listSrxFirewallNetworks",
            "updateNetwork",
            "listF5LoadBalancerNetworks",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The guest network the Load Balancer will be created for"
        },
        {
          "name": "description",
          "required": False,
          "related": [],
          "length": 4096,
          "type": "string",
          "description": "the description of the Load Balancer"
        },
        {
          "name": "scheme",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the load balancer scheme. Supported value in this release is Internal"
        },
        {
          "name": "instanceport",
          "required": True,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the TCP port of the virtual machine where the network traffic will be load balanced to"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of the Load Balancer"
        }
      ],
      "requiredparams": [
        "sourceport",
        "sourceipaddressnetworkid",
        "algorithm",
        "networkid",
        "scheme",
        "instanceport",
        "name"
      ],
      "description": "Creates a Load Balancer"
    }
  },
  "associate": {
    "ipaddress": {
      "name": "associateIpAddress",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the availability zone you want to acquire an public IP address from"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the account to associate with this IP address"
        },
        {
          "name": "networkid",
          "required": False,
          "related": [
            "updateNetwork",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The network this ip address should be associated to."
        },
        {
          "name": "isportable",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "should be set to True if public IP is required to be transferable across zones, if not specified defaults to False"
        },
        {
          "name": "regionid",
          "required": False,
          "related": [
            "addRegion"
          ],
          "length": 255,
          "type": "integer",
          "description": "region ID from where portable ip is to be associated."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the domain to associate with this IP address"
        },
        {
          "name": "vpcid",
          "required": False,
          "related": [
            "listVPCs",
            "restartVPC"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the VPC you want the ip address to be associated with"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Deploy vm for the project"
        }
      ],
      "requiredparams": [],
      "description": "Acquires and associates a public IP to an account."
    },
    "ucsprofiletoblade": {
      "name": "associateUcsProfileToBlade",
      "related": [
        "listUcsBlades",
        "disassociateUcsProfileFromBlade",
        "instantiateUcsTemplateAndAssocaciateToBlade",
        "refreshUcsBlades"
      ],
      "isasync": True,
      "params": [
        {
          "name": "profiledn",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "profile dn"
        },
        {
          "name": "bladeid",
          "required": True,
          "related": [
            "listUcsBlades",
            "disassociateUcsProfileFromBlade",
            "instantiateUcsTemplateAndAssocaciateToBlade",
            "refreshUcsBlades",
            "associateUcsProfileToBlade"
          ],
          "length": 255,
          "type": "uuid",
          "description": "blade id"
        },
        {
          "name": "ucsmanagerid",
          "required": True,
          "related": [
            "addUcsManager"
          ],
          "length": 255,
          "type": "uuid",
          "description": "ucs manager id"
        }
      ],
      "requiredparams": [
        "profiledn",
        "bladeid",
        "ucsmanagerid"
      ],
      "description": "associate a profile to a blade"
    }
  },
  "reboot": {
    "systemvm": {
      "name": "rebootSystemVm",
      "related": [
        "scaleSystemVm"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "rebootSystemVm",
            "scaleSystemVm"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the system virtual machine"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Reboots a system VM."
    },
    "router": {
      "name": "rebootRouter",
      "related": [
        "startRouter",
        "stopInternalLoadBalancerVM",
        "listInternalLoadBalancerVMs",
        "changeServiceForRouter"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "startRouter",
            "stopInternalLoadBalancerVM",
            "listInternalLoadBalancerVMs",
            "rebootRouter",
            "changeServiceForRouter"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the router"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Starts a router."
    },
    "virtualmachine": {
      "name": "rebootVirtualMachine",
      "related": [
        "detachIso",
        "migrateVirtualMachineWithVolume",
        "updateVMAffinityGroup",
        "startVirtualMachine",
        "migrateVirtualMachine",
        "stopVirtualMachine",
        "removeNicFromVirtualMachine",
        "updateVirtualMachine",
        "changeServiceForVirtualMachine",
        "updateDefaultNicForVirtualMachine",
        "revertToVMSnapshot",
        "listVirtualMachines",
        "resetPasswordForVirtualMachine",
        "assignVirtualMachine",
        "destroyVirtualMachine",
        "restoreVirtualMachine"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the virtual machine"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Reboots a virtual machine."
    }
  },
  "find": {
    "hostsformigration": {
      "name": "findHostsForMigration",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "virtualmachineid",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "attachIso",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "find hosts to which this VM can be migrated and flag the hosts with enough CPU/RAM to host the VM"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        }
      ],
      "requiredparams": [
        "virtualmachineid"
      ],
      "description": "Find hosts suitable for migrating a virtual machine."
    },
    "storagepoolsformigration": {
      "name": "findStoragePoolsForMigration",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the volume"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Lists storage pools available for migration of a volume."
    }
  },
  "attach": {
    "volume": {
      "name": "attachVolume",
      "related": [
        "uploadVolume",
        "resizeVolume",
        "updateVolume",
        "createVolume",
        "detachVolume"
      ],
      "isasync": True,
      "params": [
        {
          "name": "virtualmachineid",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "recoverVirtualMachine",
            "deployVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "resetSSHKeyForVirtualMachine",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "attachIso",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "    the ID of the virtual machine"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "uploadVolume",
            "resizeVolume",
            "updateVolume",
            "createVolume",
            "detachVolume",
            "attachVolume"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the disk volume"
        },
        {
          "name": "deviceid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "the ID of the device to map the volume to within the guest OS. If no deviceId is passed in, the next available deviceId will be chosen. Possible values for a Linux OS are:* 1 - /dev/xvdb* 2 - /dev/xvdc* 4 - /dev/xvde* 5 - /dev/xvdf* 6 - /dev/xvdg* 7 - /dev/xvdh* 8 - /dev/xvdi* 9 - /dev/xvdj"
        }
      ],
      "requiredparams": [
        "virtualmachineid",
        "id"
      ],
      "description": "Attaches a disk volume to a virtual machine."
    },
    "iso": {
      "name": "attachIso",
      "related": [
        "detachIso",
        "migrateVirtualMachineWithVolume",
        "updateVMAffinityGroup",
        "startVirtualMachine",
        "migrateVirtualMachine",
        "stopVirtualMachine",
        "rebootVirtualMachine",
        "removeNicFromVirtualMachine",
        "updateVirtualMachine",
        "changeServiceForVirtualMachine",
        "updateDefaultNicForVirtualMachine",
        "revertToVMSnapshot",
        "listVirtualMachines",
        "resetPasswordForVirtualMachine",
        "assignVirtualMachine",
        "destroyVirtualMachine",
        "restoreVirtualMachine"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "registerIso",
            "prepareTemplate",
            "listIsos",
            "copyIso",
            "updateIso",
            "updateTemplate",
            "listTemplates"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the ISO file"
        },
        {
          "name": "virtualmachineid",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "attachIso",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the virtual machine"
        }
      ],
      "requiredparams": [
        "id",
        "virtualmachineid"
      ],
      "description": "Attaches an ISO to a virtual machine."
    }
  },
  "add": {
    "networkserviceprovider": {
      "name": "addNetworkServiceProvider",
      "related": [
        "updateNetworkServiceProvider"
      ],
      "isasync": True,
      "params": [
        {
          "name": "servicelist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "the list of services to be enabled for this physical network service provider"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name for the physical network service provider"
        },
        {
          "name": "destinationphysicalnetworkid",
          "required": False,
          "related": [
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the destination Physical Network ID to bridge to"
        },
        {
          "name": "physicalnetworkid",
          "required": True,
          "related": [
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID to add the provider to"
        }
      ],
      "requiredparams": [
        "name",
        "physicalnetworkid"
      ],
      "description": "Adds a network serviceProvider to a physical network"
    },
    "ciscoasa1000vresource": {
      "name": "addCiscoAsa1000vResource",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "insideportprofile",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Nexus port profile associated with inside interface of ASA 1000v"
        },
        {
          "name": "clusterid",
          "required": True,
          "related": [
            "updateCluster"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Cluster ID"
        },
        {
          "name": "physicalnetworkid",
          "required": True,
          "related": [
            "createPhysicalNetwork",
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        },
        {
          "name": "hostname",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Hostname or ip address of the Cisco ASA 1000v appliance."
        }
      ],
      "requiredparams": [
        "insideportprofile",
        "clusterid",
        "physicalnetworkid",
        "hostname"
      ],
      "description": "Adds a Cisco Asa 1000v appliance"
    },
    "nictovirtualmachine": {
      "name": "addNicToVirtualMachine",
      "related": [
        "detachIso",
        "migrateVirtualMachineWithVolume",
        "updateVMAffinityGroup",
        "startVirtualMachine",
        "migrateVirtualMachine",
        "listLoadBalancerRuleInstances",
        "stopVirtualMachine",
        "rebootVirtualMachine",
        "removeNicFromVirtualMachine",
        "updateVirtualMachine",
        "recoverVirtualMachine",
        "deployVirtualMachine",
        "changeServiceForVirtualMachine",
        "updateDefaultNicForVirtualMachine",
        "revertToVMSnapshot",
        "resetSSHKeyForVirtualMachine",
        "listVirtualMachines",
        "resetPasswordForVirtualMachine",
        "assignVirtualMachine",
        "attachIso",
        "destroyVirtualMachine",
        "restoreVirtualMachine"
      ],
      "isasync": True,
      "params": [
        {
          "name": "ipaddress",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "IP Address for the new network"
        },
        {
          "name": "virtualmachineid",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "listLoadBalancerRuleInstances",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "recoverVirtualMachine",
            "deployVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "resetSSHKeyForVirtualMachine",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "addNicToVirtualMachine",
            "attachIso",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Virtual Machine ID"
        },
        {
          "name": "networkid",
          "required": True,
          "related": [
            "createNetwork",
            "listSrxFirewallNetworks",
            "listNetworks",
            "updateNetwork",
            "listF5LoadBalancerNetworks",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Network ID"
        }
      ],
      "requiredparams": [
        "virtualmachineid",
        "networkid"
      ],
      "description": "Adds VM to specified network by creating a NIC"
    },
    "accounttoproject": {
      "name": "addAccountToProject",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "projectid",
          "required": True,
          "related": [
            "createProject",
            "activateProject",
            "listProjects",
            "suspendProject",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of the project to add the account to"
        },
        {
          "name": "email",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "email to which invitation to the project is going to be sent"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of the account to be added to the project"
        }
      ],
      "requiredparams": [
        "projectid"
      ],
      "description": "Adds acoount to a project"
    },
    "externalloadbalancer": {
      "name": "addExternalLoadBalancer",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Username of the external load balancer appliance."
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "URL of the external load balancer appliance."
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Zone in which to add the external load balancer appliance."
        },
        {
          "name": "password",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Password of the external load balancer appliance."
        }
      ],
      "requiredparams": [
        "username",
        "url",
        "zoneid",
        "password"
      ],
      "description": "Adds F5 external load balancer appliance."
    },
    "cluster": {
      "name": "addCluster",
      "related": [
        "updateCluster",
        "listClusters"
      ],
      "isasync": False,
      "params": [
        {
          "name": "publicvswitchname",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Name of virtual switch used for public traffic in the cluster.  This would override zone wide traffic label setting."
        },
        {
          "name": "password",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the password for the host"
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID for the cluster"
        },
        {
          "name": "podid",
          "required": True,
          "related": [
            "createPod",
            "updatePod",
            "listPods"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Pod ID for the host"
        },
        {
          "name": "guestvswitchtype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Type of virtual switch used for guest traffic in the cluster. Allowed values are, vmwaresvs (for VMware standard vSwitch) and vmwaredvs (for VMware distributed vSwitch)"
        },
        {
          "name": "vsmusername",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the username for the VSM associated with this cluster"
        },
        {
          "name": "clustername",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the cluster name"
        },
        {
          "name": "url",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the URL"
        },
        {
          "name": "vsmipaddress",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the ipaddress of the VSM associated with this cluster"
        },
        {
          "name": "hypervisor",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "hypervisor type of the cluster: XenServer,KVM,VMware,Hyperv,BareMetal,Simulator"
        },
        {
          "name": "publicvswitchtype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Type of virtual switch used for public traffic in the cluster. Allowed values are, vmwaresvs (for VMware standard vSwitch) and vmwaredvs (for VMware distributed vSwitch)"
        },
        {
          "name": "guestvswitchname",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Name of virtual switch used for guest traffic in the cluster. This would override zone wide traffic label setting."
        },
        {
          "name": "username",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the username for the cluster"
        },
        {
          "name": "allocationstate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Allocation state of this cluster for allocation of new resources"
        },
        {
          "name": "clustertype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "type of the cluster: CloudManaged, ExternalManaged"
        },
        {
          "name": "vsmpassword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the password for the VSM associated with this cluster"
        }
      ],
      "requiredparams": [
        "zoneid",
        "podid",
        "clustername",
        "hypervisor",
        "clustertype"
      ],
      "description": "Adds a new cluster"
    },
    "networkdevice": {
      "name": "addNetworkDevice",
      "related": [
        "listNetworkDevice"
      ],
      "isasync": False,
      "params": [
        {
          "name": "networkdevicetype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Network device type, now supports ExternalDhcp, PxeServer, NetscalerMPXLoadBalancer, NetscalerVPXLoadBalancer, NetscalerSDXLoadBalancer, F5BigIpLoadBalancer, JuniperSRXFirewall, PaloAltoFirewall"
        },
        {
          "name": "networkdeviceparameterlist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "parameters for network device"
        }
      ],
      "requiredparams": [],
      "description": "Adds a network device of one of the following types: ExternalDhcp, ExternalFirewall, ExternalLoadBalancer, PxeServer"
    },
    "vmwaredc": {
      "name": "addVmwareDc",
      "related": [
        "listVmwareDcs"
      ],
      "isasync": False,
      "params": [
        {
          "name": "zoneid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "The Zone ID."
        },
        {
          "name": "password",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The password for specified username."
        },
        {
          "name": "username",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The Username required to connect to resource."
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Name of VMware datacenter to be added to specified zone."
        },
        {
          "name": "vcenter",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The name/ip of vCenter. Make sure it is IP address or full qualified domain name for host running vCenter server."
        }
      ],
      "requiredparams": [
        "zoneid",
        "name",
        "vcenter"
      ],
      "description": "Adds a VMware datacenter to specified zone"
    },
    "baremetalpxekickstartserver": {
      "name": "addBaremetalPxeKickStartServer",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "pxeservertype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "type of pxe device"
        },
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Credentials to reach external pxe device"
        },
        {
          "name": "podid",
          "required": False,
          "related": [
            "updatePod"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Pod Id"
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "URL of the external pxe device"
        },
        {
          "name": "tftpdir",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Tftp root directory of PXE server"
        },
        {
          "name": "physicalnetworkid",
          "required": True,
          "related": [
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        },
        {
          "name": "password",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Credentials to reach external pxe device"
        }
      ],
      "requiredparams": [
        "pxeservertype",
        "username",
        "url",
        "tftpdir",
        "physicalnetworkid",
        "password"
      ],
      "description": "add a baremetal pxe server"
    },
    "baremetalpxepingserver": {
      "name": "addBaremetalPxePingServer",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "tftpdir",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Tftp root directory of PXE server"
        },
        {
          "name": "physicalnetworkid",
          "required": True,
          "related": [
            "createPhysicalNetwork",
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        },
        {
          "name": "podid",
          "required": False,
          "related": [
            "createPod",
            "updatePod",
            "listPods"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Pod Id"
        },
        {
          "name": "pingdir",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Root directory on PING storage server"
        },
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Credentials to reach external pxe device"
        },
        {
          "name": "pxeservertype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "type of pxe device"
        },
        {
          "name": "pingcifspassword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Password of PING storage server"
        },
        {
          "name": "password",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Credentials to reach external pxe device"
        },
        {
          "name": "pingstorageserverip",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "PING storage server ip"
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "URL of the external pxe device"
        },
        {
          "name": "pingcifsusername",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Username of PING storage server"
        }
      ],
      "requiredparams": [
        "tftpdir",
        "physicalnetworkid",
        "pingdir",
        "username",
        "pxeservertype",
        "password",
        "pingstorageserverip",
        "url"
      ],
      "description": "add a baremetal ping pxe server"
    },
    "s3": {
      "name": "addS3",
      "related": [
        "listSwifts",
        "addImageStore",
        "createSecondaryStagingStore",
        "listSecondaryStagingStores"
      ],
      "isasync": False,
      "params": [
        {
          "name": "connectiontimeout",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "connection timeout (milliseconds)"
        },
        {
          "name": "maxerrorretry",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "maximum number of times to retry on error"
        },
        {
          "name": "secretkey",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "S3 secret key"
        },
        {
          "name": "endpoint",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "S3 host name"
        },
        {
          "name": "usehttps",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "connect to the S3 endpoint via HTTPS?"
        },
        {
          "name": "accesskey",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "S3 access key"
        },
        {
          "name": "bucket",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of the template storage bucket"
        },
        {
          "name": "sockettimeout",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "socket timeout (milliseconds)"
        }
      ],
      "requiredparams": [
        "secretkey",
        "accesskey",
        "bucket"
      ],
      "description": "Adds S3"
    },
    "bigswitchvnsdevice": {
      "name": "addBigSwitchVnsDevice",
      "related": [
        "listBigSwitchVnsDevices"
      ],
      "isasync": True,
      "params": [
        {
          "name": "hostname",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Hostname of ip address of the BigSwitch VNS Controller."
        },
        {
          "name": "physicalnetworkid",
          "required": True,
          "related": [
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        }
      ],
      "requiredparams": [
        "hostname",
        "physicalnetworkid"
      ],
      "description": "Adds a BigSwitch VNS device"
    },
    "ciscovnmcresource": {
      "name": "addCiscoVnmcResource",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "hostname",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Hostname or ip address of the Cisco VNMC Controller."
        },
        {
          "name": "physicalnetworkid",
          "required": True,
          "related": [
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        },
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Credentials to access the Cisco VNMC Controller API"
        },
        {
          "name": "password",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Credentials to access the Cisco VNMC Controller API"
        }
      ],
      "requiredparams": [
        "hostname",
        "physicalnetworkid",
        "username",
        "password"
      ],
      "description": "Adds a Cisco Vnmc Controller"
    },
    "ucsmanager": {
      "name": "addUcsManager",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "zoneid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the Zone id for the ucs manager"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of UCS manager"
        },
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the username of UCS"
        },
        {
          "name": "password",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the password of UCS"
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of UCS url"
        }
      ],
      "requiredparams": [
        "zoneid",
        "username",
        "password",
        "url"
      ],
      "description": "Adds a Ucs manager"
    },
    "niciranvpdevice": {
      "name": "addNiciraNvpDevice",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Credentials to access the Nicira Controller API"
        },
        {
          "name": "l3gatewayserviceuuid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The L3 Gateway Service UUID configured on the Nicira Controller"
        },
        {
          "name": "physicalnetworkid",
          "required": True,
          "related": [
            "createPhysicalNetwork",
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        },
        {
          "name": "password",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Credentials to access the Nicira Controller API"
        },
        {
          "name": "transportzoneuuid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The Transportzone UUID configured on the Nicira Controller"
        },
        {
          "name": "hostname",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Hostname of ip address of the Nicira NVP Controller."
        }
      ],
      "requiredparams": [
        "username",
        "physicalnetworkid",
        "password",
        "transportzoneuuid",
        "hostname"
      ],
      "description": "Adds a Nicira NVP device"
    },
    "baremetaldhcp": {
      "name": "addBaremetalDhcp",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "physicalnetworkid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        },
        {
          "name": "password",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Credentials to reach external dhcp device"
        },
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Credentials to reach external dhcp device"
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "URL of the external dhcp appliance."
        },
        {
          "name": "dhcpservertype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Type of dhcp device"
        }
      ],
      "requiredparams": [
        "physicalnetworkid",
        "password",
        "username",
        "url",
        "dhcpservertype"
      ],
      "description": "adds a baremetal dhcp server"
    },
    "trafficmonitor": {
      "name": "addTrafficMonitor",
      "related": [
        "listTrafficMonitors"
      ],
      "isasync": False,
      "params": [
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Zone in which to add the external firewall appliance."
        },
        {
          "name": "excludezones",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Traffic going into the listed zones will not be metered"
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "URL of the traffic monitor Host"
        },
        {
          "name": "includezones",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Traffic going into the listed zones will be metered"
        }
      ],
      "requiredparams": [
        "zoneid",
        "url"
      ],
      "description": "Adds Traffic Monitor Host for Direct Network Usage"
    },
    "ldapconfiguration": {
      "name": "addLdapConfiguration",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "hostname",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Hostname"
        },
        {
          "name": "port",
          "required": True,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "Port"
        }
      ],
      "requiredparams": [
        "hostname",
        "port"
      ],
      "description": "Add a new Ldap Configuration"
    },
    "vpnuser": {
      "name": "addVpnUser",
      "related": [
        "listVpnUsers"
      ],
      "isasync": True,
      "params": [
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "username for the vpn user"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional domainId for the vpn user. If the account parameter is used, domainId must also be used."
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "an optional account for the vpn user. Must be used with domainId."
        },
        {
          "name": "password",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "password for the username"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "add vpn user to the specific project"
        }
      ],
      "requiredparams": [
        "username",
        "password"
      ],
      "description": "Adds vpn users"
    },
    "traffictype": {
      "name": "addTrafficType",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "isolationmethod",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Used if physical network has multiple isolation types and traffic type is public. Choose which isolation method. Valid options currently 'vlan' or 'vxlan', defaults to 'vlan'."
        },
        {
          "name": "kvmnetworklabel",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The network name label of the physical device dedicated to this traffic on a KVM host"
        },
        {
          "name": "hypervnetworklabel",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The network name label of the physical device dedicated to this traffic on a Hyperv host"
        },
        {
          "name": "vmwarenetworklabel",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The network name label of the physical device dedicated to this traffic on a VMware host"
        },
        {
          "name": "vlan",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The VLAN id to be used for Management traffic by VMware host"
        },
        {
          "name": "physicalnetworkid",
          "required": True,
          "related": [
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        },
        {
          "name": "xennetworklabel",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The network name label of the physical device dedicated to this traffic on a XenServer host"
        },
        {
          "name": "traffictype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the trafficType to be added to the physical network"
        }
      ],
      "requiredparams": [
        "physicalnetworkid",
        "traffictype"
      ],
      "description": "Adds traffic type to a physical network"
    },
    "host": {
      "name": "addHost",
      "related": [
        "listExternalLoadBalancers",
        "updateHost",
        "listHosts",
        "prepareHostForMaintenance"
      ],
      "isasync": False,
      "params": [
        {
          "name": "podid",
          "required": True,
          "related": [
            "createPod",
            "updatePod"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Pod ID for the host"
        },
        {
          "name": "password",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the password for the host"
        },
        {
          "name": "clustername",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the cluster name for the host"
        },
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the username for the host"
        },
        {
          "name": "allocationstate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Allocation state of this Host for allocation of new resources"
        },
        {
          "name": "clusterid",
          "required": False,
          "related": [
            "updateCluster"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the cluster ID for the host"
        },
        {
          "name": "hosttags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "list of tags to be added to the host"
        },
        {
          "name": "hypervisor",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "hypervisor type of the host"
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the host URL"
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID for the host"
        }
      ],
      "requiredparams": [
        "podid",
        "password",
        "username",
        "hypervisor",
        "url",
        "zoneid"
      ],
      "description": "Adds a new host."
    },
    "srxfirewall": {
      "name": "addSrxFirewall",
      "related": [
        "listSrxFirewalls",
        "configureSrxFirewall"
      ],
      "isasync": True,
      "params": [
        {
          "name": "physicalnetworkid",
          "required": True,
          "related": [
            "createPhysicalNetwork",
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "URL of the SRX appliance."
        },
        {
          "name": "networkdevicetype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "supports only JuniperSRXFirewall"
        },
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Credentials to reach SRX firewall device"
        },
        {
          "name": "password",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Credentials to reach SRX firewall device"
        }
      ],
      "requiredparams": [
        "physicalnetworkid",
        "url",
        "networkdevicetype",
        "username",
        "password"
      ],
      "description": "Adds a SRX firewall device"
    },
    "swift": {
      "name": "addSwift",
      "related": [
        "listSwifts",
        "addImageStore",
        "createSecondaryStagingStore",
        "listSecondaryStagingStores",
        "addS3"
      ],
      "isasync": False,
      "params": [
        {
          "name": "username",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the username for swift"
        },
        {
          "name": "key",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": " key for the user for swift"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the account for swift"
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the URL for swift"
        }
      ],
      "requiredparams": [
        "url"
      ],
      "description": "Adds Swift."
    },
    "externalfirewall": {
      "name": "addExternalFirewall",
      "related": [
        "listExternalFirewalls"
      ],
      "isasync": False,
      "params": [
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Zone in which to add the external firewall appliance."
        },
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Username of the external firewall appliance."
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "URL of the external firewall appliance."
        },
        {
          "name": "password",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Password of the external firewall appliance."
        }
      ],
      "requiredparams": [
        "zoneid",
        "username",
        "url",
        "password"
      ],
      "description": "Adds an external firewall appliance"
    },
    "paloaltofirewall": {
      "name": "addPaloAltoFirewall",
      "related": [
        "configurePaloAltoFirewall",
        "listPaloAltoFirewalls"
      ],
      "isasync": True,
      "params": [
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Credentials to reach Palo Alto firewall device"
        },
        {
          "name": "networkdevicetype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "supports only PaloAltoFirewall"
        },
        {
          "name": "password",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Credentials to reach Palo Alto firewall device"
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "URL of the Palo Alto appliance."
        },
        {
          "name": "physicalnetworkid",
          "required": True,
          "related": [
            "createPhysicalNetwork",
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        }
      ],
      "requiredparams": [
        "username",
        "networkdevicetype",
        "password",
        "url",
        "physicalnetworkid"
      ],
      "description": "Adds a Palo Alto firewall device"
    },
    "netscalerloadbalancer": {
      "name": "addNetscalerLoadBalancer",
      "related": [
        "listNetscalerLoadBalancers",
        "configureNetscalerLoadBalancer"
      ],
      "isasync": True,
      "params": [
        {
          "name": "gslbproviderprivateip",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "public IP of the site"
        },
        {
          "name": "password",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Credentials to reach netscaler load balancer device"
        },
        {
          "name": "networkdevicetype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Netscaler device type supports NetscalerMPXLoadBalancer, NetscalerVPXLoadBalancer, NetscalerSDXLoadBalancer"
        },
        {
          "name": "gslbproviderpublicip",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "public IP of the site"
        },
        {
          "name": "gslbprovider",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if NetScaler device being added is for providing GSLB service"
        },
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Credentials to reach netscaler load balancer device"
        },
        {
          "name": "isexclusivegslbprovider",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if NetScaler device being added is for providing GSLB service exclusively and can not be used for LB"
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "URL of the netscaler load balancer appliance."
        },
        {
          "name": "physicalnetworkid",
          "required": True,
          "related": [
            "updatePhysicalNetwork",
            "createPhysicalNetwork",
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        }
      ],
      "requiredparams": [
        "password",
        "networkdevicetype",
        "username",
        "url",
        "physicalnetworkid"
      ],
      "description": "Adds a netscaler load balancer device"
    },
    "region": {
      "name": "addRegion",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Name of the region"
        },
        {
          "name": "id",
          "required": True,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "Id of the Region"
        },
        {
          "name": "endpoint",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Region service endpoint"
        }
      ],
      "requiredparams": [
        "name",
        "id",
        "endpoint"
      ],
      "description": "Adds a Region"
    },
    "stratospheressp": {
      "name": "addStratosphereSsp",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "username",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "stratosphere ssp api username"
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the zone ID"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "stratosphere ssp api name"
        },
        {
          "name": "tenantuuid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "stratosphere ssp tenant uuid"
        },
        {
          "name": "password",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "stratosphere ssp api password"
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "stratosphere ssp server url"
        }
      ],
      "requiredparams": [
        "zoneid",
        "name",
        "url"
      ],
      "description": "Adds stratosphere ssp server"
    },
    "secondarystorage": {
      "name": "addSecondaryStorage",
      "related": [
        "addSwift",
        "listSwifts",
        "addImageStore",
        "createSecondaryStagingStore",
        "listS3s",
        "listSecondaryStagingStores",
        "addS3",
        "listImageStores"
      ],
      "isasync": False,
      "params": [
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID for the secondary storage"
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the URL for the secondary storage"
        }
      ],
      "requiredparams": [
        "url"
      ],
      "description": "Adds secondary storage."
    },
    "f5loadbalancer": {
      "name": "addF5LoadBalancer",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "URL of the F5 load balancer appliance."
        },
        {
          "name": "physicalnetworkid",
          "required": True,
          "related": [
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        },
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Credentials to reach F5 BigIP load balancer device"
        },
        {
          "name": "networkdevicetype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "supports only F5BigIpLoadBalancer"
        },
        {
          "name": "password",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Credentials to reach F5 BigIP load balancer device"
        }
      ],
      "requiredparams": [
        "url",
        "physicalnetworkid",
        "username",
        "networkdevicetype",
        "password"
      ],
      "description": "Adds a F5 BigIP load balancer device"
    },
    "resourcedetail": {
      "name": "addResourceDetail",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "details",
          "required": True,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "Map of (key/value pairs)"
        },
        {
          "name": "resourcetype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "type of the resource"
        },
        {
          "name": "resourceid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "resource id to create the details for"
        }
      ],
      "requiredparams": [
        "details",
        "resourcetype",
        "resourceid"
      ],
      "description": "Adds detail for the Resource."
    },
    "imagestore": {
      "name": "addImageStore",
      "related": [
        "listSwifts",
        "createSecondaryStagingStore"
      ],
      "isasync": False,
      "params": [
        {
          "name": "details",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "the details for the image store. Example: details[0].key=accesskey&details[0].value=s389ddssaa&details[1].key=secretkey&details[1].value=8dshfsss"
        },
        {
          "name": "url",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the URL for the image store"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID for the image store"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name for the image store"
        },
        {
          "name": "provider",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the image store provider name"
        }
      ],
      "requiredparams": [
        "provider"
      ],
      "description": "Adds backup image store."
    },
    "baremetalhost": {
      "name": "addBaremetalHost",
      "related": [
        "listExternalLoadBalancers",
        "addHost",
        "updateHost",
        "listHosts",
        "prepareHostForMaintenance"
      ],
      "isasync": False,
      "params": [
        {
          "name": "ipaddress",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "ip address intentionally allocated to this host after provisioning"
        },
        {
          "name": "password",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the password for the host"
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the host URL"
        },
        {
          "name": "hosttags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "list of tags to be added to the host"
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID for the host"
        },
        {
          "name": "clusterid",
          "required": False,
          "related": [
            "updateCluster"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the cluster ID for the host"
        },
        {
          "name": "hypervisor",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "hypervisor type of the host"
        },
        {
          "name": "clustername",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the cluster name for the host"
        },
        {
          "name": "allocationstate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Allocation state of this Host for allocation of new resources"
        },
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the username for the host"
        },
        {
          "name": "podid",
          "required": True,
          "related": [
            "createPod",
            "updatePod",
            "listPods"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Pod ID for the host"
        }
      ],
      "requiredparams": [
        "password",
        "url",
        "zoneid",
        "hypervisor",
        "username",
        "podid"
      ],
      "description": "add a baremetal host"
    },
    "iptonic": {
      "name": "addIpToNic",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "nicid",
          "required": True,
          "related": [
            "listNics"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the nic to which you want to assign private IP"
        },
        {
          "name": "ipaddress",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Secondary IP Address"
        }
      ],
      "requiredparams": [
        "nicid"
      ],
      "description": "Assigns secondary IP to NIC"
    }
  },
  "verbs": [
    "authorize",
    "restore",
    "suspend",
    "revoke",
    "disassociate",
    "migrate",
    "lock",
    "dedicate",
    "activate",
    "refresh",
    "reconnect",
    "cancel",
    "query",
    "recover",
    "extract",
    "archive",
    "detach",
    "prepare",
    "start",
    "revert",
    "create",
    "associate",
    "reboot",
    "find",
    "attach",
    "add",
    "restart",
    "deploy",
    "ldap",
    "destroy",
    "enable",
    "configure",
    "get",
    "stop",
    "update",
    "change",
    "replace",
    "disable",
    "scale",
    "import",
    "copy",
    "generate",
    "resize",
    "reset",
    "expunge",
    "upgrade",
    "register",
    "list",
    "upload",
    "remove",
    "mark",
    "instantiate",
    "clean",
    "release",
    "assign",
    "delete"
  ],
  "restart": {
    "network": {
      "name": "restartNetwork",
      "related": [
        "associateIpAddress"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listSrxFirewallNetworks",
            "updateNetwork",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The id of the network to restart."
        },
        {
          "name": "cleanup",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If cleanup old network elements"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Restarts the network; includes 1) restarting network elements - virtual routers, dhcp servers 2) reapplying all public ips 3) reapplying loadBalancing/portForwarding rules"
    },
    "vpc": {
      "name": "restartVPC",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "restartVPC"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the id of the VPC"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Restarts a VPC"
    }
  },
  "deploy": {
    "virtualmachine": {
      "name": "deployVirtualMachine",
      "related": [
        "detachIso",
        "migrateVirtualMachineWithVolume",
        "updateVMAffinityGroup",
        "startVirtualMachine",
        "migrateVirtualMachine",
        "stopVirtualMachine",
        "rebootVirtualMachine",
        "removeNicFromVirtualMachine",
        "updateVirtualMachine",
        "changeServiceForVirtualMachine",
        "updateDefaultNicForVirtualMachine",
        "revertToVMSnapshot",
        "listVirtualMachines",
        "resetPasswordForVirtualMachine",
        "assignVirtualMachine",
        "attachIso",
        "destroyVirtualMachine",
        "restoreVirtualMachine"
      ],
      "isasync": True,
      "params": [
        {
          "name": "startvm",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if network offering supports specifying ip ranges; defaulted to True if not specified"
        },
        {
          "name": "displayvm",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "an optional field, whether to the display the vm to the end user or not."
        },
        {
          "name": "diskofferingid",
          "required": False,
          "related": [
            "listDiskOfferings",
            "createDiskOffering"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the disk offering for the virtual machine. If the template is of ISO format, the diskOfferingId is for the root disk volume. Otherwise this parameter is used to indicate the offering for the data disk volume. If the templateId parameter passed is from a Template object, the diskOfferingId refers to a DATA Disk Volume created. If the templateId parameter passed is from an ISO object, the diskOfferingId refers to a ROOT Disk Volume created."
        },
        {
          "name": "group",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "an optional group for the virtual machine"
        },
        {
          "name": "iptonetworklist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "ip to network mapping. Can't be specified with networkIds parameter. Example: iptonetworklist[0].ip=10.10.10.11&iptonetworklist[0].ipv6=fc00:1234:5678::abcd&iptonetworklist[0].networkid=uuid - requests to use ip 10.10.10.11 in network id=uuid"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "an optional account for the virtual machine. Must be used with domainId."
        },
        {
          "name": "affinitygroupnames",
          "required": False,
          "related": [
            "listAffinityGroups"
          ],
          "length": 255,
          "type": "list",
          "description": "comma separated list of affinity groups names that are going to be applied to the virtual machine.Mutually exclusive with affinitygroupids parameter"
        },
        {
          "name": "keyboard",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "an optional keyboard device type for the virtual machine. valid value can be one of de,de-ch,es,fi,fr,fr-be,fr-ch,is,it,jp,nl-be,no,pt,uk,us"
        },
        {
          "name": "networkids",
          "required": False,
          "related": [
            "listSrxFirewallNetworks",
            "updateNetwork",
            "listF5LoadBalancerNetworks",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "list",
          "description": "list of network ids used by virtual machine. Can't be specified with ipToNetworkList parameter"
        },
        {
          "name": "ip6address",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the ipv6 address for default vm's network"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Deploy vm for the project"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional domainId for the virtual machine. If the account parameter is used, domainId must also be used."
        },
        {
          "name": "hostid",
          "required": False,
          "related": [
            "listExternalLoadBalancers",
            "addHost",
            "updateHost",
            "listHosts",
            "prepareHostForMaintenance"
          ],
          "length": 255,
          "type": "uuid",
          "description": "destination Host ID to deploy the VM to - parameter available for root admin only"
        },
        {
          "name": "details",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "used to specify the custom parameters."
        },
        {
          "name": "size",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "the arbitrary size for the DATADISK volume. Mutually exclusive with diskOfferingId"
        },
        {
          "name": "templateid",
          "required": True,
          "related": [
            "registerIso",
            "prepareTemplate",
            "listIsos",
            "copyIso",
            "registerTemplate",
            "updateIso",
            "updateTemplate",
            "listTemplates"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the template for the virtual machine"
        },
        {
          "name": "ipaddress",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the ip address for default vm's network"
        },
        {
          "name": "userdata",
          "required": False,
          "related": [],
          "length": 32768,
          "type": "string",
          "description": "an optional binary data that can be sent to the virtual machine upon a successful deployment. This binary data must be base64 encoded before adding it to the request. Using HTTP GET (via querystring), you can send up to 2KB of data after base64 encoding. Using HTTP POST(via POST body), you can send up to 32K of data after base64 encoding."
        },
        {
          "name": "securitygroupids",
          "required": False,
          "related": [
            "listSecurityGroups"
          ],
          "length": 255,
          "type": "list",
          "description": "comma separated list of security groups id that going to be applied to the virtual machine. Should be passed only when vm is created from a zone with Basic Network support. Mutually exclusive with securitygroupnames parameter"
        },
        {
          "name": "securitygroupnames",
          "required": False,
          "related": [
            "listSecurityGroups"
          ],
          "length": 255,
          "type": "list",
          "description": "comma separated list of security groups names that going to be applied to the virtual machine. Should be passed only when vm is created from a zone with Basic Network support. Mutually exclusive with securitygroupids parameter"
        },
        {
          "name": "serviceofferingid",
          "required": True,
          "related": [
            "createServiceOffering",
            "listServiceOfferings"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the service offering for the virtual machine"
        },
        {
          "name": "keypair",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of the ssh key pair used to login to the virtual machine"
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "availability zone for the virtual machine"
        },
        {
          "name": "affinitygroupids",
          "required": False,
          "related": [
            "listAffinityGroups"
          ],
          "length": 255,
          "type": "list",
          "description": "comma separated list of affinity groups id that are going to be applied to the virtual machine. Mutually exclusive with affinitygroupnames parameter"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "host name for the virtual machine"
        },
        {
          "name": "hypervisor",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the hypervisor on which to deploy the virtual machine"
        },
        {
          "name": "displayname",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "an optional user generated name for the virtual machine"
        }
      ],
      "requiredparams": [
        "templateid",
        "serviceofferingid",
        "zoneid"
      ],
      "description": "Creates and automatically starts a virtual machine based on a service offering, disk offering, and template."
    }
  },
  "ldap": {
    "createaccount": {
      "name": "ldapCreateAccount",
      "related": [
        "listAccounts",
        "markDefaultZoneForAccount",
        "createAccount",
        "disableAccount"
      ],
      "isasync": False,
      "params": [
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Creates the user under the specified domain."
        },
        {
          "name": "accountdetails",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "details for account used to store specific parameters"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Creates the user under the specified account. If no account is specified, the username will be used as the account name."
        },
        {
          "name": "networkdomain",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Network domain for the account's networks"
        },
        {
          "name": "accountid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Account UUID, required for adding account from external provisioning system"
        },
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Unique username."
        },
        {
          "name": "userid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "User UUID, required for adding account from external provisioning system"
        },
        {
          "name": "timezone",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Specifies a timezone for this command. For more information on the timezone parameter, see Time Zone Format."
        },
        {
          "name": "accounttype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "short",
          "description": "Type of the account.  Specify 0 for user, 1 for root admin, and 2 for domain admin"
        }
      ],
      "requiredparams": [
        "username",
        "accounttype"
      ],
      "description": "Creates an account from an LDAP user"
    }
  },
  "destroy": {
    "systemvm": {
      "name": "destroySystemVm",
      "related": [
        "migrateSystemVm",
        "changeServiceForSystemVm",
        "rebootSystemVm",
        "listSystemVms",
        "startSystemVm",
        "scaleSystemVm",
        "stopSystemVm"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "migrateSystemVm",
            "changeServiceForSystemVm",
            "destroySystemVm",
            "rebootSystemVm",
            "listSystemVms",
            "startSystemVm",
            "scaleSystemVm",
            "stopSystemVm"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the system virtual machine"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Destroyes a system virtual machine."
    },
    "router": {
      "name": "destroyRouter",
      "related": [
        "startRouter",
        "stopInternalLoadBalancerVM",
        "listInternalLoadBalancerVMs",
        "rebootRouter",
        "changeServiceForRouter"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "destroyRouter",
            "startRouter",
            "stopInternalLoadBalancerVM",
            "listInternalLoadBalancerVMs",
            "rebootRouter",
            "changeServiceForRouter"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the router"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Destroys a router."
    },
    "virtualmachine": {
      "name": "destroyVirtualMachine",
      "related": [
        "revertToVMSnapshot",
        "listVirtualMachines"
      ],
      "isasync": True,
      "params": [
        {
          "name": "expunge",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If True is passed, the vm is expunged immediately. False by default. Parameter can be passed to the call by ROOT/Domain admin only"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "revertToVMSnapshot",
            "listVirtualMachines",
            "destroyVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the virtual machine"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Destroys a virtual machine. Once destroyed, only the administrator can recover it."
    }
  },
  "reset": {
    "apilimit": {
      "name": "resetApiLimit",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "account",
          "required": False,
          "related": [
            "listAccounts",
            "markDefaultZoneForAccount"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the acount whose limit to be reset"
        }
      ],
      "requiredparams": [],
      "description": "Reset api count"
    },
    "sshkeyforvirtualmachine": {
      "name": "resetSSHKeyForVirtualMachine",
      "related": [
        "detachIso",
        "migrateVirtualMachineWithVolume",
        "updateVMAffinityGroup",
        "startVirtualMachine",
        "migrateVirtualMachine",
        "stopVirtualMachine",
        "rebootVirtualMachine",
        "removeNicFromVirtualMachine",
        "updateVirtualMachine",
        "recoverVirtualMachine",
        "deployVirtualMachine",
        "changeServiceForVirtualMachine",
        "updateDefaultNicForVirtualMachine",
        "revertToVMSnapshot",
        "listVirtualMachines",
        "resetPasswordForVirtualMachine",
        "assignVirtualMachine",
        "attachIso",
        "destroyVirtualMachine",
        "restoreVirtualMachine"
      ],
      "isasync": True,
      "params": [
        {
          "name": "keypair",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of the ssh key pair used to login to the virtual machine"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "an optional account for the ssh key. Must be used with domainId."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional domainId for the virtual machine. If the account parameter is used, domainId must also be used."
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "activateProject",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional project for the ssh key"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "recoverVirtualMachine",
            "deployVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "resetSSHKeyForVirtualMachine",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "attachIso",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the virtual machine"
        }
      ],
      "requiredparams": [
        "keypair",
        "id"
      ],
      "description": "Resets the SSH Key for virtual machine. The virtual machine must be in a \"Stopped\" state. [async]"
    },
    "passwordforvirtualmachine": {
      "name": "resetPasswordForVirtualMachine",
      "related": [
        "detachIso",
        "migrateVirtualMachineWithVolume",
        "startVirtualMachine",
        "migrateVirtualMachine",
        "stopVirtualMachine",
        "updateVirtualMachine",
        "changeServiceForVirtualMachine",
        "revertToVMSnapshot",
        "listVirtualMachines",
        "assignVirtualMachine",
        "destroyVirtualMachine",
        "restoreVirtualMachine"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "updateVirtualMachine",
            "changeServiceForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the virtual machine"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Resets the password for virtual machine. The virtual machine must be in a \"Stopped\" state and the template must already support this feature for this command to take effect. [async]"
    },
    "vpnconnection": {
      "name": "resetVpnConnection",
      "related": [
        "listVpnConnections"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "resetVpnConnection",
            "listVpnConnections"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of vpn connection"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional domainId for connection. If the account parameter is used, domainId must also be used."
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "an optional account for connection. Must be used with domainId."
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Reset site to site vpn connection"
    }
  },
  "enable": {
    "account": {
      "name": "enableAccount",
      "related": [
        "listAccounts",
        "ldapCreateAccount",
        "lockAccount",
        "markDefaultZoneForAccount",
        "createAccount",
        "disableAccount",
        "updateAccount"
      ],
      "isasync": False,
      "params": [
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Enables specified account in this domain."
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listAccounts",
            "ldapCreateAccount",
            "lockAccount",
            "markDefaultZoneForAccount",
            "createAccount",
            "enableAccount",
            "disableAccount",
            "updateAccount"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Account id"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Enables specified account."
        }
      ],
      "requiredparams": [],
      "description": "Enables an account"
    },
    "storagemaintenance": {
      "name": "enableStorageMaintenance",
      "related": [
        "findStoragePoolsForMigration",
        "updateStoragePool",
        "cancelStorageMaintenance",
        "createStoragePool",
        "listStoragePools"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "findStoragePoolsForMigration",
            "updateStoragePool",
            "cancelStorageMaintenance",
            "createStoragePool",
            "enableStorageMaintenance",
            "listStoragePools"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Primary storage ID"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Puts storage pool into maintenance state"
    },
    "cisconexusvsm": {
      "name": "enableCiscoNexusVSM",
      "related": [
        "disableCiscoNexusVSM"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "enableCiscoNexusVSM",
            "disableCiscoNexusVSM"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Id of the Cisco Nexus 1000v VSM device to be enabled"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Enable a Cisco Nexus VSM device"
    },
    "staticnat": {
      "name": "enableStaticNat",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "ipaddressid",
          "required": True,
          "related": [
            "associateIpAddress",
            "restartNetwork"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the public IP address id for which static nat feature is being enabled"
        },
        {
          "name": "networkid",
          "required": False,
          "related": [
            "listSrxFirewallNetworks",
            "updateNetwork",
            "listF5LoadBalancerNetworks",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The network of the vm the static nat will be enabled for. Required when public Ip address is not associated with any Guest network yet (VPC case)"
        },
        {
          "name": "virtualmachineid",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "recoverVirtualMachine",
            "deployVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "attachIso",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the virtual machine for enabling static nat feature"
        },
        {
          "name": "vmguestip",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "VM guest nic Secondary ip address for the port forwarding rule"
        }
      ],
      "requiredparams": [
        "ipaddressid",
        "virtualmachineid"
      ],
      "description": "Enables static nat for given ip address"
    },
    "user": {
      "name": "enableUser",
      "related": [
        "createUser",
        "disableUser",
        "getUser",
        "lockUser",
        "listUsers",
        "updateUser"
      ],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "createUser",
            "disableUser",
            "getUser",
            "lockUser",
            "enableUser",
            "listUsers",
            "updateUser"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Enables user by user ID."
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Enables a user account"
    },
    "autoscalevmgroup": {
      "name": "enableAutoScaleVmGroup",
      "related": [
        "updateAutoScaleVmGroup"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "enableAutoScaleVmGroup",
            "updateAutoScaleVmGroup"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the autoscale group"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Enables an AutoScale Vm Group"
    }
  },
  "configure": {
    "netscalerloadbalancer": {
      "name": "configureNetscalerLoadBalancer",
      "related": [
        "listNetscalerLoadBalancers"
      ],
      "isasync": True,
      "params": [
        {
          "name": "lbdevicecapacity",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "capacity of the device, Capacity will be interpreted as number of networks device can handle"
        },
        {
          "name": "inline",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if netscaler load balancer is intended to be used in in-line with firewall, False if netscaler load balancer will side-by-side with firewall"
        },
        {
          "name": "lbdevicededicated",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if this netscaler device to dedicated for a account, False if the netscaler device will be shared by multiple accounts"
        },
        {
          "name": "podids",
          "required": False,
          "related": [
            "createPod",
            "updatePod",
            "listPods"
          ],
          "length": 255,
          "type": "list",
          "description": "Used when NetScaler device is provider of EIP service. This parameter represents the list of pod's, for which there exists a policy based route on datacenter L3 router to route pod's subnet IP to a NetScaler device."
        },
        {
          "name": "lbdeviceid",
          "required": True,
          "related": [
            "listNetscalerLoadBalancers",
            "configureNetscalerLoadBalancer"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Netscaler load balancer device ID"
        }
      ],
      "requiredparams": [
        "lbdeviceid"
      ],
      "description": "configures a netscaler load balancer device"
    },
    "paloaltofirewall": {
      "name": "configurePaloAltoFirewall",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "fwdevicecapacity",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "capacity of the firewall device, Capacity will be interpreted as number of networks device can handle"
        },
        {
          "name": "fwdeviceid",
          "required": True,
          "related": [
            "configurePaloAltoFirewall"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Palo Alto firewall device ID"
        }
      ],
      "requiredparams": [
        "fwdeviceid"
      ],
      "description": "Configures a Palo Alto firewall device"
    },
    "f5loadbalancer": {
      "name": "configureF5LoadBalancer",
      "related": [
        "addF5LoadBalancer"
      ],
      "isasync": True,
      "params": [
        {
          "name": "lbdevicecapacity",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "capacity of the device, Capacity will be interpreted as number of networks device can handle"
        },
        {
          "name": "lbdeviceid",
          "required": True,
          "related": [
            "addF5LoadBalancer",
            "configureF5LoadBalancer"
          ],
          "length": 255,
          "type": "uuid",
          "description": "F5 load balancer device ID"
        }
      ],
      "requiredparams": [
        "lbdeviceid"
      ],
      "description": "configures a F5 load balancer device"
    },
    "virtualrouterelement": {
      "name": "configureVirtualRouterElement",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "configureVirtualRouterElement"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the virtual router provider"
        },
        {
          "name": "enabled",
          "required": True,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "Enabled/Disabled the service provider"
        }
      ],
      "requiredparams": [
        "id",
        "enabled"
      ],
      "description": "Configures a virtual router element."
    },
    "srxfirewall": {
      "name": "configureSrxFirewall",
      "related": [
        "listSrxFirewalls"
      ],
      "isasync": True,
      "params": [
        {
          "name": "fwdeviceid",
          "required": True,
          "related": [
            "listSrxFirewalls",
            "configureSrxFirewall"
          ],
          "length": 255,
          "type": "uuid",
          "description": "SRX firewall device ID"
        },
        {
          "name": "fwdevicecapacity",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "capacity of the firewall device, Capacity will be interpreted as number of networks device can handle"
        }
      ],
      "requiredparams": [
        "fwdeviceid"
      ],
      "description": "Configures a SRX firewall device"
    },
    "internalloadbalancerelement": {
      "name": "configureInternalLoadBalancerElement",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "enabled",
          "required": True,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "Enables/Disables the Internal Load Balancer element"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "configureInternalLoadBalancerElement"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the internal lb provider"
        }
      ],
      "requiredparams": [
        "enabled",
        "id"
      ],
      "description": "Configures an Internal Load Balancer element."
    }
  },
  "get": {
    "apilimit": {
      "name": "getApiLimit",
      "related": [
        "resetApiLimit"
      ],
      "isasync": False,
      "params": [],
      "requiredparams": [],
      "description": "Get API limit count for the caller"
    },
    "vmpassword": {
      "name": "getVMPassword",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "recoverVirtualMachine",
            "deployVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "resetSSHKeyForVirtualMachine",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "attachIso",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the virtual machine"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Returns an encrypted password for the VM"
    },
    "user": {
      "name": "getUser",
      "related": [
        "disableUser",
        "lockUser",
        "listUsers",
        "updateUser"
      ],
      "isasync": False,
      "params": [
        {
          "name": "userapikey",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "API key of the user"
        }
      ],
      "requiredparams": [
        "userapikey"
      ],
      "description": "Find user account by API key"
    },
    "cloudidentifier": {
      "name": "getCloudIdentifier",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "userid",
          "required": True,
          "related": [
            "lockUser",
            "listUsers"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the user ID for the cloud identifier"
        }
      ],
      "requiredparams": [
        "userid"
      ],
      "description": "Retrieves a cloud identifier."
    }
  },
  "stop": {
    "systemvm": {
      "name": "stopSystemVm",
      "related": [
        "migrateSystemVm",
        "changeServiceForSystemVm",
        "rebootSystemVm",
        "listSystemVms",
        "startSystemVm",
        "scaleSystemVm"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "migrateSystemVm",
            "changeServiceForSystemVm",
            "rebootSystemVm",
            "listSystemVms",
            "startSystemVm",
            "scaleSystemVm",
            "stopSystemVm"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the system virtual machine"
        },
        {
          "name": "forced",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "Force stop the VM.  The caller knows the VM is stopped."
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Stops a system VM."
    },
    "router": {
      "name": "stopRouter",
      "related": [
        "destroyRouter",
        "startRouter",
        "stopInternalLoadBalancerVM",
        "listInternalLoadBalancerVMs",
        "rebootRouter",
        "startInternalLoadBalancerVM",
        "changeServiceForRouter"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "destroyRouter",
            "stopRouter",
            "startRouter",
            "stopInternalLoadBalancerVM",
            "listInternalLoadBalancerVMs",
            "rebootRouter",
            "startInternalLoadBalancerVM",
            "changeServiceForRouter"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the router"
        },
        {
          "name": "forced",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "Force stop the VM. The caller knows the VM is stopped."
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Stops a router."
    },
    "internalloadbalancervm": {
      "name": "stopInternalLoadBalancerVM",
      "related": [
        "startRouter",
        "listInternalLoadBalancerVMs",
        "changeServiceForRouter"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "startRouter",
            "stopInternalLoadBalancerVM",
            "listInternalLoadBalancerVMs",
            "changeServiceForRouter"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the internal lb vm"
        },
        {
          "name": "forced",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "Force stop the VM. The caller knows the VM is stopped."
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Stops an Internal LB vm."
    },
    "virtualmachine": {
      "name": "stopVirtualMachine",
      "related": [
        "migrateVirtualMachineWithVolume",
        "revertToVMSnapshot",
        "listVirtualMachines",
        "destroyVirtualMachine"
      ],
      "isasync": True,
      "params": [
        {
          "name": "forced",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "Force stop the VM (vm is marked as Stopped even when command fails to be send to the backend).  The caller knows the VM is stopped."
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "migrateVirtualMachineWithVolume",
            "stopVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "destroyVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the virtual machine"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Stops a virtual machine."
    }
  },
  "update": {
    "loadbalancerrule": {
      "name": "updateLoadBalancerRule",
      "related": [
        "listLoadBalancerRules",
        "createLoadBalancerRule"
      ],
      "isasync": True,
      "params": [
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the load balancer rule"
        },
        {
          "name": "description",
          "required": False,
          "related": [],
          "length": 4096,
          "type": "string",
          "description": "the description of the load balancer rule"
        },
        {
          "name": "algorithm",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "load balancer algorithm (source, roundrobin, leastconn)"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the id of the load balancer rule to update"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates load balancer"
    },
    "domain": {
      "name": "updateDomain",
      "related": [
        "listDomainChildren"
      ],
      "isasync": False,
      "params": [
        {
          "name": "networkdomain",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Network domain for the domain's networks; empty string will update domainName with NULL value"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "updates domain with this name"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "ID of domain to update"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates a domain with a new name"
    },
    "instancegroup": {
      "name": "updateInstanceGroup",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "updateInstanceGroup"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Instance group ID"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "new instance group name"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates a vm group"
    },
    "diskoffering": {
      "name": "updateDiskOffering",
      "related": [
        "listDiskOfferings",
        "createDiskOffering"
      ],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listDiskOfferings",
            "updateDiskOffering",
            "createDiskOffering"
          ],
          "length": 255,
          "type": "uuid",
          "description": "ID of the disk offering"
        },
        {
          "name": "sortkey",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "sort key of the disk offering, integer"
        },
        {
          "name": "displayoffering",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "an optional field, whether to display the offering to the end user or not."
        },
        {
          "name": "displaytext",
          "required": False,
          "related": [],
          "length": 4096,
          "type": "string",
          "description": "updates alternate display text of the disk offering with this value"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "updates name of the disk offering with this value"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates a disk offering."
    },
    "virtualmachine": {
      "name": "updateVirtualMachine",
      "related": [
        "migrateVirtualMachineWithVolume",
        "stopVirtualMachine",
        "revertToVMSnapshot",
        "listVirtualMachines",
        "destroyVirtualMachine",
        "restoreVirtualMachine"
      ],
      "isasync": False,
      "params": [
        {
          "name": "isdynamicallyscalable",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if VM contains XS/VMWare tools inorder to support dynamic scaling of VM cpu/memory"
        },
        {
          "name": "userdata",
          "required": False,
          "related": [],
          "length": 32768,
          "type": "string",
          "description": "an optional binary data that can be sent to the virtual machine upon a successful deployment. This binary data must be base64 encoded before adding it to the request. Using HTTP GET (via querystring), you can send up to 2KB of data after base64 encoding. Using HTTP POST(via POST body), you can send up to 32K of data after base64 encoding."
        },
        {
          "name": "displayvm",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "an optional field, whether to the display the vm to the end user or not."
        },
        {
          "name": "displayname",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "user generated name"
        },
        {
          "name": "haenable",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if high-availability is enabled for the virtual machine, False otherwise"
        },
        {
          "name": "group",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "group of the virtual machine"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "migrateVirtualMachineWithVolume",
            "stopVirtualMachine",
            "updateVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the virtual machine"
        },
        {
          "name": "ostypeid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the OS type that best represents this VM."
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates properties of a virtual machine. The VM has to be stopped and restarted for the new properties to take effect. UpdateVirtualMachine does not first check whether the VM is stopped. Therefore, stop the VM manually before issuing this call."
    },
    "portforwardingrule": {
      "name": "updatePortForwardingRule",
      "related": [
        "listPortForwardingRules",
        "createPortForwardingRule",
        "listIpForwardingRules"
      ],
      "isasync": True,
      "params": [
        {
          "name": "privateip",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the private IP address of the port forwarding rule"
        },
        {
          "name": "protocol",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the protocol for the port fowarding rule. Valid values are TCP or UDP."
        },
        {
          "name": "ipaddressid",
          "required": True,
          "related": [
            "associateIpAddress",
            "restartNetwork"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the IP address id of the port forwarding rule"
        },
        {
          "name": "privateport",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the private port of the port forwarding rule"
        },
        {
          "name": "virtualmachineid",
          "required": False,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "deployVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "attachIso",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the virtual machine for the port forwarding rule"
        },
        {
          "name": "publicport",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the public port of the port forwarding rule"
        }
      ],
      "requiredparams": [
        "protocol",
        "ipaddressid",
        "privateport",
        "publicport"
      ],
      "description": "Updates a port forwarding rule.  Only the private port and the virtual machine can be updated."
    },
    "cluster": {
      "name": "updateCluster",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "clustername",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the cluster name"
        },
        {
          "name": "clustertype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "hypervisor type of the cluster"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "updateCluster"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Cluster"
        },
        {
          "name": "managedstate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "whether this cluster is managed by cloudstack"
        },
        {
          "name": "hypervisor",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "hypervisor type of the cluster"
        },
        {
          "name": "allocationstate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Allocation state of this cluster for allocation of new resources"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates an existing cluster"
    },
    "hostpassword": {
      "name": "updateHostPassword",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "clusterid",
          "required": False,
          "related": [
            "updateCluster"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the cluster ID"
        },
        {
          "name": "hostid",
          "required": False,
          "related": [
            "listExternalLoadBalancers",
            "addHost",
            "updateHost",
            "listHosts",
            "prepareHostForMaintenance"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the host ID"
        },
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the username for the host/cluster"
        },
        {
          "name": "password",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the new password for the host/cluster"
        }
      ],
      "requiredparams": [
        "username",
        "password"
      ],
      "description": "Update password of a host/pool on management server."
    },
    "pod": {
      "name": "updatePod",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "gateway",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the gateway for the Pod"
        },
        {
          "name": "netmask",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the netmask of the Pod"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the Pod"
        },
        {
          "name": "allocationstate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Allocation state of this cluster for allocation of new resources"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "updatePod"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Pod"
        },
        {
          "name": "startip",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the starting IP address for the Pod"
        },
        {
          "name": "endip",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the ending IP address for the Pod"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates a Pod."
    },
    "isopermissions": {
      "name": "updateIsoPermissions",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "isfeatured",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True for featured template/iso, False otherwise"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "registerIso",
            "prepareTemplate",
            "listIsos",
            "copyIso",
            "updateIso",
            "updateTemplate"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the template ID"
        },
        {
          "name": "accounts",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "a comma delimited list of accounts. If specified, \"op\" parameter has to be passed in."
        },
        {
          "name": "isextractable",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if the template/iso is extractable, False other wise. Can be set only by root admin"
        },
        {
          "name": "op",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "permission operator (add, remove, reset)"
        },
        {
          "name": "ispublic",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True for public template/iso, False for private templates/isos"
        },
        {
          "name": "projectids",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "list",
          "description": "a comma delimited list of projects. If specified, \"op\" parameter has to be passed in."
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates iso permissions"
    },
    "resourcelimit": {
      "name": "updateResourceLimit",
      "related": [
        "listResourceLimits"
      ],
      "isasync": False,
      "params": [
        {
          "name": "resourcetype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "Type of resource to update. Values are 0, 1, 2, 3, 4, 6, 7, 8, 9, 10 and 11. 0 - Instance. Number of instances a user can create. 1 - IP. Number of public IP addresses a user can own. 2 - Volume. Number of disk volumes a user can create.3 - Snapshot. Number of snapshots a user can create.4 - Template. Number of templates that a user can register/create.6 - Network. Number of guest network a user can create.7 - VPC. Number of VPC a user can create.8 - CPU. Total number of CPU cores a user can use.9 - Memory. Total Memory (in MB) a user can use.10 - PrimaryStorage. Total primary storage space (in GiB) a user can use.11 - SecondaryStorage. Total secondary storage space (in GiB) a user can use."
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Update resource limits for project"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Update resource for a specified account. Must be used with the domainId parameter."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Update resource limits for all accounts in specified domain. If used with the account parameter, updates resource limits for a specified account in specified domain."
        },
        {
          "name": "max",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "  Maximum resource limit."
        }
      ],
      "requiredparams": [
        "resourcetype"
      ],
      "description": "Updates resource limits for an account or domain."
    },
    "vpcoffering": {
      "name": "updateVPCOffering",
      "related": [
        "listVPCOfferings",
        "createVPCOffering"
      ],
      "isasync": True,
      "params": [
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "update state for the VPC offering; supported states - Enabled/Disabled"
        },
        {
          "name": "displaytext",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the display text of the VPC offering"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "listVPCOfferings",
            "updateVPCOffering",
            "createVPCOffering"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the id of the VPC offering"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the VPC offering"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates VPC offering"
    },
    "network": {
      "name": "updateNetwork",
      "related": [
        "listNetscalerLoadBalancerNetworks"
      ],
      "isasync": True,
      "params": [
        {
          "name": "networkofferingid",
          "required": False,
          "related": [
            "updateNetworkOffering"
          ],
          "length": 255,
          "type": "uuid",
          "description": "network offering ID"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the new name for the network"
        },
        {
          "name": "guestvmcidr",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "CIDR for Guest VMs,Cloudstack allocates IPs to Guest VMs only from this CIDR"
        },
        {
          "name": "changecidr",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "Force update even if cidr type is different"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "updateNetwork",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the network"
        },
        {
          "name": "networkdomain",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "network domain"
        },
        {
          "name": "displaynetwork",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "an optional field, whether to the display the network to the end user or not."
        },
        {
          "name": "displaytext",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the new display text for the network"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates a network"
    },
    "cloudtouseobjectstore": {
      "name": "updateCloudToUseObjectStore",
      "related": [
        "addSwift",
        "listSwifts",
        "addImageStore",
        "createSecondaryStagingStore",
        "listS3s",
        "listSecondaryStagingStores",
        "addS3",
        "listImageStores",
        "addSecondaryStorage"
      ],
      "isasync": False,
      "params": [
        {
          "name": "url",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the URL for the image store"
        },
        {
          "name": "provider",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the image store provider name"
        },
        {
          "name": "details",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "the details for the image store. Example: details[0].key=accesskey&details[0].value=s389ddssaa&details[1].key=secretkey&details[1].value=8dshfsss"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name for the image store"
        }
      ],
      "requiredparams": [
        "provider"
      ],
      "description": "Migrate current NFS secondary storages to use object store."
    },
    "projectinvitation": {
      "name": "updateProjectInvitation",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "projectid",
          "required": True,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of the project to join"
        },
        {
          "name": "token",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list invitations for specified account; this parameter has to be specified with domainId"
        },
        {
          "name": "accept",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "if True, accept the invitation, decline if False. True by default"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "account that is joining the project"
        }
      ],
      "requiredparams": [
        "projectid"
      ],
      "description": "Accepts or declines project invitation"
    },
    "autoscalepolicy": {
      "name": "updateAutoScalePolicy",
      "related": [
        "createAutoScalePolicy"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "updateAutoScalePolicy",
            "createAutoScalePolicy"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the autoscale policy"
        },
        {
          "name": "quiettime",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the cool down period for which the policy should not be evaluated after the action has been taken"
        },
        {
          "name": "conditionids",
          "required": False,
          "related": [
            "listConditions"
          ],
          "length": 255,
          "type": "list",
          "description": "the list of IDs of the conditions that are being evaluated on every interval"
        },
        {
          "name": "duration",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the duration for which the conditions have to be True before action is taken"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates an existing autoscale policy."
    },
    "globalloadbalancerrule": {
      "name": "updateGlobalLoadBalancerRule",
      "related": [
        "listGlobalLoadBalancerRules"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "updateGlobalLoadBalancerRule",
            "listGlobalLoadBalancerRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the global load balancer rule"
        },
        {
          "name": "gslblbmethod",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "load balancer algorithm (roundrobin, leastconn, proximity) that is used to distributed traffic across the zones participating in global server load balancing, if not specified defaults to 'round robin'"
        },
        {
          "name": "gslbstickysessionmethodname",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "session sticky method (sourceip) if not specified defaults to sourceip"
        },
        {
          "name": "description",
          "required": False,
          "related": [],
          "length": 4096,
          "type": "string",
          "description": "the description of the load balancer rule"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "update global load balancer rules."
    },
    "serviceoffering": {
      "name": "updateServiceOffering",
      "related": [
        "createServiceOffering",
        "listServiceOfferings"
      ],
      "isasync": False,
      "params": [
        {
          "name": "displaytext",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the display text of the service offering to be updated"
        },
        {
          "name": "sortkey",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "sort key of the service offering, integer"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the service offering to be updated"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "createServiceOffering",
            "listServiceOfferings",
            "updateServiceOffering"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the service offering to be updated"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates a service offering."
    },
    "storagepool": {
      "name": "updateStoragePool",
      "related": [
        "findStoragePoolsForMigration",
        "cancelStorageMaintenance",
        "createStoragePool",
        "listStoragePools"
      ],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "findStoragePoolsForMigration",
            "updateStoragePool",
            "cancelStorageMaintenance",
            "createStoragePool",
            "listStoragePools"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Id of the storage pool"
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "comma-separated list of tags for the storage pool"
        },
        {
          "name": "capacityiops",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "IOPS CloudStack can provision from this storage pool"
        },
        {
          "name": "capacitybytes",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "bytes CloudStack can provision from this storage pool"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates a storage pool."
    },
    "hypervisorcapabilities": {
      "name": "updateHypervisorCapabilities",
      "related": [
        "listHypervisorCapabilities"
      ],
      "isasync": False,
      "params": [
        {
          "name": "maxguestslimit",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "the max number of Guest VMs per host for this hypervisor."
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listHypervisorCapabilities",
            "updateHypervisorCapabilities"
          ],
          "length": 255,
          "type": "uuid",
          "description": "ID of the hypervisor capability"
        },
        {
          "name": "securitygroupenabled",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "set True to enable security group for this hypervisor."
        }
      ],
      "requiredparams": [],
      "description": "Updates a hypervisor capabilities."
    },
    "template": {
      "name": "updateTemplate",
      "related": [
        "registerIso",
        "listIsos",
        "copyIso",
        "updateIso"
      ],
      "isasync": False,
      "params": [
        {
          "name": "sortkey",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "sort key of the template, integer"
        },
        {
          "name": "ostypeid",
          "required": False,
          "related": [
            "listOsTypes"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the OS type that best represents the OS of this image."
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "registerIso",
            "listIsos",
            "copyIso",
            "updateIso",
            "updateTemplate"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the image file"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the image file"
        },
        {
          "name": "displaytext",
          "required": False,
          "related": [],
          "length": 4096,
          "type": "string",
          "description": "the display text of the image"
        },
        {
          "name": "isrouting",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if the template type is routing i.e., if template is used to deploy router"
        },
        {
          "name": "bootable",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if image is bootable, False otherwise"
        },
        {
          "name": "isdynamicallyscalable",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if template/ISO contains XS/VMWare tools inorder to support dynamic scaling of VM cpu/memory"
        },
        {
          "name": "passwordenabled",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if the image supports the password reset feature; default is False"
        },
        {
          "name": "format",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the format for the image"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates attributes of a template."
    },
    "defaultnicforvirtualmachine": {
      "name": "updateDefaultNicForVirtualMachine",
      "related": [
        "detachIso",
        "migrateVirtualMachineWithVolume",
        "startVirtualMachine",
        "migrateVirtualMachine",
        "stopVirtualMachine",
        "updateVirtualMachine",
        "changeServiceForVirtualMachine",
        "revertToVMSnapshot",
        "listVirtualMachines",
        "resetPasswordForVirtualMachine",
        "assignVirtualMachine",
        "destroyVirtualMachine",
        "restoreVirtualMachine"
      ],
      "isasync": True,
      "params": [
        {
          "name": "virtualmachineid",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "updateVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Virtual Machine ID"
        },
        {
          "name": "nicid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "NIC ID"
        }
      ],
      "requiredparams": [
        "virtualmachineid",
        "nicid"
      ],
      "description": "Changes the default NIC on a VM"
    },
    "volume": {
      "name": "updateVolume",
      "related": [
        "uploadVolume",
        "resizeVolume",
        "createVolume",
        "detachVolume"
      ],
      "isasync": True,
      "params": [
        {
          "name": "storageid",
          "required": False,
          "related": [
            "findStoragePoolsForMigration",
            "updateStoragePool",
            "cancelStorageMaintenance",
            "createStoragePool",
            "listStoragePools"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Destination storage pool UUID for the volume"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "uploadVolume",
            "resizeVolume",
            "updateVolume",
            "createVolume",
            "detachVolume"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the disk volume"
        },
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The state of the volume"
        },
        {
          "name": "displayvolume",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "an optional field, whether to the display the volume to the end user or not."
        },
        {
          "name": "path",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The path of the volume"
        }
      ],
      "requiredparams": [],
      "description": "Updates the volume."
    },
    "host": {
      "name": "updateHost",
      "related": [
        "listExternalLoadBalancers",
        "listHosts",
        "prepareHostForMaintenance"
      ],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listExternalLoadBalancers",
            "updateHost",
            "listHosts",
            "prepareHostForMaintenance"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the host to update"
        },
        {
          "name": "oscategoryid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the id of Os category to update the host with"
        },
        {
          "name": "allocationstate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Change resource state of host, valid values are [Enable, Disable]. Operation may failed if host in states not allowing Enable/Disable"
        },
        {
          "name": "url",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the new uri for the secondary storage: nfs://host/path"
        },
        {
          "name": "hosttags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "list of tags to be added to the host"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates a host."
    },
    "networkaclitem": {
      "name": "updateNetworkACLItem",
      "related": [
        "createNetworkACL"
      ],
      "isasync": True,
      "params": [
        {
          "name": "protocol",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the protocol for the ACL rule. Valid values are TCP/UDP/ICMP/ALL or valid protocol number"
        },
        {
          "name": "icmptype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "type of the icmp message being sent"
        },
        {
          "name": "number",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "The network of the vm the ACL will be created for"
        },
        {
          "name": "action",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "scl entry action, allow or deny"
        },
        {
          "name": "cidrlist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "the cidr list to allow traffic from/to"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "updateNetworkACLItem",
            "createNetworkACL"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the network ACL Item"
        },
        {
          "name": "traffictype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the traffic type for the ACL,can be Ingress or Egress, defaulted to Ingress if not specified"
        },
        {
          "name": "startport",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the starting port of ACL"
        },
        {
          "name": "endport",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the ending port of ACL"
        },
        {
          "name": "icmpcode",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "error code for this icmp message"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates ACL Item with specified Id"
    },
    "vpc": {
      "name": "updateVPC",
      "related": [
        "createVPC",
        "listVPCs",
        "restartVPC"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "createVPC",
            "listVPCs",
            "restartVPC",
            "updateVPC"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the id of the VPC"
        },
        {
          "name": "displaytext",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the display text of the VPC"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the VPC"
        }
      ],
      "requiredparams": [
        "id",
        "name"
      ],
      "description": "Updates a VPC"
    },
    "resourcecount": {
      "name": "updateResourceCount",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "domainid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "If account parameter specified then updates resource counts for a specified account in this domain else update resource counts for all accounts & child domains in specified domain."
        },
        {
          "name": "projectid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "Update resource limits for project"
        },
        {
          "name": "resourcetype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "Type of resource to update. If specifies valid values are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 and 11. If not specified will update all resource counts0 - Instance. Number of instances a user can create. 1 - IP. Number of public IP addresses a user can own. 2 - Volume. Number of disk volumes a user can create.3 - Snapshot. Number of snapshots a user can create.4 - Template. Number of templates that a user can register/create.5 - Project. Number of projects that a user can create.6 - Network. Number of guest network a user can create.7 - VPC. Number of VPC a user can create.8 - CPU. Total number of CPU cores a user can use.9 - Memory. Total Memory (in MB) a user can use.10 - PrimaryStorage. Total primary storage space (in GiB) a user can use.11 - SecondaryStorage. Total secondary storage space (in GiB) a user can use."
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Update resource count for a specified account. Must be used with the domainId parameter."
        }
      ],
      "requiredparams": [
        "domainid"
      ],
      "description": "Recalculate and update resource count for an account or domain."
    },
    "storagenetworkiprange": {
      "name": "updateStorageNetworkIpRange",
      "related": [
        "listStorageNetworkIpRange"
      ],
      "isasync": True,
      "params": [
        {
          "name": "vlan",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "Optional. the vlan the ip range sits on"
        },
        {
          "name": "endip",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the ending IP address"
        },
        {
          "name": "startip",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the beginning IP address"
        },
        {
          "name": "netmask",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the netmask for storage network"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "listStorageNetworkIpRange",
            "updateStorageNetworkIpRange"
          ],
          "length": 255,
          "type": "uuid",
          "description": "UUID of storage network ip range"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Update a Storage network IP range, only allowed when no IPs in this range have been allocated."
    },
    "configuration": {
      "name": "updateConfiguration",
      "related": [
        "listConfigurations"
      ],
      "isasync": False,
      "params": [
        {
          "name": "clusterid",
          "required": False,
          "related": [
            "updateCluster",
            "listClusters"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Cluster to update the parameter value for corresponding cluster"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the configuration"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Zone to update the parameter value for corresponding zone"
        },
        {
          "name": "value",
          "required": False,
          "related": [],
          "length": 4095,
          "type": "string",
          "description": "the value of the configuration"
        },
        {
          "name": "storageid",
          "required": False,
          "related": [
            "findStoragePoolsForMigration",
            "updateStoragePool",
            "cancelStorageMaintenance",
            "createStoragePool",
            "enableStorageMaintenance",
            "listStoragePools"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Storage pool to update the parameter value for corresponding storage pool"
        },
        {
          "name": "accountid",
          "required": False,
          "related": [
            "listAccounts",
            "ldapCreateAccount",
            "lockAccount",
            "markDefaultZoneForAccount",
            "createAccount",
            "enableAccount",
            "disableAccount",
            "updateAccount"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Account to update the parameter value for corresponding account"
        }
      ],
      "requiredparams": [
        "name"
      ],
      "description": "Updates a configuration."
    },
    "templatepermissions": {
      "name": "updateTemplatePermissions",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "op",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "permission operator (add, remove, reset)"
        },
        {
          "name": "accounts",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "a comma delimited list of accounts. If specified, \"op\" parameter has to be passed in."
        },
        {
          "name": "isfeatured",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True for featured template/iso, False otherwise"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "listIsos"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the template ID"
        },
        {
          "name": "isextractable",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if the template/iso is extractable, False other wise. Can be set only by root admin"
        },
        {
          "name": "ispublic",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True for public template/iso, False for private templates/isos"
        },
        {
          "name": "projectids",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "a comma delimited list of projects. If specified, \"op\" parameter has to be passed in."
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates a template visibility permissions. A public template is visible to all accounts within the same domain. A private template is visible only to the owner of the template. A priviledged template is a private template with account permissions added. Only accounts specified under the template permissions are visible to them."
    },
    "autoscalevmprofile": {
      "name": "updateAutoScaleVmProfile",
      "related": [
        "listAutoScaleVmProfiles"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listAutoScaleVmProfiles",
            "updateAutoScaleVmProfile"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the autoscale vm profile"
        },
        {
          "name": "counterparam",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "counterparam list. Example: counterparam[0].name=snmpcommunity&counterparam[0].value=public&counterparam[1].name=snmpport&counterparam[1].value=161"
        },
        {
          "name": "autoscaleuserid",
          "required": False,
          "related": [
            "createUser",
            "disableUser",
            "getUser",
            "lockUser",
            "enableUser",
            "listUsers",
            "updateUser"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the user used to launch and destroy the VMs"
        },
        {
          "name": "destroyvmgraceperiod",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the time allowed for existing connections to get closed before a vm is destroyed"
        },
        {
          "name": "templateid",
          "required": False,
          "related": [
            "registerIso",
            "prepareTemplate",
            "listIsos",
            "copyIso",
            "registerTemplate",
            "updateIso",
            "updateTemplate",
            "listTemplates"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the template of the auto deployed virtual machine"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates an existing autoscale vm profile."
    },
    "traffictype": {
      "name": "updateTrafficType",
      "related": [
        "addTrafficType"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "addTrafficType",
            "updateTrafficType"
          ],
          "length": 255,
          "type": "uuid",
          "description": "traffic type id"
        },
        {
          "name": "hypervnetworklabel",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The network name label of the physical device dedicated to this traffic on a Hyperv host"
        },
        {
          "name": "kvmnetworklabel",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The network name label of the physical device dedicated to this traffic on a KVM host"
        },
        {
          "name": "xennetworklabel",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The network name label of the physical device dedicated to this traffic on a XenServer host"
        },
        {
          "name": "vmwarenetworklabel",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The network name label of the physical device dedicated to this traffic on a VMware host"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates traffic type of a physical network"
    },
    "account": {
      "name": "updateAccount",
      "related": [
        "listAccounts",
        "ldapCreateAccount",
        "lockAccount",
        "markDefaultZoneForAccount",
        "createAccount",
        "disableAccount"
      ],
      "isasync": False,
      "params": [
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the domain where the account exists"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listAccounts",
            "ldapCreateAccount",
            "lockAccount",
            "markDefaultZoneForAccount",
            "createAccount",
            "disableAccount",
            "updateAccount"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Account id"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the current account name"
        },
        {
          "name": "newname",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "new name for the account"
        },
        {
          "name": "accountdetails",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "details for account used to store specific parameters"
        },
        {
          "name": "networkdomain",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Network domain for the account's networks; empty string will update domainName with NULL value"
        }
      ],
      "requiredparams": [
        "newname"
      ],
      "description": "Updates account information for the authenticated user"
    },
    "zone": {
      "name": "updateZone",
      "related": [
        "listZones",
        "createZone"
      ],
      "isasync": False,
      "params": [
        {
          "name": "dns2",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the second DNS for the Zone"
        },
        {
          "name": "ispublic",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "updates a private zone to public if set, but not vice-versa"
        },
        {
          "name": "internaldns2",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the second internal DNS for the Zone"
        },
        {
          "name": "details",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "the details for the Zone"
        },
        {
          "name": "dns1",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the first DNS for the Zone"
        },
        {
          "name": "domain",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Network domain name for the networks in the zone; empty string will update domain with NULL value"
        },
        {
          "name": "ip6dns1",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the first DNS for IPv6 network in the Zone"
        },
        {
          "name": "dnssearchorder",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "the dns search order list"
        },
        {
          "name": "internaldns1",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the first internal DNS for the Zone"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the Zone"
        },
        {
          "name": "guestcidraddress",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the guest CIDR address for the Zone"
        },
        {
          "name": "allocationstate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Allocation state of this cluster for allocation of new resources"
        },
        {
          "name": "dhcpprovider",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the dhcp Provider for the Zone"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Zone"
        },
        {
          "name": "localstorageenabled",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if local storage offering enabled, False otherwise"
        },
        {
          "name": "ip6dns2",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the second DNS for IPv6 network in the Zone"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates a Zone."
    },
    "vmaffinitygroup": {
      "name": "updateVMAffinityGroup",
      "related": [
        "detachIso",
        "migrateVirtualMachineWithVolume",
        "startVirtualMachine",
        "migrateVirtualMachine",
        "stopVirtualMachine",
        "removeNicFromVirtualMachine",
        "updateVirtualMachine",
        "changeServiceForVirtualMachine",
        "updateDefaultNicForVirtualMachine",
        "revertToVMSnapshot",
        "listVirtualMachines",
        "resetPasswordForVirtualMachine",
        "assignVirtualMachine",
        "destroyVirtualMachine",
        "restoreVirtualMachine"
      ],
      "isasync": True,
      "params": [
        {
          "name": "affinitygroupids",
          "required": False,
          "related": [
            "listAffinityGroups"
          ],
          "length": 255,
          "type": "list",
          "description": "comma separated list of affinity groups id that are going to be applied to the virtual machine. Should be passed only when vm is created from a zone with Basic Network support. Mutually exclusive with securitygroupnames parameter"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the virtual machine"
        },
        {
          "name": "affinitygroupnames",
          "required": False,
          "related": [
            "listAffinityGroups"
          ],
          "length": 255,
          "type": "list",
          "description": "comma separated list of affinity groups names that are going to be applied to the virtual machine. Should be passed only when vm is created from a zone with Basic Network support. Mutually exclusive with securitygroupids parameter"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates the affinity/anti-affinity group associations of a virtual machine. The VM has to be stopped and restarted for the new properties to take effect."
    },
    "physicalnetwork": {
      "name": "updatePhysicalNetwork",
      "related": [
        "createPhysicalNetwork",
        "listPhysicalNetworks"
      ],
      "isasync": True,
      "params": [
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "Tag the physical network"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "updatePhysicalNetwork",
            "createPhysicalNetwork",
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "physical network id"
        },
        {
          "name": "vlan",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the VLAN for the physical network"
        },
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Enabled/Disabled"
        },
        {
          "name": "networkspeed",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the speed for the physical network[1G/10G]"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates a physical network"
    },
    "region": {
      "name": "updateRegion",
      "related": [
        "listRegions",
        "addRegion"
      ],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "Id of region to update"
        },
        {
          "name": "endpoint",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "updates region with this end point"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "updates region with this name"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates a region"
    },
    "networkoffering": {
      "name": "updateNetworkOffering",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "update state for the network offering"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the network offering"
        },
        {
          "name": "sortkey",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "sort key of the network offering, integer"
        },
        {
          "name": "maxconnections",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "maximum number of concurrent connections supported by the network offering"
        },
        {
          "name": "availability",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the availability of network offering. Default value is Required for Guest Virtual network offering; Optional for Guest Direct network offering"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "updateNetworkOffering"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the id of the network offering"
        },
        {
          "name": "keepaliveenabled",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "if True keepalive will be turned on in the loadbalancer. At the time of writing this has only an effect on haproxy; the mode http and httpclose options are unset in the haproxy conf file."
        },
        {
          "name": "displaytext",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the display text of the network offering"
        }
      ],
      "requiredparams": [],
      "description": "Updates a network offering."
    },
    "project": {
      "name": "updateProject",
      "related": [
        "createProject"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of the project to be modified"
        },
        {
          "name": "displaytext",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "display text of the project"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "new Admin account for the project"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates a project"
    },
    "vpncustomergateway": {
      "name": "updateVpnCustomerGateway",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "dpd",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If DPD is enabled for VPN connection"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "updateVpnCustomerGateway"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of customer gateway"
        },
        {
          "name": "ipsecpsk",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "IPsec Preshared-Key of the customer gateway"
        },
        {
          "name": "gateway",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "public ip address id of the customer gateway"
        },
        {
          "name": "ikelifetime",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "Lifetime of phase 1 VPN connection to the customer gateway, in seconds"
        },
        {
          "name": "ikepolicy",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "IKE policy of the customer gateway"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of this customer gateway"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the account associated with the gateway. Must be used with the domainId parameter."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the domain ID associated with the gateway. If used with the account parameter returns the gateway associated with the account for the specified domain."
        },
        {
          "name": "esppolicy",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "ESP policy of the customer gateway"
        },
        {
          "name": "esplifetime",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "Lifetime of phase 2 VPN connection to the customer gateway, in seconds"
        },
        {
          "name": "cidrlist",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "guest cidr of the customer gateway"
        }
      ],
      "requiredparams": [
        "id",
        "ipsecpsk",
        "gateway",
        "ikepolicy",
        "esppolicy",
        "cidrlist"
      ],
      "description": "Update site to site vpn customer gateway"
    },
    "iso": {
      "name": "updateIso",
      "related": [
        "listIsos"
      ],
      "isasync": False,
      "params": [
        {
          "name": "ostypeid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the OS type that best represents the OS of this image."
        },
        {
          "name": "sortkey",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "sort key of the template, integer"
        },
        {
          "name": "isrouting",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if the template type is routing i.e., if template is used to deploy router"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the image file"
        },
        {
          "name": "isdynamicallyscalable",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if template/ISO contains XS/VMWare tools inorder to support dynamic scaling of VM cpu/memory"
        },
        {
          "name": "displaytext",
          "required": False,
          "related": [],
          "length": 4096,
          "type": "string",
          "description": "the display text of the image"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "listIsos",
            "updateIso"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the image file"
        },
        {
          "name": "passwordenabled",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if the image supports the password reset feature; default is False"
        },
        {
          "name": "format",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the format for the image"
        },
        {
          "name": "bootable",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if image is bootable, False otherwise"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates an ISO file."
    },
    "networkserviceprovider": {
      "name": "updateNetworkServiceProvider",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "updateNetworkServiceProvider"
          ],
          "length": 255,
          "type": "uuid",
          "description": "network service provider id"
        },
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Enabled/Disabled/Shutdown the physical network service provider"
        },
        {
          "name": "servicelist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "the list of services to be enabled for this physical network service provider"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates a network serviceProvider of a physical network"
    },
    "autoscalevmgroup": {
      "name": "updateAutoScaleVmGroup",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "maxmembers",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the maximum number of members in the vmgroup, The number of instances in the vm group will be equal to or less than this number."
        },
        {
          "name": "scaleuppolicyids",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "list of scaleup autoscale policies"
        },
        {
          "name": "scaledownpolicyids",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "list of scaledown autoscale policies"
        },
        {
          "name": "minmembers",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the minimum number of members in the vmgroup, the number of instances in the vm group will be equal to or more than this number."
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "updateAutoScaleVmGroup"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the autoscale group"
        },
        {
          "name": "interval",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the frequency at which the conditions have to be evaluated"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates an existing autoscale vm group."
    },
    "user": {
      "name": "updateUser",
      "related": [
        "disableUser",
        "lockUser",
        "listUsers"
      ],
      "isasync": False,
      "params": [
        {
          "name": "timezone",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Specifies a timezone for this command. For more information on the timezone parameter, see Time Zone Format."
        },
        {
          "name": "userapikey",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The API key for the user. Must be specified with userSecretKey"
        },
        {
          "name": "email",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "email"
        },
        {
          "name": "firstname",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "first name"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "disableUser",
            "lockUser",
            "listUsers",
            "updateUser"
          ],
          "length": 255,
          "type": "uuid",
          "description": "User uuid"
        },
        {
          "name": "usersecretkey",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The secret key for the user. Must be specified with userApiKey"
        },
        {
          "name": "lastname",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "last name"
        },
        {
          "name": "password",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Clear text password (default hashed to SHA256SALT). If you wish to use any other hasing algorithm, you would need to write a custom authentication adapter"
        },
        {
          "name": "username",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Unique username"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates a user account"
    }
  },
  "change": {
    "serviceforvirtualmachine": {
      "name": "changeServiceForVirtualMachine",
      "related": [
        "detachIso",
        "migrateVirtualMachineWithVolume",
        "startVirtualMachine",
        "migrateVirtualMachine",
        "stopVirtualMachine",
        "updateVirtualMachine",
        "revertToVMSnapshot",
        "listVirtualMachines",
        "assignVirtualMachine",
        "destroyVirtualMachine",
        "restoreVirtualMachine"
      ],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "updateVirtualMachine",
            "changeServiceForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the virtual machine"
        },
        {
          "name": "serviceofferingid",
          "required": True,
          "related": [
            "listServiceOfferings"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the service offering ID to apply to the virtual machine"
        },
        {
          "name": "details",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "name value pairs of custom parameters for cpu, memory and cpunumber. example details[i].name=value"
        }
      ],
      "requiredparams": [
        "id",
        "serviceofferingid"
      ],
      "description": "Changes the service offering for a virtual machine. The virtual machine must be in a \"Stopped\" state for this command to take effect."
    },
    "serviceforsystemvm": {
      "name": "changeServiceForSystemVm",
      "related": [
        "migrateSystemVm",
        "rebootSystemVm",
        "listSystemVms",
        "scaleSystemVm"
      ],
      "isasync": False,
      "params": [
        {
          "name": "serviceofferingid",
          "required": True,
          "related": [
            "createServiceOffering",
            "listServiceOfferings"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the service offering ID to apply to the system vm"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "migrateSystemVm",
            "changeServiceForSystemVm",
            "rebootSystemVm",
            "listSystemVms",
            "scaleSystemVm"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the system vm"
        },
        {
          "name": "details",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "name value pairs of custom parameters for cpu, memory and cpunumber. example details[i].name=value"
        }
      ],
      "requiredparams": [
        "serviceofferingid",
        "id"
      ],
      "description": "Changes the service offering for a system vm (console proxy or secondary storage). The system vm must be in a \"Stopped\" state for this command to take effect."
    },
    "serviceforrouter": {
      "name": "changeServiceForRouter",
      "related": [
        "startRouter",
        "listInternalLoadBalancerVMs"
      ],
      "isasync": False,
      "params": [
        {
          "name": "serviceofferingid",
          "required": True,
          "related": [
            "createServiceOffering",
            "listServiceOfferings"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the service offering ID to apply to the domain router"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "startRouter",
            "listInternalLoadBalancerVMs",
            "changeServiceForRouter"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the router"
        }
      ],
      "requiredparams": [
        "serviceofferingid",
        "id"
      ],
      "description": "Upgrades domain router to a new service offering"
    }
  },
  "replace": {
    "networkacllist": {
      "name": "replaceNetworkACLList",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "gatewayid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the private gateway"
        },
        {
          "name": "networkid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the network"
        },
        {
          "name": "aclid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the network ACL"
        }
      ],
      "requiredparams": [
        "aclid"
      ],
      "description": "Replaces ACL associated with a Network or private gateway"
    }
  },
  "disable": {
    "account": {
      "name": "disableAccount",
      "related": [
        "listAccounts",
        "markDefaultZoneForAccount"
      ],
      "isasync": True,
      "params": [
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Disables specified account."
        },
        {
          "name": "lock",
          "required": True,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If True, only lock the account; else disable the account"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Disables specified account in this domain."
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listAccounts",
            "markDefaultZoneForAccount",
            "disableAccount"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Account id"
        }
      ],
      "requiredparams": [
        "lock"
      ],
      "description": "Disables an account"
    },
    "cisconexusvsm": {
      "name": "disableCiscoNexusVSM",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "disableCiscoNexusVSM"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Id of the Cisco Nexus 1000v VSM device to be deleted"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "disable a Cisco Nexus VSM device"
    },
    "user": {
      "name": "disableUser",
      "related": [
        "lockUser",
        "listUsers"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "disableUser",
            "lockUser",
            "listUsers"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Disables user by user ID."
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Disables a user account"
    },
    "staticnat": {
      "name": "disableStaticNat",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "ipaddressid",
          "required": True,
          "related": [
            "associateIpAddress"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the public IP address id for which static nat feature is being disableed"
        }
      ],
      "requiredparams": [
        "ipaddressid"
      ],
      "description": "Disables static rule for given ip address"
    },
    "autoscalevmgroup": {
      "name": "disableAutoScaleVmGroup",
      "related": [
        "enableAutoScaleVmGroup",
        "updateAutoScaleVmGroup"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "enableAutoScaleVmGroup",
            "updateAutoScaleVmGroup",
            "disableAutoScaleVmGroup"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the autoscale group"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Disables an AutoScale Vm Group"
    }
  },
  "scale": {
    "systemvm": {
      "name": "scaleSystemVm",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "serviceofferingid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the service offering ID to apply to the system vm"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "scaleSystemVm"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the system vm"
        },
        {
          "name": "details",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "name value pairs of custom parameters for cpu, memory and cpunumber. example details[i].name=value"
        }
      ],
      "requiredparams": [
        "serviceofferingid",
        "id"
      ],
      "description": "Scale the service offering for a system vm (console proxy or secondary storage). The system vm must be in a \"Stopped\" state for this command to take effect."
    },
    "virtualmachine": {
      "name": "scaleVirtualMachine",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the virtual machine"
        },
        {
          "name": "serviceofferingid",
          "required": True,
          "related": [
            "createServiceOffering",
            "listServiceOfferings"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the service offering for the virtual machine"
        },
        {
          "name": "details",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "name value pairs of custom parameters for cpu,memory and cpunumber. example details[i].name=value"
        }
      ],
      "requiredparams": [
        "id",
        "serviceofferingid"
      ],
      "description": "Scales the virtual machine to a new service offering."
    }
  },
  "import": {
    "ldapusers": {
      "name": "importLdapUsers",
      "related": [
        "searchLdap",
        "listLdapUsers"
      ],
      "isasync": False,
      "params": [
        {
          "name": "accountdetails",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "details for account used to store specific parameters"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "timezone",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Specifies a timezone for this command. For more information on the timezone parameter, see Time Zone Format."
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Specifies the domain to which the ldap users are to be imported. If no domain is specified, a domain will created using group parameter. If the group is also not specified, a domain name based on the OU information will be created. If no OU hierarchy exists, will be defaulted to ROOT domain"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "group",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Specifies the group name from which the ldap users are to be imported. If no group is specified, all the users will be imported."
        },
        {
          "name": "accounttype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "short",
          "description": "Type of the account.  Specify 0 for user, 1 for root admin, and 2 for domain admin"
        }
      ],
      "requiredparams": [
        "accounttype"
      ],
      "description": "Import LDAP users"
    }
  },
  "copy": {
    "iso": {
      "name": "copyIso",
      "related": [
        "listIsos",
        "updateIso"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listIsos",
            "copyIso",
            "updateIso"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Template ID."
        },
        {
          "name": "destzoneid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "ID of the zone the template is being copied to."
        },
        {
          "name": "sourcezoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "ID of the zone the template is currently hosted on. If not specified and template is cross-zone, then we will sync this template to region wide image store"
        }
      ],
      "requiredparams": [
        "id",
        "destzoneid"
      ],
      "description": "Copies an iso from one zone to another."
    },
    "template": {
      "name": "copyTemplate",
      "related": [
        "registerIso",
        "prepareTemplate",
        "createTemplate",
        "listIsos",
        "copyIso",
        "registerTemplate",
        "updateIso",
        "updateTemplate",
        "listTemplates"
      ],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "copyTemplate",
            "registerIso",
            "prepareTemplate",
            "createTemplate",
            "listIsos",
            "copyIso",
            "registerTemplate",
            "updateIso",
            "updateTemplate",
            "listTemplates"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Template ID."
        },
        {
          "name": "destzoneid",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "ID of the zone the template is being copied to."
        },
        {
          "name": "sourcezoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "ID of the zone the template is currently hosted on. If not specified and template is cross-zone, then we will sync this template to region wide image store"
        }
      ],
      "requiredparams": [
        "id",
        "destzoneid"
      ],
      "description": "Copies a template from one zone to another."
    }
  },
  "generate": {
    "usagerecords": {
      "name": "generateUsageRecords",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "List events for the specified domain."
        },
        {
          "name": "enddate",
          "required": True,
          "related": [],
          "length": 255,
          "type": "date",
          "description": "End date range for usage record query. Use yyyy-MM-dd as the date format, e.g. startDate=2009-06-03."
        },
        {
          "name": "startdate",
          "required": True,
          "related": [],
          "length": 255,
          "type": "date",
          "description": "Start date range for usage record query. Use yyyy-MM-dd as the date format, e.g. startDate=2009-06-01."
        }
      ],
      "requiredparams": [
        "enddate",
        "startdate"
      ],
      "description": "Generates usage records. This will generate records only if there any records to be generated, i.e if the scheduled usage job was not run or failed"
    },
    "alert": {
      "name": "generateAlert",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "Zone id for which alert is generated"
        },
        {
          "name": "description",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Alert description"
        },
        {
          "name": "type",
          "required": True,
          "related": [],
          "length": 255,
          "type": "short",
          "description": "Type of the alert"
        },
        {
          "name": "podid",
          "required": False,
          "related": [
            "updatePod"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Pod id for which alert is generated"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Name of the alert"
        }
      ],
      "requiredparams": [
        "description",
        "type",
        "name"
      ],
      "description": "Generates an alert"
    }
  },
  "resize": {
    "volume": {
      "name": "resizeVolume",
      "related": [
        "uploadVolume",
        "createVolume",
        "detachVolume"
      ],
      "isasync": True,
      "params": [
        {
          "name": "shrinkok",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "Verify OK to Shrink"
        },
        {
          "name": "diskofferingid",
          "required": False,
          "related": [
            "listDiskOfferings",
            "updateDiskOffering",
            "createDiskOffering"
          ],
          "length": 255,
          "type": "uuid",
          "description": "new disk offering id"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "uploadVolume",
            "resizeVolume",
            "createVolume",
            "detachVolume"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the disk volume"
        },
        {
          "name": "size",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "New volume size in G"
        }
      ],
      "requiredparams": [],
      "description": "Resizes a volume"
    }
  },
  "count": 466,
  "expunge": {
    "virtualmachine": {
      "name": "expungeVirtualMachine",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "attachIso",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the virtual machine"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Expunge a virtual machine. Once expunged, it cannot be recoverd."
    }
  },
  "upgrade": {
    "routertemplate": {
      "name": "upgradeRouterTemplate",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "upgrades router with the specified Id"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "upgrades all routers within the specified zone"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "upgrades all routers owned by the specified account"
        },
        {
          "name": "podid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "upgrades all routers within the specified pod"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "upgrades all routers owned by the specified domain"
        },
        {
          "name": "clusterid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "upgrades all routers within the specified cluster"
        }
      ],
      "requiredparams": [],
      "description": "Upgrades router to use newer template"
    }
  },
  "register": {
    "userkeys": {
      "name": "registerUserKeys",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "lockUser",
            "listUsers"
          ],
          "length": 255,
          "type": "uuid",
          "description": "User id"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "This command allows a user to register for the developer API, returning a secret key and an API key. This request is made through the integration API port, so it is a privileged command and must be made on behalf of a user. It is up to the implementer just how the username and password are entered, and then how that translates to an integration API request. Both secret key and API key should be returned to the user"
    },
    "iso": {
      "name": "registerIso",
      "related": [
        "listIsos",
        "copyIso",
        "updateIso"
      ],
      "isasync": False,
      "params": [
        {
          "name": "checksum",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the MD5 checksum value of this ISO"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional domainId. If the account parameter is used, domainId must also be used."
        },
        {
          "name": "isdynamicallyscalable",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if iso contains XS/VMWare tools inorder to support dynamic scaling of VM cpu/memory"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "an optional account name. Must be used with domainId."
        },
        {
          "name": "bootable",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if this ISO is bootable. If not passed explicitly its assumed to be True"
        },
        {
          "name": "imagestoreuuid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Image store uuid"
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the URL to where the ISO is currently being hosted"
        },
        {
          "name": "ispublic",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if you want to register the ISO to be publicly available to all users, False otherwise."
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the ISO"
        },
        {
          "name": "ostypeid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the OS Type that best represents the OS of this ISO. If the iso is bootable this parameter needs to be passed"
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the zone you wish to register the ISO to."
        },
        {
          "name": "displaytext",
          "required": True,
          "related": [],
          "length": 4096,
          "type": "string",
          "description": "the display text of the ISO. This is usually used for display purposes."
        },
        {
          "name": "isextractable",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if the iso or its derivatives are extractable; default is False"
        },
        {
          "name": "isfeatured",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if you want this ISO to be featured"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Register iso for the project"
        }
      ],
      "requiredparams": [
        "url",
        "name",
        "zoneid",
        "displaytext"
      ],
      "description": "Registers an existing ISO into the CloudStack Cloud."
    },
    "sshkeypair": {
      "name": "registerSSHKeyPair",
      "related": [
        "listSSHKeyPairs"
      ],
      "isasync": False,
      "params": [
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Name of the keypair"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "activateProject",
            "listProjects",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional project for the ssh key"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "an optional account for the ssh key. Must be used with domainId."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional domainId for the ssh key. If the account parameter is used, domainId must also be used."
        },
        {
          "name": "publickey",
          "required": True,
          "related": [],
          "length": 5120,
          "type": "string",
          "description": "Public key material of the keypair"
        }
      ],
      "requiredparams": [
        "name",
        "publickey"
      ],
      "description": "Register a public key in a keypair under a certain name"
    },
    "template": {
      "name": "registerTemplate",
      "related": [
        "registerIso",
        "prepareTemplate",
        "listIsos",
        "copyIso",
        "updateIso",
        "updateTemplate",
        "listTemplates"
      ],
      "isasync": False,
      "params": [
        {
          "name": "templatetag",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the tag for this template."
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the template"
        },
        {
          "name": "ispublic",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if the template is available to all accounts; default is True"
        },
        {
          "name": "requireshvm",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if this template requires HVM"
        },
        {
          "name": "bits",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "32 or 64 bits support. 64 by default"
        },
        {
          "name": "displaytext",
          "required": True,
          "related": [],
          "length": 4096,
          "type": "string",
          "description": "the display text of the template. This is usually used for display purposes."
        },
        {
          "name": "checksum",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the MD5 checksum value of this template"
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the URL of where the template is hosted. Possible URL include http:// and https://"
        },
        {
          "name": "hypervisor",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the target hypervisor for the template"
        },
        {
          "name": "passwordenabled",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if the template supports the password reset feature; default is False"
        },
        {
          "name": "isextractable",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if the template or its derivatives are extractable; default is False"
        },
        {
          "name": "details",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "Template details in key/value pairs."
        },
        {
          "name": "isfeatured",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if this template is a featured template, False otherwise"
        },
        {
          "name": "ostypeid",
          "required": True,
          "related": [
            "listOsTypes"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the OS Type that best represents the OS of this template."
        },
        {
          "name": "format",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the format for the template. Possible values include QCOW2, RAW, and VHD."
        },
        {
          "name": "isrouting",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if the template type is routing i.e., if template is used to deploy router"
        },
        {
          "name": "isdynamicallyscalable",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if template contains XS/VMWare tools inorder to support dynamic scaling of VM cpu/memory"
        },
        {
          "name": "sshkeyenabled",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if the template supports the sshkey upload feature; default is False"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Register template for the project"
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the zone the template is to be hosted on"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "an optional accountName. Must be used with domainId."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional domainId. If the account parameter is used, domainId must also be used."
        }
      ],
      "requiredparams": [
        "name",
        "displaytext",
        "url",
        "hypervisor",
        "ostypeid",
        "format",
        "zoneid"
      ],
      "description": "Registers an existing template into the CloudStack cloud. "
    }
  },
  "list": {
    "alerts": {
      "name": "listAlerts",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listAlerts"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the alert"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list by alert name"
        },
        {
          "name": "type",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list by alert type"
        }
      ],
      "requiredparams": [],
      "description": "Lists all alerts."
    },
    "networkdevice": {
      "name": "listNetworkDevice",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "networkdeviceparameterlist",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "parameters for network device"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "networkdevicetype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Network device type, now supports ExternalDhcp, PxeServer, NetscalerMPXLoadBalancer, NetscalerVPXLoadBalancer, NetscalerSDXLoadBalancer, F5BigIpLoadBalancer, JuniperSRXFirewall, PaloAltoFirewall"
        }
      ],
      "requiredparams": [],
      "description": "List network devices"
    },
    "instancegroups": {
      "name": "listInstanceGroups",
      "related": [
        "updateInstanceGroup",
        "createInstanceGroup"
      ],
      "isasync": False,
      "params": [
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "updateInstanceGroup",
            "listInstanceGroups",
            "createInstanceGroup"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list instance groups by ID"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list instance groups by name"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "activateProject",
            "listProjects",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        }
      ],
      "requiredparams": [],
      "description": "Lists vm groups"
    },
    "ucsmanagers": {
      "name": "listUcsManagers",
      "related": [
        "addUcsManager"
      ],
      "isasync": False,
      "params": [
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the zone id"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "addUcsManager",
            "listUcsManagers"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the ucs manager"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        }
      ],
      "requiredparams": [],
      "description": "List ucs manager"
    },
    "physicalnetworks": {
      "name": "listPhysicalNetworks",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": False,
          "related": [
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list physical network by id"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID for the physical network"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "search by name"
        }
      ],
      "requiredparams": [],
      "description": "Lists physical networks"
    },
    "networks": {
      "name": "listNetworks",
      "related": [
        "listSrxFirewallNetworks",
        "updateNetwork",
        "listF5LoadBalancerNetworks",
        "listPaloAltoFirewallNetworks",
        "listNetscalerLoadBalancerNetworks"
      ],
      "isasync": False,
      "params": [
        {
          "name": "issystem",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if network is system, False otherwise"
        },
        {
          "name": "supportedservices",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "list networks supporting certain services"
        },
        {
          "name": "restartrequired",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "list networks by restartRequired"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "type",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the type of the network. Supported values are: Isolated and Shared"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "activateProject",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "physicalnetworkid",
          "required": False,
          "related": [
            "createPhysicalNetwork",
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list networks by physical network id"
        },
        {
          "name": "acltype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list networks by ACL (access control list) type. Supported values are Account and Domain"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID of the network"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "specifyipranges",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if need to list only networks which support specifying ip ranges"
        },
        {
          "name": "forvpc",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "the network belongs to vpc"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "vpcid",
          "required": False,
          "related": [
            "createVPC",
            "listVPCs",
            "restartVPC",
            "updateVPC"
          ],
          "length": 255,
          "type": "uuid",
          "description": "List networks by VPC"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "canusefordeploy",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "list networks available for vm deployment"
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List resources by tags (key/value pairs)"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listSrxFirewallNetworks",
            "listNetworks",
            "updateNetwork",
            "listF5LoadBalancerNetworks",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list networks by id"
        },
        {
          "name": "traffictype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "type of the traffic"
        }
      ],
      "requiredparams": [],
      "description": "Lists all available networks."
    },
    "ldapconfigurations": {
      "name": "listLdapConfigurations",
      "related": [
        "addLdapConfiguration",
        "deleteLdapConfiguration"
      ],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "hostname",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Hostname"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "port",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "Port"
        }
      ],
      "requiredparams": [],
      "description": "Lists all LDAP configurations"
    },
    "capabilities": {
      "name": "listCapabilities",
      "related": [],
      "isasync": False,
      "params": [],
      "requiredparams": [],
      "description": "Lists capabilities"
    },
    "clusters": {
      "name": "listClusters",
      "related": [
        "updateCluster"
      ],
      "isasync": False,
      "params": [
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "lists clusters by the cluster name"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "lists clusters by Zone ID"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "clustertype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "lists clusters by cluster type"
        },
        {
          "name": "hypervisor",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "lists clusters by hypervisor type"
        },
        {
          "name": "showcapacities",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "flag to display the capacity of the clusters"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "allocationstate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "lists clusters by allocation state"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "updateCluster",
            "listClusters"
          ],
          "length": 255,
          "type": "uuid",
          "description": "lists clusters by the cluster ID"
        },
        {
          "name": "managedstate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "whether this cluster is managed by cloudstack"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "podid",
          "required": False,
          "related": [
            "createPod",
            "updatePod",
            "listPods"
          ],
          "length": 255,
          "type": "uuid",
          "description": "lists clusters by Pod ID"
        }
      ],
      "requiredparams": [],
      "description": "Lists clusters."
    },
    "resourcelimits": {
      "name": "listResourceLimits",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "resourcetype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "Type of resource to update. Values are 0, 1, 2, 3, and 4.0 - Instance. Number of instances a user can create. 1 - IP. Number of public IP addresses an account can own. 2 - Volume. Number of disk volumes an account can own.3 - Snapshot. Number of snapshots an account can own.4 - Template. Number of templates an account can register/create.5 - Project. Number of projects an account can own.6 - Network. Number of networks an account can own.7 - VPC. Number of VPC an account can own.8 - CPU. Number of CPU an account can allocate for his resources.9 - Memory. Amount of RAM an account can allocate for his resources.10 - Primary Storage. Amount of Primary storage an account can allocate for his resoruces.11 - Secondary Storage. Amount of Secondary storage an account can allocate for his resources."
        },
        {
          "name": "id",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "Lists resource limits by ID."
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        }
      ],
      "requiredparams": [],
      "description": "Lists resource limits."
    },
    "firewallrules": {
      "name": "listFirewallRules",
      "related": [
        "listEgressFirewallRules",
        "createFirewallRule"
      ],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": False,
          "related": [
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Lists rule with the specified ID."
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "networkid",
          "required": False,
          "related": [
            "listSrxFirewallNetworks",
            "updateNetwork",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list firewall rules for ceratin network"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List resources by tags (key/value pairs)"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "ipaddressid",
          "required": False,
          "related": [
            "associateIpAddress"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the id of IP address of the firwall services"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        }
      ],
      "requiredparams": [],
      "description": "Lists all firewall rules for an IP address."
    },
    "supportednetworkservices": {
      "name": "listSupportedNetworkServices",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "service",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "network service name to list providers and capabilities of"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "provider",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "network service provider name"
        }
      ],
      "requiredparams": [],
      "description": "Lists all network services provided by CloudStack or for the given Provider."
    },
    "loadbalancerrules": {
      "name": "listLoadBalancerRules",
      "related": [
        "createLoadBalancerRule"
      ],
      "isasync": False,
      "params": [
        {
          "name": "publicipid",
          "required": False,
          "related": [
            "associateIpAddress",
            "restartNetwork"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the public IP address id of the load balancer rule "
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the load balancer rule"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the availability zone ID"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the load balancer rule"
        },
        {
          "name": "virtualmachineid",
          "required": False,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the virtual machine of the load balancer rule"
        },
        {
          "name": "networkid",
          "required": False,
          "related": [
            "listSrxFirewallNetworks",
            "updateNetwork",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list by network id the rule belongs to"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List resources by tags (key/value pairs)"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        }
      ],
      "requiredparams": [],
      "description": "Lists load balancer rules."
    },
    "autoscalepolicies": {
      "name": "listAutoScalePolicies",
      "related": [
        "updateAutoScalePolicy",
        "createAutoScalePolicy"
      ],
      "isasync": False,
      "params": [
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "action",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the action to be executed if all the conditions evaluate to True for the specified duration."
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listAutoScalePolicies",
            "updateAutoScalePolicy",
            "createAutoScalePolicy"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the autoscale policy"
        },
        {
          "name": "vmgroupid",
          "required": False,
          "related": [
            "enableAutoScaleVmGroup",
            "updateAutoScaleVmGroup",
            "disableAutoScaleVmGroup",
            "createAutoScaleVmGroup"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the autoscale vm group"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "conditionid",
          "required": False,
          "related": [
            "listConditions"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the condition of the policy"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        }
      ],
      "requiredparams": [],
      "description": "Lists autoscale policies."
    },
    "niciranvpdevices": {
      "name": "listNiciraNvpDevices",
      "related": [
        "addNiciraNvpDevice"
      ],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "physicalnetworkid",
          "required": False,
          "related": [
            "createPhysicalNetwork",
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        },
        {
          "name": "nvpdeviceid",
          "required": False,
          "related": [
            "addNiciraNvpDevice",
            "listNiciraNvpDevices"
          ],
          "length": 255,
          "type": "uuid",
          "description": "nicira nvp device ID"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists Nicira NVP devices"
    },
    "f5loadbalancernetworks": {
      "name": "listF5LoadBalancerNetworks",
      "related": [
        "listSrxFirewallNetworks",
        "updateNetwork",
        "listPaloAltoFirewallNetworks",
        "listNetscalerLoadBalancerNetworks"
      ],
      "isasync": False,
      "params": [
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "lbdeviceid",
          "required": True,
          "related": [
            "addF5LoadBalancer"
          ],
          "length": 255,
          "type": "uuid",
          "description": "f5 load balancer device ID"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [
        "lbdeviceid"
      ],
      "description": "lists network that are using a F5 load balancer device"
    },
    "templatepermissions": {
      "name": "listTemplatePermissions",
      "related": [
        "listIsoPermissions"
      ],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listTemplatePermissions",
            "listIsoPermissions"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the template ID"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "List template visibility and all accounts that have permissions to view this template."
    },
    "projects": {
      "name": "listProjects",
      "related": [
        "createProject",
        "activateProject",
        "listProjectAccounts",
        "updateProject"
      ],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": False,
          "related": [
            "createProject",
            "activateProject",
            "listProjects",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list projects by project ID"
        },
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list projects by state"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List projects by tags (key/value pairs)"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list projects by name"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "displaytext",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list projects by display text"
        }
      ],
      "requiredparams": [],
      "description": "Lists projects and provides detailed information for listed projects"
    },
    "systemvms": {
      "name": "listSystemVms",
      "related": [
        "rebootSystemVm",
        "scaleSystemVm"
      ],
      "isasync": False,
      "params": [
        {
          "name": "systemvmtype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the system VM type. Possible types are \"consoleproxy\" and \"secondarystoragevm\"."
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "hostid",
          "required": False,
          "related": [
            "listHosts"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the host ID of the system VM"
        },
        {
          "name": "storageid",
          "required": False,
          "related": [
            "findStoragePoolsForMigration"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the storage ID where vm's volumes belong to"
        },
        {
          "name": "podid",
          "required": False,
          "related": [
            "updatePod"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Pod ID of the system VM"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the system VM"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "rebootSystemVm",
            "listSystemVms",
            "scaleSystemVm"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the system VM"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID of the system VM"
        },
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the state of the system VM"
        }
      ],
      "requiredparams": [],
      "description": "List system virtual machines."
    },
    "portforwardingrules": {
      "name": "listPortForwardingRules",
      "related": [
        "createPortForwardingRule",
        "listIpForwardingRules"
      ],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listPortForwardingRules",
            "createPortForwardingRule",
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Lists rule with the specified ID."
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List resources by tags (key/value pairs)"
        },
        {
          "name": "ipaddressid",
          "required": False,
          "related": [
            "associateIpAddress",
            "restartNetwork"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the id of IP address of the port forwarding services"
        },
        {
          "name": "networkid",
          "required": False,
          "related": [
            "listSrxFirewallNetworks",
            "updateNetwork",
            "listF5LoadBalancerNetworks",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list port forwarding rules for ceratin network"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists all port forwarding rules for an IP address."
    },
    "bigswitchvnsdevices": {
      "name": "listBigSwitchVnsDevices",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "physicalnetworkid",
          "required": False,
          "related": [
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        },
        {
          "name": "vnsdeviceid",
          "required": False,
          "related": [
            "listBigSwitchVnsDevices"
          ],
          "length": 255,
          "type": "uuid",
          "description": "bigswitch vns device ID"
        }
      ],
      "requiredparams": [],
      "description": "Lists BigSwitch Vns devices"
    },
    "networkacllists": {
      "name": "listNetworkACLLists",
      "related": [
        "createNetworkACLList"
      ],
      "isasync": False,
      "params": [
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "networkid",
          "required": False,
          "related": [
            "listSrxFirewallNetworks",
            "updateNetwork",
            "listF5LoadBalancerNetworks",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list network ACLs by network Id"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listNetworkACLLists",
            "createNetworkACLList"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Lists network ACL with the specified ID."
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list network ACLs by specified name"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "vpcid",
          "required": False,
          "related": [
            "createVPC",
            "listVPCs",
            "restartVPC",
            "updateVPC"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list network ACLs by Vpc Id"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        }
      ],
      "requiredparams": [],
      "description": "Lists all network ACLs"
    },
    "storageproviders": {
      "name": "listStorageProviders",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "type",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the type of storage provider: either primary or image"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [
        "type"
      ],
      "description": "Lists storage providers."
    },
    "vpngateways": {
      "name": "listVpnGateways",
      "related": [
        "createVpnGateway"
      ],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "vpcid",
          "required": False,
          "related": [
            "createVPC",
            "listVPCs",
            "restartVPC",
            "updateVPC"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of vpc"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listVpnGateways",
            "createVpnGateway"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of the vpn gateway"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "activateProject",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        }
      ],
      "requiredparams": [],
      "description": "Lists site 2 site vpn gateways"
    },
    "baremetalpxeservers": {
      "name": "listBaremetalPxeServers",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "Pxe server device ID"
        }
      ],
      "requiredparams": [],
      "description": "list baremetal pxe server"
    },
    "loadbalancerruleinstances": {
      "name": "listLoadBalancerRuleInstances",
      "related": [
        "detachIso",
        "migrateVirtualMachineWithVolume",
        "updateVMAffinityGroup",
        "startVirtualMachine",
        "migrateVirtualMachine",
        "stopVirtualMachine",
        "rebootVirtualMachine",
        "removeNicFromVirtualMachine",
        "updateVirtualMachine",
        "recoverVirtualMachine",
        "deployVirtualMachine",
        "changeServiceForVirtualMachine",
        "updateDefaultNicForVirtualMachine",
        "revertToVMSnapshot",
        "resetSSHKeyForVirtualMachine",
        "listVirtualMachines",
        "resetPasswordForVirtualMachine",
        "assignVirtualMachine",
        "attachIso",
        "destroyVirtualMachine",
        "restoreVirtualMachine"
      ],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "updatePortForwardingRule",
            "createIpForwardingRule",
            "listPortForwardingRules",
            "createPortForwardingRule",
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the load balancer rule"
        },
        {
          "name": "applied",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if listing all virtual machines currently applied to the load balancer rule; default is True"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "List all virtual machine instances that are assigned to a load balancer rule."
    },
    "hosts": {
      "name": "listHosts",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "podid",
          "required": False,
          "related": [
            "updatePod"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Pod ID for the host"
        },
        {
          "name": "details",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "comma separated list of host details requested, value can be a list of [ min, all, capacity, events, stats]"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listHosts"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the id of the host"
        },
        {
          "name": "hahost",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "if True, list only hosts dedicated to HA"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID for the host"
        },
        {
          "name": "hypervisor",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "hypervisor type of host: XenServer,KVM,VMware,Hyperv,BareMetal,Simulator"
        },
        {
          "name": "clusterid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "lists hosts existing in particular cluster"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the host"
        },
        {
          "name": "resourcestate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list hosts by resource state. Resource state represents current state determined by admin of host, valule can be one of [Enabled, Disabled, Unmanaged, PrepareForMaintenance, ErrorInMaintenance, Maintenance, Error]"
        },
        {
          "name": "virtualmachineid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "lists hosts in the same cluster as this VM and flag hosts with enough CPU/RAm to host this VM"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the state of the host"
        },
        {
          "name": "type",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the host type"
        }
      ],
      "requiredparams": [],
      "description": "Lists hosts."
    },
    "accounts": {
      "name": "listAccounts",
      "related": [
        "markDefaultZoneForAccount"
      ],
      "isasync": False,
      "params": [
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "accounttype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "list accounts by account type. Valid account types are 1 (admin), 2 (domain-admin), and 0 (user)."
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list accounts by state. Valid states are enabled, disabled, and locked."
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listAccounts",
            "markDefaultZoneForAccount"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list account by account ID"
        },
        {
          "name": "iscleanuprequired",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "list accounts by cleanuprequred attribute (values are True or False)"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list account by account name"
        }
      ],
      "requiredparams": [],
      "description": "Lists accounts and provides detailed account information for listed accounts"
    },
    "counters": {
      "name": "listCounters",
      "related": [
        "createCounter"
      ],
      "isasync": False,
      "params": [
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "createCounter",
            "listCounters"
          ],
          "length": 255,
          "type": "uuid",
          "description": "ID of the Counter."
        },
        {
          "name": "source",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Source of the counter."
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Name of the counter."
        }
      ],
      "requiredparams": [],
      "description": "List the counters"
    },
    "configurations": {
      "name": "listConfigurations",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "storageid",
          "required": False,
          "related": [
            "findStoragePoolsForMigration",
            "createStoragePool",
            "listStoragePools"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Storage pool to update the parameter value for corresponding storage pool"
        },
        {
          "name": "clusterid",
          "required": False,
          "related": [
            "updateCluster"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Cluster to update the parameter value for corresponding cluster"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "accountid",
          "required": False,
          "related": [
            "listAccounts",
            "ldapCreateAccount",
            "lockAccount",
            "markDefaultZoneForAccount",
            "createAccount",
            "disableAccount"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Account to update the parameter value for corresponding account"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Zone to update the parameter value for corresponding zone"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "lists configuration by name"
        },
        {
          "name": "category",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "lists configurations by category"
        }
      ],
      "requiredparams": [],
      "description": "Lists all configurations."
    },
    "paloaltofirewalls": {
      "name": "listPaloAltoFirewalls",
      "related": [
        "configurePaloAltoFirewall"
      ],
      "isasync": False,
      "params": [
        {
          "name": "physicalnetworkid",
          "required": False,
          "related": [
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "fwdeviceid",
          "required": False,
          "related": [
            "configurePaloAltoFirewall",
            "listPaloAltoFirewalls"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Palo Alto firewall device ID"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "lists Palo Alto firewall devices in a physical network"
    },
    "usagerecords": {
      "name": "listUsageRecords",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "accountid",
          "required": False,
          "related": [
            "listAccounts",
            "ldapCreateAccount",
            "lockAccount",
            "markDefaultZoneForAccount",
            "createAccount",
            "disableAccount",
            "updateAccount"
          ],
          "length": 255,
          "type": "uuid",
          "description": "List usage records for the specified account"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "type",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "List usage records for the specified usage type"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "List usage records for specified project"
        },
        {
          "name": "enddate",
          "required": True,
          "related": [],
          "length": 255,
          "type": "date",
          "description": "End date range for usage record query. Use yyyy-MM-dd as the date format, e.g. startDate=2009-06-03."
        },
        {
          "name": "startdate",
          "required": True,
          "related": [],
          "length": 255,
          "type": "date",
          "description": "Start date range for usage record query. Use yyyy-MM-dd as the date format, e.g. startDate=2009-06-01."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "List usage records for the specified domain."
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List usage records for the specified user."
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [
        "enddate",
        "startdate"
      ],
      "description": "Lists usage records for accounts"
    },
    "storagepools": {
      "name": "listStoragePools",
      "related": [
        "findStoragePoolsForMigration"
      ],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "findStoragePoolsForMigration",
            "listStoragePools"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the storage pool"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "podid",
          "required": False,
          "related": [
            "updatePod"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Pod ID for the storage pool"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "ipaddress",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the IP address for the storage pool"
        },
        {
          "name": "clusterid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list storage pools belongig to the specific cluster"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the storage pool"
        },
        {
          "name": "path",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the storage pool path"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID for the storage pool"
        },
        {
          "name": "scope",
          "required": False,
          "related": [
            "findStoragePoolsForMigration",
            "listStoragePools"
          ],
          "length": 255,
          "type": "string",
          "description": "the ID of the storage pool"
        }
      ],
      "requiredparams": [],
      "description": "Lists storage pools."
    },
    "ucsblades": {
      "name": "listUcsBlades",
      "related": [
        "instantiateUcsTemplateAndAssocaciateToBlade",
        "refreshUcsBlades"
      ],
      "isasync": False,
      "params": [
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "ucsmanagerid",
          "required": True,
          "related": [
            "addUcsManager"
          ],
          "length": 255,
          "type": "uuid",
          "description": "ucs manager id"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [
        "ucsmanagerid"
      ],
      "description": "List ucs blades"
    },
    "snapshots": {
      "name": "listSnapshots",
      "related": [
        "createSnapshot",
        "revertSnapshot"
      ],
      "isasync": False,
      "params": [
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "snapshottype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "valid values are MANUAL or RECURRING."
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List resources by tags (key/value pairs)"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list snapshots by zone id"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "createSnapshot",
            "listSnapshots",
            "revertSnapshot"
          ],
          "length": 255,
          "type": "uuid",
          "description": "lists snapshot by snapshot ID"
        },
        {
          "name": "volumeid",
          "required": False,
          "related": [
            "uploadVolume",
            "createVolume"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the disk volume"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "lists snapshot by snapshot name"
        },
        {
          "name": "intervaltype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "valid values are HOURLY, DAILY, WEEKLY, and MONTHLY."
        }
      ],
      "requiredparams": [],
      "description": "Lists all available snapshots for the account."
    },
    "vmwaredcs": {
      "name": "listVmwareDcs",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "Id of the CloudStack zone."
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        }
      ],
      "requiredparams": [
        "zoneid"
      ],
      "description": "Retrieves VMware DC(s) associated with a zone."
    },
    "dedicatedguestvlanranges": {
      "name": "listDedicatedGuestVlanRanges",
      "related": [
        "dedicateGuestVlanRange"
      ],
      "isasync": False,
      "params": [
        {
          "name": "physicalnetworkid",
          "required": False,
          "related": [
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "physical network id of the guest VLAN range"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listDedicatedGuestVlanRanges",
            "dedicateGuestVlanRange"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list dedicated guest vlan ranges by id"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the domain ID with which the guest VLAN range is associated.  If used with the account parameter, returns all guest VLAN ranges for that account in the specified domain."
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "project who will own the guest VLAN range"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "zone of the guest VLAN range"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "guestvlanrange",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the dedicated guest vlan range"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the account with which the guest VLAN range is associated. Must be used with the domainId parameter."
        }
      ],
      "requiredparams": [],
      "description": "Lists dedicated guest vlan ranges"
    },
    "serviceofferings": {
      "name": "listServiceOfferings",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of the service offering"
        },
        {
          "name": "systemvmtype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the system VM type. Possible types are \"consoleproxy\", \"secondarystoragevm\" or \"domainrouter\"."
        },
        {
          "name": "issystem",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "is this a system vm offering"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the domain associated with the service offering"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listServiceOfferings"
          ],
          "length": 255,
          "type": "uuid",
          "description": "ID of the service offering"
        },
        {
          "name": "virtualmachineid",
          "required": False,
          "related": [
            "migrateVirtualMachineWithVolume",
            "stopVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the virtual machine. Pass this in if you want to see the available service offering that a virtual machine can be changed to."
        }
      ],
      "requiredparams": [],
      "description": "Lists all available service offerings."
    },
    "ciscoasa1000vresources": {
      "name": "listCiscoAsa1000vResources",
      "related": [
        "addCiscoAsa1000vResource"
      ],
      "isasync": False,
      "params": [
        {
          "name": "hostname",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Hostname or ip address of the Cisco ASA 1000v appliance."
        },
        {
          "name": "resourceid",
          "required": False,
          "related": [
            "addCiscoAsa1000vResource",
            "listCiscoAsa1000vResources"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Cisco ASA 1000v resource ID"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "physicalnetworkid",
          "required": False,
          "related": [
            "updatePhysicalNetwork",
            "createPhysicalNetwork",
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists Cisco ASA 1000v appliances"
    },
    "affinitygrouptypes": {
      "name": "listAffinityGroupTypes",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists affinity group types available"
    },
    "publicipaddresses": {
      "name": "listPublicIpAddresses",
      "related": [
        "associateIpAddress",
        "restartNetwork"
      ],
      "isasync": False,
      "params": [
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "associatednetworkid",
          "required": False,
          "related": [
            "listSrxFirewallNetworks",
            "listNetworks",
            "updateNetwork",
            "listF5LoadBalancerNetworks",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "lists all public IP addresses associated to the network specified"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "activateProject",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "isstaticnat",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "list only static nat ip addresses"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "allocatedonly",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "limits search results to allocated public IP addresses"
        },
        {
          "name": "vpcid",
          "required": False,
          "related": [
            "createVPC",
            "listVPCs",
            "restartVPC",
            "updateVPC"
          ],
          "length": 255,
          "type": "uuid",
          "description": "List ips belonging to the VPC"
        },
        {
          "name": "vlanid",
          "required": False,
          "related": [
            "listVlanIpRanges",
            "dedicatePublicIpRange",
            "createVlanIpRange"
          ],
          "length": 255,
          "type": "uuid",
          "description": "lists all public IP addresses by VLAN ID"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listPublicIpAddresses",
            "associateIpAddress",
            "restartNetwork"
          ],
          "length": 255,
          "type": "uuid",
          "description": "lists ip address by id"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "lists all public IP addresses by Zone ID"
        },
        {
          "name": "forloadbalancing",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "list only ips used for load balancing"
        },
        {
          "name": "ipaddress",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "lists the specified IP address"
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List resources by tags (key/value pairs)"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "issourcenat",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "list only source nat ip addresses"
        },
        {
          "name": "forvirtualnetwork",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "the virtual network for the IP address"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "physicalnetworkid",
          "required": False,
          "related": [
            "createPhysicalNetwork",
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "lists all public IP addresses by physical network id"
        }
      ],
      "requiredparams": [],
      "description": "Lists all public ip addresses"
    },
    "networkserviceproviders": {
      "name": "listNetworkServiceProviders",
      "related": [
        "listTrafficTypes",
        "updateNetworkServiceProvider",
        "addNetworkServiceProvider"
      ],
      "isasync": False,
      "params": [
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list providers by state"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list providers by name"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "physicalnetworkid",
          "required": False,
          "related": [
            "updatePhysicalNetwork",
            "createPhysicalNetwork",
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        }
      ],
      "requiredparams": [],
      "description": "Lists network serviceproviders for a given physical network."
    },
    "capacity": {
      "name": "listCapacity",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "type",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "lists capacity by type* CAPACITY_TYPE_MEMORY = 0* CAPACITY_TYPE_CPU = 1* CAPACITY_TYPE_STORAGE = 2* CAPACITY_TYPE_STORAGE_ALLOCATED = 3* CAPACITY_TYPE_VIRTUAL_NETWORK_PUBLIC_IP = 4* CAPACITY_TYPE_PRIVATE_IP = 5* CAPACITY_TYPE_SECONDARY_STORAGE = 6* CAPACITY_TYPE_VLAN = 7* CAPACITY_TYPE_DIRECT_ATTACHED_PUBLIC_IP = 8* CAPACITY_TYPE_LOCAL_STORAGE = 9."
        },
        {
          "name": "clusterid",
          "required": False,
          "related": [
            "updateCluster"
          ],
          "length": 255,
          "type": "uuid",
          "description": "lists capacity by the Cluster ID"
        },
        {
          "name": "fetchlatest",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "recalculate capacities and fetch the latest"
        },
        {
          "name": "podid",
          "required": False,
          "related": [
            "createPod",
            "updatePod",
            "listPods"
          ],
          "length": 255,
          "type": "uuid",
          "description": "lists capacity by the Pod ID"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "sortby",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Sort the results. Available values: Usage"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "lists capacity by the Zone ID"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists all the system wide capacities."
    },
    "diskofferings": {
      "name": "listDiskOfferings",
      "related": [
        "createDiskOffering"
      ],
      "isasync": False,
      "params": [
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listDiskOfferings",
            "createDiskOffering"
          ],
          "length": 255,
          "type": "uuid",
          "description": "ID of the disk offering"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of the disk offering"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the domain of the disk offering."
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists all available disk offerings."
    },
    "lbstickinesspolicies": {
      "name": "listLBStickinessPolicies",
      "related": [
        "createLBStickinessPolicy"
      ],
      "isasync": False,
      "params": [
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "lbruleid",
          "required": True,
          "related": [
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the load balancer rule"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        }
      ],
      "requiredparams": [
        "lbruleid"
      ],
      "description": "Lists LBStickiness policies."
    },
    "srxfirewallnetworks": {
      "name": "listSrxFirewallNetworks",
      "related": [
        "updateNetwork",
        "listNetscalerLoadBalancerNetworks"
      ],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "lbdeviceid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "netscaler load balancer device ID"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [
        "lbdeviceid"
      ],
      "description": "lists network that are using SRX firewall device"
    },
    "externalfirewalls": {
      "name": "listExternalFirewalls",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones"
          ],
          "length": 255,
          "type": "uuid",
          "description": "zone Id"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        }
      ],
      "requiredparams": [
        "zoneid"
      ],
      "description": "List external firewall appliances."
    },
    "vmsnapshot": {
      "name": "listVMSnapshot",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "virtualmachineid",
          "required": False,
          "related": [
            "migrateVirtualMachineWithVolume",
            "stopVirtualMachine",
            "updateVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the vm"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "vmsnapshotid",
          "required": False,
          "related": [
            "listVMSnapshot"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the VM snapshot"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List resources by tags (key/value pairs)"
        },
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "state of the virtual machine snapshot"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "lists snapshot by snapshot name or display name"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "List virtual machine snapshot by conditions"
    },
    "securitygroups": {
      "name": "listSecurityGroups",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List resources by tags (key/value pairs)"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "virtualmachineid",
          "required": False,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "lists security groups by virtual machine id"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listSecurityGroups"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list the security group by the id provided"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "securitygroupname",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "lists security groups by name"
        }
      ],
      "requiredparams": [],
      "description": "Lists security groups"
    },
    "dedicatedzones": {
      "name": "listDedicatedZones",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "domainid",
          "required": False,
          "related": [
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the domain associated with the zone"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the account associated with the zone. Must be used with domainId."
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Zone"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "affinitygroupid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list dedicated zones by affinity group"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "List dedicated zones."
    },
    "baremetaldhcp": {
      "name": "listBaremetalDhcp",
      "related": [
        "addBaremetalDhcp"
      ],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "DHCP server device ID"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "dhcpservertype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Type of DHCP device"
        }
      ],
      "requiredparams": [],
      "description": "list baremetal dhcp servers"
    },
    "conditions": {
      "name": "listConditions",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "counterid",
          "required": False,
          "related": [
            "createCounter"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Counter-id of the condition."
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listConditions"
          ],
          "length": 255,
          "type": "uuid",
          "description": "ID of the Condition."
        },
        {
          "name": "policyid",
          "required": False,
          "related": [
            "createAutoScalePolicy"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the policy"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        }
      ],
      "requiredparams": [],
      "description": "List Conditions for the specific user"
    },
    "swifts": {
      "name": "listSwifts",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "the id of the swift"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        }
      ],
      "requiredparams": [],
      "description": "List Swift."
    },
    "hypervisorcapabilities": {
      "name": "listHypervisorCapabilities",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listHypervisorCapabilities"
          ],
          "length": 255,
          "type": "uuid",
          "description": "ID of the hypervisor capability"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "hypervisor",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the hypervisor for which to restrict the search"
        }
      ],
      "requiredparams": [],
      "description": "Lists all hypervisor capabilities."
    },
    "tags": {
      "name": "listTags",
      "related": [
        "listResourceDetails"
      ],
      "isasync": False,
      "params": [
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "value",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list by value"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "key",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list by key"
        },
        {
          "name": "customer",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list by customer name"
        },
        {
          "name": "resourcetype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list by resource type"
        },
        {
          "name": "resourceid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list by resource id"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        }
      ],
      "requiredparams": [],
      "description": "List resource tag(s)"
    },
    "routers": {
      "name": "listRouters",
      "related": [
        "destroyRouter",
        "stopRouter",
        "startRouter",
        "stopInternalLoadBalancerVM",
        "listInternalLoadBalancerVMs",
        "rebootRouter",
        "startInternalLoadBalancerVM",
        "changeServiceForRouter"
      ],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "networkid",
          "required": False,
          "related": [
            "createNetwork",
            "listSrxFirewallNetworks",
            "listNiciraNvpDeviceNetworks",
            "listNetworks",
            "updateNetwork",
            "listF5LoadBalancerNetworks",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list by network id"
        },
        {
          "name": "podid",
          "required": False,
          "related": [
            "createPod",
            "updatePod",
            "listPods"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Pod ID of the router"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "activateProject",
            "listProjects",
            "suspendProject",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "vpcid",
          "required": False,
          "related": [
            "createVPC",
            "listVPCs",
            "restartVPC",
            "updateVPC"
          ],
          "length": 255,
          "type": "uuid",
          "description": "List networks by VPC"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the router"
        },
        {
          "name": "hostid",
          "required": False,
          "related": [
            "listExternalLoadBalancers",
            "addBaremetalHost",
            "addHost",
            "cancelHostMaintenance",
            "updateHost",
            "listHosts",
            "prepareHostForMaintenance"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the host ID of the router"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "version",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list virtual router elements by version"
        },
        {
          "name": "forvpc",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "if True is passed for this parameter, list only VPC routers"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "listLoadBalancerRuleInstances",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "recoverVirtualMachine",
            "deployVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "resetSSHKeyForVirtualMachine",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "addNicToVirtualMachine",
            "attachIso",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the disk router"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the state of the router"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID of the router"
        },
        {
          "name": "clusterid",
          "required": False,
          "related": [
            "updateCluster",
            "listClusters",
            "addCluster"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the cluster ID of the router"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "List routers."
    },
    "projectinvitations": {
      "name": "listProjectInvitations",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list invitations by state"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list by project id"
        },
        {
          "name": "activeonly",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "if True, list only active invitations - having Pending state and ones that are not timed out yet"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listProjectInvitations"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list invitations by id"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists projects and provides detailed information for listed projects"
    },
    "internalloadbalancervms": {
      "name": "listInternalLoadBalancerVMs",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the state of the Internal LB VM"
        },
        {
          "name": "vpcid",
          "required": False,
          "related": [
            "restartVPC"
          ],
          "length": 255,
          "type": "uuid",
          "description": "List Internal LB VMs by VPC"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "revertToVMSnapshot",
            "listVirtualMachines"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Internal LB VM"
        },
        {
          "name": "forvpc",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "if True is passed for this parameter, list only VPC Internal LB VMs"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the Internal LB VM"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "networkid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list by network id"
        },
        {
          "name": "podid",
          "required": False,
          "related": [
            "updatePod"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Pod ID of the Internal LB VM"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID of the Internal LB VM"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "hostid",
          "required": False,
          "related": [
            "listHosts"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the host ID of the Internal LB VM"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        }
      ],
      "requiredparams": [],
      "description": "List internal LB VMs."
    },
    "storagenetworkiprange": {
      "name": "listStorageNetworkIpRange",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "podid",
          "required": False,
          "related": [
            "updatePod"
          ],
          "length": 255,
          "type": "uuid",
          "description": "optional parameter. Pod uuid, if specicied and range uuid is absent, using it to search the range."
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listStorageNetworkIpRange"
          ],
          "length": 255,
          "type": "uuid",
          "description": "optional parameter. Storaget network IP range uuid, if specicied, using it to search the range."
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "optional parameter. Zone uuid, if specicied and both pod uuid and range uuid are absent, using it to search the range."
        }
      ],
      "requiredparams": [],
      "description": "List a storage network IP range."
    },
    "sshkeypairs": {
      "name": "listSSHKeyPairs",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "A key pair name to look for"
        },
        {
          "name": "fingerprint",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "A public key fingerprint to look for"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "activateProject",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "List registered keypairs"
    },
    "users": {
      "name": "listUsers",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List users by state of the user account."
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "accounttype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "long",
          "description": "List users by account type. Valid types include admin, domain-admin, read-only-admin, or user."
        },
        {
          "name": "username",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List user by the username"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listUsers"
          ],
          "length": 255,
          "type": "uuid",
          "description": "List user by ID."
        }
      ],
      "requiredparams": [],
      "description": "Lists user accounts"
    },
    "privategateways": {
      "name": "listPrivateGateways",
      "related": [
        "createPrivateGateway"
      ],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "ipaddress",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list gateways by ip address"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "vpcid",
          "required": False,
          "related": [
            "createVPC",
            "listVPCs",
            "restartVPC",
            "updateVPC"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list gateways by vpc"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listPrivateGateways",
            "createPrivateGateway"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list private gateway by id"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "vlan",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list gateways by vlan"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "activateProject",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list gateways by state"
        }
      ],
      "requiredparams": [],
      "description": "List private gateways"
    },
    "isos": {
      "name": "listIsos",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "domainid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list all isos by name"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "hypervisor",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the hypervisor for which to restrict the search"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "isofilter",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "possible values are \"featured\", \"self\", \"selfexecutable\",\"sharedexecutable\",\"executable\", and \"community\". * featured : templates that have been marked as featured and public. * self : templates that have been registered or created by the calling user. * selfexecutable : same as self, but only returns templates that can be used to deploy a new VM. * sharedexecutable : templates ready to be deployed that have been granted to the calling user by another user. * executable : templates that are owned by the calling user, or public templates, that can be used to deploy a VM. * community : templates that have been marked as public but not featured. * all : all templates (only usable by admins)."
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the zone"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "ispublic",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if the ISO is publicly available to all users, False otherwise."
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List resources by tags (key/value pairs)"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listIsos"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list ISO by id"
        },
        {
          "name": "isready",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if this ISO is ready to be deployed"
        },
        {
          "name": "showremoved",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "show removed ISOs as well"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "bootable",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if the ISO is bootable, False otherwise"
        }
      ],
      "requiredparams": [],
      "description": "Lists all available ISO files."
    },
    "dedicatedpods": {
      "name": "listDedicatedPods",
      "related": [
        "dedicatePod"
      ],
      "isasync": False,
      "params": [
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the domain associated with the pod"
        },
        {
          "name": "affinitygroupid",
          "required": False,
          "related": [
            "createAffinityGroup",
            "listAffinityGroups"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list dedicated pods by affinity group"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "podid",
          "required": False,
          "related": [
            "createPod",
            "updatePod",
            "listPods"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the pod"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the account associated with the pod. Must be used with domainId."
        }
      ],
      "requiredparams": [],
      "description": "Lists dedicated pods."
    },
    "dedicatedclusters": {
      "name": "listDedicatedClusters",
      "related": [
        "dedicateCluster"
      ],
      "isasync": False,
      "params": [
        {
          "name": "clusterid",
          "required": False,
          "related": [
            "updateCluster"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the cluster"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "affinitygroupid",
          "required": False,
          "related": [
            "listAffinityGroups"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list dedicated clusters by affinity group"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the domain associated with the cluster"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the account associated with the cluster. Must be used with domainId."
        }
      ],
      "requiredparams": [],
      "description": "Lists dedicated clusters."
    },
    "usagetypes": {
      "name": "listUsageTypes",
      "related": [],
      "isasync": False,
      "params": [],
      "requiredparams": [],
      "description": "List Usage Types"
    },
    "domainchildren": {
      "name": "listDomainChildren",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list children domain by parent domain ID."
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "to return the entire tree, use the value \"True\". To return the first level children, use the value \"False\"."
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list children domains by name"
        }
      ],
      "requiredparams": [],
      "description": "Lists all children domains belonging to a specified domain"
    },
    "domains": {
      "name": "listDomains",
      "related": [
        "updateDomain",
        "listDomainChildren"
      ],
      "isasync": False,
      "params": [
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List domain by domain name."
        },
        {
          "name": "level",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "List domains by domain level."
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "List domain by domain ID."
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        }
      ],
      "requiredparams": [],
      "description": "Lists domains and provides detailed information for listed domains"
    },
    "networkisolationmethods": {
      "name": "listNetworkIsolationMethods",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists supported methods of network isolation"
    },
    "netscalerloadbalancers": {
      "name": "listNetscalerLoadBalancers",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "physicalnetworkid",
          "required": False,
          "related": [
            "createPhysicalNetwork",
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "lbdeviceid",
          "required": False,
          "related": [
            "listNetscalerLoadBalancers"
          ],
          "length": 255,
          "type": "uuid",
          "description": "netscaler load balancer device ID"
        }
      ],
      "requiredparams": [],
      "description": "lists netscaler load balancer devices"
    },
    "s3s": {
      "name": "listS3s",
      "related": [
        "addSwift",
        "listSwifts",
        "addImageStore",
        "createSecondaryStagingStore",
        "listSecondaryStagingStores",
        "addS3"
      ],
      "isasync": False,
      "params": [
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists S3s"
    },
    "hypervisors": {
      "name": "listHypervisors",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the zone id for listing hypervisors."
        }
      ],
      "requiredparams": [],
      "description": "List hypervisors"
    },
    "ucstemplates": {
      "name": "listUcsTemplates",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "ucsmanagerid",
          "required": True,
          "related": [
            "addUcsManager"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the id for the ucs manager"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [
        "ucsmanagerid"
      ],
      "description": "List templates in ucs manager"
    },
    "traffictypes": {
      "name": "listTrafficTypes",
      "related": [
        "updateNetworkServiceProvider",
        "addNetworkServiceProvider"
      ],
      "isasync": False,
      "params": [
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "physicalnetworkid",
          "required": True,
          "related": [
            "createPhysicalNetwork",
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        }
      ],
      "requiredparams": [
        "physicalnetworkid"
      ],
      "description": "Lists traffic types of a given physical network."
    },
    "vlanipranges": {
      "name": "listVlanIpRanges",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "vlan",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the ID or VID of the VLAN. Default is an \"untagged\" VLAN."
        },
        {
          "name": "physicalnetworkid",
          "required": False,
          "related": [
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "physical network id of the VLAN IP range"
        },
        {
          "name": "podid",
          "required": False,
          "related": [
            "updatePod"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Pod ID of the VLAN IP range"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID of the VLAN IP range"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the account with which the VLAN IP range is associated. Must be used with the domainId parameter."
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listVlanIpRanges"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the VLAN IP range"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "project who will own the VLAN"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the domain ID with which the VLAN IP range is associated.  If used with the account parameter, returns all VLAN IP ranges for that account in the specified domain."
        },
        {
          "name": "forvirtualnetwork",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if VLAN is of Virtual type, False if Direct"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "networkid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "network id of the VLAN IP range"
        }
      ],
      "requiredparams": [],
      "description": "Lists all VLAN IP ranges."
    },
    "traffictypeimplementors": {
      "name": "listTrafficTypeImplementors",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "traffictype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Optional. The network traffic type, if specified, return its implementor. Otherwise, return all traffic types with their implementor"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        }
      ],
      "requiredparams": [],
      "description": "Lists implementors of implementor of a network traffic type or implementors of all network traffic types"
    },
    "isopermissions": {
      "name": "listIsoPermissions",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listIsoPermissions"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the template ID"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "List iso visibility and all accounts that have permissions to view this iso."
    },
    "snapshotpolicies": {
      "name": "listSnapshotPolicies",
      "related": [
        "createSnapshotPolicy"
      ],
      "isasync": False,
      "params": [
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "volumeid",
          "required": True,
          "related": [
            "uploadVolume",
            "createVolume",
            "detachVolume"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the disk volume"
        }
      ],
      "requiredparams": [
        "volumeid"
      ],
      "description": "Lists snapshot policies."
    },
    "loadbalancers": {
      "name": "listLoadBalancers",
      "related": [
        "createLoadBalancer"
      ],
      "isasync": False,
      "params": [
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "sourceipaddress",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the source ip address of the Load Balancer"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "sourceipaddressnetworkid",
          "required": False,
          "related": [
            "createNetwork",
            "listSrxFirewallNetworks",
            "listNetworks",
            "updateNetwork",
            "listF5LoadBalancerNetworks",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the network id of the source ip address"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the Load Balancer"
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List resources by tags (key/value pairs)"
        },
        {
          "name": "scheme",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the scheme of the Load Balancer. Supported value is Internal in the current release"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "networkid",
          "required": False,
          "related": [
            "createNetwork",
            "listSrxFirewallNetworks",
            "listNetworks",
            "updateNetwork",
            "listF5LoadBalancerNetworks",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the network id of the Load Balancer"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "activateProject",
            "listProjects",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "updatePortForwardingRule",
            "createIpForwardingRule",
            "listPortForwardingRules",
            "createPortForwardingRule",
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Load Balancer"
        }
      ],
      "requiredparams": [],
      "description": "Lists Load Balancers"
    },
    "paloaltofirewallnetworks": {
      "name": "listPaloAltoFirewallNetworks",
      "related": [
        "listSrxFirewallNetworks",
        "updateNetwork",
        "listNetscalerLoadBalancerNetworks"
      ],
      "isasync": False,
      "params": [
        {
          "name": "lbdeviceid",
          "required": True,
          "related": [
            "configurePaloAltoFirewall"
          ],
          "length": 255,
          "type": "uuid",
          "description": "palo alto balancer device ID"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [
        "lbdeviceid"
      ],
      "description": "lists network that are using Palo Alto firewall device"
    },
    "imagestores": {
      "name": "listImageStores",
      "related": [
        "addSwift",
        "listSwifts",
        "addImageStore",
        "createSecondaryStagingStore",
        "listS3s",
        "listSecondaryStagingStores",
        "addS3"
      ],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "addSwift",
            "listSwifts",
            "addImageStore",
            "createSecondaryStagingStore",
            "listS3s",
            "listSecondaryStagingStores",
            "addS3",
            "listImageStores"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the storage pool"
        },
        {
          "name": "protocol",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the image store protocol"
        },
        {
          "name": "provider",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the image store provider"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the image store"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID for the image store"
        }
      ],
      "requiredparams": [],
      "description": "Lists image stores."
    },
    "autoscalevmgroups": {
      "name": "listAutoScaleVmGroups",
      "related": [
        "enableAutoScaleVmGroup",
        "updateAutoScaleVmGroup",
        "disableAutoScaleVmGroup",
        "createAutoScaleVmGroup"
      ],
      "isasync": False,
      "params": [
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "vmprofileid",
          "required": False,
          "related": [
            "createAutoScaleVmProfile",
            "listAutoScaleVmProfiles",
            "updateAutoScaleVmProfile"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the profile"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "policyid",
          "required": False,
          "related": [
            "listAutoScalePolicies",
            "updateAutoScalePolicy",
            "createAutoScalePolicy"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the policy"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "activateProject",
            "listProjects",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the availability zone ID"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "lbruleid",
          "required": False,
          "related": [
            "updatePortForwardingRule",
            "createIpForwardingRule",
            "listPortForwardingRules",
            "createPortForwardingRule",
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the loadbalancer"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listAutoScaleVmGroups",
            "enableAutoScaleVmGroup",
            "updateAutoScaleVmGroup",
            "disableAutoScaleVmGroup",
            "createAutoScaleVmGroup"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the autoscale vm group"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists autoscale vm groups."
    },
    "internalloadbalancerelements": {
      "name": "listInternalLoadBalancerElements",
      "related": [
        "createInternalLoadBalancerElement",
        "configureInternalLoadBalancerElement"
      ],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "nspid",
          "required": False,
          "related": [
            "listTrafficTypes",
            "updateNetworkServiceProvider",
            "addNetworkServiceProvider"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list internal load balancer elements by network service provider id"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listInternalLoadBalancerElements",
            "createInternalLoadBalancerElement",
            "configureInternalLoadBalancerElement"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list internal load balancer elements by id"
        },
        {
          "name": "enabled",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "list internal load balancer elements by enabled state"
        }
      ],
      "requiredparams": [],
      "description": "Lists all available Internal Load Balancer elements."
    },
    "projectaccounts": {
      "name": "listProjectAccounts",
      "related": [
        "createProject",
        "updateProject"
      ],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "projectid",
          "required": True,
          "related": [
            "createProject",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of the project"
        },
        {
          "name": "role",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list accounts of the project by role"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list accounts of the project by account name"
        }
      ],
      "requiredparams": [
        "projectid"
      ],
      "description": "Lists project's accounts"
    },
    "autoscalevmprofiles": {
      "name": "listAutoScaleVmProfiles",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "otherdeployparams",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the otherdeployparameters of the autoscale vm profile"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listAutoScaleVmProfiles"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the autoscale vm profile"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "templateid",
          "required": False,
          "related": [
            "listIsos",
            "updateIso"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the templateid of the autoscale vm profile"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        }
      ],
      "requiredparams": [],
      "description": "Lists autoscale vm profiles."
    },
    "apis": {
      "name": "listApis",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "API name"
        }
      ],
      "requiredparams": [],
      "description": "lists all available apis on the server, provided by the Api Discovery plugin"
    },
    "vpcs": {
      "name": "listVPCs",
      "related": [
        "restartVPC"
      ],
      "isasync": False,
      "params": [
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "restartrequired",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "list VPCs by restartRequired option"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "displaytext",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by display text of the VPC"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listVPCs",
            "restartVPC"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list VPC by id"
        },
        {
          "name": "vpcofferingid",
          "required": False,
          "related": [
            "listVPCOfferings"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list by ID of the VPC offering"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List resources by tags (key/value pairs)"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "supportedservices",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "list VPC supporting certain services"
        },
        {
          "name": "cidr",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list by cidr of the VPC. All VPC guest networks' cidrs should be within this CIDR"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list by zone"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list VPCs by state"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list by name of the VPC"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists VPCs"
    },
    "resourcedetails": {
      "name": "listResourceDetails",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "fordisplay",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "if set to True, only details marked with display=True, are returned. Always False is the call is made by the regular user"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "key",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list by key"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "resourceid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list by resource id"
        },
        {
          "name": "resourcetype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list by resource type"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        }
      ],
      "requiredparams": [
        "resourceid",
        "resourcetype"
      ],
      "description": "List resource detail(s)"
    },
    "f5loadbalancers": {
      "name": "listF5LoadBalancers",
      "related": [
        "addF5LoadBalancer",
        "configureF5LoadBalancer"
      ],
      "isasync": False,
      "params": [
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "physicalnetworkid",
          "required": False,
          "related": [
            "updatePhysicalNetwork",
            "createPhysicalNetwork",
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        },
        {
          "name": "lbdeviceid",
          "required": False,
          "related": [
            "listF5LoadBalancers",
            "addF5LoadBalancer",
            "configureF5LoadBalancer"
          ],
          "length": 255,
          "type": "uuid",
          "description": "f5 load balancer device ID"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "lists F5 load balancer devices"
    },
    "vpncustomergateways": {
      "name": "listVpnCustomerGateways",
      "related": [
        "updateVpnCustomerGateway"
      ],
      "isasync": False,
      "params": [
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "updateVpnCustomerGateway",
            "listVpnCustomerGateways"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of the customer gateway"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists site to site vpn customer gateways"
    },
    "dedicatedhosts": {
      "name": "listDedicatedHosts",
      "related": [
        "dedicateHost"
      ],
      "isasync": False,
      "params": [
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the domain associated with the host"
        },
        {
          "name": "affinitygroupid",
          "required": False,
          "related": [
            "listAffinityGroups"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list dedicated hosts by affinity group"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "hostid",
          "required": False,
          "related": [
            "listExternalLoadBalancers",
            "addHost",
            "updateHost",
            "listHosts",
            "prepareHostForMaintenance"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the host"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the account associated with the host. Must be used with domainId."
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        }
      ],
      "requiredparams": [],
      "description": "Lists dedicated hosts."
    },
    "networkofferings": {
      "name": "listNetworkOfferings",
      "related": [
        "createNetworkOffering",
        "updateNetworkOffering"
      ],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": False,
          "related": [
            "createNetworkOffering",
            "listNetworkOfferings",
            "updateNetworkOffering"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list network offerings by id"
        },
        {
          "name": "supportedservices",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "list network offerings supporting certain services"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list netowrk offerings available for network creation in specific zone"
        },
        {
          "name": "guestiptype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list network offerings by guest type: Shared or Isolated"
        },
        {
          "name": "istagged",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if offering has tags specified"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list network offerings by name"
        },
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list network offerings by state"
        },
        {
          "name": "networkid",
          "required": False,
          "related": [
            "createNetwork",
            "listSrxFirewallNetworks",
            "listNetworks",
            "updateNetwork",
            "listF5LoadBalancerNetworks",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the network. Pass this in if you want to see the available network offering that a network can be changed to."
        },
        {
          "name": "isdefault",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if need to list only default network offerings. Default value is False"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "traffictype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list by traffic type"
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 4096,
          "type": "string",
          "description": "list network offerings by tags"
        },
        {
          "name": "forvpc",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "the network offering can be used only for network creation inside the VPC"
        },
        {
          "name": "displaytext",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list network offerings by display text"
        },
        {
          "name": "sourcenatsupported",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if need to list only netwok offerings where source nat is supported, False otherwise"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "availability",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the availability of network offering. Default value is Required"
        },
        {
          "name": "specifyvlan",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "the tags for the network offering."
        },
        {
          "name": "specifyipranges",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if need to list only network offerings which support specifying ip ranges"
        }
      ],
      "requiredparams": [],
      "description": "Lists all available network offerings."
    },
    "zones": {
      "name": "listZones",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "networktype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the network type of the zone that the virtual machine belongs to"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the domain associated with the zone"
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List zones by resource tags (key/value pairs)"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listZones"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the zone"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the zone"
        },
        {
          "name": "showcapacities",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "flag to display the capacity of the zones"
        },
        {
          "name": "available",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if you want to retrieve all available Zones. False if you only want to return the Zones from which you have at least one VM. Default is False."
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists zones"
    },
    "virtualmachines": {
      "name": "listVirtualMachines",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List resources by tags (key/value pairs)"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "podid",
          "required": False,
          "related": [
            "updatePod"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the pod ID"
        },
        {
          "name": "vpcid",
          "required": False,
          "related": [
            "restartVPC"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list vms by vpc"
        },
        {
          "name": "affinitygroupid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list vms by affinity group"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of the virtual machine"
        },
        {
          "name": "hostid",
          "required": False,
          "related": [
            "listHosts"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the host ID"
        },
        {
          "name": "groupid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the group ID"
        },
        {
          "name": "hypervisor",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the target hypervisor for the template"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "forvirtualnetwork",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "list by network type; True if need to list vms using Virtual Network, False otherwise"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the availability zone ID"
        },
        {
          "name": "details",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "comma separated list of host details requested, value can be a list of [all, group, nics, stats, secgrp, tmpl, servoff, iso, volume, min, affgrp]. If no parameter is passed in, the details will be defaulted to all"
        },
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "state of the virtual machine"
        },
        {
          "name": "networkid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list by network id"
        },
        {
          "name": "isoid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list vms by iso"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listVirtualMachines"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the virtual machine"
        },
        {
          "name": "templateid",
          "required": False,
          "related": [
            "listIsos"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list vms by template"
        },
        {
          "name": "storageid",
          "required": False,
          "related": [
            "findStoragePoolsForMigration"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the storage ID where vm's volumes belong to"
        }
      ],
      "requiredparams": [],
      "description": "List the virtual machines owned by the account."
    },
    "netscalerloadbalancernetworks": {
      "name": "listNetscalerLoadBalancerNetworks",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "lbdeviceid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "netscaler load balancer device ID"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        }
      ],
      "requiredparams": [
        "lbdeviceid"
      ],
      "description": "lists network that are using a netscaler load balancer device"
    },
    "oscategories": {
      "name": "listOsCategories",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list os category by name"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listOsCategories"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list Os category by id"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists all supported OS categories for this cloud."
    },
    "ldapusers": {
      "name": "listLdapUsers",
      "related": [
        "searchLdap"
      ],
      "isasync": False,
      "params": [
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "listtype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Determines whether all ldap users are returned or just non-cloudstack users"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists all LDAP Users"
    },
    "affinitygroups": {
      "name": "listAffinityGroups",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "type",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "lists affinity groups by type"
        },
        {
          "name": "virtualmachineid",
          "required": False,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "lists affinity groups by virtual machine id"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "lists affinity groups by name"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listAffinityGroups"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list the affinity group by the id provided"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        }
      ],
      "requiredparams": [],
      "description": "Lists affinity groups"
    },
    "secondarystagingstores": {
      "name": "listSecondaryStagingStores",
      "related": [
        "listSwifts",
        "addImageStore",
        "createSecondaryStagingStore"
      ],
      "isasync": False,
      "params": [
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the staging store"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "provider",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the staging store provider"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "protocol",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the staging store protocol"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Zone ID for the staging store"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listSwifts",
            "addImageStore",
            "createSecondaryStagingStore",
            "listSecondaryStagingStores"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the staging store"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists secondary staging stores."
    },
    "virtualrouterelements": {
      "name": "listVirtualRouterElements",
      "related": [
        "createVirtualRouterElement",
        "configureVirtualRouterElement"
      ],
      "isasync": False,
      "params": [
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "createVirtualRouterElement",
            "configureVirtualRouterElement",
            "listVirtualRouterElements"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list virtual router elements by id"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "nspid",
          "required": False,
          "related": [
            "listTrafficTypes",
            "updateNetworkServiceProvider",
            "addNetworkServiceProvider"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list virtual router elements by network service provider id"
        },
        {
          "name": "enabled",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "list network offerings by enabled state"
        }
      ],
      "requiredparams": [],
      "description": "Lists all available virtual router elements."
    },
    "ciscovnmcresources": {
      "name": "listCiscoVnmcResources",
      "related": [
        "addCiscoVnmcResource"
      ],
      "isasync": False,
      "params": [
        {
          "name": "physicalnetworkid",
          "required": False,
          "related": [
            "updatePhysicalNetwork",
            "createPhysicalNetwork",
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        },
        {
          "name": "resourceid",
          "required": False,
          "related": [
            "addCiscoVnmcResource",
            "listCiscoVnmcResources"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Cisco VNMC resource ID"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        }
      ],
      "requiredparams": [],
      "description": "Lists Cisco VNMC controllers"
    },
    "asyncjobs": {
      "name": "listAsyncJobs",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "startdate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "tzdate",
          "description": "the start date of the async job"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists all pending asynchronous jobs for the account."
    },
    "ostypes": {
      "name": "listOsTypes",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "description",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list os by description"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listOsTypes"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list by Os type Id"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "oscategoryid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list by Os Category id"
        }
      ],
      "requiredparams": [],
      "description": "Lists all supported OS types for this cloud."
    },
    "globalloadbalancerrules": {
      "name": "listGlobalLoadBalancerRules",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "regionid",
          "required": False,
          "related": [
            "addRegion"
          ],
          "length": 255,
          "type": "integer",
          "description": "region ID"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listGlobalLoadBalancerRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the global load balancer rule"
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List resources by tags (key/value pairs)"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists load balancer rules."
    },
    "networkacls": {
      "name": "listNetworkACLs",
      "related": [
        "updateNetworkACLItem",
        "createNetworkACL"
      ],
      "isasync": False,
      "params": [
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "activateProject",
            "listProjects",
            "suspendProject",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "networkid",
          "required": False,
          "related": [
            "createNetwork",
            "listSrxFirewallNetworks",
            "listNiciraNvpDeviceNetworks",
            "listNetworks",
            "updateNetwork",
            "listF5LoadBalancerNetworks",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list network ACL Items by network Id"
        },
        {
          "name": "protocol",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list network ACL Items by Protocol"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List resources by tags (key/value pairs)"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "action",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list network ACL Items by Action"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "updateNetworkACLItem",
            "createNetworkACL",
            "listNetworkACLs"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Lists network ACL Item with the specified ID"
        },
        {
          "name": "aclid",
          "required": False,
          "related": [
            "listNetworkACLLists",
            "createNetworkACLList"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list network ACL Items by ACL Id"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "traffictype",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list network ACL Items by traffic type - Ingress or Egress"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        }
      ],
      "requiredparams": [],
      "description": "Lists all network ACL items"
    },
    "eventtypes": {
      "name": "listEventTypes",
      "related": [],
      "isasync": False,
      "params": [],
      "requiredparams": [],
      "description": "List Event Types"
    },
    "remoteaccessvpns": {
      "name": "listRemoteAccessVpns",
      "related": [
        "createRemoteAccessVpn"
      ],
      "isasync": False,
      "params": [
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "networkid",
          "required": False,
          "related": [
            "listSrxFirewallNetworks",
            "updateNetwork",
            "listPaloAltoFirewallNetworks",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list remote access VPNs for ceratin network"
        },
        {
          "name": "publicipid",
          "required": False,
          "related": [
            "associateIpAddress",
            "restartNetwork"
          ],
          "length": 255,
          "type": "uuid",
          "description": "public ip address id of the vpn server"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listRemoteAccessVpns",
            "createRemoteAccessVpn"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Lists remote access vpn rule with the specified ID"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        }
      ],
      "requiredparams": [],
      "description": "Lists remote access vpns"
    },
    "ucsprofiles": {
      "name": "listUcsProfiles",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "ucsmanagerid",
          "required": True,
          "related": [
            "addUcsManager"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the id for the ucs manager"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [
        "ucsmanagerid"
      ],
      "description": "List profile in ucs manager"
    },
    "nics": {
      "name": "listNics",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "virtualmachineid",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the vm"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "nicid",
          "required": False,
          "related": [
            "listNics"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the nic to to list IPs"
        }
      ],
      "requiredparams": [
        "virtualmachineid"
      ],
      "description": "list the vm nics  IP to NIC"
    },
    "lbhealthcheckpolicies": {
      "name": "listLBHealthCheckPolicies",
      "related": [
        "createLBHealthCheckPolicy"
      ],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "lbruleid",
          "required": True,
          "related": [
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the load balancer rule"
        }
      ],
      "requiredparams": [
        "lbruleid"
      ],
      "description": "Lists load balancer HealthCheck policies."
    },
    "regions": {
      "name": "listRegions",
      "related": [
        "addRegion"
      ],
      "isasync": False,
      "params": [
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "List Region by region ID."
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List Region by region name."
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists Regions"
    },
    "vpcofferings": {
      "name": "listVPCOfferings",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "state",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list VPC offerings by state"
        },
        {
          "name": "supportedservices",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "list VPC offerings supporting certain services"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listVPCOfferings"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list VPC offerings by id"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list VPC offerings by name"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "displaytext",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list VPC offerings by display text"
        },
        {
          "name": "isdefault",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if need to list only default VPC offerings. Default value is False"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        }
      ],
      "requiredparams": [],
      "description": "Lists VPC offerings"
    },
    "sslcerts": {
      "name": "listSslCerts",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "accountid",
          "required": False,
          "related": [
            "listAccounts",
            "markDefaultZoneForAccount",
            "disableAccount"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Account Id"
        },
        {
          "name": "certid",
          "required": False,
          "related": [
            "listSslCerts"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Id of SSL certificate"
        },
        {
          "name": "lbruleid",
          "required": False,
          "related": [
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Loadbalancer Rule Id"
        }
      ],
      "requiredparams": [],
      "description": "Lists SSL certificates"
    },
    "niciranvpdevicenetworks": {
      "name": "listNiciraNvpDeviceNetworks",
      "related": [
        "createNetwork",
        "listSrxFirewallNetworks",
        "listNetworks",
        "updateNetwork",
        "listF5LoadBalancerNetworks",
        "listPaloAltoFirewallNetworks",
        "listNetscalerLoadBalancerNetworks"
      ],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "nvpdeviceid",
          "required": True,
          "related": [
            "addNiciraNvpDevice",
            "listNiciraNvpDevices"
          ],
          "length": 255,
          "type": "uuid",
          "description": "nicira nvp device ID"
        }
      ],
      "requiredparams": [
        "nvpdeviceid"
      ],
      "description": "lists network that are using a nicira nvp device"
    },
    "events": {
      "name": "listEvents",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "entrytime",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the time the event was entered"
        },
        {
          "name": "startdate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "date",
          "description": "the start date range of the list you want to retrieve (use format \"yyyy-MM-dd\" or the new format \"yyyy-MM-dd HH:mm:ss\")"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listEvents"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the event"
        },
        {
          "name": "level",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the event level (INFO, WARN, ERROR)"
        },
        {
          "name": "enddate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "date",
          "description": "the end date range of the list you want to retrieve (use format \"yyyy-MM-dd\" or the new format \"yyyy-MM-dd HH:mm:ss\")"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "type",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the event type (see event types)"
        },
        {
          "name": "duration",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "the duration of the event"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        }
      ],
      "requiredparams": [],
      "description": "A command to list events."
    },
    "templates": {
      "name": "listTemplates",
      "related": [
        "registerIso",
        "prepareTemplate",
        "listIsos",
        "copyIso",
        "updateIso",
        "updateTemplate"
      ],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List resources by tags (key/value pairs)"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "hypervisor",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the hypervisor for which to restrict the search"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "registerIso",
            "prepareTemplate",
            "listIsos",
            "copyIso",
            "updateIso",
            "updateTemplate",
            "listTemplates"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the template ID"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the template name"
        },
        {
          "name": "templatefilter",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "possible values are \"featured\", \"self\", \"selfexecutable\",\"sharedexecutable\",\"executable\", and \"community\". * featured : templates that have been marked as featured and public. * self : templates that have been registered or created by the calling user. * selfexecutable : same as self, but only returns templates that can be used to deploy a new VM. * sharedexecutable : templates ready to be deployed that have been granted to the calling user by another user. * executable : templates that are owned by the calling user, or public templates, that can be used to deploy a VM. * community : templates that have been marked as public but not featured. * all : all templates (only usable by admins)."
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "showremoved",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "show removed templates as well"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list templates by zoneId"
        }
      ],
      "requiredparams": [
        "templatefilter"
      ],
      "description": "List all public, private, and privileged templates."
    },
    "cisconexusvsms": {
      "name": "listCiscoNexusVSMs",
      "related": [
        "enableCiscoNexusVSM",
        "disableCiscoNexusVSM"
      ],
      "isasync": False,
      "params": [
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "clusterid",
          "required": False,
          "related": [
            "updateCluster"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Id of the CloudStack cluster in which the Cisco Nexus 1000v VSM appliance."
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Id of the CloudStack cluster in which the Cisco Nexus 1000v VSM appliance."
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        }
      ],
      "requiredparams": [],
      "description": "Retrieves a Cisco Nexus 1000v Virtual Switch Manager device associated with a Cluster"
    },
    "ipforwardingrules": {
      "name": "listIpForwardingRules",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "virtualmachineid",
          "required": False,
          "related": [
            "revertToVMSnapshot",
            "listVirtualMachines",
            "destroyVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Lists all rules applied to the specified Vm."
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "ipaddressid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list the rule belonging to this public ip address"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Lists rule with the specified ID."
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        }
      ],
      "requiredparams": [],
      "description": "List the ip forwarding rules"
    },
    "srxfirewalls": {
      "name": "listSrxFirewalls",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "fwdeviceid",
          "required": False,
          "related": [
            "listSrxFirewalls"
          ],
          "length": 255,
          "type": "uuid",
          "description": "SRX firewall device ID"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "physicalnetworkid",
          "required": False,
          "related": [
            "listPhysicalNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Physical Network ID"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "lists SRX firewall devices in a physical network"
    },
    "vpnconnections": {
      "name": "listVpnConnections",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "vpcid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "id of vpc"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listVpnConnections"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of the vpn connection"
        }
      ],
      "requiredparams": [],
      "description": "Lists site to site vpn connection gateways"
    },
    "trafficmonitors": {
      "name": "listTrafficMonitors",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "zone Id"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [
        "zoneid"
      ],
      "description": "List traffic monitor Hosts."
    },
    "vpnusers": {
      "name": "listVpnUsers",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "username",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the username of the vpn user."
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listVpnUsers"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The uuid of the Vpn user"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        }
      ],
      "requiredparams": [],
      "description": "Lists vpn users"
    },
    "egressfirewallrules": {
      "name": "listEgressFirewallRules",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "networkid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list firewall rules for ceratin network"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "id",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "Lists rule with the specified ID."
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List resources by tags (key/value pairs)"
        },
        {
          "name": "ipaddressid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the id of IP address of the firwall services"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "networkid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the id network network for the egress firwall services"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "id",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "Lists rule with the specified ID."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        }
      ],
      "requiredparams": [],
      "description": "Lists all egress firewall rules for network id."
    },
    "externalloadbalancers": {
      "name": "listExternalLoadBalancers",
      "related": [
        "listHosts"
      ],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "zone Id"
        }
      ],
      "requiredparams": [],
      "description": "Lists F5 external load balancer appliances added in a zone."
    },
    "pods": {
      "name": "listPods",
      "related": [
        "createPod",
        "updatePod"
      ],
      "isasync": False,
      "params": [
        {
          "name": "allocationstate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list pods by allocation state"
        },
        {
          "name": "showcapacities",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "flag to display the capacity of the pods"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list Pods by Zone ID"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list Pods by name"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "createPod",
            "updatePod",
            "listPods"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list Pods by ID"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        }
      ],
      "requiredparams": [],
      "description": "Lists all Pods."
    },
    "staticroutes": {
      "name": "listStaticRoutes",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listStaticRoutes"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list static route by id"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "vpcid",
          "required": False,
          "related": [
            "createVPC",
            "listVPCs",
            "restartVPC"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list static routes by vpc id"
        },
        {
          "name": "gatewayid",
          "required": False,
          "related": [
            "createPrivateGateway"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list static routes by gateway id"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List resources by tags (key/value pairs)"
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        }
      ],
      "requiredparams": [],
      "description": "Lists all static routes"
    },
    "portableipranges": {
      "name": "listPortableIpRanges",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "regionid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "Id of a Region"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listPortableIpRanges"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Id of the portable ip range"
        }
      ],
      "requiredparams": [],
      "description": "list portable IP ranges"
    },
    "volumes": {
      "name": "listVolumes",
      "related": [
        "migrateVolume",
        "uploadVolume",
        "resizeVolume",
        "updateVolume",
        "createVolume",
        "detachVolume",
        "attachVolume"
      ],
      "isasync": False,
      "params": [
        {
          "name": "hostid",
          "required": False,
          "related": [
            "listExternalLoadBalancers",
            "addBaremetalHost",
            "addHost",
            "cancelHostMaintenance",
            "updateHost",
            "listHosts",
            "prepareHostForMaintenance"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list volumes on specified host"
        },
        {
          "name": "podid",
          "required": False,
          "related": [
            "createPod",
            "updatePod",
            "listPods"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the pod id the disk volume belongs to"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list only resources belonging to the domain specified"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "migrateVolume",
            "uploadVolume",
            "resizeVolume",
            "updateVolume",
            "createVolume",
            "detachVolume",
            "listVolumes",
            "attachVolume"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the disk volume"
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "isrecursive",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "defaults to False, but if True, lists all resources from the parent specified by the domainId till leaves."
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the disk volume"
        },
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "listall",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "If set to False, list only resources belonging to the command's caller; if set to True - list resources that the caller is authorized to see. Default value is False"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "activateProject",
            "listProjects",
            "suspendProject",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "list objects by project"
        },
        {
          "name": "storageid",
          "required": False,
          "related": [
            "findStoragePoolsForMigration",
            "updateStoragePool",
            "cancelStorageMaintenance",
            "createStoragePool",
            "enableStorageMaintenance",
            "listStoragePools"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the storage pool, available to ROOT admin only"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the availability zone"
        },
        {
          "name": "type",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the type of disk volume"
        },
        {
          "name": "virtualmachineid",
          "required": False,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "updateVMAffinityGroup",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "listLoadBalancerRuleInstances",
            "stopVirtualMachine",
            "rebootVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "recoverVirtualMachine",
            "deployVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "resetSSHKeyForVirtualMachine",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "attachIso",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the virtual machine"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "list resources by account. Must be used with the domainId parameter."
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "List resources by tags (key/value pairs)"
        }
      ],
      "requiredparams": [],
      "description": "Lists all volumes."
    },
    "deploymentplanners": {
      "name": "listDeploymentPlanners",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "keyword",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "List by keyword"
        },
        {
          "name": "page",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        },
        {
          "name": "pagesize",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": ""
        }
      ],
      "requiredparams": [],
      "description": "Lists all DeploymentPlanners available."
    }
  },
  "upload": {
    "volume": {
      "name": "uploadVolume",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "an optional accountName. Must be used with domainId."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "an optional domainId. If the account parameter is used, domainId must also be used."
        },
        {
          "name": "checksum",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the MD5 checksum value of this volume"
        },
        {
          "name": "url",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the URL of where the volume is hosted. Possible URL include http:// and https://"
        },
        {
          "name": "imagestoreuuid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Image store uuid"
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the zone the volume is to be hosted on"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the name of the volume"
        },
        {
          "name": "format",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the format for the volume. Possible values include QCOW2, OVA, and VHD."
        },
        {
          "name": "projectid",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "Upload volume for the project"
        }
      ],
      "requiredparams": [
        "url",
        "zoneid",
        "name",
        "format"
      ],
      "description": "Uploads a data disk."
    },
    "sslcert": {
      "name": "uploadSslCert",
      "related": [
        "listSslCerts"
      ],
      "isasync": False,
      "params": [
        {
          "name": "password",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Password for the private key"
        },
        {
          "name": "certchain",
          "required": False,
          "related": [],
          "length": 2097152,
          "type": "string",
          "description": "Certificate chain of trust"
        },
        {
          "name": "certificate",
          "required": True,
          "related": [],
          "length": 16384,
          "type": "string",
          "description": "SSL certificate"
        },
        {
          "name": "privatekey",
          "required": True,
          "related": [],
          "length": 16384,
          "type": "string",
          "description": "Private key"
        }
      ],
      "requiredparams": [
        "certificate",
        "privatekey"
      ],
      "description": "Upload a certificate to cloudstack"
    },
    "customcertificate": {
      "name": "uploadCustomCertificate",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "privatekey",
          "required": False,
          "related": [],
          "length": 65535,
          "type": "string",
          "description": "The private key for the attached certificate."
        },
        {
          "name": "domainsuffix",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "DNS domain suffix that the certificate is granted for."
        },
        {
          "name": "certificate",
          "required": True,
          "related": [],
          "length": 65535,
          "type": "string",
          "description": "The certificate to be uploaded."
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "A name / alias for the certificate."
        },
        {
          "name": "id",
          "required": False,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "An integer providing the location in a chain that the certificate will hold. Usually, this can be left empty. When creating a chain, the top level certificate should have an ID of 1, with each step in the chain incrementing by one. Example, CA with id = 1, Intermediate CA with id = 2, Site certificate with ID = 3"
        }
      ],
      "requiredparams": [
        "domainsuffix",
        "certificate"
      ],
      "description": "Uploads a custom certificate for the console proxy VMs to use for SSL. Can be used to upload a single certificate signed by a known CA. Can also be used, through multiple calls, to upload a chain of certificates from CA to the custom certificate itself."
    }
  },
  "remove": {
    "fromgloballoadbalancerrule": {
      "name": "removeFromGlobalLoadBalancerRule",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "loadbalancerrulelist",
          "required": True,
          "related": [
            "updatePortForwardingRule",
            "createIpForwardingRule",
            "listPortForwardingRules",
            "createPortForwardingRule",
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "list",
          "description": "the list load balancer rules that will be assigned to gloabal load balacner rule"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "updateGlobalLoadBalancerRule",
            "listGlobalLoadBalancerRules",
            "createGlobalLoadBalancerRule"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the load balancer rule"
        }
      ],
      "requiredparams": [
        "loadbalancerrulelist",
        "id"
      ],
      "description": "Removes a load balancer rule association with global load balancer rule"
    },
    "fromloadbalancerrule": {
      "name": "removeFromLoadBalancerRule",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the load balancer rule"
        },
        {
          "name": "virtualmachineids",
          "required": True,
          "related": [
            "migrateVirtualMachineWithVolume",
            "stopVirtualMachine",
            "updateVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "list",
          "description": "the list of IDs of the virtual machines that are being removed from the load balancer rule (i.e. virtualMachineIds=1,2,3)"
        }
      ],
      "requiredparams": [
        "id",
        "virtualmachineids"
      ],
      "description": "Removes a virtual machine or a list of virtual machines from a load balancer rule."
    },
    "resourcedetail": {
      "name": "removeResourceDetail",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "resourceid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Delete details for resource id"
        },
        {
          "name": "resourcetype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Delete detail by resource type"
        },
        {
          "name": "key",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Delete details matching key/value pairs"
        }
      ],
      "requiredparams": [
        "resourceid",
        "resourcetype"
      ],
      "description": "Removes detail for the Resource."
    },
    "region": {
      "name": "removeRegion",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [],
          "length": 255,
          "type": "integer",
          "description": "ID of the region to delete"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Removes specified region"
    },
    "nicfromvirtualmachine": {
      "name": "removeNicFromVirtualMachine",
      "related": [
        "detachIso",
        "migrateVirtualMachineWithVolume",
        "startVirtualMachine",
        "migrateVirtualMachine",
        "stopVirtualMachine",
        "updateVirtualMachine",
        "changeServiceForVirtualMachine",
        "updateDefaultNicForVirtualMachine",
        "revertToVMSnapshot",
        "listVirtualMachines",
        "resetPasswordForVirtualMachine",
        "assignVirtualMachine",
        "destroyVirtualMachine",
        "restoreVirtualMachine"
      ],
      "isasync": True,
      "params": [
        {
          "name": "nicid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "NIC ID"
        },
        {
          "name": "virtualmachineid",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "removeNicFromVirtualMachine",
            "updateVirtualMachine",
            "changeServiceForVirtualMachine",
            "updateDefaultNicForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "resetPasswordForVirtualMachine",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Virtual Machine ID"
        }
      ],
      "requiredparams": [
        "nicid",
        "virtualmachineid"
      ],
      "description": "Removes VM from specified network by deleting a NIC"
    },
    "vpnuser": {
      "name": "removeVpnUser",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "username",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "username for the vpn user"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "an optional account for the vpn user. Must be used with domainId."
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "remove vpn user from the project"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "an optional domainId for the vpn user. If the account parameter is used, domainId must also be used."
        }
      ],
      "requiredparams": [
        "username"
      ],
      "description": "Removes vpn user"
    },
    "vmwaredc": {
      "name": "removeVmwareDc",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The id of Zone from which VMware datacenter has to be removed."
        }
      ],
      "requiredparams": [
        "zoneid"
      ],
      "description": "Remove a VMware datacenter from a zone."
    },
    "certfromloadbalancer": {
      "name": "removeCertFromLoadBalancer",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "lbruleid",
          "required": True,
          "related": [
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the load balancer rule"
        }
      ],
      "requiredparams": [
        "lbruleid"
      ],
      "description": "Removes a certificate from a Load Balancer Rule"
    },
    "ipfromnic": {
      "name": "removeIpFromNic",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "addIpToNic"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the secondary ip address to nic"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Removes secondary IP from the NIC."
    }
  },
  "mark": {
    "defaultzoneforaccount": {
      "name": "markDefaultZoneForAccount",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "account",
          "required": True,
          "related": [
            "markDefaultZoneForAccount"
          ],
          "length": 255,
          "type": "string",
          "description": "Name of the account that is to be marked."
        },
        {
          "name": "domainid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "Marks the account that belongs to the specified domain."
        },
        {
          "name": "zoneid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "The Zone ID with which the account is to be marked."
        }
      ],
      "requiredparams": [
        "account",
        "domainid",
        "zoneid"
      ],
      "description": "Marks a default zone for this account"
    }
  },
  "instantiate": {
    "ucstemplateandassocaciatetoblade": {
      "name": "instantiateUcsTemplateAndAssocaciateToBlade",
      "related": [
        "refreshUcsBlades"
      ],
      "isasync": True,
      "params": [
        {
          "name": "ucsmanagerid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "ucs manager id"
        },
        {
          "name": "bladeid",
          "required": True,
          "related": [
            "instantiateUcsTemplateAndAssocaciateToBlade",
            "refreshUcsBlades"
          ],
          "length": 255,
          "type": "uuid",
          "description": "blade id"
        },
        {
          "name": "templatedn",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "template dn"
        },
        {
          "name": "profilename",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "profile name"
        }
      ],
      "requiredparams": [
        "ucsmanagerid",
        "bladeid",
        "templatedn"
      ],
      "description": "create a profile of template and associate to a blade"
    }
  },
  "asyncapis": [
    "createCondition",
    "reconnectHost",
    "copyTemplate",
    "addNicToVirtualMachine",
    "extractVolume",
    "addAccountToProject",
    "deleteEgressFirewallRule",
    "deleteCiscoNexusVSM",
    "createVpnConnection",
    "suspendProject",
    "deleteLoadBalancer",
    "authorizeSecurityGroupIngress",
    "addNetscalerLoadBalancer",
    "deleteDomain",
    "createPortableIpRange",
    "configureNetscalerLoadBalancer",
    "createTemplate",
    "migrateVolume",
    "deleteLBHealthCheckPolicy",
    "updatePhysicalNetwork",
    "deleteStaticRoute",
    "deletePaloAltoFirewall",
    "destroySystemVm",
    "enableStorageMaintenance",
    "removeFromGlobalLoadBalancerRule",
    "stopRouter",
    "attachVolume",
    "updateVPCOffering",
    "resetSSHKeyForVirtualMachine",
    "cleanVMReservations",
    "createAffinityGroup",
    "deleteTags",
    "deleteAccountFromProject",
    "addBaremetalPxePingServer",
    "deletePortableIpRange",
    "updateVolume",
    "uploadCustomCertificate",
    "createAutoScaleVmProfile",
    "releaseDedicatedGuestVlanRange",
    "cancelHostMaintenance",
    "releaseDedicatedHost",
    "deleteStorageNetworkIpRange",
    "createInternalLoadBalancerElement",
    "deleteFirewallRule",
    "deleteNiciraNvpDevice",
    "deleteProject",
    "removeIpFromNic",
    "deleteIpForwardingRule",
    "createGlobalLoadBalancerRule",
    "resizeVolume",
    "createStaticRoute",
    "deleteGlobalLoadBalancerRule",
    "activateProject",
    "releaseDedicatedZone",
    "createVMSnapshot",
    "configureF5LoadBalancer",
    "createIpForwardingRule",
    "addPaloAltoFirewall",
    "releaseDedicatedCluster",
    "updateVPC",
    "associateUcsProfileToBlade",
    "startInternalLoadBalancerVM",
    "updateAutoScaleVmProfile",
    "updatePortForwardingRule",
    "createStorageNetworkIpRange",
    "createLoadBalancer",
    "cancelStorageMaintenance",
    "deployVirtualMachine",
    "revokeSecurityGroupEgress",
    "createNetworkACLList",
    "deleteCondition",
    "createPortForwardingRule",
    "createVPCOffering",
    "createEgressFirewallRule",
    "destroyRouter",
    "assignToGlobalLoadBalancerRule",
    "updateTrafficType",
    "addSrxFirewall",
    "addNiciraNvpDevice",
    "updateNetworkACLItem",
    "addIpToNic",
    "deleteNetworkACLList",
    "configureInternalLoadBalancerElement",
    "releaseHostReservation",
    "assignCertToLoadBalancer",
    "deleteVpnGateway",
    "expungeVirtualMachine",
    "createAutoScaleVmGroup",
    "rebootRouter",
    "deleteNetworkServiceProvider",
    "createLBHealthCheckPolicy",
    "deleteIso",
    "createVpnCustomerGateway",
    "deleteAutoScalePolicy",
    "deleteSrxFirewall",
    "detachVolume",
    "deleteNetworkACL",
    "deleteVPC",
    "createPhysicalNetwork",
    "updateLoadBalancerRule",
    "deleteTemplate",
    "deleteVpnCustomerGateway",
    "createVirtualRouterElement",
    "addBigSwitchVnsDevice",
    "releaseDedicatedPod",
    "updateAutoScalePolicy",
    "dedicateZone",
    "createVpnGateway",
    "dedicateCluster",
    "deleteCounter",
    "updateStorageNetworkIpRange",
    "deleteBigSwitchVnsDevice",
    "dedicatePod",
    "addF5LoadBalancer",
    "deleteAutoScaleVmGroup",
    "updateGlobalLoadBalancerRule",
    "authorizeSecurityGroupEgress",
    "disableAutoScaleVmGroup",
    "disassociateUcsProfileFromBlade",
    "prepareHostForMaintenance",
    "deletePrivateGateway",
    "stopInternalLoadBalancerVM",
    "deleteTrafficType",
    "deleteLoadBalancerRule",
    "attachIso",
    "deletePortForwardingRule",
    "removeCertFromLoadBalancer",
    "configureSrxFirewall",
    "updateProjectInvitation",
    "createTags",
    "enableAutoScaleVmGroup",
    "scaleVirtualMachine",
    "removeVpnUser",
    "updateVpnCustomerGateway",
    "stopSystemVm",
    "restartNetwork",
    "rebootVirtualMachine",
    "enableCiscoNexusVSM",
    "updateVMAffinityGroup",
    "configurePaloAltoFirewall",
    "deleteVpnConnection",
    "startSystemVm",
    "deleteF5LoadBalancer",
    "updateProject",
    "deleteNetwork",
    "deleteNetscalerLoadBalancer",
    "addTrafficType",
    "disableUser",
    "configureVirtualRouterElement",
    "deleteProjectInvitation",
    "migrateSystemVm",
    "removeNicFromVirtualMachine",
    "revokeSecurityGroupIngress",
    "updateDefaultNicForVirtualMachine",
    "disableStaticNat",
    "createNetworkACL",
    "createVPC",
    "addBaremetalPxeKickStartServer",
    "addResourceDetail",
    "disassociateIpAddress",
    "createVolume",
    "resetPasswordForVirtualMachine",
    "assignToLoadBalancerRule",
    "startRouter",
    "extractIso",
    "removeResourceDetail",
    "deleteRemoteAccessVpn",
    "resetVpnConnection",
    "extractTemplate",
    "createRemoteAccessVpn",
    "startVirtualMachine",
    "detachIso",
    "deleteAccount",
    "associateIpAddress",
    "disableAccount",
    "migrateVirtualMachine",
    "removeFromLoadBalancerRule",
    "addVpnUser",
    "createPrivateGateway",
    "deleteLBStickinessPolicy",
    "disableCiscoNexusVSM",
    "deleteVMSnapshot",
    "deleteAutoScaleVmProfile",
    "deleteSnapshot",
    "createProject",
    "createLoadBalancerRule",
    "createAutoScalePolicy",
    "restoreVirtualMachine",
    "deleteAffinityGroup",
    "copyIso",
    "uploadVolume",
    "createLBStickinessPolicy",
    "stopVirtualMachine",
    "migrateVirtualMachineWithVolume",
    "createCounter",
    "createSnapshot",
    "destroyVirtualMachine",
    "updateNetwork",
    "dedicateHost",
    "createFirewallRule",
    "instantiateUcsTemplateAndAssocaciateToBlade",
    "addNetworkServiceProvider",
    "rebootSystemVm",
    "revertToVMSnapshot",
    "markDefaultZoneForAccount",
    "restartVPC",
    "replaceNetworkACLList",
    "generateAlert",
    "scaleSystemVm",
    "updateAutoScaleVmGroup",
    "deletePhysicalNetwork",
    "addBaremetalDhcp",
    "deleteVPCOffering",
    "updateNetworkServiceProvider",
    "revertSnapshot"
  ],
  "release": {
    "publiciprange": {
      "name": "releasePublicIpRange",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listVlanIpRanges",
            "dedicatePublicIpRange"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the id of the Public IP range"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Releases a Public IP range back to the system pool"
    },
    "hostreservation": {
      "name": "releaseHostReservation",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listExternalLoadBalancers",
            "addHost",
            "updateHost",
            "listHosts",
            "prepareHostForMaintenance"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the host ID"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Releases host reservation."
    },
    "dedicatedcluster": {
      "name": "releaseDedicatedCluster",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "clusterid",
          "required": True,
          "related": [
            "updateCluster"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Cluster"
        }
      ],
      "requiredparams": [
        "clusterid"
      ],
      "description": "Release the dedication for cluster"
    },
    "dedicatedzone": {
      "name": "releaseDedicatedZone",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "zoneid",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Zone"
        }
      ],
      "requiredparams": [
        "zoneid"
      ],
      "description": "Release dedication of zone"
    },
    "dedicatedhost": {
      "name": "releaseDedicatedHost",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "hostid",
          "required": True,
          "related": [
            "listExternalLoadBalancers",
            "addBaremetalHost",
            "addHost",
            "updateHost",
            "listHosts",
            "prepareHostForMaintenance"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the host"
        }
      ],
      "requiredparams": [
        "hostid"
      ],
      "description": "Release the dedication for host"
    },
    "dedicatedpod": {
      "name": "releaseDedicatedPod",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "podid",
          "required": True,
          "related": [
            "createPod",
            "updatePod"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Pod"
        }
      ],
      "requiredparams": [
        "podid"
      ],
      "description": "Release the dedication for the pod"
    },
    "dedicatedguestvlanrange": {
      "name": "releaseDedicatedGuestVlanRange",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listDedicatedGuestVlanRanges",
            "dedicateGuestVlanRange"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the dedicated guest vlan range"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Releases a dedicated guest vlan range to the system"
    }
  },
  "clean": {
    "vmreservations": {
      "name": "cleanVMReservations",
      "related": [],
      "isasync": True,
      "params": [],
      "requiredparams": [],
      "description": "Cleanups VM reservations in the database."
    }
  },
  "assign": {
    "virtualmachine": {
      "name": "assignVirtualMachine",
      "related": [
        "migrateVirtualMachineWithVolume",
        "stopVirtualMachine",
        "updateVirtualMachine",
        "revertToVMSnapshot",
        "listVirtualMachines",
        "destroyVirtualMachine",
        "restoreVirtualMachine"
      ],
      "isasync": False,
      "params": [
        {
          "name": "virtualmachineid",
          "required": True,
          "related": [
            "migrateVirtualMachineWithVolume",
            "stopVirtualMachine",
            "updateVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of the VM to be moved"
        },
        {
          "name": "networkids",
          "required": False,
          "related": [
            "updateNetwork",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "list",
          "description": "list of new network ids in which the moved VM will participate. In case no network ids are provided the VM will be part of the default network for that zone. In case there is no network yet created for the new account the default network will be created."
        },
        {
          "name": "account",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "account name of the new VM owner."
        },
        {
          "name": "domainid",
          "required": True,
          "related": [
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "domain id of the new VM owner."
        },
        {
          "name": "securitygroupids",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "list of security group ids to be applied on the virtual machine. In case no security groups are provided the VM is part of the default security group."
        }
      ],
      "requiredparams": [
        "virtualmachineid",
        "account",
        "domainid"
      ],
      "description": "Change ownership of a VM from one account to another. This API is available for Basic zones with security groups and Advanced zones with guest networks. A root administrator can reassign a VM from any account to any other account in any domain. A domain administrator can reassign a VM to any account in the same domain."
    },
    "certtoloadbalancer": {
      "name": "assignCertToLoadBalancer",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "lbruleid",
          "required": True,
          "related": [
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the load balancer rule"
        },
        {
          "name": "certid",
          "required": True,
          "related": [
            "listSslCerts"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the certificate"
        }
      ],
      "requiredparams": [
        "lbruleid",
        "certid"
      ],
      "description": "Assigns a certificate to a Load Balancer Rule"
    },
    "togloballoadbalancerrule": {
      "name": "assignToGlobalLoadBalancerRule",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "gslblbruleweightsmap",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "Map of LB rule id's and corresponding weights (between 1-100) in the GSLB rule, if not specified weight of a LB rule is defaulted to 1. Specified as 'gslblbruleweightsmap[0].loadbalancerid=UUID&gslblbruleweightsmap[0].weight=10'"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "updateGlobalLoadBalancerRule",
            "listGlobalLoadBalancerRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the global load balancer rule"
        },
        {
          "name": "loadbalancerrulelist",
          "required": True,
          "related": [
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "list",
          "description": "the list load balancer rules that will be assigned to gloabal load balacner rule"
        }
      ],
      "requiredparams": [
        "id",
        "loadbalancerrulelist"
      ],
      "description": "Assign load balancer rule or list of load balancer rules to a global load balancer rules."
    },
    "toloadbalancerrule": {
      "name": "assignToLoadBalancerRule",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "virtualmachineids",
          "required": True,
          "related": [
            "detachIso",
            "migrateVirtualMachineWithVolume",
            "startVirtualMachine",
            "migrateVirtualMachine",
            "stopVirtualMachine",
            "updateVirtualMachine",
            "changeServiceForVirtualMachine",
            "revertToVMSnapshot",
            "listVirtualMachines",
            "assignVirtualMachine",
            "destroyVirtualMachine",
            "restoreVirtualMachine"
          ],
          "length": 255,
          "type": "list",
          "description": "the list of IDs of the virtual machine that are being assigned to the load balancer rule(i.e. virtualMachineIds=1,2,3)"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the load balancer rule"
        }
      ],
      "requiredparams": [
        "virtualmachineids",
        "id"
      ],
      "description": "Assigns virtual machine or a list of virtual machines to a load balancer rule."
    }
  },
  "delete": {
    "loadbalancerrule": {
      "name": "deleteLoadBalancerRule",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the load balancer rule"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a load balancer rule."
    },
    "domain": {
      "name": "deleteDomain",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "ID of domain to delete"
        },
        {
          "name": "cleanup",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "True if all domain resources (child domains, accounts) have to be cleaned up, False otherwise"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a specified domain"
    },
    "projectinvitation": {
      "name": "deleteProjectInvitation",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "id of the invitation"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Accepts or declines project invitation"
    },
    "ciscoasa1000vresource": {
      "name": "deleteCiscoAsa1000vResource",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "resourceid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "Cisco ASA 1000v resource ID"
        }
      ],
      "requiredparams": [
        "resourceid"
      ],
      "description": "Deletes a Cisco ASA 1000v appliance"
    },
    "vpc": {
      "name": "deleteVPC",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "createVPC",
            "listVPCs",
            "restartVPC"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the VPC"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a VPC"
    },
    "ciscovnmcresource": {
      "name": "deleteCiscoVnmcResource",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "resourceid",
          "required": True,
          "related": [
            "addCiscoVnmcResource"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Cisco Vnmc resource ID"
        }
      ],
      "requiredparams": [
        "resourceid"
      ],
      "description": "Deletes a Cisco Vnmc controller"
    },
    "externalloadbalancer": {
      "name": "deleteExternalLoadBalancer",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listExternalLoadBalancers",
            "addBaremetalHost",
            "addHost",
            "cancelHostMaintenance",
            "updateHost",
            "listHosts",
            "prepareHostForMaintenance"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Id of the external loadbalancer appliance."
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a F5 external load balancer appliance added in a zone."
    },
    "securitygroup": {
      "name": "deleteSecurityGroup",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the account of the security group. Must be specified with domain ID"
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the domain ID of account owning the security group"
        },
        {
          "name": "id",
          "required": False,
          "related": [
            "listSecurityGroups"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the security group. Mutually exclusive with name parameter"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the project of the security group"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The ID of the security group. Mutually exclusive with id parameter"
        }
      ],
      "requiredparams": [],
      "description": "Deletes security group"
    },
    "portforwardingrule": {
      "name": "deletePortForwardingRule",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the port forwarding rule"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a port forwarding rule"
    },
    "cluster": {
      "name": "deleteCluster",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the cluster ID"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a cluster."
    },
    "accountfromproject": {
      "name": "deleteAccountFromProject",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "projectid",
          "required": True,
          "related": [
            "createProject",
            "activateProject",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of the project to remove the account from"
        },
        {
          "name": "account",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "name of the account to be removed from the project"
        }
      ],
      "requiredparams": [
        "projectid",
        "account"
      ],
      "description": "Deletes account from the project"
    },
    "networkdevice": {
      "name": "deleteNetworkDevice",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listExternalLoadBalancers",
            "addHost",
            "updateHost",
            "listHosts",
            "prepareHostForMaintenance"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Id of network device to delete"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes network device."
    },
    "host": {
      "name": "deleteHost",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the host ID"
        },
        {
          "name": "forced",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "Force delete the host. All HA enabled vms running on the host will be put to HA; HA disabled ones will be stopped"
        },
        {
          "name": "forcedestroylocalstorage",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "Force destroy local storage on this host. All VMs created on this local storage will be destroyed"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a host."
    },
    "firewallrule": {
      "name": "deleteFirewallRule",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "updatePortForwardingRule",
            "createIpForwardingRule",
            "listPortForwardingRules",
            "createPortForwardingRule",
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the firewall rule"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a firewall rule"
    },
    "pod": {
      "name": "deletePod",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "createPod",
            "updatePod",
            "listPods"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Pod"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a Pod."
    },
    "ipforwardingrule": {
      "name": "deleteIpForwardingRule",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "updatePortForwardingRule",
            "createIpForwardingRule",
            "listPortForwardingRules",
            "createPortForwardingRule",
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the id of the forwarding rule"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes an ip forwarding rule"
    },
    "secondarystagingstore": {
      "name": "deleteSecondaryStagingStore",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listSwifts",
            "addImageStore",
            "createSecondaryStagingStore",
            "listSecondaryStagingStores",
            "addS3"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the staging store ID"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a secondary staging store ."
    },
    "diskoffering": {
      "name": "deleteDiskOffering",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "createDiskOffering"
          ],
          "length": 255,
          "type": "uuid",
          "description": "ID of the disk offering"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Updates a disk offering."
    },
    "snapshotpolicies": {
      "name": "deleteSnapshotPolicies",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": False,
          "related": [
            "createSnapshotPolicy"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the Id of the snapshot policy"
        },
        {
          "name": "ids",
          "required": False,
          "related": [
            "createSnapshotPolicy"
          ],
          "length": 255,
          "type": "list",
          "description": "list of snapshots policy IDs separated by comma"
        }
      ],
      "requiredparams": [],
      "description": "Deletes snapshot policies for the account."
    },
    "vpcoffering": {
      "name": "deleteVPCOffering",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the VPC offering"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes VPC offering"
    },
    "network": {
      "name": "deleteNetwork",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listSrxFirewallNetworks",
            "updateNetwork",
            "listNetscalerLoadBalancerNetworks"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the network"
        },
        {
          "name": "forced",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "Force delete a network. Network will be marked as 'Destroy' even when commands to shutdown and cleanup to the backend fails."
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a network"
    },
    "zone": {
      "name": "deleteZone",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Zone"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a Zone."
    },
    "remoteaccessvpn": {
      "name": "deleteRemoteAccessVpn",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "publicipid",
          "required": True,
          "related": [
            "associateIpAddress"
          ],
          "length": 255,
          "type": "uuid",
          "description": "public ip address id of the vpn server"
        }
      ],
      "requiredparams": [
        "publicipid"
      ],
      "description": "Destroys a l2tp/ipsec remote access vpn"
    },
    "bigswitchvnsdevice": {
      "name": "deleteBigSwitchVnsDevice",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "vnsdeviceid",
          "required": True,
          "related": [
            "listBigSwitchVnsDevices"
          ],
          "length": 255,
          "type": "uuid",
          "description": "BigSwitch device ID"
        }
      ],
      "requiredparams": [
        "vnsdeviceid"
      ],
      "description": " delete a bigswitch vns device"
    },
    "alerts": {
      "name": "deleteAlerts",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "startdate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "date",
          "description": "start date range to delete alerts (including) this date (use format \"yyyy-MM-dd\" or the new format \"yyyy-MM-ddThh:mm:ss\")"
        },
        {
          "name": "ids",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "the IDs of the alerts"
        },
        {
          "name": "enddate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "date",
          "description": "end date range to delete alerts (including) this date (use format \"yyyy-MM-dd\" or the new format \"yyyy-MM-ddThh:mm:ss\")"
        },
        {
          "name": "type",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "delete by alert type"
        }
      ],
      "requiredparams": [],
      "description": "Delete one or more alerts."
    },
    "autoscalepolicy": {
      "name": "deleteAutoScalePolicy",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "updateAutoScalePolicy",
            "createAutoScalePolicy"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the autoscale policy"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a autoscale policy."
    },
    "ucsmanager": {
      "name": "deleteUcsManager",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "ucsmanagerid",
          "required": True,
          "related": [
            "addUcsManager"
          ],
          "length": 255,
          "type": "uuid",
          "description": "ucs manager id"
        }
      ],
      "requiredparams": [
        "ucsmanagerid"
      ],
      "description": "Delete a Ucs manager"
    },
    "globalloadbalancerrule": {
      "name": "deleteGlobalLoadBalancerRule",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "updateGlobalLoadBalancerRule",
            "listGlobalLoadBalancerRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the global load balancer rule"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a global load balancer rule."
    },
    "niciranvpdevice": {
      "name": "deleteNiciraNvpDevice",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "nvpdeviceid",
          "required": True,
          "related": [
            "addNiciraNvpDevice",
            "listNiciraNvpDevices"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Nicira device ID"
        }
      ],
      "requiredparams": [
        "nvpdeviceid"
      ],
      "description": " delete a nicira nvp device"
    },
    "serviceoffering": {
      "name": "deleteServiceOffering",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listServiceOfferings"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the service offering"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a service offering."
    },
    "template": {
      "name": "deleteTemplate",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of zone of the template"
        },
        {
          "name": "id",
          "required": True,
          "related": [
            "registerIso",
            "prepareTemplate",
            "listIsos",
            "copyIso",
            "registerTemplate",
            "updateIso",
            "updateTemplate",
            "listTemplates"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the template"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a template from the system. All virtual machines using the deleted template will not be affected."
    },
    "vpngateway": {
      "name": "deleteVpnGateway",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "createVpnGateway"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of customer gateway"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Delete site to site vpn gateway"
    },
    "snapshot": {
      "name": "deleteSnapshot",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "createSnapshot",
            "revertSnapshot"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the snapshot"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a snapshot of a disk volume."
    },
    "networkacllist": {
      "name": "deleteNetworkACLList",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the network ACL"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a Network ACL"
    },
    "events": {
      "name": "deleteEvents",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "startdate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "date",
          "description": "start date range to delete events (including) this date (use format \"yyyy-MM-dd\" or the new format \"yyyy-MM-ddThh:mm:ss\")"
        },
        {
          "name": "type",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "delete by event type"
        },
        {
          "name": "enddate",
          "required": False,
          "related": [],
          "length": 255,
          "type": "date",
          "description": "end date range to delete events (including) this date (use format \"yyyy-MM-dd\" or the new format \"yyyy-MM-ddThh:mm:ss\")"
        },
        {
          "name": "ids",
          "required": False,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "the IDs of the events"
        }
      ],
      "requiredparams": [],
      "description": "Delete one or more events."
    },
    "autoscalevmgroup": {
      "name": "deleteAutoScaleVmGroup",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "enableAutoScaleVmGroup",
            "updateAutoScaleVmGroup",
            "disableAutoScaleVmGroup"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the autoscale group"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a autoscale vm group."
    },
    "srxfirewall": {
      "name": "deleteSrxFirewall",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "fwdeviceid",
          "required": True,
          "related": [
            "listSrxFirewalls",
            "configureSrxFirewall"
          ],
          "length": 255,
          "type": "uuid",
          "description": "srx firewall device ID"
        }
      ],
      "requiredparams": [
        "fwdeviceid"
      ],
      "description": " delete a SRX firewall device"
    },
    "trafficmonitor": {
      "name": "deleteTrafficMonitor",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listExternalLoadBalancers",
            "listHosts",
            "prepareHostForMaintenance"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Id of the Traffic Monitor Host."
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes an traffic monitor host."
    },
    "sslcert": {
      "name": "deleteSslCert",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listSslCerts"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Id of SSL certificate"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Delete a certificate to cloudstack"
    },
    "networkacl": {
      "name": "deleteNetworkACL",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "createNetworkACL"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the network ACL"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a Network ACL"
    },
    "storagepool": {
      "name": "deleteStoragePool",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "findStoragePoolsForMigration"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Storage pool id"
        },
        {
          "name": "forced",
          "required": False,
          "related": [],
          "length": 255,
          "type": "boolean",
          "description": "Force destroy storage pool (force expunge volumes in Destroyed state as a part of pool removal)"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a storage pool."
    },
    "ldapconfiguration": {
      "name": "deleteLdapConfiguration",
      "related": [
        "addLdapConfiguration"
      ],
      "isasync": False,
      "params": [
        {
          "name": "hostname",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Hostname"
        }
      ],
      "requiredparams": [
        "hostname"
      ],
      "description": "Remove an Ldap Configuration"
    },
    "tags": {
      "name": "deleteTags",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "resourcetype",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Delete tag by resource type"
        },
        {
          "name": "resourceids",
          "required": True,
          "related": [],
          "length": 255,
          "type": "list",
          "description": "Delete tags for resource id(s)"
        },
        {
          "name": "tags",
          "required": False,
          "related": [],
          "length": 255,
          "type": "map",
          "description": "Delete tags matching key/value pairs"
        }
      ],
      "requiredparams": [
        "resourcetype",
        "resourceids"
      ],
      "description": "Deleting resource tag(s)"
    },
    "netscalerloadbalancer": {
      "name": "deleteNetscalerLoadBalancer",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "lbdeviceid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "netscaler load balancer device ID"
        }
      ],
      "requiredparams": [
        "lbdeviceid"
      ],
      "description": " delete a netscaler load balancer device"
    },
    "lbstickinesspolicy": {
      "name": "deleteLBStickinessPolicy",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "createLBStickinessPolicy"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the LB stickiness policy"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a LB stickiness policy."
    },
    "staticroute": {
      "name": "deleteStaticRoute",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listStaticRoutes",
            "createStaticRoute"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the static route"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a static route"
    },
    "traffictype": {
      "name": "deleteTrafficType",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "addTrafficType"
          ],
          "length": 255,
          "type": "uuid",
          "description": "traffic type id"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes traffic type of a physical network"
    },
    "externalfirewall": {
      "name": "deleteExternalFirewall",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listHosts"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Id of the external firewall appliance."
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes an external firewall appliance."
    },
    "user": {
      "name": "deleteUser",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "disableUser",
            "getUser",
            "lockUser",
            "listUsers",
            "updateUser"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of the user to be deleted"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a user for an account"
    },
    "portableiprange": {
      "name": "deletePortableIpRange",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listPortableIpRanges"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Id of the portable ip range"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "deletes a range of portable public IP's associated with a region"
    },
    "storagenetworkiprange": {
      "name": "deleteStorageNetworkIpRange",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "createStorageNetworkIpRange",
            "listStorageNetworkIpRange",
            "updateStorageNetworkIpRange"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the uuid of the storage network ip range"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a storage network IP Range."
    },
    "vmsnapshot": {
      "name": "deleteVMSnapshot",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "vmsnapshotid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the VM snapshot"
        }
      ],
      "requiredparams": [
        "vmsnapshotid"
      ],
      "description": "Deletes a vmsnapshot."
    },
    "condition": {
      "name": "deleteCondition",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listConditions"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the condition."
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Removes a condition"
    },
    "autoscalevmprofile": {
      "name": "deleteAutoScaleVmProfile",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listAutoScaleVmProfiles"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the autoscale profile"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a autoscale vm profile."
    },
    "affinitygroup": {
      "name": "deleteAffinityGroup",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "domainid",
          "required": False,
          "related": [
            "listDomainChildren"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the domain ID of account owning the affinity group"
        },
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the account of the affinity group. Must be specified with domain ID"
        },
        {
          "name": "name",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "The name of the affinity group. Mutually exclusive with id parameter"
        },
        {
          "name": "id",
          "required": False,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the affinity group. Mutually exclusive with name parameter"
        }
      ],
      "requiredparams": [],
      "description": "Deletes affinity group"
    },
    "volume": {
      "name": "deleteVolume",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "uploadVolume",
            "createVolume"
          ],
          "length": 255,
          "type": "uuid",
          "description": "The ID of the disk volume"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a detached disk volume."
    },
    "account": {
      "name": "deleteAccount",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listAccounts",
            "markDefaultZoneForAccount",
            "disableAccount"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Account id"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a account, and all users associated with this account"
    },
    "cisconexusvsm": {
      "name": "deleteCiscoNexusVSM",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "enableCiscoNexusVSM",
            "disableCiscoNexusVSM",
            "listCiscoNexusVSMs"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Id of the Cisco Nexus 1000v VSM device to be deleted"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": " delete a Cisco Nexus VSM device"
    },
    "paloaltofirewall": {
      "name": "deletePaloAltoFirewall",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "fwdeviceid",
          "required": True,
          "related": [
            "configurePaloAltoFirewall",
            "listPaloAltoFirewalls",
            "addPaloAltoFirewall"
          ],
          "length": 255,
          "type": "uuid",
          "description": "Palo Alto firewall device ID"
        }
      ],
      "requiredparams": [
        "fwdeviceid"
      ],
      "description": " delete a Palo Alto firewall device"
    },
    "networkoffering": {
      "name": "deleteNetworkOffering",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "createNetworkOffering",
            "updateNetworkOffering"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the network offering"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a network offering."
    },
    "vpncustomergateway": {
      "name": "deleteVpnCustomerGateway",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "updateVpnCustomerGateway",
            "listVpnCustomerGateways"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of customer gateway"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Delete site to site vpn customer gateway"
    },
    "privategateway": {
      "name": "deletePrivateGateway",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "createPrivateGateway"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the private gateway"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a Private gateway"
    },
    "counter": {
      "name": "deleteCounter",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "createCounter"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the counter"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a counter"
    },
    "lbhealthcheckpolicy": {
      "name": "deleteLBHealthCheckPolicy",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listLBHealthCheckPolicies",
            "createLBHealthCheckPolicy"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the load balancer HealthCheck policy"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a load balancer HealthCheck policy."
    },
    "vpnconnection": {
      "name": "deleteVpnConnection",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "resetVpnConnection",
            "listVpnConnections"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of vpn connection"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Delete site to site vpn connection"
    },
    "project": {
      "name": "deleteProject",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "createProject",
            "activateProject",
            "listProjectAccounts",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "id of the project to be deleted"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a project"
    },
    "vlaniprange": {
      "name": "deleteVlanIpRange",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listVlanIpRanges",
            "dedicatePublicIpRange"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the id of the VLAN IP range"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Creates a VLAN IP range."
    },
    "f5loadbalancer": {
      "name": "deleteF5LoadBalancer",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "lbdeviceid",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "netscaler load balancer device ID"
        }
      ],
      "requiredparams": [
        "lbdeviceid"
      ],
      "description": " delete a F5 load balancer device"
    },
    "iso": {
      "name": "deleteIso",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "registerIso",
            "prepareTemplate",
            "listIsos",
            "copyIso",
            "registerTemplate",
            "updateIso",
            "updateTemplate",
            "listTemplates"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the ISO file"
        },
        {
          "name": "zoneid",
          "required": False,
          "related": [
            "listZones",
            "createZone",
            "updateZone"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the zone of the ISO file. If not specified, the ISO will be deleted from all the zones"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes an ISO file."
    },
    "instancegroup": {
      "name": "deleteInstanceGroup",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the instance group"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a vm group"
    },
    "imagestore": {
      "name": "deleteImageStore",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the image store ID"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes an image store ."
    },
    "egressfirewallrule": {
      "name": "deleteEgressFirewallRule",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "updatePortForwardingRule",
            "createIpForwardingRule",
            "listPortForwardingRules",
            "createPortForwardingRule",
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the firewall rule"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes an ggress firewall rule"
    },
    "networkserviceprovider": {
      "name": "deleteNetworkServiceProvider",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "listTrafficTypes",
            "updateNetworkServiceProvider",
            "addNetworkServiceProvider"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the network service provider"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a Network Service Provider."
    },
    "physicalnetwork": {
      "name": "deletePhysicalNetwork",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Physical network"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a Physical Network."
    },
    "sshkeypair": {
      "name": "deleteSSHKeyPair",
      "related": [],
      "isasync": False,
      "params": [
        {
          "name": "account",
          "required": False,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "the account associated with the keypair. Must be used with the domainId parameter."
        },
        {
          "name": "domainid",
          "required": False,
          "related": [
            "updateDomain",
            "listDomainChildren",
            "createDomain",
            "listDomains"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the domain ID associated with the keypair"
        },
        {
          "name": "projectid",
          "required": False,
          "related": [
            "createProject",
            "updateProject"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the project associated with keypair"
        },
        {
          "name": "name",
          "required": True,
          "related": [],
          "length": 255,
          "type": "string",
          "description": "Name of the keypair"
        }
      ],
      "requiredparams": [
        "name"
      ],
      "description": "Deletes a keypair by name"
    },
    "loadbalancer": {
      "name": "deleteLoadBalancer",
      "related": [],
      "isasync": True,
      "params": [
        {
          "name": "id",
          "required": True,
          "related": [
            "updatePortForwardingRule",
            "createIpForwardingRule",
            "listPortForwardingRules",
            "createPortForwardingRule",
            "listIpForwardingRules"
          ],
          "length": 255,
          "type": "uuid",
          "description": "the ID of the Load Balancer"
        }
      ],
      "requiredparams": [
        "id"
      ],
      "description": "Deletes a load balancer"
    }
  }
}
